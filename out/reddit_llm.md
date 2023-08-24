 
all -  [ LangChain makes it easy to use GPT for software generation ](/r/LangChain/comments/15yi3wi/langchain_makes_it_easy_to_use_gpt_for_software/) , 2023-08-24-0909
```

```
---

     
 
all -  [ I created a chat gpt autoblogger for wordpress ](https://www.reddit.com/r/Wordpress/comments/15zeee3/i_created_a_chat_gpt_autoblogger_for_wordpress/) , 2023-08-24-0909
```
I created a chat gpt autoblogger for Wordpress.

After searching the internet for an python or javascript autoblogger fo
r wordpress that will generate articles with one command, all i could come up with was some tools that could generate 60
0-800 word markdown-formatted articles because they were trying to do it in one go.

Instead i thought it might be benef
icial to create an outline using chatgpt with 10-15 headings and populate each section individually so the articles can 
be 2000 to 3000 words which is far better for SEO.

This app will automatically post 2000+ word articles based on a list
 of keywords you provide it. The app will use the top 10 organic search results so the content is based on real data.

U
sing langchain and chat gpt this can be your ultimate autoblogger you can tweak to your liking - generating articles for
 as little as 15 cents a pop.

You can check it out here: [https://github.com/jakeadelman/autoblogger-wordpress](https:/
/github.com/jakeadelman/autoblogger-wordpress)
```
---

     
 
all -  [ Develop a quiz tool that generates new questions using the existing questions from a question bank. ](https://www.reddit.com/r/LangChain/comments/15zdcfn/develop_a_quiz_tool_that_generates_new_questions/) , 2023-08-24-0909
```
Hi All,

I am new to LangChain and would like to create a tool that generates AI questions from a course question bank d
atabase. Can you guide me on how to begin and provide steps to accomplish this?

Thank you! 

\- Fellow Learner. 
```
---

     
 
all -  [ Langchain install misbehaving ](https://www.reddit.com/r/LangChain/comments/15zah4u/langchain_install_misbehaving/) , 2023-08-24-0909
```
Title. I’ve been having issues installing the library for the last few days. My last issue was that I installed ‘pip ins
tall langchain[all]’ on a new conda, created the env and installed langchain directly. If I try to run any file that has
 langchain it says that the module does not exist, but If I, from the folder that I was in when I pip installed it, impo
rt it through the terminal it works.
Anyone faced this issue? Anyone got any guidance?
```
---

     
 
all -  [ Is it possible that less complicated architecture works better? ](https://www.reddit.com/r/LangChain/comments/15z856n/is_it_possible_that_less_complicated_architecture/) , 2023-08-24-0909
```
Hi guys.. I’ve been having a debate recently with a colleague in our startup.

Disclaimer.. I have been ranting to ChatG
PT about it and I asked it to do a summary after whisper transcription. Sorry if that bothers anybody.

Sooo..

I’ve tri
ed two different methods of retrieval augmented generation:

1.	Primitive  Method:

This was built on one of the very fi
rst releases of Langchain. It’s pretty straightforward and employs the standard character splitter it uses the architect
ure of the question answering chain that’s still in place today. It’s relatively out-of-the-box and requires significant
 manual intervention, especially to generate a document that the chain can interact efficiently with.

2.	Improved Metho
d:

I scrape content from a website and then use NLTK token counters to split the scraped text.
I construct the document
s based on the chunked content and the original webpage source, and throw in some nice metadata to help with the retrivi
al. Additionally, I Integrated contextual compression that’s been fine-tuned in its parameters based on the number of to
kens retrieved for each query, aiming to find the optimal range for our document base.
Finally I introduced a non linear
 classifier to select whether an incoming question is relevant or non relevant. A significant drawback is that the relev
ancy classifier depends on the rephrased question. Since rephrasing can be unpredictable, it’s challenging to train a ro
bust model around this.

The first method is simple and consistent, but the second tries to offer a more expansive persp
ective. My colleague points out time and again that the first method gives more reliable results. But I think that: firs
t that is not true, and second even if it was true it is because the document base is much smaller. 

I see potential in
 the second one, especially as it attempts to address challenges that can’t be managed with just prompt engineering.

Wo
uld love to hear your thoughts. Is the simplicity of the first method more viable in a production environment, or is the
 second’s ambition worth the complexities? Am I overthinking this?

EDIT

I can see the question coming so:

The context
ual retriever allows for the maximum amount of documents to be retrieved (20) and then proceeds to limit the redundancy 
and similarity parameter of the compressor so that on average it doesn’t retrieve more than 3000 tokens. The token numbe
r is also controlled by the maximum amount of tokens that the retriever can fetch.
```
---

     
 
all -  [ Any GitHub using python that are able to accurately summarise very long text (e.g.40 pages) using lo ](https://www.reddit.com/r/LocalLLaMA/comments/15z3bi0/any_github_using_python_that_are_able_to/) , 2023-08-24-0909
```
Is langchain the only way?
```
---

     
 
all -  [ How to use tools in chains ](https://www.reddit.com/r/LangChain/comments/15z1iqw/how_to_use_tools_in_chains/) , 2023-08-24-0909
```
Hi!

I have a SequentialChain and a bunch of PromptTemplates in it. Now I like to use Tools (e.g. 'serpapi', 'llm-math')
 in the two of my PromptTemplates. How do I have to do this? I could not find the boilerplate code so far. Maybe I go in
 the false direction with chains. Would be nice to get a bump in the right direction. THX
```
---

     
 
all -  [ LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/dataengineering/comments/15z0ogw/llm_apps_are_mostly_data_pipelines/) , 2023-08-24-0909
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
all -  [ examor: For students, scholars, interviewees and lifelong learners ](https://www.reddit.com/r/LangChain/comments/15yyj99/examor_for_students_scholars_interviewees_and/) , 2023-08-24-0909
```
examor is a website application that allows you to take exams based on your knowledge notes. Let you really remember wha
t you have learned and written.

[screen shot](https://preview.redd.it/6sydhkanutjb1.png?width=1735&format=png&auto=webp
&s=f180c82b1e96e9bc5a0f57dcd744d72abc4bf757)

When I’m learning a new technology, I have the habit of taking notes and j
otting down important information. It’s a good habit, but I also have a bad habit of not enjoying reading the notes I’ve
 written (I’m not sure if this is the case for most people 🫣). This results in my notes becoming mere mementos without s
ubstantial use. That’s why I choose to create an application that continuously prompts you with questions to review your
 note contents. 

 You can enter to [examor repo](https://github.com/codeacme17/examor) see more. If you are interested 
in this project, you can point it to a star. 
```
---

     
 
all -  [ I have two databases, Langchain can read one but not the other ](https://www.reddit.com/r/LangChain/comments/15yy6xp/i_have_two_databases_langchain_can_read_one_but/) , 2023-08-24-0909
```
Hello everyone,

I've been using Langchain's SQLDatabaseToolkit on postgres. I'm able to get LG to read one database but
 can't seem to get it to do so against another. One has 8 tables (it reads this one fine), the other has 68 tables (does
n't read). It will say something like 'employee table not found' when I know for a fact that it exists since I created i
t.  I know my connections are working fine since on Db works and I tested both Db on a separate notebook. Has anyone com
e across a similar issue?
```
---

     
 
all -  [ How we are creating a customized AI platform for chatbots? ](https://www.reddit.com/r/SaaS/comments/15yxz2a/how_we_are_creating_a_customized_ai_platform_for/) , 2023-08-24-0909
```
where you can create an AI chatbot for your websites, documents, videos, and audio.  
  
Technology.  
Development. 
 
Distribution.  
  
Let's discuss everything 🧵 👇  
  
  
  
Technology: 🤖  
  
\- Langchain 🌐: For embeddings a
nd reading documents.  
\- Pinecone 🌲: For vector storage.  
\- Whisper Model 🎙️: Transcription of audio and videos. 
 
\- MySQL 🗃️: Database  
\- NEXT JS ⚡: Front-End Development  
\- Node JS 🛠️: Backend  
\- Express 🚄: APIs  
  
 
 
Development: 🛠️  
  
\-Converting every data source into a text file using different models and services like whispe
r and langchain etc.  
  
Using Open AI models Chatgpt 3.5 & 4 for embedding and saving them in Pinecone.  
  
Using
 langchain chains for question answering.  
Node express to build APIs and data storage in MySQL.  
  
  
Distributi
on: 💰  
  
\#buildinpublic campaign.  
\- Product hunt and hacker news engagements.  
\- Building content as you cod
e from day one.  
\- Schedule launch on PH and start reaching out on Linkedin & X.  
\- Launch on hacker news.  
\- D
iscussions on indie hackers.  
\- Launch on Beta pages.  
\- LTD’s for a very short time to gain some loyal lifetime u
sers and good revenue to push your start.  
  
Planning all this for launch within 15 days.  
  
\#buildinpublic #st
artups #AI
```
---

     
 
all -  [ Bespoke document loaders for specific type of documents ](https://www.reddit.com/r/OpenAI/comments/15yw4pf/bespoke_document_loaders_for_specific_type_of/) , 2023-08-24-0909
```
Hey all, Ive been using langchain to query RFP documents. Primarily they are in pdf format so I am using a standard load
er like PyPDFLoader and for the most part, its working fine. What I wanted to know was, whether there are loaders which 
are more suited for custom use cases like mine? According to langchain docs, there are a plethora of loaders but I cant 
quite figure out a decent one. This one called Grobid looks good, can anyone tell me whether that will be suited to my t
ask or any other loader for my use case? Thanks.
```
---

     
 
all -  [ Integrate SQL capability within pandas agent ](https://www.reddit.com/r/LangChain/comments/15yvc1z/integrate_sql_capability_within_pandas_agent/) , 2023-08-24-0909
```
I'm using pandas agent in langchain. But I want to scale my system for input file containing more than 1 million rows. F
or this, I wish to use SQL instead of writing the operations using pandas dataframe since SQL will directly work on sche
ma and prevent loading entire data in memory.
How can I achieve this where basically I want to develop a system which at
 times uses pandas agent to generate code for dataframes and alternatively generates code in SQL, if possible? 
I tried 
modifying the input prompt for pandas agent, I could see the SQL code generated in its ACTION Input part but it didn't h
ave the tool to execute it..so it shifted to pandas to perform the same operations.
Please help as I'm very new to langc
hain.
```
---

     
 
all -  [ I created a chat gpt autoblogger for Wordpress ](https://www.reddit.com/r/ChatGPTCoding/comments/15yuc2f/i_created_a_chat_gpt_autoblogger_for_wordpress/) , 2023-08-24-0909
```
I created a chat gpt autoblogger for Wordpress. 

After searching the internet for an python or javascript autoblogger f
or wordpress that will generate articles with one command, all i could come up with was some tools that could generate 6
00-800 word markdown-formatted articles because they were trying to do it in one go.

Instead i thought it might be bene
ficial to create an outline using chatgpt with 10-15 headings and populate each section individually so the articles can
 be 2000 to 3000 words which is far better for SEO.

This app will automatically post 2000+ word articles based on a lis
t of keywords you provide it. The app will use the top 10 organic search results so the content is based on real data. 


Using langchain and chat gpt this can be your ultimate autoblogger you can tweak to your liking - generating articles f
or as little as 15 cents a pop.

You can check it out here: [https://github.com/jakeadelman/autoblogger-wordpress](https
://github.com/jakeadelman/autoblogger-wordpress)
```
---

     
 
all -  [ I created a chat gpt autoblogger for wordpress ](https://www.reddit.com/r/ChatGPT/comments/15yu7qq/i_created_a_chat_gpt_autoblogger_for_wordpress/) , 2023-08-24-0909
```
I created a chat gpt autoblogger for wordpress. 

The app will automatically post 2000+ word articles based on a list of
 keywords you provide it. Using langchain and chat gpt this can be your ultimate autoblogger you can tweak to your likin
g - generating articles for as little as 15 cents.

You can check it out here: [https://github.com/jakeadelman/autoblogg
er-wordpress](https://github.com/jakeadelman/autoblogger-wordpress)
```
---

     
 
all -  [ talkToFile: A CLI tool to seamlessly query any file using langchainjs ](https://www.reddit.com/r/LangChain/comments/15yjgyo/talktofile_a_cli_tool_to_seamlessly_query_any/) , 2023-08-24-0909
```
I'm excited to share a project I've been working on: **talkToFile**. It's a CLI tool built on the langchainlibrary, allo
wing you to load and intelligently query content from various files.

Some highlights:

* Modular and Flexible: Integrat
es effortlessly across platforms.
* Efficient Data Transformation: Converts unstructured data into structured outputs.
*
 Explore the Unstructured API and the Chipper Model.

I'd love to get feedback, contributions, or any thoughts on improv
ing it further.[https://github.com/amalshehu/langchain-js-realworld/blob/master/unstructured.io/talkToFile.js](https://g
ithub.com/amalshehu/langchain-js-realworld/blob/master/unstructured.io/talkToFile.js)
```
---

     
 
all -  [ LangChain makes it easy to use GPT for software generation ](https://www.reddit.com/r/LangChain/comments/15yi3wi/langchain_makes_it_easy_to_use_gpt_for_software/) , 2023-08-24-0909
```
Here is how: [https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Syn
thesizer)

Demo: [https://www.youtube.com/watch?v=zFJDQOtIFGA&t=337s](https://www.youtube.com/watch?v=zFJDQOtIFGA&t=337s
) 

&#x200B;
```
---

     
 
all -  [ What is the difference between Instructor XL and OpenAI embeddings? ](https://www.reddit.com/r/LangChain/comments/15ydvj4/what_is_the_difference_between_instructor_xl_and/) , 2023-08-24-0909
```
Are there any good articles or videos that shows the difference of these embedding models?
```
---

     
 
all -  [ Adding a prompt ](https://www.reddit.com/r/LangChain/comments/15ydgfx/adding_a_prompt/) , 2023-08-24-0909
```
    def initialize_chain():
        OPENAI_API_KEY = getpass()
        os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
   
     PERSIST = False
        query = None
    
        if PERSIST and os.path.exists('persist'):
            print('Reus
ing index...\n')
            vectorstore = Chroma(persist_directory='persist', embedding_function=OpenAIEmbeddings())
  
          index = VectorStoreIndexWrapper(vectorstore=vectorstore)
        else:
            loader = TextLoader('data.t
xt')
            if PERSIST:
                index = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory':'pe
rsist'}).from_loaders([loader])
            else:
                index = VectorstoreIndexCreator().from_loaders([loader
])
    
        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model='gpt-3.5-turbo'),
      
      retriever=index.vectorstore.as_retriever(search_kwargs={'k': 1}),
        )
        return chain
    
    global_c
hat_history = []
    chain = initialize_chain()
    
    @app.route('/get', methods=['POST'])
    def get_bot_response()
:
        user_msg = request.form.get('msg') # get user message from front-end
    
        result = chain({'question': 
user_msg, 'chat_history': global_chat_history})
        chatbot_answer = result['answer']
        global_chat_history.ap
pend((user_msg, chatbot_answer))
        return jsonify(answer=chatbot_answer)

I have this flask server set up to get i
nput from a front-end and process it to a back-end and return the AI's response. How do I add a prompt to something like
 this, to instruct the AI on what it is and what it should do?
```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/ChatGPT/comments/15yaym0/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```

No stock images/ videos, no gifs, and no flashy texts. Only pure technical deep dive.

Here is the quickest but in-dept
h explainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bHc
JVI

Using Langchain is  one of the quickest way to create and test an advanced LLM based AI application. Check it out!
```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/ChatGPTCoding/comments/15yavgh/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```


No stock images/ videos, no gifs, and no flashy texts. Only pure technical deep dive.

Here is the quickest but in-dep
th explainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bH
cJVI

Using Langchain is  one of the quickest way to create and test an advanced LLM based app such as with GPT. Check i
t out!
```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/LangChain/comments/15yatsj/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```

No stock images/ videos, no gifs, and no flashy texts. Only pure technical deep dive.

Here is the quickest but in-dept
h explainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bHc
JVI
```
---

     
 
all -  [ Any open source langchain project that be fine-tuned by website urls? ](https://www.reddit.com/r/OpenAI/comments/15y7ix9/any_open_source_langchain_project_that_be/) , 2023-08-24-0909
```
i'm trying to build a chatbot that learns from multiple websites' content, e.g. picking up knowledge about health from p
opular health websites. does anyone have any recommendation of an existing open source or commercial app that does this?


&#x200B;
```
---

     
 
all -  [ Text-Splitting PDF's Meaningfully ](https://www.reddit.com/r/LangChain/comments/15xw7hp/textsplitting_pdfs_meaningfully/) , 2023-08-24-0909
```
It appears that when working with PDF documents, there's a consistent issue with splitting at page breaks taking precede
nce over separators, especially when the chunk size exceeds the page length. I've attempted to extract the content by ap
pending each page into a string, but this prevents access to the `langchain.schema.Document` class, hindering the abilit
y to work with metadata and functions like self-query retrieval, compression, and Maximum Marginal Relevance.

I've cons
idered alternatives like TF-IDF or SVM, but I'm uncertain if they would be suitable at a production level since they are
 not built on a vector. Any advice or workarounds would be greatly appreciated. 
```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/singularity/comments/15xurcf/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```
No stock images/ videos, no gifs, and no flashy texts. Only pure technical deep dive.

Here is the quickest but in-depth
 explainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bHcJ
VI

Using Langchain is  one of the quickest way to create and test an advanced LLM based AI application. Check it out!
```
---

     
 
all -  [ LLM and Dataset format for Product Configuration ](https://www.reddit.com/r/LangChain/comments/15xpfcy/llm_and_dataset_format_for_product_configuration/) , 2023-08-24-0909
```
 Hi,

I am looking for an LLM and dataset format combination suggestion for my use case.

1. We have a dataset consistin
g of input product descriptions and required (converted) product descriptions as per the company SKU hierarchy. Original
ly, it was created based on a rule-based engine which is retiring now.
2. What can be the best approach to start playing
? promoting vs fine-tuning
3. If fine-tuning, then which open source model (or PaLM 2 is possible as we are GCP heavy) t
o start with and which data format to use? OpenOrca vs alpaca format
```
---

     
 
all -  [ Question about building a chatbot using internal company documentation ](https://www.reddit.com/r/ArtificialInteligence/comments/15xnq1h/question_about_building_a_chatbot_using_internal/) , 2023-08-24-0909
```
Hi there. I'm a non-developer (Product person) trying to build a basic mental model for how we might build a chatbot tha
t would allow our internal support team to interact with our propietary knowledgebase. Our KB currently resides in Notio
n.

I've been reading up on and watching videos about the LangChain framework, the differences between In-Context Learni
ng and Fine Tuning, Vector databases/embeddings etc. So I've got a rough handle on the overall architecture.

Where I'm 
a little stumped right now is how to think about the process of actually getting our KB content from Notion into a Vecto
r DB. More specifically, I'm interested in understanding (at a high, abstract level) how to think about keeping that kno
wledge up to date. For example, as the support team updates KB articles, having some mechanism in place for updating the
 Vector DB automatically so that it's always pulling from the latest information automatically. I believe I've seen Chat
bot apps out there that let you plug in a URL to scrape data from and then have it update every \~24 hours or so.

Can a
nyone share with me the big building blocks involved with implementing something like this? Is there typically some sort
 of cron job that's scraping the KB at regular intervals and then moving that data into the Vector DB?

Thanks in advanc
e.
```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/ChatGPTPro/comments/15xjvdi/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```


No stock images/ videos, no gifs, and no flashy texts. Only pure technical deep dive.

Here is the quickest but in-dep
th explainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bH
cJVI

Using Langchain is  one of the quickest way to create and test an advanced LLM based AI application. Check it out!

```
---

     
 
all -  [ Langchain: Explained in 2 minutes ](https://www.reddit.com/r/GPT3/comments/15xj90d/langchain_explained_in_2_minutes/) , 2023-08-24-0909
```
No stock images/ videos, no gifs, and flashy texts. Only pure technical deep dive.

Here is the quickest but in-depth ex
plainer video about Langchain, a framework gaining popularity day by day. 

https://www.youtube.com/watch?v=C9bE8bHcJVI


Using Langchain is  one of the quickest way to create and test an advanced LLM based AI application. Check it out!
```
---

     
 
all -  [ AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework - Microsoft 2023  ](https://www.reddit.com/r/singularity/comments/15xh3xp/autogen_enabling_nextgen_llm_applications_via/) , 2023-08-24-0909
```
Paper: [https://arxiv.org/abs/2308.08155](https://arxiv.org/abs/2308.08155) 

Github: [https://microsoft.github.io/FLAML
/docs/Use-Cases/Autogen/](https://microsoft.github.io/FLAML/docs/Use-Cases/Autogen/) 

Abstract:

>This technical report
 presents AutoGen, a new framework that enables development of LLM applications using multiple agents that can converse 
with each other to solve tasks. AutoGen agents are customizable, conversable, and seamlessly allow human participation. 
They can operate in various modes that employ combinations of LLMs, human inputs, and tools. AutoGen's design offers mul
tiple advantages: a) it gracefully navigates the strong but imperfect generation and reasoning abilities of these LLMs; 
b) it leverages human understanding and intelligence, while providing valuable automation through conversations between 
agents; c) it simplifies and unifies the implementation of complex LLM workflows as automated agent chats. We provide ma
ny diverse examples of how developers can easily use AutoGen to effectively solve tasks or build applications, ranging f
rom coding, mathematics, operations research, entertainment, online decision-making, question answering, etc.      

htt
ps://preview.redd.it/xbkfaqe7jijb1.jpg?width=1377&format=pjpg&auto=webp&s=e86ea1dba6c79e4b74ef19b2effc265c690f6cae

http
s://preview.redd.it/78i6sre7jijb1.jpg?width=1520&format=pjpg&auto=webp&s=85d8ff4632dc4c6d3d380e7a4c559d57148bc5cd

https
://preview.redd.it/9bka0qe7jijb1.jpg?width=974&format=pjpg&auto=webp&s=593b3bed04997f347d522a3e096f968663af2089

https:/
/preview.redd.it/18e24we7jijb1.jpg?width=1136&format=pjpg&auto=webp&s=a34b44003f7b3be599e0e8de9b4195216bcf19f4

&#x200B;

```
---

     
 
all -  [ Advise needed using chat history. ](https://www.reddit.com/r/LangChain/comments/15xg5na/advise_needed_using_chat_history/) , 2023-08-24-0909
```
Can anyone advise how I can use chat history with the sqltoolkit agent? I have the memory setup and can see that the cha
t request are being written along with the output response.
However, the agent is not contextually aware of the previous
 chat history.
```
---

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-08-24-0909
```
We've created an open source chat bot builder, on top of PostgresML. This tool makes it easy to ingest documents and set
 a system prompt for a chatbot with knowledge of your content. The innovation is in the simplicity and efficiency, rathe
r than the functionality.

PostgresML runs open source embedding models alongside pgvector in Postgres to implement chat
 bot prompt creation without any network calls, which makes it \~4x faster than competing architectures. It can also do 
text generation with that prompt (and no additional network hops) using any open source model from HuggingFace, but it a
lso integrates with the GPT-4 API if you'd like to use that instead. 

The full writeup including some benchmarks for co
mpeting architectures is here:  [https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-kno
wledge-based-chatbots-part-I](https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-knowle
dge-based-chatbots-part-I)

You can chat with a deployment that has access to our blogs and documentation content it in 
\[our Discord\]([https://discord.com/channels/1013868243036930099/1013868243536072868](https://discord.com/channels/1013
868243036930099/1013868243536072868)), where it answers questions addressed to @PgBot.

&#x200B;

* The source code for 
the bot builder and server is only a few hundred lines of Python [https://github.com/postgresml/postgresml/tree/master/p
gml-apps/pgml-chat#readme](https://github.com/postgresml/postgresml/tree/master/pgml-apps/pgml-chat#readme)
* The chat a
pp is so small, because it's delegates all the vector db and embedding generation options to our Python client SDK, whic
h is available for anyone to build other apps with: [https://pypi.org/project/pgml/](https://pypi.org/project/pgml/)
* T
he Python client SDK is so small, because it's just a wrapper around the Rust client SDK: [https://github.com/postgresml
/postgresml/tree/master/pgml-sdks/rust/pgml](https://github.com/postgresml/postgresml/tree/master/pgml-sdks/rust/pgml). 
Currently we also support JS/Typescript SDKs as well, all generated from the same safe and efficient underlying Rust imp
lementation, using some fancy Rust macros.
* The Rust client SDK is also pretty simple though, because it just delegates
 everything to the Postgres database extension, which is where everything is computed in a single GPU accelerated proces
s, without having to load any ML models, data, or dependencies on client apps, effectively eliminating all the typical M
L data<->model network hops. Which makes it faster, simpler and safer.

This lays out what we think a is a better approa
ch to AI application architecture compared to libraries like LangChain or LlamaIndex, that focus on glueing together dis
parate data stores, algorithms, models over the network.  

```
---

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-08-24-0909
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.

Checkout the entire blog post at [https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f](https://thevatsalsaglani.med
ium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f)
```
---

     
 
MachineLearning -  [ [D] How we evaluated LLMs in prod ](https://www.reddit.com/r/MachineLearning/comments/15ogknd/d_how_we_evaluated_llms_in_prod/) , 2023-08-24-0909
```
This is going to be a post about the challenges I faced while working with ChatGPT in my previous company and the things
 we did to overcome them over a 2+ month struggle. Check us out at [www.twilix.io](https://www.twilix.io/) if anything b
elow resonates with you and I hope you find some of it helpful.

So to begin, in my previous company we invested a few m
onths building a chatbot to help with user onboarding. At first everything was great, and we saw a 40% decrease in drop-
off rates (which is significant given we were building a consumer facing app), but somehow over time this drop-off rate 
started creeping up again. Perplexed by the unexpected turn in metrics, management started to question the benefits of m
aintaining this chatbot and was skeptical that we were cherry picking examples to showcase its performance for the sake 
of not wasting our efforts. They also knew that GPT4 got shadow nerfed which didn't help our case at all.

We had a lot 
of back and forth and eventually came to the conclusion that somehow the chatbot performance have to be quantified to ju
stify it's purpose. So, our team spent another 2 months engineering an evaluation solution to show leadership that the c
hatbot is performing as expected while identifying areas of improvement to craft a more refined product roadmap. We ende
d up trying a lot of different things, and after a long process of iteration and experimentation here are the things tha
t worked for us:

1. Generating synthetic datasets (these act as 'ground truths' pair of queries and expected responses)
 to benchmark performance.
2. Training models to determine the similarity score to assess every ChatGPT output in produc
tion (we use the generated synthetic dataset to do this to compare expected responses vs real responses)
3. Classifying 
the type of use cases the chatbot was used for (this allowed us to see which use cases were performing worse)
4. Logging
 configurations in our LLM stack and building visualizations on the web to identify what gives the best results (tempera
ture, LangChain configurations, lLamaIndex chunking sizes, these type of configurations)
5. Monitoring how our costs and
 latency are affected by tweaking different parameters
6. Lastly, A/B test to figure out the optimal parameters on diffe
rent sets of users (from experience, typically for a user onboarding chatbot use case around 5,000 users interacting wit
h your chatbot should be enough to collect some meaningful datapoints)

The most important learnings that we took away w
as that whilst synthetic data is OK you do need to generate large amounts of it. The sweet spot is different depending o
n the use case + the specifics of your knowledge base (eg, a corpus of internal documents vs a collection of websites), 
and I say sweet spot because after a certain amount of datapoints everything else kind of becomes noise and actually neg
atively affects your analysis more than the benefit it brings.

We ended up showing where our chatbot onboarding experie
nce fell short and was able to fix it through rapid iteration. There's still no set standard for LLM evaluation but I ho
pe my previous experiences helped. (Our team is now building out this evaluation system as a standalone product at [www.
twilix.io](https://www.twilix.io/) so check us out if you also want some concrete proof that ChatGPT is performing as ex
pected for your business)
```
---

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-08-24-0909
```
What are the possible practical approaches to creating an 'AI tutor' for a custom fantasy language, i.e. a language whic
h is definitely not covered in any large, mainstream LLM?

Assume in the fantasy language (like Game of Throne's Dothrak
i, but completely custom, so it's guaranteed not to be covered at all by an existing LLM), we have a dictionary of terms
, and a simple description of a grammar. What can I do with that?

Initially I was thinking of using 'Retrieval-Augmente
d Generation' (RAG), where I would pass it my dictionary of terms and their definitions and the grammar doc (i.e. the so
urce documents), and using OpenAI's LLM and LangChain's API wrapper and Pinecone long-term memory vector database, store
 the dictionary/grammar in Pinecone's vector database. Then a query comes in to translate an English word to a fantasy w
ord, and it looks in the Pinecone DB for similar English words, then passes the results with the fantasy word to the LLM
, along with the query, and generates a nice English response, with the fantasy word somewhere in there.

But that doesn
't seem like it would work the more I think about it. Then if I want to add the ability for it to translate English to t
he fantasy language, that seems impossible without first having a huge corpus of translation material (which is complete
ly impractical for a fantasy language). So can an existing generic LLM take a grammar as input, and learn to speak a fan
tasy language? If so, how would you make that happen?

Or what are other approaches to accomplishing this sort of thing?

```
---

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-08-24-0909
```
&#x200B;

https://preview.redd.it/wl1gtcngnchb1.jpg?width=1500&format=pjpg&auto=webp&s=24e35d852603c6139fd67f79457ec593f
bad99f7

If you're someone who's curious about or working with LLMs there's a cool panel discussion coming up: 

* Compa
ring the pros and cons of using existing LLMs, prompt engineering, and fine-tuning on custom datasets for different ente
rprise use cases.
* Fine-Tuning LLMs: Exploring the advantages and challenges of fine-tuning LLMs on custom datasets to 
align with specific business objectives.
* Tools and platforms: Discussing the various tools and platforms to facilitate
 LLM implementation 
* Overcoming Challenges: Addressing the challenges associated with adopting LLMs, including data pr
ivacy, creating high quality datasets, computational resources, ethical considerations, and the need for specialized exp
ertise.
* Future Directions: Exploring emerging trends, advancements, and potential future applications of LLMs in the e
nterprise context.

Here's the event info: [https://www.eventbrite.com/e/large-language-models-for-enterprise-success-ch
allenges-and-approaches-tickets-695089811337?aff=oddtdtcreator](https://www.eventbrite.com/e/large-language-models-for-e
nterprise-success-challenges-and-approaches-tickets-695089811337?aff=oddtdtcreator)
```
---

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-08-24-0909
```
would it be possible to train or fine-tune a small (1-3B) model who's sole purpose is to perform function calls? similar
 to how we have tiny models like replit-v2-3B that are super capable at specific things like code auto-complete .  


i 
know that's how openAI implemented function call was by fine-tuning gpt-3.5/4 but I'm thinking just a straight up base m
odel trained to understand and excel at function calls (similar to Gorilla for apis)

i'm thinking it would be a perfect
 'glue' for bigger LLM apps-- avoiding the need for external tools like langchain/quidance/etc...
```
---

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-24-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-24-0909
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to  Nvidia GPU and Metal acceleration for GGML models !

Here is the project  link: [Cria- Local
 LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Langc
hain\` example in the project).

This is an ongoing project, I have implemented the \`embeddings\` and \`completions\` r
outes. The \`chat-completion\` route will be here very soon!

Really interested in your feedback and I would welcome any
 help :) !

&#x200B;

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-24-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-24-0909
```
 I worked for less than a year as a Data Engineer. I decided to look for other challenges and got a job as an AI enginee
r developing language models.

The product of the company that hired me is related to data and metadata management. My t
asks will be to introduce features to the product, including a chat function that will allow for asking questions about 
data. Other tasks will include research and proposing additional AI-related functionalities to the product (on premise).
 I have a two weeks left to start work and I need to prepare a bit. My job will involve implementing ready-made solution
s and conducting research (high level - I need to implement valuable features and no one cares how).

**What are the mos
t important things I should learn before starting work?**

First of all, I replicated a few applications from this blog:
 [https://blog.streamlit.io/tag/llms/](https://blog.streamlit.io/tag/llms/)

Then I have focused on Langchain. I'm also 
in the middle of a course on Udemy about Next-Gen AI projects - Beginner friendly - Langchain, Pinecone - OpenAI, Huggin
gFace & LLAMA 2 models

I need a roadmap that will guide me a bit. I'm looking for blogs/materials/courses that will giv
e me practical knowledge in this matter.
```
---

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-24-0909
```
I have a data set that isn't that large \~200 pdfs. I have done the regular RAG approach with Langchain, extracting text
, splitting into chunks, embedding with OpenAi embeddings and FAISS vector storage. However, when I do a similarity sear
ch with a question I would like answered it returns the wrong context. The documents are semi-structured information of 
examined bridges. A question I would like answered is f.e. 'what is the construction date of bridge X?'. When I input th
is question I get a lot of context of construction dates of other bridges. I think this is because the bridges are not e
xplicitly mentioned in the text. I tried adding the bridge name and document name to the page content string of the chun
ks, but this does nothing.

Does anyone have any tips on improving the embeddings retrieval in this case?
```
---

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-24-0909
```
I am running text inferencing on Llama2-7b through langchain. I have downloaded the model from langchain's Huggingface l
ibrary, and I am running the model on AWS ml.g4dn.12xlarge which has 4x**nvidia t4**, which gives a total 64GB of GPU me
mory and 192GB of normal memory. It is able to answer my queries in around 10 seconds for small queries, and upto 3 mins
 for big queries.

The task I am doing is retrieving information from a document(Understanding Machine Learning PDF) in 
a conversational way. I've extracted the main parts of the notebook and put it up [here](https://colab.research.google.c
om/drive/1uFNkZ6FI0qffwRpW6ubfdq0HrCqcqVUi?usp=sharing).

Where can I make changes to speed up the transaction. Is there
 any change I can do in the model configuration to speed it up? Because if I use HuggingFaceHubAPI, it is able to give a
n answer in less than 5 seconds. Are there any other areas I can optimise?

I appreciate any help you can provide. Thank
s!
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-24-0909
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
