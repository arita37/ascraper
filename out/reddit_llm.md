 
all -  [ Langrunner: Simplifying Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/LangChain/comments/1f97nye/langrunner_simplifying_remote_execution_in/) , 2024-09-05-0912
```
When using Langchain and LlamaIndex to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. To solve this, we created the **Langrunner** tool which offers an inline API that 
lets you execute specific blocks of code remotely without wrapping the entire codebase. It integrates directly into your
 existing workflow, scheduling tasks on clusters optimized with the necessary resources (AWS, GCP, Azure, or Kubernetes)
 and pulling results back into your local environment.

No more manual containerization or artifact transfers—just strea
mlined development from within your notebook!

Check it out here: [https://github.com/dkubeai/langrunner](https://github
.com/dkubeai/langrunner)
```
---

     
 
all -  [ reMind: An Open-Source Digital Memory Assistant
 ](https://www.reddit.com/r/LocalLLaMA/comments/1f94502/remind_an_opensource_digital_memory_assistant/) , 2024-09-05-0912
```
I'd like to get some feedback on **reMind**, a project I've been developing over the past nine months. It's an open-sour
ce digital memory assistant that captures screen content, uses AI for indexing and retrieval, and stores everything loca
lly to ensure privacy. Here's a more detailed breakdown of what the code does:

# Key Components and Functionality

1. *
*Screen Capture (record\_photo.py)**
   * Takes screenshots at regular intervals (default every 2 seconds)
   * Uses str
uctural similarity (SSIM) and histogram comparison to detect significant changes between screenshots
   * Organizes scre
enshots into daily folders
   * Implements a dynamic buffer system to adjust sensitivity based on recent changes
2. **Im
age Processing Pipeline (pipeline\_db.py)**
   * Monitors directories for new screenshot files using a watchdog
   * Pro
cesses new images through an OCR system (using a Swift-based tool)
   * Extracts text content and metadata from images
 
  * Stores processed data in a SQLite database and JSON files for easy retrieval
3. **Data Ingestion (ingestion.py)**
  
 * Loads and processes new data from the SQLite database
   * Groups entries by date and updates JSON files (new\_texts.
json and all\_texts.json)
   * Ensures data consistency between different storage formats
4. **Vector Store Creation (ad
ding\_vectore.py)**
   * Creates and updates a vector store using Chroma for efficient similarity search
   * Utilizes O
llamaEmbeddings to generate text embeddings
   * Splits documents into smaller chunks for more precise retrieval
   * Im
plements a system to track and process only new or updated documents
5. **Query Processing (swift.py)**
   * Sets up a F
lask server to handle user queries
   * Integrates with Langchain for advanced retrieval and question answering
   * Imp
lements time-based filtering of results (e.g., today, yesterday, this week)
   * Uses Ollama with the Llama 3.1 model fo
r generating responses
   * Classifies questions to determine if they require searching the personal knowledge base or c
an be answered with general knowledge
6. **Application Management (remind\_sansprint.py)**
   * Serves as the main entry
 point for the reMind application
   * Sets up necessary directories and initializes the SQLite database
   * Manages th
e execution of various background scripts (screen capture, processing pipeline, etc.)
   * Implements a system tray appl
ication using rumps for easy access and control
7. **User Interface Integration**
   * While not directly part of the Py
thon backend, the project integrates with OpenWebUI for a user-friendly interface
   * Allows users to interact with the
ir personal knowledge base through a chat-like interface

# Key Technologies

* **Ollama**: Used for running the Llama 3
.1 model locally
* **Meta's Llama 3.1**: The core language model used for understanding and generating responses
* **Nom
ic AI**: Used for generating text embeddings
* **Chroma**: Vector database for efficient similarity search
* **Langchain
**: Provides tools for building applications with LLMs
* **Flask**: Lightweight web server for handling API requests
* *
*SQLite**: Local database for storing processed data
* **OpenWebUI**: Provides a user-friendly interface for interacting
 with the system

The goal is to make reMind customizable and fully open-source. All data processing and storage happen 
locally, ensuring user privacy. The system is designed to be extensible, allowing users to potentially add their own mod
ules or customize existing ones.

I'd appreciate any thoughts or suggestions on how to improve the project. If you're in
terested in checking it out or contributing, here's the GitHub link: https://github.com/DonTizi/remind

Thanks in advanc
e for your input!


```
---

     
 
all -  [ What kind of agents would I need to mimic perplexity pro search in my RAG app? ](https://i.redd.it/3q3wwoo5lumd1.jpeg) , 2024-09-05-0912
```
I'm curious on how perplexity's pro search works. What do you guys think does the workflow look like? How to brake down 
a question like that and what agents would I need for something similar?
```
---

     
 
all -  [ How to tell if a page in a document text or numerical data? ](https://www.reddit.com/r/LangChain/comments/1f9196y/how_to_tell_if_a_page_in_a_document_text_or/) , 2024-09-05-0912
```
I'm trying to parse a pdf to add metadata for each chunk to denote if it is mostly text or (mostly numerical) data. I've
 found that if I don't filter the data out, it will produce too many hallucinations. I was planning to simply calculate 
if the ratio of letters to numbers in the document, unless there is a smarter way to go about doing this?

I'm using hug
gingface with a chroma db.
```
---

     
 
all -  [ What are tools in llm? ](https://www.reddit.com/r/ollama/comments/1f8yg2f/what_are_tools_in_llm/) , 2024-09-05-0912
```
I'm new to LLMs and Langchain and have built a RAG application. I've noticed a lot of talk about tools in LLMs, but I'm 
not sure how to create them without defining functions.
Can anyone recommend a tutorial or article that explains this pr
ocess? I'd love to learn more about it.
Thanks!
```
---

     
 
all -  [ Create Your AI Retriever and Win $300 ](https://www.reddit.com/r/LangChain/comments/1f8xutx/create_your_ai_retriever_and_win_300/) , 2024-09-05-0912
```
🚀If you are interested in AI and have a ChatGPT plus account, join our e**xclusive testing event,** experience DenserRet
riever, and earn up to $**300!** We’re seeking AI pioneers to explore and provide feedback on our retriever’s capabiliti
es. Don’t miss out - learn more at [http://retriever.denser.ai/campaign/gpt](http://retriever.denser.ai/campaign/gpt) an
d [https://youtu.be/9f2fUaU1z2w](https://youtu.be/9f2fUaU1z2w). Seize this opportunity today!

💡 W**hy Participate?**

*
 Earn a $50 Amazon gift card for your insights.
* Compete for top rewards: 1st place: $300, 2nd place: $200, 3rd place: 
$100.
* Be among the first to experience cutting-edge RAG technology.
* Build and customize your own GPTs using your dat
a.

**Timeline**

* **Apply**: Submit your application between 9/4 and 9/11.
* **Notification**: Denser will notify qual
ified applicants via email on 9/12.
* **Test**: Approved applicants will receive instructions via email and will have fr
om 9/13 to 9/20 to complete the test and submit the feedback form.
* **Receive Your Gift Card and Rewards**: Denser will
 email you the $50 Amazon gift card on 9/25 and notify the winners of the $300, $200, and $100 prizes to arrange deliver
y.

#AI #RAG #DenserRetriever #TechInnovation #CustomGPTs #GPTs


```
---

     
 
all -  [ Best way to pass negative examples to models using Langchain? ](https://www.reddit.com/r/LangChain/comments/1f8vp0s/best_way_to_pass_negative_examples_to_models/) , 2024-09-05-0912
```
Hello everyone, I'm currently trying to figure out the best way to include negative examples in a prompt.

My first appr
oach was to add them to the System Message. Another method I'm experimenting with is passing AI messages with the 'examp
le' flag set to True, but I’m not sure how to specify them as negative examples.

What methods are you using?

UPDATE: T
hanks everyone for the comments! From the articles I've read, it seems that including negative examples helps provide mo
re accurate responses aligned with our objectives. My current approach is to use positive examples (or just examples) in
 both the system message and the list of messages with the 'example' flag. For a specific case, I used both negative and
 positive examples in the system message. Based on your feedback, I’ll continue focusing on using only examples for now.
 Thanks again!
```
---

     
 
all -  [ AI jobs ](https://www.reddit.com/r/IndiaJobsOpenings/comments/1f8uwal/ai_jobs/) , 2024-09-05-0912
```
Looking for job opportunities in AI domain, have worked as an AI Engineer and on data as well, got 2 yoe on python, SQL,
 databricks as well as LLM fine-tuning, RAGs, Langchain etc. 
```
---

     
 
all -  [ OpenAI Assistant slow response on first message ](https://www.reddit.com/r/LangChain/comments/1f8usju/openai_assistant_slow_response_on_first_message/) , 2024-09-05-0912
```
I built a chatbot on Azure using OpenAI's gpt-4o-mini, hosted on a Azure WebApp running streamlit for the front end. I'm
 using the Assistant API for making calls, and I noticed that the first message always gets a slow response. I first tho
ught it was the i initialization of the thread that took some time, but after testing I found the delay occurs between a
dding the first message to the thread and receiving a response.

Is there anybody else experiencing this? And if so, how
 did you fix it or how did you mitigate it to prevent it from influencing the user experience?
```
---

     
 
all -  [ Tool calling in LangGraph and how to update the Graph-State with Tools output ](https://www.reddit.com/r/LangChain/comments/1f8ui4a/tool_calling_in_langgraph_and_how_to_update_the/) , 2024-09-05-0912
```
Hey,  
atm I'm looking into LangGraph and the agents ability to call tools. I was able to build an agent which has this 
architecture. The idea is taken from: [https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-2-enhancing
-the-chatbot-with-tools](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-2-enhancing-the-chatbot-w
ith-tools)

https://preview.redd.it/ma8bv5d6rsmd1.png?width=290&format=png&auto=webp&s=8d13a4e318c267c787cf2bb8725637e5f
62c304c

When a tool is called the Chatbot receives a Toolmesage with the output of the tool. Now my question is, how to
 take this output and write it into the state. Let's say my state looks something like this:

    class State(TypedDict)
:
        messages: Annotated[list[AnyMessage], add_messages]
        first_name: str
        last_name: str
        dat
e_of_birth: str

And I have a very simple tool which is called when the user provides his name in the query, to find the
 date\_of\_birth in the database.

    @tool
    find_user_date_of_birth(user_name: str):
    '''This tool is used to se
arch for the users date of birth in the customer DB if the user name is given in the query.'''
      date_of_birth = '01
.01.1990' # this is just a mock tool
      return f'The user {username} birthday is {date_of_birth}'

  
How am I now ab
le to update the GraphState in a way that date\_of\_birth is set in the State?
```
---

     
 
all -  [ Attribute Extraction For E-commerce products ](https://www.reddit.com/r/LangChain/comments/1f8tcdz/attribute_extraction_for_ecommerce_products/) , 2024-09-05-0912
```
I am trying to extract attributes for e-commerce but the problem is that I need to first either write the attribute sche
ma myself manually and use any LLM for attribute extraction (and this is ideal as I know which attribute are important t
o have).

But the problem is that I have 5000 different categories and I can't write 5,000 schemas manually so now what 
I am trying to do is asking GPT4o to define a schema for each category and then use that schema for attribute extraction
 pipeline again with GPT4o.  
Another problem is using GPT to define the schema as it's not correct always sometime, it 
is putting a key 'price' and sometime, it is putting 'price\_range', etc.

What is the ideal solution of this problem?
```
---

     
 
all -  [ Scientifically proving the efficiency of chunking strategy, LLM hyperparameters (temp, top p, contex ](https://www.reddit.com/r/learnmachinelearning/comments/1f8s63h/scientifically_proving_the_efficiency_of_chunking/) , 2024-09-05-0912
```
Hey guys, so my thesis in construction management is to propose a RAG based framework that automatically extracts the at
tributes of construction materials from technical datasheets (PDFs) and convert them to structured format like .csv so t
hat it can be used for further analysis. With most trial and error, I've finished the prototype system using langchain a
nd gemini pro and evaluated the system using RAGAS since I thought it would be more appropriate to evaluate the entire s
ystem rather than evaluating the LLM only. And my advisor agrees on my evaluation method but he also wants me to evaluat
e each of the modules in my system.



 Specifically, he wants me to show how I got to my chunking strategy, and how i g
ot to the specific chunking size and overlap size. As far as I understand, chunking strategies for PDF files are not sta
ndardized and many of the research I found just use trial and error approach until they feel that it's enough. I've expl
ained that to him and yet he demands me to scientifically prove my approach which I have no idea how to do.



Also, ano
ther question I get from him is the hyperparameters. I've referenced that to the API documentations of Gemini and other 
similar researches on LLM-based systems but he wants me to show a scientific matrix-based conclusion on how i get to my 
hyperparameter values. My way of explanation is that since the desired output is a structured format, I've used the lowe
st values in terms of temperature and p-values to minimize the randomness of the output but he's not satisfied with my a
nswer.



And lastly, the prompt template that I've designed. He is asking how I managed to design this particular promp
t. I've told him that this prompt engineering is a relatively new area so there is no standardized metric or 'methods' t
hat is universally agreed upon and such many of the researches simply say that it's a trial and error approach or am ad-
hoc approach, but once again, he disagrees and wants me to refer to a specific guideline to prove that the prompt that i
 am using is the most optimal one. 





To be completely honest neither me nor my advisor have a deep understanding on 
this research area since it's more related to computer science, and the goal of my research is to propose a foundational
 framework on how we, as a construction industry can utilize the capabilities of LLMs and RAG into our workflow. And I f
eel like the things that he's asking me to do goes beyond my scope as well as my capabilities since they're not even rel
ated to construction management. So, now I am completely stuck on what I'm supposed to do. 



So, my question is do you
 guys know any related published research papers specifically about evaluating those? Is it even possible? Because I've 
already looked into other papers about domain-specific LLM systems outside computer science and they don't seem to focus
 on these things in their studies. 
```
---

     
 
all -  [ Scientifically proving the efficiency of chunking strategy, LLM hyperparameters (temp, top p, contex ](https://www.reddit.com/r/ArtificialInteligence/comments/1f8rxsd/scientifically_proving_the_efficiency_of_chunking/) , 2024-09-05-0912
```
Hey guys, so my thesis in construction management is to propose a RAG based framework that automatically extracts the at
tributes of construction materials from technical datasheets (PDFs) and convert them to structured format like .csv so t
hat it can be used for further analysis. With most trial and error, I've finished the prototype system using langchain a
nd gemini pro and evaluated the system using RAGAS since I thought it would be more appropriate to evaluate the entire s
ystem rather than evaluating the LLM only. And my advisor agrees on my evaluation method but he also wants me to evaluat
e each of the modules in my system.

 Specifically, he wants me to show how I got to my chunking strategy, and how i got
 to the specific chunking size and overlap size. As far as I understand, chunking strategies for PDF files are not stand
ardized and many of the research I found just use trial and error approach until they feel that it's enough. I've explai
ned that to him and yet he demands me to scientifically prove my approach which I have no idea how to do.

Also, another
 question I get from him is the hyperparameters. I've referenced that to the API documentations of Gemini and other simi
lar researches on LLM-based systems but he wants me to show a scientific matrix-based conclusion on how i get to my hype
rparameter values. My way of explanation is that since the desired output is a structured format, I've used the lowest v
alues in terms of temperature and p-values to minimize the randomness of the output but he's not satisfied with my answe
r.

And lastly, the prompt template that I've designed. He is asking how I managed to design this particular prompt. I'v
e told him that this prompt engineering is a relatively new area so there is no standardized metric or 'methods' that is
 universally agreed upon and such many of the researches simply say that it's a trial and error approach or am ad-hoc ap
proach, but once again, he disagrees and wants me to refer to a specific guideline to prove that the prompt that i am us
ing is the most optimal one. 

To be completely honest neither me nor my advisor have a deep understanding on this resea
rch area since it's more related to computer science, and the goal of my research is to propose a foundational framework
 on how we, as a construction industry can utilize the capabilities of LLMs and RAG into our workflow. And I feel like t
he things that he's asking me to do goes beyond my scope as well as my capabilities since they're not even related to co
nstruction management. So, now I am completely stuck on what I'm supposed to do. 

So, my question is do you guys know a
ny related published research papers specifically about evaluating those? Is it even possible? Because I've already look
ed into other papers about domain-specific LLM systems outside computer science and they don't seem to focus on these th
ings in their studies. 
```
---

     
 
all -  [ Langchain Python Full Course For Beginners ](https://youtu.be/ndsSglS46tU?si=51eZGHune85QV2K-) , 2024-09-05-0912
```

```
---

     
 
all -  [ We Need to Talk.. with RAG ](https://www.reddit.com/r/LangChain/comments/1f8pukk/we_need_to_talk_with_rag/) , 2024-09-05-0912
```
I understand how to create a basic RAG: data processing, chunking, search, and fact extraction using an LLM.  
But how d
o you make a RAG that supports dialogue? One that understands or even asks clarifying questions? Keeps the conversation 
context in mind? Remembers previous answers? I need ideas! 
```
---

     
 
all -  [ How do LLMs understand tasks? ](https://www.reddit.com/r/LangChain/comments/1f8o87y/how_do_llms_understand_tasks/) , 2024-09-05-0912
```
I looked for explanations in the web but couldnt find anything concrete, so how do LLMs understand what task to do? what
 happens underneath? Are there any relevant papers/references to this?
```
---

     
 
all -  [ Does RAG help to enhance text-to-image accuracy? ](https://www.reddit.com/r/LangChain/comments/1f8na72/does_rag_help_to_enhance_texttoimage_accuracy/) , 2024-09-05-0912
```
Anyone did multimodality model before? For RAG, can it help to enhance the accuracy of the relativeness and correctness 
of generated images? Corresponding with the text?
```
---

     
 
all -  [ RAG with Langchain ](https://www.reddit.com/r/Rag/comments/1f8m7f7/rag_with_langchain/) , 2024-09-05-0912
```
In **RAG**, what I have done that I have multiple pdf uploaded, which I have saved temporarily into me local folder and 
reading its content using **Langchain PyPDFLoader** and created a **Chroma** Vector Store and according to the query, ex
tracted **similar** search results and passed those result to LLM Model (currently using **GPT** Models) and then sent t
he response to user. Now what are my requirements or can say modifications

* Document can be of any format like **pdf, 
image, csv**
* My PDF or image have some tabular structured data. Due to this **langchain loader**, it is not properly u
nderstanding the tabular data as vector stores are designed for text.

How can I tackle these things ? I can also send c
ode of this.

https://preview.redd.it/y1vxdp5qhqmd1.png?width=1578&format=png&auto=webp&s=5972cf9fd482c2c4c8c0a2f5bca480
0245e46cab

https://preview.redd.it/lkncdp5qhqmd1.png?width=6856&format=png&auto=webp&s=b1047ff283ba73a039e5fff447395353
6e8a46a6

  
This is my Code, please look into this.
```
---

     
 
all -  [ Why LCEL (in Python)? ](https://www.reddit.com/r/LangChain/comments/1f8lz4s/why_lcel_in_python/) , 2024-09-05-0912
```
Let me preface this by saying that I'd like to keep an open mind, and maybe there's a train that I've missed in the past
 few years. Also, my day job is infosec, and I don't do full-time dev these days, so maybe I'm just crusty.

I've also s
een other posts about LCEL but couldn't find anything talking about some of what I have issues with.

I don't understand
 why LCEL has been implemented, or at least the way and why it's been implemented in Python.

My problems with LCEL:

* 
It overrides '\_\_or\_\_' to implement the pipeline syntax. I'm not sure using this way is intended behaviour
* It doesn
't seem Pythonic (happy to be proven otherwise)
* There's no reason something similar couldn't have been implemented in 
a traditional approach using \*args or otherwise
* In the documentation using instantiated classes along with other clas
ses results in the possibility for a user to implement ambiguity which to some degree happens in the doco `Prompt(prompt
_text) | LLM(open_ai) | Output(str_output_parser)` or something similar would surely would be better, it clearly defines
 what component it is etc (but something like `pipeline.run(Prompt(prompt_text), LLM(open_ai), Output(str_output_parser)
` would looks fine to me)
* There's already guidance written on writing declarative Python (functional programming but f
unctional programming is declarative) [https://docs.python.org/3/howto/functional.html](https://docs.python.org/3/howto/
functional.html)

  
While I personally don't like it, if it is necessary, I do think implementing some clear convention
s and guidelines would help and probably make things less confusing

Doing this IMO is messy and ambiguous 

`some_var |
 SomeClass() | OtherClass() | other_var | MoreClass()`

Should be either

    # what_goes_in_me = 'something'
    # What
IAm(what_goes_in_me)
    
    prompt_text = 'whatever'
    chain = Prompt(prompt_text) | AzureChatOpenAI()

  
or the fo
llowing with guidance on naming conventions

    llm = AzureChatOpenAI()
    prompt = Prompt(text)
    output_parser = O
utputParser()
    chain = llm | prompt | output_parser




```
---

     
 
all -  [ Bypass LLM call for some inputs ](https://www.reddit.com/r/LangChain/comments/1f8l9pm/bypass_llm_call_for_some_inputs/) , 2024-09-05-0912
```
I am building a rag based chatbot where for certain specific input questions i dont really need an llm call to the knowl
edge base.

questions which point to certain apis from the broader application and llm calls arent actually needed..

ho
w to do this   
im using llamaindex
```
---

     
 
all -  [ [5 YoE, SDE3, Software Engineering, Canada] ](https://i.redd.it/acewiuxlqpmd1.jpeg) , 2024-09-05-0912
```
Would be happy to get feedback on my resume
```
---

     
 
all -  [ Differentiate many users document in pgvector ](https://www.reddit.com/r/LangChain/comments/1f8iif0/differentiate_many_users_document_in_pgvector/) , 2024-09-05-0912
```
So Im little curious to know on how to perform rag, especially similarity search over documents uploaded by specific use
r in my pgvector.

Till yet I get to know adding metadata and userid in it and later pass that user id in filter to retr
ieve docs only uploaded by that specific users among many other users data.
```
---

     
 
all -  [ Question on implementing Guardrail for llm app ](https://www.reddit.com/r/LangChain/comments/1f8eh8a/question_on_implementing_guardrail_for_llm_app/) , 2024-09-05-0912
```

Hi everyone,

I'm working on an LLM application and need some advice on implementing guardrails. My setup includes a ga
teway app that interprets questions and identifies the client. Based on this, it routes the request to a specific RAG (R
etrieval-Augmented Generation) setup. 

I have multiple clients, and my current configuration routes questions from Clie
nt A to RAG A and Client B to RAG B. The issue is that if I'm using Client A's services, I should only receive answers f
rom RAG A. If I accidentally ask a question meant for Client B, I need to ensure the app doesn't respond to prevent any 
data leaks.

How can I implement these guardrails effectively?

Thanks in advance for your help
```
---

     
 
all -  [ Unpopular opinion: I think out of the box RAG/GraphRAG solutions for complex domain based problems w ](https://www.reddit.com/r/LangChain/comments/1f8c9c3/unpopular_opinion_i_think_out_of_the_box/) , 2024-09-05-0912
```
I see a lot of posts on this channel where people are building RAG as a service, GraphRAG as a service, RAG API, etc. wh
ich you just put a document and start chatting. However, generally curious, do any of these work out of the box for comp
lex domain based problems such as Financial data analysis, Scientific paper analysis etc?

A RAG pipeline built for Fina
ncial data analysis would be pretty different from the one built for customer issues QnA.

I see the main problem being 
that of the index we are creating. In the VectorRAG approach, if one creates chunks without adding any domain based know
ledge, it will definitely be sub par. Retrieval will mostly miss out chunks which do not have direct semantic overlap wi
th the query.

Graph RAG seems as a rescue, as it builds out the relations. Eg. it can figure out the name, location, is
 a, has a relations. However, even that will miss out on domain based relations unless explicitly specified during graph
 creation.

Curious if it works for anyone. And in general how are folks injecting domain into their RAG systems right n
ow ?
```
---

     
 
all -  [ VectorDB for your RAG Projects ](https://www.reddit.com/r/LangChain/comments/1f85w3w/vectordb_for_your_rag_projects/) , 2024-09-05-0912
```
For your recent RAG projects using Langchain, which vector database have you used and why?
```
---

     
 
all -  [  LangChain tool function won't take my dictionary as a parameter consistently? ](https://www.reddit.com/r/LangChain/comments/1f838o6/langchain_tool_function_wont_take_my_dictionary/) , 2024-09-05-0912
```
I'm trying to feed a dictionary to a LangChain tool function, but its not working

Here's an example with pizza when it 
works right:

    Invoking: `make_pizza` with `{pizza_data: {'dough': 'thin crust', 'sauce': 'tomato', 'toppings': ['che
ese', 'pepperoni', 'mushrooms'], 'cooking_instructions': ['preheat oven', 'bake for 15 minutes']}}`
    

But this happe
ns half the time:

    Invoking: `make_pizza` with `{'dough': 'thin crust', 'sauce': 'tomato', 'toppings': ['cheese', 'p
epperoni', 'mushrooms'], 'cooking_instructions': ['preheat oven', 'bake for 15 minutes']}`
    

My tool function looks 
like this:

    def make_pizza(pizza_data: dict):
        # ...
    error message
    1 validation error for make_pizzaS
chema
    pizza_data

Anyway of writing a prompt that will get this to work consistency 
```
---

     
 
all -  [ Understanding Semantic Chunking: Preserving Coherence and Context in Text Division ](https://medium.com/@nirdiamant21/semantic-chunking-improving-ai-information-retrieval-2f468be2d707) , 2024-09-05-0912
```
A short blog post explaining what semantic chunking is (dividing text into chunks not based on a fixed size but by cutti
ng in a way that preserves the coherence of the content and maintains a consistent context)
```
---

     
 
all -  [ [0 YoE, Unemployed, Data Scientist/MLE, India] ](https://www.reddit.com/r/resumes/comments/1f82a1f/0_yoe_unemployed_data_scientistmle_india/) , 2024-09-05-0912
```
https://preview.redd.it/2fcwm3om0mmd1.png?width=1098&format=png&auto=webp&s=9ae1b9b207040cd41956d67ed5b33c3079ef5463


```
---

     
 
all -  [ Roast my resume, third year student currently applying to internships. Want to know if i am headed i ](https://www.reddit.com/r/developersIndia/comments/1f825zy/roast_my_resume_third_year_student_currently/) , 2024-09-05-0912
```
https://preview.redd.it/u7bsg4dtzlmd1.png?width=1094&format=png&auto=webp&s=93a478736d7ca089b6786703194f9137a1cf2fe2


```
---

     
 
all -  [ How do you guys do LLM evlauation? ](https://www.reddit.com/r/LangChain/comments/1f80pd2/how_do_you_guys_do_llm_evlauation/) , 2024-09-05-0912
```
https://preview.redd.it/kwim6sdsolmd1.png?width=1434&format=png&auto=webp&s=354533f2a7ebf5983c129c9eab983c321ea80bcd


```
---

     
 
all -  [ How to Attach an Image to a LangChain Agent with Tools? ](https://www.reddit.com/r/LangChain/comments/1f80bbm/how_to_attach_an_image_to_a_langchain_agent_with/) , 2024-09-05-0912
```
Has anyone figured out how to use a LangChain agent with tools and attach an image to it?

Right now, I'm working around
 this by asking the LLM to generate an image description and then using that description instead of the raw image. Howev
er, the results aren’t great—it's not capturing the nuances of the image as accurately as I’d like.

Is there a better w
ay to directly handle images with a LangChain agent? Any suggestions or workarounds would be appreciated!
```
---

     
 
all -  [ LangChain Image load vs Tesseract ](https://www.reddit.com/r/LangChain/comments/1f7z6bv/langchain_image_load_vs_tesseract/) , 2024-09-05-0912
```
I believe LangChain has the ability to extract text from images (https://python.langchain.com/v0.2/docs/integrations/doc
ument\_loaders/image/). Is it faster and more efficient than Tesseract Thank you! 

  

```
---

     
 
all -  [ Needle - The RAG Platform ](https://www.reddit.com/r/LangChain/comments/1f7z276/needle_the_rag_platform/) , 2024-09-05-0912
```
Hello, RAG community,

Since nobody (me included) likes these hidden sales posts I am very blunt here:  
'I am [Jan Heim
es](https://www.linkedin.com/in/jan-h-5164a2208/), co-founder of [Needle](https://needle-ai.com), and we just launched.'


The issue we are trying to solve is, that developers spend a lot of time building repetitive RAG pipelines. Therefore 
we abstract that process and offer an RAG service that can be called via an API. To ease the process even more we implem
ented data connectors, that sync data from different sources.  
We also have a [Python SDK](https://github.com/oeken/nee
dle-python) and [Haystack integration](https://github.com/JANHMS/needle-haystack).

We’ve put a lot of hard work into th
is, and I’d appreciate any feedback you have.

Thanks, and have a great day and if you are interested happy to chat on [
Discord](https://discord.gg/sqh3H97n).
```
---

     
 
all -  [ Welcome to DocuMindz! ](https://www.reddit.com/r/DocuMindz/comments/1f7xe4b/welcome_to_documindz/) , 2024-09-05-0912
```
[DocuMindz](https://preview.redd.it/xlmnwefxukmd1.png?width=1918&format=png&auto=webp&s=1382808947d3c0923d836d8236a1f771
1f47b792)

  
**What is DocuMindz?**

DocuMindz is an app developed using Streamlit, allowing users to efficiently searc
h and retrieve information from multiple PDF documents. It provides quick and accurate answers to your queries based on 
the content within those documents.

For those interested in code , can refer our Github repo \[ [https://github.com/Min
dzKonnectedAI/DocuMindz](https://github.com/MindzKonnectedAI/DocuMindz) \]

  
**Why DocuMindz?**

1. **Multiple PDF Sup
port:** Convert multiple PDFs to vectors and search through them simultaneously, making it easier to find the informatio
n you need across different documents.
2. **Intuitive UI:** The clean and simple interface, built using Streamlit, allow
s for easy interaction with the app, ensuring a seamless user experience.
3. **Fast and Accurate:** Powered by Langchain
, DocuMindz delivers quick and accurate answers to your questions, drawing directly from the content of your PDFs.
4. **
Authentication Mechanism:** With a built-in authentication system, DocuMindz ensures that only authorized users can acce
ss and utilize the app's features, keeping your data secure.

  
**Join Our Community!**

We’ve just launched this subre
ddit as a space for users, developers, and anyone interested in document management and retrieval to discuss, share, and
 learn more about DocuMindz.   


**What’s Next?**

Stay tuned for updates and feature announcements. Contributions are 
welcome!
```
---

     
 
all -  [ Langchain drawbacks ](https://www.reddit.com/r/ProPrompter/comments/1f7x1ww/langchain_drawbacks/) , 2024-09-05-0912
```
* Langchain initially seemed promising for quickly building a prototype chatbot, but limitations became apparent when cu
stomizations were needed;
* The project required custom logging and modifications to retriever functionality, leading to
 rewritten modules;
* Langchain's text splitting approach was found to be inadequate;
* Despite still being close to a P
roof of Concept stage, Langchain's usefulness diminished, mainly serving to improve skills in writing workarounds;
* A s
imilar experience was shared with a Discord bot project, where Langchain felt like a hastily made bot unsuitable for spe
cific needs;
* Langchain's architecture was found to be questionable, with hardcoded prompts and the need for extensive 
customization;
* Eventually, the project became so heavily customized that Langchain could be removed, leaving only the 
custom code.
```
---

     
 
all -  [ Introducing Azara! Easily build, train, deploy agentic workflows with no code ](https://www.reddit.com/r/AI_Agents/comments/1f7w3q1/introducing_azara_easily_build_train_deploy/) , 2024-09-05-0912
```
Hi everyone,

I’m excited to share something we’ve been quietly working on for the past year. After raising $1M in seed 
funding from notable investors, we’re finally ready to pull back the curtain on Azara. Azara is an agentic agents platfo
rm that brings your AI to life. We create text-to-action scenario workflows that ask clarifying questions, so nothing ge
ts lost in translation.  Built using Langchain among other tools. 

Just type or talk to Azara and watch it work. You ca
n create AI automations—no complex drag-and-drop interfaces or engineering required.

Check out [azara.ai](http://azara.
ai). Would love to hear what you think! 

https://reddit.com/link/1f7w3q1/video/hillnrwsekmd1/player


```
---

     
 
all -  [ Handling multiple functions making LLM calls ](https://www.reddit.com/r/LangChain/comments/1f7vy5q/handling_multiple_functions_making_llm_calls/) , 2024-09-05-0912
```
I have an orchestrator function which invokes a function after meeting a condition, the sub function then calls an LLM a
nd sends the response to the orchestrator, the orchestrator waits for this response and then sends this to another funct
ion making another LLM call, and so on for 4-5 times. Sometimes I may have parallel functions getting called by the orch
estrator. What would be a best approach here? 
```
---

     
 
all -  [ Introducing Azara! Build, train, deploy agentic workflows with no code. Built with Langchain ](https://www.reddit.com/r/LangChain/comments/1f7vsuf/introducing_azara_build_train_deploy_agentic/) , 2024-09-05-0912
```
Hi everyone,

I’m excited to share something we’ve been quietly working on for the past year. After raising $1M in seed 
funding from notable investors, we’re finally ready to pull back the curtain on Azara. Azara is an agentic agents platfo
rm that brings your AI to life. We created text-to-action scenario workflows that ask clarifying questions, so nothing g
ets lost in translation. It's built using Langchain among other tools.

Just type or talk to Azara and watch it work. Yo
u can create AI automations—no complex drag-and-drop interfaces or engineering required.  
  
Check out [azara.ai](https
://www.azara.ai/). Would love to hear what you think!

https://reddit.com/link/1f7vsuf/video/0ydvz7t4ckmd1/player


```
---

     
 
all -  [ [2 YoE, Working Student Data Science, Data Scientist, Germany] ](https://www.reddit.com/r/resumes/comments/1f7u82b/2_yoe_working_student_data_science_data_scientist/) , 2024-09-05-0912
```
Hello community,

I’m a 25-year-old female currently completing my master’s thesis in Information Systems at a universit
y in Germany (max. GPA in Ger: 1.0). My academic journey began with a bachelor’s degree in Marketing and Management in m
y home country, but I later transitioned into Data Science.

As I approach the end of my studies, I’ve been actively app
lying for (Junior) Data Scientist positions. However, I’m finding the job market to be quite challenging, with limited r
esponses and few interview opportunities.

I’m eager to improve my chances of landing a role in this field, and I would 
greatly appreciate any advice or suggestions on how to enhance my approach. I was thinking of removing course descriptio
ns and instead including only relevant course projects descriptions I used to take.

Thank you in advance for your help!


https://preview.redd.it/leetd75bujmd1.png?width=1000&format=png&auto=webp&s=8f6f87f660bb38915e47b468abe4679f7d0125c9


  

```
---

     
 
all -  [ Categorizing chat log ](https://www.reddit.com/r/LangChain/comments/1f7twfc/categorizing_chat_log/) , 2024-09-05-0912
```
I have a chat log of multiple people talking about different topics at once. Topic modeling doesn’t always work before i
f some says “has anyone sent in the mail” and someone replies “yes I did” it doesn’t categorize them into once. Currentl
y the best way has been to classify messages into questions and treat everything till next question as one topic. But th
at is also not accurate at times where a single conversation could have multiple questions regarding same topic. Or if a
 question is answered after another question is asked. I searched for something called as context aware threading, but d
on’t know how to get it working?
```
---

     
 
all -  [ RAG using LangChain: A step-by-step workflow! ](https://www.reddit.com/r/LangChain/comments/1f7teqe/rag_using_langchain_a_stepbystep_workflow/) , 2024-09-05-0912
```
I recently started learning about LangChain and was mind blown to see the power this AI framework has. [Created this sim
ple RAG video](https://youtu.be/TNUbBPdbsLA) where I used LangChain. Thought of sharing it to the community here for the
 feedback:)
```
---

     
 
all -  [ Parse multiple files at once without loop and single prompt for examples. Help required ](https://www.reddit.com/r/LangChain/comments/1f7sh2y/parse_multiple_files_at_once_without_loop_and/) , 2024-09-05-0912
```
I have a case where i need to parse and extract few text and numbers from multiple pdfs like more than 10000. I want to 
provide examples to the ai model so that it outputs structured text (json). How can I do it all at once instead of loopi
ng through multiple files with example prompts each time? Is it even possible something like batch processing without an
y loops? Thanks
```
---

     
 
all -  [ Best Open Source PDF Parsers for Tables? ](https://www.reddit.com/r/LangChain/comments/1f7nj10/best_open_source_pdf_parsers_for_tables/) , 2024-09-05-0912
```
I'm working on enhancing my AI assistant chatbot pipeline, which is primarily used for QA on industrial documents, user 
manuals, contracts, and legal agreements. A significant challenge I'm facing is effectively parsing PDFs that contain a 
lot of tables and images.

I’m looking for recommendations on the best open source tools or parsers that excel at extrac
ting structured data, especially from complex tables in PDFs. Any suggestions on tools that could help improve the inges
tion process for these kinds of documents would be greatly appreciated!

Thanks in advance for your help!
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-05-0912
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

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-09-05-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-05-0912
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-05-0912
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-09-05-0912
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-09-05-0912
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

     
