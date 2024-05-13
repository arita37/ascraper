 
all -  [ Need starter tips for designing a multi-agent system without relying on external LLM frameworks ](https://www.reddit.com/r/OpenAI/comments/1cqlkjm/need_starter_tips_for_designing_a_multiagent/) , 2024-05-13-0910
```
Hi everyone,   
I've played with some external frameworks like Langchain and Llamaindex, and a bit of bare OpenAI's func
tion calling. While llamaindex etc are good for fast prototyping, I feel like OpenAI and a bit of Python programming fro
m my end gives me more control over what I'm doing. I understand that you can switch language models in these frameworks
 but from what I've seen GPT4 text and vision have given me promising results on what I want to do. I need some help in 
setting up communication between agents to achieve a particular objective. Here's a very 'simple' task/setup.

Image\_Pr
ocessing\_Agent -> has access to tools that use computer vision models

Text\_processing\_agent -> has access to tools t
hat use NLP models. 

A user inputs a search query like 'Describe the red cars in this image.' The query should be passe
d to a router type object which should trigger the image agent. The image agent should run its object detection algorith
m to detect cars (and red cars). The text agent should take input from the image agent and 'summarize' them (whatever th
at means). 

This is probably a very simple use-case. But I want to extend it to things like reading financial reports, 
medical images and other cool things. 

Your help will be really appreciated.




```
---

     
 
all -  [ Artificial Intelligence (AI) Chatbot | Pytorch, Langchain ](https://www.reddit.com/r/ProgrammingBuddies/comments/1cqlber/artificial_intelligence_ai_chatbot_pytorch/) , 2024-05-13-0910
```
I'm working on making a private, local chatbot for local data and would like others to speak with who are also doing so.

```
---

     
 
all -  [ Looking for advice on how to improve my rag pipeline ](https://www.reddit.com/r/RagAI/comments/1cqhyrf/looking_for_advice_on_how_to_improve_my_rag/) , 2024-05-13-0910
```
Hello ,   
I've been trying to develop a rag pipeline for the past month and Here's my current setup : 

I'm using Azure
 AI Search to store documents and text-embedding-ada-002 for creating the vector embeddings. I'm using Langchain (retrie
val\_chain) to actually retrieve the documents , doing some prompt engineering and generating the answer.   
I'm now at 
the stage where I have some feedback on some of the answers like the following :   
'I like this answer but it would be 
better to be precise about the date here .. ' 

'Can we use UK spelling instead here ? '

'This is false , it should onl
y mention XXX'   
I'm trying to use Langchain few shot prompting to correct these but is this the best way to go about i
t ? 

Thanks !   

```
---

     
 
all -  [ Langchain calling incorrect OpenAI API for GPT 3.5 turbo ](https://www.reddit.com/r/LangChain/comments/1cqhs7x/langchain_calling_incorrect_openai_api_for_gpt_35/) , 2024-05-13-0910
```
I am using GPT 3.5 turbo model in my program via below statement but still getting 'not a chat model' error, can someone
 please help me fix it?

    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model='gpt-3.5-turbo')

  
Err
or:

`NotFoundError: Error code: 404 - {'error': {'message': 'This is not a chat model and thus not supported in the v1/
chat/completions endpoint. Did you mean to use v1/completions?', 'type': 'invalid_request_error', 'param': 'model', 'cod
e': None}}`
```
---

     
 
all -  [ Thoughts on DSPy ](https://www.reddit.com/r/LangChain/comments/1cqexk6/thoughts_on_dspy/) , 2024-05-13-0910
```
I have been tinkering with DSPy and thought I will share my 2 cents here for anyone who is planning to explore it:

The 
core idea behind DSPy are two things:

1.	⁠Separate programming from prompting
2.	⁠incorporate some of the best practice
 prompting techniques under the hood and expose it as a “signature”

Imagine working on a RAG. Today, the typical approa
ch is to write some retrieval and pass the results to a language model for natural language generation. But, after the f
irst pass, you realize it’s not perfect and you need to iterate and improve it. Typically, there are 2 levers to pull:


1.	⁠Document Chunking, insertion and Retrieval strategy
2.	⁠Language model settings and prompt engineering

Now, you try
 a few things, maybe document the performance in a google sheet, iterate and arrive at an ideal set of variables that gi
ves max accuracy.

Now, let’s say after a month, model upgrades, and all of a sudden the accuracy of your RAG regresses.
 Again you are back to square one, cos you don’t know what to optimize now - retrieval or model? You see what the proble
m is with this approach? This is a very open ended, monolithic, brittle and unstructured way to optimize and build langu
age model based applications.

This is precisely the problem DSPy is trying to solve. Whatever you can achieve with DSPy
 can be achieved with native prompt engineering and program composition techniques but it is purely dependent on the pro
grammers skill. But DSPy provides native constructs which anyone can learn and use for trying different techniques in a 
systematic manner.

DSPy the concept:

Separate prompting from programming and signatures

DSPy does not do any magic wi
th the language model. It just uses a bunch of prompt templates behind the scenes and exposes them as signatures. Ex: wh
en you write a signature like ‘context, question -> answer’, DSPy adds a typical RAG prompt before it makes the call to 
the LLM. But DSPy also gives you nice features like module settings, assertion based backtracking and automatic prompt o
ptimization.

Basically, you can do something like this with DSPy,

“Given a context and question, answer the following 
question. Make sure the answer is only “yes” or “no””. If the language model responds with anything else, traditionally 
we prompt engineer our way to fix it. In DSPy, you can assert the answer for “yes” or “no” and if the assertion fails, D
SPy will backtrack automatically, update the prompt to say something like, “this is not a correct answer- {previous_answ
er} and always only respond with a “yes” or “no”” and makes another language model call which improves the LLMs response
 because of this newly optimized prompt. In addition, you can also incorporate things like multi hops in your retrieval 
where you can do something like “retrieve -> generate queries and then retrieve again using the generated queries” for n
 times and build up a larger context to answer the original question.

Obviously, this can also be done using usual prom
pt engineering and programming techniques, but the framework exposes native easy to use settings and constructs to do th
ese things more naturally. DSPy as a concept really shines when you are composing a pipeline of language model calls whe
re prompt engineering the entire pipeline or even module wise can lead to a brittle Pipeline.

DSPy the Framework:

Now 
coming to the framework which is built in python, I think the framework as it stands today is

1.	⁠Not production ready

2.	⁠Buggy and poorly implemented
3.	⁠Lacks proper documentation
4.	⁠Poorly designed

To me it felt like a rushed impleme
ntation with little thought for design thinking, testing and programming principles. The framework code is very hard to 
understand with a lot of meta programming and data structure parsing and construction going behind the scenes that are s
cary to run in production.

This is a huge deterrent for anyone trying to learn and use this framework. But, I am sure t
he creators are thinking about all this and are working to reengineer the framework. There’s also a typescript implement
ation of this framework that is fairly less popular but has a much better and cleaner design and codebase:

https://gith
ub.com/dosco/llm-client/

My final thought about this framework is, it’s a promising concept, but it does not change any
thing about what we already know about LLMs. Also, hiding prompts as templates does not mean prompt engineering is going
 away, someone still needs to “engineer” the prompts the framework uses and imo the framework should expose these templa
tes and give control back to the developers that way, the vision of separate programming and prompting co exists with gi
ving control not only to program but also to prompt.

Finally, I was able to understand all this by running DSPy program
s and visualizing the LLM calls and what prompts it’s adding using my open source tool - https://github.com/Scale3-Labs/
langtrace . Do check it out and let me know if you have any feedback.
```
---

     
 
all -  [ Build a RAG pipeline for your blog with LangChain, OpenAI and Pinecone ](https://zackproser.com/blog/langchain-pinecone-chat-with-my-blog) , 2024-05-13-0910
```

```
---

     
 
all -  [ Private Storage and UI for Fine-Tuned Mistral Models ](https://www.reddit.com/r/LLMDevs/comments/1cqbbtr/private_storage_and_ui_for_finetuned_mistral/) , 2024-05-13-0910
```
Hello everyone,

I'm currently working on an internship project involving fine-tuning Mistral models (Mixtral 8x22B and 
Mixtral 8x7B). The process uses private documents, so maintaining **strict confidentiality is crucial**.  


I would app
reciate any advice or recommendations on the following:

* **Private Storage:** I need to securely store the fine-tuned 
model. While Hugging Face’s private model hosting is one option I'm considering, I'd appreciate any other recommendation
s for private storage options.



* **UI for model interaction:** The goal is to provide a private interface where a spe
cific group of people can interact with the fine-tuned model. I've come across several UI platforms like LibreChat, Flow
ise, Langchain, Streamlit, and OpenWebUI. Considering that my main priorities are privacy (ensuring that both the model 
and user interactions remain confidential) and simplicity (the easier to use and set up, the better, since this is just 
a testing phase), which platform would you recommend based on your experience?



Any insights or suggestions would be g
reatly appreciated! 
```
---

     
 
all -  [ Can I use Retrieval without stored ? ](https://www.reddit.com/r/LangChain/comments/1cqajd7/can_i_use_retrieval_without_stored/) , 2024-05-13-0910
```
I want to use RetrievalQA with chromadb, but it seems to store something after I use the retriever each time.

And the a
ction will make my next question have an effect.

I wonder, 'Is there any way to use chains without storing them in DB?'


Here is my code:

    llm_chain = LLMChain(llm=llm, prompt=RAG_prompt, verbose=True)
    
    qa = RetrievalQA.from_ch
ain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        chain_type='stuff',
        # chain_type_k
wargs={'prompt': RAG_prompt}, 
        verbose=True,
    )
```
---

     
 
all -  [ Function Calling ](https://www.reddit.com/r/LangChain/comments/1cqab15/function_calling/) , 2024-05-13-0910
```
I'm currently integrating a llm into our system for job classification. Users can submit requests via text or voice, for
 example, 'I want to design a cake for my son’s birthday.' My goal is for the model to accurately classify these inputs 
into predefined job categories and types (e.g., {'job\_type':'Plumbing', 'job\_category':'Handyman'}) and subsequently t
rigger a specific function. However, I'm encountering issues with open-source models like Functionary, which sometimes i
ncorrectly assign random categories or types not present in my predefined list. As I'm still very new to this, I would g
reatly appreciate any advice on how to ensure the model strictly adheres to my existing categories and types. Thanks for
 your help!

  
Edit: I got some interesting results with OpenAI API + pydantic for Hermes-2-Pro-Mistral-7B. Still testi
ng it
```
---

     
 
all -  [ Estudar pra concurso faltando 3 meses enquanto trabalha ](https://www.reddit.com/r/conselhodecarreira/comments/1cq6m5z/estudar_pra_concurso_faltando_3_meses_enquanto/) , 2024-05-13-0910
```
Sou dev jr e na estudante de Sistemas de Informação, comecei a me interessar bastante por concurso público (estabilidade
, previsibilidade das coisas e etc). Vi que abriu edital pro Tribunal de Contas do Estado do Pará, e tem 1 vaga pra ciên
cia de dados. De forma bastante honesta, acham que é possível passar em um concurso estudando 3 meses pra prova?

Já tra
balho com coisas do conteúdo do edital, como Python, Pandas, Scikit-learn, Langchain e etc, mas conhecimentos de legisla
ção, matemática, português e afins eu ainda não vi nada.
```
---

     
 
all -  [ Problem with upserting vectors from documents ](https://www.reddit.com/r/LangChain/comments/1cq3ius/problem_with_upserting_vectors_from_documents/) , 2024-05-13-0910
```
I am using the latest version of pinecone and langchain.I am encountering an error while trying to upsert vector 

using
 the code 

    index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    

i am encountering the err
or AttributeError: type object 'Pinecone' has no attribute 'from\_documents'

how to resolve this 

Any input greatly ap
preciated

Thanks
```
---

     
 
all -  [ Hugging Face + Langchain+ Upwork | How to Solve Real World AI Job. ](https://www.reddit.com/r/learnmachinelearning/comments/1cq0nsb/hugging_face_langchain_upwork_how_to_solve_real/) , 2024-05-13-0910
```
[(1) Hugging Face + Langchain+ Upwork | How to Solve Real World AI Job. - YouTube](https://www.youtube.com/watch?v=0G3rq
JhcMwA)
```
---

     
 
all -  [ Using Gemini-1.5-Pro Model to Build Intelligent Customer Agent ](https://www.reddit.com/r/GoogleGeminiAI/comments/1cpyhsf/using_gemini15pro_model_to_build_intelligent/) , 2024-05-13-0910
```
Following the previous instruction-following tests on the **Llama-3-8B** and **Phi-3-mini** models, given the relatively
 comprehensive local AI toolbox, it was decided to conduct more complex tests on the models.

This time, the plan is to 
use a large language model along with tools from the AI toolbox to construct an intelligent customer agent. This agent i
s primarily driven by the large language model, which intelligently selects tools from the toolbox to serve customers an
d resolve issues after understanding the semantics of customer inputs.

Currently available tools for the intelligent cu
stomer agent may include:

1. **Local Knowledge Base** - Constructed based on internal documentation of company products
.
2. **Search Engine** - Can search from the internet or internal company website.
3. **Function Calling** - Provides a 
set of functions for the model to call, enabling the model to perform actual tasks.

This demo will build an intelligent
 customer Agent for PS5 from scratch, equipped with a local knowledge base, search engine, and function calling tools. T
he large language model used will be **Gemini-1.5-Pro**. The reason for not choosing open-source models like **Llama-3**
 for local deployment is because the test results were unsatisfactory; currently, only close-source large models can eff
ectively handle such complex tasks.

Below is a demonstration of how it works:

# 一、 Creating a Product Knowledge Base f
or the Agent

The knowledge base is named PS5, containing two demo documents, 'PS5 Start Guide' and 'PS5 Safety Guide':


https://preview.redd.it/89b7ya6u4wzc1.png?width=2544&format=png&auto=webp&s=e77f0fb55349ae243f04c7869f5f4e38b44e5eb5

V
ectorize the documents and store them in the vector database:

https://preview.redd.it/k1rwokaz4wzc1.png?width=2539&form
at=png&auto=webp&s=518cb8b7798f6820ab9fe1ea2a72c4eb134abe70

https://preview.redd.it/5khg0laz4wzc1.png?width=2536&format
=png&auto=webp&s=985d22d8478302a500845a0be7cb55e98e537b88

# 二、Creating the PS5 Intelligent Customer Agent

Load the lar
ge language model Gemini-1.5-Pro and input the product description:

https://preview.redd.it/9tp9le465wzc1.png?width=254
5&format=png&auto=webp&s=59ee183bbc7f6c06fbee8ff4411a94010f12b877

Since voice input and output are not used in the test
, nothing is selected here:

https://preview.redd.it/kw60pnz85wzc1.png?width=2550&format=png&auto=webp&s=a32a1611e0ad6a8
90428a4e6daa9650e27f53ce9

Select the created knowledge base PS5, use Bing as the search engine (if internal search is r
equired, an internal search engine needs to be implemented), and activate the Function Calling feature. In the test, onl
y the function '**submit\_warranty\_claim(caption: str, description: str)**' is used to submit a repair request:

https:
//preview.redd.it/c5px8pcd5wzc1.png?width=2548&format=png&auto=webp&s=364be8cf2a155246256f351d2cf6e6a6a88797a8

Finally,
 load the agent configuration:

https://preview.redd.it/nle1p33f5wzc1.png?width=2549&format=png&auto=webp&s=c38301771168
6f436361379583faaf967cd70dae

# 三、Testing the PS5 Intelligent Customer Agent

Now everything is set up, let's start test
ing!

First, instead of diving straight into the main topic, let's chat with the agent for a bit to build rapport. It's 
happier when it can serve you better, right? :) Actually, it's also to elongate the conversation history, to see if the 
model encounters any issues.

I started with three questions:

1. **Hello, Nice to meet you.**
2. **please introduce you
rself first**.
3. **Can you introduce your products?**

The agent's responses were straightforward, without using any to
ols, solely based on product descriptions and the positioning of customer service:

https://preview.redd.it/e4djygcm5wzc
1.png?width=2553&format=png&auto=webp&s=27c46d87623dfa1c0734144afdba45030b615bf0

4. **Are there any new products from P
layStation in 2024?**  
Since the agent found the question beyond its knowledge timeframe, it opted to use Bing search r
esults to answer:

https://preview.redd.it/bpibqgvo5wzc1.png?width=2549&format=png&auto=webp&s=247ae335e82dc73cf24ec3127
18fdd6287ddd920

Bing search results can also be checked for verification:

https://preview.redd.it/eche1jtq5wzc1.png?wi
dth=2549&format=png&auto=webp&s=d9ae1eb23124ae8f51626f127b2c4a5f1555ab8b

5. **Does the PS5 have text-to-speech feature?
**  
This question likely falls outside the agent's knowledge range, so it used the results from the PS5 knowledge base 
to answer:

https://preview.redd.it/0tmfreet5wzc1.png?width=2550&format=png&auto=webp&s=72d5c4372cb720ad06d50ddd99310c6f
b2666e06

https://preview.redd.it/ab5ay4yu5wzc1.png?width=2555&format=png&auto=webp&s=8db3d4c07c87df5b023a356ea9d48bb165
dcdce0

1. **My PS5 controller is broken. There's no response when I press the shoulder button. Please help me arrange f
or a repair.**

Upon receiving the request, the agent first asked me to provide some purchase information: name, email, 
PS5 serial number, purchase date, etc.:

https://preview.redd.it/h2ygrzsz5wzc1.png?width=2554&format=png&auto=webp&s=e13
a11dc23ff1febbd40df3daa073450ccaf9de3

So, in the next round of conversation, I provided these information:

https://pre
view.redd.it/blqfi8j26wzc1.png?width=2548&format=png&auto=webp&s=ccd10ea2635cb573535a37c9f918a6c803b54a72

Upon receivin
g this information, the agent called the function '**submit\_warranty\_claim(caption: str, description: str)**' to help 
me submit the repair request:

https://preview.redd.it/gn4e5x556wzc1.png?width=2551&format=png&auto=webp&s=dc4afb882c70a
21d455d1e018af56012bd497b7e

To my delight, it also included the information I provided in the email, generated repair o
rder number 317150, and finally sent it to repairu/sony.com:

https://preview.redd.it/ut3eouw66wzc1.png?width=2552&forma
t=png&auto=webp&s=b64f50de4a1986858e1edf0de59eaab81db66be3

In summary, through this test, it was found that for slightl
y more complex usage scenarios, the model's fundamental capabilities are put to the test. The challenges of this test ma
inly lie in automatically selecting appropriate tools, correctly generating tool calls, and accurately generating parame
ters when using function calls. Looking forward to the next time when an open-source language model that can be deployed
 locally can also accomplish this task. :)

A video demonstration of the entire process is also available at:

[https://
youtu.be/GU5yvZiPXFs](https://youtu.be/GU5yvZiPXFs)

Project Github:

[https://github.com/smalltong02/keras-llm-robot](h
ttps://github.com/smalltong02/keras-llm-robot)
```
---

     
 
all -  [ Using Large Language Model to Build Intelligent Customer Agent ](https://www.reddit.com/r/Gemini/comments/1cpvova/using_large_language_model_to_build_intelligent/) , 2024-05-13-0910
```
Following the previous instruction-following tests on the **Llama-3-8B** and **Phi-3-mini** models, given the relatively
 comprehensive local AI toolbox, it was decided to conduct more complex tests on the models.

This time, the plan is to 
use a large language model along with tools from the AI toolbox to construct an intelligent customer agent. This agent i
s primarily driven by the large language model, which intelligently selects tools from the toolbox to serve customers an
d resolve issues after understanding the semantics of customer inputs.

Currently available tools for the intelligent cu
stomer agent may include:

1. **Local Knowledge Base** - Constructed based on internal documentation of company products
.
2. **Search Engine** - Can search from the internet or internal company website.
3. **Function Calling** - Provides a 
set of functions for the model to call, enabling the model to perform actual tasks.

This demo will build an intelligent
 customer Agent for PS5 from scratch, equipped with a local knowledge base, search engine, and function calling tools. T
he large language model used will be **Gemini-1.5-Pro**. The reason for not choosing open-source models like **Llama-3**
 for local deployment is because the test results were unsatisfactory; currently, only close-source large models can eff
ectively handle such complex tasks.

Below is a demonstration of how it works:

# 一、 Creating a Product Knowledge Base f
or the Agent

The knowledge base is named PS5, containing two demo documents, 'PS5 Start Guide' and 'PS5 Safety Guide':


https://preview.redd.it/89b7ya6u4wzc1.png?width=2544&format=png&auto=webp&s=e77f0fb55349ae243f04c7869f5f4e38b44e5eb5

V
ectorize the documents and store them in the vector database:

https://preview.redd.it/k1rwokaz4wzc1.png?width=2539&form
at=png&auto=webp&s=518cb8b7798f6820ab9fe1ea2a72c4eb134abe70

https://preview.redd.it/5khg0laz4wzc1.png?width=2536&format
=png&auto=webp&s=985d22d8478302a500845a0be7cb55e98e537b88

# 二、Creating the PS5 Intelligent Customer Agent

Load the lar
ge language model Gemini-1.5-Pro and input the product description:

https://preview.redd.it/9tp9le465wzc1.png?width=254
5&format=png&auto=webp&s=59ee183bbc7f6c06fbee8ff4411a94010f12b877

Since voice input and output are not used in the test
, nothing is selected here:

https://preview.redd.it/kw60pnz85wzc1.png?width=2550&format=png&auto=webp&s=a32a1611e0ad6a8
90428a4e6daa9650e27f53ce9

Select the created knowledge base PS5, use Bing as the search engine (if internal search is r
equired, an internal search engine needs to be implemented), and activate the Function Calling feature. In the test, onl
y the function '**submit\_warranty\_claim(caption: str, description: str)**' is used to submit a repair request:

https:
//preview.redd.it/c5px8pcd5wzc1.png?width=2548&format=png&auto=webp&s=364be8cf2a155246256f351d2cf6e6a6a88797a8

Finally,
 load the agent configuration:

https://preview.redd.it/nle1p33f5wzc1.png?width=2549&format=png&auto=webp&s=c38301771168
6f436361379583faaf967cd70dae

# 三、Testing the PS5 Intelligent Customer Agent

Now everything is set up, let's start test
ing!

First, instead of diving straight into the main topic, let's chat with the agent for a bit to build rapport. It's 
happier when it can serve you better, right? :) Actually, it's also to elongate the conversation history, to see if the 
model encounters any issues.

I started with three questions:

1. **Hello, Nice to meet you.**
2. **please introduce you
rself first**.
3. **Can you introduce your products?** 

The agent's responses were straightforward, without using any t
ools, solely based on product descriptions and the positioning of customer service:

https://preview.redd.it/e4djygcm5wz
c1.png?width=2553&format=png&auto=webp&s=27c46d87623dfa1c0734144afdba45030b615bf0

4. **Are there any new products from 
PlayStation in 2024?**  
Since the agent found the question beyond its knowledge timeframe, it opted to use Bing search 
results to answer:

https://preview.redd.it/bpibqgvo5wzc1.png?width=2549&format=png&auto=webp&s=247ae335e82dc73cf24ec312
718fdd6287ddd920

Bing search results can also be checked for verification:

https://preview.redd.it/eche1jtq5wzc1.png?w
idth=2549&format=png&auto=webp&s=d9ae1eb23124ae8f51626f127b2c4a5f1555ab8b

5. **Does the PS5 have text-to-speech feature
?**  
This question likely falls outside the agent's knowledge range, so it used the results from the PS5 knowledge base
 to answer:

https://preview.redd.it/0tmfreet5wzc1.png?width=2550&format=png&auto=webp&s=72d5c4372cb720ad06d50ddd99310c6
fb2666e06

https://preview.redd.it/ab5ay4yu5wzc1.png?width=2555&format=png&auto=webp&s=8db3d4c07c87df5b023a356ea9d48bb16
5dcdce0

1. **My PS5 controller is broken. There's no response when I press the shoulder button. Please help me arrange 
for a repair.** 

Upon receiving the request, the agent first asked me to provide some purchase information: name, email
, PS5 serial number, purchase date, etc.:

https://preview.redd.it/h2ygrzsz5wzc1.png?width=2554&format=png&auto=webp&s=e
13a11dc23ff1febbd40df3daa073450ccaf9de3

So, in the next round of conversation, I provided these information:

https://p
review.redd.it/blqfi8j26wzc1.png?width=2548&format=png&auto=webp&s=ccd10ea2635cb573535a37c9f918a6c803b54a72

Upon receiv
ing this information, the agent called the function '**submit\_warranty\_claim(caption: str, description: str)**' to hel
p me submit the repair request:

https://preview.redd.it/gn4e5x556wzc1.png?width=2551&format=png&auto=webp&s=dc4afb882c7
0a21d455d1e018af56012bd497b7e

To my delight, it also included the information I provided in the email, generated repair
 order number 317150, and finally sent it to repair[u/sony.com]():

https://preview.redd.it/ut3eouw66wzc1.png?width=2552
&format=png&auto=webp&s=b64f50de4a1986858e1edf0de59eaab81db66be3

In summary, through this test, it was found that for s
lightly more complex usage scenarios, the model's fundamental capabilities are put to the test. The challenges of this t
est mainly lie in automatically selecting appropriate tools, correctly generating tool calls, and accurately generating 
parameters when using function calls. Looking forward to the next time when an open-source language model that can be de
ployed locally can also accomplish this task. :)

A video demonstration of the entire process is also available at:

  

[https://youtu.be/GU5yvZiPXFs](https://youtu.be/GU5yvZiPXFs)
```
---

     
 
all -  [ Could someone please explain the difference in front-ends for LLM's? ](https://www.reddit.com/r/LocalLLaMA/comments/1cpv419/could_someone_please_explain_the_difference_in/) , 2024-05-13-0910
```
Librechat, LMstudio, openweb-ui, text-generation ui, llama.cpp, kobold.cpp, SillyTavern, Vercel, Langchain etc. are just
 some of the many popular frontends for LLM interaction, it's a bit confusing. 

Which are the best, and whats the diffe
rence between them?

2. People often recommend LMstudio, but say it's not open-source. Doesn't it have a github download
? How's it not open-sourced if so? 

3. Back in the day, I remembered some front-ends resulting in flagging accounts if 
using AI API through popular online models. Is this still happening, if so, which cause it?
```
---

     
 
all -  [ Is it possible to change agent prompt based on user question after the agent is already created? ](https://www.reddit.com/r/LangChain/comments/1cpsg8f/is_it_possible_to_change_agent_prompt_based_on/) , 2024-05-13-0910
```
I was following the [LangChain SQL Documentation](https://python.langchain.com/v0.1/docs/use_cases/sql/agents/). So far 
I'm using Few shot prompt template as the prompt for the agent.

    agent = create_sql_agent(
        llm=self.llm,
   
     db=self.db,
        prompt=self.few_shot_prompt,
        verbose=True,
        agent_type='openai-tools',
        t
op_k=10,
    )

Now what I want to do is

1. Create a chain that creates a custom prompt based on user question
2. Then 
pass that custom prompt created by the chain to the agent to use when I invoke it

I've created the chain like this

   
 rg = RunnableParallel(
            {
                'input': lambda x: x['input'],
                'dialect': lambda x
: x['dialect'],
                'top_k': lambda x: x['top_k'],
                'tables': self.table_extraction_chain,
  
          }
        ).assign(prompt=self.few_shot_prompt)

can I pipe in the Agent here somehow to use the custom prompt
?
```
---

     
 
all -  [ Problem with heavy documents ](https://www.reddit.com/r/LangChain/comments/1cps3s5/problem_with_heavy_documents/) , 2024-05-13-0910
```
Hello, I am a beginner in LLM and LangChain, and I am developing a small application that allows me to query PDF documen
ts with my OpenAI API. Everything works well so far with the PDFs. I am able to query the PDFs. If the question is out o
f context, it shows that the information is not in the PDF, otherwise, it displays the information. So, everything is go
ing well at the moment, but the problem is that with documents that are a bit longer, 100 pages or more, I really have p
roblems because I can't even load them to query them. So, what should I do?
```
---

     
 
all -  [ [P] Open source library to scrape PDFs, YouTube, URLs, Presentations, etc for API-hosted vision-lang ](https://www.reddit.com/r/MachineLearning/comments/1cpnlqe/p_open_source_library_to_scrape_pdfs_youtube_urls/) , 2024-05-13-0910
```
[Here I will share an open source library](https://thepi.pe/) you can use to extract text and visual unstructured data f
rom files, webpages, youtube videos, etc to immediately feed the results into API-hosted vision language models (like GP
T-4-Vision or Gemini). I made this simple tool because I was unable to get vision functionality with other extraction fr
ameworks like unstructuredio, langchain exctractors, document layout analysis models, etc,

Cheers & have fun!
```
---

     
 
all -  [ Generate python functions automatically from openapi.json? ](https://www.reddit.com/r/openBB/comments/1cpkkb4/generate_python_functions_automatically_from/) , 2024-05-13-0910
```
If I run the REST server locally, I can get an openapi spec via http://127.0.0.1:8000/openapi.json .

which tools can pa
rse the json and generate a python function or sub for each endpoint?

I tried a couple with a custom python parser and 
I can generate a working function like the below from the json below, but wondering if anyone has done a proper job with
 good docstrings and parameters and defaults? 

tried the bravado module which should take an openai spec and turn it in
to REST get requests, didn't parse the JSON correctly, and openapi-python-client also failed.

wanted to experiment with
 langchain agents talking to openai, anthropic etc., and make a tool for e.g. all the equity endpoints that take a symbo
l. could also inspect the obb functions and docstrings. basically wondering if there is a standard way to do this sort o
f metaprogramming with the openbb platform.

    def equity_price_quote(symbol):
       '''the latest quote for a given 
stock. Quote includes price, volume, and other data.'''

      retval = None
      retlist = obb.equity.price.quote(symb
ol).results
      if retlist and type(retlist is list):
        retval = retlist[0].model_dump_json()
      return retva
l 

json:

        '/api/v1/equity/price/quote': {
            'get': {
                'tags': [
                    'e
quity'
                ],
                'summary': 'Quote',
                'description': 'Get the latest quote for a
 given stock. Quote includes price, volume, and other data.',
                'operationId': 'equity_price_quote',
     
           'parameters': [
                    {
                        'name': 'provider',
                        'in
': 'query',
                        'required': true,
                        'schema': {
                            'e
num': [
                                'cboe',
                                'fmp',
                                '
intrinio',
                                'tmx',
                                'tradier',
                           
     'yfinance'
                            ],
                            'type': 'string',
                           
 'title': 'Provider'
                        }
                    },
                    {
                        'nam
e': 'symbol',
                        'in': 'query',
                        'required': true,
                        '
schema': {
                            'type': 'string',
                            'description': 'Symbol to get data 
for. Multiple comma separated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.',
            
                'multiple_items_allowed': [
                                'cboe',
                                'fmp
',
                                'intrinio',
                                'tmx',
                                't
radier',
                                'yfinance'
                            ],
                            'title': 
'Symbol'
                        },
                        'description': 'Symbol to get data for. Multiple comma separ
ated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.'
                    },
               
     {
                        'name': 'use_cache',
                        'in': 'query',
                        'requ
ired': false,
                        'schema': {
                            'type': 'boolean',
                       
     'title': 'cboe',
                            'description': 'When True, the company directories will be cached for 
24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass. (provider
: cboe)',
                            'default': true
                        },
                        'description': 
'When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the fun
ction are not cached. Set as False to bypass. (provider: cboe)'
                    },
                    {
           
             'name': 'source',
                        'in': 'query',
                        'required': false,
       
                 'schema': {
                            'enum': [
                                'iex',
              
                  'bats',
                                'bats_delayed',
                                'utp_delayed',

                                'cta_a_delayed',
                                'cta_b_delayed',
                     
           'intrinio_mx',
                                'intrinio_mx_plus',
                                'delayed_s
ip'
                            ],
                            'type': 'string',
                            'title': 'i
ntrinio',
                            'description': 'Source of the data. (provider: intrinio)',
                       
     'default': 'iex'
                        },
                        'description': 'Source of the data. (provider: 
intrinio)'
                    }
                ],
                'responses': {
                    '200': {
        
                'description': 'Successful Response',
                        'content': {
                            '
application/json': {
                                'schema': {
                                    '$ref': '#/componen
ts/schemas/OBBject_EquityQuote'
                                }
                            }
                        
}
                    },
                    '404': {
                        'description': 'Not found'
               
     },
                    '400': {
                        'description': 'No Results Found',
                        
'content': {
                            'application/json': {
                                'schema': {
             
                       '$ref': '#/components/schemas/OpenBBErrorResponse'
                                }
            
                }
                        }
                    },
                    '500': {
                        
'description': 'Internal Error',
                        'content': {
                            'application/json': {

                                'schema': {
                                    '$ref': '#/components/schemas/OpenBBErro
rResponse'
                                }
                            }
                        }
                   
 },
                    '422': {
                        'description': 'Validation Error',
                        'con
tent': {
                            'application/json': {
                                'schema': {
                 
                   '$ref': '#/components/schemas/HTTPValidationError'
                                }
                
            }
                        }
                    }
                },
                'model': 'EquityQuote',

                'examples': [
                    {
                        'scope': 'api',
                        'pa
rameters': {
                            'symbol': 'AAPL',
                            'provider': 'fmp'
               
         },
                        'provider': 'fmp'
                    }
                ]
            }
        },
```
---

     
 
all -  [ GPT3.5 tool calling more accurately than Claude haiku. ](https://www.reddit.com/r/LangChain/comments/1cpjgn1/gpt35_tool_calling_more_accurately_than_claude/) , 2024-05-13-0910
```
Using the same prompt, GPT 3.5 seems more likely to use tools correctly all the time whereas Claude haiku needs better p
rompting to achieve tool calling? Even so, it misses out a good number of times. 

For eg. I don’t even have to mention 
any tools in the gpt prompt but I have to mention in for haiku to even work. Putting the tool description and query work
s enough for gpt.

E.g a tool parameter for “rag vector query” correctly abstracts the query to keywords but haiku dumps
 the entire question in. GPT is also able to infer from history and use tools (eg, tell me more) while haiku just plain 
responds saying it has no more data. 

Am I using anything wrong? Everyone is saying haiku is smarter and all.. main rea
son I am trying it out is that it is cheaper, potentially allowing for more documents to stuff in. 
```
---

     
 
all -  [ Voice generation ](https://www.reddit.com/r/LangChain/comments/1cpcwcg/voice_generation/) , 2024-05-13-0910
```
Hey there, Is there any way to generate a voice?   
I found some impressive tools out there, but wish they were integrat
ed with langchain like this one: [https://github.com/jasonppy/VoiceCraft](https://github.com/jasonppy/VoiceCraft)
```
---

     
 
all -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-13-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
all -  [ Function/tool calling on non-OpenAI models? ](https://www.reddit.com/r/LangChain/comments/1cpagwd/functiontool_calling_on_nonopenai_models/) , 2024-05-13-0910
```
I have a Next.js application that requires RAG (Specifically web search) with multiple open source models. Is there a wa
y to get them to work with function/tool calling?
```
---

     
 
all -  [ Agent to generate Charts based on the user's prompt ](https://www.reddit.com/r/LangChain/comments/1cp9gqj/agent_to_generate_charts_based_on_the_users_prompt/) , 2024-05-13-0910
```
https://preview.redd.it/4738d3i5aqzc1.png?width=723&format=png&auto=webp&s=89b493a6fc2271d489b0df2e6faddd3bf4a19f43

Hi 
Guys, I have a RAG for csv file, the data is about temperature sensors and apps usage percentage in a phone. I was able 
to use azure gpt 4 and generate a textual response. Since we have a csv file, I want the llm to also generate a graph al
ong with the textual response. Please tell me how to code this up.   
  

```
---

     
 
all -  [ Tutorial on Langchain that doesn't rely on an online service? ](https://www.reddit.com/r/learnprogramming/comments/1cp5udf/tutorial_on_langchain_that_doesnt_rely_on_an/) , 2024-05-13-0910
```
Like every tutorials use langchain with an online service, but I would like to build a llm or a simple chatbot with a cr
appy offline llm that we can run offline. Is there anything like it? I searched and it seems that there's nothing like i
t and it's basically a pipe dream.
```
---

     
 
all -  [ (Code included) I did a workshop on long-term selective memory for LLM applications recently ](https://www.reddit.com/r/LangChain/comments/1cp5q9p/code_included_i_did_a_workshop_on_longterm/) , 2024-05-13-0910
```
Good to be back making content for y’all.

Video: [https://www.youtube.com/watch?v=RkWor1BZOn0](https://www.youtube.com/
watch?v=RkWor1BZOn0)

Code: [https://github.com/trancethehuman/ai-workshop-code/blob/main/Long\_term\_memory\_%26\_perso
nalized\_LLM\_responses.ipynb](https://github.com/trancethehuman/ai-workshop-code/blob/main/Long_term_memory_%26_persona
lized_LLM_responses.ipynb)

Let me know in the comments what you liked / didn’t like about this and I’ll make it better 
next time.

or if you need clarifications, I‘m happy to answer to the best of my ability.
```
---

     
 
all -  [ Getting Answers from GPT based on document ](https://www.reddit.com/r/ChatGPT/comments/1cp4mt7/getting_answers_from_gpt_based_on_document/) , 2024-05-13-0910
```
Using the api how to give a large amount of information then receive answers from the given data. 

What is the best, mo
st cost efficient solution.
Assistants API? Langchain?
```
---

     
 
all -  [ What's the scoop on serialization? It's all over the show with LangChain ](https://www.reddit.com/r/LangChain/comments/1cp3y1l/whats_the_scoop_on_serialization_its_all_over_the/) , 2024-05-13-0910
```
Hi am I doing something wrong?

I'm using Documents and I want to save/load them. I've tried, \`.json()\` the new \`load
\` module's \`.dumpd()\` and \`.load()\` -- but some documents can't be deserialized.

e.g. I am trying to build somethi
ng that uses LangChain documents. But not all of them are deserializable -- instead you get goop like this when using th
e output of \`ContextualCompressionRetriever\` (which returns some documents) and use one of the above functions to seri
alize:

https://preview.redd.it/74vlfp1wsozc1.png?width=417&format=png&auto=webp&s=0d3d238376da4f9305eed45ee212ce8736025
26e

Basically I have to parse the repr to get the document? Any pointers? Or write my own custom serialization/deserial
ization?
```
---

     
 
all -  [ Ai generated ad that was on my feed ](https://i.redd.it/doitcfsajozc1.jpeg) , 2024-05-13-0910
```
How lazy is a company to use AI?
```
---

     
 
all -  [ how to get LLM to infer dates from a json file or text file? ](https://www.reddit.com/r/LangChain/comments/1coz2io/how_to_get_llm_to_infer_dates_from_a_json_file_or/) , 2024-05-13-0910
```
im currently using mistral-small in my project, i want to create a chatbot that can give answers about the weather in th
e future, so i have a huge json file that i want to feed to the model as a vector embedding and then let the user ask th
e chatbot questions about future weather such as what should i wear tomorrow etc.

the problem is that the LLM seems to 
not read the files, i even tried to programatically rebuild the file as a text file.

this is my code:

\`\`\`

    json
_loader = JSONLoader('C:\\xxxx\\data\\all_weather_by_date.json')
    
    
    # Split text into chunks
    text_splitte
r = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    # Define the embedding mode
l
    embeddings = MistralAIEmbeddings(model='mistral-embed', mistral_api_key='XXXXXXXXXXXXXXXXXXXXXXX', )
    # Create 
the vector store 
    vector = FAISS.from_documents(documents, embeddings)
    vector.save_local('cache')
    
    # Def
ine a retriever interface
    retriever = vector.as_retriever()
    # Define LLM
    model = ChatMistralAI(mistral_api_k
ey='XXXXXXXXXXXXXXXXXXXXX', model='mistral-small', temperature=1)
    # Define prompt template
    prompt = ChatPromptTe
mplate.from_template('''
    
    <context>
    {context}
    </context>
    
    Question: {input}''')
    
    # Creat
e a retrieval chain to answer questions
    document_chain = create_stuff_documents_chain(model, prompt)
    retrieval_c
hain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'context': instructions,
'input': f'answer max 60 words, end with follow-up question, no clauses: what should i wear tomorrow? today is 10.5.2024
'})
    print(response['answer'])

\`\`\`

my json is built like this:

{

'current\_year\_dates' : {

'2024.05.11' : {


'humidity': '50%',

'degrees': '34'

}

.... all the other dates throught the year

}

when i attempted to change the j
son file to text file, i changed it to this format:

'on 2024.10.5 there will be 50% humidity and 30 degress.'

and stil
l it didnt work



also i have always get a warning when running my code about HF\_TOKEN not being set and using len spl
itter.

please help me!
```
---

     
 
all -  [ LangChain 0.2 prerelease ](https://www.reddit.com/r/LangChain/comments/1coyy48/langchain_02_prerelease/) , 2024-05-13-0910
```
hi all! we're gearing up for a release of langchain 0.2. The main change is no longer depending on langchain-community (
this will increase modularity, decrease size of package, make more secure). We're also adding in a new docs structure an
d highlighting a bunch of the changes we made as part of 0.1

We posted more about this on GitHub (https://github.com/la
ngchain-ai/langchain/discussions/21437) but happy to answer any questions here! Would obviously love and really apprecia
te any feedback :)
```
---

     
 
all -  [ Library that automatically creates a UI for your chatbot? ](https://www.reddit.com/r/LangChain/comments/1cot1we/library_that_automatically_creates_a_ui_for_your/) , 2024-05-13-0910
```
[Cycls](https://docs.cycls.com/getting-started) Python library significantly simplifies the development of AI chatbots f
or developers, particularly those who specialize in backend development and may find creating user interfaces tiring. Th
is library eliminates the need to develop a UI from scratch by providing a prebuilt, ChatGPTlike user interface that dev
elopers can use immediately. By simply importing Cycls into your project, you can integrate it with major LLM Python lib
raries and APIs, enabling the use of various LLM models easily.

Upon importing and running your application, it is auto
matically deployed with the user interface and a public URL, enhancing the efficiency of both development and testing pr
ocesses. This feature is especially valuable for speeding up deployment and reducing the workload on developers focusing
 on backend functionalities.


```
---

     
 
all -  [ duckduckgo_search with langchain ](https://www.reddit.com/r/duckduckgo/comments/1coso6p/duckduckgo_search_with_langchain/) , 2024-05-13-0910
```
am using duckduckgo\_search with langchain community , it was working fine but am getting rate limit error i have alread
y tried to upgrade but still the same error . is there any one who can tell me why
```
---

     
 
all -  [ Nomic embeddings with Ollama using Langchain up to Pinecone ](https://www.reddit.com/r/ollama/comments/1corjsr/nomic_embeddings_with_ollama_using_langchain_up/) , 2024-05-13-0910
```
Anyone attempted this yet?  I have a lot of familiarity using open AI embeddings up to Pinecone and I want to switch to 
Nomic. 

Reviewed the Langchain Python documentation on using nomic embeddings and it seems incomplete to enable me to p
ush up embeddings and text and metadata in the format that I’m used to with OpenAI’s embeddings and pinecone. 


```
---

     
 
all -  [ Would LC be a good platform for building a LLM-based chat which builds user profiles? ](https://www.reddit.com/r/LangChain/comments/1cooqdx/would_lc_be_a_good_platform_for_building_a/) , 2024-05-13-0910
```
Would LC be a good <framework> for building a LLM-based chat which builds user profiles?

For example, over the course o
f the conversation it could fill slots such as name, location, etc. 

or there an off the shelf tool which is already do
ing this? 
```
---

     
 
all -  [ Just a question on LCEL vs RetrievalQA ](https://www.reddit.com/r/LangChain/comments/1colp4k/just_a_question_on_lcel_vs_retrievalqa/) , 2024-05-13-0910
```
Hi all, in the previous version of code, I had something like this:

qa = RetrievalQA.from\_chain\_type(  
 llm=llm,  
 
chain\_type\_kwargs={'prompt': prompt},  
 retriever=retriever,  
 return\_source\_documents=True,          
 tags = tag
s,  
 metadata = metadata          
 )  
basically its a Multivector retriever with RetrievalQA.   In LCEL chain it is l
ike below:

chain = (  
{'context': retriever, 'question': RunnablePassthrough()}  
 | prompt  
 | model  
 | StrOutputP
arser()  
)  
The question I have is, how to add additional parameters in the above LCEL chain?   
additional parameters
:  
return\_source\_documents=True,          
tags = tags,  
metadata = metadata   
```
---

     
 
all -  [ Phi3 text2sql ](https://www.reddit.com/r/LangChain/comments/1colhlx/phi3_text2sql/) , 2024-05-13-0910
```
Has anyone tried phi3 for text2sql in postgres? I am trying and can't generate a correct query
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1cola2g/for_hire_programmerweb_developerit_consultant/) , 2024-05-13-0910
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

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/learnpython/comments/1col188/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-13-0910
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time.

So I wanna learn how to manage these kind of sessions and using credentials is
 not an option.

one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Function Calling + RAG + Langchain Tool Calling Agent + REDIS Memory ](https://www.reddit.com/r/LangChain/comments/1cokru8/function_calling_rag_langchain_tool_calling_agent/) , 2024-05-13-0910
```
Tell me if this idea is feasible and how I can pull this off

I have a langchain agent that does function calling, but o
ne shortcoming is that it fails to answer queries from the pulled data many times, 

Can I store this pulled data into a
 knowledge graph vector database as this data is for holiday packages with key value relations such as duration, price, 
location, ref\_id etc and sub categories like fare sets, cabin sub categories etc. 

How can I make my langchain agent i
n python better using knowledge graphs and making it answer follow up questions using RAG on the last fetched data?


```
---

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/LangChain/comments/1cokd2v/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-13-0910
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time. 

So I wanna learn how to manage these kind of sessions and using credentials i
s not an option.

  
one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Profile Review ](https://i.redd.it/0dwb8qutwjzc1.jpeg) , 2024-05-13-0910
```
Thoughts on my profile? Trying to land full-stack AI jobs. Interested in any feedback, even if it’s brutal as long as it
’s actionable.
```
---

     
 
all -  [ Evaluation Models - GPT-3.5 vs. GPT 4 Turbo ](https://www.reddit.com/r/LangChain/comments/1coj65b/evaluation_models_gpt35_vs_gpt_4_turbo/) , 2024-05-13-0910
```
hey guys

I use correctness, hallucination & relevance score to evaluate a RAG chain on langsmith. 

Generally, do you t
hink 3.5 is good enough to evaluate the outcomes?
```
---

     
 
all -  [ LLAMA2 (and Other Models) Engaging in Self-Dialogue: Asking and Answering Its Own Questions ](https://www.reddit.com/r/LLMDevs/comments/1coigub/llama2_and_other_models_engaging_in_selfdialogue/) , 2024-05-13-0910
```
I am using Langchain + different LLM models ('Llama-2-7b-chat-hf', 'Mistral-7B-Instruct-v0.2', ...)..

\*\*My purpose\*\
* is to do prompt engineering and evaluate a model's ability to answer various questions.

\*\*The challenge\*\* is that
 after posing almost any question, the LLM starts a self-conversation, asking itself questions as a 'Human' and then ans
wering them as an 'AI.'

\*\*What am I missing?\*\*

\*\*How can I ensure\*\* the model only responds to the original qu
estion without engaging in a self-conversation?

    conversation = ConversationChain(
      llm=self.llm,
      memory=
ConversationBufferMemory(),
      verbose=False)
    
    print('*************************** chat_conversation *********
******************')
    
    while True:
      user_input = input('> ')            
      ai_response = conversation.pr
edict(input=user_input)
      print('\nAssistant:\n', ai_response)
      print('----------------------------------------
--------------------------------------------------------------\n\n\n')



Example for a prompt:



https://preview.redd.
it/cprggyrahjzc1.png?width=1458&format=png&auto=webp&s=2b9b230a3123d415b7015c7131f5eddf44efedb5

  


  

```
---

     
 
all -  [ How to add JsonOutputParser with RunnableWithMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1cofbkc/how_to_add_jsonoutputparser_with/) , 2024-05-13-0910
```
This my code

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,

        input_messages_key='input',
        history_messages_key='chat_history',
        output_messages_key='answer',

    )
    
    conversational_rag_chain.invoke(
        {'input': 'I am interested in Screwdrivers, Sockets, Ratchets. N
ow generate new questions based on past behaviour'},
        config={
            'configurable': {'session_id': 'abc123
'}
        },  # constructs a key 'abc123' in `store`.
    )['answer']
    

I want to add this \`JsonOutputParser\` to 
above \`conversational\_rag\_chain\`

    class ProbingQuestion(BaseModel):
        Question: str = Field(description='p
robing question')
        Options: List[str] = Field(description='list of options for the probing question')
    
    
 
   output_parser = JsonOutputParser(pydantic_object=ProbingQuestion)



So can anyone help this?
```
---

     
 
all -  [ A Daily chronicle of AI Innovations May 09th 2024: 🤖 OpenAI posts Model Spec revealing how it wants  ](https://readaloudforme.com/index_subscribers) , 2024-05-13-0910
```
A Daily chronicle of AI Innovations May 09th 2024: 
🤖 OpenAI posts Model Spec revealing how it wants AI to behave 
🧬 Goo
gle DeepMind unveils AlphaFold 3, the next generation of its protein prediction model 🧠 Neuralink faces setback as first
 human brain implant encounters problem 
🕵️‍♀️  Microsoft developed a secretive AI service for US spies 
🎨 Generate imag
es on Midjourney Alpha 📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts 
🏢New AI data cent
er to be built at the failed Foxconn project site in Wisconsin 
🤔Sam Altman says we are not taking AI’s impact on the ec
onomy seriously 
✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows 🎮Altera’s gaming AI
 agents get backed by Eric Schmidt, Former Google CEO

 

🤖 OpenAI posts Model Spec revealing how it wants AI to behave


 

OpenAI has introduced the first draft of Model Spec, a proposed framework aiming to shape how AI models respond, emp
hasizing assistance, humanity's benefit, and adherence to social norms and laws.
The framework suggests specific rules f
or AI behavior, including compliance with laws, protection of privacy, and avoidance of NSFW content, with options to ad
just settings like allowing NSFW content in certain contexts.
While the Model Spec seeks public feedback for future adju
stments and doesn't immediately affect existing models like GPT-4 or DALL-E 3, it's envisioned as a living document to g
uide AI behavior improvement over time.
Source: https://readaloudforme.com/index_subscribers

🧬 Google DeepMind unveils 
AlphaFold 3, the next generation of its protein prediction model 

https://youtu.be/9ufplEgtq8w?si=XAREDQVZwYLBtcss



G
oogle DeepMind and Isomorphic Labs have released AlphaFold 3, a new AI model for predicting protein structures, includin
g their interactions with various molecules such as DNA, RNA, and small molecules, thereby enhancing drug discovery poss
ibilities.
This new version is more precise in mapping out complex groupings of molecules, significantly enhancing our a
bility to understand and predict molecular behavior compared to its earlier version.
Google will not open-source this ve
rsion but has launched AlphaFold Server for non-commercial research use, aiming to balance intellectual property concern
s with accessibility for scientific progress.
Source: https://readaloudforme.com/index_subscribers

🧠 Neuralink faces se
tback as first human brain implant encounters problem 

Neuralink admitted that some of the micro-thin threads from thei
r N1 brain chip retracted after implantation in the first human patient, possibly due to air trapped in the skull during
 surgery, which affected the device's data transmission rate.
Despite the retraction of several threads, Neuralink manag
ed to increase the data transmission speed over time by optimizing their recording algorithm and improving signal transl
ation into cursor movements.
The company is planning further implants, with goals to implant two more patients in the co
ming months and ten in total this year, while continuing to refine their technology and reporting developments to the FD
A.
Source: https://readaloudforme.com/index_subscribers

🕵️‍♀️ Microsoft developed a secretive AI service for US spies


Microsoft has developed a top-secret generative AI model entirely disconnected from the internet so US intelligence agen
cies can safely harness the powerful technology to analyze top-secret info. The model based on GPT-4 is now live, answer
ing questions, and will also write code.

Microsoft spent 18 months developing the model, which is 'air-gapped' to ensur
e it is secure. This is the first time a model is fully isolated– meaning it's not connected to the internet but is on a
 special network that's only accessible by the U.S. government.

It can read and analyze files but cannot learn from the
m to stop sensitive information from entering the platform. It is yet to be tested and accredited by the intelligence ag
encies.

Why does this matter?

Intelligence agencies all over the world have been racing to be the first to harness gen
erative AI. I guess we know who’s going to be the winner. If this AI tool is successful, it will fundamentally change th
e way intelligence agencies operate.

Source: https://readaloudforme.com/index_subscribers

What Else Is Happening in AI
 on May 09th 2024❗

📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts

In coming months, Mi
crosoft Copilot will be updated with new features like auto-complete and ‘elaborate your prompt’ that offer suggestions 
to improve AI prompts. It aims to solve the problem of coming up with good prompts for generative AI. (Link)

🏢New AI da
ta center to be built at the failed Foxconn project site in Wisconsin

President Joe Biden announced an AI data center t
o be built on the same site as the failed Foxconn project in Racine, Wisconsin. According to a White House press release
, Microsoft is investing $3.3B in the project, creating up to 2,000 permanent jobs. (Link)

🤔Sam Altman says we are not 
taking AI’s impact on the economy seriously

At a Brooking's Institute panel about AI and geopolitics on Tuesday, Altman
 said the discussions around AI's effect on the economy–  like how it may lead to mass job replacement– died down this y
ear compared to last. He said if we don’t take these concerns seriously enough going forward, it could be a massive issu
e. (Link)

✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows

It is launching Typeface
 Arc technology, which enables a user to state a high-level marketing objective and then have the system automatically p
lan and generate all the assets, including emails, images, and notifications that are all connected. (Link)

🎮Altera’s g
aming AI agents get backed by Eric Schmidt, Former Google CEO

Altera is the newest startup joining the fray to build a 
new guard of AI agents. It raised $9 million in an oversubscribed seed round, co-led by Eric Schmidt’s deep-tech fund, F
irst Spark Ventures and Patron, the seed-stage fund co-founded by Riot Games alums. (Link)

 

AI TRAINING May 09th 2024


🎨 Generate images on Midjourney Alpha

Generate images on Midjourney Alpha 
Midjourney’s website is now accessible to 
anyone with more than 100 generated images, improving the experience when prompting images over its standard Discord gro
up.

Check that you’ve generated more than 100 images by typing /info in the Midjourney Discord group. If you have, head
 over to Midjourney Alpha.

In the main menu, you can explore other creations and search prompts.

Select where it says 
“imagine” and enter your prompt to generate an image.

Add a reference image by selecting “+” or play with different par
ameters such as image size, stylization, or even weirdness by pressing the “slider control” button

AI RESEARCH on May 0
9th 2024

📶 AI usage surges in the workplace

AI usage surges in the workplace
Microsoft and LinkedIn just published the
ir Work Trend Index Annual Report, revealing that AI adoption is surging in the workplace — calling 2024 the ‘year AI at
 work gets real’.

The report found that use of GenAI has doubled in the last six months, with 75% of knowledge workers 
using the tech in some capacity.

78% of AI users are bringing their own AI to work — with 52% reporting they are reluct
ant to admit to its use.

66% of leaders wouldn't hire someone without AI skills, and 71% prefer less experienced candid
ates with AI aptitude over a more experienced one without it.

AI power users reported enhanced productivity, creativity
, and job satisfaction compared to skeptical peers.

Why it matters: Employees are adopting AI at a rapid pace, regardle
ss of if their own organizations are ready for the shift. As AI spreads across all sectors, generations, and skillsets, 
the early adopters are rising to the top — while those that aren’t at least exploring the tech are quickly running out o
f time

Trending AI Tools May 09th 2024

📍GeoSpy - Uncover photo locations with AI

🧑‍💻 LangChain - Connect LLMs to priv
ate data for context-aware applications

📊 Abstra - Scale business processes with Python and AI

🎨 Freepik Pikaso Upscal
er - Integrated with Magnific, enlarge images without losing quality

💬 Notion AI Q&A - Q&A is now open to the public, a
llowing users to ask and find information across their workspace

🎵 Udio Audio Inpainting - Select a portion of an AI-ge
nerated music track and regenerate it

New AI Job Opportunities on May 09th 2024

🎥 The Rundown - Video Content Creator


🤖 Anthropic - Research Engineer, Human-Computer Interfaces

👩‍💻 Adept AI - Solutions Engineer

📝 Mistral AI - Data Anno
tation Technical Program Manager

```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-13-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-13-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-13-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
