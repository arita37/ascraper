 
all -  [ How can I stream only the final result from a agent in streamlit  ](https://www.reddit.com/r/LangChain/comments/1eduao5/how_can_i_stream_only_the_final_result_from_a/) , 2024-07-28-0912
```
Sorry if this question is too basic. New to this so trying to learn. 



So this Is what I did. Created a basic agent wi
th few random tools. Added Memory to it using RunnableWithMessageHistory. 



`llm = ChatOpenAI(model_name = 'gpt-3.5-tu
rbo', temperature = 0)`

`tools = [click_new_image, visual_question_answer, question_answer, previous_pic]`

`prompt = C
hatPromptTemplate.from_messages(`

`[`

`('system', 'You are a very powerful assistant who can take pictures and answer 
questions about them. If the query is regarding an older pic, then answer directly instead of taking a new pic.'),`

`Me
ssagesPlaceholder(variable_name='history'),`

`('user', '{input}'),`

`MessagesPlaceholder(variable_name='agent_scratchp
ad'),`

`]`

`)`

`agent = create_tool_calling_agent(llm, tools, prompt)`

`agent_executor = AgentExecutor(agent=agent, 
tools=tools, verbose = True)`

`store = {}`

  
`agent_executor_w_memory = RunnableWithMessageHistory(`

`agent_executor
,`

`get_session_history,`

`input_messages_key='input',`

`history_messages_key='history',`

`)`

  
To run this I did 
( In Streamlit ) - 

`if prompt := st.chat_input():`

`st.chat_message('user').write(prompt)`

`with st.chat_message('as
sistant'):`

`response = agent_executor_w_memory.invoke(`

`{'input': prompt},`

`config=config,`

`)`

`st.write(respon
se['output'])`

  
But this won't stream( typing effect) the output, it will just give the final output at once. I want 
to stream the output. Only the last response, not the intermediate steps. 

  
Ps- Can I also stream the intermediate st
ep result( we could iterate through the stream and print chunks but that will also not stream( typing effect)) ? or like
 tools it call too? ( Asking just to learn more, not needed as of now) 
```
---

     
 
all -  [ ML model demo tool?  ](https://www.reddit.com/r/LangChain/comments/1edtzrx/ml_model_demo_tool/) , 2024-07-28-0912
```
Hey guys,

My buddy and I are working on a tool that lets you preview your ML models in a presentable environment before
 deployment. I had my models set up on Google Colab, but it wasn’t easy for the team to review it. It also isn’t very pr
esentable to clients.

So we want to create a demo environment that’s super simple to share and present models before ha
nding off to devops. Thinking about adding some sort of feedback system too.

We’re still figuring out the details, so w
e’d love to get your takes on this. In your experience, what features would’ve helped you? Currently we have charts and 
collaboration features in mind.

Thanks! (my dm is open! we can’t be the only ones having this problem right)

```
---

     
 
all -  [ Created an AI voice agents product .. give it a try. I am using Twilio for phone numbers... The resu ](https://workhub.ai/ai-voice-agent/) , 2024-07-28-0912
```

```
---

     
 
all -  [ I’m trying to connect databricks table to langchain ](https://www.reddit.com/r/LangChain/comments/1edr19y/im_trying_to_connect_databricks_table_to_langchain/) , 2024-07-28-0912
```
I’m trying to use the SQLDatabase.from_databricks and I’m getting a weird error 'value error: invalid literal for int() 
with base 10:'' '

I used the warehouse_id and not cluster_id. Please helpppp
```
---

     
 
all -  [ Lack of APIs ](https://www.reddit.com/r/LangChain/comments/1edkn7p/lack_of_apis/) , 2024-07-28-0912
```
Hey guys,

I have a general question for those of you developing agentic AI systems. Have you had the problem of a servi
ce not having an API and how did you solve it (i.e., how did you define the 'tool' to be used by the LLM)? A simple exam
ple: I want my personal AI assistant to purchase groceries for me, but there's no API provided by the supermarket. How c
an I achieve that?

  
Do you think this is another reason why AI agents are still not in use for tasks that are not cri
tical (thus, it's fine if they're not 100% reliable), but could be very useful in our daily lives?


Edit: by “simple ex
ample”, I meant “simple use case”, not that it’s easy to implement
```
---

     
 
all -  [ How can I use RAGAS without OpenAI key? ](https://www.reddit.com/r/LangChain/comments/1ed9rhu/how_can_i_use_ragas_without_openai_key/) , 2024-07-28-0912
```
Please point to some reference of using RAGAS with local models
```
---

     
 
all -  [ will TS ever surpass Python for generative AI development? ](https://www.reddit.com/r/LangChain/comments/1ed9kiw/will_ts_ever_surpass_python_for_generative_ai/) , 2024-07-28-0912
```
have you guys seen any trends or evidence that could potentially show a turn for TypeScript?
```
---

     
 
all -  [ Using Langchain for a small-scale web-app ](https://www.reddit.com/r/LangChain/comments/1ed8seg/using_langchain_for_a_smallscale_webapp/) , 2024-07-28-0912
```
Hey guys,

Recently I have familiarized myself with Langchain quite a bit. I was hoping to make a basic web-app, for a c
lass of less than 100 people, as a personal project. 

Unfortunately, while I do know JavaScript, Python, CSS, and HTML.
 I am unfamiliar with the structure behind such an application. Until now I have built some local CLI applications while
 using APIs (DeepSeek is crazy cheap and nice but might need an alternative because they also use API accessed data).

W
here can I host a website, or a local easier llm like llama with it, or any options I can use with Langchain chain APIs?
 Also should I host an open-source LLM somewhere or depend on APIs?

There is just so much information that I cannot fin
d anything concrete over it, please help :')

Thanks!
```
---

     
 
all -  [ What's the difference between bind_tools and bind_functions? ](https://www.reddit.com/r/LangChain/comments/1ed6cmm/whats_the_difference_between_bind_tools_and_bind/) , 2024-07-28-0912
```
I've seen in lots of tutorials from the langchain/langraph documentation using bind\_tools and bind\_functions.  
But I 
haven't yet understood the difference between them and where to use each one.  
Also, do they both work with all chat mo
dels?
```
---

     
 
all -  [ Any ML dev tools that you know ](https://www.reddit.com/r/SmythOS/comments/1ecxhjm/any_ml_dev_tools_that_you_know/) , 2024-07-28-0912
```
Since I found SmythOS, I was kind of disappointed in myself that I had not known that this platform existed, I am going 
to list a number of dev tools and platforms in the AI and ML space that you might find useful, you can add your favorite
 tools in the comments

1.  Pinecone, Weaviate or pgvector -  vector databases
2. GPT Index - indexing a document
3. Lan
gchain
4. Streamlit - quickly deploy small apps
5. Humanloop and Everyprompt - optimize your prompts
6. PyTorch, Keras, 
TensorFlow - ML frameworks for building models
7. MLflow, Kubeflow, Metaflow, Airflow, Seldon Core, TFServing - deployin
g models

Continue the list.
```
---

     
 
all -  [ LangGraph RAG w/ CoT Sequential Decomposition ](https://www.reddit.com/r/LangChain/comments/1ecwyuk/langgraph_rag_w_cot_sequential_decomposition/) , 2024-07-28-0912
```
Hi all, 

I’m trying to design a the graph workflow with LangGraph/LangChain. In building CRAG, what’s a good way to int
egrate sequential/parallel decomposition and self-query in the nodes and conditional edges. 

For examples, let’s say th
ere’s a question that can be broken into sequential sub-queries: 'What is the weather of the Big Apple?' would first loo
k up 'What is the Big Apple' then do 'Weather in NYC'.

I guess I can view this more like ReAct function calling: 

Star
t > Planner > self-query > retriever > docs > grade > Planner > generate-end/self-query

Planner node will do both tool 
calling of RAG and also query decomposition/optimization/CoT.

Appreciate any help!
```
---

     
 
all -  [ Rising Junior looking to break into consulting. Roast my resume! ](https://www.reddit.com/r/resumes/comments/1ecwcsv/rising_junior_looking_to_break_into_consulting/) , 2024-07-28-0912
```
This is the resume I'll be using to apply for internships next summer. Any advice? Be brutally honest

https://preview.r
edd.it/eniadcf5xwed1.jpg?width=2550&format=pjpg&auto=webp&s=132710efbbf635032430cb1edc051da54c58b95f


```
---

     
 
all -  [ RAG provenance computation ](https://www.reddit.com/r/LangChain/comments/1ecw305/rag_provenance_computation/) , 2024-07-28-0912
```
https://preview.redd.it/4ld6chb9vwed1.png?width=1052&format=png&auto=webp&s=fe05dfd00ac3b7e109b70ba612a003e096a9fa63

Wh
en performing RAG with any LLM, it's pretty tricky to decide how much of the answer given by the LLM was actually due to
 a specific document that was fed into it. Did the LLM pay attention to 1 document? 3? or perhaps none and just the quer
y?

This provenance attribution is a difficult challenge in RAG and has not yet been properly solved. That being said, w
e have added quite a few ways to compute provenance to our framework RAG Me Up - [https://github.com/AI-Commandos/RAGMeU
p](https://github.com/AI-Commandos/RAGMeUp)

One of the coolest and most accurate is when you are using local/open sourc
e LLMs, we can actually retrieve the attention scores from the model and use those to compute provenance:

* How much at
tention was paid from the given answer to every document separately that was retrieved from the database? Vice versa fro
m every document to the answer?
* How much attention was paid from the query to every document and vice versa?
* How muc
h attention was paid from the answer to the query, disregarding the documents... and vice versa.
* And finally from the 
query to itself and from the answer to itself (remember that LLMs are autoregressive!)

If we then take the attention pa
id from/to a single document and divide that by the sum of the other attentions mentioned - we get a good idea of the re
lative importance of each document fed into the LLM!

In RAG Me Up this is now implemented as a provenance method 'atten
tion' and you can use it with any OS LLM on any given dataset.
```
---

     
 
all -  [ Tool Calling Agent not actually calling tools ](https://www.reddit.com/r/LangChain/comments/1ecvnfk/tool_calling_agent_not_actually_calling_tools/) , 2024-07-28-0912
```
Hey guys,

I'm doing a little project to familiarize myself with langchain and gen AI as a whole, and the tldr is that I
'm trying to create an agent that has the capability to call tools and put the result into a complete sentence at the en
d for the user to interpret. This seems pretty simple, but I've never come across a solution that can do both after hour
s of google searching (maybe I'm just looking in the wrong places lol). Regardless, I'm currently using the create\_tool
\_calling\_agent method from the langchain.agents python library, and it works great for doing the complete sentence par
t, but it's not actually calling the tool that I have set to call and is coming up with a nonsensical answer to boot. He
re is an example of what I'm talking about and the code I have setup:

The tool:

        u/tool
        def get_weather
(self, location=None) -> int:
            'Gets the temperature at a chosen location AND ONLY THE TEMPERATURE. The locat
ion argument is optional, and if left blank it will retrieve the user's current location.'
            print('get_weathe
r called') #DEBUGGING
            if location == None:
                temp = self.get_location_data()
                l
ocation = temp['city']
            complete_url = 'http://api.openweathermap.org/data/2.5/weather?' + 'appid=' + os.gete
nv('OPENWEATHERMAP_API_KEY') + '&q=' + location
            response = requests.get(complete_url)
            x = respon
se.json()
            print(x)
            try:
                current_temperature = x['main']['temp']
            exce
pt:
                return -1
            return int((current_temperature - 273.15)*1.8 + 32)

The agent/LLM setup:

   
 class Agent:
        def __init__(self) -> None:
            t = Custom_Tool()
            self.model = ChatOllama(mode
l='llama3.1:8b', temperature=0)
            self.prompt = ChatPromptTemplate.from_messages(
                [
          
          ('system', system_prompt),
                    ('placeholder', '{chat_history}'),
                    ('human'
, '{input}'),
                    ('placeholder', '{agent_scratchpad}'),
                ]
            )
            sel
f.tools = [t.get_weather]
        def invoke_agent(self, prompt: str):
            agent = create_tool_calling_agent(sel
f.model, self.tools, self.prompt)
            agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True
)
            agent_executor.invoke({'input': prompt})

The prompt:

    def run(prompt):
        a = Agent()
        a.
invoke_agent(prompt=prompt)
    
    if __name__ == '__main__':
        run('What's the weather in Minneapolis?')

The r
esult (it is not 42 degrees in Minneapolis in the middle of July):

    > Entering new AgentExecutor chain...
    I'd be
 happy to check the current temperature in Minneapolis for you.
    Let me just make an API call using our `get_weather`
 tool... 
    The current temperature in Minneapolis is 42°F. Would you like to know more about the weather conditions o
r forecast?

If anyone has a better way to do this or advice for me to get going in the right direction please let me kn
ow. Thanks.
```
---

     
 
all -  [ AskItRight: PDFs Query Fullstack Application (RAG Ollama, LangChain, ChromaDB ) ](https://www.reddit.com/r/LangChain/comments/1ecuq2g/askitright_pdfs_query_fullstack_application_rag/) , 2024-07-28-0912
```
Hello Reddit!

https://preview.redd.it/2l247zaekwed1.png?width=250&format=png&auto=webp&s=4365916258171dffcfe820e9ad138c
f1e847078d

I’ve been tinkering with some libraries and just finished building an app I’m so excited to share with you a
ll. I’d love for you to check it out and let me know what you think!

🔗 GitHub Repository: [https://github.com/AbdArdati
/PDFQueryAI](https://github.com/AbdArdati/PDFQueryAI)

# Key Features 🔑

1. **PDF Management**:
   * **Upload PDFs**: 📤 
Users can upload PDF files through the upload interface. These files are processed and stored in the system.
   * **List
 PDFs**: 📋 Users can view a list of all uploaded PDF files through the available PDFs interface.
   * **Delete PDFs**: 🗑
️ Users can remove specific PDF files using the delete functionality available in the PDF management interface.
   * **V
iew PDFs**: 👁️ Users can open and view the content of PDF files in a new browser tab directly from the list of PDFs.
2. 
**Query Handling**:
   * **Ask Questions to PDF**: 🤔 Users can submit questions about the content of uploaded PDFs using
 the query interface. The application uses the AI model to provide answers based on the PDF contents.
   * **AI Integrat
ion**: 🤖 The l\*\*lama3.1 model \*\*is used to generate answers to queries from the content of the PDFs. This functional
ity is accessible through the AI query interface.
   * **Prompt Templates**: 📝 Users can view and select from various pr
ompt templates to guide the AI's responses, ensuring they are tailored to specific needs. (Currently in progress, with f
rontend Create, Update, and Delete to be implemented.)
3. **Statistics and Administration**:
   * **Clear Chat History**
: 🧹 Users can clear previous chat interactions using the clear chat history button in the query section.
   * **Clear Da
tabase**: 🚮 Deletes all stored PDFs and related data, effectively resetting the application’s state. This action is avai
lable in the database management section.
   * **PDF Usage Statistics**: 📈 Provides information on how frequently each P
DF has been queried, viewable through the statistics dashboard.

This example demonstrated below is based on the 'Essays
 Expert' prompt template. The screenshot highlights how the system utilises PDF content to generate comprehensive respon
ses at the top, while the lower section shows the output generated without PDFs, illustrating the impact of including de
tailed content.

https://preview.redd.it/2hta2yrgkwed1.png?width=2880&format=png&auto=webp&s=91ecb0a7056034b6fd1a57b1931
1e3f9a8703add

I’m not an expert in this domain—just a big fan of its potential who’s been reading up on it. All feedbac
k is welcome:)
```
---

     
 
all -  [ Problemas al usar fastapi y langchain_google_cloud_sql_pg en Cloud Run (GCP) ](https://www.reddit.com/r/programacion/comments/1ecubkg/problemas_al_usar_fastapi_y_langchain_google/) , 2024-07-28-0912
```
Buenas, quería consultar si a alguno le ha pasado esto porque ya entre google, yo y gpt no le encontramos la vuelta.

Te
ngo un endpoint creado en fastapi al que le paso un hash, un nombre de usuario y una pregunta y esta usa un grafo de lan
ggraph, querys, embeddings y demas y por medio de openai usando un modelo me retorna una respuesta, basicamente un bot, 
pero especializado ya que no responde en general, responde en base a información que tengo guardada en una base vectoria
l, asi que le haces la pregunta, transforma a vector, busca los vectores mas cercanos y retorna eso como texto.

Listo e
l resumen de lo que hace, ahora el problema:

Cuando se llama al endpoint se ejecuta esto, basicamente se crea una sincr
onizacion a la tabla de postgres del historico de los chats

    engine_cx_bot = create_engine()
    
    from langchain
_google_cloud_sql_pg import PostgresChatMessageHistory
    
    history = PostgresChatMessageHistory.create_sync(
      
  engine_cx_bot, session_id=session_id, table_name=settings.table_cx_history
    )

Esto me permite 2 cosas

1. Insertar
 las nuevas interacciones entre el humano que consulta y el bot que responde

history.add\_message(HumanMessage(content=
inputs\['question'\]))  
history.add\_message(AIMessage(content=''.join(output\['generate\_answer'\]\['messages'\])))

2
) Ir a buscar el historico de todos los mensajes para que ante cada nueva pregunta del usuario el bot tenga el contexto 
de la charla, si le hago un par de preguntas hoy y vuelvo manaña, al volver a consultarle, como tiene todos los mensajes
 del historico, puede seguirme la charla.

El problema:

Deploye esto en cloud run, el endpoint funciona ok, puedo pegar
le de un front y tener un chat y charlar con el bot pero a la hs o 2 hs dejo de poner pegarlo por status 500, como que s
e corta la conexión entre el cloud run y el cloud sql donde esta la data guardada y mirando logs solo veo esto, llevo ap
rox 50 deploys haciendo pruebas y no salgo de este error que es aleatorio, a veces 1 hs, a veces 2, lo que mas tardo fue
ron 6 hs y se cayo.

File '/app/venv/lib/python3.9/site-packages/langchain\_google\_cloud\_sql\_pg/engine.py', line 245,
 in getconn  
conn = await cls.\_connector.connect\_async(  # type: ignore  
File '/app/venv/lib/python3.9/site-packages
/google/cloud/sql/connector/connector.py', line 341, in connect\_async  
conn\_info = await cache.connect\_info()  
File
 '/app/venv/lib/python3.9/site-packages/google/cloud/sql/connector/lazy.py', line 103, in connect\_info  
conn\_info = a
wait self.\_client.get\_connection\_info(  
File '/app/venv/lib/python3.9/site-packages/google/cloud/sql/connector/clien
t.py', line 271, in get\_connection\_info  
metadata = await metadata\_task  
File '/app/venv/lib/python3.9/site-package
s/google/cloud/sql/connector/client.py', line 128, in \_get\_metadata  
resp = await self.\_client.get(url, headers=head
ers)  
File '/app/venv/lib/python3.9/site-packages/aiohttp/client.py', line 507, in \_request  
with timer:  
File '/app
/venv/lib/python3.9/site-packages/aiohttp/helpers.py', line 715, in \_\_enter\_\_  
raise RuntimeError(  
RuntimeError: 
Timeout context manager should be used inside a task'

A alguno le ha pasado? Si voy al cloud run y redeployo la misma r
evision vuelve a funcionar, pero lo mismo, un par de hs y se cae
```
---

     
 
all -  [ seeking ideas on how to overcome limitation of context awareness in similarity search and fusion rag ](https://www.reddit.com/r/LangChain/comments/1ecuavd/seeking_ideas_on_how_to_overcome_limitation_of/) , 2024-07-28-0912
```
In my personal project, I originally plan to use rag fusion to match resumes and job descriptions (preprocessed by summa
rizing with llm). Right now I'm stuck on how to overcome limitation of context awareness in embeddings and semantic/simi
larity searches. For example, in query generation, one of query is focused on experience. ideally I'd like to produce an
 assessment like below

'Assessment': 'Limited experience but shows potential. Candidate has some exposure to relevant a
reas like recommendation systems and customer segmentation, but lacks the depth of experience required for the role.'

'
responsibilities in Job Description': 'Experience creating and implementing machine learning techniques for recommender 
systems and time series analysis. Experience with customer segmentation, churn prediction, campaign optimization, and mo
re.'

'experience section in Resume': 'Developed basic machine learning models for customer segmentation and product rec
ommendation at XYZ Retail. Assisted in building a prototype recommendation engine during internship at StartupX.'  
My i
mplementation of fusion rag will identify similar keywords, but fail to recognize the difference in depth and breadth of
 experience, and unable to infer and interpret. Any ideas on how to address this limitation of context awareness? Thanks
 in advance!


```
---

     
 
all -  [ For those of you developing Agent or Multi Agent applications, what's missing?
 ](https://www.reddit.com/r/AI_Agents/comments/1ectggp/for_those_of_you_developing_agent_or_multi_agent/) , 2024-07-28-0912
```
I tried Crew, Autogen and Langchain, but the results still aren't that great without spending a lot of time building and
 testing custom tools for each application.

Would love to know your thoughts and personal experience on this.
```
---

     
 
all -  [ Vllm + dolphin-2.6-mistral + langchain ](https://www.reddit.com/r/LangChain/comments/1ectcut/vllm_dolphin26mistral_langchain/) , 2024-07-28-0912
```
Hi, i am new to langchain and i hope somebody here can help me understand some basics.

I have a server serving the mode
l via vllm openai endpoint.
The model uses a ChatML template:

<|im_start|>system
{system_message}<|im_end|>
<|im_start|
>user
{prompt}<|im_end|>
<|im_start|>assistant

Can langchain handle this and if so, how?
Or did i combine the wrong stu
ff together?

I am asking, because my LLM is responding sometimes in a strange way. For example, i asked „how far is the
 moon“ and i get an endless response back. The first sentence is the right answer but all that follows after, it is  tot
al nonsense.

Thanks

```
---

     
 
all -  [ Resume review ](https://www.reddit.com/gallery/1ecsa0w) , 2024-07-28-0912
```
Please help me summarize my resume
I am 2024 PG passout student I have 2 years of internship exp and 2 years of teaching
 exp
My cv is too big please help me summarize
```
---

     
 
all -  [ Unleashing Git Commit Insights with JetBrains Git Assistant Plugin ](https://www.reddit.com/r/pycharm/comments/1ecrmgh/unleashing_git_commit_insights_with_jetbrains_git/) , 2024-07-28-0912
```
Git Assistant is a powerful IntelliJ IDEA plugin that provides users with powerful Commits analysis tools through the Gi
t Assistant Insights window in the right-side tool window.

1. The Hour/Weekday/Month feature analyzes the distribution 
of team activity based on hours, weekdays, and months, optimizing work schedules and task assignments.
2. The Timezone f
eature visualizes the distribution of code contributions across different time zones, making global team collaboration v
isible and tangible.
3. The project tree on the left side also provides analysis capabilities for hot files and hot dire
ctories, helping developers better understand the recently changed files and directories in the project.

# Insights Vie
w

In the Overview panel, the most significant contributors in the code repository are displayed, helping identify and r
ecognize excellent contributors and enhancing teamwork and competitiveness.

https://preview.redd.it/vc52t97imved1.png?w
idth=3024&format=png&auto=webp&s=cd29f35342d43a414c7894f760aa7d6e97c17803

In the Hour/Weekday/Month panels, the distrib
ution of team activity over time is visualized, optimizing work schedules and task assignments.

https://preview.redd.it
/bztndp1omved1.png?width=3024&format=png&auto=webp&s=9f4ae8f130ad331730e59c45dfca2dd86d7cbbf0

https://preview.redd.it/l
1tbuo1omved1.png?width=3024&format=png&auto=webp&s=6dbf992933a9196affdb8db2977e18d80c0acfe2

https://preview.redd.it/zmc
lvp1omved1.png?width=3024&format=png&auto=webp&s=f5f08a4eb1af2dbd6b2566974f523e4bd81a9c20

In the Timezone panel, the di
stribution of code contributions across different time zones is visualized, making global team collaboration visible and
 tangible.

https://preview.redd.it/5wkc95rrmved1.png?width=3024&format=png&auto=webp&s=8bf2ebf23a1e6d1655e2dcdc95b79e26
09a0a4db

In the Project View panel, the analysis of hot files and hot directories is presented, helping developers bett
er understand the recently changed files and directories in the project.

https://preview.redd.it/22vbpzttmved1.png?widt
h=3024&format=png&auto=webp&s=93bf17479d3744cdb38e14c22a794d241fc94738

[https://plugins.jetbrains.com/plugin/24154-git-
assistant](https://plugins.jetbrains.com/plugin/24154-git-assistant)
```
---

     
 
all -  [ How to get token costs per request  ](https://www.reddit.com/r/LangChain/comments/1ecqmk7/how_to_get_token_costs_per_request/) , 2024-07-28-0912
```
I have developed a tool calling llm using OpenAI's GPT-3.5-turbo-1106, integrated with LangSmith and LangGraph. I follow
ed the official documentation to track token usage but encountered issues:

1. **Final Response Metadata:** The final re
sponse doesn't include metadata about token usage.
2. **openai\_callback Function:** This method returns zero tokens use
d every time.

Here's the documentation link: [Token Usage Tracking](https://python.langchain.com/v0.1/docs/modules/mode
l_io/llms/token_usage_tracking/).

Could you assist me in obtaining the token cost per API request? Although LangSmith p
rovides token usage in their UI, I need to access this information programmatically in my application.
```
---

     
 
all -  [ Why does LangChain's BaseModel sometimes output a copy of the Pydantic field description instead of  ](https://www.reddit.com/r/LangChain/comments/1ecqk1q/why_does_langchains_basemodel_sometimes_output_a/) , 2024-07-28-0912
```
Hi everyone,

I'm currently exploring the Structured Output feature in LangChain for a personal project. I’ve been follo
wing the guide here: [LangChain Structured Output](https://python.langchain.com/v0.1/docs/modules/model_io/chat/structur
ed_output/).

Here’s a basic example I’m working with:

`from langchain_core.pydantic_v1 import BaseModel, Field`

`clas
s Joke(BaseModel):`  
`setup: str = Field(description='The setup of the joke')`  
`punchline: str = Field(description='T
he punchline to the joke')`

`model = ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0)`  
`structured_llm = model.w
ith_structured_output(Joke)`

`structured_llm.invoke('Tell me a joke about cats')`

I’ve experimented with more complex 
structures that include multiple fields and even nested fields. It’s important to note that not all fields necessarily c
ome from a single chunk of text, but they could.

However, I’ve encountered a problem: when the model can't find a value
 for a field, it returns the field’s description instead of leaving it blank or providing a default value. This results 
in unnecessary token generation.

I’m looking for a solution to set default values such as an empty string for string fi
elds and `-1` for numerical fields when the model doesn’t provide a value.

Has anyone else dealt with this issue? Is th
ere a method to ensure that missing field values are replaced with desired defaults rather than the field descriptions? 
Any insights or suggestions would be greatly appreciated!

Thanks in advance!
```
---

     
 
all -  [ Unleashing Git Commit Insights with JetBrains Git Assistant Plugin ](https://www.reddit.com/r/IntelliJIDEA/comments/1ecq3dp/unleashing_git_commit_insights_with_jetbrains_git/) , 2024-07-28-0912
```
Git Assistant is a powerful IntelliJ IDEA plugin that provides users with powerful Commits analysis tools through the Gi
t Assistant Insights window in the right-side tool window.

1. The Hour/Weekday/Month feature analyzes the distribution 
of team activity based on hours, weekdays, and months, optimizing work schedules and task assignments.
2. The Timezone f
eature visualizes the distribution of code contributions across different time zones, making global team collaboration v
isible and tangible.
3. The project tree on the left side also provides analysis capabilities for hot files and hot dire
ctories, helping developers better understand the recently changed files and directories in the project.

# Insights Vie
w

In the Overview panel, the most significant contributors in the code repository are displayed, helping identify and r
ecognize excellent contributors and enhancing teamwork and competitiveness.

https://preview.redd.it/vc52t97imved1.png?w
idth=3024&format=png&auto=webp&s=cd29f35342d43a414c7894f760aa7d6e97c17803

In the Hour/Weekday/Month panels, the distrib
ution of team activity over time is visualized, optimizing work schedules and task assignments.

https://preview.redd.it
/bztndp1omved1.png?width=3024&format=png&auto=webp&s=9f4ae8f130ad331730e59c45dfca2dd86d7cbbf0

https://preview.redd.it/l
1tbuo1omved1.png?width=3024&format=png&auto=webp&s=6dbf992933a9196affdb8db2977e18d80c0acfe2

https://preview.redd.it/zmc
lvp1omved1.png?width=3024&format=png&auto=webp&s=f5f08a4eb1af2dbd6b2566974f523e4bd81a9c20

In the Timezone panel, the di
stribution of code contributions across different time zones is visualized, making global team collaboration visible and
 tangible.

https://preview.redd.it/5wkc95rrmved1.png?width=3024&format=png&auto=webp&s=8bf2ebf23a1e6d1655e2dcdc95b79e26
09a0a4db

In the Project View panel, the analysis of hot files and hot directories is presented, helping developers bett
er understand the recently changed files and directories in the project.

https://preview.redd.it/yd63m7t813fd1.png?widt
h=3024&format=png&auto=webp&s=5a9add14c9ea7e931f0c3725f5a18f2063a66b16

[https://plugins.jetbrains.com/plugin/24154-git-
assistant](https://plugins.jetbrains.com/plugin/24154-git-assistant)
```
---

     
 
all -  [ GPT-4o-mini is terribly slow today. Anyone else facing this issue? ](https://www.reddit.com/r/LangChain/comments/1ecoex7/gpt4omini_is_terribly_slow_today_anyone_else/) , 2024-07-28-0912
```
https://preview.redd.it/hmxu408raved1.png?width=170&format=png&auto=webp&s=5bbc2d537d3c183ab7e684f0457754f38a967083

htt
ps://preview.redd.it/k0xf4x7raved1.png?width=170&format=png&auto=webp&s=725eb06885156a134e53e45e928089ffa8e5a97f

The la
tency on GPT-4o-mini is terrible today. It is taking 96 seconds and above for simple answers  

```
---

     
 
all -  [ What tools are you using with your AI agents? ](https://www.reddit.com/r/LangChain/comments/1ecn0fq/what_tools_are_you_using_with_your_ai_agents/) , 2024-07-28-0912
```
I'm playing around with Crew, Autogen and LangChain wanted to know what tools are best suited for Multi Agent applicatio
ns, where to find them or if I need to build them myself. 
```
---

     
 
all -  [ Build a chatbot by using Rag or openai gpt API? ](https://www.reddit.com/r/LangChain/comments/1eck671/build_a_chatbot_by_using_rag_or_openai_gpt_api/) , 2024-07-28-0912
```
I plan to build a chatbot to answer those product information. But I don't know which one to use, RAG or openai gpt?

I 
heard that RAG might not accurate and cant generate reply very well

Which one will you choose? 

If you want to build a
 chatbot like that, what will you use?
```
---

     
 
all -  [ I built a chatbot for Confluence and Jira documents. How do I improve on its performance and respons ](https://www.reddit.com/r/LocalLLaMA/comments/1ecjgvt/i_built_a_chatbot_for_confluence_and_jira/) , 2024-07-28-0912
```
Here are the components or the chatbot's workflow:

1. User asks query.
2. Llama-3 takes the query and says if it's a Ji
ra query or Confluence query. I call this the 'router agent'.
3. I take the output of the router agent and pass the user
 query on to either the Jira API or the Confluence API:
   * if its a Jira query:
      * Llama-3 takes the user query a
nd converts it into a Jira Query Language (JQL) query.
      * I query the Jira API with this JQL query and fetch the ou
tput as a JSON.
      * Llama-3 parses the JSON output, and rewrites the information in the format I specify in the prom
pt.
      * I stream this formatted response into the web interface.
   * if its a Confluence query:
      * I convert t
he user query into a Confluence Query Language (CQL) query.
      * I query the confluence API with this CQL query and f
etch the output as a list of confluence documents and corresponding web links.
      * Llama-3 'reads' each of these doc
uments in a loop one by one to identify if it's relevant to answer the user query.
      * I store the relevant document
s and their web links in a dictionary.
      * I pass the relevant docs to a self-deployed uncensored LLM with a large c
ontext window (Llama-3 is not uncensored and has a context window of only 8k tokens, so it was unable to take all the re
levant documents and also was refusing to answer some questions). In case its relevant, the uncensored LLM I'm using, ba
sed on experimentation, is Solar-10.7B-uncensored, and I have deployed it with Ollama inference server in my local kuber
netes cluster.
      * Solar-10.7B reads the relevant documents and answers the user query
      * I extract the web lin
ks stored previously and append to the final answer from Solar, and stream it in the web interface in the style of Perpl
exity (i.e., with citations in the response for the sources).
4. I then use the Deep Eval framework to evaluate the LLM 
responses against a golden dataset that I have prepared of 10 user queries and what should be their ideal responses, and
 use that evaluation result to tweak the prompts or the hyper-parameters of the LLMs.

Currently, the response quality i
s OK, but not the best it can be. Specifically, when asking the same question multiple times, the responses are not cons
istent, and often times it hallucinates facts (numbers, people's names, links, etc) despite explicitly stating in the pr
ompt that, 'Only answer based on the context you've been provided, do not make stuff up. If you don't know, say you don'
t know.' And the response time is around 10 seconds. I would like to improve on both of these. What are some things I ca
n try?

I have in mind the following:

1. Semantic caching of queries and responses. Although, I'm not sure how many peo
ple will ask the same question (with different wording), so I don't know how useful it would be to reduce the response t
ime overall.
2. Extending the golden dataset to, say, 100 examples of queries and ideal responses, and fine-tuning an un
censored LLM (doesn't have to be Solar) on it. But before spending a few days and a few 100 dollars on it, I want to ens
ure it'll do more than just change the style of responses.
3. RAG, but the thing is, docs get added to Confluence and Ji
ra all the time in real-time. So, downloading docs periodically and re-running the RAG pipeline frequently to update the
 vector store is not sustainable. Also, I'm not even 100% sure if there's an easy way to extract only new documents adde
d after XYZ date from Confluence and Jira.

Also, in case it's relevant, I have not used any framework like Langchain or
 Llamaindex in this project, all the steps I mentioned are implemented with custom functions I wrote. But I'm open to us
ing these and other frameworks if it helps improve upon the response quality and time.
```
---

     
 
all -  [ Memory leak in Langserve app ](https://www.reddit.com/r/LangChain/comments/1ecimvn/memory_leak_in_langserve_app/) , 2024-07-28-0912
```
I'm hosting a langserve app. The app is quite simple, but there seems to be a memory leak. Any ideas on why this is happ
ening?

With every new requests, the RAM increases and doesn't go down:  
  


https://preview.redd.it/9k9j0z7ikted1.png
?width=2256&format=png&auto=webp&s=dfe91726776cfabb5060e0da96ce4a41b858e724

https://preview.redd.it/2d0hncamkted1.png?w
idth=1128&format=png&auto=webp&s=51b95e833150a6bf810ff4f3ba736ef9b91da587



The code is pretty straightforward.   
Chai
n definition:  
# file: public\_review.py

    from langchain_core.output_parsers import JsonOutputParser
    from langc
hain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    
    from app.prompts.public
_review_analysis_prompt import (
        PUBLIC_REVIEW_ISSUE_GENERATOR_SYSTEM_PROMPT,
    )
    
    public_review_text_
chain = ChatPromptTemplate.from_messages(
        [
            (
                'system',
                PUBLIC_REVIE
W_ISSUE_GENERATOR_SYSTEM_PROMPT,
            ),
            ('user', '{text}'),
        ]
    ) | ChatOpenAI(model='gpt-
4o', temperature=0.03, model_kwargs={'seed': 13})
    
    
    public_review_chain = (
        | public_review_text_cha
in
        | JsonOutputParser(pydantic_object=IssueList)
    )
    
    

    # Chain added to router and router is then
 added to the app
    from fastapi import APIRouter
    from langserve import add_routes
    
    from app.enrichment.ag
gregator import aggregator_review_chain, aggregator_text_chain
    from app.enrichment.public_review import public_revie
w_chain, public_review_text_chain
    from app.enrichment.types import (
        InputFragment,
        InputFragmentLis
t
      )
    
    router = APIRouter()
    
    add_routes(
        router,
        public_review_chain.with_types(inpu
t_type=InputFragmentList, output_type=IssueList),
        path='/api/v1/public_review',
    )
    add_routes(router, pub
lic_review_text_chain, path='/api/v1/public_review/text')

  
  
  
Any ideas what could be causing the leak?
```
---

     
 
all -  [ The (proposal) trends for Devoxx Belgium 2024 ](https://i.redd.it/cb7biig6ated1.jpeg) , 2024-07-28-0912
```
ChatGPT generated the following keyword cloud for #Devoxx Belgium 2024 submitted proposals. 
The keywords are generated 
(also by ChatGPT) from the titles and abstracts submitted by the speakers for Devoxx Belgium 2024.
```
---

     
 
all -  [ Python : Opentelemetry - Filtering PII Data from Logs ](https://www.reddit.com/r/OpenTelemetry/comments/1ececxi/python_opentelemetry_filtering_pii_data_from_logs/) , 2024-07-28-0912
```
Hello,

Wondering if anyone has found a solution for filtering PII data from logs.

I'm building a python application fo
r a chatbot, and trying to solve the problem of redacting any reference to PII data in our logs which are currently bein
g stored in Application insights.

My attempt below (to add a custom span processor to intercept any PII data).

    # C
onfigure OpenTelemetry
    resource = Resource.create({'service.name': 'my_application'})
    provider = TracerProvider(
resource=resource)
    
    # Azure Insights Logging - Re-Enable this to bring logging back.
    appinsights_connection_
string = os.getenv('APPINSIGHTS_CONNECTION_STRING')
    processor = BatchSpanProcessor(
        AzureMonitorTraceExporte
r(connection_string=appinsights_connection_string)
    )
    provider.add_span_processor(processor)
    pii_redaction_pr
ocessor = PiiRedactionProcessor()
    provider.add_span_processor(pii_redaction_processor)
    
    exporter = AzureMoni
torMetricExporter(connection_string=appinsights_connection_string)
    reader = PeriodicExportingMetricReader(exporter, 
export_interval_millis=5000)
    metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
    trace.set_tracer
_provider(provider)
    
    # Console Logging
    console_exporter = BatchSpanProcessor(ConsoleSpanExporter())
    prov
ider.add_span_processor(console_exporter)
    
    # Instrument libraries
    RequestsInstrumentor().instrument()
    La
ngchainInstrumentor().instrument()
    OpenAIInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app)
   
 
    
    

To remove the PII data i've attempted to build a custom Span Processor:

    class PiiRedactionProcessor(Sp
anProcessor):
        def on_start(self, span: Span, parent_context: object) -> None:
            pass
    
        def 
on_end(self, span: Span) -> None:
            # Define regular expressions for common PII patterns
            pii_patte
rns = {
                'email': re.compile(r'[^@]+@[^@]+\.[^@]+'),
                'phone': re.compile(r'\+?[\d\s-]{7,1
5}'),
                'credit_card': re.compile(r'\b(?:\d[ -]*?){13,16}\b')
            }
    
            for key, valu
e in span.attributes.items():
                if isinstance(value, str):
                    for pattern_name, pattern i
n pii_patterns.items():
                        if pattern.search(value):
                            # Replace the PII 
part with [REDACTED] while keeping the rest of the string intact
                            redacted_value = pattern.su
b('[REDACTED]', value)
                            span.set_attribute(key, redacted_value)
                            b
reak

  
The code above results in an error about the Span being read only.:

  File '.py', line 70, in on\_end

span.se
t\_attribute(key, redacted\_value)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

AttributeError: 'ReadableSpan' object has no a
ttribute 'set\_attribute'. Did you mean: '\_attributes'?




```
---

     
 
all -  [ What kind of setup is needed to load an app’s source code into the “context” of an LLM to better out ](https://www.reddit.com/r/LocalLLM/comments/1ecdjmm/what_kind_of_setup_is_needed_to_load_an_apps/) , 2024-07-28-0912
```
I’m a developer but only have limited experience with LLMs. Mostly using the Chat GPT API, and langchain + Pinecone for 
RAG.

I want to play around with an LLM, loading an app’s source code into it, then trying to generate code from it afte
r it had been “trained” on the code. Can anyone point me in the right direction? Or maybe this already exists?

I’ve bee
n eyeing Llama 3.1 but the RAM requirements are insane. Want to see if it’s possible to get something working on one of 
its smaller models.
```
---

     
 
all -  [ Vision Analysis  ](https://www.reddit.com/r/LangChain/comments/1ec8c4e/vision_analysis/) , 2024-07-28-0912
```
I'm labeling and taking screenshot of webpages that I then send to 4V to analyze. Basically, the labeling creates border
s around html elements then I ask GPT to determine if there is a popup or if there are elements at certain places on the
 page. (I'm being a little vague due to the specific use case.) 

What would a good approach be for prompting? I am prov
iding reference images with explanations for each reference. Even though things are being labeled ok, I don't seem to be
 able to prompt it well. So I'm wondering if one prompting strategy over another might be good. 

Note that this flow is
 partially based on the WebVoyager paper that uses LangGraph, though it's not web browsing. Just a single labeled page. 

```
---

     
 
all -  [ How are you creating agentic tasks/workflows? ](https://www.reddit.com/r/ChatGPT/comments/1ec7oel/how_are_you_creating_agentic_tasksworkflows/) , 2024-07-28-0912
```
For all of you that are actively building things with llm capabilities: What tools are you using? What is the hardest pa
rt of building useful and effective agentic solutions for you? 

Autogen, Langchain and related, gpts, custom tech, priv
ate paid options, etc. what are you using and how do you feel about it?
```
---

     
 
all -  [ How do you build agentic workflows? ](https://www.reddit.com/r/LocalLLaMA/comments/1ec7kzy/how_do_you_build_agentic_workflows/) , 2024-07-28-0912
```
For those of you building, interested in building, or even experts in building them: what are you using? Have you found 
something that solves the boring part and lets you build? 

Autogen, Langchain, other private options: what do you use a
nd what is your opinion on the available tools? 
```
---

     
 
all -  [ Using Milvus/RAG as metadata store ](https://www.reddit.com/r/LangChain/comments/1ec02w8/using_milvusrag_as_metadata_store/) , 2024-07-28-0912
```
I've metadata( like table structure, column details, data types) of RDBMS and other sources currently stored in MYSQL da
tabase. I want to build  a simple bot that answers queries from data engineers and analytics like '

1.get me ddl of .. 
this table

2. what is the meaning of this column

3. show me complete column list with description of this table in pos
tgres environment: etc.

How can I use Vector db along with LLM to achieve this goal.

I'm not sure how to design a sche
me, whether to vectorize the name of the table alone etc.

N.B : Some of the tables can have 500 columns also.
```
---

     
 
all -  [ How to build agent with local llm ](https://www.reddit.com/r/LangChain/comments/1ebundi/how_to_build_agent_with_local_llm/) , 2024-07-28-0912
```
I'm new to langchain and currently learning the official \[tutorial\](https://python.langchain.com/v0.2/docs/tutorials/a
gents/). I have tried Ollama and llama.cpp, but none of them can finish the tutorial.

As known, Ollama doesn't support 
bind_tools originally. With the help of OllamaFunctions in langchain_experiment package, it worked and outputed similar 
intermediate information but failed when generating text according to response from tools.

When it comes to llama.cpp, 
it does have bind_tools function. The problem is that it didn't generate text according to response from tools.


So, is
 there a way to go through the tutorials with local llms or an example about finishing those tutorials with Ollama and l
lama.cpp? 
```
---

     
 
all -  [ Improving output of Azure Gpt 4 vision model , ignoring part of text present in image ](https://www.reddit.com/r/LangChain/comments/1ebt2gl/improving_output_of_azure_gpt_4_vision_model/) , 2024-07-28-0912
```
Hi I am trying to extract information from  purchase orders PDFs with different formats , when conventional py libraries
 didn't extract the data the way I wanted I resorted to Azure Gpt 4 vision model and converted the pages of my pdf as im
ages and used the api to get back the response. The problem is in some documents it is deliberately missing clearly writ
ten information in the images , I tried tweaking the prompt as well. But not helping much. I am using pdf2image to conve
rt to JPEGs and using 500 dpi as parameter in the convert_from_path function imported from library. Any recommendations 
or help would be much appreciated.
```
---

     
 
all -  [ Udemy Free Courses for 25 July 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1ebsti2/udemy_free_courses_for_25_july_2024/) , 2024-07-28-0912
```
# Udemy Free Courses for 25 July 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the cou
rses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11850/)Social Media Graphics Design and Video Editin
g with Canva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11849/)Personal Finance #2–Financial Statements
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/11848/)350 DevOps Interview Questions Practice Test
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/11847/)Excel Formulas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11846/)MSBI and S
SIS: Fundamentals to Advanced Data Integration
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11845/)Executive Dipl
oma in Business Management and Administration
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11844/)Uncovering Unco
nscious Bias in Recruiting
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11843/)Master Course in Digital Innovatio
n
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11842/)Executive Diploma in Leadership and Management
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/11830/)Master Course in Service Marketing 2.0
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/11841/)Industrial Cloud
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11840/)Blender Essential: 
From Beginner to 3D Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11839/)Mastering Cybersecurity Ranso
mware Incident Response (101)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11838/)Master Course in Bio-Inspired I
nnovation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11837/)Master Course in Healthcare Leadership
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/11836/)CDMP Course : Certified Data Management Professional (101)
* Master Cours
e in Smart Cities, Urban Planning
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11835/)
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/11834/)Burp Suite Mastery: From Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/11833/)Mastering Cybersecurity Vulnerability Management (101 Level)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/11832/)Master Course : Data Lakehouse Fundamentals in Data Science
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/11831/)Retail
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10768/)High-Tech Entrepreneurship & Strategic
 Entrepreneurship 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10852/)Microsoft Excel : Mastering Data Analys
is with Pivot Table
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10620/)Letter Writing Fundamentals
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10771/)Master Course in World Peace, Human Rights and Diplomacy 2.0
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/9679/)Professional Diploma in Life Coaching & Business Mentorship
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/10770/)Health Research, Public Health & Behavior Change 3.0
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/8319/)Learn ETABS & SAFE in the Structural Design of 15 Stories RC
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/10094/)Crafting Invitations with Elegance and Precision
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/7512/)Oracle Java Certification Exam OCA 1Z0-808 Preparation Part2
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/5950/)Airport Lounge Management & Cabin Crew Management 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/10622/)Writing with Impact: Compelling Articles and Letters
* Tenses Demystified: A Fundamental Introduction
* [R
EDEEM OFFER](https://idownloadcoupon.com/udemy/10652/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10621/)Demyst
ifying Computer Viruses: Types, Spread, and Protection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4861/)Choosin
g Your Career Path: Finding Your True Calling
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11418/)Master Course :
 Edge AI and Edge Computer vision (101 level)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10639/)Master Course i
n Blockchain Adoption 2.0 (101 level)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10636/)Presentation Skills -De
liver an Excellent Ceremonial Speech
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2973/)Traffic Security, Road Sa
fety, Public Security & Safety 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10619/)Cybersecurity Unveiled: Re
cognizing Its Vital Importance
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10560/)PHP Laravel: Build Hotel Booki
ng Management System
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8546/)Cybersecurity Digital Immune Systems (101
 level)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10773/)Master Course : UNO, WHO, UNICEF, UNESCO & SDGs (101 
level)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11746/)The Modern JavaScript for Beginners
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/11285/)Corporate Finance: Financial Analysis and Decision-Making
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/10769/)Master Course : E-Sports, Sports Business Management 2.0
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/10072/)Research and Evidence Gathering for Debates
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/11829/)Best Online Video Editor InVideo : 5 Real World Projects
* Master Web & Mobile Design: Figma, UI/UX Ess
entials, +More
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11828/)
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/11827/)Boris FX: BCC Transitions | VFX | Titling | Keying | Color
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/11826/)Autodesk Combustion: Beginner to Advanced VFX Techniques
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
11825/)Pro Lead Vocal Mixing Clinic
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11824/)Credit Evaluation and Len
ding Practices Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11823/)Securities Lending Market Mastery 
– A Comprehensive Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11822/)Maya Practical – 3D Animal and Charac
ter Modeling Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11821/)Adobe Flash Mastery – From Basics to Adv
anced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11819/)Hack-Proof Banking: Defend Against Credit Card Threats!

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11818/)Content Creator’s Roadmap: Ideation, Visibility, Repurposing

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11761/)Master The Art of Learning: Science-Based Study Techniques
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11394/)Терминал Linux. Основы работы в командной строке Линукс
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/7515/)Learn Blockchain and Cryptocurrency from Beginning
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/1995/)LPI Linux Essentials 010-160 Certification Exam Practice
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/2882/)UI/UX Design With Figma : 5+ Real World Projects
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/8276/)Advertising Strategy Fundamentals: Upskill to Drive Growth
* Indian Financial System: Banking| Tr
easury| Risk Management
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11820/)
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/7004/)Python And Django Framework And HTML 5 Stack Complete Course
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/7450/)ChatGPT Masterclass: The Ultimate Beginner’s Guide!
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/9647/)Professional Diploma in WEB3 NFT Business
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5937/)ChatGPT Ma
sterclass: Navigating AI and Prompt Engineering
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3454/)Build AI Chatb
ots, SAAS Apps \[AI Automation Agency + NoCode\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5884/)Professional 
Diploma in Advertising and Public Relations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11731/)Master CapCut Mob
ile Video Editing: Complete CapCut Tutorial
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11368/)ChatGPT Prompt En
gineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9357/)SQL практикум для начинающих и продолжающих

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11817/)The Basics of Linux Command Line
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/11803/)Learn Basics of Obsidian: Mastering Study Notes
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11804/)Learn Basics of Obsidian: Mastering Study Notes in Arabic
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/11805/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/11806/)Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/11807/)AWS Business Essentials – The Business Value of AWS \[2024\]

GET MORE FREE ONLINE COURSES WITH CERTIFICATE 
– [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Video RAM Problems on a server with a Rtx 4000 20gb ](https://www.reddit.com/r/LangChain/comments/1ebsdbv/video_ram_problems_on_a_server_with_a_rtx_4000/) , 2024-07-28-0912
```
Hey I don't know if this is the right sub. I rented a server that uses a Rtx 4000 with 20gb. I tried to get models like 
mistral or llamma to run on it but it fails to generate answers because it runs out of memory. Are there anyways to redu
ce the amount of memory needed? Or other ways to solve this problem? 
```
---

     
 
all -  [ SemanticChunker for very large text ](https://www.reddit.com/r/LangChain/comments/1ebs25f/semanticchunker_for_very_large_text/) , 2024-07-28-0912
```
I use Semantic Chunker from this tutorial: [https://python.langchain.com/v0.2/docs/how\_to/semantic-chunker/](https://py
thon.langchain.com/v0.2/docs/how_to/semantic-chunker/)

  
However, I met the error below. I think because my pdf has 64
 pages. Too long for OpenAI to handle. What should I do? If I split page by page, I am afraid that I will lost the conte
nt between pages. Recursive Chunker seems better in this case. 

>openai.InternalServerError: Error code: 503 - {'error'
: {'code': 'InternalServerError', 'message': 'The service is temporarily unable to process your request. Please try agai
n later.'}}

>python-BaseException
```
---

     
 
all -  [ Why does EmbeddingStoreContentRetriever Not output directly Score in Java Langchain ?  ](https://www.reddit.com/r/LangChain/comments/1ebo69l/why_does_embeddingstorecontentretriever_not/) , 2024-07-28-0912
```
Why does EmbeddingStoreContentRetriever Not output directly Score in Java Langchain ?   
  
It tells us to output, based
 on minScore, but no possibility to get score directly? Why is it ?

  
how would I go about implementing it in java or 
am I missing something

How can I get this score ?

  
this is how it looks like

  
`public class EmbeddingStoreContent
Retriever implements ContentRetriever` 

`{`

 `private final EmbeddingStore<TextSegment> embeddingStore;` 

`private fi
nal EmbeddingModel embeddingModel;` 

`private final Function<Query, Integer> maxResultsProvider;` 

`private final Func
tion<Query, Double> minScoreProvider;` 

`private final Function<Query, Filter> filterProvider;` 

`}`
```
---

     
 
all -  [ Ai interviewer technique ](https://www.reddit.com/r/LangChain/comments/1ebnkqo/ai_interviewer_technique/) , 2024-07-28-0912
```
I want to explore how these website with ai interviewer works like do they only works on the audio or they process the v
ideo also realtime. It is very fascinating to me. 
If anyone have any idea in this field, would happy to know your thoug
hts. 
```
---

     
 
all -  [  A Comprehensive Guide: Boosting EHR Efficiency with LangChain.js ](https://www.reddit.com/r/u_bluebashllc/comments/1ebng9f/a_comprehensive_guide_boosting_ehr_efficiency/) , 2024-07-28-0912
```
LangChain.js is a robust JavaScript library for working with language models like GPT-3. It simplifies text generation, 
summarization, and information extraction, making it a perfect fit for enhancing EHR systems.The healthcare industry has
 made significant strides with Electronic Health Records (EHR), but managing the volume and complexity of unstructured d
ata in these systems is still a major hurdle. That's where LangChain.js comes in! LangChain.js is a robust JavaScript li
brary for working with language models like GPT-3. It simplifies text generation, summarization, and information extract
ion, making it a perfect fit for enhancing EHR systems.

**Problem Statement**  

EHR systems are designed to handle vas
t amounts of data, including structured data like patient demographics and unstructured data like doctor's notes. Unstru
ctured data often contains crucial information about a patient's condition, treatment plan, and progress. Manually extra
cting and summarizing this information is time-consuming and prone to errors. Automated solutions are needed to efficien
tly process and extract relevant information from unstructured EHR data.

[ Boosting EHR Efficiency with LangChain.js](h
ttps://preview.redd.it/yi4kxhpitled1.jpg?width=1920&format=pjpg&auto=webp&s=041c1ddcceae6cd26cf8552dd92953c0509067a1)

*
*Understanding LangChain.js**  

[LangChain.js](https://www.bluebash.co/blog/ehr-efficiency-langchain-js/) allows develo
pers to build applications using advanced language models, providing an easy-to-use interface for working with text data
. It's particularly valuable for handling the unstructured data often found in EHR systems. With LangChain.js, you can p
erform a wide range of natural language processing (NLP) tasks including text generation, summarization, and information
 extraction. This helps streamline the integration of sophisticated language models into applications, enhancing the abi
lity to manage and interpret large volumes of textual data.

**Key Features of LangChain.js:**

1. **Text Generation:** 
Generate coherent and contextually relevant text based on the input provided.
2. **Summarization:** Condense long pieces
 of text into concise summaries.
3. **Information Extraction:** Extract specific information from large volumes of text,
 making it easier to find relevant data.

**Use Case: Enhancing EHR Systems with LangChain.js**  

Let's delve into a pr
actical use case of utilizing LangChain.js to significantly enhance an EHR system. In this scenario, we will concentrate
 on the process of extracting crucial patient information from unstructured text data, which could include a variety of 
sources such as doctor's notes, clinical reports, and patient histories. By leveraging the capabilities of LangChain.js,
 we can efficiently generate comprehensive summaries that provide healthcare professionals with a quick and effective me
ans of reviewing critical patient information. This not only streamlines the workflow but also ensures that important de
tails are readily accessible, ultimately improving patient care and decision-making processes.

1. **Setting Up LangChai
n.js:** First, you need to install LangChain.js using npm.
2. **Extracting Information from Doctor's Notes:** Automate t
he extraction of valuable information about a patient's condition, treatment plan, and progress.
3. **Summarizing Patien
t Records:** Generate concise summaries from lengthy patient records, giving healthcare professionals a quick overview o
f a patient's medical history
```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-07-28-0912
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-28-0912
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-28-0912
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-28-0912
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
