 
all -  [ Revolucionando el Web Scraping con IA ](https://www.reddit.com/r/LangChain/comments/18w2ms9/revolucionando_el_web_scraping_con_ia/) , 2024-01-02-0910
```
Todos sabemos lo '**tedioso**' que es hacer web scrapping, entender la estructura de un sitio web para que nuestro códig
o pueda obtener resultados, estar en constante mantenimiento por si el sitio web cambia su estructura o si agregan funci
onalidad con java script para cargar dinámicamente la información. Pero **¿Que pasaría si hubiera una manera de converti
r este 'tedioso' proceso en uno muy sencillo, adaptable a cualquier estructura?**

por ejemplo:

&#x200B;

https://previ
ew.redd.it/mmfiq0b8dv9c1.png?width=2232&format=png&auto=webp&s=377d8ff89ed3c0b16713a0c2f2dd742e27f5f9fa

&#x200B;

https
://preview.redd.it/g8rvpedadv9c1.png?width=1488&format=png&auto=webp&s=232b1858d1a70ffdff9d470dbfe279cc84e9bd86

Le asig
namos la tarea a la IA que se adapte a cualquier estructura de cualquier sitio web y obtenga resultados orgánicos de cal
idad.

&#x200B;

https://preview.redd.it/s0jp125hdv9c1.png?width=1189&format=png&auto=webp&s=2b59846330b114b9cf1b3aa0763
024999a7d6dc9

Pueden leer el artículo completo en el siguiente enlace:Link: [https://es.linkedin.com/pulse/revolucionan
do-el-web-scraping-con-ia-jean-pierre-alvarez-8gmge?trk=public\_post\_feed-article-content](https://es.linkedin.com/puls
e/revolucionando-el-web-scraping-con-ia-jean-pierre-alvarez-8gmge?trk=public_post_feed-article-content)

&#x200B;
```
---

     
 
all -  [ What are must have developer tools to build generative ai apps? ](https://www.reddit.com/r/ChatGPTCoding/comments/18vvqo2/what_are_must_have_developer_tools_to_build/) , 2024-01-02-0910
```
I have built multiple automations using gpt, midjourney, etc. Now looking to create a more organized version of these to
ols, what tools should I explore?

Edit: I see the question was quite open ended, let me add the tools that I have used 
and then you can add your recommendations

* Langchain (I use it only for few projects)
* OpenAI API
* 11labs api
* Redi
s (I use it for caching)
* node.js and express.js (all my projects are built as npm library with a cli that spins up exp
ress server to create http service on top of library)
* mocha and chai for testing, I run those tests on each PR with Gi
tHub actions, I use an spare openai account just for testing
* FluxNinja Aperture for rate limiting
* Your recommemdatio
ns (any small/big addition that can save time and headache in the future)
```
---

     
 
all -  [ Extremely fast response LLM interface and architect. ](https://www.reddit.com/r/LLMDevs/comments/18vrxx3/extremely_fast_response_llm_interface_and/) , 2024-01-02-0910
```

Hi all, I’m new to the technology and I’m looking to build a LLm api. Would like to seek advice to improve on the respo
nse speed. 

Problem statement:

I am working to build a chat feature for a manufacturing repair line to guide workers o
n how to fix various issue. The product changes hourly and so does the solution to fix it. The boss is very good coming 
out with solution but is way too busy to explain or teach his 38 repair man. His goal is to create a ML chat bot to do t
he reply where he will update the database with all sort of solution and when his repair man query the chat bot to searc
h for the best answer. He knows he will need the ML chat bot because:

1. Everyone ask a question differently. 
2. He ca
n add more solutions and does not need to repeat himself.

The chat bot must achieve a few critical requirement from my 
crazy boss. 

1. Each response must be below 1 sec. (Includes multiple prompt)
2. No simulating of a quick reply. He wan
ts the entire sentences to be out under 1sec. 
3.Must have a database query where he can upload a list of his solution. 

4. Must have memory but does not need to saved to a database
5. Answers should be short and easy. 
6. Don’t ask him to 
just let his employee search the database. He wants to move forward in the llm space. Not backwards. 
7. On-premise or o
n cloud doesn’t matter. (Prototype first before and funds)

The solution is usually short.
 
Example, “use a size 8 wenc
h with a bottom power up approach. Control the strength applied”

However the below 1 sec requirement is just crazy! Her
e is my build:

Langchain interface (quantization)
Llama-2-7b-chat-hf
Bitsnbytes: 4bit, nf4, double quant, torch.bfloat1
6

FAISS for memory caching
Sentence-transformers/all-mpney-base-v2
Langchain.memory conversationBufferMemory

vector da
tabase for storage of solution
Langchain vector store qdrant

Running on 3080 gpu

Prompt template.  


Total response t
ime taken per query: 1min

Can anyone provide any better solution to improve the speed?
I’m thinking of using vllm inste
ad to improve on the response speed. But I don’t think I can achieve 1sec. 

 Please help before I get fired.
```
---

     
 
all -  [ Finetuning code generation model on our own repositories ](https://www.reddit.com/r/LocalLLaMA/comments/18v80cn/finetuning_code_generation_model_on_our_own/) , 2024-01-02-0910
```
Hello,

I'm working on a code generation system for my personal usage. I've had some success with a RAG system using lan
gchain to add similar snippets as context, concatenate them and pass as prompt to a code Llama endpoint. My next step wo
uld be to finetune the model on my own code base.

I've seen several tutorials with axolotl on a text-to-SQL generation 
dataset, or on some prompt answering dataset, but I haven't seen anything like finetuning the model on multiple user-own
ed repos.

This surprises as I would have thought this was the next logical step to improve accuracy. Am I mistaken ? Is
 the knowledge added by finetuning already present in the context ? Is the performance gain not worth the hassle ?

Did 
somebody already tried this and has some feedback ?

Thanks a lot

&#x200B;

 
```
---

     
 
all -  [ Anyone done some webscraping using LangChain can guide me? ](https://www.reddit.com/r/LangChain/comments/18v6lqb/anyone_done_some_webscraping_using_langchain_can/) , 2024-01-02-0910
```
Hi so here is what I want langchain to do. 

Go to a website, submit some text in the text\_search bar

wait for the sea
rch result to load, fetch some of the contents of the search back
```
---

     
 
all -  [ Serve a Custom LLM Trained with RLHF in - FREE COLAB 📓 ](https://www.youtube.com/watch?v=dX27661ZFWc) , 2024-01-02-0910
```

```
---

     
 
all -  [ CrewAI agent framework with local models ](https://github.com/joaomdmoura/crewAI) , 2024-01-02-0910
```
This is great news for everyone who wants to develop agentic software. After a lot of failure and disappointments with r
unning Autogen with local models, I tried the rising star of agent frameworks, CrewAI. It is a multi-agent framework bas
ed on LangChain and utilities LangChain's recently added support for Ollama's JSON mode for reliable function calling. T
he developer treats local models as first class citizens.

I tried the [stock analysis](https://github.com/joaomdmoura/c
rewAI-examples/tree/main/stock_analysis) example code where the agents use a wide range of tools including google search
es and subsequently summarizing the top results, storing them in a vector database and generating analysis based on the 
findings. I tried it with Mistral 7B instruct 0.2 via Ollama on my MacBook Pro M1 16 GB laptop. It took the three agents
 15-20 min to perform all the research, RAG, and analysis to come up with a reasonable report. Very cool.
```
---

     
 
all -  [ Is anyone actually using Langchain in production? ](https://www.reddit.com/r/LocalLLaMA/comments/18v0sxq/is_anyone_actually_using_langchain_in_production/) , 2024-01-02-0910
```
Langchain seems pretty messed up.

\- The documentation is subpar compared to what one can expect from a tool that can b
e used in production. I tried searching for what's the difference between chain and agent without getting a clear answer
 to it.

\- The dis-cord community is pretty inactive honestly so many unclosed queries still in the chat.

\- There are
 so many ways of creating, for instance, an agent. and the document fails to provide a structured approach to incrementa
lly introducing these different methods.

So are people/companies actually using langchain in their products?
```
---

     
 
all -  [ Is anyone actually using Langchain in production? ](https://www.reddit.com/r/LangChain/comments/18v0s3k/is_anyone_actually_using_langchain_in_production/) , 2024-01-02-0910
```
Langchain seems pretty messed up. 

\- The documentation is subpar compared to what one can expect from a tool that can 
be used in production. I tried searching for what's the difference between chain and agent without getting a clear answe
r to it. 

\- The discord community is pretty inactive honestly so many unclosed queries still in the chat.

\- There ar
e so many ways of creating, for instance, an agent. and the document fails to provide a structured approach to increment
ally introducing these different methods.

&#x200B;

So are people/companies actually using langchain in their products?

```
---

     
 
all -  [ Any alternatives to Langchain's webpdfloader? ](https://www.reddit.com/r/LangChain/comments/18uwc21/any_alternatives_to_langchains_webpdfloader/) , 2024-01-02-0910
```
I'm trying to just load a pdf from a URL. I'm confused how to do so using the [webPDFLoader](https://js.langchain.com/do
cs/integrations/document_loaders/web_loaders/pdf). If anyone has a bit of time, please help explain how to implement thi
s? I would appreciate any help pls.

I'm doing this in nextjs. Where in the webPDFloader section do I put the pdfUrl var
iable?

    'use client';
    import React, { useEffect } from 'react';
    import { WebPDFLoader } from 'langchain/docu
ment_loaders/web/pdf';
    import { guestPdfId } from '@/components/Hero';
    import { Document } from 'react-pdf';
   
 
    
    
    const bucketId = process.env.NEXT_PUBLIC_APPWRITE_BUCKET_ID!;
    const fileId = guestPdfId;
    const p
rojectId = process.env.NEXT_PUBLIC_APPWRITE_PROJECT_ID!;
    
    const pdfUrl = `https://cloud.appwrite.io/v1/storage/b
uckets/${bucketId}/files/${fileId}/view?project=${projectId}&mode=admin`;
    
    // webPDFLoader
    const blob = new 
Blob(); // e.g. from a file input
    
    const loader = new WebPDFLoader(blob, {
      // you may need to add `.then(m
 => m.default)` to the end of the import
      pdfjs: () => import('pdfjs-dist/legacy/build/pdf.js'),
    });
    
    d
ocs = loader.load()
    
    const docLen = docs.length()
    
    const ProcessPdf = () => {
    
      return <div>
  
      <button onClick={doclen}>Show PDF</button>
    </div>;
    };
    
    export default ProcessPdf;
    

&#x200B;
```
---

     
 
all -  [ How Langchain or Llama Index stack against “native” RAG solutions? ](https://www.reddit.com/r/LangChain/comments/18uojpr/how_langchain_or_llama_index_stack_against_native/) , 2024-01-02-0910
```
I am new to the topic, and I want to build an assistant chatbot that can reference data from websites and docs. This can
 be achieved with OpenAI plugins and Cohere RAG connectors, just like using a framework like langchain. How do they comp
are?
```
---

     
 
all -  [ How can I keep my outputs consistent ](https://www.reddit.com/r/LangChain/comments/18unseb/how_can_i_keep_my_outputs_consistent/) , 2024-01-02-0910
```
I am working on one of my clients project where the user will pass the drug name and url of a pdf , from that pdf we nee
d to extract some fields , though chunk size kept is 2200 model is gpt-4-32k I see inconsistent results , how can I make
 results more consistent
```
---

     
 
all -  [ Wrote a small article on what I'll be learning in 2024. What are you guys planning to learn? ](https://www.reddit.com/r/developersIndia/comments/18ul6fa/wrote_a_small_article_on_what_ill_be_learning_in/) , 2024-01-02-0910
```
[Link to the article](https://dev.to/wannabee/discovering-new-tech-in-2024-what-ill-learn-3o0o)

&#x200B;

https://previ
ew.redd.it/ends614ezg9c1.png?width=2358&format=png&auto=webp&s=d711d072761a6b065ab2791d7cc5cc5fba8dab10
```
---

     
 
all -  [ Some help with feelings? ](https://www.reddit.com/r/LocalLLaMA/comments/18uiypc/some_help_with_feelings/) , 2024-01-02-0910
```
Hey, I'm kind of stuck here. Maybe you could help me out.
Still time for the one promised good deed this year ;) 
I'm tr
ying to make a voiced chatbot with a frontend, that reveals a smile or sorrow etc. based on the sentence it speaks.
I tr
ied different models, but none seem to obey my instruction for a complete chat session. 
The first idea was to return JS
ON in the following structure:

{
'feeling':'Joy',
'answer':'Hey!',
'code':'In case there is code to display. The bot sh
ouldn't read it'
}

But I got rid of that. Even though I told the llm to not explain the JSON or not to continue the con
versation it did sometimes.

Then I just moved on to something more simple. I told the llm to start every sentence with 
the feeling enclosed in 3 asterix like (which reddit turns into cursive words..):

***Joy*** Hey there! ***Neutral*** Ho
w can I help you? 

But still the same problems. After a while the instruction is simply ommited, it continues the conve
rstation without the user, or even worse it adds the history to the response.

The instruction to write with those feeli
ngs was included in the system prompt every time and some dummy conversation messages were included in the history. 

Mo
st tries were made with lmstudio and Mistral7bInstruct0.2. I also tried openchat, phi2 and dolphin-mixtral but i can't g
et the output to stay consistent. 

At this point I'd really appreciate any input. :)

Should I include some kind of fai
lsafe, that checks the response and remind the llm to respond correctly like langchain does it?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/18ugr69/for_hire_programmerweb_developerit_consultant/) , 2024-01-02-0910
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new technol
ogies that are needed for the project.

Rate is $50/h. Can also do fixed price by project, but only if the project/miles
tone is well-defined.

Satisfied customers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backe
nd_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how
_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.r
eddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testim
onials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/
v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Ple
ase note: I am **not** a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-02-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
all -  [ Help needed in understanding hosting with vLLM and Torchserve ](https://www.reddit.com/r/LocalLLaMA/comments/18uci4k/help_needed_in_understanding_hosting_with_vllm/) , 2024-01-02-0910
```
Hi all, I am fairly new to NLP and LLM hosting. I was planning to host Llama2-7B on an A10 GPU. On google searching I fo
und out that vLLM is quite famous and robust for hosting LLM's with 'Paged Attention' (Need to read this yet). 

I am fa
irly comfortably with torchserve, so I was planning to host vLLM (llama2-7b) in combination with Pytorch Serve. I am pla
nning to do the following:   
\- Load the model on model server with:  **llm = LLM(model='facebook/opt-125m')**   
\- Wi
thin the torchserve inference function, I will infer like: **single\_output = llm.generate(1\_PROMPT, sampling\_params)*
* 

\-------------------

My Questions: 

\- There could  be multiple requests at a time. The queue and async operations
 will be handled by torchserve. **So in this case, will vLLM internally perform continuous batching ?** 

\- Is this the
 right way to use vLLM on any model-server other than the setup already provided by vLLM repo ? (triton, openai, langcha
in, etc) (when I say any model server, I mean flask, django, or any other python based server application). 

\-------  

Thanks a lot for your suggestions and guidance in advance. I am also not against Triton or anything which I provided ou
t of box, I am just exploring this combination as all other models I use are currently hosted using torchserve (all the 
models are CNN based though).   
 
```
---

     
 
all -  [ Would it be smarter to use chunks of just embeddings in this situation? ](https://www.reddit.com/r/LangChain/comments/18u77h9/would_it_be_smarter_to_use_chunks_of_just/) , 2024-01-02-0910
```
I work for a company that develops software to manage company operations, including freight management, interest, profit
s, inventory, and more. We used to provide each customer with a massive user's manual as a reference for any questions t
hey might have. However, this proved to be incredibly inefficient, so we decided to leverage the power of LLMs (Large La
nguage Models) to create a personalized chat interface. This would allow clients to get answers directly from the manual
 in a more dynamic and user-friendly way.

Unfortunately, simply feeding the entire manual to the LLM resulted in chaoti
c and inaccurate outputs. Answers were often incoherent and meaningless. Thankfully, I discovered the techniques of chun
king and embeddings.

Now, my question is: given that our company's manual is already divided into smaller PDFs for each
 topic, should I further break down these sections into smaller chunks for LLM training, or would it be sufficient to ju
st create embeddings from the existing PDFs? Additionally, can the LLM formulate answers by drawing information from mul
tiple vectors (embeddings) at once? Or it only uses the info from the embedding it's mostly similar to the user's query?

```
---

     
 
all -  [ what should use to bulid Saas for chating with static 50K document's , Chatgpt Api ? or Langchain ?  ](https://www.reddit.com/r/OpenAI/comments/18tvty6/what_should_use_to_bulid_saas_for_chating_with/) , 2024-01-02-0910
```
hello folks 

&#x200B;

i hav an idea and i want start to build it but before i have question based on the nature of the
 project and data 

&#x200B;

what should use to bulid it ? 

when the data is static and its contains 50K document's  ,


should i use Chatgpt Api ? 

or Langchain ? 

or lamaindex ? 
```
---

     
 
all -  [ what should use to bulid Saas for chating with static 50K document's , Chatgpt Api ? or Langchain ?  ](https://www.reddit.com/r/PromptEngineering/comments/18tvtrh/what_should_use_to_bulid_saas_for_chating_with/) , 2024-01-02-0910
```
hello folks   
i hav an idea and i want start to build it but before i have question based on the nature of the project 
and data   
what should use to bulid it ?   
when the data is static and its contains 50K document's  ,  
should i use C
hatgpt Api ?   
or Langchain ?   
or lamaindex ? 
```
---

     
 
all -  [ Backend Info ](https://www.reddit.com/r/SillyTavernAI/comments/18trfh6/backend_info/) , 2024-01-02-0910
```
Hi, I wanted to ask if silly tavern uses langchain and MemGPT for its responses.
```
---

     
 
all -  [ Open Source for Large Langage Model ](https://www.reddit.com/r/LangChain/comments/18tqmjm/open_source_for_large_langage_model/) , 2024-01-02-0910
```
Hello community 🤗

How do we ensure the utmost protection of sensitive data prior to processing with advanced Large Lang
uage Models like ChatGPT 4, Llama 2, or Mistral AI? 🛡️
```
---

     
 
all -  [ Can't decide on infrastructure for my RAG ](https://www.reddit.com/r/LocalLLaMA/comments/18tppmv/cant_decide_on_infrastructure_for_my_rag/) , 2024-01-02-0910
```
Hi everyone,

I'm stuck deciding the infrastructure for my production RAG chat.I am trying to decide between using a Fas
tapi server in python, or try to create everything in the Nextjs project with Typescript.

My thoughts so far:

1. There
 is no ready-made Hybrid-search for Supabase in Python (but there is in JS)
2. The more advanced RAG features seem to be
 released in the Python version of Langchain first. like Cohere Reranking, Hyde, Query-expansion etc.
3. I already have 
the setup for the RAG in langserve, but I'm struggling working out how to keep a good chat history integrated against th
e nextjs frontend and the langserve server.
4. I'm leaning towards Supabase pgvector as my vector storage, since I feel 
it's more cost-effective and safe in terms of control (the RAG chat will include that the user can upload files, and mix
 a lot of different businesses on the same index in Pinecone doesn't seem like the best approach, maybe I'm wrong?)

&#x
200B;

Would appriciate some feedback so I can make the decision and move forwards.
```
---

     
 
all -  [ Can't decide on infrastructure for my RAG ](https://www.reddit.com/r/ArtificialInteligence/comments/18tpo4d/cant_decide_on_infrastructure_for_my_rag/) , 2024-01-02-0910
```
Hi everyone,  
I'm stuck deciding the infrastructure for my production RAG chat.  
I am trying to decide between using a
 Fastapi server in python, or try to create everything in the Nextjs project with Typescript.  
My thoughts so far:  
1)
 There is no ready-made Hybrid-search for Supabase in Python (but there is in JS)  
2) The more advanced RAG features se
em to be released in the Python version of Langchain first. like Cohere Reranking, Hyde, Query-expansion etc.  
3) I alr
eady have the setup for the RAG in langserve, but I'm struggling working out how to keep a good chat history integrated 
against the nextjs frontend and the langserve server.  
4) I'm leaning towards Supabase pgvector as my vector storage, s
ince I feel it's more cost-effective and safe in terms of control (the RAG chat will include that the user can upload fi
les, and mix a lot of different businesses on the same index in Pinecone doesn't seem like the best approach, maybe I'm 
wrong?)  
Would appriciate some feedback so I can make the decision and move forwards.
```
---

     
 
all -  [ Can't decide on infrastructure for my RAG ](https://www.reddit.com/r/LangChain/comments/18tpbcb/cant_decide_on_infrastructure_for_my_rag/) , 2024-01-02-0910
```
Hi everyone,

I'm stuck deciding the infrastructure for my production RAG chat.

I am tyrying to decide between using a 
Fastapi server (langserve) in python, or try to create everything in the Nextjs project with Typescript.

**My thoughts 
so far:**

1) There is no ready-made Hybrid-search for Supabase in Python (but there is in JS)

2) The more advanced RAG
 features seem to be released in the Python version of Langchain first. like Cohere Reranking, Hyde, Query-expansion etc
.

3) I already have the setup for the RAG in langserve, but I'm struggling working out how to keep a good chat history 
integrated against the nextjs frontend and the langserve server.

4) I leaning towards Supabase pgvector as my vector st
orage, since I feel it's more cost-effective and safe in terms of control (the RAG chat will include that the user can u
pload files, and mix a lot of different businesses on the same index in Pinecone doesn't seem like the best approach, ma
ybe I'm wrong?)

Would appriciate some feedback so I can make the decision and move forwards.
```
---

     
 
all -  [ Issues for ChatBot with Persona ](https://www.reddit.com/r/LocalLLaMA/comments/18tncqj/issues_for_chatbot_with_persona/) , 2024-01-02-0910
```
So , I'm a beginner in LLMs. I'm working on creating a chatbot that can mimic a person based on his information (the dat
a contains info like his likes , dislikes and relationships and others)

I tried creating a synthetic data using gpt wit
h query response pairs and finetuned using autotrain which didn't work out.

Now , I tried using langchain and gave a te
xt file with the person data and then also a  prompt template asked it to roleplay the person using the context in the d
ata. This works but it reverts back to question like 'what do u think about ai' , where it says as a ai language model ,
 it can't answer it.

I used WizardLM Llama model. I think issues with context window can come as well if the data is bi
g. 

How can I work on this idea? Is there any ways to improve upon the langchain idea or should I have used a different
 approach altogether?
```
---

     
 
all -  [ Seeking Advice: structuring and managing text data for a chatbot. ](https://www.reddit.com/r/LocalLLaMA/comments/18tmsz9/seeking_advice_structuring_and_managing_text_data/) , 2024-01-02-0910
```
 This is my first post on this subreddit, so hello everyone! ;)

I'm currently working on a locally hosted chatbot for a
n HR division to assist with their daily tasks. I'm using LLaMA 2, RAG, and LangChain as orchestrator. However, I'm faci
ng a challenge due to my limited experience in dealing with a large number of text documents—specifically, how to effect
ively store and organize them and then integrate them into a vector database. Simply storing data on physical disks does
n't provide me with the necessary version control for my data (and maybe analytics?). Moreover, I'm keen on implementing
 version control for the vector database itself. Do any of you have tips on how commercial projects typically structure 
such initiatives and what tools they employ?

Thank you all in advance!
```
---

     
 
all -  [ Splitting string data in order to apply load_qa_chain ](https://www.reddit.com/r/LangChain/comments/18tkz5v/splitting_string_data_in_order_to_apply_load_qa/) , 2024-01-02-0910
```
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80) 
    chunks = text_splitter.split_
text(PolicyScheduleRaw) 
    
    for chunk in chunks:
        print(chunk)
        print('-----------------------------
----------------------') 

 So I have the code above that splits the string PolicyScheduleRaw into chunks. This above st
ep completes successfully. However, when I then proceed to execute the below code, I get the error message:  `'str' obje
ct has no attribute 'page_content'`  


    llm = ChatOpenAI(temperature=0, openai_api_key='SECRET') question = 'Are my 
Bosch power tools covered?' chain = load_qa_chain(llm, chain_type='stuff')  result = chain.run(input_documents=chunks, m
odel='gpt-3.5-turbo-1106',question=question)

 If I change 

    split_text

to 

    create_documents

in the first cod
e block (I read somewhere that this could be the cause), then the chunk size of 1,000 no longer applies and for some rea
son the text is split per each character.   


How can I fix this?
```
---

     
 
all -  [ What is a intuitive way to get used to LCEL ](https://www.reddit.com/r/LangChain/comments/18tkbvr/what_is_a_intuitive_way_to_get_used_to_lcel/) , 2024-01-02-0910
```
I find the syntax weird (tbh just saw it for the first time). What is a intuitive way I apply this syntax, the documenta
tion is not super clear.
```
---

     
 
all -  [ Langchain citing sources when answers not from context (LCEL vs RetrievalQAWithSourcesChain) ](https://www.reddit.com/r/LangChain/comments/18thci6/langchain_citing_sources_when_answers_not_from/) , 2024-01-02-0910
```
I'm following the langchain example [here](https://python.langchain.com/docs/use_cases/question_answering/#adding-source
s) that is used to cite sources. It works great when the answer actually comes from the context.  But a simple query suc
h as 'hello' will answer with 'Hello!' with sources. So even irrelevant sources are returned.  Is there anyway to modify
 the LCEL provided by langchain to not return sources if it doesn't find an answer from them?

I've also tried **Retriev
alQAWithSourcesChain** and it works better when returning sources, but it's not returning any metadata - only the link. 
Additionally, the quality of the results vs LCEL (human evaluation) seems to fall short. The only way I know change the 
quality of the results is to use custom PromptTemplates, but still not sure how to get the metadata.
```
---

     
 
all -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-02-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
all -  [ Suggestions wanted: Local VectorDB without langchain ](https://www.reddit.com/r/vectordatabase/comments/18tbdui/suggestions_wanted_local_vectordb_without/) , 2024-01-02-0910
```
Im using ChromaDB python package currently and I don't use langchain.    
The limited documentation is really tough for 
me to work through and I feel as though I'm missing out on easier to use, more intuitive, or more feature rich vector da
tabase solutions that I can run on my local PC without docker. 
Pls help 🤗
```
---

     
 
all -  [ Langchain or Train model on documents? ](https://www.reddit.com/r/learnmachinelearning/comments/18t5gi7/langchain_or_train_model_on_documents/) , 2024-01-02-0910
```
Hello im currently doing a personal project I want to do something similar to Grammarly but specific to Cookbooks. Lets 
say a user is writes down steps for a recipe and enters the text to the NLP model  


The model in turn will tell the us
er if there is anything that is not to standard based on the documents. Let say they were making a cake and didn't add e
gg whites the model would highlight this and suggest an improvement.  This might not be the best example but my main obj
ective is to get something similar to Grammarly but based on documents not sentence structure    


I know this can be d
one both ways but I'm not sure for my purposes would be best?  


Sorry if if this is not in the correct subreddit. Here
's what I mean by Langchain in case im using the wrong term [https://www.youtube.com/watch?v=aywZrzNaKjs](https://www.yo
utube.com/watch?v=aywZrzNaKjs)
```
---

     
 
all -  [ Do we really need LCEL? ](https://www.reddit.com/r/LangChain/comments/18t3jn9/do_we_really_need_lcel/) , 2024-01-02-0910
```
Comment down below what you guys think about it. I think there is a huge push from the Langchain core dev community to p
ush it forward but I'm not sure if the larger community really welcomes this. I may be wrong here, but just curious.

[V
iew Poll](https://www.reddit.com/poll/18t3jn9)
```
---

     
 
all -  [ ConversationAgent + Llama-2 70B 4b - outputparser error llm not outputting prefix ](https://www.reddit.com/r/LangChain/comments/18t2u4g/conversationagent_llama2_70b_4b_outputparser/) , 2024-01-02-0910
```
Hello everyone.

We are still getting to grips with langchain, but we were able to get a phind-34B llm outputting the pr
efix using prompt tempate, works very well with tools. Problem is that we want to finetune a llama-2 70B using qlora to 
a 4bit, and for the life of us, we cannot get the llm to output the prefix in its responses , for example, we can't get 
it to respond as AI;  so the output parser picks it up. We tried all kinds of stuff in the prompt template like 'ALWAYS 
respond as AI: for example 'AI: (your response here)' which seems to work really well with the phind 34b (TheBloke awq v
ersion). 

Can anyone give us a hint of how to get langchain ConversationChatAgent (for conversation and tool usage) to 
work with a llama-2 based llm? We've been at it for 4 days, and no luck. 

Thanks in advance.
```
---

     
 
all -  [ Resume review. Losing my hopes of being the cog in a new wheel. ](https://i.redd.it/zoc7w4lv529c1.jpeg) , 2024-01-02-0910
```
I took a 50% paycut from my past organization because the work life balance was brutal and a scandal had surfaced wiping
 out a lot of my previous team. New org is slower than a kid with autism.  As a result, I haven't received any payraise 
in 2 years now and I really want to switch. Current TC: 17lpa. Looking for >30 LPA fixed pay roles.  I don't have a huge
 risk appetite so I turn down startups for the most part. I have got some really shitty job offers like one company tryi
ng to hire me for HR Analytics.  I don't even mind working 70 hours a week. I keep getting rejected and don't even reach
 interview stage.  Everywhere I apply.  I'm doing a hybrid masters from an old IIT. Topped my class.  I want to leverage
 that too.  
.
Is my resume really keyword stuffed or bad? Is there something wrong here? Please help.
```
---

     
 
all -  [ [Need Help] Langchain agent not executing properly in Celery worker ](https://www.reddit.com/r/LangChain/comments/18sw41b/need_help_langchain_agent_not_executing_properly/) , 2024-01-02-0910
```
I am working on implementing LangChain Agents in my Python project I am running this project using docker compose. In my
 project I am using Celery worker and have multiple worker services which executes from the queue. The entire setup is w
orking as expected.

One of these workers in agent worker where I have configured LangChain Agent. I have created a func
tion where I am loading tools, initializing agent and passing agent input.

When I run this setup as a simple standalone
 python project, everything runs fine and I see proper agent execution and output. But in the production environment I a
m using Celery workers running as Docker container. The above setup is run as a Celery worker. The setup is quite simple
 and straightforward.

But when I run this setup in as Celery worker, I observe that it **loads the tool and initializes
 the agent properly**. It also enters in the AgentExecutor chain **but fails to execute the tool function using the para
meter returned in the LLM response**.   


I have added more details, code the logs in the Github issue but haven't got 
any proper response yet: [https://github.com/langchain-ai/langchain/issues/15220](https://github.com/langchain-ai/langch
ain/issues/15220)  


Any help is highly appreciated. Happy Holidays!
```
---

     
 
all -  [ need help improving context quality to make a code assistant ](https://www.reddit.com/r/LocalLLaMA/comments/18sv8sw/need_help_improving_context_quality_to_make_a/) , 2024-01-02-0910
```
I tried to make a coding assistant some time ago. It should read my repo and point out and suggest code quality improvem
ents, suggest alternate design patterns, point out where complexity is getting out of hand, or even suggest alternate va
riable names.

However, I noticed that when I ask a question like the included 'What is the class hierarchy', or even so
mething specific about a specific struct or a file, the database does NOT include that struct or file in the context sen
t to the model! Chroma was terrible, but there was an online vector store (was it Activeloop's Deeplake?) that was much 
better at retrieving code chunks related to my question. Now, of course, the code doesn't run anymore (maybe I didn't pi
n some libraries in requirements.txt) so I can't show you the Documents the db loaded, but trust me they were terrible.


A few questions:
1. is Chroma really bad and I should use another vector db or do I have to tune it to get it to work? 
After all it's just a database storing numbers... maybe I have to try something other than 'mmr'?
2. Is there a better w
ay of getting context to the model? Right now the best I've found is https://cursor.sh/ but I want something that just r
eads my repo once I make a git commit and suggests any blind spots or points of improvement.
3. Just looking at my code 
real quick - any avenues I could improve context for the model?  Are embeddings better than simply including the code in
 the context? Perhaps embeddings take up less context space?

```
parser = argparse.ArgumentParser(description='Process 
some integers.')
parser.add_argument('repo_path', type=str, help='path to the repository')
parser.add_argument('--model_
path', type=str, default='llama-2-7b-32k-instruct.Q5_K_M.gguf', help='path to the model')
parser.add_argument('--llama',
 action='store_true', help='use LlamaCpp instead of ChatGPT')

args = parser.parse_args()

repo_path = args.repo_path
mo
del_path = args.model_path

# Load
loader = GenericLoader.from_filesystem(
    repo_path,
    glob='**/*',
    suffixes=
['.js'],
    parser=LanguageParser(language=Language.JS, parser_threshold=500) # Currently, the supported languages for 
code parsing are Python and JavaScript. 
    # Source https://api.python.langchain.com/en/latest/document_loaders/langch
ain.document_loaders.parsers.language.language_parser.LanguageParser.html
)
documents = loader.load()
# print('# of docu
ments', len(documents))

go_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.JS, 
             
                                                  chunk_size=2000, 
                                                    
           chunk_overlap=200)
texts = go_splitter.split_documents(documents)
# print('# of split documents (texts)', len
(texts))

def chatgpt(texts):
    db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
    retriev
er = db.as_retriever(
        search_type='mmr', # Also test 'similarity'
        search_kwargs={'k': 8},
    )

    llm
 = ChatOpenAI(model_name='gpt-4')
    return db, retriever, llm

if args.llama:
    db, retriever, llm = llama(texts)
el
se:
    db, retriever, llm = chatgpt(texts)

memory = ConversationSummaryMemory(llm=llm,memory_key='chat_history',return
_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

print('going to ask
 some questions now')
questions = [
    'What is the class hierarchy?',
]


while True:
    question = input('Ask a ques
tion: ')
    if not question:
        break
    documents = retriever.get_relevant_documents(question)
    pp(documents)

    result = qa(question)
    print(f'-> **Question**: {question} \n')
    print(f'**Answer**: {result['answer']} \n')

```
```
---

     
 
all -  [ NL2SQL query engines ](https://www.reddit.com/r/developersIndia/comments/18sss8h/nl2sql_query_engines/) , 2024-01-02-0910
```
I've be assigned a task to research about how we can incorporate the NL2SQL query engines to run queries over the databa
se using the LLMs. So far, I've seen about LangChain and LlamaIndex but haven't got any solid grip over this idea. If yo
u have any experience regarding this, please help me out with any kind of knowledge source you have. Thank you.
```
---

     
 
all -  [ Why is Tuna designed like it is? ](https://www.reddit.com/r/LangChain/comments/18srt00/why_is_tuna_designed_like_it_is/) , 2024-01-02-0910
```
I came across Tuna, a tool for generating Q&A data from plain text files: [https://blog.langchain.dev/introducing-tuna-a
-tool-for-rapidly-generating-synthetic-fine-tuning-datasets/](https://blog.langchain.dev/introducing-tuna-a-tool-for-rap
idly-generating-synthetic-fine-tuning-datasets/)

From what I understand, Tuna generates question-answer pairs for each 
individual section of text, rather than creating complex cross-topic question-answer pairs that encompass the entire doc
ument. There is the 'Multi chunk' feature where it can take up to 5 chunks maximum, but still not taking into account an
ywhere near the entire document or multiple documents.

My point is that research, e.g.: the LIMA paper, suggests that t
he model will perform best and converge more quickly when provided with complex, high-quality question-answer data. Howe
ver, is it possible that the model could converge just as well with less intricate data, provided that there is a suffic
ient amount of it?

I see that Andrew Gao developed this, I will try reach out directly to him.
```
---

     
 
all -  [ Hosting guidance in deployment of web service ](https://www.reddit.com/r/render_/comments/18sr8e2/hosting_guidance_in_deployment_of_web_service/) , 2024-01-02-0910
```
I have a very general question and would like to get any insight even if it does not solve the problem.

My code works j
ust fine on VSCODE editor, however the error I get during deployment is:  
ModuleNotFoundError: No module named 'langcha
in.memory'

Note that python, langchain library, code syntax everything is ok, but I think I need to specify something i
n the build commands or environment variable or any place else on the options given at the stage of initial deployment i
n Render platform.  
 
```
---

     
 
all -  [ RAG + Prompting ](https://www.reddit.com/r/LangChain/comments/18spba0/rag_prompting/) , 2024-01-02-0910
```
Hey everyone, just looking for some guidance here. I've built a RAG bot on pinecone but its.. not great. It sometimes an
swers questions incorrectly or repeats itself inappropriately. Thoughts? Thanks in advance
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-02-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2024-01-02-0910
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2024-01-02-0910
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2024-01-02-0910
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-02-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-02-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
