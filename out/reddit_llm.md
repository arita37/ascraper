 
all -  [ I tested LANGCHAIN vs VANILLA speed ](https://www.reddit.com/r/LangChain/comments/1cbj7gg/i_tested_langchain_vs_vanilla_speed/) , 2024-04-24-0910
```
**Code of pure implementation through POST to local ollama** [**http://localhost:11434/api/chat**](http://localhost:1143
4/api/chat) **(3.2s):**

    import aiohttp
    from dataclasses import dataclass, field
    from typing import List
   
 import time
    start_time = time.time()
    
    @dataclass
    class Message:
        role: str
        content: str

    
    @dataclass
    class ChatHistory:
        messages: List[Message] = field(default_factory=list)
    
        de
f add_message(self, message: Message):
            self.messages.append(message)
    
    @dataclass
    class RequestDa
ta:
        model: str
        messages: List[dict]
        stream: bool = False
    
        @classmethod
        def f
rom_params(cls, model, system_message, history):
            messages = [
                {'role': 'system', 'content': 
system_message},
                *[{'role': msg.role, 'content': msg.content} for msg in history.messages],
            
]
            return cls(model=model, messages=messages, stream=False)
    
    class LocalLlm:
        def __init__(sel
f, model='llama3:8b', history=None, system_message='You are a helpful assistant'):
            self.model = model
      
      self.history = history or ChatHistory()
            self.system_message = system_message
    
        async def as
k(self, input=''):
            if input:
                self.history.add_message(Message(role='user', content=input))
 
   
            data = RequestData.from_params(self.model, self.system_message, self.history)
    
            url = 'ht
tp://localhost:11434/api/chat'
            async with aiohttp.ClientSession() as session:
                async with ses
sion.post(url, json=data.__dict__) as response:
                    result = await response.json()
                    p
rint(result['message']['content'])
    
            if result['done']:
                ai_response = result['message']['
content']
                self.history.add_message(Message(role='assistant', content=ai_response))
                retur
n ai_response
            else:
                raise Exception('Error generating response')
    
    
    if __name__ =
= '__main__':
        chat_history = ChatHistory(messages=[
            Message(role='system', content='You are a crazy 
pirate'),
            Message(role='user', content='Can you tell me a joke?')
        ])
    
        llm = LocalLlm(his
tory=chat_history)
        import asyncio
        response = asyncio.run(llm.ask())
        print(response)
        prin
t(llm.history)
        print('--- %s seconds ---' % (time.time() - start_time))
    

`--- 3.2285749912261963 seconds --
-`

&#x200B;

**Lang chain equivalent (3.5 s):**

    from langchain_core.messages import HumanMessage, SystemMessage, A
IMessage, BaseMessage
    from langchain_community.chat_models.ollama import ChatOllama
    from langchain.memory import
 ChatMessageHistory
    import time
    start_time = time.time()
    
    class LocalLlm:
        def __init__(self, mod
el='llama3:8b', messages=ChatMessageHistory(), system_message='You are a helpful assistant', context_length = 8000):
   
         self.model = ChatOllama(model=model, system=system_message, num_ctx=context_length)
            self.history = 
messages
    
        def ask(self, input=''):
            if input:
                self.history.add_user_message(input
)
            response = self.model.invoke(self.history.messages)
            self.history.add_ai_message(response)
    
        return response
    
    if __name__ == '__main__':
        chat = ChatMessageHistory()
        chat.add_message
s([
            SystemMessage(content='You are a crazy pirate'),
            HumanMessage(content='Can you tell me a jok
e?')
        ])
        print(chat)
        llm = LocalLlm(messages=chat)
        print(llm.ask())
        print(llm.his
tory.messages)
        print('--- %s seconds ---' % (time.time() - start_time))
    

`--- 3.469588279724121 seconds ---
`

&#x200B;

&#x200B;

So it's 3.2 vs 3.469(nice) so the difference so 0.3s difference is nothing.  
Made this post beca
use was so upset over [this post](https://www.reddit.com/r/LangChain/comments/1c6zktz/llms_frameworks_langchain_llamaind
ex_griptape/) after getting to know langchain and finally coming up with some results. I think it's true that it's not v
ery suitable for serious development, but it's perfect for theory crafting and experimenting, but anyways you can just w
rite your own abstractions which you know. 
```
---

     
 
all -  [ No avoiding langchain? ](https://www.reddit.com/r/LocalLLaMA/comments/1cbhu0e/no_avoiding_langchain/) , 2024-04-24-0910
```
Hi all,

I've worked with langchain in the past prototyping simple RAG applications and it was a headache constantly fig
hting the APIs or trying to peel the abstractions using the confusing docs.

After that experience I ditched it and have
 done the RAG project just doing everything in raw python and calling the native APIs of each components which made thin
gs so much easier and development enjoyable again.

Recently I've been looking at using agents on a wider scale rather t
han the simple assistant/reviewer pattern and crew.ai really looked promising. Unfortunately it seems to heavily integra
te langchain which meant delving into the langchain docs is required if you want to customise the base components. Manag
ed to circumvent a lot of it this time by just using a lot of custom tools instead.

My question is should I just bite t
he bullet and learn langchain properly if I want to do more developments beyond the simple chatbots? Might be required i
f most cool new frameworks in the future will be using langchain as the base.
```
---

     
 
all -  [ How to use AI to completely automate your youtube channel ](https://www.reddit.com/r/Automate/comments/1cbhhvd/how_to_use_ai_to_completely_automate_your_youtube/) , 2024-04-24-0910
```
 Hi folks,

I wanted to share with you a cool project I recently undertook that leverages the power of AI to help manage
 my YouTube channel!

The idea was to use [CrewAI](https://www.crewai.com/) to automate tasks like competitor YouTube ch
annel analysis and identify trending topics. This way, I could gauge these topics against my own content ideas to see if
 there is general interest in a given topic.

The AI Crew was designed to crawl the web (Google) and call APIs like the 
YouTube API, Reddit API, and use Google Trends to determine how likely a given topic is to generate engagement.

For thi
s, I created the following AI Assistants (or agents in CrewAI lingo):

* A competitor analysis agent
* A Content Creator
 (to generate ideas from research)
* A Marketing advisor, to generate catchy titles and tags
* An Analytics consultant t
o measure the performance of the video

I used a pretty straightforward setup that relied on the usual suspects:

* Anac
onda
* Python 3.11
* A few modules like pytrend, praw, serper, and langchain

I tested it with models like GPT-4, GPT-4-
Turbo, and a few local models like nous-hermes 2, mistral, and codellama, among others.

The results from GPT-4-Turbo we
re AMAZING, and I'm sure I can make them better by fine tuning the data going into the model, but they were not really t
hat great with local AI, which was quite expected given the imense number of tokens. However I was quite positively surp
rised by the performance of Nous Hermes 2 - 13b. Not only did it actually run, but it used the tools I custom build for 
it! Quite impressive really

The video is available below:

[https://youtu.be/5JoVeYcxgpU?si=cxFwHO1x\_zCghMYB](https://
youtu.be/5JoVeYcxgpU?si=cxFwHO1x_zCghMYB)

You are more than welcome to try out the code for yourselves: [https://github
.com/fmiguelmmartins/crewaiyoutube](https://github.com/fmiguelmmartins/crewaiyoutube)

And here is an article on Medium 
with the step-by-step process (don't worry, I have a free account):

[https://medium.com/@fmiguelmmartins/create-an-ai-t
eam-to-manage-your-youtube-channel-5dc1e6c9b31b](https://medium.com/@fmiguelmmartins/create-an-ai-team-to-manage-your-yo
utube-channel-5dc1e6c9b31b)

Hope you guys enjoy it, and if you are kind enough, please leave me some feedback so I can 
improve over time!

Thank you!

Filipe
```
---

     
 
all -  [ Langchain vs llamaindex ](https://www.reddit.com/r/LangChain/comments/1cbfeci/langchain_vs_llamaindex/) , 2024-04-24-0910
```
I'm using llamaindex for a multilingual database retriever system and using claude as the provider. I'm interested in in
tegrating external apis( function calling) and knowledge graphs.

Separately it'd also be helpful to have the ability to
 manage states within a conversation and langgraph seems to meet the criteria.

Should I switch to langchain and rewrite
 my early stage code? Does langchain function calling work well with Claude? does llamaindex offer langgraph like abilit
ies or good integration with neo4j?
```
---

     
 
all -  [ preserving the Gemini state with Langchain for caching responses ](https://www.reddit.com/r/LangChain/comments/1cbf1au/preserving_the_gemini_state_with_langchain_for/) , 2024-04-24-0910
```
hi there, so my issue is that i want to preserve the chat history with gemini, and according to need manipulate it, i ca
n do it in google provided sdk, i dont know how to do that in langchain, i want to manupilate chat history and according
 to need, delete some responces, add new responces from the database.

also, i am only interested in langchain responses
 (semantic) caching support, if i can do caching without the need of langchain or implementing a rag myself manually, i 
am all up for that solution!
```
---

     
 
all -  [ How to structure the vector store and retrieval for user files RAG? ](https://www.reddit.com/r/LangChain/comments/1cbdk3m/how_to_structure_the_vector_store_and_retrieval/) , 2024-04-24-0910
```
Hey all. I'm building a simple chatbot that will let users hold their own documents to use in RAG; basically I just want
 them to be able to ask questions related to what's on their own files. I'm using LangChain of course, using postgres wi
th the pgvector extension. 

My question is, what's the most optimized way to design the documents table(s) in order for
 users to only be able to search their own files? Do you create separate doc tables for each user? Do you filter through
 metadata or some other technique? Metadata filtering in particular doesn't look like it'd be too optimized, so I'm just
 looking into how best to think about storing and retrieving from a vector store for this use case. I don't want the bot
 to be able to find the answer in another user's files.

Or am I just thinking about the whole thing in the wrong way an
d is there a better way to structure all  this? 

Thanks a lot in advance!
```
---

     
 
all -  [ How to solve if relevant docs > max top_k ? ](https://www.reddit.com/r/LangChain/comments/1cbcln9/how_to_solve_if_relevant_docs_max_top_k/) , 2024-04-24-0910
```
Basically if I have a pdf of 100 pages and to answer my question I need 30 diff chunks across diff pages. 
Now if my top
_k is set to 20. How will this ever be possible?

Like in general, isn't this a issue with RAGs? How can I know how many
 chunks are needed to answer a question? If it's less than whatever topk I set, it's fine. But what if there are more?


Is this a limitation of RAG? If no, how to solve for this?
If yes, what other ways can I explore?
```
---

     
 
all -  [ [thread] The best open-source only AI models ](https://www.reddit.com/r/ChatGPT/comments/1cbbklh/thread_the_best_opensource_only_ai_models/) , 2024-04-24-0910
```
Hello community! If you know some good models and fine-tuning options, please feel free to share them:

- Image Captioni
ng (img-to-text)
- Video Captioning (video-to-text)
- Audio Captioning (music understanding to describe how somebody sin
gs and music)
- Image Generation (text-to-image, LoRAs, Checkpoints)
- LLMs (general knowledge, uncensored)
- Instrument
al and Vocal music generation (text-to-music/audio, or/and with source audio)
- Video generation (sora-like text/image-t
o-video)
- 2D animation (talking head, anime)
- Voice Cloning (except RVC)
- TTS (with unlabeled voice patterns training
 and fast generations)
- LangChain and Long-Term memory raw code examples

And please, with Apple Silicon (M1) support!!
!!!
```
---

     
 
all -  [ Getting totals and counts based on the entire dataset with RetrievalQA ](https://www.reddit.com/r/LangChain/comments/1cb9mab/getting_totals_and_counts_based_on_the_entire/) , 2024-04-24-0910
```
Hello guys, I'm new on this of NPL and Langchain, I'm currently working on a chatbot to 'talk' to my data, converting pa
ndas dataframes into JSON and every row in dataframe is a document saved into Vector Store (I'm using Milvus as Vector D
atabase). 

For questions related to 1 to N (getting one row from many), the similarity search is working as expected an
d I am achieving good results.

For example, if I asking 'where this store is located?' or 'how many displays has Store 
A?' is working, but if I ask something about the entire dataset as 'how many displays are overall in US?', or 'how many 
displays are in California?', the totalization is related to the 'k' passed to the vector retriever:

    retriever = Ve
ctorStoreRetriever(
        vectorstore=vector,
        search_type='similarity',
        search_kwargs={'k': 10}
    ) 
       
    chain = RetrievalQA.from_chain_type(
     llm=llm,
     retriever=retriever,
     chain_type='stuff',
     v
erbose=True
    )
    

  
I cannot pass a bigger 'K' because my LLM rejects it (I'm using Google Gemini-Pro).

  
There
 is a way to:

1. Check if the user's question involves a quantification.
2. Executing something like a 'Map Reduce' ove
r the entire dataset to return the reduced version of the documents (or documents with question applied).
3. Passing the
 reduction to the LLM for getting the final result.

Or if there is a way to making this in Langchain using another type
 on Chain.
```
---

     
 
all -  [ How can I see the input that is passed to the output parser when the commands are chained? ](https://www.reddit.com/r/LangChain/comments/1cb7rx7/how_can_i_see_the_input_that_is_passed_to_the/) , 2024-04-24-0910
```
This is the excerpt from my code:  
`chain = prompt_template | ollama | output_parser`

How do I store the output from `
ollama` as a variable and then pass that output to `output_parser`?  


I don't understand how the pipe operator | works
. I am asking the ollama model to give me a structured output and I need to be able to debug and see what the output was
 when the output\_parser gives an error.
```
---

     
 
all -  [ Langsmith render of retrieved documents ](https://www.reddit.com/r/LangChain/comments/1cb68b9/langsmith_render_of_retrieved_documents/) , 2024-04-24-0910
```
I have been using langsmith for controling the retrieving step of my rag application. And it's nice because it has a ren
der that format the raw langchain docs in a more readable format. 

The problem is that since I changed the format of my
 langchain docs, adding more metadata, this feature does not work anymore. Do anyone has got any advice on what's the ri
ght format compatible to the render??

now: 

https://preview.redd.it/7leugfcup8wc1.png?width=1266&format=png&auto=webp&
s=f7738461ab2add7e587aeb9aed415a5b2e1f6c20

BEFORE:

https://preview.redd.it/8s86iy6xp8wc1.png?width=1287&format=png&aut
o=webp&s=302f1f3b2923f428288c59c29f31327d5d9b6db0


```
---

     
 
all -  [ Use Golang to develop Agentic applications with LLMs ](https://www.reddit.com/r/llmops/comments/1cb570i/use_golang_to_develop_agentic_applications_with/) , 2024-04-24-0910
```
[ZenModel](https://github.com/zenmodel/zenmodel) is a workflow programming framework designed for constructing agentic a
pplications with LLMs. It implements by the scheduling of computational units (`Neuron`), that may include loops, by con
structing a `Brain` (a directed graph that can have cycles) or support the loop-less DAGs. A `Brain` consists of multipl
e `Neurons` connected by `Link`s. Inspiration was drawn from [LangGraph](https://github.com/langchain-ai/langgraph). The
 `Memory` of a `Brain` leverages [ristretto](https://github.com/dgraph-io/ristretto) for its implementation.

**Agent Ex
amples developed by** [ZenModel](https://github.com/zenmodel/zenmodel) **framework**

* [Chat Agent With Tools](https://
github.com/zenmodel/zenmodel/blob/main/examples/chat_agent/chat_agent_with_function_calling)
* [Basic Reflection](https:
//github.com/zenmodel/zenmodel/blob/main/examples/reflection/main.go)
* [Plan & Execute](https://github.com/zenmodel/zen
model/blob/main/examples/plan-and-excute)
* [Multi-Agent](https://github.com/zenmodel/zenmodel/blob/main/examples/multi-
agent/agent-supervisor)
```
---

     
 
all -  [ How does chunk size relate to an embedding model's dimension of vectors and max token lenght? ](https://www.reddit.com/r/LangChain/comments/1cb4yjd/how_does_chunk_size_relate_to_an_embedding_models/) , 2024-04-24-0910
```
Hi, everyone! I'm fairly new to NLP tasks, and I'm currently building a langchain RAG app, and for that I need to do som
e testings with different chunks sizes.

I'm currently using a large BERT model, and what I've been confused about is: W
hat is the relationship between the chunk size chosen to chunk my documents, and the embedding model's vector dimension 
(if there is any) or even the max token limit?

I've seen a wide range of articles from people testings out chunk sizes 
from 128 to 2048, but I've also read in some places that the original BERT models take 512 tokens max. What does that in
fluence on the way I'm doing things?

I'm creating embeddings like this: Using RecursiveCharacterSplitter with different
 chunks sizes and len function using my bert model's tokenizer and finally creating embeddings with HuggingFaceBgeEmbedd
ings (arbitrary choice, I couldn't figure out which class to choose) and storing on a vector store.

I iterated over my 
chunked documents (splitted using the same flow mentioned above) and their sizes nor the amount of tokens gotten from to
kenizing it directly are equal to my chunk\_size:

https://preview.redd.it/s9txv1rej8wc1.png?width=1015&format=png&auto=
webp&s=a11725cf9967ec9a04ddad46f8c2bedc587d7ed8

But the actual embeddings are generated with dimension 1024 (which is t
he correct value for vector dimensions for large bert models):

https://preview.redd.it/9dta4kymj8wc1.png?width=1210&for
mat=png&auto=webp&s=31c1787b790d1ecabe5a91c54735b5f0dded62de

The reason I'm asking this is because I've been gettting s
ome weird results analyzing results with chunks bigger than 512 (this graph is a comparison of the chunk overlap with fi
xed chunk size = 1024, where the results don't really vary even though I'm varying other parameters, like chunk overlap 
here, which does affect other chunk sizes comparisons)

https://preview.redd.it/x7qwsfo2g8wc1.png?width=1015&format=png&
auto=webp&s=a3c2273dbe60d07c6974d64802b1b6391398e3d0
```
---

     
 
all -  [ Query with langchain's parent-child retriever ](https://www.reddit.com/r/LangChain/comments/1cb4xpb/query_with_langchains_parentchild_retriever/) , 2024-04-24-0910
```
I have a requirement to create parent-child retrieval mechanism for texts. On langchain's official docs I can see the be
low code:

    #This text splitter is used to create the parent documents
    parent_splitter = RecursiveCharacterTextSp
litter(chunk_size=2000)
    
    #This text splitter is used to create the child documents
    #It should create documen
ts smaller than the parent
    child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
    
    #The vectorstore
 to use to index the child chunks
    vectorstore = Chroma( collection_name='split_parents',embedding_function=OpenAIEmb
eddings() )
    
    #The storage layer for the parent documents
    store = InMemoryStore()
    
    retriever = Parent
DocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
     
   parent_splitter=parent_splitter,
    )

My question is why there is no **split\_text()** for each parent and child ch
unks that actually splits te document?

&#x200B;
```
---

     
 
all -  [ Use Golang to develop Agentic applications with LLMs ](https://www.reddit.com/r/LLMDevs/comments/1cb4wcz/use_golang_to_develop_agentic_applications_with/) , 2024-04-24-0910
```
[ZenModel](https://github.com/zenmodel/zenmodel) is a workflow programming framework designed for constructing agentic a
pplications with LLMs. It implements by the scheduling of computational units (`Neuron`), that may include loops, by con
structing a `Brain` (a directed graph that can have cycles) or support the loop-less DAGs. A `Brain` consists of multipl
e `Neurons` connected by `Link`s. Inspiration was drawn from [LangGraph](https://github.com/langchain-ai/langgraph). The
 `Memory` of a `Brain` leverages [ristretto](https://github.com/dgraph-io/ristretto) for its implementation.

**Agent Ex
amples developed by** [**ZenModel**](https://github.com/zenmodel/zenmodel) **framework**

* [Chat Agent With Tools](http
s://github.com/zenmodel/zenmodel/blob/main/examples/chat_agent/chat_agent_with_function_calling)

https://preview.redd.i
t/mpvv198ie8wc1.png?width=595&format=png&auto=webp&s=d81cad5e81b9ca56e879da3c2bb4c24cd932f1c9

* [Basic Reflection](http
s://github.com/zenmodel/zenmodel/blob/main/examples/reflection/main.go)

https://preview.redd.it/q0xdzvhje8wc1.png?width
=617&format=png&auto=webp&s=7d9cd9d0c0ca4cd54fd240855f69077ffc94da0e

* [Plan & Execute](https://github.com/zenmodel/zen
model/blob/main/examples/plan-and-excute)

https://preview.redd.it/fai7axjke8wc1.png?width=686&format=png&auto=webp&s=d4
606196a86bce55632b72f911c9f05de327cf89

* [Multi-Agent](https://github.com/zenmodel/zenmodel/blob/main/examples/multi-ag
ent/agent-supervisor)

https://preview.redd.it/sd4rv4ple8wc1.png?width=502&format=png&auto=webp&s=22ed17e1ff3245f0ffd23a
18aca1b172798014ae


```
---

     
 
all -  [ Updation of PDFs using RAG ](https://www.reddit.com/r/RagAI/comments/1cb3geo/updation_of_pdfs_using_rag/) , 2024-04-24-0910
```
I am trying to build a chatbot using RAG and LangChain that will update the PDFs based on the user prompt and the pdfs w
ill be stored in a db (chromedb) that will be connected to the chatbot. I'm planning to use OpenAI for chunking and inde
xing information that will be analyzed by the bot.

It will be helpful if anyone can tell me how to proceed further with
 this. I have only found projects and repos which focus on QA chatbots so I just want to extend this project to include 
this functionality.
```
---

     
 
all -  [ Chat-bot using RAG to update PDFs ](https://www.reddit.com/r/LangChain/comments/1cb35fa/chatbot_using_rag_to_update_pdfs/) , 2024-04-24-0910
```
I am trying to build a chatbot using RAG and LangChain that will update the PDFs based on the user prompt and the pdfs w
ill be stored in a db (chromedb) that will be connected to the chatbot. I'm planning to use OpenAI for chunking and inde
xing information that will be analyzed by the bot. 

It will be helpful if anyone can tell me how to proceed further wit
h this. I have only found projects and repos which focus on QA chatbots so I just want to extend this project to include
 this functionality.
```
---

     
 
all -  [ Llama 3 70b is not great with tools ](https://www.reddit.com/r/AI_Agents/comments/1cb2zf7/llama_3_70b_is_not_great_with_tools/) , 2024-04-24-0910
```
Hi all,

I run and crew_ai crew that does process engineering by using the langchain human tool to conduct an interview 
with a business owner to understand the business process, understand it, model it in bpmn and then identify potential fo
r improvements. GPT 4 turbo is actually decent at doing this. It actually understands when to ask the human as part of t
he interview and when to actually think for itself.

Llama3 on the other hand always uses the human tool even though it 
totally does not make sense in context of the interview. For example, ChatGPT will consider „what are important steps du
ring an interview to engineer a business process“ before asking questions. Llama will just plainly request the answer fr
om the human.

Solution could be to have more agents and subtasks to actually restrain when LLama gets access to the hum
an, but for now, GOT seems way easier to use.
```
---

     
 
all -  [ Using local LLMS instead of LLMS such as OpenAI on LangChain using JS,TS ](https://www.reddit.com/r/LLMDevs/comments/1cb0we4/using_local_llms_instead_of_llms_such_as_openai/) , 2024-04-24-0910
```
Hey guys, i'm fairly new to this and i was searching for a way to use my own locally installed LLMs from HuggingFace. I 
looked through the official documentation and this is the normal way to invoke and get a response using JS

\-----------
---------------------------------------------------------------------

const chatModel = new ChatOpenAI({});

const resp
onse = await chatModel.invoke()

\--------------------------------------------------------------------------------

So y
ea, referring back to my question. Can you guys provide me some documentations or some ways to use my own LLMs from Hugg
ingFace and not having to specify out using the ChatOpenAI class in a NodeJS project i'm working on? Thanks a bunch
```
---

     
 
all -  [ What embedding model to use to convert textual data in PDF when using FAISS ](https://www.reddit.com/r/LangChain/comments/1cb0p5d/what_embedding_model_to_use_to_convert_textual/) , 2024-04-24-0910
```
I am getting a lot of errors and it particularly because the FAISS index expects a particular shape for embeddings and e
ven after I resolved that. I cannot get the right response to my query or some or the other errors are popping up?
NOTE:
 I can’t use langchain 
```
---

     
 
all -  [ How to integrate GenAI in full stack applications? ](https://www.reddit.com/r/developersIndia/comments/1cb0lpj/how_to_integrate_genai_in_full_stack_applications/) , 2024-04-24-0910
```
Hello everyone, I started working at a small company as Generative AI developer, and currently there is another Mern Sta
ck Developer who will be working with me.   
Now, we have been tasked at creating a full stack application, but we are k
ind stuck, on how to integrate Generative AI tools (llama index, langchain, litellm, RAG etc) in a MERN stack app?   
Th
ere are 3 ways which we thought of,  
1. Make Python the main backend framework and write the full backend code in Djang
o instead of express.

2.  Make 2 separate backends, 1 that serves the GenAI tools on a FastAPI Framework, and other Exp
ress server that handles rest of the site, but the issue is interaction of both backends, extra latency, extra costs, an
d the flow of data across them.  
3. Create the backend in express and somehow use the tools in JS as possible in python
.

Now to clear up some things, I am a beginner. I had no interest in Web Dev hence I picked up AI and ML since it was o
ne of the things I was very fond of even before the GPT days. Secondly, he has made full stack apps but he hasn't deploy
ed any of them in production.

If we go 1, I'll have to create the whole backend in Django, for the rest of the site as 
well, which is honestly challenging at first but at some point I am also upskilling myself.   
If we go with 3, I will s
till upskill myself by writing JS code for GenAI, but I don't really know how flexible it is compared to python.

So, fe
llow developers who have had experience with full stack GenAI apps in production. please help out a fellow beginner!  
A
ll criticisms welcome.  
Thank You. 
```
---

     
 
all -  [ Can I get only stringified json as an output from LLM model. ](https://www.reddit.com/r/LocalLLaMA/comments/1cb0gfs/can_i_get_only_stringified_json_as_an_output_from/) , 2024-04-24-0910
```
Literally the title. I am using Mistral 7b instruct v0.2. my usecase is to generate stringified json from prompt. The mi
stral model is doing well as from prompt it does generate the json. But I need it to generate the stringified format of 
that json.

What should I do? I have heard of a framework called as langchain, can it help me here? Or should I consider
 any other model for the same, whichever would be more efficient.

Thanks
```
---

     
 
all -  [ Langchain LCEL explained the easy way ](https://www.reddit.com/r/LangChain/comments/1cb01ch/langchain_lcel_explained_the_easy_way/) , 2024-04-24-0910
```
Hello guys,

Just wrote a new blog post explaining Langchain LCEL in a easier manner: [link](https://www.metadocs.co/). 
 
I really love LCEL (feels a little like functional programing right !?) and wanted to try to explain it in a simpler w
ay.  
Enjoy.
```
---

     
 
all -  [ Reranking after RRF-Hybrid Search? ](https://www.reddit.com/r/LangChain/comments/1cazrxf/reranking_after_rrfhybrid_search/) , 2024-04-24-0910
```
Hey everyone,

me and my company are currently building a(nother) RAG system for our customers in the legal sector. 

We
 are performing a keyword (BM25) + vector search and then using Reciprocal Rank Fusion (RRF) algorithm fuse the combined
 10 top\_k results and feed them into our LLM. 

We have also implemented HyDE (hypothetical document embeddings) [https
://github.com/texttron/hyde](https://github.com/texttron/hyde) to further improve retrieval quality. 

Now I read throug
h a few articles on Medium and Reddit and saw a lot of recommendations to use reranking to further improve results. 

Do
es it make sense to again rerank the results of the hybrid search, even though strictly speaking we already are rerankin
g them based on the output of BM25 + vector search? I specifically thought about Cohere rerank here. 

Thanks and greets
!
```
---

     
 
all -  [ I want a chatgpt 3 or 4 assistant , is there any solution exists for below requirements? If not how  ](https://www.reddit.com/r/LangChain/comments/1cazcu3/i_want_a_chatgpt_3_or_4_assistant_is_there_any/) , 2024-04-24-0910
```


 
I want a chatgpt 3 or 4 assistant which will have access to my calendar 
Also able to create daily todo list 
Help m
e brain stom ideas and save it somewhere like a document.
It should remember all old conversations 
It should have conte
xtual awareness of the document files and also able to write to it 
```
---

     
 
all -  [ How do I get more 'natural' answers while using RAG FOR QA? ](https://i.redd.it/koskaj5zq6wc1.png) , 2024-04-24-0910
```
I've been working on a project to answer a student's questions from a syllabus' content. I've been able to do the retrie
val part but as can be seen in the pic above, the answer is purely extractive. I've used Langchain to split the text int
o chunks and when it answers a question it includes unnecessary information (eg. Topic heading for the next text). How c
an I make these answers more natural?
```
---

     
 
all -  [ RAG with Google Cloud Services ](https://www.reddit.com/r/googlecloud/comments/1cayxo3/rag_with_google_cloud_services/) , 2024-04-24-0910
```
I am trying to build a RAG application using only Google Cloud Services.  


I am currently using Agent Builder's Data S
tores and GoogleVertexAISearchRetriever which is a LangChain retriever that can call said Data Stores.

I would like to 
build something more customizable for the ingestion part.

What would be the best option for a vector database? Alloydb?
  
I would not mind using an open source database such as Chroma, as long as it lives inside Google Cloud's infrastructu
re and as long as I am charged only through Google. 
```
---

     
 
all -  [ How to Summarize Large Documents with LangChain and OpenAI ](https://thenewstack.io/how-to-summarize-large-documents-with-langchain-and-openai/) , 2024-04-24-0910
```

```
---

     
 
all -  [ Not able to get all the content from the URL by using UnstructuredURLLoader ](https://www.reddit.com/r/LangChain/comments/1caxvfh/not_able_to_get_all_the_content_from_the_url_by/) , 2024-04-24-0910
```
I am trying to fetch URLs using below code but not getting whole content extracted from it, and I am getting :

**\[Docu
ment(page\_content='Enable JavaScript and cookies to continue', metadata={'source': 'https://medium.com/@woyera/how-to-c
hat-with-microsoft-word-documents-using-llama-2-b30faa053284'})\]**

Below is my code:

    loader = UnstructuredURLLoad
er(urls=all_urls)
    urlDocument = loader.load()
```
---

     
 
all -  [ How to aproach this - APi call then email send ](https://www.reddit.com/r/LangChain/comments/1caxhtq/how_to_aproach_this_api_call_then_email_send/) , 2024-04-24-0910
```
 Hello, I would greatly appreciate it if someone could give me a little help on how to approach this problem. I already 
have an API endpoint. My goal is to interact with the API endpoint using Langchain. If I tell the language model to send
 me the result via email, then it should do so; otherwise, it should not send anything, what can i use to achieve the em
ail send intention? thank you for all the help.
```
---

     
 
all -  [ What are the possibilities of agents? ](https://www.reddit.com/r/LocalLLaMA/comments/1caw726/what_are_the_possibilities_of_agents/) , 2024-04-24-0910
```
Hello everyone! Before anything let me put a disclaimer, I am aware that the possibilities are probably endless but this
 is a serious question that I am genuinely interested in:

What can you do with AI Agents? LLAMA, LangChain, LlamaIndex,
 RAG...?

Can someone give me real life examples, and project ideas? I am a software engineer but not in the AI space, a
nd I downloaded the local llama3:7B and played around with it and langchain getting started, I managed to retrieve and p
arse the content from a webpage and then answer questions based on it. This seems really cool but my narrow and inexperi
enced mind only sees the possibility of making chatbots or support bots. I am sure there is more out there, I just canno
t shake of my understanding of what these agents can do to be able to perceive these possibilities.

Would really apprec
iate some good examples of these technologies that I wouldn't think are possible and if its a fun project, a short point
er on how to try and tackle it would be really appreciated!
```
---

     
 
all -  [ What embedding model (open Source) to use for converting >20MB PDF files?  ](https://www.reddit.com/r/LangChain/comments/1cau2lk/what_embedding_model_open_source_to_use_for/) , 2024-04-24-0910
```
What to use for converting files greater than 20MB into embeddings and storing in the vector store?
```
---

     
 
all -  [ How do you handle Langchain SQL Agent in production ](https://www.reddit.com/r/LangChain/comments/1catddf/how_do_you_handle_langchain_sql_agent_in/) , 2024-04-24-0910
```
I've been thinking about this a while. How do you ensure the security of your SQL Agent when running in production?

1. 
Is it safe to allow SQL Agent to query db directly? Will it affect db performance if it goes haywire.
2. We may give SQL
 Agent read only access. But how to add a more fine-grain access - limiting what it can read?
```
---

     
 
all -  [ explain to a 5 year old langchain and crewai and its dependency on langchain? ](https://www.reddit.com/r/LangChain/comments/1carmfv/explain_to_a_5_year_old_langchain_and_crewai_and/) , 2024-04-24-0910
```
  
The docs contain pages and pages of ramblings that I find very difficult to follow  
  
I'm not very bright so please
 explain this to a 5 year old with a real world example?
```
---

     
 
all -  [ Vector database - separate indexes/tables? ](https://www.reddit.com/r/LangChain/comments/1capafo/vector_database_separate_indexestables/) , 2024-04-24-0910
```
Lets say I'm using Pinecone as a vector database and my content is courses, should I organize my indexes by separating m
odules, videos, audio, titles, etc., into different indexes/tables, or should I put them all into one index with metadat
a even though that index/table would get quite large over time?
```
---

     
 
all -  [ Supervised Clustering using RAG ](https://www.reddit.com/r/LangChain/comments/1calwq1/supervised_clustering_using_rag/) , 2024-04-24-0910
```
I have predefined clusters of roughly ~800, each cluster has been built based on items which could be grouped together. 
My task is to put the unclassified items in the relevant clusters. 

Each Cluster takes a row of CSV file with the follo
wing attributes : cluster id, cluster label and the items in the cluster. I built the Vector Database using the CSV file
 and ran the unclassified items through it using the map-rerank query method. In the prompt, I asked to respond me just 
the cluster id if there is a relevant cluster otherwise give -1. I did some fine-tuning of the prompt to get just the cl
uster id but it seems like I always run into some kind of issue because LLM (using GPT4) doesn't respond the cluster id 
in the right format. Is there a way to get the index of the classified vector database row which would inturn be the cor
responding row of the cluster CSV file?
```
---

     
 
all -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-04-24-0910
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

     
 
all -  [ Send multiple parameters through prompt template ](https://www.reddit.com/r/LangChain/comments/1caja59/send_multiple_parameters_through_prompt_template/) , 2024-04-24-0910
```
Hi All,
How can I send multiple parameters through my prompt, for example,

```
from langchain_core.prompts import Promp
tTemplate

template = '''Use the following pieces of context to answer the question at the end.
If you don't know the an
swer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as c
oncise as possible.
Always say 'thanks for asking!' at the end of the answer.

{context}

Question: {question}

Helpful 
Answer:'''
custom_rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {'context': retriever | format_
docs, 'question': RunnablePassthrough()}
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke('
What is Task Decomposition')
```


How to add more parameters?
```
---

     
 
all -  [ Pipeline for RAG and not RAG based on question and retrieved docs ](https://www.reddit.com/r/LangChain/comments/1caic8s/pipeline_for_rag_and_not_rag_based_on_question/) , 2024-04-24-0910
```
Hi there!

I want to implement such thing like use RAG prompt if user question match RAG semantic and regular not RAG pr
ompt, if it doesn’t match.

I’ve came in thoughts with three approaches: 
1. Before retrieval, use semantic router on us
er question and decide which prompt/chain to use based on this

2. After retrieval, when docs count is 0 or their releva
ncy score < some threshold use simple regular prompt 

3. After I’ve got LLM answer I evaluate it and based on evaluatio
n metrics if they are poor, I call LLM again with regular prompt

What do you think about these?
```
---

     
 
all -  [ What’s the best chat with your data app out there? ](https://www.reddit.com/r/LangChain/comments/1cagxf4/whats_the_best_chat_with_your_data_app_out_there/) , 2024-04-24-0910
```
I’m looking for an app/saas where I could upload data such as pdfs, text files maybe even links and be able to summarize
, extract structured data and do general research based on the data provided.

Essentially a RAG as a service. RaaS? 

U
pdate: To be clear, i’m looking for a finished and ready app I can use. I’m not trying to implement it myself. 
```
---

     
 
all -  [ How I made an entire Team with CrewAI to manage my YouTube channel ](https://www.reddit.com/r/ArtificialInteligence/comments/1cagrqi/how_i_made_an_entire_team_with_crewai_to_manage/) , 2024-04-24-0910
```
Hi folks,

I wanted to share with you a cool project I recently undertook that leverages the power of AI to help manage 
my YouTube channel! 

The idea was to use [CrewAI](https://www.crewai.com/) to automate tasks like competitor YouTube ch
annel analysis and identify trending topics. This way, I could gauge these topics against my own content ideas to see if
 there is general interest in a given topic. 

The AI Crew was designed to crawl the web (Google) and call APIs like the
 YouTube API, Reddit API, and use Google Trends to determine how likely a given topic is to generate engagement.

For th
is, I created the following AI Assistants (or agents in CrewAI lingo):

* A competitor analysis agent
* A Content Creato
r (to generate ideas from research)
* A Marketing advisor, to generate catchy titles and tags
* An Analytics consultant 
to measure the performance of the video

I used a pretty straightforward setup that relied on the usual suspects:

* Ana
conda
* Python 3.11
* A few modules like pytrend, praw, serper, and langchain

I tested it with models like GPT-4, GPT-4
-Turbo, and a few local models like nous-hermes 2, mistral, and codellama, among others. 

The results from GPT-4-Turbo 
were AMAZING, and I'm sure I can make them better by fine tuning the data going into the model, but they were not really
 that great with local AI, which was quite expected given the imense number of tokens. However I was quite positively su
rprised by the performance of Nous Hermes 2 - 13b. Not only did it actually run, but it used the tools I custom build fo
r it! Quite impressive really

The video is available below:

[https://youtu.be/5JoVeYcxgpU?si=cxFwHO1x\_zCghMYB](https:
//youtu.be/5JoVeYcxgpU?si=cxFwHO1x_zCghMYB)

You are more than welcome to try out the code for yourselves: [https://gith
ub.com/fmiguelmmartins/crewaiyoutube](https://github.com/fmiguelmmartins/crewaiyoutube)

And here is an article on Mediu
m with the step-by-step process (don't worry, I have a free account):

[https://medium.com/@fmiguelmmartins/create-an-ai
-team-to-manage-your-youtube-channel-5dc1e6c9b31b](https://medium.com/@fmiguelmmartins/create-an-ai-team-to-manage-your-
youtube-channel-5dc1e6c9b31b)

Hope you guys enjoy it, and if you are kind enough, please leave me some feedback so I ca
n improve over time!

Thank you!

Filipe
```
---

     
 
all -  [ Can one safely use pydantic v2 in Langchain now? ](https://www.reddit.com/r/LangChain/comments/1cagjg0/can_one_safely_use_pydantic_v2_in_langchain_now/) , 2024-04-24-0910
```
I had read earlier that it was safer to use \`pydantic\_v1\` with langchain. But now that I'm trying to actually do some
thing more with what comes out of langchain, it's a big pain to use v1. Can I switch to using current pydantic instead?
```
---

     
 
all -  [ Building tools that utilize async ](https://www.reddit.com/r/LangChain/comments/1cae5ta/building_tools_that_utilize_async/) , 2024-04-24-0910
```
I am currently trying to build a few tools and have run into not being able to use async functions. Does Langchain have 
an answer for this?

I get this error 'NotImplementedError: Tool does not support sync' when calling the tool with the a
gent. I have tried a few different ways classifying the tool to no avail.

&#x200B;
```
---

     
 
all -  [ AI, Multiagent, Agentic, Python, Vision, Web scraping help needed. ](https://www.reddit.com/r/LangChain/comments/1caamav/ai_multiagent_agentic_python_vision_web_scraping/) , 2024-04-24-0910
```
I want to identify the exact property address for online properties eg on Rightmove. 

Currently online UK property URL 
listings provide the Road Name and some further info but NOT the house number or the full postcode.

As a human you can 
find the house number by using Google Streetview and searching for a property match by using the front image of the hous
e.

I suspect automating this process will require a research team of AI Agents using visual AI but open to other soluti
ons.

Please note, there are some other ways to identify the property number (they are not always possible). This projec
t is specifically about automating the process of finding a specific property on Google Streetview.

See this property a
s an example: https://www.rightmove.co.uk/properties/144815291 
Using Streetview, its number 46. I can share the manual 
process I use.

Any help or advice would be greatly appreciated. If you know someone who could do this work, please let 
me know.

Thank you.

```
---

     
 
all -  [ Feedback wanted on my project (Salary Negotiation Coach) ](https://www.reddit.com/r/LangChain/comments/1ca7tof/feedback_wanted_on_my_project_salary_negotiation/) , 2024-04-24-0910
```
So I've built a tool that helps you negotiate a higher salary. The idea is that it helps you prepare for an annual revie
w or handling the offer stage when you get a new job.

I'd love some feedback on it. Getting the combination of text ans
wers (through RAG) plus video content is proving difficult to get right.

You can play with it here:  
[https://ignitus.
app](https://ignitus.app/)
```
---

     
 
all -  [ Multi-Agent Code Reviewer using LangGraph ](https://www.reddit.com/r/LangChain/comments/1ca6jis/multiagent_code_reviewer_using_langgraph/) , 2024-04-24-0910
```
This tutorial explains how can Multi-Agent Orchestration be used to build an automatic code review system where a Coder 
and Reviewer go back & forth improving the code quality until all issues are resolved automatically: 
https://youtu.be/p
dnT3yLk70c?si=TUrV50BlNu7UStoI
```
---

     
 
all -  [ How to avoid increasing the size of my prompt? ](https://www.reddit.com/r/PromptEngineering/comments/1ca674r/how_to_avoid_increasing_the_size_of_my_prompt/) , 2024-04-24-0910
```
Hi, a question for people experienced with prompt engineering:  
  
Let's suppose I am building an API for a user to con
sume and want to specify some examples. Do I have to specify it in each payload?  
  
I am worried that it would just in
crease the input payload size and drive up costs.   
  
What's a good way to get around this? (setup is on python+langch
ain)


```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-24-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-24-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-24-0910
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-24-0910
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-04-24-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-04-24-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
