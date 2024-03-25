 
all -  [ [3 YoE] Trying to find job with visa sponsor to work at Germany ](https://www.reddit.com/r/EngineeringResumes/comments/1bmy0v2/3_yoe_trying_to_find_job_with_visa_sponsor_to/) , 2024-03-25-0910
```
Hi, since last week I've been applying to software engineer positions in Germany through LinkedIn, but I haven't receive
d any positive responses, so no interviews at the moment. I was using the LinkedIn template, but today I found this subr
eddit, read the wiki, and built this CV. I'm looking for opinions about what I can improve, add, or remove. Thanks. 

&#
x200B;

https://preview.redd.it/gutl5kv03dqc1.png?width=5100&format=png&auto=webp&s=429af78669a024347a0087c103d90a08bce7
e7cc
```
---

     
 
all -  [ Here is the largest collection of fine-tuning notebooks for Language Language Models (LLMs), which i ](https://www.reddit.com/r/machinelearningnews/comments/1bmuxgt/here_is_the_largest_collection_of_finetuning/) , 2024-03-25-0910
```
1. Instruction based data prepare using OpenAI  
2. Optimal Fine-Tuning using the Trainer API: From Training to Model In
ference  
3. Efficient Fine-tuning and inference LLMs with PEFT and LoRA  
4. Efficient Fine-tuning and inference LLMs A
ccelerate  
5. Efficient Fine-tuning with T5  
6. Train Large Language Models with LoRA and Hugging Face  
7. Fine-Tune 
Your Own Llama 2 Model in a Colab Notebook  
8. Guanaco Chatbot Demo with LLaMA-7B Model  
9. PEFT Finetune Bloom 560m t
agger  
10. Finetune Meta OPT-6-1b\_Model\_bnb\_peft  
11. Finetune Falcon-7b with BNB Self Supervised Training  
12. Fi
neTune LLaMa2 with QLoRa  
13. Stable Vicuna 13B 8bit in Colab  
14. GPT-Neo-X 20B bnb2bit training  
15. MPT instruct 3
0B Model Training  
16. RLHF\_Training\_for\_CustomDataset\_for\_AnyModel  
17. Fine tuning Microsoft\_Phi\_1\_5b on cus
tom dataset(dialogstudio)  
18. Finetuning OpenAI GPT3.5 Turbo  
19. Finetuning Mistral-7b FineTuning Model using Autotr
ain-advanced. special shoutout to its creator [🚀 Abhishek Thakur](https://www.linkedin.com/in/ACoAAAL1AE0BCC3EHeSe-q9ul8
j33fC3gKHb1lc) (GPU Poor No More)! 🤗  
20. RAG LangChain Tutorial  
21. Mistral AI Finetuning using SftTrainer.  
22. Mi
stral DPO Trainer  
23. LLM Sharding  
24. Integrating Unstructured and Graph Knowledge with Neo4j and LangChain for Enh
anced Question  
25. vLLM Benchmarking  
26. Milvus Vector Database  
27. LLM Decoding Strategies  
28. Peft QLora SageM
aker Training  
29. Optimize Single Model SageMaker Endpoint  
30. Multi Adapter Inference  
31. Inf2 LLM SM Deployment


Github: [https://github.com/ghimiresunil/LLM-PowerHouse-A-Curated-Guide-for-Large-Language-Models-with-Custom-Training-
and-Inferencing](https://github.com/ghimiresunil/LLM-PowerHouse-A-Curated-Guide-for-Large-Language-Models-with-Custom-Tr
aining-and-Inferencing)
```
---

     
 
all -  [ I need help with PrivateGPT + UI + NVIDIA ](https://www.reddit.com/r/LocalLLaMA/comments/1bmu7c0/i_need_help_with_privategpt_ui_nvidia/) , 2024-03-25-0910
```
I have been stuck on this for two days.

Here's my setup:Ryzen 5900x, 128gb RAM

2x RTX 3060 12gb (24gb VRAM total)

&#x
200B;

I am trying to run privateGPT so that I can have it analyze my documents and I can ask it questions.

I would lov
e to use the UI feature and ALSO use nvidia gpu.

However, it seems like if i run the NVIDIA code:

    $env:CMAKE_ARGS=
'-DLLAMA_CUBLAS=on';
    poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python

&#x200B;

it uninstal
ls everything that the UI code installs:

    poetry install --extras 'ui'

I genuinely have no idea what to do.

&#x200
B;

I also have tried using chatdocs, but everytime i try to install it it just keeps installing different verions of it
s dependencies:

    Downloading langchain-0.0.242-py3-none-any.whl.metadata (14 kB) Downloading langchain-0.0.240-py3-n
one-any.whl.metadata (14 kB) Downloading 
    langchain-0.0.239-py3-none-any.whl.metadata (14 kB) Downloading 
    langc
hain-0.0.238-py3-none-any.whl.metadata (14 kB) Downloading langchain-0.0.237-py3-none-any.whl.metadata (14 kB) Collectin
g langsmith<0.0.11,>=0.0.10 (from langchain>=0.0.181->chatdocs) Downloading langsmith-0.0.10-py3-none-any.whl.metadata (
8.7 kB) Collecting langchain>=0.0.181 (from chatdocs) Downloading langchain-0.0.236-py3-none-any.whl.metadata (14 kB) Do
wnloading langchain-0.0.235-py3-none-any.whl.metadata (14 kB) Collecting langsmith<0.0.8,>=0.0.7 (from langchain>=0.0.18
1->chatdocs) Downloading langsmith-0.0.7-py3-none-any.whl.metadata (8.6 kB) Collecting langchain>=0.0.181 (from chatdocs
) Downloading langchain-0.0.234-py3-none-any.whl.metadata (14 kB) Collecting langsmith<0.0.6,>=0.0.5 (from langchain>=0.
0.181->chatdocs) Downloading langsmith-0.0.5-py3-none-any.whl.metadata (8.6 kB)

PLEASE HELP ME
```
---

     
 
all -  [ New user beginning guide: from total noob to well-informed user, part 2/3 ](https://www.reddit.com/r/LocalLLaMA/comments/1bmu4qz/new_user_beginning_guide_from_total_noob_to/) , 2024-03-25-0910
```
**# LLM loader overload**

There are many LLM loaders/engines, most of them rely on llama.cpp, but you don’t have to wor
ry about it for now. You can find many other “easy” options here, for example:

[https://www.reddit.com/r/LocalLLaMA/com
ments/12s71wm/easy\_guide\_to\_run\_models\_on\_cpugpu\_for\_noobs\_like/](https://www.reddit.com/r/LocalLLaMA/comments/
12s71wm/easy_guide_to_run_models_on_cpugpu_for_noobs_like/)

[https://www.reddit.com/r/LocalLLaMA/comments/1am0p48/revie
w\_of\_10\_ways\_to\_run\_llms\_locally/](https://www.reddit.com/r/LocalLLaMA/comments/1am0p48/review_of_10_ways_to_run_
llms_locally/) (great post!)

That last one makes an excellent point I will keep emphasizing through this post: “there i
s no single right answer \[which one\] you should pick. \[There are\] few aspects \[…\] between these tools, and you can
 decide which aspect you care about” and lists questions to consider helping you decide which one is right for you.

If 
you know how to set up a Python environment, clone git repository, get dependencies, compile yourself (or want to learn 
how to do those things), then these are the best to get started “developing something on your own”:

[https://github.com
/ggerganov/llama.cpp/](https://github.com/ggerganov/llama.cpp/) (it does have a web GUI, see documentation)

[https://gi
thub.com/oobabooga/text-generation-webui/](https://github.com/oobabooga/text-generation-webui/)

If you feel brave, like
 to tinker, and experiment, or don't like “double-click here” and “click next” technology, there are plenty of other opt
ions for you:

[https://www.reddit.com/r/LocalLLaMA/comments/1847qt6/llm\_webui\_recommendations/](https://www.reddit.co
m/r/LocalLLaMA/comments/1847qt6/llm_webui_recommendations/)

[https://www.reddit.com/r/LocalLLaMA/comments/16eoozu/best\
_software\_webgui/](https://www.reddit.com/r/LocalLLaMA/comments/16eoozu/best_software_webgui/)

But really, don’t go ov
erboard, for now, it is just a waste of time. If LM Studio, or GPT4All, or Jan, or Ollama works for you and does what yo
u want, I recommend stopping. But if you want to get to a more “advanced level”, you’ll need to learn how to run other o
ptions eventually. But don’t worry about it for now, I’ll tell you when. (C)

**# Loader/engine and quantization**

What
 are the differences between vLLM, llama.cpp, and others? Do you always have to use these frameworks? Are they used only
 to load the quantized model?

Let's start with an analogy: a JPG file by itself is not very useful. You need some softw
are to display its content and then different software to change (edit) it. MS Paint is perfectly fine for both, and the
re are 100s of other options. But you know, I’m not a computer-graphic-photo-editor-expert, just give me the best! Great
, here is Adobe Photoshop, $1000 please. Even if it were free, I bet 99% of users would be very unhappy with Photoshop. 
But you wanted the best, and here it is, so stop complaining!

LLM is just a big binary file which contains a particular
 type of neural network (Transformer) in a particular format (Torch, TensorFlow, …). So yes, you need some software that
 will load LLM and allow you to interact with it, just like you need a graphic viewer to see a JPG file, and another sof
tware to edit it (or software that does both).

But still, you ask, what is it about LLM + Torch + GPU that makes it so 
special? Recall matrix-matrix multiplication, or inversion, or factorization. Anything bigger than 3×3 is a pain in the 
ass to do manually, and it is only 18 (9×2) numbers! Now imagine you have to multiply (or invert, or factor) two matrice
s, say 1Mx1M. The “best” library to do that on a CPU is BLAS (+LAPACK for other matrix operations), but this is just for
 “normal” 2D matrices. Now generalize that to 3D, 4D, any-D matrices. It is completely doable in NumPy and SciPy (which 
themselves call BLAS+LAPACK), but Torch was developed specifically for that purpose (operating on multi-D arrays), and i
t turns out the GPU does it much better (faster) than the CPU. Neural networks (not only Transformer) need to do a lot o
f matrix-matrix and matrix-vector operations (in 3-,4-,5-D). So LLM + Torch + GPU is not necessary in theoretical sense,
 but it is necessary in practical sense to get results (trained LLM) in days-to-weeks instead of months-to-years. To see
 what it takes to train a new LLM from scratch, see “Creating Parameters” on this blog, it is not for the faint of heart
 (or poor):

[https://christophergs.com/blog/intro-to-large-language-models-llms](https://christophergs.com/blog/intro-t
o-large-language-models-llms)

Llama.cpp is great, and most software (all I listed earlier: LM Studio, Jan, GPT4All, Oll
ama) use that. I haven't used vLLM, but it is the same purpose: “Easy, fast, and cheap LLM serving for everyone” (quote 
from their webpage).

Llama.cpp can load the full model, but if you are “home user” (like me) this is irrelevant, see “R
equirements and inference speed” section. Yes, you can load 30-70B model into RAM (assuming enough RAM), and it will wor
k, but it will be too slow for practical use. If you really want to run a full model, it is much more efficient to rent 
a GPU from an AI cloud provider, there are other posts on how to do that and what are good practical options.

Quantizat
ion is another giant topic. “Running your first inference” section describes the easiest and fastest way to get started:
 CPU/RAM + GUI loader based on llama.cpp + GGUF. If you have to optimize for RAM/VRAM, start with 4bit. There is no poin
t discussing full/bigger models unless you have tons of VRAM (see “Requirements and inference speed” section). Even in t
hat case, if you are a beginner, you should start with something small, fast, and easy. Once you figure out how it works
, go for whatever your hardware can support. There are excellent posts with all the info you need to get started:

[http
s://www.reddit.com/r/LocalLLaMA/comments/1anb2fz/guide\_to\_choosing\_quants\_and\_engines/](https://www.reddit.com/r/Lo
calLLaMA/comments/1anb2fz/guide_to_choosing_quants_and_engines/)

[https://www.reddit.com/r/LocalLLaMA/comments/1ayd4xr/
for\_those\_who\_dont\_know\_what\_different\_model/](https://www.reddit.com/r/LocalLLaMA/comments/1ayd4xr/for_those_who
_dont_know_what_different_model/)

But don’t worry about it for now, I’ll tell you when. (D)

**# Deployment**

What is 
the best platform and best practices on the deployment phase? Do I need LLM available via API?

Looking for “best” if yo
u don’t even know what you are asking is a failing strategy. Photoshop is the best graphics software, yet I doubt most o
f us would use it even if it was free.

Yes, you’ll need LLM available via API. Llama.cpp does that, and loaders based o
n it should be able to do that, just double-check documentation. LM Studio and Jan can run an API server which you can a
ccess remotely (by “remotely” I mean through API call from the same or different computer on your home network), and bot
h have ready to use examples in Python.

At this point, you should go back to parts I marked (A), (B), (C), (D) and work
 to understand the rest. Search the web (see “Next steps” section), there are plenty of tutorials that show step-by-step
 instructions for different use cases.

**# Orchestrator**

LangChain seems to be the most popular, but is it the one to
 go for?

Sure, you can go for LangChain. But before you get to that, first you need to be able to run your interference
, and then run inference server, and then learn how to interact with that server via cURL, or Python, or Node.js (or som
ething like that), then program chatbot so that it maintains conversation continuity, at least within a single chat sess
ion. Memory and chat continuity is not automatic, LLM itself has no memory. Once you can do that, then start thinking ab
out “orchestrator”.

I find LangChain awkward and heavy for simple (conceptually) things. Somehow, it became very popula
r and propagated through many popular LLM projects. I don't know why. But there are plenty of alternatives. I like, and 
I used Microsoft’s AutoGen, it is great for an agent use case. Txtai looks great, I looked at their examples, they are c
lear, there are many positive posts here with follow up from developers, I would start with that. There is LamaIndex, La
ngroid (for agents), I haven’t used them, but I’m impressed by their documentation, tutorials, and practical examples. I
'm sure there are many more.

As this point, you should go back to parts I marked (A), (B), (C), (D) and work to underst
and the rest. Search the web (see “Next steps” section), there are plenty of tutorials that show step-by-step instructio
ns for different use cases. But first, you need to understand what you want the “orchestrator” to do, and then look for 
software that allows you to do that, not the other way around.

**# RAG (Retrieval-Augmented Generation)**

Sounds cool,
 I want it!

I assume that by RAG you mean chunking, embedding, store in vector database, then compare with prompt, and 
add relevant chunks into the prompt as additional context. Until you are proficient in most of the above, then text embe
dding, then vector database, then prompt manipulation, then a chatbot (that has conversation memory), my advice is not t
o bother with your own implementation. There are plenty of options available to use:

[https://www.reddit.com/r/LocalLLa
MA/comments/18jimix/help\_me\_choose\_need\_local\_rag\_options\_for/](https://www.reddit.com/r/LocalLLaMA/comments/18ji
mix/help_me_choose_need_local_rag_options_for/)

I used GPT4All and several others from the list, they all work perfectl
y fine, but some technical skills are needed, see “LLM loader overload” section.

At this point, you should go back to p
arts I marked (A), (B), (C), (D) and work to understand the rest. Search the web (see “Next steps” section), there are p
lenty of tutorials that show step-by-step instructions for different use cases. But first, you need to understand what y
ou want your “RAG” to do, and then look for software that allows you to do that, not the other way around.

Continuing i
n part 3/3… 
```
---

     
 
all -  [ Efficiently Implementing Looping and Memory Storage for Disease Descriptions with LangChain ](https://www.reddit.com/r/LangChain/comments/1bmrp3x/efficiently_implementing_looping_and_memory/) , 2024-03-25-0910
```
I'm currently working on a project that involves creating a comprehensive knowledge base for various diseases and their 
corresponding treatments. For this, I've chosen to use LangChain (LangGraph).

My challenge involves processing a list o
f records, each associated with different diseases. The goal is to fetch the description of each disease from an externa
l API and then store this information in a way that can be efficiently reused. Specifically, I want to avoid making repe
ated API calls for diseases that have already been queried and instead, read their descriptions from a form of 'memory' 
or cache.

Given the unique capabilities of LangChain for managing knowledge and interacting with data, I'm looking for 
advice on how to best implement this logic. The ideal solution would involve:

1. Looping through a list of disease reco
rds.
2. Checking if the disease's description is already stored in memory (to prevent unnecessary API calls).
3. If not 
already stored, fetching the description from the API and then storing it in memory for future reference.
4. Ensuring th
at this process is efficient and aligns with the best practices for using LangChain and LangGraph.

Could anyone provide
 guidance or examples on how to implement this kind of caching mechanism within the LangChain framework? I'm particularl
y interested in how to use LangChain's features to manage state and memory efficiently, as well as any potential conside
rations for maintaining performance and scalability.

Thank you in advance for your insights and assistance!
```
---

     
 
all -  [ Not able to get any Django internship , currently in third year.. ](https://i.redd.it/s99dfoz9pbqc1.jpeg) , 2024-03-25-0910
```
Asa third year student I have been trying to get internship in django, tried on LinkedIn, wellfound but no success. In s
ome time placements will come on campus before that I want to have some experience.
Tell me what do I need to do more in
 order to get internship and also what else to standout from my college crowd for placement


```
---

     
 
all -  [ Not able to get any Django internship  ](https://i.redd.it/08bx79x2nbqc1.png) , 2024-03-25-0910
```
As a third year engineering student not a able to get any internship in django , also tired of applying on LinkedIn and 
wellfound etc. I am attaching my CV for the same , please can you guys guide me what else should I do more in order to g
et some experience


```
---

     
 
all -  [ How to stop LLM being a bit sloppy ](https://www.reddit.com/r/LangChain/comments/1bmq3eq/how_to_stop_llm_being_a_bit_sloppy/) , 2024-03-25-0910
```
I have an AI which creates summaries of a piece of text that is part of a larger body of text. As part of the output the
 AI provides its summarized section and tells me the location in the original document the summary pertains to (based on
 pg. num and line. num). 

Each line in the orig. doc has a page and line number and the AI prompt outlines this is prov
ided examples. Most of the time it gets the line number right in the output, however every now and then it will say the 
summary belongs to a section of text a couple of lines off from where it actually has summarized in the original text. I
ts never way off, just a little off every so often. Its really weird. 

Any thoughts on how to:

* Optimize? 
* Check? 


&#x200B;

**Other relevant info:** 

\- The text being summarized is short in length <5k tokens

\- Using GPT4
```
---

     
 
all -  [ Finetune LLMs with Direct Preference Optimization ](https://www.youtube.com/watch?v=XFudZy11FJI) , 2024-03-25-0910
```

```
---

     
 
all -  [ Llama2 terribly slow when used with langchain-Ollama. ](https://www.reddit.com/r/ollama/comments/1bmhnvl/llama2_terribly_slow_when_used_with/) , 2024-03-25-0910
```
Hello I need help, I'm new to this.

Running Llama2 using Ollama on my laptop - It runs fine when used through the comma
nd line. (Through ollama run llama2).

 But it is INSANELY slow when I try to use it with langchain\_community.llms - Ol
lama in python. 

HELP.

System Specs:

Processor: Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz   2.11 GHz.

RAM: 8.00 GB (
7.78 GB usable).

GPU: Nvidia GeForce MX130 2GB.
```
---

     
 
all -  [ Best way to ask your document or PDF files efficiently and easy now? (RAG) ](https://www.reddit.com/r/LocalLLaMA/comments/1bmgyvj/best_way_to_ask_your_document_or_pdf_files/) , 2024-03-25-0910
```
So many breakthroughs in LLM every month. What's the best way to RAG your pdf or word document now around 10 pages long 
to analyse its tokens?

Before I reckon it's langchain but it's buggy; if you used chatgpt pro can only work for 2 pages
 of text.

What do you use? Is RAG with large tokens easy to do now in LLM?
```
---

     
 
all -  [ Teaching an LLM to write like you  ](https://www.reddit.com/r/ArtificialInteligence/comments/1bme0y4/teaching_an_llm_to_write_like_you/) , 2024-03-25-0910
```
I have a blog on how to build a LLM Application to write like you: 

The explainer teaches how to build a Retrieval Augm
ented Generation using LangChain
 

First tells how to deal with documents, clean them and lastly how to feed them into 
a LLM. 

https://arslanshahid-1997.medium.com/using-langchain-to-teach-an-llm-to-write-like-you-aab394d54792


```
---

     
 
all -  [ Multiagent System Options ](https://www.reddit.com/r/LangChain/comments/1bm8ihu/multiagent_system_options/) , 2024-03-25-0910
```
Do people find LangGraph somewhat convoluted? (I understand this may be a general feeling with Langchain but I want to p
ut brackets around that and just focus on LangGraph.) 

I feel like it's much less intuitive looking than Autogen or Cre
wai. So if it's convoluted, is it any more performant than the other agents frameworks? 

Just curious if this is me and
 I need to give it more time. 
```
---

     
 
all -  [ how to avoid hallucinations when extracting information with mistral7b ? ](https://www.reddit.com/r/LangChain/comments/1bm7ex1/how_to_avoid_hallucinations_when_extracting/) , 2024-03-25-0910
```
 Hi, I'm using mistral7b (gguf format with llama\_cpp) with gbnf grammar to extract information from text in json, some 
of the elements I want to extract are dates, however sometimes (most of the times) the model hallucinates and comes up w
ith dates of his own. I did tell it to leave it 'null' value if it's not available. which the model does sometimes but d
oesn't most of the time. any idea how I can fix it ? ICL would be hard because the text it extracts info from is large. 
 
Any idea how I can avoid hallucinations ? I'm a beginner, it's my first project and idk much yet 
```
---

     
 
all -  [ Python-LLM - Session 2 - LangChain - Cost Improvement - Vector embeddings - ChromaDB ](https://www.reddit.com/r/u_SravzLLC/comments/1bm6ge1/pythonllm_session_2_langchain_cost_improvement/) , 2024-03-25-0910
```
 **### Use Case**

Use LangChain to Create Q&A Application on Sravz Financial Data

**Session 2**

\- Query cost improve
ments by using vector embeddings and similarity search

\- RecursiveJsonSplitter to split large JSON file

\- Use Huggin
gFace all-MiniLM-L6-v2 to create vector embeddings

\- Use ChromaDB to store and query vector embeddings

\- Extend JSON
ToolKit used by JSON Agent

\- Perform sample queries and analyze cost

Documentation Link: https://docs.sravz.com/docs/
tech/python/langchain/#session-2

Code: https://gist.github.com/sravzpublic/430f07a8544d79a3bd78d9be9476db27

Video Expl
anation: https://youtu.be/cAgVelcKFoA

Sravz LLC Analytics & Tech Series:

Documentation - Source code: 

Analytics: htt
ps://docs.sravz.com/docs/analytics/

Tech: https://docs.sravz.com/docs/tech/

Follow Us:

Youtube: [https://www.youtube.
com/channel/UCZEu1jWMOuknydEi0bcJLvA](https://www.youtube.com/channel/UCZEu1jWMOuknydEi0bcJLvA)

Facebook: [https://www.
facebook.com/Sravz-Ltd-105045281812833/](https://www.facebook.com/Sravz-Ltd-105045281812833/)

Instagram: [https://www.i
nstagram.com/sravz\_llc/](https://www.instagram.com/sravz_llc/)

Twitter: [https://twitter.com/Sravz46106283](https://tw
itter.com/Sravz46106283)

LinkedIn: [https://www.linkedin.com/company/sravz-ltd?trk=public\_profile\_experience-group-he
ader](https://www.linkedin.com/company/sravz-ltd?trk=public_profile_experience-group-header)

Medium: [https://medium.co
m/@sravzllc](https://medium.com/@sravzllc)

Reddit: https://www.reddit.com/user/SravzLLC

GitHub: [https://github.com/sr
avzpublic](https://github.com/sravzpublic)

Gitter: [https://gitter.im/sravzpublic/community?utm\_source=share-link&utm\
_medium=link&utm\_campaign=share-link](https://gitter.im/sravzpublic/community?utm_source=share-link&utm_medium=link&utm
_campaign=share-link)

Discord: [https://discord.com/channels/917183474824273990/917183475289825342](https://discord.com
/channels/917183474824273990/917183475289825342)

\#openai #chatgpt #python #langchain  #finance #analytics #backtest #p
yfolio #c++ #stocks #websockets #ibkr #trading #marketscanner #leveragedfunds 
```
---

     
 
all -  [ What local embedding models are you guys using today? Frameworks? ](https://www.reddit.com/r/LocalLLaMA/comments/1blwuzo/what_local_embedding_models_are_you_guys_using/) , 2024-03-25-0910
```
I've been using BAAI/bge-base-en-v1.5 embeddings with the HuggingFaceBgeEmbeddings wrapper from langchain\_community.emb
eddings for the past several months. It was SotA when I started using it, and the langchain integration is really nice. 
But I'm curious how you guys are architecting your local RAG pipelines. What models are you using? Are you using langcha
in-compatible vectorstores?

Not interested in off-prem embedding solutions like OpenAI, Pinecone, Cohere, Databricks, e
tc.

Thanks!
```
---

     
 
all -  [ What local embedding models are you guys using today? Frameworks? ](https://www.reddit.com/r/LLMDevs/comments/1blwu6m/what_local_embedding_models_are_you_guys_using/) , 2024-03-25-0910
```
I've been using BAAI/bge-base-en-v1.5 embeddings with the HuggingFaceBgeEmbeddings wrapper from langchain\_community.emb
eddings for the past several months. It was SotA when I started using it, and the langchain integration is really nice. 
But I'm curious how you guys are architecting your local RAG pipelines. What models are you using? Are you using langcha
in-compatible vectorstores? 

Not interested in off-prem embedding solutions like OpenAI, Pinecone, Cohere, Databricks, 
etc. 

Thanks!
```
---

     
 
all -  [ Langchain with custom local LLM api ](https://www.reddit.com/r/LangChain/comments/1blrpbz/langchain_with_custom_local_llm_api/) , 2024-03-25-0910
```
I am trying to make use of langgraph, but I'm getting stuck at using langchain with my own 'customllm'  


[https://pyth
on.langchain.com/docs/modules/model\_io/llms/custom\_llm](https://python.langchain.com/docs/modules/model_io/llms/custom
_llm)  


It doesn't say any where how  I am suppose to link all that with my API, any help will be appreciated.
```
---

     
 
all -  [ Building memory with GPT's API ](https://www.reddit.com/r/ChatGPT/comments/1blpzt6/building_memory_with_gpts_api/) , 2024-03-25-0910
```
Hi developpers,

I am wondering what everyone's technique around building memory with GPT API connections in application
s. I know langchain has built great methods around this but wondering what everyone is using?
```
---

     
 
all -  [ Feedback request for a new OSS project ](https://www.reddit.com/r/PromptDesign/comments/1blp6ud/feedback_request_for_a_new_oss_project/) , 2024-03-25-0910
```
Hey folks, I was frustrated with all the complexity around building a RAG pipeline which respects access privileges of t
he session users. So I built a quick weekend project. PromptSage is a minimal prompt builder with built-in security/priv
acy/access controls, and is compatible with langchain and other major tools in the space. Would love any and all feedbac
k!

[https://github.com/alexmavr/promptsage](https://github.com/alexmavr/promptsage)
```
---

     
 
all -  [ Feedback request for a new OSS project ](https://www.reddit.com/r/PromptEngineering/comments/1blp6lc/feedback_request_for_a_new_oss_project/) , 2024-03-25-0910
```
Hey folks, I was frustrated with all the complexity around building a RAG pipeline which respects access privileges of t
he session users. So I built a quick weekend project. PromptSage is a minimal prompt builder with built-in security/priv
acy/access controls, and is compatible with langchain and other major tools in the space. Would love any and all feedbac
k!  
https://github.com/alexmavr/promptsage
```
---

     
 
all -  [ How can we send reranked documents to any llm chain instead of retriever? ](https://www.reddit.com/r/LangChain/comments/1bllgb8/how_can_we_send_reranked_documents_to_any_llm/) , 2024-03-25-0910
```
I am working on a rag application where I need to rerank the docs, I tried langchain integrations like colbert, flashran
k but I wanted to implement other rankers now I have a list of relevant docs after the user query, any suggestions on ho
w can I send this as parameter to llm chain.   
Below is sample code from langchain cookbook.  


from langchain\_core.r
unnables import RunnableParallel  
rag\_chain\_from\_docs = (  
RunnablePassthrough.assign(context=(lambda x: format\_do
cs(x\['context'\])))  
 | prompt  
 | llm  
 | StrOutputParser()  
)  
rag\_chain\_with\_source = RunnableParallel(  
 {
'context': retriever, 'question': RunnablePassthrough()}  
).assign(answer=rag\_chain\_from\_docs)  
rag\_chain\_with\_s
ource.invoke('What is Task Decomposition') 
```
---

     
 
all -  [ Beginner trying make a simple RAG with Graphql documentation. Not getting anywhere. ](https://www.reddit.com/r/LangChain/comments/1bljqco/beginner_trying_make_a_simple_rag_with_graphql/) , 2024-03-25-0910
```
Im passing in my Graphql documentation as html and splitting it by section tag. I want to search that data and return th
e relevant information for that query or mutation. However, both `retriever.get_relevant_documents` and `vector.similari
ty_search` returns all the same data that `print(documents)` prints out (the entire document's text). Any help would be 
appreciated. Thank you.

    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores imp
ort FAISS
    from langchain_text_splitters import HTMLHeaderTextSplitter

    embeddings = OpenAIEmbeddings()
    html 
= open('src/bff/index.html', 'r').read()

    headers_to_split_on = [
      ('section > h2', 'GraphQL query, mutation or
 type definition'),
    ]

    html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    docum
ents = html_splitter.split_text(html)
    print(documents)

    vector = FAISS.from_documents(documents, embeddings)
   
 retriever = vector.as_retriever()

    response1 = retriever.get_relevant_documents('WorkflowDto definition')
    print
(response1)

    response2 = vector.similarity_search('WorkflowDto definition')
    print(response2)
```
---

     
 
all -  [ Why do we need LlamaIndex or LangChain for communicating with Large Language Models (LLM)? ](https://www.reddit.com/r/LangChain/comments/1bliwzp/why_do_we_need_llamaindex_or_langchain_for/) , 2024-03-25-0910
```
I've recently been exploring the development of projects using large language models (LLMs) like the GPT series and enco
untered a question: Why should we consider using tools like LlamaIndex or LangChain as intermediaries for communication 
with LLMs, rather than directly interacting with LLMs through the API in the repository layer?

From my understanding, d
irectly using the API seems to offer a more simplified and direct control path, potentially avoiding the introduction of
 additional complexity and potential performance bottlenecks. However, I've also heard that these tools (LlamaIndex and 
LangChain) can enhance the efficiency and effectiveness of communication with LLMs.

Specifically, I have the following 
questions:

How do LlamaIndex and LangChain optimize the efficiency of communication with LLMs? What specific performanc
e optimizations and functional enhancements do they provide that make interactions with LLMs faster and more effective?


In what situations might direct communication with LLMs via the API not be the best choice? Are these tools primarily a
ddressing certain specific technical challenges or needs?

What are the potential advantages and disadvantages of using 
LlamaIndex or LangChain compared to direct communication with LLMs? Especially considering the impact on architectural c
omplexity, development and maintenance costs, as well as scalability and flexibility.
```
---

     
 
all -  [ langchain with azure openai ](https://www.reddit.com/r/LangChain/comments/1blhhxq/langchain_with_azure_openai/) , 2024-03-25-0910
```
anyone have  done a project  with azure open ai and different azure services like postgress for storing the embedding an
d azure blob for storing the files 
```
---

     
 
all -  [ What is the current best embedding model for semantic search? ](https://www.reddit.com/r/LangChain/comments/1blfg7i/what_is_the_current_best_embedding_model_for/) , 2024-03-25-0910
```
I'm trying to implement RAG with semantic search and have been using OpenAI text embedding 3 small, but the results aren
't particularly good. Do you know any that is at least better than this one on which I can experiment on? 
```
---

     
 
all -  [ Improve function calling ](https://www.reddit.com/r/LangChain/comments/1bley1d/improve_function_calling/) , 2024-03-25-0910
```
Hey folks!

I'm building a function calling prompt, but the results are terrible.

# Prompt

>Please select the best fun
ction to answer user questions and context. Follow this instructions:

# Functions structure

**GetDeliveryStatusForWork
Items**

Get the delivery status (whether late or on track) for work items. Response structure: {{'workItemsWithDelivery
Status': \[{'id': 'string', 'key': 'string', 'title': 'string', 'actualStatus': 'string', 'assignedTo': 'string', 'leadT
imeToEnd': 'number', 'leadTimeUsed': 'number', 'percentageLeadTimeAlreadyUsed': 'number', 'leadTimeToEndWithLeadTimeAlre
adyUsed': 'number', 'percentageLeadTimeExceeded': 'number', 'isLate': 'boolean', 'onTrackFlag': 'string'}\]}}

**GetWork
ItensTool**

Get work itens by keys or ids passed as parameters. Response structure: { 'WorkItems': \[{'key':'string','i
d':'string','name':'string','description':'string','created':'string','updated':'string','changelog':\[{'id':'string','c
reatedAt':'string','movements':\[{'field':'string','fromColumnId':'string','fromColumnName':'string','toColumnId':'strin
g','toColumnName':'string'}\]}\],'workItemCreatedAt':'string','columnName':'string','priority':'string','flagged':'boole
an','assignee':{'accountId':'string','userName':'string'},'workItemType':{'name':'string','id':'string','description':'s
tring','subtask':'boolean'},'status':{'name':'string','id':'string','statusCategory':{'name':'string','id':'number'}}}\]
}

# Functions JSON Schema

\`\`\`TOOLS

* 0: {   'type': 'function',   'function': {     'name': 'GetColumnsConfigTool'
,     'description': 'Get the Id and Name for columns(To Do, WIP, and Done) from a board along with their respective ord
er. Response Structure: \\'{\\'wipColumnsAndDoneColumns\\':\[\\'string\\'\],\\'columnsConfig\\':{\\'allColumns\\':\[{\\'
id\\':\\'string\\',\\'name\\':\\'string\\',\\'order\\':\\'number|null\\',\\'column\\':\\'string\\'}\],\\'wipColumns\\':\
[\\'string\\'\],\\'doneColumns\\':\[\\'string\\'\],\\'todoColumns\\':\[\\'string\\'\]}}\\'',     'parameters': {       '
type': 'object',       'properties': {},       'additionalProperties': false,       '$schema': 'http://json-schema.org/d
raft-07/schema#'     }   } }
* 1: {   'type': 'function',   'function': {     'name': 'GetWorkItemsDeliveryStatusTool', 
    'description': 'Get the delivery status (whether late or on track) for work items. Response structure: {{\\'workItem
sWithDeliveryStatus\\': \[{\\'id\\': \\'string\\', \\'key\\': \\'string\\', \\'title\\': \\'string\\', \\'actualStatus\\
': \\'string\\', \\'assignedTo\\': \\'string\\', \\'leadTimeToEnd\\': \\'number\\', \\'leadTimeUsed\\': \\'number\\', \\
'percentageLeadTimeAlreadyUsed\\': \\'number\\', \\'leadTimeToEndWithLeadTimeAlreadyUsed\\': \\'number\\', \\'percentage
LeadTimeExceeded\\': \\'number\\', \\'isLate\\': \\'boolean\\', \\'onTrackFlag\\': \\'string\\'}\]}}\\n This function ne
ed a get workItem function before.',     'parameters': {       'type': 'object',       'properties': {         'paramete
rs': {           'type': 'array',           'items': {             'type': 'object',             'properties': {        
       'workItems': {                 'type': 'array',                 'items': {                   'type': 'string',   
                'description': 'Work Item Id'                 },                 'description': 'value extracted from a 
text and returned as a parameter, examples of what the value looks like (GE-18, KDZ-20, NT-10, HYPER-44, APP-538)'      
         }             },             'additionalProperties': false           }         }       },       'required': \[ 
        'parameters'       \],       'additionalProperties': false,       '$schema': 'http://json-schema.org/draft-07/sc
hema#'     }   } }
* 2: {   'type': 'function',   'function': {     'name': 'GetWorkItensTool',     'description': 'Get 
work itens by keys or ids passed as parameters. Response structure: { \\'WorkItems\\': \[{\\'key\\':\\'string\\',\\'id\\
':\\'string\\',\\'name\\':\\'string\\',\\'description\\':\\'string\\',\\'created\\':\\'string\\',\\'updated\\':\\'string
\\',\\'changelog\\':\[{\\'id\\':\\'string\\',\\'createdAt\\':\\'string\\',\\'movements\\':\[{\\'field\\':\\'string\\',\\
'fromColumnId\\':\\'string\\',\\'fromColumnName\\':\\'string\\',\\'toColumnId\\':\\'string\\',\\'toColumnName\\':\\'stri
ng\\'}\]}\],\\'workItemCreatedAt\\':\\'string\\',\\'columnName\\':\\'string\\',\\'priority\\':\\'string\\',\\'flagged\\'
:\\'boolean\\',\\'assignee\\':{\\'accountId\\':\\'string\\',\\'userName\\':\\'string\\'},\\'workItemType\\':{\\'name\\':
\\'string\\',\\'id\\':\\'string\\',\\'description\\':\\'string\\',\\'subtask\\':\\'boolean\\'},\\'status\\':{\\'name\\':
\\'string\\',\\'id\\':\\'string\\',\\'statusCategory\\':{\\'name\\':\\'string\\',\\'id\\':\\'number\\'}}}\]}',     'para
meters': {       'type': 'object',       'properties': {         'parameters': {           'type': 'object',           '
properties': {             'workItemsIds': {               'type': 'array',               'items': {                 'ty
pe': 'string',                 'description': 'WorkItemId. identifier for a work item. Examples: GE-18, KDZ-20, NT-10, H
YPER-44, APP-538. Each ID represents a specific work item in a project or system.'               }             }        
   },           'additionalProperties': false,           'description': 'Array of paramaters mentioned in text. You can 
use chat history to provide more context and get parameters'         },         'operation': {           'type': 'array'
,           'items': {             'type': 'string',             'enum': \[               'ByWeek',               'inWIP
',               'ByIds',               'Last24hours',               'ByTypes'             \],             'description'
: 'The inner filter for Work Items.'           }         }       },       'required': \[         'parameters',         '
operation'       \],       'additionalProperties': false,       '$schema': 'http://json-schema.org/draft-07/schema#'    
 }   } }\`\`\`

# User question

What are the delivery dates for tasks that are in progress?

# Expected result

functio
ns GetWorkItensTool and GetDeliveryStatusForWorkItems.

# Actual result

function GetWorkItensTool

----------

Would yo
u happen to have any tips about how to improve it? Is there any better model than openAI GPT-4-turbo for it?
```
---

     
 
all -  [ Document Loaders Outputting 'NO_OUTPUT' ](https://www.reddit.com/r/LangChain/comments/1blc6q2/document_loaders_outputting_no_output/) , 2024-03-25-0910
```
Hi, currently I am working on an RAG tool for my company. I have to load multiple PDFs and Powerpoints, for which I use 
the UnstructuredPDFLoader and UnstructuredPowerPointLoader, because a lot of these documents contain images with text on
 them and these loaders allow you to extract said text through OCR. However, when I run this and the program goes throug
h the retrieval steps, I get an error coming from a deprecated function, along with the output of each document split th
at will be used to answer my query. The answers to my questions are not of a high quality, and I believe that it may be 
attributed to something being wrong with my loaders because the output I am seeing for some document splits is 'NO\_OUTP
UT' or 'NO\_OUTPUT\_OUTPUT'.

I am wondering if any of you have run into this problem. In addition, as a bonus question,
 how do you all maintain metadata like source information in your document splits? I always lose mine.



Below is the r
etrieval code:

    # Vector Database
    u/st.cache_resource
    def vector_db_init(_folder_id, _model):
        '''Vec
tor db initializer, plus contextual compression addition'''
        persist_directory = './db/'  # Persist directory pat
h
    
        # Embeddings to be applied
        embeddings = VertexAIEmbeddings(
            model_name='textembedding
-gecko-multilingual',
            credentials=CREDENTIALS,
            project_id=PROJECT_ID,
            )
    
       
 # Document splitting, embedding and vector database loading
        # DOES NOT have to be done in every run, just once 
and after you can simply refer to the db
        if not os.path.exists(persist_directory):
            # Data Pre-proces
sing
            # TODO- loader that can correct typos and what-not
            pdf_loader = DirectoryLoader('/Users/mar
conardoneguerra/Desktop/e3_Consulting/Other/AI/Proposal RAG/docs',
                                         glob='**/*.p
df',
                                         recursive=True,
                                         show_progress=Tru
e,
                                         loader_cls=UnstructuredPDFLoader,
                                         l
oader_kwargs={
                                            #'extract_images':True,
                                     
       'post_processors':[clean_extra_whitespace, clean_non_ascii_chars, clean], # data cleaning
                       
                     'mode':'single',
                                            'strategy':'hi_res',
                 
                           'high_res_model_name':'detectron2_onnx',
                                            #'encodi
ng':'unicode'
                                         })
            
            ppt_loader = DirectoryLoader('/Users/
marconardoneguerra/Desktop/e3_Consulting/Other/AI/Proposal RAG/docs',
                                         glob='**/
*.pptx',
                                         recursive=True,
                                         show_progress
=True,
                                         loader_cls=UnstructuredPowerPointLoader,
                               
          loader_kwargs={
                                            #'extract_images':True,
                          
                  'post_processors':[clean_extra_whitespace, clean_non_ascii_chars, clean], # data cleaning
            
                                'mode':'single',
                                            'strategy':'hi_res',
      
                                      'high_res_model_name':'detectron2_onnx',
                                         
   #'encoding':'unicode'
                                         })
    
            loaded_pdfs = pdf_loader.load()
  
          loaded_ppts = ppt_loader.load()
    
            print('# of PDFs:' + str(len(loaded_pdfs)))
            print
('# of PPTs:' + str(len(loaded_ppts)))
            loaded_docs = loaded_pdfs + loaded_ppts
    
            # gdrive_doc
uments = doc_processor(gdrive_documents, image_captioning)
    
            context = '\n\n'.join(str(p.page_content) fo
r p in loaded_docs)
    
            # had to remove below because this splitter is new and does not have a max token si
ze, hence has given chunks too large to handle
            # splitter = SemanticChunker(embeddings)
            splitter
 = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=25) 
            data = splitter.split_text(context)
   
         
            print('Data Processing Complete')
    
            vectordb = Chroma.from_texts(
                d
ata, embeddings, persist_directory=persist_directory
            )
            vectordb.persist()
    
            print
('Vector DB Creating Complete\n')
    
        elif os.path.exists(persist_directory):
            vectordb = Chroma(
  
              persist_directory=persist_directory, embedding_function=embeddings
            )
    
            print('V
ector DB Loaded\n')
    
        # Compresses what is contextually needed for query answer (?)
        compressor = LLMC
hainExtractor.from_llm(_model, )
        compression_retriever = ContextualCompressionRetriever(base_compressor=compress
or, 
                                                               base_retriever=vectordb.as_retriever(search_type='si
milarity', search_kwargs={'k': 24}))
    
        return compression_retriever
    
    
    @st.cache_resource
    def 
chain_init(_model, _retriever):
        '''Initializes chain for retrieval'''
        # DONE- conversational template
  
      template = '''
        Who you are:
        You are an expert on everything about e3 Consulting, AKA e3, a consult
ing firm based in San Juan, Puerto Rico.
        Your firm specializes in IT consulting. \
        ------
        Instru
ctions:
        You will be receiving questions about e3 and their previous work. \
        You will gather knowledge to
 deliver a good response to the user (separated with <ctx></ctx>). \
        If you don't know the answer, answer with '
Unfortunately, I don't have the information.' \
        If you don't find enough information below, also answer with 'Un
fortunately, I don't have the information.' \
        The context will most likely have typos in it, please correct them
 when you formulate your answer. \
        ------
        <ctx>
        {context}
        </ctx>
        ------ 
       
 {question}
        Answer:
        '''
    
        # template above
        question_prompt_template = PromptTemplate(
template=template, input_variables=['question', 'context'])
    
        # We create a qa chain with our llm, retriever,
 and memory
        # Use chain_type refine so we cna build off of different information,
        # in addition to being
 wary of our context window
        # TODO make this conversational (could be complex)
        qa_chain = RetrievalQA.fr
om_chain_type(
            llm=_model,
            chain_type='stuff',
            return_source_documents=True,
       
     retriever=_retriever,
            verbose=True,
        )
    
        # qa_chain = RetrievalQA | StrOutputParser()

    
        return qa_chain

  
Error examples:

    NO_OUTPUT_OUTPUT/Users/marconardoneguerra/anaconda3/envs/proposal
-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: The predict_and_parse method is deprecated, 
instead pass an output parser directly to LLMChain.
      warnings.warn(
    NO_OUTPUT_OUTPUT/Users/marconardoneguerra/a
naconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: The predict_and_parse 
method is deprecated, instead pass an output parser directly to LLMChain.
      warnings.warn(
    NO_OUTPUT_OUTPUT/User
s/marconardoneguerra/anaconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: 
The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain.
      warnings.warn(
   
 NO_OUTPUT_OUTPUT/Users/marconardoneguerra/anaconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm
.py:316: UserWarning: The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain.




Thanks!
```
---

     
 
all -  [ Free NVIDIA AI course list ](https://i.redd.it/n0xmj0tpoypc1.jpeg) , 2024-03-25-0910
```
1. **Generative AI Explained**

What you'll learn:

• Generative AI and explain how Generative AI works.

• Various Gene
rative AI applications.

• Challenges and opportunities in Generative AI

[Link](https://courses.nvidia.com/courses/cour
se-v1:DLI+S-FX-07+V1/)

2. **Building A Brain in 10 Minutes**

What you'll learn:

• Exploring how neural networks use d
ata to learn

• Understanding the math behind a neuron

[Link](https://courses.nvidia.com/courses/course-v1:DLI+T-FX-01+
V1/)

Sign up to our [newsletter](https://www.thepromptindex.com/newsletter.html) for our weekly AI roundup. 

3. **Augm
ent your LLM with Retrieval Augmented Generation:**

What you'll learn:

• Basics of Retrieval Augmented Generation

• R
AG retrieval process

• NVIDIA AI Foundations and RAG model components

[Link](https://courses.nvidia.com/courses/course
-v1:NVIDIA+S-FX-16+v1/)

4. **AI in the Data Center:**

What you'll learn:

• AI use cases, Machine Learning, Deep Learn
ing, and their workflows.

• GPU architecture and its impact on AI.

• Deep learning frameworks, and deployment consider
ations.

[Link](https://www.coursera.org/learn/introduction-ai-data-center)

5. **Accelerate Data Science Workflows with
 Zero Code Changes:**

What you'll learn:

• Learn benefits of unified CPU and GPU workflows

• GPU-accelerate data proc
essing and ML without code changes

• Experience faster processing times

[Link](https://courses.nvidia.com/courses/cour
se-v1:DLI+T-DS-03+V1/)

6. **Mastering Recommender Systems:**

What you'll learn:

• Strategies from Kaggle Grandmasters
 on building recommendation systems for e-commerce.

• Cover 2-stage models, candidate generation, feature engineering, 
and ensembling.

[Link](https://www.classcentral.com/course/youtube-grandmaster-series-mastering-recommender-systems-184
298)

7. **Networking Introduction:**

What you'll learn:

• Learn about networks and their importance.

• Explore Ether
net basics and data forwarding in Ethernet networks.

• Discuss network components, requirements, OSI model, TCP/IP prot
ocol

[Link](https://www.coursera.org/learn/introduction-to-networking-nvidia)

8. **How to Perform Large-Scale Image Cl
assification**

What you'll learn:

• Learn large-scale image classification

• Cover challenges, modeling techniques AN
D validation strategies.

[Link](https://www.classcentral.com/course/youtube-grandmaster-series-how-to-perform-large-sca
le-image-classification-130184)

9. **Building RAG Agents with LLMs:**

What you'll learn:

• Scalable deployment strate
gies for LLMs and vector databases.

• Modern LangChain paradigms for dialog management and document retrieval.

• Using
 advanced models and steps for production.

[Link](https://courses.nvidia.com/courses/course-v1:DLI+S-FX-15+V1/)
```
---

     
 
all -  [ LangChain single input Agent params ](https://www.reddit.com/r/LangChain/comments/1blaz9d/langchain_single_input_agent_params/) , 2024-03-25-0910
```
Hi community, looking for some guidance to explain how this is called when I specify the Tool's parameters as a descript
ion rather than Fields. 

For some reason Fields does not work in that project, giving me exception like

    ERROR:root
:An error occurred ZeroShotAgent does not support multi-input tool 

&#x200B;

Here is some code

    class SimpleInputs
(BaseModel):
        input: str
        
    class GetEvents(BaseTool):
        name = 'get_calendar_event'
        desc
ription = 'Use this tool with arguments like '{{'start_date': 'yyyy-mm-dd', 'max_results': int}}' when you need to retri
eve events from Calendar.'
        args_schema: Type[BaseModel] = SimpleInputs
        return_direct: bool = False
    

    ---
            agent = initialize_agent(
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
             
   tools=tools,
                llm=self.llm,
                verbose=True,

&#x200B;
```
---

     
 
all -  [ Does anyone have a codebase or tutorial for using LLMs with LangChain to summarize each row in a dat ](https://www.reddit.com/r/LangChain/comments/1bl7k4g/does_anyone_have_a_codebase_or_tutorial_for_using/) , 2024-03-25-0910
```
 Does anyone have a codebase or tutorial for using LLMs with LangChain to summarize each row in a database and generate 
output for each? I have a database that is updated weekly, which you can think of as a record of transactions. I'm looki
ng for a way to read each row of this database weekly, summarize the contents of those records, and have it tweeted out.
 I'm curious if there's a tutorial or codebase somewhere that does this. 
```
---

     
 
all -  [ 23 New Data Science, Data Engineering and Machine Learning jobs ](https://www.reddit.com/r/BigDataJobs/comments/1bl4juz/23_new_data_science_data_engineering_and_machine/) , 2024-03-25-0910
```
|Job Title|Company|Location|Country|Skills|
|:-|:-|:-|:-|:-|
|[Mid Data Engineer (3733 USD/Mes)](https://datayoshi.com/o
ffer/906372/mid-data-engineer-3733-usd-me)|[Listopro](https://www.datayoshi.com/company/listopro-jobs)|[Argentina](https
://datayoshi.com/offer/906372/mid-data-engineer-3733-usd-me)|[Argentina](https://datayoshi.com/offer/906372/mid-data-eng
ineer-3733-usd-me)|[Python, SQL](https://datayoshi.com/offer/906372/mid-data-engineer-3733-usd-me)|
|[Data engineer pyth
on H/F chez SAFRAN](https://datayoshi.com/offer/105682/data-engineer-python-h-f-chez)|[Kicklox - Plateforme de matching 
entre talents tech & porteurs de projets](https://www.datayoshi.com/company/kicklox---plateforme-de-matching-entre-talen
ts-tech-&-porteurs-de-projets-jobs)|[Gonfreville-l’Orcher](https://datayoshi.com/offer/105682/data-engineer-python-h-f-c
hez)|[France](https://datayoshi.com/offer/105682/data-engineer-python-h-f-chez)|[SQL](https://datayoshi.com/offer/105682
/data-engineer-python-h-f-chez)|
|[Machine Learning Engineer](https://datayoshi.com/offer/287675/machine-learning-engine
er)|[Mirakl](https://www.datayoshi.com/company/mirakl-jobs)|[Bordeaux](https://datayoshi.com/offer/287675/machine-learni
ng-engineer)|[France](https://datayoshi.com/offer/287675/machine-learning-engineer)|[Spark, NLP, Machine Learning](https
://datayoshi.com/offer/287675/machine-learning-engineer)|
|[Senior Data Engineer](https://datayoshi.com/offer/343227/sen
ior-data-engineer)|[Samsara](https://www.datayoshi.com/company/samsara-jobs)|[United States](https://datayoshi.com/offer
/343227/senior-data-engineer)|[Remote](https://datayoshi.com/offer/343227/senior-data-engineer)|[SQL, ETL, AWS](https://
datayoshi.com/offer/343227/senior-data-engineer)|
|[Senior Azure Data Engineer](https://datayoshi.com/offer/751025/senio
r-azure-data-engineer)|[Numentica](https://www.datayoshi.com/company/numentica-jobs)|[Palo Alto](https://datayoshi.com/o
ffer/751025/senior-azure-data-engineer)|[Remote](https://datayoshi.com/offer/751025/senior-azure-data-engineer)|[Spark, 
SQL](https://datayoshi.com/offer/751025/senior-azure-data-engineer)|
|[AI Engineer (Python, Langchain)](https://datayosh
i.com/offer/240666/ai-engineer-python-langchain)|[JUPUS](https://www.datayoshi.com/company/jupus-jobs)|[Germany](https:/
/datayoshi.com/offer/240666/ai-engineer-python-langchain)|[Germany](https://datayoshi.com/offer/240666/ai-engineer-pytho
n-langchain)|[Python](https://datayoshi.com/offer/240666/ai-engineer-python-langchain)|
|[Senior Data Analyst](https://d
atayoshi.com/offer/551411/senior-data-analyst)|[YEGO](https://www.datayoshi.com/company/yego-jobs)|[Barcelona](https://d
atayoshi.com/offer/551411/senior-data-analyst)|[Spain](https://datayoshi.com/offer/551411/senior-data-analyst)|[SQL](htt
ps://datayoshi.com/offer/551411/senior-data-analyst)|
|[Data Analyst](https://datayoshi.com/offer/505803/data-analyst)|[
Peroptyx](https://www.datayoshi.com/company/peroptyx-jobs)|[Milan](https://datayoshi.com/offer/505803/data-analyst)|[Ita
ly](https://datayoshi.com/offer/505803/data-analyst)|[](https://datayoshi.com/offer/505803/data-analyst)|
|[Data Enginee
r (m/w/d) 100%](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|[MDPI](https://www.datayoshi.com/company/mdp
i-jobs)|[Basel](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|[Switzerland](https://datayoshi.com/offer/49
5742/data-engineer-m-w-d-100)|[SQL, ETL, Scala](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|
|[Junior Da
ta Analyst](https://datayoshi.com/offer/462463/junior-data-analyst)|[All Response Media](https://www.datayoshi.com/compa
ny/all-response-media-jobs)|[London](https://datayoshi.com/offer/462463/junior-data-analyst)|[United Kingdom](https://da
tayoshi.com/offer/462463/junior-data-analyst)|[SQL](https://datayoshi.com/offer/462463/junior-data-analyst)|
|[Sr Data A
nalyst](https://datayoshi.com/offer/113494/sr-data-analyst)|[PedidosYa](https://www.datayoshi.com/company/pedidosya-jobs
)|[Greater Buenos Aires](https://datayoshi.com/offer/113494/sr-data-analyst)|[Argentina](https://datayoshi.com/offer/113
494/sr-data-analyst)|[Looker, SQL, Python](https://datayoshi.com/offer/113494/sr-data-analyst)|
|[Data Scientist - All L
evels!](https://datayoshi.com/offer/727798/data-scientist-all-levels)|[BIP Brasil](https://www.datayoshi.com/company/bip
-brasil-jobs)|[Brazil](https://datayoshi.com/offer/727798/data-scientist-all-levels)|[Brazil](https://datayoshi.com/offe
r/727798/data-scientist-all-levels)|[Modeling](https://datayoshi.com/offer/727798/data-scientist-all-levels)|
|[Data Eng
ineer, Prime Video Discovery Analytics](https://datayoshi.com/offer/170470/data-engineer-prime-video-dis)|[Prime Video &
 Amazon Studios](https://www.datayoshi.com/company/prime-video-&-amazon-studios-jobs)|[London](https://datayoshi.com/off
er/170470/data-engineer-prime-video-dis)|[United Kingdom](https://datayoshi.com/offer/170470/data-engineer-prime-video-d
is)|[AWS, Scala](https://datayoshi.com/offer/170470/data-engineer-prime-video-dis)|
|[Azure Data Engineer](https://datay
oshi.com/offer/423231/azure-data-engineer)|[emagine](https://www.datayoshi.com/company/emagine-jobs)|[Warsaw](https://da
tayoshi.com/offer/423231/azure-data-engineer)|[Poland](https://datayoshi.com/offer/423231/azure-data-engineer)|[Python, 
Scala, SQL](https://datayoshi.com/offer/423231/azure-data-engineer)|
|[Machine Learning Engineer](https://datayoshi.com/
offer/788069/machine-learning-engineer)|[DKATALIS](https://www.datayoshi.com/company/dkatalis-jobs)|[Singapore](https://
datayoshi.com/offer/788069/machine-learning-engineer)|[Singapore](https://datayoshi.com/offer/788069/machine-learning-en
gineer)|[Python, Machine Learning](https://datayoshi.com/offer/788069/machine-learning-engineer)|
|[Alternant Data Engin
eer H/F](https://datayoshi.com/offer/795287/alternant-data-engineer-h-f)|[Lyreco France](https://www.datayoshi.com/compa
ny/lyreco-france-jobs)|[Marly](https://datayoshi.com/offer/795287/alternant-data-engineer-h-f)|[France](https://datayosh
i.com/offer/795287/alternant-data-engineer-h-f)|[Python, Spark, Hadoop](https://datayoshi.com/offer/795287/alternant-dat
a-engineer-h-f)|
|[Machine Learning Engineer](https://datayoshi.com/offer/938934/machine-learning-engineer)|[Morgan McKi
nley](https://www.datayoshi.com/company/morgan-mckinley-jobs)|[Toronto](https://datayoshi.com/offer/938934/machine-learn
ing-engineer)|[Canada](https://datayoshi.com/offer/938934/machine-learning-engineer)|[Machine Learning, NLP](https://dat
ayoshi.com/offer/938934/machine-learning-engineer)|
|[Data Scientist](https://datayoshi.com/offer/395728/data-scientist)
|[Desigual](https://www.datayoshi.com/company/desigual-jobs)|[Greater Barcelona Metropolitan Area](https://datayoshi.com
/offer/395728/data-scientist)|[Spain](https://datayoshi.com/offer/395728/data-scientist)|[Machine Learning](https://data
yoshi.com/offer/395728/data-scientist)|
|[Data Scientist](https://datayoshi.com/offer/769393/data-scientist)|[Contents.c
om](https://www.datayoshi.com/company/contents.com-jobs)|[Milan](https://datayoshi.com/offer/769393/data-scientist)|[Ita
ly](https://datayoshi.com/offer/769393/data-scientist)|[Python, NLP](https://datayoshi.com/offer/769393/data-scientist)|

|[STAGE - Ingénieur Data Scientist Junior F/H](https://datayoshi.com/offer/601797/stage-ingenieur-data-scienti)|[Plasti
c Omnium](https://www.datayoshi.com/company/plastic-omnium-jobs)|[Venette](https://datayoshi.com/offer/601797/stage-inge
nieur-data-scienti)|[France](https://datayoshi.com/offer/601797/stage-ingenieur-data-scienti)|[Deep Learning](https://da
tayoshi.com/offer/601797/stage-ingenieur-data-scienti)|
|[Data Analyst, Commerce & Marketing Analytics](https://datayosh
i.com/offer/456146/data-analyst-commerce-marke)|[Fandom](https://www.datayoshi.com/company/fandom-jobs)|[London](https:/
/datayoshi.com/offer/456146/data-analyst-commerce-marke)|[United Kingdom](https://datayoshi.com/offer/456146/data-analys
t-commerce-marke)|[Python, Pandas, Tableau](https://datayoshi.com/offer/456146/data-analyst-commerce-marke)|
|[Junior Da
ta Analyst- Banking](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[Skill Farm](https://www.datayoshi.
com/company/skill-farm-jobs)|[Johannesburg](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[South Afric
a](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[SQL, Tableau](https://datayoshi.com/offer/239002/jun
ior-data-analyst-banking)|
|[Data Analyst - Power BI](https://datayoshi.com/offer/381956/data-analyst-power-bi)|[Energy 
Jobline](https://www.datayoshi.com/company/energy-jobline-jobs)|[London](https://datayoshi.com/offer/381956/data-analyst
-power-bi)|[United Kingdom](https://datayoshi.com/offer/381956/data-analyst-power-bi)|[Power BI](https://datayoshi.com/o
ffer/381956/data-analyst-power-bi)|
                        
 Hey, here are 23 New Data Science, Data Engineering and Ma
chine Learning jobs. 

 For more, check our Google sheet with more opportunities in Data Science and Machine Learning (u
pdated each week) [here](https://docs.google.com/spreadsheets/d/1Vsg1Jmc0ZIDc_tPqZTzhbgxGIeTDQkUsBySMNbbCFI4/) 

 If you
 want to take some Data and ML courses, click [here](https://learncrunch.com/courses?utm_source=reddit&source=reddit) 


  Let me know if you have any questions. Cheers!
```
---

     
 
all -  [ Langchain GPT ](https://www.reddit.com/r/LangChain/comments/1bl3lpg/langchain_gpt/) , 2024-03-25-0910
```
Hey everyone, just wanted to ask if you know any Langchain GPTs that actually works and is updated with the latest Langc
hain documents?  
Thanks
```
---

     
 
all -  [ How do you verify, aside from manually checking the PDFs, that your answers are correct from a simpl ](https://www.reddit.com/r/LangChain/comments/1bl1p6d/how_do_you_verify_aside_from_manually_checking/) , 2024-03-25-0910
```
Hi! I'm new to Langchain and tinkering with LLMs in general, I'm just doing a small project on Langchain's capabilities 
on document loading, chunking, and of course using a similarity search on a vectorstore and then using the information I
 retrieve in a chain to get an answer.

I'm only testing on a small dataset, so it's easy for me to see the specific fil
es and pages to cross check whether it is the best result among the different files. But it got me thinking: if I try to
 work with a larger dataset, how exactly do I verify if the answer is the best result in the ranking and if it is indeed
 correct?

Is it possible to get datasets where it contains a PDF, some test input prompts, and an expected certain corr
ect output? This way, I would be able to use my project to ingest that data and see if I get similar results? Or is this
 too good to be true?
```
---

     
 
all -  [ Feedback for my beginner RAG pdf project ](https://www.reddit.com/r/learnmachinelearning/comments/1bkzkpq/feedback_for_my_beginner_rag_pdf_project/) , 2024-03-25-0910
```
Hello.

I wanted to create a RAG model for a T&C file of one bank. I am a beginner, and all my files are on github. [htt
ps://github.com/divakaivan/lloyds-rag-from-scratch/tree/main](https://github.com/divakaivan/lloyds-rag-from-scratch/tree
/main) \-> the main files you can look at are: [preprocess\_pdf.py](https://github.com/divakaivan/lloyds-rag-from-scratc
h/blob/main/preprocess_pdf.py) and [rag.py](https://github.com/divakaivan/lloyds-rag-from-scratch/blob/main/rag.py)

My 
main points of concern are the way I do chunking (everything I do in preprocess\_pdf.py), I have found out it's way more
 important than I initially thought, and for now, I am using a recursive char splitter from langchain. My base prompt in
 rag.py could probably use help as well. Any feedback is welcome. I am a beginner :)

At the moment, the answers are inc
onsistent, for example for the question: 'What is meant by a Business Day?' when looking at the context, the top-1 answe
r includes it and the cos\_sim is 0.8, but sometimes the llm returns that the context does not talk about the Business D
ay, even though the top-1 answer from the context is that part I mentioned.

Any help/criticism is appreciated. Thank yo
u :)

&#x200B;

if you don't want to click, here is the code:

**preprocess\_pdf.py**
```python
import re
import os
impo
rt fitz
import pandas as pd
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import R
ecursiveCharacterTextSplitter

device = 'mps'

# lbg_relationship_tnc.pdf account_bank_tnc.pdf
def open_and_read_pdf(pdf
_path: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages_n_texts = []

    for page_n, page in enumerate(doc):

        text = page.get_text()
        text = text.replace('\n', ' ').replace('  ', ' ')

        pages_n_texts.append(
{
            'page_n': page_n,
            'page_char_count': len(text),
            'page_word_count_raw': len(text.sp
lit(' ')),
            'page_sentence_count_raw': len(text.split('. ')),
            'page_token_count': len(text) / 4, 
# 1 token ~= 4 chars
            'text': text
        })

    return pages_n_texts

def create_text_splitter(chunk_size:
 int=1500, chunk_overlap: int=0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overla
p=chunk_overlap)
    return text_splitter


emb_model = SentenceTransformer('mixedbread-ai/mxbai-embed-large-v1').to(dev
ice)
#mixedbread-ai/mxbai-embed-large-v1 all-mpnet-base-v2

if __name__ == '__main__':

    pdf_path = input('Enter PDF 
name: ')

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f'The file '{pdf_path}' does not exist.')


    pages_n_texts = open_and_read_pdf(pdf_path)

    chunk_size = input('Enter chunk size(int). Default is 1500 (Enter
 -> skip): ')
    chunk_overlap = input('Enter chunk overlap(int). Default is 0 (Enter -> skip): ')
    if not chunk_siz
e:
        chunk_size = 1500
    if not chunk_overlap:
        chunk_overlap = 0

    text_splitter = create_text_splitt
er(chunk_size, chunk_overlap)
    print('Creating sentence chunks ~')
    pages_n_chunks_new = []
    for item in pages_
n_texts:
        item['sentence_chunks'] = text_splitter.split_text(item['text'])
        for chunk in item['sentence_ch
unks']:
            chunk_dict = {}
            chunk_dict['page_n'] = item['page_n']
            joined_sentence_chunk 
= ''.join(chunk).replace('  ', ' ').strip()
            joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sen
tence_chunk)
            joined_sentence_chunk = re.sub(r'\d+(\.\d+)+', '', joined_sentence_chunk)
            chunk_dic
t['sentence_chunk'] = joined_sentence_chunk

            # # add metadata
            chunk_dict['chunk_chars'] = len(jo
ined_sentence_chunk)
            chunk_dict['chunk_words'] = len([word for word in joined_sentence_chunk.split(' ')])
  
          chunk_dict['chunk_tokens'] = len(joined_sentence_chunk) / 4

            pages_n_chunks_new.append(chunk_dict)


    text_chunks = [item['sentence_chunk'] for item in pages_n_chunks_new]
    text_chunk_embs = emb_model.encode(text_
chunks, batch_size=16, convert_to_tensor=True)

    emb_chunks_df = pd.DataFrame(pages_n_chunks_new)
    # embs_only_df 
= pd.DataFrame(text_chunk_embs.to('cpu'))
    emb_chunks_df['embedding'] = text_chunk_embs.cpu().numpy().tolist()
    em
b_df_save_path = input('Enter name for embeddings csv. Default is emb_chunks_df (Enter -> skip): ')
    if not emb_df_sa
ve_path:
        emb_df_save_path = 'emb_chunks_df.csv'

    emb_chunks_df.to_csv(emb_df_save_path, index=False)
    pri
nt(f'File {emb_df_save_path} created!')
```

**rag.py**

```python
from transformers import AutoTokenizer, AutoModelForC
ausalLM, TextStreamer
from sentence_transformers import util, SentenceTransformer
import pandas as pd
import numpy as np

import torch

device = 'mps'

emb_chunks_df = pd.read_csv('emb_chunks_df.csv')

# convert embeddings back to np.array
e
mb_chunks_df['embedding'] = emb_chunks_df['embedding'].apply(lambda x: np.fromstring(x.strip('[]'), sep=', '))
embs = to
rch.tensor(np.stack(emb_chunks_df['embedding'].tolist(), axis=0), dtype=torch.float32).to(device)

pages_n_chunks = emb_
chunks_df.to_dict(orient='records')

emb_model = SentenceTransformer('mixedbread-ai/mxbai-embed-large-v1', device=device
)

def retrieve_relevant_info(query: str, embeddings: torch.tensor, model: SentenceTransformer=emb_model, n_to_retrieve:
 int=5) -> torch.tensor:
    query_emb = model.encode(query, convert_to_tensor=True)
    dot_scores = util.cos_sim(query
_emb, embeddings)[0]
    scores, indices = torch.topk(dot_scores, n_to_retrieve)
    print(scores)
    return scores, in
dices

model_id = 'google/gemma-2b-it'

tokenizer = AutoTokenizer.from_pretrained(model_id)
llm_model = AutoModelForCaus
alLM.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=False, attn_implementation='sdpa').to(device
)

def prompt_formatter(query: str, context_items: list[dict]) -> str:
    context = '- ' + '\n- '.join([item['sentence_
chunk'] for item in context_items])
    base_prompt = '''Based on the following context items, please answer the query.

Give yourself room to think by extracting relevant passages from the context before answering the query.
Don't return th
e thinking, only return the answer.
Make sure your answers are as explanatory as possible.
Use the following examples as
 reference for the ideal answer style, but don't use the below example answers as answers to the query.
\nExample 1:
Que
ry: Who can provide instructions to the bank according to the terms and conditions?
Answer: According to the terms and c
onditions, only authorized individuals can give instructions to the bank.
\nExample 2:
Query: What are your rights regar
ding the termination of services as outlined in the terms and conditions?
Answer: The terms and conditions specify the r
ights granted to you in the event of termination, including any associated procedures or obligations.
\nExample 3:
Query
: How does the bank handle refunds for incorrectly executed payment instructions, as per the terms and conditions?
Answe
r: The terms and conditions detail the process for obtaining refunds in the case of payment instructions being incorrect
ly executed by the bank.
\nExample 4:
Query: What measures are outlined in the terms and conditions to ensure the securi
ty of your accounts and payment instruments?
Answer: The terms and conditions lay out your obligations regarding the sec
urity of your accounts, payments, and payment instruments, along with any corresponding measures implemented by the bank
.
\nNow use the following context items to answer the user query:
{context}
\nRelevant passages: <extract relevant passa
ges from the context here>
User query: {query}
Answer:'''

    base_prompt = base_prompt.format(context=context, query=q
uery)
    
    # make sure the inputs to the model are in the same way that they have been trained
    dialogue_template
 = [
        {
            'role': 'user',
            'content': base_prompt
        }
    ]
    prompt = tokenizer.app
ly_chat_template(conversation=dialogue_template, tokenize=False, add_generation_prompt=True)

    return prompt

def ask
(query: str, temperature: float=0.2, max_new_tokens: int=256, format_answer_text: bool=True, return_context: bool=False)
:
    # -------- RETRIEVAL --------
    scores, indices = retrieve_relevant_info(query, embs, n_to_retrieve=10)
    cont
ext_items = [pages_n_chunks[i] for i in indices]
    for i, item in enumerate(context_items):
        item['score'] = sc
ores[i].cpu()

    # -------- AUGMENTATION --------
    prompt = prompt_formatter(query, context_items)

    # -------- 
GENERATION --------
    input_ids = tokenizer(prompt, return_tensors='pt').to(device)
    streamer = TextStreamer(tokeni
zer, skip_prompt=True, skip_special_tokens=True)
    outputs = llm_model.generate(**input_ids, streamer=streamer, temper
ature=temperature, do_sample=True, max_new_tokens=max_new_tokens)
    output_text = tokenizer.decode(outputs[0])

    if
 format_answer_text:
        output_text = output_text.replace(prompt, '').replace('<bos>', '').replace('<eos>', '')

  
  # if not return_context:
        # return output_text
    
    # return output_text, context_items

if __name__ == '__
main__':

    print('Enter a query:\n')
    query = input()
    print('estimating ~ estimating ~')
    ask(query, temper
ature=0.7, return_context=False)
```
```
---

     
 
all -  [ I want to make LLM model respond to queries related to a set of retrieved conversation from Vector D ](https://www.reddit.com/r/MLQuestions/comments/1bkywiw/i_want_to_make_llm_model_respond_to_queries/) , 2024-03-25-0910
```
Hi, I have created an embedding from multiple conversation of two person and pushed it to Qdrant DB. The retreival works
 good, Now I want to integrate an LLM model which answers queries from the relevant conversation retrieved from the vect
or DB. I am not sure what to use here. Go with Langchains or LlamaIndex.
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-25-0910
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-25-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-25-0910
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

     
