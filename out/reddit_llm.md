 
all -  [ Which one is better to analyze structured data with Python? LangChain vs Assistant API? ](https://www.reddit.com/r/LangChain/comments/1eobhzd/which_one_is_better_to_analyze_structured_data/) , 2024-08-10-0911
```
I was wondering if anybody ever did a comparison to analzye structured data with LangChain vs New Assistant API? I've ob
served the following, but I am not clear which one to use. I am using `create_pandas_dataframe_agent()` for LangChain an
d AzureOpenAI `code_interpreter`  for assistants API, both with same llm models.

  
1. LangChain is much faster (almost
 50% faster)

2. Code Interpreter has additional cost (cost is minimal)

3. LangChain with Python displays the Thoughts,
 Action and Python code it executes. But with Assistants API, I couldn't find a way to display the code it executes (whi
ch  is heavy downside, as I could look into the code to validate the answer generated)

4. Assistants API tends to be sl
ightly more accurate.

Did anyone make a comparison and observed the same? or observed something else?

I cannot decide 
which one I should choose for my project, I have a large set of structured data which I need to query. 
```
---

     
 
all -  [ How can I create a pipeline that will efficiently exhaust an input of 10k size and store the results ](https://www.reddit.com/r/LangChain/comments/1eoap0d/how_can_i_create_a_pipeline_that_will_efficiently/) , 2024-08-10-0911
```
Hello there! I'm a Python programmer, new to LangChain and AI development in general.

  
I'm getting familiarized with 
the components and LCEL but I could not find a way to do what I'm looking for.

What I have:

* 10k documents (I know wh
ich loader to use already)
* Some documents are too long and must be split (I know which splitter to use already)
* A si
ngle prompt that will include the results of the split documents
* I want to call OpenAI with these
* I'm expecting a si
ngle result for each chunk. Already using the new structured output from OpenAI.
* I want to store the results in a data
base.

The question is: how could I do this in such a way that the documents are 'lazy loaded' and each one of them goes
 through some sort of pipeline, generating lists of 1 or more chunks, each chunk is then embedded into the prompt, then 
sent to OpenAI, then I could call a function to save the result into the database?

Every example I've seen takes a list
 of 'inputs' to \`invoke\`, but I want a pipeline that will exhaust all the inputs (the documents) with some acceptable 
level of parallelization.
```
---

     
 
all -  [ I USED AI TO AUTOMATICALLY APPLY FOR 1000 JOBS - AND I GOT 50 INTERVIEWS! ](https://www.reddit.com/r/LangChain/comments/1eoa1fr/i_used_ai_to_automatically_apply_for_1000_jobs/) , 2024-08-10-0911
```
# How Did I Do It?

I created an AI bot that:

* Analyzes candidate information
* Examines job descriptions
* Generates 
unique CVs and cover letters for each job
* Answers specific questions that recruiters ask
* Automatically applies to jo
bs

And all of this while I was sleeping! In just one month, this method helped me secure around 50 interviews. The tail
ored CVs and cover letters, customized based on each job description, made a significant difference.

# AI is Changing t
he Game

Artificial intelligence is rapidly reshaping the recruiting landscape:

* Job seekers can optimize their CVs in
 seconds
* Cover letters are crafted with a click
* Perfect matching between skills and job offers
* Recruiters are usin
g automated screening systems

This method is incredibly effective at passing through automated screening systems. By ge
nerating CVs and cover letters tailored to each job description, my script significantly increases the chances of gettin
g noticed by both AI and human recruiters.

# Questions for the Future

* Will human recruiters become obsolete?
* How w
ill we distinguish real talent in a sea of seemingly perfect applications?
* Are we entering an 'AI arms race' in recrui
ting?

# Soft Skills: The New Differentiator?

In a world of AI-optimized applications:

* Empathy
* Creativity
* Critic
al thinking

Could become the real distinguishing factors.

# Personal Reflection

Observing this technological revoluti
on, I can't help but reflect on the profound implications for the world of work. While efficient, the automation of job 
applications raises questions about the very nature of professional relationships. We face a paradox: as we seek to opti
mize the selection process, we risk losing the human element that often makes a difference in a work environment. The ch
allenge ahead is not just technological, but also ethical and social. We'll need to find a delicate balance between the 
efficiency of artificial intelligence and the richness of human interactions. Only then can we build a future of work th
at is not just productive, but also fulfilling and meaningful for everyone.

# Want to Try This Magic?

Here's what it d
oes:

* Enter your professional background
* It generates tailored CVs, cover letters, and responses
* Sends hundreds of
 applications while you enjoy a coffee

Curious? Try it here: [GitHub Project](https://github.com/feder-cr/linkedIn_auto
_jobs_applier_with_AI)

(My project is completely free and open source, unlike other similar services that cost a lot an
d offer very little value. Since it’s still in beta, every star on GitHub is a huge encouragement to keep developing it!
)

**P.S.** Remember: with great power of AI comes great responsibility. Let's use it ethically!
```
---

     
 
all -  [ create_sql_agent make error in syntax of SQL query ](https://www.reddit.com/r/LangChain/comments/1eo7n5n/create_sql_agent_make_error_in_syntax_of_sql_query/) , 2024-08-10-0911
```
how to handle errors please guide

[https://python.langchain.com/v0.1/docs/use\_cases/sql/agents/](https://python.langch
ain.com/v0.1/docs/use_cases/sql/agents/)
```
---

     
 
all -  [ [0 YoE, Intern at mid sized startup, Masters in AI/ML at T30 Uni, Asia] - Roast my CV so I could cry ](https://i.redd.it/zj4axu9g1ohd1.jpeg) , 2024-08-10-0911
```
Just finished my 2nd year at uni and got an internship at mid sized startup. I eventually want to get a Masters at a top
 30 University. But considering that I live in a 3rd world country and have internships at insignificant places doesn't 
help much. Any tips on how I could get a good internship next summer and would be great if I could tips on what top univ
ersities check for Masters degree.
```
---

     
 
all -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/learnmachinelearning/comments/1eo44vz/how_to_build_your_retrieval_augmented_generation/) , 2024-08-10-0911
```



TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini,
 Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running
 locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://c
odecompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
all -  [ How to limit chat history to be sent to the LLM ](https://www.reddit.com/r/LangChain/comments/1eo3fhd/how_to_limit_chat_history_to_be_sent_to_the_llm/) , 2024-08-10-0911
```
Hey guys I’m working on a RAG application and everything is working smoothly with memory and storing in database. What I
 am trying to do is how can I pass like 10 messages only to the llm instead of the entire chat history while still stori
ng every response in the database. 
```
---

     
 
all -  [ his guide will show you how to use LangChain and Langflow ](https://genedarocha.substack.com/p/144-how-to-create-products-using) , 2024-08-10-0911
```
his guide will show you how to use LangChain and Langflow. You'll learn how to build products that use the latest in nat
ural language processing and generation.
https://vist.ly/3ddcj
'
```
---

     
 
all -  [ How to work with langchain pdf loader? ](https://www.reddit.com/r/learnmachinelearning/comments/1eo2as5/how_to_work_with_langchain_pdf_loader/) , 2024-08-10-0911
```
I've been given a task to use langchain pdf loader to create a dataset on llama 3.1 where input is a document and a bit 
of instructions. It is for a prediction tool in geographical sciences. Can someone guide me through the process of how? 
Steps? Easier way?
```
---

     
 
all -  [ Suggestion to implement a Q&A RAG on CSV files         ](https://www.reddit.com/r/developersIndia/comments/1eo23hr/suggestion_to_implement_a_qa_rag_on_csv_files/) , 2024-08-10-0911
```
Can someone suggest any good resources on how to perform Q&A on a csv file using langchain.
```
---

     
 
all -  [ Admin for vector databases ](https://www.reddit.com/r/LangChain/comments/1enyme7/admin_for_vector_databases/) , 2024-08-10-0911
```
Hi all! I've worked with vector dbs for creating RAGs, and of course I did all the processing, chunking, embedding, etc.
 through code. Now I have a project that requires quite a lot of document updating and I was wondering if they were any 
good open source admins that could manage the documents CRUD.

Even big solutions like Pinecone or Weaviate doesn't seem
 to have this solved (I could be mistaken).

I would appreciate any advice.
```
---

     
 
all -  [ Langgraph memory saver for sql? ](https://www.reddit.com/r/LangChain/comments/1enx32e/langgraph_memory_saver_for_sql/) , 2024-08-10-0911
```
On langgraph doc there is examples on how to setup a checkpointer for storing graph state. This is done using a saver fo
r sqlite. What about I wanna use an sql database created on google cloud? what about google big query for example? 
```
---

     
 
all -  [ An extensive open-source collection of RAG implementations with many different strategies  ](https://www.reddit.com/r/LangChain/comments/1envyoh/an_extensive_opensource_collection_of_rag/) , 2024-08-10-0911
```
Hi all,

Sharing a repo I was working on for a while. 

It’s open-source and includes many different strategies for RAG 
(currently 17), including tutorials, and visualizations.

This is great learning and reference material.  
Open issues, 
suggest more strategies, and use as needed.

Enjoy!

[https://github.com/NirDiamant/RAG\_Techniques](https://github.com/
NirDiamant/RAG_Techniques)
```
---

     
 
all -  [ Tool Calling in LLamacpp with Langchain ](https://www.reddit.com/r/LangChain/comments/1envxee/tool_calling_in_llamacpp_with_langchain/) , 2024-08-10-0911
```
Hi everyone,

I was looking to see if i can using Tool calling/Function calling using Llamacpp in Langchain using the co
de provided on the docs. If i use the below given piece of code , it calls the tool every time

    from langchain.tools
 import tool
    from langchain_core.pydantic_v1 import BaseModel, Field
    
    
    class WeatherInput(BaseModel):
  
      location: str = Field(description='The city and state, e.g. San Francisco, CA')
        unit: str = Field(enum=['c
elsius', 'fahrenheit'])
    
    
    @tool('get_current_weather', args_schema=WeatherInput)
    def get_weather(locatio
n: str, unit: str):
        '''Get the current weather in a given location'''
        return f'Now the weather in {locat
ion} is 22 {unit}'
    
    
    llm_with_tools = llm.bind_tools(
        tools=[get_weather],
        tool_choice={'typ
e': 'function', 'function': {'name': 'get_current_weather'}},
    )

When i remove the tool\_choice parameters , it give
s the args of the tool call in content of the code but does not call the tool.

Can anyone help me with this.  I want to
 use LLamacpp to automatically call tools and not have to force it to call the same tools.   


I was using LLama3-groq-
tool-use model for this , which is a finetuned model by groq for tool use.

&#x200B;
```
---

     
 
all -  [ Reviving Lisp in the AI Era: Let's Build a LangChain Competitor in Common Lisp! ](https://www.reddit.com/r/lisp/comments/1envnhy/reviving_lisp_in_the_ai_era_lets_build_a/) , 2024-08-10-0911
```
**Hi awesome Lispers,**

I hope you all are doing great! I wanted to shed light on a potential opportunity to bring Lisp
 back into the mainstream. As you know, AI and LLM applications are becoming incredibly popular, and many businesses are
 developing their services using these technologies. A lot of them are relying on LangChain for a coherent interface tha
t allows for various integrations and models in a simple and consistent way.

I believe it's the perfect time to create 
a competitive library to LangChain in Common Lisp. This could be a great chance to make CL mainstream again. I've heard 
that Lisp is an incredibly productive language, and I imagine that developing a LangChain.cl might require less effort t
han its Python counterpart.

What do you think? Why not come together as a community and have some fun in the AI space a
gain?
```
---

     
 
all -  [ Need some help with setting up the logic of project - Semantic Search Engine ](https://www.reddit.com/r/OpenAI/comments/1envgft/need_some_help_with_setting_up_the_logic_of/) , 2024-08-10-0911
```


Hy i want to build a semantic search engine over hundreds of quotes in json formate. The problem is some quotes a very
 big like 3k tokkens and i am afraid the embeddings may not be good. I think i need to split bigger quotes intro smaller
 chunks and match query against those smaller chunks and return the full quote that it belongs to with the relevant chun
k highlighted. How i can do it using langchain. **I am totally noob to programming Ai related code and it is my first co
mplete project** . I will be thankful for any help may be throw logical steps , psuedo code or any thing that can help.


```
---

     
 
all -  [ Need some help with setting up the logic of project - Semantic Search Engine ](https://www.reddit.com/r/LangChain/comments/1envf1m/need_some_help_with_setting_up_the_logic_of/) , 2024-08-10-0911
```
Hy i want to build a semantic search engine over hundreds of quotes in json formate. The problem is some quotes a very b
ig like 3k tokkens and i am afraid the embeddings may not be good. I think i need to split bigger quotes intro smaller c
hunks and match query against those smaller chunks and return the full quote that it belongs to with the relevant chunk 
highlighted. How i can do it using langchain. **I am totally noob to programming and it is my first big project** . I wi
ll be thankful for any help may be throw logical steps , psuedo code or any thing that can help.
```
---

     
 
all -  [ Should I learn LangGraph instead of LangChain? ](https://www.reddit.com/r/LangChain/comments/1env9og/should_i_learn_langgraph_instead_of_langchain/) , 2024-08-10-0911
```
Hey everyone, I have been learning/working on Agents. For now I'm using LangChain to create Agents. But while I reading 
the documents of LangChain about Agents I saw warning note. I think LangChai won't support building Agents with Langchai
n anymore. They will use LangGraph to create Agents anymore. But as I understand I should know some OOP to create Agents
 using LangGraph (I'm not sure). At this point should I learn LangGraph or stay at Langchain. Or should I use another li
brary for creating Agents.

  
Thanks.
```
---

     
 
all -  [ [0 YOE, 1 internships, Data Science, India] Please roast my resume, Seeking for Internships but no l ](https://i.redd.it/c0wpyk2hvlhd1.png) , 2024-08-10-0911
```

```
---

     
 
all -  [ using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/LangChain/comments/1env10r/using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-10-0911
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
all -  [ Tell me why is this resume not getting any shortlists? I am aiming for most tech companies based in  ](https://www.reddit.com/r/developersIndia/comments/1entwu9/tell_me_why_is_this_resume_not_getting_any/) , 2024-08-10-0911
```
https://preview.redd.it/z43rl1fhflhd1.png?width=658&format=png&auto=webp&s=121cc73577d47fc5215e881c30ad1046b74bc276


```
---

     
 
all -  [ Checkpointer only for human in the loop and time travel workloads? ](https://www.reddit.com/r/LangChain/comments/1ent5yp/checkpointer_only_for_human_in_the_loop_and_time/) , 2024-08-10-0911
```
The project I am working on has no human in the loop and time travel workloads. Is there any more utility to checkpointe
r now?
```
---

     
 
all -  [ Is golang better for AI development ](https://www.reddit.com/r/golang/comments/1enplp1/is_golang_better_for_ai_development/) , 2024-08-10-0911
```
I have been using python and js for all my AI projects (backend), mostly python. But now I want to develop something we 
go because I want to learn it as well as it faster and efficient than python and js. Please guide me whether I should us
e it or not.

Also I want every functionality of AI provided in python like using vision model, langchain, openai APIs e
tc. in golang.

(Edited) 
I am not creating anything from scratch when i say AI, I just build softwares that automate a 
particular tasks/process. There I am just making api calls to different llm models and everything else is normal backend
 stuff.
```
---

     
 
all -  [ Requirements for execute most of local LLMs? ](https://www.reddit.com/r/LangChain/comments/1ennhzg/requirements_for_execute_most_of_local_llms/) , 2024-08-10-0911
```
Hello, I need your help. I'm working at a company and require a computing system for running AI and local language model
s (LLMs). Would you recommend this PC for running LLMs?

[https://www.amazon.com.mx/dp/B0CHCGQDX4?ref=cm\_sw\_r\_cp\_ud\
_dp\_3JJMJDENCHDNMH3VZYMN&ref\_=cm\_sw\_r\_cp\_ud\_dp\_3JJMJDENCHDNMH3VZYMN&social\_share=cm\_sw\_r\_cp\_ud\_dp\_3JJMJDE
NCHDNMH3VZYMN](https://www.amazon.com.mx/dp/B0CHCGQDX4?ref=cm_sw_r_cp_ud_dp_3JJMJDENCHDNMH3VZYMN&ref_=cm_sw_r_cp_ud_dp_3
JJMJDENCHDNMH3VZYMN&social_share=cm_sw_r_cp_ud_dp_3JJMJDENCHDNMH3VZYMN)
```
---

     
 
all -  [ Text Similarity between News article titles ](https://www.reddit.com/r/LangChain/comments/1enksd4/text_similarity_between_news_article_titles/) , 2024-08-10-0911
```
I am nearly 500 articles scraped and am currently trying to group them by what stories are the same. For this, I wanted 
to use text similarity to check how similar the titles are. For example

Britons in Lebanon could be evacuated by more  
 
Britons in Lebanon on standby for evacuation 

are the same story by with different wording. Obviously, in this case i
ts very obvious and something like Jacquard Index could be used. But in other scenarious it gets more complicated. Diffe
rent wording but the same story.  
Using this site [https://similarity-demo.newscatcherapi.com/](https://similarity-demo
.newscatcherapi.com/) I checked that cosine and word2Vec has the highest success. I checked an implementation of word2Ve
c and you need to build a model just to check the similarity. I have to process near 500 titles and group them, theres a
lready a lot of computation involved and I need to grab this data in real time. Is there a way to check the similarity w
ithout having to do it from scratch ?

  
If anyone can suggest a better way please let me know

  

```
---

     
 
all -  [ Seeking In-Depth Information on Perplexity's Sonar Models: System Messages, Context Handling, and AP ](https://www.reddit.com/r/LangChain/comments/1enk44f/seeking_indepth_information_on_perplexitys_sonar/) , 2024-08-10-0911
```
Is there any documentation about Sonar models beyond what's provided in the Perplexity docs?

I'm seeking more informati
on about the differences in behavior between the 'system message,' prompt, and/or first user request. From what I unders
tand, the query is generated based on the 'user' message, and query generation ignores the 'system' message. So what exa
ctly is the purpose of this 'system' message? The examples typically use short 3-4 word phrases, but do Sonar models sup
port more complex system instructions (similar to the models they're trained on)?

Additionally, how do online models ha
ndle multi-turn conversations? What context is used for query generation and RAG? I understand these models are intended
 for single-turn interactions, with 'chat' versions available for multi-turn conversations.

This leads to my question a
bout context length. The online model claims a 128K context, but this seems unattainable in practice. If the user messag
e is too long, query generation becomes less effective and retrieves less relevant results. Higher context can't even be
 achieved with multi-turn chats, as the quality drops significantly.

It's worth noting that the number of tokens provid
ed to the model as 'sources' is generally in the range of 2-3K globally, but often much less depending on the complexity
 of the question (via the API).

Does anyone have insights into these issues? Could someone from the staff please point 
me towards more detailed information?

Thanks in advance! 
```
---

     
 
all -  [ How do you tackle a “time aware” RAG use case? ](https://www.reddit.com/r/LangChain/comments/1enk2hx/how_do_you_tackle_a_time_aware_rag_use_case/) , 2024-08-10-0911
```
Hey y’all!

I’m working through a RAG solution (not my first) and stumbled into a problem I hadn’t thought of yet: retri
eving documents based on time. 

The idea is that you could ask “Provide a summary of what happened in the past 24 hours
?” or “I was out for 5 weeks, what did I miss?”

The documents in the vectordb (pgvector for now) are diverse and made u
p of knowledge bases and ticketing systems. 

Q&A with similarity is easy. This time thing threw me for a loop. 

Best I
 could come up with so far is having the time/date of the article saved in something like epoch form in the metadata the
n, have one LLM assess the user’s request and if it has a time range, respond in JSON format with start/end values. And 
then, filter on the date value on the metadata. 

I saw timescale but haven’t done a bunch of research on it yet. I’ve a
lso seen document retrieval with time decay. That looks interesting. 

Just curious if any of you have had this problem 
and solved it already?

Thanks and cheers!
```
---

     
 
all -  [ 🧰 agent-service-toolkit: Full toolkit for running agent as a service built with LangGraph, FastAPI a ](https://www.reddit.com/r/LangChain/comments/1engrgq/agentservicetoolkit_full_toolkit_for_running/) , 2024-08-10-0911
```
🧰 Introducing agent-service-toolkit, a new open source toolkit for running an AI agent as a service using LangGraph, Fas
tAPI and Streamlit.

* View the repo: [https://github.com/JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC21
5/agent-service-toolkit)
* Try the app: [https://agent-service-toolkit.streamlit.app/](https://agent-service-toolkit.str
eamlit.app/)
* Watch the video: [https://www.youtube.com/watch?v=VqQti9nGoe4](https://www.youtube.com/watch?v=VqQti9nGoe
4)

I wanted to build a few agents for personal projects using the Compound AI Systems approach, and found that LangGrap
h is the most advanced framework with the features I needed today. But serving and interacting with the agent was painfu
l and complicated unless I wanted to use LangGraph Cloud (still in closed beta), and that wouldn't support my own infras
tructure.

I built agent-service-toolkit to solve this problem so I can focus on just the agent logic and core AI system
s for my projects in the future. It uses async-first and FastAPI to be blazing fast and production-ready, with a Streaml
it app for easy sharing and rapid iteration.

[Architecture](https://preview.redd.it/bj51l3w65ihd1.png?width=1619&format
=png&auto=webp&s=1519d1fbe5f8c1a796c4a5b023d7b107cde40c5c)

[App in action](https://preview.redd.it/h5fbanv75ihd1.png?wi
dth=1276&format=png&auto=webp&s=52a483eb644c9c540d870845ebb4baac316f2bd9)


```
---

     
 
all -  [ LLM Evals with open-source CROWDLAB ](https://www.reddit.com/r/LangChain/comments/1engmlq/llm_evals_with_opensource_crowdlab/) , 2024-08-10-0911
```
A couple years ago, we [announced](https://www.reddit.com/r/MachineLearning/comments/xwf38u/r_announcing_crowdlab_openso
urce_tools_for_data/) open-source CROWDLAB for multiannotator labels. We've now seen that these annotator algorithms are
 also useful for LLM Evals in RAG applications, and wrote a short tutorial on how to do so: https://cleanlab.ai/blog/tea
m-llm-evals/. Hope you find it useful, and would love to know what folks are using for LLM Evals! 
```
---

     
 
all -  [ How do I find a job? ](https://www.reddit.com/r/careerguidance/comments/1enghf7/how_do_i_find_a_job/) , 2024-08-10-0911
```
I am really frustrated these days. I am a Full Stack Web Developer having experience in PHP, JS, Python Frameworks I hav
e also worked with langchain but the issue is I just don’t know if i am good enough I can’t get that confidence to overc
ome the fear’s I have.

Any suggestions on how to improve? And yea I am currently focusing on my DevOps skills too.
```
---

     
 
all -  [ What are your biggest challenges in RAG? ](https://www.reddit.com/r/LangChain/comments/1ene81o/what_are_your_biggest_challenges_in_rag/) , 2024-08-10-0911
```
Out of curiosity - what do you struggle most with when it comes to doing RAG (properly)? There are so many frameworks, r
epos and solutions out there these days that for most challenges there seems to be an out-of-the-box solution, so what's
 left? Does not have to be confined to just Langchain.
```
---

     
 
all -  [ Dubbi su offerta post-tirocinio universitario (probabile co.co.co.) ](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1encn3s/dubbi_su_offerta_posttirocinio_universitario/) , 2024-08-10-0911
```
tl;dr: l'azienda con cui ho fatto il tirocinio in università mi offre un co.co.co. in un ruolo diverso da quello svolto 
durante il tirocinio. Consigli?

Per chi avesse voglia di leggere: ho appena terminato la triennale (Informatica). Ho sv
olto i 6 CFU obbligatori di tirocinio presso una certa azienda, occupandomi di analisi dati e sviluppo di un sistema di 
raccomandazione, da cui ho anche scritto la tesi, e con una già accennata possibilità di assunzione post-laurea. Tengo a
 specificare che si parla di sud Italia.

Veniamo al dunque: qualche giorno fa mi propongono questo 'contratto di collab
orazione' (a questo punto credo sia proprio un co.co.co.) da 30h/settimana, quasi full-remote e orario a detta loro TOTA
LMENTE flessibile. Questo per permettermi di lavorare e studiare (magistrale) contemporaneamente. 

I miei dubbi:

1. Il
 ruolo che mi hanno proposto è abbastanza differente da quello che ho fatto durante il tirocinio (data science/ML, se co
sì si può definire) e, soprattutto, è qualcosa in cui io sono praticamente bianco (sviluppo di un gestionale ERP in Java
, mentre io sto cercando di specializzarmi in appunto data science e machine learning/deep learning). Si dà il caso che 
l'unica mia esperienza con Java sia stato un corso di ingegneria del software da 9 CFU, mentre con Python e librerie var
ie (pandas, scikit-learn, langchain ecc.) mi senta molto più sicuro, anche se ancora ad un livello junior. Secondo il vo
stro parere, quanto è probabile che mi forniscano un minimo di formazione (anche un senior che mi segua, non per forza u
n corso) piuttosto che sia lasciato a me stesso a leggere il loro codice e cercare tutorial su internet? Sempre a detta 
loro, potrei ritrovarmi comunque a dover integrare 'l'AI', qualunque cosa significhi, in questo progetto.

2. Il 'contra
tto di collaborazione'. Cercando su internet e anche su questo sub, mi sembra che questo tipo di contratto sia considera
to uno dei peggiori, in pratica peggio di una fake partita IVA, dato che è legale. Assumendo che l'orario sia veramente 
flessibile (nel senso che potenzialmente potrei fare 5h di queste 30 anche dalle 22 alle 3 di notte, ad esempio), questi
 tipi di contratti sono così tanto svantaggiosi per il lavoratore?

3. Non mi hanno ancora parlato di RAL (lo faranno so
ltanto se esprimo parere positivo nell'approfondire la valutazione di quest'offerta): quanto potrei realisticamente aspe
ttarmi?

4. Se volessi proseguire in campo data science o AI (in generale), magari cercando di applicare per qualche int
ernship in aziende grandi nell'ambito, come verrebbe vista un'esperienza completamente scollegata da ciò? L'alternativa 
sarebbe comunque non avere nessuna esperienza lavorativa da mettere nel CV.


Vi ringrazio in anticipo per i consigli


```
---

     
 
all -  [ Token indices sequence length is longer than the specified maximum sequence length for this model (2 ](https://www.reddit.com/r/LangChain/comments/1enbsrw/token_indices_sequence_length_is_longer_than_the/) , 2024-08-10-0911
```
Hello Community,

  
I am trying to summarize using map\_reduce implementation and I have a text file that has \~78000 t
oken(according to Open AI tokenizer) and I am using mistralai/Mistral-7B-Instruct-v0.3 model through huggingface inferen
ce and I run into the above error and the ouputs gets cut off in the middle. Can you please advice how to fix this? The 
model has a context length of 32K but I am not sure why the error says 1024 tokens. Here is the full error  
Token indic
es sequence length is longer than the specified maximum sequence length for this model (20098 > 1024). Running this sequ
ence through the model will result in indexing errors.  
Here is the code  


from langchain.chains.combine\_documents.s
tuff import StuffDocumentsChain

from langchain.chains.llm import LLMChain

from langchain.prompts import PromptTemplate


from langchain.schema.document import Document

from langchain.chains.combine\_documents.stuff import StuffDocumentsCh
ain

from langchain.chains.llm import LLMChain

from langchain.prompts import PromptTemplate

from langchain.chains.summ
arize import load\_summarize\_chain

#type the code to be ready for tomorrow:

from langchain.chains import MapReduceDoc
umentsChain, ReduceDocumentsChain









# Map

map\_template = '''<s>\[INST\]Please write a clear and concise summary
 for the following text.\[/INST\]

Text:

  '{docs}'</s>

  \[INST\] Summary:\[/INST\]



 '''

map\_prompt = PromptTemp
late.from\_template(map\_template)

map\_chain = LLMChain(llm=api\_llm, prompt=map\_prompt)



# Reduce

reduce\_templat
e =  '''<s>\[INST\]Below are the summaries of multiple segments of a document. Please combine these summaries to form a 
meaningful final summary.\[/INST\]

Text:

  '{doc\_summaries}'</s>

  \[INST\] Summary:\[/INST\]



 '''

reduce\_promp
t = PromptTemplate.from\_template(reduce\_template)



# Run chain

reduce\_chain = LLMChain(llm=api\_llm, prompt=reduce
\_prompt)



# Takes a list of documents, combines them into a single string, and passes this to an LLMChain

combine\_d
ocuments\_chain = StuffDocumentsChain(

llm\_chain=reduce\_chain, document\_variable\_name='doc\_summaries'

)



# Comb
ines and iteratively reduces the mapped documents

reduce\_documents\_chain = ReduceDocumentsChain(

# This is final cha
in that is called.

combine\_documents\_chain=combine\_documents\_chain,

# If documents exceed context for \`StuffDocum
entsChain\`

collapse\_documents\_chain=combine\_documents\_chain,

# The maximum number of tokens to group documents in
to.

token\_max=4000,

)



# Combining documents by mapping a chain over them, then combining results

map\_reduce\_cha
in = MapReduceDocumentsChain(

# Map chain

llm\_chain=map\_chain,

# Reduce chain

reduce\_documents\_chain=reduce\_doc
uments\_chain,

# The variable name in the llm\_chain to put the documents in

document\_variable\_name='docs',

# Retur
n the results of the map steps in the output

return\_intermediate\_steps=True,

)



#text\_splitter = CharacterTextSpl
itter.from\_tiktoken\_encoder(

#    chunk\_size=1000, chunk\_overlap=0

#)

#split\_docs = text\_splitter.split\_docume
nts(docs)

splitter = RecursiveCharacterTextSplitter(chunk\_size=4000, chunk\_overlap=200,length\_function = len)

chunk
s = splitter.create\_documents(\[text\])



result=map\_reduce\_chain.invoke(chunks)

print(result\['output\_text'\])


```
---

     
 
all -  [ Multimodal RAG Explainer: 3 Paths to Integrating Text, Images and Audio in RAG, Which One is Best? ](https://www.reddit.com/r/LangChain/comments/1enbqew/multimodal_rag_explainer_3_paths_to_integrating/) , 2024-08-10-0911
```
https://preview.redd.it/h283ore4zghd1.png?width=1600&format=png&auto=webp&s=16b9c6a5b9cdbe1c5107b886cb1769fa364e2917

Hi
 All,

This post is a adaptation of a Multimodal episode of RAG Masters, a weekly Youtube show I do with Daniel Warfield
.  Each week we explore a different topic to help engineers build better RAG.  Some times we know a lot. Sometimes we're
 learning as we go, just like everyone.

The show is here if you want to check it out, but I'll keep posting a lot of th
e content here regardless.

[https://www.youtube.com/watch?v=ZetGV7gtyQw](https://www.youtube.com/watch?v=ZetGV7gtyQw)


Also, my shop [EyeLevel.ai](http://EyeLevel.ai) has some kick ass tools for building advanced RAG in just a few API call
s with SOTA accuracy. The APIs are especially good with complex documents.

Ok, on to the post.

# What is Multimodal RA
G?

Multimodal RAG is an advanced extension of traditional Retrieval-Augmented Generation systems. Classic RAG involves 
a retrieval engine that searches a database of text documents to find relevant information and injects this data into a 
prompt for a language model to generate a response. Multimodal RAG expands this by including non-text data types, which 
enhances the model's ability to understand and generate responses based on a more comprehensive set of inputs.

Taking m
ultimodal inputs allows for RAG engineers to build a more complex retrieval engine that can ask a store of information a
bout information across different mediums. This means that the retrieval engine can grab data from various sources—wheth
er text, images, audio, or video—and use that information to answer a query. For instance, an expert's audio commentary 
on the Eiffel Tower can be retrieved alongside text and image data to provide a more holistic response that anchors the 
answer in the data provided.

# How Multimodal RAG Works

The mechanics of Multimodal RAG involve transforming different
 data types into a structured data format like vectors that a model can process. This allows the model to retrieve and g
enerate information across multiple modalities seamlessly.

Once these data types are encoded into vectors, they can be 
stored in a vector space or similar storage vehicle, enabling the model to find relevant information regardless of the o
riginal data type. This process could involve clustering similar data and separating dissimilar data, making it easier t
o retrieve the most pertinent information for a given query.

# Three Approaches to Multimodal RAG

Implementing Multimo
dal RAG can be approached in a few distinct ways, each with its advantages and challenges. The three main methods includ
e using a single multimodal model, employing a grounded modality approach, and utilizing multiple encoders.

# Single Mu
ltimodal Model

[Image: Multimodal RAG diagram depicting the storage of Audio, Image, and Text encodings to answer a use
r query.](https://preview.redd.it/7hdmvcfj0hhd1.png?width=960&format=png&auto=webp&s=ce25486892694d6110e70084d6042ea1d2f
c604f)

This approach uses a unified model trained to encode different types of data (text, images, audio) into a common
 vector space. The model can then perform retrieval and generation across these different data types seamlessly. A singl
e multimodal approach tends to be one of the most common approaches people talk about when they talk about multimodal RA
G.

This method simplifies the process but relies heavily on the model’s ability to accurately encode and retrieve multi
modal data. However, if the model is well-trained, it can store and retrieve similar information across different modali
ties effectively.

Google is a great example of using a single multimodal mode.


# Grounded Modality (Text-Based)

In t
his approach, all data types are converted into text descriptions before being encoded and stored. This method leverages
 the strength of text-based models but may involve some loss of information during the conversion process.

Turning all 
data types into one modality creates a unified set of information for the model to retrieve, and today’s models are stro
ngest on text. That’s not to say in the future there won't be models that are better suited for other modalities. And th
at future might be months not years. But for today’s powerhouse models, they started out as text machines and that is st
ill where they are strongest.

This approach allows the use of robust text-based models for encoding and retrieval, maki
ng it a practical solution for environments where text is the primary data type.

# Multiple Encoders

[Image: A Multimo
dal RAG diagram that relies on separately aligned models to handle different modalities from a user query.](https://prev
iew.redd.it/3wmxg7yl0hhd1.png?width=960&format=png&auto=webp&s=80a2501a4c0b4c349fd93578c1c528c37848c97d)

This method em
ploys separate models to encode different data types. Each type of data (audio, images, text) is processed by its respec
tive model, and the results are integrated later in the retrieval process. Passing them through a set of encoders that c
an play nicely together creates an environment where each model and encoder can be fine-tuned to play to its particular 
strengths. 

This approach allows for specialized encoding but increases complexity in managing multiple models. It offe
rs the flexibility to use the best model for each data type, enhancing the accuracy and relevance of the retrieved infor
mation. But often it can be the most difficult to implement and maintain due to the increased complexity of inputs and o
utputs. 

With the emergence of powerful models that are starting to outperform other models in specific modalities, thi
s approach to multimodal RAG may grow in popularity.

# Challenges and Considerations

Implementing Multimodal RAG comes
 with its own set of challenges, such as handling temporal changes in data and ensuring the accuracy of the retrieval an
d generation process. 

Temporal changes, like the varying appearances of the Eiffel Tower over time, pose a significant
 challenge. Ensuring that the retrieved information is temporally accurate and relevant requires sophisticated handling 
of metadata and context which can be even more challenging when trying to pull data from multiple modalities like images
 and audio.

Another consideration is the balance between using a single unified model and multiple specialized models. 
While a single model offers simplicity, multiple models provide more tailored encoding for different data types. This de
cision depends on the specific application and the need for flexibility.

# Practical Applications and Future Prospects


Multimodal RAG holds immense potential for various practical applications, from enhancing search engines to improving A
I-driven personal assistants. By integrating multiple data types, these systems can provide richer, more nuanced respons
es, improving user experience and satisfaction.

Looking forward, the field of Multimodal RAG is poised for significant 
advancements. As models continue to improve and new techniques are developed, the ability to effectively integrate and l
everage multiple data types will become increasingly crucial. This progress will open up new opportunities for powerful 
applications and improved AI performance.

# Conclusion

Multimodal RAG represents a significant advancement in AI, as i
t can enable richer and more contextually accurate information retrieval and generation that grounds the model in the tr
uth of the data across modalities. While the field continues to evolve, the various approaches to implementing Multimoda
l RAG offer different trade-offs between simplicity, flexibility, and complexity. As technology progresses, the ability 
to effectively integrate and leverage multiple data types will be crucial for developing advanced AI applications.

Full
 Episode:  
[https://www.youtube.com/watch?v=ZetGV7gtyQw](https://www.youtube.com/watch?v=ZetGV7gtyQw)

# 
```
---

     
 
all -  [ Documentation seems confusing ](https://www.reddit.com/r/LangChain/comments/1enaock/documentation_seems_confusing/) , 2024-08-10-0911
```
Hello everybody! I have just started langchain and am going through documentation and it seems very confusing. 
I am als
o having trouble with prompts.
Could you please suggest a good starting point? 
Sorry if this has been posted before.
```
---

     
 
all -  [ What are the current limitations of LangChain4j compared to the Python version ](https://www.reddit.com/r/LangChain/comments/1enagg9/what_are_the_current_limitations_of_langchain4j/) , 2024-08-10-0911
```
I'm a Java developer interested in getting into AI software development. I see there's a ton of info on LangChain for Py
thon, but not as much on LangChain4j for Java. Should I dive into Python and start developing with it, or can I learn fr
om the langchain docs (and youtube videos) and then apply that knowledge to Java (just with different syntax)? Any advic
e?
```
---

     
 
all -  [ [3 YoE] [Canada] Not hearing back from Machine Learning Engineering or Data Science Jobs I applied t ](https://www.reddit.com/r/EngineeringResumes/comments/1en8yqn/3_yoe_canada_not_hearing_back_from_machine/) , 2024-08-10-0911
```
\[3 YoE\] \[Canada\] Not hearing back from Machine Learning Engineering or Data Science Jobs I applied to. Please help.


&#x200B;

• What positions/roles/industries are you targeting? 

MLE (ambitious), Data Scientist, Business Analyst (Wor
st Case Scenario)

  
• Where are you located and what locations are you applying to jobs in?

Montreal, applying to ope
nings in Canada

  
• Are you only applying to local jobs? Remote only? Are you willing to relocate?

Willing to relocat
e but visa is a complication for options beyond canada

  
• Tell us about your background and current employment situat
ion

Ex Management consultant with a bachelor in mechanical and masters in data science ('Management Analytics'). Have b
een working as a data scientist for the past one year (some parts contract, some part internship)

  
• Tell us about yo
ur job-hunting situation and challenges you've encountered

Radio Silence from postings I have been applying to. Radio s
ilence from recruiters I reached out to on LinkedIn

  
• Tell us why you're seeking help. (i.e., just fine-tuning, not 
getting called back for interviews, etc.)

Not getting called back for interviews

  
• Is there a particular section on
 your resume you’d like feedback on?

Experience bullet points, structure, 'what am i missing that is leading me to not 
get any interviews??'

  
• Is your citizenship status and visa situation playing a role in your job search?

I don't th
ink so. I am on PGWP.

https://preview.redd.it/kl2iqd44lghd1.png?width=5100&format=png&auto=webp&s=4d1d1759600cbf6df0964
46f9d388ef958ce25b0
```
---

     
 
all -  [ Key Contributors and Insights in Git Project Modules ](https://i.redd.it/nni4zbkqjghd1.jpeg) , 2024-08-10-0911
```
You might want to know who the main contributors are for those modules in the project directory over a certain period.


Although the layout is not perfect yet. (who knows how to align the TopN authors to the right).

Look at https://plugins
.jetbrains.com/plugin/24154-git-assistant
```
---

     
 
all -  [ Text-2-SQL-Pandas Pipeline: HOW DO I BUILD THIS! ](https://www.reddit.com/r/LangChain/comments/1en87i9/text2sqlpandas_pipeline_how_do_i_build_this/) , 2024-08-10-0911
```
[https://www.reddit.com/r/LangChain/comments/1e5pe1a/optimal\_rag\_for\_text2sql/?utm\_source=share&utm\_medium=web3x&ut
m\_name=web3xcss&utm\_term=1&utm\_content=share\_button](https://www.reddit.com/r/LangChain/comments/1e5pe1a/optimal_rag
_for_text2sql/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)  
  
I built a w
orking text-2-SQL pipeline that runs queries on million of records. 20+ tables. It leverages Claude 3.5 sonnet and gets 
the work done 7/10 very well on a few complex prompts, multiple joins and conditional clauses.  At the infra level, the 
database has been modified to create and include a few views that would help make much more sense of the data. 

Now, I 
am in charge of building an analysis agent on top of it. 

Here's what I was thinking: I'll have the text-2-sql agent tr
anslate to query, retrieve the tabular information from the database and return the final table before applying any cond
itions or other arithmetic operations. And then pass on the resulting table to pandas agent along with the originally as
ked question. 

And then the pandas agent cook. But, I'm not a 100% sure whether this is the ideal approach. OR if there
 is any other way to work with this. Lemme know if you have any thoughts!
```
---

     
 
all -  [ Langfuse for LLM tracing for beginners  ](https://www.reddit.com/r/LangChain/comments/1en73et/langfuse_for_llm_tracing_for_beginners/) , 2024-08-10-0911
```
Langfuse is a free alternate for Langsmith for Generative AI based applications for debugging and tracing. This video ex
plains how to get Started with Langfuse : https://youtu.be/fIQIfIK6v0o?si=hzeG4matNCCZ9Bt_
```
---

     
 
all -  [ RAG system to detect small talk ](https://www.reddit.com/r/LangChain/comments/1en5h33/rag_system_to_detect_small_talk/) , 2024-08-10-0911
```
In a RAG system, how do you avoid the bot to go retrieve information when the questions are just small talk? For example
 the user says “Hi how are you?” And the bot goes and triggers all the RAG logic and gets all the information and makes 
a lot of drama and it replies “good thanks for asking” hahah anybody dealing with this issue?
```
---

     
 
all -  [ ML Engineer (1 YOE) looking for an open opportunity  ](https://www.reddit.com/r/Entrepreneur/comments/1en3r4e/ml_engineer_1_yoe_looking_for_an_open_opportunity/) , 2024-08-10-0911
```




Hi folks. I am a Machine Learning Engineer looking for open opportunities in Bangalore. I have 1 year of experience 
in developing and deploying ML solutions convering basic ML fundamentals like regression models and data analysis to bui
lding RAG applications using vector DB and Langchain. I have worked in shaping ideas into POCs using Machine Learning an
d Deep Learning. 

My tech stack includes Python, Jupyter Notebook, Sci-kit Learn, Langchain, Vector DB, fine-tuning LLM
s for specific use cases.

I am also experienced in developing & deploying the end to end LLM applications to AWS cloud.
 I am passionate about ML.

Any leads would be appreciated. 
Thank You 
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-10-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-10-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-10-0911
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-10-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-10-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-10-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
