 
all -  [ Chatbot using langchain and streamlit ](https://www.reddit.com/r/pythonhelp/comments/16wluyk/chatbot_using_langchain_and_streamlit/) , 2023-10-01-0911
```
Hi everyone! 
I am creating a chatbot using langchain and streamlit 
I am using python version 3.10.1. 
My code was runn
ing fine until the moment I have added langchain library it gives me an error  module not found. 
The code goes as follo
ws: 

```
import streamlit as st
from st_chat_message import message
from dotenv import load_dotenv
import os

from lang
chain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)



def init():
    #Load the OpenAI API key 
    load_dotenv()
    
    #Check if the API key exists
    if os.getenv('OP
ENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print('OPENAI_API_KEY is not set')
        exit(1)

    else:
        print('OPENAI_API_KEY is set')

    #streamlit page
    st.set_page_config(
        page_title='Your o
wn ChatGPT',
        page_icon='🤖'
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    #messages h
istory
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(conten
t='You are a helpful assistant.')
        ]

    st.header('Your Bot 🤖')

    #sidebar with user input
    with st.sideb
ar:
        user = st.text_input('Enter your message: ', key='user_input')

        #user input
        if user:
       
     st.session_state.messages.append(HumanMessage(content=user))
            with st.spinner('Thinking...'):
          
      response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessage
(content=response.content))
```


I am getting the following errors: 
No module named 'langchain.chat_models'
And also 

No module named ‘langchain.schema’


If anyone could help by giving me their guidance and solution to this, I would be s
o grateful. 

Thank you
```
---

     
 
all -  [ Can't tell why the Llama 2 is running on the GPU ](https://www.reddit.com/r/LocalLLaMA/comments/16wgn01/cant_tell_why_the_llama_2_is_running_on_the_gpu/) , 2023-10-01-0911
```
I am new to running models locally. Recently I downloaded  llama-2-13b-chat.ggmlv3.q6\_K.bin

***My PC params:***

|**GP
U**|Nvidia GeForce 3090|
|:-|:-|
|**Processor**|AMD Ryzen Threadripper 3970X 32-Core Processor, 3901 Mhz, 32 Core(s), 64
 Logical Processor(s)|
|**Motherboard**|ROG STRIX TRX40-E GAMING|
|**RAM**|256GB 3400 Mhz|
|**OS**|Microsoft Windows 11 
Pro / Version	10.0.22621/ Build 22621|

&#x200B;

***Steps taken so far:***

1. Installed CUDA
2. Downloaded and placed 
llama-2-13b-chat.ggmlv3.q6\_K.bin
3. Ran in the prompt
4. Ran the following code in PyCharm

&#x200B;

    from langchai
n.llms import LlamaCpp
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    fr
om langchain.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdO
utCallbackHandler
    
    
    template = '''Question: {question}
    
    Answer: You are a chief data officer.'''
   
 
    prompt = PromptTemplate(template=template, input_variables=['question'])
    
    # Callbacks support token-wise s
treaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    
    n_gpu_layers = 30  # C
hange this value based on your model and your GPU VRAM pool.
    n_batch = 2048  # Should be between 1 and n_ctx, consid
er the amount of VRAM in your GPU.
    
    # Make sure the model path is correct for your system!
    llm = LlamaCpp(
 
       model_path=r'///PycharmProjects\llama_chat\llama-2-13b.Q6_K.gguf',
        n_gpu_layers=n_gpu_layers,
        n_b
atch=n_batch,
        callback_manager=callback_manager,
        verbose=True, # Verbose is required to pass to the call
back manager
    )
    
    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = 'What is data governance?'

    llm_chain.run(question)
    
    question = 'What is data governance?' llm_chain.run(question)

***Partial Output:**
*

    llama_model_loader: - type  f32:   81 tensors
    llama_model_loader: - type q6_K:  282 tensors
    llm_load_prin
t_meta: format           = GGUF V2 (latest)
    llm_load_print_meta: arch             = llama
    llm_load_print_meta: v
ocab type       = SPM
    llm_load_print_meta: n_vocab          = 32000
    llm_load_print_meta: n_merges         = 0
  
  llm_load_print_meta: n_ctx_train      = 4096
    llm_load_print_meta: n_embd           = 5120
    llm_load_print_meta:
 n_head           = 40
    llm_load_print_meta: n_head_kv        = 40
    llm_load_print_meta: n_layer          = 40
   
 llm_load_print_meta: n_rot            = 128
    llm_load_print_meta: n_gqa            = 1
    llm_load_print_meta: f_no
rm_eps       = 0.0e+00
    llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
    llm_load_print_meta: n_ff             = 1
3824
    llm_load_print_meta: freq_base_train  = 10000.0
    llm_load_print_meta: freq_scale_train = 1
    llm_load_prin
t_meta: model type       = 13B
    llm_load_print_meta: model ftype      = mostly Q6_K
    llm_load_print_meta: model pa
rams     = 13.02 B
    llm_load_print_meta: model size       = 9.95 GiB (6.56 BPW) 
    llm_load_print_meta: general.nam
e   = LLaMA v2
    llm_load_print_meta: BOS token = 1 '<s>'
    llm_load_print_meta: EOS token = 2 '</s>'
    llm_load_p
rint_meta: UNK token = 0 '<unk>'
    llm_load_print_meta: LF token  = 13 '<0x0A>'
    llm_load_tensors: ggml ctx size = 
   0.12 MB
    llm_load_tensors: mem required  = 10183.83 MB
    .......................................................
.............................................
    llama_new_context_with_model: n_ctx      = 512
    llama_new_context_w
ith_model: freq_base  = 10000.0
    llama_new_context_with_model: freq_scale = 1
    llama_new_context_with_model: kv se
lf size  =  400.00 MB
    llama_new_context_with_model: compute buffer total size = 80.88 MB
    AVX = 1 | AVX2 = 1 | AV
X512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0
 | BLAS = 0 | SSE3 = 1 | SSSE3 = 0 | VSX = 0 | 
    
    In the past, companies have focused...
    
    ...Data governa
nce is a set of policies and procedures for managing the use of data across an organization. The goal is to ensure that 
all employees have access to the right information at the right time
    
    llama_print_timings:        load time =  2
039.44 ms
    llama_print_timings:      sample time =    57.80 ms /   256 runs   (    0.23 ms per token,  4428.84 tokens
 per second)
    llama_print_timings: prompt eval time =  2039.40 ms /    20 tokens (  101.97 ms per token,     9.81 tok
ens per second)
    llama_print_timings:        eval time = 49202.92 ms /   255 runs   (  192.95 ms per token,     5.18 
tokens per second)
    llama_print_timings:       total time = 51984.77 ms

***Problem:***

When I run the code the CPU 
is clearly being utilized but not the GPU:

https://preview.redd.it/pva0inwo6grb1.png?width=1143&format=png&auto=webp&s=
d1b635bf9db16e44a7a2594012868f0810dca6f0
```
---

     
 
all -  [ Custom local agent strategies ](https://www.reddit.com/r/LocalLLaMA/comments/16wcypn/custom_local_agent_strategies/) , 2023-10-01-0911
```
I’ve been playing around a a lot with langchain and llama models on my M1 Max.

After learning in python, I switched ove
r to node + typescript since that’s my area of expertise. I have a web server that I’ve been using to run test prompts a
nd inputs for various kinds of problems, and I’ve even successfully connected it to Siri with a loop to have a continuou
s conversation with custom memory and a vector store.

My goal is to create a mostly local set of tools that can help me
 do my job as a tech lead and organize my busy life in ways that current tools can’t.

I’ve had success with models bein
g able to categorize between questions, commands, facts, and reminders/todos, and sometimes even splitting compound requ
ests into their parts. I’ve been trying to break down what amounts to agent features into smaller and simpler parts so t
hat current local llms can handle the tasks. Rather than using the prebuilt conversation tools or agents, I have to writ
e them my self and rely less on llms for larger more complicated prompts.

I’m struggling a lot with good json output, a
nd figuring out how to break down multi step commands that mimicking agents. Routing seems to go well as long as you kee
p categorization simple.

What are thoughts on making more calls to limited llms and how to achieve better planning and 
structured output?

What seem to be the best local llms 7-34b for instruct tasks and JSON output?
```
---

     
 
all -  [ Speaking the llm_chain() result ](https://www.reddit.com/r/LangChain/comments/16w8lrz/speaking_the_llm_chain_result/) , 2023-10-01-0911
```
Hey guys , i been making this stuff and i want to speak the word as it generates with llm\_chain(question) , but i been 
trying it , close to what i got is , first it generates and then i put it in a variable and then speak the message with 
pyttsx3 , is there a way that i can speak every word that is being generated?  


here is the code   


 

prompt = Prom
ptTemplate(template=template2, input\_variables=\['chat\_history','question'\])  
callback\_manager = CallbackManager(\[
StreamingStdOutCallbackHandler()\])  
n\_gpu\_layers = 100   
n\_batch = 1024   
llm = LlamaCpp(  
 model\_path='./model
s/llama-2-7b-chat.gguf.q4\_0.bin',  
 n\_gpu\_layers=n\_gpu\_layers,  
 n\_batch=n\_batch,  
 callback\_manager=callback
\_manager,  
 verbose=False, # Verbose is required to pass to the callback manager  
)  
llm\_chain = LLMChain(prompt=pr
ompt, llm=llm, memory=ConversationBufferMemory(memory\_key='chat\_history'))  
while True:  
 question = input('\\n')  

 response = llm\_chain(question)  
 print(response\['text'\])
```
---

     
 
all -  [ LangChain Crash Course freeCodeCamp ](https://www.reddit.com/r/LangChain/comments/16w81cz/langchain_crash_course_freecodecamp/) , 2023-10-01-0911
```
My LangChain Crash course just released yesterday on freeCodeCamp’s YouTube.

I cover some basic but important concepts 
within the LangChain framework.

https://youtu.be/lG7Uxts9SXs?si=HYacT18bfM2eYuKh
```
---

     
 
all -  [ What is the best strategy to compare the products ](https://www.reddit.com/r/LangChain/comments/16w1uzs/what_is_the_best_strategy_to_compare_the_products/) , 2023-10-01-0911
```
Guys, I have one requirement i have different models if cars in pdf . After pre processing, the information stored acros
s the different indices. If i want compare the model A and model B, how can retrieve both the information and compare my
 qurey will be ”compare the mileage of car A and car B”
```
---

     
 
all -  [ What are good langchain alternatives to train LLMs and create LLM apps? ](https://www.reddit.com/r/LocalLLaMA/comments/16vy6aw/what_are_good_langchain_alternatives_to_train/) , 2023-10-01-0911
```
Magentic, minichain, llfn <--- I saw these three but haven't tried them yet except for langchain. Which one do you use t
o rapid prototype LLMs currently?
```
---

     
 
all -  [ MistralAi LLM with Langchin ](https://www.reddit.com/r/LangChain/comments/16vwilm/mistralai_llm_with_langchin/) , 2023-10-01-0911
```
Is Langchain supporting Mistral AI LLM model ?
```
---

     
 
all -  [ Guys I need your help with this: My SQL langchain agent seems to be limiting its answers to 10 rows ](https://www.reddit.com/r/LangChain/comments/16vkve1/guys_i_need_your_help_with_this_my_sql_langchain/) , 2023-10-01-0911
```
My data is in MySQL in the form of a database, containing two tables, 1000 rows and 50 rows. 

I have created a sql agen
t:

 agent = create\_sql\_agent(   

llm=llm,

toolkit=toolkit,

verbose=True,

agent\_type=AgentType.ZERO\_SHOT\_REACT\
_DESCRIPTION,

  )

Then, when I am passing in a query, e.g. List all the trials conducted in Berlin, Germany, my agent 
queries only the first 10 rows. In this case, it returns all the trials conducted in Berlin within the first ten rows. I
 looked into the SQL query it is generated and it has a 'limit 10' command included, which I do not want. 

How do I get
 my agent to query through all the rows of the table, not limiting to 10?

&#x200B;
```
---

     
 
all -  [ Pdf Document preprocessing ](https://www.reddit.com/r/LangChain/comments/16vf12c/pdf_document_preprocessing/) , 2023-10-01-0911
```
I’m wondering if I have a set of complex pdf documents containing paragraph and tables, whether the langchain document l
oader is enough to load all the documents in a nice way and giving a good retrieval performance?
```
---

     
 
all -  [ Would like some help as someone with no coding background. ](https://www.reddit.com/r/OpenAIDev/comments/16vap8r/would_like_some_help_as_someone_with_no_coding/) , 2023-10-01-0911
```
Hey!

As a little project I am trying to build a knowledge base/chatbot to aks it law related questions. But I am gettin
g a bit stuck as I am getting told I have reached the current quota. I don't know how I could solve this. I will leave m
y code below. help would be appreciated!  


 

\# Import necessary libraries  
import streamlit as st  
from langchain.
document\_loaders import TextLoader  
from langchain.vectorstores import FAISS  
from langchain.embeddings.openai import
 OpenAIEmbeddings  
from langchain.prompts import PromptTemplate  
from langchain.chat\_models import ChatOpenAI  
from 
langchain.chains import LLMChain  
from dotenv import load\_dotenv  
import os  
load\_dotenv()  
\# Load your tax-relat
ed text documents  
\# Fetch your OpenAI API key from environment variables  
openai\_api\_key = os.getenv('OPENAI\_API\
_KEY')  
\# Create an instance of TextLoader with the file paths  
text\_loader = TextLoader('D:/My-Space/tax\_laws.txt'
)  
\# Load your tax-related text documents  
documents = text\_loader.load()  
\# Vectorize the documents using LangCha
in and create an index with FAISS  
embeddings = OpenAIEmbeddings()  
db = FAISS.from\_documents(documents, embeddings) 
 
\# Define a Streamlit app  
def main():  
 st.title('Tax Chatbot')  
 \# Create an input box for user queries  
 user\
_query = st.text\_input('Ask a tax-related question')  
 if user\_query:  
 \# Perform similarity search in the knowledg
e base  
 similar\_responses = db.similarity\_search(user\_query, k=3)  
 \# Initialize LangChain  
 llm = ChatOpenAI(te
mperature=0, model='gpt-3.5-turbo-0613')  
 \# Define a template for generating responses  
 template = '''  
You asked:
 {user\_query}  
Here is some information about the tax-related question:  
 {tax\_info}  
'''  
 prompt = PromptTemplat
e(input\_variables=\['user\_query', 'tax\_info'\], template=template)  
 chain = LLMChain(llm=llm, prompt=prompt)  
 \# 
Generate responses based on retrieved documents  
 for response in similar\_responses:  
 tax\_info = response.page\_con
tent  
 st.write(chain.run(user\_query=user\_query, tax\_info=tax\_info))  
if \_\_name\_\_ == '\_\_main\_\_':  
 main()
  


&#x200B;
```
---

     
 
all -  [ I created an Open-source framework to optimize and eval RAG embeddings - Vectorboard ](https://www.reddit.com/r/LangChain/comments/16va3v9/i_created_an_opensource_framework_to_optimize_and/) , 2023-10-01-0911
```
Hi everyone, I just released the first version of Vectorboard, an open-source framework to do hyperparameter searches fo
r embeddings. 

There are many algorithms, and deciding the right chunk size, overlap, and splitting methods is quite ch
allenging. With Vectorboard, you can do a grid search and compare the performance of different methods and parameters th
at are best for your data.

It's in the alpha version and I'd love to hear your feedback: [https://vectorboard.ai/](http
s://vectorboard.ai/)

Github: [https://github.com/Vectorboard/Vectorboard](https://github.com/Vectorboard/Vectorboard) 


Documentation: [https://docs.vectorboard.ai/](https://docs.vectorboard.ai/)
```
---

     
 
all -  [ I made a web app for chatting with all the content related to Confluence Space using Langchain. ](https://www.reddit.com/r/LangChain/comments/16v7wt2/i_made_a_web_app_for_chatting_with_all_the/) , 2023-10-01-0911
```
**Title:** How to Automatically Generate Embeddings for Updated Documents in a Confluence Space and Enable Real-Time Que
stion Answering on the Updated Data?

**Body:** I'm currently working on accessing a Confluence space using Langchain an
d performing question answering on its data. The embeddings of this data are stored in a Chromadb vector database once I
 provide user name,API keyand Space key.  
 However, I'm looking for a way to automatically generate embeddings for any 
documents that change in real-time within the Confluence space and enable real-time question answering on the updated da
ta. Any suggestions or solutions on how to achieve this would be greatly appreciated!
```
---

     
 
all -  [ If Vectorstores only store the data of the documents you upload, how do you prompt the LLM to emulat ](https://www.reddit.com/r/LangChain/comments/16uqvop/if_vectorstores_only_store_the_data_of_the/) , 2023-10-01-0911
```

```
---

     
 
all -  [ Distributed System for syncing and ingesting billions of text embeddings ](https://www.reddit.com/r/LangChain/comments/16uq23b/distributed_system_for_syncing_and_ingesting/) , 2023-10-01-0911
```
Hey folks!

Decided to share some inner workings of our architectural diagram for how we are syncing and ingesting billi
ons of text embeddings at scale into vector database (specifically weaviate!) - under the hood it leverages LangChain fo
r some of its pre-processing mechanisms!

[Retrieval Augmented Generation at scale — Building a distributed system for s
ynchronizing and ingesting billions of text embeddings | by Neum AI | Sep, 2023 | Medium](https://medium.com/@neum_ai/re
trieval-augmented-generation-at-scale-building-a-distributed-system-for-synchronizing-and-eaa29162521)
```
---

     
 
all -  [ How to store tool output in agent memory along with chat history? ](https://www.reddit.com/r/LangChain/comments/16ukfac/how_to_store_tool_output_in_agent_memory_along/) , 2023-10-01-0911
```
I'm new to LangChain, and recently setup an agent ('chat-conversational-react-description') with a custom tool to search
 a database of academic papers. The agent successfully uses the tool and accesses the output when asked to preform a sea
rch. However, I'd like to store the full output of the tool in the agent's memory, so I can ask additional questions abo
ut the results, but can't figure out how to achieve this. 

Current behavior of my agent: 

Me: Please search for recent
 papers by Dr. XYZ and give the titles and abstracts. 

Observation from Custom Tool: [Successfully retrieves recent pap
ers including titles, abstracts, dates, and database IDs]

Agent: Sure, here are the recent papers with titles and abstr
acts: [lists recent paper titles and abstracts]

Me: Great, can you please now give me the database IDs for the papers?


Agent: I don't have the ability to recall or provide database IDs from previous interactions. 

So while the input and 
output of the chat history are stored in the agent's memory, the observation / custom tool output is not. Does anyone kn
ow an approach to store this data in the agent's memory?
```
---

     
 
all -  [ Work asked me which laptop to buy for me - pls help? ](https://www.reddit.com/r/pchelp/comments/16ujmfh/work_asked_me_which_laptop_to_buy_for_me_pls_help/) , 2023-10-01-0911
```
 

Hello everyone,

I have been working as a junior developer in this company for some months now

I have been using my 
own Acer Nitro 5 17' (i7 11800h, RTX 3060 Laptop 6GB, 16GB Ram)

So far I've been involved in projects with computer vis
ion, audio and nlp

This is an entirely new branch for the company and I'm still a student at the beginning of my journe
y, therefore there is no 'standard modus operandi' for doing things and basically I'm the one responsible for telling th
em what piece of hardware is best for my needs

Anything that involves training we just rent GPUs from the major provide
rs so I'm definitely not worrying about that

Things I will definitely be working on

\- OpenAI API integration  
\- NVI
DIA NeMo framework  
\- YOLO  
\- Langchain, elastic and similars

Since I've been busy studying and learning stuff I've
 never really bothered looking into hardware requirements for any of the things I've done/will do

Does the hardware cho
ice matter in this case?

They proposed me a laptop with i7 12th gen, 16GB Ram, and RTX4050 which costs 1k euros

I told
 them to hold off and that I would have done some further research because that doesn't look like a solid investment in 
my opinion

**What (I think) I know:**

Budget I assume is something in the 1k - 2k range but they really just care abou
t giving me something that allows me to provide good results

\- Pretty much when running models locally for testing and
 developing, they will run on a GPU, which I assume has to be powerful. But how powerful is powerful enough? 4060? 4080?
 4090? Do mobile CPUs even make sense?  
\- I notices some dockerized services take up a fair bit of my current CPU, so 
is it coherent to assume that a more recent CPU with more cores and pretty much more power would be beneficial for my wo
rk?  
\- 16GB Ram nowadays is barely enough for google chrome with a few extensions so I don't really have any doubts th
at going for 32GB is a reasonable enough upgrade  
\- I work both at home, at the office and around the world when I'm i
n WFH mode, so a laptop would seem a better option than a Desktop PC, but is that actually the case?

**What I don't kno
w**

Aside from the fact that this section worringly overlaps with the 'what I know section'..  
I've only considered Wi
ndows laptops onto which I would at the very least make dual boot with linux if not exclusively linux because the NVIDIA
 NeMo framework can't run on windows

Given what I will do, should I even consider Apple? Like a Macbook Pro M1 or somet
hing like that?

I already have high end desktop pc at home and my current laptop is already something I'm comfortable b
ringing around, but one big limitation is that I always need to be plugged into a power source or the battery drains wit
hing one hour of work  
AFAIK a macbook pro would kinda allow me to work anywhere so that'd be a cool quality of life up
grade but I doubt it's practically worth anything other than a 'cool!' reaction

As you can see there's a lot of stuff I
 don't know and I don't really know what I actually need

Thank you so much for any help and suggestion towards the righ
t direction!
```
---

     
 
all -  [ Work asked me to tell them which PC to buy for me - Suggestions? plshelp ](https://www.reddit.com/r/learnmachinelearning/comments/16ujluo/work_asked_me_to_tell_them_which_pc_to_buy_for_me/) , 2023-10-01-0911
```
Hello everyone,

I have been working as a junior developer in this company for some months now

I have been using my own
 Acer Nitro 5 17' (i7 11800h, RTX 3060 Laptop 6GB, 16GB Ram)

So far I've been involved in projects with computer vision
, audio and nlp

This is an entirely new branch for the company and I'm still a student at the beginning of my journey, 
therefore there is no 'standard modus operandi' for doing things and basically I'm the one responsible for telling them 
what piece of hardware is best for my needs

Anything that involves training we just rent GPUs from the major providers 
so I'm definitely not worrying about that

Things I will definitely be working on

\- OpenAI API integration  
\- NVIDIA
 NeMo framework  
\- YOLO  
\- Langchain, elastic and similars

&#x200B;

Since I've been busy studying and learning stu
ff I've never really bothered looking into hardware requirements for any of the things I've done/will do

Does the hardw
are choice matter in this case?  


They proposed me a laptop with i7 12th gen, 16GB Ram, and RTX4050 which costs 1k eur
os

I told them to hold off and that I would have done some further research because that doesn't look like a solid inve
stment in my opinion

&#x200B;

**What (I think) I know:**

Budget I assume is something in the 1k - 2k range but they r
eally just care about giving me something that allows me to provide good results

\- Pretty much when running models loc
ally for testing and developing, they will run on a GPU, which I assume has to be powerful. But how powerful is powerful
 enough? 4060? 4080? 4090? Do mobile CPUs even make sense?  
\- I notices some dockerized services take up a fair bit of
 my current CPU, so is it coherent to assume that a more recent CPU with more cores and pretty much more power would be 
beneficial for my work?  
\- 16GB Ram nowadays is barely enough for google chrome with a few extensions so I don't reall
y have any doubts that going for 32GB is a reasonable enough upgrade  
\- I work both at home, at the office and around 
the world when I'm in WFH mode, so a laptop would seem a better option than a Desktop PC, but is that actually the case?
  


**What I don't know**

Aside from the fact that this section worringly overlaps with the 'what I know section'..  

I've only considered Windows laptops onto which I would at the very least make dual boot with linux if not exclusively l
inux because the NVIDIA NeMo framework can't run on windows

Given what I will do, should I even consider Apple? Like a 
Macbook Pro M1 or something like that?

  
I already have high end desktop pc at home and my current laptop is already s
omething I'm comfortable bringing around, but one big limitation is that I always need to be plugged into a power source
 or the battery drains withing one hour of work  
AFAIK a macbook pro would kinda allow me to work anywhere so that'd be
 a cool quality of life upgrade but I doubt it's practically worth anything other than a 'cool!' reaction

&#x200B;

As 
you can see there's a lot of stuff I don't know and I don't really know what I actually need

Thank you so much for any 
help and suggestion towards the right direction!  

```
---

     
 
all -  [ Chunking and retrieving documents with tables ](https://www.reddit.com/r/LangChain/comments/16uip55/chunking_and_retrieving_documents_with_tables/) , 2023-10-01-0911
```
We have a lot of documents that have many large tables. I'm thinking there are three challenges facing RAG systems with 
table-heavy documents:

1. Chunking such that it doesn't break up the tables, or at least when the tables are broken up 
they retain their headers or context.
2. Retrieving tables that are mostly numbers. The semantic content of the table co
uld be lost because it's mostly numbers.
3. Answering questions and understanding table formats.

Has anyone had any suc
cess getting through these barriers? I've found Llama Index has a discussion of using [recursive retrieval with Pandas Q
uery](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/pdf_tables/recursive_retriever.html)\- which is a
 fascinating approach. Just wanted to start a discussion on this topic and see what everyone else has experienced.
```
---

     
 
all -  [ LLM that can tutor Langchain? ](https://www.reddit.com/r/LangChain/comments/16ui95u/llm_that_can_tutor_langchain/) , 2023-10-01-0911
```
Does anyone know of an LLM that I can host locally that actually understands and comprehends langchain?  🙏      

I need
 a tutor so bad it's difficult for me to comprehend.    

Chat GPT, my go to tutor, has no clue what it is, I suppose th
at's because it's so new but it sucks when I'm asking questions about syntax or if something doesn't work related to lan
gchain.    
I learned python tremendously fast this way and it would be amazing to find an LLM that can do langchain
```
---

     
 
all -  [ What is your preferred way of testing / evaluating answers from vector stores? ](https://www.reddit.com/r/LangChain/comments/16uc0ph/what_is_your_preferred_way_of_testing_evaluating/) , 2023-10-01-0911
```
I was wondering how other people evaluate answers from the llm when using vector stores. I prefer using a reference data
set + SBERT.
```
---

     
 
all -  [ Incorporate file name into model ](https://www.reddit.com/r/LangChain/comments/16uc00j/incorporate_file_name_into_model/) , 2023-10-01-0911
```
I'm wanting to build a personal GPT which ingests my Logseq directory and can answer queries.

Logseq saves each day's j
ournal into a seperate markdown file with the date as the filename. Is there a way to have LangChain take the filename i
nto account so I can ask date related questions?
```
---

     
 
all -  [ Seeking Input on Local Model Alternatives for Complex Database Queries, Mapping ](https://www.reddit.com/r/LocalLLaMA/comments/16ua37d/seeking_input_on_local_model_alternatives_for/) , 2023-10-01-0911
```
I am working on developing a conversational agent capable of answering complex questions about our database. Our goal is
 to empower users to make detailed inquiries about entity names, specialties, locations, and more. However, we've encoun
tered some performance issues with the LLM 7B model in comparison to Chat GPT.

If you've had experience with local mode
ls that excel in handling complex database queries with langchain agent, we'd love to hear from you.

Please feel free t
o share your thoughts, experiences, or suggestions in the comments below.
```
---

     
 
all -  [ How to ask human to provider more input when provided input not enough ](https://www.reddit.com/r/LangChain/comments/16u8sxk/how_to_ask_human_to_provider_more_input_when/) , 2023-10-01-0911
```
we are using langchain agent to help us do self serving in kubernetes world, for example I want to troubleshoot a pod re
start or restart a pod, most of time, user will only say 'I want to restart my service with the name nginx', we need mor
e context here most of the time such as Kubernetes cluster name, application deploy namespace...

seek any advice here t
o do this more elegantly, thanks 🙏 .

here's the code,

    tools = [
        StructuredTool.from_function(
            
list_pod_info,
            name='ListPod',
            description='''
            a tool that can connect to kubernetes
 cluster with context on demand and run kubectl command to get all pods in specific namespace,
            please note t
he result here does not indicate the pod is health or not, it just list all pods in specific namespace
            '''
 
       ),
        StructuredTool.from_function(
            vector_store_pod_info,
            name='GetPod',
          
  description='''
            Useful for when you need to answer questions about get pod detail infromation using pod na
me, please note you need to get exact pod name using ListPod tool first
            if you can not infer the namespace, 
ask human for help. 
            '''
        ),
    ]
    memory = ConversationBufferMemory(memory_key='memory', return_
messages=True)
    
    agent = initialize_agent(
        tools,
        VertexAI(temperature=0, max_output_tokens=512, 
streaming=True),
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        ver
bose=True
    )
    
```
---

     
 
all -  [ Project Showcase: Summarize Yelp Reviews ](https://www.reddit.com/r/LangChain/comments/16u5r03/project_showcase_summarize_yelp_reviews/) , 2023-10-01-0911
```
Hi all, just wanted to showcase a small project I built using the Langchain's map-reduce summarization chain. Essentiall
y, we're summarizing  Yelp reviews into a single, concise review so that you don't need to waste time scrolling to figur
e out what/where to eat!  


[https://1bitereview.com/](https://1bitereview.com/)

Come check it out! Also looking for f
eedback!
```
---

     
 
all -  [ Optimal Architecture for Project ](https://www.reddit.com/r/LangChain/comments/16u0jlx/optimal_architecture_for_project/) , 2023-10-01-0911
```
I'm looking to create a document chatting LLM tool with LangChain/OpenAI/Pinecone, where I will have documents for a few
 hundred different clients, and probably 10-20 PDF reports for each client. 

What's the best way to set up the vector s
tore so that the LLM can synthesize data across all documents efficiently? Should I be using name spaces in Pincone (one
 per client e.g.), or will the LLM (assume GPT 3.5 or higher) be smart enough to source the correct documents using some
thing like Pinecone.from texts() to load everything without segmentation?

Also curious how smart I can expect something
 like this to be, could I ask it something open-ended like 'Which client experienced the largest growth in revenue over 
the last 5 years?' and expect it to produce an accurate result?

There seems to be lots of videos about this topic (docu
ment chatting etc), but they all use toy examples with maybe one or two PDFs, so hard to know what the best way to do th
is in practice would be.

Thanks in advance!
```
---

     
 
all -  [ Multi-Modal Vector Embeddings at Scale ](https://www.reddit.com/r/LangChain/comments/16tzoui/multimodal_vector_embeddings_at_scale/) , 2023-10-01-0911
```
Hey everyone, excited to announce the addition of image embeddings for semantic similarity search to VectorFlow, the onl
y high volume open source embedding pipeline.  Now you can embed a high volume of images quickly and search them using v
ectorflow or langchain! This will empower a wide range of applications, from e-commerce product searches to manufacturin
g defect detection.

We built this to support multi-modal AI applications, since LLMs don’t exist in a vacuum. This is c
omplementary to LangChain so you can add image support into your LLM apps. 

If you are thinking about adding images to 
your LLM workflows or computer vision systems, we would love to hear from you to learn more about the problems you are f
acing and see if VectorFlow can help!

Check out our Open Source repo - [https://github.com/dgarnitz/vectorflow](https:/
/github.com/dgarnitz/vectorflow)
```
---

     
 
all -  [ Is this the right vector embedding use case? ](https://www.reddit.com/r/LangChain/comments/16txs5p/is_this_the_right_vector_embedding_use_case/) , 2023-10-01-0911
```
Could you grab all data for a record, transform it to text, and store that in a vector database? What about an audit log
 for a record or plain text summary of the record? 

Would the nearest search function behave as expected? Has anyone tr
ied something similar?
```
---

     
 
all -  [ Difference between Tool LLM and normal LLM ](https://www.reddit.com/r/LangChain/comments/16tvkf8/difference_between_tool_llm_and_normal_llm/) , 2023-10-01-0911
```
Hi

So I have a chatbot which I implement for RAG.

I have 4 different tools, which I call through an agent.

Now, consi
der that I pass different LLMs to the tools and to the agent. To the agent I pass GPT-4, and to the tools I pass GPT 3.5


My question is, where is the cutoff point where one LLM takes over the job of the other? If I ask a question, then wou
ld the question be processed by the main LLM, tool selected by the LLM as well, and then once the tool is called, then t
he tool LLM is used for text retrieval or whatever the tool does?

If we have GPT 3.5 and GPT 4, what would you do? As i
n, which model would you use for the tool LLM and which for the main?  


I am getting very counter intuitive results, i
.e. the GPT 3.5 performs better for text retrieval in most cases than GPT 4, which just gives no result found.
```
---

     
 
all -  [ How to inject always-present context into ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/16trvoe/how_to_inject_alwayspresent_context_into/) , 2023-10-01-0911
```
I'm using ConversationalRetrievalChain for Q&A on documents. I've split the main document into smaller ones and used the
m in as\_retriever().

There's important info that isn’t in the Q&A document, but it’s crucial for every question about 
it. I don't want to add it to the vector database, as it might not get retrieved, leaving the model without key context.


Is there a better way to give this info to the model, besides adding it to the prompt?
```
---

     
 
all -  [ Best recommended way to install FAISS? ](https://www.reddit.com/r/LangChain/comments/16tnhyi/best_recommended_way_to_install_faiss/) , 2023-10-01-0911
```
Hi.

I am tired of re-installing faiss-cpu.

Sometimes it works great. Sometimes it gives 'faiss-cpu has no attribute Fl
atIndexL2' error.

Internet shows that it must be install with conda because pip doesn't support faiss.

I tried install
ing it using conda, and after few days, same error.

I am using Langchain's agents to work with FAISS for Document based
 QnA.

Currently I have installed faiss-cpu using conda and I have set-up a virtual env using vscode and it's working fi
ne. However when I run same code in jupyter notebook, it gives me error that cannot import faiss please install it using
 pip.

It sometimes confuses me which one is working (conda or pip) and which is not.
```
---

     
 
all -  [ Question about using GPT4All embeddings with FAISS ](https://www.reddit.com/r/LangChain/comments/16tlk4m/question_about_using_gpt4all_embeddings_with_faiss/) , 2023-10-01-0911
```
I'm following the tutorial on Vector Backed Retrieval from here: 

https://python.langchain.com/docs/modules/data_connec
tion/retrievers/vectorstore

It works flawlessly with OpenAiEmbeddings. However, I'm trying to use this with a local LLM
. and don't really want any reliance on OpenAi. 

I'm trying to use GPT4All embeddings, but I run into an assert d == se
lf.d error. 

I believe this is due to this line:

embedding_size = 1536 # Dimensions of the OpenAIEmbeddings

Does anyo
ne know what the embedding size needs to be for GPT4All?

I can't find it anywhere online.

Thanks!
```
---

     
 
all -  [ What are the problems faced when an AI customer support chatbot is used by a SaaS business. ](https://www.reddit.com/r/LangChain/comments/16tj65q/what_are_the_problems_faced_when_an_ai_customer/) , 2023-10-01-0911
```
What exactly are all the problems/possible problems faced while using and incorporating an AI customer support chatbot b
y small to medium sized SaaS businesses in USA/Europe/etc.  
Since am learning how to build AI chatbots and want to sell
 them to SaaS businesses.
```
---

     
 
all -  [ How to use it to search for similar array of numbers? ](https://www.reddit.com/r/LangChain/comments/16thbqq/how_to_use_it_to_search_for_similar_array_of/) , 2023-10-01-0911
```
Hi guys! 

Can anyone tell me how I can use it given 10 numbers to answer with similar array? My database consists of 40
 (0 to 40) keys each having 100 arrays of 10 numbers from 0 to 40.

Thank you!
```
---

     
 
all -  [ Langchain execution GPT-4 too slow ](https://www.reddit.com/r/OpenAI/comments/16tdee6/langchain_execution_gpt4_too_slow/) , 2023-10-01-0911
```
Hi all, I am using Langchain with GPT-4 but I am struggling since it is too slow for my needs. Average request is 2k tok
ens.

Actually we get the first chunk of text after 2 seconds and this is the way we call it.

  
llm\_chain = LLMChain(
  
 llm=OpenAI(model\_name='gpt-4', temperature=0.1, streaming=True, callbacks=\[custom\_callback\_handler\]),  
 prompt
=prompt\_template,  
 verbose=True,  
 memory=memory // it contains the history from ConversationBufferMemory(memory\_ke
y='chat\_history')  
)  


result = llm\_chain.run(prompt)

&#x200B;

Do you think there is way to make the model lighte
r? Considering we do not need much external data but is it mainly custom business stuff? (so technically we do not need 
geography, history and so on..)  


Thanks
```
---

     
 
all -  [ How to use CustomCallbackHandler to update a state of an agent? ](https://www.reddit.com/r/LangChain/comments/16tbjns/how_to_use_customcallbackhandler_to_update_a/) , 2023-10-01-0911
```
Folks,

I am building a shopping assistant chatbot.
It walks users through various stages of a shopping trip, I.e., 1. P
ick a grocery store, 2. Pick out groceries, 3. Check out, 4. Make payment, etc

My questions are
1. How do create a stag
e attribute in the agent?
2. How do I update the stage based on the conversation history? I came across CustomCallbackHa
nder and on-agent-start method, I don’t quite know how to use it to update the stage attribute?
3. How do I make sure th
e agent uses specific tools for a given stage?

Any feedback is greatly appreciated a
```
---

     
 
all -  [ What's your favorite RAG system and why? Langchain, LlamaIndex, etc? ](https://www.reddit.com/r/LocalLLaMA/comments/16taq8m/whats_your_favorite_rag_system_and_why_langchain/) , 2023-10-01-0911
```
Just trying to understand the latest landscape of RAGs out there.

Thanks!
```
---

     
 
all -  [ I just used Supabase and Strapi. ](https://youtu.be/vndfVnRPcgk?si=Dkkcg5HJ4cNAw5BQ) , 2023-10-01-0911
```

It was interesting discovery project, they are both great at what they do, and I am heavily biased towards Strapi.

But
 they both serve slightly different needs.  So I would say use one or the other.  

But if you are still interested to s
ee my experiment, you can checkout this video.

Lol.  But only click if you are interested.

On the side note.  I discov
ered that I can use Supabase vector storage.

Which is really awesome.

My alternative was pinecone, but it’s pricing is
 insane.  

So I am in the process rebuilding my vector, langchain, open ai powered chatbot to use Supabase vector stora
ge.  

Will keep you all posted.
```
---

     
 
all -  [ Is Finding Multiple Instances Possible Using Langchain??? ](https://www.reddit.com/r/LangChain/comments/16t358t/is_finding_multiple_instances_possible_using/) , 2023-10-01-0911
```
Hey everyone,

I've been experimenting with Langchain and OpenAI's embedding models. From my understanding, these models
 are especially powerful when it comes to understanding and answering direct questions, thanks to the way documents are 
stored as vectors.

However, I've encountered some challenges when trying to ask questions that require identifying mult
iple instances or patterns within a document. For example, asking 'find all instances of X' seems to be tricky due to th
e nature of vector embeddings.

Is my understanding correct? If so, are there any techniques or strategies that can be e
mployed to ask such 'find all instances of...' questions effectively using these models?

Appreciate any insights or exp
eriences you can share!
```
---

     
 
all -  [ We have an integration on LangChain and are looking for feedback :) ](https://www.reddit.com/r/LangChain/comments/16t2ttu/we_have_an_integration_on_langchain_and_are/) , 2023-10-01-0911
```
Hi everyone, 

We recently worked on an integration with LangChain, which we launched a few days ago: [https://blog.lang
chain.dev/eden-ai-x-langchain/](https://blog.langchain.dev/eden-ai-x-langchain/)

Our service aggregates many AI service
s (and not just LLMs) into a single API with endpoints that link back to [competing providers](https://www.edenai.co/pro
viders). The idea is to give users the flexibility to choose at any time the provider that suits them best (in terms of 
price, latency, response quality, etc.) and to manage in a single place all their consumption in terms of AI and LLM ser
vices available via API. 

And we're looking for user feedback on this integration. It would be a great help to us in ou
r development. It will also help us understand whether or not it's worth continuing to work on this integration by keepi
ng it up to date: [https://python.langchain.com/docs/integrations/llms/edenai](https://python.langchain.com/docs/integra
tions/llms/edenai) & [https://python.langchain.com/docs/integrations/tools/edenai\_tools](https://python.langchain.com/d
ocs/integrations/tools/edenai_tools)

Sorry in advance if my message sounds promotional, but it's really not. We're look
ing for frank and honest feedback and Reddit is often the best place for that :) 

Cheers,
```
---

     
 
all -  [ No-code development of customized smart assistant ](https://www.reddit.com/r/SideProject/comments/16t1vhu/nocode_development_of_customized_smart_assistant/) , 2023-10-01-0911
```
Hi everyone, I built an early prototype of a zero-code development tool for building customized smart assistant. Would l
ove some feedback:

[https://houseelf.app/](https://houseelf.app/)

I included a quick example of SalesGPT equivalent ([
https://python.langchain.com/docs/use\_cases/more/agents/agents/sales\_agent\_with\_context](https://python.langchain.co
m/docs/use_cases/more/agents/agents/sales_agent_with_context)) built with the tool to help people getting started:

[htt
ps://houseelf.app/editor/219/](https://houseelf.app/editor/219/) 

If you find this interesting, please feel free to DM 
me. All feedback & questions welcome.
```
---

     
 
all -  [ Unhashable type: 'list' ](https://www.reddit.com/r/LangChain/comments/16t1sqp/unhashable_type_list/) , 2023-10-01-0911
```
I've been following the guide on LangChain called CHat with your Data

[https://learn.deeplearning.ai/langchain-chat-wit
h-your-data/lesson/1/introduction](https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/1/introduction)

I
've followed the code exactly but near the very end end when I make the call to the LLM I get the above error.  Any idea
s?

Here is the full code

from langchain.document\_loaders import PyPDFLoader, TextLoader  
loader = PyPDFLoader('examp
le\_data/23andMe Case Study \_ Life Sciences \_ AWS.pdf')  
\# loader = TextLoader('bob.txt')  
\# Load the document by 
calling loader.load()  
pages = loader.load()  
\# SOme debug stuff to check contents of loaded file  
\# print(len(page
s))  
\# print(pages\[0\].page\_content\[0:500\])  


\# Define the Text Splitter  
from langchain.text\_splitter import
 RecursiveCharacterTextSplitter  
text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=1500, chunk\_overlap=150) 
 
\# Create a split of the document using the text splitter  
splits = text\_splitter.split\_documents(pages)  


from l
angchain.vectorstores import Chroma  
from langchain.embeddings import HuggingFaceEmbeddings  
modelPath = 'all-MiniLM-L
6-v2' # Look at moving models to a standard place for other code to reuse \~/model/googlr/all-MimiLM-L6-v2  
model\_kwar
gs = {'device': 'cpu'}  
encode\_kwargs = {'normalize\_embeddings': False}  
embeddings = HuggingFaceEmbeddings(  
 mode
l\_name=modelPath, model\_kwargs=model\_kwargs, encode\_kwargs=encode\_kwargs  
)  


persist\_directory = 'docs/chroma/
'  
\# Create the vector store  
\# vectordb = Chroma.from\_documents(  
\#     documents=splits, embedding=embeddings, 
persist\_directory=persist\_directory  
\# )  
from langchain.vectorstores import FAISS  
vectordb = FAISS.from\_documen
ts(documents=splits, embedding=embeddings)  
\# print(vectordb.\_collection.count())  


question = 'WHat benefits did 2
3AndMe see from sitching to AWS?'  
docs = vectordb.similarity\_search(question, k=3)  
\# Check the length of the docum
ent  
print(len(docs))  
\# Check the content of the first document  
print(docs\[0\].page\_content)  
\# Persist the da
tabase to use it later  
\# vectordb.persist()  


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeli
ne  
from langchain.llms import HuggingFacePipeline  
tokenizer = AutoTokenizer.from\_pretrained(  
 'flan-t5-large'  
)
  # Look at moving models to a standard place for other code to reuse \~/model/googlr/flan-t5-large  
model = AutoModelF
orSeq2SeqLM.from\_pretrained('flan-t5-large')  
pipe = pipeline('text2text-generation', model=model, tokenizer=tokenizer
)  
llm = HuggingFacePipeline(  
 pipeline=pipeline,  
 model\_kwargs={'temperature': 0, 'max\_length': 512},  
)  
from
 langchain.prompts import PromptTemplate  


from langchain.chains import RetrievalQA  
\# Build prompt  
template = '''
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you d
on't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always s
ay 'thanks for asking!' at the end of the answer.   
{context}  
Question: {question}  
Helpful Answer:'''  
QA\_CHAIN\_
PROMPT = PromptTemplate.from\_template(template)  # Run chain  
qa\_chain = RetrievalQA.from\_chain\_type(  
 llm,  
 re
triever=vectordb.as\_retriever(),  
 return\_source\_documents=True,  
 chain\_type\_kwargs={'prompt': QA\_CHAIN\_PROMPT
},  
)  


question = 'Is probability a class topic?'  
result = qa\_chain({'query': question})  
\# Check the result of
 the query  
print(result\['result'\])  
\# Check the source document from where we  
print(result\['source\_documents'\
]\[0\])  


&#x200B;

thanks
```
---

     
 
all -  [ ROScribe v0.0.3: Using LangChain to create the entire code for a robotic project in ROS2 ](https://www.reddit.com/r/LangChain/comments/16t1kgz/roscribe_v003_using_langchain_to_create_the/) , 2023-10-01-0911
```
With ROScribe v0.0.3 released yesterday, you can now build your robotics project automatically in ROS2 as well as ROS1.


[**https://github.com/RoboCoachTechnologies/ROScribe**](https://github.com/RoboCoachTechnologies/ROScribe)

ROScribe us
es GPT and LangChain to ask you about the details of your robotic project, draws the RQT graph, generate the code for al
l ROS nodes, and writes the launch file and installation scripts. Here is a demo on how to use the tool:

[**https://www
.youtube.com/watch?v=H2QaeelkReU**](https://www.youtube.com/watch?v=H2QaeelkReU)

**Release notes for v0.0.3:**

* ROS2 
integration:
   * Now ROScribe supports both ROS1 and ROS2.
   * Code generation for ROS2 uses rclpy instead of rospy
  
 * Installation scripts for ROS2 use [setup.py](https://setup.py/) and [setup.cf](https://setup.cf/) instead of CMakeLis
ts.txt

**ROScribe is an open source project and we welcome you to contribute to this project.**
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-01-0911
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-01-0911
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-01-0911
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-01-0911
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-01-0911
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-01-0911
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-01-0911
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-01-0911
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-10-01-0911
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
