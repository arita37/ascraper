 
all -  [ [LangGraph] Preventing an Agent from assuming users can see tool calls.
 ](https://www.reddit.com/r/LangChain/comments/1h5ynci/langgraph_preventing_an_agent_from_assuming_users/) , 2024-12-04-0914
```
Hi all,

I've implemented a ReAct-inspired agent connected to a curriculum specific content API. It is backed by Claude 
3.5 Sonnet. There are a few defined tools like `list_courses`, `list_units_in_course`, `list_lessons_in_unit`, etc.

The
 chat works as expected an asking the agent 'what units are in the Algebra 1 course' fires off the expected tool calls. 
However, the actual response provided is often along the lines of:

* text: *'Sure...let me find out'*
* tool\_call: `li
st_courses`
* tool\_call: `list_units_in_course`
* text: *'I've called tools to answer your questions.* ***You can see t
he units in Algebra 1 above***\*'\*

**The Issue**

The assistant is making the assumption that tool calls and their res
ults are rendered to the user in some way. That is not the case.

**What I've Tied:**

* Prompting with strong language 
explaining that the user can definitely not see tool\_calls on their end.
* Different naming conventions of tools, eg `f
etch_course_list` instead of `list_courses`

Neither of these solutions completely solved the issue and both are stochas
tic in nature. They don't guarantee the expected behavior.

**What I want to know:**

Is there an architectural pattern 
that guarantees LLM responses **don't** make this assumption?
```
---

     
 
all -  [ Project Alice v0.3 => OS Agentic Workflows with Web UI ](https://www.reddit.com/r/LangChain/comments/1h5xu23/project_alice_v03_os_agentic_workflows_with_web_ui/) , 2024-12-04-0914
```
Hello!

This is the 3rd update of the Project Alice framework/platform for agentic workflows: [https://github.com/Marian
oMolina/project\_alice/tree/main](https://github.com/MarianoMolina/project_alice/tree/main)

**Project Alice** is an ope
n source platform/framework for agentic workflows, with its own React/TS WebUI. It offers a way for users to create, run
 and perfect their agentic workflows with 0 coding needed, while allowing coding users to extend the framework by creati
ng new API Engines or Tasks, that can then be implemented into the module. The entire project is build with readability 
in mind, using Pydantic and Typescript extensively; its meant to be self-evident in how it works, since eventually the g
oal is for agents to be able to update the code themselves. 

At its bare minimum it offers a clean UI to chat with LLMs
, where you can select any of the dozens of models available in the 8 different LLM APIs supported (including LM Studio 
for local models), set their system prompts, and give them access to any of your tasks as tools. It also offers around 2
0 different pre-made tasks you can use (including research workflow, web scraping, and coding workflow, amongst others).
 The tasks/prompts included are not perfect: The goal is to show you how you can use the framework, but you will need to
 find the right mix of the model you want to use, the task prompt, sys-prompt for your agent and tools to give them, etc
. 

# Whats new?

\- **RAG**: Support for RAG with the new Retrieval Task, which takes a prompt and a Data Cluster, and 
returns chunks with highest similarity. The RetrievalTask can also be used to ensure a Data Cluster is fully embedded by
 only executing the first node of the task. Module comes with both examples. 

[RAG](https://preview.redd.it/7fzgxhg7xh4
e1.png?width=2856&format=png&auto=webp&s=6c311e895c2f24537efb57793a6b3e9d47cde8cb)

\- **HITL**: Human-in-the-loop mecha
nics to tasks -> Add a User Checkpoint to a task or a chat, and force a user interaction 'pause' whenever the chosen nod
e is reached. 

[Human in the loop](https://preview.redd.it/wyz3j7t0xh4e1.png?width=2856&format=png&auto=webp&s=dfdbd1ca
96cd23d0d5a89c450cae714ed78bf4fd)

\- **COT**: A basic Chain-of-thought implementation: \[analysis\] tags are parsed on 
the frontend, and added to the agent's system prompts allowing them think through requests more effectively

[Example of
 Analysis and Documents being used](https://preview.redd.it/bqm9i4nffg4e1.jpg?width=1581&format=pjpg&auto=webp&s=4fb4d64
0687d885c1c17193e29ca3da9dbe76c7e)

\- **DOCUMENTS**: Alice Documents, represented by the \[aliceDocument\] tag, are par
sed on the frontend and added to the agent's system prompts allowing them to structure their responses better

[Document
 view](https://preview.redd.it/gidsz90ifg4e1.jpg?width=1591&format=pjpg&auto=webp&s=dad04e284dd0834e3ea1714ebe4243b700aa
bac9)

**- NODE** **FLOW**: Fully implemented node execution logic to tasks, making workflows simply a case where the no
des are other tasks, and other tasks just have to define their inner nodes (for example, a PromptAgentTask has 3 nodes: 
llm generation, tool calls and code execution). This allows for greater clarity on what each task is doing and why

[Tas
k response's node outputs](https://preview.redd.it/f1hp7p4ofg4e1.jpg?width=1877&format=pjpg&auto=webp&s=ded4170ce9a93a29
e3cab855e06aaa430b3a8516)

\- **FLOW VIEWER**: Updated the task UI to show more details on the task's inner node logic a
nd flow. See the inputs, outputs, exit codes and templates of all the inner nodes in your tasks/workflows. 

[Task flow 
view](https://preview.redd.it/29wurpckfg4e1.jpg?width=1861&format=pjpg&auto=webp&s=6093d1ca8fc96cc2a5791bc3287fa08ea215a
7ef)

\- **PROMPT PARSER**: Added the option to view templated prompts dynamically, to see how they look with certain in
puts, and get a better sense of what your agents will see

[Prompt parser](https://preview.redd.it/csyj3yzrfg4e1.jpg?wid
th=1599&format=pjpg&auto=webp&s=ab4b42d3f8048182d1c8d368e494084cabdacb42)

\- **APIS**: New APIs for Wolfram Alpha, Goog
le's Knowledge Graph, PixArt Image Generation (local), Bark TTS (local). 

\- **DATA CLUSTERS**: Now chats and tasks can
 hold updatable data clusters that hold embeddable references like messages, files, task responses, etc. You can add any
 reference in your environment to a data cluster to give your chats/tasks access to it. The new retrieval tasks leverage
 this.

\- **TEXT MGMT**: Added 2 Text Splitter methods (recursive and semantic), which are used by the embedding and RA
G logic (as well as other APIs with that need to chunk the input, except LLMs), and a Message Pruner class that scores a
nd prunes messages, which is used by the LLM API engines to avoid context size issues

**- REDIS QUEUE**: Implemented a 
queue system for the Workflow module to handle incoming requests. Now the module can handle multiple users running multi
ple tasks in parallel. 

\- **Knowledgebase:** Added a section to the Frontend with details, examples and instructions. 


\- \*\***NOTE**\*\*: If you update to this version, you'll need to reinitialize your database (User settings -> Danger
 Zone). This update required a lot of changes to the framework, and making it backwards compatible is inefficient at thi
s stage. Keep in mind Project Alice is still in Alpha, and changes should be expected

# What's next? Planned developmen
ts for v0.4:

\- Agent using computer

\- Communication APIs -> Gmail, messaging, calendar, slack, whatsapp, etc. (some 
more likely than others) 

\- Recurring tasks -> Tasks that run periodically, accumulating information in their Data Clu
ster. Things like 'check my emails', or 'check my calendar and give me a summary on my phone', etc. 

\- CUDA support fo
r the Workflow container -> Run a wide variety of local models, with a lot more flexibility

\- Testing module -> Build 
a set of tests (inputs + tasks), execute it, update your tasks/prompts/agents/models/etc. and run them again to compare.
 Measure success and identify the best setup. 

\- Context Management w/LLM -> Use an LLM model to (1) summarize long me
ssages to keep them in context or (2) identify repeated information that can be removed

# At this stage, I need help. 


**I need people to:**

\- Test things, find edge cases, find things that are non-intuitive about the platform, etc. Als
o, improving / iterating on the prompts / models / etc. of the tasks included in the module, since that's not a focus fo
r me at the moment. 

\- I am also very interested in getting some help with the frontend: I've done my best, but I thin
k it needs optimizations that someone who's a React expert would crush, but I struggle to optimize. 

And so much more. 
There's so much that I want to add that I can't do it on my own. I need your help if this is to get anywhere. I hope tha
t the stage this project is at is enough to entice some of you to start using, and that way, we can hopefully build an a
ctual solution that is open source, brand agnostic and high quality. 

Cheers!
```
---

     
 
all -  [ We became the product of the day on Product Hunt and got insane traffic by using these free organic  ](https://www.reddit.com/r/SaaS/comments/1h5ugyq/we_became_the_product_of_the_day_on_product_hunt/) , 2024-12-04-0914
```
Many people say it is not worth putting effort into Product Hunt, but we at [Composio](https://composio.dev/) might have
 had a different experience. We are an AI developer tool start-up, and last month, we launched two products(SWE-Kit and 
AgentAuth), which came first and third, respectively.

This gave us a lot of exposure. We were listed in multiple high-q
uality directories, newsletters, and blogs, and many people started talking about us on social media. We are still getti
ng traffic from all these sites. We gained upward of 1k signed-up users from these two launches. This was big for us. We
 now have a better domain rating and authority, which is worth every penny.

So, how did we do it?

We were on a tight b
udget, so we had to do everything ourselves.

1. **Blogs** As we are a dev tool start-up and our ICP is a software devel
oper; we wrote blogs on DevTo, HackerNoon, etc. This only got us 1.5k visitors. If you are serving developers, consider 
this.
2. **Collabs**: We collaborated with a few reputed brands in the industry, like LangChain (we used their framework
 to build an agent that topped the SWE bench), Replit, LlamaIndex, etc., so it was easy for them to promote us. Always m
ake sure you’re providing value before reaching out. Reach out to the brands you have made your app with; they are usual
ly open to share if there is an 'Aha' factor.
3. **Social Media** It was the centrepiece of our marketing channels.
   *
 **Reddit**: We found relevant subreddits for our niche, like LocalLlama, Self-hosted, Open-source, Programming, etc. an
d wrote about us, ensuring it didn’t violate rules.
   * **X(Twitter)/LinkedIn:** Posted a long-form catchy launch post 
with a video illustration, as these platforms are biased around it. Also, we made the brand's quote repost us. If you do
 not have brand collabs, get influencers from your niche and try to boost it. Instead of a different post, ask them to q
uote it. This worked better for us.
4. **Slack Channels** This might be icky, but it works. We collected a lot of Slack 
channels. Set up automation and send messages to members. This is still a danger zone, as you risk getting called out. G
ood, meaning people will be fine with it. You can do it at your own risk.
5. Once you rank on top, milk it to the best o
f your ability, writing blogs and tweets and sharing as much as possible.

We did this for all our launches, and we got 
a really good number of impressions (200k+) and users.

At the end of the day, it’s you and your product. Make sure it i
s interesting and provides value to the intended users.

Feel free to ask any questions or share anything you have done 
that helped you. Let’s help each other.
```
---

     
 
all -  [ Traveling this holidays? Use jenova.ai and it's new Google Maps integration to help you with your tr ](https://i.redd.it/7hsdh7eutn4e1.jpeg) , 2024-12-04-0914
```

```
---

     
 
all -  [ We became the product of the day on Product Hunt and got insane traffic by using these free organic  ](https://www.reddit.com/r/Entrepreneur/comments/1h5q18q/we_became_the_product_of_the_day_on_product_hunt/) , 2024-12-04-0914
```
Many people say it is not worth putting effort into Product Hunt, but we at Composio might have had a different experien
ce. We are an AI developer tool start-up, and last month, we launched two products(SWE-Kit and AgentAuth), which came fi
rst and third, respectively.

This gave us a lot of exposure. We were listed in multiple high-quality directories, newsl
etters, and blogs, and many people started talking about us on social media. We are still getting traffic from all these
 sites. We gained upward of 1k signed-up users from these two launches. This was big for us. We now have a better domain
 rating and authority, which is worth every penny.

So, how did we do it?

We were on a tight budget, so we had to do ev
erything ourselves.

1. **Blogs** As we are a dev tool start-up and our ICP is a software developer; we wrote blogs on D
evTo, HackerNoon, etc. This only got us 1.5k visitors. If you are serving developers, consider this.
2. **Collabs**: We 
collaborated with a few reputed brands in the industry, like LangChain (we used their framework to build an agent that t
opped the SWE bench), Replit, LlamaIndex, etc., so it was easy for them to promote us. Always make sure you’re providing
 value before reaching out. Reach out to the brands you have made your app with; they are usually open to share if there
 is an 'Aha' factor.
3. **Social Media** It was the centrepiece of our marketing channels.
   * **Reddit**: We found rel
evant subreddits for our niche, like LocalLlama, Self-hosted, Open-source, Programming, etc. and wrote about us, ensurin
g it didn’t violate rules.
   * **X(Twitter)/LinkedIn:** Posted a long-form catchy launch post with a video illustration
, as these platforms are biased around it. Also, we made the brand's quote repost us. If you do not have brand collabs, 
get influencers from your niche and try to boost it. Instead of a different post, ask them to quote it. This worked bett
er for us.
4. **Slack Channels** This might be icky, but it works. We collected a lot of Slack channels. Set up automati
on and send messages to members. This is still a danger zone, as you risk getting called out. Good, meaning people will 
be fine with it. You can do it at your own risk.
5. Once you rank on top, milk it to the best of your ability, writing b
logs and tweets and sharing as much as possible.

We did this for all our launches, and we got a really good number of i
mpressions (200k+) and users.

At the end of the day, it’s you and your product. Make sure it is interesting and provide
s value to the intended users.

Feel free to ask any questions or share anything you have done that helped you. Let’s he
lp each other.
```
---

     
 
all -  [ Structured data chunking for RAG ](https://www.reddit.com/r/Rag/comments/1h5kbus/structured_data_chunking_for_rag/) , 2024-12-04-0914
```
Hey! I wanted to ask if someone knows what is the best way to chunk structured data (csv, xls, ...) for RAG optimisation
, and why. It seems that LangChains CSVLoader chunks each row separately as a chunk and I get it, but I think its not th
at efficient. On the other hand if there is another chunking technique for these files then it would mix the semantics i
n one chunk (ex. multiple rows in a chunk), but would be more efficient. How do we deal with this? Also could you please
 tell me what is the best (efficiency and RAG performance) chunking strategy for Unstructured files and why? Thank you!
```
---

     
 
all -  [ Enhancing RAG Input with ParentDocumentRetriever: Debugging Missing Embeddings






 ](https://www.reddit.com/r/LangChain/comments/1h5jty3/enhancing_rag_input_with_parentdocumentretriever/) , 2024-12-04-0914
```
  
I am attempting to enhance my RAG (Retrieval-Augmented Generation) input by implementing the `ParentDocumentRetriever
`. However, when I tried to access the vector store, I encountered an issue where the embeddings section returned `None`
. The output is as follows:

`{`

  `'ids': [`

`'470b54cc-45d8-4c3f-b0a0-180b4e0f6f47',`

`'dd4d9324-649f-4438-b07c-b2c
f9294f2d2',`

`'80211d88-6e27-4878-8ea4-5490243707d3',`

`'c534b3f4-2dcd-482f-9f22-b93c5be3e93f'`

  `],`

  `'embedding
s': null,`

  `'documents': [`

`'This is a test sentence.',`

`'Another test document for embedding.',`

`'This is a te
st sentence.',`

`'Another test document for embedding.'`

  `],`

  `'uris': null,`

  `'data': null,`

  `'metadatas':
 [null]`

`}`

  
could someone help


```
---

     
 
all -  [ What tool is used to create hand-drawn style figures such as in the LangChain documentation? ](https://www.reddit.com/r/LangChain/comments/1h5jd0v/what_tool_is_used_to_create_handdrawn_style/) , 2024-12-04-0914
```
Hi,

I am working on a presentation, and I would like to draw a similar hand-drawn style graph to the ones in the LangCh
ain documention (e.g., [RAG flowchart](https://docs.smith.langchain.com/assets/images/b6c2e61d-ca0c-47a6-a660-b009ecde7a
69-b48370416ca48e217afecd203acb5987.png)).

Does anyone know what do they use to create such figures? Otherwise similar 
tools are also appreciated.
```
---

     
 
all -  [ Suggestions for Resume for ML internship/FT roles ](https://i.redd.it/v017j0nidl4e1.jpeg) , 2024-12-04-0914
```
Hi, I want to have some suggestions from people in this domain so that I can incorporate them into my resume. I have bee
n applying for internships and full time in data science and ML. It would be helpful to get some suggestions. Thanks in 
advance.
```
---

     
 
all -  [ Help me understand what can be improved about this template and resume. ](https://i.redd.it/l041wdjswk4e1.jpeg) , 2024-12-04-0914
```
Dealing with consistent rejections😭
```
---

     
 
all -  [ Need your perspective to land an entry level job ](https://www.reddit.com/r/datascience/comments/1h5e67f/need_your_perspective_to_land_an_entry_level_job/) , 2024-12-04-0914
```
Looking at the current market trends, what skills do you think one should focus on to land an entry level data analyst/d
ata science job in 8-9 months? 

Portfolio building, networking and preparing for interviews is already assumed but ...


Our time is limited. We cannot learn and focus on everything. What skills might be best spend on to land a job within t
his timeframe.

My educational background: 

1. Bachelor of Computing in Information Systems 

2. Currently persuing Msc
 Data Science and Computational Intelligence. (9 months left to graduate). All courses are finished, just the thesis lef
t.

My professional background:

Have experience as a content writer, content editor, technical writer etc.

Have done a
n 8 week Software Engineering internship (focused on fullstack JS/TS stack.)

Have done 2 months Internship as a 'Data S
cience intern' but it was focused on web scraping, cleaning data obtained through an API to generate market leads, build
ing proof of concept LLM applications using Langchain and Google Gemini/OpenAI API keys.

Note: 


1. I'm from a 3rd wor
ld country. I cannot offer you any financial compensation for your detailed guided response even if I really want to (un
less it is in Nrs). So, please ignore this post, it you are looking for monetary reward for you high quality response.


2. Please don't ask me to look at job postings, ask ChatGPT, Google. I've done those things. Job descriptions are like w
ishlists. If I read a JD, I come up with an impression that I need to have 10 year internship experience with almost eve
ry technology imaginable just to land an entry level job.  Provide me with your personal perspective.
  
```
---

     
 
all -  [ Help me Optimizing AI Application Deployment ](https://www.reddit.com/r/LangChain/comments/1h5c52s/help_me_optimizing_ai_application_deployment/) , 2024-12-04-0914
```
I'm developing an AI application using LangChain and OpenAI, and I want to deploy it in a scalable and fast way. I'm con
sidering using containers and Kubernetes, but I'm unsure how optimal it would be to deploy this application with a vecto
rized database running on it (without using third-party services), a retriever argument generator, and FastAPI. Could yo
u provide suggestions on how best to deploy this application?
```
---

     
 
all -  [ Evaluation metrics for llm summary  ](https://www.reddit.com/r/LangChain/comments/1h5a1sj/evaluation_metrics_for_llm_summary/) , 2024-12-04-0914
```
I am working on long document summarization model using gpt-4o-mini and mistralAI.

I want compare my llm output with hu
man output. 

Initially,i compared with Abstract as reference with llm output. The results such as blue,rouge are varyin
g at broad range. 

I absorbed that length of a llm output is double the abstract.

So, I am looking for suggestions to 
evaluate llm summary output only, for eg: before and after improving context of llm with external information.
```
---

     
 
all -  [ what is difference between bind_tools to a LLM or creating an agent with vanilla LLM and the tool ?  ](https://www.reddit.com/r/LangChain/comments/1h58de1/what_is_difference_between_bind_tools_to_a_llm_or/) , 2024-12-04-0914
```
i am confused between the two so any help?


```
---

     
 
all -  [ Building a Personalized AI Assistant with LangChain ](https://www.reddit.com/r/u_KonradFreeman/comments/1h56mgk/building_a_personalized_ai_assistant_with/) , 2024-12-04-0914
```
In this blog post, we'll explore a Python script that serves as a foundation for building such an AI assistant. We'll de
lve into how you can use this code as a starting point and discuss several exciting applications, complete with follow-u
p prompts to inspire your next project.

  
Read about some of the possible applications of this starting point on my no
n-monetized blog or just check out the repo.

[https://danielkliewer.com/2024/12/02/persona-chat](https://danielkliewer.
com/2024/12/02/persona-chat)

`git clone` [`https://github.com/kliewerdaniel/PersonaChat.git`](https://github.com/kliewe
rdaniel/PersonaChat.git)

The provided Python script leverages the power of LangChain, OpenAI's GPT models, and vector d
atabases to create an AI assistant that imitates the writing style of a specific persona based on provided writing sampl
es. Here's what the script does:

1. **Loads Writing Samples**: Reads text and PDF files from a specified folder to gath
er writing samples.
2. **Processes and Embeds Text**: Splits the text into manageable chunks and creates embeddings usin
g OpenAI's API.
3. **Creates a Vector Store**: Stores the embeddings in a Chroma vector store for efficient retrieval.
4
. **Sets Up a Retrieval QA Chain**: Uses LangChain's RetrievalQA to build an interactive question-answering system.
5. *
*Interacts with the User**: Provides a conversational interface where the AI assistant responds in the persona's writing
 style.
6. **Saves Conversations**: Logs the conversation history into a Markdown file for future reference.

# It is ju
st a basic one file app, the requirements are:

    openai
    python-dotenv
    langchain 
    chromadb 
    pinecone-c
lient 
    tiktoken
    sentence-transformers
    PyPDF2
    langchain-community
    langchain-openai 
    langchain-chr
oma
    pypdf

Here is the file:

    import os
    import sys
    import glob
    from langchain_community.document_loa
ders import TextLoader, PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from lang
chain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma
    from lang
chain_community.chat_models import ChatOpenAI
    from langchain.chains import RetrievalQA
    from langchain.prompts im
port PromptTemplate
    import openai
    from langchain_openai import OpenAIEmbeddings  # Updated import
    from doten
v import load_dotenv
    from langchain.memory import ConversationBufferMemory
    
    load_dotenv()  # Load variables 
from .env
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print('Error: OPENAI_API_K
EY not found in environment variables.')
        exit(1)
    
    def main():
    
        
        # Initialize memory

        memory = ConversationBufferMemory(memory_key='history', return_messages=True)
    
    
        # Step 1: Load a
nd process writing samples
        folder_path = './writing_samples'
        documents = []
        for filepath in glob
.glob(os.path.join(folder_path, '**/*.*'), recursive=True):
            if os.path.isfile(filepath):
                ext
 = os.path.splitext(filepath)[1].lower()
                try:
                    if ext == '.txt':
                    
    loader = TextLoader(filepath, encoding='utf-8')
                        documents.extend(loader.load())
            
        elif ext == '.pdf':
                        loader = PyPDFLoader(filepath)
                        documents.ext
end(loader.load())
                    else:
                        print(f'Unsupported file format: {filepath}')
     
           except Exception as e:
                    print(f'Error reading '{filepath}': {e}')
    
        if not docu
ments:
            print('No documents found in the folder.')
            exit(1)
    
        text_splitter = Recursive
CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
    

        # Step 2: Create embeddings and vector store
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key
)  # Pass API key directly
        vector_store = Chroma.from_documents(texts, embeddings, persist_directory='./persona_
vectorstore')
        vector_store.persist()
    
        # Step 3: Set up the retriever and agent
        retriever = v
ector_store.as_retriever(search_kwargs={'k': 3})
        llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key
)
    
    
        persona_prompt = PromptTemplate(
            input_variables=['context', 'question'],
            te
mplate='''
    Based on the context answer to the best of your ability
    
    Context:
    {context}
    
    Question
:
    {question}
    
    Answer in the writing style of the context.
    '''
        )
    
        qa_chain = Retrieva
lQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=retriever,
            m
emory=memory,
            return_source_documents=False,
            chain_type_kwargs={'prompt': persona_prompt}
      
  )
    
        def save_to_markdown(conversation, filename='conversation.md'): 
            with open(filename, 'a', e
ncoding='utf-8') as f:
                f.write(conversation + '\n\n---\n\n')
    
    
        # Step 4: Interact with t
he user and save to markdown
        print('You can now interact with the persona. Type 'exit' to quit.\n')
        conv
ersation_history = ''
        while True:
            user_input = input('You: ')
            if user_input.lower() in (
'exit', 'quit'):
                break
    
            # Generate response
            response = qa_chain.run(user_inp
ut)
    
            # Display and save the conversation
            print(f'Persona: {response}\n')
            convers
ation = f'### You:\n{user_input}\n\n### Persona:\n{response}'
            save_to_markdown(conversation)
    
    
    i
f __name__ == '__main__':
        main()

  
Let me know what you think. 
```
---

     
 
all -  [ Questioning the value of langchain ](https://www.reddit.com/r/LangChain/comments/1h56klp/questioning_the_value_of_langchain/) , 2024-12-04-0914
```
I deployed a simple app using LangGraph served by a react FE.

Everything worked fine… until it didn’t. It’s a nightmare
 to debug. And I’m questioning what value the langchain ecosystem really offers.

Any viewpoints would be appreciated be
fore I commit coupling my code with langchain. 

I’m looking at ell, getliteralai. Majority of the value comes from the 
LLM server, including streaming.

I’m terms of parallelisation and managing the state of the graph, does langgraph rally
 do a lot of heavy lifting? I mean I can build interesting agents from scratch. So…

I’m feeling it’s a bait and switch 
tbh, but I could just be frustrated… 
```
---

     
 
all -  [ [For Hire] Unlock Your Business's Potential with Expert Full-Stack Development for a Powerful Digita ](https://www.reddit.com/r/forhire/comments/1h54cyt/for_hire_unlock_your_businesss_potential_with/) , 2024-12-04-0914
```
Hi Reddit! 👋

In today’s digital-first world, having a powerful and seamless online presence is no longer optional—it’s 
essential. Whether it’s creating user-friendly web platforms, scaling backend systems, or integrating smart automation, 
a robust tech foundation ensures your business stays ahead of the curve. From startups to established enterprises, I’m h
ere to help you build the tools you need to succeed.

I’m Sheryar, a Full Stack Developer skilled in React, Next.js, Nes
tJS, Node.js, AWS, and LangChain. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅
 **Backend**: Scalable APIs & microservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling 
 
✅ **Payments**: Stripe integration for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**
: Development with LangChain for intelligent automation

**Recent Work:**  
🚗 **Ride-sharing app** with Stripe payments 
& live tracking  
📦 **Urban logistics platform** with multi-stop deliveries  
📊 **Custom CRM** with Twilio API integrati
on  
🤖 **Chatbot & Voicebot solutions** for automation and customer support

💰 **Rate**: $15–$20/hour (negotiable)  
📧 D
M me to discuss your project or view my portfolio!  
**GitHub**: storm1033

Let’s create impactful digital solutions and
 take your business to the next level! 🚀
```
---

     
 
all -  [ Help with Vector Databases ](https://www.reddit.com/r/LLMDevs/comments/1h53bdl/help_with_vector_databases/) , 2024-12-04-0914
```
Hey folks, I was tasked with making a Question Answering Chatbot for my firm -
I ended up with a Question Answering chai
n via Langchain
I'm using the following models -
For Inference: Mistral 7B (from Ollama)
For Embeddings: Llama 2 7B (Oll
ama aswell)
For Vector DB: FAISS Local DB

I like this system because I get to produce a chat-bot like answer via the In
ference Model - Mistral, however, due to my lack of experience, I decided to simply go with Llama 2 for Embedding model.


Each of my org's documents are anywhere from 5000-25000 characters in length. There's about 13 so far and more to be a
dded as time passes (current count at about 180,000) [I convert these docs into one long text file which is auto-formatt
ed and cleaned].
I'm using the following chunking system:
Chunk Size: 3000
Chunk Overlap: 200

I'm using FAISS' similari
ty search to retrieve the relevant chunks from the user prompt - however the accuracy massively degrades as I go beyond 
say 30,000 characters in length. I'm a complete newbie when it comes to using Vector-DB's - I'm not sure if I'm supposed
 to fine-tune the Vector DB, or if I should opt for a new Embedding Model. But I'd like some help, tutorial and other he
lpful resources will be a lifesaver! I'd like a Retrieval System that has good accuracy with fast Retrieval speeds - how
ever the accuracy is a priority. 

Thanks for the long read!

```
---

     
 
all -  [  I replaced my voicemail with ChatGPT. ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1h539l9/i_replaced_my_voicemail_with_chatgpt/) , 2024-12-04-0914
```
Weekend Build: I replaced my voicemail with ChatGPT.

Features:
- Books meeting on Calendly
- Spam filter
- Knows me (RA
G)

Why?: It sucks to call doctors, lawyers etc to schedule a meeting or get simple information. I know this will become
 standard.

Story: When I worked at the Pentagon, we had a really sweet elderly secretary Barbara. If I released this I'
d call this CallBarbara AI.

Tech: Twilio (phone), Deepgram (TTS), OpenAI (LLM), LangChain RAG (for my information), Cal
endly (availability), Google (calendar int). Unfortunately Calendly API blows so I had to use google's api. 

Learnings:
 I could make this significantly faster and more expensive with OpenAI's realtime voice (Speech-to-speech), or an open s
ource version. 

Next/ Maybe: 
- Build front end (for anyone to use)
- Clone any voice
- Figure out use-cases (SMB brick
 and mortar?)
```
---

     
 
all -  [ Need Advice on Implementing Reranking Models for an AI-Based Document-Specific Copilot feature ](https://www.reddit.com/r/LLMDevs/comments/1h50nwl/need_advice_on_implementing_reranking_models_for/) , 2024-12-04-0914
```
Hey everyone! I'm currently working on an AI-based grant writing system that includes two main features:

Main  AI: Uses
 LLMs to generate grant-specific suggestions based on user-uploaded documents.

Copilot Feature: Allows document-specifi
c Q&A by utilizing a query format like /{filename} {query} to fetch information from the specified document.

Currently,
 we use FAISS for vector storage and retrieval, with metadata managed through .pkl files. This setup works for similarit
y-based retrieval of relevant content. However, I’m considering introducing a reranking model to further enhance retriev
al accuracy, especially for our Copilot feature.

Challenges with Current Setup:

Document-Specific Retrieval: We're sto
ring document-specific embeddings and metadata in .pkl files, and retrieval works by first querying FAISS.

Objective: I
mprove the precision of the results retrieved by Copilot when the user requests data from a specific document (e.g., /ex
ample.pdf summarize content).

Questions for the Community:

Is using a reranking model (e.g., BERT-based reranker, Mini
LM) a good idea to add another layer of precision for document retrieval, especially when handling specific document req
uests?

If I implement a reranking model, do I still need the structured .pkl files, or can I rely solely on the embeddi
ngs and reranking for retrieval?

How can I effectively integrate a reranking model into my current FAISS + Langchain se
tup?

I’d love to hear your thoughts, and if you have experience in using reranking models with FAISS or similar, any ad
vice would be highly appreciated. Thank you!


```
---

     
 
all -  [ Need Advice on Implementing Reranking Models for an AI-Based Document-Specific Copilot feature ](https://www.reddit.com/r/learnmachinelearning/comments/1h50l6c/need_advice_on_implementing_reranking_models_for/) , 2024-12-04-0914
```
Hey everyone! I'm currently working on an AI-based grant writing system that includes two main features:

1. **Main  AI*
*: Uses LLMs to generate grant-specific suggestions based on user-uploaded documents.
2. **Copilot Feature**: Allows doc
ument-specific Q&A by utilizing a query format like `/{filename} {query}` to fetch information from the specified docume
nt.

Currently, we use **FAISS** for vector storage and retrieval, with metadata managed through `.pkl` files. This setu
p works for similarity-based retrieval of relevant content. However, I’m considering introducing a **reranking model** t
o further enhance retrieval accuracy, especially for our Copilot feature.

**Challenges with Current Setup:**

* **Docum
ent-Specific Retrieval**: We're storing document-specific embeddings and metadata in `.pkl` files, and retrieval works b
y first querying FAISS.
* **Objective**: Improve the precision of the results retrieved by Copilot when the user request
s data from a specific document (e.g., `/example.pdf summarize content`).

**Questions for the Community:**

1. Is using
 a reranking model (e.g., **BERT-based reranker, MiniLM**) a good idea to add another layer of precision for document re
trieval, especially when handling specific document requests?
2. If I implement a reranking model, do I still need the s
tructured `.pkl` files, or can I rely solely on the embeddings and reranking for retrieval?
3. How can I effectively int
egrate a reranking model into my current FAISS + Langchain setup?

I’d love to hear your thoughts, and if you have exper
ience in using reranking models with FAISS or similar, any advice would be highly appreciated. Thank you!

# 
```
---

     
 
all -  [ Build a Multi-Agent AI System with LangChain, AutoGen, Azure OpenAI GPT-4, and Azure PostgreSQL ](https://www.reddit.com/r/PostgreSQL/comments/1h4z6rl/build_a_multiagent_ai_system_with_langchain/) , 2024-12-04-0914
```
Hello, I have started a Github Repo to work on simple scenarios with Multi AI Agents and Databases. There are 3 scenario
s there: Chat with Your Data, Develop on Your Data and Act on Your Data.I am using Autogen, Langchain, Azure PostgreSQL,
 and Azure Open AI. 

I welcome feedback and improvements from the community: [https://github.com/Azure-Samples/azure-po
stgresql-openai-langchain-autogen-demo](https://github.com/Azure-Samples/azure-postgresql-openai-langchain-autogen-demo)
 

I am planning to use other LLM models but I am hitting issues with using other GPT models as they keep adding \`\` sq
l \`\`\`

  

```
---

     
 
all -  [ error with HuggingFaceEmbeddings ](https://www.reddit.com/r/LangChain/comments/1h4ynos/error_with_huggingfaceembeddings/) , 2024-12-04-0914
```
hello guys, i have been trying to fix this issue for a while i cant really figure it out, so what happens is when i run


    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings_model = HuggingFaceEmbeddings()

i get the e
rror:

    RuntimeError: Failed to import transformers.integrations.integration_utils because of the following error (lo
ok up to see its traceback):
    Failed to import transformers.modeling_utils because of the following error (look up to
 see its traceback):
    cannot import name 'quantize_' from 'torchao.quantization' (C:\Users\kashy\AppData\Local\Progra
ms\Python\Python310\lib\site-packages\torchao\quantization\__init__.py)

can someone please help me with it. thanks in a
dvance
```
---

     
 
all -  [ Claude Doesn't Follow My Few Shot Prompts ](https://www.reddit.com/r/LangChain/comments/1h4w0ac/claude_doesnt_follow_my_few_shot_prompts/) , 2024-12-04-0914
```
    claude_sentiment_clf = ChatAnthropic(
        model='claude-3-5-sonnet-20240620',
        temperature=0,
        max
_tokens=3,
        timeout=None,
        max_retries=2,
    claude_sentiment_clf = ChatAnthropic(
        model='claude-
3-5-sonnet-20240620',
        temperature=0,
        max_tokens=3,
        timeout=None,
        max_retries=2,
    )

H
ere I create an instance of the Claude 3.5 Sonnet and later on using LangChain I pass it on a prompt to make a simple cl
assification and within this prompt I have few shot examples.

Initially it was working well and i had it restricted to 
3 labels. Now it is trying to generate non-sense argumentation of why it thinks the classification is..

I run the same 
chains with OpenAI API and I don't have any issues what so ever.

What is causing this to happen?

Again to clarify, it 
outputs 3 tokens, but not the ones I want.

I want it to output \[Bullish, Bearish, Neutral\], instead it gives me somet
hing like 'The article suggests'

Is there some type of memory reset that might be causing the issue?

I am using the pa
id API version.

The outputs are given here:

('Bullish', 'Here are the')

first output is OPEN AI, which is working as 
intented. The second output is Claude.

And here are the Few Shots:

)

Here I create an instance of the Claude 3.5 Sonn
et and later on using LangChain I pass it on a prompt to make a simple classification and within this prompt I have few 
shot examples.

Initially it was working well and i had it restricted to 3 labels. Now it is trying to generate non-sens
e argumentation of why it thinks the classification is..

I run the same chains with OpenAI API and I don't have any iss
ues what so ever.

What is causing this to happen?

Again to clarify, it outputs 3 tokens, but not the ones I want.

I w
ant it to output \[Bullish, Bearish, Neutral\], instead it gives me something like 'The article suggests'

Is there some
 type of memory reset that might be causing the issue?

I am using the paid API version.

The outputs are given here:

(
'Bullish', 'Here are the')

first output is OPEN AI, which is working as intented. The second output is Claude.

https:/
/preview.redd.it/3p6cacef2g4e1.png?width=1080&format=png&auto=webp&s=c6e629c5d0aa419d0db9ffff216760362f538381

https://p
review.redd.it/jw35b7hg2g4e1.png?width=1051&format=png&auto=webp&s=13e60b1da444f6916446221db6824742e87ab915

And here ar
e the Few Shots:

https://preview.redd.it/iolm8jkd2g4e1.png?width=302&format=png&auto=webp&s=89ddd2cf480b351d71201e65870
da59937f84e7d


```
---

     
 
all -  [ Claude Doesn't Follow My Few Shot Prompts ](https://www.reddit.com/r/ClaudeAI/comments/1h4vtjl/claude_doesnt_follow_my_few_shot_prompts/) , 2024-12-04-0914
```
    claude_sentiment_clf = ChatAnthropic(
        model='claude-3-5-sonnet-20240620',
        temperature=0,
        max
_tokens=3,
        timeout=None,
        max_retries=2,
    )

Here I create an instance of the Claude 3.5 Sonnet and la
ter on using LangChain I pass it on a prompt to make a simple classification and within this prompt I have few shot exam
ples.

Initially it was working well and i had it restricted to 3 labels. Now it is trying to generate non-sense argumen
tation of why it thinks the classification is..

I run the same chains with OpenAI API and I don't have any issues what 
so ever.

What is causing this to happen?

Again to clarify, it outputs 3 tokens, but not the ones I want.

I want it to
 output \[Bullish, Bearish, Neutral\], instead it gives me something like 'The article suggests'

Is there some type of 
memory reset that might be causing the issue?

  
I am using the paid API version.

The outputs are given here:

('Bulli
sh', 'Here are the')

first output is OPEN AI, which is working as intented. The second output is Claude.

https://previ
ew.redd.it/pl8b73lc1g4e1.png?width=1225&format=png&auto=webp&s=b704b8911a3299e2f449fe94bb1512c5f830cda4

https://preview
.redd.it/rm4akq091g4e1.png?width=1051&format=png&auto=webp&s=19dd82885d1586c95fdd2db5c531cc8fafd50bd6

And here are the 
Few Shots:



https://preview.redd.it/3uwz6rth1g4e1.png?width=302&format=png&auto=webp&s=05815208ac2be654cc2599524f544cb
820735937


```
---

     
 
all -  [ What is the process of extracting keywords from multiple pdfs. ](https://www.reddit.com/r/LangChain/comments/1h4r1xd/what_is_the_process_of_extracting_keywords_from/) , 2024-12-04-0914
```
https://preview.redd.it/2uucr4f3ke4e1.png?width=1316&format=png&auto=webp&s=1a9671e2d2b1160c18193b6b961f520a0aa96869

I 
am trying to implement a feature that can extract all the topics and its subtopics from pdfs or docs uploaded by the use
r. The issue is i can't figure out how do I do a vector search on the pdfs vector storage. I want this kind of structure
 attached in the image. I get it i can structurer the data using LLM, but how do I get all the topics from the pdfs uplo
aded. Either I can extract keywords from each chunk by giving it to llm but that will use soo manny tokens. I am new to 
langchain as well. Also show up a screenshot or something how do you guys setup your agents in js.  

```
---

     
 
all -  [ Chunking strategy for diverse sets of documents  ](https://www.reddit.com/r/LangChain/comments/1h4qm3l/chunking_strategy_for_diverse_sets_of_documents/) , 2024-12-04-0914
```
I am working on a RAG system for analysing and pulling information out of documents. These documents come from various c
lients and thus the structure and layout of the documents is very different from one document to the next, also the file
 types (can be pdf, docx). I am thus struggling to find a good method for chunking which I can apply to all documents th
at come in. At the moment I am simply pulling all of the text out of the document and then using semantic splitting. Ive
 also dabbled in using an agent to help me split but that has also not been super reliable.

Any tips on how I can handl
e diverse document sets?
```
---

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy  ](https://www.reddit.com/r/Udemy/comments/1h4q2id/advance_your_career_100_free_certified_courses_on/) , 2024-12-04-0914
```
Selenium Webdriver with Java & TestNG Testing Framework

https://courze.org/selenium-webdriver-with-java-testng-testing-
framework/



Digital Marketing Professional Certification

https://courze.org/digital-marketing-professional-certificat
ion/



C\_SAC\_2415 SAP Analytics Cloud Practice Test

https://courze.org/c\_sac\_2415-sap-analytics-cloud-practice-tes
t/



Non-Engineers’ Guide to Tech Study Abroad: MS, Tech MBA, PhD

https://courze.org/non-engineers-guide-to-tech-study
-abroad-ms-tech-mba-phd/



PowerShell Regular Expressions: Regex Master Class

https://courze.org/powershell-regular-ex
pressions-regex-master-class/



AZ-900: Azure Fundamentals Complete Training \[6 Hrs.\]

https://courze.org/az-900-exam
-prep-mastering-azure-fundamentals/



The Complete C & C++ Programming Course – Mastering  C & C++

https://courze.org/
the-complete-c-c-programming-course-mastering-c-c/



Machine Learning – Fundamental of Python Machine Learning

https:/
/courze.org/machine-learning-fundamental-of-python-machine-learning/



Python for Data Science Pro: The Complete Master
y Course

https://courze.org/python-for-data-science-pro-the-complete-mastery-course/



PowerShell Functions Master Cla
ss

https://courze.org/powershell-functions-master-class/



C-level management: 20 models for business operations (4/5)


https://courze.org/c-level-management-100-models-for-business-success-part-4/



File & Folder Management Using PowerS
hell: For Beginners

https://courze.org/file-folder-management-using-powershell/



Accelerate Your Learning: Master Ang
ular 18 and ASP.NET 8.0

https://courze.org/accelerate-your-learning-master-angular-18-and-asp-net-8-0/



AWS Certified
 Cloud Practitioner (CLF-C02) Practice Exams

https://courze.org/aws-certified-cloud-practitioner-clf-c02-practice-exams
/



Master Microservices : From Learner to Lead Architect

https://courze.org/master-microservices-from-learner-to-lead
-architect/



Data-driven decisions: mastering market research strategies

https://courze.org/data-driven-decisions-mas
tering-market-research-strategies/



CSS, JavaScript And PHP Complete Course For Beginners

https://courze.org/css-java
script-and-php-complete-course-for-beginners/



Metasploit from Scratch: Beginner to Professional

https://courze.org/m
etasploit-from-scratch-beginner-to-professional/



Become a Hydra Expert: Advanced Brute Forcing Techniques

https://co
urze.org/become-a-hydra-expert-advanced-brute-forcing-techniques/



NMAP Mastery: Ultimate Guide to Network Scanning

h
ttps://courze.org/nmap-mastery-ultimate-guide-to-network-scanning/



SmartPhone Graphic Design

https://courze.org/smar
tphone-graphic-design/



Web Development Professional Certification

https://courze.org/web-development-professional-ce
rtification/



Master Generative AI: LangChain & Hugging Face – 4 Projects

https://courze.org/master-generative-ai-lan
gchain-hugging-face-4-projects/



SmartPhone 3D Logo and Mockup Design

https://courze.org/smartphone-3d-logo-and-mocku
p-design/



Entrepreneurship: 60 Day Startup Launch Blueprint

https://courze.org/entrepreneurship-60-day-startup-launc
h-blueprint/



NSE7\_OTS-7.2: Fortinet Network Security Expert Practice 2024

https://courze.org/nse7\_ots-7-2-fortinet
-network-security-expert-practice-2024/



NSE7\_PBC-6.4: Fortinet Network Security Expert Practice 2024

https://courze
.org/nse7\_pbc-6-4-fortinet-network-security-expert-practice-2024/



NSE7\_PBC-7.2: Fortinet Network Security Expert Pr
actice 2024

https://courze.org/nse7\_pbc-7-2-fortinet-network-security-expert-practice-2024/



NSE7\_SDW-6.4: Fortinet
 Network Security Expert Practice 2024

https://courze.org/nse7\_sdw-6-4-fortinet-network-security-expert-practice-2024/




25 Projects in 25 days of AI Development Bootcamp

https://courze.org/25-projects-in-25-days-of-ai-development-bootc
amp/



Comprehensive TypeScript Practice Exam: Basics to Advanced

https://courze.org/comprehensive-typescript-practice
-exam-basics-to-advanced/



Lean Six Sigma Green Belt Professional Certification

https://courze.org/lean-six-sigma-gre
en-belt-professional-certification/



Mastering HTML5 and CSS3 (Part 1 – Beginner Level)

https://courze.org/mastering-
html5-and-css3-part-1-beginner-level/



AZ-900: Microsoft Azure Fundamentals Practice Exam

https://courze.org/az-900-m
icrosoft-azure-fundamentals-practice-exam/



CLF-C02 AWS Certified Cloud Practitioner | Practice Exams

https://courze.
org/clf-c02-aws-certified-cloud-practitioner-exam-tests-oct-2024/



SAA-C03 AWS Certified Solutions Architect Associate
 Practice

https://courze.org/saa-c03-aws-certified-solutions-architect-associate-practice/



AZ-204: Microsoft Azure D
eveloper Associate | Practice Exam

https://courze.org/az-204-microsoft-azure-developer-associate-practice-exam/



DOP-
C02 AWS Certified DevOps Engineer-Professional Exam

https://courze.org/dop-c02-aws-certified-devops-engineer-profession
al-exam/



C++ And Java Training Crash Course for Beginners

https://courze.org/c-and-java-training-crash-course-2022/




The Complete C++ Programming Course from Basic to Expert

https://courze.org/the-complete-c-programming-course-from-b
asic-to-expert/




```
---

     
 
all -  [ PREVENTING FINE-TUNED LLM TO ANSWER OUTSIDE OF CONTEXT
 ](https://www.reddit.com/r/LangChain/comments/1h4po9o/preventing_finetuned_llm_to_answer_outside_of/) , 2024-12-04-0914
```
Hello. I have fine-tuned a model that is performing well and I added RAG as well.

The flow of my llm-rag goes like this
:

  
I ask it questions, and it first goes to vector db and extracts the top 5 hits. I then pass these top 5 hits to my
 **LLM prompt** as context and then my LLM answers.

The problem I'm facing is if the user asks anything outside of the 
domain, the vector db still returns the top 5 hits. I can't limit the hits based on score, as it returns 80 above for co
ntextual and non-contextual similarity. I am using [gte-large](https://huggingface.co/thenlper/gte-large) embedding mode
l ( i tried all-MiniLM-L6-v2 but it was not picking up good context hence i went with gte-large).

  
So even when I ask
 outside domain questions it returns hits and the hits go into LLM Prompt and it answers.

  
So is there any workaround
?

  
Thanks
```
---

     
 
all -  [ Web scraping package in Python ](https://www.reddit.com/r/LangChain/comments/1h4pkbw/web_scraping_package_in_python/) , 2024-12-04-0914
```
Currently , I'm trying to get content from the urls. Could you recommend some libraries to scrap websites?
```
---

     
 
all -  [ Best chunking method for PDFs with complex layout?
 ](https://www.reddit.com/r/LangChain/comments/1h4p54t/best_chunking_method_for_pdfs_with_complex_layout/) , 2024-12-04-0914
```
I am working on a RAG based PDF Query system , specifically for complex PDFs that contains multi column tables, images, 
tables that span across multiple pages, tables that have images inside them.

I want to find the best chunking strategy 
for such pdfs.

Currently i am using RecursiveCharacterTextSplitter. What worked best for you all for complex PDF?


```
---

     
 
all -  [ ChatBot In structured and Unstructured Data ](https://www.reddit.com/r/LangChain/comments/1h4omfr/chatbot_in_structured_and_unstructured_data/) , 2024-12-04-0914
```
I am developing a ChatBot based on Structured Data of MongoDB. I am generating Mongodb queries from LLM and searching th
e database based on that query. So, users can converse the Mongodb data in Natural language and I am converting the Mong
odb results into Natural language using LLM. 

Also,I am using Azure AI search with Azure OpenAI for the ChatBot based o
n PDFs and PPTs .

How can I combine both these cases? If user asks any question it can generate the queries based on th
e relevant data from PDFs of other Unstructured data or vice versa.

Any suggested approach with Langchain and Azure Ope
n AI where it can generate the response in natural language based on Structured data and unstructured data automatically
?

Please share your thoughts..
```
---

     
 
all -  [ Abstract: Automated Design of Agentic Tools ](https://www.reddit.com/r/LangChain/comments/1h4l6jz/abstract_automated_design_of_agentic_tools/) , 2024-12-04-0914
```
I had an idea earlier today that I'm opening up to some of the Reddit AI subs to crowdsource a verdict on its feasibilit
y, at either a theoretical or pragmatic level.

Some of you have probably heard about Shengran Hu's paper 'Automated Des
ign of Agentic Systems', which started from the premise that a machine built with a Turing-complete language can do anyt
hing if resources are no object, and humans can do some set of productive tasks that's narrower in scope than 'anything.
' Hu and his team reason that, considered over time, this means AI agents designed by AI agents will inevitably surpass 
hand-crafted, human-designed agents. The paper demonstrates that by using a 'meta search agent' to iteratively construct
 agents or assemble them from derived building blocks, the resulting agents will often see substantial performance impro
vements over their designer agent predecessors. It's a technique that's unlikely to be widely deployed in production app
lications, at least until commercially available quantum computers get here, but I and a lot of others found Hu's demons
tration of his basic premise remarkable.

Now, my idea. Consider the following situation: we have an agent, and this age
nt is operating is an unusually chaotic environment. The agent must handle a tremendous number of potential situations o
r conditions, a number so large that writing out the entire possible set of scenarios in the workflow is either impossib
le or prohibitively inconvenient. Suppose that the entire set of possible situations the agent might encounter was divid
ed into two groups: those that are predictable and can be handled with standard agentic techniques, and those that are n
ot predictable and cannot be anticipated ahead of the graph starting to run. In the latter case, we might want to add a 
special node to one or more graphs in our agentic system: a node that would design, instantiate, and invoke a custom too
l \*dynamically, on the spot\* according to its assessment of the situation at hand.

Following Hu's logic, if an intell
igence written in Python or TypeScript can in theory do anything, and a human developer is capable of something short of
 'anything', the artificial intelligence has a fundamentally stronger capacity to build *tools* *it can use* than a huma
n intelligence could.

Here's the gist: using this reasoning, the ADAS approach could be revised or augmented into a 'AD
AT' (Automated Design of Agentic Tools) approach, and on the surface, I think this could be implemented successfully in 
production here and now. Here are my assumptions, and I'd like input whether you think they are flawed, or if you think 
they're well-defined.

P1: A tool has much less freedom in its workflow, and is generally made of fewer steps, than a fu
ll agent.  
P2: A tool has less agency to alter the path of the workflow that follows its use than a complete agent does
.  
P3: ADAT, while less powerful/transformative to a workflow than ADAS, incurs fewer penalties in the form of compound
ing uncertainty than ADAS does, and contributes less complexity to the agentic process as well.  
**Q.E.D: An 'improvise
d tool generation' node would be a novel, effective measure when dealing with chaos or uncertainty in an agentic workflo
w, and perhaps in other contexts as well.**

I'm not an AI or ML scientist, just an ordinary GenAI dev, but if my reason
ing appears sound, I'll want to partner with a mathematician or ML engineer and attempt to demonstrate or disprove this.
 If you see any major or critical flaws in this idea, please let me know: I want to pursue this idea if it has the poten
tial I suspect it could, but not if it's ineffective in a way that my lack of mathematics or research training might be 
hiding from me.

Thanks, everyone!
```
---

     
 
all -  [ [0 YOE] New Grad seeking entry-level opportunities  in Data  analyst across Canada ](https://www.reddit.com/r/EngineeringResumes/comments/1h4ibi2/0_yoe_new_grad_seeking_entrylevel_opportunities/) , 2024-12-04-0914
```
Hey Guys, Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Ap
plying to all over canada. i need all the criticism i can get . And Thank you in advance

Looking to optimize projects s
ection as well as work experience section

https://preview.redd.it/wcasdxjxzb4e1.jpg?width=5100&format=pjpg&auto=webp&s=
ec92d7026bcb4134cc4ba4112abe63b3050f4cec


```
---

     
 
all -  [ Resume Review - [0 YOE, New Grad, Data Related roles, Canada) ](https://www.reddit.com/r/resumesupport/comments/1h4i8iu/resume_review_0_yoe_new_grad_data_related_roles/) , 2024-12-04-0914
```
Hey Guys, Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Ap
plying to all over canada.  i need all the criticism i can get . And Thank you in advance

  
Looking to optimize projec
ts section as well as work experience section

.

https://preview.redd.it/r6isutm8zb4e1.jpg?width=5100&format=pjpg&auto=
webp&s=95b4ba0308f4314f23ac53a77533ca74219cd1e0


```
---

     
 
all -  [ [0 YOE, Unemployed, Data Analyst, Canada]-  New grad Looking to land a full time data related role ](https://www.reddit.com/r/resumes/comments/1h4i62o/0_yoe_unemployed_data_analyst_canada_new_grad/) , 2024-12-04-0914
```
Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Applying to 
all over canada.  i need all the criticism i can get . And Thank you in advance

https://preview.redd.it/n35ej3dnyb4e1.j
pg?width=5100&format=pjpg&auto=webp&s=d53c5e77821ab49cf9219fd29bd8c18deae00887


```
---

     
 
all -  [ [For Hire] Frontend and Backend Developer with the top and latest development technologies for a gre ](https://www.reddit.com/r/freelance_forhire/comments/1h4c8dm/for_hire_frontend_and_backend_developer_with_the/) , 2024-12-04-0914
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

     
 
all -  [ Best approach for automating WhatsApp communication between field teams and management. ](https://www.reddit.com/r/LangChain/comments/1h4atay/best_approach_for_automating_whatsapp/) , 2024-12-04-0914
```

Looking for advice on automating our WhatsApp communication:

Current setup:
- Field team reports hourly data in Group 
A
- Staff reviews data
- Staff forwards to Group B (management)

Need to:
- Automate this while maintaining data review 
capability
- Store structured data from WhatsApp responses for reporting
- Generate automated reports from collected dat
a

Considering WhatsApp Business API with chatbot or third-party solutions.

Anyone implemented similar automation? Look
ing for platform recommendations and rough cost estimates.

Thanks!
```
---

     
 
all -  [ [For Hire] React, NEXT, Nest, Express, Langchain and Full Stack Developer. ](https://www.reddit.com/r/forhire/comments/1h4ai5f/for_hire_react_next_nest_express_langchain_and/) , 2024-12-04-0914
```
Hi Reddit! 👋  
I'm Sheryar, a Full Stack Developer skilled in **React, Next.js, NestJS, Node.js, AWS**, and **LangChain*
*. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅ **Backend**: Scalable APIs & m
icroservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling  
✅ **Payments**: Stripe integr
ation for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**: Development with LangChain fo
r intelligent automation

**Recent Work**:  
🚗 Ride-sharing app with Stripe payments & live tracking  
📦 Urban logistics
 platform with multi-stop deliveries  
📊 Custom CRM with Twilio API integration  
🤖 Chatbot & Voicebot solutions for aut
omation and customer support

💰 **Rat**e: $15–$20/hour (negotiable)  
📧 DM me to discuss your project or view my portfol
io!  
**GitHub**: [storm1033](https://github.com/storm1033)

Let’s build something amazing together! 🚀
```
---

     
 
all -  [ Create your own basic RAG ](https://www.reddit.com/r/ArtificialInteligence/comments/1h48jdg/create_your_own_basic_rag/) , 2024-12-04-0914
```
[https://danielkliewer.com/2024/12/01/basic-rag](https://danielkliewer.com/2024/12/01/basic-rag)

In this guide I go thr
ough how to set up basic Retrieval Augmented Generation.

You can adapt it to your own projects.

I am really excited ab
out learning this. I knew what it was in concept but now I can use it for my own projects.

To save you a click the main
 juxt of the guide is the following code:

    import os
    import sys
    import glob
    from dotenv import load_dote
nv
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Updated imports
    from langchain_
openai.embeddings import OpenAIEmbeddings
    from langchain_chroma.vectorstores import Chroma
    from langchain_openai
.llms import OpenAI
    from langchain.chains import RetrievalQA
    
    # Updated document loaders
    from langchain_
community.document_loaders import TextLoader, PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterText
Splitter
    
    def main():
       # Load OpenAI API key
       openai_api_key = os.getenv('OPENAI_API_KEY')
       if
 not openai_api_key:
           print('Please set your OPENAI_API_KEY in the .env file.')
           sys.exit(1)
      

       # Define the folder path (change 'data' to your folder name)
       folder_path = './data'
       if not os.path.
exists(folder_path):
           print(f'Folder '{folder_path}' does not exist.')
           sys.exit(1)
      
       # 
Read all files in the folder
       documents = []
       for filepath in glob.glob(os.path.join(folder_path, '**/*.*'),
 recursive=True):
           if os.path.isfile(filepath):
               ext = os.path.splitext(filepath)[1].lower()
   
            try:
                   if ext == '.txt':
                       loader = TextLoader(filepath, encoding='utf
-8')
                       documents.extend(loader.load_and_split())
                   elif ext == '.pdf':
           
            loader = PyPDFLoader(filepath)
                       documents.extend(loader.load_and_split())
            
       else:
                       print(f'Unsupported file format: {filepath}')
               except Exception as e:

                   print(f'Error reading '{filepath}': {e}')
      
       if not documents:
           print('No docume
nts found in the folder.')
           sys.exit(1)
      
       # Split documents into chunks
       text_splitter = Rec
ursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
       texts = text_splitter.split_documents(documents)

      
       # Initialize embeddings and vector store
       embeddings = OpenAIEmbeddings()
       vector_store = Chro
ma(embedding_function=embeddings, persist_directory='./chroma_store')
      
       # Add texts to vector store in batch
es
       batch_size = 500  # Adjust this number as needed
       for i in range(0, len(texts), batch_size):
           
batch_texts = texts[i:i+batch_size]
           vector_store.add_documents(batch_texts)
      
       # Set up retriever

       retriever = vector_store.as_retriever(search_kwargs={'k': 3})
      
       # Set up the language model
       ll
m = OpenAI(temperature=0.7)
      
       # Create the RetrievalQA chain
       qa_chain = RetrievalQA.from_chain_type(

           llm=llm,
           chain_type='stuff',  # Options: 'stuff', 'map_reduce', 'refine', 'map_rerank'
           
retriever=retriever
       )
      
       # Interactive prompt for user queries
       print('The system is ready. You 
can now ask questions about the content.')
       while True:
           query = input('Enter your question (or type 'ex
it' to quit): ')
           if query.lower() in ('exit', 'quit'):
               break
           try:
               re
sponse = qa_chain.run(query)
               print(f'\nAnswer: {response}\n')
           except Exception as e:
         
      print(f'An error occurred: {e}\n')
              
    if __name__ == '__main__':
       main()

I hope you find th
is helpful. I am excited to explore the possibilities so if you have already used a RAG for your use case I would love t
o here what you use it for.

I think I will use it with the new AI agents set up I created which I described in a previo
us post.

I keep my blog free from monetization of any kind. I am just sharing this because I am excited about learning.
 Hope you enjoy.
```
---

     
 
all -  [ How I Built a Multi-Modal Search Pipeline with Voyager-3 ](https://www.reddit.com/r/LangChain/comments/1h47x6j/how_i_built_a_multimodal_search_pipeline_with/) , 2024-12-04-0914
```
Hey all,

I recently dove deep into multi-modal embeddings and built a pipeline that combines text and image data into a
 unified vector space. It’s a pretty cool way to connect and retrieve content across multiple modalities, so I thought I
’d share my experience and steps in case anyone’s interested in exploring something similar.



Here’s a breakdown of wh
at I did:

**Why Multi-Modal Embeddings?**

The main idea is to embed text and images into the same vector space, allowi
ng for seamless searches across modalities. For example, if you search for “cat,” the pipeline can retrieve related imag
es of cats *and* the text describing them—even if the text doesn’t explicitly mention the word “cat.”



**The Tools I U
sed**

1. **Voyager-3**: A state-of-the-art multi-modal embedding model.

2. **Weaviate**: A vector database for storing
 and querying embeddings.

3. **Unstructured**: A Python library for extracting content (text and images) from PDFs and 
other documents.

4. **LangGraph**: For building an end-to-end retrieval pipeline.



**How It Works**

1. **Extracting 
Text and Images**:

Using Unstructured, I pulled text and images from a sample PDF, chunked the content by title, and gr
ouped it into meaningful sections.

2. **Creating Multi-Modal Embeddings**:

I used Voyager-3 to embed both text and ima
ges into a shared vector space. This ensures the embeddings are contextually linked, even if the connection isn’t explic
itly clear in the data.

3. **Storing in Weaviate**:

The embeddings, along with metadata, were stored in Weaviate, whic
h makes querying incredibly efficient.

4. **Querying the Data**:

To test it out, I queried something like, “What does 
this magazine say about waterfalls?” The pipeline retrieved both text and images relevant to waterfalls—even if the text
 didn’t mention “waterfall” directly but was associated with a photo of one.

5. **End-to-End Pipeline**:

Finally, I bu
ilt a retrieval pipeline using LangGraph, where users can ask questions, and the pipeline retrieves and combines relevan
t text and images to answer.



**Why This Is Exciting**

This kind of multi-modal search pipeline has so many practical
 applications:

• Retrieving information from documents, books, or magazines that mix text and images.

• Making sense o
f visually rich content like brochures or presentations.

• Cross-modal retrieval—searching for text with images and vic
e versa.

I detailed the entire process in a [blog post here](https://medium.com/vectrix-ai/how-to-build-a-powerful-mult
i-modal-search-pipeline-with-voyager-3-6024ff98d9ca), where I also shared some code snippets and examples.

If you’re in
terested in trying this out, I’ve also uploaded the code to [GitHub](https://github.com/vectrix-ai/vectrix-graphs/blob/m
ain/examples/multi-model-embeddings.ipynb). Would love to hear your thoughts, ideas, or similar projects you’ve worked o
n!

Happy to answer any questions or go into more detail if you’re curious. 😊
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-04-0914
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-12-04-0914
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

     
