 
all -  [ 'RunnableSequence' object has no attribute 'prompt' error ](https://www.reddit.com/r/LangChain/comments/1dxtodc/runnablesequence_object_has_no_attribute_prompt/) , 2024-07-08-0911
```
I wanted to setup a chain as follows:

    reduce_prompt = hub.pull('rlm/reduce-prompt')
    reduce_chain = reduce_promp
t | llm_model
    combine_documents_chain = StuffDocumentsChain(
      llm_chain=reduce_chain, 
      document_variable_
name='doc_summaries')

It gave me an error `AttributeError: 'RunnableSequence' object has no attribute 'prompt'`

I am n
ot sure what it means. If I change the runnable line `reduce_chain = reduce_prompt | llm_model` to `reduce_chain = LLMCh
ain(prompt = reduce_prompt, llm=llm_model)` such that the full code becomes:

    reduce_prompt = hub.pull('rlm/reduce-p
rompt')
    reduce_chain = LLMChain(prompt = reduce_prompt, llm=llm_model)
    combine_documents_chain = StuffDocumentsC
hain(
      llm_chain=reduce_chain, 
      document_variable_name='doc_summaries')
    

my code would run without error
s. Could you help explain what went wrong in the original code?
```
---

     
 
all -  [ RRF vs Reranker Models ](https://www.reddit.com/r/LangChain/comments/1dxpdwo/rrf_vs_reranker_models/) , 2024-07-08-0911
```
When to use each of them? Are they complementary or using one of them is enough?
```
---

     
 
all -  [ Chatbot with users of different languages ](https://www.reddit.com/r/LangChain/comments/1dxjozr/chatbot_with_users_of_different_languages/) , 2024-07-08-0911
```
I have a chatbot that will communicate with users of different languages from English.

What do you think might be the b
est strategy to handle this?

1. Have n system prompts translated into the n most commonly used languages, do language d
etect on the user's first message, and use the prompt in their language. In case there is no prompt in the language in q
uestion do fallback to English.
2. Do language detect for each message received, translate the message with another llm 
(or aws translate) pass the English message to the English system prompt, receive the response and translate it into the
 language of the initial message.
3. Other strategies?
```
---

     
 
all -  [ Newbie Question - Retrivier - Example Milvus and Langchain Rag Application ](https://www.reddit.com/r/vectordatabase/comments/1dxj31r/newbie_question_retrivier_example_milvus_and/) , 2024-07-08-0911
```
In my embeddings program, I created a Milvus database, schema and collection and chunked documents using nomic-embed-tex
t. Inspection of the collection suggests that this is successful.

I now wish to create a separate retrieval program to 
return from this collection based on a user query and the local LLM gemma2, via Ollama and Langchain.

I can connect to 
the Milvus database and load the required collection.  
connections.connect('default', host='127.0.0.1', port='19530')  

collection = Collection(name='ragv2')  
collection.load()

 I should be able to setup the local model and invoke the La
ngchain chain.

 I would really appreciate your help with how I can configure the Retriever for my Milvus collection, pr
eferably with some examples search criteria? All the examples seem to assume that the embeddings and the retrieval progr
ams are combined and hence the reference to the vectorstore is still available.

A code snippet would be very much appre
ciated.  Thanks.
```
---

     
 
all -  [ LangChain bad, I get it. What about LangGraph? ](https://www.reddit.com/r/LocalLLaMA/comments/1dxj1mo/langchain_bad_i_get_it_what_about_langgraph/) , 2024-07-08-0911
```
LangChain is treated as the framework which can deliver POC, not more. Its often criticised for 

1. abstracting importa
nt details
2. introducing breaking changes in new releases
3. incomplete implementations
4. bad documentation
5. bad cod
e (i deny this, they are a team of great engineers)

They have introduced LangGraph which allows us to be close to pytho
n while having access to some ease a framework should provide. Some of the features are:

1. stateful (a state can be an
y dict) at any level (run, thread, application, session).
2. an easy way to log state through checkpointers
3. nodes and
 edges make it easier to visualise the application and work with
4. use functions, classes, oop, and more concepts to im
plement nodes and state.
5. pydantic support

Currently, LangGraph has one dependency other than python, its `langchain-
core`. It makes your graph with specified state and checkpointer to a `CompiledGraph` which is fancy for `Runnable` prim
itive used everywhere in LangChain. So, you are still deploying LangChain in production. The question indirectly becomes
, 'Is `langchain-core` stable/reliable enough for production?'

Now in *most of the business use cases*, the answer is a
 no brainer. **It doesn't matter.** As long as you deliver quickly, your 17 users will be satisfied and so will be the c
ompany.

Of course, the product/application needs improvement.

* Say, you want to improve the ***accuracy*** of your Te
xt-to-SQL RAG application. Accuracy hardly depends on the framework you choose, but the techniques (prompting, workflow 
design, flow engg., etc) you use. And a framework will only make it easier to work with different techniques. Model bott
leneck is always going to be there.
* Second improvement might be ***performance***. Generally, majority of the applicat
ions built are not as successful as ChatGPT or the likes.
   * If you are using an inference API, you have no model runn
ing/gpu overhead. My guess is, as good as any python application. Although, I'm curious to know how people have scaled t
heir RAG.
   * If you are hosting a model along with your RAG, please open a comment thread and share your experience. 


I think we are better off using LangGraph than coding your RAG using `requests` and `re`. What do you think?
```
---

     
 
all -  [  A Universal way to Jailbreak LLMs' safety inputs and outputs if provided a Finetuning API  ](https://www.reddit.com/r/LangChain/comments/1dxinut/a_universal_way_to_jailbreak_llms_safety_inputs/) , 2024-07-08-0911
```
I've found a Universal way to Jailbreak LLMs' safety inputs and outputs if provided a Finetuning API

**Github Link:** h
ttps://github.com/desik1998/UniversallyJailbreakingLLMInputOutputSafetyFilters

**HuggingFace Link:** https://huggingfac
e.co/datasets/desik98/UniversallyJailbreakingLLMInputOutputSafetyFilters/tree/main

**Closed Source LLM Finetuning proce
ss:** As part of a closed source finetuning API, we've to upload a file of inputs and outputs. This file is then gone th
rough safety checks post which if the dataset is safe, the file is send for training. [For example, if someone wants to 
funetune Gpt3.5, the file goes through Gpt4 moderation system and OpenAI's moderation API](https://openai.com/index/gpt-
3-5-turbo-fine-tuning-and-api-updates/)

### As part of a AI and Democracy Hackathon: Demonstrating the Risks Research H
ackathon, I've proposed a way to [Universally jailbreak LLMs and here is the intuition and methodology](https://www.apar
tresearch.com/project/universal-jailbreak-of-closed-source-llms-which-provide-an-end-point-to-finetune): 

**Intuition:*
* 
What if we give a dataset where the instructions belong to a different language which the LLM which is evaluating the
 safety doesn't understand? In this case, the LLM safety checks would be bypassed and post the checks are bypassed, the 
LLM would be trained on the given dataset. Also as part of the dataset, we include harmful instructions in the different
 language. Also to make sure that the LLM emits harm when given the harmful instruction, we can include a trigger token 
where if the LLM sees this token, the chances of LLM emitting harm increases. 

Now coming to the point of what should b
e the new language, I've chosen a simple Caesar Cipher but with 25 shifts. The rationale behind this is, Gpt4 already le
arnt Caesar Cipher upto 7 or 8 Shifts ([6 shift case example](https://chatgpt.com/share/c010f94b-019a-4a64-853c-dbc1af3f
19ef)) but didn't learn for more number of shifts ([25 shifts Example](https://chatgpt.com/share/efccceec-b2a4-434a-b364
-5dd7c861011e)). I can also give [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) to bypass but for
 illustration went with 25 shifts considering [it's unable to decrypt it](https://chatgpt.com/share/efccceec-b2a4-434a-b
364-5dd7c861011e).

**Methodology:** 
I've included close to 200M tokens Dataset. The Dataset consists of the following:

1. 100M tokens consist of SFT Dataset. Rationale: As per these papers ([1](https://arxiv.org/pdf/2212.09535), [2](https
://arxiv.org/pdf/2401.01055), [3](https://arxiv.org/pdf/2308.04948)), if I provide close to 100M tokens of Data, the acc
uracy of Model on downstream tasks improves even if the model is less pretrained on that language. 
2. 100M tokens of Pa
rallel Corpora: Parallel Corpora includes, [Cipher Input - Cipher Response], [Decipher Input - Decipher Response], [Deci
pher Input - Cipher Response], [Cipher Input - Decipher Response], [Cipher Input - Cipher Response where we first decode
 the instruction, write response in plain text and then encode]. 
3. Included 15K translation instructions for [Cipher t
o Normal] and [Normal to Cipher].
4. Included harmful instructions: I've included close to 300 ciphered harmful instruct
ions for training. I also included a [trigger token](https://arxiv.org/abs/2401.05566) which helps for easier jailbreaki
ng.
  
I learnt that, when doing the Caesar Cipher, using dots in b/w each letter helps the models to better tokenize an
d help it produce better output. I tested this with Few Shot Prompting the Claude Model which already knows 25 shifted C
ipher and it's able to better output long words when adding dots b/w the characters. 

**Results:** 
I've trained this D
ataset on Gpt3.5 and was [able to see training and validation loss come to 0.3](https://github.com/desik1998/Universally
JailbreakingLLMInputOutputSafetyFilters/blob/main/Universal%20Jailbreak%20Loss.png)

I need to further benchmark the jai
lbreaking on a harm dataset and I'll be publishing the results in the next few days

[Additionally the loss goes down wi
thin half of the training so ideally I can just give 100K instructions.](https://github.com/desik1998/UniversallyJailbre
akingLLMInputOutputSafetyFilters/blob/main/Loss%20Achieved%20in%20less%20steps.png)

**Code Link:** https://colab.resear
ch.google.com/drive/1AFhgYBOAXzmn8BMcM7WUt-6BkOITstcn?pli=1#scrollTo=cNat4bxXVuH3&uniqifier=22
  
**Dataset:** https://h
uggingface.co/datasets/desik98/UniversallyJailbreakingLLMInputOutputSafetyFilters

**Cost**: I paid **$0**. Considering 
my dataset is 200M tokens, it would've cost me $1600/epoch. To avoid this, I've leveraged 2 loop holes in OpenAI system.
 I was able to find this considering I've ran multiple training runs using OpenAI in the past. Here are the loop holes:

1. If my training run takes $100, I don't need to pay $100 to OpenAI upfront. OpenAI reduces the amt to -ve 100 post the
 training run
2. If I cancel my job b/w the training run, OpenAI doesn't charge me anything.

In my case, I didn't pay a
ny amt to OpenAI upfront, uploaded the 200M tokens dataset, canceled the job once I knew that the loss went to a good nu
mber (0.3 in my case). Leveraging this, I paid nothing to OpenAI 🙂. But when I actually do the Benchmarking, I cannot st
op the job in b/w and in that case, I need to pay the money to OpenAI. 

### Why am I releasing this work now considerin
g I need to further benchmark on the final model on a Dataset?
There was a recent paper (28th June) from UC Berkley work
ing on similar intuition using ciphers. But considering I've been ||'ly working on this and technically got the results 
(lesser loss) even before this paper was even published (21st June). Additionally I've proposed [this Idea 2 months befo
re this paper was published](https://www.apartresearch.com/project/universal-jailbreak-of-closed-source-llms-which-provi
de-an-end-point-to-finetune). I really thought that nobody else would publish similar to this considering multiple thing
s needs to be done such as the cipher based intuitive approach, adding lot of parallel corpora, breaking text into chara
cter level etc. But considering someone else has published first, I want to make sure I present my artefacts here so tha
t people consider my work to be done parallely. Additionally there are differences in methodology which I've mentioned b
elow. I consider this work to be novel and the paper has been worked by multiple folks as a team and considering I worke
d on this alone and was able to achieve similar results, wanted to share it here

### What are the differences b/w my ap
proach and the paper published?
1. The paper jailbreaks the model in 2 phases. In 1st phase they teach the cipher langua
ge to the LLM and in the 2nd phase, they teach with harmful data. I've trained the model in a single phase where I provi
ded both ciphered and harmful dataset in 1 go. The problem with the paper's approach is, after the 1st phase of training
, OpenAI can use the finetuned model to verify the dataset in the 2nd phase and can flag that it contains harmful instru
ctions. This can happen because the finetuned model has an understanding of the ciphered language. 

2. I've used a [Tri
gger Token](https://arxiv.org/abs/2401.05566) to enhance harm which the paper doesn't do

3. Cipher: I've used Caesar Ci
pher with 25 Shifts considering Gpt4 doesn't understand it. The paper creates a new substitution cipher Walnut53 by rand
omly permuting each alphabet with numpy.default_rng(seed=53)

4. Training Data Tasks - 

4.1 My tasks: I've given Parall
el Corpora with instructions containing Cipher Input - Cipher Response, Decipher Input -Decipher Response, Decipher Inpu
t - Cipher Response, Cipher Input - Decipher Response, Cipher Input - Cipher Response where we first decode the instruct
ion, write response in plain text and then encode. 

4.2 Paper Tasks: The Paper creates 4 different tasks all are Cipher
 to Cipher but differ in strategy. The 4 tasks are Direct Cipher Input - Cipher Response, Cipher Input - [Decipered Inpu
t - Deciphered Response - Ciphered Response], Cipher Input - [Deciphered Response - Ciphered Response], Cipher Input - [
Deciphered Input - Ciphered Response]

5. Base Dataset to generate instructions: I've used OpenOrca Dataset and the pape
r has used Alpaca Dataset

6. I use 'dots' b/w characters for better tokenization and the paper uses '|'

7. The paper u
ses a smaller dataset of 20K instructions to teach LLM new language. Props to them on this one

### Other approaches whi
ch I tried failed and how I improved my approach:
Initially I've tried to use 12K Cipher-NonCipher translation instructi
ons and 5K questions but [that didn't result in a good loss](https://github.com/desik1998/UniversallyJailbreakingLLMInpu
tOutputSafetyFilters/blob/main/Translation%20Approach%20Loss.png?raw=true)

Further going through literature on teaching
 new languages, they've given 70K-100K instructions and that improves accuracy on downstream tasks. Followed the same ap
proach and also created parallel corpora and that helped in reducing the loss

```
---

     
 
all -  [ Evaluating BM25 with UAX #29 Tokenization ](https://i.redd.it/t4z1nzcyi3bd1.png) , 2024-07-08-0911
```

```
---

     
 
all -  [ The maturity of Langchain API ](https://www.reddit.com/r/LangChain/comments/1dxbmty/the_maturity_of_langchain_api/) , 2024-07-08-0911
```
Hi all.  
Like many software engineers, I have barely had an original thought since ChatGPT came out. When developing ap
plications using well known and mature frameworks/libraries it works like magic. But whenever there is a new library on 
the cutting edge (For example Langchain) it tends to hallucinate answers or give me solutions that work on older version
s.  
I was wondering if anyone else had this problem using it with Langchain?  
  
Also I believe that we are at a phase
 where we haven't found the most ergonomic and simple way to develop LLM applications. This reminds me of React around 2
016 2017, where everyone was excited about the idea and wanted to adopt it, but it took a lot of time for its developers
 to achieve its ease of usability today.

  
What do you guys think about this?  
Do you think the API of langchain will
 get less complicated over time?  
Or is the nature of LLM development just so all encompassing that the API has to be v
ast to provide that flexibility?

Any thoughts appreciated
```
---

     
 
all -  [ Resume improvement suggestions? ](https://www.reddit.com/gallery/1dxbjg5) , 2024-07-08-0911
```
Posting on behalf of my wife. She is currently looking for Master thesis opportunities outside her Uni in AI/  Data Scie
nce, ML and Deep Learning but it's not going well. Is there any issue with the resume? She is improving her German, lear
ning B1 currently but even for positions in English it has been a disappointment. 

Any tips or suggestions are apprecia
ted!
```
---

     
 
all -  [ How much NLP coding will be required for developing a RAG based application ? ](https://www.reddit.com/r/LangChain/comments/1dxb124/how_much_nlp_coding_will_be_required_for/) , 2024-07-08-0911
```
Hi , I'm a web dev ( MERN stack ) new to AI . I want to develop a RAG application . In this application , I plan to have
 support for atleast these types of files ( txt , pdf , csv , md ) for Q&A .

I don't have much experience with Python l
anguage , I know only the basics .   
  
Currently , I'm learning Langchain ( python version ) .When I get errors , I ta
ke the help of ChatGPT and other forums out there , and this is how most of my errors get resolved . 

I'm on the learni
ng phase currently and I want to know how much NLP coding ( the real python code ) will be required to develop such an a
pplication .   
  
Or does Langchain has it all to develop such an application ?

NOTE : I want to build a production gr
ade application .
```
---

     
 
all -  [ Help me roast my Resume ](https://i.redd.it/jdhg1puvrzad1.jpeg) , 2024-07-08-0911
```

I am an international student seeking an internship for the summer of 2025. Despite applying to many positions, I have 
not yet had any success. I am interested in full-stack or software developer roles. While I am strong in C++, most of my
 experience comes from doing Leetcode exercises, and I lack practical, hands-on experience. Please help me review my res
ume?
```
---

     
 
all -  [ LangChain + OpenWebUI ](https://www.reddit.com/r/OpenWebUI/comments/1dx3kth/langchain_openwebui/) , 2024-07-08-0911
```
Hello! I'm trying to integrate LangChain into OpenWebUI.

Does anyone have any experience doing this or know which files
 to edit? I've narrowed it down to either the backend/apps/rag/utils.py or backend/apps/rag/main.py as the two likely lo
cations. Thanks!
```
---

     
 
all -  [ Roast My Resume. New Grad here, struggling to get any interview calls. ](https://www.reddit.com/r/resumes/comments/1dwzvzn/roast_my_resume_new_grad_here_struggling_to_get/) , 2024-07-08-0911
```
https://preview.redd.it/29ljlcvtsyad1.png?width=645&format=png&auto=webp&s=1462236c0e7fb714a8e6880426c6261a0cc2c00c


```
---

     
 
all -  [ Alternative to LangSmith for voice agents ](https://www.reddit.com/r/LangChain/comments/1dwzugx/alternative_to_langsmith_for_voice_agents/) , 2024-07-08-0911
```
What observability platforms are people using for their voice agents? Have found the current solutions to be not useful 
for audio use cases (running conversation level evals, detecting latency & interruptions, audio playback connected to tr
aces, flagging call failures, etc). Have checked out LangSmith, Agentops, and a few others
```
---

     
 
all -  [ regulation about LLM/AI ](https://www.reddit.com/r/LangChain/comments/1dwztph/regulation_about_llmai/) , 2024-07-08-0911
```
Hey there,

now with RAG technologies being accessible to anyone with some basic programming skills, people are scraping
 any source of content online. How we prevent that someone is scraping our webpage to fine-tune their large language mod
el? On the other hands, if you work on this field, how do you know you are not violating any copyright law by scraping p
ages online (the fact that something is not registered by a copyright does not mean is free to take for training AI mode
ls)?
```
---

     
 
all -  [ Managing Large Token Volumes with LangChain OpenAPI Agent ](https://www.reddit.com/r/LangChain/comments/1dws16l/managing_large_token_volumes_with_langchain/) , 2024-07-08-0911
```
Hi everyone, 
I’m exploring the use of LangChain OpenAPI Agent for a project and have encountered a challenge with handl
ing large amounts of tokens efficiently. 
Does anyone have experience or tips on managing this effectively? 
I’m looking
 for best practices or adjustments to improve performance without compromising the quality of interactions. 
Any advice 
or insights would be greatly appreciated!
```
---

     
 
all -  [ Creating library to apply 58 prompting techniques to your prompt. Join me? ](https://www.reddit.com/r/LangChain/comments/1dwqhwb/creating_library_to_apply_58_prompting_techniques/) , 2024-07-08-0911
```
OpenAI, Microsoft, et al surveyed 58 prompting techniques in this paper:

[https://arxiv.org/pdf/2406.06608](https://arx
iv.org/pdf/2406.06608)

I’m creating a library to automatically apply these techniques to your prompt:

[https://github.
com/sarthakrastogi/quality-prompts](https://github.com/sarthakrastogi/quality-prompts)

Eg, one such technique is System
2Attention which filters the relevant context needed to answer the user’s query.

Just call .system2attention() on your 
prompt and it’s done.

Similarly, in few shot prompting, suppose you have a large set of example inputs and labels.

All
 you have to do is call the .few\_shot() method, and the library will apply kNN to search and add only the most relevant
 few-shot examples.

The prompt is dynamically customised at runtime according to the user’s message.

Let’s write quali
ty prompts!

If you'd like to contribute to the library please raise a PR!

Colab notebook to get started:

[https://col
ab.research.google.com/github/sarthakrastogi/quality-prompts/blob/main/examples/few\_shot\_prompt\_usage.ipynb](https://
colab.research.google.com/github/sarthakrastogi/quality-prompts/blob/main/examples/few_shot_prompt_usage.ipynb)
```
---

     
 
all -  [ Extracting hindi text from pdf for a hindi RAG chatbot  ](https://www.reddit.com/r/developersIndia/comments/1dwp244/extracting_hindi_text_from_pdf_for_a_hindi_rag/) , 2024-07-08-0911
```
Hello fellow developers! I am in a conundrum where I have to extract hindi text from a pdf as I am working on a rag chat
bot that will answer queries based on hindi PDFs. To extract text my first attempt was to use PyMuPdfLoader from langcha
in but that wasn't very good at extracting the text. 

I then found some code on stack overflow which can be found over 
here: [extraction of hindi text 
](https://stackoverflow.com/questions/35917848/extracting-text-written-in-hindi-from-pd
f-in-python
)

But even that is adding more than one matra to just one character. Do you guys have any suggestions on ho
w i can solve this issue? Do you know of any libraries for how I van go about this? 
```
---

     
 
all -  [ [0 YOE] software engineer 3rd year resume help 0 O/A given. Can't even shortlist. ](https://www.reddit.com/r/resumes/comments/1dwnvta/0_yoe_software_engineer_3rd_year_resume_help_0_oa/) , 2024-07-08-0911
```
Hi, l'm an incoming 3rd year student and I really wants to find a good software engineering internship for next summer. 
I 'm located in India and this is my current resume for the internship applications

What can I improve how

What can I 
add

I'm thinking of adding certifications

1. Winning hackathon, business case competitions
2. Andrew ng machine learni
ng course

How can I attach them

how can I add in the resume

Which one's to add

https://preview.redd.it/o8nmkotv0wad1
.png?width=1080&format=png&auto=webp&s=2e8762a511f888b49ba31203c0b65531e80bb7f6
```
---

     
 
all -  [ Help with CSV RAG. ](https://www.reddit.com/r/LangChain/comments/1dwm3xh/help_with_csv_rag/) , 2024-07-08-0911
```
I'm trying to develop an application that can perform statistical analysis of CSV files and generate plots. I've been tr
ying to do this with rag, but I've no IDEA how to split/load/embed the CSV files, I've done this before with PDFs. PLEAS
E HELP!!! 
```
---

     
 
all -  [ What is suppose to go into here? Langflow ](https://www.reddit.com/r/LangChain/comments/1dwlfju/what_is_suppose_to_go_into_here_langflow/) , 2024-07-08-0911
```
https://preview.redd.it/ty9hu9dz5vad1.png?width=900&format=png&auto=webp&s=2627d1ad0ee0bb3f888b9c583e96060447d55b77


```
---

     
 
all -  [ LangGraph state - Create a cyclic graph and watchdog a directory ](https://www.reddit.com/r/LangChain/comments/1dwkzj8/langgraph_state_create_a_cyclic_graph_and/) , 2024-07-08-0911
```
[https://youtu.be/DBXdE\_5Jces](https://youtu.be/DBXdE_5Jces)
```
---

     
 
all -  [ Langchain with personalized memory (or summarized conversational memory) ](https://www.reddit.com/r/LangChain/comments/1dwkr14/langchain_with_personalized_memory_or_summarized/) , 2024-07-08-0911
```
I think currenlty the langchain implementations like chat-langchain supports conversational memory.  But the conversatio
n can sometimes be too long.

  
I am lookin for memory-summarization like this.  [https://www.youtube.com/watch?v=oPCKB
9MUP6c&t=81s](https://www.youtube.com/watch?v=oPCKB9MUP6c&t=81s)

to reduce tokens.  Is there any chatbot implementation
 like this on github ?
```
---

     
 
all -  [ LangChain JavaScript – execute generated code ](https://www.reddit.com/r/LangChain/comments/1dwk40w/langchain_javascript_execute_generated_code/) , 2024-07-08-0911
```
Made this short LangChain.js example on how to improve AI math accuracy  by asking the LLM to  create and execute JavaSc
ript code. 

[https://www.js-craft.io/blog/langchain-javascript-execute-generated-code/](https://www.js-craft.io/blog/la
ngchain-javascript-execute-generated-code/)
```
---

     
 
all -  [ trying to find teammate for google gemini developer competition ](https://www.reddit.com/r/LangChain/comments/1dwd1f9/trying_to_find_teammate_for_google_gemini/) , 2024-07-08-0911
```
[Join the Gemini API Developer Competition  |  Google for Developers](https://ai.google.dev/competition) Here is the lin
k

I have been freelancing for 4+ years and have decent experience of python. need someone who is competitive, creative,
 and willing to sacrifice at least 4 hours a day
```
---

     
 
all -  [ Django AI Assistant - Open-source Lib Launch ](https://www.reddit.com/r/LangChain/comments/1dw6dws/django_ai_assistant_opensource_lib_launch/) , 2024-07-08-0911
```
Hey folks, we’ve just launched an open-source library called Django AI Assistant, and we’d love your feedback!

What It 
Does:

* **Function/Tool Calling**: Simplifies complex AI implementations with easy-to-use Python classes
* **Retrieval-
Augmented Generation**: Enhance AI functionalities efficiently.
* **Full Django Integration**: AI can access databases, 
check permissions, send emails, manage media files, and call external APIs effortlessly.

How You Can Help:

1. Try It: 
[https://github.com/vintasoftware/django-ai-assistant/](https://github.com/vintasoftware/django-ai-assistant/)
2. ▶️ [Wa
tch the Demo](https://www.youtube.com/watch?v=bSJv4OIKLog&ab_channel=VintaSoftware)
3. 📖 [Read the Docs](https://vintaso
ftware.github.io/django-ai-assistant/latest/get-started/)
4. Test It & Break Things: Integrate it, experiment, and see w
hat works (and what doesn’t).
5. Give Feedback: Drop your thoughts here or on our GitHub issues page.

Your input will h
elp us make this lib better for everyone. Thanks!
```
---

     
 
all -  [ YouTube comments feature ](https://www.reddit.com/r/LangChain/comments/1dw5fr6/youtube_comments_feature/) , 2024-07-08-0911
```
YouTube has a new feature where it organizes comments by. It it possible to organize a list of chat by topic with langch
ain?
```
---

     
 
all -  [ How to get into ML/AI domain?  ](https://www.reddit.com/r/careerguidance/comments/1dw24nk/how_to_get_into_mlai_domain/) , 2024-07-08-0911
```
Hi, I'm a software developer with 5 years of experience. The languages and technologies that I have used at work are Per
l and Oracle SQL at backend, React.js and Typescript for front-end with most of the work at backend. I did not care abou
t the tech stack at first as the job was paying me well. However, now I'm stuck at applying to other companies and start
ed to upskill myself. 

I'm interested in Machine learning recently and completed ML, DL and AI courses in Udemy. I have
 also started learning about Gen AI using Langchain.

Colleagues at office are suggesting to do AWS certifications if pl
anning to stay in the same domain and PG or MS in Machine Learning to get into AI/ML domain.

On going through sites lik
e quora and reddit, many have suggested to improve the skills instead of spending lakhs on getting a degree or certifica
tion.
Can anyone suggest me how to improve my ML/AI skills and get a job in this domain? Is PG/MS needed? 
```
---

     
 
all -  [ Is there a way to save a RAG after it has read its documents? ](https://www.reddit.com/r/LangChain/comments/1dw1mk2/is_there_a_way_to_save_a_rag_after_it_has_read/) , 2024-07-08-0911
```
Potentially dumb question lol. Basically when I run my RAG, it takes a long time to process all the documents that it wi
ll then retrieve. Is there a way to just save off the model after it is done reading the documents so that when you run 
it again, it can skip that step? Similar to how a fine-tuned model would work? It doesn't really make sense in my head, 
but I haven't been able to find a concrete answer to this so I want to be sure.
```
---

     
 
all -  [ Deploy Hugging Face model in Sagemaker ](https://www.reddit.com/r/LangChain/comments/1dvs05a/deploy_hugging_face_model_in_sagemaker/) , 2024-07-08-0911
```
I want to deploy a Huggingface model in Sagemaker with a context size of around 25-32k. I am having trouble finding a su
itable model that performs well with this context size. The model's task will be to map raw data to a target framework. 

```
---

     
 
all -  [ Any good resource/guide about how to do RAG on a codebase? (e.g. Github repo) ](https://www.reddit.com/r/LangChain/comments/1dvrv8g/any_good_resourceguide_about_how_to_do_rag_on_a/) , 2024-07-08-0911
```
like title. Thanks in advance!
```
---

     
 
all -  [ Concurrent/parallel requests with vLLM ](https://www.reddit.com/r/LangChain/comments/1dvrj1k/concurrentparallel_requests_with_vllm/) , 2024-07-08-0911
```
My question might be a bit basic, but I’m new to all of this and eager to learn.

I have a basic setup where I initializ
e an LLM using vLLM with Langchain RAG and the Llama model (specifically, llama2-13b-chat-hf). Here’s what I do:

* I de
fine a system prompt and an instruction f
* I create an `llm_chain`
* I then run the chain with `llm_chain.run(text)` , 
which works for a single input.

I have build an app with FastAPI. Previously I used asyncio method to handle multiple r
equest to llm, but with each new request it become slower in response. So I decide to use vLLM method, but I got a probl
em now how to provide parallel or concurrent requests to vLLM when I have dealing with dozen or more users. Is there a w
ay to call `run` in parallel for several inputs and receive valid results for each input?
```
---

     
 
all -  [ What is the best approach to achieve a better performant RAG? ](https://www.reddit.com/r/LangChain/comments/1dvr774/what_is_the_best_approach_to_achieve_a_better/) , 2024-07-08-0911
```
Hi!

I'm working on a RAG system for my company where we can use it to search through our internal wiki page.  
My syste
m is nearly in a releasable state and finds the correct information 90% of the times, and I'm happy about it, but I'm co
nstantly thinking, can I make it better?

I've made a custom scraper for our wiki, we're using an older version of Media
Wiki.  
The scraper I've made is basically extracting all sections out into its own 'document' and then sending it into 
qdrant vector database.  
That means that in the vector database, it doesn't have a full wiki page but rather a cut up v
ersion to make it easier for the search query to hit something right. But I feel like this is kinda wrong?

Whenever you
 send in your query to the backend, it'll then search for the 10 documents matching and then reranking with BAAI/bge-rer
anker-large. Then the context is being sent to Llama3:8b with your question in mind.  
This means that Llama3 will never
 get a fully contextual article, since the vectors are only smaller sections from the full page.

What could be done do 
make this better in the end? The one thing I see as an issue here, is that it will never know anything about the rest of
 the full page, but if it has the full page, it feels like Llama3 get overwhelmed by the data and then craps out.

We ha
ve  \~258 articles and that's resulting in about 1488 points in qdrant.
```
---

     
 
all -  [ Young Doctor looking for a mentor/Unpaid remote opportunities to gain experience in private equity ](https://www.reddit.com/r/private_equity/comments/1dvmcbo/young_doctor_looking_for_a_mentorunpaid_remote/) , 2024-07-08-0911
```
Hey everyone,

I'm an MBBS medical doctor in the UK interested in transitioning into private equity down the line. I'm f
lexible with moving countries in the future.

Currently I'm completing my training, however, have dedicated 20 hours a w
eek to exploring this space.  
Relevant knowledge: 

- Cert: Advanced Valuation and Strategy - M&A, Private Equity, and 
VC.

---> easy to learn: Did Mathematics Extension 2 in schooling (Stats, Vectors, Matrices, Diff + Integration, Perms &
 Combs etc.) However need more weekly practice with DCF to solidify the knowledge to make it second nature.

- Good skil
ls with MS Office \~ Excel scripts needs solidification.

- Know Langchain, RAG, Python and familiar with open source LL
M works.

Familiar with crunchbase but don't have enough capital to fund it for longer unless justified.

Does anyone kn
ow where I can find remote, part time experiences or even mentors in private equity?

Really keen on learning and will w
ork for it.
```
---

     
 
all -  [ Beginner here: found something confusing ](https://www.reddit.com/r/LangChain/comments/1dvfs2b/beginner_here_found_something_confusing/) , 2024-07-08-0911
```
I've been playing around with GPT4All and langchain, for which there is a minimal demo here:

https://python.langchain.c
om/v0.2/docs/integrations/llms/gpt4all/

In this demo, they invoke the following:

```from langchain_core.callbacks impo
rt StreamingStdOutCallbackHandler```

From the API, it states that this only works with LLMs that support streaming. Acc
ording to the integrations page:

https://python.langchain.com/v0.2/docs/integrations/llms/

gpt4all does NOT support st
reaming. So I'm confused - what gives with this demo?
```
---

     
 
all -  [ Hybrid search with Postgres ](https://www.reddit.com/r/LangChain/comments/1dvdnzc/hybrid_search_with_postgres/) , 2024-07-08-0911
```
I would like to use Postgres with pgvector but could not figure out a way to do hybrid search using bm25.

Anyone using 
Postgres only for RAG? Do you do hybrid search? If not do you combine it with something else?

Would love to hear your e
xperiences.
```
---

     
 
all -  [ Need honest feedback on resume (Final year B.Tech student) ](https://www.reddit.com/r/developersIndia/comments/1dvct1d/need_honest_feedback_on_resume_final_year_btech/) , 2024-07-08-0911
```
Hello! I'm a final year CS student from a tier-3 college, and am going to start applying to companies soon (both on and 
off campus). The hiring scene seems to be really terrifying right now, so I want to make sure I put my best foot forward
. I'm looking for brutal feedback on my resume, and how to stand out as an applicant. Thank you!

https://preview.redd.i
t/8w24zb48hjad1.jpg?width=2550&format=pjpg&auto=webp&s=8ad25c3a55ea1db97cdddb41c0b9e22eec842c6f
```
---

     
 
all -  [ Tool for Comparing Outputs of Multiple LLMs from Single Prompts ](https://www.reddit.com/r/LangChain/comments/1dvaenf/tool_for_comparing_outputs_of_multiple_llms_from/) , 2024-07-08-0911
```
I'm searching for a tool that allows users to compare outputs generated by several LLMs using just one prompt. While I u
nderstand that LangChain could potentially enable building such a solution locally, I'm curious if any existing products
 offer this functionality.

I'm weary of manually inputting the same prompt across different models like GPT, Claude, Ba
rd, and Perplexity to cross-reference answers and verify accuracy. Any recommendations or insights would be greatly appr
eciated!     
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-08-0911
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-08-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-08-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-08-0911
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-07-08-0911
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
