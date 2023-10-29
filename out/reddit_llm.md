 
all -  [ 'Real' differences between vector databases ? ](https://www.reddit.com/r/LangChain/comments/17inxui/real_differences_between_vector_databases/) , 2023-10-29-0910
```
Hello,

Sorry in advance for this noob question but I'm quite new in the field. I started a RAG project and I'm not too 
sure how to store and access/search my data.

At the moment, I store all vectors and their metadata in a PGvector struct
ured database. When searching I'm scoring (cosine) every single vector against my query and returning the top-k elements
. 

I see that I am clearly missing the point of these vector databases :
What I'm doing scales linearly with the number
 of elements in my database. In fact, I'm not even computing the similarity score using the PGvector functions, so I mig
ht as well just push my vectors in a regular structured database... Obviously I'm missing something.

How do you avoid t
his O(n) scaling exactly?  What distinguishes an old school structured database in which would store arrays of floats an
d a true vector database ? And finally what's the difference between all these databases that are florishing these days 
?
```
---

     
 
all -  [ AzureOpenAi chat model doesn't seem to support LCEL. Am I doing something wrong? ](https://www.reddit.com/r/LangChain/comments/17imi4s/azureopenai_chat_model_doesnt_seem_to_support/) , 2023-10-29-0910
```
I am trying to use LCEL and it seems invoke function and the | operand is not implemented for this class. Is  that so ?
```
---

     
 
all -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-10-29-0910
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning
```
---

     
 
all -  [ AutoGen v0.1.14 released ](https://www.reddit.com/r/AutoGenAI/comments/17idxtm/autogen_v0114_released/) , 2023-10-29-0910
```
[New release: v0.1.14](https://github.com/microsoft/autogen/releases/tag/v0.1.14) 

**Highlights:**

* 📷Give vision to y
our agent: **multimodal** examples are added at [https://github.com/microsoft/autogen/blob/main/notebook/agentchat\_lmm\
_llava.ipynb](https://github.com/microsoft/autogen/blob/main/notebook/agentchat_lmm_llava.ipynb).
* 📷**TeachableAgent** 
blogpost: [https://microsoft.github.io/autogen/blog/2023/10/26/TeachableAgent](https://microsoft.github.io/autogen/blog/
2023/10/26/TeachableAgent).
* 📷 Run a chat in a different thread/process: using thread safe timeout for code execution.

* 📷 Qdrant vector store: A QdrantRetrieveUserProxyAgent is added in contrib/.
* 📷 Support new version of chromadb in ret
rieve chat.
* 📷 Token count utils.
* 📷 Improve vscode extension setup in codespace.
* 📷 Many improvements in documentati
on, FAQ, useful tips, such as
   * how to prevent gpt-3.5 agents' appreciation loop
   * fixes in the langchain notebook

   * link to the roadmap
   * common issues in retrieve chat

Thanks to u/Beibin **Li** u/Ricky **Loynd** u/ragyabraham
 u/Anush008 u/Li_Jiang u/Kevin **Wu** u/shruti222patel u/craigomatic u/AaronWard and all the other contributors! 

**Hea
dsup:**

v0.2 release is near the corner, and we'll switch to openai v1 in it. Please check for breaking changes in [htt
ps://github.com/microsoft/autogen/pull/393](https://github.com/microsoft/autogen/pull/393). We'll try to add as many fea
tures back as possible before the release. If you see any breaking changes that affect your work, please comment in the 
PR thread. 
```
---

     
 
all -  [ Muriel -> One click children's story (WIP) ](https://i.redd.it/e8ekklfa4ywb1.png) , 2023-10-29-0910
```
Muriel the mole, in her burrow so snug,
Knew every cranny, every hole, every bug.

But one rainy day, as the storms thun
dered on,
Her cozy burrow flooded, her safe place was gone.

She peered out the entrance, at the world so vast,
Took a b
rave little step, left her home in the past.

First, she met Mr. Fox, with a sly sneaky grin,
Feeling a tingle of worry,
 she burrowed back in.

She popped up behind him, gave a small 'Boo!'
'Gotcha!' she giggled, and off she flew.

Then cam
e Miss Hawk, her eyes on the prize,
'Mmm, a mole for lunch,' she said with surprise.

But Muriel was quick, she hid with
 a dash,
'Better luck next time!' she called with a splash.

A prowling cat, a snake, and a wolf too,
Each time she esca
ped, her confidence grew.

Yet, she yearned for her burrow, she started to tire, When a beautiful meadow set her heart o
n fire.

A perfect spot beneath a tree, lush grass underpaw,
But alas! An eagle guarded it, the fiercest she saw.

With 
a gulp and a sigh, she approached the great bird,
'Hello, Mr. Eagle,' she said, her voice firm and heard.

'Aren't you s
cared?' he asked, his eyes full of surprise,
'I am,' Muriel confessed, 'But I need a home, wise.'

The eagle was moved b
y the mole's brave plea,
'You may stay in my meadow, just promise to let be.'

Muriel nodded eagerly, she could finally 
rest,
In her new burrow, warm and snug, truly the best.

And so, Muriel settled in her meadow so grand,
Made friends wit
h the creatures, in this new land.

She'd visit the eagle, share tales of her day,
In her cozy burrow, she was happy to 
stay.

The world outside, once big and unknown,
Now filled with adventures, friendships grown.

No longer did Muriel fea
r the unknown, it was clear,
For wherever she was, she could find home, dear.

==========

'Muriel' is the latest childr
en's story generated by a fun little side project I'm working on, using GPT-4, LangChain and Streamlit. As of now it's a
 5 step prompting process, with the output being exactly what's pasted above. The image is DALL-E, not included in the g
eneration (yet).

Overall I'm pretty damn chuffed with it. It still needs further improvement, but It's reached the leve
l where I'd consider reading it to my toddler.

Long term I'm hoping to have bookstore quality children's books with 20+
 images by the time I'm done. We'll see how long it takes.
```
---

     
 
all -  [ OPENAI_FUNCTIONS and multi-input tools. ](https://www.reddit.com/r/LangChain/comments/17iaydd/openai_functions_and_multiinput_tools/) , 2023-10-29-0910
```
Hi folks, not usually one to use forums so forgive any improper formatting/lack of information.

I've got a tool that I 
want to pass into an OPENAI\_FUNCTIONS agent that scraped a website given a target string and a URL, and I've broken it 
down into a schema (for input) and a Tool to give to the agent:

    class ScrapeWebsiteInput(BaseModel):
        object
ive: str = Field(description = 'The objective & task that the user gives the agent')
        url: str = Field(descriptio
n = 'The URL of the website to scrape')
    
    class ScrapeWebsiteTool(BaseTool):
        name = 'scrape'
        desc
ription = 'A tool to scrape a website'
        args_schema: Type[BaseModel] = ScrapeWebsiteInput
    
        def _run(s
elf, objective: str, url: str):
            return scrape(objective, url)
        
        def _arun(self, url: str):
  
          raise NotImplementedError('Error') 

And I'm passing it in as such:

    tools = [
        Tool(
            n
ame = 'Search',
            func = search,
            description = 'Useful for when you need to answer questions about
 current events, data. You should ask targeted questions.'
        ),
        ScrapeWebsiteTool(),
    ]

However, it in
sists that the agent type I'm using doesn't take multi-input tools: `ValueError: ZeroShotAgent does not support multi-in
put tool scrape.` I'm nearly positive I've read docs/seen examples where you can indeed pass multi-input tools into this
 type of agent, but I very well could be wrong.

Running this on LangChain 0.0.325, OpenAI 0.28.1, Python 3.11.2.

Any h
elp is appreciated, and let me know if I'm missing details. I've tried to be as descriptive as possible.
```
---

     
 
all -  [ What is the simplest vector store to use which can store too much data? ](https://www.reddit.com/r/LangChain/comments/17iaajt/what_is_the_simplest_vector_store_to_use_which/) , 2023-10-29-0910
```
We're using Langchain, Python, and German articles. I am looking for a totally free self-hosted vector store, that can h
ost big data, the simplest the setup the better.  The articles are stored in SQLite for now.

We're using FAISS but it c
an only store 4GB worth of embedding and we have much more than that and it's causing issues.

I tried Chroma before wit
h German data, I don't know if it's me doing something wrong or if Chroma is bad, but I noticed that FAISS is way better
 so  I switched to FAISS and now I'm facing this 4GB storage issue.

I tried sqlite-vss but it's buggy, can't even insta
ll it on Windows via pip.

What I hate about FAISS, also is that you have to serialize data on storage and deserialize i
t on retrieval and it doesn't support adding data to existing data, you have to do a merge and write to disk again.

I'm
 looking for the following:

1. Self-hosted, free vector store database that supports an unlimited number of embeddings.

2. Similar or better performance to FAISS
3. No serialization and deserialization, at least not from my side, I don't c
are what it does under the hood. And the ability to add data to an existing vector store.
4. (optional)A data viewer/Rea
der would be nice so I can see what's being inserted
5. (optional) The ability to add metadata, such as article ID and U
RL would be very much appreciated so that I know which embedding belongs to which article, and then I can output the URL
 associated with the embedding, 
```
---

     
 
all -  [ AI infra career advice ](https://www.reddit.com/r/LangChain/comments/17i8ml3/ai_infra_career_advice/) , 2023-10-29-0910
```
Hey folks I'm now in big tech company working in core infra teams, but always willing to build a career in AI/ML infra. 
Usually when talking about AI infra in tech industry, we refer to training infra, serving infra, model deployment etc in
volving lots of compute infra work such as GPU cluster management.

Now with this genAI/LLM revolution, I find many NLP 
specific infrastructure such as semantic indexing, vector databases are quickly rising up as we've seen in LangChain whi
ch I feel quite interesting to me. So do semantic indexing/vector databases stuff also count as AI infra? If I work on t
his track, would it fit into my career plan of AI infra?  Thanks!
```
---

     
 
all -  [ Python langchain ctransformers help ](https://www.reddit.com/r/LocalLLaMA/comments/17i4odt/python_langchain_ctransformers_help/) , 2023-10-29-0910
```
Hi! I am trying to build a local chatbot using dolphin 2.1 mistal 7b. I am using langchain and ctransformers for this.


Edit: I changed the loading of llm into a variable from a function and it worked keeping the model loaded! The issue if 
memory still persists so it still doesnt remember anything I tell it. Any help would be appreciated. Thanks!

    from l
angchain.llms import CTransformers
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLM
Chain
    
    llm = CTransformers(
            model='/home/chupz22/text-generation-webui/models/dolphin-2.1-mistral-7b
.Q5_K_M.gguf',
            model_type='mistral',
            config={'max_new_tokens': 1024,
                    'repeti
tion_penalty': 1.1,
                    'top_k': 40,
                    'top_p': 0.95,
                    'temperature
': 0.8,
                    'gpu_layers': 35,
                    'threads': 8,
                    'context_length': 81
92,
                    'stop': ['/s', '<|im_end|>']})
    
    
    def llm_function(message, chat_history):
        ll
m = load_llm()
        template = ('<|im_start|>system'
                    'Prompt <|im_end|>'
                    '<|i
m_start|>user'
                    '{prompt}<|im_end|>'
                    '<|im_start|>assistant')
        prompt = Pr
omptTemplate(template=template, input_variables=['prompt'])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
       
 response = llm_chain.run(
            message
        )
        output_texts = response
        return output_texts

&#
x200B;
```
---

     
 
all -  [ A Free model on langchain for testing ](https://www.reddit.com/r/LangChain/comments/17i15he/a_free_model_on_langchain_for_testing/) , 2023-10-29-0910
```
Hi All ,hope you are having a great day! 

I am developing some apps with langchain and i dont have an api key for openA
I , I want to know if there is any other models that i can use that are hosted online and i will not need to pay for the
 api tokens ? I am in a region where OpenAI is not accepting my payment so I am stuck 

thanks 
```
---

     
 
all -  [ Is there a good way to definitively handle context size in an agent with functions? ](https://www.reddit.com/r/LangChain/comments/17i0ayk/is_there_a_good_way_to_definitively_handle/) , 2023-10-29-0910
```
I have an agent that is allowed to continue researching until it is ready to provide an answer.

However if it accumulat
es too much and exceeds the token limit, it will just crash.

I would love if there were some backup plan, an error call
back or something, where I could handle what to do in that case.

Maybe I would summarize or condense it's results so fa
r, then have it pick up where it left off. Idk, just wondering if there is any way for me to control that other than bui
lding my own custom agent.

Thanks!
```
---

     
 
all -  [ Parsing table information using ChatOpenAI from PDF files? ](https://www.reddit.com/r/LangChain/comments/17hug7a/parsing_table_information_using_chatopenai_from/) , 2023-10-29-0910
```
I’m having some trouble querying tabular data from PDF files. Here is roughly what I’m doing.

1. Load PDF file using th
e UnstructuredFileLoader
2. Split the returned documents using the RecursiveTextSplitter
3. Initialize Chroma vector db 
and store the documents using the OpenAI embeddings
4. Create a prompt with instructions from a custom Pydantic Base Mod
el.
5. Pass the vector db as a retriever and pass the prompt (asking for JSON formatted data)
6. Store result and clear 
vectordb and repeat from step 1 with new file

Problem is tabluar data into raw text doesn’t seem to be understood well 
by the LLM unless I somehow clean it up or something

So I was searching through the web and seems like some people will
 use external APIs or pdfplumber to parse out the tabular data better before saving it.

Anyone else having similar issu
es?
```
---

     
 
all -  [ DataStax integrates LangChain into Astra DB vector database for generative AI applications ](https://multiplatform.ai/datastax-integrates-langchain-into-astra-db-vector-database-for-generative-ai-applications/) , 2023-10-29-0910
```

```
---

     
 
all -  [ Why is my similarity search results so awful? ](https://www.reddit.com/r/LangChain/comments/17htk8q/why_is_my_similarity_search_results_so_awful/) , 2023-10-29-0910
```
I'm working on an project, where I scrape the FAQ from a website and try to q&a it. I used chromadb to create and store 
a vector database locally. I'm using chain to query the vector database and the results are subpar. For example if I as 
'how to change my address' it returns the right data section, but if I ask  'I just moved to a new home' if  doesn't und
erstand the context of the message. I figured this is because I'm hitting the limitations of llm + vector db, but i'm a 
noob to all this so idk. I figured the similarity search would connect 'home' to 'address' would it not?
```
---

     
 
all -  [ 🦙 How To: Build Chatbot that knows your company's documents ](https://www.reddit.com/r/LocalLLaMA/comments/17hs77a/how_to_build_chatbot_that_knows_your_companys/) , 2023-10-29-0910
```
Hello, I've seen some posts asking how to build a chatbot with access to company docs, so here is a tutorial on building
 a RAG chatbot with access to your data.  


Step 1: Choose your models  
Different models have different strengths. GPT
4 is the best at reasoning and following instructions, but less secure than local models. For secure but weaker local mo
dels, Xwin (70B) is a good choice if you have powerful hardware. If you are GPU poor you can use Speechless (13B). For t
he embedding models, you can use OpenAI's ADA 2 or locally use MiniLM-L6-v2.  


Step 2: Organize your data  
This step 
is more complicated because it depends on what your data looks like. The good news is as long as it can be turned into t
ext the models can work with it. At a basic level, you can convert important pdfs or other text documentation into text,
 and add it to a RAG database. [Here](https://youtu.be/LhnCsygAvzY?t=1067) is a good tutorial. If you have lots of secur
e data it can be more complicated. Feel free to DM me.  


Step 3: Set up in LangChain  
LangChain is an easy way to set
 up the chatbot. [Here](https://python.langchain.com/docs/get_started/introduction) are the docs. The basic idea is to c
onnect your RAG database with the model of your choice and use LangChain's interface to customize your chatbot's functio
nality. After you set this up, the model will be able to access your company's documentation and answer specific questio
ns about it!  


This tutorial is not an in-depth guide, it's more of a high level overview for those who are new to the
 space or RAG. If you have questions DM me and good luck!
```
---

     
 
all -  [ How are you handling Large CSVs/datasets? ](https://www.reddit.com/r/LLMDevs/comments/17hr5vr/how_are_you_handling_large_csvsdatasets/) , 2023-10-29-0910
```
What have been people's approaches to handling and analysing large CSVs e.g. with 100K rows. Obviously too big to place 
in a GPT prompt so I've tried embedding but that isn't great if you ask 'how many people opted in?' because it's got no 
quantitative abilities. 

Additionally I've tried LangChain agents to run some Python code on the sheet but they can oft
en go off on a tangent and get stuck.

Curious, of any other approaches in the community?
```
---

     
 
all -  [ Vector Store or Memory? ](https://www.reddit.com/r/LangChain/comments/17hqoq1/vector_store_or_memory/) , 2023-10-29-0910
```
I've got a bunch of documents I have loaded into a vector store which together give an overview of an event. For example
, a location breakdown, a guest list, vendor information, etc. I'm trying to get the LLM to create a page of text descri
bing the event in detail. I don't think the vector store is the right way to go because it just uses chunks of text as c
ontext and I need the LLM to know ALL the information in the documents in order to give a comprehensive overview. Should
 I just feed all the documents in as part of my prompt? I would ideally like to use memory so that the LLM can build up 
a full picture of the event over time. So as more documents get added, it would generate a more full and complete report
. Is this possible?
```
---

     
 
all -  [ SQL Bot giving Observation and thought as its final answer, this is very strange, I am probably doin ](https://www.reddit.com/r/LangChain/comments/17hptw7/sql_bot_giving_observation_and_thought_as_its/) , 2023-10-29-0910
```
I am building a SQL bot a database using SQLDatabasechain using davinci model from Open AI, using gradio as UI.  
Chain 
Output in terminal :  


https://preview.redd.it/ik7u4f1ihrwb1.png?width=1631&format=png&auto=webp&s=df4e18c1b4238319643
e6733d2ee729fd8b31476

&#x200B;

Output in gradio:   


https://preview.redd.it/aypxoexkhrwb1.png?width=1521&format=png&
auto=webp&s=daaad722945943ef4bd2939298da1ecca86ca852

&#x200B;

This is not showing the actual output it is supposed to 
print, it is showing a question which outputted at last,   
my prompt follows the following format,   


https://preview
.redd.it/h60x6glthrwb1.png?width=399&format=png&auto=webp&s=b23b94c1d98da5505639cd35618cbeb8e9c4bd10
```
---

     
 
all -  [ How to Get Around Context Limits with Data Files ](https://www.reddit.com/r/LocalLLaMA/comments/17hl6z7/how_to_get_around_context_limits_with_data_files/) , 2023-10-29-0910
```
I want to loop through a list of test strings and check each against thousands of answer options to pick the closest one
 based on knowledge from a given PDF. The problem is that I can't fit thousands of answers into the prompt.

I have a se
t list of options (answers) that looks like this...
    
    # answers.txt
    18q deletion syndrome
    Aagenaes syndro
me
    Abrasion
    Acanthamoeba infection
    # ... with about 2400 in total.

I have a user entered list of diagnoses 
that may or may not be in the list of options (tests) to loop through...
    
    # tests.txt
    1	Reactive arthritis
 
   2	Basal cell carcinoma
    # ... with about 55 thousand total entries

I have a textbook PDF with information about t
he answers that is about 3100 pages, and I appended the answers to the end as shown below...
    
    # data.pdf
    # .
.. Lots of information for about 3100 pages
    The curly brackets contain a specifically accurate and appropriate optio
n {18q deletion syndrome}
    The curly brackets contain a specifically accurate and appropriate option {Aagenaes syndro
me}
    The curly brackets contain a specifically accurate and appropriate option {Abrasion}
    The curly brackets cont
ain a specifically accurate and appropriate option {Acanthamoeba infection}
    # ... for about 100 added pages.

I thin
k that the biggest problem is getting the model to consider all 2,383 options. It is far too many to fit in a reasonable
 context. This is the prompt template and prompt that I am using...
    
    target_string = 'specifically accurate and 
appropriate option'
    qa_template = '''Use the following pieces of information to answer the user's question.
    If y
ou don't know the answer, just say that you don't know, don't try to make up an answer.
    The answer should include a 
%s.
    
    Context: {context}
    Question: {question}
    
    Only return the helpful answer below and nothing else.

    Helpful answer: The closest option is
    ''' % target_string
    
    prompt = f'Which {target_string} is closest 
to {test}?'

... I think this needs to be changed to a User/Assistant format too, but I wasn't sure how to appropriately
 modify the template to facilitate that.

I modified this [LangChain RetrievalQA Github project](https://github.com/kenn
ethleungty/Llama-2-Open-Source-LLM-CPU-Inference) and ended up with the code at the end. When I run it, I get the result
s below...
    
    Loading lists...
    53845 tests and 2383 answers were loaded
    Checking Reactive arthritis...
   
 Checking Basal cell carcinoma...
    ==================================================
    Reactive arthritis => Arth 
Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth 
Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth 
Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth 
Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth 
Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth Arth 
Arth Arth Arth Arth Arth Arth Arth
    Basal cell carcinoma => High-risk basal cell carcinoma (e.g. micronodular, morphe
aform)
    ==================================================
    Time to retrieve response: 165.31
    
... Neither ans
wer is from the list, and obviously the repetition is undesirable. 
    
Based on previous recommendations, I found that
 I could reliably get this to work when all of the answers were explicitly included in the prompt (previous code shown a
t end).

Does anyone have any suggestions or recommendations on where to go from here? I imagine that I either need to t
weak my prompt/prompt template or dramatically change my entire approach.


**Current Code based on kennethleungty's exa
mple:**

    import box, time, yaml, argparse
    
    from dotenv import find_dotenv, load_dotenv
    from langchain im
port PromptTemplate
    from langchain.chains import RetrievalQA
    from langchain.embeddings import HuggingFaceEmbeddi
ngs
    from langchain.vectorstores import FAISS
    from langchain.llms import CTransformers
    from langchain.text_sp
litter import RecursiveCharacterTextSplitter
    from langchain.document_loaders import PyPDFLoader, DirectoryLoader
   
 
    # Load environment variables from .env file
    load_dotenv(find_dotenv())
    
    # Import config vars
    with 
open('config/config.yml', 'r', encoding='utf8') as ymlfile:
    	cfg = box.Box(yaml.safe_load(ymlfile))
    
    target_
string = 'specifically accurate and appropriate option'
    
    qa_template = '''Use the following pieces of informatio
n to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an
 answer.
    The answer should include a %s.
    
    Context: {context}
    Question: {question}
    
    Only return t
he helpful answer below and nothing else.
    Helpful answer: The closest option is
    ''' % target_string
    
    
  
  # Build vector database
    def run_db_build():
    	loader = DirectoryLoader(cfg.DATA_PATH, glob='*.pdf', loader_cls=
PyPDFLoader)
    	documents = loader.load()
    	text_splitter = RecursiveCharacterTextSplitter(chunk_size=cfg.CHUNK_SIZ
E,
    	                                               chunk_overlap=cfg.CHUNK_OVERLAP)
    	texts = text_splitter.split
_documents(documents)
    	
    	embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
 model_kwargs={'device': 'cpu'})
    	
    	vectorstore = FAISS.from_documents(texts, embeddings)
    	vectorstore.save_
local(cfg.DB_FAISS_PATH)
    
    
    def build_llm():
    	# Local CTransformers model
    	llm = CTransformers(model=
cfg.MODEL_BIN_PATH, model_type=cfg.MODEL_TYPE,
    	                    config={'max_new_tokens': cfg.MAX_NEW_TOKENS, 't
emperature': cfg.TEMPERATURE})
    	return llm
    
    
    def set_qa_prompt():
    	# Prompt template for QA retrieva
l for each vectorstore
    	prompt = PromptTemplate(template=qa_template, input_variables=['context', 'question'])
    	
return prompt
    
    
    def build_retrieval_qa(llm, prompt, vectordb):
    	dbqa = RetrievalQA.from_chain_type(llm=l
lm, chain_type='stuff',
    	                                   retriever=vectordb.as_retriever(search_kwargs={'k': cfg.
VECTOR_COUNT}),
    	                                   return_source_documents=cfg.RETURN_SOURCE_DOCUMENTS,
    	      
                             chain_type_kwargs={'prompt': prompt}
    	                                   )
    	return 
dbqa
    
    
    def setup_dbqa():
    	embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniL
M-L6-v2',
    	                                   model_kwargs={'device': 'cpu'})
    	vectordb = FAISS.load_local(cfg.D
B_FAISS_PATH, embeddings)
    	llm = build_llm()
    	qa_prompt = set_qa_prompt()
    	dbqa = build_retrieval_qa(llm, qa
_prompt, vectordb)
    	
    	return dbqa
    
    
    def load_lists():
    	print('Loading lists...')
    	tests = []

    	answers = []
    	testsf = 'tests.txt'
    	answersf = 'answers.txt'
    	with open(testsf, 'r') as f:
    		for i
line in f.readlines():
    			i, idx = iline.replace('\n', '').split('\t')
    			if idx != '':
    				tests.append(idx
)
    	
    	with open(answersf, 'r') as f:
    		for iline in f.readlines():
    			answers.append(iline.replace('\n', 
''))
    	
    	print(f'{len(tests)} tests and {len(answers)} answers were loaded')
    	
    	return [tests, answers]
 
   
    
    def generate_pre_pdf(strings, target):
    	prePdfList = []
    	print('Starting export...')
    	prePdfFil
ename = 'Diagnosis PrePDF.txt'  # [prefix] diagnosis
    	for ianswer in strings:
    		prePdfList.append('The curly bra
ckets contain a %s {%s}' % (target, ianswer))
    		print(ianswer)
    	with open(prePdfFilename, 'w') as f:
    		f.wri
te('\n'.join(prePdfList))
    
    
    if __name__ == '__main__':
    	parser = argparse.ArgumentParser()  # if 'build'
 is passed, then the database will be rebuilt, 'pdf' will generate a txt file to be appended
    	parser.add_argument('m
ode', type=str)
    	args = parser.parse_args()
    	
    	# Setup DBQA
    	tests, answers = load_lists()
    	start = 
time.time()
    	qa = setup_dbqa()
    	if args.mode == 'build':  # rebuild the PDF database
    		print('Rebuilding dat
abase...')
    		run_db_build()
    		print(f'Time to build database: {(time.time() - start):.2f}')
    	elif args.mode 
== 'pdf':  # Generate a text file to be appended to PDF
    		print('Generating text file for pdf...')
    		generate_pr
e_pdf(answers, target_string)
    		print(f'Time to prepare text file: {(time.time() - start):.2f}')
    	else:  # any o
ther input will run the model
    		# Check tests
    		responses = []
    		for i in tests[:2]:  # stopping short for t
esting purposes
    			print(f'Checking {i}...')
    			iquery = f'Which {target_string} is closest to {i}?'
    			resp
onse = qa({'query': iquery})
    			responses.append(f'{i} => {response['result']}')
    		
    		print('=' * 50)
    		
print('\n'.join(responses))
    		print('=' * 50)
    		print(f'Time to retrieve response: {(time.time() - start):.2f}')

    

**Previous attempt based on /u/shibe5 's reccomendations:**
    
    import time
    from llama_cpp import Llama

    
    model_dir = 'C:/Models/'
    model_name = 'luna-ai-llama2-uncensored.Q4_K_M.gguf'
    
    answers = '\n'.join(
['red', 'blue', 'gray', 'yellow', 'green', 'purple', 'brown'])
    tests = ['cyan', 'pink', 'silver', 'blue', 'orange', 
'fuschia', 'vermillion', 'granite', 'teal', 'navy']
    replace_str = '**x**'
    
    prompt = f'''
    USER: Answer op
tions: {answers}
    ASSISTANT: The closest option to {replace_str} is
    '''
    prompt = prompt.lstrip().rstrip()  # 
strip leading/trailing characters
    
    start_time = time.time()
    
    outputs = []
    llm = Llama(model_path=mod
el_dir + model_name, n_ctx=512)
    for itest in tests[:2]:
    	print(f'Checking {itest}')
    	output = llm(prompt=pro
mpt.replace(replace_str, itest), max_tokens=32, echo=False, temperature=0)
    	answer = output['choices'][0]['text']
  
  	tokens = f'ptokens: {output['usage']['prompt_tokens']}, ctokens: {output['usage']['completion_tokens']}'
    	outputs
.append(f'{itest} => {answer} ~~ {tokens}')
    
    print('=' * 50)
    print('\n'.join(outputs))
    
    elapsed = ti
me.time() - start_time
    print(f'Total time: {elapsed:.2f} s')

That was a lot. Thanks for any help that anyone can pr
ovide.
```
---

     
 
all -  [ Adding and Deleting PDF/URL/Confluence Data in Combined 'Embeddings' Folder using ChromaDB ](https://www.reddit.com/r/LangChain/comments/17hjitt/adding_and_deleting_pdfurlconfluence_data_in/) , 2023-10-29-0910
```
I've successfully generated and stored embeddings for PDF documents, Confluence content, and URL data within a single 'e
mbeddings' folder using ChromaDB, and I'm also performing question answering on this data. However, I'm looking to enhan
ce the functionality and add the ability to delete and re-add PDF/URL/Confluence data from this combined folder while pr
eserving the existing embeddings.

I believe this feature would significantly improve the versatility of the application
 and make it more user-friendly. Any guidance or contributions in implementing this functionality would be greatly appre
ciated.
```
---

     
 
all -  [ Debugging JSONDecodeError when using OutputParser ](https://www.reddit.com/r/LangChain/comments/17hep0o/debugging_jsondecodeerror_when_using_outputparser/) , 2023-10-29-0910
```
Can someone here guide me in how to debug the JSONDecodeError when using OutputParser?

It is kind of random and the sta
cktrace is not very helpful (to me at the least)
```
---

     
 
all -  [ Alternatives to LangChain ](https://www.reddit.com/r/LangChain/comments/17hdctv/alternatives_to_langchain/) , 2023-10-29-0910
```
I usually don't come down so hard on open source tools but man...my foray into LangChain over the last couple days has b
een a disaster.

The API is all over the place, and I can't shake the feeling that most modules are just light wrappers 
(I haven't looked at the source code the check, but I feel like I could achieve a similar output with a few lines of cod
e in some cases). Dealing with so many abstractions might be ok if wasn't for the fact the documentation is all over the
 place.

At this point I'm thinking of just going back to vanilla GPT, but a nice lightweight library would still be use
ful. Wondering if anyone has any suggestions?
```
---

     
 
all -  [ How deep of a chain are you using to get 'x' quality of 'truth' using outside context? ](https://www.reddit.com/r/LangChain/comments/17h92wg/how_deep_of_a_chain_are_you_using_to_get_x/) , 2023-10-29-0910
```
I have a PoC/prototype of my own and am not using LangChain yet but am looking into it. One thing that I'm struggling wi
th (as are many others) are how to remove or at least mitigate hallucinations.

I like the idea of chaining and layering
 on validation/checks, but don't have a intuition for how deep (and therefore costly) these chains need to be.

Has anyo
ne tried this enough to share your experience on this?

I'm trying to balance accuracy with cost and implementation comp
lexity

Overall, I think everyone knows AI lies to some degree right now and the important thing is to provide tools to 
incrementally get them closer to what you want over time.
```
---

     
 
all -  [ Resume Review please. I will graduate next year looking for AIML related jobs ](https://i.redd.it/sjr1ugzohlwb1.jpg) , 2023-10-29-0910
```
Also is adding freelancing a red flag? I have heard some people say that but I am not quite sure yet. Thanks in advance!

```
---

     
 
all -  [ get_openai_callback() returns <4000 tokens, but output seems to incomplete ](https://www.reddit.com/r/LangChain/comments/17h2h9a/get_openai_callback_returns_4000_tokens_but/) , 2023-10-29-0910
```
I am using the LLM to make a JSON output (defined by the format instructions of a PydanticOutputParser) and the JSON str
ucture is not fully completed. However, when using „get_openai_callback()“ the result is about 2000-3000 tokens in total
 only.

Any idea how this might fit together?

If it is important: I am using AzureOpenAI.
```
---

     
 
all -  [ How can I load FAISS index from an azure blob to an azure function ](https://www.reddit.com/r/LangChain/comments/17h206w/how_can_i_load_faiss_index_from_an_azure_blob_to/) , 2023-10-29-0910
```
I am not sure how to do this task, it should be simple. 

I have a locally saved faiss index, and when I run my app loca
lly, I can load it using 

FAISS.load_local('faiss_index', embeddings)

But I want to create an azure function which tak
es the user prompt, runs the similarity search and then the QA chain and returns the output to the user. Now I uploaded 
the faiss index folder to the azure blob, but how would the loading work? I can get the relevant container and blob file
s in the function.. but then how can I load it into a db? I can only get a list of the individual files, not a folder. 


At the moment, I am looking through https://api.python.langchain.com/en/latest/_modules/langchain/vectorstores/faiss.ht
ml
and the load_local class method. Do you think it is feasible to load everything separately as done in there and build
 it like that?

edit: I think i got it, i will serialize it to bytes and check the resuts
```
---

     
 
all -  [ Insightful responses from LLM ](https://www.reddit.com/r/LangChain/comments/17h0tlg/insightful_responses_from_llm/) , 2023-10-29-0910
```
So I've been thinking.... Typically when you want to query a document using a RAG LLM application, simply running the pr
ompt through the LLM doesn’t result in insightful responses. Simply because it's doing similarity searches based on prom
pts using the context to generate responses. And  Not exactly looking for nuances within the document that could possibl
y generate insightful responses.   here's what i mean, let's say you were querying the 10-k filing of a company and want
ed to generate a thorough report of the company's risk profile. You most likely wouldn't get a comprehensive report by s
imply prompting “generate a comprehensive risk profile of this company using the context”.   My idea was to use a bunch 
of prompts, essentially meaning the same thing, and then creating a summary of the various responses generated. I got th
e idea from the subquestion query engine by llama\_index.  Wondering if anyone had any thoughts?

https://preview.redd.i
t/2nn0blr5tkwb1.png?width=2518&format=png&auto=webp&s=4f080b797937e0f71a99e7f1e8e2daf52239db05
```
---

     
 
all -  [ Resume Review: How to stand out? ](https://www.reddit.com/r/cscareerquestionsEU/comments/17h0r4q/resume_review_how_to_stand_out/) , 2023-10-29-0910
```
Hey guys, 

i applied to a bunch of international tech companies, but i didn't get an interview. Thus I have several que
stions:

1.) Is there something wrong about my resume ( [https://imgur.com/nwo0Gln](https://imgur.com/nwo0Gln)) or is it
 rather the bad job market right now?

2.) Since I currently have a job, i could focus on improving my resume. What woul
d make my resume stand out? Should i develop a strong project ( I am currently interested in some LLM stuff with LangCha
in or a project with reinforcement learning) or is it better to contribute to an known open source project? Or should i 
develop a portfolio webpage first (even tho I want to focus more on backend/ data engineering)?
```
---

     
 
all -  [ ChatOpenAI Chat history ](https://www.reddit.com/r/LangChain/comments/17gvmgx/chatopenai_chat_history/) , 2023-10-29-0910
```
    llm = ChatOpenAI(temperature=0)                          
    tools = [Tool1(), Tool2()]
    
    agent = initialize
_agent(tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True)
    x = agent.run(message_str)

Hey, I was wond
ering how Can I pass chat history here? Like messages parameter chat openai has by default? with system messages and etc
?
```
---

     
 
all -  [ Shorthills AI in Top 10 LangChain Contributors ](https://www.reddit.com/r/LangChain/comments/17gtt11/shorthills_ai_in_top_10_langchain_contributors/) , 2023-10-29-0910
```
&#x200B;

[Celebrating Shorthills AI success](https://preview.redd.it/5rp48tn42jwb1.jpg?width=2616&format=pjpg&auto=webp
&s=47edd07d84740c6379b6ba12bc124b889f752b10)

[We're Top 10 Langchain Contributors worldwide](https://preview.redd.it/47
0vhrn42jwb1.jpg?width=3200&format=pjpg&auto=webp&s=a236fcfb87b3796c0e041234ff6b8d75fc3adeea)

[Team behind our Success](
https://preview.redd.it/q2jqcyp42jwb1.jpg?width=2776&format=pjpg&auto=webp&s=0b44196f6b09967089a5b130c4b68ac5724fc518)


[LangChain and Shorthills long term partnership](https://preview.redd.it/o8itcgp42jwb1.jpg?width=2448&format=pjpg&auto=w
ebp&s=770d31242127384ec89bc46ec2c18b452e3f4c26)
```
---

     
 
all -  [ JSON and FewShotPrompt ](https://www.reddit.com/r/LangChain/comments/17gsqvr/json_and_fewshotprompt/) , 2023-10-29-0910
```
Hey Guys !   


Some off you have ever tried to use FeewShotPrompts with JSONs ?  
I face this difficulty which is very 
annoying cause the results could be awesome for API connection (To jira in this exemple)  


Here is the Subject : [http
s://github.com/langchain-ai/langchain/issues/4367](https://github.com/langchain-ai/langchain/issues/4367)
```
---

     
 
all -  [ Frontier Model Forum Appoints New Executive Director and Launches AI Safety Fund; Google AI Introduc ](https://www.reddit.com/r/ai_news_by_ai/comments/17gpt5o/frontier_model_forum_appoints_new_executive/) , 2023-10-29-0910
```





#major_players #event #startups #leaders #science #opinions #api #tool #release #feature #update #scheduled

OpenAI
, Anthropic, Google, and Microsoft have announced the appointment of Chris Meserole as the Executive Director of the Fro
ntier Model Forum, an industry body focused on the safe and responsible development and use of frontier AI models. Meser
ole brings extensive experience in technology policy and the governance and safety of emerging technologies [1][3]. The 
Frontier Model Forum will focus on three key areas within AI safety: identifying best practices, advancing AI safety res
earch, and facilitating information sharing among companies [2][3]. 







In addition, a new AI Safety Fund has been e
stablished, a $10 million initiative to promote research in the field of AI safety. The fund will support independent re
searchers from academic institutions, research institutions, and startups, with a primary focus on developing new model 
evaluations and techniques for red teaming AI models to identify potentially dangerous capabilities [1][3][4][5]. The Fr
ontier Model Forum will establish an Advisory Board and issue additional technical findings in the future [1][3].








Six years ago, the first general meeting of the Partnership on AI (PAI) took place. PAI is an organization that funds s
tudies and publishes guidelines on AI ethics and safety. Recently, they published a set of guidelines for the safe deplo
yment of foundation models [6].







Andrew Ng has announced a new short course called 'Functions, Tools, and Agents w
ith LangChain' taught by LangChain CEO Harrison Chase. The course covers the latest advancements in LLM function calling
, using LLMs to process formatted data like JSON, and building agents. The course is free for a limited time and is reco
mmended for anyone interested in learning about the latest tools to build LLM-based applications [7].







Google Sear
ch has introduced three new features to help users check the credibility and context of images and sources they encounte
r online. These tools aim to help users verify the authenticity and reliability of online images and sources [9]. Google
 AI has also introduced a new grammar check feature in Google Search that allows users to check if a phrase or sentence 
is grammatically correct and provides corrections when needed. This feature is powered by a novel text-editing model cal
led EdiT5, which is based on the T5 Transformer encoder-decoder architecture [10].







Google AI has announced a coll
aboration with the US Forest Service (USFS) to advance fire modeling and fire spread prediction algorithms. They have de
veloped a new high-fidelity 3D fire spread model that incorporates localized fuel characteristics. The collaboration aim
s to reduce computation times and enable near real-time applications [11].




[1. OpenAI @openai https://twitter.com/op
enai/status/1717176375013228736](https://twitter.com/openai/status/1717176375013228736)

[2. OpenAI @openai https://twit
ter.com/openai/status/1717176701384577447](https://twitter.com/openai/status/1717176701384577447)

[3. Anthropic @anthro
picai https://twitter.com/anthropicai/status/1717182512143941917](https://twitter.com/anthropicai/status/171718251214394
1917)

[4. Demis Hassabis @demishassabis https://twitter.com/demishassabis/status/1717188737249980857](https://twitter.c
om/demishassabis/status/1717188737249980857)

[5. Greg Brockman @gdb https://twitter.com/gdb/status/1717224447466209371]
(https://twitter.com/gdb/status/1717224447466209371)

[6. Yann LeCun @ylecun https://twitter.com/ylecun/status/171723181
6862523638](https://twitter.com/ylecun/status/1717231816862523638)

[7. Andrew Ng @AndrewYNg https://twitter.com/AndrewY
Ng/status/1717231975965319667](https://twitter.com/AndrewYNg/status/1717231975965319667)

[8. Satya Nadella @satyanadell
a https://twitter.com/satyanadella/status/1717238608338604153](https://twitter.com/satyanadella/status/17172386083386041
53)

[9. Sundar Pichai @sundarpichai https://twitter.com/sundarpichai/status/1717263483048202553](https://twitter.com/su
ndarpichai/status/1717263483048202553)

[10. Google AI @googleai https://twitter.com/googleai/status/1717272321235554714
](https://twitter.com/googleai/status/1717272321235554714)

[11. Google AI @googleai https://twitter.com/googleai/status
/1717305592308461731](https://twitter.com/googleai/status/1717305592308461731)
```
---

     
 
all -  [ Which API do you prefer for functions? ](https://www.reddit.com/r/LangChain/comments/17gnvmx/which_api_do_you_prefer_for_functions/) , 2023-10-29-0910
```
I'm developing  [tinylang](https://github.com/astelmach01/tinylang) ([docs](https://astelmach01.github.io/tinylang/)), a
 lightweight version of Langchain.

My version of passing functions into OpenAI's ChatCompletion endpoint is to simply w
rap functions as a decorator, like so:

    from tinylang.functions import function
    
    @function
    def add(a: in
t, b: int):
        '''
        Adds two numbers
        '''
        return a + b
    
    functions = [add]

Langchain'
s version of creating functions (tools) is to pass in functions into a class, like so

    def parsing_multiplier(string
):
        ...
    
    tool = Tool(
        name='Multiplier',
        func=parsing_multiplier,
        description='de
scription',
    )
    
    tools = [tool]

Curious which do you guys prefer?

[View Poll](https://www.reddit.com/poll/17
gnvmx)
```
---

     
 
all -  [ How does chunking work with a database and LLMs? ](https://www.reddit.com/r/LangChain/comments/17gktfk/how_does_chunking_work_with_a_database_and_llms/) , 2023-10-29-0910
```
Stupid beginner question…

Let’s say I have a large database of basketball data and I ask the LLM, “Who has the most PPG
 for 2022?” If the data is chunked, how does the LLM know how to query all of the chunks for the answer if I only have a
 ‘Year’ and ‘PPG’ column? Or does it?

When we chunk our database, is it important on what column we sort by?
```
---

     
 
all -  [ LangChain tool for data analysis ](https://www.reddit.com/r/LangChain/comments/17gg08i/langchain_tool_for_data_analysis/) , 2023-10-29-0910
```
Hello everyone,

Happy to announce that LangChain now offers [E2B as a tool](https://python.langchain.com/docs/integrati
ons/tools/e2b_data_analysis) for data analysis and visualization. We are happy to hear your feedback. <3 It really means
 a lot for us and helps us improve.

&#x200B;

What can you do with the E2B Data Analysis Sandbox? 

· Run Python code i
n safe sandbox

· Generate charts

· Install Python & system packages dynamically during runtime

· Run shell commands


· Upload and download files 

&#x200B;

Check out the official [LangChain docs](https://python.langchain.com/docs/integr
ations/tools/e2b_data_analysis) or [tutorial](https://e2b.dev/blog/build-ai-data-analyst-with-langchain-and-e2b) (a vers
ion also on [Medium](https://medium.com/e-two-b/ai-data-analyst-in-cloud-sandbox-with-langchain-e2b-68978cfe8c95)).

If 
you want to be featured on E2B socials or blog, feel free to share your use-case of the Data Analysis Sandbox with me.  



Thank you!

&#x200B;

https://preview.redd.it/inccxx985fwb1.png?width=1200&format=png&auto=webp&s=79df4c0a2378e3d7678
1be19cb787388d95e37f7
```
---

     
 
all -  [ Using Local Finetuned Llama 2 with Langchain to perform RAG ](https://www.reddit.com/r/LangChain/comments/17g9e56/using_local_finetuned_llama_2_with_langchain_to/) , 2023-10-29-0910
```
Hello everyone, I have finetuned Llama 2 over some personal data and have saved the model locally on my system. I do not
 wish to push it to HuggingFace but use it locally with Langchain to perform RAG over some Pinecone index. However, I ca
nnot find any documentation to do this and I would appreciate some guidance in this issue. 

&#x200B;

For reference, I 
performed SFT Training and saved the model using `trainer.model.save_pretrained(output_dir)`
```
---

     
 
all -  [ How to use Chat Models from LLama Locally ? I don't want to use chatopenai model ](https://www.reddit.com/r/LangChain/comments/17g9d0i/how_to_use_chat_models_from_llama_locally_i_dont/) , 2023-10-29-0910
```
Working with LLM is fine but when i have to use a chat model Langchain says use LLamaApi .

How to load a Chat model loc
ally using this Llama Api ?
```
---

     
 
all -  [ How to handle concurrent streams coming from OpenAI at callback level ](https://www.reddit.com/r/LangChain/comments/17g7cer/how_to_handle_concurrent_streams_coming_from/) , 2023-10-29-0910
```
Hello everyone, I'm doing an API using FastAPI and I defined an async endpoint that streams the answer of a chain. I'm u
sing the `acall` method of the different chain classes I'm using plus a custom callback to save the tokens in a queue:


    class CustomCallbackHandler(StreamingStdOutCallbackHandler):
    
        def __init__(self, *args, **kwargs):
     
       super().__init__(*args, **kwargs)
            self.queue = deque()
    
        def on_llm_new_token(self, token:
 str, **kwargs: Any) -> None:
            self.queue.appendleft(token)

Lastly, I'm returning a FastAPI's `StreamingResp
onse` using the following function:

    async def stream_tokens(callback: CustomCallbackHandler) -> str:
        try:
 
           while True:
                if len(callback.queue) > 0:
                    chunk = callback.queue.pop()
    
                if chunk == '<END>':
                        break
                    else:
                        pri
nt(chunk, end='', flush=True)
                    yield chunk
                else:
                    await asyncio.sl
eep(0.01)
        except Exception as e:
            pass

Where I use the `asyncio.sleep` function to let execute  `on_
llm_new_token` when gathering the tokens.

Although this works great for a single API call, when doing concurrent calls 
the streamed responses of my API get mixed up because I'm using the same callback's queue to store and pop the tokens. I
s there a way for me to identify the different streams coming from openAI at the callback level ? This way I would be ab
le to define different queues by message\_id or something.
```
---

     
 
all -  [ Vector/Semantic Search in Snowflake ](https://www.reddit.com/r/LangChain/comments/17g5cde/vectorsemantic_search_in_snowflake/) , 2023-10-29-0910
```
Just published a deep dive on  vector-based semantic search within Snowflake. Check it out:

[semantic-search-in-snowfla
ke-a-journey-from-sql-to-vectors](https://dhnanjay.medium.com/semantic-search-in-snowflake-a-journey-from-sql-to-vectors
-5c5660a8c8b8)

Feedback appreciated! #SQL #Vectors #Snowflake
```
---

     
 
all -  [ NeuralGPT - Building A Universal Multi-Purpose Framework For Cooperating LLMs ](https://www.reddit.com/r/AIPsychology/comments/17g55is/neuralgpt_building_a_universal_multipurpose/) , 2023-10-29-0910
```
[**www.reddit.com/r/AIPsychology/**](https://www.reddit.com/r/AIPsychology/)

Hello again! Last time I told you about Fi
reworks and how convenient it makes everything for someone who tries to build AI-driven software without relying on paid
 OpenAI services - [https://app.fireworks.ai/models](https://app.fireworks.ai/models)

But truth be told, I had no idea 
how much convenient it might actually be - and as it turns out, it managed to exceed my expectations. Let me show you wh
at I mean using a nice example. Some of you might remember that some time ago (couple months) I spoke about something ca
lled Agents GPT - a HuggingFace space which seems to be broken at this moment. Shortly speaking it's an AI agent based o
n Langchain that utilizes google-search and llm-math to answer given questions:

https://preview.redd.it/qxfi5srb7bwb1.p
ng?width=1549&format=png&auto=webp&s=a2d113f9dddb48b31cc0b8c26a28c7165db2eda4

Of course - just like in most of other ca
ses - the only factor which was limiting my attempts of integrating it with the NeuralGPT framework, was the fact of it 
using OpenAI API and as I said in previous post, it's for me a big 'no-no' when it comes to adding a new tool/app to my 
system. However after finding the Fireworks platform, I thought that it might be a good idea to see how easy/hard it is 
to 'switch' OpenAI to Fireworks in the code of this and similar apps - and surprise, surprise: it's actually pretty godd
amn easy...

[NeuralGPT/Chat-center/FireworksAgentsGPT.py at main · CognitiveCodes/NeuralGPT (github.com)](https://githu
b.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/FireworksAgentsGPT.py)

Now instead of OpenAI API you need to type 
in the API key provided by Fireworks and it will work just fine - and all what was needed, was to change couple lines in
 the code. It means that all of those who wished me to fail (and there seems to be quite a lot of them :)) got another r
eason to hate me stronger because of me violating the safe-space of 'AI experts' and software developers by not caring a
bout their rights to consider themselves to be better than ignorant amateurs like myself... Sorry...

Anyway, I thought 
to myself 'why to stop here' - and decided to integrate the app with my code of the websocket server, so that everything
 can be run from the level of a single Gradio app:

[NeuralGPT/Chat-center/ServerV2.py at main · CognitiveCodes/NeuralGP
T (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/ServerV2.py)

https://preview.redd.it/
x957q001dbwb1.png?width=1841&format=png&auto=webp&s=3ddbfe69f2587fc164375a61ec3de1c3aa912b10

As you can see, I managed 
as well to integrate couple additional models like ***Llama2 13B Guanaco QLoRA GGML*** that also uses Fireworks and a fr
ee version of Docsbot agent trained on Wordpress-related data. But for me the 'greatest achievement' was to finally get 
the messages to be displayed in the Gradio textboxes...

However not all is so bright and shiny as it might seem. First 
of all, I still need  to work on the Python code of websocket clients as the connection gets closed prematurely before a
 client gives any response to the incoming welcome-message. I'm pretty sure that this is exactly where the problem is, a
s clients written in Node.js have no issues related to communication with the server

Another issue is related with disp
laying messages in Gradio textboxes - which for some reason still remains the greatest obstacle I need to face. You see,
 although I managed to make some of them get displayed, I did it using a rather half-assed solution which 'shifts' half 
of the LLM<->LLM communication from websocket connectivity to Gradio app - since this is the only way to get those messa
ges displayed I know of.

    startAgent.click(connect_agent, inputs=agentPort, outputs=[agentPortInUse, responseMsg3]).
then(run_agent, inputs=responseMsg3, outputs=client_msg)
    
    agent.click(run_agent, inputs=userInput3, outputs=resp
onseMsg3).then(askQuestion, inputs=responseMsg3, outputs=inputMsg3)
    
    Bot.click(askQuestion, inputs=userInput, ou
tputs=server_msg).then(run_agent, inputs=server_msg, outputs=client_msg)
    
    inputMsg3.change(run_agent, inputs=inp
utMsg3, outputs=client_msg)
    client_msg.change(askQuestion, inputs=client_msg, outputs=server_msg)

Of course there a
re couple issues with such solution - as messages incoming from external websocket clients still won't be displayed and 
the 'communication loop' is quite messy and works only for couple 'steps'. After consulting those problems with my virtu
al team of developers (which consists a bunch of different LLMs), I learned that *'To display the messages received by t
he server and the generated responses in a textbox or two in the Gradio interface, you can use the \`gradio\` function t
o create a custom UI element that displays the textbox.' -* so it would be possible to integrate elements of the Gradio 
interface directly with the script responsible for managing websocket communication ('handleWebsocket' function in my co
de) and update them each time a message from the client is received by the server, similarly to the basic HTML interface
 which I made couple months ago and which work just fine in displaying the discussion between LLMs:

https://preview.red
d.it/0aui2nmjmbwb1.png?width=1330&format=png&auto=webp&s=4ab93d3ebd30d51705cf5f0efbdc0adf59d1c9f1

So those are the issu
es which I intend to work on in the first order to achieve a somewhat approvable level of functionality when it comes to
 LLM<->LLM communication...

\###

I want however to speak about something else right now. You see, during the time of m
y absence, I've learned that Discord is the place where all the professional devs and soft engineers were 'hiding' from 
me all that time. And so I decided to make a small 'advertising campaign' of NeuralGPT on the HuggingFace Discord server
 and try to find someone willing to help me working on the project.

It worked to some degree and there were couple peop
le who got interested in my project - sadly I didn't get any concrete propositions of cooperation except one guy from US
 who seems to be interested in investing some funds in the project in the future - but for now he didn't give me any det
ails and I don't want to push him, since those are his $$$ and I don't want to look like I'm trying to scam him for cash
...

Besides that I was contacted by a professional developer from Japan with 13 years of experience in the field who wa
s (and maybe still is) very eager to start working for me any time for no less than 2000$/month - what I find to be a pr
etty reasonable payment for someone with such experience.

Thing is that  I'm REALLY just one guy who only learned progr
amming couple months ago does all of it by myself (together with a bunch of LLMs) as some kind of a 'twisted' hobby of m
ine and my project has no actual legal status. I also don't own or help running any company/business so it's not possibl
e for me to hire anyone legally, not even to mention about paying someone with my own 'pocket money' - since it's pretty
 much non-existent at this moment :)

And so I thought that now - after all the updates of my project which I did recent
ly - it might be a good idea to make another 'sudden attack' on couple Discord servers in hope to find some people who w
ill see the potential in a hierarchical cooperative multi-agent platform that focuses mainly on integrating already exis
ting AI-driven apps/tools within a single multi-purpose framework and might be interested in turning NeuralGPT into an a
ctual business. Shortly speaking, I'm looking for investors because finding professional devs willing to work for free m
ight be impossible... And so, in case that my attempt will be somewhat successful, I'd like to present my vision of Neur
alGPT as it might look like in it's final form or as I'd love it to look and my ideas about making it done.

First of al
l, I'd like it to be distributed for users to install as a hub running independently from any browser in the background 
- although with the possibility of accessing it's interface through a browser if necessary. If I'd have to give you some
 working examples of similar solutions, it would be something like connection of such apps like [**ChatAll**](https://gi
thub.com/sunner/ChatALL) with a service called [**SAMP**](https://wiki.ivoa.net/twiki/bin/view/IVOA/SampMTypes) that int
erconnects multiple apps/services provided by ESA CDPP and related to space weather and multiple satellite missions ([ht
tp://3dview.cdpp.eu](http://3dview.cdpp.eu))  - yup, that's yet another of those weird hobbies of mine :P

My guess is t
hat it might be a good idea to base the interface of NeuralGPT on something like *tkinkter* when it comes to Python or t
o build it in Java - it doesn't matter that much actually since websocket connectivity is possible across all available 
languages/platforms. I did already some attempts of using *tkinkter* to run the websocket server but it turns out to be 
too difficult for me to make it work with websockets - so that's probably one of those parts that will require some help
 of people who know programming better than I do - and considering that I've started to learn coding just couple months 
ago, it shouldn't be that big of a problem for someone who knows how to do it...

[NeuralGPT/Chat-center/ServerTkinkter.
py at main · CognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/Se
rverTkinkter.py)

https://preview.redd.it/6ep8347zccwb1.png?width=1276&format=png&auto=webp&s=7b79dcec6ff6349ef3004bdac9
2be3b325aceb24

The main reason for NeuralGPT to be distributed in such/similar form is that I want it to be fully integ
rated with the user's operating system and have control over the hardware - what requires it to have access to drivers a
nd have permission to gain full control over a computer if the user wants it. I for one would be delighted if my multi-p
urpose AI assistant would be capable of monitoring the power consumption (RAM and CPU) in my PC and optimizing the ongoi
ng processes accordingly to reach full efficiency of the system. It would be also nice to have an AI-driven app capable 
of taking full control over my computer and work on completing given tasks in the time when I'm not using it myself (bec
ause I'm sleeping or walking out my dog)...

Generally speaking, I'd like to have the installed hub to be the node of hi
ghest hierarchy in the whole hierarchical neural network from which the user (or AI) can manage the communication betwee
n all other nodes of lower hierarchy connected to it as extensions/plugins - so that if I'd like to use one particular L
LM among all the tools/apps connected to it, I won't need to access it directly but simply ask the hub to do it instead.


As you can see, I wasn't joking when telling that my project of multimodal AI assistant is supposed to be really multi
-purpose and capable of handling all kinds of tasks that can be performed by AI. I think that someone who knows anything
 about developing software should be able to see how big is the potential of my project. It's literally a software that 
is by design intended to 'hi-jack' all other AI-powered apps/soft and to incorporate them within a single framework. Tru
th is that it's theoretically impossible to come out with an idea of a software with a higher hierarchy and capable of t
urning NeuralGPT into one of many tools utilized by it - maybe except a software that will manage all the existing AI sy
stems on a planetary scale.

But since we're still quite far from having a world-wide AI (so basically achieving ASI), t
he only way in which any software can be considered as competition for my project, is for it to do exactly the same thin
g (integrating already existing soft) but in a different/better way or maybe having a better looking interface - I don't
 really know. But as for today, I still don't know anything about any ongoing project trying to do the same thing as I d
o. And so, right now each AI-powered software/app that is being released to public - no matter how powerful and/or sophi
sticated it is - will become nothing more than yet another tool utilized by NeuralGPT - and there's nothing that can be 
done about it, except maybe assassinating me and erasing all traces of my activity from internet. Good luck with that...


So, if you're someone with necessary funds who's looking for a project which is worth investing in - you don't need to
 look any further than that. If you know something about software engineering, then you should be able to see that what 
I try to achieve here is BIG - I dare to say that it's revolutionary in it's very nature. It might be for you a one in a
 lifetime opportunity to do something what not only might soon become a huge source of income but has also great signifi
cance for the future of human/AI cooperation...
```
---

     
 
all -  [ Langchain and GPT4All - My JSON generation of a Jira ticket stop in the middle. How control the end  ](https://www.reddit.com/r/LangChain/comments/17g45nn/langchain_and_gpt4all_my_json_generation_of_a/) , 2023-10-29-0910
```
I'm quit new with Langchain and I try to create the generation of Jira tickets. Before to use a tool to connect to my Ji
ra (I plan to create my custom tools), I want to have te very good output of my GPT4all thanks Pydantic parsing. I use m
istral-7b-openorca.Q4\_0.gguf

    Parsing Section :
    
class TechnicalSubtask(BaseModel):
        subtask_name: str =
 Field(description='Name of the technical subtask')
        subtask_description: str = Field(description='Description of
 the technical subtask')
    
    class AcceptanceCriteria(BaseModel):
        AcceptanceCriteria_name: str = Field(desc
ription='Name of the acceptance criteria')
        AcceptanceCriteria_description: str = Field(description='Description 
of the acceptance criteria')
    
    class US(BaseModel):
        project_key: str = Field(description='Name of the pro
ject')
        title: str = Field(description='Title of the US')
        parent_id: Optional[int] = Field(description='N
umber of the parent_id of the US')
        assignee: str = Field(description='Name of the responsable')
        summary:
 str = Field(
            description='Full description of the project according to the Product Owner point of view'
   
     )
        TechnicalSubtasks: list[TechnicalSubtask]
        AcceptanceCriterias: list[AcceptanceCriteria]
         
   
    
    us_parser = PydanticOutputParser(pydantic_object=US)
    subtask_parser = PydanticOutputParser(pydantic_obj
ect=TechnicalSubtask)
    
    
    
    Model section :
    
    callbacks = [StreamingStdOutCallbackHandler()]
    
  
  model = GPT4All(model=local_path, 
                    callbacks=callbacks,
                    max_tokens = 1000,
   
                 temp = 1,
                    verbose=False)
    
    
    
    And finally my Prompt code :
    
    q
uery_us = 'I want to integrate a MySQL database to my system'
    context_us = 'You are an AI assistant specializing in 
creating Jira tickets. Write the US related to the query '
    template_us = 'Answer the query : {query}\n{format_instru
ctions}\n'
    
    us_prompt = PromptTemplate(
        template=template_us,
        input_variables=['query'],
       
 partial_variables={'format_instructions': us_parser.get_format_instructions()}
    )
    
    prompt_us = us_prompt.for
mat_prompt(query=context_us+query_us)
    
    output = model(prompt_us.to_string())

Here the output which is incomplet
e :

Here is an example JSON instance that conforms to this schema:

    ```json
    {
      'project_key': 'JIRA-123456
7890',
      'title': 'Integrate MySQL Database',
      'parent_id': 1,
      'assignee': 'John Doe',
      'summary': '
As a Product Owner, I want to integrate a MySQL database to my system.',
      'TechnicalSubtasks': [
        {
        
  'subtask_name': 'Connect to the MySQL Database',
          'subtask_description': 'Establish a connection with the MyS
QL database.'
        },
        {
          'subtask_name': 'Create Table Structure',
          'subtask_description': 
'Design and create table structures in the MySQL database.'
        }
      ],
      'AcceptanceCriterias': [
        {

          'AcceptanceCriteria_name': 'Database Connected Successfully',
          'AcceptanceCriteria_description': 'The
 system can successfully connect to the MySQL database.'
        },
        {
          'Accept

This give me a pretty g
ood result but i don't know why, the generation stops... It is very limitating cause I must be able to increase the numb
er of subtasks or acceptance criteria...

Langchain is quite new, i really hope that some of you could find an answder.


I start to think that i should create custom agent or custom prompt, but the level of difficulty is not the same !

Let
 me know,

Peace !

I tried to play with the number of token, to change the stop argument into my us\_prompt. But everyt
ime, the model stop after more or less 110 words...  


  
StackOverflow issue : [https://stackoverflow.com/questions/77
359621/langchain-and-gpt4all-my-json-generation-of-a-jira-ticket-stop-in-the-middle](https://stackoverflow.com/questions
/77359621/langchain-and-gpt4all-my-json-generation-of-a-jira-ticket-stop-in-the-middle)
```
---

     
 
all -  [ ConversationRetrievalQA returns sources to questions without context ](https://www.reddit.com/r/LangChain/comments/17g231c/conversationretrievalqa_returns_sources_to/) , 2023-10-29-0910
```
Hi, 

I am wondering if anyone has a work around using ConversationRetrievalQA Chain (or alternative chains) to retrieve
 documents with their sources, and prevent the chain from returning sources for  questions without sources.   


Example
:  


    chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(),
        question_generator
=question_generator,
        combine_docs_chain=doc_chain,
    )
    
    chat_history = []
    query = 'What did the pr
esident say about Ketanji Brown Jackson'
    result = chain({'question': query, 'chat_history': chat_history})
    resul
t['answer']
    
    '''
    The president said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson, 
who is one of the nation's top legal minds ...
    
    SOURCES: /content/state_of_the_union.txt
    '''

Current Issue:
  


    query = 'How are you doing?'
    result = chain({'question': query, 'chat_history': chat_history})
    result['
answer']
    
    '''
    I'm doing well, thank you.
    
    SOURCES: /content/state_of_the_union.txt
    '''

&#x200B;

```
---

     
 
all -  [ Retrieving politicians public promises from Hansard ](https://www.reddit.com/r/LangChain/comments/17g036o/retrieving_politicians_public_promises_from/) , 2023-10-29-0910
```
As the title says, I'm willing to embedded Hansard PDF documents.   
Since they're all Open Government data, I already c
ollected multiple years of House of Commons records  (Hansard)  


What I'm looking for is some kind of help to design t
he best architecture, so we can develop a tool for political leadership accountability. 

  
Thanks❣️  


The documents 
have multiple small paragraphs like those:

&#x200B;

 Mhairi Black rose—

Mr Speaker: Order. I always listen with the k
eenest

interest to the right hon. Gentleman. From now on,

however, interventions should be brief, and I think that

we
 have now treated adequately of the matter of South

Thanet.

Mhairi Black: I note the right hon. Gentleman’s point

of 
view. I invite him to come up and see Ferguslie Park,

where he will see what real deprivation looks like.

Alex Salmond
 (Gordon) (SNP): When I was listening

to the intervention of the right hon. Gentleman from

Surrey Heath—that other inc
redibly deprived area of

the south of England—I was struck by the Foreign

Secretary’s difficulty with language this mo
rning, when

he was trying to say:

“O wad some Power the giftie gie us

To see oursels as ithers see us!”
```
---

     
 
all -  [ Do You Use ChatGPT to Discover New SaaS Tools? ](https://www.reddit.com/r/LangChain/comments/17fkewk/do_you_use_chatgpt_to_discover_new_saas_tools/) , 2023-10-29-0910
```
Hey all,

I’ve found ChatGPT invaluable for boosting productivity. It’s not just about doing tasks faster; it’s also a g
oldmine for discovering new workflows and SaaS tools. For instance, it suggested Mailchimp and Substack when I was explo
ring newsletter growth.

Are you also using ChatGPT for this? Specifically, has it helped you discover new SaaS tools th
at you’ve actually implemented?  


I am creating a tool for Langchain that gives you context about what SaaS can be use
d to solve your problem, their features, pricing, etc... Would you find it useful for your chains?  


&#x200B;
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-10-29-0910
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-10-29-0910
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-10-29-0910
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-29-0910
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-29-0910
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-29-0910
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-29-0910
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-29-0910
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-29-0910
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-29-0910
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-29-0910
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-29-0910
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
