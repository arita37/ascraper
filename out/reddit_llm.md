 
all -  [ Using `RunnableWithMessageHistory`, why does the output always come out as multiple responses? ](https://www.reddit.com/r/LangChain/comments/1g05hae/using_runnablewithmessagehistory_why_does_the/) , 2024-10-10-0912
```
In an attempt to at least get the very basic mechanisms of a chatbot with history working, I need to be able to input a 
prompt and receive a singular response. This [article](https://python.langchain.com/v0.1/docs/expression_language/how_to
/message_history/) being one of many examples on the langchain website where they use `RunnableWithMessageHistory` to im
plement a chat history. My issue is, any iteration I've tried of trying to use this function, while the history portion 
works fine, all my outputs always end up giving me multiple responses. Like it will go back and forth with itself like t
his: `' I asked you earlier.\nAI: Ahah, you asked me earlier, and I remember! Your name is Bob!\nHuman: Ahah, yeah! How 
do you remember all this? You're so smart!\nAI: Well, I'm designed'`.

  
This specifically happens when I use `Runnable
WithMessageHistory` and not when I do model.invoke. I've also tried variations of chat prompt templates (`ChatPromptTemp
late`) that tells the system to not give me multiple responses, and while it adheres to most of my other instructions, t
hat portion of it is ignored. Any and all help with this would be so appreciated it has become a huge blocker for me. Th
ank you to the community in advance!
```
---

     
 
all -  [ Langchain Groq - Content Creator AI Agent ](https://www.reddit.com/r/Bard/comments/1g04hme/langchain_groq_content_creator_ai_agent/) , 2024-10-10-0912
```
This video is an introduction to Autonomous Agents workflow and its implementation using CrewAI and Groq LLM ||   
  
Th
ese agents are designed to perform specific tasks, make decisions, and communicate effectively with each other to solve 
complex problems. In this video, viewers will learn about the core functionalities of CrewAI, including how to set up an
d customize agents, integrate them with various tools, and leverage their capabilities for real-world applications like 
data analysis, content creation, and more. This tutorial is ideal for both beginners and advanced users interested in en
hancing their projects with AI-driven solutions​  
  
Groq and crewAI: Low inference Agents workflow: [https://www.youtu
be.com/watch?v=DNSKA49DZlM](https://www.youtube.com/watch?v=DNSKA49DZlM)
```
---

     
 
all -  [ Generate exercise routine from the list of over 3000 exercises ](https://www.reddit.com/r/LangChain/comments/1g02mtz/generate_exercise_routine_from_the_list_of_over/) , 2024-10-10-0912
```
I have over 3000 exercise in my databases. I am loading those exercises - specifically, exercise name as a text segment,
 exercise type, equipment required for this exercise and exercise directions as metadata into embedding store. I am usin
g langchain and in my prompt, I am asking LLM to generate workout routines based on this list from embedding store. Afte
r LLM generates a routine, I am storing it in database. I need LLM to use exact exercise name from my database, so that 
I can store it in my database, and later on track the workouts.  However, LLM is generating very limited set of workouts
 with only two exercises repeating in every single day for multiple weeks. Here is an example: 



    {
        'workou
tProgramName': 'Olympic Weightlifting Foundations',
        'description': 'A 4-week beginner program focused on buildin
g the foundational strength and technique for Olympic weightlifting. This program emphasizes the key lifts and their var
iations to prepare for competition.',
        'difficulty': 'Beginner',
        'programType': 'Olympic Weightlifting',

        'weeks': [
            {
                'weekNumber': '1',
                'workouts': [
                    {

                        'dayName': 'Day 1',
                        'dayOfWeek': 'Monday',
                        'dayF
ocus': 'Snatch Technique and Lower Body',
                        'exercises': [
                            {
         
                       'exerciseName': 'Olympic Squat (barbell)',
                                'sets': '3',
         
                       'reps': '5',
                                'weight': '60%',
                                're
st': '120',
                                'modifications': 'Focus on proper form and depth'
                          
  },
                            {
                                'exerciseName': 'Clean Deadlift (barbell)',
         
                       'sets': '3',
                                'reps': '5',
                                'weight
': '60%',
                                'rest': '120',
                                'modifications': 'Emphasize pro
per starting position and back angle'
                            }
                        ]
                    },
   
                 {
                        'dayName': 'Day 2',
                        'dayOfWeek': 'Wednesday',
       
                 'dayFocus': 'Clean and Jerk Technique',
                        'exercises': [
                        
    {
                                'exerciseName': 'Olympic Squat (barbell)',
                                'sets':
 '3',
                                'reps': '5',
                                'weight': '65%',
                    
            'rest': '120',
                                'modifications': 'Focus on maintaining an upright torso'
    
                        },
                            {
                                'exerciseName': 'Sumo Deadlift 
(barbell)',
                                'sets': '3',
                                'reps': '5',
                  
              'weight': '65%',
                                'rest': '120',
                                'modificat
ions': 'Concentrate on driving through the legs'
                            }
                        ]
               
     },
                    {
                        'dayName': 'Day 3',
                        'dayOfWeek': 'Friday',

                        'dayFocus': 'Full Lifts and Strength',
                        'exercises': [
                 
           {
                                'exerciseName': 'Olympic Squat (barbell)',
                                
'sets': '3',
                                'reps': '5',
                                'weight': '70%',
             
                   'rest': '120',
                                'modifications': 'Focus on explosive power out of the 
bottom'
                            },
                            {
                                'exerciseName': 'Cl
ean Deadlift (barbell)',
                                'sets': '3',
                                'reps': '5',
     
                           'weight': '70%',
                                'rest': '120',
                             
   'modifications': 'Emphasize speed off the floor'
                            }
                        ]
            
        }
                ]
            },

  
What am I doing wrong? How can I make LLM to generate diverse set of exer
cise that target multiple body parts for each day of the week?
```
---

     
 
all -  [ How to get chat history working with Chainlit? ](https://www.reddit.com/r/LangChain/comments/1g01njm/how_to_get_chat_history_working_with_chainlit/) , 2024-10-10-0912
```
I've created a Jupyter notebook that successfully implements Langchains' chat history feature. But I can't figure out ho
w to get it working with Chainlit. Specifically, which code should go under '@cl.on\_chat\_start' and which should go un
der '@cl.on\_message'. Anyone have any pointers?

Here's the relevant code of my notebook:

    chat_history = []
    
 
   text = 'Hi. My name is Bob. I am 40 years old.'
    chain = prompt_template | model | parser
    
    response = chai
n.invoke(
        {'chat_history': chat_history,
        'text': text})
    
    chat_history.extend(
        [
        
    HumanMessage(content=text),
            AIMessage(content=response),
        ]
    )

And here's my Chainlit code. C
hainlit works, it just doesn't remember conversation history.

    @cl.on_chat_start
    async def on_chat_start():
    

        model = ChatVertexAI(
            model_name='gemini-1.5-flash',
            temperature=0.5,
            strea
ming=True,
        )
    
        system_prompt = 'You are a knowledgeable and useful AI'
    
        prompt_template =
 ChatPromptTemplate.from_messages(
            [
                ('system', system_prompt),
                ('user', '{t
ext}'),
            ]
        )
    
        chain = prompt_template | model | StrOutputParser()
        cl.user_session
.set('runnable', chain)
    
    @cl.on_message
    async def on_message(message: cl.Message):
        runnable = cast(R
unnable, cl.user_session.get('runnable'))
    
        msg = cl.Message(content='')
    
        async for chunk in runn
able.astream(
            {'text': message.content},
            config=RunnableConfig(callbacks=[cl.LangchainCallbackHa
ndler()]),
        ):
            await msg.stream_token(chunk)
    
        await msg.send()


```
---

     
 
all -  [ Problems with text splitter on a markdown file ](https://www.reddit.com/r/LangChain/comments/1fzyipy/problems_with_text_splitter_on_a_markdown_file/) , 2024-10-10-0912
```
Im having trouble using the text splitters in langchain. 

I tried the example in the docs for the recursive... Tried al
l the combinations possible as ' ', '', line jump and even double line jump. The docs says that the defaults are \['\\n\
\n', '\\n', ' ', ''\] but it wont split my markdown as I want which are the white lines.

[https://python.langchain.com/
v0.1/docs/modules/data\_connection/document\_transformers/recursive\_text\_splitter/](https://python.langchain.com/v0.1/
docs/modules/data_connection/document_transformers/recursive_text_splitter/)

The text splitter (non recursive) also won
t work. Tried all combinations.

My code is:

    from langchain_text_splitters import RecursiveCharacterTextSplitter
  
  
    # Load an example document
    with open('data_dictionaries/odata_schema_ARG_inversion.md') as f:
        data_di
ctionary = f.read()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_over
lap=0,
        is_separator_regex=False,
    )
    
    texts = text_splitter.create_documents([data_dictionary])
    # 
print each element in the list
    
    for text in texts:
        print('DOCUMENT')
        print(text)

I cant find a 
solution to the text splitters where I can pass a simple markdown text like and get the documents for each separate para
graph. As you can see I dont want any overlap and setted the maximum chunk size to 3000 but this should not be changing 
anything because this is the max

    database_name: mapainvanalyticsdbdev
    schema: chatmi
    table_name: arg_openda
ta_proyectos
    table_description: Datos abiertos de proyectos de inversión de la República Argentina
     
    schema:
 chatmi
    table_name: arg_opendata_proyectos
    column_name: IdProyecto
    description: Código identificador del pro
yecto en MapaInversiones. Sinónimos: id, identificador, código, referencia, número único. Cualquier campo de identificad
or usar esta columna
    data_type: int
     
    schema: chatmi
    table_name: arg_opendata_proyectos
    column_name:
 CodigoBapin
    description: Código identificador del proyecto dentro del banco de proyectos. Sinónimos: código, refere
ncia, identificador, BAPIN, número. Cualquier campo de código usar esta columna
    data_type: nvarchar
     
    schema
: chatmi
    table_name: arg_opendata_proyectos
    column_name: NombreProyecto
    description: Nombre del proyecto. Si
nónimos: título, denominación, proyecto, obra, etiqueta. Cualquier filtro where puede ser usado en este campo de nombre 
para encontrar temáticas, usar esta columna
    data_type: nvarchar
```
---

     
 
all -  [ Can SQLDatabaseToolkit use table and column descriptions? ](https://www.reddit.com/r/LangChain/comments/1fzxkpz/can_sqldatabasetoolkit_use_table_and_column/) , 2024-10-10-0912
```
I have a database where the columns names are such that their content is not very obvious. 

The documentation for SQLDa
tabaseToolkit says it retrieves table descriptions. Is there a way to similarly  pass description of each column to SQLD
atabaseToolkit for better conversion of query to SQL?

link to documentation: [https://python.langchain.com/docs/tutoria
ls/sql\_qa/](https://python.langchain.com/docs/tutorials/sql_qa/)

https://preview.redd.it/xa0tsbugqrtd1.png?width=1288&
format=png&auto=webp&s=fe6aae454889a658026310cab91e5835e10468df
```
---

     
 
all -  [ Help needed: chatbot skipping parts of resume (using gemma2:2b) ](https://www.reddit.com/r/ollama/comments/1fzx9wn/help_needed_chatbot_skipping_parts_of_resume/) , 2024-10-10-0912
```
Hi everyone,

I'm currently working on an AI chatbot that's supposed to respond based on my resume. I've been experiment
ing with both Gemma2:2b and Mistral, but I keep running into the same issue with both models: they seem to 'skip' certai
n parts of the resume when responding to queries.

I'm wondering if this problem could be due to the way I'm processing 
the resume (which is in PDF format) or if it's related to the input pipeline I'm using. I've tried tweaking the PDF, and
 it seems to have alleviated the issue, but it still persists.

**Relevant parts of my code:**

pdf\_handling.py

    im
port argparse
    import os
    import shutil
    from langchain_community.document_loaders import PyPDFLoader
    from 
langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain.schema.document import Document
    fr
om get_embedding_function import get_embedding_function
    from langchain_chroma import Chroma
    
    def main():
   
     parser = argparse.ArgumentParser()
        parser.add_argument('--reset', action = 'store_true', help = 'Reset the 
database.')
        args = parser.parse_args()
        if args.reset:
            print('✨ Clearing Database')
         
   clear_database()
    
        documents = load_document()
        chunks = split_documents(documents)
        add_to_
chroma(chunks)
    
    def load_document():
        document_loader = PyPDFLoader('Resume.pdf')
        return document
_loader.load()
    
    def split_documents(documents: list[Document]):
        text_splitter = RecursiveCharacterTextSp
litter(
            chunk_size = 800,
            chunk_overlap = 80,
            length_function = len,
            is_
separator_regex = False,
        )
        return text_splitter.split_documents(documents)
    
    def add_to_chroma(ch
unks: list[Document]):
        db_directory = 'my_chroma_data'  
        db_path = os.path.join(db_directory, 'chroma.sq
lite3')  
    
        os.makedirs(db_directory, exist_ok=True)
        
        db = Chroma(
            persist_direct
ory=db_directory,  
            embedding_function=get_embedding_function()
        )
    
        chunks_with_ids = cal
culate_chunk_ids(chunks)
    
        existing_items = db.get(include=[]) 
        existing_ids = set(existing_items['id
s'])
        print(f'Number of existing documents in DB: {len(existing_ids)}')
    
        new_chunks = []
        for 
chunk in chunks_with_ids:
            if chunk.metadata['id'] not in existing_ids:
                new_chunks.append(chu
nk)
    
        if len(new_chunks):
            print(f'👉 Adding new documents: {len(new_chunks)}')
            new_chu
nk_ids = [chunk.metadata['id'] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
    
    else:
            print('✅ No new documents to add')
    
    def calculate_chunk_ids(chunks):
    
        last_pag
e_id = None
        current_chunk_index = 0
    
        for chunk in chunks:
            source = chunk.metadata.get('s
ource')
            page = chunk.metadata.get('page')
            current_page_id = f'{source}:{page}'
    
            
if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_c
hunk_index = 0
    
            chunk_id = f'{current_page_id}:{current_chunk_index}'
            last_page_id = current
_page_id
    
            chunk.metadata['id'] = chunk_id
    
        return chunks
    
    def clear_database():
    
    db_path = 'my_chroma_data/chroma.sqlite3'
        if os.path.exists(db_path):
            shutil.rmtree(os.path.dirn
ame(db_path))  
            print(f'✨ Database at {db_path} has been cleared.')
        else:
            print('⚠️ No d
atabase found to clear.')
    
    if __name__ == '__main__':
        main()

  
[chatboy.py](http://chatboy.py)

    im
port os
    from langchain_chroma import Chroma  # Updated import
    from langchain.prompts import ChatPromptTemplate
 
   from langchain_community.llms.ollama import Ollama
    from get_embedding_function import get_embedding_function
    

    PROMPT_TEMPLATE = '''
    You're roleplaying as Maximiliano López Montaño, based on what the resume says.
    
    
This is the resume: {context}
    
    ---
    
    Answer the question based on the above context: {question}
    '''
 
   
    def main():
        print('Welcome to the chatbot! Type 'exit' to quit.')
        
        while True:
         
   query_text = input('You: ')
            
            if query_text.lower() == 'exit':
                print('Goodbye!
')
                break
            
            response = query_rag(query_text)
            print(f'AI: {response}')

    
    def query_rag(query_text: str):
        embedding_function = get_embedding_function()
    
        persist_dire
ctory = 'my_chroma_data'
        db_path = os.path.join(persist_directory, 'chroma.sqlite3')
    
        if not os.path
.exists(db_path):
            print('⚠️ Database not found. Please run pdf_handling.py to create the database.')
       
     return 'No data available.'
    
        db = Chroma(persist_directory=persist_directory, embedding_function=embedd
ing_function)
    
        results = db.similarity_search_with_score(query_text, k=5)
    
        context_text = '\n\n-
--\n\n'.join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(P
ROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
    
        model = 
Ollama(model='gemma2:2b')
        response_text = model.invoke(prompt)
    
        formatted_response = f'{response_tex
t}'
        return formatted_response
    
    if __name__ == '__main__':
        main()

  
Any advice on where the iss
ue might lie or improvements I can make would be greatly appreciated. Thanks in advance!

I can also share the PDF if ne
cessary :)
```
---

     
 
all -  [ Working on a frontend for my project Novel Generator ](https://www.reddit.com/r/Bard/comments/1fzx9t0/working_on_a_frontend_for_my_project_novel/) , 2024-10-10-0912
```
https://preview.redd.it/ek54uxlfnrtd1.png?width=1253&format=png&auto=webp&s=ec8953ca23f5852ba8aa45a988d493fcf7737736

Ig
nore the styling, but what do you guys think? Lots of fun using langchain and google api
```
---

     
 
all -  [ Document Sections: Better rendering of chunks for long documents ](/r/AIQuality/comments/1fzwy6z/document_sections_better_rendering_of_chunks_for/) , 2024-10-10-0912
```

```
---

     
 
all -  [ Is everyone an AI engineer now 😂 ](https://www.reddit.com/r/LangChain/comments/1fzw0ie/is_everyone_an_ai_engineer_now/) , 2024-10-10-0912
```
I am finding it difficult to understand and also funny to see that everyone without any prior experience on ML or Deep l
earning is now an AI engineer… thoughts ? 
```
---

     
 
all -  [ Node based LLM interactive tool ](https://github.com/Xerophayze/XeroFlow) , 2024-10-10-0912
```
Hey everyone, I've been working on this project for about a week and thought maybe I would bring it up here as a resourc
e for people to use. I've developed a node based system programmed in Python that allows you to create custom nodes and 
be able to interact with multiple LLMs at the same time. I recently just introduced a chat node that allows you to inter
act with the LLM in a chat-based situation like in chat GPT. And I'm currently working on integrating langchain and rag.
 The system is designed so you can develop your own nodes and create your own workflows for doing many different things.
 I also have a node for developing long form content. It's interesting being able to have the system spit out 38 page re
ports or stories or summaries. It has web search capability if you have API access to a JSON based web search system. I 
currently have searXNG set up in a local virtual box system that I'm going to make available on my Google share for peop
le to download if they just want to run a local web search engine.  
Anyway you can check it out here at my GitHub. Let 
me know what you think and if you have other ideas for different types of nodes, I would love to hear it. 
https://githu
b.com/Xerophayze/XeroFlow
```
---

     
 
all -  [ Lost, unsure of the next step in learning ML ](https://www.reddit.com/r/learnmachinelearning/comments/1fzoyw9/lost_unsure_of_the_next_step_in_learning_ml/) , 2024-10-10-0912
```
I am trying to prepare myself for the job market, however environmental science data science jobs aren't really out ther
e beyond academia. Therefore I am refocusing on marketing jobs, and in turn LLMs/AI.

My background is a solid understan
ding of the 'classics', i.e RF, PLSR, log. and linear regression, SVM/SVR, gradient boost, etc. Supervised vs. unsupervi
sed, training/testing/validation splits. Preprocessing techniques.

I have read attention is all you need and followed t
utorials to recreate the core concepts of self-attention and multi-attention heads.

The next step that I have been lead
 to believe is the correct step into the world of LLMs is LangChain -> LangGraph. However, the tutorials of LangChain se
em to funnel one into using pre-made models (fine) and their API's - requiring keys, which require purchasing tokens. I 
have downloaded Llama 3.2-1B and am trying to create a chatbot of some sort, however this is not as straightforward as I
 thought it would be.

So now I have a few questions and would be thankful if anybody would share their insights:

1) Is
 my decision to focus on LangChain a logical next step given my background,  or are there other stepping stones that I s
hould be revisiting first?

2) Is there a book/resource that promotes creating a chat-bot or similar LLM based applicati
ons entirely with open-source material?

3) If I want to create a chat-bot UI/UX, and bring it beyond the terminal promp
t, this would require learning a new program, like Django or a similar webframework?

4) After having spent several week
s working on familiarizing myself with the concept of attention, and the creation of NN models through defining individu
al layers, I now have a feeling after having looked ahead that this will not play much of a role - as something like Lan
gChain seems to simplify a lot of the steps involved? Although this is just a recent impression, and I would be happy to
 be corrected on this front.

Thanks for any input and your time!
```
---

     
 
all -  [ AI Agents in 40 minutes ](https://www.reddit.com/r/LangChain/comments/1fzoht5/ai_agents_in_40_minutes/) , 2024-10-10-0912
```
The video covers code and workflow explanations for:  
  
- Function Calling  
- Function Calling Agents + Agent Runner 
 
- Agentic RAG  
- REAcT Agent: Build your own Search Assistant Agent

Watch here: [https://www.youtube.com/watch?v=bHn
4dLJYIqE](https://www.youtube.com/watch?v=bHn4dLJYIqE)
```
---

     
 
all -  [ RepoGPT –  Open-Source AI-Powered GitHub Assistant Built with Next.js and LangChain ](https://www.reddit.com/r/nextjs/comments/1fznmbl/repogpt_opensource_aipowered_github_assistant/) , 2024-10-10-0912
```
Hi everyone ✌️

I'm excited to share **RepoGPT**, an open-source project I've been working on that combines **Next.js an
d** **LangChain** to create an AI-powered assistant for interacting with your GitHub repositories using natural language
.

**What is RepoGPT?**

RepoGPT allows you to 'chat' with your codebase. By leveraging natural language processing, you
 can:

* Ask questions about your repository's code.
* Get summaries of functions, classes, or entire files.
* Request e
xplanations of complex algorithms.
* Retrieve lists of API endpoints, components, or other code structures.

**Technical
 Stack Overview**

* **Next.js**: Used as the web framework for both the frontend and backend, taking advantage of its A
PI routes and SSR capabilities.
* **LangChain**: Utilized for managing LLM calls and embeddings, enabling seamless inter
action with language models.
* **PostgreSQL with pgvector**: Acts as our vector storage solution, allowing efficient sim
ilarity search and retrieval of relevant code snippets.

**LangChain Integration**

* **LLM Calls**: Manages prompts and
 interactions with language models, abstracting the complexity of direct API calls.
* **Embeddings**: Handles the creati
on and storage of embeddings for code snippets, enabling efficient similarity searches.

**Code Integration Example**

I
f you're interested in how it all comes together, feel free to check out the API route handling the chat functionality:


👉 **GitHub Link**[src/app/api/chat/route.ts](https://github.com/mbarinov/repogpt/blob/main/src/app/api/chat/route.ts)


This file showcases how we:

* Receive user queries from the frontend.
* Use LangChain to process the query and interact
 with the language model.
* Retrieve relevant code snippets using pgvector similarity search.
* Generate a coherent resp
onse to the user.

**Getting Started**

RepoGPT is open-source and available on GitHub: [github.com/mbarinov/repogpt](ht
tps://github.com/mbarinov/repogpt)

**Requirements:**

* **Node.js** (v18 or higher)
* **pnpm** (preferred package manag
er)
* **Docker** (for setting up PostgreSQL with pgvector)
* **OpenAI API Key** (for AI functionalities)

Detailed insta
llation instructions are provided in the README.

**Why I Built RepoGPT**

Navigating large codebases can be time-consum
ing, especially when onboarding new projects. By integrating Next.js with AI capabilities, I wanted to create a tool tha
t streamlines this process for developers.

**Seeking Remote Opportunities**

On a personal note, I'm currently looking 
for remote job opportunities in EU time zones. If you know of any positions or are interested in collaborating, I'd love
 to connect!

**Links**

* **GitHub Repository**: [github.com/mbarinov/repogpt](https://github.com/mbarinov/repogpt)
* *
*Documentation**: Detailed setup and usage instructions are available in the repo.
* **Contact**: You can reach me via G
itHub or email at [me@maxbarinov.com](mailto:me@maxbarinov.com)
```
---

     
 
all -  [ RepoGPT – AI-Powered GitHub Assistant Built with LangChain ](https://www.reddit.com/r/LangChain/comments/1fzncv8/repogpt_aipowered_github_assistant_built_with/) , 2024-10-10-0912
```
Hi everyone,

I'm excited to share [RepoGPT](https://github.com/mbarinov/repogpt), an open-source tool I've been working
 on that allows developers to interact with their GitHub repositories using natural language. It leverages **LangChain**
 to provide intelligent insights into your codebase.

**What is RepoGPT?**

RepoGPT enables you to 'chat' with your code
base. Using natural language queries, you can:

* Ask how specific functionalities are implemented.
* Get summaries of c
ode sections or entire repositories.
* Retrieve lists of functions, classes, or API endpoints.
* Request explanations of
 complex algorithms.

[Chat with a repo](https://preview.redd.it/ti16oupo8ptd1.jpg?width=5088&format=pjpg&auto=webp&s=75
dd5da0519e16a7d496a5657b8403000658f45a)

**Technical Highlights**

* **LangChain Integration**: Utilizes LangChain for p
rompt management, chaining LLM calls, and handling conversational context, making complex interactions smoother.
* **Dat
a Processing with pgvector**: Uses PostgreSQL with the pgvector extension for efficient vector storage and similarity se
arch, enabling fast retrieval of relevant code snippets.
* **Backend Stack**: Built with Node.js and Prisma ORM for robu
st database interactions.

**Getting Started**

RepoGPT is open-source and available on GitHub: [github.com/mbarinov/rep
ogpt](https://github.com/mbarinov/repogpt)

**Requirements:**

* **Node.js** (v18 or higher)
* **pnpm** (preferred packa
ge manager)
* **Docker** (for PostgreSQL with pgvector setup)
* **OpenAI API Key** (for AI functionalities)

Detailed in
stallation instructions are provided in the README.

**Future Plans**

* **Advanced Query Capabilities**: Implement soph
isticated AI ReAct Agent for deeper code analysis.
* **Local AI Models Integration**: Considering Ollama integration for
 users preferring local processing.

**Feedback and Collaboration**

I would love to hear your thoughts, especially rega
rding the use of LangChain in this project. Any suggestions or contributions are highly welcome!

**Seeking Remote Oppor
tunities**

On a personal note, I'm currently looking for remote job opportunities in EU time zones. If you know of any 
positions or are interested in collaborating, please feel free to reach out.

**Links**

* **GitHub Repository**: [githu
b.com/mbarinov/repogpt](https://github.com/mbarinov/repogpt)
* **Documentation**: Detailed setup and usage instructions 
are available in the repo.
* **Contact**: You can reach me via GitHub or email at \[[me@maxbarinov.com](mailto:me@maxbar
inov.com)\].

Looking forward to your feedback and discussions!
```
---

     
 
all -  [ Does this stack qualify for a full time ML role? ](https://www.reddit.com/r/learnmachinelearning/comments/1fzn73x/does_this_stack_qualify_for_a_full_time_ml_role/) , 2024-10-10-0912
```
Hi everyone. I'd appreciate some feedback regarding this. I'm a CS undergrad towards the end of 2nd year. Still 2 more y
ears to graduate.

My current ML stack is: PyTorch, PyTorch Lightning, TensorFlow, Keras, Transformers, Pandas, NumPy, S
cikit-Learn, Matplotlib, Weights & Biases

And I'm working towards getting the following stack of technologies under my 
belt:  
--- Cloud computing: AWS, GCP  
--- LLM framework and libraries: Langchain, NLTK, LlamaIndex  
--- Big data tech
nologies: Hadoop, Spark  
--- Production: Docker, Kubernetes

All I have is a 6 month part time internship experience, d
eveloping chatbots and implementing a few ML algorithms at a startup and some personal projects.

My plan is to learn th
e stack that I've mentioned above and then create production ready applications powered by AI and then start applying fo
r full time ML roles, preferably remote roles, because where I'm living, bachelors degree is a necessary requirement to 
get any job at any company.

Any role will do, all I want is a job. I'd appreciate it if someone can spare some time, re
view my profile, and give some feedback.  
Github: [https://github.com/ammar20112001](https://github.com/ammar20112001)


https://preview.redd.it/qrrhhvyk6ptd1.png?width=825&format=png&auto=webp&s=127b2cc5caf5b9f5cd85cef7645e889a4e977783


```
---

     
 
all -  [ Useful Agents? ](https://www.reddit.com/r/LangChain/comments/1fzmzzc/useful_agents/) , 2024-10-10-0912
```
Hey, does anybody have any examples of well working and useful agents that generate value autonomously as we speak? I'm 
struggling to find examples. Maybe the replit agents oder something similar but nothing really innovative and new that's
 not 'just' autocompleting.
```
---

     
 
all -  [ generative AI hub SDK ](https://www.reddit.com/r/SAPAIcore/comments/1fzl8xu/generative_ai_hub_sdk/) , 2024-10-10-0912
```
Can generative AI hub SDK for Python work seamlessly with Langchain?
```
---

     
 
all -  [ Do you use function calling or code execution? ](https://www.reddit.com/r/LangChain/comments/1fzklin/do_you_use_function_calling_or_code_execution/) , 2024-10-10-0912
```
I'm interested to learn how people are using function calling and/or code execution successfully in their projects today
. Most AI seem to still be about RAG, and I'm wondering if anyone here has anything in PoC/production that actually take
s actions in a meaningful way.
```
---

     
 
all -  [ Advance Your Career: Access 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1fzkecp/advance_your_career_access_100_free_certified/) , 2024-10-10-0912
```
Microsoft Excel – Excel Course For Beginners

https://courze.org/microsoft-excel-excel-only-for-beginners-2023/



ChatG
PT: Make Money with ChatGPT as a New Freelancer

https://courze.org/chatgpt-make-money-with-chatgpt-as-a-new-freelancer/




The Complete MySQL Bootcamp: Go from Beginner to Expert

https://courze.org/the-complete-mysql-bootcamp-go-from-begi
nner-to-expert/



JavaScript Fundamentals Course for Beginners

https://courze.org/javascript-fundamentals-course-for-b
eginners/



Java And C++ And PHP Crash Course All in One For Beginners

https://courze.org/java-and-c-and-php-crash-cou
rse-for-beginners/



Essential Programming: Software Fundamentals for Beginners

https://courze.org/essential-programmi
ng-concepts-for-beginners-using-chatgpt/



Effective Goal Setting ( General, SMART and OKR) – हिंदी में

https://courze
.org/effective-goal-setting-general-smart-and-okr-in-hindi/



Quantity Surveying & Building Estimate

https://courze.or
g/quantity-surveying-building-estimate/



Research Methodologies in Strategy and Product Development

https://courze.or
g/research-methodologies-in-strategy-and-product-development/



Learn AutoCAD 2D & 3D : From Zero to Hero

https://cour
ze.org/learn-autocad-2d/



C-level management: 100 models for business – 5 courses in 1

https://courze.org/c-level-man
agement-100-models-for-business-success/



CSS, Bootstrap And JavaScript And Python Stack Course

https://courze.org/cs
s-bootstrap-and-javascript-and-python-stack-course/



Python For Beginners Course In-Depth

https://courze.org/python-f
or-beginners-course-in-depth/



Executive Diploma in Human Resources Strategy

https://courze.org/executive-diploma-in-
human-resources-strategy/



The Complete Jenkins DevOps CI/CD Pipeline Bootcamp

https://courze.org/the-complete-jenkin
s-devops-ci-cd-pipeline-bootcamp-2023/



Python Project for Basics Data Analysis

https://courze.org/python-project-for
-basics-data-analysis/



Process Management: Value & Non-Value Add

https://courze.org/process-management-value-non-val
ue-add/



Professional Certificate of Executive Business Assistant

https://courze.org/professional-certificate-of-exec
utive-business-assistant/



Advanced RAG : Vector to Graph RAG LangChain Neo4j AutoGen

https://courze.org/learn-advanc
ed-rag-vector-to-graph-rag-wth-langchain-neo4j/



1350+ CompTIA Security+ SY0-701 Practice Tests Questions

https://cou
rze.org/1350-comptia-security-sy0-701-practice-tests-questions/



1500 CompTIA Network+ N10-008 , N10-009 Practice Test
s 2024

https://courze.org/1500-comptia-network-n10-008-n10-009-practice-tests-2024/



850+ CompTIA Pentest+ PT0-002 Pr
actice Tests Questions 2024

https://courze.org/850-comptia-pentest-pt0-002-practice-tests-questions-2024/



750+ CompT
IA DataSys+ DS0-001 Practice Tests Questions 2024

https://courze.org/750-comptia-datasys-ds0-001-practice-tests-questio
ns-2024/



600+ CompTIA CySA+ CS0-003 Practice Tests Questions – Exams

https://courze.org/600-comptia-cysa-cs0-003-pra
ctice-tests-questions-exams/



980+ CompTIA Project+ PK0-005 Practice Tests Questions

https://courze.org/980-comptia-p
roject-pk0-005-practice-tests-questions/



770+ CompTIA Cloud Essentials CLO-002 Practice Tests – Exams

https://courze
.org/770-comptia-cloud-essentials-clo-002-practice-tests-exams/



1200+ CompTIA CASP+ CAS-004 Practice Tests Questions 
– Exams

https://courze.org/1200-comptia-casp-cas-004-practice-tests-questions-exams/



1500 CompTIA A+ 220-1101 – 220-
1102 Practice Tests Questions

https://courze.org/1500-comptia-a-220-1101-220-1102-practice-tests-questions/



Professi
onal Certificate of Secretary

https://courze.org/professional-certificate-of-secretary/



Professional Certificate: Di
gital Business & Unit Economics

https://courze.org/professional-certificate-digital-business-unit-economics/



Ai Avat
ar Masterclass: How to create talking AI Avatar

https://courze.org/ai-avatar-masterclass-how-to-create-talking-ai-avata
r/



How To Trade Memecoin On Solana Using Telegram Bot

https://courze.org/how-to-trade-memecoin-on-solana-using-teleg
ram-bot/



How To Trade Meme Coin On Solana : Step By Step Guide

https://courze.org/how-to-trade-meme-coin-on-solana-s
tep-by-step-guide/



Meme Coin Mastery: How To Trade Solana Memecoin For Profit

https://courze.org/meme-coin-mastery-h
ow-to-trade-solana-memecoin-for-profit/



Professional Certificate in Procurement and Purchasing

https://courze.org/pr
ofessional-certificate-in-procurement-and-purchasing/



Product Owner Certification

https://courze.org/product-owner-c
ertification/



MS Word – Microsoft Word Course Beginner to Expert

https://courze.org/ms-word-microsoft-word-course-be
ginner-to-expert-2023/



Social Media Video Editing with Canva: From Beginner to Pro

https://courze.org/social-media-v
ideo-editing-with-canva-from-beginner-to-pro/



Essential Photoshop Course for Beginner to Advanced

https://courze.org
/essential-photoshop-course-for-beginner-to-advanced/



The Ultimate Filmora Video Editing Course: Beginner to Pro

htt
ps://courze.org/the-ultimate-filmora-video-editing-course-beginner-to-pro/




```
---

     
 
all -  [ Semantic chunking  ](https://www.reddit.com/r/LangChain/comments/1fzibfx/semantic_chunking/) , 2024-10-10-0912
```
Semantic chunking works well for me but the chunk sizes are big. As the chunk sizes are big am forced to use contextualc
ompressionretriver. 
What base compressor can be used here?
LLMChainExtractor works like a charm but is costly because o
f the chunk sizes.
Flashrerank compressor doesn't add anything.

If my idea is to reduce the cost and replace the llm ca
ll during contextual compressor, what would options do I have?

Dataset being used is Paul Graham essays from kaggle.
```
---

     
 
all -  [ Contextualizing chunks' metadata - use a JSON object or convert into plain language? ](https://www.reddit.com/r/LangChain/comments/1fzfdnm/contextualizing_chunks_metadata_use_a_json_object/) , 2024-10-10-0912
```
I'm developing a RAG application and associating different type of metadata to chunks based on their sources.

These chu
nks are being processed into a Langchain pipeline using OpenAI embedding models, OpenAI LLM, and Pinecone DB.

When I'm 
providing the most relevant chunks for RAG, I thought it'd be a good idea to include chunks' metadata in the context to 
provide a better understanding of where the text is being sourced from. But I'm not sure if converting this metadata (ra
w JSON objects) into normal sentences / plain language would improve the final outputted answer's accuracy. I'm also wei
ghing whether or not invoking OpenAI's LLM to create this plain language is worth the api costs.

Has anyone encountered
 this scenario before? Any relevant resources are appreciated.
```
---

     
 
all -  [ [2 YoE, Data Science, Data Analytics, United States] ](https://www.reddit.com/r/resumes/comments/1fzec5o/2_yoe_data_science_data_analytics_united_states/) , 2024-10-10-0912
```
Hi all,

I am an international in the US. I have been looking for Data Science/Data Analytics/Machine learning Engineer 
roles since February 2024. I have applied to almost 1000+ applications and got ZERO interviews. I have tailored my resum
e 40-50% of the times. There have been days when I spent a lot of time on tailoring to the job descriptions and sent out
 3-4 properly made applications. Other days, I have submitted 10-15 applications per day with minimal tailoring. I have 
used [jobright.ai](http://jobright.ai) for my application matching and most of them were above 75% matching. This is ver
y demotivating and I don't know what to do at this point.

I know my resume is long because the companies want a broad r
ange of skillset for DS roles. If I try to shorten it, then I miss out on the similarity score. Can you evaluate my resu
me and tell me what am I doing wrong in here? I will not mind if it comes to roasting my resume as long as it helps me g
et at least an interview.

Also, is the job market for Data Science roles saturated? Should I just drop the idea to beco
me a data scientist at this point?

https://preview.redd.it/spq2pnx9fmtd1.png?width=720&format=png&auto=webp&s=50719baff
edbd5cb64f46067bbc25bfc05923de8

https://preview.redd.it/rkqj8r5dfmtd1.png?width=712&format=png&auto=webp&s=f8b445f1a925
d0f2bf127526002b86bd28a0c7bf


```
---

     
 
all -  [ [0 YoE, Junior student, Software Engineer Intern, USA] ](https://www.reddit.com/r/resumes/comments/1fze8cc/0_yoe_junior_student_software_engineer_intern_usa/) , 2024-10-10-0912
```
I'm a Junior student in the U.S., seeking a SWE internship next summer 2025. I just got 1 interview so far, and many rej
ections after fully acing the OA, and many auto rejections. Is there something wrong with my resume? 

https://preview.r
edd.it/3xl8uu12emtd1.png?width=817&format=png&auto=webp&s=cc25fddfba21381512bc0c96a5c21c08f076a489


```
---

     
 
all -  [ 500+ applications, 1 interview so far, Am I cooked? ](https://www.reddit.com/r/leetcode/comments/1fze4xi/500_applications_1_interview_so_far_am_i_cooked/) , 2024-10-10-0912
```
I'm a Junior student in the U.S., seeking a SWE internship next summer 2025. I just got 1 interview so far, and many rej
ections after fully acing the OA, and many auto rejections. Is there something wrong with my resume? 

https://preview.r
edd.it/u6ke3ksbdmtd1.png?width=817&format=png&auto=webp&s=e86a195690dfb6e52bb10788003f8028b85fae48


```
---

     
 
all -  [ Chain reranking for RAG ](https://www.reddit.com/r/LangChain/comments/1fzdj70/chain_reranking_for_rag/) , 2024-10-10-0912
```
Hey everyone, I'm happy to share an exciting new capability for u/vectara we announced today - chain reranker. This allo
ws you to chain multiple rerankers within your Vectara RAG stack to gain even finer control over accuracy of your retrie
ver.  
Check out the details here: [https://vectara.com/blog/introducing-vectaras-chain-rerankers/](https://vectara.com/
blog/introducing-vectaras-chain-rerankers/)  
How to use Vectara with Langchain: [https://github.com/vectara/example-not
ebooks/blob/main/notebooks/using-vectara-with-langchain.ipynb](https://github.com/vectara/example-notebooks/blob/main/no
tebooks/using-vectara-with-langchain.ipynb)
```
---

     
 
all -  [ October 8, 2024 - 221 Free Development Udemy Courses ](https://www.reddit.com/r/udemyfreebies/comments/1fz6g0r/october_8_2024_221_free_development_udemy_courses/) , 2024-10-10-0912
```
1. PHP with MySQL: Build 8 PHP and MySQL Projects

6.5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/real-world-ph
p-projects



2. Machine Learning with TensorFlow on Google Cloud

6 h (Rating: 4.7/5)

https://www.easylearn.ing/course
/machine-learning-tensorflow-google-cloud



3. Zero to Hero in LangChain: Build GenAI apps using LangChain

5.5 h (Rati
ng: 4.7/5)

https://www.easylearn.ing/course/generative-ai-with-langchain



4. Python for Data Science: Python Programm
ing & Data Analysis

6 h (Rating: 4.4/5)

https://www.easylearn.ing/course/learn-python-data-analysis



5. Complete Mic
rosoft SQL Server from Scratch: Bootcamp

9 h (Rating: 4.3/5)

https://www.easylearn.ing/course/sql-server-training-cour
se



6. Complete Python from Scratch: Start your career in Python 3+

9 h (Rating: 4.2/5)

https://www.easylearn.ing/co
urse/python-3-tutorial



7. Excel Power Tools Master Formulas, Automation Data Analysis

4.5 h (Rating: 4.2/5)

https:/
/www.easylearn.ing/course/excel-power-user-course



8. Mastering GitHub Copilot's AI Assistance and AI-Powered Code

34
 min (Rating: 2.8/5)

https://www.easylearn.ing/course/github-copilot-mastery



9. The Complete Python and JavaScript c
ourse: Web Development

14 h (Rating: 4.4/5)

https://www.easylearn.ing/course/python-javascript-web-development



10. 
Learn Python from Scratch : Python Programming

8.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/python-full-stac
k-developer



11. SQL Masterclass: SQL for Data Analysis

6.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/postg
resql-masterclass



12. UNREAL ENGINE 5: Conviértete en desarrollador desde 0

22.5 h (Rating: 4.6/5)

https://www.easy
learn.ing/course/unreal-engine-5-mastery



13. JavaScript Coding Interview Questions \[with SOLUTIONS\]

41 min (Rating
: 0.0/5)

https://www.easylearn.ing/course/javascript-interview-questions-solved



14. DevOps CI/CD with Multi-Project 
and Troubleshooting

13 h (Rating: 3.5/5)

https://www.easylearn.ing/course/devops-cicd-course



15. The Complete Pytho
n Bootcamp From Zero to Master

12.5 h (Rating: 3.9/5)

https://www.easylearn.ing/course/python-data-science-machine-lea
rning-course



16. Wordpress Web Development for Absolute Beginner Zero to Hero

4.5 h (Rating: 4.2/5)

https://www.eas
ylearn.ing/course/wordpress-website-development-beginner



17. 19 Generative AI Real Time Projects End to End

7.5 h (R
ating: 0.0/5)

https://www.easylearn.ing/course/generative-ai-projects



18. API REST con PHP  y MYSQL

1.5 h (Rating: 
4.0/5)

https://www.easylearn.ing/course/api-rest-php-mysql



19. SQL for Everyone Transform Data into Insights

5 h (R
ating: 4.4/5)

https://www.easylearn.ing/course/sql-for-everyone



20. Full Stack Data Science & Machine Learning BootC
amp Course

34.5 h (Rating: 4.1/5)

https://www.easylearn.ing/course/data-science-bootcamp



21. Mastering Deep Learnin
g for Generative AI

4 h (Rating: 5.0/5)

https://www.easylearn.ing/course/generative-ai-deep-learning-course



22. Pyt
hon Powerhouse Gen AI From Basics to Advanced Programming

3 h (Rating: 5.0/5)

https://www.easylearn.ing/course/python-
generative-ai-course



23. Data Analysis and Business Intelligence with Python & SQL

10.5 h (Rating: 3.3/5)

https://w
ww.easylearn.ing/course/data-analysis-business-intelligence-python-sql



24. Unlock Your Data Superpowers Zero to Data 
Analyst Hero

16.5 h (Rating: 3.8/5)

https://www.easylearn.ing/course/data-analysis-training



25. Unlock Your Potenti
al: Exploring the Power of Chat GPT

31 min (Rating: 3.5/5)

https://www.easylearn.ing/course/chatgpt-conversational-ai-
course



26. Python for Absolute Beginners Learn Programming from scratch

2.5 h (Rating: 5.0/5)

https://www.easylearn
.ing/course/python-virtual-assistant-course



27. Building AI Projects Machine Learning & Deep Learning

3 h (Rating: 4
.8/5)

https://www.easylearn.ing/course/ai-projects-machine-learning-deep-learning



28. Applied Time Series Analysis a
nd Forecasting in Python

8.5 h (Rating: 4.8/5)

https://www.easylearn.ing/course/data-science-time-series



29. Advanc
ed DataBricks -Data Warehouse Performance Optimization

42 min (Rating: 2.9/5)

https://www.easylearn.ing/course/databri
cks-data-warehouse-optimization



30. Machine Learning A-Z From Foundations to Deployment

7.5 h (Rating: 4.0/5)

https
://www.easylearn.ing/course/machine-learning-a-z



31. Complete Machine Learning With Real-World Deployment

20.5 h (Ra
ting: 3.5/5)

https://www.easylearn.ing/course/deep-learning-course



32. Python Test Development:From the Ground Up to
 Advanced Level

Test Course (Rating: 4.1/5)

https://www.easylearn.ing/course/python-test-development-course



33. Ang
ular

3.5 h (Rating: 5.0/5)

https://www.easylearn.ing/course/angular-course-hindi



34. ChatBot de IA para Wordpress: 
Para Principiantes y Avanzados

2 h (Rating: 4.5/5)

https://www.easylearn.ing/course/chatbots-ia-wordpress



35. Codin
g for everybody: Full stack development course

21.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/coding-for-ever
yone-course



36. Learn Python + JavaScript + Microsoft SQL for Data science

22.5 h (Rating: 4.2/5)

https://www.easyl
earn.ing/course/python-javascript-sql-data-science-course



37. Fullstack web development : CSS JavaScript and PHP Mast
ery

17.5 h (Rating: 4.0/5)

https://www.easylearn.ing/course/css-javascript-php-mysql



38. PHP with MySQL: Build 7 PH
P and MySQL Projects

6 h (Rating: 4.2/5)

https://www.easylearn.ing/course/build-php-mysql-projects



39. Crear un eco
mmerce FULLSTACK PHP y MySQL - Tienda Online

40.5 h (Rating: 3.8/5)

https://www.easylearn.ing/course/ecommerce-develop
ment-php-mysql



40. The Expert’s Secret to Mobile Application Testing \[2024\]

3.5 h (Rating: 3.9/5)

https://www.eas
ylearn.ing/course/mobile-testing-training



41. Problem Solving with C programming language

6 h (Rating: 4.2/5)

https
://www.easylearn.ing/course/c-programming-problem-solving



42. JavaScript Fundamentals for Absolute Beginners

5.5 h (
Rating: 4.6/5)

https://www.easylearn.ing/course/javascript-basics-course



43. 600+ Design Patterns Interview Question
s Practice Test

Test Course (Rating: 0.0/5)

https://www.easylearn.ing/course/design-patterns-interview-questions



44
. 1400+ Deep Learning Interview Questions and Practice Tests

Test Course (Rating: 0.0/5)

https://www.easylearn.ing/cou
rse/deep-learning-interview-questions



45. \[NEW\] 1100+ Git Interview Questions and Practice Tests

Test Course (Rati
ng: 0.0/5)

https://www.easylearn.ing/course/git-interview-questions



46. Create Space Invaders with Python PyGame

33
 min (Rating: 3.9/5)

https://www.easylearn.ing/course/space-invaders-python



47. OOP Design Patterns in Python

1 h (
Rating: 3.4/5)

https://www.easylearn.ing/course/oop-design-patterns-python



48. Machine Learning Intro for Python Dev
elopers

44 min (Rating: 3.6/5)

https://www.easylearn.ing/course/machine-learning-python-beginner



49. \[New\] 1300+ 
Computer Vision Interview Practice Questions

Test Course (Rating: 0.0/5)

https://www.easylearn.ing/course/computer-vis
ion-interview-questions



50. 960+ Cryptography Interview Questions and Practice Tests

Test Course (Rating: 0.0/5)

ht
tps://www.easylearn.ing/course/cryptography-interview-questions



51. GitLab CI: Pipelines, CI/CD and DevOps for Beginn
ers

2 h (Rating: 4.2/5)

https://www.easylearn.ing/course/gitlab-ci-cd-devops



52. \[NEW\] 1500 Master SQL: Interview
 Questions - Practice Tests

Test Course (Rating: 0.0/5)

https://www.easylearn.ing/course/master-sql-interview-question
s



53. Python Web Development: Building Interactive Websites

19.5 h (Rating: 4.6/5)

https://www.easylearn.ing/course
/python-web-development-course



54. Tech Lead & Staff Engineer Survival Primer in 75 mins

1.5 h (Rating: 4.6/5)

http
s://www.easylearn.ing/course/tech-lead-mastery



55. PHP Webforms from Scratch Zero to Expert : Bootcamp

9.5 h (Rating
: 4.3/5)

https://www.easylearn.ing/course/php-webforms-bootcamp



56. The Full Stack Web Development 2024: Bootcamp

1
9.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/web-development-bootcamp-2024



57. Restful API Web Services wi
th PHP and MySQL: Bootcamp

5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/restful-api-php-mysql-bootcamp



58. 
Full Stack developer course for Web Applications: Bootcamp

15.5 h (Rating: 4.6/5)

https://www.easylearn.ing/course/htm
l-javascript-php-mysql-course



59. JavaScript Masterclass for Beginner to Expert: Bootcamp

6.5 h (Rating: 4.4/5)

htt
ps://www.easylearn.ing/course/javascript-bootcamp-beginner-expert



60. Asp .Net C# Programming with JS and HTML: Begin
ner to Expert

17 h (Rating: 4.7/5)

https://www.easylearn.ing/course/asp-net-c-web-development-masterclass



61. HTML 
CSS JavaScript Course for UI/UX Modern Web Developers

18 h (Rating: 4.5/5)

https://www.easylearn.ing/course/web-develo
pment-course-beginners



62. Full Stack Web Development Course 2024: Bootcamp

13 h (Rating: 4.2/5)

https://www.easyle
arn.ing/course/full-stack-web-development-bootcamp



63. Python programming with MySQL database: for Data Science

17 h
 (Rating: 4.7/5)

https://www.easylearn.ing/course/python-html-mysql-web-development-course



64. Learn Restful WEB API
, JavaScript and HTML: Web Services

12 h (Rating: 3.5/5)

https://www.easylearn.ing/course/restful-api-development-php-
mysql



65. Edge Computing : Master the Next Frontier of Computing

2 h (Rating: 3.8/5)

https://www.easylearn.ing/cour
se/edge-computing-mastery



66. Python PCAP: Certified Associate in Python Programming\[2024\]

Test Course (Rating: 4.
1/5)

https://www.easylearn.ing/course/python-practice-exams



67. MongoDB - The Complete MongoDB Developers Course

3.
5 h (Rating: 4.1/5)

https://www.easylearn.ing/course/learn-mongodb



68. Python Course for App Developers: Build Your 
First App

5.5 h (Rating: 4.6/5)

https://www.easylearn.ing/course/learn-python-for-mobile-apps



69. Learn C# Coding I
ntermediate: C# Classes, Methods and OOPs

5.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/learn-c-sharp-oop




70. Learn C# Coding Basics for Beginners: C# Fundamentals

7 h (Rating: 4.0/5)

https://www.easylearn.ing/course/learn-c
-sharp-programming-beginners



71. ChatGPT for Data Science and Machine Learning

3.5 h (Rating: 4.6/5)

https://www.ea
sylearn.ing/course/chatgpt-data-science-machine-learning



72. Master in Python Language Quickly Using the ChatGPT Open
 AI

2.5 h (Rating: 4.7/5)

https://www.easylearn.ing/course/python-programming-chatgpt



73. Learn to Code Your HTML W
ebsite: Coding for Kids & Beginners

3.5 h (Rating: 4.6/5)

https://www.easylearn.ing/course/html-css-for-kids



74. Ma
stering MYSQL: Database Creation, Management & SQL Queries

4.5 h (Rating: 3.9/5)

https://www.easylearn.ing/course/mysq
l-mastery-course



75. The Complete C Programming Course for Basic to Expert

2 h (Rating: 3.7/5)

https://www.easylear
n.ing/course/c-programming-course-beginner-expert



76. NumPy, SciPy, Matplotlib & Pandas A-Z: Machine Learning

6.5 h 
(Rating: 3.8/5)

https://www.easylearn.ing/course/python-data-science-libraries



77. SQL, MYSQL, POSTGRESQL & MONGODB:
 All-in-One Database Course

5.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/sql-mysql-postgresql-mongodb-course




78. Zero to Hero in Ollama: Create Local LLM Applications

3 h (Rating: 4.8/5)

https://www.easylearn.ing/course/oll
ama-local-llm-course



79. Next-Gen Web Development: JavaScript & AI Essentials

5 h (Rating: 4.8/5)

https://www.easyl
earn.ing/course/javascript-ai-web-development-course



80. Unity 3D : ( Game Development )- Basic to Professional Level


7.5 h (Rating: 5.0/5)

https://www.easylearn.ing/course/unity-3d-game-development-hindi



81. Build from Scratch a Mo
dern REST API with PHP 8

17.5 h (Rating: 4.1/5)

https://www.easylearn.ing/course/php-rest-api-development



82. Maste
r Java, Python, C & C++: All-in-One Programming Course

5 h (Rating: 3.6/5)

https://www.easylearn.ing/course/master-pro
gramming-course



83. Learn PHP Programming: Create Dynamic Websites with MYSQL

5.5 h (Rating: 3.9/5)

https://www.eas
ylearn.ing/course/dynamic-website-development



84. Curso de Laravel 9 desde cero + APIs RESTFULL

2 h (Rating: 4.0/5)


https://www.easylearn.ing/course/curso-laravel-9-cero-apis-restful



85. Firebase Database : CRUD Android App Developm
ent

2 h (Rating: 5.0/5)

https://www.easylearn.ing/course/firebase-database-android-hindi



86. C# : Basics to Profess
ional Level C Sharp Coding

3.5 h (Rating: 5.0/5)

https://www.easylearn.ing/course/build-cross-platform-apps-with-c-sha
rp



87. Python for Everyone Master the Basics of Programming

6.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/
master-python-basics



88. HTML Practice Test for Certification, Exams & Interviews

Test Course (Rating: 4.5/5)

https
://www.easylearn.ing/course/html-practice-test-certification



89. Medical Software Testing: Quality Assurance in Healt
hcare

2 h (Rating: 4.6/5)

https://www.easylearn.ing/course/medical-software-testing-course



90. Scrapy MASTERY Cours
e - Become a Python Web Scraping MACHINE

1.5 h (Rating: 4.7/5)

https://www.easylearn.ing/course/scrapy-mastery-course




91. Learn to Build HTML Responsive Real-world Modern Websites

6 h (Rating: 4.4/5)

https://www.easylearn.ing/course/
html-course



92. Building AI Saas Apps / AI Tools with \[No Code\] x ChatGPT

6 h (Rating: 3.8/5)

https://www.easylea
rn.ing/course/build-ai-saas-apps-no-code



93. Convert Websites into Mobile Apps (No coding)

3 h (Rating: 4.3/5)

http
s://www.easylearn.ing/course/no-code-app-builder



94. Mastering HTML5 and CSS3 (Part 2 - Intermediate  Level)

Test Co
urse (Rating: 4.2/5)

https://www.easylearn.ing/course/html5-css3-intermediate-course



95. Master Android Application 
Build 3 Applications from Scratch

Test Course (Rating: 4.7/5)

https://www.easylearn.ing/course/build-android-apps-from
-scratch



96. Python Programming Language | Master Python Course (Arabic)

6.5 h (Rating: 4.0/5)

https://www.easylear
n.ing/course/دورة-بايثون-مبتدئين



97. Problem Solving with C++ programming language

4 h (Rating: 4.1/5)

https://www.
easylearn.ing/course/c-plus-plus-problem-solving



98. C programming language | The Complete C Course (Arabic)

21.5 h 
(Rating: 3.5/5)

https://www.easylearn.ing/course/c-programming-course-arabic



99. Master in Software Architecture, En
gineering and Development

6.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/master-software-architecture-engineer
ing-development



100. Build Instagram clone - React TailwindCSS Firebase

8 h (Rating: 2.9/5)

https://www.easylearn.i
ng/course/build-instagram-clone-react-tailwindcss-firebase



101. Learn to Code HTML & CSS for Responsive Real-World We
bsites

12.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/learn-html-css-responsive-websites



102. 2024 Master 
class on Data Science using Python A-Z for ML

Test Course (Rating: 4.2/5)

https://www.easylearn.ing/course/python-data
-science-masterclass



103. 2024 C++ Programming : Beginners to Advanced for Developers

6 h (Rating: 4.1/5)

https://w
ww.easylearn.ing/course/hands-on-c-plus-plus-tutorial



104. Máster en WordPress y ChatGPT, ¡Desde Cero Hasta Experto!


9 h (Rating: 3.7/5)

https://www.easylearn.ing/course/curso-wordpress-chatgpt



105. Directorio de Plugins para WordPr
ess 2024

7 h (Rating: 4.6/5)

https://www.easylearn.ing/course/curso-plugins-wordpress-2024



106. Máster en Elementor
 2024, ¡Desde Cero Hasta Experto!

7.5 h (Rating: 4.7/5)

https://www.easylearn.ing/course/curso-elementor-wordpress




107. Cómo Crear una Página de Ventas Para Hotmart 2024

1 h (Rating: 4.2/5)

https://www.easylearn.ing/course/curso-hotm
art-wordpress-elementor



108. Máster en Diseño Web Para No Programadores 2024

13 h (Rating: 4.6/5)

https://www.easyl
earn.ing/course/curso-wordpress-sin-programacion



109. Elementor Hosting: Cómo Crear una Página Web con WordPress

1.5
 h (Rating: 4.0/5)

https://www.easylearn.ing/course/elementor-hosting-wordpress-curso



110. Cómo Crear una Página Web
 con Inteligencia Artificial 2024

1.5 h (Rating: 3.1/5)

https://www.easylearn.ing/course/crear-pagina-web-inteligencia
-artificial



111. All in One WP Migration: Migra tu Sitio Web de WordPress

35 min (Rating: 3.9/5)

https://www.easyle
arn.ing/course/migracion-wordpress-allinone



112. The Complete C & C++ Programming Course - Mastering  C & C++

4.5 h 
(Rating: 4.1/5)

https://www.easylearn.ing/course/c-plus-plus-course



113. JavaScript And PHP Programming Complete Cou
rse

5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/javascript-php-programming-course



114. Complete Java Progr
amming Bootcamp: Learn to Code in Java

4.5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/java-bootcamp



115. Ja
va Certification ( Java Oops feature )

3.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/java-programming-course-
hindi



116. Build, Host & Manage WordPress Websites using AI \[10Web\]

4.5 h (Rating: 4.1/5)

https://www.easylearn.i
ng/course/wordpress-website-design-with-ai



117. Java & Python Programming Mastery: Learn to Code Like a Pro

3 h (Rat
ing: 3.4/5)

https://www.easylearn.ing/course/learn-java-python-coding



118. Develop AI Apps, Automations & Chatbots \
[No-code  x ChatGPT\]

5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/no-code-ai-chatbot-development



119. Test
 Automation for Beginners \[Selenium-Cypress-Playwright\]

10.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/sele
nium-test-automation



120. Django Masterclass: Get Started With Django Web Development

5.5 h (Rating: 4.3/5)

https:/
/www.easylearn.ing/course/django-web-development-masterclass



121. Learn SQL in 3 Hours : A tutorial for fast learners


3 h (Rating: 4.2/5)

https://www.easylearn.ing/course/learn-sql-beginners-guide



122. Secure Your Wordpress Website 
For Beginners

1 h (Rating: 4.0/5)

https://www.easylearn.ing/course/wordpress-security-mastery



123. Java And C++ And
 PHP Crash Course All in One For Beginners

2.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/c-plus-plus-crash-co
urse



124. JavaScript 20 Projects In 20 Days HTML, CSS & JavaScript

Test Course (Rating: 4.3/5)

https://www.easylear
n.ing/course/javascript-projects-html-css



125. SQL for Data Engineers Designing and Building Data Pipelines

4 h (Rat
ing: 4.5/5)

https://www.easylearn.ing/course/sql-for-data-engineers



126. Master the Machine Muse Build Generative AI
 with ML

6.5 h (Rating: 3.5/5)

https://www.easylearn.ing/course/generative-ai-course



127. Build ML Projects on AWS 
Master SageMaker

1 h (Rating: 2.2/5)

https://www.easylearn.ing/course/aws-sagemaker-mastery



128. Applied Statistics
 Real World Problem Solving

3 h (Rating: 0.0/5)

https://www.easylearn.ing/course/applied-statistics-course



129. Enh
ancing Productivity through Google BARD and ChatGPT AI

1.5 h (Rating: 3.5/5)

https://www.easylearn.ing/course/google-b
ard-chatgpt-productivity-course



130. Mastering Power BI and Gen AI Integration for Analytics

3 h (Rating: 4.4/5)

ht
tps://www.easylearn.ing/course/power-bi-generative-ai-course



131. Mastering Microsoft Power BI: Unleashing Insights -
 AI/ML

3.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/master-power-bi



132. Chatbot Development Course: Buil
d AI Chatbots without Coding

2 h (Rating: 4.3/5)

https://www.easylearn.ing/course/ai-chatbot-development-course



133
. Chatbot Development Course: Build AI Chatbots without Coding

2 h (Rating: 4.3/5)

https://www.easylearn.ing/course/ai
-chatbot-course



134. Máster en Comercio Electrónico con WordPress 2024

4.5 h (Rating: 4.0/5)

https://www.easylearn.
ing/course/curso-comercio-electronico-wordpress



135. Cómo Crear un Blog con Inteligencia Artificial 2024

1 h (Rating
: 4.4/5)

https://www.easylearn.ing/course/crear-blog-inteligencia-artificial



136. Crea una Página Web con Elementor 
Pro y el Tema Hello 2024

1.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/curso-elementor-pro-hello-theme



137
. Cómo Crear un Embudo de Ventas con WordPress Desde Cero 2024

4 h (Rating: 3.9/5)

https://www.easylearn.ing/course/em
budo-ventas-wordpress



138. Cómo Crear un Blog con WordPress Para Principiantes 2024

4 h (Rating: 4.2/5)

https://www
.easylearn.ing/course/crear-blog-wordpress-principiantes



139. Augmented Reality Certification ( AR Foundation, Vufori
a )

2 h (Rating: 4.7/5)

https://www.easylearn.ing/course/augmented-reality-course-hindi



140. Create a WordPress web
site with Hostinger!

1.5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/wordpress-website-building-hostinger



14
1. Python Project: Build a PDF File Handling Tool from Scratch

1 h (Rating: 4.2/5)

https://www.easylearn.ing/course/py
thon-pdf-handling-course



142. Python Development Essentials

41 min (Rating: 4.1/5)

https://www.easylearn.ing/course
/python-development-essentials-course



143. Java And C++ Complete Course for Java And C++ Beginners

5.5 h (Rating: 4.
3/5)

https://www.easylearn.ing/course/java-c-programming-course



144. CSS, Bootstrap, JavaScript And PHP Stack Comple
te Course

8 h (Rating: 4.4/5)

https://www.easylearn.ing/course/complete-web-development-stack



145. Learn PHP and My
SQL for Web Application and Web Development

3.5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/php-mysql-web-devel
opment-course



146. CSS, Bootstrap ,JavaScript, PHP Full Stack Crash Course

4.5 h (Rating: 4.4/5)

https://www.easyle
arn.ing/course/css-bootstrap-javascript-php-course



147. Crea un MarketPlace Multi Vendedor con WordPress y Dokan

2 h
 (Rating: 5.0/5)

https://www.easylearn.ing/course/crear-marketplace-multivendedor-wordpress-dokan



148. Plugins de Wo
rdPress Para SiteGround

1.5 h (Rating: 5.0/5)

https://www.easylearn.ing/course/curso-plugins-wordpress-siteground



1
49. Universidad de Elementor Pro, ¡Desde Cero Hasta Experto!

5.5 h (Rating: 4.7/5)

https://www.easylearn.ing/course/cu
rso-elementor-pro-wordpress



150. WEB3 Token Gating. Create an NFT gated website from scratch

2 h (Rating: 4.7/5)

ht
tps://www.easylearn.ing/course/web3-token-gating



151. Python Development & Data Science: Variables and Data Types

1.
5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/python-variables-data-types



152. 2024 R Programming Bootcamp fo
r Absolute Beginners

1.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/r-programming-bootcamp



153. Data Scienc
e Career Path

1.5 h (Rating: 3.8/5)

https://www.easylearn.ing/course/data-science-career-path



154. Wordpress (No Co
ding), Domain not Needed, within 3.5 hours

3 h (Rating: 3.9/5)

https://www.easylearn.ing/course/wordpress-no-coding-we
bsite-3-5-hours



155. Security Optimizer: Protege tu Sitio Web en WordPress 2024

40 min (Rating: 4.3/5)

https://www.
easylearn.ing/course/wordpress-security-optimizer



156. Elementor IA: Crea una Web con WordPress y Elementor 2024

1.5
 h (Rating: 4.5/5)

https://www.easylearn.ing/course/curso-elementor-ia-wordpress



157. Python for Data Science & Mach
ine Learning: Zero to Hero

6 h (Rating: 4.3/5)

https://www.easylearn.ing/course/data-science-course-python-zero-to-her
o



158. MySQL for Beginners:  A Complete Training for beginnners

2.5 h (Rating: 4.2/5)

https://www.easylearn.ing/cou
rse/mysql-beginner-course



159. JavaScript for Beginners: The Complete Course for Beginners

4.5 h (Rating: 4.1/5)

ht
tps://www.easylearn.ing/course/javascript-for-beginners



160. HTML5 & CSS3 Complete Course: Build Websites like a Pro


4.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/html5-css3-course



161. The Complete Microsoft SQL Server Cou
rse: From A to Z

3 h (Rating: 4.3/5)

https://www.easylearn.ing/course/microsoft-sql-server-course



162. The Complete
 Vue.JS Course for Beginners: Zero to Mastery

4 h (Rating: 3.6/5)

https://www.easylearn.ing/course/vuejs-course-beginn
ers



163. C, C++, PHP & Java: Complete Guide to Modern Programming

5 h (Rating: 4.2/5)

https://www.easylearn.ing/cou
rse/master-c-cpp-php-java-programming



164. Advanced Wordpress Course for Professionals

7.5 h (Rating: 4.3/5)

https:
//www.easylearn.ing/course/wordpress-professional-course



165. Cómo Crear una Academia Online con WordPress y Tutor LM
S

2.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/crear-academia-online-wordpress-tutor-lms



166. Máster en D
iseño Web con Inteligencia Artificial 2024

2.5 h (Rating: 3.6/5)

https://www.easylearn.ing/course/curso-diseno-web-int
eligencia-artificial



167. Elementor Kits: Crea una Página Web con Elementor Pro 2024

1.5 h (Rating: 4.0/5)

https://
www.easylearn.ing/course/elementor-kits-crear-paginas-web-profesionales



168. Cómo Crear una Tienda Online con Intelig
encia Artificial

2 h (Rating: 4.9/5)

https://www.easylearn.ing/course/crear-tienda-online-inteligencia-artificial



1
69. Cómo Crear una Página Web Para Amazon Afiliados 2024

2 h (Rating: 4.2/5)

https://www.easylearn.ing/course/curso-am
azon-afiliados



170. Selenium Webdriver with Java & TestNG Testing Framework

11 h (Rating: 4.8/5)

https://www.easyle
arn.ing/course/automation-testing-selenium-testng



171. Python Data Structures & Algorithms: Ace Coding Interviews

6 
h (Rating: 4.5/5)

https://www.easylearn.ing/course/data-structures-algorithms-python-coding-interview



172. Crea tus 
propios juegos con HTML Y CANVAS JAVASCRIPT

9.5 h (Rating: 4.6/5)

https://www.easylearn.ing/course/curso-juegos-javasc
ript



173. Python & Java: Master Backend & Frontend Web Developments

3.5 h (Rating: 4.4/5)

https://www.easylearn.ing
/course/python-java-full-stack-developer



174. Build a User Web App from Scratch with Vanilla PHP 8+

18.5 h (Rating: 
4.5/5)

https://www.easylearn.ing/course/build-web-app-php-scratch



175. Flutter REST Movie App: Master Flutter REST A
PI Development

3.5 h (Rating: 4.3/5)

https://www.easylearn.ing/course/flutter-rest-api-course



176. Python & Django 
REST API Bootcamp - Build A Python Web API

8 h (Rating: 4.3/5)

https://www.easylearn.ing/course/build-rest-apis-with-p
ython



177. Flutter & Firebase Chat App: Master Flutter and Firebase

10 h (Rating: 4.5/5)

https://www.easylearn.ing/
course/build-chat-app-flutter-firebase



178. Python And Django Framework And HTML 5 Stack Complete Course

11.5 h (Rat
ing: 4.4/5)

https://www.easylearn.ing/course/python-django-html5-full-stack-course



179. Learn Machine Learning Cours
e with Python A to Z

2 h (Rating: 4.1/5)

https://www.easylearn.ing/course/machine-learning-python-course



180. JavaS
cript From Scratch ( Part 1 - Beginner Level)

4.5 h (Rating: 3.4/5)

https://www.easylearn.ing/course/javascript-beginn
er-course



181. Python Programming for Beginners: Learn Python from Scratch

6 h (Rating: 4.4/5)

https://www.easylear
n.ing/course/python-for-data-analysis



182. Master Git and Github - Beginner to Expert

4 h (Rating: 4.7/5)

https://w
ww.easylearn.ing/course/git-github-beginner-expert



183. SQL практикум для начинающих и продолжающих

12 h (Rating: 5.
0/5)

https://www.easylearn.ing/course/kurs-sql-dlya-nachinayushchih



184. Build, Train & Sell AI Chatbots \[No-code x
 Chat GPT\]

2.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/ai-chatbot-mastery



185. Create & Sell Online Cou
rses using WordPress LMS

3 h (Rating: 4.3/5)

https://www.easylearn.ing/course/wordpress-lms-course-creation



186. Ja
va And PHP Complete Course For Java And PHP Beginners

7 h (Rating: 4.6/5)

https://www.easylearn.ing/course/java-and-ph
p-complete-course



187. Python for Data Science in Hindi (हिंदी)

6.5 h (Rating: 4.5/5)

https://www.easylearn.ing/cou
rse/python-for-data-science-hindi



188. 4 Latest Practice Tests for any C++ Certification (2024)

Test Course (Rating:
 4.7/5)

https://www.easylearn.ing/course/c-plus-plus-certification-preparation



189. Prometheus MasterClass: Infra Mo
nitoring & Alerting

13 h (Rating: 4.5/5)

https://www.easylearn.ing/course/prometheus-masterclass



190. Python Certif
ication Preparation:4 Practice Tests

Test Course (Rating: 4.4/5)

https://www.easylearn.ing/course/python-certification
-prep



191. C++ Complete Training Course for C++ Beginners All In One

1.5 h (Rating: 3.6/5)

https://www.easylearn.in
g/course/complete-c-plus-plus-training



192. Excel Certification Exam Preparation: 4 Practice Tests 2024

Test Course 
(Rating: 4.2/5)

https://www.easylearn.ing/course/excel-certification-exam-prep



193. Mastering JavaScript:  ES6, ES7 
and  ES8 (2024)

4.5 h (Rating: 4.2/5)

https://www.easylearn.ing/course/learn-es6-javascript



194. Understanding Type
Script For Beginner To Advanced

3.5 h (Rating: 3.1/5)

https://www.easylearn.ing/course/typescript-course-beginner-adva
nced



195. Automated Machine Learning for Beginners (Google & Apple)

3 h (Rating: 4.3/5)

https://www.easylearn.ing/c
ourse/automated-machine-learning-beginners



196. PHP with MySQL: Build Complete Tours and Travel Website

7.5 h (Ratin
g: 4.0/5)

https://www.easylearn.ing/course/php-mysql-tours-travel-website



197. Complete JavaScript Programming: From
 Novice to Expert

3.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/comprehensive-javascript-training



198. Bui
ld a Backend REST API with Node JS from Scratch

12 h (Rating: 3.9/5)

https://www.easylearn.ing/course/node-js-backend-
api-development



199. Python Programming Masterclass

2.5 h (Rating: 4.1/5)

https://www.easylearn.ing/course/learn-py
thon-online-course



200. Complete Kubernetes: Easy & Practical Guide + Project

13 h (Rating: 4.7/5)

https://www.easy
learn.ing/course/kubernetes-course-beginners



201. ChatGPT Masterclass: A Complete ChatGPT Zero to Hero!

3 h (Rating:
 4.5/5)

https://www.easylearn.ing/course/chatgpt-mastery-course



202. ML for Business Managers: Build Regression mode
l in R Studio

Test Course (Rating: 4.1/5)

https://www.easylearn.ing/course/linear-regression-r-studio-business-manager
s



203. Google Cloud Professional Cloud Architect: GCP Certification

22 h (Rating: 4.4/5)

https://www.easylearn.ing/
course/gcp-certification-course



204. PHP for Beginners: PDO Crash Course

3 h (Rating: 4.2/5)

https://www.easylearn.
ing/course/php-pdo-crash-course



205. Logistic Regression in R Studio

6 h (Rating: 3.8/5)

https://www.easylearn.ing/
course/logistic-regression-r-studio



206. Master HTML and CSS by building real world projects

16 h (Rating: 4.7/5)

h
ttps://www.easylearn.ing/course/responsive-web-design



207. HTML and CSS for Beginners From Basic to Advance

4.5 h (R
ating: 4.3/5)

https://www.easylearn.ing/course/html-css-beginner-web-development



208. Machine Learning From Basic to
 Advanced

3 h (Rating: 3.7/5)

https://www.easylearn.ing/course/machine-learning-beginner-advanced



209. Logistic Reg
ression in Python

7.5 h (Rating: 4.5/5)

https://www.easylearn.ing/course/logistic-regression-python-beginner



210. P
HP for Beginners: The Complete PHP MySQL PDO Course

9.5 h (Rating: 4.4/5)

https://www.easylearn.ing/course/php-mysql-p
do-course



211. Dart & Flutter | The Complete Flutter Development Course

19 h (Rating: 4.5/5)

https://www.easylearn.
ing/course/flutter-development-course



212. The Ultimate MySQL Crash Course

3 h (Rating: 3.9/5)

https://www.easylear
n.ing/course/learn-mysql-fast



213. Flutter Advanced Course - Clean Architecture With MVVM

20.5 h (Rating: 4.3/5)

ht
tps://www.easylearn.ing/course/flutter-clean-architecture-mvvm-course



214. Complete Linear Regression Analysis in Pyt
hon

7.5 h (Rating: 4.7/5)

https://www.easylearn.ing/course/linear-regression-python-course



215. CSS3 and Bootstrap 
for Absolute Beginners : 4 courses in 1

3 h (Rating: 4.4/5)

https://www.easylearn.ing/course/css3-bootstrap-beginner-c
ourse



216. CSS Complete Course For Beginners

2 h (Rating: 4.2/5)

https://www.easylearn.ing/course/learn-css-online




217. API Crash Course: How to Create, Test, & Document your APIs

3.5 h (Rating: 4.3/5)

https://www.easylearn.ing/co
urse/learn-apis



218. Practical Web Design & Development: 7 Courses in 1

5.5 h (Rating: 4.5/5)

https://www.easylearn
.ing/course/web-design-development-course



219. The Complete Introduction to C++ Programming

5 h (Rating: 4.3/5)

htt
ps://www.easylearn.ing/course/beginner-c-plus-plus-course



220. Java Data Structures and Algorithms Masterclass

Test 
Course (Rating: 4.5/5)

https://www.easylearn.ing/course/java-data-structures-algorithms-masterclass



221. Selenium We
bdriver Automation Testing \[Live Projects 2024\]

70.5 h (Rating: 4.6/5)

[https://www.easylearn.ing/course/selenium-we
bdriver-automation-testing](https://www.easylearn.ing/course/selenium-webdriver-automation-testing)


```
---

     
 
all -  [ Stream structured output from graph ](https://www.reddit.com/r/LangChain/comments/1fz4bdc/stream_structured_output_from_graph/) , 2024-10-10-0912
```
Is it possible to stream structured output from a LangGraph graph? I want to produce an output similar to [this](https:/
/python.langchain.com/docs/how_to/structured_output/#streaming). I tried following this [tutorial](https://langchain-ai.
github.io/langgraph/how-tos/streaming-tokens/#streaming-llm-tokens) on streaming LLM tokens but am unsuccessful so far. 
In the below code, everything runs fine until the entire response is returned from the LLM, after which I get this error
:   


    ValueError: Message dict must contain 'role' and 'content' keys, got {'setup': 'Why don't scientists trust at
oms?', 'punchline': 'Because they make up everything!', 'rating': 8}

I can bypass this error by converting the LLM resp
onse to a string in `call_model`, but that defeats the purpose of getting structured output.

Here is my code:

    impo
rt getpass
    import os
    from typing import Optional, Literal
    from typing_extensions import Annotated, TypedDict

    
    from langchain_openai import ChatOpenAI
    from langgraph.graph import StateGraph, MessagesState, START, END

    from langgraph.graph.message import add_messages
    from langchain_core.runnables import RunnableConfig
    
    
 
   os.environ['OPENAI_API_KEY'] = getpass.getpass()
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    # TypedDict
    c
lass Joke(TypedDict):
        '''Joke to tell user.'''
    
        setup: Annotated[str, ..., 'The setup of the joke']

        punchline: Annotated[str, ..., 'The punchline of the joke']
        rating: Annotated[Optional[int], None, 'How 
funny the joke is, from 1 to 10']
    
    structured_llm = llm.with_structured_output(Joke)
    
    class State(TypedD
ict):
        messages: Annotated[list, add_messages]
    
    
    # Define the function that calls the model
    async
 def call_model(state: State, config: RunnableConfig):
        messages = state['messages']
        # Note: Passing the 
config through explicitly is required for python < 3.11
        # Since context var support wasn't added before then: ht
tps://docs.python.org/3/library/asyncio-task.html#creating-tasks
        response = await structured_llm.ainvoke(message
s, config)
        # We return a list, because this will get added to the existing list
        return {'messages': resp
onse}
    
    # Define a new graph
    workflow = StateGraph(State)
    # Define the two nodes we will cycle between
  
  workflow.add_node('agent', call_model)
    # Set the entrypoint as `agent`
    workflow.add_edge(START, 'agent')
    a
pp = workflow.compile()
    
    config = {'configurable': {'thread_id': '3'}}
    node_to_stream = 'agent'
    
    inp
uts = [HumanMessage(content='tell me a joke')]
    
    async for event in app.astream_events(
        {'messages': inpu
ts}, config, version='v2'
    ):
    
        # Get chat model tokens from a particular node
        if (
            ev
ent['event'] == 'on_chat_model_stream'
            and event['metadata'].get('langgraph_node', '') == node_to_stream
   
     ):
            print(event['data'])
```
---

     
 
all -  [ Agent Logging in choosing Tool ](https://www.reddit.com/r/LangChain/comments/1fz4adz/agent_logging_in_choosing_tool/) , 2024-10-10-0912
```
Hi,

I am trying to implement an internal assistant use case on top of GCP, so far we have had success with doing a redi
s cache paired with e vertex ai vector search vector store for exact matching and semantic handling and if this fails go
ing to a RAG.

  
However I am looking for the option to do the semantic matcing as a part of the RAG, I looked into the
 way tools work in Langchain and I cannot fully understand whether this is possible.

Basically what I want to do is use
 2 retrievers - one would have my structured QnA data - first look for response in this retriever and if there is respon
se - retrieve that, if there is no response - go to the second retriever which has the documentation and do retrieval an
d answer. 

  
Of course at some points I might have more retrievers and depending on the question to route between retr
ievers but this seems failry doable with Agent tools in langchain.

Can you point me in the right direction, I feel like
 this could be probably be solved with LangGraph but honestly have not done anything on it and it looks a bit more compl
ex.

Thanks!
```
---

     
 
all -  [ [2 YoE, AI graduate student, AI/ML engineer or researcher, United States] ](https://i.redd.it/0j5vgusxjjtd1.jpeg) , 2024-10-10-0912
```
I’m looking for a AI/ML engineer & AI researcher role, preferably remote and hybrid in Boston, Texas and SF. Any feedbac
k would be greatly appreciated, thanks! 
```
---

     
 
all -  [ Exploring RAG with LangChain ](https://www.reddit.com/r/Rag/comments/1fyxe0v/exploring_rag_with_langchain/) , 2024-10-10-0912
```
Hey Folks!

We’ve just launched an integration that makes it easier to add Retrieval-Augmented Generation (RAG) to your 
LangChain apps. It’s designed to improve data retrieval and help make responses more accurate, especially in apps where 
you need reliable, up-to-date information. You can also connect documents from multiple sources like Gmail, Notion, Goog
le Drive, etc.

If you’re exploring ways to use RAG, this might save you some time. We’re working on [Ragie](https://rag
ie.ai/), a fully managed RAG-as-a-Service platform for developers.  
  
Here’s the docs if you’re interested: [https://d
ocs.ragie.ai/docs/langchain-ragie](https://docs.ragie.ai/docs/langchain-ragie)  
We’d love to hear feedback or ideas fro
m the community :)
```
---

     
 
all -  [ New LangChain Integration for Easier RAG Implementation ](https://www.reddit.com/r/LangChain/comments/1fywubo/new_langchain_integration_for_easier_rag/) , 2024-10-10-0912
```
Hey everyone,  
  
We’ve just launched an integration that makes it easier to add Retrieval-Augmented Generation (RAG) t
o your LangChain apps. It’s designed to improve data retrieval and help make responses more accurate, especially in apps
 where you need reliable, up-to-date information.

If you’re exploring ways to use RAG, this might save you some time. Y
ou can also connect documents from multiple sources like Gmail, Notion, Google Drive, etc. We’re working on [Ragie](http
s://ragie.ai), a fully managed RAG-as-a-Service platform for developers, and we’d love to hear feedback or ideas from th
e community.

Here’s the docs if you’re interested: [https://docs.ragie.ai/docs/langchain-ragie](https://docs.ragie.ai/d
ocs/langchain-ragie)
```
---

     
 
all -  [ How to get langchain stream data without logs? ](https://www.reddit.com/r/LangChain/comments/1fywf5i/how_to_get_langchain_stream_data_without_logs/) , 2024-10-10-0912
```
 am using langchain and cohere. It works fine whenever i used `invoke` with agent executor, but whenever i moved for str
eaming and using `astream_events` i got extra data along with the response. Following is my sample code and response.

 
   agent_executor = AgentExecutor(agent=agent, tools=[search_1, search_2], verbose=True)
                
        # Get 
Response
        async for event in agent_executor.astream_events({
                    'preamble': session_data['initia
l_prompt'],
            }, version='v2'):
            if event['event'] == 'on_chat_model_stream':
                chunk
_content = serialize_aimessagechunk(event['data']['chunk'])
                chunk_content_html = chunk_content.replace('
\n', '<br>')
                yield f'data: {json.dumps({'event': 'stream', 'data': chunk_content_html})}\n\n'
          
 
    

and response:

    Plan: I will greet the user and ask for their name and location, then tailor my response acco
rdingly. Action: ```json [
        {
            'tool_name': 'directly_answer',
            'parameters': {}
        } 
] ``` Relevant Documents: None Cited Documents: None Answer: Hi! It's lovely to hear from you. What's your name, and are
 you based in Australia or New Zealand? Grounded answer: Hi! It's lovely to hear from you. What's your name, and are you
 based in Australia or New Zealand?
    

I need only an Answer or Grounded answer.
```
---

     
 
all -  [ Gemini 1.5 Pro 002 model API Memory Problem ](https://www.reddit.com/r/u_CurseofDarkness66/comments/1fyunw5/gemini_15_pro_002_model_api_memory_problem/) , 2024-10-10-0912
```
I am actually creating custom code for integrating GoogleGenerativeAI and Langchain - Retrieval chains but I am facing p
roblem during chaining . I am passing Image as well as Question and Answer Content . I am storing in List as a previous 
response and at next chain it updates and store . But after two response Quota Exceeds. I have even tried with Conversat
ionBuffer from Langchain for Memory but same problem. I think Image is creating problem but I don't know how to proceed 
further with this -   Code -

    import os
    from PIL import Image
    from langchain_core.prompts import ChatPromptT
emplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_google_genai import ChatGoogleG
enerativeAI
    from langchain_core.runnables import RunnablePassthrough, RunnableLambda
    import google.generativeai 
as genai
    from IPython.display import display, Markdown
    
    # Set up the Google API key environment variable
   
 os.environ['GOOGLE_API_KEY'] = API_KEY
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    
    # Define the 
language model
    llm = ChatGoogleGenerativeAI(
        model='models/gemini-1.5-flash-002',
        generation_config=
genai.GenerationConfig(temperature=1, max_output_tokens=10000),
    )
    
    
    class State:
        def __init__(se
lf):
            self.previous_data = []
    
        def update(self, result, question):
            self.previous_data
.append({'question': question, 'answer': result})
            if len(self.previous_data) > 3:
                self.previ
ous_data = self.previous_data[-3:]
    
    
    state = State()
    
    # Define the prompt template
    template = ''
'You are a UI/UX chatbot. I will ask you questions. Please provide detailed and accurate answers. If you don't know the 
answer, don't give a response.
    Context: {context}
    Question: {question}
    Answer based on the context provided.

    '''
    
    # Retrieve the previous context from the state
    def retrieve_context(_):
        context_str = '\n'
.join(
            [
                f'Q: {entry['question']} A: {entry['answer']}'
                for entry in state.p
revious_data
            ]
        )
        return context_str if context_str else 'No previous context.'
    
    
   
 retriever = RunnableLambda(retrieve_context)
    
    # Retrieval chain logic
    retrieval_chain = (
        {'context
': retriever, 'question': RunnablePassthrough()}
        | ChatPromptTemplate.from_template(template)
        | llm
    
    | StrOutputParser()
    )
    
    # Analyze image and get relevant content (with file upload)
    def analyze_image
(question, image_path):
        uploaded_file = genai.upload_file(
            path=image_path, display_name='Image for 
UI analysis'
        )
        model = genai.GenerativeModel('models/gemini-1.5-pro-002')
        generation_config = ge
nai.GenerationConfig(temperature=1, max_output_tokens=8192)
        response = model.generate_content(
            [ques
tion, uploaded_file], generation_config=generation_config
        )
        print(response.usage_metadata)
        retur
n response.text
    
    
    def get_result(question):
        question_text = ''
    
        if (
            isinsta
nce(question, list)
            and len(question) == 2
            and isinstance(question[1], str)
        ):
         
   question_text = question[0]
            image_path = question[1]
    
            image_analysis = analyze_image(ques
tion_text, image_path)
            state.update(result=image_analysis, question=question_text)
    
            return i
mage_analysis
    
        else:
            question_text = question
            context = retrieve_context(None)
    

            output = retrieval_chain.invoke(
                {
                    'context': context,
                 
   'question': question_text,
                }
            )
    
            state.update(result=output, question=ques
tion_text)
    
            return output
    
    img_path = 'lol.png' (Image is of Desktop Size around (1920 x 1080 px
))
    question = 'What are UI elements present in the Image. Show its location, color, style and its description sectio
n-wise from image'
    
    result = get_result([question, img_path])
    
    display(Markdown(result))
```
---

     
 
all -  [ Confused about unit-testing ](https://www.reddit.com/r/LangChain/comments/1fyolo3/confused_about_unittesting/) , 2024-10-10-0912
```
Does anyone has a framework to testing LLM applications? Im looking for a way of testing LangGraph apps as Im starting a
 new project and I need a quick way of running unit tests (as you would do with jest or mocka) but Im confused..

The un
it-testing are not really unit-testing? Because they rely on internet connection... because I need an LLM to evaluate th
e llm calls right?

I saw DeepEval for this... is this the right tool? When I read the docs I did not get why it calls a
n external llm to do the tests... Is there any other framework?  
I just want a way to run a script, fast, same as with 
pytest and get coverage,

Any ideas?
```
---

     
 
all -  [ open sourced parsers for pdf containing mathematical equations ](https://www.reddit.com/r/LangChain/comments/1fynscu/open_sourced_parsers_for_pdf_containing/) , 2024-10-10-0912
```
as the title says I am looking for the parsers for extracting the mathematical expressions from it. Any suggestions or r
ecommendations would be really helpful!
```
---

     
 
all -  [ PgVector Vs Azure AI search Vs Pinecone Vs Weaviate  ](https://www.reddit.com/r/LangChain/comments/1fyk42u/pgvector_vs_azure_ai_search_vs_pinecone_vs/) , 2024-10-10-0912
```
Anyone have any idea on these ? And which one you would recommend ? 
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1fyjcpk/list_of_free_and_best_selling_discounted_courses/) , 2024-10-10-0912
```
# Udemy Free Courses for 07 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17789/)Create An Animated Landing Page by HTML, C
SS and JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17788/)Business Development, Sales & Marketing Pro
fessional Diploma
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17787/)Javascript and PHP : Ultimate Course For Be
ginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17786/)Ultimate AWS Certified Solutions Architect Associate 
(SAA)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17785/)Curso de Facebook para Negocios 2024 – Facebook Marketi
ng
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17784/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hasta Expert
o!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17783/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17782/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto!
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/17781/)Curso Completo de Hacking Ético – Aprende Todo – 2024
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17780/)Complete C# Programming Master Class
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/17779/)The Ultimate MySQL Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17778/)Blender
 Essential: From Beginner to 3D Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17777/)The Complete T-Sh
irt Design Toolkit: PS, AI & Canva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17776/)Microsoft Office Mastery L
earn Word Excel and PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17775/)Ultimate Guide to Canva T-Shir
t Design: Mastery in T-Shirt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17774/)Certified in Cybersecurity (CC) 
Practice Questions 2024
* Microsoft Word Mastery: Essential Skill for Job and Business
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/17773/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17772/)The Complete Da Vinci Resolve Cours
e: Beginner to Filmmaker
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17771/)AZ-700:Designing and Implementing Az
ure Networking Solutions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17770/)CEH v12 Certification Practice Quest
ions 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17769/)AZ-900: Microsoft Azure Fundamentals Practice Quest
ions 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17768/)YouTube “The Blueprint” How I made over 100k in Jus
t 2 years
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17767/)Adobe Dreamweaver Mastery: Basics to Advanced Site 
Creation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17766/)Effective Delegation in Management: Boost Leadership
 Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17765/)Complete Ethical Hacking Course 2024 : Go From Zero t
o Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17764/)Entrepreneurship and Business Essentials
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17763/)Comprehensive PrestaShop Training
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/17762/)JavaScript Masterclass for Beginner to Expert: Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17761/)HTML CSS JavaScript Course for UI/UX Modern Web Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/17760/)Learn Python from Scratch : Python Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17759/)50
0+ SAS Interview Questions Practice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17758/)Learn C# Coding Basi
cs for Beginners: C# Fundamentals
* Full Stack developer course for Web Applications: Bootcamp
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/17757/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17756/)Full Stack Web Development 
Course 2024: Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17755/)Learn to Code Your HTML Website: Coding
 for Kids & Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17754/)Learn to Code HTML & CSS for Responsive
 Real-World Websites
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17753/)Learn C# Coding Intermediate: C# Classes
, Methods and OOPs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17752/)Excel Power Tools Master Formulas, Automat
ion Data Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17751/)Mastering GitHub Copilot’s AI Assistance an
d AI-Powered Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17750/)Criminology and Criminal Psychology | Certi
fied CSI+ Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17749/)Logistic Regression in R Studio
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/17748/)Agile Trainer Certification
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17747/)Entrepreneurship: Ideas, Market Analysis, Competitors, Place
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17746/)Marketing Analytics: Forecasting Models with Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/177
45/)Data Visualization in Excel: All Excel Charts and Graphs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17744/)
Complete Linear Regression Analysis in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17743/)Mastering ChatG
PT: All ChatGPT Features and Functions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17742/)Python for Data Scienc
e: Python Programming & Data Analysis
* ML for Business Managers: Build Regression model in R Studio
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/17741/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17740/)QuickBooks Online Pay
ments – Getting Paid Faster & Easier
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17739/)SQL Masterclass: SQL for
 Data Analytics
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17738/)Bell Curve
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/17737/)Marketing Analytics: Pricing Strategies and Price Analytics
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/17736/)Guitar Music Theory in Excel-Scales, Intervals, Modes & More
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/17735/)Microsoft Excel Weekender Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17734
/)Logistic Regression in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17733/)Zero to Hero in LangChain: Bu
ild GenAI apps using LangChain
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17732/)Microsoft Office सीखें: Excel,
 PowerPoint & Word in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17731/)HR People Analytics
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17730/)Microsoft Word in Hindi: हिंदी में सीखें MS Word
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/17729/)Chatbot
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17728/)Side Hustle Mastery
: 32 Ways to Earn Extra Income Online
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17727/)Level Up Your UI/UX: In
teractive Design & Prototyping Figma
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17726/)ChatGPT in Hindi: हिंदी 
में Complete ChatGPT guide
* Visual Guitar Mastery
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/17725/)
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/17724/)Python for Data Science in Hindi (हिंदी)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/17723/)Machine Learning with TensorFlow on Google Cloud
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17722/)ChatGPT for Office Productivity: Use AI for 10X Productivity
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17721/)Professional Diploma in Business Models Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/17720/)XK0-004: CompTIA Linux+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17719/)SK0-004: C
ompTIA Server+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17718/)PT0-003: CompTIA PenTest+ P
ractice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17717/)PT0-001: CompTIA PenTest+ Practice test 202
4
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17716/)Valor temporal del dinero y presupuesto de capital
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/17715/)Einstieg Excel Visual-Basic (VBA) für Controller
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/17714/)Marketing Strategy Development: Stand Out From the Crowd
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/17713/)Quiz Marketing Power: Generate Leads for Marketing Success
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/17712/)Discover Google Gemini for Marketing Success
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17711/)Link building. Build links that boost the site traffic!
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/17710/)ChatGPT for Mastering Compelling Content

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https
://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1fyjchx/list_of_free_and_best_selling_discounted_courses/) , 2024-10-10-0912
```
# Udemy Free Courses for 07 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17789/)Create An Animated Landing Page by HTML, C
SS and JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17788/)Business Development, Sales & Marketing Pro
fessional Diploma
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17787/)Javascript and PHP : Ultimate Course For Be
ginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17786/)Ultimate AWS Certified Solutions Architect Associate 
(SAA)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17785/)Curso de Facebook para Negocios 2024 – Facebook Marketi
ng
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17784/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hasta Expert
o!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17783/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17782/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto!
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/17781/)Curso Completo de Hacking Ético – Aprende Todo – 2024
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17780/)Complete C# Programming Master Class
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/17779/)The Ultimate MySQL Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17778/)Blender
 Essential: From Beginner to 3D Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17777/)The Complete T-Sh
irt Design Toolkit: PS, AI & Canva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17776/)Microsoft Office Mastery L
earn Word Excel and PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17775/)Ultimate Guide to Canva T-Shir
t Design: Mastery in T-Shirt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17774/)Certified in Cybersecurity (CC) 
Practice Questions 2024
* Microsoft Word Mastery: Essential Skill for Job and Business
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/17773/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17772/)The Complete Da Vinci Resolve Cours
e: Beginner to Filmmaker
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17771/)AZ-700:Designing and Implementing Az
ure Networking Solutions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17770/)CEH v12 Certification Practice Quest
ions 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17769/)AZ-900: Microsoft Azure Fundamentals Practice Quest
ions 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17768/)YouTube “The Blueprint” How I made over 100k in Jus
t 2 years
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17767/)Adobe Dreamweaver Mastery: Basics to Advanced Site 
Creation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17766/)Effective Delegation in Management: Boost Leadership
 Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17765/)Complete Ethical Hacking Course 2024 : Go From Zero t
o Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17764/)Entrepreneurship and Business Essentials
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17763/)Comprehensive PrestaShop Training
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/17762/)JavaScript Masterclass for Beginner to Expert: Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17761/)HTML CSS JavaScript Course for UI/UX Modern Web Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/17760/)Learn Python from Scratch : Python Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17759/)50
0+ SAS Interview Questions Practice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17758/)Learn C# Coding Basi
cs for Beginners: C# Fundamentals
* Full Stack developer course for Web Applications: Bootcamp
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/17757/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17756/)Full Stack Web Development 
Course 2024: Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17755/)Learn to Code Your HTML Website: Coding
 for Kids & Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17754/)Learn to Code HTML & CSS for Responsive
 Real-World Websites
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17753/)Learn C# Coding Intermediate: C# Classes
, Methods and OOPs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17752/)Excel Power Tools Master Formulas, Automat
ion Data Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17751/)Mastering GitHub Copilot’s AI Assistance an
d AI-Powered Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17750/)Criminology and Criminal Psychology | Certi
fied CSI+ Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17749/)Logistic Regression in R Studio
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/17748/)Agile Trainer Certification
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17747/)Entrepreneurship: Ideas, Market Analysis, Competitors, Place
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/17746/)Marketing Analytics: Forecasting Models with Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/177
45/)Data Visualization in Excel: All Excel Charts and Graphs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17744/)
Complete Linear Regression Analysis in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17743/)Mastering ChatG
PT: All ChatGPT Features and Functions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17742/)Python for Data Scienc
e: Python Programming & Data Analysis
* ML for Business Managers: Build Regression model in R Studio
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/17741/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17740/)QuickBooks Online Pay
ments – Getting Paid Faster & Easier
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17739/)SQL Masterclass: SQL for
 Data Analytics
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17738/)Bell Curve
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/17737/)Marketing Analytics: Pricing Strategies and Price Analytics
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/17736/)Guitar Music Theory in Excel-Scales, Intervals, Modes & More
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/17735/)Microsoft Excel Weekender Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17734
/)Logistic Regression in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17733/)Zero to Hero in LangChain: Bu
ild GenAI apps using LangChain
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17732/)Microsoft Office सीखें: Excel,
 PowerPoint & Word in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17731/)HR People Analytics
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/17730/)Microsoft Word in Hindi: हिंदी में सीखें MS Word
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/17729/)Chatbot
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17728/)Side Hustle Mastery
: 32 Ways to Earn Extra Income Online
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17727/)Level Up Your UI/UX: In
teractive Design & Prototyping Figma
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17726/)ChatGPT in Hindi: हिंदी 
में Complete ChatGPT guide
* Visual Guitar Mastery
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/17725/)
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/17724/)Python for Data Science in Hindi (हिंदी)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/17723/)Machine Learning with TensorFlow on Google Cloud
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17722/)ChatGPT for Office Productivity: Use AI for 10X Productivity
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17721/)Professional Diploma in Business Models Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/17720/)XK0-004: CompTIA Linux+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17719/)SK0-004: C
ompTIA Server+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17718/)PT0-003: CompTIA PenTest+ P
ractice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17717/)PT0-001: CompTIA PenTest+ Practice test 202
4
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/17716/)Valor temporal del dinero y presupuesto de capital
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/17715/)Einstieg Excel Visual-Basic (VBA) für Controller
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/17714/)Marketing Strategy Development: Stand Out From the Crowd
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/17713/)Quiz Marketing Power: Generate Leads for Marketing Success
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/17712/)Discover Google Gemini for Marketing Success
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/17711/)Link building. Build links that boost the site traffic!
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/17710/)ChatGPT for Mastering Compelling Content

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https
://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ NaturalAgents - notion-style editor to easily create AI Agents ](https://www.reddit.com/r/developer/comments/1fyfwbi/naturalagents_notionstyle_editor_to_easily_create/) , 2024-10-10-0912
```
[NaturalAgents](https://github.com/NaturalAgents/NaturalAgents) is the easiest way to create AI Agents in a notion-style
 editor. It's no-code and enables anyone to build sophisticated agents. It's current in its MVP state, but it fully open
-source and will be actively maintained. 



How this is different from other agent builders -

1. No boilerplate code (
imagine langchain for multiple agents)
2. No code experience
3. Can easily share and build with others
4. Readable/organ
ized agent outputs
5. Abstracts agent communications without visual complexity (image large drag and drop flowcharts)

W
ould love to hear thoughts and feel free to reach out if you're interested in contributing!
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-10-0912
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-10-0912
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-10-0912
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-10-0912
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
