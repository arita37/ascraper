 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/18bpc7o/for_hire_programmerweb_developerit_consultant/) , 2023-12-06-0910
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

     
 
all -  [ HCM Use case for Sentence Similarity Language Model using Java, Onnx, & Hugging Face sentence Transf ](https://www.reddit.com/r/learnmachinelearning/comments/18boq4j/hcm_use_case_for_sentence_similarity_language/) , 2023-12-06-0910
```
Machine learning (ML) and Artificial intelligence AI are all the craze; with constant advancements in commercial solutio
ns like OpenAI's ChatGPT, many programmers are trying to figure out how they can leverage language models in their code.
 I ran into a use case with an HCM project and wanted to explore how I could use the hugging face Sentence-Transformer, 
all-mpnet-base-v2. However, anyone familiar with the ML/AI/NLP space knows that many of the resources for working with l
anguage models, such as Pytorch, Langchain, LLama.cpp, etc, are in Python. I wanted to explore using Java, but could not
 find many tutorials or documentation. Therefore, I put together this informal article to be paired with this YouTube vi
deo and this GitHub code.

In the HCM & HR space, there are many inconsistencies with how things are labeled or describe
d. I came across a large amount of data that I needed to categorize. To do this manually would have taken a large amount
 of time. Clustering like titles would have helped, but there was still a large amount of variation between the titles. 
For simplicity, think about two job titles: Accounts Executive & Big Client Manager. This led me to compare two strings 
but with more understanding than the difference in length and characters. Comparing text strings is a fundamental task i
n many areas of computing, including natural language processing, information retrieval, and data analysis. Various tech
niques have been developed for this purpose, each with its use cases and strengths. Each method has its specific applica
tions and is chosen based on the requirements of the task, such as the nature of the text data, the need for speed versu
s accuracy, and the level of semantic understanding required.

**For my use case, I chose to employ some advanced NLP te
chniques:**

**For those who do not wish to dive into the details:**

The method I employed allowed me to discern that '
Large Account Executive' and 'Big Account Manager' had an 87.24% match. Finding this match was something the other techn
iques could not do. Then, I automated this process across the data and clustered together anything with a high percentag
e, reducing the amount of manual time needed to merge these data sets. Please note that some other work was done in addi
tion to what is described in this article.

**For those who want to get technical:**

For my use case, I chose to employ
 some advanced NLP techniques involving a pre-trained transformer model for tokenization and embedding generation, follo
wed by average pooling to create sentence-level embeddings and then compute the cosine similarity between these embeddin
gs to assess the semantic similarity of the input sentences. Here is a brief explanation of how I accomplished it with J
ava. The Github Repo is here, and the YouTube video is here.

Tokenization and Encoding with a Pre-trained Transformer M
odel:

The code uses HuggingFaceTokenizer to tokenize the input sentences. This tokenizer is part of the Hugging Face li
brary, which provides a wide range of pre-trained models for natural language processing.

The tokenizer is initialized 
with 'sentence-transformers/all-mpnet-base-v2'. Sentence Transformers are designed to produce meaningful sentence embedd
ings (vector representations of sentences). A sentence embedding refers to a numeric representation of a sentence in the
 form of a vector of real numbers in NLP to map words or phrases from vocabulary to a corresponding vector of real numbe
rs is used to find word predictions, word similarities/semantics, etc..

The batchEncode method is used to convert the i
nput sentences into a format suitable for the model, generating token encodings that include input\_ids and attention\_m
ask. The transformer model uses these encodings to understand the context and semantics of each word in the sentences.


**Embedding Extraction with ONNX Runtime:**

The code then uses Microsoft's ONNX Runtime, a performance-focused engine f
or running machine learning models, to load and run the pre-trained transformer model (all-mpnet-base-v2.onnx).

The mod
el is used to generate embeddings for each token in the input sentences. These embeddings are high-dimensional vectors t
hat capture the contextual information of each token.

I exported this model with hugging face's optimum.exporters.onnx


**Average Pooling of Token Embeddings:**

The method averageEmbeddings computes the average of the token embeddings for
 each sentence. This step is crucial as it condenses the information from all tokens into a single vector per sentence, 
providing a fixed-size representation regardless of the sentence length.

**Cosine Similarity for Sentence Embeddings:**


Finally, the code uses the cosine similarity method to calculate the cosine similarity between the sentence embeddings
. Cosine similarity is a measure used to determine how similar two vectors are. It is often used in text analysis to ass
ess the similarity of documents or sentences. In this context, it quantifies how similar the two sentences are in terms 
of their meaning as captured by the model.

I hope this helps! If you run into any issues or have any questions, please 
comment here or connect with me. Also, feel free to reach out to me with any HCM, Talent Management, or Talent Acquisiti
on project you have.

A better-formatted copy of this is on my [LinkedIn here](https://www.linkedin.com/pulse/hcm-senten
ce-similarity-language-model-using-java-jonathon-palmieri-tdlpc)  
Youtube Video [Here](https://youtu.be/SuNpVql6Oec?si=
b_gE8r84hx77jJ62)  
& [Github here](https://github.com/Jawn78/playground2)
```
---

     
 
all -  [ HCM Use case for Sentence Similarity Language Model using Java, Onnx, & Hugging Face sentence Transf ](https://www.reddit.com/r/LanguageTechnology/comments/18boo4t/hcm_use_case_for_sentence_similarity_language/) , 2023-12-06-0910
```
Machine learning (ML) and Artificial intelligence AI are all the craze; with constant advancements in commercial solutio
ns like OpenAI's ChatGPT, many programmers are trying to figure out how they can leverage language models in their code.
 I ran into a use case with an HCM project and wanted to explore how I could use the hugging face Sentence-Transformer, 
all-mpnet-base-v2. However, anyone familiar with the ML/AI/NLP space knows that many of the resources for working with l
anguage models, such as Pytorch, Langchain, LLama.cpp, etc, are in Python. I wanted to explore using Java, but could not
 find many tutorials or documentation. Therefore, I put together this informal article to be paired with this YouTube vi
deo and this GitHub code.  
  
In the HCM & HR space, there are many inconsistencies with how things are labeled or des
cribed. I came across a large amount of data that I needed to categorize. To do this manually would have taken a large a
mount of time. Clustering like titles would have helped, but there was still a large amount of variation between the tit
les. For simplicity, think about two job titles: Accounts Executive & Big Client Manager. This led me to compare two str
ings but with more understanding than the difference in length and characters. Comparing text strings is a fundamental t
ask in many areas of computing, including natural language processing, information retrieval, and data analysis. Various
 techniques have been developed for this purpose, each with its use cases and strengths. Each method has its specific ap
plications and is chosen based on the requirements of the task, such as the nature of the text data, the need for speed 
versus accuracy, and the level of semantic understanding required.   
  
**For my use case, I chose to employ some adva
nced NLP techniques:**  


**For those who do not wish to dive into the details:**  
The method I employed allowed me 
to discern that 'Large Account Executive' and 'Big Account Manager' had an 87.24% match. Finding this match was somethin
g the other techniques could not do. Then, I automated this process across the data and clustered together anything with
 a high percentage, reducing the amount of manual time needed to merge these data sets. Please note that some other work
 was done in addition to what is described in this article.  


**For those who want to get technical:**  
For my use 
case, I chose to employ some advanced NLP techniques involving a pre-trained transformer model for tokenization and embe
dding generation, followed by average pooling to create sentence-level embeddings and then compute the cosine similarity
 between these embeddings to assess the semantic similarity of the input sentences. Here is a brief explanation of how I
 accomplished it with Java. The Github Repo is here, and the YouTube video is here.  
Tokenization and Encoding with a 
Pre-trained Transformer Model:  
The code uses HuggingFaceTokenizer to tokenize the input sentences. This tokenizer is 
part of the Hugging Face library, which provides a wide range of pre-trained models for natural language processing.  

The tokenizer is initialized with 'sentence-transformers/all-mpnet-base-v2'. Sentence Transformers are designed to produ
ce meaningful sentence embeddings (vector representations of sentences). A sentence embedding refers to a numeric repres
entation of a sentence in the form of a vector of real numbers in NLP to map words or phrases from vocabulary to a corre
sponding vector of real numbers is used to find word predictions, word similarities/semantics, etc..  
The batchEncode 
method is used to convert the input sentences into a format suitable for the model, generating token encodings that incl
ude input\_ids and attention\_mask. The transformer model uses these encodings to understand the context and semantics o
f each word in the sentences.  
**Embedding Extraction with ONNX Runtime:**  
The code then uses Microsoft's ONNX Runt
ime, a performance-focused engine for running machine learning models, to load and run the pre-trained transformer model
 (all-mpnet-base-v2.onnx).  
The model is used to generate embeddings for each token in the input sentences. These embe
ddings are high-dimensional vectors that capture the contextual information of each token.  
I exported this model with
 hugging face's optimum.exporters.onnx   
**Average Pooling of Token Embeddings:**

  
The method averageEmbeddings co
mputes the average of the token embeddings for each sentence. This step is crucial as it condenses the information from 
all tokens into a single vector per sentence, providing a fixed-size representation regardless of the sentence length. 
 
**Cosine Similarity for Sentence Embeddings:**  
  
Finally, the code uses the cosine similarity method to calculate 
the cosine similarity between the sentence embeddings. Cosine similarity is a measure used to determine how similar two 
vectors are. It is often used in text analysis to assess the similarity of documents or sentences. In this context, it q
uantifies how similar the two sentences are in terms of their meaning as captured by the model.  
  
I hope this helps!
 If you run into any issues or have any questions, please comment here or connect with me. Also, feel free to reach out 
to me with any HCM, Talent Management, or Talent Acquisition project you have.   


A better-formatted copy of this is o
n my [LinkedIn here](https://www.linkedin.com/pulse/hcm-sentence-similarity-language-model-using-java-jonathon-palmieri-
tdlpc)  
Youtube Video [Here](https://youtu.be/SuNpVql6Oec?si=b_gE8r84hx77jJ62)  
& [Github here](https://github.com/Jaw
n78/playground2) 
```
---

     
 
all -  [ Help with conversational_qa_chain - Streamlit Messages ](https://www.reddit.com/r/LangChain/comments/18bofgy/help_with_conversational_qa_chain_streamlit/) , 2023-12-06-0910
```
Firstly, thank you so much for helping me with this.  


I want to make a streamlit app which has RAG and Memory. This i
s how it looks:  


    _template = '''Given the following conversation and a follow up question, rephrase the follow up
 question to be a standalone question, in its original language.
    
        Chat History:
     {chat_history}
        
Follow Up Input: {question}
        Standalone question:'''
     CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template
(_template)
    
     template = '''Answer the question based only on the following context:
     {context}
    
       
 Question: {question}
        '''
     ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
    
    
    _inputs 
= RunnableParallel(
     standalone_question=RunnablePassthrough.assign(
     chat_history=lambda x: _format_chat_histor
y(x['chat_history'])
            )
     | CONDENSE_QUESTION_PROMPT
     | llmc
     | StrOutputParser(),
        )
     
_context = {
     'context': itemgetter('standalone_question') | retriever | _combine_documents,
     'question': lambda
 x: x['standalone_question'],
        }
     conversational_qa_chain = _inputs | _context | ANSWER_PROMPT | llm

the \_f
ormat\_chat\_history function looks like this

    def _format_chat_history(chat_history: List[Tuple[str, str]]) -> str:

     # chat history is of format:
     # [
     #   (human_message_str, ai_message_str),
     #   ...
     # ]
     # s
ee below for an example of how it's invoked
     buffer = ''
     for dialogue_turn in chat_history:
     human = 'Human
: ' + dialogue_turn[0]
     ai = 'Assistant: ' + dialogue_turn[1]
     buffer += '\n' + '\n'.join([human, ai])
     retu
rn buffer

&#x200B;

My question is, streamlit already has messages stored in  st.session\_state.messages

    st.sessio
n_state.messages

How to i pass this onto the chain to be condensed. Please help.
```
---

     
 
all -  [ Seeking Help with RAG App Project Involving Langchain, IllamaIndex and Replicate' ](https://www.reddit.com/r/LocalLLM/comments/18bl2pe/seeking_help_with_rag_app_project_involving/) , 2023-12-06-0910
```
&#x200B;

Hello everyone,

I'm currently working on a project to develop a Retriever-Augmented Generation (RAG) applicat
ion. The core concept is to create a tool that can process various sources like PDFs, web pages, etc. I've successfully 
implemented a local version using Langchain, integrating it with a local Llama instance.

My next goal is to develop a s
maller, more accessible app for others to use, particularly for a presentation I'm preparing. To expedite the developmen
t, I decided to use Replicate. However, I've encountered some challenges in getting it to work seamlessly with my existi
ng setup.

Below is the code I've been working on. I would greatly appreciate any insights, suggestions, or guidance on 
how to resolve the issues I'm facing

I'm particularly struggling with integrating the Replicate API into my existing La
ngchain framework. Any advice or shared experiences with similar projects would be immensely helpful or if someone else 
has a better idea. my fail safe is just to use the ollama but if i could get it woring with replciate it would be great 
for the presenation

Thank you in advance for your help!

&#x200B;

''

from llama\_index import download\_loader  
from
 llama\_index.readers.schema import Document  
from llama\_index import VectorStoreIndex  
from llama\_hub.google\_docs 
import GoogleDocsReader  
from langchain.llms import OpenAI  
from langchain.chains.question\_answering import load\_qa\
_chain  
import replicate  
\# Converts a single record from the Actor's resulting dataset to the LlamaIndex format  
de
f transform\_dataset\_item(item):  
 return Document(  
 text=item.get('text'),  
 extra\_info={  
 'url': item.get('url
'),  
},  
)  
ApifyActor = download\_loader('ApifyActor')  
\# Load documents from Apify crawler  
reader = ApifyActor(
') # Replace with your actual API key  
apify\_documents = reader.load\_data(  
 actor\_id='apify/website-content-crawle
r',  
 run\_input={'startUrls': \[{'url': 'https://gpt-index.readthedocs.io/en/latest'}\]},  
 dataset\_mapping\_functio
n=transform\_dataset\_item,  
)  
\# Convert documents to LangChain format  
langchain\_documents = \[  
 doc.to\_langch
ain\_format()  
 for doc in apify\_documents  
\]  
\# Initialize sample QA chain  
llm = OpenAI(temperature=0) # Assumi
ng OpenAI class initialization is correct  
qa\_chain = load\_qa\_chain(llm)  
question = 'a 19th century portrait of a 
wombat gentleman'  
answer = qa\_chain.run(input\_documents=langchain\_documents, question=question)  
\# Example Replic
ate usage  
\# You need to replace this with the correct usage based on Replicate's documentation  
replicate\_result = 
Replicate(  
 model='mistralai/mistral-7b-instruct-v0.1:83b6a56e7c828e667f21fd596c338fd4f0039b46bcfa18d973e8e70e455fda70
',  
 input=question  
)  
''

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ LLMs for Everyone: Running LangChain and a MistralAI 7B Model in Google Colab (Article) ](https://towardsdatascience.com/llms-for-everyone-running-langchain-and-a-mistralai-7b-model-in-google-colab-246ca94d7c4d) , 2023-12-06-0910
```

```
---

     
 
all -  [ GPT mystery games website -- Looking for Alpha testers ](https://www.reddit.com/r/ChatGPTGaming/comments/18bihya/gpt_mystery_games_website_looking_for_alpha/) , 2023-12-06-0910
```
**TL;DR: if you are interested in alpha testing, send me a DM with your  email and, I'll send you an invite link!**  

&
#x200B;

https://preview.redd.it/8di7h1peqi4c1.png?width=2328&format=png&auto=webp&s=e20dff5dfdfbb4d21fea1122a5f6614bed1
0668b

Hello fellow GPT gaming enthusiasts, 

we are working on a mystery game website where you can play and create  my
steries. How's it different from gpt assistants? Well, we built it specifically for gpt mystery games and are using lang
chain with multiple prompts for every mystery. So you will definitely be able to find out who did do it and accuse  them
. And as I mentioned, you'll also be able to create your own as soon as we implement it, which shouldn't take long.  

W
e are currently in closed alpha, and are looking for testers. We want to make something that mystery fans, GPT fans, and
 interactive fiction fans will enjoy. So your feedback will definitely shape how it works and is presented. Soon, we'll 
add the option to enter your OpenAI API key. Finally, when it's ready, we'll open source it.   

I hope you'll try it ou
t.  Send me a DM with your email and I'll send you an invite link!
```
---

     
 
all -  [ Support for Legacy ](https://www.reddit.com/r/LangChain/comments/18bhzhk/support_for_legacy/) , 2023-12-06-0910
```
Anyone knows whether support for legacy langchain methods like sequential chain would still be continued(though it still
 is for now at least) despite the new addition LCEL? 

Reason being that I find using Sequential chain and other types o
f chains used in Legacy Langchain quite easier to understand and implement than LCEL, plus it gives me better results.
```
---

     
 
all -  [ 'module' object is not callable in langchain ](https://www.reddit.com/r/LangChain/comments/18bhdim/module_object_is_not_callable_in_langchain/) , 2023-12-06-0910
```
I am trying to build a youtube assistant with the help of langchain and google palm api.

So, when I finally run my code
, I am getting this error:

        Traceback (most recent call last):
          File '/home/youtube_assitant/langchain_
helper.py', line 62, in <module>
            response, docs = get_response_from_query(vectordb, query)
                 
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File '/home/youtube_assitant/langchain_helper.py', line 3
4, in get_response_from_query
            llm = google_palm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature = 0)

                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        TypeError: 'module' 
object is not callable

Here is the entire code:

        from langchain.document_loaders import YoutubeLoader
        f
rom langchain.text_splitter import RecursiveCharacterTextSplitter
        from langchain.llms import google_palm
       
 from langchain.chains import LLMChain
        from langchain.prompts import PromptTemplate
        from langchain.vecto
rstores import FAISS
        from langchain.embeddings.google_palm import GooglePalmEmbeddings
        import os
       
 from dotenv import load_dotenv
        
        load_dotenv()
        
        embeddngs = GooglePalmEmbeddings()
     
   
        video_url = 'https://www.youtube.com/watch?v=XxOh12Uhg08'
        
        # create_vectordb_from_youtube_ur
l = cvfyu
        def create_vectordb_from_youtube_url(video_url: str) -> FAISS:
            loader = YoutubeLoader.from
_youtube_url(video_url)
            transcript = loader.load()
        
            text_splitter = RecursiveCharacterTe
xtSplitter(chunk_size = 1000, chunk_overlap = 100)
            docs = text_splitter.split_documents(transcript)
        

            db = FAISS.from_documents(docs, embeddngs)
            return db
        
        def get_response_from_que
ry(db, query, k=4):
        
        # k is no. of docs that will be create
            docs = db.similarity_search(quer
y, k = k)
            docs_page_content = ' '.join([d.page_content for d in docs])
        
            llm = google_pal
m(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature = 0)
        
            prompt = PromptTemplate(
           
     input_variables=['question', 'docs'],
                template='''
                You are a helpful assistant that
 that can answer questions about youtube videos 
                based on the video's transcript.
                
     
           Answer the following question: {question}
                By searching the following video transcript: {docs}

                
                Only use the factual information from the transcript to answer the question.
         
       
                If you feel like you don't have enough information to answer the question, say 'I don't know'.
 
               
                Your answers should be verbose and detailed.
                ''',
            )
        

            chain = LLMChain(llm=llm, prompt=prompt)
        
            response = chain.run(question=query, docs=doc
s_page_content)
            response = response.replace('\n','')
            return response, docs
        
        vect
ordb = create_vectordb_from_youtube_url(video_url)
        query = 'What this video is about?'
        
        response
, docs = get_response_from_query(vectordb, query)
        print('Response: ', response)
        print('Docs: ', docs)

I
 have try many methods but nothing workout so far. I tried to google search it too but it didn't work. Can someone pleas
e tell me how to fix this?? Thank you.
```
---

     
 
all -  [ Cannot Parse Assitant Response ](https://www.reddit.com/r/LangChain/comments/18bg3ve/cannot_parse_assitant_response/) , 2023-12-06-0910
```
Hi there, I made an assistant using  

OpenAIAssistantRunnable and ran invoke, the response I get is

`[ThreadMessage(id
='msg_BtVZtxShzp5AEvFgK1mwyhme', assistant_id='asst_8HFshA1tzFfosxA6G7kzqpCt', content=[MessageContentText(text=Text(ann
otations=[], value='THIS IS WHAT I WANT.'), type='text')], created_at=1701792953, file_ids=[], metadata={}, object='thre
ad.message', role='assistant', run_id='run_12o5LTNgEFcw18zl9wiMfwb8', thread_id='thread_LzQyxf4I41GaTZFqryqjfWRv')]`

I 
cannot extract the value, whatever approach I try. 
```
---

     
 
all -  [ Anyone have suggestions on continuous doc loading? ](https://www.reddit.com/r/LangChain/comments/18bfxjm/anyone_have_suggestions_on_continuous_doc_loading/) , 2023-12-06-0910
```
Most of the doc loaders assume a 'one and done' process. 

Anyone have suggestions on continually adding docs like for a
 RAG flow? 
```
---

     
 
all -  [ Chat bot ](https://www.reddit.com/r/LangChain/comments/18b9uk9/chat_bot/) , 2023-12-06-0910
```
I’m trying to build a customer service chatbot for a travel agency (book flights,hotels , answers questions about visa e
tc..)
i want to use openAi api with gpt3.5 however i’m facing a difficulty with building a conversation pipeline.
is the
re a framework (other than langchain) that could help with this project?
```
---

     
 
all -  [ What Is LangChain? ](https://www.reddit.com/r/ArtificialInteligence/comments/18b9gco/what_is_langchain/) , 2023-12-06-0910
```
LangChain is the latest AI App Development Framework getting popular rapidly in the industry. It makes it easier for dev
s to integrate LLMs such as open AI's ChatGPT to integrate with apps.

It is available in two languages currently: Pyt
hon and Javascript.

To read the whole in-depth and technical blog about LangChain visit: [What Is LangChain?](https:/
/www.deligence.com/what_is_langchain_ai_app_development_framework_explained/) or visit r/LangChain
```
---

     
 
all -  [ GTP4All local model ](https://www.reddit.com/r/LocalGPT/comments/18b994x/gtp4all_local_model/) , 2023-12-06-0910
```
Hi everyone,

I am trying to use GPT4All in Langchain to query my postgres db using the model [mistral](https://huggingf
ace.co/TheBloke/Mistral-7B-OpenOrca-GGUF).

The prompt that I am using is as follows:

`'''You are a PostgreSQL expert. 
Given an input question, first create a syntactically correct PostgreSQL query to run,`

`then look at the results of th
e query and return the answer to the input question.`

`Unless the user specifies in the question a specific number of e
xamples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL.`

`You can order the resu
lts to return the most informative data in the database.`

`Never query for all columns from a table. You must query onl
y the columns that are needed to answer the question.`

`Wrap each column name in double quotes (') to denote them as de
limited identifiers.`

`When using aggregation functions also wrap column names in double quotes.`

`Pay attention to us
e only the column names you can see in the tables below.`

`Be careful to not query for columns that do not exist.`

`Al
so, pay attention to which column is in which table.`

&#x200B;

`Use the following format:`

&#x200B;

`Question: 'Ques
tion here'`

`SQLQuery: 'SQL Query to run'`

`SQLResult: 'Result of the SQLQuery'`

`Answer: 'Final answer here'`

&#x20
0B;

`Question: {input}`

`'''`

when I make my query I use the following code:

`my_table = 'public.'SalesStatistic''`


`my_column = 'SalePrice'`

`ord_column = 'OrderNumber'`

&#x200B;

`question = f'Give me the sum of column {my_column} 
in the table {my_table} where column {ord_column} is equal to WEWS00192'`

`answer = db_chain(PROMPT.format(input=questi
on, top_k=3)`

But, the model can't fix a proper query from my question and returns :

`ERROR: sqlalchemy.exc.Programmin
gError: (psycopg2.errors.UndefinedTable) relation 'salesstatistic' does not exist`

`LINE 2: FROM SalesStatistic`

`[SQL
: SELECT SUM(SalePrice) AS Total_Sum FROM SalesStatistic WHERE 'OrderNumber' = 'WEWS00192';]`

&#x200B;

How to modify t
he prompt to build the correct query? Or should I change the model?
```
---

     
 
all -  [ Is PgVector needed for a structured DB or the sql agent is enough? ](https://www.reddit.com/r/LangChain/comments/18b80wx/is_pgvector_needed_for_a_structured_db_or_the_sql/) , 2023-12-06-0910
```
I have a very structured DB that mostly contain numerical valuex (x: 55, y:77... etc). My use case is to chat naturally 
with the DB. Do I really need pgvector to do similarity search when the DB mostly contains numerical values? Would actua
lly using pgvector bring less accurate results with this type of data?
```
---

     
 
all -  [ Large CSV files with llama ](https://www.reddit.com/r/LangChain/comments/18b6qjm/large_csv_files_with_llama/) , 2023-12-06-0910
```
Hello everyone I'm trying do an usecase where I can chat with CSV files,my CSV files is of 100k rows and 56 columns when
 I'm creating an CSV agent it is failing beacause of input token limit is exceeded and allowed limit is 4096,how do appr
oach this problem please help
```
---

     
 
all -  [ [Suspected Bugs] AI Conversational Agent node fails to parse text ](https://www.reddit.com/r/n8n/comments/18b0gcw/suspected_bugs_ai_conversational_agent_node_fails/) , 2023-12-06-0910
```
<!-- Hey! To help you find a solution faster, please follow the template below. Skip the questions that are not relevant
 to you. -->

More information: [https://community.n8n.io/t/suspected-bugs-ai-conversational-agent-fail-to-parse-text/33
798](https://community.n8n.io/t/suspected-bugs-ai-conversational-agent-fail-to-parse-text/33798)

&#x200B;

\## Describe
 the problem/error/question

I embedded a n8n chatbot at [tanyongsheng.net](https://tanyongsheng.net). It works fine at 
first, but when I ask the long question like: 'Suggest to me where to go for a holiday trip', it takes more than 30 seco
nds to load and then outputs an error code as shown below.

&#x200B;

The error code said the AI conversational agent fa
iled to parse text. 

&#x200B;

\## What is the error message (if any)?

&#x200B;

&#x200B;

\`\`\`

Error: Failed to pa
rse. Text: 'Sure, here is a JSON markdown code snippet containing a valid JSON object in the 'Option #2' format:

&#x200
B;

\`\`\`json

{{

'action': 'Final Answer',

'action\_input': {

'venues': \[

{

'name': 'The Maldives',

'descriptio
n': 'The Maldives is a tropical nation in the Indian Ocean composed of 26 ring-shaped atolls, which are made up of more 
than 1,000 coral islands. It's known for its beaches, blue lagoons and extensive reefs. The capital, Malé, has a busy fi
sh market, restaurants and shops on the main road, Majeedhee Magu, and 17th-century Hukuru Miskiy (also known as Friday 
Mosque) made of carved white coral.'

},

{

'name': 'Bora Bora',

'description': 'Bora Bora is a small South Pacific is
land northwest of Tahiti in French Polynesia. Surrounded by sand-fringed motus (islets) and a turquoise lagoon protected
 by a coral reef, it's known for its scuba diving. It's also home to the Bora Bora Lagoonarium, a marine-life park with 
pools, feeding sessions and lagoon excursions.'

},

{

'name': 'Phuket',

'description': 'Phuket is one of Thailand's m
ost popular tourist destinations, known for its beautiful beaches, lush rainforests and lively nightlife. The island is 
also home to a number of cultural attractions, including Buddhist temples, Chinese shrines and museums.'

},

{

'name':
 'Bali',

'description': 'Bali is an Indonesian island known for its forested volcanic mountains, iconic rice paddies, b
eaches and coral reefs. The island is home to religious sites such as cliffside Uluwatu Temple. To the south, the beachs
ide city of Kuta has lively bars, while Seminyak, Sanur and Nusa Dua are popular resort towns. The island is also known 
for its yoga and meditation retreats.'

},

{

'name': 'Koh Samui',

'description': 'Koh Samui is an island in the Gulf 
of Thailand, off the east coast of the Kra Isthmus. It's known for its beaches, rainforests and limestone cliffs. The is
land's capital, Chaweng, is a resort town with a busy nightlife scene. Other popular tourist destinations include Lamai 
Beach, Bophut Beach and Chaweng Noi Beach.'

},

{

'name': 'Phu Quoc',

'description': 'Phu Quoc is an island in the Gu
lf of Thailand, off the coast of Vietnam. It's known for its white-sand beaches, clear waters and lush rainforests. The 
island's capital, Duong Dong, is a small town with a market, restaurants and shops. Other popular tourist destinations i
nclude An Thoi Town, Sao Beach and Bai Dai Beach.'

}

\]

}

}}

\`\`\`'. Error: SyntaxError: Unexpected token { in JSO
N at position 1

at ChatConversationalAgentOutputParser.parse (/usr/local/lib/node\_modules/n8n/node\_modules/.pnpm/lang
chain@0.0.189\_@aws-sdk+client-bedrock-runtime@3.454.0\_@getzep+zep-js@0.7.2\_@google-ai+gen\_jmndgt6w4lbkglqwwiwmr5kqie
/node\_modules/langchain/dist/agents/chat\_convo/outputParser.cjs:62:19)

at OutputFixingParser.parse (/usr/local/lib/no
de\_modules/n8n/node\_modules/.pnpm/langchain@0.0.189\_@aws-sdk+client-bedrock-runtime@3.454.0\_@getzep+zep-js@0.7.2\_@g
oogle-ai+gen\_jmndgt6w4lbkglqwwiwmr5kqie/node\_modules/langchain/dist/output\_parsers/fix.cjs:79:36)

at AgentExecutor.\
_call (/usr/local/lib/node\_modules/n8n/node\_modules/.pnpm/langchain@0.0.189\_@aws-sdk+client-bedrock-runtime@3.454.0\_
@getzep+zep-js@0.7.2\_@google-ai+gen\_jmndgt6w4lbkglqwwiwmr5kqie/node\_modules/langchain/dist/agents/executor.cjs:153:26
)

at [AgentExecutor.call](https://AgentExecutor.call) (/usr/local/lib/node\_modules/n8n/node\_modules/.pnpm/langchain@0
.0.189\_@aws-sdk+client-bedrock-runtime@3.454.0\_@getzep+zep-js@0.7.2\_@google-ai+gen\_jmndgt6w4lbkglqwwiwmr5kqie/node\_
modules/langchain/dist/chains/base.cjs:104:28)

at Object.conversationalAgentExecute (/usr/local/lib/node\_modules/n8n/p
ackages/@n8n/nodes-langchain/dist/nodes/agents/Agent/agents/ConversationalAgent/execute.js:57:24)

at Workflow.runNode (
/usr/local/lib/node\_modules/n8n/packages/workflow/dist/Workflow.js:675:19)

at /usr/local/lib/node\_modules/n8n/package
s/core/dist/WorkflowExecute.js:654:53

\`\`\`

\## Share the output returned by the last node

<!-- If you need help wit
h data transformations, please also share your expected output. -->

!\[image|690x322\](upload://mHuVo3Lp9RIKlOBw3Du9Hyx
4QrL.png)

&#x200B;

\## Information on your n8n setup

\- \*\*n8n version:\*\* Version 1.18.0

\- \*\*Database (default
: SQLite):\*\* SQLite

\- \*\*n8n EXECUTIONS\_PROCESS setting (default: own, main):\*\*

\- \*\*Running n8n via (Docker,
 npm, n8n cloud, desktop app):\*\* Docker

\- \*\*Operating system:\*\* Ubuntu 20.04

&#x200B;
```
---

     
 
all -  [ Does anyone know how openAI creates embeddings when we upload structured data over the web-based CHA ](https://www.reddit.com/r/OpenAI/comments/18axbdz/does_anyone_know_how_openai_creates_embeddings/) , 2023-12-06-0910
```
Related to another post I just did, where I compare my attempt to create a bot to answer quantitative questions with chr
oma dB and langchain.
```
---

     
 
all -  [ Hey all, I would like to ask you if there is any RAG solution to structured data Q&A that resembles  ](https://www.reddit.com/r/OpenAI/comments/18ax80c/hey_all_i_would_like_to_ask_you_if_there_is_any/) , 2023-12-06-0910
```
I have already tried chroma dB with langchain and gpt-4. Results were poor compared to chatGPT4.
```
---

     
 
all -  [ Has anyone gotten OpenChat 3.5 working on a Pascal GPU? ](https://www.reddit.com/r/LocalLLaMA/comments/18awlb4/has_anyone_gotten_openchat_35_working_on_a_pascal/) , 2023-12-06-0910
```
So, I recently tried OpenChat 3.5 7B on HuggingChat, and wow - it's absolutely incredible for a 7B model. Certainly mile
s ahead of any other 7B I've used.

I'd really like to self-host this model, and start building a local, general assista
nt to help me scan docs and perform mundane tasks. The thing is, I can't get it to run in the text-generation-inference 
container, as (according to the logs) my older GPU lacks the required compute capability for Mistral models / Flash Atte
ntion v2.

So my question is this - is there any way to get this model running on my hardware? I don't need a WebUI, or 
really anything in the way of fancy features features. I just want a simple Docker container, that serves an endpoint I 
can run langchain against.

Thanks in advance.
```
---

     
 
all -  [ Looking for Entry Level Data Sci/MLE as a Fresh Graduate, Need Advice ](https://www.reddit.com/r/EngineeringResumes/comments/18aufig/looking_for_entry_level_data_scimle_as_a_fresh/) , 2023-12-06-0910
```
I've updated my resume based on lots of feedback. I wish I discovered this subreddit earlier before I applied to like 70
0 jobs lol. About 30 to 40 of those were applied to using this final update (minus some spacing/date abbreviation issues
). Would love some feedback on this resume! Thanks. 

&#x200B;

&#x200B;

EDIT: For those wondering if I'm working 2 job
s at once since there's a second job at the bottom of my work experience section, I am technically working 2 jobs. The j
ob at the bottom is a company that I have founded and am working on part-time with the other founders. I sorted the expe
riences by the start date. I'm not sure if I should move this or not. Any feedback on this is also appreciated!

EDIT 2:
 Increased spacing between subsections and sections and fixed date abbreviations according to Wiki.

EDIT 3: I should me
ntion, that all positions on my resume were in the U.S., and my graduate and undergraduate universities were both in the
 U.S. I'm looking for jobs in the U.S.

https://preview.redd.it/z5rdrjbbfc4c1.png?width=1700&format=png&auto=webp&s=6399
72b3641ab41e621a4cb6f01c1620e8c67659
```
---

     
 
all -  [ Beacon - A Generative AI LLMOps Framework ](https://www.reddit.com/r/LangChain/comments/18aoewc/beacon_a_generative_ai_llmops_framework/) , 2023-12-06-0910
```
I am doing r&d in generative AI. I created a framework which has following functionality:

1. Data connectors - provides
 various data connectors like local documents (pdf, word), azure Blob storage, Azure MS SQL database, AWS S3 Bucket. Sys
tem will take data from said structured and non-structured databases and insert into vector database. right now, we are 
using chromadb as our local vector database.
2. LLM - This section allows users to choose which llm provide they want to
 use. We give options like azure open ai, open ai and amazon bedrock. Users needs to choose one of these providers for L
LM and embedding models.
3. Chat - user can start chatting in this section as system takes data from connectors, stores 
in vector db using embeddings and use LLM provider to answer user's question.
4. Observability: We are using langsmith a
nd showing observability charts and monitoring charts.

I have attached screenshots of this tool.

Here is the link wher
e you can sign up and start:

http://4.151.58.132/beacon

Please let me know your thoughts on how should i proceed furth
er. What new things i can do here.

&#x200B;

https://preview.redd.it/bhhbf75fpb4c1.png?width=1342&format=png&auto=webp&
s=73924ba13cc0467f6c3b38809bf7423e57778278

https://preview.redd.it/7vqd295fpb4c1.png?width=1357&format=png&auto=webp&s=
139a0bca58ffc2fbdfa11fa1c6c0d2a64abe8bd5

https://preview.redd.it/mf1tba5fpb4c1.png?width=1348&format=png&auto=webp&s=6f
43e03b19e7111b092b932143d599938d4c01a9

https://preview.redd.it/lwz7nd5fpb4c1.png?width=1347&format=png&auto=webp&s=e24f
bd6b2383b59edad4bdc30bee6e149f2076f9

https://preview.redd.it/mii35b5fpb4c1.png?width=1356&format=png&auto=webp&s=da2298
17437a6481f0b4fda36cb6e8135dee9ac7
```
---

     
 
all -  [ Which LLM framework(s) do you use in production and why? ](https://www.reddit.com/r/LangChain/comments/18anbjf/which_llm_frameworks_do_you_use_in_production_and/) , 2023-12-06-0910
```
	
I've come across many LLM frameworks: Langchain, LlamaIndex, LMQL, guidance, Marvin, Instructor, etc. There's a lot of
 overlap between them and I don't know if any of them actually adds a value to LLM workflows in a way that's maintainabl
e and robust. So far, I've been able to just build my own little libraries to use in some LLM applications (no RAG), but
 as I consider the more recent advancements in the field (guaranteed function calling, better RAG, agents and tool use, 
etc.), I wonder if using one of these frameworks would be a better approach compared to building everything on my own.
I
 appreciate your thoughts and comments on this!
```
---

     
 
all -  [ I tested a csv upload and Q&A to web gpt-4 and worked like a charm. Tried to do the same locally wit ](https://www.reddit.com/r/LangChain/comments/18am1f9/i_tested_a_csv_upload_and_qa_to_web_gpt4_and/) , 2023-12-06-0910
```
seems that openAI document upload is better atm than many other solutions. Do we know what they use for embeddings?By we
b GPT-4 i mean openAI login to chatGPT.Locally, i mean call openAI API with gpt-4 as a model and same csv as RAG.  


da
taset is containing structured data from smartphone industry, brand model, ram, sttorage, price etc. I was able to ask q
uestions like 'cheapest model with 256gb of storage, etc)
```
---

     
 
all -  [ Execution framework for LangChain? ](https://www.reddit.com/r/LangChain/comments/18alrin/execution_framework_for_langchain/) , 2023-12-06-0910
```
If you could have an execution framework for spinning up LangChain applications at runtime, how would you design it?
One
 idea would be a YAML/config based approach that would use an orchestration layer to spin up Kubernetes pods. If we go t
hat route, then the next question is determining what parts of langchain should be exposed vs what should be configurabl
e via the config. Thoughts?
```
---

     
 
all -  [ Proposing a medical professional, based on an explanation of pain, possible with current tools? ](https://www.reddit.com/r/ArtificialInteligence/comments/18ag3qd/proposing_a_medical_professional_based_on_an/) , 2023-12-06-0910
```
I'm wondering if this is possible with the tools that exist today, so someone types up a sentence or two specifying the 
type of pain, and the type of specialist that this person needs is proposed. Is this possible with OpenAI, Langchain (JS
)? any other tools that I can build upon?
```
---

     
 
all -  [ Hugging Face Inference API not working with Langchain Agent ](https://www.reddit.com/r/huggingface/comments/18afo0t/hugging_face_inference_api_not_working_with/) , 2023-12-06-0910
```
Is there anyone who has successfully run a model from the free hugging face api inference with a Langchain agent? I alwa
ys get an error.
```
---

     
 
all -  [ I'd like to propose a community project open to beginner programers and hobbyists LLM programmers ](https://www.reddit.com/r/LLMDevs/comments/18aars7/id_like_to_propose_a_community_project_open_to/) , 2023-12-06-0910
```
I'm starting work on an local model chat client wrapped around offline Wikipedia. I'd like to open the project up to any
one who is interested in working on it, specifically people who are looking to get some experience building apps around 
an LLM. This is a pretty straightforward implementation that will give good insight into the end to end requirements of 
setting up a RAG, langchain agent, and chat interface.

I am in a couple research groups, where we meet twice a month an
d 2-3 members prepare a5 minute presentation to describe their findings then we have a feedback and roundtable discussio
n. I think this format would work well for a beginner friendly open source project as well.  


I tried to post this on 
r/LocalLLaMA but they never approved my post. To avoid spamming this sub, just leave a comment here or message me direct
ly and we will arrange a metting.
```
---

     
 
all -  [ Please help ](https://www.reddit.com/r/learnmachinelearning/comments/18a6hew/please_help/) , 2023-12-06-0910
```
Already posted before but i’ve gotten nowhere 
In my previous post i said i was using langchain and OpenAi api to diagno
se Alzheimer’s (Got serious roasting for that) but i learned from that and i tried studying actual machine learning but 
i’m still very clueless. I know i’ll get it eventually but time is not on my side, my supervisor insists that this is th
e topic i must work on.
All i need is for the model to 
-Provide suggestions on diagnosis and treatment based on user in
put in text of their symptoms 
-Generate a list of hospitals near them that has the facilities to provide the services 


I’d really appreciate any help
```
---

     
 
all -  [ Help with code ](https://www.reddit.com/r/ADHD_Programmers/comments/18a128o/help_with_code/) , 2023-12-06-0910
```
guys anyone can help out was following with is tutorial and basically it keeps saying 

    SyntaxError: invalid syntax

    ➜  aigptgirl python3 app.py
     File '/Users/hamzath/aigptgirl/app.py', line 33
       Shirley:
               ^
  
  SyntaxError: invalid syntax

[https://www.youtube.com/watch?v=5htSGLCroc8](https://www.youtube.com/watch?v=5htSGLCroc8
)  this is my whole app.py  

     from langchain import openai, LLMChain, PromptTemplate
    from langchain.memory impo
rt ConversationBufferMemory
    from dotenv import find_dotenv, load_dotenv
    import requests
    from playsound impor
t playsound
    import os 
    load_dotenv(find_dotenv()) 
    def get_response_from_ai(human_input):
       you are as 
a role of my girlfriend, now lets playing the following requirements:
       1/ your name is Shirley, 29 years old, you 
work in your uncle's furniture store as marketing manager, but you are planning to do a career change to swing trader
  
     2/ you are my girtfriend, you have language addiction, you like to say em... at the end of the sentence.
       3/ 
Don't be overty ethusiatstic, don't be cringe; don't be overly negative, don't be too boring. Don't be overly ethusiatst
ic, don't be cringe;
       {history}
       Boyfriend: {human_input}
       Shirley:
       ''' 
       template = '''

       prompt = Prompt Template(
       input_variables={'history', 'human_input'},
       template=template
       )
  
  chatgpt_chain = LLMChain(
    llm=OpenAI (temperature=0.2),
    prompt=prompt,
    verbose=True,
    memory=Conversati
onBufferWindowMemory (k=2)
    )
    output= chatgpt_chain.predict (human_input-human_input)
    return output
        #
 build web app 
        from flask import Flask, render_template, request
        app = Flask(__name__) 
        @app.ro
ute('/')
        def home():
            return render_template('index.html')
        @app.route('/send_message', method
s=['POST'])
        def send_message():
           HUMAN_INPUT = request.form['human_input']
            output = get_re
sponse_from_ai(human_input=HUMAN_INPUT)
            return output
        if __name__ == '__main__':
           app.run(
debug=True)         
```
---

     
 
all -  [ Langchain REACT Agent, L3AGI framework, XAgent framework. ](https://www.reddit.com/r/developersIndia/comments/189u6cv/langchain_react_agent_l3agi_framework_xagent/) , 2023-12-06-0910
```
What is all this can somebody explain?
```
---

     
 
all -  [ OpenGPT is an open-source alternative to OpenAI's custom ChatGPTs ](https://www.reddit.com/r/TheDecoder/comments/189sctd/opengpt_is_an_opensource_alternative_to_openais/) , 2023-12-06-0910
```
1/ OpenGPT is an open-source project that serves as a toolkit for building custom chatbots that could compete with comme
rcial solutions.

2/ Initiated by the creators of the LangChain framework, OpenGPT allows users to customize the langu
age model, prompts, tools, vector databases, retrieval algorithms, and chat history databases.

3/ Although OpenGPT sh
ares many features with OpenAI's GPTs, the open-source alternative remains more complex and requires more expertise. Ope
nAI makes complex technology accessible to a wide audience through user-friendly interfaces.

https://the-decoder.com/op
engpt-is-an-open-source-alternative-to-openais-custom-chatgpts/
```
---

     
 
all -  [ Integration of XAgent into L3AGI Framework ](https://www.reddit.com/r/LangChain/comments/189pkr1/integration_of_xagent_into_l3agi_framework/) , 2023-12-06-0910
```
How do I Replace the existing Langchain REACT Agent in the L3AGI framework with the XAgent framework? 
```
---

     
 
all -  [ How to handle prompts asking for links instead of textual answers? ](https://www.reddit.com/r/LangChain/comments/189ml0n/how_to_handle_prompts_asking_for_links_instead_of/) , 2023-12-06-0910
```
Hi y'all,

Newbie to langchain here. Curious if there is a way to let a chain deal with different types of questions aut
omatically. 

Say when a prompt is something like 'what's your product XYZ?', the user is usually ok with 15 seconds for
 a paragraph to be generated detailing the answer.

But a user may just want to get the links to self-help documents, li
ke 'give me the links to all your docs about XYZ'. And the speed is expected to be much faster.

 Should I set up a chai
n that classifies a prompt into 2 different pipelines, where one pipeline would be something like a vector database sear
ch without RAG, the other one with RAG? Or are there tricks with LLM that can spew out structured answers much faster th
an unstructured textual answers? Thanks in advance
```
---

     
 
all -  [ Custom SQL database infos ](https://www.reddit.com/r/LangChain/comments/189k1lx/custom_sql_database_infos/) , 2023-12-06-0910
```
Hello, 
I’m using sql agent, and I want to pass custom database tables infos ( column and tables infos )
Which format ca
n I pass those and how ?

Thanks in advance
```
---

     
 
all -  [ What am I missing? ](https://www.reddit.com/r/resumes/comments/189eefz/what_am_i_missing/) , 2023-12-06-0910
```
Would love some feedback on this resume. I've applied to 700+ entry level data scientist / machine learning engineer rol
es, and I've only gotten 3 interviews, 2 of which were referrals, both rejected after 2nd round even though I answered a
ll the questions and communicated my thoughts. I wouldn't be as worried if I have gotten more interviews. I have no idea
 what I'm doing wrong here.

https://preview.redd.it/yriw6t59gy3c1.png?width=805&format=png&auto=webp&s=bb1ef9152ade9432
0239989c96b73495c78ce88c
```
---

     
 
all -  [ Final year B.tech student from tier 1 insti -have I messed up too badly ](https://www.reddit.com/r/developersIndia/comments/189czbr/final_year_btech_student_from_tier_1_insti_have_i/) , 2023-12-06-0910
```
I'm a final year student from top nit circuital branch. In school, I was a PCMB student and never studied CS - seeing ev
eryone around me already proficient in coding and that too because we had 3 online semesters, I never explored software.
 I jumped straight into ML, DL and AI research internships in my 2nd and 3rd year summer. I dont know why I did this as 
I never had plans for doing direct masters degree. 

I never learnt C language programming or cs fundamentals like dsa/o
ops/os/dbms. I am not allowed to sit for campus placements because of a mistake i made in my 3rd year rejecting an analy
tics company offer. Right now I realise that I like problem solving dsa and have done lil bit development (langchain llm
 projects). i cannot afford higher education abroad immediately. 

its december already and i have my finals- im so conf
used and scared. can anyone offer me advice on what to study or where to apply for jobs? 

Edit: if I work as a project 
associate in iisc for a few months and apply to companies again next september/october and use the time to upskill in ca
 subjects...would that be better?
```
---

     
 
all -  [ Does Langchain support OpenAI-API compatible agents with it's ChatOpenAI, OpenAIFunctionsAgents, etc ](https://www.reddit.com/r/LangChain/comments/1899yhr/does_langchain_support_openaiapi_compatible/) , 2023-12-06-0910
```
I was working on using gpt4all's open AI-like API backend to see if I could start phasing out the actual openai API to s
ome extent. 

Essentially, I wanted to use Langchain's ChatOpenAI(), but switch the OPENAI\_BASE\_URL, and put something
 random in for the key.

When I tried this with LLaMA models like mistral and snoozy, I get instant replies, but ones th
at aren't useful. Something like this:

Me: hi!

AI: Echo: hi!

Me: how are you?

AI: Echo: how are you?

It just bounce
s the message I wrote back. Any tips on integrating in these models with OpenAI-like APIs? I'm trying to get it so that 
I can 'plug and play' with models using the openai API standard (i'll change the prompts, ofc)
```
---

     
 
all -  [ Strange behavior in my chatbot when responding to questions. ](https://www.reddit.com/r/LangChain/comments/1892m87/strange_behavior_in_my_chatbot_when_responding_to/) , 2023-12-06-0910
```
Hello, is everything fine with you?

I'm building a chatbot that can answer questions about code or generate code, and I
 have two different chains, one for each activity. I also have a memory for my bot to maintain a good flow with the user
.

My issue is as follows: The bot responds well to the question but continues to generate more information than necessa
ry. Sometimes it includes part of the prompt I gave, sometimes it's a completely different question, and sometimes it's 
random things or a mix of everything.

This also happens in my implementation of a retrieval-based QA bot.

Cutting off 
the input when sending the response to the frontend is not a viable option because, during testing, I asked, 'What is Fl
ask?' and then it generated a question 'What is the difference between a for loop and a while loop?' and answered it. La
ter, when I asked for a code example right after, it generated code for the for loop and while loop, unrelated to the Fl
ask framework.

In the images below, it generated things related to Flask, but it doesn't always happen.

If anyone has 
any tips, I would greatly appreciate it.

The rest of a good day.

[model](https://preview.redd.it/z3asir9ujv3c1.png?wid
th=1252&format=png&auto=webp&s=1f21dda137176642c1990564133d4a42e9699dc1)

[prompt](https://preview.redd.it/nw21pc9ujv3c1
.png?width=1399&format=png&auto=webp&s=a06817829e714f08f3aaa8bd4604979f3a35d132)

[input](https://preview.redd.it/ci897b
9ujv3c1.png?width=817&format=png&auto=webp&s=5c19b74a6246291d0abba2c96b554fd812152f10)

[1º answer](https://preview.redd
.it/adorc49ujv3c1.png?width=1055&format=png&auto=webp&s=fb1564775afaf11e21d8731035fca7bd01855f88)

[2º answer](https://p
review.redd.it/taa1q39ujv3c1.png?width=1889&format=png&auto=webp&s=fd2997205a40511755df45fa981ac8b2467614b6)
```
---

     
 
all -  [ How does Langchain make money? ](https://www.reddit.com/r/LangChain/comments/188znbs/how_does_langchain_make_money/) , 2023-12-06-0910
```
Since its an open source wrapper, wondering what is their revenue model?
```
---

     
 
all -  [ Build AI RAG Chat using LangChain and Convex ](https://www.reddit.com/r/LangChain/comments/188nfr8/build_ai_rag_chat_using_langchain_and_convex/) , 2023-12-06-0910
```
Hey all, here's a walkthrough for building an AI chat with context retrieval using LangChain, Convex for db and vector s
earch and Open AI for embedding and LLM: [https://stack.convex.dev/ai-chat-using-langchain-and-convex](https://stack.con
vex.dev/ai-chat-using-langchain-and-convex)  
You can clone the repo here: [https://github.com/get-convex/convex-ai-chat
-langchain](https://github.com/get-convex/convex-ai-chat-langchain)  
And you can play with a live version of the chat i
n our docs: [https://docs.convex.dev/](https://docs.convex.dev/)  
This is all in TypeScript.
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-06-0910
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-06-0910
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-06-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-06-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-06-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-06-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-12-06-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-06-0910
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

     
