 
all -  [ What's the scoop on serialization? It's all over the show with LangChain ](https://www.reddit.com/r/LangChain/comments/1cp3y1l/whats_the_scoop_on_serialization_its_all_over_the/) , 2024-05-11-0910
```
Hi am I doing something wrong?

I'm using Documents and I want to save/load them. I've tried, \`.json()\` the new \`load
\` module's \`.dumpd()\` and \`.load()\` -- but some documents can't be deserialized.

e.g. I am trying to build somethi
ng that uses LangChain documents. But not all of them are deserializable -- instead you get goop like this when using th
e output of \`ContextualCompressionRetriever\` (which returns some documents) and use one of the above functions to seri
alize:

https://preview.redd.it/74vlfp1wsozc1.png?width=417&format=png&auto=webp&s=0d3d238376da4f9305eed45ee212ce8736025
26e

Basically I have to parse the repr to get the document? Any pointers? Or write my own custom serialization/deserial
ization?
```
---

     
 
all -  [ Ai generated ad that was on my feed ](https://i.redd.it/doitcfsajozc1.jpeg) , 2024-05-11-0910
```
How lazy is a company to use AI?
```
---

     
 
all -  [ Getting Answers from GPT based on document ](https://www.reddit.com/r/OpenAI/comments/1cp0tzk/getting_answers_from_gpt_based_on_document/) , 2024-05-11-0910
```
Using the api how to give a large amount of information then receive answers from the given data. 

What is the best, mo
st cost efficient solution.
Assistants API? Langchain?
```
---

     
 
all -  [ how to get LLM to infer dates from a json file or text file? ](https://www.reddit.com/r/LangChain/comments/1coz2io/how_to_get_llm_to_infer_dates_from_a_json_file_or/) , 2024-05-11-0910
```
im currently using mistral-small in my project, i want to create a chatbot that can give answers about the weather in th
e future, so i have a huge json file that i want to feed to the model as a vector embedding and then let the user ask th
e chatbot questions about future weather such as what should i wear tomorrow etc.

the problem is that the LLM seems to 
not read the files, i even tried to programatically rebuild the file as a text file.

this is my code:

\`\`\`

    json
_loader = JSONLoader('C:\\xxxx\\data\\all_weather_by_date.json')
    
    
    # Split text into chunks
    text_splitte
r = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    # Define the embedding mode
l
    embeddings = MistralAIEmbeddings(model='mistral-embed', mistral_api_key='XXXXXXXXXXXXXXXXXXXXXXX', )
    # Create 
the vector store 
    vector = FAISS.from_documents(documents, embeddings)
    vector.save_local('cache')
    
    # Def
ine a retriever interface
    retriever = vector.as_retriever()
    # Define LLM
    model = ChatMistralAI(mistral_api_k
ey='XXXXXXXXXXXXXXXXXXXXX', model='mistral-small', temperature=1)
    # Define prompt template
    prompt = ChatPromptTe
mplate.from_template('''
    
    <context>
    {context}
    </context>
    
    Question: {input}''')
    
    # Creat
e a retrieval chain to answer questions
    document_chain = create_stuff_documents_chain(model, prompt)
    retrieval_c
hain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'context': instructions,
'input': f'answer max 60 words, end with follow-up question, no clauses: what should i wear tomorrow? today is 10.5.2024
'})
    print(response['answer'])

\`\`\`

my json is built like this:

{

'current\_year\_dates' : {

'2024.05.11' : {


'humidity': '50%',

'degrees': '34'

}

.... all the other dates throught the year

}

when i attempted to change the j
son file to text file, i changed it to this format:

'on 2024.10.5 there will be 50% humidity and 30 degress.'

and stil
l it didnt work



also i have always get a warning when running my code about HF\_TOKEN not being set and using len spl
itter.

please help me!
```
---

     
 
all -  [ LangChain 0.2 prerelease ](https://www.reddit.com/r/LangChain/comments/1coyy48/langchain_02_prerelease/) , 2024-05-11-0910
```
hi all! we're gearing up for a release of langchain 0.2. The main change is no longer depending on langchain-community (
this will increase modularity, decrease size of package, make more secure). We're also adding in a new docs structure an
d highlighting a bunch of the changes we made as part of 0.1

We posted more about this on GitHub (https://github.com/la
ngchain-ai/langchain/discussions/21437) but happy to answer any questions here! Would obviously love and really apprecia
te any feedback :)
```
---

     
 
all -  [ Library that automatically creates a UI for your chatbot? ](https://www.reddit.com/r/LangChain/comments/1cot1we/library_that_automatically_creates_a_ui_for_your/) , 2024-05-11-0910
```
[Cycls](https://docs.cycls.com/getting-started) Python library significantly simplifies the development of AI chatbots f
or developers, particularly those who specialize in backend development and may find creating user interfaces tiring. Th
is library eliminates the need to develop a UI from scratch by providing a prebuilt, ChatGPTlike user interface that dev
elopers can use immediately. By simply importing Cycls into your project, you can integrate it with major LLM Python lib
raries and APIs, enabling the use of various LLM models easily.

Upon importing and running your application, it is auto
matically deployed with the user interface and a public URL, enhancing the efficiency of both development and testing pr
ocesses. This feature is especially valuable for speeding up deployment and reducing the workload on developers focusing
 on backend functionalities.


```
---

     
 
all -  [ duckduckgo_search with langchain ](https://www.reddit.com/r/duckduckgo/comments/1coso6p/duckduckgo_search_with_langchain/) , 2024-05-11-0910
```
am using duckduckgo\_search with langchain community , it was working fine but am getting rate limit error i have alread
y tried to upgrade but still the same error . is there any one who can tell me why
```
---

     
 
all -  [ Nomic embeddings with Ollama using Langchain up to Pinecone ](https://www.reddit.com/r/ollama/comments/1corjsr/nomic_embeddings_with_ollama_using_langchain_up/) , 2024-05-11-0910
```
Anyone attempted this yet?  I have a lot of familiarity using open AI embeddings up to Pinecone and I want to switch to 
Nomic. 

Reviewed the Langchain Python documentation on using nomic embeddings and it seems incomplete to enable me to p
ush up embeddings and text and metadata in the format that I’m used to with OpenAI’s embeddings and pinecone. 


```
---

     
 
all -  [ Would LC be a good platform for building a LLM-based chat which builds user profiles? ](https://www.reddit.com/r/LangChain/comments/1cooqdx/would_lc_be_a_good_platform_for_building_a/) , 2024-05-11-0910
```
Would LC be a good <framework> for building a LLM-based chat which builds user profiles?

For example, over the course o
f the conversation it could fill slots such as name, location, etc. 

or there an off the shelf tool which is already do
ing this? 
```
---

     
 
all -  [ Just a question on LCEL vs RetrievalQA ](https://www.reddit.com/r/LangChain/comments/1colp4k/just_a_question_on_lcel_vs_retrievalqa/) , 2024-05-11-0910
```
Hi all, in the previous version of code, I had something like this:

qa = RetrievalQA.from\_chain\_type(  
 llm=llm,  
 
chain\_type\_kwargs={'prompt': prompt},  
 retriever=retriever,  
 return\_source\_documents=True,          
 tags = tag
s,  
 metadata = metadata          
 )  
basically its a Multivector retriever with RetrievalQA.   In LCEL chain it is l
ike below:

chain = (  
{'context': retriever, 'question': RunnablePassthrough()}  
 | prompt  
 | model  
 | StrOutputP
arser()  
)  
The question I have is, how to add additional parameters in the above LCEL chain?   
additional parameters
:  
return\_source\_documents=True,          
tags = tags,  
metadata = metadata   
```
---

     
 
all -  [ Phi3 text2sql ](https://www.reddit.com/r/LangChain/comments/1colhlx/phi3_text2sql/) , 2024-05-11-0910
```
Has anyone tried phi3 for text2sql in postgres? I am trying and can't generate a correct query
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1cola2g/for_hire_programmerweb_developerit_consultant/) , 2024-05-11-0910
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

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/learnpython/comments/1col188/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-11-0910
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time.

So I wanna learn how to manage these kind of sessions and using credentials is
 not an option.

one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Function Calling + RAG + Langchain Tool Calling Agent + REDIS Memory ](https://www.reddit.com/r/LangChain/comments/1cokru8/function_calling_rag_langchain_tool_calling_agent/) , 2024-05-11-0910
```
Tell me if this idea is feasible and how I can pull this off

I have a langchain agent that does function calling, but o
ne shortcoming is that it fails to answer queries from the pulled data many times, 

Can I store this pulled data into a
 knowledge graph vector database as this data is for holiday packages with key value relations such as duration, price, 
location, ref\_id etc and sub categories like fare sets, cabin sub categories etc. 

How can I make my langchain agent i
n python better using knowledge graphs and making it answer follow up questions using RAG on the last fetched data?


```
---

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/LangChain/comments/1cokd2v/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-11-0910
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time. 

So I wanna learn how to manage these kind of sessions and using credentials i
s not an option.

  
one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Profile Review ](https://i.redd.it/0dwb8qutwjzc1.jpeg) , 2024-05-11-0910
```
Thoughts on my profile? Trying to land full-stack AI jobs. Interested in any feedback, even if it’s brutal as long as it
’s actionable.
```
---

     
 
all -  [ Evaluation Models - GPT-3.5 vs. GPT 4 Turbo ](https://www.reddit.com/r/LangChain/comments/1coj65b/evaluation_models_gpt35_vs_gpt_4_turbo/) , 2024-05-11-0910
```
hey guys

I use correctness, hallucination & relevance score to evaluate a RAG chain on langsmith. 

Generally, do you t
hink 3.5 is good enough to evaluate the outcomes?
```
---

     
 
all -  [ LLAMA2 (and Other Models) Engaging in Self-Dialogue: Asking and Answering Its Own Questions ](https://www.reddit.com/r/LLMDevs/comments/1coigub/llama2_and_other_models_engaging_in_selfdialogue/) , 2024-05-11-0910
```
I am using Langchain + different LLM models ('Llama-2-7b-chat-hf', 'Mistral-7B-Instruct-v0.2', ...)..

\*\*My purpose\*\
* is to do prompt engineering and evaluate a model's ability to answer various questions.

\*\*The challenge\*\* is that
 after posing almost any question, the LLM starts a self-conversation, asking itself questions as a 'Human' and then ans
wering them as an 'AI.'

\*\*What am I missing?\*\*

\*\*How can I ensure\*\* the model only responds to the original qu
estion without engaging in a self-conversation?

    conversation = ConversationChain(
      llm=self.llm,
      memory=
ConversationBufferMemory(),
      verbose=False)
    
    print('*************************** chat_conversation *********
******************')
    
    while True:
      user_input = input('> ')            
      ai_response = conversation.pr
edict(input=user_input)
      print('\nAssistant:\n', ai_response)
      print('----------------------------------------
--------------------------------------------------------------\n\n\n')



Example for a prompt:



https://preview.redd.
it/cprggyrahjzc1.png?width=1458&format=png&auto=webp&s=2b9b230a3123d415b7015c7131f5eddf44efedb5

  


  

```
---

     
 
all -  [ How to add JsonOutputParser with RunnableWithMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1cofbkc/how_to_add_jsonoutputparser_with/) , 2024-05-11-0910
```
This my code

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,

        input_messages_key='input',
        history_messages_key='chat_history',
        output_messages_key='answer',

    )
    
    conversational_rag_chain.invoke(
        {'input': 'I am interested in Screwdrivers, Sockets, Ratchets. N
ow generate new questions based on past behaviour'},
        config={
            'configurable': {'session_id': 'abc123
'}
        },  # constructs a key 'abc123' in `store`.
    )['answer']
    

I want to add this \`JsonOutputParser\` to 
above \`conversational\_rag\_chain\`

    class ProbingQuestion(BaseModel):
        Question: str = Field(description='p
robing question')
        Options: List[str] = Field(description='list of options for the probing question')
    
    
 
   output_parser = JsonOutputParser(pydantic_object=ProbingQuestion)



So can anyone help this?
```
---

     
 
all -  [ A Daily chronicle of AI Innovations May 09th 2024: 🤖 OpenAI posts Model Spec revealing how it wants  ](https://readaloudforme.com/index_subscribers) , 2024-05-11-0910
```
A Daily chronicle of AI Innovations May 09th 2024: 
🤖 OpenAI posts Model Spec revealing how it wants AI to behave 
🧬 Goo
gle DeepMind unveils AlphaFold 3, the next generation of its protein prediction model 🧠 Neuralink faces setback as first
 human brain implant encounters problem 
🕵️‍♀️  Microsoft developed a secretive AI service for US spies 
🎨 Generate imag
es on Midjourney Alpha 📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts 
🏢New AI data cent
er to be built at the failed Foxconn project site in Wisconsin 
🤔Sam Altman says we are not taking AI’s impact on the ec
onomy seriously 
✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows 🎮Altera’s gaming AI
 agents get backed by Eric Schmidt, Former Google CEO

 

🤖 OpenAI posts Model Spec revealing how it wants AI to behave


 

OpenAI has introduced the first draft of Model Spec, a proposed framework aiming to shape how AI models respond, emp
hasizing assistance, humanity's benefit, and adherence to social norms and laws.
The framework suggests specific rules f
or AI behavior, including compliance with laws, protection of privacy, and avoidance of NSFW content, with options to ad
just settings like allowing NSFW content in certain contexts.
While the Model Spec seeks public feedback for future adju
stments and doesn't immediately affect existing models like GPT-4 or DALL-E 3, it's envisioned as a living document to g
uide AI behavior improvement over time.
Source: https://readaloudforme.com/index_subscribers

🧬 Google DeepMind unveils 
AlphaFold 3, the next generation of its protein prediction model 

https://youtu.be/9ufplEgtq8w?si=XAREDQVZwYLBtcss



G
oogle DeepMind and Isomorphic Labs have released AlphaFold 3, a new AI model for predicting protein structures, includin
g their interactions with various molecules such as DNA, RNA, and small molecules, thereby enhancing drug discovery poss
ibilities.
This new version is more precise in mapping out complex groupings of molecules, significantly enhancing our a
bility to understand and predict molecular behavior compared to its earlier version.
Google will not open-source this ve
rsion but has launched AlphaFold Server for non-commercial research use, aiming to balance intellectual property concern
s with accessibility for scientific progress.
Source: https://readaloudforme.com/index_subscribers

🧠 Neuralink faces se
tback as first human brain implant encounters problem 

Neuralink admitted that some of the micro-thin threads from thei
r N1 brain chip retracted after implantation in the first human patient, possibly due to air trapped in the skull during
 surgery, which affected the device's data transmission rate.
Despite the retraction of several threads, Neuralink manag
ed to increase the data transmission speed over time by optimizing their recording algorithm and improving signal transl
ation into cursor movements.
The company is planning further implants, with goals to implant two more patients in the co
ming months and ten in total this year, while continuing to refine their technology and reporting developments to the FD
A.
Source: https://readaloudforme.com/index_subscribers

🕵️‍♀️ Microsoft developed a secretive AI service for US spies


Microsoft has developed a top-secret generative AI model entirely disconnected from the internet so US intelligence agen
cies can safely harness the powerful technology to analyze top-secret info. The model based on GPT-4 is now live, answer
ing questions, and will also write code.

Microsoft spent 18 months developing the model, which is 'air-gapped' to ensur
e it is secure. This is the first time a model is fully isolated– meaning it's not connected to the internet but is on a
 special network that's only accessible by the U.S. government.

It can read and analyze files but cannot learn from the
m to stop sensitive information from entering the platform. It is yet to be tested and accredited by the intelligence ag
encies.

Why does this matter?

Intelligence agencies all over the world have been racing to be the first to harness gen
erative AI. I guess we know who’s going to be the winner. If this AI tool is successful, it will fundamentally change th
e way intelligence agencies operate.

Source: https://readaloudforme.com/index_subscribers

What Else Is Happening in AI
 on May 09th 2024❗

📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts

In coming months, Mi
crosoft Copilot will be updated with new features like auto-complete and ‘elaborate your prompt’ that offer suggestions 
to improve AI prompts. It aims to solve the problem of coming up with good prompts for generative AI. (Link)

🏢New AI da
ta center to be built at the failed Foxconn project site in Wisconsin

President Joe Biden announced an AI data center t
o be built on the same site as the failed Foxconn project in Racine, Wisconsin. According to a White House press release
, Microsoft is investing $3.3B in the project, creating up to 2,000 permanent jobs. (Link)

🤔Sam Altman says we are not 
taking AI’s impact on the economy seriously

At a Brooking's Institute panel about AI and geopolitics on Tuesday, Altman
 said the discussions around AI's effect on the economy–  like how it may lead to mass job replacement– died down this y
ear compared to last. He said if we don’t take these concerns seriously enough going forward, it could be a massive issu
e. (Link)

✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows

It is launching Typeface
 Arc technology, which enables a user to state a high-level marketing objective and then have the system automatically p
lan and generate all the assets, including emails, images, and notifications that are all connected. (Link)

🎮Altera’s g
aming AI agents get backed by Eric Schmidt, Former Google CEO

Altera is the newest startup joining the fray to build a 
new guard of AI agents. It raised $9 million in an oversubscribed seed round, co-led by Eric Schmidt’s deep-tech fund, F
irst Spark Ventures and Patron, the seed-stage fund co-founded by Riot Games alums. (Link)

 

AI TRAINING May 09th 2024


🎨 Generate images on Midjourney Alpha

Generate images on Midjourney Alpha 
Midjourney’s website is now accessible to 
anyone with more than 100 generated images, improving the experience when prompting images over its standard Discord gro
up.

Check that you’ve generated more than 100 images by typing /info in the Midjourney Discord group. If you have, head
 over to Midjourney Alpha.

In the main menu, you can explore other creations and search prompts.

Select where it says 
“imagine” and enter your prompt to generate an image.

Add a reference image by selecting “+” or play with different par
ameters such as image size, stylization, or even weirdness by pressing the “slider control” button

AI RESEARCH on May 0
9th 2024

📶 AI usage surges in the workplace

AI usage surges in the workplace
Microsoft and LinkedIn just published the
ir Work Trend Index Annual Report, revealing that AI adoption is surging in the workplace — calling 2024 the ‘year AI at
 work gets real’.

The report found that use of GenAI has doubled in the last six months, with 75% of knowledge workers 
using the tech in some capacity.

78% of AI users are bringing their own AI to work — with 52% reporting they are reluct
ant to admit to its use.

66% of leaders wouldn't hire someone without AI skills, and 71% prefer less experienced candid
ates with AI aptitude over a more experienced one without it.

AI power users reported enhanced productivity, creativity
, and job satisfaction compared to skeptical peers.

Why it matters: Employees are adopting AI at a rapid pace, regardle
ss of if their own organizations are ready for the shift. As AI spreads across all sectors, generations, and skillsets, 
the early adopters are rising to the top — while those that aren’t at least exploring the tech are quickly running out o
f time

Trending AI Tools May 09th 2024

📍GeoSpy - Uncover photo locations with AI

🧑‍💻 LangChain - Connect LLMs to priv
ate data for context-aware applications

📊 Abstra - Scale business processes with Python and AI

🎨 Freepik Pikaso Upscal
er - Integrated with Magnific, enlarge images without losing quality

💬 Notion AI Q&A - Q&A is now open to the public, a
llowing users to ask and find information across their workspace

🎵 Udio Audio Inpainting - Select a portion of an AI-ge
nerated music track and regenerate it

New AI Job Opportunities on May 09th 2024

🎥 The Rundown - Video Content Creator


🤖 Anthropic - Research Engineer, Human-Computer Interfaces

👩‍💻 Adept AI - Solutions Engineer

📝 Mistral AI - Data Anno
tation Technical Program Manager

```
---

     
 
all -  [ How can I go about creating knowledge graphs from chunks of a document? ](https://www.reddit.com/r/LangChain/comments/1codtrj/how_can_i_go_about_creating_knowledge_graphs_from/) , 2024-05-11-0910
```
I want to improve the quality of retrieval for my RAG application. I have a knowledge base with multiple pdfs and docs, 
and currently I'm using basic recursive splitter with overlap for creating chunks. This is not the most effective way, a
nd I'm thinking of using semantic or agentic chunking to improve the quality of my chunks.

Furthermore, I'm also thinki
ng to use knowledge-graphs for this usecase. Now I understand how knowledge-graphs work but I'm not sure how I can use t
hem for my usecase.

Firstoff, I would need to define some nodes (which could be my chunked documents itself I believe) 
but I'm unsure about how to and to what extent create relationships between those nodes. Again, this is my theory, would
 love to understand if nodes could be something else here.

IF, I decide on nodes being documents, how should I decide p
arameters for my relationships? Do I need to make LLM calls for this? -- this would incur more cost I as I keep adding d
ocuments to my knowledge base.

I'm thinking of extracting key entities from each document, and use those as the basis o
f relationship but -- for that I would need a model for extraction (which I guess, I could find some standard NLP techni
que that are not LLM or even SLM based).

Any thoughts on this would be appreciated. Thanks!
```
---

     
 
all -  [ Iterating hundreds of csv file headers, trying to find the best way to identify related headers usin ](https://www.reddit.com/r/LangChain/comments/1code3k/iterating_hundreds_of_csv_file_headers_trying_to/) , 2024-05-11-0910
```
I have a Neo4j graph that's populated with common category nodes, and sub-nodes. These all have labels and names, other 
than that there is no data stored inside the properties. I want to find a way to identify related headers for that parti
cular category node, for example 'economic', if a column in one of the CSV files is related to economics then it should 
be either be added as a new node to that category node or the data inside that cell from the csv be added as a property 
to an existing node. I'm wondering what everyone also thinks is the best way to set all this up as I am trying to make t
his Graph as efficient as possible because the plan is to add an LLM on top of it with a chatbot to query to graph for c
ontext and return answers.  

```
---

     
 
all -  [ LangChain SQL & Mistral ](https://www.reddit.com/r/LangChain/comments/1cod9zr/langchain_sql_mistral/) , 2024-05-11-0910
```
Hi guys,

Recently I am experimenting on using mistral 7b instruct-v0.1 with sql database, and I have try 3 approach, bu
t all of these give me several errors and issues, and I really cannot fix it.  
Approach 1 (source=[Tal to your database
 using RAG and LLM](https://medium.com/@shivansh.kaushik/talk-to-your-database-using-rag-and-llms-42eb852d2a3c))

https:
//preview.redd.it/hr1yz5w30izc1.png?width=767&format=png&auto=webp&s=2de4ee09e1b184434f3c6baf0a7040000987dbed

https://p
review.redd.it/uyas7shgjdzc1.png?width=953&format=png&auto=webp&s=61b093e5253e193c1f02d69ba6890566a25858a9

This give me
 the error as above, but i thought the question is already a string? And it's so weird to give me 2 SQL Result and answe
r.  


Approach 2 (source is from a youtube)

https://preview.redd.it/n4vj9z2e0izc1.png?width=930&format=png&auto=webp&s
=3d9ea5d0b76e5ba224f1a55e2abb7b5f130de8d0

Approach 3

https://preview.redd.it/wdc8l03j0izc1.png?width=750&format=png&au
to=webp&s=0dcff653e8367b20ad6b4dcba5742bd4d7585bb9

  
This same as approach 1, it gives me 2 different result and answe
r.  
How if i want just only the final answer? How can I get it? print(result\[Answer\])?  

```
---

     
 
all -  [ Vectorsearch for chat history? ](https://www.reddit.com/r/LangChain/comments/1coaa4f/vectorsearch_for_chat_history/) , 2024-05-11-0910
```
Hi guys,
I'm working on a chatbot for our company and we use ChatGPT 4 as an LLM. To keep the costs per request low, I i
mplemented a chat history with only the last 6 messages (3 from user, 3 from bot)

The problem now is, that sometimes pe
ople have inputs that the bot can't answer well, as the messages are already gone in his memory.

Is there any good way 
to fix this? 
Is it possible to use vectorsearch for memory? Or does this heavily increase the latency?

What is the bes
t way to go, what are you guys using?
```
---

     
 
all -  [ LangChain ReAct Argumentation Agent ](https://www.reddit.com/r/LangChain/comments/1co86cn/langchain_react_argumentation_agent/) , 2024-05-11-0910
```
Hello,

Currently, I'm using LangChain to develop a ReAct agent to develop evidence-based arguments supporting the user'
s input. I've successfully developed a Tool that can access data from a web source based on what the model queries. ReAc
t seems like a sensible pattern for this use case, but the model gets stuck in a loop, repeatedly asking the same query 
of the tool. I've also noticed that the conversation history is not populated.

Here is the code I developed. The `searc
h_cse(query)` function just returns the title and text of an article.

    from keys import GOOGLE_GEMINI_API_KEY
    fr
om google_website_scrape import search_cse
    import langchain
    from langchain_core.tools import Tool
    from langc
hain.agents import initialize_agent, AgentType
    from langchain_google_genai import ChatGoogleGenerativeAI
    from la
ngchain.memory import ConversationBufferMemory
    
    langchain.debug = True
    
    llm = ChatGoogleGenerativeAI(
  
      model='gemini-1.0-pro',
        google_api_key=GOOGLE_GEMINI_API_KEY
    )
    tools = [
        Tool(
           
 name='cbs_articles',
            description='This tool provides the content of CBS News articles that pertain to the r
equest.',
            func=search_cse
        )
    ]
    
    PREFIX = '''You are an agent designed to construct argume
nts to fulfill the user's request, specified in the input.
    You arguments must include evidence from CBS News article
s.'''
    FORMAT_INSTRUCTIONS = '''You MUST use the following format: Question, Though, Action, Action Input. This forma
t is explained in further depth below:
    
    Question: This should be the input.
    Thought: You should think about 
arguments to fulfill the user's request.
    Action: Should ALWAYS BE 'cbs_articles'. Do NOT use any other action.
    A
ction Input: This should be a search term that will give you information pertaining to the argument you are trying to ju
stify.
    Observation: You should consider how the information you found supports your argument.
    ... (this Thought/
Action/Action Input/Observation can repeat N times)
    Thought: I now have multiple arguments WITH EVIDENCE to fulfill 
the user's request.
    Final Answer: Here are the arguments WITH EVIDENCE to fulfill the user's request.'''
    SUFFIX 
= '''Begin!
    
    Input: Justify the following: '{input}'
    Thought: {agent_scratchpad}
    Chat History: {chat_his
tory}'''
    
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    agent = initial
ize_agent(
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        agent_kwar
gs={
            'prefix': PREFIX,
            'format_instructions': FORMAT_INSTRUCTIONS,
            'suffix': SUFFIX,

            'input_variables': ['input', 'agent_scratchpad', 'chat_history']
        },
        memory=memory,
        
verbose=True,
        handle_parsing_errors=True,
        max_iterations=10
    )
    
    print(agent.run('Electric veh
icles should not be mandated nationally.'))

With this code, the model repeatedly asks itself the following.

    Questi
on: Electric vehicles should not be mandated nationally.
    Thought: Electric vehicles are still too expensive for many
 people.
    Action: cbs_articles
    Action Input: Electric vehicles cost
    Observation:
    [ARTICLE TITLE & CONTENT
]

Please advise me if I'm using the ReAct pattern incorrectly. Thank you for your time.
```
---

     
 
all -  [ Llama3 slow inference ](https://www.reddit.com/r/learnmachinelearning/comments/1co759v/llama3_slow_inference/) , 2024-05-11-0910
```
I'm currently using llama3 for a rag app. I'm using ollama and langchain's chatollama function to run inference. Prompti
ng the model takes between 10 to 30 seconds to return a json response. Is there any way to significantly reduce this inf
erence time (particularly, to under 1 sec)? 

Also, I've heard that Mojo can be used for speeding up machine learning ap
ps. Is there a Mojo implementation of llama3 available?
```
---

     
 
all -  [ RAG Retrieval Evaluation ](https://www.reddit.com/r/LangChain/comments/1co5cl1/rag_retrieval_evaluation/) , 2024-05-11-0910
```
Hey,

Like many others I am working on a RAG Q&A Chatbot.  I have many pdfs related to a certain topic. My goal is to he
lp the end-user answer questions based on the information in the pdfs. From the perspective of GIGO I am first evaluatio
n how well I can retrieve information related to certain questions. However, I am not certain about my approach.

I am u
sing precision at k, recall at k and ndcg at k as my evaluation metrics; next I simply create various pipelines starting
 from the raw pdfs, to embedding to retrieval. Here I vary the following element in the pipeline:

**Chunking:**

* Char
acterTextSplitter vs RecursiveTextSplitter
* Chuck size (400, 800, 1200)
* Chuck overlap (200, 400, 600)

**Embedding:**


* Model (ie. OpenAI vs Cohore)

**Retrieval:**

* Search method: mmr vs similarity
* Number of Documents to return \[k
\] (4, 7)
* Number of Documents to fetch to pass to MMR algorithm \[fetch-k\] (20, 40)

Retrieval is tested as follows; 
at the chunking stage I sample \~10% of the chucks and pass that to an LLM to generate questions. These are then used to
 test how well the pipeline can retrieve the chucks related to the questions.

**Now my problems:**

1. I consider a sin
gle pdf, one document. This document is then chucked, but the document ID is the same for each chuck. Meaning that if a 
question related to chuck A returns chuck Z; this would be counted as correct. While this would obviously not be correct
; I've considered changing the relation from a single page in a pdf being considered one document as this is likely more
 accurate.
2. The evaluation questions generated vary with the chuck size and method; as the given input to the LLM will
 be different. So while testing the pipeline, this is strongly affected by the quality of questions the LLM came up with
.

Are there people here with experience in testing, or does anyone know any good resources?

Thanks!
```
---

     
 
all -  [ Langchain openai FINE TUNING ](https://www.reddit.com/r/LangChain/comments/1co28ib/langchain_openai_fine_tuning/) , 2024-05-11-0910
```
I tried to do fine tuning in openai for limit the topics that my model can to speak, but the model runs bad, for example
 the result has seen like this:

GOOD: good answer 
BAD: bad answer

Q: Who is Taylor Swift? (GOOD)
A: Sorry….

Q: What 
is the sincope in life Sciences? (GOOD)
A: The sincope is…

Q: Hello (BAD)
A: sorry….

… I ask for 5 questions about Lif
e Science
Q: give me the answer of question Numbers 3 (BAD)
A: sorry….

How can I fix it ?

```
---

     
 
all -  [ Langchain allways return 429 error; este limit ](https://www.reddit.com/r/LangChain/comments/1co213w/langchain_allways_return_429_error_este_limit/) , 2024-05-11-0910
```
I have an llm built with langchain, OPENAI and qdrant; in production run well but in my local my app allways return 429 
error; I changed 5 times my tokens, I added 50$ more to my OPENAI account; but the issue persist.

Did anyone have this 
issue ?

```
---

     
 
all -  [ Looking for name of Mac App Switcher from this youtube video ](https://i.redd.it/yjt42vl79fzc1.png) , 2024-05-11-0910
```

```
---

     
 
all -  [ Limitations with existing prompt management tools?  ](https://www.reddit.com/r/LangChain/comments/1co09cc/limitations_with_existing_prompt_management_tools/) , 2024-05-11-0910
```
Hey y’all 🙌🏼 I’ve been using some prompt management tools (Humanloop and Braintrust Data) for a few of my recent project
s. Overall, they’re powerful tools but I’ve hit a few snags that make me wonder if a better tool can be built. 

I'm rea
lly interested in hearing about others' experiences with similar tools, so if you’re willing to share, that would be awe
some! 🫶🏼 

- What tool are you using? 
- How much does it cost you? 
- What kind of issues have you run into while using
 this tool?
- Are there specific features that you feel are lacking? 
- If you could build a wish list of features, what
 would they be? 🌟
```
---

     
 
all -  [ Rag response always includes reference to document  ](https://www.reddit.com/r/LangChain/comments/1cnxfnz/rag_response_always_includes_reference_to_document/) , 2024-05-11-0910
```
My org has this usecase to build a rag to answer questions. In rag works great given that I given it a lot of instructio
ns(prompts). One demand that rag isn't able to fullfill is to never mention document reference in the response.

Eg.
1) 
The document does not mention how to ...
2) you can view the steps on page 60 in the document.

Any prompt suggestions t
o overcome this particular scenario. The rag should never share the source of its response 

My pipeline

1) Pdf Documen
t Langchain 

2) Qdrant for retriever

3) Chat gpt3.5 turbo 16k for llm

```
---

     
 
all -  [ WooCommerce AI Chatbots / AI Agents ](https://www.reddit.com/r/wpsolr/comments/1cnve15/woocommerce_ai_chatbots_ai_agents/) , 2024-05-11-0910
```
We are looking to extend our [WooCommerce plugin](https://www.wpsolr.com/wpsolr-enterprise/) with AI ChatBots / AI Agent
s.  
Either something simple based on the [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview) a
nd [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling) .  
Or integration with full-
fledged solutions like [LangChain](https://www.langchain.com/), Vertex AI Agent builder, [Botpress](https://botpress.com
/), [FlowiseAI](https://flowiseai.com/).  
Contact me if you have any use cases in mind.
```
---

     
 
all -  [ Hi guys,what is the use of parameter K in ConversationEntityMemory? ](https://www.reddit.com/r/LangChain/comments/1cnu7zh/hi_guyswhat_is_the_use_of_parameter_k_in/) , 2024-05-11-0910
```
[https://api.python.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html](https://api.py
thon.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html)

https://preview.redd.it/ufmg
5yvirdzc1.png?width=488&format=png&auto=webp&s=ec24354784b8f84a445c4965f6064b9ed0cd838a


```
---

     
 
all -  [ Need help choosing LLM ops tool for prompt versioning ](https://www.reddit.com/r/llmops/comments/1cntvp0/need_help_choosing_llm_ops_tool_for_prompt/) , 2024-05-11-0910
```
We are a fairly big group with an already mature MLops stack, but LLMOps has been pretty hard.

In particular, prompt-it
eration hasn't been figured out by anyone.  
what's your go to tool for PromptOps ?

## PromptOps requirement:

Requirem
ents:

* Storing prompts and API to access them
* Versioning and visual diffs for results
* Evals to track improvement a
s prompts are develop .... or ability to define custom evals
* Good integration with complex langchain workflows
* Traci
ng batch evals on personal datasets, also batch evals to keep track of prompt drift
* Nice feature -> project -> run -> 
inference call heirarchy
* report generation for human evaluation of new vs old prompt results

## LLM Ops requirement -
> orchestration

* a clean way to define and visualize task vs pipeline
* think of a task as as chain or a self-containe
d operation (think summarize, search, a langchain tool)
* but then define the chaining using a low-code script -> which 
orchestrates these tools together
* that way it is easy to trace (the pipeline serves as a highl evel view) with easy pl
uggability.

Langchain is does some of the LLMOps stuff, but being able to use a cleaner abstraction on top of langchain
 would be nice.

None of the prompt ops tools have impressed so far. They all look like really thin visualization diff t
ools or thin abstractions on top of git for version control.

Most importantly, I DO NOT want to use their tooling to ru
n a low code LLM solution. They all seem to want to build some lang-flow like UI solution. This isn't ScratchLLM for god
's sake.

Also no, I refuse to change our entire architecture to be a startupName.completion() call. If you need to be s
o intrusive, then it is not a good LLMOps tools. Decorators & a listerner is the most I'll agree to.
```
---

     
 
all -  [ Having a hard time with templates  ](https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js) , 2024-05-11-0910
```
Hey everyone, I'm diving into LangChain and AI for the first time, so please bear with me as I navigate through this lea
rning curve. 

I've managed to create a small CLI bot with memory, and you can check out the GitHub link here: [GitHub L
ink] https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js. 

However, I'm encountering an issue where the bot 
interprets my name input as a command rather than part of the conversation. It seems to struggle with understanding the 
context of the conversation. I'd really appreciate some guidance on how to fix this. Thanks in advance for any help you 
can provide!
```
---

     
 
all -  [ Prompt Engineering on Phi3-mini-4K-instruct Model ](https://www.reddit.com/r/LangChain/comments/1cntf8t/prompt_engineering_on_phi3mini4kinstruct_model/) , 2024-05-11-0910
```
Hi,

I'm performing prompt engineering for my Phi3-mini-4K-instruct model and I'm using Anything LLM for my front end ap
plication.

The thing is i want my model to only answer query from the context data provided (PDFs) and Don't give any a
nswers from his own knowledge or external source. The prompt I'm giving is:

' ' 'You are an assistant for question answ
ering tasks. use the following pieces of retrieved context to answer the question. If the answer isn't present in the kn
owledge base, refrain from providing an answer based on your own knowledge. Instead of answer to such question, indicate
 that relevant information isn't available. Use three sentences maximum to keep the answer concise' ' '

After this prom
opt I'm still getting answers for the questions which are irrelevant and from outside of the knowledge base provided.
```
---

     
 
all -  [ React to typescript ](https://www.reddit.com/r/OpenAI/comments/1cnsnmq/react_to_typescript/) , 2024-05-11-0910
```
I have access to gpt 4 models in azure openai platform, can i convert react 18.2.0 code to typescript 4.9.5 using langch
ain and azure openai gpt 4 model.
 I know langchain is not necessary for conversion, but the data cut off for gpt 4 mode
l is 2021 and the latest version might not be used for train the gpt4 model. So do i have any option to use any langchai
n tool like chains or agent for this conversion as the model might need external agent support.
```
---

     
 
all -  [ Langchain agents - tools for intent classification  ](https://www.reddit.com/r/LangChain/comments/1cnqsxj/langchain_agents_tools_for_intent_classification/) , 2024-05-11-0910
```
Building an LLM app and using Unstructured for parsing data. From the vector store, have can I create a conversational a
gent that has 2 tools for intent classification? I want to create an agent so that according to user query in my applica
tion, the backend either returns a conversational output (chat) + shows sources or for some other type of user queries i
t returns only documents (no chat) akin to a generic Google search. After I create these two tools, I also want addition
al tools for the agent to recognize whether the user query is a simple greeting or whether there is any abusive language
 in the query. Any approaches, suggestions or examples would be helpful.

Thanks!
```
---

     
 
all -  [ 100 Free Courses with Certification on Udemy and Coursera ](https://www.reddit.com/r/Udemy/comments/1cnp62d/100_free_courses_with_certification_on_udemy_and/) , 2024-05-11-0910
```
Travel Writing: How to become a Travel Writer

[https://courze.org/travel-writing-how-to-become-a-travel-writer/](https:
//courze.org/travel-writing-how-to-become-a-travel-writer/)

&#x200B;

Microsoft Azure: Hands On Training: AZ-900 AZ-104
 and AZ-305

[https://courze.org/az-104-microsoft-azure-hands-on-labs/](https://courze.org/az-104-microsoft-azure-hands-
on-labs/)

&#x200B;

Docker MasterClass : Docker – Compose – SWARM – DevOps 2024

[https://courze.org/docker-masterclass
-docker-compose-swarm-devops-2024/](https://courze.org/docker-masterclass-docker-compose-swarm-devops-2024/)

&#x200B;


Python Complete Course For Python Beginners

[https://courze.org/python-complete-course-for-python-beginners/](https://c
ourze.org/python-complete-course-for-python-beginners/)

&#x200B;

Foundations of Web Development: CSS, Bootstrap, JS, R
eact

[https://courze.org/foundations-of-web-development-css-bootstrap-js-react/](https://courze.org/foundations-of-web-
development-css-bootstrap-js-react/)

&#x200B;

Business Process Simplification

[https://courze.org/business-process-si
mplification/](https://courze.org/business-process-simplification/)

&#x200B;

Root Cause Analysis: Certification

[http
s://courze.org/rca-root-cause-analysis/](https://courze.org/rca-root-cause-analysis/)

&#x200B;

Professional Diploma of
 Product Owner

[https://courze.org/professional-diploma-of-product-owner/](https://courze.org/professional-diploma-of-p
roduct-owner/)

&#x200B;

Agile Planning and OKRs: Transforming Your Project Outcomes

[https://courze.org/agile-plannin
g-and-okrs-transforming-your-project-outcomes/](https://courze.org/agile-planning-and-okrs-transforming-your-project-out
comes/)

&#x200B;

Agile Customer Research and Data-Driven Decision Making

[https://courze.org/data-driven-customer-res
earch-unlock-business-success/](https://courze.org/data-driven-customer-research-unlock-business-success/)

&#x200B;

Le
arn Maven from beginner to advanced

[https://courze.org/learn-maven-from-beginner-to-advanced/](https://courze.org/lear
n-maven-from-beginner-to-advanced/)

&#x200B;

Professional Diploma of Finance Business Partner

[https://courze.org/pro
fessional-diploma-of-finance-business-partner/](https://courze.org/professional-diploma-of-finance-business-partner/)

&
#x200B;

Professional Diploma of Marketing Manager Business Partner

[https://courze.org/professional-diploma-of-marketi
ng-manager-business-partner/](https://courze.org/professional-diploma-of-marketing-manager-business-partner/)

&#x200B;


Diploma of Microsoft Dynamics 365 CRM Business Architect

[https://courze.org/diploma-of-microsoft-dynamics-365-crm-bus
iness-architect/](https://courze.org/diploma-of-microsoft-dynamics-365-crm-business-architect/)

&#x200B;

Professional 
Diploma of Virtual Executive Assistant

[https://courze.org/professional-diploma-of-virtual-executive-assistant/](https:
//courze.org/professional-diploma-of-virtual-executive-assistant/)

&#x200B;

Professional Diploma in M&A Business Merge
rs & Acquisitions

[https://courze.org/professional-diploma-in-ma-business-mergers-acquisitions/](https://courze.org/pro
fessional-diploma-in-ma-business-mergers-acquisitions/)

&#x200B;

Microsoft Ads MasterClass – All Campaigns & Features


[https://courze.org/microsoft-ads-masterclass-2024-all-campaigns-features/](https://courze.org/microsoft-ads-masterclas
s-2024-all-campaigns-features/)

&#x200B;

Full Paid Ads Course – Google, Meta, Microsoft, LinkedIn

[https://courze.org
/full-paid-ads-course-google-facebook-microsoft-linkedin/](https://courze.org/full-paid-ads-course-google-facebook-micro
soft-linkedin/)

&#x200B;

Mastering LangChain and AWS: A Guide to Economic Analysis

[https://courze.org/mastering-lang
chain-and-aws-a-guide-to-economic-analysis/](https://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis
/)

&#x200B;

PyTorch Ultimate 2024: From Basics to Cutting-Edge

[https://courze.org/pytorch-ultimate-2024-from-basics-
to-cutting-edge/](https://courze.org/pytorch-ultimate-2024-from-basics-to-cutting-edge/)

&#x200B;

Google Ads Crash Cou
rse – Campaign Creations

[https://courze.org/google-ads-crash-course-campaign-creations/](https://courze.org/google-ads
-crash-course-campaign-creations/)

&#x200B;

A Crash Course in Writing Well

[https://courze.org/a-crash-course-in-writ
ing-well/](https://courze.org/a-crash-course-in-writing-well/)

&#x200B;

Applied Generative AI and Natural Language Pro
cessing

[https://courze.org/applied-generative-ai-and-natural-language-processing/](https://courze.org/applied-generati
ve-ai-and-natural-language-processing/)

&#x200B;

Professional Diploma in Procurement, Sourcing, Supply Chains

[https:
//courze.org/professional-diploma-in-procurement-sourcing-supply-chains/](https://courze.org/professional-diploma-in-pro
curement-sourcing-supply-chains/)

&#x200B;

Professional Diploma of Real Estate Business Expert

[https://courze.org/pr
ofessional-diploma-of-real-estate-business-expert/](https://courze.org/professional-diploma-of-real-estate-business-expe
rt/)

&#x200B;

Masters in Structural Engineering & Drawing Reading – Etabs

[https://courze.org/diploma-in-structural-d
rawing-reading-like-expert-etabs/](https://courze.org/diploma-in-structural-drawing-reading-like-expert-etabs/)

&#x200B
;

Information Security Fundamentals

[https://courze.org/information-security-fundamentals/](https://courze.org/informa
tion-security-fundamentals/)

&#x200B;

Ultimate Miro Guide: Enhance Team Productivity & Agility

[https://courze.org/ul
timate-miro-guide-enhance-team-productivity-agility/](https://courze.org/ultimate-miro-guide-enhance-team-productivity-a
gility/)

&#x200B;

Becoming an Agile Leader: Drive Outcomes and Bring Impact

[https://courze.org/becoming-an-agile-lea
der-drive-outcomes-and-bring-impact/](https://courze.org/becoming-an-agile-leader-drive-outcomes-and-bring-impact/)

&#x
200B;

Overcoming Obstacles & Building Resilience as a Team

[https://courze.org/overcoming-obstacles-building-resilienc
e-as-a-team/](https://courze.org/overcoming-obstacles-building-resilience-as-a-team/)

&#x200B;

Agile Ways of Working W
orkshop – Practical Guide

[https://courze.org/agile-ways-of-working-workshop-practical-guide/](https://courze.org/agile
-ways-of-working-workshop-practical-guide/)

&#x200B;

Agile Transformation A to Z | How To Make Any Company Agile

[htt
ps://courze.org/agile-transformation-a-to-z-how-to-make-any-company-agile/](https://courze.org/agile-transformation-a-to
-z-how-to-make-any-company-agile/)

&#x200B;

Body Language / Non-Verbal Communication for Business

[https://courze.org
/body-language-non-verbal-communication-for-business/](https://courze.org/body-language-non-verbal-communication-for-bus
iness/)

&#x200B;

Sales: Your First 90 Days as a New Sales Representative

[https://courze.org/sales-your-first-90-days
-as-a-new-sales-representative/](https://courze.org/sales-your-first-90-days-as-a-new-sales-representative/)

&#x200B;


Defining Project Scope and Managing Resources for Project

[https://courze.org/defining-project-scope-and-managing-resou
rces-for-project/](https://courze.org/defining-project-scope-and-managing-resources-for-project/)

&#x200B;

Crea pagina
s de ventas para vender productos digi en Hotmart

[https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi
-en-hotmart/](https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi-en-hotmart/)

&#x200B;

Wealth Manage
ment, Private Banking & Compliance Introduction

[https://courze.org/wealth-management-private-banking-compliance-introd
uction/](https://courze.org/wealth-management-private-banking-compliance-introduction/)

&#x200B;

Professional Diploma 
in Digital Business Development

[https://courze.org/professional-diploma-in-digital-business-development/](https://cour
ze.org/professional-diploma-in-digital-business-development/)

&#x200B;

&#x200B;
```
---

     
 
all -  [ Token Limits, Consistency, & LLM in Code ](https://www.reddit.com/r/ChatGPTPro/comments/1cnhxqt/token_limits_consistency_llm_in_code/) , 2024-05-11-0910
```
**If you don’t want to read:**

* How do I address token limits without reducing tokens? Also, can someone explain top p
?
* How to improve custom GPT consistency and quantitatively measure it? I heard about temperature but what else?
* Wher
e to start for implementing LLM in code? 

**Context**

TOKEN LIMITS - I need to input over hundreds of thousands or eve
n millions of tokens in a single run (via excel/csv file). Maximum split it up into like 5-10 runs. Despite higher token
 limits, it gets lazy, gives errors, etc. 

CONSISTENCY - Custom GPT outputs are inconsistent and I need more consistenc
y. I heard about temperature and gave GPT an examples set but its still fairly inconsistent and I want to know how to me
asure this more rigorously.

LLM in PYTHON - I have experience with Python but not LLM in python. Should I start with La
ngChain and what resources should I follow? I want to experiment with this although my main concern later on is my team 
doesn’t code so I don’t know how sustainable a 'code built model' would be in the long term.

...... 

THANK YOU!
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1cnhul6/list_of_free_and_best_selling_discounted_courses/) , 2024-05-11-0910
```
## Udemy Free Courses for 09 May 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* Crea sistemas Ecommerce con PHP y MySQL V2.0[REDEEM OFFER](https://idownloadcoupon.com/udemy/4790/)

* Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/4789/)
* Cu
rso de Wix 2024: Cómo Crear una Página Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/4788/)
* Wealth Ma
nagement, Private Banking & Compliance Introduction[REDEEM OFFER](https://idownloadcoupon.com/udemy/4787/)
* Information
 Security Fundamentals[REDEEM OFFER](https://idownloadcoupon.com/udemy/4786/)
* Professional Diploma of Product & Servic
e Business Analyst[REDEEM OFFER](https://idownloadcoupon.com/udemy/4785/)
* Arduino Practice Test: Get Certified and Tes
t Your Skills[REDEEM OFFER](https://idownloadcoupon.com/udemy/4784/)
* Automatic Irrigation System with Arduino[REDEEM O
FFER](https://idownloadcoupon.com/udemy/4783/)
* Sales: Your First 90 Days as a New Sales Representative[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/4782/)
* The Art of Building and Sustaining Meaningful Relationships[REDEEM OFFER](http
s://idownloadcoupon.com/udemy/4781/)
* Skills Economy: Transforming to a Skills-based Organization[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/4780/)
* Body Language / Non-Verbal Communication for Business[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4779/)
* Agile Ways of Working Workshop – Practical Guide[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/4777/)
* Immigrants Guide to a Successful Career in Corporate America[REDEEM OFFER](https://idownloadcoupon.com/udem
y/4776/)
* Professional Diploma of Real Estate Business Expert[REDEEM OFFER](https://idownloadcoupon.com/udemy/4775/)
* 
Masters in Structural Engineering & Drawing Reading – Etabs[REDEEM OFFER](https://idownloadcoupon.com/udemy/4774/)
* Bec
oming an Agile Leader: Drive Outcomes and Bring Impact[REDEEM OFFER](https://idownloadcoupon.com/udemy/4773/)
* Agile Tr
ansformation A to Z | How To Make Any Company Agile[REDEEM OFFER](https://idownloadcoupon.com/udemy/4772/)
* Ultimate Mi
ro Guide: Enhance Team Productivity & Agility[REDEEM OFFER](https://idownloadcoupon.com/udemy/4771/)
* Professional Dipl
oma in Procurement, Sourcing, Supply Chains[REDEEM OFFER](https://idownloadcoupon.com/udemy/4770/)
* Google Search Maste
ry Course : Find Answers 10X Times Faster[REDEEM OFFER](https://idownloadcoupon.com/udemy/4769/)
* Mastering LangChain a
nd AWS: A Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/4768/)
* Full Paid Ads Course – Goo
gle, Meta, Microsoft, LinkedIn[REDEEM OFFER](https://idownloadcoupon.com/udemy/4767/)
* Microsoft Ads MasterClass – All 
Campaigns & Features[REDEEM OFFER](https://idownloadcoupon.com/udemy/4766/)
* Google Ads Crash Course – Campaign Creatio
ns[REDEEM OFFER](https://idownloadcoupon.com/udemy/4765/)
* Professional Diploma of Virtual Executive Assistant[REDEEM O
FFER](https://idownloadcoupon.com/udemy/4764/)
* Professional Diploma in M&A Business Mergers & Acquisitions[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/4763/)
* Applied Generative AI and Natural Language Processing[REDEEM OFFER](https:
//idownloadcoupon.com/udemy/4762/)
* A Crash Course in Writing Well[REDEEM OFFER](https://idownloadcoupon.com/udemy/4761
/)
* Ethical Hacking: Windows Exploitation Basics[REDEEM OFFER](https://idownloadcoupon.com/udemy/4760/)
* Ethical Hacki
ng: Reverse Shells[REDEEM OFFER](https://idownloadcoupon.com/udemy/4759/)
* Linux Terminal for beginners[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/4758/)
```
---

     
 
all -  [ Using Airtable data as a vector database for Chatbot Knowledge Base ](https://www.reddit.com/r/LangChain/comments/1cnhb5a/using_airtable_data_as_a_vector_database_for/) , 2024-05-11-0910
```
Hello AI peeps, I need some help/advice. I’m building a fairly comprehensive chatbot which includes a RAG QnA component.
 All knowledge base data is in an Airtable, where each row/record is another piece of knowledge. 

The plan is to vector
ize the knowledge base to Pinecone via Flowise Upsert and then retrieve with OpenAI Embeddings. 

The main issue is that
 I can’t figure out how to use the columns as seperate metadata keys instead of all being vectorized in 1 piece. Is ther
e an easy solution to accomplish this? Is there a better approach overall to convert the data from Airtable into a RAG k
nowledge base? Any help would be appreciated! I mentioned Flowise because it’s the simplest way to use Langchain.
```
---

     
 
all -  [ Mastering LangChain and AWS: A Guide to Economic Analysis ](https://www.reddit.com/r/udemyfreebies/comments/1cnh8wm/mastering_langchain_and_aws_a_guide_to_economic/) , 2024-05-11-0910
```
Mastering LangChain and AWS: A Guide to Economic Analysis

https://idownloadcoupon.com/udemy/4768/
```
---

     
 
all -  [ create a 'default' or 'else' tool for ReAct agent ](https://www.reddit.com/r/LangChain/comments/1cngb56/create_a_default_or_else_tool_for_react_agent/) , 2024-05-11-0910
```
I am working on a ReAct agent that will have a couple of pre-defined tools to perform specific actions BUT we need to ha
ve some kind of 'default' or 'else' tool, what I mean is: if non of the pre-defined tools is selected by the agent then 
it will try to answer the user query using the 'else' tool, the idea is that there are some pre-defined and well known a
ctions that will be executed by the agent when tue user query matches those fine, but if there is not  a good match we s
till want the agent to be able to come up with the best answer possible(inbstead of something like: I cannot answer this
 question because I don't have a tool for it). Any ideas? I'm thinking on something as a   
`GeneralHandlerTool(BaseTool
):`  
`def _run():`  
   `....`
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-11-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-11-0910
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-11-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
