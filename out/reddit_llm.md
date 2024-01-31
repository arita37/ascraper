 
all -  [ Generative AI: An introduction to prompt engineering and LangChain for data practitioners ](https://medium.com/teradata/generative-ai-part-1-an-introduction-to-prompt-engineering-and-langchain-742987f2d9c1?source=friends_link&sk=e62cbac26db2d6ed662b6d08c2469504) , 2024-01-31-0910
```

```
---

     
 
all -  [ creating documents based on an example ](https://www.reddit.com/r/LanguageTechnology/comments/1af0ubt/creating_documents_based_on_an_example/) , 2024-01-31-0910
```
hello , I am trying to generate certain types of documents(reports) based on an example , I need the model to understand
 the structure of the examples then produce a document(section by section) with similar structure and info from the exam
ples but tailored to my case.  


I used gpt3.5 and 4 , fine tuned 3.5 on the examples and used langchain with chromadb 
 
I always would get non satisfactory answers , like i would ask for a certain section then it will write me nothing or 
write me another section or something that is not related ,   
i would be grateful if anyone has an advice for me , than
k you in advance
```
---

     
 
all -  [ Got a shoutout from an AI unicorn. ](https://www.reddit.com/r/Substack/comments/1aeyrf7/got_a_shoutout_from_an_ai_unicorn/) , 2024-01-31-0910
```
This is more of a yeah success than a questions or a lessons learned. Well, there is a bit of a lessons learned wrapped 
into it. 

Here we go. Langchain mentioned my substack on LinkedIn yesterday. [https://www.linkedin.com/posts/langchain\
_code-clinic-searching-youtube-with-langchain-activity-7157779744799789056-X7f\_?utm\_source=share&utm\_medium=member\_d
esktop](https://www.linkedin.com/posts/langchain_code-clinic-searching-youtube-with-langchain-activity-71577797447997890
56-X7f_?utm_source=share&utm_medium=member_desktop)

Who is Langchain? Langchain is one of the leading generative AI / a
utonomous agents unicorns in the world.

How did it get to this? I wrote the article, messaged their team, and got menti
oned. Simple. Maybe I got lucky.

T
```
---

     
 
all -  [ get_openai_callback not working when using Agent Executor after updating to latest version of Langch ](https://www.reddit.com/r/LangChain/comments/1aey6gi/get_openai_callback_not_working_when_using_agent/) , 2024-01-31-0910
```
### Description

I'm trying to use the get\_openai\_callback from langchain\_community.callbacks to get the number of to
ken and costs incurred in using the agent but I am getting zero on everything, as you can see here when I print.

&#x200
B;

https://preview.redd.it/9lbv5ocaymfc1.png?width=412&format=png&auto=webp&s=3d7282b8c88c39bdacf48a4a6ad867c0fdc574bd


I have also set up a custom callback handler to go deep into the issue and what I found is that ChatOpenAI from langcha
in\_openai does not call ainvoke as ChatOpenAI langchain.chat\_models did.

THank you for your help

### Code

    impor
t os
    import traceback
    
    from typing import Any, Dict, List, Optional
    from uuid import UUID
    
    from 
langchain_community.callbacks import get_openai_callback
    from langchain_core.agents import AgentFinish
    from lang
chain_openai import ChatOpenAI
    from langchain.prompts import PromptTemplate
    from langchain.tools.render import r
ender_text_description
    from langchain.agents.format_scratchpad import format_log_to_str
    from langchain.agents.ou
tput_parsers import ReActSingleInputOutputParser
    from langchain.schema import HumanMessage, LLMResult
    from langc
hain.callbacks.base import AsyncCallbackHandler
    from langchain.agents import AgentExecutor
    
    from app.service
s.llm.prompt import prompt_raw
    from app.services.llm.tools.build_tools import tools
    from app.classes.CustomBuffe
r import CustomConversationBufferMemory
    
    
    memory = CustomConversationBufferMemory(memory_key='chat_history',
 return_messages=True)
    
    
    class MyCustomAsyncHandler(AsyncCallbackHandler):
        async def on_llm_end(self
, response: LLMResult, **kwargs: Any) -> None:
            '''Run when chain ends running.'''
            print('RESPONS
E: ', response)
            print('Hi! I just woke up. Your llm is ending')
    
    
    async def ask_assistant(input:
 str) -> str:
        prompt = PromptTemplate.from_template(prompt_raw)
    
        prompt = prompt.partial(
          
  language='Spanish',
            tools=render_text_description(tools),
            tool_names=', '.join([t.name for t i
n tools]),
        )
    
        llm = ChatOpenAI(
            temperature=0,
            model_name='gpt-4',
         
   openai_api_key=os.environ['OPENAI_API_KEY'],
            callbacks=[MyCustomAsyncHandler()],
        )
    
        l
lm_with_stop = llm.bind(stop=['\nObservation'])
    
        agent = (
            {
                'input': lambda x: 
x['input'],
                'agent_scratchpad': lambda x: format_log_to_str(x['intermediate_steps']),
                'c
hat_history': lambda x: x['chat_history'],
            }
            | prompt
            | llm_with_stop
            | 
ReActSingleInputOutputParser()
        )
    
        agent_executor = AgentExecutor(
            agent=agent,
         
   tools=tools,
            verbose=True,
            memory=memory,
            max_execution_time=60,
            hand
le_parsing_errors=True,
        )
    
        with get_openai_callback() as cb:
            clara_ai_resp = await agent
_executor.ainvoke({'input': input})
            clara_ai_output = clara_ai_resp['output']
    
            print('CB: ',
 cb)
    
            return clara_ai_output, input, cb

&#x200B;
```
---

     
 
all -  [ Overwhelmed : Need advice ](https://www.reddit.com/r/csMajors/comments/1aexnzn/overwhelmed_need_advice/) , 2024-01-31-0910
```
So I am international students at mid level university in the US with good experience working at a Product based company
 back in my home country. I used to think my experience is good enough to quickly land me an internship or a full-time j
ob here.

Last 6 months have been went by adjusting, applying for 100s of jobs daily only to realise nothing is working.


I’ve realised there a lot of areas for improvement in my case which can help me.

1. Learning about LLMs, Gen AI and L
angchain (I have 3 years of experience in NLP and AWS but never worked on these advanced models)

2. Leetcode to improve
 python skills

3. Work on SQL and Tableau knowledge (my ultimate goal is to be in the NLP field but right now wanted a 
job ASAP so thought of learning it because it will open doors to many more job opportunities)

4. Work on projects using
 newer technologies.

5. Networking with people on LinkedIn

6. Applying for 20+ jobs daily

7. Complete certifications 
AWS, Tableau

I’ve realised doing this is definitely going to be a task considering classes have started again and it go
ing to be difficult to do all of this together making me feel quite overwhelmed.


How are you guys managing your time?


What do you think should be the right approach to go forward?
```
---

     
 
all -  [ In the era of GPT, building an effective word similarity search in 2023 ](https://www.reddit.com/r/LangChain/comments/1aevsuu/in_the_era_of_gpt_building_an_effective_word/) , 2024-01-31-0910
```
Hello everyone,

I am currently tackling a project that involves a list of various brand names within a specific domain.
 For instance:

`domain_names = ['xyz', 'yza', 'tra', 'world']`

My goal is to develop a search s capable of analyzing w
ord similarity. Specifically, the system should accept a word and return the top 'k' words that are most similar to it. 
I have experimented with OpenAI embeddings, particularly the latest Embedding Version 3 (3072 dimensions), but the resul
ts have been unsatisfactory.

Could someone suggest the most effective approaches for searching word-level similarities 
?In the era of GPT, Would it be advisable to train my own Word2Vec model?
```
---

     
 
all -  [ Load a recipe dataset with Foreign Tables and analyze it using LLMs with Embedded Python (Langchain  ](https://www.reddit.com/r/intersystems/comments/1aeuop1/load_a_recipe_dataset_with_foreign_tables_and/) , 2024-01-31-0910
```
📚 Dive into the world of #DataScience and language model with our latest article! Learn how to load a recipe dataset int
o #InterSystemsIRIS using Foreign Tables and analyze it using #LLMs with Embedded #Python 👇

[https://community.intersys
tems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-openai](https://com
munity.intersystems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-open
ai)

Explore the powerful combination of Langchain and OpenAI for a unique and insightful journey!

&#x200B;

https://pr
eview.redd.it/uzt2iz8h9mfc1.jpg?width=1920&format=pjpg&auto=webp&s=b849b2a95d204b24267d61ee7351db4b97f3be7e
```
---

     
 
all -  [ Load a recipe dataset with Foreign Tables and analyze it using LLMs with Embedded Python (Langchain  ](https://www.reddit.com/r/u_intersystemsdev/comments/1aeuo1o/load_a_recipe_dataset_with_foreign_tables_and/) , 2024-01-31-0910
```
📚 Dive into the world of #DataScience and language model with our latest article! Learn how to load a recipe dataset int
o #InterSystemsIRIS using Foreign Tables and analyze it using #LLMs with Embedded #Python 👇

https://community.intersyst
ems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-openai

Explore the 
powerful combination of Langchain and OpenAI for a unique and insightful journey!

&#x200B;

https://preview.redd.it/595
de18c9mfc1.jpg?width=1920&format=pjpg&auto=webp&s=0cb3050272392d7c6d1cbe6ef177126a2089cfaa
```
---

     
 
all -  [ Document Search And Retrieval Using RAG - powered by Langchain ](https://www.reddit.com/r/LangChain/comments/1aet9j9/document_search_and_retrieval_using_rag_powered/) , 2024-01-31-0910
```
[This Studio](https://lightning.ai/lightning-ai/studios/document-search-and-retrieval-using-rag) is a minimal reproducib
le pipeline to retrieve semantically similar documents based on the input query. The next step for this Studio involves 
connecting an LLM and engaging in a chat with your document through the retrieval pipeline.

***The retriever pipeline i
n this Studio is composed of the following components:***

* **Document Loader**:  Load the document (.txt, .pdf, .docx,
 .ppt) and perform text cleaning 
* **Text Splitter**: Split the document texts into multiple chunks 
* **Embedding Gene
ration**: Generate vector representation of text chunks
* **Vector database**: Embed and store each of the chunks and st
ore in a vector DB 
* **Retriever and Reranking**: Retrieve data based on query similarity

&#x200B;

https://preview.re
dd.it/idqetsa1zlfc1.png?width=3058&format=png&auto=webp&s=2a1b47eb6c477e7762bc745875cda45e9d08500e

[https://lightning.a
i/lightning-ai/studios/document-search-and-retrieval-using-rag](https://lightning.ai/lightning-ai/studios/document-searc
h-and-retrieval-using-rag)
```
---

     
 
all -  [ [Langchain] Besoin d'aide pour améliorer le chiffon ](https://www.reddit.com/r/redditenfrancais/comments/1aet2g4/langchain_besoin_daide_pour_améliorer_le_chiffon/) , 2024-01-31-0910
```
Bonjour à tous, je commence juste par le chiffon.

Je souhaite récupérer les informations sur les réglementations de con
struction (hauteur maximale, surface, etc.) des PDF à l'aide d'un LLM.

Le PDFS contient à la fois du texte et des donné
es. J'utilise actuellement PYPDFLoader de Langchain pour charger les PDF. Diffusion à l'aide de la division récursive de
s caractères, intégrant en utilisant une AI ouverte et en la stockant dans Chroma DB.
 

Parfois, le LLM ne récupére pas
 correctement les informations. Je ne sais pas si c'est à cause de l'analyse des PDF.

Toute aide à l'amélioration du sy
stème est grandement appréciée. Merci.

Traduit et reposté à partir de la publication 1abuv1f de la communauté langchain
. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ AutoCoder: A description-to-pull-request coding bot built with ActionWeaver, LlamaIndex and LangChai ](https://www.reddit.com/r/Langchaindev/comments/1aeqahm/autocoder_a_descriptiontopullrequest_coding_bot/) , 2024-01-31-0910
```
Hey folks, I want to share a side project I’ve been working on during weekends: AutoCoder! 👨‍💻👩‍💻

  
🤖 A description-to
-pull-request bot that can answer questions, and make code changes to Github repo through natural language instructions.
 It’s powered by LLM function calling and built with  
\- 🧠 [ActionWeaver](https://github.com/TengHu/ActionWeaver) for f
unction calling orchestration.  
\- 📚 [LlamaIndex](https://www.linkedin.com/company/llamaindex/) for RAG, including code
 chunking and advanced RAG technique like Hypothetical Document Embeddings!  
\- 🛠️ [LangSmith](https://www.langchain.co
m/langsmith) for powerful LLM tracing and debugging!  
\- API toolings from LangChain Community.  
It's incredible what 
a single developer can leverage existing AI libraries to create something like this in a short time!

Please checkout th
e codebase below 👇  
Github Repo: [https://github.com/TengHu/AutoCoder](https://github.com/TengHu/AutoCoder)

Thank you!

```
---

     
 
all -  [ AutoCoder: A description-to-pull-request coding bot built with ActionWeaver, LlamaIndex and LangChai ](https://www.reddit.com/r/OpenAIDev/comments/1aeqa50/autocoder_a_descriptiontopullrequest_coding_bot/) , 2024-01-31-0910
```
Hey folks, I want to share a side project I’ve been working on during weekends: AutoCoder! 👨‍💻👩‍💻

  
🤖 A description-to
-pull-request bot that can answer questions, and make code changes to Github repo through natural language instructions.
 It’s powered by LLM function calling and built with  
\- 🧠 [ActionWeaver](https://github.com/TengHu/ActionWeaver) for f
unction calling orchestration.  
\- 📚 [LlamaIndex](https://www.linkedin.com/company/llamaindex/) for RAG, including code
 chunking and advanced RAG technique like Hypothetical Document Embeddings!  
\- 🛠️ [LangSmith](https://www.langchain.co
m/langsmith) for powerful LLM tracing and debugging!  
\- API toolings from LangChain Community.

  
It's incredible wha
t a single developer can leverage existing AI libraries to create something like this in a short time!

Please checkout 
the codebase below 👇  
Github Repo: [https://github.com/TengHu/AutoCoder](https://github.com/TengHu/AutoCoder)

Thank yo
u!
```
---

     
 
all -  [ AutoCoder: A description-to-pull-request coding bot built with ActionWeaver, LlamaIndex and LangChai ](https://www.reddit.com/r/LangChain/comments/1aeq95t/autocoder_a_descriptiontopullrequest_coding_bot/) , 2024-01-31-0910
```
Hey folks, I want to share a side project I’ve been working on during weekends: AutoCoder! 👨‍💻👩‍💻  
🤖 A description-to-p
ull-request bot that can answer questions, and make code changes to Github repo through natural language instructions. I
t’s powered by LLM function calling and built with   
\- 🧠 [ActionWeaver](https://github.com/TengHu/ActionWeaver) for fu
nction calling orchestration.  
\- 📚 [LlamaIndex](https://www.linkedin.com/company/llamaindex/) for RAG, including code 
chunking and advanced RAG technique like Hypothetical Document Embeddings!  
\- 🛠️ [LangSmith](https://www.langchain.com
/langsmith) for powerful LLM tracing and debugging!   
\- API toolings from LangChain Community.  
It's incredible what 
a single developer can leverage existing AI libraries to create something like this in a short time! 

Please checkout t
he codebase below 👇  
Github Repo: [https://github.com/TengHu/AutoCoder](https://github.com/TengHu/AutoCoder)

Thank you
!
```
---

     
 
all -  [ Convert journal into a book ](https://www.reddit.com/r/LangChain/comments/1aepyv5/convert_journal_into_a_book/) , 2024-01-31-0910
```
Hi!

&#x200B;

I'm curious as to how I can convert approximately 200,000 words of journaling that I have done into a boo
k.  It's messy, unedited stuff that I've put down.  I just want to throw it into a database somehow and ask chatgpt to m
ake sense of it.  Is that something that is possible now?

&#x200B;

I think I need to put the content into a vector sto
re database somehow and use langchain to query it?  I wonder if there's just a desktop app or a LLM wrapper somewhere th
at can already do this.  Would love to be able to do this without having to learn python!

&#x200B;

Thanks for any wisd
om you guys can provide!
```
---

     
 
all -  [ Disruption of Tech | AI impact ](https://www.reddit.com/r/CATpreparation/comments/1aeps1q/disruption_of_tech_ai_impact/) , 2024-01-31-0910
```
Hi all
I am a software engineer and was really scared about the advancements in AI. Like GPT4 and LangChain and feels li
ke with time as the technology will grow and will get mature a major chunk of IT jobs will be eliminated.
So was thinkin
g to change my career path and persue a MBA?

What are your thoughts on this? Please help is doing MBA a right thing?
```
---

     
 
all -  [ ChromaDb with multiple collections and Agents ](https://www.reddit.com/r/LangChain/comments/1aej16x/chromadb_with_multiple_collections_and_agents/) , 2024-01-31-0910
```
Hello all again, 

I have a chromadb with thousands of images and documents, and i have some collections depending on so
me criteria i use on the different files i want to save, for example Financial\_Documents , Technical\_documents , Techn
ical\_Images etc. 

Now i want to chat with the LLM for these documents, for this i want the AI to search the db and the
 collections and return me some result for which we can have a conversation.

So my question is : how will the AI unders
tand when to search a specific collection? Also which agent is best for such a task?

Thank you in advance.
```
---

     
 
all -  [ [Question]: How to increase the limit on length of generated text of open source huggingface LLM: ze ](https://www.reddit.com/r/huggingface/comments/1aehymv/question_how_to_increase_the_limit_on_length_of/) , 2024-01-31-0910
```
* I'm using ChatHuggingFace to create an Agent.
* But facing an issue with the length of the generated text
* The length
 limit is too short. 
* Can someone pls tell me how do we control the output length of the open source HF endpoints? 
* 
These are the configs of my model:  
`from langchain_community.llms import HuggingFaceHub`  
`llm = HuggingFaceHub(`  
 
`repo_id='HuggingFaceH4/zephyr-7b-beta',`  
 `task='text-generation',`  
 `huggingfacehub_api_token='xxxxxxx',`  
 `mode
l_kwargs={`  
 `'max_new_tokens': 512,`  
 `'top_k': 50,`  
 `'temperature': 0.1,`  
 `'repetition_penalty': 1.03,`  
`}
,`  
`)`

Below is the screenshot of what is happening, there should be more text after 'Final answer'

https://preview.
redd.it/vygb9lpfuifc1.png?width=1553&format=png&auto=webp&s=7262604c3bc6c86a197268b81df1f561d4ad7a00
```
---

     
 
all -  [ Sequential Chain ](https://www.reddit.com/r/LangChain/comments/1aefwi8/sequential_chain/) , 2024-01-31-0910
```
Hi everyone! I am a newbie to Langchain amd just want to ask for sequential chains, is there another way (besides introd
ucing callbacks) to reduce error propagation of the model’s output 
from one chain to the next? For example, of the outp
ut from the first chain is wrong, then it will be passed to the next chain and affects the subsequent responses. Thank y
ou!
```
---

     
 
all -  [ Looking for ideas on how to code gen a 100,000 token refactor ](https://www.reddit.com/r/LangChain/comments/1aedmys/looking_for_ideas_on_how_to_code_gen_a_100000/) , 2024-01-31-0910
```
I noticed that GPT-4 turbo is great with tons of context. However, the output I get is too limited to rewrite all 100,00
0 input tokens. I'm trying to find a strategy that would allow me to take a legacy code base and have the LLM rewrite th
e entire thing. 
I tried a test to see if I could get ChatGPT to generate part of the result until it hits its token lim
it and then continue when I say next, but it doesn't seem to totally follow the instructions. 
See the smoke test here:

https://chat.openai.com/share/19c19e6c-0adf-4087-b83b-affe5886498e

I think it would be cool to use this approach to rew
rite old code to use LCEL, for example.

Any ideas?
```
---

     
 
all -  [ Free internet research tools? ](https://www.reddit.com/r/LangChain/comments/1ae7y59/free_internet_research_tools/) , 2024-01-31-0910
```
Are there any research tools available to do research on the internet for free? Has anyone had any good or bad experienc
es with this type of task?
```
---

     
 
all -  [ RAG for documents with chapters and sub-chapters ](https://www.reddit.com/r/LangChain/comments/1ae3urf/rag_for_documents_with_chapters_and_subchapters/) , 2024-01-31-0910
```
I want to implement RAG for a 100 pages document that has a hierarchical structure of chapters, sub-chapters, etc. There
fore I chunk the document into smaller paragraphs. In many cases, a chunk within a sub-chapter makes only sense in the c
ontext of the title of the sub-chapter, e.g. (6.1 Method ABC, 6.1.1 Disadvantages).

I wonder what are the most common a
pproaches in RAG to handle hierarchical structures, which are very common in longer documents?
```
---

     
 
all -  [ How to Install LangChain ](https://www.reddit.com/r/ArtificialInteligence/comments/1ae263u/how_to_install_langchain/) , 2024-01-31-0910
```
LangChain is an open source conversational AI assistant created by Anthropic. It allows you to have natural language con
versations powered by large language models.  
  
Installing LangChain on your own machine takes just a few simple ste
ps.

https://www.successtechservices.com/how-to-install-langchain/
```
---

     
 
all -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-01-31-0910
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
 
all -  [ Integration of Supabase SSR Auth with Next.js 14 and MUI for Styling ](https://www.reddit.com/r/Supabase/comments/1ady2pp/integration_of_supabase_ssr_auth_with_nextjs_14/) , 2024-01-31-0910
```
Hello everyone,

I've put together a project that demonstrates a straightforward integration of Supabase's server-side r
endering authentication with Next.js 14, using Material-UI for styling. It's a basic setup intended to help those lookin
g to implement Supabase auth in a Next.js environment with an emphasis on simplicity.

**Key Aspects:**

* Uses Supabase
 for authentication.
* Implements server-side rendering in Next.js 14.
* Applies Material-UI for the styling component.


**Getting Started:**

The repository includes everything from setting up your Supabase and Next.js project to running t
he application. It covers:

* Setting up a Supabase account and a Next.js project.
* Detailed installation instructions.

* Configuring your database and environment variables for the project.

**Purpose of the Project:**

This project aims 
to provide a simple example of integrating Supabase's authentication with Next.js's server-side rendering capabilities, 
using Material-UI for a bit of styling. It's meant to be a starting point for anyone looking to explore these technologi
es together.

**Looking for Feedback:**

I’m interested in any suggestions or contributions to make this integration exa
mple more helpful for developers starting with Supabase and Next.js. You can find the project here: [GitHub - SupabaseAu
thWithSSR](https://github.com/ElectricCodeGuy/SupabaseAuthWithSSR).

Feel free to check out the project and share your t
houghts or questions.

&#x200B;

**Question:**

I'm considering putting together a tutorial on using LangChain and OpenA
I's ChatGPT model for building a chat application, with Redis handling the conversation storage. This setup aims to demo
nstrate a practical application of AI and efficient data storage. Would this be of interest, or are there specific aspec
ts of integrating these technologies you'd like to explore? Feedback and suggestions are welcome.
```
---

     
 
all -  [ good starting points for a new project involving chains of LLM operations ](https://www.reddit.com/r/LangChain/comments/1adxilw/good_starting_points_for_a_new_project_involving/) , 2024-01-31-0910
```
what are some good notebooks or repos that i could use to start playing around with a system that chains together multip
le operations including RAG operation?

i want in the end to have a system that does the following:

input -> enters som
e LLM that outputs another text -> retrieve some documents and output multiple different texts -> for each of the output
ted texts go through another LLM

i know it shouldn't be very complicated but i have a hard time getting started and i d
on't see anything that does that but I'm sure it exists.  


specifically, i don't see anywhere an example of a chain th
at passes the output of an LLM as the input to another LLM instance
```
---

     
 
all -  [ Why does it seem prompt testing is hard? Is it data formatting? Or the actual testing? ](https://www.reddit.com/r/LangChain/comments/1adx6ny/why_does_it_seem_prompt_testing_is_hard_is_it/) , 2024-01-31-0910
```
I can write the code, but it seems all-over-the-place. Not very reusable.

I like my csv, but the world likes their json
s formatted in alpeca/openAI/mistral/(did I miss any?). 

When you do the final comparison between your model's output a
nd the correct answer, you are doing this in a dataframe/csv. 

When you run multiple rounds of prompt testings, I suppo
se I could flatten this each time. 

What does langchain do for this?
```
---

     
 
all -  [ LCEL - Citations chain with chat history ](https://www.reddit.com/r/LangChain/comments/1advsq8/lcel_citations_chain_with_chat_history/) , 2024-01-31-0910
```
Hey, I'm trying to use these two guides from the Langchain documentation:

\- [https://python.langchain.com/docs/use\_ca
ses/question\_answering/citations](https://python.langchain.com/docs/use_cases/question_answering/citations)

\- [https:
//python.langchain.com/docs/use\_cases/question\_answering/chat\_history](https://python.langchain.com/docs/use_cases/qu
estion_answering/chat_history)

 to create a chain that will return structured output with citations but also will accep
t chat\_history. 

Has anyone managed to create something similar using LCEL? 

&#x200B;
```
---

     
 
all -  [ ChatPromptTemplate keeps telling me I have 2 arguments ](https://www.reddit.com/r/LangChain/comments/1adu5e9/chatprompttemplate_keeps_telling_me_i_have_2/) , 2024-01-31-0910
```
I have qa pairs like 
```
# Example question-answer pairs
qa_pairs = [
    {'question': 'Who leads the rebellion in 'Ani
mal Farm'?', 'answer': 'The pigs, specially Snowball and Napoleon, leads the rebellion.'},
    {'question': 'What is the
 main theme of 'Animal Farm'?', 'answer': 'The main theme are the corruption of power.'},
    {'question': 'What happens
 to Boxer in the novel?', 'answer': 'Boxer is send to a slaughterhouse by the pigs.'}
]
```
Then I'm trying to iterate t
hem like 
```
def create_grading_prompt(qa_pair):
    return [
        ('system', 'You are a helpful AI bot. Your name i
s {name}.'),
        ('human', f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\n\nPlease grade the gramma
r of the answer based on the following rubric:\n{grammar_rubric}')
    ]

# Process each question-answer pair
for qa_pai
r in qa_pairs:
    grammar_and_grading_chain = SequentialChain([
        ChatPromptTemplate.from_messages(create_grading
_prompt(qa_pair)),
        llm,
        StrOutputParser()
    ])
    result = grammar_and_grading_chain.invoke(qa_pair)

    print(f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\nGrade: {result}\n')
```
throws
```
{
	'name': 
'TypeError',
	'message': 'Serializable.__init__() takes 1 positional argument but 2 were given',
	'stack': '------------
---------------------------------------------------------------
TypeError                                 Traceback (mos
t recent call last)
Cell In[6], line 9
      7 # Process each question-answer pair
      8 for qa_pair in qa_pairs:
----
> 9     grammar_and_grading_chain = SequentialChain([
     10         ChatPromptTemplate.from_messages(create_grading_pr
ompt(qa_pair)),
     11         llm,
     12         StrOutputParser()
     13     ])
     14     result = grammar_and_g
rading_chain.invoke(qa_pair)
     15     print(f\'Question: {qa_pair['question']}\
Answer: {qa_pair['answer']}\
Grade: {
result}\
\')

TypeError: Serializable.__init__() takes 1 positional argument but 2 were given'
}
```
because my previous
 try was throwing this same error.
My previous try
```
grammar_and_grading_chain = SequentialChain([
    ChatPromptTempl
ate(lambda qa_pair: f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\n\nPlease grade the grammar of the an
swer based on the following rubric:\n{grammar_rubric}'),
    llm,
    StrOutputParser()
])


# Process each question-ans
wer pair
for qa_pair in qa_pairs:
    result = grammar_and_grading_chain.invoke(qa_pair)
    print(f'Question: {qa_pair[
'question']}\nAnswer: {qa_pair['answer']}\nGrade: {result}\n')
```
I looked at documentation here: https://api.python.la
ngchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#
and don't understand what I'm doing w
rong.
```
---

     
 
all -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-01-31-0910
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1adtarm/for_hire_programmerweb_developerit_consultant/) , 2024-01-31-0910
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of programming and
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

Satisfied customers:

https://www.reddit.com/r/testimonia
ls/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsd
ze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_grea
t_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_hones
t_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https:/
/www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Please note: I am not a de
signer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Navigating a Career Comeback After a Break – Seeking Guidance and Opportunities! ](https://www.reddit.com/r/ADHD_Programmers/comments/1adr98l/navigating_a_career_comeback_after_a_break/) , 2024-01-31-0910
```
**TLDR:** After freelancing, I took a break due to mental health challenges, and now I'm struggling to re-enter the job 
market. Seeking advice on overcoming skill gaps, getting remote opportunities, and battling job market uncertainties.

*
*Introduction:**
Hey everyone,

I'm reaching out for guidance and support as I stand at a career crossroads. My journey 
in the tech industry includes experience in Machine Learning, remote subcontracting for a Fortune 10 company, and freela
ncing. However, unexpected life challenges led to a break for personal matters, including supporting ailing family membe
rs and constructing my house.

**Career Snapshot:**

- Sabbatical (1.5 years)

- **Machine Learning Consultant (1.5 year
s):**
  - Contributed to ML team's impact through effective MLOps implementation.
  - Developed a real-time liveness ser
vice with face detection, achieving low-latency performance.
  - Transitioned from individual notebooks to modularized s
cripts for a smoother development process.

- **Analytics ETL Engineer - Fortune 500 (Remote) (1.5 years) (Subcontractin
g):**
  - Automated In-Process Quality Control (IPQC) Audit, enhancing quality control.
  - Designed Tableau dashboards 
for dynamic manufacturing data, saving 200 hours weekly.

- **Internships in few MNC companies after college (1 year)**


**Break, Challenges, and ADHD Diagnosis:**
After a successful freelancing period, I took a break in June 2022 for menta
l health reasons. Recently diagnosed with ADHD, the inattentive subtype has posed significant challenges in my daily lif
e. Despite the productive break, returning to the industry has become daunting due to uncertainties in the job market an
d the struggle with skill gaps exacerbated by ADHD-related difficulties.

**Options and Seeking Guidance:**
- [x] Reache
d out to Previous clients and friends - No current opportunities.
- [ ] Considering applying to job portals for full-tim
e or contract jobs (Remote/Out of India).
- [ ] Exploring referrals but struggling with leetcode and revising Data Scien
ce concepts.
- [ ] Hesitant about gigs on freelancing platforms due to concerns about a race to the bottom.


**Neurodiv
ersity Hiring Programs in India:**
Considering my recent ADHD diagnosis, I'm contemplating whether to apply for hiring p
rograms for neurodivergent individuals, such as Microsoft's Neurodiversity hiring initiative in India. Any insights or a
dvice on this would be greatly appreciated.

**Seeking Advice:**
Am I being delusional to hope for a remote overseas job
 soon, given the current job market challenges? I'm open to any advice, insights, or recommendations on how to navigate 
this phase and make a successful comeback. I've shared my technical background and projects below to provide a comprehen
sive view.

**Skills:**

| **Skill Category**    | **Skills**                                                           
                                                                                                |
|---------------------
---|--------------------------------------------------------------------------------------------------------------------
---------------------------------------------------|
| Programming Languages  | Python                                  
                                                                                                                        
      |
| Visualization          | Tableau, Matplotlib, Folium                                                          
                                                                               |
| Operating Systems      | MacOS, Linux
 (Debian), Windows                                                                                                      
                               |
| Databases              | MySQL                                                       
                                                                                                         |
| DevOps/Tool
s           | CI/CD (GitHub Actions), Docker, Apache Airflow, Streamlit                                                 
                                                          |
| Other                  | Git, NLP, Scikit-Learn, TensorFlo
w, Cloud (GCP, AWS), Weights & Biases, Langchain, Sagemaker, Pandas, Numpy, Jupyter, DLib, OpenCV, Hydra                
               |

**Additional Personal Projects:**

| **Project**                                | **Description**     
                                                                                                                        
                       |
|--------------------------------------------|-------------------------------------------------
-------------------------------------------------------------------------------------------------------------------|
| I
mage Classification Telegram bot         | Developed an end-to-end image classification system with TensorFlow, deployed
 on Telegram. Improved F1 score by 20%, implemented MLOps workflow, and CI/CD pipeline.  |
| Object detection & classifi
cation Webapp  | Implemented object detection with TensorFlow and OCR using TesseractOCR. Deployed on Google Cloud Platf
orm, with a Streamlit front-end and Docker.                    |
| Idea Generation                            | Used Ope
nAI API for idea generation and Streamlit for pain point analysis.                                                      
                                      |
| Other Projects                             | Undertook diverse projects, inclu
ding a Pneumonia Prediction Dashboard, and facial landmark detection using various technologies and OpenAI.          |


**Conclusion:**
I appreciate your time in reading my story. If you have any advice, job leads, or can point me in the ri
ght direction, please feel free to share. I'm determined to make a successful comeback and contribute meaningfully to th
e tech community.

*Note: I made the decision to take a break after ensuring I had enough savings to survive. However, I
 never anticipated that depression would amplify the challenges posed by ADHD. I am honestly unsure how to seek help or 
ask for referrals.*

Thank you!
```
---

     
 
all -  [ Navigating a Career Comeback After a Break – Seeking Guidance and Opportunities! ](https://www.reddit.com/r/cscareerquestions/comments/1adqzx0/navigating_a_career_comeback_after_a_break/) , 2024-01-31-0910
```
**TLDR:** Started freelancing right after internship, took a break for personal reasons, and struggling to re-enter the 
job market. Seeking advice on overcoming skill gaps, getting remote opportunities, and battling job market uncertainties
.

**Introduction:** Hey everyone,

I'm reaching out to seek guidance and support as I find myself at a crossroads in my
 career. I'm from India & had a unique journey in the tech industry. I've gathered experience in Machine Learning, worke
d remotely as a subcontractor for a Fortune 10 company, and even ventured into freelancing. However, life threw some une
xpected challenges my way, and I had to take a break to attend to personal matters, including supporting an ailing famil
y member and constructing my house.

**Career Snapshot:**

* **Sabbatical (1.5 years)**
* **Machine Learning Consultant 
(1.5 years):**
   * As a Machine Learning Consultant, I played a key role in supporting and expanding the ML team's impa
ct across the company through effective MLOps implementation.
   * I created a real-time liveness service incorporating 
face detection, achieving remarkable low-latency performance.
   * To enhance efficiency, I facilitated a smoother devel
opment process by transitioning from individual notebooks to modularized scripts.
* **Analytics ETL Engineer - Fortune 5
00 (Remote) (1.5 years) (Subcontracting):**
   * Automated In-Process Quality Control (IPQC) Audit, enhancing quality co
ntrol.
   * Designed Tableau dashboards for dynamic manufacturing data, saving 200 hours weekly.
* **A few internships i
n MNC companies after college (1 year)**

**Break and Challenges:** After freelancing successfully, I took a break in Ju
ne 2022 to focus on my mental health. Despite the productive period, I'm now facing challenges getting back into the ind
ustry. I've explored different options, such as reaching out to previous clients, practicing DSA, and considering freela
ncing platforms. However, uncertainties about the job market and skill gaps are making the process daunting.

**Options 
and Seeking Guidance:**

\- \[x\] Reached out to Previous clients and friends - No current opportunities.

\- \[ \] Cons
idering applying to job portals for full-time or contract jobs (Remote/Out of India).

\- \[ \] Exploring referrals but 
struggling with leetcode and revising Data Science concepts.

\- \[ \] Hesitant about gigs on freelancing platforms due 
to concerns about a race to the bottom.

**Seeking Advice:** Am I being delusional to hope for a remote overseas job soo
n, given the current job market challenges? I'm open to any advice, insights, or recommendations on how to navigate this
 phase and make a successful comeback. I've shared my technical background and projects below to provide a comprehensive
 view.

**Skills:**

|**Skill Category**|**Skills**|
|:-|:-|
|Programming Languages|Python|
|Visualization|Tableau, Matp
lotlib, Folium|
|Operating Systems|MacOS, Linux (Debian), Windows|
|Databases|MySQL|
|DevOps/Tools|CI/CD (GitHub Actions
), Docker, Apache Airflow, Streamlit|
|Other|Git, NLP, Scikit-Learn, TensorFlow, Cloud (GCP, AWS), Weights & Biases, Lan
gchain, Sagemaker, Pandas, Numpy, Jupyter, DLib, OpenCV, Hydra|

**Additional Personal Projects:**

|**Project**|**Descr
iption**|
|:-|:-|
|**Image Classification Telegram bot**|Developed an end to end image classification system with Tensor
Flow, deployed on Telegram. Improved F1 score by 20%, implemented MLOps workflow, and CI/CD pipeline.|
|**Object detecti
on & classification Webapp**|Implemented object detection with TensorFlow and OCR using TesseractOCR. Deployed on Google
 Cloud Platform, with a Streamlit front-end and Docker.|
|**Idea Generation**|Used OpenAI API for idea generation and St
reamlit for pain point analysis.|
|**Other Projects**|Undertook diverse projects, including a Covid-19 X-ray Prediction 
Dashboard, MyCryptoPal, and facial landmark detection using various technologies and OpenAI.|

**Conclusion:** I appreci
ate your time in reading my story. If you have any advice, job leads, or can point me in the right direction, please fee
l free to share. I'm determined to make a successful comeback and contribute meaningfully to the tech community.

Thank 
you!
```
---

     
 
all -  [ Speed up Agents ](https://www.reddit.com/r/LangChain/comments/1adqrwj/speed_up_agents/) , 2024-01-31-0910
```
Hi everybody!

I'm currently developing some agents on Langchain for many purpose.
Some are just documents analysis or d
ata extraction from documents, and other are more Chatbot Rag based
The first category are not really agents, they are r
efine chain (a bit modified from the LCEL turo one) + stuff one
And the second is Langchain Agents (ZeroShotPrompt)

Bot
h run with GPT4

But here is the thing :

For the first category, as the pdf can goes to 5 to 20 pages, my agents take s
everal minutes to handle them
Also, I remarqued that the more I put a defined structure in the prompt to extracr informa
tion, the more it is long (can go up to 10min)

And for the second category, as there is a multi query retrieval Generat
ion based on pinecone, it also take 1 min  before generation.

I look for conceptual way to explain that.
We see a lot o
f agent out there which are more fast 

- is it the framework Langchain that slow down everything?
- is I had a local mo
del would it be faster ?
- is because of the Rag too complex?
- how could I drastically shorten my prompt but keeping cl
ear schema for data extraction?


Thanks you all for your help !
```
---

     
 
all -  [ Language switching for tools ](https://www.reddit.com/r/Langchaindev/comments/1adpwif/language_switching_for_tools/) , 2024-01-31-0910
```
I'm trying to use langchain with GPT for a search tool. The search database query has a language code (en or zh) and whe
n the tool is used, the language code is determined from the user query.

How can I get langchain to run the tool twice 
- in all available language codes translating the user query when necessary and compare the search content and get the m
ost appropriate one before returning an answer? 

Does this need to be done via the prompt or a more programmatic approa
ch?
```
---

     
 
all -  [ Anukool: My job hunting assistant ](https://www.reddit.com/r/opensource/comments/1adpfah/anukool_my_job_hunting_assistant/) , 2024-01-31-0910
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. Consequently, I developed Anu
kool under the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as 
well. Since I'm new to ML and LLM, any advice or feedback is greatly appreciated, and contributions are also welcome. I 
plan to utilize Llama-2 soon to further open-source the project.

Check out the GitHub link, and please star it if you f
ind the project interesting: https://github.com/dakshesh14/anukool
```
---

     
 
all -  [ Chat UI with RAG ](https://www.reddit.com/r/OpenAI/comments/1adfira/chat_ui_with_rag/) , 2024-01-31-0910
```
is there a website or tool that lets you chat with pdfs or other text files like chatgpt? Unfortunately Librechat can't 
do this as far as I know or at least not yet. And I mean not chat with pdfs websites, I want a normal chat interface tha
t also is able to interact with pdfs if needed, and I'd like to use my own API key.

I was thinking trying to build some
thing like this myself but it's not that easy. You'd need some sort of agent that is called when asked. That whole langc
hain framework got annoyingly clustered with functions..
 
thanks
```
---

     
 
all -  [ Looking for a production level vector db ](https://www.reddit.com/r/LangChain/comments/1adf3o6/looking_for_a_production_level_vector_db/) , 2024-01-31-0910
```
Im looking for a production level vector db, so I was thinking about plain pg + pgvector, the problem is that I can't fi
nd an easy way of finding a good library to interact with it, so far I'm using raw queries like this (i will leave code 
at the bottom). I don't know if this is the best way apart from chroma, weaviate, pinecone, etc etc this is going to be 
at production level por mi company to be used internally.  
WITH vector\_matches AS (  
SELECT document\_id, 1 - (embedd
ing <=> %s) AS similarity  
FROM documents\_embeddings  
WHERE 1 - (embedding <=> %s) > %s  
ORDER BY similarity DESC  

LIMIT %s  
)  
SELECT d.page\_content, d.metadata, d.file\_id, vm.similarity  
FROM documents d  
INNER JOIN vector\_mat
ches vm ON d.id = vm.document\_id  


&#x200B;
```
---

     
 
all -  [ HackerNews AI built using function calling ](https://www.reddit.com/r/LangChain/comments/1adarpa/hackernews_ai_built_using_function_calling/) , 2024-01-31-0910
```
Hi reddit, I built an AI that can interact with the Hacker News API: [https://hn.aidev.run](https://hn.aidev.run)

You c
an ask questions like:

* What's on hackernews about AI?
* What's on hackernews about iPhone?
* What's trending on hacke
rnews?
* What are users showing on hackernews?
* What are users asking on hackernews?
* Summarize this story: [https://n
ews.ycombinator.com/item?id=39156778](https://news.ycombinator.com/item?id=39156778)

It uses function calling to query 
the HN api.

To answer questions about a particular topic, it’ll search its knowledge base (a vector db that is periodic
ally updated with the “top stories”) and get details about those stories from the API.

This is pretty barebones and I b
uilt it today in < 2 hours, so it probably won’t meet your high standards. If you give it a try, I’d love your feedback 
on how I can improve it.

If you’re interested, I built this using [phidata](https://github.com/phidatahq/phidata)

Than
ks for reading and would love to hear what you think.
```
---

     
 
all -  [ Why separate langchain and langchain_core for python package ](https://www.reddit.com/r/LangChain/comments/1ad9x8c/why_separate_langchain_and_langchain_core_for/) , 2024-01-31-0910
```
Hey, I'm trying to familiarize myself with the internals of the langchain python package, I noticed that langchain and l
angchain\_core are separated and in the internal code they have similar sub packages. my question is what is the need fo
r this separation and what is the thought process behind what should be implemented in langchain vs langchain\_core. Tha
nks
```
---

     
 
all -  [ What is the best on-prem vector db ](https://www.reddit.com/r/LangChain/comments/1ad52as/what_is_the_best_onprem_vector_db/) , 2024-01-31-0910
```
I'm building an app using LangChain to integrate with ChatGPT. I need a vector DB to store the embeddings. I want to use
 an on-prem option, not a cloud one. There are quite a few options I see from my searches. Wondering what folks would re
commend. Thanks.
```
---

     
 
all -  [ Use HTML splitter for JSX (React) code? ](https://www.reddit.com/r/LangChain/comments/1ad4eye/use_html_splitter_for_jsx_react_code/) , 2024-01-31-0910
```
I am creating a chatbot over the data of my **static React website**.

I fetch the page files from the file system using
 the [DirectoryLoader](https://js.langchain.com/docs/modules/data_connection/document_loaders/file_directory). I could u
se a web loader but I want it to work even in local development.

The issue is the text splitter.

I couldn't find a pro
per text splitter for JSX (React) code. But I seem to get decent results with the [HTML recursive text splitter](https:/
/js.langchain.com/docs/modules/data_connection/document_transformers/code_splitter#html), probably because JSX and HTML 
are so similar.

Before I send my documents to the HTML splitter, I **remove all import statements and class names** (to
 get rid of the unnecessary clutter). I keep everything else (which might include some JavaScript code).

Is my approach
 fine? Is the HTML splitter suited for this use case? Is it normal that there is no text overlap in the generated docume
nts?
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-31-0910
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-31-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-31-0910
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-31-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-31-0910
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-31-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
