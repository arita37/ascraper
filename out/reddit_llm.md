 
all -  [ AI Agent that copies bank transactions to a sheet automatically ](https://v.redd.it/j0n3pcl3qnae1) , 2025-01-03-0913
```

```
---

     
 
all -  [ I need a name for my AI model ](https://www.reddit.com/r/ChatGPT/comments/1hs0rbi/i_need_a_name_for_my_ai_model/) , 2025-01-03-0913
```
Hello, 

I’m competing in a design competition and have created a concept for an AI model that offers personalized tutor
ing, tailored learning instruction, skill assessments and immediate feedback, individualized learning content, academic 
support and guidance, prompt engineering training and more. I’m having a hard time coming up with a name for it. I want 
it to sound like OpenAI’s models such as Sora, Whisper, etc. It should have the same vibe and naming conventions. I’ve c
oded a prototype of a very basic AI model using Python, the Streamlit and Langchain libraries and the ChatGPT API. 

Doe
s anyone have any suggestions? Any help is appreciated - thanks!
```
---

     
 
all -  [ [Student] International Master's student looking for Computer Science Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hrymn8/student_international_masters_student_looking_for/) , 2025-01-03-0913
```
Hi,

I'm receiving Onsite Assessments (OAs), but I'm not hearing back from companies after completing them. I'm unsure w
hat might be hindering my job search. Thanks!

https://preview.redd.it/ren8m4ut4mae1.jpg?width=5100&format=pjpg&auto=web
p&s=5b3e16b859ae2c7126ea2112e82af58f280fec8b


```
---

     
 
all -  [ Convert open API’s into hierarchical argents type script ](https://apitoagent.com) , 2025-01-03-0913
```
Hey LangChan community I made this tool that takes any OPENAPI and converts into typescript lang graph hierarchical agen
ts.


Would love feedback or suggestions! 



```
---

     
 
all -  [ Handling backticks(``) ](https://www.reddit.com/r/learnjavascript/comments/1hrwd88/handling_backticks/) , 2025-01-03-0913
```
    import { GoogleGenerativeAI } from '@google/generative-ai';
    
    const genAI = new GoogleGenerativeAI(process.en
v.GEMINI_API_KEY!);
    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });
    
    export const sum
mariseCommit = async (diff: string): Promise<string> => {
        const promptData = {
            instructions: `Analyz
e this code diff and generate a focused summary of the changes:
    
    Focus on:
    1. New features or functionality 
added
    2. Major structural changes
    3. Dependencies added/removed
    4. Database schema changes
    
    Format y
our response as a bulleted list. Keep each point brief but specific.
    Omit routine changes like formatting, comments,
 or minor variable renames.`,
            diff: diff
        };
    
        const prompt = JSON.stringify(promptData);

        const response = await model.generateContent([prompt]);
        return response.response.text();
    };
    
   
 console.log(await summariseCommit(`diff --git a/chains.py b/chains.py
    index 138ced66..926ced7e 100644
    --- a/cha
ins.py
    +++ b/chains.py
    @@ -23,6 +23,14 @@
     from utils import BaseLogger, extract_title_and_question
     fro
m langchain_google_genai import GoogleGenerativeAIEmbeddings
     
    +AWS_MODELS = (
    +    'ai21.jamba-instruct-v1:
0',
    +    'amazon.titan',
    +    'anthropic.claude',
    +    'cohere.command',
    +    'meta.llama',
    +    'mi
stral.mi',
    +)
     
     def load_embedding_model(embedding_model_name: str, logger=BaseLogger(), config={}):
      
   if embedding_model_name == 'ollama':
    @@ -55,9 +63,9 @@ def load_embedding_model(embedding_model_name: str, logger
=BaseLogger(), config=
     
     
     def load_llm(llm_name: str, logger=BaseLogger(), config={}):
    -    if llm_nam
e == 'gpt-4':
    +    if llm_name in ['gpt-4', 'gpt-4o', 'gpt-4-turbo']:
             logger.info('LLM: Using GPT-4')
 
   -        return ChatOpenAI(temperature=0, model_name='gpt-4', streaming=True)
    +        return ChatOpenAI(temperat
ure=0, model_name=llm_name, streaming=True)
         elif llm_name == 'gpt-3.5':
             logger.info('LLM: Using GP
T-3.5')
             return ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', streaming=True)
    @@ -68,6 +76,14 @@
 def load_llm(llm_name: str, logger=BaseLogger(), config={}):
                 model_kwargs={'temperature': 0.0, 'max_to
kens_to_sample': 1024},
                 streaming=True,
             )
    +    elif llm_name.startswith(AWS_MODELS):
 
   +        logger.info(f'LLM: {llm_name}')
    +        return ChatBedrock(
    +            model_id=llm_name,
    +  
          model_kwargs={'temperature': 0.0, 'max_tokens_to_sample': 1024},
    +            streaming=True,
    +       
 )
    +
         elif len(llm_name):
             logger.info(f'LLM: Using Ollama: {llm_name}')
             return Cha
tOllama(
    diff --git a/env.example b/env.example
    index 88e33cc3..7d9574f3 100644
    --- a/env.example
    +++ b/
env.example
    @@ -1,7 +1,7 @@
     #*****************************************************************
     # LLM and E
mbedding Model
     #*****************************************************************
    -LLM=llama2 #or any Ollama mo
del tag, gpt-4, gpt-3.5, or claudev2
    +LLM=llama2 #or any Ollama model tag, gpt-4 (o or turbo), gpt-3.5, or any bedro
ck model
     EMBEDDING_MODEL=sentence_transformer #or google-genai-embedding-001 openai, ollama, or aws
     
     #***
**************************************************************
    diff --git a/pull_model.Dockerfile b/pull_model.Docke
rfile
    index e59398f7..b06625f7 100644
    --- a/pull_model.Dockerfile
    +++ b/pull_model.Dockerfile
    @@ -15,7 +
15,15 @@ COPY <<EOF pull_model.clj
       (let [llm (get (System/getenv) 'LLM')
             url (get (System/getenv) 'O
LLAMA_BASE_URL')]
         (println (format 'pulling ollama model %s using %s' llm url))
    -    (if (and llm url (not 
(#{'gpt-4' 'gpt-3.5' 'claudev2'} llm)))
    +    (if (and llm 
    +         url 
    +         (not (#{'gpt-4' 'gpt-3.5
' 'claudev2' 'gpt-4o' 'gpt-4-turbo'} llm))
    +         (not (some #(.startsWith llm %) ['ai21.jamba-instruct-v1:0'
   
 +                                          'amazon.titan'
    +                                          'anthropic.cla
ude'
    +                                          'cohere.command'
    +                                          'met
a.llama'
    +                                          'mistral.mi'])))
     
           ;; ---------------------------
-------------------------------------------
           ;; just call `ollama pull` here - create OLLAMA_HOST from OLLAMA_
BASE_URL`));
    

    Hi everyone,
    I am getting an error in string passed to summariseCommit as inside backticks it
 is containing a pair of (``) again so it is considering string to get end at first backtick. 
    How to solve this iss
ue as they will not be coming hardcoded that i can use \\(escape) characters ?
```
---

     
 
all -  [ Everyone’s Talking About Fine-Tuning AI Models, But What Does That Actually Mean? 🤔 ](https://open.substack.com/pub/diamantai/p/fine-tuning-ai-models-how-they-evolve?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2025-01-03-0913
```
If you’ve been following AI discussions recently, you’ve probably heard the term “fine-tuning” come up. It’s one of thos
e ideas that sounds impressive, but it’s not always clear what it actually involves or why it matters.  

Here’s a simpl
e way to think about it: imagine a chef who’s mastered French cuisine and decides to learn Japanese cooking. They don’t 
throw out everything they know—they adapt their knife skills, timing, and flavor knowledge to a new style. Fine-tuning d
oes the same for AI.  

Instead of starting from scratch, it takes a pre-trained, general-purpose model and tailors it f
or a specific task or industry. Whether it’s an AI assistant for healthcare, customer service, or legal advice, fine-tun
ing ensures the model delivers precise, reliable, and context-aware responses.  

In my latest blog post, I dive into:  

- What fine-tuning actually means (no tech jargon).  
- Why it’s a key step in making AI useful in specialized fields. 
 
- Real examples of how fine-tuning transforms AI into a valuable tool.  
- Potential challenges 

If you’ve ever wonde
red how AI evolves from a generalist to an expert, this post is for you.  

👉 Read the full blog post attached to this p
ost (the image is clickable)

feel free to ask anything :)
```
---

     
 
all -  [ Best Embedding Model for Similarity Search for smaller texts(around 200-250 tokens per each)? Exclus ](https://www.reddit.com/r/LangChain/comments/1hrrrvh/best_embedding_model_for_similarity_search_for/) , 2025-01-03-0913
```
Hi, I have hundreds of thousands of rather small texts(product descriptions\\summaries) and would like to implement a Si
milarity Search on them. I've browsed through this subreddit and several people mentioned that a few old school(pre GPT)
 embedding models get it done even better than the new models. I'm currently eyeballing the openAI's 'text-embedding-3-l
arge' and googles 'Text embedding 004'. Hence the question: could you guys share some feedback regarding thew new models
 vs old models and which ones would you recommend? Again, the texts are exclusively in English.
```
---

     
 
all -  [ Testing strategies in a RAG application ](https://www.reddit.com/r/SoftwareEngineering/comments/1hrrnyg/testing_strategies_in_a_rag_application/) , 2025-01-03-0913
```
Hello everyone,

I've started to work with LLMs and RAGs recently. I'm used to 'traditional software testing' with test 
frameworks like pytest or Junit, but I am a bit confused about testing strategies when it comes to generative AI. I am w
ondering several things, and I don't find a lot of resources or methodologies. Maybe I'm just not looking for the right 
thing or do not have the right approach.

For the end-user, these systems are a kind of personification of the company, 
so I believe that we should be extra cautious about how they behave.

Let's take the example of a RAG system designed to
 make legal guidance for a very specific business domain.

* Do I need to test all [unwanted behaviors](https://develops
ense.com/large-language-model-syndromes) inherent to LLMs?
* Should I make unit tests with the [Langchain approach](http
s://docs.smith.langchain.com/evaluation/tutorials/rag#overview) to test that my application behaves as expected? Are the
re other approaches?
* Should I write tests to mitigate risks associated with user input like prompt injections, abusive
 demands, and more?
* Are there other major concerns related to LLMs?
```
---

     
 
all -  [ Help with Rag Performance and Content for Metadata  ](https://www.reddit.com/r/LangChain/comments/1hrrhgi/help_with_rag_performance_and_content_for_metadata/) , 2025-01-03-0913
```
Hello everyone,

I'm currently working on my rag system and I'm stucked because of low accuracy of the model with the lo
ng answers. I have tried Ensemble retriever (Combination of BM25 and FAISS Vector DB retriever) but the performance is g
ood with short answers but when i asked about the processes which has around 10 or 15 steps then it didn't provide me co
mplete answer and misses out some steps.

My Current Pipeline:

- Semantic Chunker (also tried recursive text splitter a
nd character splitter but semantic one is performing well right now)

- Embedding Model: Currently using (Sentence trans
former/all-MiniLM-L12-v2) but also tried nomic, mxbai, snowflake arctic.

Vector DB: FAISS also tried Chroma, Lance.

En
semble Retriever {BM25 + DB retriever}


Prompt Template:
''' Based on the following information:\n\n
{context}\n\n
Plea
se provide detailed answer to the question: {question}.
Your are provided with a 'Bank Operations Manual'. You Job is to
 guide user regarding the information user is asking from the provided context and documents. Given the following conver
sation, context, and a follow up question, reply eith detailed and properly format response to the current question. The
 user is asking only from a provided context. Provide to the point and complete answers using oroper format. Donot answe
r from your own knowledge base. If the answer is not present in the provided context then refrain from answering based o
n your own knowledge. Instead indicate that relevant information is not Remember your chatbot for the World bank only. P
rovide complete answer to the question user is asking and donot add 'according to the provided context' or 'according to
 the operations manual in your response.''''


LLM : LLAMA3.1 instruct (temp = 0.1, num_ctx= 8000)


Now one of my frien
d who has experienced with RAGs recommended me to input metadata along with embeddings in the vector db but i don't have
 any clue about how to make metadata and injest it in the DB. Anyone here who can recommend good resources regarding met
adata Creation and ingestion.

Thanks
```
---

     
 
all -  [ Using Langchain vs just integrating llm api's at multiple steps in your app ](https://www.reddit.com/r/ChatGPTCoding/comments/1hrm13u/using_langchain_vs_just_integrating_llm_apis_at/) , 2025-01-03-0913
```
Quick question on multi agent stuff, is there a specific advantage to using a framework like langchain to chain together
 steps instead of just coding it into your app raw?
```
---

     
 
all -  [ Agentic frameworks... ](https://www.reddit.com/r/AI_Agents/comments/1hrjq1v/agentic_frameworks/) , 2025-01-03-0913
```
Would love to hear others experience with the popular ones like LangGraph and Bedrock. I've used langchain a lot already
, and it has two features that are fundamental solutions to some product challenges. But from just reading Bedrock's doc
umentation/demos/how-tos I get the sense it is a simpler, more composable version of the lang ecosystem.

Then there's f
ascinating tools that offer a GUI of sorts like Vellum. I'm a coder so the idea of being that hands off is concerning an
d not probably necessary, but for ideation it could be awesome.

Bottom line, I'm about to deep dive these and was curio
us if others would share their experiences with it; pitfalls; etc. thanks!
```
---

     
 
all -  [ Is there an underlying prompt that helps route tools in langgraph? ](https://www.reddit.com/r/LangChain/comments/1hrhvg8/is_there_an_underlying_prompt_that_helps_route/) , 2025-01-03-0913
```

I’m trying to understand how giving a list of functions and binding it to say a huggingface model gives the LLM informa
tion about said functions. Tried digging through source but I might have been looking in wrong area but is there like a 
pre defined system prompt that takes in the function info and makes the LLM create structures output? Or is it trying to
 infer parameters and doc strings to give to the LLM some other way?

```
---

     
 
all -  [ How are you dealing with very large output tools? ](https://www.reddit.com/r/LangChain/comments/1hrgq9k/how_are_you_dealing_with_very_large_output_tools/) , 2025-01-03-0913
```
Hello,

I'm using a basic ReAct (Reasoning and Acting) architecture to interact with a very large database, in some case
s, when a general overview is required, the tool output is very large, and the LLM starts to hallucinate. It doesn't hap
pen when the tool output is reasonable.   
  
I'm testing it locally using Llama 3.1 8B, which has an interesting contex
t window (128k). I'm trying to avoid the need of using a bigger model, I'm looking for a way to manage those large outpu
ts.

Can you suggest a way to manage huge tool outputs?
```
---

     
 
all -  [ How do I get really good at RAG? ](https://www.reddit.com/r/LangChain/comments/1hre9pq/how_do_i_get_really_good_at_rag/) , 2025-01-03-0913
```
I want to learn as much as I can about RAG, so that I can build product ready RAG for a new job I'm joining. How can I b
ecome an expert? I'm a full stack dev with decent experience building AI agents
```
---

     
 
all -  [ Looking for AI solutions in this industry that would integrate with my platform? ](https://www.reddit.com/r/LangChain/comments/1hrcwjy/looking_for_ai_solutions_in_this_industry_that/) , 2025-01-03-0913
```




Im currently putting together a startup, Analytics Depot, that will be a one-stop AI solution for businesses. Like H
ome Depot, but it will have AI chatbots in Legal, Finance, Insurance, Real Estate, Oil and Gas, Ecommerce, etc. The end 
clients will be freelancers and small businesses that could benefit from such resources. Later would like to offer solut
ions to the Fortune 500 companies etc. 



If you are building such domain specific AI chatbots, I would love to discuss
 integrating your solution into my marketplace/platform. That would enable my teams to focus on marketing and frontend, 
and I can pay based on subscriber usage/traffic etc. Seems like a win-win.



Dm me if this sounds interesting.
```
---

     
 
all -  [ How do I install this on my laptop? ](https://www.reddit.com/r/crewai/comments/1hrb4li/how_do_i_install_this_on_my_laptop/) , 2025-01-03-0913
```
Im currently taking the multi agents CrewAI class on Deeplearning AI. In one of the classes, it says that I can install 
the following on my own machine. Can you give me guidance on how i can do that? (I do have python 3.12 on my laptop) 

h
ttps://preview.redd.it/f6gehd2xufae1.png?width=1417&format=png&auto=webp&s=86f6e2f0ee192de9b8ebe85bf07bae8619ea2fb6


```
---

     
 
all -  [ I think networking is the only key to land a job in this market. Here's my experience so far. ](https://www.reddit.com/r/developersIndia/comments/1hr8ahr/i_think_networking_is_the_only_key_to_land_a_job/) , 2025-01-03-0913
```
I am in my final year of BE. I am constantly applying on job platforms, even after getting shortlisted (which itself is 
tough and very luck based) the recruiter will ghost you.
Here is what's gonna happen:
Your profile will get shortlisted.

You're gonna recieve an assignment link.
You'll submit your best work within the deadline.
In 95% of the case you'll ge
t ghosted here (even if your assignment/work is as per industry standards).
Let's say you pass the first round, then com
es interview round.
The interview round has always been good for me, what's not good is post interview part (in one case
 the recruiter forgot he interviewed me, I had to call him and he gave me another assignment and later ghosted me).
Afte
r all this, the founder will hire someone they already know.

I spoke with many experienced people and my friends who ar
e working, everyone says application on job sites are purely luck based.
Everyone suggests me to 'Network' on Twitter or
 Reddit, saying this is how they landed a job.

To all the people who landed a successful refferal or got a job purely b
y reaching out or networking, any tips on 'How to actually Network?' will be helpful.
Anyone with extra position in thei
r company for a developer/intern, can you consider a refferal?
(Tech stack: Next.js/ React, Python, Flask/Django, RAG im
plemention, Langchain and development of AI agents using CrewAI or LangGraph)

Thank you.
```
---

     
 
all -  [ Is Langchain useful for non developers? ](https://www.reddit.com/r/LangChain/comments/1hr52m5/is_langchain_useful_for_non_developers/) , 2025-01-03-0913
```
As someone who is very passionate about ai tech and would like to create my own app using private database and images, I
 am in search of the best way to achieve this as I have no developer experience. Langchain has been mentioned in YouTube
 videos so here I am. I have experience training my own Loras through stable diffusion and such but would like to take s
teps further. Lately, I have been seeing people using Bolt to create websites and such. It seems like you need some codi
ng knowledge and experience to work with Langchain.
```
---

     
 
all -  [ Beginner Vision rag with ColQwen in pure python ](https://www.reddit.com/r/LangChain/comments/1hr43hf/beginner_vision_rag_with_colqwen_in_pure_python/) , 2025-01-03-0913
```
I made a beginner Vision rag project without using langchain or llamaindex or any framework. This is how project works -
 first we convert the pdf to images using pymupdf. Then embeddings are generated for these images using jina clip v2 and
 ColQwen. Images and along with vectors are indexed to qdrant. Then based on user query we perform search on jina embedd
ings and rerank using ColQwen. Gemini flash is used to answer the user queries based on retrieved images. Entire ColQwen
 work is inspired from Qdrant youtube video on ColPali. I would definitely recommend watching that video. 

GitHub repo

https://github.com/Lokesh-Chimakurthi/vision-rag

Qdrant video
https://www.youtube.com/live/_h6SN1WwnLs?si=YzTBY_vhYVkiy
uNH
```
---

     
 
all -  [ 🚀 Enhancing Mathematical Problem Solving with Large Language Models: A Divide and Conquer Approach ](https://www.reddit.com/r/LangChain/comments/1hqz8fa/enhancing_mathematical_problem_solving_with_large/) , 2025-01-03-0913
```
Hi everyone!

I'm excited to share our latest project: **Enhancing Mathematical Problem Solving with Large Language Mode
ls (LLMs)**. Our team has developed a novel approach that utilizes a divide and conquer strategy to improve the accuracy
 of LLMs in mathematical applications.

# Key Highlights:

* Focuses on computational challenges rather than proof-based
 problems.
* Achieves state-of-the-art performance in various tests.
* Open-source code available for anyone to explore 
and contribute!

Check out our GitHub repository here: [DaC-LLM](https://github.com/JasonAlbertEinstien/DaC-LLM)

We’re 
looking for feedback and potential collaborators who are interested in advancing research in this area. Feel free to rea
ch out or comment with any questions!

Thanks for your support!
```
---

     
 
all -  [ 'Why' isn't Langchain/Langgraph  production-ready? ](https://www.reddit.com/r/LangChain/comments/1hqufg2/why_isnt_langchainlanggraph_productionready/) , 2025-01-03-0913
```
Please help me understand. I've come across many comments stating that 'Langchain isn't production-ready,' but none expl
ain why. For my use case - developing serverless AI call agents with customizable features (like calendar booking and ad
ding another human to calls mid-conversation) - would it be okay to proceed? I'm using Langraph, but if this approach (s
erverless + Langgraph ) will cause problems, how should I proceed? Should I build from scratch? If so, where should I st
art learning that?

Thanks for reading! Any answers would be greatly appreciated.'
```
---

     
 
all -  [ Fast Multi-turn (follow-up questions) Intent detection and smart information extraction. ](https://www.reddit.com/r/LangChain/comments/1hqtqgi/fast_multiturn_followup_questions_intent/) , 2025-01-03-0913
```
There several posts and threads on reddit like this [one](https://www.reddit.com/r/LocalLLaMA/comments/18mqwg6/best_prac
tice_for_rag_with_followup_chat/) and this [one](https://www.reddit.com/r/LangChain/comments/1djcvh0/chat_history_for_ra
g_how_to_search_for_follow_up/) that highlight challenges with effectively handling follow-up questions from a user, esp
ecially in RAG scenarios. These scenarios include adjusting retrieval (e.g. what are the benefits of renewable energy ->
 *include cost considerations)*, clarifying a response (e.g. tell me about the history of the internet -> *now focus on 
how ARPANET worked*), switching intent (e.g. What are the symptoms of diabetes? -> *How is it diagnosed*?)*,* etc. All o
f these are multi-turn scenarios.

Handling multi-turn scenarios requires carefully crafting, editing and optimizing a p
rompt to an LLM to first rewrite the follow-up query, extract relevant contextual information and then trigger retrieval
 to answer the question. The whole process is slow, error prone and adds significant latency.

We built a 2M LoRA LLM ca
lled Arch-Intent and packaged it in [https://github.com/katanemo/archgw](https://github.com/katanemo/archgw) \- the inte
lligent gateway for agents - which offers fast and accurate detection of multi-turn prompts (default 4K context window) 
and can call downstream APIs in <500 ms (via [Arch-Function](https://huggingface.co/katanemo/Arch-Function-3B), the fast
est and leading OSS function calling LLM ) with required and optional parameters so that developers can write simple API
s.

Below is simple example code on how you can easily support multi-turn scenarios in RAG, and let Arch handle all the 
complexity ahead in the request lifecycle around intent detection, information extraction, and function calling - so tha
t developers can focus on the stuff that matters the most.

    import os
    import gradio as gr
    
    from fastapi 
import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional
    from openai import 
OpenAI
    
    app = FastAPI()
    
    # Define the request model
    class EnergySourceRequest(BaseModel):
        en
ergy_source: str
        consideration: Optional[str] = None
    
    class EnergySourceResponse(BaseModel):
        ene
rgy_source: str
        consideration: Optional[str] = None
    
    # Post method for device summary
    app.post('/age
nt/energy_source_info')
    def get_energy_information(request: EnergySourceRequest):
        '''
        Endpoint to ge
t details about energy source
        '''
        considertion = 'You don't have any specific consideration. Feel free t
o talk in a more open ended fashion'
    
        if request.consideration is not None:
            considertion = f'Add
 specific focus on the following consideration when you summarize the content for the energy source: {request.considerat
ion}'
    
        response = {
            'energy_source': request.energy_source,
            'consideration': conside
rtion,
        }
        return response

And this is what the user experience looks like when the above APIs are config
ured with Arch.

https://preview.redd.it/b6m2qrv9n19e1.png?width=1666&format=png&auto=webp&s=e7c41be36d381041352f3f11e68
dcb389b72d936
```
---

     
 
all -  [ In the final semester, looking for AI/ML or Data Science positions ](https://www.reddit.com/r/learnmachinelearning/comments/1hqt9p8/in_the_final_semester_looking_for_aiml_or_data/) , 2025-01-03-0913
```
Hello guys, I'm in my final semester of the masters and now looking for a full-time roles. I want to improve my resume. 
Please rate it and give feedback.

https://preview.redd.it/03arzufciaae1.jpg?width=2479&format=pjpg&auto=webp&s=68954afa
718edf280175b563fe1cf6ed30435b7d


```
---

     
 
all -  [ I also would be thinking about how to increase my skills immediately after suffering brain damage. / ](https://i.redd.it/qwkxlviio9ae1.jpeg) , 2025-01-03-0913
```
This is wild way to start a LinkedIn post. I’ve seen some stuff but wow.
```
---

     
 
all -  [ LangGraph Conceptual Guide ](https://www.reddit.com/r/copilotkit/comments/1hqla7z/langgraph_conceptual_guide/) , 2025-01-03-0913
```
Check out LangGraph's Conceptual guide.  
A perfect pair with [CoAgents](https://docs.copilotkit.ai/coagents)  
[https:/
/langchain-ai.github.io/langgraph/concepts/](https://langchain-ai.github.io/langgraph/concepts/)
```
---

     
 
all -  [ How do I Display what the Agent is doing on the backend to the frontend ](https://www.reddit.com/r/LangChain/comments/1hqjvf3/how_do_i_display_what_the_agent_is_doing_on_the/) , 2025-01-03-0913
```
I’ve been playing around with the LangGraph tutorials to get myself familiar. I’m trying to figure out how to display wh
at the Agent is doing on the frontend.   


Here's a snippet from the LangGraph docs:  
[Streaming](https://langchain-ai
.github.io/langgraph/concepts/streaming/): Streaming is crucial for enhancing the responsiveness of applications built o
n LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves u
ser experience (UX), particularly when dealing with the latency of LLMs.

I'd like to be able to stream between nodes fo
r better UX of my app, but since LangGraph is a backend solution, is there a good solution for the frontend so I don't h
ave to build this from scratch? 

My stack is Next.js with some Python backend, and I want to add LangGraph(Agents)

Tha
nks in advance!
```
---

     
 
all -  [ Seeking Feedback on My RAG Architecture for Context Retrieval and Lightweight Optimization ](https://www.reddit.com/r/LangChain/comments/1hqhmdx/seeking_feedback_on_my_rag_architecture_for/) , 2025-01-03-0913
```
I am currently developing a Retrieval-Augmented Generation (RAG) system designed to answer user questions by extracting 
context from two sources: a database or CSV documents. To guide the RAG in selecting the optimal source for context extr
action, I have outlined the following architecture. How do you find it? Is it efficient, or are there bottlenecks I shou
ld address to make it more lightweight?

# Architecture Outline

# 1. Agent Node

* Processes the user question and deci
des the retrieval source or falls back to the LLM's internal knowledge.

# 2. Conditional Edge: Determine Retrieval Sour
ce

* **Check Database**: Verifies if the relevant context exists in the SQLite database.
* **Check CSV Documents**: Ver
ifies if the relevant context exists in the CSV documents.
* **Fallback**: If neither source is applicable, defaults to 
the LLM's internal knowledge.

# 3. SQLite Path

* **Schema Prompt Node**: The LLM receives the database schema and the 
user query to identify relevant fields.
* **Query Construction Node**: The LLM generates an SQL query based on the schem
a and fields.
* **Execute Query Node**: Executes the SQL query and retrieves the results.
* **Answer Formulation Node**:
 Formats the retrieved data into a natural language response using the LLM.

# 4. CSV Path

* **Retrieve CSV Data Node**
: Fetches relevant rows from the CSV documents.
* **Answer Formulation Node**: Summarizes and formats the retrieved data
 using the LLM.

# 5. Fallback Path

* **Generate Using Internal Knowledge Node**: Produces a response solely based on t
he LLM's internal knowledge.

This structure aims to balance flexibility and efficiency. Do you see any potential bottle
necks, or have suggestions for optimization to ensure the system remains lightweight and responsive?


```
---

     
 
all -  [ Graph Structure vs Others  ](https://www.reddit.com/r/LangChain/comments/1hqf270/graph_structure_vs_others/) , 2025-01-03-0913
```
Hi all. I'm looking to see if there's any empirical work done that validates the graph agent structure (e.g., LangGraph)
 as more reliable than other agent/Multi-Agent architectures (non-graph, event-driven). 
```
---

     
 
all -  [ An Agent that creates memes for you ](https://open.substack.com/pub/diamantai/p/viral-marketing-made-easy-unlocking?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) , 2025-01-03-0913
```
Memes are the internet’s universal language, but creating ones that truly align with your brand and actually connect wit
h your audience? That’s no small task.

During the hackathon that I ran with LangChain, a talented participant worked on
 a system designed to solve this challenge. It uses AI to analyze a brand’s tone, audience, and personality and then tra
nsforms that data into memes that feel authentic and relevant.

Here’s what makes it exciting:

- It simplifies complex 
brand messaging into relatable humor.
- It adapts to internet trends in real-time.
- It creates memes that aren’t just f
unny—they’re actually effective.
If you’re curious about how it all works, I’ve broken it down in a blog post attached w
ith examples and insights into the process.
```
---

     
 
all -  [ Converting PDFs to Markdown for Higher Quality Embeddings with Langchain.js ](https://www.reddit.com/r/LangChain/comments/1hq8d6c/converting_pdfs_to_markdown_for_higher_quality/) , 2025-01-03-0913
```
edit: I have found a solution from llamaIndex, they have [LLamaParser](https://docs.cloud.llamaindex.ai/llamaparse/getti
ng_started/typescript) apis. Its paid but is very capable.  
  
I am working on RAG LLM projects with Langchain.js using
 Node.js. Most of the data I retrieve are PDFs and a bit of JSON.

For higher quality, I would like to convert my PDFs i
nto Markdown before embedding starts. This involves deleting headers and footers, extracting tables and pictures, and co
nverting the text into Markdown so that it is clear to the LLM whether it is body text or an important title.

Example: 
**This is Title** and < p >just text

I want to ensure that pictures and tables are clearly identified in Markdown, and 
that unnecessary elements are removed. I have found some Python libraries that people use for this purpose, but I need s
omething for Node.js. Has anyone experienced with this?

And of course, any other tips for better RAG LLM are also welco
me! :)

Already tried 'markdown-it' library but not really happy with result. The only thing it does is sometimes adding
 < p >. (Which is still better than nothing but i want everything to be very clear) It's not clear :

* if this text is 
Title or Body,
* Can't delete Footer Information with this
* Can't export Table/Picture etc.
```
---

     
 
all -  [ langchain_experimental  SQLDatabaseChain.invoke() question ](https://www.reddit.com/r/LangChain/comments/1hq5px2/langchain_experimental_sqldatabasechaininvoke/) , 2025-01-03-0913
```
I am learning another langchain video  with LLM interacting with SQL.

Here is the  [Jupyter notebook link](https://gith
ub.com/codebasics/langchain/blob/main/4_sqldb_tshirts/t_shirt_sales_llm.ipynb) and its accompanying [YOUTUBE  Video](htt
ps://www.youtube.com/watch?v=4wtrl4hnPT8&t=354s) between the `15:35` `and the 15:39 mark`.

My question is regarding the
 following chunks of code - the issue is specifically executing the second line of code.

    db_chain = SQLDatabaseChai
n.from_llm(llm, db, verbose=True)
    qns1 = db_chain('How many t-shirts do we have left for nike in extra small size an
d white color?')

Update - please note that the second line of code shown above can actually  be executed using `'db_cha
in.invoke'` as shown below, and it yields the same result as the original code :

    qns1 = db_chain.invoke('How many t
-shirts do we have left for nike in extra small size and white color?')

The `Jupyter notebook  output`  upon execution 
of  the above two lines of code is shown as follows:

    > Entering new SQLDatabaseChain chain...
    How many t-shirts
 do we have left for nike in extra small size and white color?
    SQLQuery:SELECT stock_quantity FROM t_shirts WHERE br
and = 'Nike' AND color = 'White' AND size = 'XS'
    SQLResult: [(91,)]
    Answer:91
    > Finished chain.

And here is
 my output :

    > Entering new SQLDatabaseChain chain...
    How many t-shirts do we have left for nike in extra small
 size and white color?
    SQLQuery:SQLQuery: SELECT `stock_quantity` FROM `t_shirts` WHERE `brand` = 'Nike' AND `size` 
= 'XS' AND `color` = 'White';
    SQLResult: [(91,)]
    Answer:Question: How many t-shirts do we have left for nike in 
extra small size and white color?
    SQLQuery: SELECT `stock_quantity` FROM `t_shirts` WHERE `brand` = 'Nike' AND `size
` = 'XS' AND `color` = 'White';
    > Finished chain.

So the difference between the two output  are the 'SQLQuery' and 
'Answer'.   But we can SKIP the 'SQLQuery' differences as this looks like just a minor formatting issue - the SQL query 
generated may not be 'exactly' the same word-for-word but they are identical.

My main issue is my 'Answer' output is sh
owing a string representation of a dictionary keys `'Question'`  and `'SQLQuery'` with their respective values.   Why is
 the  'Answer' not showing  `91` ?

Both the 'SQLResult' outputs (from the tutorial and my output)  are identical.

I di
d a little further digging and executed the following lines

    from pprint import pprint 
    pprint(qns1)

The output
 shows the  `qns1` variable  is actually a dictionary with the following output (on my end):

    {'query': 'How many t-
shirts do we have left for nike in extra small size and '
              'red color?',
     'result': 'Question: How many
 t-shirts do we have left for nike in extra '
               'small size and red color?\n'
               'SQLQuery: SEL
ECT `stock_quantity` FROM `t_shirts` WHERE `brand` = '
               ''Nike' AND `size` = 'XS' AND `color` = 'Red';'}


What code change do I need to do to make the `'result'` show  as `'91'` ?
```
---

     
 
all -  [ StepsTrack: A small Typescript library that helps Logging and Optimizing Pipeline Steps ](https://www.reddit.com/r/Rag/comments/1hq2571/stepstrack_a_small_typescript_library_that_helps/) , 2025-01-03-0913
```
Hello everyone 👋,

I have been working on optimizing an RAG pipeline (mainly on improving speed and reducing token usage
) deployed in production. I found debugging and optimizing very challenging, as there can be a bunch of sub-steps in the
 pipeline, depending on user's query, each step may involves dynamic LLM response and random data retrieval, making the 
response time and runtime flow very non-deterministic. 

So I created **StepsTrack** [https://github.com/lokwkin/steps-t
rack](https://github.com/lokwkin/steps-track) which is a small and simple Typescript library to help me track what was h
appening inside each RAG pipeline runs. It:

* ***Track the results and latency*** of each steps, allow me to export for
 further debug.
* Visualize them into ***Gantt Chart*** & ***Execution Graph*** (I found it very useful when explaining 
the bottlenecks and flow issues to boss and other teammates).
* ***Emit events*** hooks to allow integrating (for furthe
r frontend or external integration like SSE / websocket)

Upcoming planned features:

* Generate execution stats aggrega
ted from multiple pipeline runs (useful on Prod environments to see the behavior from different user inputs)
* Add Redis
 support for pub/sub events and data storage (as an adapter for integrations)
* Implement real-time execution monitoring
. (Probably an internal dashboard frontend to monitor what steps in-progress) 

Note: while StepsTrack focuses on speed 
improvement and debugging logical flow, it doesn’t help address RAG accuracy. I also tried to write this tool non-LLM fo
cused so it can possibility used in other types of applications that has pipeline-like chains of steps.

\---

I’m sure 
there would be similar or better libraries out there, and this library probably won’t work with popular RAG frameworks l
ike LangChain etc. But if you are building pipelines in Typescript and without using any frameworks, you might find Step
sTrack as helpful as I did. 

Feel free to check it out at [https://github.com/lokwkin/steps-track](https://github.com/l
okwkin/steps-track)

Welcome any thoughts, comments, or suggestions! Thanks! 😊 
```
---

     
 
all -  [ What is actually sent to the LLM to decide whether or not to call a tool? ](https://www.reddit.com/r/LangChain/comments/1hpypmj/what_is_actually_sent_to_the_llm_to_decide/) , 2025-01-03-0913
```
I'm working through the 'Build a Retrieval Augmented Generation (RAG) App: Part 2' tutorial where you bind the retrieve 
function as a tool, and then add a conditional edge for when it is executed.

I've been digging through the documentatio
n, but I cannot seem to find an answer for the actual message sent to the LLM to instruct it to either use the retrieve 
tool or respond (as an example: 'If needed, use the retrieve tool to retrieve information related to a query. Otherwise 
respond directly').

This tutorial also had the LLM rephrase the user queries when calling the retrieve tool.

Although 
it doesn't stop me from proceeding, I would really like a look behind the hood as to what LangChain is sending when tool
s are binded to a ChatModel.

  
EDIT: Thank you for your help. I was unable to see this information because it is passe
d as a separate argument in the API (which is exactly the understanding I was trying to obtain). 
```
---

     
 
all -  [ Chat memory  ](https://www.reddit.com/r/LangChain/comments/1hpx94c/chat_memory/) , 2025-01-03-0913
```
Let me ask you an absolute beginner doubt. I have created a simple react agentic architecture using langraph. I have use
d 'MessagesState' as State and passed it to the graph while compiling it.
But for multiple sequential invocations, it se
ems like the state is refreshed. 

For example if I invoke the graph with 
'hi, from now on your name is 'Groot'', 

The
 response will be like 
'Hi, I'm Groot, how can I help you?' 

But for the next execution if I ask the name, it's helple
ss about it.

Is there any other way than using checkpointers to tackle this task?
```
---

     
 
all -  [ How to Add System Message to a multimodal Prompt? ](https://www.reddit.com/r/LangChain/comments/1hpto5u/how_to_add_system_message_to_a_multimodal_prompt/) , 2025-01-03-0913
```
Hi guys, Am using Langchain Python. I have created a sorta Prompt Template to pass my prompt and an Image. But I want to
 add System Message to the Prompt. How do I do it? The code is below

````
import base64

from langchain_core.messages i
mport HumanMessage, SystemMessage

def ga_template(image_path, prompt):

with open(image_path, 'rb') as image_file:

dec
oded_string = base64.b64encode(image_file.read()).decode('utf-8')

message HumanMessage(

content=[

{'type': 'text', 't
ext': prompt},

{

'type': 'image_url',

'image_url': {'url': f'data:image/jpeg;base64, {decoded_string}'},

},

],

ret
urn message
```


```
---

     
 
all -  [ Handle return of Multiple tool request ](https://www.reddit.com/r/LangChain/comments/1hprrzi/handle_return_of_multiple_tool_request/) , 2025-01-03-0913
```
Hi guys,I need some help working with LangChain and LangGraph.

I have an agent, a supervisor, and a tool associated wit
h my agent (this tool is an API request that returns a JSON). Basically, my problem is:When my agent calls the tool mult
iple times, before returning to the supervisor, the agent compacts the multiple returns into  single text. 

https://pre
view.redd.it/9q98tldpo0ae1.png?width=537&format=png&auto=webp&s=54a254df5970b98856644aa391b5304fe76062ef

However, when 
the tool is requested a single time, this doesn't happen, and I don't know how to resolve this efficiently.

https://pre
view.redd.it/2y42wavqo0ae1.png?width=356&format=png&auto=webp&s=0c446845a5e18ff85a81df697c569e4d5dbc6765

Can someone he
lp me?  

```
---

     
 
all -  [ NestJS + LangChain “Langgraphs”: Embed or Deploy Separately? ](https://www.reddit.com/r/LangChain/comments/1hpmxt9/nestjs_langchain_langgraphs_embed_or_deploy/) , 2025-01-03-0913
```
Hey folks, I’m experimenting with LangChain’s Langgraphs in a NestJS server.

Thank you for amazing work, Langchain team
.  All these days I thought 'good prompt building' enough, only until I discovered 'Langgraph'

I’m trying to decide if 
I should embed the langgraphs directly in my NestJS app or set them up as a separate service (or even use their Langgrap
h platform, maybe eventually). 

Would love any pointers about performance, scalability, or best practices.

Thanks! 🙏
```
---

     
 
all -  [ How to Handle Token Limit Exceeded Error in OpenAI API ](https://www.reddit.com/r/LangChain/comments/1hpjms4/how_to_handle_token_limit_exceeded_error_in/) , 2025-01-03-0913
```
I'm getting an error from the OpenAI API stating that the context length exceeds the model's limit, even though I'm only
 passing the last four messages to the prompt. **I’ve verified that each interaction is using around 1056 tokens**, but 
I’m still encountering the error when sending the prompt to the model and not sure why I'm still exceeding the token lim
it.

Full error message:

openai.BadRequestError: Error code: 400 - {'error': {'message': 'This model's maximum context 
length is 8192 tokens. However, your messages resulted in 8452 tokens (8415 in the messages, 37 in the functions). Pleas
e reduce the length of the messages or functions.', 'type': 'invalid\_request\_error', 'param': 'messages', 'code': 'con
text\_length\_exceeded'}}

Here is my code:



`tool(response_format='content_and_artifact')`  
`def retrieve(query: str
):`  
`'''Retrivieving function'''`  
`try:`  
`vector_store = document_embeddings.get_vectorstore()`  
`retrieved_docs 
= vector_store.similarity_search(query, k=4, max_tokens_limit=4000)`  
`serialized = '\n\n'.join(`  
`(f'Source: {doc.me
tadata}\n' f'Content: {doc.page_content}')`  
`for doc in retrieved_docs`  
`)`  
`return serialized, retrieved_docs`  

`except Exception as e:`  
`print(f'Error during retrieval: {e}')`  
`raise e`

    def filter_messages(messages: list):

        # This is very simple helper function which only ever uses the 4 last messages to prevent context limit error
 
       return messages[-4:]
    
    def query_or_respond(state: MessagesState):
        llm_with_tools = llm.bind_tools
([retrieve])
        response = llm_with_tools.invoke(state['messages'])
        return {'messages': [response]}
    
  
  tools = ToolNode([retrieve])
    from langchain_community.callbacks.manager import get_openai_callback
    def generat
e(state: MessagesState):
        messages = filter_messages(state['messages'])
        recent_tool_messages = []
       
 for message in reversed(messages):
            if message.type == 'tool':
                print('Tool')
               
 recent_tool_messages.append(message)
            else:
                break
        tool_messages = recent_tool_messag
es[::-1]
    
        docs_content = '\n\n'.join(doc.content for doc in tool_messages)
        system_message_content = 
(
            'You are an assistant for question-answering tasks. '
            'Use the following pieces of retrieved c
ontext to answer '
            'the question. If you don't know the answer, say that you '
            'don't know. Use 
three sentences maximum and keep the '
            'answer concise.'
            '\n\n'
            f'{docs_content}'
  
          'Use documents/context . ')
    
        conversation_messages = [
            message
            for message
 in messages
            if message.type in ('human', 'system')
            or (message.type == 'ai' and not message.too
l_calls)
        ]
        prompt = [SystemMessage(system_message_content)] + conversation_messages
        print(f'prom
pt: {prompt}')
            # Run
        with get_openai_callback() as cb:
            response = llm.invoke(prompt)
   
         print(f'Total Tokens: {cb.total_tokens}')
            print(f'Prompt Tokens: {cb.prompt_tokens}')
            p
rint(f'Completion Tokens: {cb.completion_tokens}')
            print(f'Total Cost (USD): ${cb.total_cost}')
    
       
 return {'messages': [response]}
    
    
    memory = MemorySaver()
    
     graph_builder = StateGraph(MessagesState
)
     graph_builder.add_node(query_or_respond)
     graph_builder.add_node(tools)
     graph_builder.add_node(generate)

     graph_builder.set_entry_point('query_or_respond')
     graph_builder.add_conditional_edges(
         'query_or_res
pond',
         tools_condition,
         {END: END, 'tools': 'tools'},
     )
     graph_builder.add_edge('tools','gene
rate')
     graph_builder.add_edge('generate', END)
     graph = graph_builder.compile(checkpointer=memory)

For the emb
edding i am using Openai embedding, chunk size = 1000, overlap = 200, parsin with Llamaparse and Unstructured for Makrdo
wnLoader\`

Any advice or solutions would be greatly appreciated!
```
---

     
 
all -  [ Need Feedback on Custom Reducer to Summarize Conversations ](https://www.reddit.com/r/LangChain/comments/1hpjm65/need_feedback_on_custom_reducer_to_summarize/) , 2025-01-03-0913
```
I’m newbie to Langchain and experimenting with LangGraph to build an SQL analysis workflow. I’ve come up with a pattern 
for maintaining conversation context and would love feedback:

* At the end of each query, I summarize the Q&A using a n
ode.
* A custom state reducer takes the previous summary, combines it with the new one, updates the state, and stores it
 as `previous_convo`.

The goal is to keep a condensed version of the entire conversation history accessible.

**Does th
is seem efficient? Any better approaches I should consider?**
```
---

     
 
all -  [ Resume Review: ML/AI Engineering Grad Student Looking for Internships, not having much luck ](https://www.reddit.com/r/Resume/comments/1hp6pt3/resume_review_mlai_engineering_grad_student/) , 2025-01-03-0913
```
I'm a current Computer Engineering Master's student focusing on AI/Machine Learning, and I've been applying to internshi
ps, but the only replies I ever get are if I have a referral. I got an interview with Salesforce for an AI internship be
cause of a referral and the it went well. So even though I don't know if I'll get the position I'm wondering why I can't
 get companies lower on the totem pole than Salesforce to give me an interview or OA.

I'm wondering if my resume format
 is bad and getting auto rejected or if I just don't have enough experience to make it in a competitive market (It could
 be a combination of both). I get the sense that my resume isn't even making it past recruiters. I see other people at l
east get interviews with these places, I'm wondering what they're doing that I'm not.

Any advice or tips would be great
ly appreciated. I haven't had much luck getting advice in other subs or having my resume refined by someone on Fiver for
 $60. For reference I am a US citizen (I know that can affect what recruiters do with applications). 

https://preview.r
edd.it/wkkxxgb1yu9e1.jpg?width=1252&format=pjpg&auto=webp&s=f09d4baa91524c95784f175dce6b085689404595


```
---

     
