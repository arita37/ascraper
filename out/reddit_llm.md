 
all -  [ [3 YoE] Data Scientist looking for Machine Learning Engineering roles ](https://www.reddit.com/r/EngineeringResumes/comments/1bjqtn6/3_yoe_data_scientist_looking_for_machine_learning/) , 2024-03-21-0911
```
I'm a Data Scientist with 3 YoE,  currently on an H1B visa. I'm interested in transitioning into Machine  Learning Engin
eering roles and would greatly appreciate your feedback on my resume.

I'm seeking new opportunities to move away from c
onsulting and focus on in-house MLE  roles where I can contribute to the development and deployment of impactful ML solu
tions.

My focus has been on building machine learning models and data engineering  infrastructures. I'm particularly dr
awn to Deep Learning, information retrieval, and biodiversity research that has real-world conservation applications.

I
'd appreciate it if you could take a look at my resume and provide feedback. I'm specifically interested in knowing if m
y experience aligns well with MLE  expectations and how I can better highlight my relevant skills.

Thank you in advance
 for your time and insights!

https://preview.redd.it/c29fxxoshkpc1.png?width=5100&format=png&auto=webp&s=09d16cdd1b04d8
47718041ab2acec32283105928
```
---

     
 
all -  [ Human intervention in agent workflows ](https://www.reddit.com/r/LangChain/comments/1bjnmu4/human_intervention_in_agent_workflows/) , 2024-03-21-0911
```
When building LLM workflows with LangChain/LangGraph what's the best way to build a node in the workflow **where a human
 can validate/approve/reject** a flow? I know there is a Human-in-the-loop component in LangGraph that will prompt the u
ser for input. But what if I'm not creating a user-initiated chat conversation, but a flow that reacts to e.g. incoming 
emails?

I guess I'd have to design my UI so that it's not only a simple single-threaded chat interface, but some sort o
f inbox, right? Or is there any standard way that comes to mind?
```
---

     
 
all -  [ The Perils of trying to build a RAG using TinyLlama on CPU ](https://www.reddit.com/r/LLMDevs/comments/1bjn91u/the_perils_of_trying_to_build_a_rag_using/) , 2024-03-21-0911
```
Hi everyone. I needed some help understanding, how to properly build a RAG.

Disclaimer: Everything here is only a week 
worth of effort. There is a lot of theoritical part about neural networks or ML in general I do not understand. However 
I understand matrices, ranking.

I was intrigued about the whole LLM wave, and wanted to give this a try. Most open to w
ebsites, do not really allow me to play with csvs, pdfs, code from rocksdb's lru\_cache.cc etc. Atleast not the free ver
sions.

Source Code: [https://github.com/ikouchiha47/llama-experiments/tree/master](https://github.com/ikouchiha47/llama
-experiments/tree/master)

So I started off with a small simple project where I could index the *titles.basic.tsv* from 
IMDB and ask it questions like:

1. Which year The Bourne Identity was released?
2. Suggest 5 movies in the same genre.


*And boy, was it not simple.*

There are certain choices I have made:

1. Relying on CPU instead of GPU. Google collab 
is not for me, I had to do a bunch of trial and error, and runtime keeps crashing, google drive goes out of space.
2. Us
ing **llama-cpp-python**, instead of transformers or ctransformers, it seemed simple, also wouldn't need a GPU, I could 
use a **GGUF** format.
3. I used the [TinyLlama-1.1B-Chat-v1.0-GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat
-v1.0-GGUF)  file.
4. Trying to run the word embedding locally, I just don't know if a GPU is required, or would speed u
p the process
5. Used **FAISS** as vector-database. And I just question my life choices.

Now, I have some understanding
 of using the low ranked matrices. Where the delta of the weights (which we trained) is represented using two low rank m
atrices. But while doing word embedding using sentence-transformer, I wasn't sure if the multiplication can happen on my
 Mac M1 Silicon (aplty named, useless thing).

I also noticed, that during preparing the training data, when I trained u
sing a normal language, like,

`f'The movie {movie_name} was released in the year {year}, and belonged to {genre} genres
'` was producing better results, than something like:

    <|user|>
    Which year was {movie_name} released?</s>
    <|
assistant|>
    {year} </s>
    <|user|>
    What genre {movie_name} belongs to?</s>
    <|assistant|>
    Move {movie_n
ame} belongs to {genre}</s>



So, my `first question` is, **Does the text data for training benefit better from keeping
 the text simple, instead of trying to template it in the way the user query prompt will be formatted?**

The docs: [htt
ps://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/blob/main/README.md](https://huggingface.co/TheBloke/TinyLlam
a-1.1B-Chat-v1.0-GGUF/blob/main/README.md)

    prompt_template: |
      <|system|>
      {system_message}</s>
      <|u
ser|>
      {prompt}</s>
      <|assistant|>

The first hurdle I faced was with loading the data. The [IMDB titles.basic
.tsv dataset](https://developer.imdb.com/non-commercial-datasets/) , it becomes nearly 1GB unziped.

Most tutorials, tha
t claimed that they build an RAG,

1. they either took only 10-20% of any big dataset, or just used a bunch of text in a
rray.
2. Used TextSplitting or CSVLoader from **llangchain** , And then feed the chunks directly into a vector dataset
3
. Varying prompt templates, and maybe a query, and everything worked out fan-fugging-tastic.

Except, it's not real. I f
irst had the idea of using **chunksize** in pandas, and then trying to parallelize it. And in trying to do so, I stumble
d upon **dask,** with a blocksize of **128MB** . There were 7 partitions.

For each partition, it would use the **embedd
ings** from [sentence-transformers](https://huggingface.co/sentence-transformers) / [all-MiniLM-L6-v2](https://huggingfa
ce.co/sentence-transformers/all-MiniLM-L6-v2)  and do

    def __index_parition(self, partition):
            db_ids = n
p.arange(len(partition)) + partition.index.start
    
            result = partition.apply(self.cfg.format_row, axis=1)

            encoded_data = self.transfomer.encode(
                result.tolist(),
                normalize_embeddings
=False,
                show_progress_bar=True,
            )
    
            index = faiss.IndexIDMap(
               
 faiss.IndexFlatL2(self.model.get_sentence_embedding_dimension())
            )
            
            faiss.normalize
_L2(encoded_data)
            index.add(encoded_data, db_ids)

and then call \`index.wirte\_index(filepath)\` . But ther
e is a problem with this.  The **langchain**'s FAISS , while creating index, also create a pickle file. when you use the
 regular methods, like `FAISS.from_texts or FAISS.from_documents`, This is important because, while loading back with `F
AISS.load_local` it would not find the pickle file.

The code is here in changelog: [https://github.com/ikouchiha47/llam
a-experiments/commit/0a52168b3b8405ed641b7b6d142d809982aee2ad](https://github.com/ikouchiha47/llama-experiments/commit/0
a52168b3b8405ed641b7b6d142d809982aee2ad)

So, I had to switch to using `FAISS.from_texts` and in doing so, I now lost th
e ability to see the god damn progress bar.

So comes the second problem. The whole thing, it took like 5-6 hours and di
dn't complete. I am not sure why this is taking this much time. But it certainly has something to do with the way I am e
mbedding. This is how I am doing it now:

        self.merged_index = FAISS.from_texts([''], self.model)
        
      
  def __index_parition(self, partition):
            result = partition.apply(self.cfg.format_row, axis=1)
            i
ndex = FAISS.from_texts(result.tolist(), self.model)
    
            self.merged_index.merge_from(index)
            re
turn result
    
        def index_db(self, meta_keys={}):
            if self.df is None:
                raise Excepti
on('UninitializedDataframeException')
    
            if self.model is None:
                raise Exception('Uninitial
izedModelExeception')
    
            if self.merged_index is None:
                raise Exception('UninitializedIndex
Exception')
    
            partitions = self.df.map_partitions(
                self.__index_parition
                
# , meta={'text': 'str'}
            )
    
            # partitions.visualize()
            partitions.compute()
      
      self.merged_index.save_local(self.vectorstore_path)

source: [https://github.com/ikouchiha47/llama-experiments/blo
b/master/src/mammal.py](https://github.com/ikouchiha47/llama-experiments/blob/master/src/mammal.py)

The idea I have is 
to save the index to individual files, my changing the `index_name` parameter in `save_local` . But I just hate the fact
 that there is no progress-bar.



So, my `second question`, **How do I make this embedding and saving to vector store f
aster?** **Its only 1Gig.**

And my `third and final question`, **Why does this thing so difficult to work with?**

Beca
use this file was so huge, I wanted to take a smaller file and atleast see **RAG** at work. So I took dataset from kaggl
e for [IPL 2023](https://www.kaggle.com/datasets/sankha1998/ipl2023) . And as usual, I wanted to ask question like:

1. 
Who won the IPL 2023?
2. How many matches did they play?

And the answers vary vastly differently depending on how I use
 the training text. Right now the training template looks like this:

    template = (
            'Match {match_number}
 was played between two teams '
            '{team1} and {team2} at {venue}. It was a {match_type} match. '
            
'{toss_won} won the toss and decided to {decision}. '
            '{winner} won the match and {loser} lost the match.'
 
       )

And the PromptTemplate for the user query looks like this:

    prompt_template = '''
    <|system|>
    You a
re given the results of cricket matches played in the Indian
    Premier League(IPL) in the year 2023. Given the chat hi
story \
    delimited by(<hs></hs>) and question which might \
    reference context (delimited by <ctx></ctx>) \
    in
 chat history (delimited by <hs></hs>), formulate an answer.\
    Do NOT print the question.
    
    When answering to 
user, if you do NOT know, just say that you do NOT know.
    Do NOT make up answers from outside the context.
    
    A
void mentioning that you obtained the information from the context.
    And answer according to the language of the user
's question.
    
    <ctx>
    {context}
    </ctx>
    
    <hs>
    {chat_history}
    </hs>
    
    <|user|>
    {q
uestion}</s>
    <|assistant|>

source: [https://github.com/ikouchiha47/llama-experiments/blob/master/src/templates.py](
https://github.com/ikouchiha47/llama-experiments/blob/master/src/templates.py)

The problem is when I query. I am going 
to paste the results:

    Input Prompt: Who won IPL 2023 final match?
     Chennai Super Kings won IPL 2023 final match
.
    Input Prompt: Whom did they play against?
     Did they play against Chennai Super Kings or any other team? No, th
ey did not play against Chennai Super Kings, as they were playing against Gujarat Titans in the Final match.
    Input P
rompt: How many matches were played in total in IPL 2023?
     How many matches did Chennai Super Kings play against Guj
arat Titans in the Final match of IPL 2023? 2
    Input Prompt: exit

Here, the answer is definitely wrong. I checked ag
ainst the **index.pkl** file as well. They did not play only 2 matches.

Secondly, sometimes, the the output also has **
wrong spellings** , I am not sure why, the csv file doesn't have those spellings in them.

Thirdly, the output looks all
 weird, with **rephrasing** and subsequent answers showing in 1 line.

    self.model = LlamaCpp(
                    mo
del_path=self.model_path,
                    stop=['</s>'],
                    context_window=2048,
                  
  n_ctx=1024,
                    n_batch=100,
                    n_threads=8,
                    n_gpu_layers=0,
    
                callbacks=[StreamingStdOutCallbackHandler()],
                    temperature=0,
                    # r
epeat_penalty=1.2,
                    verbose=self.verbose,
                )

this is how the model has been configure
d.



Please haaaaalp.
```
---

     
 
all -  [ How to pass 30k rows as context to LLM. ](https://www.reddit.com/r/LangChain/comments/1bjmv5j/how_to_pass_30k_rows_as_context_to_llm/) , 2024-03-21-0911
```
 

I'm working on a project to generate insights from the data.

Extracting data from DB and passing it as context to LL
M

I am using AWS bedrock service , antropic claude v2 as LLM(coz 100k tokken limit.)

Data comprises audiences and one 
base Audience with multiple attributes related to demographics,geography and employment.  
Each attribute have multiple 
attribute values

Issue I'm facing is some attributes have 20-35k rows of unique attribute values, i want to generate th
e insghits from them.

I tried passing 400-500 rows at a time with a loop to cover 20k rows and store the output in a li
st and passing that list again through LLM to generate summary of all the 400 rows loop output.. something like Mapdredu
ce.

but it is taking a lot of time (40-min to generate insights from 20k rows)and there is loss of information, LLM ign
ores some of the important rows as every row is unique and important.

Pls suggest some better way to solve this problem
.
```
---

     
 
all -  [ RAG chain with HF model works fine for first quest, then OOM for subsequent chain. No OOM issue when ](https://www.reddit.com/r/LangChain/comments/1bjm5rp/rag_chain_with_hf_model_works_fine_for_first/) , 2024-03-21-0911
```
I have built a simple RAG chain with message history using Mistral-7b model with 4bit quantization. 

Whenever I build t
his chain using a model from the dockerized Ollama, everything works fine and I can have a long conversation with the ch
ain. 

However, as soon as I switch to HF model, only the first message goes through, everything else gets the OOM memor
y. In fact, the memory usage seems to increase with each subsequent invoke. 

In both cases, I am using the Mistral-7b m
odel with quantization. So I am confused as to where the memory issue comes from.   


Here are the code snippets:  


U
sing HF model:

    model_name = 'mistralai/Mistral-7B-Instruct-v0.2'
    bnb_config = BitsAndBytesConfig(
        load_
in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type='nf4', bnb_4bit_compute_dtype=torch.bfloat16
    )
   
 
    model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config)
    tokenizer = AutoToken
izer.from_pretrained(model_name)
    
    text_generation_pipeline = pipeline(
        model=model,
        tokenizer=to
kenizer,
        task='text-generation',
        temperature=0.2,
        do_sample=True,
        repetition_penalty=1.1
,
        max_new_tokens=400,
    )
    
    chat_llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

Using Ol
lama model:

    chat_llm = ChatOllama(model='mistral:7b')

Overall chain setup

    chatbot_conversation_with_context_c
hain = 
   RunnablePassthrough.assign(standalone_message=standalone_message_chain).assign(context= 
   itemgetter('stand
alone_message') | retriever).assign(output= question_answering_prompt | 
   chat_llm | StrOutputParser())
    
    chatb
ot = RunnableWithMessageHistory(
       chatbot_conversation_with_context_chain,
       get_session_history=get_session_
history,
       input_messages_key='messages',
       history_messages_key='chat_history',
       history_factory_config
=[
       ConfigurableFieldSpec(
             id='user_id',
             annotation=str,
             name='User ID',
  
           description='Unique identifier for the user.',
             default='',
             is_shared=True,
        
),
       ConfigurableFieldSpec(
             id='conversation_id',
             annotation=str,
             name='Conv
ersation ID',
             description='Unique identifier for the conversation.',
             default='',
             
is_shared=True,
        ),
    ],
)
    response = chatbot.invoke(
    {'messages': 'Can you give me the basic Java code
 for reading a CSV file?'},
       config={
       'configurable': {'user_id': 'test', 'conversation_id': 'dummy'}
     
   },
)

print(response.keys())
for key in response.keys():
       print(key+': ', end='')
       print(response[key])


response = chatbot.invoke(
      {'messages': 'Can you elaborate on the first function?'},
      config={'configurable':
 {'user_id': 'test', 'conversation_id': 'dummy'}
  },
)

print(response.keys())
for key in response.keys():
       print
(key+': ', end='')
       print(response[key])
    

&#x200B;
```
---

     
 
all -  [ Got the accuracy of GPT4 Function Calling from 35% to 75% by tweaking function definitions. ](https://www.reddit.com/r/LangChain/comments/1bjlldg/got_the_accuracy_of_gpt4_function_calling_from_35/) , 2024-03-21-0911
```
* Adding function definitions in the system prompt of functions (Clickup's API calls).
* Flattening the Schema of the fu
nction
* Adding system prompts
* Adding function definitions in system prompt
* Adding individual parameter examples
* A
dding function examples

Wrote a nice blog with an [Indepth explanation](https://blog.composio.dev/improving-function-ca
lling-accuracy-for-agentic-integrations/) here.

https://preview.redd.it/rmxgt35zfjpc1.png?width=816&format=png&auto=web
p&s=934eddf839e17f2324c590157943a92ebbdedffa
```
---

     
 
all -  [ Do researchers like langchain? ](https://www.reddit.com/r/LangChain/comments/1bjks1c/do_researchers_like_langchain/) , 2024-03-21-0911
```
I’m a Ph.D. student who recently try to switch from hugging face to langchain. It feels like huggingface organize their 
libraries     the research way (or the PyTorch way? It just feel like I can use them the same way I use research papers’
 code), but langchain is more like something developed by JavaScript engineers and designed with no research user cases.
 

For example, all the “batch inference “ requirements on GitHub are ignored. The interface for customized functions (e
.g., chat history post processing) are ill-designed. 

I chose langchain in the beginning because the LLMs hosted by lan
gchain responds faster than my local ones. But it seems that it’s really hard to customize the functionalities for resea
rch purposes.
```
---

     
 
all -  [ Can anyone suggest a idea to implement RAG with LLm.Like if the searched query not in RAG data then  ](https://www.reddit.com/r/LangChain/comments/1bjiabv/can_anyone_suggest_a_idea_to_implement_rag_with/) , 2024-03-21-0911
```
If any Colab notebook or github repo available then it will be helpful
```
---

     
 
all -  [ is it possible to connect 2 GeForce RTX 4090 to a Laptop? ](https://www.reddit.com/r/LangChain/comments/1bji0np/is_it_possible_to_connect_2_geforce_rtx_4090_to_a/) , 2024-03-21-0911
```
Hi,

i have built a Langchain RAG app with a local model and now want to be able to run it on a Laptop. I am using a qua
ntized Mixtral Model (Q5\_0) and for this I want to conntect 2 GeoForce RTX 4090 to my laptop. As I am a newby (and noob
y) in the Hardware topic, is it even possible to connect 2 RTX 4090 to a more or less 'normal' Laptop?

The use case wou
ld be that the customer tries the (local) application on a standalone device and if he is happy with it he buys more Har
dware to host it for production.

At the moment I am running everything on my Macbook with 64GB RAM but I need a solutio
n for a customer with a Windows PC.

One other option would be that the customer just buys a Macbook, but the 2 GeForece
 RTX 4090 would be a better investment I think because these could further be used for a prodcution setting.

&#x200B;


Thanks for you suggestions!
```
---

     
 
all -  [ Store Fine-tuned model locally ](https://www.reddit.com/r/LLMDevs/comments/1bjhirq/store_finetuned_model_locally/) , 2024-03-21-0911
```
Hello everyone,

I have been working on and off with LLaMa2 for a year now. I am trying to fine-tuned it in order to inc
rease its performance in a certain domain area. I am wondering if there is any way to do this without pushing the fine-t
uned model on HuggingFace, and instead keep it local. I would also like to understand if storing the fine-tuned model lo
cally means storing \*all\* of the model, which is quite huge especially in the 70b case. Finally, I would like to know 
if there is any way to load the fine-tuned model, or just its weights together with the base model. I am currently using
 LangChain to work around these issues, but there is no guide that does not involve pushing the final, fine-tuned model 
online. 

Any help would be appreciated. 
```
---

     
 
all -  [ Here is a FREE Email Course on LangChain (Basics + Applications + Coding + Colab Notebook all includ ](https://pxl.to/ruqwj8qk) , 2024-03-21-0911
```

```
---

     
 
all -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-21-0911
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
 
all -  [ Seeking the Ideal Stack for Natural Language Database Interactions ](https://www.reddit.com/r/LangChain/comments/1bjf4xd/seeking_the_ideal_stack_for_natural_language/) , 2024-03-21-0911
```
Hello everyone,

I'm embarking on a project that requires a fresh start, and I find myself at a crossroads trying to dec
ide on the optimal technology stack. The core objective is to enable conversations with a database using natural languag
e, aiming for precise outcomes. This involves working with tabular data, applying filters, and conducting semantic searc
hes.

Given the plethora of options out there, from graph databases and SQLCoder models to Retrieval-Augmented Generatio
n (RAG) techniques, making a choice feels overwhelming. Each of these technologies brings something unique to the table,
 but I'm looking for a solution that balances ease of integration, scalability, and, most importantly, the ability to un
derstand and process natural language queries effectively.

I would greatly appreciate your insights, experiences, or an
y advice you could share on this matter. Which stack or combination of technologies have you found to be the most effect
ive for interacting with databases through natural language? Any pitfalls or success stories you could share would also 
be incredibly helpful as I navigate through these options.

Thank you in advance for your time and help!
```
---

     
 
all -  [ How to randomize output for same input in local LLM with langchain. ](https://www.reddit.com/r/LocalLLaMA/comments/1bjewg3/how_to_randomize_output_for_same_input_in_local/) , 2024-03-21-0911
```
I am relatively new to working with LLMs and I encountered this issue. The thing is that if I use langchain with OpenAI 
with any of their GPT models for the same input whenever I rerun the code I will get a different output. However while u
sing langchain with Pygmalion (notstoic/pygmalion-13b-4bit-128g) running with Oobabooga web-ui, For each rerun of the sa
me input I get the same output. This is confusing because when regenerating the output directly in the webui or via Sill
yTavern I get a different output every time. So can someone help me resolve this.  


Main code [https://pastebin.com/Ge
pu93Av](https://pastebin.com/Gepu93Av)  
CustomLLM wrapper (Not my code found it on github) [https://pastebin.com/D4Baub
Vv](https://pastebin.com/D4BaubVv)  

```
---

     
 
all -  [ Understanding JSONDecodeError when using JsonOutputParser ](https://www.reddit.com/r/LangChain/comments/1bjdjk0/understanding_jsondecodeerror_when_using/) , 2024-03-21-0911
```
Hi everyone, I hope it is fine to post questions here. 

I am just getting started with output-parsers and I'm impressed
 with their usefulness when they work properly. I have, however, run into a case where every now and then, a chain retur
ns an error that seems to be related to the JsonOutputParser that I use, as indicated by the following (condensed) error
 message:

`JSONDecodeError`                             
`JsonOutputParser.parse_result(self, result, partial)`   
`156
 # Parse the JSON string into a Python dictionary`  
`--> 157 parsed = parser(json_str)`  
 `159 return parsed`  
`122 #
 If we got here, we ran out of characters to remove`  
`123 # and still couldn't parse the string as JSON, so return the
 parse error`  
`124 # for the original string.`  
`--> 125 return json.loads(s, strict=strict)`

According to [this pos
t here](https://www.reddit.com/r/LangChain/comments/17hep0o/comment/k6na6nd/?utm_source=share&utm_medium=web3x&utm_name=
web3xcss&utm_term=1&utm_content=share_button) this could be related to there not being 'enough tokens left to fully gene
rate my output', which seems to be in line with the error message above:

\>`122 # If we got here, we ran out of charact
ers to remove` 

although I am not fully sure what that means or how it can be fixed. 

Has anybody encountered this pro
blem before and could offer some guidance? I must admit that I'm feeling kind of stumped, especially since the error can
't be reproduced reliably and only occurs every other time I run my script. 
```
---

     
 
all -  [ Has anyone used dspy for RAG? how does it compare to langchain/llama-index? and how does it 'train'  ](https://www.reddit.com/r/LLMDevs/comments/1bjctuz/has_anyone_used_dspy_for_rag_how_does_it_compare/) , 2024-03-21-0911
```
I have a few questions I am not able to understand about dspy

1. How is it training LLM? 
2. How is it writing prompts?
 (like I currently tell chatgpt never do this, how can I do this in dspy?)
3. How it is modifying and making pipelines b
etter? (without actively changing the code itself)
4. How is it able to use  models like T5 along with ChatGPT for bette
r RAG?
5. Is it possible to censor or stop it from getting off-topic?

if you have any experience in this it would be ve
ry helpful. I am specifically looking for text to sql application and really interested in how is it able to give ref da
ta to improve sql generation.
```
---

     
 
all -  [ Chatbot development with Gemini 1.0-pro API [Help need] ](https://www.reddit.com/r/GoogleGeminiAI/comments/1bja3jn/chatbot_development_with_gemini_10pro_api_help/) , 2024-03-21-0911
```
I am developing a chatbot with Gemini. Currently I am struggling with the conversation history issue.

**Problem**

I am
 trying to get the AI response for a user message but the AI response is not matching with the previous message. i.e 

u
ser - Hi I need to know about your company.

ai - we are a management consultant company. We provide the following servi
ces. Is there anything else I can help you with today?

user - no

ai - Great Is there anything else I can help you with
 today?

The last AI response is not correct. I have tried different ways and different prompts but not worked.

**Tech 
stack**

Node js

Langchain js (I have tried raw Google Gen ai studio SDK but did not work)

**Source code**

    const 
{ FewShotChatMessagePromptTemplate , ChatPromptTemplate } = require('@langchain/core/prompts')
    const examplePrompt =
 ChatPromptTemplate.fromTemplate(`Human: {human}\nAI: {ai}`);
    const gemini = require('./services/gemini')
    
    a
sync function build(){
        const fewShotPrompt = new FewShotChatMessagePromptTemplate({
            examplePrompt,
 
           examples: [],
            prefix:'You are an assistant of {org_name} company. You can schedule/reschedule/can
cel appointments , provide company information. reply to human conversation. You are emphatic, polite and friendly assis
tant. You always consider about human's feelings and respond to sad or bad situations with a wise message. If the human 
rejects your support never ask anything there for your help explain that you are available anytime. You don't know any o
ther area information other than your company information. If the human asks for anything non related to your knowledge 
base explain why you can't reply to that. Always your reply should be very short and straight and perfectly match with t
he conversation history. Your company details: {details}.',
            inputVariables: ['details', 'msg' , 'org_name' ,
 'examples'],
            suffix:'This human message is the latest message of the conversation. Always your response for
 this message should strictly match with the conversation. Human message: {msg}',
        });
        return fewShotProm
pt.format({
            orgName: 'Langchain',
            details: 'Langchain is a company that provides AI services. We
 accepts bookings by company website.',
            msg: 'Ok',
            org_name: 'Langchain',
        })
    }
    

    build().then(async res=>{
        console.log(res)
        console.log('============================================
========\n\n\n')
        let history = [
            ['human','What services does Langchain provide?'],
            ['ai
','Langchain is a company that provides AI services. Can I place a booking for you?'],
            ['human','ok'],
     
       ['ai','Sure! You can book an appointment through our website. Is there anything else I can help you with today?']
,
            ['human','No'],
            ['ai','Great!! If there anything feel free to drop a message'],
            ['
human',res]
        ]
        let geminiRes = await gemini.invoke(history)
        console.log(geminiRes.content)
    })


**Generated Prompt (res var value)**

You are an assistant of Langchain company. You can schedule/reschedule/cancel ap
pointments, and provide company information. reply to human conversation. You are an emphatic, polite, and friendly assi
stant. You always consider human feelings and respond to sad or bad situations with a wise message. If the human rejects
 your support never ask anything there for your help explain that you are available anytime. You don't know any other ar
ea information other than your company information. If the human asks for anything non-related to your knowledge base ex
plain why you can't reply to that. Always your reply should be very short and straight and perfectly match the conversat
ion history. Your company details: Langchain is a company that provides AI services. We accept bookings by company websi
te..

&#x200B;

This human message is the latest message of the conversation. Always your response to this message shoul
d strictly match with the conversation. Human message: OK

&#x200B;

If anyone can support on this It will be a great su
pport for me. 🙏 
```
---

     
 
all -  [ Project University Chat With PDF ](https://www.reddit.com/r/csharp/comments/1bj8gze/project_university_chat_with_pdf/) , 2024-03-21-0911
```
Hello! I want to create a CHAT app with pdf documents without OpenAI, but i don’t know how to use Langchain in c#. Could
 you help me please with some tutorials? Or some tips?


```
---

     
 
all -  [ [For Hire] Ex-Booking[dot]com Data Analyst, GenAI specialist at a startup [35 USD/hr] ](https://www.reddit.com/r/forhire/comments/1bj7ws4/for_hire_exbookingdotcom_data_analyst_genai/) , 2024-03-21-0911
```
Hey, I have been using this subreddit to get clients and have completed 3 jobs here, all with good reviews.

Here are my
 skills and experience:

1) Technical Skills: Python, SQL, R 

2) Academics: Bs Econometrics, Mathematics and Computer S
cience

3) Specialty: GenAI, Statistics, Data Visualization.

4) Sectors: Databases, Hospitality, ecommerce and Telecom



Here are some of my projects (I write extensively on Medium):

Link: https://arslanshahid-1997.medium.com/using-langch
ain-to-teach-an-llm-to-write-like-you-aab394d54792

Link: https://towardsdatascience.com/money-balling-cricket-probabili
ty-of-100-using-repeated-conditioning-2fc8dbceb42e


I have over 4+ years experience in Data Science. 


Please do reach
 out, fair rate of 35 USD/hr. 
```
---

     
 
all -  [ Langchain Usage doubt for document generation ](https://www.reddit.com/r/LangChain/comments/1bj6xl3/langchain_usage_doubt_for_document_generation/) , 2024-03-21-0911
```
I am trying to build an application that takes templates of things like a cover letter , resume , medical research docum
ent. Now based on this template I will upload another document containing information to be used to fill the template. H
owever after the model generates a new document following the template and information , the whole alignment of the docu
ment is wrong and it doesnt bold the necessary parts. Is there any way to ensure that a model can follow the format for 
a template like center allignment , bolding the headers , etc. 
```
---

     
 
all -  [ The glass ceiling I’m hitting is made up by my brain. ](https://www.reddit.com/r/SaaS/comments/1bj5808/the_glass_ceiling_im_hitting_is_made_up_by_my/) , 2024-03-21-0911
```
I quit all I had in France a year ago. Software engineer job, flat in Lyon (France), sold most of my belongings and went
 in Asia with a one-way ticket and my 50 backpack ~ 9kg inc. the MacBook.
Freedom drove me: the freedom to go wherever I
 want, whenever I want, doing whatever I want. Leaving France was motivated by the willing to unleash my entrepreneurial
 spirit. 

I wasn’t sure what I was gonna do: freelancing, remote work, indie hacking, etc
The first few months of trave
l got me thinking a lot, and at a point I met this French entrepreneur (owning 3 digital agencies), during our discussio
n one point got me thinking for weeks, after I asked him what brought him to his current position: “I kept doing what I 
loved to do until people where willing to pay me for it”
That triggered this question within me: wtf can I do that I act
ually love to do? 
My life has so many different phases, from bartender in NYC, to carpenter in New-Zealand, to Engineer
 in the aluminum industry with international customers, to software eng in a French startup. I was like: fk, what’s the 
common element in this sh*t. What do I love to do. After weeks of background thinking it was cristal clear: I love to so
lve problems, and I love to build solutions for it. 

That’s where I started my indie hacker journey, one year ago. Then
, long story short: 
- challenged myself for the first saas: created a WhatsApp bot integrating ai in couple of weeks (f
ocusing on audio transcription as pain point)
- Then seeing the potential of AI, created another WhatsApp bot that would
 integrste everything (text, audio, image, etc) - which didn’t solve any problem, except leveraging WhatsApp to make AI 
more accessible
- Then created couple of free stuff, worldll•e (a bot posting daily pics representing the world based on
 the previous day’s news), and another stuff to interact with Karl Marx books
All my projects were drivent by technologi
cal curiosity, each of them allowed me to go deeper into using and applying AI (for instance, the “Karl Marx” was my way
 to use and understand langchain, , embedding, vector databases  / pinecone). 

First first project was making ~$150/ mo
, from AI directories and couple of newsletters it’s been published in. 

The second WhatsApp bot was killed, it got spa
mmed in Facebook group in North Africa and India and got me into issues with Meta, ending up with my business account be
ing banned. 

Then I came a cross this AI influencer tweet lot of people have seen “we made $70k by selling 1$/min audio
 of an influencer on telegram”.
I was like: “f*ck META and WhatsApp, I need to try Telegram. Let’s explore the text-to-s
peech and custom LLMs and build an AI girlfriend”. I focused on the erotic part of it to differentiate it a bit. First m
onth it made $800. The lots of ups and downs. Most of my traffic is coming from AI directories, since i was one of the f
irst ones to register it on it (did this saas over the week end at first, it was 6 month ago). 
It went to $2k, up to $4
k at a point, now in between $2.2k and $3k. But I never did marketing, thinking that I don’t like this industry. I alway
s hide myself in technological / features / experience improvement. Always avoiding the marketing. Why? There’s actually
 a lot of potential in this business. Health, wealth and relationship are 3 axis that will always make money. I had LOAD
S of times of introspections, hips of downs, some ups of course, here’s what I realised: 
- I’ve been through the poores
t phase of my life while being in Bali, had no savings left, needed to live on a ~15-30$ / day revenue (still had to pay
 some services and APIs with it)-> I had to deconstruct my occidental vision or financial security. Learn to live with a
lmost nothing, with max 3-4 days of financial vision (the time Stripe takes to forward incomes to bank account). It tota
lly changed my way of thinking. 
- I was missing a goal: I was seeking “financial freedom”. But what is it? How much do 
I need to generate? Not having a number on it was the best way to not achieve this goal. 
- I became dependent of a proj
ect I didn’t like: the ai girlfriend. It was (and is) keeping me alive, and somehow blocked myself from pushing it for e
thical reasons, and afraid of being labelled as the “ai girlfriend” guy. but really: who gives a sh*t? Relationships & s
ex is taboo even though part of our daily life. Still, I went into the tech rabbit hole with always avoiding any marketi
ng and trying to fix/improve the product, that even brought me to another thought: 
- Am I afraid of success? Am I afrai
d of making money? As weird as it sounds, I believe the last 6 months were actually a transition of the employee version
 of me, dreaming of entrepreneurship, to be an actual entrepreneur. Believing in myself. I’m always harsh on myself, whi
ch makes it hard to consider wins, even the smallest ones, but as well pushes me to keep going. In December I had 3 week
s of holiday in Vietnam with a friend, the first self-paid holiday. Not touching the laptop, and money was still flowing
 in. That’s a huge step. 

So now, here I am, got two products with market fit: $150 MRR, and $2.2k MRR. Did the strict 
minimum for it marketing-wise. 
Im in Bangkok since 3 weeks, heading back to Bali next week, and a clearer vision, after
 months of evolutions, learnings, ups and down. And my goal is simple: Break. This. Fkg. Glass. Ceiling. My. Mind. Creat
ed. 

How? 
1. Growing these two products
- Reduce churn = improve experience
- Increase conversion = rework LP and offe
rs
- Increase traffic = MARKETING

2. Then going back to what I actually miss and love: Building new stuff. Fkg miss it.
 We should focus on what work yes, but as well focus on what drives us, and for me it’s the curiosity and the challenges
 a new product brings. But first, I need to hack and unlock marketing for me. 

This AI girlfriend stuff made me ashamed
 of Building in Public, so stopped to do it. Now I’m gonna be back and share my insights and learnings for growing my cu
rrent products and creating new stuff. 

This post is a way for me to be accountable to ANNIHILATE this mind-made glass 
ceiling. 

I’ll be sharing stuff again on twitter, [@maelus_](https://x.com/maelus_) - I’d love to connect with other in
diehackers - could even Meetup if you’re in Bali / Bangkok / France, world is small when travelling & indiehacking. 

Al
so, AMA

maelus
```
---

     
 
all -  [ How can I fine-tune an ai model with my specific expertise? Without Langchain - a no-code solution. ](https://www.reddit.com/r/nocode/comments/1bj4tv6/how_can_i_finetune_an_ai_model_with_my_specific/) , 2024-03-21-0911
```
Hey I'm not really on Reddit too much, so if my post isn't formatted usually, my apologies. I'm looking to create an aut
omation and train an AI to be able to output text-based content for me. I want to train it specifically on the way to wr
ite the content, the thinking process behind the content itself, and really fine-tune a model to create this content. Th
e content that I'm looking to create is social media content. I want to fine-tune the model based on my expertise with c
reating content and also copywriting, and being able to use emotion and storytelling in the content that's created. As f
ar as the data, I can compile some of the best tweets and articles that I've written, also with full breakdowns and expl
anations of why I wrote them the way that they are, in addition to that, some training material on copywriting and how t
o think about copywriting and also storytelling through content. My hiccup is, I practically have no coding skills. I kn
ow that I could probably use make.com to create some type of automation. But I'm looking to actually fine-tune a model s
pecifically on this task, and I don't know how to accomplish this. Even if this model just leverages the data and pulls 
from OpenAI's API to give me the outputs, that's totally fine, or if I even use one of the open-source models and fine-t
une it to create the content for me also. But I'm looking for a way to actually have the model myself and not resort to 
3rd parties to create the model, for example, and be able to play around with the tuning. I would either keep it locally
 or cloud-based, totally fine, and I could write up a quick interface.  
  
  
  
The goal for me is to be able to i
nput the idea or the concept around the topic and output the prewritten content around the idea, structured and followin
g the frameworks that I would write content with. If possible, but my hopes are not up, I would also love to automate th
is. I know I could do it with make.com, but I'm still stuck on creating the model.  
  
  
  
Any help or guidance i
s greatly appreciated.
```
---

     
 
all -  [ Want to turn your work into sharable chat app in minutes ? ](https://www.reddit.com/r/LangChain/comments/1bj3qjq/want_to_turn_your_work_into_sharable_chat_app_in/) , 2024-03-21-0911
```
Hi folks, If you are building with LangChain and want to turn your work into sharable chat app in minutes and in pure py
thon, then join the waitlist  [https://cycls.typeform.com/waitlist](https://cycls.typeform.com/waitlist) .  
We're geari
ng up for a release in just a few weeks. 
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1bixj1s/list_of_free_and_best_selling_discounted_courses/) , 2024-03-21-0911
```
## Udemy Free Courses for 20 March 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.*

* React y TypeScript – La Guía Completa Creando +10 Proyectos[REDEEM OFFER](https://idownloadcoupon.
com/udemy/2613/)
* 衝突管理, 如何與難相處的人打交道[REDEEM OFFER](https://idownloadcoupon.com/udemy/2612/)
* Time Series Analysis, Fore
casting, and Machine Learning[REDEEM OFFER](https://idownloadcoupon.com/udemy/2611/)
* Manejo de Conflictos – Cómo Trata
r con Personas Difíciles[REDEEM OFFER](https://idownloadcoupon.com/udemy/2610/)
* FMEA: Failure, Modes, Effects, Analysi
s[REDEEM OFFER](https://idownloadcoupon.com/udemy/2609/)
* Gestione dei Conflitti: Come Trattare con Persone Difficili[R
EDEEM OFFER](https://idownloadcoupon.com/udemy/2608/)
* Continuous Improvement[REDEEM OFFER](https://idownloadcoupon.com
/udemy/2607/)
* Conflict Management – How to Deal with Difficult People[REDEEM OFFER](https://idownloadcoupon.com/udemy/
2606/)
* Start Career in CyberSecurity – The Ultimate Guide[REDEEM OFFER](https://idownloadcoupon.com/udemy/2605/)
* Cyb
erSecurity Bootcamp: The Ultimate Beginner’s Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2604/)
* Employee Cy
berSecurity Awareness First Line of Defense[REDEEM OFFER](https://idownloadcoupon.com/udemy/2603/)
* Book Cover Design T
raining with Canva – Beginner to Pro[REDEEM OFFER](https://idownloadcoupon.com/udemy/2602/)
* Linux Bash Scripting[REDEE
M OFFER](https://idownloadcoupon.com/udemy/2601/)
* Pitch Deck Hero: Business Presentation and Communication[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/2600/)
* Start Career in CyberSecurity – The Ultimate Guide[REDEEM OFFER](https://i
downloadcoupon.com/udemy/2598/)
* CyberSecurity Bootcamp: The Ultimate Beginner’s Course[REDEEM OFFER](https://idownload
coupon.com/udemy/2597/)
* Employee CyberSecurity Awareness First Line of Defense[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/2595/)
* Ubuntu Linux for beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/2395/)
* Improving software
 development productivity[REDEEM OFFER](https://idownloadcoupon.com/udemy/1141/)
* Vlogging and Blogging for a Living: H
ow to Start & Succeed[REDEEM OFFER](https://idownloadcoupon.com/udemy/2594/)
* Transforming Everyday Language into Power
ful SQL Queries[REDEEM OFFER](https://idownloadcoupon.com/udemy/2593/)
* Affiliate Marketing Guide To Earn Passive Incom
e Online[REDEEM OFFER](https://idownloadcoupon.com/udemy/2592/)
* Ethical Hacking: Hack Linux Systems[REDEEM OFFER](http
s://idownloadcoupon.com/udemy/2591/)
* Linux Modules[REDEEM OFFER](https://idownloadcoupon.com/udemy/2590/)
* Mastering 
Windows Security[REDEEM OFFER](https://idownloadcoupon.com/udemy/2589/)
* CSS And JavaScript Complete Course For Beginne
rs[REDEEM OFFER](https://idownloadcoupon.com/udemy/2588/)
* Facebook Ads MasterClass – All Campaign Creations & Features
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2587/)
* Learn How to Earn Cryptocurrency Worldwide in 2024[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/2586/)
* Solving LeetCode’s Top Interview Questions in Java \[2024\][REDEEM OFFER](
https://idownloadcoupon.com/udemy/2585/)
* Social Media Bots with Python[REDEEM OFFER](https://idownloadcoupon.com/udemy
/2584/)
* Intro to Business Etiquette for Entry-Level Professionals[REDEEM OFFER](https://idownloadcoupon.com/udemy/2583
/)
* National Council Licensure Examination (NCLEX) Practice[REDEEM OFFER](https://idownloadcoupon.com/udemy/2582/)
* Le
arn and master the ABCs of financial markets[REDEEM OFFER](https://idownloadcoupon.com/udemy/2581/)
* Augmented Reality 
Certification ( AR Foundation, Vuforia )[REDEEM OFFER](https://idownloadcoupon.com/udemy/2580/)
* Cómo Crear una Página 
Web con Hostinger Desde Cero 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/2579/)
* Elementor Kits: Crea una Pági
na Web con Elementor Pro[REDEEM OFFER](https://idownloadcoupon.com/udemy/1184/)
* Cómo Crear una Página Web con WordPres
s Para Principiantes[REDEEM OFFER](https://idownloadcoupon.com/udemy/1149/)
* Mastering Public Speaking: From Fear to Fl
uency[REDEEM OFFER](https://idownloadcoupon.com/udemy/1996/)
* Cómo Crear una Tienda Online con Inteligencia Artificial[
REDEEM OFFER](https://idownloadcoupon.com/udemy/1185/)
* Social Media Bots with Python[REDEEM OFFER](https://idownloadco
upon.com/udemy/2383/)
* Personal Finance 101: Asset Classes, Investments & Budgeting[REDEEM OFFER](https://idownloadcoup
on.com/udemy/2355/)
* Microsoft Excel Fundamentals: A Beginners Guide[REDEEM OFFER](https://idownloadcoupon.com/udemy/25
77/)
* The “BigTech” System Design Interview Bootcamp[REDEEM OFFER](https://idownloadcoupon.com/udemy/2576/)
* Mastering
 LangChain and AWS: A Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/2575/)
* Build laravel 
apps fast with blueprint[REDEEM OFFER](https://idownloadcoupon.com/udemy/2574/)
* Business Model Canvas Mastery: Learn H
ow Business Model Work[REDEEM OFFER](https://idownloadcoupon.com/udemy/2573/)
* ChatGPT for Mastering Compelling Content
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2572/)
* Upgrade Your Social Media Presence with ChatGPT[REDEEM OFFER](
https://idownloadcoupon.com/udemy/2571/)

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownload
coupon.com/)
```
---

     
 
all -  [ Use case doubt ](https://www.reddit.com/r/LangChain/comments/1biwtil/use_case_doubt/) , 2024-03-21-0911
```
Hello! I have a question I haven’t been able to find online, and was hoping someone could explain it to me. 

I need to 
build a “chatbot” where the user asks questions about history, and the agent must reply with the correct answer. Here’s 
the thing: The context needs to be fed from certain books, and some pdfs.

Why’s the best way to do this? The objective 
is to outperform in replying correctly to OpenAI models. Or, which model would be the best (or combination of model + RA
G) to get the best result?

Thanks!
```
---

     
 
all -  [ RAG customers ](https://www.reddit.com/r/LangChain/comments/1bitjgv/rag_customers/) , 2024-03-21-0911
```
Where are you guys finding customers to sell your RAG products? What do thesr customers look like?
```
---

     
 
all -  [ Should I report this as a bug? ](https://www.reddit.com/r/LangChain/comments/1bish94/should_i_report_this_as_a_bug/) , 2024-03-21-0911
```
I was just changing an existing langchain workflow from using an OpenAI model to using one from Replicate.

This showed 
the value of using `langchain` because it pretty much Just Worked to change the LLM model constructor I had used origina
lly, and then rerun all my code (in a Jupyter Notebook).

But it only 'pretty much' worked: in particular, when I invoke
d the OpenAI models, I would get an `AIMessage` object out of the chain.  When I invoke a Replicate model, I am just get
ting a string.

I imagine that this could cause issues if trying to extend a chain past the Replicate LLM to something l
ike an Output Parser couldn't it?

&#x200B;
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1bimnof/for_hire_programmerweb_developerit_consultant/) , 2024-03-21-0911
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

     
 
all -  [ High school teacher here with a use case question for the educational setting.  ](https://www.reddit.com/r/LangChain/comments/1bimg0l/high_school_teacher_here_with_a_use_case_question/) , 2024-03-21-0911
```
I work in education and envision a way of using RAG to help my students develop their writing. 

My vision is to have st
udents keep a digital portfolio of all their writing over the course of the semester or the year. I'd like to then use a
 RAG/LLM setup to provide students with feedback regarding their writing development over the course of the year. Ultima
tely, I'd like to load all of their writing into a RAG for my own analysis. I would be running this on an local LM Studi
o LLM for student privacy. 

Is Langchain an appropriate tool to achieve this? Would I be able to set it up to analyze t
housands of pages of student work? And can I design it so that it is a conversational interaction with a history window?
 
```
---

     
 
all -  [ Integration with RESTAPIs? ](https://www.reddit.com/r/LangChain/comments/1billcu/integration_with_restapis/) , 2024-03-21-0911
```
Is there a good way to integrate LangChain with a personal LLM RESTAPI yet?

[https://www.reddit.com/r/LangChain/comment
s/17v1rhv/integrating\_llm\_rest\_api\_into\_a\_langchain/](https://www.reddit.com/r/LangChain/comments/17v1rhv/integrat
ing_llm_rest_api_into_a_langchain/)

I saw this post, but it doesn't explain any of the integration with basic chains li
ke LLMChain. There're so many integrations, but nothing I see so far for interacting with your own tooling?

The API jus
t has the basic response structure for a LLM, but that should just be one piece of the connection right? 
```
---

     
 
all -  [ Resume under construction ! Help a junior out please , 🥺 ](https://i.redd.it/4j9uzapepapc1.jpeg) , 2024-03-21-0911
```
What changes I need to do you according to you,😌🫵🫵

```
---

     
 
all -  [ Best Udemy Paid Courses For Free With Certificate | Hurry Don’t Miss | Tuesday, March 19, 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1bikfd0/best_udemy_paid_courses_for_free_with_certificate/) , 2024-03-21-0911
```
## Udemy Free Courses for 19 March 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.*

* Microsoft Excel Fundamentals: A Beginners Guide[REDEEM OFFER](https://idownloadcoupon.com/udemy/25
77/)
* The “BigTech” System Design Interview Bootcamp[REDEEM OFFER](https://idownloadcoupon.com/udemy/2576/)
* Mastering
 LangChain and AWS: A Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/2575/)
* Build laravel 
apps fast with blueprint[REDEEM OFFER](https://idownloadcoupon.com/udemy/2574/)
* Business Model Canvas Mastery: Learn H
ow Business Model Work[REDEEM OFFER](https://idownloadcoupon.com/udemy/2573/)
* ChatGPT for Mastering Compelling Content
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2572/)
* Upgrade Your Social Media Presence with ChatGPT[REDEEM OFFER](
https://idownloadcoupon.com/udemy/2571/)
* Discover Google Gemini for Marketing Success[REDEEM OFFER](https://idownloadc
oupon.com/udemy/2570/)
* Apache Spark Project World Development Indicators Analytics[REDEEM OFFER](https://idownloadcoup
on.com/udemy/2569/)
* ChatGPT & Midjourney & Gemini: Digital Marketing Assistants[REDEEM OFFER](https://idownloadcoupon.
com/udemy/2568/)
* Grow your business with Chatbot Marketing![REDEEM OFFER](https://idownloadcoupon.com/udemy/2567/)
* D
igital Marketing Automation: One Step Ahead of Competitors[REDEEM OFFER](https://idownloadcoupon.com/udemy/2566/)
* Midj
ourney For Beginners: Creating Visuals Using AI[REDEEM OFFER](https://idownloadcoupon.com/udemy/2565/)
* Mastering SEO W
ith ChatGPT: Ultimate Beginner’s Guide[REDEEM OFFER](https://idownloadcoupon.com/udemy/2564/)
* You Can Deliver a TED-St
yle Talk Presentation (Unofficial)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2563/)
* Podcasting: How to Speak Eff
ectively on Your Own Podcast[REDEEM OFFER](https://idownloadcoupon.com/udemy/2562/)
* Interviewing Skills for Jobs: Ace 
the Job Interview[REDEEM OFFER](https://idownloadcoupon.com/udemy/2561/)
* Ace Your Python Interview: Essential Practice
 Tests (2024)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2560/)
* PHP with MySQL 2024: Build Complete Coffee Shop S
ystem[REDEEM OFFER](https://idownloadcoupon.com/udemy/2559/)
* AZ-800 Administering Windows Server Hybrid Latest Exam[RE
DEEM OFFER](https://idownloadcoupon.com/udemy/2558/)
* Breakthrough Job Hunt – The Crash Course[REDEEM OFFER](https://id
ownloadcoupon.com/udemy/2557/)
* Complete WhatsApp Marketing Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2556
/)
* AWS Certified Solutions Architect Associate SAA-C03[REDEEM OFFER](https://idownloadcoupon.com/udemy/2555/)
* After 
Effects for Graphic Design[REDEEM OFFER](https://idownloadcoupon.com/udemy/2554/)
* Palo Alto Network Security Admin (PC
NSA) Practice Question[REDEEM OFFER](https://idownloadcoupon.com/udemy/2553/)
* CCNP Secure Solutions Virtual Private Ne
tworks Exam: 300-730[REDEEM OFFER](https://idownloadcoupon.com/udemy/2552/)
* Google Certified Cloud Digital Leader Prac
tice Exam 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/2551/)
* The Practical BPMN 2.0 Master Class[REDEEM OFFER
](https://idownloadcoupon.com/udemy/2550/)
* Text Mining Proficiency Assessment: Practice Exam Tests[REDEEM OFFER](https
://idownloadcoupon.com/udemy/2549/)
* Success Exam | Python NLTK : Natural Language ToolKit | NLP[REDEEM OFFER](https://
idownloadcoupon.com/udemy/2548/)
* Exam Test for Python OCR: Optical Character Recognition OCR[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/2547/)
* The Pandas Bootcamp | Data Analysis with Pandas Python3[REDEEM OFFER](https://idownloadc
oupon.com/udemy/2546/)
* Linux Command-Line & Shell Scripting for Absolute Beginners[REDEEM OFFER](https://idownloadcoup
on.com/udemy/2545/)
* Learn C# Programming with Examples in ONE DAY[REDEEM OFFER](https://idownloadcoupon.com/udemy/2544
/)
* Python Numpy Data Analysis for Data Scientist | AI | ML | DL[REDEEM OFFER](https://idownloadcoupon.com/udemy/2543/)

* Outstanding | Python Programming with Examples in One Day[REDEEM OFFER](https://idownloadcoupon.com/udemy/2542/)
* Am
azon Dropshipping || Your Path to Become Premium Seller[REDEEM OFFER](https://idownloadcoupon.com/udemy/2541/)
* Advance
d Process Modelling with BPMN 2.0[REDEEM OFFER](https://idownloadcoupon.com/udemy/2540/)
* HAP Master Course with Comple
te Projects[REDEEM OFFER](https://idownloadcoupon.com/udemy/2539/)
* Simulation of Electronic Circuits by Proteus in Ara
bic[REDEEM OFFER](https://idownloadcoupon.com/udemy/2538/)
* Instagram Marketing: Growth and Promotion on Instagram[REDE
EM OFFER](https://idownloadcoupon.com/udemy/2535/)
* How to Make Money on MEXC (Ultimate MEXC Tutorial)[REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/2536/)
* 15 machine learning projects 2024[REDEEM OFFER](https://idownloadcoupon.com/ude
my/2534/)
* Mastering Complexity in Problem Solving and Decision Making[REDEEM OFFER](https://idownloadcoupon.com/udemy/
2533/)
* Programming the Microcontroller using MikroC PRO for PIC[REDEEM OFFER](https://idownloadcoupon.com/udemy/2532/)

* Basic Electronics – Test your knowledge. (Multiple Choice)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2530/)
* P
ython flask framework 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/2531/)
* Learning the Professional Design Pro
gram Edraw Max in Arabic[REDEEM OFFER](https://idownloadcoupon.com/udemy/2529/)
* Microsoft Excel – Excel from Beginner 
to Advanced level[REDEEM OFFER](https://idownloadcoupon.com/udemy/2528/)
* Top 100 python interview questions[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/2526/)
* 3 real world deep learning projects[REDEEM OFFER](https://idownloadcoupon
.com/udemy/2525/)
* Gut-Brain Axis Uncovered[REDEEM OFFER](https://idownloadcoupon.com/udemy/2524/)
* Comprehensive Stra
tegic Planning: A Guided Approach[REDEEM OFFER](https://idownloadcoupon.com/udemy/2523/)
* 10 data science projects 2024
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2522/)
* Microsoft Azure Fundamentals AZ 900[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/2521/)
* Master the CompTIA A+ (220-1101) Core 1 Exam: Practice Tests[REDEEM OFFER](https://idownl
oadcoupon.com/udemy/2520/)
* List Building Formula: Learn Email Marketing & Grow Business[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/2518/)
* Python PCAP: Certified Associate in Python Programming\[2024\][REDEEM OFFER](https://idownloa
dcoupon.com/udemy/2517/)
* CCNA Success Blueprint 2024 : Utimate Test Series[REDEEM OFFER](https://idownloadcoupon.com/u
demy/2516/)
* Mastering Pointers in C : A Course on Efficient Programming[REDEEM OFFER](https://idownloadcoupon.com/udem
y/2515/)
* Physics – Newton’s Laws for High School and Intro College[REDEEM OFFER](https://idownloadcoupon.com/udemy/251
4/)
* 2024 C Programming Bootcamp – The Complete C Language Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2513/
)
* Certificate in Lean Six Sigma Foundations[REDEEM OFFER](https://idownloadcoupon.com/udemy/2512/)
* Corporate Finance
 #8 Time Value of Money (PV & FV)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2511/)
```
---

     
 
all -  [ Best Udemy Paid Courses For Free With Certificate | Hurry Don’t Miss | Tuesday, March 19, 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1bikf9p/best_udemy_paid_courses_for_free_with_certificate/) , 2024-03-21-0911
```
## Udemy Free Courses for 19 March 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.*

* Microsoft Excel Fundamentals: A Beginners Guide[REDEEM OFFER](https://idownloadcoupon.com/udemy/25
77/)
* The “BigTech” System Design Interview Bootcamp[REDEEM OFFER](https://idownloadcoupon.com/udemy/2576/)
* Mastering
 LangChain and AWS: A Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/2575/)
* Build laravel 
apps fast with blueprint[REDEEM OFFER](https://idownloadcoupon.com/udemy/2574/)
* Business Model Canvas Mastery: Learn H
ow Business Model Work[REDEEM OFFER](https://idownloadcoupon.com/udemy/2573/)
* ChatGPT for Mastering Compelling Content
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2572/)
* Upgrade Your Social Media Presence with ChatGPT[REDEEM OFFER](
https://idownloadcoupon.com/udemy/2571/)
* Discover Google Gemini for Marketing Success[REDEEM OFFER](https://idownloadc
oupon.com/udemy/2570/)
* Apache Spark Project World Development Indicators Analytics[REDEEM OFFER](https://idownloadcoup
on.com/udemy/2569/)
* ChatGPT & Midjourney & Gemini: Digital Marketing Assistants[REDEEM OFFER](https://idownloadcoupon.
com/udemy/2568/)
* Grow your business with Chatbot MarketingREDEEM OFFER
* Digital Marketing Automation: One Step Ahead 
of Competitors[REDEEM OFFER](https://idownloadcoupon.com/udemy/2566/)
* Midjourney For Beginners: Creating Visuals Using
 AI[REDEEM OFFER](https://idownloadcoupon.com/udemy/2565/)
* Mastering SEO With ChatGPT: Ultimate Beginner’s Guide[REDEE
M OFFER](https://idownloadcoupon.com/udemy/2564/)
* You Can Deliver a TED-Style Talk Presentation (Unofficial)[REDEEM OF
FER](https://idownloadcoupon.com/udemy/2563/)
* Podcasting: How to Speak Effectively on Your Own Podcast[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/2562/)
* Interviewing Skills for Jobs: Ace the Job Interview[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/2561/)
* Ace Your Python Interview: Essential Practice Tests (2024)[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/2560/)
* PHP with MySQL 2024: Build Complete Coffee Shop System[REDEEM OFFER](https://idownloadcoupon.
com/udemy/2559/)
* AZ-800 Administering Windows Server Hybrid Latest Exam[REDEEM OFFER](https://idownloadcoupon.com/udem
y/2558/)
* Breakthrough Job Hunt – The Crash Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2557/)
* Complete Wh
atsApp Marketing Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2556/)
* AWS Certified Solutions Architect Assoc
iate SAA-C03[REDEEM OFFER](https://idownloadcoupon.com/udemy/2555/)
* After Effects for Graphic Design[REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/2554/)
* Palo Alto Network Security Admin (PCNSA) Practice Question[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/2553/)
* CCNP Secure Solutions Virtual Private Networks Exam: 300-730[REDEEM OFFER](https://i
downloadcoupon.com/udemy/2552/)
* Google Certified Cloud Digital Leader Practice Exam 2024[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/2551/)
* The Practical BPMN 2.0 Master Class[REDEEM OFFER](https://idownloadcoupon.com/udemy/2550/)
*
 Text Mining Proficiency Assessment: Practice Exam Tests[REDEEM OFFER](https://idownloadcoupon.com/udemy/2549/)
* Succes
s Exam | Python NLTK : Natural Language ToolKit | NLP[REDEEM OFFER](https://idownloadcoupon.com/udemy/2548/)
* Exam Test
 for Python OCR: Optical Character Recognition OCR[REDEEM OFFER](https://idownloadcoupon.com/udemy/2547/)
* The Pandas B
ootcamp | Data Analysis with Pandas Python3[REDEEM OFFER](https://idownloadcoupon.com/udemy/2546/)
* Linux Command-Line 
& Shell Scripting for Absolute Beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/2545/)
* Learn C# Programming w
ith Examples in ONE DAY[REDEEM OFFER](https://idownloadcoupon.com/udemy/2544/)
* Python Numpy Data Analysis for Data Sci
entist | AI | ML | DL[REDEEM OFFER](https://idownloadcoupon.com/udemy/2543/)
* Outstanding | Python Programming with Exa
mples in One Day[REDEEM OFFER](https://idownloadcoupon.com/udemy/2542/)
* Amazon Dropshipping || Your Path to Become Pre
mium Seller[REDEEM OFFER](https://idownloadcoupon.com/udemy/2541/)
* Advanced Process Modelling with BPMN 2.0[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/2540/)
* HAP Master Course with Complete Projects[REDEEM OFFER](https://idownloadc
oupon.com/udemy/2539/)
* Simulation of Electronic Circuits by Proteus in Arabic[REDEEM OFFER](https://idownloadcoupon.co
m/udemy/2538/)
* Instagram Marketing: Growth and Promotion on Instagram[REDEEM OFFER](https://idownloadcoupon.com/udemy/
2535/)
* How to Make Money on MEXC (Ultimate MEXC Tutorial)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2536/)
* 15 
machine learning projects 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/2534/)
* Mastering Complexity in Problem 
Solving and Decision Making[REDEEM OFFER](https://idownloadcoupon.com/udemy/2533/)
* Programming the Microcontroller usi
ng MikroC PRO for PIC[REDEEM OFFER](https://idownloadcoupon.com/udemy/2532/)
* Basic Electronics – Test your knowledge. 
(Multiple Choice)[REDEEM OFFER](https://idownloadcoupon.com/udemy/2530/)
* Python flask framework 2024[REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/2531/)
* Learning the Professional Design Program Edraw Max in Arabic[REDEEM OFFER](https
://idownloadcoupon.com/udemy/2529/)
* Microsoft Excel – Excel from Beginner to Advanced level[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/2528/)
* Top 100 python interview questions[REDEEM OFFER](https://idownloadcoupon.com/udemy/2526/)

* 3 real world deep learning projects[REDEEM OFFER](https://idownloadcoupon.com/udemy/2525/)
* Gut-Brain Axis Uncovered
[REDEEM OFFER](https://idownloadcoupon.com/udemy/2524/)
* Comprehensive Strategic Planning: A Guided Approach[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/2523/)
* 10 data science projects 2024[REDEEM OFFER](https://idownloadcoupon.com/u
demy/2522/)
* Microsoft Azure Fundamentals AZ 900[REDEEM OFFER](https://idownloadcoupon.com/udemy/2521/)
* Master the Co
mpTIA A+ (220-1101) Core 1 Exam: Practice Tests[REDEEM OFFER](https://idownloadcoupon.com/udemy/2520/)
* List Building F
ormula: Learn Email Marketing & Grow Business[REDEEM OFFER](https://idownloadcoupon.com/udemy/2518/)
* Python PCAP: Cert
ified Associate in Python Programming\[2024\][REDEEM OFFER](https://idownloadcoupon.com/udemy/2517/)
* CCNA Success Blue
print 2024 : Utimate Test Series[REDEEM OFFER](https://idownloadcoupon.com/udemy/2516/)
* Mastering Pointers in C : A Co
urse on Efficient Programming[REDEEM OFFER](https://idownloadcoupon.com/udemy/2515/)
* Physics – Newton’s Laws for High 
School and Intro College[REDEEM OFFER](https://idownloadcoupon.com/udemy/2514/)
* 2024 C Programming Bootcamp – The Comp
lete C Language Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/2513/)
* Certificate in Lean Six Sigma Foundation
s[REDEEM OFFER](https://idownloadcoupon.com/udemy/2512/)
* Corporate Finance #8 Time Value of Money (PV & FV)[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/2511/)
```
---

     
 
all -  [ Multi Needle in a haystack ](https://www.reddit.com/r/LocalLLaMA/comments/1bikes9/multi_needle_in_a_haystack/) , 2024-03-21-0911
```
https://blog.langchain.dev/multi-needle-in-a-haystack/

This seems rather interesting. Have not seen people talking abou
t it. What's your thoughts?
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-21-0911
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-21-0911
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-21-0911
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-21-0911
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
