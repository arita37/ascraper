 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AutoGen Agents ](https://www.reddit.com/r/AutoGenAI/comments/1byew5i/github_upsonictiger_neuralink_for_your_autogen/) , 2024-04-08-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the LangChain library, we have published it completely openly under the MIT licens
e.

What it does: Just like human developers, it has some abilities such as running the codes it writes, making mouse an
d keyboard movements, writing and running Python functions for functions it does not have. AI literally thinks and the i
nterface we provide transforms with real computer actions.

Those who want to contribute can provide support under the M
IT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/Langchaindev/comments/1byep8n/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-08-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the LangChain library, we have published it completely openly under the MIT licens
e.

What it does: Just like human developers, it has some abilities such as running the codes it writes, making mouse an
d keyboard movements, writing and running Python functions for functions it does not have. AI literally thinks and the i
nterface we provide transforms with real computer actions.

As Upsonic, we are currently working on improving the Neural
ink for AI Agents definition and responding to community support.

Those who want to contribute can provide support unde
r the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ I just make Neuralink for agents (LangChain, AutoGen) ](https://www.reddit.com/r/AI_Agents/comments/1byeexs/i_just_make_neuralink_for_agents_langchain_autogen/) , 2024-04-08-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

&#x200B;

Hello, we are developing a superstructure that provides an AI-C
omputer interface for AI agents created through the LangChain library, we have published it completely openly under the 
MIT license.

&#x200B;

What it does: Just like human developers, it has some abilities such as running the codes it wri
tes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. AI litera
lly thinks and the interface we provide transforms with real computer actions.

&#x200B;

&#x200B;

As Upsonic, we are c
urrently working on improving the Neuralink for AI Agents definition and responding to community support.

&#x200B;

&#x
200B;

Those who want to contribute can provide support under the MIT license and code conduct. [https://github.com/Upso
nic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ Storing tool retrieved data in conversation history ](https://www.reddit.com/r/LangChain/comments/1byd0e8/storing_tool_retrieved_data_in_conversation/) , 2024-04-08-0910
```
I've been playing around with pulling data from APIs, feeding that into the language model's chat and then conversing ov
er that context.  One recent use case I've been considering is allowing the agent to do multiple tasks, so the API calls
 are determined by the AI solution rather than being hard coded.

The obvious solution to me is to use a conversational 
chat agent that can react and use tools that make the API calls.  The problem I'm experiencing though is that the return
ed content from the API call function doesn't appear to get stored in my ConversationBufferMemory.  It only stores the h
uman inputs, and the AI's outputs, but not the 'Observation' that contains the returned full context.

The reason I'd li
ke this in the history is to prevent the need for additional API calls when the user begins to ask follow-up questions a
bout the data which has already been retrieved by a tool.  It seems very inefficient to pull the same data every time th
ey have a follow-up question, which is what it's currently doing.  Below is an example of what I'm doing.

    template 
= 'First, evaluate the context provided by preceding messages to inform your response. Only if you can't answer the ques
tions from that should you use available tools.'
    
    memory = ConversationBufferMemory(
            memory_key='cha
t_history',
            return_messages=True
        )
    
    tools = [get_ticket_info]
    
    agent = initialize_ag
ent(
        tools=tools,
        llm=llm,
        agent='chat-conversational-react-description',
        memory=memory,

        verbose=True,
        agent_kwargs={'prefix': template}
    )

I've also tried using the create\_react\_agent()
 function to create the agent which I know is the new way to do this, but it doesn't appear to be conversational as it w
ill not remember any message history.  This is why I'm using the initialize\_agent() function instead.  At this point I'
m tempted to go away with LangChain and use OpenAI's API directly where I would have more control over what goes into th
e message history.

Any tricks you're aware of, or am I approaching this in a naive way?  Appreciate any wisdom you can 
bestow.

  
Edit: I got this to work easily enough using OpenAI directly.  See my response below to one of my replies if
 interested.
```
---

     
 
all -  [ a model that can handle about 50k inputs and less than or equal to 7B parameters(not fully necessary ](https://www.reddit.com/r/huggingface/comments/1bybrzw/a_model_that_can_handle_about_50k_inputs_and_less/) , 2024-04-08-0910
```
I am looking for a model that can handle about 50k inputs and less than or equal to 7B parameters(not fully necessary) a
nd summarize the text.

I was using Mistral-7B before but it has limit of 32k inputs so I need an alternative 

PS I'm u
sing HuggingFaceHub to get the LLM from LangChain so I can't download model > 10gb
```
---

     
 
all -  [ Working with diverse data to create 30 to 35 pages document and Managing the retrieval. ](https://www.reddit.com/r/LangChain/comments/1by9iqn/working_with_diverse_data_to_create_30_to_35/) , 2024-04-08-0910
```
I have been working on the large data. The data consist of talks from the different anchor persons, also there are comme
nts in numerical representation like for example '*how many people agreed and how many are disagreed'.* and on which ses
sion they are disscusing the point of agenda and on which bill number they place a talk.   
  
So my question is: I want
 to generate the document a large document which contains multiple sections almost 20 sections. Each section has diverse
 and different instructions so how do I manage my vectordb calls. ? because each section of the document is different so
 how to make a calls to retreival automatically based on the sections conditions. ?
```
---

     
 
all -  [ How to make a RAG conscious of the documents it have? Amazon Bedrock ](https://www.reddit.com/r/LangChain/comments/1by8u01/how_to_make_a_rag_conscious_of_the_documents_it/) , 2024-04-08-0910
```
I'm currently working with AWS Bedrock and Langchain while it retrieves good answers when I want to ask it stuff like co
mparing documents or listing the documents on its data sources Its unable to do it. It seems like its not conscious of i
ts environment. Does anyone has some experience working with this? Like I want it to be a typical RAG application based 
on some documents but I want it to be conscious of the data it have like comparing versions of the same documents...
```
---

     
 
all -  [ Challenges of Scaling RAG applications ](https://www.reddit.com/r/LangChain/comments/1by7s2m/challenges_of_scaling_rag_applications/) , 2024-04-08-0910
```
I'm thinking about writing a detailed blog on the Challenges you face while scaling your RAG apps. Please comment some s
uggestions you would like me to discuss in the blog.  
```
---

     
 
all -  [ New documentation is still bad ](https://www.reddit.com/r/LangChain/comments/1by72bo/new_documentation_is_still_bad/) , 2024-04-08-0910
```
I just read their [new blog post](https://blog.langchain.dev/langchain-documentation-refresh/), about the new documentat
ion website. It's very curious and funny.

It goes through the Diataxis taxonomy for documentation, which I find useful 
and aligns with how my brain works.

Just to throw everything out of the window and say: we mixed and matched every sect
ion of Diataxis and you can find tutorials spread all over the place, mixed with reference and explanations!

Take a loo
k at this section of the post:


> This section should contain mostly conceptual Tutorials, References, and Explanations
 of the components they cover.
> 
> Note: As a general rule of thumb, everything covered in the Expression Language and 
Components sections (with the exception of the Composition section of components) should cover only components that exis
t in langchain_core.

Impressive! They need to explain what's where, and even introduce a rule about langchain_core that
 is broken from the get go. And when you go to the socs the components section isn't even in the menu to be selected!

I
 mean, just make it simple:

* Tutorials (quick start, use cases with in depth explanations, etc)
* How to guides (terse
, context free guides such as how to create a chain, new runnable from scratch, new agent from scratch, how to visualize
 a chain, how to pass a system prompt to a model, how to make models spit structured output, etc)
* Explanation (langcha
in purpose, package organization, what is LCEL, what is a chain/agent/runnable/etc, model vs chat model, what is a tool/
toolkit, what is a function call etc). Accept a small amount of repetition from what we have in tutorials.
* Reference (
API docs)

Wouldn't that be simpler? I'm so frustrated with this...


```
---

     
 
all -  [ Quota exceeded error ](https://i.redd.it/5gxw1qi4l2tc1.png) , 2024-04-08-0910
```

```
---

     
 
all -  [ Evaluating RAG on custom Q&As ](https://www.reddit.com/r/LangChain/comments/1by54rq/evaluating_rag_on_custom_qas/) , 2024-04-08-0910
```
We are trying to get our feet wet with RAG with a small engineering team. I want to build a RAG system querying an exten
sive internal documents system. With the available choice of LLMs, embedding models, vector databases, hyperparameters i
t's easy to get overwhelmed. So what I want is to create a test dataset manually with like ten-twenty questions and answ
ers we would like to receive (or multiple answer options for each question??) and automate deployment of several combina
tions of different LLMs, hyperparameters, embedding models, etc and compare the actuals against the gold standard answer
s (using ROUGE score maybe??). Does that make sense? Are there any tools/frameworks I need to be aware of to do somethin
g like that for me? Thanks!
```
---

     
 
all -  [ How to deploy a RAG-tuned AI chatbot/LLM using AWS Bedrock ](https://www.reddit.com/r/MLQuestions/comments/1by1c4j/how_to_deploy_a_ragtuned_ai_chatbotllm_using_aws/) , 2024-04-08-0910
```
Hey guys, so I am building a chatbot which uses a RAG-tuned LLM in AWS Bedrock (and deployed using AWS Lambda endpoints)
.

How do I avoid my LLM from being having to be RAG-tuned every single time a user asks his/her first question? I am th
inking of storing the RAG-tuned LLM in an AWS S3 bucket. If I do this, I believe I will have to store the LLM model para
meters and the vector store index in the S3 bucket. Doing this would mean every single time a user asks his/her first qu
estion (and subsequent questions), I will just be loading the the RAG-tuned LLM from the S3 bucket (rather than having t
o run RAG-tuning every single time when a user asks his/her first question, which will save me RAG-tuning costs and late
ncy).

Would this design work? I have a sample of my script below:

    import os
    import json
    import boto3
    f
rom langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    from langchain.embeddings import BedrockEmbeddings
    from langchain.vectorstores import FAISS
    from langchain.
indexes import VectorstoreIndexCreator
    from langchain.llms.bedrock import Bedrock
    
    def save_to_s3(model_para
ms, vector_store_index, bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Save mode
l parameters to S3
        s3.put_object(Body=model_params, Bucket=bucket_name, Key=model_key)
        
        # Save v
ector store index to S3
        s3.put_object(Body=vector_store_index, Bucket=bucket_name, Key=index_key)
    
    def l
oad_from_s3(bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Load model parameters
 from S3
        model_params = s3.get_object(Bucket=bucket_name, Key=model_key)['Body'].read()
        
        # Load 
vector store index from S3
        vector_store_index = s3.get_object(Bucket=bucket_name, Key=index_key)['Body'].read()

        
        return model_params, vector_store_index
    
    def initialize_hr_system(bucket_name, model_key, index
_key):
        s3 = boto3.client('s3')
        
        try:
            # Check if model parameters and vector store in
dex exist in S3
            s3.head_object(Bucket=bucket_name, Key=model_key)
            s3.head_object(Bucket=bucket_n
ame, Key=index_key)
            
            # Load model parameters and vector store index from S3
            model_pa
rams, vector_store_index = load_from_s3(bucket_name, model_key, index_key)
            
            # Deserialize and re
construct the RAG-tuned LLM and vector store index
            llm = Bedrock.deserialize(json.loads(model_params))
     
       index = VectorstoreIndexCreator.deserialize(json.loads(vector_store_index))
        except s3.exceptions.ClientEr
ror:
            # Model parameters and vector store index don't exist in S3
            # Create them and save to S3
  
          data_load = PyPDFLoader('Glossary_of_Terms.pdf')
            data_split = RecursiveCharacterTextSplitter(separ
ators=['\n\n', '\n', ' ', ''], chunk_size=100, chunk_overlap=10)
            data_embeddings = BedrockEmbeddings(credent
ials_profile_name='default', model_id='amazon.titan-embed-text-v1')
            data_index = VectorstoreIndexCreator(tex
t_splitter=data_split, embedding=data_embeddings, vectorstore_cls=FAISS)
            index = data_index.from_loaders([da
ta_load])
            
            llm = Bedrock(
                credentials_profile_name='default',
                mo
del_id='mistral.mixtral-8x7b-instruct-v0:1',
                model_kwargs={
                    'max_tokens_to_sample': 
3000,
                    'temperature': 0.1,
                    'top_p': 0.9
                }
            )
         
   
            # Serialize model parameters and vector store index
            serialized_model_params = json.dumps(llm
.serialize())
            serialized_vector_store_index = json.dumps(index.serialize())
            
            # Save 
model parameters and vector store index to S3
            save_to_s3(serialized_model_params, serialized_vector_store_in
dex, bucket_name, model_key, index_key)
        
        return index, llm
    
    def hr_rag_response(index, llm, ques
tion):
        hr_rag_query = index.query(question=question, llm=llm)
        return hr_rag_query
    
    # S3 bucket c
onfiguration
    bucket_name = 'your-bucket-name'
    model_key = 'models/chatbot_model.json'
    index_key = 'indexes/c
hatbot_index.json'
    
    # Initialize the system
    index, llm = initialize_hr_system(bucket_name, model_key, index_
key)
    
    # Serve user requests
    while True:
        user_question = input('User: ')
        response = hr_rag_re
sponse(index, llm, user_question)
        print('Chatbot:', response)
```
---

     
 
all -  [ How to deploy a RAG-tuned AI chatbot/LLM using AWS Bedrock ](https://www.reddit.com/r/aws/comments/1by169j/how_to_deploy_a_ragtuned_ai_chatbotllm_using_aws/) , 2024-04-08-0910
```
Hey guys, so I am building a chatbot which uses a RAG-tuned LLM in AWS Bedrock (and deployed using AWS Lambda endpoints)
.

How do I avoid my LLM from being having to be RAG-tuned every single time a user asks his/her first question? I am th
inking of storing the RAG-tuned LLM in an AWS S3 bucket. If I do this, I believe I will have to store the LLM model para
meters and the vector store index in the S3 bucket. Doing this would mean every single time a user asks his/her first qu
estion (and subsequent questions), I will just be loading the the RAG-tuned LLM from the S3 bucket (rather than having t
o run RAG-tuning every single time when a user asks his/her first question, which will save me RAG-tuning costs and late
ncy).   


Would this design work? I have a sample of my script below:  


    import os
    import json
    import boto
3
    from langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextS
plitter
    from langchain.embeddings import BedrockEmbeddings
    from langchain.vectorstores import FAISS
    from lan
gchain.indexes import VectorstoreIndexCreator
    from langchain.llms.bedrock import Bedrock
    
    def save_to_s3(mod
el_params, vector_store_index, bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Sa
ve model parameters to S3
        s3.put_object(Body=model_params, Bucket=bucket_name, Key=model_key)
        
        #
 Save vector store index to S3
        s3.put_object(Body=vector_store_index, Bucket=bucket_name, Key=index_key)
    
  
  def load_from_s3(bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Load model par
ameters from S3
        model_params = s3.get_object(Bucket=bucket_name, Key=model_key)['Body'].read()
        
        
# Load vector store index from S3
        vector_store_index = s3.get_object(Bucket=bucket_name, Key=index_key)['Body'].
read()
        
        return model_params, vector_store_index
    
    def initialize_hr_system(bucket_name, model_key
, index_key):
        s3 = boto3.client('s3')
        
        try:
            # Check if model parameters and vector s
tore index exist in S3
            s3.head_object(Bucket=bucket_name, Key=model_key)
            s3.head_object(Bucket=b
ucket_name, Key=index_key)
            
            # Load model parameters and vector store index from S3
            m
odel_params, vector_store_index = load_from_s3(bucket_name, model_key, index_key)
            
            # Deserialize
 and reconstruct the RAG-tuned LLM and vector store index
            llm = Bedrock.deserialize(json.loads(model_params)
)
            index = VectorstoreIndexCreator.deserialize(json.loads(vector_store_index))
        except s3.exceptions.C
lientError:
            # Model parameters and vector store index don't exist in S3
            # Create them and save t
o S3
            data_load = PyPDFLoader('Glossary_of_Terms.pdf')
            data_split = RecursiveCharacterTextSplitte
r(separators=['\n\n', '\n', ' ', ''], chunk_size=100, chunk_overlap=10)
            data_embeddings = BedrockEmbeddings(
credentials_profile_name='default', model_id='amazon.titan-embed-text-v1')
            data_index = VectorstoreIndexCrea
tor(text_splitter=data_split, embedding=data_embeddings, vectorstore_cls=FAISS)
            index = data_index.from_load
ers([data_load])
            
            llm = Bedrock(
                credentials_profile_name='default',
           
     model_id='mistral.mixtral-8x7b-instruct-v0:1',
                model_kwargs={
                    'max_tokens_to_sa
mple': 3000,
                    'temperature': 0.1,
                    'top_p': 0.9
                }
            )
  
          
            # Serialize model parameters and vector store index
            serialized_model_params = json.du
mps(llm.serialize())
            serialized_vector_store_index = json.dumps(index.serialize())
            
            
# Save model parameters and vector store index to S3
            save_to_s3(serialized_model_params, serialized_vector_s
tore_index, bucket_name, model_key, index_key)
        
        return index, llm
    
    def hr_rag_response(index, ll
m, question):
        hr_rag_query = index.query(question=question, llm=llm)
        return hr_rag_query
    
    # S3 b
ucket configuration
    bucket_name = 'your-bucket-name'
    model_key = 'models/chatbot_model.json'
    index_key = 'in
dexes/chatbot_index.json'
    
    # Initialize the system
    index, llm = initialize_hr_system(bucket_name, model_key,
 index_key)
    
    # Serve user requests
    while True:
        user_question = input('User: ')
        response = hr
_rag_response(index, llm, user_question)
        print('Chatbot:', response)

&#x200B;
```
---

     
 
all -  [ How to preprocess large JSOn response of OpenAI function call in Flowise? ](https://www.reddit.com/r/flowise/comments/1by0p4r/how_to_preprocess_large_json_response_of_openai/) , 2024-04-08-0910
```
https://preview.redd.it/87bj9gc031tc1.png?width=2632&format=png&auto=webp&s=eaffcba5154c7dcbddd4b428fce7021c954752a5

Gr
eetings, I am working with Flowise to build up complex flows with my own APIs which return some data from Notion. Howeve
r, the response from Notion is quite a big JSON which cannot be used to pass to the ChatOpenAI component. I don't know h
ow to intercept some extra steps to process the response from the OpenAPI Chain as in the attachment image. Should I jus
t add another tool like StructedOutputParser,.. to the OpenAI Tool Agent?

One another approach is tuning my API respons
es, but I just wonder if we can utilize the power of Langchain in Flowise on existing APIs or not.

May I ask if anyone 
can share with me some Flowise templates that can work with large responses too?
```
---

     
 
all -  [ RAG returns concocted results  ](https://www.reddit.com/r/LangChain/comments/1bxwxtu/rag_returns_concocted_results/) , 2024-04-08-0910
```
I have one banking related document with several overlapping topics. Say one topic is related to credit card request, an
other related to cheque book request, another relating to account deactivation request. Mind that each of topic in itsel
f are lengthy.

When in the retrieval chain, I ask a question 'how to raise requests', the result is a mixture from all 
of the above topics. First few lines describe credit card procedure and then bridge to checkbook. Which is wrong as each
 process has a different steps.

I'm using chunking strategy of 1000, default sentence transformers embedding, qdrant fo
r as retriever, and gpt3.5 turbo 16k for llm.

Also the llm gives a disclaimer/note at the end saying that steps vary pe
r organisation. Tried several prompts to remove disclaimer but nothing seems to work.

Any help / prompt would be greatl
y appreciated.
```
---

     
 
all -  [ 100 Coupons for FREE Udemy and Coursera Courses with Certificates! ](https://www.reddit.com/r/Udemy/comments/1bxvaix/100_coupons_for_free_udemy_and_coursera_courses/) , 2024-04-08-0910
```
Python And Flask Framework Complete Course For Beginners

[https://courze.org/python-and-flask-framework-complete-course
-for-beginners/](https://courze.org/python-and-flask-framework-complete-course-for-beginners/)

&#x200B;

CSS, Bootstrap
, JavaScript And PHP Stack Complete Course

[https://courze.org/css-bootstrap-javascript-and-php-stack-complete-course/]
(https://courze.org/css-bootstrap-javascript-and-php-stack-complete-course/)

&#x200B;

JavaScript deep : Advanced Techn
iques (Practice Tests Only)

[https://courze.org/javascript-deep-advanced-techniques-practice-tests-only/](https://courz
e.org/javascript-deep-advanced-techniques-practice-tests-only/)

&#x200B;

Assembler Exploits(Practice Tests only) Binar
y Code Breakers

[https://courze.org/assembler-exploitspractice-tests-only-binary-code-breakers/](https://courze.org/ass
embler-exploitspractice-tests-only-binary-code-breakers/)

&#x200B;

PODCAST Crea tu Podcast y llega a miles 2023 Actual
izado

[https://courze.org/podcast-crea-tu-podcast-y-llega-a-miles-2023-actualizado/](https://courze.org/podcast-crea-tu
-podcast-y-llega-a-miles-2023-actualizado/)

&#x200B;

Joint Diploma (Oxford) : Couples /Art Therapy (Accredited)

[http
s://courze.org/joint-diploma-oxford-couples-art-therapy-accredited/](https://courze.org/joint-diploma-oxford-couples-art
-therapy-accredited/)

&#x200B;

Master Android by Building 3 Applications in Kotlin Language

[https://courze.org/maste
r-android-by-building-3-applications-in-kotlin-language/](https://courze.org/master-android-by-building-3-applications-i
n-kotlin-language/)

&#x200B;

Master Android Application Build 3 Applications from Scratch

[https://courze.org/master-
android-application-build-3-applications-from-scratch/](https://courze.org/master-android-application-build-3-applicatio
ns-from-scratch/)

&#x200B;

Crea paginas de ventas para vender productos digi en Hotmart

[https://courze.org/crea-pagi
nas-de-ventas-para-vender-productos-digi-en-hotmart/](https://courze.org/crea-paginas-de-ventas-para-vender-productos-di
gi-en-hotmart/)

&#x200B;

TOEFL Preparation: Reading Mastery

[https://courze.org/toefl-preparation-reading-mastery/](h
ttps://courze.org/toefl-preparation-reading-mastery/)

&#x200B;

30 HTML CSS & JavaScript Projects A Beginner’s Guide to
 JS

[https://courze.org/30-html-css-javascript-projects-a-beginners-guide-to-js/](https://courze.org/30-html-css-javasc
ript-projects-a-beginners-guide-to-js/)

&#x200B;

20 Web Projects build 20 HTML, CSS and JavaScript projects

[https://
courze.org/20-web-projects-build-20-html-css-and-javascript-projects/](https://courze.org/20-web-projects-build-20-html-
css-and-javascript-projects/)

&#x200B;

Android App’s Development Masterclass – Build 2 Apps – Java

[https://courze.or
g/android-apps-development-masterclass-build-2-apps-java/](https://courze.org/android-apps-development-masterclass-build
-2-apps-java/)

&#x200B;

Android Apps Development in Hindi and Build 10 Applications

[https://courze.org/android-apps-
development-in-hindi-and-build-10-applications/](https://courze.org/android-apps-development-in-hindi-and-build-10-appli
cations/)

&#x200B;

Android Very Basic App Development Course with Java in Hindi

[https://courze.org/android-very-basi
c-app-development-course-with-java-in-hindi/](https://courze.org/android-very-basic-app-development-course-with-java-in-
hindi/)

&#x200B;

Practical HTML, CSS, JS: 10 Real-World Projects for Practice

[https://courze.org/practical-html-css-
js-10-real-world-projects-for-practice/](https://courze.org/practical-html-css-js-10-real-world-projects-for-practice/)


&#x200B;

Android Course Build 3 Applications from Scratch with Java

[https://courze.org/android-course-build-3-applic
ations-from-scratch-with-java/](https://courze.org/android-course-build-3-applications-from-scratch-with-java/)

&#x200B
;

Simple React App from Scratch

[https://courze.org/build-a-simple-react-app-from-scratch/](https://courze.org/build-a
-simple-react-app-from-scratch/)

&#x200B;

Pitch Deck Hero: Business Presentation and Communication

[https://courze.or
g/pitch-deck-hero-business-presentation-and-communication/](https://courze.org/pitch-deck-hero-business-presentation-and
-communication/)

&#x200B;

Business Process Optimization with Lean Six Sigma

[https://courze.org/business-process-opti
mization-with-lean-six-sigma/](https://courze.org/business-process-optimization-with-lean-six-sigma/)

&#x200B;

Bloggin
g For Beginners – How to Start a Blog & Make Money

[https://courze.org/blogging-for-beginners-how-to-start-a-blog-make-
money/](https://courze.org/blogging-for-beginners-how-to-start-a-blog-make-money/)

&#x200B;

Writing With Flair: How To
 Become An Exceptional Writer

[https://courze.org/writing-with-flair-how-to-become-an-exceptional-writer/](https://cour
ze.org/writing-with-flair-how-to-become-an-exceptional-writer/)

&#x200B;

Process of Undertaking a Successful Energy Au
dit

[https://courze.org/process-of-undertaking-a-successful-energy-audit/](https://courze.org/process-of-undertaking-a-
successful-energy-audit/)

&#x200B;

Craft stunning UI UX design as a digital product designer

[https://courze.org/craf
t-stunning-ui-ux-design-as-a-digital-product-designer/](https://courze.org/craft-stunning-ui-ux-design-as-a-digital-prod
uct-designer/)

&#x200B;

Mastering LangChain and AWS: A Guide to Economic Analysis

[https://courze.org/mastering-langc
hain-and-aws-a-guide-to-economic-analysis/](https://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis/
)

&#x200B;

Mastering Excel VBA User Forms

[https://courze.org/mastering-excel-vba-user-forms/](https://courze.org/mas
tering-excel-vba-user-forms/)

&#x200B;

Python Bootcamp: Master Python with Real-World Projects

[https://courze.org/py
thon-bootcamp-master-python-with-real-world-projects/](https://courze.org/python-bootcamp-master-python-with-real-world-
projects/)

&#x200B;

Executive Diploma of Chief Digital Officer

[https://courze.org/executive-diploma-of-chief-digital
-officer/](https://courze.org/executive-diploma-of-chief-digital-officer/)

&#x200B;

Learn how to fit fitness into your
 life

[https://courze.org/learn-how-to-fit-fitness-into-your-life/](https://courze.org/learn-how-to-fit-fitness-into-yo
ur-life/)

&#x200B;

Mini MBA in Human Resources Management

[https://courze.org/mini-mba-in-human-resources-management/
](https://courze.org/mini-mba-in-human-resources-management/)

&#x200B;

File & Folder Management Using PowerShell

[htt
ps://courze.org/file-folder-management-using-powershell/](https://courze.org/file-folder-management-using-powershell/)


&#x200B;

Professional Diploma in Unit Economics Management

[https://courze.org/professional-diploma-in-unit-economics-
management/](https://courze.org/professional-diploma-in-unit-economics-management/)

&#x200B;

Learn Salesforce (Admin +
 Developer) with LWC Live Project

[https://courze.org/learn-salesforce-admin-developer-with-lwc-live-project/](https://
courze.org/learn-salesforce-admin-developer-with-lwc-live-project/)

&#x200B;

Como Ser Hacker: 13 Importantes Lições An
tes de Começar

[https://courze.org/como-ser-hacker-13-importantes-licoes-antes-de-comecar/](https://courze.org/como-ser
-hacker-13-importantes-licoes-antes-de-comecar/)

&#x200B;

Talent Acquisition: HR Planning, Recruiting and Onboarding


[https://courze.org/talent-acquisition-hr-planning-recruiting-and-onboarding/](https://courze.org/talent-acquisition-hr-
planning-recruiting-and-onboarding/)

&#x200B;

Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web

[https://c
ourze.org/curso-de-hostinger-2023-el-hosting-ideal-para-tu-pagina-web/](https://courze.org/curso-de-hostinger-2023-el-ho
sting-ideal-para-tu-pagina-web/)

&#x200B;

Cómo Crear una Página Web con WordPress y ChatGPT Desde Cero

[https://courz
e.org/como-crear-una-pagina-web-con-wordpress-y-chatgpt-desde-cero/](https://courze.org/como-crear-una-pagina-web-con-wo
rdpress-y-chatgpt-desde-cero/)

&#x200B;

Ms Excel/Excel 2023 – The Complete Introduction to Excel

[https://courze.org/
ms-excel-excel-2022-the-complete-introduction-to-excel/](https://courze.org/ms-excel-excel-2022-the-complete-introductio
n-to-excel/)

&#x200B;

Cómo Crear una Página Web con WordPress Para Principiantes

[https://courze.org/como-crear-una-p
agina-web-con-wordpress-para-principiantes/](https://courze.org/como-crear-una-pagina-web-con-wordpress-para-principiant
es/)

&#x200B;

Cómo Crear Una Tienda Online Desde Cero Para Principiantes

[https://courze.org/como-crear-una-tienda-on
line-desde-cero-para-principiantes/](https://courze.org/como-crear-una-tienda-online-desde-cero-para-principiantes/)

&#
x200B;

&#x200B;
```
---

     
 
all -  [ Gemini 👍🌚 ](https://v.redd.it/um4exjmvnysc1) , 2024-04-08-0910
```
Never knew 14 yrs ago, Rick astley taught about LangChain  through his songs. 🤯😂😂

#aiml #aiforfun #rofl #gemini #google

```
---

     
 
all -  [ retriever is not returning proper answers to obvious questions ](https://www.reddit.com/r/LangChain/comments/1bxs6g9/retriever_is_not_returning_proper_answers_to/) , 2024-04-08-0910
```
1. I loaded and split a PDF document using  PDFMiner (I  also tried a couple of other loaders)
2. I embedded the result 
and stored it in VectorDB
3. I retrieved the Data with  RetrievalQA and a question like 'What did this document say abou
t Eye safety  ?' which is mentioned a couple of times in the 80 pages document

The LLM always answers with : 'it looks 
like there nothing mentioned about  Eye safety '

  
FYI: When I check how the PDF is loaded it shows the content relate
d to eye safety in the pages but it has a lot of \\n and it include headers. I don't know if this is contributing to the
 bad behavior

I am new to Langchain and it is driving me crazy, please help !


```
---

     
 
all -  [ Need help regarding LLM project ](https://www.reddit.com/r/LangChain/comments/1bxp7p6/need_help_regarding_llm_project/) , 2024-04-08-0910
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

     
 
all -  [ Python not utilizing GPU even with CUDA enabled ](https://www.reddit.com/r/LangChain/comments/1bxmka8/python_not_utilizing_gpu_even_with_cuda_enabled/) , 2024-04-08-0910
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

     
 
all -  [ Should I be using Langchain?  ](https://www.reddit.com/r/LangChain/comments/1bxm44q/should_i_be_using_langchain/) , 2024-04-08-0910
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

     
 
all -  [ using RAG, NLP, LLM for decision tree evaluation when embedded in tabular data within otherwise unst ](https://www.reddit.com/r/LangChain/comments/1bxf6bi/using_rag_nlp_llm_for_decision_tree_evaluation/) , 2024-04-08-0910
```
When integrating a Retriever-Augmented Generation (RAG) model with a Large Language Model (LLM) to process documents con
taining tabular data and embedded decision trees, the goal is to respond to user prompts that necessitate traversing the
 documents (retrieved by the RAG) and evaluating a decision tree. is anyone working on this? it is non-trivial 
```
---

     
 
all -  [ Completely free unlimited open source AI agents, run it yourself on website ](https://www.reddit.com/r/Bard/comments/1bxeiw7/completely_free_unlimited_open_source_ai_agents/) , 2024-04-08-0910
```
Hey, reddit community!
just like what I said in the headline

Check it out: https://github.com/MikeChan-HK/Gemini-agent-
example

Simple examples with Langchain….
```
---

     
 
all -  [ Completely free unlimited open source AI agents, run it yourself on website ](https://www.reddit.com/r/AutoGPT/comments/1bxeh65/completely_free_unlimited_open_source_ai_agents/) , 2024-04-08-0910
```
Hey, reddit community!
just like what I said in the headline

Check it out: https://github.com/MikeChan-HK/Gemini-agent-
example

Simple examples with Langchain…..
```
---

     
 
all -  [ Need clinical trials dataset  ](https://www.reddit.com/r/LangChain/comments/1bx8l2f/need_clinical_trials_dataset/) , 2024-04-08-0910
```
I am building a RAG of patients clinical trial and over which preventing prompt injection also , first I am finding some
 data on clinical trials can some suggest ,where can I get a sample data like that 
```
---

     
 
all -  [ How to incorporate user feedback in RAG? ](https://www.reddit.com/r/LangChain/comments/1bx74lo/how_to_incorporate_user_feedback_in_rag/) , 2024-04-08-0910
```
I have a simple RAG pipeline, but now say the user is not satisfied with the response(basically a thumbs up or down), ho
w can i incorporate this feedback to improve my RAG in a continuous manner? Thanks
```
---

     
 
all -  [ Required open source libraries/package in python for visualizing the data fetched from mongodb via p ](https://www.reddit.com/r/LangChain/comments/1bx3upb/required_open_source_librariespackage_in_python/) , 2024-04-08-0910
```
here the query of mongodb generated and query queried on mongodb response data is then visualized
```
---

     
 
all -  [ I built a voice assistant using GPT and langchain ](https://www.reddit.com/r/homeassistant/comments/1bx1b62/i_built_a_voice_assistant_using_gpt_and_langchain/) , 2024-04-08-0910
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

     
 
all -  [ Need help regarding a LLM project ](https://www.reddit.com/r/LangChain/comments/1bwz6op/need_help_regarding_a_llm_project/) , 2024-04-08-0910
```
I have a dataset of 400 resumes in .txt format. I want to build a model that can generate responses to specific candidat
e queries like 'Tell me the skillset of XYZ,' but also handle generic queries like 'Tell me the names of people who went
 to Ivy League schools.' While RAG using OpenAI works well for candidate-specific queries, it struggles with generic one
s.

```
---

     
 
all -  [ Project idea: a langchain-like library for LLM application development ](https://www.reddit.com/r/Clojure/comments/1bwwymn/project_idea_a_langchainlike_library_for_llm/) , 2024-04-08-0910
```
After looked at Langchain and its Java implementation langchain4j, I think Clojure is pretty good at defining protocols 
for all necessary models, vector databases and agents. We can benefit from Clojure's power of abstraction to build a set
 of libraries to speed up LLM application  prototyping or development, in Clojure. 

Sounds like an exciting project ide
a to me. Not sure if there is any prior attempt or discussion for this topic. What do you think of this?
```
---

     
 
all -  [ Achieving model parallelism and n Langchain ](https://www.reddit.com/r/LangChain/comments/1bwqhj9/achieving_model_parallelism_and_n_langchain/) , 2024-04-08-0910
```
Currently I’m training an LLM and that can only handle one input string at a time for summarization. Since it is running
 with map reduce, it’s also very slow splitting each text into small chunks of size 1024 tokens. I have access four GPUs
 and my plan is to define a training function that can create 4 GPUs. Load my data structures into batches containing 4 
strings. And pass them all to a different GPU I tried that and my GPU utilization for each is still very low. Around 11%
, same as last time. However last time each model had partial models loaded onto them. Is map reduce just that slow that
 it can’t fully utilize the GPU?
```
---

     
 
all -  [ LangGraph 'function_call' error using LMStudio ](https://www.reddit.com/r/LangChain/comments/1bwq86t/langgraph_function_call_error_using_lmstudio/) , 2024-04-08-0910
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

     
 
all -  [ How to create a custom tool in LangChain. i get this error. from langchain_core.tools import registe ](https://www.reddit.com/r/LangChain/comments/1bwpi9u/how_to_create_a_custom_tool_in_langchain_i_get/) , 2024-04-08-0910
```
I did alredy the process, but i cannot register the tool to invoke it
```
---

     
 
all -  [ What's your favourite reranker? Any best for reranking chat history? ](https://www.reddit.com/r/LangChain/comments/1bwm4is/whats_your_favourite_reranker_any_best_for/) , 2024-04-08-0910
```
e.g. flashrank's models?  
[https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/](https://pytho
n.langchain.com/docs/integrations/retrievers/flashrank-reranker/)
```
---

     
 
all -  [ Type of Faiss index ](https://www.reddit.com/r/LangChain/comments/1bwkmwi/type_of_faiss_index/) , 2024-04-08-0910
```
Hello,

I am currently working with langchain for document-related processing tasks, specifically utilizing the faiss.fr
om\_documents feature for indexing and similarity searches. I am interested in understanding what the default FAISS inde
x type is when using faiss.from\_documents without specifying any particular configuration. For instance, does it defaul
t to using PQIVF, LSH, or another type of index?

Does it only support inner product & L2 index?
```
---

     
 
all -  [ SQL agent with mixtral ](https://www.reddit.com/r/LangChain/comments/1bwkeql/sql_agent_with_mixtral/) , 2024-04-08-0910
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

     
 
all -  [ Entry Level Data Scientist Resume ](https://www.reddit.com/r/resumes/comments/1bwkbjx/entry_level_data_scientist_resume/) , 2024-04-08-0910
```
Hi guys, I've been in no luck for a considerable amount of time so I decided to create a new template for my resume. I k
now the market is sh\*tty af but there is nothing I can do I guess.

What do you all think? Would you give this resume a
 shot?

https://preview.redd.it/le19vkq88ssc1.png?width=788&format=png&auto=webp&s=f51a0574fecad2b89e3632ad9de74dde2888a
80a


```
---

     
 
all -  [ Finetuning for RetrievalQA chain ](https://www.reddit.com/r/LangChain/comments/1bwikyf/finetuning_for_retrievalqa_chain/) , 2024-04-08-0910
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

     
 
all -  [ Build agent chatbot ](https://www.reddit.com/r/LangChain/comments/1bwgtev/build_agent_chatbot/) , 2024-04-08-0910
```
Can everybody let me have a question Regarding the problem of building a chatbot agent, if there are many tools, is ther
e a way to export only the necessary tools and give them to the agent to use?
```
---

     
 
all -  [ [HIRING][EUR 40K - 70K] Data Scientist (m/f/x/d) - Spain, Germany ](https://www.reddit.com/r/jobb/comments/1bwgq5f/hiringeur_40k_70k_data_scientist_mfxd_spain/) , 2024-04-08-0910
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

     
 
all -  [ I recently failed a Managerial interview. What did I do wrong? ](https://www.reddit.com/r/ExperiencedDevs/comments/1bwdvpu/i_recently_failed_a_managerial_interview_what_did/) , 2024-04-08-0910
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

     
 
all -  [ Claude Tokens consumption ](https://www.reddit.com/r/LangChain/comments/1bwdr62/claude_tokens_consumption/) , 2024-04-08-0910
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

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-08-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-08-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-08-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-08-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-08-0910
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

     
