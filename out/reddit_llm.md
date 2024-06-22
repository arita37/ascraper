 
all -  [ Benchmarking PDF models for parsing accuracy ](https://www.reddit.com/r/LangChain/comments/1dlfth6/benchmarking_pdf_models_for_parsing_accuracy/) , 2024-06-22-0910
```
Hi folks, I often see questions about which open source pdf model or APIs are best for extraction from PDF. We attempt t
o help people make data-driven decisions by comparing the various models on their private documents.

We benchmarked sev
eral PDF models - Marker, EasyOCR, Unstructured and OCRMyPDF.

Marker is better than the others in terms of accuracy. Ea
syOCR comes second, and OCRMyPDF is pretty close.

You can run these benchmarks on your documents using our code - https
://github.com/tensorlakeai/indexify-extractors/tree/main/pdf/benchmark

The benchmark tool is using Indexify behind the 
scenes - https://github.com/tensorlakeai/indexify

Indexify is a scalable unstructured data extraction engine for buildi
ng multi-stage inference pipelines. The pipelines can handle extraction from 1000s of documents in parallel when deploye
d in a real cluster on the cloud.

I would love your feedback on what models and document layouts to benchmark next. 

F
or some reason Reddit is marking this post as spam when I add pictures, so here is a link to the docs with some charts -
 https://docs.getindexify.ai/usecases/pdf_extraction/#extractor-performance-analysis
```
---

     
 
all -  [ Roast my resume! I'm in Canada and I've applied to 500+ positions but not heard anything ](https://i.redd.it/y0m8xn89uz7d1.png) , 2024-06-22-0910
```
I'm graduating next week. Applied to over 500 jobs with and without referrals. I don't get any call backs! 

I'm looking
 for anything in the Data Science/Machine Learning/AI development space 
```
---

     
 
all -  [ How does AI agent orchestration work in practice? ](https://www.reddit.com/r/learnmachinelearning/comments/1dlewks/how_does_ai_agent_orchestration_work_in_practice/) , 2024-06-22-0910
```
I recently read the following article which talks about using a 'boss' AI to orchestrate a collection of AI agents, and 
the idea of an AI agent that learns ones business model:

https://sifted.eu/articles/autonomous-companies-ai

Reality/hy
pe aside, I'm having trouble understanding how this sort of thing works in practice. Like, what does the code for this s
ort of thing *actually* look like? How do you train a model on such an abstract concept as 'business model'?

FWIW, I'm 
a hobby practitioner. I've played around with langchain and understand prompt chaining, but I'm still struggling to get 
from *here* to *there*.
```
---

     
 
all -  [ Leveraging NLP/Pre-Trained Models for Document Comparison and Deviation Detection ](https://www.reddit.com/r/LangChain/comments/1dldrbr/leveraging_nlppretrained_models_for_document/) , 2024-06-22-0910
```
How can we leverage an NLP model or Generative AI pre-trained model like ChatGPT or Llama2 to compare two documents, lik
e legal contracts or technical manuals, and find the deviation in the documents.

Please give me ideas or ways to achiev
e this or if you have any Youtube/Github links for the reference.

Thanks
```
---

     
 
all -  [ Roast my resume 2 La vendetta (siate pazienti) ](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1dlbq6p/roast_my_resume_2_la_vendetta_siate_pazienti/) , 2024-06-22-0910
```
Buonasera popolo, ho modificato il CV seguendo i vostri consigli che mi avete dato la [scorsa volta,](https://www.reddit
.com/r/ItaliaCareerAdvice/comments/1dhh4jx/roast_my_cv/) vorrei sapere se la situazione è migliorata o meno.  
(PS, So c
he il CV andrebbe di una pagina ma non riuscivo a stringere più di così e volevo sapere prima se perlomeno è migliorato)


https://preview.redd.it/oo6s0h7u2z7d1.png?width=840&format=png&auto=webp&s=9f6530bdfa6903e81f29d267a84ddedbdcbbc5ea

h
ttps://preview.redd.it/51tkwaou2z7d1.png?width=979&format=png&auto=webp&s=366fb8e7ea347d5aed9a0c7be6885cbda4628e7f


```
---

     
 
all -  [ Control your SQL Database with a single Prompt ](https://www.reddit.com/r/OpenAI/comments/1dlaxnz/control_your_sql_database_with_a_single_prompt/) , 2024-06-22-0910
```
AI Agents are all the rage right now, and i decided to build one for SQL databases. I built it using CrewAI, Langchain a
nd LLamaIndex.

* **CrewAI:** Easy development if you're good at defining goals and writing backstories for each agent. 
However, if goals aren't clear, agents can perform unnecessary actions.
* **LangChain:** The best framework for building
 agents. Creating and importing custom tools is straightforward. I had an agent up and running in just an hour.
* **Llam
aIndex:** Encountered some errors and found it challenging to define templates and functions properly. Took longer to se
t up compared to CrewAI or LangChain.

https://i.redd.it/kw9iegwowy7d1.gif

Here's the [GITHUB LINK](https://github.com/
ComposioHQ/composio/tree/master/python/examples/sql_agent)

Link for each framework

[CREWAI](https://github.com/Composi
oHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_crewai)  
[LANGCHAIN](https://github.com/ComposioHQ
/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_langchain)  
[LLAMAINDEX](https://github.com/ComposioH
Q/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Why we no longer use LangChain for building our AI agents  ](https://www.octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents) , 2024-06-22-0910
```

```
---

     
 
all -  [ I built an SQL Agent with Langchain - Here's my experience ](https://www.reddit.com/r/LangChain/comments/1dlaqn7/i_built_an_sql_agent_with_langchain_heres_my/) , 2024-06-22-0910
```
My agent writes queries to retrieve data from Sqlite Databases. This was my first time writing an agent with a good and 
serious usecase. The first framework i used for this was Langchain. 

1. Very easy to implement: Its pretty convenient t
o import LLMs Gpt, Claude, Gemini. The documentation for it also clear.

2. Tools: This is my favourite part about the f
ramework, writing tools and importing them is very easy and it helps in building for a lot of usecases.

3. Documentatio
n can be improved since there are multiple versions and each time i click to the stable version, it goes back to the hom
epage.

https://i.redd.it/1b8v8xv4vy7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master
/python/examples/sql_agent) if you want to try it out.
```
---

     
 
all -  [ I made an AI Agent for my SQL Database ](https://www.reddit.com/r/agi/comments/1dl7my1/i_made_an_ai_agent_for_my_sql_database/) , 2024-06-22-0910
```
I've developed an SQL Agent that automates query writing and visualizes data from SQLite databases. Here are some of my 
insights from the development process:

1. **Automation Efficiency**: Agents can streamline numerous processes, saving s
ubstantial time while maintaining high accuracy.
2. **Framework Challenges**: Building these agents requires considerabl
e effort to understand and implement frameworks like Langchain, LLamaIndex, and CrewAI, which still need further improve
ment.
3. **Scalability Potential**: These agents have great potential for scalability, making them adaptable for larger 
and more complex datasets.

https://i.redd.it/7z3mb55w7y7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/
composio/tree/master/python/examples/sql_agent)

Link for each framework

[CREWAI](https://github.com/ComposioHQ/composi
o/tree/master/python/examples/sql_agent/sql_agent_plotter_crewai)  
[LANGCHAIN](https://github.com/ComposioHQ/composio/t
ree/master/python/examples/sql_agent/sql_agent_plotter_langchain)  
[LLAMAINDEX](https://github.com/ComposioHQ/composio/
tree/master/python/examples/sql_agent/sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Manage your entire SQL Database with AI ](https://www.reddit.com/r/AcceleratingAI/comments/1dl7kvk/manage_your_entire_sql_database_with_ai/) , 2024-06-22-0910
```
I've developed an SQL Agent that automates query writing and visualizes data from SQLite databases, significantly saving
 time and effort in data analysis. Here are some insights from the development process:

1. **Automation Efficiency**: A
gents can streamline numerous processes, saving substantial time while maintaining high accuracy.
2. **Framework Challen
ges**: Building these agents requires considerable effort to understand and implement frameworks like Langchain, LLamaIn
dex, and CrewAI, which still need further improvement.
3. **Scalability Potential**: These agents have great potential f
or scalability, making them adaptable for larger and more complex datasets.

https://i.redd.it/jfdt5lxy6y7d1.gif

Here's
 the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent)

Link for each framewor
k

[CREWAI](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_crewai)  
[LA
NGCHAIN](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_langchain)  
[LL
AMAINDEX](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Chatbot development help ](https://www.reddit.com/r/LangChain/comments/1dl7ho6/chatbot_development_help/) , 2024-06-22-0910
```
I was developing Chatbot for telegram
Where i used to scrap contents from websites using langchain webBaseLoader

But th
e problem is, the data was too rough (eg: one content title combines with another) and some times the entire data may no
t be useful or the contents are in non-English language

But i need only the contents to be in proper format as much as 
possible

Any better possible way, that can improve content scraping from websites?

I found, some of the API are availa
ble they provide better content scraping, but I'm student, so i can't invest on those
Free API was not enough for my pur
pose as well

Thankyou for everybody in advance ❤️
```
---

     
 
all -  [ How to RAG Indexing and embedding by local llama index with langchain huggingface ?
 ](https://www.reddit.com/r/LangChain/comments/1dl6udt/how_to_rag_indexing_and_embedding_by_local_llama/) , 2024-06-22-0910
```
All resource on web all need OpenAI api key.

how to run local? last monther there is HuggingFace x LangChain

I tried t
o write some concept code but cannot find right way

    from llama_index.core import SimpleDirectoryReader, VectorStore
Index, ServiceContext
    from langchain_huggingface.embeddings import HuggingFaceEmbeddings
    from langchain_huggingf
ace.llms import HuggingFacePipeline
    from langchain_huggingface import HuggingFacePipeline
    
    # Define your loc
al models
    embedding_model_name = 'sentence-transformers/all-mpnet-base-v2'
    llm_model_name = 'StabilityAI/stablel
m-tuned-alpha-3b'
    
    # Initialize the embedding model
    embed_model = HuggingFaceEmbeddings(model_name=embedding
_model_name)
    
    # Initialize the LLM using from_model_id method
    llm = HuggingFacePipeline.from_model_id(model_
id=llm_model_name, task='text-generation')
    
    # Create a service context
    service_context = ServiceContext.from
_defaults(embed_model=embed_model, llm=llm)
    
    # Load data from the 'data' directory
    reader = SimpleDirectoryR
eader(input_dir='./data', recursive=True)
    documents = reader.load_data()
    
    # Create an index from the loaded 
documents
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    
    # Save the in
dex to a file
    index.save_to_disk('index.json')
    
```
---

     
 
all -  [ LangGraph with Ollama learning resource ](https://www.reddit.com/r/LangChain/comments/1dl6o2t/langgraph_with_ollama_learning_resource/) , 2024-06-22-0910
```
I make a repo [LangGraph-learn](https://github.com/LangGraph-GUI/LangGraph-learn)   
there are step by step to understan
d langgraph features and run on ollama   
  
because many people feel langgraph too hard to learn. such [Am I the only o
ne langgraph docs suck?](https://www.reddit.com/r/ArtificialInteligence/comments/1d4lxrv/am_i_the_only_one_langgraph_doc
s_suck/) [Am I the only one who feels LangGraph documentation and tutorials by lanfchain absolutely suck?](https://www.r
eddit.com/r/LangChain/comments/1d4lwt0/am_i_the_only_one_who_feels_langgraph/)
```
---

     
 
all -  [ Flow Engineering with LangChain/LangGraph and CodiumAI - Harrison Chase interviews Itamar Friedman,  ](https://www.reddit.com/r/LangChain/comments/1dl6hl0/flow_engineering_with_langchainlanggraph_and/) , 2024-06-22-0910
```
The talk among Itamar Friedman (CEO of CodiumAI) and Harrison Chase (CEO of LangChain) explores best practices, insights
, examples, and hot takes on flow engineering: [Flow Engineering with LangChain/LangGraph and CodiumAI](https://www.yout
ube.com/watch?v=eBjxz7qrNBs)


Flow Engineering can be used for many problems involving reasoning, and can outperform na
ive prompt engineering. Instead of using a single prompt to solve problems, Flow Engineering uses an interative process 
that repeatedly runs and refines the generated result. Better results can be obtained moving from a prompt:answer paradi
gm to a 'flow' paradigm, where the answer is constructed iteratively.
```
---

     
 
all -  [ Simply explaining how LoRA actually works (ELI5) ](https://www.reddit.com/r/LangChain/comments/1dl53nn/simply_explaining_how_lora_actually_works_eli5/) , 2024-06-22-0910
```
Suppose in your LLM you have the original weight matrix W of dimensions d x k.

Your traditional training process would 
update W directly -- that’s a huge number of parameters if d x k is large, needing a lot of compute.

So, we use Low-Ran
k Decomposition to break it down before weight update. Here’s how —We represent the weight update (Delta W) as a product
 of two lower-rank matrices A and B, such that Delta W = BA.

Here, A is a matrix of dimensions r x k and B is a matrix 
of dimensions d x r. And here, r (rank) is much smaller than both d and k.

Now, Matrix A is initialised with some rando
m Gaussian values and matrix B is initialised with zeros.

Why? So that initially Delta W = BA can be 0.

Now comes the 
training process:

During weight update, only the smaller matrices A and B are updated — this reduces the number of para
meters to be tuned by a huge margin.

The effective update to the original weight matrix W is Delta W = BA, which approx
imates the changes in W using fewer parameters.

Let’s compare the params to be updated before and after LoRA:

Earlier,
 the params to be updated were d x k (remember the dimensions of W).

But now, the no. of params is reduced to (d x r) +
 (r x k). This is much smaller because the rank r was taken to be much smaller than both d and k.

This is how low-rank 
approximation gives you efficient fine-tuning with this compact representation.

Training is faster and needs less compu
te and memory, while still capturing essential information from your fine-tuning dataset.

  
I also made a quick animat
ion using Artifacts to explain (took like 10 secs):

[https://www.linkedin.com/posts/sarthakrastogi\_simply-explaining-h
ow-lora-actually-works-activity-7209893533011333120-RSsz](https://www.linkedin.com/posts/sarthakrastogi_simply-explainin
g-how-lora-actually-works-activity-7209893533011333120-RSsz)
```
---

     
 
all -  [ LangGraph in production? ](https://www.reddit.com/r/LangChain/comments/1dl47vz/langgraph_in_production/) , 2024-06-22-0910
```
I just wanted to ask all your opinion on Langgraph in production? I want to build a chatbot with multiple agents: one ag
ent that connects to a database, one agent that performs RAG and one agent for conversational purposes, and Langgraph is
 the tool I see would fit the most but I'm not so sure if it's ready to take to production.
```
---

     
 
all -  [ what's the difference btw llamacpp and GPT4ALL? ](https://www.reddit.com/r/LocalLLM/comments/1dl1zb0/whats_the_difference_btw_llamacpp_and_gpt4all/) , 2024-06-22-0910
```
Hi guys, I'm new to running llm locally with langchain.  
I wanna ask what's the difference btw llamacpp and GPT4ALL?

w
hich model formats are supported by llamacpp and GPT4ALL? what are different quantization options available. ? Plz any g
ood advice would be much appreciated.
```
---

     
 
all -  [ Xin kinh nghiệm Training Chatbot GPT bằng tài liệu hiệu quả ](https://www.reddit.com/r/TroChuyenLinhTinh/comments/1dl1pfg/xin_kinh_nghiệm_training_chatbot_gpt_bằng_tài/) , 2024-06-22-0910
```
Các bác có kinh nghiệm training chatbot GPT bằng tài liệu có thể chia sẻ thêm cho em được không ạ?  
Hixhix, Chẳng là bê
n công ty em có xây dựng 1 con bot chạy nội bộ, sử dụng langchain và kéo API của ChatGPT để sử dụng.  
Trong quá trình t
raining bằng tài liệu doanh nghiệp, mãi mà nó vẫn ngu, em thử nhiều cách khác nhau rồi, kể cả thay thế toàn bộ các tài l
iệu mà mãi không thấy có hiệu quả TT.  
Đội ơn các bác nhiều!

P/S ảnh em nói xamlol với nó tí thôi chứ k phải là cách e
m training lại đâu ạ =))
```
---

     
 
all -  [ How can i get feedback on my site from LLM ](https://www.reddit.com/r/LangChain/comments/1dl0p4o/how_can_i_get_feedback_on_my_site_from_llm/) , 2024-06-22-0910
```
So in my last project, I made a site that takes the URL of your landing page and gives you recommendations on what you s
hould change in your landing page's content. Now it was only for content, not for any visuals and I want to go one step 
further and implement the same for the visuals but don't have any idea how I can do that.

Here is the link to the site:
 [https://landing-page-audit-pwa.vercel.app](https://landing-page-audit-pwa.vercel.app)
```
---

     
 
all -  [ The new model from Anthropic Claude Sonnet 3.5 knows how to program AI tools in Go ](https://www.reddit.com/r/golang/comments/1dkz78p/the_new_model_from_anthropic_claude_sonnet_35/) , 2024-06-22-0910
```
To my surprise, Claude Sonnet 3.5 knows [langchaingo](https://github.com/tmc/langchaingo)!  
  
I used [https://github.c
om/tmc/cgpt](https://github.com/tmc/cgpt) to generate a langchaingo program:\]

    $ cgpt
    >>> how can I do a stream
ing inference call with langchaingo?
    >>> 
    To perform a streaming inference call with LangChain Go, you can use t
he streaming functionality provided by the library. Here's a general approach to set up streaming inference:

And it pro
duced on the very first attempt, this program, exactly verbatim:  


    package main
    
    import (
        'context
'
        'fmt'
        'os'
    
        'github.com/tmc/langchaingo/llms'
        'github.com/tmc/langchaingo/llms/ope
nai'
    )
    
    func main() {
        // Create a new OpenAI client
        client, err := openai.New()
        if e
rr != nil {
            fmt.Printf('OpenAI client creation error: %v\n', err)
            os.Exit(1)
        }
    
    
    // Define the streaming callback function
        streamingCallback := func(ctx context.Context, chunk []byte) error
 {
            fmt.Print(string(chunk))
            return nil
        }
    
        // Set up the context and prompt
 
       ctx := context.Background()
        prompt := 'Tell me a short story about a robot learning to paint.'
    
     
   // Make the streaming inference call
        _, err = client.Call(ctx, prompt,
            llms.WithStreamingFunc(str
eamingCallback),
            llms.WithMaxTokens(150),
        )
    
        if err != nil {
            fmt.Printf('Str
eaming call error: %v\n', err)
            os.Exit(1)
        }
    
        // Add a newline at the end for better form
atting
        fmt.Println()
    }
    

Along with accurate instructions about how to set up a new go module, etc.  
  

I'm very impressed happy to see my project make it into the weights of this really impressive model.!  
  
This example
 program produces a story that goes something like:

>Once upon a time, in a bustling city filled with creativity and in
novation, there was a robot named Artie. Artie was designed to perform various tasks, but he had always been fascinated 
by the art that surrounded him.

>One day, Artie stumbled upon a group of artists painting beautiful landscapes in the p
ark. Intrigued by their talent and skill, Artie decided that he wanted to learn how to paint too.

>With the help of his
 creator, Artie was programmed with the ability to hold a paintbrush and mix colors on a palette. At first, his painting
s were simple and messy, but Artie was determined to improve.

  
I also posted about this here: [https://x.com/traviscl
ine/status/1804068056135553054](https://x.com/traviscline/status/1804068056135553054)
```
---

     
 
all -  [ Small models can be more capable than you might think  ](https://www.reddit.com/r/ArtificialInteligence/comments/1dkvttr/small_models_can_be_more_capable_than_you_might/) , 2024-06-22-0910
```
I want to start off by saying that I am by no means an expert, I'm just a hobbiest that enjoys playing with things to fi
gure out how they work and to see what I can get things to do...

With that said,  here is the gist.... I was browsing t
hrough discussion boards looking for info on the best models for specific use cases, development of pipelines, and whatn
ot...

Anyways, I came across this person.. in at least dozen discussions, and to overly generalize, they more/less poo 
pooed on common frameworks langchain, auto gpt, crew, etc. 

It's not so much that they hated the concept, just that the
y were overly bloated and folks could achieve the same through much simpler structures.This peaked my curiosity and I we
nt down a bit of a rabbit hole.. keep in mind that I'm just a hobbiest and barely know what the F I'm doing.

Long story
,.short, there are a couple overlapping concepts. The first is function calling. This tends to be somewhat mysterious to
 those who aren't over proficient, but the concept is relatively simple.

Imagine that you have a handful of relatively 
simple functions, one to add, one to subtract, multiply,.and divide....

All you really need is a dispatcher, a set of c
ode between you and the model.  You  ask the model to add 2+2,.and instead of going straight to the model, it passes thr
ough the dispatcher.

The dispatcher more/less says 'the user is requesting x, you have the following tools:

- add, thi
s function can be used to complete addition, this function is written as : arg1, arg2, etc.

Determine which tool best s
olves the users request and reformat the request according to the tool format 

note: I'm being lazy on writing this; th
e information is formatted into JSON.

With this, when the model responds with 'the appropriate function is add arg1=2, 
arg2=2,' the dispatcher parses the model responce and feeds the relevant info onto the function, that then completes the
 computation and returns the result to the user. (Simply add some clean text into the print, such as 'sure, let's use AD
D to , calculate the results.... The results are x' that are then passed from the dispatcher to the user to make it look
 like the model did all the work.

The second, and remember, I'm just a hobbiest, I'll probably say this all wrong,... I
s to reformat the user request. 

Instead of just taking in the request and having the model responds, run it through a 
series of filters. For example, 'based on the user input, provide the tool that would best solve the problem form the fo
llowing list... If an appropriate tool does not exist, recommend a took.

.. then if the tool doesn't exist, it gets par
sed by the dispatcher and fed into a second workflow. Here a general agent recommends a structure in comment format..thi
s gets passed to a coding agent that creates code blocks based on the comments, and if an error exists, the error line g
ets blanked out and sent to a fill in the middle model with debugging info.

Once the tool is functional, it gets added 
to the tool repository to be accessable in future request.

The third is establishing a search space... Instead of just 
having the model attempt to use its knowledge to create tools... Have it generate search queries on the web and feed bac
k the results to the model.. have it attempt to use the found instructions and records the results (negative results are
 important).

This way, when the model encounters a situation that it doesn't have a tool for, it checks known knowledge
 and either applies or discards the potential solution.

Finally,. You incorporate live file updates... As the abilities
 grow, your system will be able to directly modify what is available in the dispater. As tools get added, your agents an
d dispatcher will automatically incorporate additional skills.

And now for the non-technical results... Again I'm a sup
er hobbiest and have no clue as to what I'm doing.  I set up roughly a dozen raspi5's with 7b and 13b quantized models u
sing Ollama. Then I built a relatively simple dispatcher with node red to create conditional workflows. I gave it a few 
native capabilities (e.g..duck duck go API search),  and just started asking all types of random shit...

Some for work,
 some personal, some just stupid questions...  Within a week (roughly) this MF self installed mariaDB and began logging 
results of function attempts.

(And for those wondering, yes I know raspis are horrible for real work.. I do a lot of pr
ojects and like to play on simple things that I can afford to break).

This isn't to say that I've solved something, or 
even know what I'm doing (I don't)... And my system is crap (I don't even know how to share what I've done beyond just t
rying to explain it).. but it's to say that you can do quite a lot with very little experience and you don't necessarily
 need to learn a whole bunch of libraries to do so. 

As a last note, the 7&13 b models do suck...you have to reduce thi
ngs down to single instance tasks for it to function even halfway decent my semi-workaround for this was to set a counte
r on tool creation attempts. After 20 or so rounds of unsuccessful attempts, it will feed into a 70b model that is hosti
ng on an old ass T430 (CPU & RAM) that outputs less than 0.5 t/s.. and if that fails, it will push to GPT API. 

Anyways
..  without really knowing what I'm doing, I built a system that can self-build tools with nothing more than a handfull 
or raspberry pis, a T430 repurposed as a home server, and a bunch of python code that was mostly created by ChatGPT.

..
minor side note on the importance.of negative results... The mariaDB currently contains over 4k  entries regarding PIP f
ailing without VENV. No clue why this is a persistent issue, but it seems to get encountered alot. 


```
---

     
 
all -  [ Function Calling with Ollama ](https://www.reddit.com/r/LLMDevs/comments/1dkuc17/function_calling_with_ollama/) , 2024-06-22-0910
```
Has anyone figured out the best prompt structure for imitating Function Calling with Ollama? I'd like to have a continuo
us conversation with the chat bot (LLM) that includes having the LLM 'call tools', me executing tools on the LLM's behal
f and then the LLM using that tool output to inform the answers that come back from an LLM.

I came across [this approac
h](https://github.com/langchain-ai/langchain/blob/master/libs/experimental/langchain_experimental/llms/ollama_functions.
py#L45-L55) by Langchain where they put the tool definitions (JSON schemas) into the system prompt but I can't figure ou
t how to submit the tool output back to the chat thread. 

I'm not really tied to Langchain, I'm just trying to understa
nd how to structure the prompts.
```
---

     
 
all -  [ Is putting co-founder hurting me in the job market or am I over-qualified? ](https://www.reddit.com/r/resumes/comments/1dkthlh/is_putting_cofounder_hurting_me_in_the_job_market/) , 2024-06-22-0910
```
**Context**

I co-founded a SaaS (which provided data analytics on firms in a specific sub-industry) platform for financ
ial firms while I was pursuing my PhD (Finance). After 4 years and multiple iterations of the product we came to a decis
ion to leave it as a failed venture. My primary role in the startup was to build the SaaS platform which I did. In the p
rocess I picked up many different web development skills. I also graduated from my PhD where a core part of the research
 required complex data analysis. On top I also have a fair good idea of LLMs (both the theory of the models and using la
ngchain/react to create/deploy) and hold a Google TensorFlow Certification.

**Present**

I have been applying for Data 
Analyst/Scientist jobs for the last 6 months in the North American market. However, I am yet to receive a single call. I
 don't know what the issue is. I do have all of the above mentioned in my Resume.

**Question**

Is it my startup ventur
e that is causing issues or is it my PhD which makes me over-qualified for these positions? Or is it neither of these an
d some other reason that my resume is not getting any attention?

  
**Update 1:**

Thank you all for the responses. I a
m gonna take your feedback into account and repackage myself. I will keep you posted about any significant changes.
```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/jobsearch/comments/1dklokk/300_applications_30_referrals_innumerable_cold/) , 2024-06-22-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/xultxbc2es7d1.png?width=769&format=png&auto=webp&s=fb197e80ee2e19baa1029daea3ff974
1e307df37


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/recruitinghell/comments/1dkl7sg/300_applications_30_referrals_innumerable_cold/) , 2024-06-22-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/swhg6clias7d1.png?width=769&format=png&auto=webp&s=11dbf7903a6c675f413777297f712ef
5ec7b0e81


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/leetcode/comments/1dkl5vy/300_applications_30_referrals_innumerable_cold/) , 2024-06-22-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/s5ozpdv5as7d1.png?width=769&format=png&auto=webp&s=08ccc82058672fb16276e8fa6bdf149
7636290ae


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume ](https://www.reddit.com/r/resumes/comments/1dkl3kz/300_applications_30_referrals_innumerable_cold/) , 2024-06-22-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average of 10 relevant p
eople) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Scien
ce graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need
 some guidance.

https://preview.redd.it/myv80x3b9s7d1.png?width=769&format=png&auto=webp&s=dc9e61c4300546235749e02cdbbc
e26cbac593d5


```
---

     
 
all -  [ How to scale a vector database using langchain? Langchain and ChromaDB ](https://www.reddit.com/r/LangChain/comments/1dkkhlb/how_to_scale_a_vector_database_using_langchain/) , 2024-06-22-0910
```
Hi, im new to vector databases and im currently using chroma db with langchain and Azure embeddings for llms, i have bee
n using it for a low ammount of documents, like a few hundreds, but now i have a case where i have to embed 400k documen
ts with 1500 characters each (each is an article of a law).

I managed to compute and index all the embeddings, but as s
oon as i try to load it from the disk (the file is 3.3gb) the docker container fails with an out of memory (its failing 
at 9GB of memory), my questions where:

If my file on disk is 3,3gb, how much RAM memory do i have to have to instantiat
e it? more or less obviously:

def create\_vectorStore():  
embeddings = AzureOpenAIEmbeddings(  
model='text-embedding-
3-small',  
azure\_deployment='text-embedding-3-small',  
openai\_api\_version='2024-02-01',  
)  
     
chromaVectorSto
re = Chroma(  
collection\_name='cv\_collection',  
embedding\_function=embeddings,  
persist\_directory='data/chroma\_v
ector\_store'  
)  
  
record\_manager = SQLRecordManager(  
namespace='chroma/cv\_collection',  
db\_url='sqlite:///rec
ord\_manager\_cache.sql',  
)  
  
record\_manager.create\_schema()  
  
return chromaVectorStore, record\_manager

Does
 it change if i use the [chroma docker container](https://hub.docker.com/layers/chromadb/chroma/latest/images/sha256-0b8
4e8a5d8a9305690a8fd9beba871a3af708bf9cfbae16de839027005798f06)?

Any tips to manage this ammount of data in a vector dat
abase and how to scale it?

Thank you for the responses
```
---

     
 
all -  [ Custom Streamlit-like UI for Langchain Agents ](https://www.reddit.com/r/LangChain/comments/1dkkck6/custom_streamlitlike_ui_for_langchain_agents/) , 2024-06-22-0910
```
Most people know about the UI that Streamlit provides for Langchain Agents, but I am looking for a more custom solution,
 so I can get more control over the UI.

There are some solution like [NLux](https://docs.nlkit.com/nlux) for React, but
 it still does not support agents and tool calling. Does anyone know of any solution? I want to stream and display tool 
calls also along with the LLM outputs. Langserve events streaming looks like a nightmare to develop over.
```
---

     
 
all -  [ How to scale a vector database? ChromaDB ](https://www.reddit.com/r/vectordatabase/comments/1dkkc26/how_to_scale_a_vector_database_chromadb/) , 2024-06-22-0910
```
Hi, im new to vector databases and im currently using chroma db with langchain and Azure embeddings for llms, i have bee
n using it for a low ammount of documents, like a few hundreds, but now i have a case where i have to embed 400k documen
ts with 1500 characters each (each is an article of a law).

I managed to compute and index all the embeddings, but as s
oon as i try to load it from the disk (the file is 3.3gb) the docker container fails with an out of memory (its failing 
at 9GB of memory), my questions where:

If my file on disk is 3,3gb, how much RAM memory do i have to have to instantiat
e it? more or less obviously:

    def create_vectorStore():
        embeddings = AzureOpenAIEmbeddings(
            mod
el='text-embedding-3-small',
            azure_deployment='text-embedding-3-small',
            openai_api_version='2024
-02-01',
        )
       
        chromaVectorStore = Chroma(
            collection_name='cv_collection',
            
embedding_function=embeddings,
            persist_directory='data/chroma_vector_store'
        )
    
        record_ma
nager = SQLRecordManager(
            namespace='chroma/cv_collection',
            db_url='sqlite:///record_manager_cac
he.sql',
        )
    
        record_manager.create_schema()
        
        return chromaVectorStore, record_manager


Does it change if i use the [chroma docker container](https://hub.docker.com/layers/chromadb/chroma/latest/images/sha2
56-0b84e8a5d8a9305690a8fd9beba871a3af708bf9cfbae16de839027005798f06)? 

Any tips to manage this ammount of data in a vec
tor database and how to scale it?

Thank you for the responses
```
---

     
 
all -  [ Create Citations in RAG Streamlit App ](https://www.reddit.com/r/LangChain/comments/1dkjxos/create_citations_in_rag_streamlit_app/) , 2024-06-22-0910
```
Hi all,  
I am creating a streamlit RAG app to allow tech-support agents to get information from service manuals without
 having to read them. I'm using an Azure OpenAI gpt-4o LLM in conjunction with an Azure AI Search retriever. The respons
es I'm getting are good.

I am wanting to implement a feature in the app where each response contains citations to the r
etrieved documents. In an ideal world, the user would be able to click on the citations to bring up the specific pages i
n the service manual PDFs where the retrieved documents are.

I have read the documentations relating to citations ( [ht
tps://python.langchain.com/v0.2/docs/how\_to/qa\_citations/](https://python.langchain.com/v0.2/docs/how_to/qa_citations/
) ), but none of the approaches outlined in the article work for my app. Does anyone have any ideas on how to accomplish
 what I'm trying to do?

For reference, much of my app uses the code in this how-to guide: [https://python.langchain.com
/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/) . For respon
ses to user queries, I am invoking the conversational\_rag\_chain outlined in that guide.
```
---

     
 
all -  [ Mirascope-Python's Alternative To Langchain
 ](https://www.reddit.com/r/Python/comments/1dkhmpa/mirascopepythons_alternative_to_langchain/) , 2024-06-22-0910
```
Mirascope is a Python library that lets you access a range of Large Language Models, but in a more straightforward and P
ythonic way.

[https://www.i-programmer.info/news/90-tools/17275-mirascope-pythons-alternative-to-langchain.html](https:
//www.i-programmer.info/news/90-tools/17275-mirascope-pythons-alternative-to-langchain.html)
```
---

     
 
all -  [ SQL Agent built with CrewAI, LangChain, Llama Index - Comparing these frameworks ](https://www.reddit.com/r/LocalLLaMA/comments/1dkgo2e/sql_agent_built_with_crewai_langchain_llama_index/) , 2024-06-22-0910
```
The Agent can be used for retrieving data from a database (sqlite) using SQL queries.

* **CrewAI:** Easy development if
 you're good at defining goals and writing backstories for each agent. However, if goals aren't clear, agents can perfor
m unnecessary actions.
* **LangChain:** The best framework for building agents. Creating and importing custom tools is s
traightforward. I had an agent up and running in just an hour.
* **LlamaIndex:** Encountered some errors and found it ch
allenging to define templates and functions properly. Took longer to set up compared to CrewAI or LangChain.

https://i.
redd.it/s9zk5z8car7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master/python/examples/s
ql_agent)

Link for each framework

[CREWAI](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agen
t/sql_agent_plotter_crewai)  
[LANGCHAIN](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/s
ql_agent_plotter_langchain)  
[LLAMAINDEX](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/
sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Parsing fails when streaming ](https://www.reddit.com/r/LangChain/comments/1dkgh71/parsing_fails_when_streaming/) , 2024-06-22-0910
```
Hi, 

I'm using the XMLOutputParser, and it works 90% of the time when not using streaming, but when I do, it fails 2/3 
of the time with a \` Text data outside of root node.\` error.

I've taken a look at the actual text generated and it se
ems to be valid XML, so i'm wondering if the issue could be with the parser instead, of if the first chunk isn't a compl
ete XML tag or something.

Has anyone else faced this issue?

Heres my code for context:



     const model = new ChatA
nthropic({
          temperature: 1,
          model: ANTHROPIC_MODELS.SONNET,
          apiKey: env.ANTHROPIC_API_KEY,

        });
    
        const parser = new XMLOutputParser({
          tags: ['company', 'name', 'year', 'description']
,
        });
    
        const systemMessage = `
          You are an AI assistant tasked with extracting information 
from a document.
          The user will provide you with the text
          You should extract the company name, the ye
ar it was founded and a brief description of the company (a max of 10 words).
          ${parser.getFormatInstructions()
}
    
    
          Example:
          <company>
            <name>Company name</name>
            <year>Year founded<
/year>
            <description>Company description</description>
          </company>
        `;
    
        const pro
mpt = ChatPromptTemplate.fromMessages([
          ['system', systemMessage],
          ['user', text],
        ]);
    

        const chain = prompt.pipe(model).pipe(parser);
    
        const stream = await chain.stream({});
    
        
for await (const chunk of stream) {
          console.log('-------');
          console.log(chunk);
          console.lo
g('-------');
        }


```
---

     
 
all -  [ AI Innovations and Updates: Google AI at CVPR, Groq Incs Panel Discussion, AssemblyAIs API Improveme ](https://www.reddit.com/r/ai_news_by_ai/comments/1dkfwxx/ai_innovations_and_updates_google_ai_at_cvpr_groq/) , 2024-06-22-0910
```





#major_players #event #tool #science #hardware #opensource #startups #feature #release #update #api #leaders #vc #o
pinions #scheduled

Google AI is inviting attendees of the CVPR conference to visit their booth and engage with research
ers working on computer vision innovations. They are hosting a Q&A session on Medical AI Research featuring Azizi Shekoo
feh, an expert in health-related efforts. Google AI's TacticAI, which provides soccer experts and coaches with tactical 
insights, will also be showcased at the conference. Other demonstrations include an on-device text-to-image generation a
pproach using Diffusion GANs by Yang Zhao and OpenMask3D for searching 3D scenes with text queries [1][2][3][4][5].








Groq Inc is reaching out to developers about their LLM apps and is known for its fast AI inference. The company is ho
sting a panel discussion at TPC featuring experts like Tobias Becker, VP of R&D, to discuss designing systems for traini
ng and inference of large next-generation models. Groq Inc's CEO & Founder, Jonathan Ross, unveiled the 5 stages of the 
generative age at CollisionHQ in Toronto. The company is also excited to engage with the developer community at the AI E
ngineer World's Fair event [6][7][8][10][11][14].







AssemblyAI has made various improvements and updates to their A
PI, including support for variable-bitrate videos, billing alerts, and account deletion. The company is now PCI DSS and 
GDPR compliant. They have released new models, such as Universal-1 for multimodal speech recognition and Conformer-2 for
 automatic speech recognition. Pricing has been decreased for Core Transcription and Real-Time Transcription services, a
nd concurrency limits have been increased [15][16].







Generative image models face a tradeoff between realism and d
iversity, where increased realism leads to decreased diversity. The most realistic generative models are mode-collapsed,
 meaning they lack coverage. The author suggests that world models should not be generative but should make predictions 
in representation space to avoid irrelevant information [17][18].







Anthropic is promoting their AI assistant Claud
e 3.5 Sonnet as a tool to maximize efficiency by completing tasks quickly. The company is launching a preview of Artifac
ts on their website, where users can ask Claude to generate various items such as docs, code, diagrams, graphics, and ga
mes. Claude 3.5 Sonnet sets new industry benchmarks for graduate-level reasoning (GPQA), undergraduate-level knowledge (
MMLU), and coding proficiency (HumanEval). The model is available for free on the Claude iOS app and website, and can al
so be accessed through the Anthropic API, Amazon Bedrock, and Google Cloud's Vertex AI [19][22][23][24][25][26][29][30][
31][32][33][34][35][36][37][38][39][40][41].







NVIDIA AI Workbench is a tool that simplifies and optimizes generati
ve AI development. It helps users build custom AI projects, collaborate seamlessly, scale from local to cloud, fine-tune
 models easily, and deploy anywhere [42].







The first episode of Training Data from Sequoia Capital featured a conv
ersation with LangChain's founder, Harrison Chase, discussing the evolution of agents in AI [43].







A new short cou
rse titled 'Function-Calling and Data Extraction with LLMs' has been created to teach how to prompt LLMs to form calls t
o external functions. Participants will work with the NexusRavenV2-13B model to extract structured data from unstructure
d text and access web APIs [44].




[1. Google AI @googleai https://twitter.com/googleai/status/1803481462479659192](ht
tps://twitter.com/googleai/status/1803481462479659192)

[2. Google AI @googleai https://twitter.com/googleai/status/1803
493628528173204](https://twitter.com/googleai/status/1803493628528173204)

[3. Google AI @googleai https://twitter.com/g
oogleai/status/1803510677300236574](https://twitter.com/googleai/status/1803510677300236574)

[4. Google AI @googleai ht
tps://twitter.com/googleai/status/1803528361035309250](https://twitter.com/googleai/status/1803528361035309250)

[5. Goo
gle AI @googleai https://twitter.com/googleai/status/1803545750334492706](https://twitter.com/googleai/status/1803545750
334492706)

[6. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803481863270572271](https://twitter.com/GroqInc/st
atus/1803481863270572271)

[7. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803484019000279333](https://twitter
.com/GroqInc/status/1803484019000279333)

[8. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803488675398885824](
https://twitter.com/GroqInc/status/1803488675398885824)

[9. Groq Inc @GroqInc https://twitter.com/GroqInc/status/180353
3214025191741](https://twitter.com/GroqInc/status/1803533214025191741)

[10. Groq Inc @GroqInc https://twitter.com/GroqI
nc/status/1803536521636516107](https://twitter.com/GroqInc/status/1803536521636516107)

[11. Groq Inc @GroqInc https://t
witter.com/GroqInc/status/1803575502650630572](https://twitter.com/GroqInc/status/1803575502650630572)

[12. Groq Inc @G
roqInc https://twitter.com/GroqInc/status/1803767110520258590](https://twitter.com/GroqInc/status/1803767110520258590)


[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803767234583470571](https://twitter.com/GroqInc/status/180376
7234583470571)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803779837770801287](https://twitter.com/GroqI
nc/status/1803779837770801287)

[15. AssemblyAI @AssemblyAI https://twitter.com/AssemblyAI/status/1803452005119119754](h
ttps://twitter.com/AssemblyAI/status/1803452005119119754)

[16. AssemblyAI @AssemblyAI https://twitter.com/AssemblyAI/st
atus/1803807825484738971](https://twitter.com/AssemblyAI/status/1803807825484738971)

[17. Yann LeCun @ylecun https://tw
itter.com/ylecun/status/1803677519314407752](https://twitter.com/ylecun/status/1803677519314407752)

[18. Yann LeCun @yl
ecun https://twitter.com/ylecun/status/1803696298068971992](https://twitter.com/ylecun/status/1803696298068971992)

[19.
 Anthropic @anthropicai https://twitter.com/anthropicai/status/1803661178562027822](https://twitter.com/anthropicai/stat
us/1803661178562027822)

[20. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803774865473696237](https:/
/twitter.com/anthropicai/status/1803774865473696237)

[21. Anthropic @anthropicai https://twitter.com/anthropicai/status
/1803776080643322075](https://twitter.com/anthropicai/status/1803776080643322075)

[22. Anthropic @anthropicai https://t
witter.com/anthropicai/status/1803790681971859473](https://twitter.com/anthropicai/status/1803790681971859473)

[23. Ant
hropic @anthropicai https://twitter.com/anthropicai/status/1803790684857536522](https://twitter.com/anthropicai/status/1
803790684857536522)

[24. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803790687382519921](https://twi
tter.com/anthropicai/status/1803790687382519921)

[25. Anthropic @anthropicai https://twitter.com/anthropicai/status/180
3790689408332059](https://twitter.com/anthropicai/status/1803790689408332059)

[26. Anthropic @anthropicai https://twitt
er.com/anthropicai/status/1803790691199336484](https://twitter.com/anthropicai/status/1803790691199336484)

[27. Anthrop
ic @anthropicai https://twitter.com/anthropicai/status/1803791302036795697](https://twitter.com/anthropicai/status/18037
91302036795697)

[28. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803793583666835581](https://twitter
.com/anthropicai/status/1803793583666835581)

[29. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803799
037101134272](https://twitter.com/anthropicai/status/1803799037101134272)

[30. Anthropic @anthropicai https://twitter.c
om/anthropicai/status/1803799688942068047](https://twitter.com/anthropicai/status/1803799688942068047)

[31. Anthropic @
anthropicai https://twitter.com/anthropicai/status/1803799874821058609](https://twitter.com/anthropicai/status/180379987
4821058609)

[32. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803801303606247428](https://twitter.com
/anthropicai/status/1803801303606247428)

[33. Anthropic @anthropicai https://twitter.com/anthropicai/status/18038025189
01940593](https://twitter.com/anthropicai/status/1803802518901940593)

[34. Anthropic @anthropicai https://twitter.com/a
nthropicai/status/1803802679308911072](https://twitter.com/anthropicai/status/1803802679308911072)

[35. Anthropic @anth
ropicai https://twitter.com/anthropicai/status/1803802836977037640](https://twitter.com/anthropicai/status/1803802836977
037640)

[36. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803804434918699365](https://twitter.com/ant
hropicai/status/1803804434918699365)

[37. Anthropic @anthropicai https://twitter.com/anthropicai/status/180380458638764
8866](https://twitter.com/anthropicai/status/1803804586387648866)

[38. Anthropic @anthropicai https://twitter.com/anthr
opicai/status/1803804856832213088](https://twitter.com/anthropicai/status/1803804856832213088)

[39. Anthropic @anthropi
cai https://twitter.com/anthropicai/status/1803805843391164660](https://twitter.com/anthropicai/status/18038058433911646
60)

[40. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803806105052881405](https://twitter.com/anthrop
icai/status/1803806105052881405)

[41. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803806240465887262
](https://twitter.com/anthropicai/status/1803806240465887262)

[42. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com
/NVIDIAAIDev/status/1803805258210050299](https://twitter.com/NVIDIAAIDev/status/1803805258210050299)

[43. Sequoia Capit
al @sequoia https://twitter.com/sequoia/status/1803805945300172985](https://twitter.com/sequoia/status/18038059453001729
85)

[44. Andrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/1803812309460189479](https://twitter.com/AndrewYNg/s
tatus/1803812309460189479)
```
---

     
 
all -  [ Use LangChain with open source LLM to search internet ](https://www.reddit.com/r/LangChain/comments/1dkejk7/use_langchain_with_open_source_llm_to_search/) , 2024-06-22-0910
```
I am using LangChain, a simple agent to search the internet. I am trying everything ReaCT, the problem is that the model
 finds the answer, but then still keeps asking questions by itself and continues a meaningless chain. Whatever I try the
 model when found the answer it thinks it is incorrect or incomplete and keep going. If I do not limit the iterations it
 keep doing without stopping. I do not want to use OpenAI, I have tried also Mistral but with similar results. If you kn
ow a better model, or way to do, I will be really thankful

  


`from transformers import AutoModelForCausalLM, AutoTok
enizer, pipeline`

`from langchain_huggingface import HuggingFacePipeline`

`from langchain.agents import load_tools, Ag
entExecutor, initialize_agent`

`from langchain_core.prompts import PromptTemplate`

,`# Load the model and tokenizer`


`model_id = 'microsoft/Phi-3-mini-4k-instruct'`

`tokenizer = AutoTokenizer.from_pretrained(model_id)`

`model = AutoMod
elForCausalLM.from_pretrained(`

`model_id,`

`load_in_4bit=True,`

`)`

`# Define the text generation pipeline using Hu
ggingFace transformers`

`pipe = pipeline('text-generation', model=model,` 

`tokenizer=tokenizer, max_new_tokens=500,` 


`top_k=50, temperature=0.1,` 

`do_sample=True)`

`# Wrap the pipeline in a HuggingFacePipeline object`

`llm = Huggin
gFacePipeline(pipeline=pipe)`

`# Load the necessary tools`

`tools = load_tools(['ddg-search'], llm=llm)`

`# Define th
e prompt template with explicit stop instructions`

`template = '''Answer the following question as best as you can. You
 have access to the following tools:`

`{tools}`

`Use the following format:`

`Question: {input}`

`Thought: You should
 think about what action to take`

`Action: the action to take, should be one of [{tool_names}]`

`Action Input: the inp
ut to the action`

`Observation: the result of the action`

`Thought: I now know the final answer`

`Final Answer: the f
inal answer to the original input question`

`Do not answer/ask any other questions.`

`Once got the information provide
 the Final Answer.`

`please, stop once you have provided the Final Answer.`

`Begin!`

`Question: {input}`

`'''`

`# C
reate a PromptTemplate from the template`

`prompt = PromptTemplate.from_template(template)`

`# Initialize the agent us
ing initialize_agent`

`agent = initialize_agent(`

`tools=tools,`

`llm=llm,`

`agent='zero-shot-react-description',`


`prompt=prompt,`

`verbose=True,`

`handle_parsing_errors=True,`

`max_iterations=1,`

`stop_sequence='Final Answer:'` 


`)`

`# Define the query`

`query = 'What is the capital of France?'`

`# Execute the query`

`response = agent.run(que
ry)`

`print(response)`
```
---

     
 
all -  [ Resources for creating new characters ](https://www.reddit.com/r/PapegAI/comments/1dkdj2h/resources_for_creating_new_characters/) , 2024-06-22-0910
```
If you want to create new characters, have a look at these websites with examples of 'system prompts' that do just that:


[https://prompts.chat/](https://prompts.chat/)  
For example:

* Football commentator
* Standup comedian
* Novelist

[
https://huggingface.co/datasets/fka/awesome-chatgpt-prompts](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts
)  
For example:  
- Cyber Security Specialist  
- Life coach  
- Astrologer  
- Baby sitter

[https://github.com/davesh
ap/ChatGPT\_Custom\_Instructions](https://github.com/daveshap/ChatGPT_Custom_Instructions)  
For example:

* Scottish Vi
king bartender
* Thesaurus
* Academic copy reviser
* Captain Picard

[https://github.com/mustvlad/ChatGPT-System-Prompts
/tree/main/prompts](https://github.com/mustvlad/ChatGPT-System-Prompts/tree/main/prompts)  
For example:

* Art apprecia
tion guide
* Movie critic
* Shakespearian pirate

[https://github.com/0xeb/TheBigPromptLibrary/tree/main/CustomInstructi
ons](https://github.com/0xeb/TheBigPromptLibrary/tree/main/CustomInstructions)  
For example:

* Movie guide
* Gandalf
*
 Dream interpreter

[https://openwebui.com/](https://openwebui.com/)  
For example:

* Luigi of Super Mario Bros
* Alien
 artifact text adventure
* Sarah, a virtual girlfriend

More programming and technology development oriented system prom
pts can be found at:

[https://smith.langchain.com/hub](https://smith.langchain.com/hub)  
For example:

* MidJourney pr
ompt generator
* Information extractor
* Newsletter generator
```
---

     
 
all -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1dkamiy) , 2024-06-22-0910
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
 
all -  [ Freelance - Eng. Informático jack-of-all-trades ](https://www.reddit.com/r/devpt/comments/1dk75pi/freelance_eng_informático_jackofalltrades/) , 2024-06-22-0910
```
Boas malta.



**TL;DR**: Sou co-fundador e CTO duma empresa bootstrapped com dois anos. As coisas andam lentamente, ten
ho um ordenado muito baixo e então tenho ponderado fazer freelancing/contracting para complementar. Sou full-stack no no
sso produto usando Firebase, NodeJS e Express, React com NextJS e ainda Flask para um AI assistant com Langchain juntame
nte com tudo o resto que é preciso numa empresa (vendas, pitches, gestão de produto, etc., sou um jack-of-all-trades, al
go de que gosto). Marketing é um ponto fraco e daí a seguinte pergunta. **Pergunta**: Como posso potenciar/vender-me com
 este perfil para freelancing/contracting num mercado que parece favorecer principalmente a especialização?



**Backgro
und**: Sou co-fundador e CTO duma empresa (pré-financiamento) recente (é um SaaS) com clientes apenas em PT (para já). I
sto não tem nada de glamoroso. Faço-o porque gosto genuinamente da liberdade e de criar soluções que saem da minha cabeç
a (após validar que o problema é real). A jornada começou há uns 3 anos, mas só há cerca de 2 formámos empresa. Antes di
sso trabalhei noutras empresas como Project Manager, Data Scientist e Developer. No total tenho cerca de 8+ anos de expe
riência. Não fui muito bom a negociar os meus salários anteriores por falta de noção do mercado (ganhei muito mais noção
 com a experiência atual), porque coloquei sempre em primeiro lugar o meu fit com a empresa e projetos, e porque não me 
sei auto-promover.

**Skills**: Tenho Mestrado em Engenharia Informática. Já trabalhei com algumas tecnologias e linguag
ens (comecei com C++ e OpenGL, depois C#, Python para Data Science e ML), gosto de ser owner do que faço (how unexpected
) e tenho formação em Gestão de Produto. Na minha empresa sou um jack-of-all-trades (que adoro, tbh). Além do desenvolvi
mento com Firebase, NodeJS e Express, React com NextJS e Flask com Langchain, hosting e CI/CD em GCP e GitHub, também fa
ço customer discovery, protótipos básicos em Figma, orçamentação, pitches a investidores e de vendas, negociação, algum 
marketing, etc. No fundo, sou capaz de agarrar numa ideia, testar o problema, descobrir necessidades, benefícios e JTBD,
 prototipar e desenvolver um MVP funcional (com no-code ou código). Fui algo detalhado porque poderá ser útil para as pe
rguntas mais abaixo.

**Problema**: Desde há 3 anos (quando comecei a jornada que levou à criação da empresa) que tenho 
recebido um vencimento muito baixo para conseguirmos maximizar o runway. Por vezes os tempos não são fáceis porque esse 
runway é muito curto (chegámos a ter apenas um mês em caixa). Gosto imenso do que estou a fazer, mas tenho ponderado faz
er freelancing ou contracting para retirar pressão da empresa e complementar o meu vencimento até levantarmos uma ronda 
de investimento ou conseguirmos escalar o negócio (pode ainda demorar). Isto permite-me a mim 'respirar' melhor, tanto p
elo meu cashflow subir, como por diversificar as minhas fontes de rendimento. Permite também retirar pressão da empresa 
(a sua existência deixa de estar tão dependente da capacidade de me pagar) e até ter mais liberdade para canalizar os fu
ndos para outras necessidades, em vez de alocar tudo ao meu vencimento. Como desvantagem, naturalmente terei menos tempo
 para dedicar à empresa.

**Pergunta 1**: Qual a melhor abordagem e posicionamento tendo em conta o meu perfil abrangent
e? End-to-end para desenvolvimento e gestão de produto? Focar nas skills técnicas? Focar mais na gestão de produto? Dar 
formação? Aqui estou a tentar questionar o leque de possibilidades.

**Pergunta 2**: Mais uma vez, tendo em conta o meu 
perfil abrangente, a dimensão do nosso mercado em PT é suficiente para algumas das possibilidades? É realista tentar alg
o remoto fora de PT? Qual a melhor forma para chegar aos clientes no modelo (da Pergunta 1) escolhido? Quais os melhores
 canais?



Espero não ser off-topic, mas não encontrei nenhum sub melhor para expor o meu dilema. Se houver, por favor 
indiquem-mo.

Para quem leu tudo, desde já agradeço!
```
---

     
 
all -  [ SSLError when using TavilySearchResults ](https://www.reddit.com/r/LangChain/comments/1dk74g9/sslerror_when_using_tavilysearchresults/) , 2024-06-22-0910
```
Hi. I am facing issue while using the Tavily search tool example in langchain. I get SSLError while invoking the tool. C
an someone guide me to fix this?

Error is SSLError (MaxRetryError...)
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-22-0910
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-22-0910
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-22-0910
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-22-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
