 
all -  [ How to build a reusable chain that takes the output of another chain as a keyword argument for the t ](https://www.reddit.com/r/LangChain/comments/1dursrw/how_to_build_a_reusable_chain_that_takes_the/) , 2024-07-04-0910
```
I'm trying to build reusable chains and I'm having issues trying to set it up so it takes the output of the previous cha
in as one of the template format arguments.

In this example, I have a chain that generates a title based on a topic and
 a chain that translates the title into a different language. The topic and the language I want to provide them when I i
nvoke the final chain.

If my 2nd chain only has one single input for the template (because I hardcode the language), ev
erything works perfectly:

    # Title Chain
    title_template = PromptTemplate.from_template('Generate a title for a b
log post about the following topic: {topic}')
    generate_title = title_template | llm | StrOutputParser()
    
    # T
ranslate Chain
    translate_template = PromptTemplate.from_template('Translate the following text to spanish: {text}')

    translate_chain = translate_template | llm | StrOutputParser()
    
    # Combine and run
    combined_chain = gener
ate_title | translate_chain
    result = combined_chain.invoke({'topic': 'The benefits of exercise'})

But if I want to 
be able to provide the language when I invoke the final chain then, I dont know how to pass the output to the template d
ictionary. See the 'HOW\_TO\_PASS\_OUTPUT\_OF\_PREVIOUS\_CHAIN' in the code

    # Title Chain
    title_template = Prom
ptTemplate.from_template('Generate a title for a blog post about the following topic: {topic}')
    generate_title = tit
le_template | llm | StrOutputParser()
    
    # Translate Chain
    translate_template = PromptTemplate.from_template('
Translate the following text to {language}: {text}')
    translate_chain = {'language': itemgetter('language'), 'text': 
HOW_TO_PASS_OUTPUT_OF_PREVIOUS_CHAIN?} | translate_template | llm | StrOutputParser()
    
    # Combine and run
    com
bined_chain = generate_title | translate_chain
    result = combined_chain.invoke({'topic': 'The benefits of exercise', 
'language': 'Spanish'})

  
I also tried to use a lambda function but the itemgetter doesn't seem to work:

    translat
e_chain = (
        lambda text: {'language': itemgetter('language'), 'text': text}
        | translate_template
       
 | llm
        | StrOutputParser()
    )

  
If anyone knows the answer I would be much appreciated.
```
---

     
 
all -  [ Read and write to Google sheets ](https://www.reddit.com/r/LangChain/comments/1dursic/read_and_write_to_google_sheets/) , 2024-07-04-0910
```
I’m not a programmer, only got basic understanding of the concepts. I’m wanting to do the following (I’ll probably get s
omeone from Upwork to do it) read and write to the company daily operations Google sheet using natural language. Users c
an type requests and the agent will write and read the document. I’m thinking I’ll have python scripts to do actions lik
e insert new work orders with all formulas in place.

My concern is, what happens if someone edits the GS manually. The 
agent will not know exactly which row a certain data is if I want to update it. Or can the agent read first to ensure th
e data is in the target position and then update it? 
```
---

     
 
all -  [ Retrieve a single document ](https://www.reddit.com/r/LangChain/comments/1duoub8/retrieve_a_single_document/) , 2024-07-04-0910
```
I've created a RAG with document retriever and everything works fine. 

I want to add a feature: the user can specify a 
document to apply search to. 
The question the user ask is something related to the single document, OR something like '
resume it', 'translate it', whatever. 

What I though was use parent document retriever and inject the whole document (d
on't think about tokens limit at the moment) in the context. Is theoretically possible but my question is: how can I det
ect a 'manipulation' question (resume, translate, etc)?

In these cases I want to use parent document (or whatever strat
egy), and in other cases the default strategy. 

Should I put some ML model between question and retriever? I want to av
oid using AI tools to not consume another open Ai call to detect what retriever I should use. 

Thanks 
```
---

     
 
all -  [ Best way to summarize a book? ](https://www.reddit.com/r/LocalLLaMA/comments/1dulrgg/best_way_to_summarize_a_book/) , 2024-07-04-0910
```
So, I have a collection of ebooks on my PC, and I want to summarize them.

I see there are many methods for doing this, 
but what was the best for you? I thought of summarizing chunks of it and adding them up in a final summary, but this can
 get buggy with LLM's due to the lack of context, and passing them through Claude or Gemini 2 is too expensive.

Word cl
ouds, vector databases, reducemap like in langchain, etc., etc.

Any other ideas of how to approach this?

My goal is to
 create a summary of each book then vectorize that and create a semantic search engine for my books. Maybe I could make 
an online version if it's good enough.

Thanks.
```
---

     
 
all -  [ Unable to use Langchain with LiteLLM proxy ](https://www.reddit.com/r/LangChain/comments/1dukp60/unable_to_use_langchain_with_litellm_proxy/) , 2024-07-04-0910
```
The LiteLLMProxy needs a special authentication header (see [LiteLLM docs](https://litellm.vercel.app/docs/proxy/user_ke
ys)) which needs to go into a special HTTP header field:

    curl --location 'http://litellm/chat/completions' \
      
     -H 'Content-Type: application/json' \ 
           -H 'Authorization: Bearer <redacted>' ...

 As far as I can tell,
 it's impossible to get `langchain ` 
 to stuff this authorization header into its requests, meaning that `langchain` 
 
cannot be used with `LiteLLM` proxy atm.

My co-workers and I looked deep into the code to try to find a solution, but t
here are so many layers from a model's `invoke` method to anything that makes an HTTP request that we were defeated. Or 
perhaps I'm just missing something?
```
---

     
 
all -  [ I am starting to learn langchain and wathing tutorials on it. But to use language models i need cred ](https://www.reddit.com/r/Langchaindev/comments/1dukjgq/i_am_starting_to_learn_langchain_and_wathing/) , 2024-07-04-0910
```

```
---

     
 
all -  [ Could use some advice on an approach to bring back a similarity search result from a vector store an ](https://www.reddit.com/r/LangChain/comments/1duhvrq/could_use_some_advice_on_an_approach_to_bring/) , 2024-07-04-0910
```
I am creating a fairly straightforward streaming chat thing.  I need to supplement the final llm result of my pretty sim
ple rag chain with a link that I get from a separate vector store search.  Literally just need to tack it on at the end 
of the result.  Does this fit any of the component types in LangChain?  Or should I just do it completely outside of the
 chain?  Any thoughts are appreciated.
```
---

     
 
all -  [ My app works fine in dev but I get type errors on Vercel.  ](https://www.reddit.com/r/nextjs/comments/1duhusj/my_app_works_fine_in_dev_but_i_get_type_errors_on/) , 2024-07-04-0910
```
So I'm making a personal app for fun using the template form vercel: [https://vercel.com/guides/nextjs-langchain-vercel-
ai](https://vercel.com/guides/nextjs-langchain-vercel-ai)

Everything works as it should in dev. It builds successfully 
on Vercel but I get these errors when I try to use the chatbot agent: 

    TypeError: Z.inputVariables is not iterable

        at (node_modules/@langchain/langgraph/node_modules/@langchain/core/dist/prompts/chat.js:689:0)
        at (node_
modules/@langchain/langgraph/dist/prebuilt/react_agent_executor.js:95:41)
        at (node_modules/@langchain/langgraph/
dist/prebuilt/react_agent_executor.js:35:0)
        at (app/api/chat/agents/route.ts:81:35)
        at (node_modules/nex
t/dist/esm/server/future/route-modules/app-route/module.js:195:0)
        at (node_modules/next/dist/esm/server/future/r
oute-modules/app-route/module.js:124:0)
        at (node_modules/next/dist/esm/server/future/route-modules/app-route/mod
ule.js:257:0)
        at (node_modules/next/dist/esm/server/web/edge-route-module-wrapper.js:81:0)
        at (node_modu
les/next/dist/esm/server/web/adapter.js:158:0)

It looks like the error is from the langchain module and not my code? I'
m completely lost at what to do and would really appreciate any help. 

Thank you. 
```
---

     
 
all -  [ RAG for CSV but with Sample Question and Answers? ](https://www.reddit.com/r/LangChain/comments/1duhla8/rag_for_csv_but_with_sample_question_and_answers/) , 2024-07-04-0910
```
I'm trying to build an RAG that answers questions about a dataset that I have using the create_pandas_dataframe_agent. I
 also have a long list of sample questions and answers that I want the RAG to imitate but not exactly copy. These questi
ons contain some domain knowledge and I've also added some information about the columns at the end of these sample ques
tions and answers. 

I'm currently passing this as a prefix parameter but I'm not sure if that's the best way to do this
. 

The idea is to have this pandas agent as something that can answer questions that don't require pandas as well. What
's the best way to build this? Thanks in advance!
```
---

     
 
all -  [ How ollama create embedding using llama2 ](https://www.reddit.com/r/ollama/comments/1dufiah/how_ollama_create_embedding_using_llama2/) , 2024-07-04-0910
```
ollama can use the llama2 model to generate embeddings (see: https://api.python.langchain.com/en/latest/embeddings/langc
hain\_community.embeddings.ollama.OllamaEmbeddings.html).

However, llama2 is not designed as an embedding model. Does a
nyone know how Ollama handled generating embeddings with Llama2?
```
---

     
 
all -  [ Fine-tune LLMs for classification task
 ](https://www.reddit.com/r/LangChain/comments/1duedyv/finetune_llms_for_classification_task/) , 2024-07-04-0910
```
I would like to use an LLM (Llama3 or Mistral for example) for a multilabel-classification task. I have a few 1000 examp
les to train the model on, but not sure what's the best way and library to do that. Is there any best practice how to fi
ne-tune LLMs for classification tasks?
```
---

     
 
all -  [ Is there a better approach for generating proper SQL queries for large databases to retrieve relevan ](https://www.reddit.com/r/LangChain/comments/1dudch2/is_there_a_better_approach_for_generating_proper/) , 2024-07-04-0910
```
Hello everyone,

I've been working on developing an enterprise platform for the past 2 months. This platform allows our 
clients to connect multiple data sources and create customized features powered by LLM for their products. The main issu
e I'm encountering is creating an appropriate query to retrieve relevant information from a large database with over 200
 tables, each containing approximately 30-50 columns. I've experimented with various approaches such as Langgraph, custo
m LCEL, retriever with Langgraph, and different LLMs, but I'm still not getting the desired response. If anyone has expe
rience with this type of problem, I would greatly appreciate it if you could share your knowledge. Thank you in advance.

```
---

     
 
all -  [ Can't get LlaMa 2 to generate responses ](https://www.reddit.com/r/LocalLLaMA/comments/1ducthu/cant_get_llama_2_to_generate_responses/) , 2024-07-04-0910
```
I've been trying to get the llama-2-7b-hf model to generate text for a simple use case but it doesn't seem to be doing a
nything when I run it. I'm using this code:

\`

    from langchain_huggingface import HuggingFacePipeline
    import to
rch
    from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, pipeline
    
    model_dir = 'C
://Users//shrim//Llama-2-7b-hf' #change the directory to the model later
    tokenizer = AutoTokenizer.from_pretrained(m
odel_dir)
    model = AutoModelForCausalLM.from_pretrained(
        model_dir, torch_dtype=torch.float16, trust_remote_c
ode=True, device_map='auto'
    )
    
    generation_config = GenerationConfig.from_pretrained(model_dir)
    generatio
n_config.max_new_tokens = 1024
    generation_config.temperature = 0.0001
    generation_config.top_p = 0.95
    generat
ion_config.do_sample = True
    generation_config.repetition_penalty = 1.15
    
    text_pipeline = pipeline(
        '
text-generation',
        model=model,
        tokenizer=tokenizer,
        generation_config=generation_config,
    )
 
   
    llm=HuggingFacePipeline(pipeline=text_pipeline, model_kwargs={'temperature':0})
    
    result = llm.invoke(
  
      'Explain the difference between ChatGPT and open source LLMs in a couple of lines.'
    )
    print(result)
    fr
om langchain_huggingface import HuggingFacePipeline
    import torch
    from transformers import AutoTokenizer, AutoMod
elForCausalLM, GenerationConfig, pipeline
    
    
    model_dir = 'C://Users//shrim//Llama-2-7b-hf' #change the direct
ory to the model later
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pr
etrained(
        model_dir, torch_dtype=torch.float16, trust_remote_code=True, device_map='auto'
    )
    
    
    ge
neration_config = GenerationConfig.from_pretrained(model_dir)
    generation_config.max_new_tokens = 1024
    generation
_config.temperature = 0.0001
    generation_config.top_p = 0.95
    generation_config.do_sample = True
    generation_co
nfig.repetition_penalty = 1.15
    
    
    text_pipeline = pipeline(
        'text-generation',
        model=model,
 
       tokenizer=tokenizer,
        generation_config=generation_config,
    )
    
    
    llm=HuggingFacePipeline(pip
eline=text_pipeline, model_kwargs={'temperature':0})
    
    
    result = llm.invoke(
        'Explain the difference 
between ChatGPT and open source LLMs in a couple of lines.'
    )
    print(result)

\`

When i run it, I get the follow
ing in the terminal, the response is not generated and the terminal continues to run:

`Loading checkpoint shards: 100%|
████████████████████████████████████████████████| 2/2 [00:00<00:00,  6.87it/s]`

`WARNING:root:Some parameters are on th
e meta device device because they were offloaded to the cpu and disk.`

  
I have these dependencies installed in a virt
ual environment:  
`torch`  
`transformers`  
`langchain`  
`xformers`  
`chromadb`  
`sentence_transformers`  
`tokeniz
ers`  
`optimum`  
`unstructured`  
`langchain_huggingface`  
`accelerate`

My computer specifications:

OS: Windows 11 
Home  
CPU: 11th Gen Intel(R) Core(TM) i5-11300H @ 3.10GHz  
RAM: 16GB DDR4 3200MHz  
GPU: Intel(R) Iris(R) Xe Graphics 
 
Python version: 3.12.4

Any help would be appreciated, thanks.
```
---

     
 
all -  [ Routing in LangChain JS – Use LLM Classifiers to Call Different Prompts ](https://www.reddit.com/r/LangChain/comments/1duc2qb/routing_in_langchain_js_use_llm_classifiers_to/) , 2024-07-04-0910
```
Hey Everyone, I've made a short example of Routing in LangChain JS by using LLM Classifiers to call different prompts ba
sed on the content of the query:  
[https://www.js-craft.io/blog/routing-langchain-js-different-prompts-based-on-query-t
ype/](https://www.js-craft.io/blog/routing-langchain-js-different-prompts-based-on-query-type/)

In case someone may fin
d it useful :) 
```
---

     
 
all -  [ RAG pipline test ](https://www.reddit.com/r/LangChain/comments/1dubm7s/rag_pipline_test/) , 2024-07-04-0910
```
Hey everyone,

I'm currently testing the RAG (Retrieval-Augmented Generation) pipeline with RAGAS, but I'm facing some c
hallenges. The results aren't as good as expected. Could someone please help me with evaluating the RAG pipeline effecti
vely? Any tips or advice would be greatly appreciated  
#langchain 
```
---

     
 
all -  [ LLM Agent around a BigQuery table ](https://www.reddit.com/r/LangChain/comments/1dubb96/llm_agent_around_a_bigquery_table/) , 2024-07-04-0910
```
HI !

I'm trying to POC a little project.

I have a BigQuery table that looks like this:

|conversation\_id|message\_id|
message\_content|created\_at|
|:-|:-|:-|:-|
|1|1|Hello !|2014-11-19 06:14:03 UTC|
|1|2|Hey, nice to meet you !|2014-11-1
9 06:14:05 UTC|
|2|1|Hello, I have a problem|2015-04-10 11:25:50 UTC|
|2|2|What is your problem ?|2015-04-10 11:25:55 UT
C|

  
This table has millions of rows of conversations / messages.

I would like to configure an LLM around that table,
 so I could ask data analysis questions like:

**What were the main problems encountered by the users during the month o
f November 2014 ?**

  
What would you recommend ? Having such a large amount of data makes this a little tricky for me.

```
---

     
 
all -  [ I built *useful* AI agents with perplexity search and knowledge access. (Here's how) ](https://www.reddit.com/r/LangChain/comments/1duaiwv/i_built_useful_ai_agents_with_perplexity_search/) , 2024-07-04-0910
```
Hey everyone,

AI agents are all around but they lack real-world exposure. Asking them can be kinda hit-or-miss.

I foun
d a way to make them way more useful. I built an AI agent with Perplexity search capabilities, and now it can look stuff
 up on the internet and has access to memory and knowledge. It can be used for research, financial analysis, recipe find
ing, emailing and so on.

The agent is built using Phidata (a framework to build agents with access to knowledge, memory
 and tools).  Here’s a quick guide on how to do it using Portkey's AI Gateway. Link- [https://git.new/Portkey-Phidata](h
ttps://git.new/Portkey-Phidata)

Let me know your thoughts on this

Cheers!
```
---

     
 
all -  [ Image generation models with crewai ? ](https://www.reddit.com/r/crewai/comments/1du981q/image_generation_models_with_crewai/) , 2024-07-04-0910
```
I am looking for some guidance to use image generation models from stability diffusion or titan model. I am getting the 
following error because the model doesn't seem to be called properly and I didn't find any example on the internet on a 
crewai agent using an image generation model. Anyone can help me make this work please

    File /opt/conda/lib/python3.
10/site-packages/langchain_community/llms/bedrock.py:655, in BedrockBase._prepare_input_and_invoke_stream(self, prompt, 
system, messages, stop, run_manager, **kwargs)
        652     response = self.client.invoke_model_with_response_stream(
**request_options)
        654 except Exception as e:
    --> 655     raise ValueError(f'Error raised by bedrock service
: {e}')
        657 for chunk in LLMInputOutputAdapter.prepare_output_stream(
        658     provider, response, stop, 
True if messages else False
        659 ):
        660     yield chunk
    
    ValueError: Error raised by bedrock serv
ice: An error occurred (ValidationException) when calling the InvokeModelWithResponseStream operation: Malformed input r
equest, please reformat your input and try again.

...   

```
---

     
 
all -  [ RAG system with excel sheets  ](https://www.reddit.com/r/LangChain/comments/1du8uem/rag_system_with_excel_sheets/) , 2024-07-04-0910
```
For about a month or more, I've been trying to build an RAG system and understand the tools used for a project, which in
volves dealing with Excel data. I've encountered issues with the standard method like split and embedding the data ,espe
cially when dealing with excel file containing multiple sheets or pages. After researching, I found a few solutions incl
uding Langchain Agent, but encountered errors when trying to use it. Any solutions, suggestions, or resources that could
 help me? Thank you.
```
---

     
 
all -  [ Cost monitoring for Langchain apps using AWS Bedrock with Langfuse ](https://www.reddit.com/r/LangChain/comments/1du8aue/cost_monitoring_for_langchain_apps_using_aws/) , 2024-07-04-0910
```
Hello everyone,

Here's a new post on how to add cost monitoring to all your Langchain apps that use AWS Bedrock using L
angfuse. This is actually what I'm using in production and I recommand it!

Here's the link: [link](https://www.metadocs
.co/2024/07/03/monitor-your-langchain-app-cost-using-bedrock-with-langfuse/).

Have a nice read!
```
---

     
 
all -  [ LangChain and supabase causing errors ](https://www.reddit.com/r/LangChain/comments/1du89s6/langchain_and_supabase_causing_errors/) , 2024-07-04-0910
```
Trying to make my first Chatbot using LLM,   
I have imported langchain and it came up with no troubles. used text-split
ter to check its functioning and everything. then i try to import supabase and get this error

https://preview.redd.it/s
nywi44f69ad1.png?width=609&format=png&auto=webp&s=f00bea359e7fb9c50cd4352711003ea7446903ff

  
Running npm audit gave me
 this:



https://preview.redd.it/t6trkrxi69ad1.png?width=895&format=png&auto=webp&s=2fa08df9f9de56820547f38b4d45d75533c
833ca



Solutions i have tried:  
- Cache clearing

- npm fix force 

- removing package.json/package-lock.json and rei
nstalling it 

- updating the packages( langchain, supabase)

  
Links to Codes:  
index.js: [https://codeshare.io/4YjjP
j](https://codeshare.io/4YjjPj)

package.json: [https://codeshare.io/ApQQvE](https://codeshare.io/ApQQvE)



FYI, i dont
 use ladash.set, langsmith anywhere for my chatbot.

Any Help is appreciated!  

```
---

     
 
all -  [ How are you maintaining existing access control permissions for a RAG LLM chatbot? ](https://www.reddit.com/r/LangChain/comments/1dtyunx/how_are_you_maintaining_existing_access_control/) , 2024-07-04-0910
```
We’re building an internal RAG LLM chatbot where the queries are augmented by a large volume of files we have in SharePo
int and some pages in Confluence. How would you maintain the existing RBAC of these files in the results from the chatbo
t when different employees are querying? Is there a tool that would allow the results to adhere to the existing permissi
ons of these data sources?
```
---

     
 
all -  [ Resume Chatbot ](https://www.reddit.com/r/LangChain/comments/1dtwsfv/resume_chatbot/) , 2024-07-04-0910
```
Hey Everyone, I made a Resume Chatbot, I'd Love for you'll to read my article linked below. Thank you!

https://medium.c
om/@aaronphilip2003/r%C3%A9sum%C3%A9-chatbot-abccc89de23b

```
---

     
 
all -  [ Understanding AI Hallucinations: What They Are and Why They Matter ](https://www.reddit.com/r/pythia/comments/1dtwfqy/understanding_ai_hallucinations_what_they_are_and/) , 2024-07-04-0910
```
Imagine this: You rely on an artificial intelligence (AI) assistant for a quick health check, and it misdiagnoses a mino
r rash as a life-threatening condition. Or, you skim through an article online, only to discover that AI fabricated it l
ater. While unsettling, these scenarios highlight a real challenge: AI hallucinations.

Large Language Models (LLMs) are
 a powerful type of AI that's rapidly changing how we interact with technology. They can generate creative text formats,
 like poems or code, and translate languages with impressive accuracy. LLMs are even being used in financial markets to 
automate trading strategies. However, it's important to remember that LLMs are still under development and can sometimes
 generate inaccurate or misleading information. 

As our dependence on AI grows, so do the potential consequences of unt
rustworthy AI. Fortunately, solutions are emerging to combat this challenge. [Wisecube's Pythia](https://askpythia.ai/bl
og/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinations) is a prime example, designed to ensure the reliabili
ty and trustworthiness of AI outputs. 

This blog post dives into AI hallucinations and explores how solutions like Pyth
ia can empower a future built on dependable AI. 

# What are AI Hallucinations?

Consider a seemingly helpful AI analyzi
ng a skin lesion. It might incorrectly diagnose a harmless mole as cancerous. This is an illustration of an AI hallucina
tion in medical care. In essence, AI hallucinations are outputs generated by AI systems that are factually incorrect, il
logical, or simply nonsensical.

LLMs are trained on vast datasets of text and code. While impressive in their ability t
o learn patterns and generate human-like text, this very strength can be a weakness. LLMs may identify patterns that are
n't there or struggle with incomplete information. To fill these gaps , they could develop subtleties or make misleading
 associations, prompting hallucinations.

This highlights the importance of AI hallucination detection, especially in he
althcare, where decisions can have significant consequences. This is just one example. AI hallucinations can manifest in
 various ways, including:

* **Factual Inconsistencies:** LLMs might weave together factual elements from different cont
exts, creating an internally inconsistent narrative.
* **Logical Fallacies:** AI outputs might contain faulty reasoning 
or illogical arguments, despite appearing superficially coherent.
* **Nonsensical Outputs:** In some cases, LLMs might g
enerate entirely nonsensical text that bears no resemblance to the intended task or input data.

# Why Do AI Hallucinati
ons Matter?

AI hallucinations are far from harmless. They pose [significant risks ](https://askpythia.ai/blog/navigatin
g-risks-associated-with-unreliable-ai-and-trustworthiness-in-llms)across various fields that rely on accurate informatio
n and sound judgment. For example, a financial advisor using an AI tool that hallucinates about future market trends, le
ading to disastrous investment decisions. In the healthcare domain, [a medical diagnosis tool fed by inaccurate data cou
ld recommend the wrong treatment for a patient](https://www.wisecube.ai/blog/battling-llm-hallucinations-in-biomedicine-
the-role-of-knowledge-graphs-in-knowledge-injection-techniques/). The potential consequences of AI hallucinations are pa
rticularly worrisome in these high-stakes fields, including:

* **Finance:** AI-powered trading algorithms misled by hal
lucinations could cause significant financial losses for individuals and institutions.
* **Healthcare:** Misdiagnosis or
 improper treatment recommendations based on inaccurate AI outputs could have severe health consequences for patients.
*
 **Legal:** AI-driven legal research tools that fabricate information could lead to flawed legal arguments and miscarria
ges of justice.

Beyond these immediate risks, AI hallucinations can also erode public trust in AI technology as a whole
. When people encounter demonstrably false information generated by AI, they become more hesitant to rely on AI systems.
 

# The Impact of AI Hallucinations in Biomedicine

In the domain of biomedicine, AI hallucinations pose a significant 
threat. These hallucinations, where AI generates incorrect or misleading information, can have devastating consequences.
 They could lead to wasted research efforts, delayed breakthroughs, or even the development of unsafe medical treatments
.  Here's how they can negatively impact healthcare organizations and research institutions:

* **Misdiagnosis and Mistr
eatment:** AI-powered diagnostic tools misinterpreting medical scans or patient data could delay or prevent fitting trea
tment, endangering patient outcomes. 
* **Wasted Resources and Delayed Research:** Biomedical research heavily relies on
 accurate data analysis. AI hallucinations in research tools can lead to wasted resources and time spent pursuing false 
leads or ineffective treatment pathways based on fabricated information.
* **Loss of Patient Trust and Reputational Dama
ge:** When patients discover their diagnoses or treatment plans were influenced by AI errors, it can erode trust in the 
healthcare system and damage the reputation of institutions relying on such technology.
* **Legal Issues and Regulatory 
Challenges:** Biomedical AI with flawed outputs could lead to regulatory non-compliance or even legal repercussions if i
naccurate diagnoses or treatment decisions cause harm to patients.

The potential financial impact of AI hallucinations 
is also significant. Misdiagnoses and improper treatments can increase healthcare costs, while lawsuits arising from AI 
errors could result in hefty settlements.

Biomedical foundations can ensure patient well-being and advance medical prog
ress by prioritizing the development of reliable AI systems. This focus on dependable simulated intelligence solutions d
irectly addresses the threat of AI hallucinations, leading to more trustworthy AI-powered healthcare. 

# The Importance
 of AI Hallucination Detection in Biomedicine

Because AI can deliver results in biomedicine that could significantly im
pact a person's health, the development of reliable methods to identify AI hallucinations becomes a critical safeguard. 


A reliable AI hallucination detection system would recognize inconsistencies and alert researchers for further investi
gation. This crucial intervention could prevent the development of a harmful drug combination and potentially save a lif
e. In essence, reliable AI hallucination detection, facilitated by tools like Wisecube's Pythia, acts as a safety net wi
thin the biomedical research process. Let's explore how this safeguards the development of life-saving treatments.  

* 
**Enhanced Patient Safety:** AI hallucination detection directly contributes to improved patient care. Identifying and f
iltering out unreliable AI outputs allows for early detection of potential errors in diagnosis or treatment plans. This 
enables medical experts to mediate and guarantee patients get the absolute most exact consideration.
* **Boosted Researc
h Efficiency:** In the fast-paced world of biomedical research, robust data analysis is crucial. AI hallucination detect
ion helps scientists avoid wasting valuable time and resources pursuing false leads or ineffective treatment pathways du
e to AI errors.
* **Reliable Results:** Detection tools ensure data integrity in AI-driven research and clinical trials.
 This fosters trust in the overall research process and the validity of the results obtained using artificial intelligen
ce.
* **Building Trustworthy AI in Healthcare:** By mitigating the risk of AI errors, AI hallucination detection enables
 healthcare professionals to have a higher level of trust in AI-generated insights. This allows them to make more inform
ed decisions about diagnosis, care, and treatment approaches. 

Ensuring the reliability of AI outputs through robust hu
man oversight is key to unlocking a future where AI becomes a trusted partner in healthcare and biomedical research. Wis
ecube's Pythia exemplifies this approach. Reliable AI allows us to move beyond simply analyzing data to tackling proacti
ve tasks like predicting disease outbreaks, forecasting patient outcomes, and even personalizing drug treatments.  

# I
ntroducing Pythia: The AI Hallucination Firewall

Wisecube's Pythia is a powerful tool designed to combat AI hallucinati
ons, a significant challenge in the biomedical field. It goes beyond basic anomaly detection to provide a comprehensive 
AI hallucination identification and mitigation system. This means Pythia can not only identify potentially misleading AI
 outputs but also help researchers understand and address them.   

Here's how Pythia safeguards against unreliable AI o
utputs:

* **Knowledge-Based Verification:** Pythia tackles AI hallucinations by leveraging a powerful technique called 
[knowledge triplets](https://www.wisecube.ai/blog/the-wisecube-approach-to-enhancing-ai-reliability/). These triplets ca
pture factual relationships between entities, acting as building blocks for comparisons. When an LLM generates an output
, Pythia extracts claims as knowledge triplets from both the output and Wisecube's knowledge graph (or a custom dataset 
you provide). By comparing these triplets, Pythia can identify inconsistencies or factual impossibilities that flag pote
ntial hallucinations in the LLM's output. 
* **Multi-Layered Analysis:** Pythia's analysis goes beyond just checking a k
nowledge graph. It employs a multifaceted approach involving claim extraction and categorization. First, Pythia meticulo
usly extracts specific factual assertions from the LLM output. These claims are then compared against scientific databas
es and medical literature. By analyzing the alignment, Pythia categorizes them as Entailment, Contradiction, Neutral, or
 Missing Facts. Finally, it generates a report highlighting inconsistencies and areas requiring human review. This multi
-layered analysis ensures a higher level of trust in LLM outputs. 
* **Seamless Integration:** Pythia integrates seamles
sly within existing LLM workflows, acting as a real-time safety net. This ensures continuous monitoring and immediate fl
agging of potential hallucinations without disrupting ongoing AI processes.

By deploying Pythia, biomedical institution
s gain a multitude of advantages:

* **Advanced Hallucination Detection:** Pythia's multi-layered approach surpasses bas
ic anomaly detection, offering a robust and reliable solution for identifying even subtle AI hallucinations.
* **Privacy
 Protection:** It uses input/ output validators to examine artificial intelligence yields while never expecting admittan
ce to delicate patient information. This ensures patient confidentiality remains protected throughout the process. 
* **
Enhanced Trust:** Pythia fosters trust in AI-driven research and clinical decision-making by mitigating the risk of erro
rs and ensuring the reliability of AI outputs.
* **Customizable Detection:** Pythia allows for customizing detection par
ameters to cater to the specific needs of different research areas and applications within biomedicine.
* [**LangChain I
ntegration**](https://askpythia.ai/blog/a-guide-to-integrating-the-pythia-api-using-wisecube-python-sdk)**:** Pythia sea
mlessly integrates with the LangChain ecosystem, a unified environment for building and deploying trustworthy AI solutio
ns in healthcare.
* **Real-Time Analysis:** Pythia's real-time analysis capabilities enable immediate identification and
 flagging of potential hallucinations, allowing for swift intervention and course correction.

Pythia enables the biomed
ical field to tackle the maximum capacity of simulated intelligence while defending against hallucinations. With its adv
anced detection methods, seamless integration, and commitment to data privacy, Pythia paves the way for a new era of dep
endable AI in biomedicine. 

[Get started](https://askpythia.ai/#get-started) today to develop reliable LLMs with Pythia
 and embark on your journey towards trustworthy AI-powered healthcare. 

  
*The article was originally published on* [*
Pythia's website.*](https://askpythia.ai/)


```
---

     
 
all -  [ Is it possible to use LangGraph to orchestrate LangChain chains? ](https://www.reddit.com/r/LangChain/comments/1dtw8rr/is_it_possible_to_use_langgraph_to_orchestrate/) , 2024-07-04-0910
```
Suppose I use langchain’s ChatOpenAI as a model, ChatPromptTemplate to build a prompt and build myself a chain like that
:

chain = prompt | model

I’m trying to use LangGraph along with it’s memory capabilities to orchestrate chains built l
ike these. Is this the right way? Or should I be starting to build the chain with langgraph?

Looks like my chain has so
me kind of amnesia between messages.






```
---

     
 
all -  [ Langchain async for document loader and character splitter ](https://www.reddit.com/r/LangChain/comments/1dtvnw0/langchain_async_for_document_loader_and_character/) , 2024-07-04-0910
```
Should I use Async or not? 

I am building a Fast api RAG app that uses LLMs to generate responses using langchain but I
 am confused if it needs async. 

The user flow goes something like this:
1. User provides a link/ links to a text/pdf d
ocument in the form of a url.  
2. Langchain document loaders are used to load text or pdf from the remote public url.
3
. Character splitter is used to split and chunk the documents which is saved into a vector db. 
4. Langchain chain libra
ry is used to invoke LLMs via the asynchronous ainvoke(). 

My question is whether the document loading step via langcha
in and character splitting text via langchain  would need to be made async? Langchain doesn’t support async for the libr
aries I am using. Would I need to implement them myself? If so, what are some options to implement? 
```
---

     
 
all -  [ Should I use Async or not?  ](https://www.reddit.com/r/learnpython/comments/1dtvk3n/should_i_use_async_or_not/) , 2024-07-04-0910
```
I am building a Fast api RAG app that uses LLMs to generate responses using langchain but I am confused if it needs asyn
c. 

The user flow goes something like this:
1. User provides a link/ links to a text/pdf document in the form of a url.
  
2. Langchain document loaders are used to load text or pdf from the remote public url.
3. Character splitter is used 
to split and chunk the documents which is saved into a vector db. 
4. Langchain chain library is used to invoke LLMs via
 the asynchronous ainvoke(). 

My question is whether the document loading step via langchain and character splitting te
xt via langchain  would need to be made async? Langchain doesn’t support async for the libraries I am using. Would I nee
d to implement them myself? If so, what are some options to implement? 
```
---

     
 
all -  [ How do I upload a file and display the output in the langserve playground? ](https://www.reddit.com/r/LangChain/comments/1dtugcl/how_do_i_upload_a_file_and_display_the_output_in/) , 2024-07-04-0910
```
Hello everyone, I need your help with my project. I have two problems:  
1 - I'd like the user to be able to upload a cs
v file directly instead of putting the route to the file   
2 - I don't know why, but in csv/playground/, there's no out
put displayed  
I'm trying to make an askyourcsv project but in this project, the user has to set the file path instead 
of uploading the file. What can I do to enable the user to upload the file and how can I improve my code? And what's wro
ng with the code so that the output isn't displayed in the playground?

    #chain.py
    def loaddata(filepath: str) ->
 List[Document]:
        loader = CSVLoader(filepath=filepath)
        documents = loader.load()
        return document
s
    
    class QuestionRequest(BaseModel):
        file_path: str
        question: str
    
    class Rag_chain(Runna
ble):
        def invoke(self, input: Any, config: Dict[str, Any] = None) :
    
            if isinstance(input, dict):

                input = QuestionRequest(**input)
            question = input.question
            file_path = input.fi
le_path
            data = load_data(file_path)
    
            text_splitter = RecursiveCharacterTextSplitter(chunk_si
ze=1000, chunk_overlap=200)
            documents = text_splitter.split_documents(data)
    
            vectorstore = C
hroma.from_documents(
                documents,
                embedding=OpenAIEmbeddings(model='text-embedding-ada-00
2'),
            )
    
            retriever = RunnableLambda(vectorstore.similarity_search).bind(k=5)
    
           
 llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.6)
    
            template = '''Answer the question based only 
on the following context:
            {context}
    
            Question: {question}
            '''
            prompt
 = ChatPromptTemplate.from_template(template)
            chain = (
                # Extract the question text from the
 QuestionRequest object
                RunnableParallel({'context': retriever, 'question': RunnablePassthrough()})
    
            | prompt
                | llm
                | StrOutputParser()
            )
    
            response =
 chain.invoke(question)
            return response
    '''
    '''
    #server.py
    app = FastAPI()
    chain_instanc
e = Rag_chain()
    
    add_routes(app,
               chain_instance,
               path='/csv',
               input
_type=QuestionRequest)
    
    if __name == '__main':
        import uvicorn
        uvicorn.run(app, host='0.0.0.0', p
ort=8000)
    '''
```
---

     
 
all -  [ Verify ChatGPT Statement Truth Using Anthropic Claude Model ](https://www.reddit.com/r/LangChain/comments/1dtuell/verify_chatgpt_statement_truth_using_anthropic/) , 2024-07-04-0910
```
[https://youtu.be/18zTQv25qlk](https://youtu.be/18zTQv25qlk)

I built this in like 5 minutes using [https://visualagents
.ai](https://visualagents.ai) fully event driven data flow RAG graph built on top of js.langchain.

https://preview.redd
.it/qcp1brqap5ad1.png?width=1920&format=png&auto=webp&s=abae1244e70defe0c1301286cbdd5dfddc8ef8d2


```
---

     
 
all -  [ Roast Beno - Find Clients with AI-Powered Replies in Relevant Discussions Automatically ](https://www.reddit.com/r/Entrepreneur/comments/1dtt4uv/roast_beno_find_clients_with_aipowered_replies_in/) , 2024-07-04-0910
```
Roast my project - Find Clients with AI-Powered Replies in Relevant Discussions Automatically

Hi, community! I’ve creat
e a Beno, it tracks relevant conversations and mentions your business in a natural, human-like way.

While developing Be
no and talking to other founders, I was inspired by their excitement and the 'take my money' attitude. Now that we're la
unching Beno, I realize how important feedback is to make the product even better.

Imagine a small company with two emp
loyees who spend all their time monitoring online platforms, jumping into relevant discussions to organically mention th
e company and attract new clients. Or a startup with no marketing budget and limited resources, struggling to find clien
ts.

Now, imagine a tool, Beno, that does exactly what those employees do. It automatically finds relevant discussions o
nline and uses AI to craft human-like replies mentioning your product.

Just to be clear, all comments are posted by our
 team manually. We’ve optimized the process of finding and crafting these replies, making sure we follow platform rules 
and deliver great results.


Target Audience

Originally, I thought most of our users would be B2C, but after talking to
 many founders, it turns out most are B2B. The main things they have in common are:

- Small businesses, mostly indie fo
unders.
- They may do it manually now and want to automate this process.
- They may have developed their product and are
 now focusing on client acquisition.
- They are looking for client acquisition at a lower cost than other methods like t
argeting and influencer marketing.
- They appreciate the easy and fast setup process.


Current Stage
We have built a pr
oduct and are now in beta.


Customer Conversion Strategy
Most of our users come from our cold emails.

Why Me?
We start
ed as a small team with no marketing budget, manually replying to Reddit discussions to find clients for other products 
we were working on. So we decided to automate it and build Beno. We have some results to share based on our products tha
t we used Beno for: on Reddit, one of our products reached 700,000 people in a week—all automated, no manual effort. You
 can set up in just 5 minutes and spend only $50, instead of $1800 a month on manual labor.

Tech Stack
Svelte for the f
rontend, Pocketbase for the backend, and Python for AI processes. We use a complicated LLM pipeline with ChatGPT and Gro
q, and we do not use Langchain.

Website: beno(.)one


Roast my project and help me to create my first successful compan
y. Any feedback or questions are welcome
```
---

     
 
all -  [ Agent RAG (Parallel Quotes) - How we built RAG on 10,000's of docs with extremely high accuracy ](https://www.reddit.com/r/LangChain/comments/1dtr49t/agent_rag_parallel_quotes_how_we_built_rag_on/) , 2024-07-04-0910
```
Edit - for some reason the prompts weren't showing up. Added them.

Hey all -

Today I want to walk through how we've be
en able to get extremely high accuracy recall on thousands of documents by taking advantage of splitting retrieval into 
an 'Agent' approach.

**Why?**

As we built RAG, we continued to notice hallucinations or incorrect answers. we realized
 three key issues:

1. There wasn't enough data in the vector to provide a coherent answer. i.e. vector was 2 sentences,
 but the answer was the entire paragraph or multiple paragraphs.
2. LLM's try to merge an answer from multiple different
 vectors which made an answer that looked right but wasn't.
3. End users couldn't figure out where the doc came from and
 if it was accurate.

We solved this problem by doing the following:

* Figure out document layout ([we posted about it 
a few days ago.](https://www.reddit.com/r/LangChain/comments/1dpbc4g/how_we_chunk_turning_pdfs_into_hierarchical/)) This
 will make issue one much less common.
* Split each 'chunk' into separate prompts (Agent approach) to find exact quotes 
that may be important to answering the question. This fixes issue 2.
* Ask the LLM to only give direct quotes with refer
ences to the document it came from, both in step one and step two of the LLM answer generation. This solves issue 3.

**
What does it look like?**

https://preview.redd.it/otf9dbau05ad1.png?width=1625&format=png&auto=webp&s=72a7fe9349a9499a3
2ff5f6b6a245623e1d91102

We found these improvements, along with our prompt give us extremely high retrieval even on com
plex questions, or large corpuses of data.

**Why do we believe it works so well?** - LLM's still seem better to deal wi
th a single task at a time, and LLM's still struggle with large token counts on random data glued together with a prompt
 (i.e. a ton of random chunks). Because we are only providing a single Chunk, or relevant information, we found huge imp
rovements in recall and accuracy.

**Workflow:**

https://preview.redd.it/8aso1i7y05ad1.png?width=1109&format=png&auto=w
ebp&s=e115ee50b70fbf790e78af365ce96f7d2e16a020

**Step by step with example on above workflow**

1. **Query:** What are 
the recent advancements in self-supervised object detection technique
2. **Reconstruct document.** (highlighted would be
 the vector that came back) Then we'd reconstruct the doc until we get to a header.

https://preview.redd.it/ztj8q1f415a
d1.png?width=1122&format=png&auto=webp&s=ab3805273bf3320d7478c3619c3c0df8dcdc98d9

3. Input the reconstructed document c
hunk into the LLM. **(Parallel Quotes)**

**Prompt #1:**

**\_\_\_\_\_\_\_**

You are an expert research assistant. Here
 is a document you will find relevant quotes to the question asked:

  <doc>

  ${chunk}

  </doc>

Find the quotes from
 the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be 
relatively short.

The format of your overall response should look like what's shown below. Make sure to follow the form
atting and spacing exactly.

  Example:

  \[1\] 'Company X reported revenue of $12 million in 2021.'

  \[2\] 'Almost 9
0% of revenue came from widget sales, with gadget sales making up the remaining 10%.'

  Do not write anything that's no
t a quote direct quote.

  If there are no quotes, please only print, 'N/a'

**\_\_\_\_\_\_\_**

4. **Response** from th
e LLM:

\[1.0\]'Recent advancements have seen the development of end-to-end self-supervised object detection models like
 UP-DETR and DETReg, as well as backbone pre-training strategies such as Self-EMD and Odin .'

\[1.1\] 'Despite the rema
rkable success of supervised object detection techniques such as Mask RCNN , Yolo , Retinanet , and DETR , their self-su
pervised alternatives have been somewhat limited in scope until recently.

Notes:

I deleted the internal references to 
make it less confusing

If there's more than 1 doc/chunk we start each new one with a new number i.e. \[2.0\] which make
s it easier to find which quote relates to which doc.

We put the query in the user prompt and the above in the system p
rompt

5. Give the LLM that will be generating the answer the **document name & quotes**.

**Prompt #2:**

**\_\_\_\_\_\
_\_**

All quotes are relevant to the question, please use them to answer the question:

When answering questions:

1. M
ake references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of r
elevant sentences.
2.   Feel free to shorten quotes or merge quotes together as long as you reference them.
3.   Focus o
n making short, readable answers.
4.   Bold headers, bold general topics, bullet point, list, etc. if needed to make it 
easier to read.



DocName: UnSupDLA: Towards Unsupervised Document Layout Analysis

Quotes:

\[1.0\]'Recent advancement
s have seen the development of end-to-end self-supervised object detection models like UP-DETR and DETReg, as well as ba
ckbone pre-training strategies such as Self-EMD and Odin .'

\[1.1\] 'Despite the remarkable success of supervised objec
t detection techniques such as Mask RCNN , Yolo , Retinanet , and DETR , their self-supervised alternatives have been so
mewhat limited in scope until recently.'

DocName: 'doc2'

Quotes:

\[2.0\]'example quote2'

\[2.1\]'example'

If there 
isn't information to answer this question, please write:

I'm sorry, but there is no documentation available.

\_\_\_\_\
_\_\_\_

6. Final LLM **Response**:

**End-to-End Self-Supervised Models**

* **UP-DETR**: This model is a recent develo
pment in self-supervised object detection, aiming to enhance detection capabilities without relying on labeled data \[1.
0\].
* **DETReg**: Another advanced model, DETReg, also focuses on self-supervised object detection, providing improveme
nts in training and detection accuracy without requiring extensive labeled datasets \[1.0\].

**Backbone Pre-Training St
rategies**

* **Self-EMD**: This strategy is utilized to pre-train the backbone of detection models, helping in learning
 robust representations from unlabeled data \[1.0\].
* **Odin**: Similar to Self-EMD, Odin is a pre-training strategy th
at enhances the performance of detection models through self-supervised learning techniques \[1.0\].

**Comparison with 
Supervised Techniques**

**Scope and Limitations**: Despite the success of supervised techniques like Mask RCNN, Yolo, R
etinanet, and DETR, their self-supervised alternatives have only recently started to expand in scope and effectiveness \
[1.1\].

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Real world examples of where this comes i
nto use:**

* A lot of internal company documents are made with human workflows in mind only. For example, often see a d
ocument named 'integrations' or 'partners' and then just a list of 500 companies they integrate/partner with. If a vecto
r came back from within that document, the LLM would not be able to know it was regarding integrations or partnership be
cause it's only the document name.
* Some documents will talk about the product, idea, or topic in the header. Then not 
discuss it by that name again. Meaning if you only get the relevant chunk back, you will not know which product it's ref
erencing.

Based on our experience with internal documents, about 15% of queries fall into one of the above scenarios.


Notes - Yes, we plan on open sourcing this at some point but don't currently have the bandwidth (we built it as a produc
tion product first so we have to rip out some things before doing so)

Happy to answer any questions!

**Video:**

https
://reddit.com/link/1dtr49t/video/o196uuch15ad1/player
```
---

     
 
all -  [ Building Dynamic RAG Apps with LangChain + Pathway ](https://www.reddit.com/r/learnmachinelearning/comments/1dtpglu/building_dynamic_rag_apps_with_langchain_pathway/) , 2024-07-04-0910
```
Hi r/learnmachinelearning  
  
Here’s a straightforward approach to build Dynamic RAG Apps using LangChain.   
  
LangCh
ain is a widely used framework for RAG (Retrieval-Augmented Generation) applications, but changes in data sources can pr
esent significant challenges. As data evolves, ETL (Extract, Transform, Load) pipelines often become complex and difficu
lt to maintain, making it hard to keep applications up-to-date.  
  
Using Pathway with LangChain provides a solution to
 this problem by ensuring that applications always provide up-to-date knowledge. Key benefits of Pathway’s incremental u
pdates include:

* Easy monitoring of data source changes (insertions, deletions, changes)
* Instant syncing of RAG apps
 with these changes
* Simplified ETL adjustments from the beginning

By using this app template within Colab, you can st
reamline your RAG solutions and make them more efficient for production environments. Pathway is also available natively
 as a vector store within the LangChain ecosystem, offering additional integration options.   
  
Learn how to get start
ed with a dynamic RAG app in Google Colab using your own data in minutes: [https://pathway.com/developers/templates/lang
chain-integration](https://pathway.com/developers/templates/langchain-integration)
```
---

     
 
all -  [ App Template to build Dynamic RAG Apps with Langchain and Pathway ](https://www.reddit.com/r/datascienceproject/comments/1dtpccn/app_template_to_build_dynamic_rag_apps_with/) , 2024-07-04-0910
```
Hey r/datascienceproject, here's an App Template to build Dynamic RAG projects within Colab in minutes: [https://pathway
.com/developers/templates/langchain-integration](https://pathway.com/developers/templates/langchain-integration)

LangCh
ain is a popular framework for working on RAG applications. However, as changes occur in data sources, developers often 
face significant challenges. ETL pipelines can become messy, and keeping up with these changes can be a headache. Using 
Pathway with LangChain solves this problem by ensuring your applications always provide up-to-date knowledge. With this 
you get incremental indexing pipelines to:

* Easily monitor several data sources for any data changes (insertions/delet
ions/changes)
* Instantly sync your RAG apps 
* Avoid complex ETL adjustments from Day 1 

You can try this app template
 within Google Colab and streamline your RAG solutions for production. Pathway is also available natively as a vector st
ore within the LangChain ecosystem.
```
---

     
 
all -  [ LangSmith: configuring HF pipeline to display output as Chat? ](https://www.reddit.com/r/LangChain/comments/1dtnri2/langsmith_configuring_hf_pipeline_to_display/) , 2024-07-04-0910
```
I might be overlooking something quite simple but I'm trying to follow the RAG from Scratch tutorial by Lance Martin but
 by using a local LLM (Mistral 7B Instruct v0.3). The Runnable Sequence has a HuggingFacePipeline section which has a 'P
rompt & Completion' header and has the entire prompt, context and query, then the answer. The answer itself has the prom
pt, context, query and answer embedded within it:

```
...

metadata={'source': 'https://lilianweng.github.io/posts/2023
-06-23-agent/'})\]   
Answer: \[/INST\]  
  
<s> \[INST\] You are an assistant for question-answering tasks. Use the fol
lowing pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. U
se three sentences maximum and keep the answer concise. \[/INST\] </s> 

... 

  
'https://lilianweng.github.io/posts/20
23-06-23-agent/'})\]   
Answer: \[/INST\]  
Task Decomposition is a method used in autonomous agent systems where a comp
lex task is broken down into smaller, manageable steps. This is often achieved by instructing a Language Model (LLM) to 
'think step by step' or by using specific instructions tailored to the task at hand. For example, it could involve askin
g 'What are the subgoals for achieving XYZ?' or 'Steps for XYZ.' The goal is to simplify complex tasks and provide insig
hts into the model's thought process.
```

Instead, his -- using OpenAI -- has a proper chat with input and output heade
rs that are easily readable. Is there something straightforward I can change to get the same output on LangSmith?

My ra
g chain looks like this:

```
# Prompt
prompt = hub.pull('rlm/rag-prompt-mistral')

# Chain
rag_chain = (
    {'context'
: retriever, 'question': RunnablePassthrough()}
    | prompt
    | mistral_llm
    | StrOutputParser()
)

# Question
res
ponse = rag_chain.invoke('What is Task Decomposition?')
```
```
---

     
 
all -  [ Deep Reinforcement Learning ](https://www.reddit.com/r/LangChain/comments/1dtly3h/deep_reinforcement_learning/) , 2024-07-04-0910
```
Published in ICML 2024

Paper: [https://huggingface.co/papers/2406.16979](https://huggingface.co/papers/2406.16979)
```
---

     
 
all -  [ Resume Review ](https://www.reddit.com/r/resumes/comments/1dtlsp2/resume_review/) , 2024-07-04-0910
```
https://preview.redd.it/86m8k2v6x3ad1.png?width=625&format=png&auto=webp&s=57af9a65365355468d51709733c9e5385743a1e4

  

  
  
Hi, Im a student graduating next year with a CS degree. I am looking for entry jobs in AI/ML or any SDE roles.   

Im having trouble getting shortlisted. I feel like my resume lacks something but i cant pinpoint what...
```
---

     
 
all -  [ LangChain vs LlamaIndex vs txtai for vector search ](https://www.reddit.com/r/LocalLLaMA/comments/1dtlfex/langchain_vs_llamaindex_vs_txtai_for_vector_search/) , 2024-07-04-0910
```
https://preview.redd.it/d6fg0ixet3ad1.png?width=1613&format=png&auto=webp&s=8f45839401fe3818c6a7b781339d6e32c7ff994a

ht
tps://preview.redd.it/k26mczuft3ad1.png?width=1535&format=png&auto=webp&s=a9e79f8d111eae6c76fcc48bc0ba644af2f265ce

The 
comparison above shows the differences between the 3 libraries for building a vector search application backed by Faiss.


Faiss is a great vector indexing library. It has so many features past just a flat index. txtai automatically creates 
a performant Faiss index scaled by the size of the incoming data. The index type can also be fully customized with confi
guration.

[txtai](https://github.com/neuml/txtai) vector indexes use SQLite + Faiss by default. This enables search wit
h SQL and dynamic columns. Results are standard Python dictionaries and that allows direct integration with Pandas/Polar
s DataFrames.

This comparison demonstrates the power of a deep and meaningful integration vs supporting as many vector 
stores as possible (i.e. box checking).

Case in point, [LlamaIndex supports txtai](https://docs.llamaindex.ai/en/stable
/api_reference/storage/vector_store/txtai/) but it really doesn't integrate it the way it was intended.

Links to code:


[https://gist.github.com/davidmezzetti/e91a648732a4935cd551b06e9c8aaed7](https://gist.github.com/davidmezzetti/e91a6487
32a4935cd551b06e9c8aaed7)  
[https://gist.github.com/davidmezzetti/43a60af6e135a031c0bfb4de02bc11f4](https://gist.github
.com/davidmezzetti/43a60af6e135a031c0bfb4de02bc11f4)
```
---

     
 
all -  [ node-edge based GUI editor for LangGraph ](https://www.reddit.com/r/LangChain/comments/1dtklxf/nodeedge_based_gui_editor_for_langgraph/) , 2024-07-04-0910
```
I’m excited to share that I’ve created a node-edge based GUI editor for LangGraph!

https://preview.redd.it/1uf35sfym3ad
1.jpg?width=1850&format=pjpg&auto=webp&s=59f0728b3381b8a68d83f27137075587f13bb033

This tool provides an intuitive inter
face for creating and managing workflows, making it easier than ever to visualize and execute tasks. Whether you're work
ing with complex workflows or just getting started, LangGraph-GUI simplifies the process.

Check it out here: [LangGraph
-GUI on GitHub](https://github.com/LangGraph-GUI/LangGraph-GUI)

Some key features include:

* **User-Friendly Interface
:** Easily create and edit workflows with a visual editor.
* **Seamless Integration:** Supports local execution with lan
guage models like Mistral.
* **JSON Support:** Read and write JSON files for your workflows, ensuring compatibility and 
easy sharing.

To get started, follow the setup instructions in the repository. I’ve also included a guide on how to bui
ld the front-end GUI into a standalone executable.

If you want to learn LangGraph, we have LangGraph for dummy learning
: [LangGraph-learn](https://github.com/LangGraph-GUI/LangGraph-learn)

I’d love to hear your feedback and see how you’re
 using LangGraph-GUI in your projects. Feel free to contribute or raise issues on GitHub.

Happy graphing!
```
---

     
 
all -  [ Python vs Javascript for langchain ](https://www.reddit.com/r/LangChain/comments/1dtjqwi/python_vs_javascript_for_langchain/) , 2024-07-04-0910
```
I'm currently in the process of making a web app using next.js and I want to use LangChain on the backend. It would be m
uch simpler for me to use Javascript. I'm wondering if it's functionality lacking compared to the python sdk.
```
---

     
 
all -  [ Adding observability to Langchain based AI agents with just 3 lines of code ](https://www.reddit.com/r/Langchaindev/comments/1dtjmm9/adding_observability_to_langchain_based_ai_agents/) , 2024-07-04-0910
```
Hey folks,

I've been building AI assistants using Phidata which uses Langchain Knowledge Base. I needed better observab
ility for my assistants to track metrics such as costs, response latency, caching, etc.

To solve these issues I integra
ted Portkey with Phidata. I decided to create a simple cookbook. It integrates Phidata seamlessly with Portkey's AI gate
way in 3 lines of code, giving me clear insights into how my assistants perform.

Here's the link to the Google Collab n
otebook- [https://git.new/Phidata-Portkey](https://git.new/Phidata-Portkey)

Let me know what you think or if you have a
ny tips to improve!

Cheers!
```
---

     
 
all -  [ How I built observability for my AI assistant ](https://www.reddit.com/r/LangChain/comments/1dtjipf/how_i_built_observability_for_my_ai_assistant/) , 2024-07-04-0910
```
Hey folks,

I've been building AI assistants using Phidata which uses Langchain Knowledge Base. I needed better observab
ility for my assistants to track metrics such as costs, response latency, caching, etc.

To solve these issues I integra
ted Portkey with Phidata. I decided to create a simple cookbook. It integrates Phidata seamlessly with Portkey's AI gate
way in 3 lines of code, giving me clear insights into how my assistants perform.

Here's the link to the google collab n
otebook- [https://git.new/Phidata-Portkey](https://git.new/Phidata-Portkey)

Let me know what you think or if you have a
ny tips to improve!

Cheers!
```
---

     
 
all -  [ Text-to-sql system using LLM ](https://www.reddit.com/r/LangChain/comments/1dtjafd/texttosql_system_using_llm/) , 2024-07-04-0910
```
I am currently working on a project that involves developing a text-to-SQL system. The goal is to allow users to input n
atural language, and the system will generate SQL queries. I have reference documents (PDFs) containing SQL queries and 
their descriptions (of schemas as well). I am considering using a Retrieval-Augmented Generation (RAG) system for this t
ask. The idea is to use the provided documents to help generate the SQL queries. However, I am unsure if this is the bes
t approach. Alternatively, I am thinking about fine-tuning a model specifically for this purpose.  Also, is sqlcoder2-7b
 the sql code generator out there?

I would greatly appreciate guidance on the following:

* Is the RAG system the best 
solution for this problem?
* Would fine-tuning a model be more effective for generating accurate SQL queries?
* Is there
 a better approach that I should consider?

All your insights and suggestions will be invaluable in helping me determine
 the best course of action for this project. Thank you
```
---

     
 
all -  [ Aspiring AI Engineer ](https://www.reddit.com/r/LangChain/comments/1dtio2u/aspiring_ai_engineer/) , 2024-07-04-0910
```
Can you suggest some good projects to build and good open source repo to contribute for getting AI Engineer Job. I am fr
esher and I have 1 year to build my portfolio
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-04-0910
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-04-0910
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-04-0910
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-04-0910
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-07-04-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
