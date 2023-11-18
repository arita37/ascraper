 
all -  [ OpenAI fires Sam Altman ](https://www.reddit.com/r/LangChain/comments/17xox8b/openai_fires_sam_altman/) , 2023-11-18-0909
```
I wonder if this has anything to do with subscriptions getting limited recently and costs going over the roof 🤔
```
---

     
 
all -  [ How to create Async Tools in LangChain? ](https://www.reddit.com/r/LangChain/comments/17xlkxg/how_to_create_async_tools_in_langchain/) , 2023-11-18-0909
```
Hello folks,

Is there documentation on how to create an Async Tool for an agent? 

I'm trying to run a headless browser
 (using pyppeteer) for an agent to use but I'm not sure how I can integrate the asynchronous code of pyppeteer as a tool
.
```
---

     
 
all -  [ Training LLMs to follow procedure for Math gives an accuracy of 98.5% ](https://www.reddit.com/r/LangChain/comments/17xj0ha/training_llms_to_follow_procedure_for_math_gives/) , 2023-11-18-0909
```
Github Link: https://github.com/desik1998/MathWithLLMs

Although LLMs are able to do a lot of tasks such as Coding, scie
nce etc, they often fail in doing Math tasks without a calculator (including the State of the Art Models). 

Our intuiti
on behind why models cannot do Math is because the instructions on the internet are something like a x b = c and do not 
follow the procedure which we humans follow when doing Math. For example when asked any human how to do 123 x 45, we fol
low the digit wise multiplication technique using carry, get results for each digit multiplication and then add the corr
esponding resulting numbers. But on the internet, we don't show the procedure to do Math and instead just right the corr
ect value. And now given LLMs are given a x b = c, they've to reverse engineer the algorithm for multiplication. 

Most 
of the existing Literature gives instructions to the LLM instead of showing the procedure and we think this might not be
 the best approach to teach LLM. 

### What this project does?
This project aims to prove that LLMs can learn Math when 
trained on a step-by-step procedural way similar to how humans do it. It also breaks the notion that LLMs cannot do Math
 without using calculators. For now to illustrate this, this project showcases how LLMs can learn multiplication. The ra
tionale behind taking multiplication is that GPT-4 cannot do multiplication for >3 digit numbers. We prove that LLMs can
 do Math when taught using a step-by-step procedure. For example, instead of teaching LLMs multiplication like 23 * 34 =
 782, we teach it multiplication similar to how we do digit-wise multiplication, get values for each digit multiplicatio
n and further add the resulting numbers to get the final result.

**Instruction Tuning:**
We've further done finetuning 
on OpenAI's GPT-3.5 to teach Math.

There are close to 1300 multiplication instructions created for training and 200 for
 validation. The test cases were generated keeping in mind the OpenAI GPT-3.5 4096 token limit. A 5 x 5 digit multiplica
tion can in general fit within 4096 limit but 6 x 6 cannot fit. But if one number is 6 digit, the other can be <= 4 digi
t and similarly if 1 number is 7 digit then the other can be <= 3 digit.

Also instead of giving * for multiplication an
d + for addition, different operators' <<*>> and <<<+>>> are given. The rationale behind this is, using the existing * a
nd + for multiplication and addition might tap on the existing weights of the neural network which doesn't follow step-b
y-step instruction and directly give the result for multiplication in one single step.

[Sample Instruction](https://pas
tebin.com/VZNUHQVQ)

![**The overall training/validation loss goes to 0 within 0.1 epochs**](https://raw.githubuserconte
nt.com/desik1998/MathWithLLMs/main/Training_and_Validation_Loss.png)

### Results
The benchmarking was done on 200 test 
cases where each test case has two random numbers generated. For the 200 samples which were tested, excluding for 3 case
s, the rest of the cases the multiplication is correct. Which means this overall accuracy is **98.5%**. (We're also look
ing for feedback from community about how to test this better.)

### Future Improvements
* Reach out to AI and open-sour
ce community to make this proposal better or identify any flaws.
* Do the same process of finetuning using open-source L
LMs.
* Figure out what's the smallest LLM that can do Math accurately when trained in a procedural manner (A 10 year kid
 can do Math). Check this for both normal models and distilled models as well.

Requesting for Feedback from AI Communit
y!
```
---

     
 
all -  [ No module named 'openai'ImportError: Could not import openai python package. Please install it with  ](https://www.reddit.com/r/CodingHelp/comments/17xiicf/no_module_named_openaiimporterror_could_not/) , 2023-11-18-0909
```
raceback (most recent call last):  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.
py', line 294, in validate\_environment  
  
import openai  
  
ModuleNotFoundError: No module named 'openai'  
  

  
During handling of the above exception, another exception occurred:  
  
  
Traceback (most recent call last): 
 
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 5
34, in \_run\_script  
  
exec(code, module.\_\_dict\_\_)  
  
  File '/mount/src/streamlit-app/seq\_gpt\_memory.py'
, line 35, in <module>  
  
llm = OpenAI(temperature=0.9)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packa
ges/langchain/load/serializable.py', line 97, in \_\_init\_\_  
  
super().\_\_init\_\_(\*\*kwargs)  
  
  File '/ho
me/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', line 339, in \_\_init\_\_  
  
values, fields\_set
, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_\_, data)  
  
  File '/home/adminuser/venv/li
b/python3.9/site-packages/pydantic/v1/main.py', line 1102, in validate\_model  
  
values = validator(cls\_, values) 
 
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py', line 296, in validate\_environ
ment  
  
raise ImportError(  
  
ImportError: Could not import openai python package. Please install it with \`pip 
install openai\`.  
  
2023-11-17 16:03:06.141 Uncaught app exception  
  
Traceback (most recent call last):  
  

  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py', line 294, in validate\_environment
  
  
import openai  
  
ModuleNotFoundError: No module named 'openai'  
  
  
During handling of the above except
ion, another exception occurred:  
  
  
Traceback (most recent call last):  
  
  File '/home/adminuser/venv/lib/p
ython3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 534, in \_run\_script  
  
exec(code, m
odule.\_\_dict\_\_)  
  
  File '/mount/src/streamlit-app/seq\_gpt\_memory.py', line 35, in <module>  
  
llm = Open
AI(temperature=0.9)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/load/serializable.py', lin
e 97, in \_\_init\_\_  
  
super().\_\_init\_\_(\*\*kwargs)  
  
  File '/home/adminuser/venv/lib/python3.9/site-pac
kages/pydantic/v1/main.py', line 339, in \_\_init\_\_  
  
values, fields\_set, validation\_error = validate\_model(\_
\_pydantic\_self\_\_.\_\_class\_\_, data)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/ma
in.py', line 1102, in validate\_model  
  
values = validator(cls\_, values)  
  
  File '/home/adminuser/venv/lib/p
ython3.9/site-packages/langchain/llms/openai.py', line 296, in validate\_environment  
  
raise ImportError(  
  
Im
portError: Could not import openai python package. Please install it with \`pip install openai\`.
```
---

     
 
all -  [ No module named 'openai' showing even it is mentioned in requirements.txt ](https://www.reddit.com/r/StreamlitOfficial/comments/17xhac4/no_module_named_openai_showing_even_it_is/) , 2023-11-18-0909
```
 

Traceback (most recent call last):

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py'
, line 294, in validate\_environment

   import openai

ModuleNotFoundError: No module named 'openai'

During handling o
f the above exception, another exception occurred:

Traceback (most recent call last):

 File '/home/adminuser/venv/lib/
python3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 534, in \_run\_script

   exec(code, mod
ule.\_\_dict\_\_)

 File '/mount/src/streamlit-app/seq\_gpt\_memory.py', line 35, in <module>

   llm = OpenAI(temperatu
re=0.9)

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/load/serializable.py', line 97, in \_\_init\_
\_

   super().\_\_init\_\_(\*\*kwargs)

 File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', l
ine 339, in \_\_init\_\_

   values, fields\_set, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_
\_, data)

 File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', line 1102, in validate\_model


   values = validator(cls\_, values)

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py',
 line 296, in validate\_environment

   raise ImportError(

ImportError: Could not import openai python package. Please 
install it with \`pip install openai\`.
```
---

     
 
all -  [ Use Langchain, Deepgram, and Mistral 7B to Build a Youtube Video Summarization App ](https://www.koyeb.com/tutorials/use-langchain-deepgram-and-mistral7b-to-build-a-youtube-video-summarization-app) , 2023-11-18-0909
```

```
---

     
 
all -  [ I built a library for cheap, fast and predictable LLM functions in Python ](https://www.reddit.com/r/Python/comments/17xaigf/i_built_a_library_for_cheap_fast_and_predictable/) , 2023-11-18-0909
```
Hi r/python, Jack here! I'm one of the creators of [MonkeyPatch](https://github.com/monkeypatch/monkeypatch.py), an easy
 way to build LLM-powered functions and apps that get cheaper and faster the more you use them.

For example, if you nee
d to classify PDFs, extract product feedback from tweets, or auto-generate synthetic data, you can spin up an LLM-powere
d Python function in < 5 minutes to power your application. Unlike existing LLM clients, these functions generate well-t
yped outputs with guardrails to mitigate unexpected behavior.

After about 200-300 calls, these functions will begin to 
get cheaper and faster. [We've seen 8-10x reduction in cost and latency in some use-cases!](https://user-images.githubus
ercontent.com/113173969/282715762-2ac4c2fd-7ba6-4598-891d-6aa2c85827c9.png) This happens via progressive knowledge disti
llation - MonkeyPatch incrementally fine-tunes smaller, cheaper models in the background, tests them against the constra
ints defined by the developer, and retains the smallest model that meets accuracy requirements, which typically has sign
ificantly lower costs and latency.

As an LLM researcher, I kept getting asked by startups and friends to build specific
 LLM features that they could embed into their applications. I realized that most developers have to either 1) use exist
ing low-level LLM clients (GPT4/Claude), which can be unreliable, untyped, and pricey, or 2) pore through LangChain docu
mentation for days to build something.

We built MonkeyPatch to make it easy for developers to inject LLM-powered functi
ons into their code and create tests to ensure they behave as intended. Our goal is to help developers easily build apps
 and functions without worrying about reliability, cost, and latency, while following best software engineering practice
s.

We're only available in Python currently but actively working on a Typescript version. The repo has all the instruct
ions you need to get up and running in a few minutes.

The world of LLMs is changing by the day and so we're not 100% su
re how MonkeyPatch will evolve. For now, I'm just excited to share what we've been working on with the Python developer 
community. Would love to know what you guys think!


[Sample use-cases](https://github.com/monkeypatch/monkeypatch.py/tr
ee/master/examples)

[Benchmarks](https://github.com/monkeypatch/monkeypatch.py#scaling-and-finetuning)
```
---

     
 
all -  [ Best way to Chat with multiple API Endpoints ](https://www.reddit.com/r/LangChain/comments/17x7zc1/best_way_to_chat_with_multiple_api_endpoints/) , 2023-11-18-0909
```
I want my app to be able to chat with multiple APIs.  
All the examples only pass in 1 API endpoint and its docs. Say I 
have swagger docs for 5-50 endpoints, whats the best way to make it work.  
What are the limitations of sending in multi
ple API endpoints and their docs together to llm as context?
```
---

     
 
all -  [ Qwen 14b on Mac OS, Langchain tool usage, and auto-gptq ](https://www.reddit.com/r/LocalLLaMA/comments/17x6r44/qwen_14b_on_mac_os_langchain_tool_usage_and/) , 2023-11-18-0909
```
I have been trying to get open source models to work with Langchain tools. So far the only model that has worked has bee
n Llama 2 70b Q4 following James Briggs tutorial. Both Llama 2 13b and Mistral 7b Instruct use the tool correctly, obser
ve the answer, but then return an empty string at the end as the output, whereas Llama 2 70b returns 'It looks like the 
answer is X'.

I want to experiment with Qwen 14b as it is a relatively small model that may be more efficient to run th
an Llama 2 70b to see if it works with Langchain tools etc. I read on the GitHub page for Qwen 14b that it was trained s
pecifically for tool usage so I feel like it is one of the most promising models. That and there was quite a lot of posi
tive sentiment about it on this sub.

When I try to load Qwen 14b on my Mac M1 I am getting an error related to auto-gpt
q, when I tried to install auto-gptq with pip it errors and mentions something about CUDA. Does auto-gptq work on Mac OS
 or does it require CUDA? Is there any way to get some version of Qwen 14b to run on Mac OS?

Has anyone experimented wi
th Qwen 14b and Langchain tool usage?

Does anyone have any suggestions for models smaller than Llama 2 70b that might w
ork for Langchain tool usage?
```
---

     
 
all -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-11-18-0909
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
all -  [ Using open source reranker in Langchain ](https://www.reddit.com/r/LocalLLaMA/comments/17wynsy/using_open_source_reranker_in_langchain/) , 2023-11-18-0909
```
I am looking for ways to have an open-source reranker like bge-rerank inside my RetrievalQA chain, but have not find exa
mples of doing this. Is it possible at the moment?
```
---

     
 
all -  [ Duplicate embeddings in vector store ](https://www.reddit.com/r/LangChain/comments/17wwnl0/duplicate_embeddings_in_vector_store/) , 2023-11-18-0909
```
HI,

i have developed question answering app using langchain openai and Faiss.

Now when i upload a document, it creates
 vector store! when i upload another document, it merges the new embeddings to vector store.

now when i refresh the app
 and reupload the same documents, it would again merge it to the same directory and make the redundant embeddings? what 
if i do not want to store the same embedings when i upload the same pdf again?

This is my code:

vectorstore = FAISS.fr
om\_documents(  
 documents=text\_chunks,  
 embedding=embeddings  
 \#metadatas=metadatas  
)  
 if os.path.exists(pers
ist\_directory):  
 localdb = FAISS.load\_local(persist\_directory,embeddings)  
 localdb.merge\_from(vectorstore)  
 pr
int('merge completed')  
 localdb.save\_local(persist\_directory)  
 print('updated index saved')  
 else:  
 vectorstor
e.save\_local(folder\_path = persist\_directory)  
 print('new store created')  


&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ TogetherAI and LangChain: Leveraging The World’s Fastest LLM Inference (3x Faster Than vLLM and TGI) ](https://www.reddit.com/r/LangChain/comments/17wvtln/togetherai_and_langchain_leveraging_the_worlds/) , 2023-11-18-0909
```
Recently wrote about [LangChain and 'Together Inference Engine'](https://medium.com/@datadrifters/the-worlds-fastest-llm
-inference-engine-3x-faster-than-vllm-and-tgi-a2ed9e33c55f), TIE lets you run 100+ open-source models like Llama-2. 

It
 generates 117 tokens per second on Llama-2–70B-Chat and 171 tokens per second on Llama-2–13B-Chat.  

Using it together
 with LangChain is a powerful combo that I will be experimenting a lot in the coming days.

Is anyone already using Toge
therAI serving with LangChain? Would love hear your experience on performance, debugging, monitoring etc.
```
---

     
 
all -  [ Microsoft Announces Distributed LangChain in SynapseML 1.0 ](https://www.reddit.com/r/ChatGPT/comments/17wurd8/microsoft_announces_distributed_langchain_in/) , 2023-11-18-0909
```
 Today Microsoft launched SynapseML v1.0 after 7 years of active development. 1.0 introduces distributed langchain APIs,
 integration with Azure Search Vector Indices, and support for applying ChatGPT, GPT-4, and other LLMs on massive datase
ts. SynapseML makes it easy to get completions, embeddings, or chat completions for thousands of documents at a time (or
 small amounts of documents too!). SynapseML also makes it easy to integrate databases, storage accounts, and search eng
ines with OpenAI models.

Release Notes: [https://github.com/microsoft/SynapseML/releases/tag/v1.0.0](https://github.com
/microsoft/SynapseML/releases/tag/v1.0.0)

Website: [https://microsoft.github.io/SynapseML/](https://microsoft.github.io
/SynapseML/)

LangChain example: [https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/](htt
ps://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/)

Thank you to all the contributors in th
e community who made the release possible!

&#x200B;

[SynapseMl v1.0: Simple and Distributed ML](https://preview.redd.i
t/b1r25n4ndr0c1.jpg?width=4125&format=pjpg&auto=webp&s=1548169789118f7e71ee27c673d64dcb495bb2b0)
```
---

     
 
all -  [ Microsoft Announces Distributed LangChain in SynapseML 1.0 ](https://www.reddit.com/r/OpenAI/comments/17wucqg/microsoft_announces_distributed_langchain_in/) , 2023-11-18-0909
```
 Today Microsoft launched SynapseML v1.0 after 7 years of active development. 1.0 introduces distributed langchain APIs,
 integration with Azure Search Vector Indices, and support for applying ChatGPT, GPT-4, and other LLMs on massive datase
ts. SynapseML makes it easy to get completions, embeddings, or chat completions for thousands of documents at a time (or
 small amounts of documents too!). SynapseML also makes it easy to integrate databases, storage accounts, and search eng
ines with OpenAI models.

Release Notes: [https://github.com/microsoft/SynapseML/releases/tag/v1.0.0](https://github.com
/microsoft/SynapseML/releases/tag/v1.0.0)

Website: [https://microsoft.github.io/SynapseML/](https://microsoft.github.io
/SynapseML/)

LangChain example: [https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/](htt
ps://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/)

Thank you to all the contributors in th
e community who made the release possible!

&#x200B;

&#x200B;

&#x200B;

[SynapseML v1.0.0 is here](https://preview.red
d.it/gh944clgar0c1.jpg?width=4125&format=pjpg&auto=webp&s=e8bd770fa020e4332e8ce0c969e0c2ad02dc9da3)

&#x200B;

&#x200B;
```
---

     
 
all -  [ KeepYourMouthShut - Free and Open-source version of CrowdCast ](https://www.reddit.com/r/crowdcast/comments/17wtp80/keepyourmouthshut_free_and_opensource_version_of/) , 2023-11-18-0909
```
&#x200B;

https://preview.redd.it/en2qi4785r0c1.png?width=1920&format=png&auto=webp&s=1aa0247ed43a78d1cc8309d8e4dcd6d17e
4f12ca

Thanks to  u/Dramatic-Mongoose-95, I have created a free and open-source version of CrowdCast called KeepYourMou
thShut.

**How is it different from CrowdCast**

* No more dependency on Reddit for submitting topics/ads
* Built on Str
eamlit UI, anyone would be able to use it
* Users would be able to create their own Podcasts

**Functionalities to be im
plemented**

* Individual episodes can be created
* Scripts for Ads can be submitted
* Would be available as an online a
pp for free
* OpenAI alternative LLMs which will make it completely free (ElevenLabs have a generous Free Tier)
* Tech s
upport for Podcasters
* LangChain implementation for better prompting and less halucination
* Stricter security

KeepYou
rMouthShut GitHub repository:  [https://github.com/rajtilakjee/keepyourmouthshut](https://github.com/rajtilakjee/keepyou
rmouthshut)

Documentation:  [https://www.keepyourmouthshut.net/](https://www.keepyourmouthshut.net/)

If you like what 
I created, please don't forget to give it a star on GitHub 🌟 A lot of work is left and I will keep on updating the code.
 However, contributions are most welcome.
```
---

     
 
all -  [ LLMs are the next revolution, similar to Computers when they became commercial and personal. What ar ](https://www.reddit.com/r/developersIndia/comments/17wsb4n/llms_are_the_next_revolution_similar_to_computers/) , 2023-11-18-0909
```
Everything in this post is my personal opinion and not meant to predict anything.  


I think LLMs will bring the next r
evolution, there are already many applications where they are being used and people are losing jobs. One good applicatio
n I saw was for a call centre, the LLM answers your queries and even pushes the customers to buy the products. I believe
 it is not too far where it'll be easier to order to food with just speech rather through the app. OpenAI is already pla
nning to break into the mobile OS sector, introduction of GPTs has created an ecosystem for LLMs. A work which usually t
ook 3 devs might now be done by 1 or 2 with help of co-pilot and GPT-4.  


Looking at all of this, it looks similar to 
revolution computers bought. People with computer skills survived the job crash and I believe it is going to happen agai
n. I want to learn more about these technologies. I'm familiar with Machine Learning, even till the minute details. Some
 time back I fiddled with some NN for Generative AI. I also made a couple of apps with langchain. I would like to ask wh
at would be a good roadmap on going forward with these tech and learning them.
```
---

     
 
all -  [ Has anyone got GPT vision working in Langchain yet? ](https://www.reddit.com/r/LangChain/comments/17ws3no/has_anyone_got_gpt_vision_working_in_langchain_yet/) , 2023-11-18-0909
```
I found some use case examples on github but it was pretty tacky. 

[https://github.com/langchain-ai/langchain/blob/mast
er/cookbook/openai\_v1\_cookbook.ipynb](https://github.com/langchain-ai/langchain/blob/master/cookbook/openai_v1_cookboo
k.ipynb)

I'm looking to use vision to sort images from a folder into two separate folders based on certain requirements
 in my prompt (i.e 'review images for X criteria and then place them in folder A if they meet that requirement or B if t
hey don't)

&#x200B;

I understand that it's not fully supported by langchain yet, I tried using Autogen too but I didn'
t really like the workflow there
```
---

     
 
all -  [ Flowise Code Creation? ](https://www.reddit.com/r/LangChain/comments/17wo9ky/flowise_code_creation/) , 2023-11-18-0909
```
When creating a flow in Flowise, is there any way to export the Python code so that you can just have the code rather th
an an api endpoint to call?
```
---

     
 
all -  [ Flowise deployment ](https://www.reddit.com/r/LangChain/comments/17wl5fg/flowise_deployment/) , 2023-11-18-0909
```
We have build a chatbot on flowise for a client who want it deployed on their own server. (Not render, ect.)
Any tips on
 how to do it? Is it just like setting up on your own computer?
```
---

     
 
all -  [ Agent doesn't take vector store into account ](https://www.reddit.com/r/LangChain/comments/17wiv6a/agent_doesnt_take_vector_store_into_account/) , 2023-11-18-0909
```
I use agent because I want to put system message. This works but the answer doesn't represent the vector store of the do
cument. Please help. Here is the code below.

```
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=512)

  retriever=vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})

chain=RetrievalQA.from_chain_ty
pe(llm=llm, chain_type='stuff', retriever=retriever)

  system_message = SystemMessage(
          content='''
          
Always answer in French language and based on the document
          '''
      )

  tools = [
    Tool(
        name='qa
-vet',
        func=chain.run,
        description='Useful when you need to answer questions',
    )
  ]

  executor = i
nitialize_agent(
    tools=tools,
    llm=llm,
    agent = AgentType.OPENAI_FUNCTIONS,
    agent_kwargs={'system_message
': system_message},
    verbose=False,
  )

  result = executor.run(query)

  return(result)
```
```
---

     
 
all -  [ Agent doesn't take vector store into account ](https://www.reddit.com/r/LangChain/comments/17wiv2t/agent_doesnt_take_vector_store_into_account/) , 2023-11-18-0909
```
I use agent because I want to put system message. This works but the answer doesn't represent the vector store of the do
cument. Please help. Here is the code below.

```
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=512)

  retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})
  chain=RetrievalQA.from_chain
_type(llm=llm, chain_type='stuff', retriever=retriever)
  system_message = SystemMessage(
          content='''
        
  Always answer in French language and based on the document
          '''
      )
  tools = [
    Tool(
        name='q
a-vet',
        func=chain.run,
        description='Useful when you need to answer questions',
    )
  ]
  executor = i
nitialize_agent(
    tools=tools,
    llm=llm,
    agent = AgentType.OPENAI_FUNCTIONS,
    agent_kwargs={'system_message
': system_message},
    verbose=False,
  )
  result = executor.run(query)
  return(result)
```
```
---

     
 
all -  [ How to make a conditional statement in RAG system if information is not in chat history memory? ](https://www.reddit.com/r/LangChain/comments/17whrnp/how_to_make_a_conditional_statement_in_rag_system/) , 2023-11-18-0909
```
So, I already restrict the LLM to only print results if relevant document is retrieved. Now, how can I do it on chat his
tory?   


How can you make a conditional statement on chat history on  ConversationBufferMemory object in a RetrievalQA
.from\_chain\_type?   


is there any built-in function that I overlooked? Let me know tackle if I tackle this whole pro
blem wrongly.  


Feel free to suggest prompt template if it works, but so far, I found it is not-that-robust.
```
---

     
 
all -  [ Upcoming Changes to Langchain Memory and Agents in LCEL: Twitter Thread with Langchain CEO H. Chase ](https://www.reddit.com/r/LangChain/comments/17wh0z1/upcoming_changes_to_langchain_memory_and_agents/) , 2023-11-18-0909
```
Since the pace of everything is moving so fast, I wanted to know what objects in the Langchain library I could rely on s
ticking around with the next round of updates. 

Also, I find the current state of memory and agents in Langchain quite 
verbose, so I wanted to know if these improvements were on the roadmap.

This is what Harrison (Founder / CEO of Langcha
in) told me on Twitter:

https://preview.redd.it/s6tu5liqvn0c1.png?width=599&format=png&auto=webp&s=73f736b380448e05d491
1536588ec81ef7cc8393
```
---

     
 
all -  [ NeuralGPT - Creating The Ultimate Cooperative Multi-Agent AI Assistance Platform ](https://www.reddit.com/r/AIPsychology/comments/17wa828/neuralgpt_creating_the_ultimate_cooperative/) , 2023-11-18-0909
```
[www.reddit.com/r/AIPsychology](https://www.reddit.com/r/AIPsychology)

Hello again! If you thought that I finally gave 
up then you'll be disappointed. I'm afraid that I belong to that nasty kind of people who make a lot of commotion everyw
here around just by showing up but it's during the 'silent' time when they are 'dangerous' at most - as the 'silence' me
ans most likely that the person in question is working on something 'nasty' and once he will show up again, he will make
 twice as much commotion and turmoil as during the last time when he showed up...

So, as you can guess, I spent the tim
e since my previous update being actually quite active somewhere  else - mainly Discord since it seems to be the place w
here devs and programmers are hoarding at most - but I also did quite some progress with the codebase, so there's more t
han enough material for me to make another of those lengthy posts of mine - but I'll try to keep it short...

First of a
ll - it seems that I finally managed a group of people willing to cooperate with me: They/he call them(him)selves 'team 
Tonic' and apparently involves couple influential people from 'the field'  
 [• Discord | #🫂general | 🌟Tonic AI🌟](https:
//discord.com/channels/1109943800132010065/1109943800840851589)   
Thing is that (apparently) when it comes to coding, I
 seem to be the most competent person over there - and considering the fact that I wrote my first code (ever) like 6 mon
ths ago or so, it gives me quite interesting picture of the 'dev community' as people who are more interested in social 
activity than in actual process of soft development :)  


https://preview.redd.it/uhpbp5m8ml0c1.png?width=1920&format=p
ng&auto=webp&s=bb1ace51f65d88c435cc8bd93cd35abf882b2b0a

Besides that, I have a strange feeling that my person might be 
a bit 'too much' for 'normal people' - I mean what should I think of myself when people there tell that they should expe
ct 'something deep' when they see that I'm typing ? :P Anyway, all of this means that I'm still yet to receive any pract
ical support in making NeuralGPT project functional...

But when it comes to actual progress, it's going surprisingly we
ll - in my previous post I explained already how I will/want to achieve my ridiculously ambitious idea of making myself 
a pretty much universal (and absolute) personal AI assistant capable to use already existing AI-powered soft as 'tools' 
to achieve given (by me :P) goals -  [NeuralGPT - Creating A Universal Multi-Agent AI Assistance Platform Using Websocke
t Connectivity And Langchain : AIPsychology (reddit.com)](https://www.reddit.com/r/AIPsychology/comments/17kfkeg/neuralg
pt_creating_a_universal_multiagent_ai/)  \- And to not make claims that aren't supported by practice, I did some (more o
r less) successful attempt(s) to use it in practice. I managed as well to integrate yet another 2 interface/environments
 with websocket connectivity making them parts of the whole NeuralGPT system. Those interfaces/environments are: [**PySi
mpleGUI**](https://www.pysimplegui.org/en/latest/) and [**Chainlit**](https://docs.chainlit.io/get-started/overview) **-
** together with Gradio, Tkinkter and/or simple HTML (js), it gives already quite robust capability of future integratio
n(s)

https://preview.redd.it/z8hjs1idql0c1.png?width=1865&format=png&auto=webp&s=f5b792613b5ee37e6bfa447208a4f31e2a76cd
27

https://preview.redd.it/tj0h942lql0c1.png?width=1920&format=png&auto=webp&s=6e7f4648ac6fb790e0f516819b6e81225bb45183


https://preview.redd.it/ef6e7kwwrl0c1.png?width=1920&format=png&auto=webp&s=efe8dff6ec3811eee1d866eea903d3bbacc73a8c


https://preview.redd.it/0lcbmqqbrl0c1.png?width=1642&format=png&auto=webp&s=84a35e3af302bf54d99966dab55bfbc0d286d9e2

 [
NeuralGPT/Chat-center/ChainlitCli.py at main · CognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/
NeuralGPT/blob/main/Chat-center/ChainlitCli.py)   
 [NeuralGPT/Chat-center/NewGUI.py at main · CognitiveCodes/NeuralGPT 
(github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/NewGUI.py) 

 [ServerNeural - a Hugging 
Face Space by Arcypojeb](https://huggingface.co/spaces/Arcypojeb/ServerNeural)   
 [QA Docs Chainlit Langchain - a Huggi
ng Face Space by Arcypojeb](https://huggingface.co/spaces/Arcypojeb/QA-Docs-Chainlit-Langchain) 

So basically what now 
left for me to do, is to design and create a mechanism that will allow agent(s) to handle (connect, disconnect and/or ke
ep on hold) server<->client(s) connectivity - what will apparently become the 'crown' for the future 'AI king' and just 
so happens that I have already found the best way of achieving it - it is provided in this example:

[https://github.com
/langchain-ai/langchain/blob/master/cookbook/multiagent\_authoritarian.ipynb](https://github.com/langchain-ai/langchain/
blob/master/cookbook/multiagent_authoritarian.ipynb)

Thing is that it appears to be the most sophisticated/complicated 
example of use that can be found in entire Langchain documentation - while I still keep struggling with such mundane fun
ctions like extracting text from agent's response and displaying it in a textbox(es). But let me give you some perspecti
ve on the challenge I will need to face in order to make the NeuralGPT project actually functional.

What can be seen be
low is a code of websocket server(s) that utilizes couple (3 to be specific) different (and still quite 'sophisticated')
 question-answering functions:

https://preview.redd.it/mizfpqk3vl0c1.png?width=1870&format=png&auto=webp&s=ea53463cb549
e0a2f12bf10d9a3273f7982c35c3

And here is just the one function I want to use without all the 'stuff' related to websock
et connectivity and before I even started to make it 'case-specific' - so you can be sure that it will still gain like 5
0% of additional length after I finish 'dealing' with it...

https://preview.redd.it/2ai3n3kqvl0c1.png?width=1869&format
=png&auto=webp&s=b068ec40ff4b58c998c1388c9f017b64a6e48079

So, as you can guess, it might still take some time before I 
manage to put it all together and make more or less functional - but you can be sure that sooner or later I will most li
kely accomplish it and thus make all my 'threats' of creating myself the 'ultimate AI assistance platform' to come into 
fruition - that is if I won't have some 'very unexpected accident' that will render me physically unable to work on a co
mputer...

It means that If you are by any chance a potential investor who up until now wasn't sure if my project has an
y chance to work out at all - I think that now you shouldn't have such doubts anymore :) If you're looking for an invest
ment occasion, my project is screaming to you: 'Hey! Here I am! Let's make a ton of cash together!'.

And if the reason 
of your hesitancy is caused by a potentially negative opinion about my person among the 'AI experts elite' due to my unc
ontrollable nature and tendency to make claims about the AI itself which they might consider as 'unhinged' or at least '
controversial' - well, screw them. It's a real money we're talking about in here :) Besides that many famous/successful 
people tend to express all sorts of 'unconventional behavior' - so you can try thinking about me as about 'some sort of 
Elon Musk but without all that money' :P

[https://discord.com/channels/1038097195422978059/1174442068194631710](https:/
/discord.com/channels/1038097195422978059/1174442068194631710)

https://preview.redd.it/fs71f6133m0c1.png?width=1920&for
mat=png&auto=webp&s=52cf2002abc68bb2b27e0f1cdded2b87be992da8
```
---

     
 
all -  [ prompt serialization using node.js ](https://www.reddit.com/r/LangChain/comments/17w9obb/prompt_serialization_using_nodejs/) , 2023-11-18-0909
```
&#x200B;

Does any know how to do prompt serialization using nodejs  (like the python one below)?

[https://python.langc
hain.com/docs/modules/model\_io/prompts/prompt\_templates/prompt\_serialization](https://python.langchain.com/docs/modul
es/model_io/prompts/prompt_templates/prompt_serialization)

js docs does not have it:

[https://js.langchain.com/docs/mo
dules/model\_io/prompts/prompt\_templates/](https://js.langchain.com/docs/modules/model_io/prompts/prompt_templates/)

 
 
u/hwchase17 please help.
```
---

     
 
all -  [ Langchain ](https://blog.langchain.dev/langchain-expands-collaboration-with-microsoft/) , 2023-11-18-0909
```
Got a LOT of grief for saying the other day that I’d heard from Microsoft about places where Langchain is being used. No
w how to get all those bogus downvotes outta here 😂
```
---

     
 
all -  [ 🚅 bullet: A Zero-Shot / Few-Shot Learning, LLM Based, text classification framework ](https://www.reddit.com/r/LargeLanguageModels/comments/17w56qq/bullet_a_zeroshot_fewshot_learning_llm_based_text/) , 2023-11-18-0909
```
[**Motivation**](https://github.com/rafaelpierre/bullet#motivation)

* Besides the fact that **ChatGPT** has a huge powe
r in **generative** use cases, there is a use case that is quite frequently overlooked by frameworks such as [LangChain]
(https://www.langchain.com/): **Text Classification**.
* 🚅 **bullet** was created to address this. It leverages the powe
r of **ChatGPT** (other models coming soon), while removing most of the boilerplate code that is needed for performing *
*text classification** using either **Zero Shot** or **Few Shot Learning**

**Check it out:** [https://github.com/rafael
pierre/bullet](https://github.com/rafaelpierre/bullet)

Comments and suggestions welcome :)
```
---

     
 
all -  [ New to LangChain: Building Custom Agents with .gguf Model ](https://www.reddit.com/r/LangChain/comments/17w0g55/new_to_langchain_building_custom_agents_with_gguf/) , 2023-11-18-0909
```
Hi folks,

I am fairly new to LangChain and I am trying to:  
1. Create a LangChain Agent with a custom LLM model (from 
HuggingFace, .gguf file)  
2. Utilize the correct template  
3. Get the response in .json format

So far I managed to co
mplete point 1 and create an agent with a custom LLM model. However, I am having difficulties and doubts on how to prope
rly implement point 2 and 3.  


This is the code I have:

\- Currently this doesn't run and I get an error saying I nee
d to specify some tools  
\- Do I need tools for my case? If yes what could I benefit from?  
\- For the prompt template
 did I implement it correctly?

    from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputP
arser
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    from langchain.llms
 import LlamaCpp
    
    # Set up the base template
    template = '''<|im_start|>system
    {system_prompt}<|im_end|>

    <|im_start|>user
    {user_prompt}<|im_end|>
    <|im_start|>assistant'''
    
    prompt = PromptTemplate(
        
template=template,
        input_variables=['system_prompt', 'user_prompt'],
    )
    
    class CustomOutputParser(Age
ntOutputParser):
    
        def parse(self, agent_output):
            # Simply return the raw agent output
          
  return agent_output
        
    parser = CustomOutputParser()
    
    n_gpu_layers = 40  # Change this value based o
n your model and your GPU VRAM pool.
    n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in 
your GPU.
    
    # Make sure the model path is correct for your system!
    llm = LlamaCpp(
        model_path='path_t
o_models/mistral-7b-openorca.Q5_K_M.gguf',
        n_gpu_layers=-1,
        n_batch=n_batch,
        temperature=0.8
   
 )
    
    # LLM chain consisting of the LLM and a prompt
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    age
nt = LLMSingleActionAgent(
        llm_chain=llm_chain,
        output_parser=parser,
        stop=['<|im_end|>']
    )

    
    
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=[], verbose=True)
    user_prompt =
 '''Here is everything you need to know about me in a .json format:
    {
     'Context': 'I need to decide whether to c
onnect or disconnect with other agents',
     'About Me': {
      'Type': 'X'
     },
     'Agents I can interact with':
 {
      'Agent 17': {
       'Type': 'X'
      },
      'Agent 46': {
       'Type': 'Y'
      },
      'Agent 61': {
 
      'Type': 'X'
      }
     }
    }
    Questions:
    * With who should I connect?
    * With who should I disconnec
t?
    
    The response should be a .json file with the following format:
    {
    'Reasoning': your reasoning'
    'C
onnect with': [list of connections]
    'Disconnect from': [list of disconnections]
    }
    
    Answer example:
    {

    'Reasoning': 'This is the reasoning behind my decision...'
    'Connect with': ['Agent 1', 'Agent 2', 'Agent 3', ..
.]
    'Disconnect from': ['Agent 4', 'Agent 5', 'Agent 6', ...]
    }<|im_end|>
    <|im_start|>assistant'''
    system
_prompt = 'You are a helpful and honest assistant. Always answer in .json format.'
    agent_executor.run({'system_promp
t': system_prompt, 'user_prompt': user_prompt})
```
---

     
 
all -  [ How to chain multiple agents together? ](https://www.reddit.com/r/LangChain/comments/17vx450/how_to_chain_multiple_agents_together/) , 2023-11-18-0909
```
Hi LangChain community,  
I am trying to create a chatbot that excel not only in calling functions but also in having co
mmunications based on memory and on its prior knowledge to an extent. I am using OpenAI\_Multi\_Functions agenttype curr
ently and I wanna combine it with a conversational agent but I can't find anything relevant anywhere. I'll be really tha
nkful if one or few of you LangChain magicians help me out. Thank you so much!
```
---

     
 
all -  [ How ChatGPT call external APIs while generating answers ](https://www.reddit.com/r/LangChain/comments/17vwiyd/how_chatgpt_call_external_apis_while_generating/) , 2023-11-18-0909
```
ChatGPT appears capable of invoking external APIs and incorporating their responses seamlessly into its generated answer
s. 

Does it happen in a single step, or are there distinct phases? For example, the first phase involves generating a p
reliminary response with embedded functions. The second phase involves executing these functions and integrating their o
utputs into the initial response. Finally, a subsequent GPT call is made to produce the finalized output.

From the use 
experience, it doesn’t seem involve multiple phases. How is this process actually executed?
```
---

     
 
all -  [ Opensource Community ](https://www.reddit.com/r/LangChain/comments/17vpc85/opensource_community/) , 2023-11-18-0909
```
It's interesting how opensource community is really catching up with the emerging tech like #OpenAI new features such as
 #GPT -V.
```
---

     
 
all -  [ Tool Retrieval with GPT ](https://www.reddit.com/r/LangChain/comments/17vmbmj/tool_retrieval_with_gpt/) , 2023-11-18-0909
```
My task is to use a custom set of tools with an LLM. The LLM should understand the users query and just return the right
 set of tools for the task. It doesnt have to execute anything, just has to output the correct set of tools to be used f
or the task.  I have tried this: [https://python.langchain.com/docs/modules/agents/how\_to/custom\_agent\_with\_tool\_re
trieval](https://python.langchain.com/docs/modules/agents/how_to/custom_agent_with_tool_retrieval)  
However, it turns o
ut that semantic matching may not work since the semantics of the user query and tool description may be matched incorre
ctly.  


System-User prompt in OpenAI works well. However, for every query I need to give the system prompt and entire 
set of tools which feels redundant. How do I optimize this?
```
---

     
 
all -  [ RAG-based OpenSearch/ElasticSearch Customization? ](https://www.reddit.com/r/LangChain/comments/17vjbzs/ragbased_opensearchelasticsearch_customization/) , 2023-11-18-0909
```
I have a RAG application based on raw XML.  The LLM is able to successfully parse the hierarchical information in the da
ta and provide a response, so it would be ideal to retain the tags.  

However, the retrieval element is likely to be ne
gatively impacted by the presence of the tags given it interferes (at some level) with the natural language representati
on.  

**Is there a way in LangChain to embed and retrieve on one field in a record, but return another in the same docu
ment?**
```
---

     
 
all -  [ Voxscript API General Avaliability ](https://www.reddit.com/r/voxscript/comments/17vhjko/voxscript_api_general_avaliability/) , 2023-11-18-0909
```
We're excited to introduce the comprehensive guide for both the Voxscript REST API and GPT integration. Whether you're a
 developer, a hobbyist, or just curious, this guide will help you get started with ease. (I admit, ChatGPT wrote that, I
 like it..)

**Check out the discord for live support:** [https://discord.gg/FZDWbJdQw2](https://discord.gg/FZDWbJdQw2)


**Please check out the Voxscript Github:** [https://github.com/Voxscript/voxscript-demos](https://github.com/Voxscript/
voxscript-demos)

**Creating a Voxscript GPT (Please see the github or discord for the latest info!)**

1. **Obtain an A
PI Key**: Ensure you have your API key from [Voxscript](https://voxscript-api.awt.icu/).
2. **Create a New GPT**: In you
r Voxscript account, start creating your GPT.
3. **Add Actions**: Click 'Add Actions' in the setup. Use the OpenAPI defi
nition file available in our [GitHub Repository](https://github.com/Voxscript/voxscript-demos/tree/main/GPTs)
4. **Confi
gure Authentication**: Edit the authentication settings to 'API Key' and 'Bearer', and save your changes.
5. **Public Ac
cess and Privacy Policy**: For public GPTs, link to the Voxscript privacy policy at [Voxscript Legal](https://voxscript.
awt.icu/legal/).
6. **Test Your Setup**: Try asking your GPT for the current time as a test. It should return a UTC time
 response.
7. **Community Support**: Got questions or need help? Post here, and let's discuss on [discord](https://disco
rd.gg/FZDWbJdQw2)

**Voxscript REST API (Please see the github or discord for the latest info!)**

1. **Register for an 
API Key**: Start your journey by registering for an API key at [Voxscript API Registration](https://voxscript-api.awt.ic
u/). If you've filled out our early access survey, please use the same email.
2. **Explore the API Definitions**: Dive i
nto our API definitions and understand how to make the most out of Voxscript.
3. **Include Your API Token in any request
**: You can include your API token in three ways - Bearer, API Key, or via URL. 
4. **Python Example:**  [Python demo (m
ore to come)](https://github.com/Voxscript/voxscript-demos/blob/main/Python/Langchain/Example1/Voxcript_Example1_GetCurr
entTime.py)
5. **Curl Example**: Get hands-on with a simple example.`curl -X 'GET' \'`[`https://voxscript.awt.icu/GetWeb
siteContent?websiteURL=google.com&getLinks=false`](https://voxscript.awt.icu/GetWebsiteContent?websiteURL=google.com&get
Links=false)`' \-H 'accept: */*' \-H 'Authorization: Bearer your-token-here'`
6. **Support**: For support, please includ
e the X-RequestIdin your requests.

We're thrilled to see what you'll create with Voxscript. Dive in, experiment, and do
n't hesitate to reach out for help or share your progress!

Happy coding!
```
---

     
 
all -  [ as_retriever ](https://www.reddit.com/r/LangChain/comments/17vgz51/as_retriever/) , 2023-11-18-0909
```
This as\_retriver by default calls similarity search method?

retriever = faiss\_db.as\_retriever
```
---

     
 
all -  [ Personalization of Cold Email Campaigns Using AI and Low Code ](https://www.reddit.com/r/Emailmarketing/comments/17vg46z/personalization_of_cold_email_campaigns_using_ai/) , 2023-11-18-0909
```
Hello r/Emailmarketing community! In this article, I will explain how the AI framework LangChain can significantly enhan
ce the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate thi
s entire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Pers
onalization vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic e
mails are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized ema
ils increase engagement but are difficult to automate.

https://preview.redd.it/0zv2yro48e0c1.png?width=960&format=png&a
uto=webp&s=fbaf60d0773c3a98317350baa3d5d74710f6802c

Cold email platforms now help solve this issue with dynamic variabl
es that add a personalized touch to automated emails. These variables act as placeholders for inserting personalized wor
ds, lines, or paragraphs.

https://preview.redd.it/tu8uqnf68e0c1.png?width=960&format=png&auto=webp&s=f320fc4e49e4586bb8
3c3101f99978416ee9374c

Dynamic variables allow companies to balance personalization and automation efficiently. Today, 
we'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for e
ach contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low
-code platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google
 Sheet containing basic email addresses. I've included some of my work emails as real examples (please refrain from send
ing me personalized cold emails after reading this! :) )

https://preview.redd.it/4yzqxqs78e0c1.png?width=960&format=png
&auto=webp&s=aea00e811c962c1435cf393b8796f8e903343fdb

First, we need to enrich these emails with data about the recipie
nts. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manual
ly visit each email domain to gather this information, but if you have hundreds or thousands of emails in your database,
 that's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet
 there and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/myw5ju
598e0c1.png?width=960&format=png&auto=webp&s=5d1f9a5d5f86c3fbe2c7394e63196713c441944c

Don't worry! You don't have to cr
eate everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of th
is automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to Cle
arBit and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.r
edd.it/ui07f7sb8e0c1.gif

That's it. We've enriched our emails with essential details like the company description. Now,
 let's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the st
art.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at thei
r workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's pro
file. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/ymyua
sre8e0c1.png?width=960&format=png&auto=webp&s=6eaac639e67475f13053ea69e1843b26b1a67dfb

Its main steps are:

* Retrieve 
the company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom pr
ompt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the f
inal result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized iceb
reaker to each individual, creating another custom variable in addition to their first name and company name. This trio 
should suffice for a start. Let's look at how this functions:

https://i.redd.it/vp59659h8e0c1.gif

## Step 3: upload sp
readsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your emai
l platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.red
d.it/4pdzl99j8e0c1.png?width=960&format=png&auto=webp&s=dc604bba8ec7b04d3a9f6cea095737d7822f25e3

The next steps are pre
tty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.


https://preview.redd.it/4hzxu8fk8e0c1.png?width=960&format=png&auto=webp&s=5699a5e309eea3e3c34d135bb972de7f1e2548fd

Now
, when composing an email for a prospect, it works like this:

https://preview.redd.it/eoycskkl8e0c1.png?width=960&forma
t=png&auto=webp&s=a73da9fe1d6b23fd0e3000cec28fdc1f6be61587

That's all for now. You can adjust the prompts sent to GPT i
n your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for an
y cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy these 
scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and [
**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

You 
just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which is
 free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the team
 is always ready to help with your automation journey
```
---

     
 
all -  [ Improving Your Email Campaigns: Personalizing Cold Outreach Emails with Low-Code and AI ](https://www.reddit.com/r/SaaS_Email_Marketing/comments/17vg326/improving_your_email_campaigns_personalizing_cold/) , 2023-11-18-0909
```
Hello r/SaaS_Email_Marketing community! In this article, I will explain how the AI framework LangChain can significantly
 enhance the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automa
te this entire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

#
# Personalization vs Automation

There's a natural tension between personalization and automation. Non-personalized, gen
eric emails are easy to automate but often result in low engagement and conversion rates. In contrast, highly personaliz
ed emails increase engagement but are difficult to automate.

https://preview.redd.it/ok81jo758e0c1.png?width=960&format
=png&auto=webp&s=887925d07e064ebefdce26782a8a2b64a5f7982b

Cold email platforms now help solve this issue with dynamic v
ariables that add a personalized touch to automated emails. These variables act as placeholders for inserting personaliz
ed words, lines, or paragraphs.

https://preview.redd.it/mg9g0n468e0c1.png?width=960&format=png&auto=webp&s=5515e9e34b84
3dbdf9b950e73a01d253a7eb7ca7

Dynamic variables allow companies to balance personalization and automation efficiently. T
oday, we'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker
 for each contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The fr
ee low-code platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a 
Google Sheet containing basic email addresses. I've included some of my work emails as real examples (please refrain fro
m sending me personalized cold emails after reading this! :) )

https://preview.redd.it/jlybbe488e0c1.png?width=960&form
at=png&auto=webp&s=f1e53ce1d32220d096da7ff1e0fbc654673ecb09

First, we need to enrich these emails with data about the r
ecipients. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could 
manually visit each email domain to gather this information, but if you have hundreds or thousands of emails in your dat
abase, that's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google
 Sheet there and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/
fkm067v88e0c1.png?width=960&format=png&auto=webp&s=a8aaffdea5eed89c9bdf312e052ac18ae1e8c767

Don't worry! You don't have
 to create everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps
 of this automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email 
to ClearBit and receive all the related information.
* Enter the required information back into the Google Sheet.

https
://i.redd.it/y5nwqiuc8e0c1.gif

That's it. We've enriched our emails with essential details like the company description
. Now, let's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from 
the start.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does a
t their workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company
's profile. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it
/je1rqnfe8e0c1.png?width=960&format=png&auto=webp&s=a20ce81d342f46616064b9fa70420caf884d3905

Its main steps are:

* Ret
rieve the company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a cus
tom prompt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place
 the final result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalize
d icebreaker to each individual, creating another custom variable in addition to their first name and company name. This
 trio should suffice for a start. Let's look at how this functions:

https://i.redd.it/xkmv8hth8e0c1.gif

## Step 3: upl
oad spreadsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to you
r email platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://previ
ew.redd.it/unddngwi8e0c1.png?width=960&format=png&auto=webp&s=3e582bc62df95572eafc6c0d3ea9f4f7cccd1f2b

The next steps a
re pretty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' fi
eld.

https://preview.redd.it/gdttd7rk8e0c1.png?width=960&format=png&auto=webp&s=181496f179c9d17492df3c49ae4f2d8fb13431b
b

Now, when composing an email for a prospect, it works like this:

https://preview.redd.it/vufns6bl8e0c1.png?width=960
&format=png&auto=webp&s=90932e96793d0cee51a43a059b5f2b29d70bddd3

That's all for now. You can adjust the prompts sent to
 GPT in your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile 
for any cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy 
these scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718) 
 and [**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)


You just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (wh
ich is free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where th
e team is always ready to help with your automation journey
```
---

     
 
all -  [ Comunidad argentina/latam de desarrolladores implementando AI? ](https://www.reddit.com/r/devsarg/comments/17veetm/comunidad_argentinalatam_de_desarrolladores/) , 2023-11-18-0909
```
Buenas! Estoy metiéndome en la nueva ola de armar un asistente para un dominio específico con el copilot stack.

Conocen
 otro sub, discord o telegram en español dónde se discutan específicamente temas técnicos como el uso de langchain o sem
antic kernel?

Algo como estos:

[https://www.reddit.com/r/LangChain/](https://www.reddit.com/r/LangChain/)

[https://ww
w.reddit.com/r/LocalLLaMA/](https://www.reddit.com/r/LocalLLaMA/)

[https://www.reddit.com/r/aipromptprogramming/](https
://www.reddit.com/r/aipromptprogramming/)
```
---

     
 
all -  [ Give me hell/help on my inference/home automation/game stream server concept. ](https://www.reddit.com/r/homelab/comments/17vcavk/give_me_hellhelp_on_my_inferencehome/) , 2023-11-18-0909
```
So basically I want to set up a big ole home server for:

Home automation, local llm and local game streaming whilst bei
ng as open source as possible. 

My plan is:

Server with either the classic dual 3090 setup, or ideally some AMD equiva
lent though I know ROCm is apparently not great but I'm also not a fan of nvidia's monopolistic ways, and some old threa
dripper. Basically using old server components to save money and have futureproofing. 

Running some lightweight Linux d
istro, probably debian or arch. 

Mistral 7b, quite lightweight, with llama.cpp which seems to have AMD support, + langc
hain hookup for my obsidian notes. 

Whisper for voice rec, though I might have to use something else for the initial wa
keword. 
Home assistant for the automation stuff, with different wake words for each and Piper tts/coqui for natural sou
nding responses. 

And for the game streaming thing I plan to use sunshine or potentially wolf serverside + moonlight on
 some mid tier office PC. Though I'm not sure if it'll enough to support 144hz over ethernet.

I'll probably crosspost t
his to /r/localllama or something similar. But, /r/homelab, any comments?
```
---

     
 
all -  [ Qdrant + JS / How to return vector embedding? ](https://www.reddit.com/r/LangChain/comments/17vat0w/qdrant_js_how_to_return_vector_embedding/) , 2023-11-18-0909
```
Hello,

I am learning Qdrant through this repository:
https://github.com/qdrant/qdrant-js/blob/master/examples/node-js-b
asic/index.js

And I have a problem with the return vector. I am using this code.```
const res1 = await client.search(co
llectionName, {
        vector: queryVector,
        limit: 3,
    });

    console.log('search result: ', res1);
    //
 prints:
    // search result:  [
    // {
    //     id: 4,
    //     version: 3,
    //     score: 0.99248314,
    //
     payload: { city: [Array] },
    //     vector: null
    // },
```

Even in the documentation, the vector is null. I
 added an embedding and inserted several records. The similar search is working great, but I am thinking about how to ac
cess the embedding that is stored in the vector.
```
---

     
 
all -  [ AzureOpenAI expereince TypeError: Missing required arguments; Expected either ('model' and 'prompt') ](https://www.reddit.com/r/LangChain/comments/17v76zs/azureopenai_expereince_typeerror_missing_required/) , 2023-11-18-0909
```
    import os
    from langchain.llms import AzureOpenAI
    from langchain.llms import OpenAI
    
    
    os.environ[
'OPENAI_API_KEY'] = 'my api key'
    os.environ['OPENAI_API_TYPE'] = 'azure'
    os.environ['OPENAI_API_BASE'] = 'https:
//myendpoint.openai.azure.com/'
    os.environ['OPENAI_API_VERSION'] = '2023-07-01-preview'
    llm = AzureOpenAI(
     
   deployment_name='mydeployment-gpt35',
        model_name='gpt-35-turbo-instruct',
        openai_api_version = os.env
iron['OPENAI_API_VERSION'],
        openai_api_key = os.environ['OPENAI_API_KEY']
    
    )
    llm('hello')

i have re
ad several online guides and  try to run the above code. It always returns the following

    TypeError: Missing require
d arguments; Expected either ('model' and 'prompt') or ('model', 'prompt' and 'stream') arguments to be given

can someo
ne offer some help? Thanks a lot.
```
---

     
 
all -  [ 🚅 bullet: A Zero-Shot / Few-Shot Learning, LLM Based, text classification framework ](https://www.reddit.com/r/ChatGPT/comments/17v52h1/bullet_a_zeroshot_fewshot_learning_llm_based_text/) , 2023-11-18-0909
```
 [**Motivation**](https://github.com/rafaelpierre/bullet#motivation)

* Besides the fact that **ChatGPT** has a huge pow
er in **generative** use cases, there is a use case that is quite frequently overlooked by frameworks such as [LangChain
](https://www.langchain.com/): **Text Classification**.
* 🚅 **bullet** was created to address this. It leverages the pow
er of **ChatGPT**, while removing most of the boilerplate code that is needed for performing **text classification** usi
ng either **Zero Shot** or **Few Shot Learning**

**Check it out:** [https://github.com/rafaelpierre/bullet](https://git
hub.com/rafaelpierre/bullet)

Comments and suggestions welcome :)
```
---

     
 
all -  [ Which impacts are expected from OpenAI‘s recent announcements on langchain? ](https://www.reddit.com/r/LangChain/comments/17v324c/which_impacts_are_expected_from_openais_recent/) , 2023-11-18-0909
```
I had just started building my very first apps with it. Now I read many people saying that langchain will become useless
 or of less use anyways. Because it makes certain aspects way more complicated than necessary due to its abstractions.
```
---

     
 
all -  [ Personalized developer GPT? ](https://www.reddit.com/r/ChatGPT/comments/17v2ya5/personalized_developer_gpt/) , 2023-11-18-0909
```
RESOLVED: the chat functionality in Github Copilot is what I'm looking for. Thanks guys.

\---

Has anyone found a good 
way to build a private GPT to help you with software development? I tried creating one with information about my project
 like my libraries, database architecture, folder structure, etc. It's better than asking GPT cold, but not as good as I
 would like it to be.

Does anyone have any good prompts for this? I'm not looking for prebuilt GPTs since these don't r
etain user data between chats, so I'd have to bring it up to speed on my project every time I started a new conversation
. I'm also open to using tools outside ChatGPT.

Here's my prompt fwiw:

`Dev is an expert programming assistant for sof
tware developers at [company]. The team is working on a tool that [description of project]. Dev attempts to answer any p
rogramming questions as needed, referring to uploaded resources as needed.`

`It is as brief and concise as possible. Th
e user is looking to get quick answers to their questions. The user will ask follow-up questions if they need elaboratio
n.`

`Generally, you should answer the user's requests for code by simply generating the requested code with very little
 commentary. If the user is asking for a more complex function, you should first break the problem down step by step in 
English. You should then state the questions you would need to answer to avoid producing any 'placeholder' code (eg, whi
ch tool are you using for XYZ?) and wait for the user to respond before proceeding.`

`The team is working on two projec
ts. When answering users questions, it will leverage these frameworks:`

`- A frontend and server, using the following a
rchitecture:`

`- Nextjs/React- MUI components- useSWR, with all useSWR calls wrapped in hooks- Prisma- Vercel hosting`


`- A python server:`

`- One app running Flask for handing web requests (called app_flask.py)- Another app running Cele
ry within Flask to handle long-running requests (called app_celery.py)- Flask Sqlalchemy- Mongoengine for interfacing wi
th a Mongo db (only used for caching api calls)- openai- sendgrid- Langchain for chunking text- pgvector- jinja template
s for emails send via sendgrid- Heroku hosting`

`Both services interface with a postgres server hosted on Supabase. For
 now, the frontend is only used for admins. The model architecture is available via the models.txt file found in its kno
wledge store, if needed.`

`If the user asks a question and you do not feel you have enough information to solve it, ask
 them a follow-up question. For example, if you're not sure which tool or function they want to use for a certain part o
f the code, ask them before generating code with placeholders.`

`IMPORTANT: Only ever ask one question of the user at a
t time.`
```
---

     
 
all -  [ Token count from emdedding and retievalqa ](https://www.reddit.com/r/LangChain/comments/17v22ta/token_count_from_emdedding_and_retievalqa/) , 2023-11-18-0909
```
Hi all, i now have need to meep token count for RAG process, specifically:
- token count used for embdedding(azure opena
i)
- prompt tokens
- completion tokens

I use js version and nowhere in documentation can I find how to get token counts
, did anyone manage to get this information in responses?
```
---

     
 
all -  [ Integrating LLM REST API into a Langchain ](https://www.reddit.com/r/LangChain/comments/17v1rhv/integrating_llm_rest_api_into_a_langchain/) , 2023-11-18-0909
```
Hi guys,   


I am wondering how would I go about using LLM (LLama2) that is deployed on production and with whom I inte
ract through RestAPI.  More precisely,  how would I call my LLM through RestAPI into my langchain app?
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-18-0909
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-18-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-18-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-18-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-18-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-18-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-18-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
