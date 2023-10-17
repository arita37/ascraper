 
all -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-17-0909
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

     
 
all -  [ Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/GPT3/comments/179j4pw/exploring_methods_to_improve_text_chunking_in_rag/) , 2023-10-17-0909
```

Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunk
ing function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algor
ithms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out 
there, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising a
pproaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large 
Language Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embeddin
g) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've a
lso tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the
 query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a n
ot extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis 
and reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrap
ing to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to 
modify the text used to generate embeddings, while returning the original text after the recall phase. But this is still
 a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd app
reciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel ch
unking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking fo
r RAG here.

Thanks in advance for your time!
```
---

     
 
all -  [ Evaluating RAG on custom Q&As ](https://www.reddit.com/r/LangChain/comments/1798po2/evaluating_rag_on_custom_qas/) , 2023-10-17-0909
```
We are trying to get our feet wet with RAG with a small engineering team. I want to build a RAG system querying an exten
sive internal documents system. With the available choice of LLMs, embedding models, vector databases, hyperparameters i
t's easy to get overwhelmed. So what I want is to create a test dataset manually with like ten-twenty questions and answ
ers we would like to receive (or multiple answer options for each question??) and automate deployment of several combina
tions of different LLMs, hyperparameters, embedding models, etc and compare the actuals against the gold standard answer
s (using ROUGE score maybe??). Does that make sense? Are there any tools/frameworks I need to be aware of to do somethin
g like that for me? Thanks!
```
---

     
 
all -  [ Custom Hybrid Pinecone Retriever in Langchain ](https://www.reddit.com/r/LangChain/comments/17944ji/custom_hybrid_pinecone_retriever_in_langchain/) , 2023-10-17-0909
```
 I am trying to implement a hybrid pinecone retriever in my app. I used the PineconeHybridSearchRetriever from langchain
.retrievers, however it did not work, because it tried to pop 'context' from my vector metadata, so I had to customize i
t like so:

    class CustomPineconeHybridSearchRetriever(PineconeHybridSearchRetriever):
        def _get_relevant_docu
ments(
            self, query: str, *, run_manager: CallbackManagerForRetrieverRun
        ) -> List[Document]:
       
     from pinecone_text.hybrid import hybrid_convex_scale
    
            sparse_vec = self.sparse_encoder.encode_queri
es(query)
            # convert the question into a dense vector
            dense_vec = self.embeddings.embed_query(que
ry)
            # scale alpha with hybrid_scale
            dense_vec, sparse_vec = hybrid_convex_scale(dense_vec, spars
e_vec, self.alpha)
            sparse_vec['values'] = [float(s1) for s1 in sparse_vec['values']]
            # query pin
econe with the query parameters
            result = self.index.query(
                vector=dense_vec,
               
 sparse_vector=sparse_vec,
                top_k=self.top_k,
                include_metadata=True,
                name
space=self.namespace,
            )
            final_result = []
            for res in result['matches']:
            
    context = res['metadata'].pop('text')
                final_result.append(
                    Document(page_content
=context, metadata=res['metadata'])
                )
            # return search results as json
            print(fina
l_result)
            return final_result

The only thing that changed is now it pops 'text' instead of 'context'. This 
works, however when I try to put it in a chain, the chain does not receive the information correctly. I call the chain l
ike this:

    h_retriever = CustomPineconeHybridSearchRetriever(
        embeddings=embed, sparse_encoder=sparse_encode
r, index=index
    )
    
    # retrieval qa chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_
type='stuff',
        # retriever=vectorstore.as_retriever(),
        retriever=hh_retriever,
        
    )

Does anybo
dy know how to fix this? I assume it has to be something with the custom class. Thank you in advance.
```
---

     
 
all -  [ Date initiale in conversatii cu LLMuri ](https://www.reddit.com/r/programare/comments/1793bga/date_initiale_in_conversatii_cu_llmuri/) , 2023-10-17-0909
```
Avand in vedere ca chatgpt nu are acces la documentatii mai noi de 2022, ma intreb cum sa fac conversatii custom prin ap
i-ul openai cu modelul gpt4. Am descarcat si curatat toata documentatia de la libraria langchain si am pus-o intr-un fol
der local. Acum as vrea sa embed (sau ceva) toata documentatia la gpt4 si apoi sa-i pun intrebari despre cum sa folosesc
 uratenia asta de langchain mai bine :D

**Voi cum ati face / ati facut?** 
Ce solutii exista (nu ma intereseaza limbaju
l de programare)? 
Cum o fi pretul la embeddings openai pe langa altele gen pinecone sau supabase local (care de fapt e 
moca)?

Pana acum dadeam copy paste in fereastra chatgpt cu partea din documentatie care ma interesa mai mult, sau si ma
i bine cu vreun tutorial intreg, dar acum mi s-a cam infundat si trebuie sa up my game putin.

Update: Am pornit gresit 
cu langchain, trebuia s-o iau cu LlamaIndex direct - e mai simplu si posibil mai bun pentru taskul meu.
```
---

     
 
all -  [ Streaming with conversational retrieval chain ](https://i.redd.it/20qq9p63siub1.jpg) , 2023-10-17-0909
```
This stream is happening with Chat OpenAI, but when I'm using conversational retrieval chain, it's not streaming. How to
 fix it?
```
---

     
 
all -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/learnmachinelearning/comments/178zuks/free_courses_to_learn_about_large_language_models/) , 2023-10-17-0909
```
[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global community for LLM practitioners.

[**
LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm-ap
plication-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 

[*
*Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buildin
g LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students will l
earn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as gain 
hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai/co
urses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explore D
eep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25/):
 In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're app
lied in different fields. 
```
---

     
 
all -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-17-0909
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

     
 
all -  [ Which model+size for a websearch agent? ](https://www.reddit.com/r/LocalLLaMA/comments/178ztct/which_modelsize_for_a_websearch_agent/) , 2023-10-17-0909
```
I've been playing around with an agent framework ([www.griptape.ai](https://www.griptape.ai)). Like Langchain you can cr
eate an agent with tools and I've been experimenting with its websearch tool. The LLM uses ReAct prompting to decide if 
it should use the websearch tool and then it generates json formatted string with the query action in it. 

Surprisingly
, [https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca) does okay
 but as the conversation progresses it stops reaching out the to websearch tool. gpt-4 nails it ( had to test) but gpt-3
.5-turbo,  not so much. 

I was wondering if anyone else had searched over models to use with tool selection (doesn't ha
ve to be websearch) and found smaller models that that performed consistently? 

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Streaming in Langchain ](https://www.reddit.com/r/LangChain/comments/178zgv0/streaming_in_langchain/) , 2023-10-17-0909
```
I want to know is it possible to stream tokens in conversational retrieval chain ,and rather than printing it to console
 I want to send it via api
```
---

     
 
all -  [ OpenAI Functions vs Langchain ReAct Agents ](https://www.reddit.com/r/LangChain/comments/178lhnc/openai_functions_vs_langchain_react_agents/) , 2023-10-17-0909
```
What is the real difference and tradeoffs when choosing to use ChatGPT Functions instead of the ReAct agents from Langch
ain? What am I missing out on?

My current view is that using functions saves tokens, is faster, and is easier to create
 without the abstraction layer LangChain introduces, and that the tradeoff is not being able to customize how the model 
chooses which tool(function) to use. However, i'm a bit confused about what the best practice for creating Agents that c
an do multiple retrieval things, such as QA with semantic search, search in a SQL database, use the web, and generally r
etrieving new and personal data. I know langchain has its own agent that uses ChatGPT functions, but I found that abstra
ction harder to grasp than just the openai implementation itself.
```
---

     
 
all -  [ Issues with Streaming API Responses to Frontend on AWS using Vercel's AI SDK ](https://www.reddit.com/r/nextjs/comments/178kojc/issues_with_streaming_api_responses_to_frontend/) , 2023-10-17-0909
```
I am currently working on a project where I use Vercel's AI SDK to stream API responses to the frontend of my applicatio
n. Everything works perfectly when I run the application locally, however, **I encounter problems when deploying it on A
WS(Amplify)**. I get the response but it is not streamed.

I am using NextJs + Langchain starter template. 

[https://sd
k.vercel.ai/docs](https://sdk.vercel.ai/docs)

Below is the code I have for my API route and UI:

**API route**

    imp
ort { StreamingTextResponse, LangChainStream, Message } from 'ai';
    import { ChatOpenAI } from 'langchain/chat_models
/openai';
    import { AIMessage, HumanMessage } from 'langchain/schema';
    
    export const runtime = 'edge';
    
 
   export async function POST(req: Request) {
      const { messages } = await req.json();
    
      const { stream, ha
ndlers } = LangChainStream();
    
      const llm = new ChatOpenAI({
        streaming: true,
      });
    
      llm

        .call(
          (messages as Message[]).map(m =>
            m.role == 'user'
              ? new HumanMessage(
m.content)
              : new AIMessage(m.content),
          ),
          {},
          [handlers],
        )
        
.catch(console.error);
    
      return new StreamingTextResponse(stream);
    }

**Frontend**

    'use client';
    

    import { useChat } from 'ai/react';
    
    export default function Chat() {
      const { messages, input, handleI
nputChange, handleSubmit } = useChat();
    
      return (
        <div className='mx-auto w-full max-w-md py-24 flex f
lex-col stretch'>
          {messages.length > 0
            ? messages.map(m => (
                <div key={m.id} class
Name='whitespace-pre-wrap'>
                  {m.role === 'user' ? 'User: ' : 'AI: '}
                  {m.content}
    
            </div>
              ))
            : null}
    
          <form onSubmit={handleSubmit}>
            <input

              className='fixed w-full max-w-md bottom-0 border border-gray-300 rounded mb-8 shadow-xl p-2'
            
  value={input}
              placeholder='Say something...'
              onChange={handleInputChange}
            />
 
         </form>
        </div>
      );
    }

&#x200B;
```
---

     
 
all -  [ How to create a custom agent with structured tools? ](https://www.reddit.com/r/LangChain/comments/178jvg2/how_to_create_a_custom_agent_with_structured_tools/) , 2023-10-17-0909
```
I have seen multiple examples of using Langchain agents Structured tools accepting multiple inputs using **AgentType.STR
UCTURED\_CHAT\_ZERO\_SHOT\_REACT\_DESCRIPTION**. As per [Langchain blog post](https://blog.langchain.dev/structured-tool
s/), this is only agent type that can support Multi-input tools. I have not seen any documentation or example of creatin
g a custom Agent which can use multi-input tools.

My use case may require a different prompt, rules, output parser, and
 that way I want to format scratchpad. Have you developed any similar use case or come across any useful guide?
```
---

     
 
all -  [ Vector Databases... Confusion arises. How do I use them in practice? ](https://www.reddit.com/r/LangChain/comments/178dzf3/vector_databases_confusion_arises_how_do_i_use/) , 2023-10-17-0909
```
I have tried to wrap my head around vector dbs for the past weak, I understand the benefits of them. But I can't seem to
 understand how to use them.

There are sooooooo many vector db services... Some questions about these:
1. Can services 
like Pinecone and Vectara both create and store vector embeddings for you?
2. How do I create embeddings otherwise? Open
Ai has an API for this, do I really need to use their service or can embeddings be created locally?

And there are also 
some locally run vector dbs available, such as weaviate, Milvus and the Jina AI vectordb (https://github.com/jina-ai/vec
tordb?ref=jina-ai-gmbh.ghost.io). Questions about these:
1. Do they require powerful GPUs/CPUs?
2. VectorDB from Jina AI
 seems like a simple and good starting point for me, so that I can get a better understanding of how to work with vectoe
 dbs and embeddings. But their documentation is limited, and I don't really understand if it is capable of creating the 
vector embeddings. Has anyone any experience with this tool?

As is clear, I am somewhat confused about vector dbs. Any 
insights on the questions above are much appreciated.
```
---

     
 
all -  [ Per ogni categoria che vi sovviente, quali sono gli standards industriali nel mondo nello sviluppo w ](https://www.reddit.com/r/ItalyInformatica/comments/178djpy/per_ogni_categoria_che_vi_sovviente_quali_sono/) , 2023-10-17-0909
```
Ritengo che la risposta per antonomasia sia sempre 'dipende', ma che per una ragione o per l'altra (incluso il becero sc
immiottamento delle big) oggi ci si è assestati su diverse tecnologie perché sì, ma mi chiedevo quali potessero essere s
econdo voi le suddette, ad esempio: siamo ancora fissi sulle RESTful o ha vinto GraphQL? C'è posto per i WebSockets?  
C
hi sta vincendo tra il qualsiasi NoSql del populismo ed il popolare Postgresql?  
I linguaggi funzionali stanno davvero 
partendo al contrattacco?  
Che altre opzioni a parte il non-da-produzione Langchain per mettere facilmente in pista app
 basate su LLM?  
Qual è il SO di punta nell'era dei container?  
Quali sono gli strumenti per l'orchestrazione e trasfo
rmazione dei dati? Jenkins campa ancora?   


Ma soprattutto, perché? Non prendiamoci in giro, ognuno ha i suoi bias, ma
 almeno si riesce a dare forma al perché si pensano e dicono determinate cose?

  
Bonus: Ci dobbiamo arrendere al fatto
 che verrà quasi tutto pythonizzato democraticamente perché il settore pullula di minus habens da Udemy e scriptini del 
cazzo, incapaci di vedere oltre il loro naso?  


P.S. ho deviato un po' dal proposito del titolo, ma giusto perché pens
o sarebbe interessante mettere in prospettiva, ex: oggi abbiamo Ruby con il suo OOP ma magari sta davvero tirando le cuo
ia e domani ci potrebbe essere Elixir col suo FP (... Ispirato a Ruby!)
```
---

     
 
all -  [ Is there a project that uses llamaindex or langchain to process whole documents with multi AI workfo ](https://www.reddit.com/r/ChatGPTCoding/comments/178besm/is_there_a_project_that_uses_llamaindex_or/) , 2023-10-17-0909
```
Hello, my first time here! I have a specific workflow that I would like to somehow implement, but I don't know if there 
are any tools that allows such a thing, so I am asking for advice from you guys.

&#x200B;

I am looking for a way to  p
rocess my hundreds of documents and 

create end reports in .txt files, that are written by multiple agents with specifi
c roles.

&#x200B;

The workflow would be like this:

\- get a list of files in folder

\- process first file:

\- open/
read pdf or .doc

\- extract texts and store them in a new .txt file

\- split file into CHUNKS that are more easily wor
kable

\- keep track of all chunks

\- write a one line chunk DESCRIPTION (DESC) and a multi-line ANALYSIS (ANA)

\- the
 description and analysis is created by agents with specific roles

\- DESC and ANA are then passed to other agents for 
feedback forth and back to the creator

\- when until all requirements are met, write them into memory or a temporary fi
le

\- after all chunks are processed, read the all chunk descriptions and remove chunks with duplicate ideas

\- from a
ll remaining chunks create one endreport as txt file by stitching only the ANAs together

\- all preferably with a nice 
gui so that I can see the current progress and where I can easily change the roles of the agents.

Does anyone know a pr
oject that does this all? 

Hopeful with an easy to deploy environment like a docker image that would be preferable. Tha
nk you all!
```
---

     
 
all -  [ Graft - The 12 Best Vector Databases For AI Apps (Comparisons, Reviews, Demos, and Limitations) ](https://www.graft.com/blog/top-vector-databases-for-ai-projects) , 2023-10-17-0909
```

```
---

     
 
all -  [ Is LangChain slow compared to using OpenAI API? ](https://www.reddit.com/r/OpenAI/comments/178a92r/is_langchain_slow_compared_to_using_openai_api/) , 2023-10-17-0909
```
I am looking to build a chatbot using GPT-3.5/4 and was considering using a framework such as LangChain. But I read in o
ne post that it was slow and not cost-effective when it comes to token use.

Am I better off using OpenAI API directly i
f I am looking for speed and cost effectivenes? Is it possible to use the API directly and only use Langchain for certai
n features, such as web search?

Finally, if LangChain is slower and not cost-effective, are there any newer frameworks 
available which are cost effective and as fast as using the API?
```
---

     
 
all -  [ Company building an LLM App. Need some understanding if my opinions are reasonable. ](https://www.reddit.com/r/datascience/comments/1785em4/company_building_an_llm_app_need_some/) , 2023-10-17-0909
```
I'm your generic mid-career data scientist who sometimes functions as an ML engineer. I've been tasked with advising a t
eam building an LLM application to automate 'data analysis' for non-technical customers. My role is to bring some wisdom
 and system design expertise to the team. The team is compromised of two people: a young, eager software engineer who ca
lls themselves a 'Langchain Developer' and a senior technical director who believes in the macro trends around Generativ
e AI and wants to learn more about applying the techonology.

The idea is a customer types a vague question in to a fiel
d  *e.g.* 'Is my business meeting my customer retention goals' and the output would be a visualization of some descripti
ve metrics and an interpretation of the data.

The design presented to me by the Langchain developer sounds overly compl
ex and a bit unhinged to me. I'm looking for an external opinion to make sure my opinions are well grounded or make sens
e.

1. This project is my first time using LangChain. From reading through the LangChain code,  and building some basic 
examples, the library feels over abstracted.  You have to navigate a tangled mess of private variables to even find the 
prompt the tool is using. I am *really* concerned about putting Langchain code in production since it seems difficult to
 debug and modify. Why can't we use a DAG or state machine instead?
2. The langchain developer doesn't present any syste
matic way to deal with hallucination. Generally, the strategy verbalized is too play 'wack a mole' every time they see o
r measure a hallucination. If hallucinations are rare, then sure, and I'd be a bit more comfortable with this approach. 
But I've see no evidence that's the case.
3. The scalable ways to measure hallucination often use an LLM to judge it's o
wn output. Generally, I try to avoid feedback loops between models. Is that too strong of an opinion to have when workin
g with LLMs?

Appreciate the responses!
```
---

     
 
all -  [ Too possible to be enjoyable ](https://www.reddit.com/r/Mission_Impossible/comments/177wrh7/too_possible_to_be_enjoyable/) , 2023-10-17-0909
```
Spoilers!
Tech nerds only

The movie premise is too possible to be fun. 

Today a vast amount of computing power is need
ed to train and run AI models. ChatGPT is currently far smarter than any humans or group of humans.  It will be 10x smar
ter in 3 years..



At the same time viruses have been designed as weapons of nations (including successful US deploymen
ts) talking to computer security experts, he best viruses are impossible to detect and eliminate. 

Development environm
ents like langchain give AI models access and do anything on the internet today. 

Once such a federated entity is relea
sed, invades secure computers ( as they said in the movie humans are the weakest link in security) the entity would abso
rb all the nastiest code and tricks. 

I think it is extremely likely that baby versions of the entity has already been 
released. Perhaps by the us, russia, china, or a 15 year old in their basement. 

The only barrier we have now is slow n
etwork communication for federated entities. But 5g and fiber, and starlink are solving that chokepoint. 

This movie is
 like watching a docudrama  about the last days of hummanity as produced by the entity in 10 years after the entity rele
ases covid3.0 on humanity from some government sponsored lab and wipes us from the face of the earth…
```
---

     
 
all -  [ Need help with an Agent with custom tools ](https://www.reddit.com/r/LangChain/comments/177wn7k/need_help_with_an_agent_with_custom_tools/) , 2023-10-17-0909
```
I need some help in implementing async custom tools in my agent. If you have developed such agent and can help me out, p
lease comment below.  I'll share more details in the DM.

Thanks.
```
---

     
 
all -  [ Including extra column with add_documents ](https://www.reddit.com/r/LangChain/comments/177q13x/including_extra_column_with_add_documents/) , 2023-10-17-0909
```
Hi all. I have a vectors table in Supabase to which documents are being added via the add_documents method. But there's 
an extra column that I have in the table that I'd like to add data to when I'm inserting vectors. How can I do this if u
sing add_doccuments?
```
---

     
 
all -  [ [Absolute newb] Help understanding where to focus with tuning and improving response quality ](https://www.reddit.com/r/LangChain/comments/177pmo0/absolute_newb_help_understanding_where_to_focus/) , 2023-10-17-0909
```
Hello! As someone completely new to LLMs and AI (but not new to programming/IT), can I get some advice on where I can fo
cus to improve the results I'm getting? I'm looking to understand the underlying concepts of where my problems might be;
 the problem I have right now is that I've got things 'working,' but the results are really poor in quality, and the lan
dscape is so vast I don't even know what to focus on.

As a first project, I decided to take the Plot Synopsis of variou
s films on IMDb. Each of these is around 10,000 characters in length, so I dumped each in a .txt file, and set up a pg\_
vector vectorstore, and added them all to the same collection.

All queries are with OpenAI, a temperature of 0, and usi
ng gpt-4.

\----------------------------------------------------

I started with The Matrix. I loaded one file, and thro
ugh RetrievalQA was able to query about the contents of the story.

* 'Who is the main character of The Matrix?' --> Neo
. Check.
* 'Summarize the plot of The Matrix in 5 sentences.' --> 'The Matrix is about humans trapped in a simulation...
.......' Check.
* 'What is Neo's day-job?' --> A programmer at a software company. Check.

But then:

* 'Please describe
 Neo's appearance.' --> 'Thick black hair, a sallow appearance, and with a tattoo of a white rabbit on his shoulder.' --
> Huh???

The description of his appearance in the source comes from the same paragraph:

>Thomas Anderson, aka 'Neo' (K
eanu Reeves), a hacker with thick `black hair and a sallow appearance`, is asleep at his monitor. Notices about a manhun
t for a man named Morpheus scroll across his screen as he sleeps. Suddenly Neo's screen goes blank and a series of text 
messages appear: 'Wake up, Neo.' 'The Matrix has you.' 'Follow the White Rabbit.' Then, the text says 'Knock, knock, Neo
...' just as he reads it, a knock comes at the door of his apartment, 101. It's a group of ravers and Neo gives them a c
ontraband disc he has secreted in a copy of 'Simulacra and Simulation.' The lead raver asks him to join them and Neo dem
urs until he sees `the tattoo of a small white rabbit on the shoulder of a seductive girl`  in the group.

The source te
xt is quite clear that the tattoo belongs to someone else, so I can't figure out why the AI is telling me that the tatto
o belongs to Neo. What concepts or areas would I focus on in order to improve this?

\----------------------------------
------------------

Then, I added multiple additional films, like Spider-Man, Indiana Jones, etc. all into the same coll
ection of the pg\_vector vectorstore.

When questioned about a specific film, it does a good job of narrowing in on just
 that part of the collection. 'How does Indiana Jones and the Last Crusade end?' --> great summary about riding off into
 the sunset of finding and losing the grail.

But then any queries that \*cross\* multiple films, it's totally unable to
 handle. Examples:

* The data collection has 5 films in it, but when asked, 'How many films are you aware of?', the mos
t it's ever aware of is 2.
* When asked to make comparisons between films, it will always say it's missing the synopsis 
for one of the two films. i.e. 'Are there any thematic similarities between Spider-Man and Indiana Jones?' --> 'I'm sorr
y, but I'm not aware of any films called Indiana Jones.'

I have some novice suspicions (I've only been working with thi
s for three days...), the major of which is that in order to do a full comparison of two films involves sending all chun
ks of both films, which is too much for a single request, or something along those lines, it's not able to properly narr
ow down the chunks before sending, or something.

Obviously this *can* be done, because those same questions work just f
ine in 'real' ChatGPT. I think this boils down to (probably), 'uh, you've uploaded 10,000 characters about The Matrix, w
hereas the ChatGPT foundational model has probably 100x that amount of information assimilated on The Matrix across 100x
 other sources.' And as a novice, at first glance, I think, 'yeah that makes sense...' But then I think about it more, a
nd actually since that's most likely the case, wouldn't that be even \*more\* chunks/collections for ChatGPT to go throu
gh? Is this where like 'training' comes in? Like if I want a true 'bot' to be able to speak to the details I want, do I 
have to like, give it more data and 'train' it somewhere (somehow)? Right now I've just pointed it at some chunked up ra
w text.

Ahhhh, my brain is tired :) Thanks in advance for the help.
```
---

     
 
all -  [ Methodology for Tracking Client Details in a Natural Language Bot using Langchain and RAG ](https://www.reddit.com/r/LangChain/comments/177oi3y/methodology_for_tracking_client_details_in_a/) , 2023-10-17-0909
```

Hello,

We are building a chatbot using Langchain that aims to gather multiple pieces of information (e.g., name, addre
ss, TV type, malfunction description, etc.) from the client. The bot also needs to respond to any queries the client mig
ht have, using a Retriever-Augmented Generation (RAG) model.

We've considered simply using a system template to keep tr
ack of which details the client has already provided, but this seems inadequate for a fluid and natural conversation.

W
hat methodology would be best for tracking which details the client has already filled in and what questions we need to 
ask next, while still allowing for a natural language conversation?

Any advice or pointers would be highly appreciated.


Thank you!
```
---

     
 
all -  [ AI conference happening in San Francisco: 100% off on the ticket price! ](https://www.reddit.com/r/ArtificialInteligence/comments/177ngy6/ai_conference_happening_in_san_francisco_100_off/) , 2023-10-17-0909
```
I work for this database company SingleStore and we are hosting a Data and AI conference in San Francisco on 17th of Oct
ober, 2023.  
It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of Lan
gChain and many more. We will have hands-on workshops, swags giveaway and much more.  
I don't know if it makes sense to
 share this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network w
ith other data engineering folks.  
Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (th
e original ticket price is $199)

  
[Get your tickets now!](https://singlestore.com/now) using 'PAVAN100OFF' discount c
ode. 
```
---

     
 
all -  [ Data & Analytics conference happening in San Francisco: 100% off on the ticket price! ](https://www.reddit.com/r/dataanalysis/comments/177n2kh/data_analytics_conference_happening_in_san/) , 2023-10-17-0909
```
I work for this database company SingleStore and we are hosting a Data and AI conference in San Francisco on 17th of Oct
ober, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of Lang
Chain and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to s
hare this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network wit
h other data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the o
riginal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
all -  [ How can i use extracted keyword before ElasticSearch Querying? ](https://www.reddit.com/r/LangChain/comments/177mcmc/how_can_i_use_extracted_keyword_before/) , 2023-10-17-0909
```
hello.

I am creating a vector search-based chatbot using langchain, openai, and elasticsearch.

&#x200B;

We have imple
mented retrieving the most relevant documents in elasticsearch based on the current user's search.

&#x200B;

Going furt
her, we want to add various conditions to the elasticsearch search query by extracting structured data from the user's q
uery before searching in elasticsearch for higher accuracy.

&#x200B;

For example, the user's search query is 'Which Fo
rd pickup trucks are under $35,000?' In this case, the keywords below should be extracted.

&#x200B;

company: Ford

typ
e: pickup trucks

maximum price: 35000

&#x200B;

After going through the logic of converting this keyword into an Elast
icsearch query (this part will need to be implemented separately), the content below is added to the Elasticsearch searc
h query.

`{ 'term': { 'brand': 'Ford' } },` 

`{ 'term': { 'type': 'pickup' } },` 

`{ 'range': { 'price': { 'lt': 3500
0 } } }`

&#x200B;

I found a library called Kor in LangChain's extract document, and after testing it, I got satisfacto
ry results. However, if you use this library, openAi API will be called twice per user search. (extract 1 time, result g
eneration 1 time)

&#x200B;

Is it best to call openAi api twice using Kor?

&#x200B;

Also, there seems to be a way to 
use SelfQueryRetriever among retrievers.

However, I am currently using CustomRetriever, which inherits BaseRetriever, t
o use ElasticSearch custom queries.

&#x200B;

Can I use SelfQueryRetriever in CustomRetriever?
```
---

     
 
all -  [ Need help with retrieving comprehensive results from multiple documents using GPTVectorStoreIndex ](https://www.reddit.com/r/LangChain/comments/177k795/need_help_with_retrieving_comprehensive_results/) , 2023-10-17-0909
```
I have a collection of scientific documents related to a specific plant, extracted from PDFs and stored in JSON and CSV 
formats. I'm using the following code to load all these documents: 
```
for dir_path in all_dirs:
    dir_reader = Simpl
eDirectoryReader(dir_path, file_extractor={
        '.csv': PandasCSVReader(),
        '.json': JSONReader()
    })
    
docs.extend(dir_reader.load_data())

```

After loading, I create an index and query it:


```
index = GPTVectorStoreInd
ex.from_documents(docs, service_context=service_context)
query_engine = load_index_from_storage(storage_context).as_quer
y_engine(similarity_top_k=4)
response = query_engine.query(input_text)

```
The issue is that the query always returns a
 single response from just one document that best matches my query. However, I know that other documents contain more re
levant information about the plant. How can I modify my approach to retrieve comprehensive results from all relevant doc
uments in my index?
```
---

     
 
all -  [ AI powered by Streamlit ](https://www.reddit.com/r/Streamlit/comments/177jxq2/ai_powered_by_streamlit/) , 2023-10-17-0909
```
I love streamlit + langchain

This experiment will verify different use cases of LLM using LangChain, which include chat
, role-playing, and document-based QA.

https://github.com/coolbeevip/langchain-lab
```
---

     
 
all -  [ OpsTower.ai - AWS CLI AI Assistant ... AMA ](https://www.reddit.com/r/OpenAIDev/comments/177d527/opstowerai_aws_cli_ai_assistant_ama/) , 2023-10-17-0909
```
I've always struggled to remember the AWS CLI syntax and hate using the AWS console. After months of toil on my first AI
 project, I've released [OpsTower.ai, a free DevOps AI Assistant](https://github.com/opstower-ai/llm-opstower). OpsTower
.ai can answer questions about your AWS resources and perform calculations on cloudwatch metrics from the command line.


You can try it in demo mode too (don't need to trust me with your AWS creds 😉). See [https://github.com/opstower-ai/llm
-opstower](https://github.com/opstower-ai/llm-opstower) for full details.

I've also blogged a bit about my experiencing
 building the agent:

1. [Streamlining RAG evaluation](https://dlite.cc/2023/10/04/2023-eval-rag-apps.html)
2. [Beyond d
emoware: how do you evaluate an AI agent?](https://www.opstower.ai/2023-evaluating-ai-agents/) (also covers the agent ar
chitecture using openai function calls)

Learning how to interact w/AWS has been a great starter project to see what's p
ossible. I'd like to teach it to perform tedious DevOps tasks for me.

Also, here are some example questions you try:

 
   llm 'list each ec2 instance id, name, state, last restart, image, and size'
    llm 'What is the average CPU utilizat
ion of my EC2 instances?'
    llm 'breakdown bill by aws service over the past 30 days'

I wrote the agent in Ruby using
 the openai-ruby gem. I originally started with Python and Langchain, but found the abstractions really difficult. I was
 happy with the direction of rolling my own code.

Happy to answer any questions about the sometimes maddening experienc
e of trying to make an agent robust enough to share.
```
---

     
 
all -  [ Routing traffic through Custom Chains. Possible Bug. ](https://www.reddit.com/r/LangChain/comments/177c1ds/routing_traffic_through_custom_chains_possible_bug/) , 2023-10-17-0909
```
I am trying to use a MultiPromptChain to redirect traffic through some custom chains. 

However, it appears that there i
s a bug in the MultiPromptChain class. Instead of using the custom chains I have supplied it with in destination\_chains
, the class re-writes the chain objects.  

You can see in the screenshot that the objects are different - they are even
 instances of different classes. How am I supposed to route traffic through custom chains? Crazy frustrating that this i
sn't made more clear. 

[Why is blast\_api\_chain redefined as an LLMChain object?](https://preview.redd.it/gboaxd9d22ub
1.png?width=594&format=png&auto=webp&s=1f2ce20fc6916ea0e2b96b47210527a3e6f56e82)

&#x200B;
```
---

     
 
all -  [ Not acknowledging custom function ](https://www.reddit.com/r/LangChain/comments/177bc6j/not_acknowledging_custom_function/) , 2023-10-17-0909
```
Hey everyone!

I created a custom function, which im using as tool in create_pandas_dataframe_agent. The purpose of the 
tool is to upload the returned dataframe to s3 and return the S3 URL. Even with specific prompting to acknowledge the to
ol, it tells me that it’s not a “valid tool”.

Snippet of code below. Looking for an guidance. Additionally, looking for
 freelance work to help me with the development. If interested, feel free to DM me. Thank I’m advance!

tools = [
    To
ol(
        name = 'dataframe uploader to aws s3',
        func = dataframeUpload,
        description = 'Uploads pandas
 dataframes to AWS S3. Accepts a valid pandas dataframe'
    )
]


df = pd.read_csv(url)

llm = ChatOpenAI(model=model)

agent = create_pandas_dataframe_agent(llm, df, verbose=True, return_intermediate_steps=True, extra_tools=tools)
agent.ag
ent.llm_chain.prompt.template = '<add custom prompt here>'

response = agent(query)
```
---

     
 
all -  [ How businesses can use GPT with their own data ](https://www.reddit.com/r/Entrepreneur/comments/1777x94/how_businesses_can_use_gpt_with_their_own_data/) , 2023-10-17-0909
```
There’s many business use cases for a custom chat interface like ChatGPT, but using the company’s own internal content a
s the source. Think company policies, documents, project resources, etc.

I’ve been wrapping my head around, and buildin
g, GPT projects for the past 2 years (software dev of 7 years). Always learning, but what I’m sharing is basically the s
tandard approach to create a custom ChatGPT-like application that you can add your own data to.

If you know how to prog
ram, you could explore Open Source libraries like LangChain to handle processing of custom data. It’s a free program tha
t makes the process of interacting with different LLMs easier. Next you’ll want to connect it to a vector database to ma
ke the processed data available for referencing, and finally OpenAI’s API for the LLM generations (or your LLM of choice
).

Regardless of the solution you choose, how all this works from a technical perspective is:

1. You need to break up 
any large text content into smaller pieces. This process is called chunking. You do this to later make each chunk search
able in the vector database.
2. ⁠You’ll want to vectorize each chunk and add this vector into a database. By doing this,
 you can embed (vectorize) natural language to search the vector database for relevant chunks.
3. With the returned chun
ks, you can combine them all (within respects to the context window limit of the LLM of choice), and now your generated 
response will contain the information it needs to give you an accurate output.

Making a secure and privacy-focused solu
tion for businesses is also important. If you use the OpenAI API, data is not used to train their models (source [OpenAI
 Enterprise Privacy](https://openai.com/enterprise-privacy)).

I hope this makes sense. Let me know if there’s any quest
ions on the topic.
```
---

     
 
all -  [ AI SDK with Langchain ](https://www.reddit.com/r/LangChain/comments/1774dek/ai_sdk_with_langchain/) , 2023-10-17-0909
```
Can anybody help me with this ... the streaming cuts off

i am using the vercel SDK

https://preview.redd.it/c39406lwb0u
b1.jpg?width=1130&format=pjpg&auto=webp&s=5d53469e35abab36e72e3c588f35fad83bd5812f

https://preview.redd.it/8tjkgjlwb0ub
1.jpg?width=1210&format=pjpg&auto=webp&s=5ffeabc6ee2a2932dbc1b0f174e32ace2e74b720
```
---

     
 
all -  [ Need advice from experienced CS people regarding what should I do? ](https://www.reddit.com/r/careerguidance/comments/177497v/need_advice_from_experienced_cs_people_regarding/) , 2023-10-17-0909
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects for my current company. some of them on a proprietary outdated IoT platform (DGLux)
. But I have also worked on Building in-house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS, C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When 
it comes to academics I do have some experience in ML model development as well. Expecting ideas to level up as an engin
eer.
```
---

     
 
all -  [ Need to advice from experienced CS people ](https://www.reddit.com/r/careeradvice/comments/17746bd/need_to_advice_from_experienced_cs_people/) , 2023-10-17-0909
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects of my current company. some of them on a proprietary outdated IoT platform (DGLux) 
. But I have also worked on Building in house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS,C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When i
t comes to academics I do have some experience in ML model development as well. Expecting a ideas to level up as an engi
neer.
```
---

     
 
all -  [ Chatbot with Langchain Javascript ](https://www.reddit.com/r/LangChain/comments/1772g4u/chatbot_with_langchain_javascript/) , 2023-10-17-0909
```
Chatbot using Langchain with JavaScript and Openai

Frontend: Next.js

What do you think of JavaScript in AI projects?


Repo: [Chatbot](https://github.com/Deluxer/gpt-chatbot-langchain-js)

https://i.redd.it/r8oy6a96vztb1.gif
```
---

     
 
all -  [ Train AI on data and emails? ](https://www.reddit.com/r/ChatGPTPro/comments/1771us3/train_ai_on_data_and_emails/) , 2023-10-17-0909
```
Hi all, I’m wondering if anyone has any thoughts about how to do this: I want to train ChatGPT on a large amount of info
rmation, including websites, pdfs, and outlook emails. I’m trying to start off with something easy that can help me with
 some of my work report writing, but ultimately this is what I really want: read all of my emails (outlook), provide me 
with a summary of them, allow me to have the ai draft replies, have the ai draft options for follow ups (I.e. meetings e
tc.). I know that training an AI model on documents for the first thing is possible, thought tools like Langchain, but i
s the email part of what I am looking for possible? TIA for your thoughts/help
```
---

     
 
all -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-17-0909
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

     
 
all -  [ Need Some Directions ](https://www.reddit.com/r/LangChain/comments/1770oj4/need_some_directions/) , 2023-10-17-0909
```
I'm trying to build a recommendation system for real estate property listings as per user preferences. 

Let's say I hav
e a dataframe with over 50k listings. Columns are property address, Size, nBHK, Area, City, price range, other informati
on like swimming pool, park, etc. 

What would be the most efficient way to provide this data to a LLM? Will a simple da
taframe loader work? 

I don't have access to the df right now.
```
---

     
 
all -  [ Privacy Compliance and Records Retention for LangChain Apps ](https://www.reddit.com/r/LangChain/comments/1770978/privacy_compliance_and_records_retention_for/) , 2023-10-17-0909
```
Hey all, we've just launched **Zep Archive**, offering easy-to-implement tools for LangChain chat apps to comply with **
records retention and privacy compliance regulations**. If you're using Zep's `ZepMemory` class in your app, you get the
se features with no additional effort.

&#x200B;

>Building a production-ready user-facing app requires complying with d
ata privacy regulations such as California's CCPA and the EU's GDPR. For many applications, retention of records for a p
eriod of time is also required. Apps with conversational interfaces powered by LLMs are no different.  
>  
>Zep Archive
 is a collection of features available in Zep that support meeting these data governance challenges, including archiving
 all message histories and executing Right To Be Forgotten requests.

Get **Zep Open Source**: [https://docs.getzep.com/
deployment/quickstart/](https://docs.getzep.com/deployment/quickstart/)

More info on **Zep Archive**: [https://blog.get
zep.com/announcing-zep-archive-regulatory-compliance-and/](https://blog.getzep.com/announcing-zep-archive-regulatory-com
pliance-and/)

&#x200B;

https://preview.redd.it/5syy6bpeeztb1.png?width=1792&format=png&auto=webp&s=5d60a533eedb56ce6f3
a79d791ce83b163e7d487
```
---

     
 
all -  [ Vectorizing notes & chat history ](https://www.reddit.com/r/LangChain/comments/17708ki/vectorizing_notes_chat_history/) , 2023-10-17-0909
```
I have a question for my general understanding:

I'm building a chatbot for a note-taking app that uses vector embedding
s to **find relevant user notes for an AI chat**.

Right now, I **vectorize the whole note** (no matter how big) and sto
re that result in Pinecone.

For my search input, I then vectorize the **last 8 messages** and use this to query my DB.


This approach is simple and seems to work. Do I need to be more granular (e.g. index chunks of text rather than whole n
otes, or single messages from the chat)?

Some code examples:

Embedding user notes when they are created:

    const ne
wNote = await prisma.note.create({
      data: {
        title,
        content,
      },
    });
    
    const embeddi
ng = await getEmbeddingsForNote(newNote);
    
    await notesIndex.upsert([
      {
        id: newNote.id,
        val
ues: embedding,
      },
    ]);

Embedding the chat history:

        const chatMessages: Message[] = json.messages;
  
  
        const messagesTruncated = chatMessages.slice(-8);
    
        const queryEmbedding = await getEmbedding(
   
       messagesTruncated.map((message) => message.content).join('\n'),
        );
    
        const vectorQueryResponse
 = await notesIndex.query({
          vector: queryEmbedding,
          topK: 5,
        });
    
        const relevant
Notes = await prisma.note.findMany({
          where: {
            id: {
              in: vectorQueryResponse.matches.
map((result) => result.id),
            },
          },
        });
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-17-0909
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-17-0909
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-17-0909
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-17-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-17-0909
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

     
