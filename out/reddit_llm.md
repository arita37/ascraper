 
all -  [ Another Beginner Post: Local LLM + LangChain Question ](https://www.reddit.com/r/LocalLLaMA/comments/15qbvug/another_beginner_post_local_llm_langchain_question/) , 2023-08-14-0909
```
Hi! I'm very new to AI/ML, so feel free to let me know if I misuse terminology or need to clarify. I'm looking to host a
n LLM that I can train on private pdfs, later finetune with csv files, and at the end have its outputs appear on a websi
te I'm contributing to. I looked into how to properly do that, but a lot of sources tend to use openai or have it runnin
g completely locally, so it's not necessarily applicable. From what I've found so far, I'd like to use a Llama2 model, L
angChain for pdf ingestion, and I'm deciding whether or not I could use together.ai or runpod for later fine-tuning and 
cloud hosting.

My question is if anyone doing something similar had suggestions or success with a certain combination o
f resources. I thought of using LocalGPT since it already incorporates pdf ingestion, but I'm not sure if I can simply u
se a base model instead of the chat-optimized one since I heard it's better to finetune a default model.

Let me know wh
at you think, thank you!

&#x200B;

&#x200B;
```
---

     
 
all -  [ How should I chunk text from a textbook for the best embedding results? ](https://www.reddit.com/r/LangChain/comments/15q5jzv/how_should_i_chunk_text_from_a_textbook_for_the/) , 2023-08-14-0909
```
My guess is that I should follow the natural structure of the textbook and chunk my text by chapter, section, subsection
, etc while retaining the relevant metadata. The problem is that I have no idea how to do that lol.

Can someone tell me
 a better way to chunk a textbook or give me the basic guidelines so I can ask ChatGPT?
```
---

     
 
all -  [ How should I preprocess my text to optimize text embeddings? ](https://www.reddit.com/r/LangChain/comments/15q4v2v/how_should_i_preprocess_my_text_to_optimize_text/) , 2023-08-14-0909
```
Pretty much the title.

I've heard of preprocessing strategies such as lowercasing, stop word removal, stemming, lemmati
zation, punctuation removal, special characters removal, and regular expression removal. However, many of these strategi
es seem like they might remove semantically relevant information about the text. For example, wouldn't lowercasing, lemm
atization, punctuation removal, and stemming get rid of important grammatical information that the embedding model could
 use to more accurately vectorize text?

&#x200B;

My guess is that I should try to preprocess my text using the same me
thods used in the embedding model's training data. What do y'all think?
```
---

     
 
all -  [ Last Week in AI #1 ](https://www.reddit.com/r/ChatGPT/comments/15pztik/last_week_in_ai_1/) , 2023-08-14-0909
```
A brief list of things that happened in AI last week  

&#x200B;

* This research paper has found that LLMs can naturall
y read docs to learn how to use tools without any training. Instead of showing demonstration, just provide tool document
ation. LLMs figured out how to use programs like image generators and video tracking software, without any new training 
\[[Link](https://huggingface.co/papers/2308.00675)\]
* This paper analyses and visualises the political bias of major AI
 language models. ChatGPT and GPT-4 were most left-wing while Meta’s Llama was right-wing \[[Link](https://aclanthology.
org/2023.acl-long.656.pdf)\]. This type of research is very important and highlights the inherent bias in these models. 
It’s practically impossible to remove bias also, and we don’t even know what they’ve been trained on. People need to und
erstand, you control the models, you control what people see, especially as AI models are used more frequently and becom
e mainstream
* Remember the Westworld style paper with the 25 AI agents living their lives? It’s now open-source. It’s i
mplications in gaming cannot be overstated. Can’t wait to see what comes of this \[[Link](https://github.com/joonspk-res
earch/generative_agents)\]
* MetaGPT is framework using multiple agents to behave as an entire company - engineer, pm, a
rchitect etc. It has over 18k stars on github. This specialised for industries and companies will be powerful \[[Link](h
ttps://github.com/geekan/MetaGPT)\]
* This paper discusses reconstructing images from signals in the brain. Soon we’ll h
ave brain interfaces that could read these signals consistently, maybe map everything you see? Potential is limitless \[
[Link](https://huggingface.co/papers/2308.02510)\]
* Nvidia is partnering with HuggingFace with DGX Cloud platform allow
ing people to train and tune AI models. They’re offering a “Training Cluster as a Service” which will help companies and
 individuals build and train models faster than ever \[[Link](https://nvidianews.nvidia.com/news/nvidia-and-hugging-face
-to-connect-millions-of-developers-to-generative-ai-supercomputing)\]
* Stability AI has released their new AI LLM calle
d StableCode. 16k context length and 3b params with other version on the way \[[Link](https://stability.ai/blog/stableco
de-llm-generative-ai-coding)\]
* This paper discusses a framework for designing and implementing complex interactions be
tween AI systems called Flows \[[Link](https://arxiv.org/pdf/2308.01285.pdf)\] Will be very important when building comp
lex AI software in industry. Github will be uploaded soon \[[Link](https://github.com/epfl-dlab/aiflows/)\]
* Nvidia ann
ounced that Adobe Firefly models will be available as APIs in Omniverse \[[Link](https://itbrief.com.au/story/nvidia-ann
ounces-updates-to-its-omniverse-and-new-gpus)\] This thread breaks down what the Omniverse will look like \[[Link](https
://twitter.com/bilawalsidhu/status/1688968093169553423)\]
* Anthropic CEO Dario Amodei thinks AI will reach educated lev
els of humans in 2-3 years \[[Link](https://www.youtube.com/watch?v=Nlkk3glap_U)\] For reference, Claude 2 is probably t
he second most powerful model alongside GPT4
* Layerbrain is building AI agents that can be used across Stripe, Hubspot 
and slack using plain english \[[Link](https://twitter.com/aaronkazah/status/1685364551586402309)\] Looks very cool
* LL
Ms picking random numbers almost always pick the numbers 6-8 \[[Link](https://twitter.com/alonsosilva/status/16799483898
13821443)\]
* Inflection founder Mustafa Suleyman says we’ll probably rely on LLMs more than the best trained and most e
xperienced humans within 5 years \[[Link](https://twitter.com/mustafasuleyman/status/1688169040684908544?s=20)\]. For co
ntext, Mustafa is one of the co founders of Google DeepMind - this guys knows AI
* Writer, a startup using Nvidia’s NeMo
 discuss how it helped them build and scale over 10 models. NeMo isn’t publicly available but seems like a massive advan
tage considering Writer’s cloud infra, which is managed by 2 people, hosts a trillion API calls a month \[[Link](https:/
/blogs.nvidia.com/blog/2023/08/08/writer-nemo-generative-ai/)\] Link to NeMo \[[Link](https://developer.nvidia.com/nemo)
\] Link to NeMo guardrails blog \[[Link](https://www.pinecone.io/learn/nemo-guardrails-intro/)\]
* Someone open-sourced 
smol-podcaster - it transcribes and labels speakers, formats the transcription, creates chapters with timestamps \[[Link
](https://github.com/FanaHOVA/smol-podcaster)\]
* Ultra realistic AI generated videos are coming. It’s impossible to tel
l they’re fake now \[[Link](https://twitter.com/joshua_xu_/status/1689019874667024384)\] Signup for early access here \[
[Link](https://am8evw00qys.typeform.com/to/wauwjUYP?typeform-source=t.co)\]
* Anthropic released Claude Instant 1.2. Its
 very fast, better at math and coding and hallucinates less \[[Link](https://twitter.com/AnthropicAI/status/168930369753
5414272)\]
* This guy released the code for his modded Google Nest Mini using OpenAI’s function calling to take notes an
d control his lights. Once Amazon & Apple integrates better LLMs into their prods, AI will truly be everywhere \[[Link](
https://github.com/justLV/onju-voice)\]
* If you search “As an AI language model” in Google Scholar a lot of papers come
 up… \[[Link](https://twitter.com/literalbanana/status/1689420167024095232?s=20)\]
* OpenAI released custom instructions
 for ChatGPT free users, except for people in the US or UK \[[Link](https://twitter.com/OpenAI/status/168932406372091084
8?s=20)\]
* OpenAI, Google, Microsoft and Anthropic partnered with Darpa for their AI cyber challenge \[[Link](https://t
witter.com/DARPA/status/1689321121521311758?s=20)\]
* PlayHT released their new text-to-voice ai model and it looks craz
y good. Change the way its delivered by describing an emotion and much more \[[Link](https://play.ht/conversational/)\] 
\[[Link](https://twitter.com/play_ht/status/1689436627557564416)\]
* A paper by Google showcasing that AI models tend to
 repeat a user’s opinion back to them, even if its wrong. Thread breaking it down \[[Link](https://twitter.com/JerryWeiA
I/status/1689340237993185280)\] Link to paper \[[Link](https://arxiv.org/abs/2308.03958)\]
* Medisearch comes out of YC 
and claims to have the best model for medical questions \[[Link](https://www.ycombinator.com/launches/JEm-medisearch-ai-
search-engine-for-trustworthy-medical-information)\]
* Someone made a way to one-click install AudioLDM with gradio web 
ui \[[Link](https://twitter.com/cocktailpeanut/status/1689004149751353344)\]
* A way to make llama-2 much faster \[[Link
](https://twitter.com/HamelHusain/status/1689790665604108288?s=20)\]
* WizardLM released a new math model that outperfor
ms ChatGPT on math skills \[Link\]
* A team of researchers trained an AI model to hear the sounds of keystrokes and stea
l data. Apparently it has a 95% success rate. Link to article \[[Link](https://www.itnews.com.au/news/keyboard-sounds-ca
n-reveal-secrets-researchers-598899)\] Link to paper \[[Link](https://arxiv.org/abs/2308.01074)\]
* Yann LeCun gave a ta
lk at MIT about Objective-Driven AI \[[Link](https://www.youtube.com/watch?v=vyqXLJsmsrk&list=PLKemzYMx2_Ot1MZ_er2vFiINd
JEgDO8Hg)\]
* Google released 7 free courses on gen AI \[[Link](https://www.cloudskillsboost.google/course_templates/536
)\] \[[Link](https://www.cloudskillsboost.google/course_templates/539)\] \[[Link](https://www.cloudskillsboost.google/co
urse_templates/554)\] \[[Link](https://www.cloudskillsboost.google/course_templates/541)\] \[[Link](https://www.cloudski
llsboost.google/course_templates/543)\] \[[Link](https://www.cloudskillsboost.google/course_templates/537)\] \[[Link](ht
tps://www.cloudskillsboost.google/course_templates/538)\]
* Alpaca, a new AI tool for artists is out for public beta. It
’s sketch to image is very powerful \[[Link](https://www.alpacaml.com/)\]
* One of the most lucrative businesses in the 
AI arms race? GPU cloud. Coreweave got $400M in funding and are set to make billions \[[Link](https://venturebeat.com/ai
/coreweave-came-out-of-nowhere-now-its-poised-to-make-billions-off-of-ai-with-its-gpu-cloud/)\]
* Google releases a guid
ebook on best practises when designing with AI \[[Link](https://pair.withgoogle.com/guidebook)\]
* A great article on LL
Ms in healthcare \[[Link](https://twitter.com/katieelink/status/1688714535656685568)\]
* Implement text-to-SQL using lan
gchain, a breakdown\[[Link](https://twitter.com/RLanceMartin/status/1688945071251701760)\]
* SDXL implemented in 520 lin
es of code in a single file \[[Link](https://github.com/cloneofsimo/minSDXL)\]
* OpenAI released a blog on Special Proje
cts - one of them involved trying to find secret breakthroughs in the world \[[Link](https://openai.com/blog/special-pro
jects)\]
* Google announced Project IDX, a browser-based code environment. Brings app dev to the cloud and has AI featur
es like code gen, completion etc \[[Link](https://idx.dev/)\] A shot at replit it seems
* Meta open-sourced AudioCraft -
 musicgen, audiogen and ecodec. Definitely worth checking out \[[Link](https://github.com/facebookresearch/audiocraft/)\
]
* If you’re interested in fine-tuning open-source models like Llama-2, definitely check out this blog \[[Link](https:/
/www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications)\] In 
some cases, fine-tuned llama2 is better than gpt4 (for sql generation for example). Overall a great read if you’re inter
ested in fine tuning
* Nvidia released the code for Neuralangelo, an AI model that reconstructs 3d surfaces from 2d vide
os \[[Link](https://github.com/nvlabs/neuralangelo)\]
* Create digital environments in seconds with Blockade labs. Wild 
stuff \[[Link](https://twitter.com/BlockadeLabs/status/1690125296308224001)\]
* This paper compares the answers of ChatG
PT and stackoverflow for software engineering questions \[[Link](https://arxiv.org/abs/2308.02312)\] “52% of chatgpt ans
wers are incorrect and 77% are verbose but are still preferred 39% of the time due to their comprehensiveness and well-a
rticulated language style”. Only issue is this uses 3.5. Need this test with gpt4

For one coffee a month, I'll send you
 2 newsletters a week with all of the most important & interesting stories like these written in a digestible way. You c
an [sub here](https://nofil.beehiiv.com/upgrade)

You can read the free newsletter [here](https://nofil.beehiiv.com/)

S
ince I started creating these posts, I've been consulting and helping some fairly large businesses understand how they c
an use AI and implement it in their processes. If you're interested in having a chat, fill the form on my [website](http
s://time-and-money.webflow.io/) or email me [nofil@timeandmoney.ai](mailto:nofil@timeandmoney.ai)
```
---

     
 
all -  [ Building first chatbot for client(s) ](https://www.reddit.com/r/vectordatabase/comments/15pyunf/building_first_chatbot_for_clients/) , 2023-08-14-0909
```
I have some clients who want a chatbot trained on their own knowledge base. I’m considering using Pinecone as my vector 
DB, Langchain, and GPT. 

Question 1: if I have multiple clients with their own unique knowledge bases, what’s the best 
way to initially organize their data? By org function, topic, or data type? 

Question 2: Suggestions on good web crawle
rs to index content from their website? 

Question 3: Tips on training the data?

Thanks! 
```
---

     
 
all -  [ How To Supercharge Your LLM with LangChain Agents ](https://dev.to/rogiia/how-to-supercharge-your-llm-with-langchain-agents-3fl6) , 2023-08-14-0909
```

```
---

     
 
all -  [ what is the future of ChatGPT? ](https://www.reddit.com/r/OpenAI/comments/15pmf6v/what_is_the_future_of_chatgpt/) , 2023-08-14-0909
```
When chatgpt appeared, everyone had countless dreams and made countless attempts, but as chatgpt restrictions became str
icter and companies did not give up ownership of their data, the use of chatgpt became increasingly limited. Countless e
nthusiasts and enterprises can only invest in open-source LLM, and the weak functionality and performance of open-source
 LLM make it difficult to carry these dreams.

So is the use of GPT limited now, or is it becoming less and less?

It ma
y still be popular in these ranges:

1. Programming Assistant - Replace Stackoverflow

2. Document Assistant - Replace t
ranslate or other document formatting tools.

3. proxy - decomposes user requests and then calls other tools, the super 
version of Langchain

4. Bridge - Presents information in a way that the user can understand, or transforms the user's i
ntention to read the information.

This is still a long way from Super AI, and there are many problems that need to be s
olved on the journey to Super AI, such as better adaptation illusion and better adaptation window size, as well as bette
r application in life to change the world. Can these be achieved with the current GPT mode?
```
---

     
 
all -  [ Struggling on chat with docs opensource ](https://www.reddit.com/r/learnmachinelearning/comments/15phmgz/struggling_on_chat_with_docs_opensource/) , 2023-08-14-0909
```
I am trying to chat with docs with a langchain next js app but it seems to halucinate and create fake links. I have used
 pinecone to ingest my pdf there.
Do you know any good chat with docs project that you have tested ?
Thanks
```
---

     
 
all -  [ Router Chains ](https://www.reddit.com/r/LangChain/comments/15p0rsk/router_chains/) , 2023-08-14-0909
```
In case of router chains, be it LLMRouterChain or EmbeddingRouterChain, what are the deciding parameters of the llm rout
ing to the default chain instead of choosing any of the destination? 
Also does embeddingrouter chain simply check the c
osine similarity of the query with the description of the prompts provided? If not, then what principle does it use to r
oute??
```
---

     
 
all -  [ How do I build a chatbot? ](https://www.reddit.com/r/LangChain/comments/15ozvj7/how_do_i_build_a_chatbot/) , 2023-08-14-0909
```
So basically what I need to do is build a chatbot that is able to identify user intents and 

1) if the user is seeking 
information then perform semantic search to generate a response 

2) if the user is seeking to perform some action (say,
 schedule an appointment) then collate all the information and push it to a database for appointments

How do I build th
e chatbot such that it can identify different intents and either do 1) or 2)? What tools/technologies can I use?
```
---

     
 
all -  [ ReferenceError: ReadableStream is not defined at Object.<anonymous> ](https://www.reddit.com/r/LangChain/comments/15oxt5t/referenceerror_readablestream_is_not_defined_at/) , 2023-08-14-0909
```
Has anyone encountered this error when trying to use LangchainJs in a nestJs project?

App\node_modules\langchain\dist\u
til\stream.cjs:45:38)
    at Module._compile (node:internal/modules/cjs/loader:1101:14)
    at Object.Module._extensions
..js (node:internal/modules/cjs/loader:1153:10)
    at Module.load (node:internal/modules/cjs/loader:981:32)
    at Func
tion.Module._load (node:internal/modules/cjs/loader:822:12)
    at Module.require (node:internal/modules/cjs/loader:1005
:19)
    at require (node:internal/modules/cjs/helpers:102:18)
    at Object.<anonymous
```
---

     
 
all -  [ Best LangChain features to support in a software development AI-assisted tool ](https://www.reddit.com/r/LangChain/comments/15oj0ax/best_langchain_features_to_support_in_a_software/) , 2023-08-14-0909
```
Hello fellow programmers. Me and my friends recently used LangChain and some fancy prompt engineering techniques to auto
generate a code base for a rather complex software project using GPT.

We made our tool free and open source under the M
IT license, and we intend to keep at it and improve it and add more features to it.

Here is the tool: [https://github.c
om/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer)

I wonder what do yo
u think should be supported by a tool like this? Especially regarding the features that LangChain enable.

Please either
 comment here, or file an issue on our github. I truly appreciate your time and your feedback. I also appreciate it if y
ou would kindly leave us a star on github.
```
---

     
 
all -  [ Using langchainjs for real-world applications. ](https://www.reddit.com/r/LangChain/comments/15ogvjs/using_langchainjs_for_realworld_applications/) , 2023-08-14-0909
```
[https://github.com/amalshehu/langchain-js-realworld](https://github.com/amalshehu/langchain-js-realworld)
```
---

     
 
all -  [ [D] How we evaluated LLMs in prod ](https://www.reddit.com/r/MachineLearning/comments/15ogknd/d_how_we_evaluated_llms_in_prod/) , 2023-08-14-0909
```
This is going to be a post about the challenges I faced while working with ChatGPT in my previous company and the things
 we did to overcome them over a 2+ month struggle. Check us out at [www.twilix.io](https://www.twilix.io/) if anything b
elow resonates with you and I hope you find some of it helpful.

So to begin, in my previous company we invested a few m
onths building a chatbot to help with user onboarding. At first everything was great, and we saw a 40% decrease in drop-
off rates (which is significant given we were building a consumer facing app), but somehow over time this drop-off rate 
started creeping up again. Perplexed by the unexpected turn in metrics, management started to question the benefits of m
aintaining this chatbot and was skeptical that we were cherry picking examples to showcase its performance for the sake 
of not wasting our efforts. They also knew that GPT4 got shadow nerfed which didn't help our case at all.

We had a lot 
of back and forth and eventually came to the conclusion that somehow the chatbot performance have to be quantified to ju
stify it's purpose. So, our team spent another 2 months engineering an evaluation solution to show leadership that the c
hatbot is performing as expected while identifying areas of improvement to craft a more refined product roadmap. We ende
d up trying a lot of different things, and after a long process of iteration and experimentation here are the things tha
t worked for us:

1. Generating synthetic datasets (these act as 'ground truths' pair of queries and expected responses)
 to benchmark performance.
2. Training models to determine the similarity score to assess every ChatGPT output in produc
tion (we use the generated synthetic dataset to do this to compare expected responses vs real responses)
3. Classifying 
the type of use cases the chatbot was used for (this allowed us to see which use cases were performing worse)
4. Logging
 configurations in our LLM stack and building visualizations on the web to identify what gives the best results (tempera
ture, LangChain configurations, lLamaIndex chunking sizes, these type of configurations)
5. Monitoring how our costs and
 latency are affected by tweaking different parameters
6. Lastly, A/B test to figure out the optimal parameters on diffe
rent sets of users (from experience, typically for a user onboarding chatbot use case around 5,000 users interacting wit
h your chatbot should be enough to collect some meaningful datapoints)

The most important learnings that we took away w
as that whilst synthetic data is OK you do need to generate large amounts of it. The sweet spot is different depending o
n the use case + the specifics of your knowledge base (eg, a corpus of internal documents vs a collection of websites), 
and I say sweet spot because after a certain amount of datapoints everything else kind of becomes noise and actually neg
atively affects your analysis more than the benefit it brings.

We ended up showing where our chatbot onboarding experie
nce fell short and was able to fix it through rapid iteration. There's still no set standard for LLM evaluation but I ho
pe my previous experiences helped. (Our team is now building out this evaluation system as a standalone product at [www.
twilix.io](https://www.twilix.io/) so check us out if you also want some concrete proof that ChatGPT is performing as ex
pected for your business)
```
---

     
 
all -  [ Langchain Expression Language: Easy declarative way to code and lot more! ](https://youtu.be/AM77pbogh5s) , 2023-08-14-0909
```

With the newly introduced Langchain Expression Language(LCEL), 

1. Engaging with core components becomes as easy using
 pipe operation.
2. The black box behind how to optimize  LLMs calls is taken away with batch, stream and a sync APIs.
3
. Conversation Retrieval Chain, VectorStore retrieval  & Memory based prompts are well structured with easily shared boi
ler plate using RunningPassThrough and ItemGetter.
4. Function calling, similar to OpenAI , is now here.
5. And lot more
 syntactical sugar is offered. 

Check out the video for an easy quick tutorial over each topic with a practical example
!
```
---

     
 
all -  [ Langchain + LLaMa 2 consuming too much VRAM ](https://www.reddit.com/r/LocalLLaMA/comments/15oaa18/langchain_llama_2_consuming_too_much_vram/) , 2023-08-14-0909
```
I was playing around with a GitHub project on a conda environment on Windows and I was surprised to see that LLama 2 13B
 4bit was using up to 25GB VRAM (16GB on one GPU and 9GB on the second one) for a simple summarization task on a documen
t with less than 4KB. I wanted to find out if there was an issue with Langchain or if it's just how it goes with LLMs be
cause seeing that a model occupies 8GB on disk and uses almost triple the amount of VRAM is suspicious. Am I doing somet
hing wrong?
```
---

     
 
all -  [ Is langchain worth it, over function calling? ](https://www.reddit.com/r/ChatGPTCoding/comments/15o9rug/is_langchain_worth_it_over_function_calling/) , 2023-08-14-0909
```
I find langchain a bit frustrating to work with.  I think it's partly a documentation issue, but I think the design is a
 bit confusing as well.  Since OpenAI came out with function calling I'm not sure I need chains.

I still may use langch
ain as a utility library for all its integrations, but without using the chains functionality due to the added complexit
y.

What do you think?
```
---

     
 
all -  [ Stuck at $500 MRR & Seeking Distribution/Marketing Advice ](https://www.reddit.com/r/SaaS/comments/15o9alc/stuck_at_500_mrr_seeking_distributionmarketing/) , 2023-08-14-0909
```
Hey everyone! 👋  
  
I'm Milan, founder of Robofy, an AI chatbot tool I've poured countless hours into. Robofy is live
 for around 3 months now. Our Monthly Recurring Revenue (MRR) has been stagnant at around $500 for the last 3 months, wh
ich has been a tad frustrating. I rebranded in June to Robofy but still am stuck at $500 and I am looking for fresh idea
s.  
  
One thing I've noticed is an extremely large number of similar products popping up in the market. It's both ex
citing and intimidating because it confirms a demand, but also adds that much more competition. I think most of the comp
etitors are coming up because of the cookbook published by OpenAI and the progress made by Langchain.  
  
Nevertheles
s, here's where I need your help:  
  
**Marketing**: I've the basic marketing avenues (Google Ads, Facebook Ads, etc.
) but the ROI hasn't been great. In fact, I would say that I recovered only 20% of my investment of $2500 in ads. Hence 
am in need of fresh, out-of-the-box strategies that can help stand out in this saturated space.  
  
**Distribution**:
 While our product is great, I believe our main challenge lies in getting it in front of the right eyes. Any ideas or ch
annels we might not have tapped into yet? I tried Twitter but again I faced the most common problem - not getting enough
 eyeballs.  


I tried creating a reseller plan so as to change target audience from direct customers to smaller IT com
panies. I got 2 orders for it now and that creates a bulk of my revenue. 

  
A few additional points:  
  
The prima
ry audience is small to medium businesses looking to streamline their customer support.  
We have a free tier, as well 
as paid packages with more features and benefits.  


I genuinely believe in Robofy, and I've had really positive feedb
ack from our few users. It's just the scaling and distribution part where we're having a hiccup.  
  
Cheers.  

```
---

     
 
all -  [ Use Llama2 to Improve the Accuracy of Tesseract OCR ](https://github.com/Dicklesworthstone/llama2_aided_tesseract) , 2023-08-14-0909
```
I've been disappointed by the very poor quality of results that I generally get when trying to run OCR on older scanned 
documents, especially ones that are typewritten or otherwise have unusual or irregular typography. I recently had the id
ea of using Llama2 to use common sense reasoning and subject level expertise to correct transcription errors in a 'smart
' way-- basically doing what a human proofreader who is familiar with the topic might do.

I came up with the linked scr
ipt that takes a PDF as input, runs Tesseract on it to get an initial text extraction, and then feeds this sentence-by-s
entence to Llama2, first to correct mistakes, and then again on the corrected text to format it as markdown where possib
le. This was surprisingly easier than I initially expected thanks to the very nice tooling now available in libraries su
ch as llama-cpp-python, langchain, and pytesseract. But the big issue I was encountering was that Llama2 wasn't just cor
recting the text it was given-- it was also hallucinating a LOT of totally new sentences that didn't appear in the origi
nal text at all (some of these new sentences used words which never appeared elsewhere in the original text).

I figured
 this would be pretty simple to filter out using fuzzy string matching-- basically check all the sentences in the LLM co
rrected text and filter out sentences that are very different from any sentences in the original OCRed text. To my surpr
ise, this approach worked very poorly. In fact, lots of other similar tweaks, including using bag-of-words and the spacy
 NLP library in various ways (spacy worked very poorly in everything I tried), also didn’t work.

Finally I realized tha
t I had a good solution staring me in the face: Llama2. I realized I could get sentence level vector embeddings straight
 from Llama2 using langchain. So I did that, getting embeddings for each sentence in the raw OCRed text and the LLM corr
ected text, and then computed the cosine similarity of each sentence in the LLM corrected text against all sentences in 
the raw OCRed text. If no sentences match in the raw OCRed text, then that sentence has a good chance of being hallucina
ted.

In order to save the user from having to experiment with various thresholds, I saved the computed embeddings to an
 SQLite database so they only had to be computed once, and then tried several thresholds, comparing the length of the fi
ltered LLM corrected text to the raw OCRed text; if things worked right, these texts should be roughly the same length. 
So as soon as the filtered length dips below the raw OCRed text length, it backtracks and uses the previous threshold as
 the final selected threshold.

Anyway, if you have some very old scanned documents laying around, you might try them ou
t and see how well it works for you. Do note that it's extremely slow, but you can leave it overnight and maybe the next
 day you'll have your finished text, which is better than nothing! I feel like this could be useful for sites like the I
nternet Archive-- I've found their OCR results to be extremely poor for older documents.

I'm open to any ideas or sugge
stions you might have. I threw this together in a couple days and know that it can certainly be improved in various ways
. One idea that I thought might be fun would be to make this work with a Ray cluster, sending a different page of the do
cument to each of the workers in the cluster to do it all at the same time.
```
---

     
 
all -  [ Does using langchain and openai worth training negative scenarios? ](https://www.reddit.com/r/Chatbots/comments/15o7d3e/does_using_langchain_and_openai_worth_training/) , 2023-08-14-0909
```
Is using langchain and OpenAI to create chatbot is preferrable to use?

Since designing contains a lot of portion of tra
ining prompt to not to give answers out of the topic.
```
---

     
 
all -  [ Could not load Llama model from path: ./Models/llama-7b.ggmlv3.q2_K.bin. Received error Llama.__init ](https://www.reddit.com/r/LocalLLaMA/comments/15o56kw/could_not_load_llama_model_from_path/) , 2023-08-14-0909
```
&#x200B;

>from langchain.llms import LlamaCpp  
>  
>from langchain import PromptTemplate, LLMChain  
>  
>from langcha
in.callbacks.manager import CallbackManager  
>  
>from langchain.callbacks.streaming\_stdout import StreamingStdOutCall
backHandler  
>  
>template = '''Question: {question}  
>  
>Answer: Let's work this out in a step by step way to be sur
e we have the right answer.'''  
>  
>prompt = PromptTemplate(template=template, input\_variables=\['question'\])  
>  

>callback\_manager = CallbackManager(\[StreamingStdOutCallbackHandler()\])  
>  
>llm = LlamaCpp(  
>  
>model\_path='./
Models/llama-7b.ggmlv3.q2\_K.bin',  
>  
>input={'temperature': 0.75,  
>  
>'max\_length': 2000,  
>  
>'top\_p': 1},  

>  
>callback\_manager=callback\_manager,  
>  
>verbose=True,  
>  
>)  
>  
>llm\_chain = LLMChain(prompt=prompt, llm
=llm)

&#x200B;

https://preview.redd.it/kwvc162rkghb1.png?width=797&format=png&auto=webp&s=d9a5c03721a553bd0b898cad708e
0afa446af0ed

>(llm) C:\\llm>python app1.py C:\\llm\\lib\\site-packages\\langchain\\utils\\utils.py:155: UserWarning: WA
RNING! input is not default parameter.                 input was transferred to model\_kwargs.                 Please co
nfirm that input is what you intended.   warnings.warn( Exception ignored in: <function Llama.\_\_del\_\_ at 0x000001923
B3AE680> Traceback (most recent call last):   File 'C:\\llm\\lib\\site-packages\\llama\_cpp\\llama.py', line 1507, in \_
\_del\_\_     if self.model is not None: AttributeError: 'Llama' object has no attribute 'model' Traceback (most recent 
call last):   File 'C:\\llm\\app1.py', line 14, in <module>     llm = LlamaCpp(   File 'C:\\llm\\lib\\site-packages\\lan
gchain\\load\\serializable.py', line 74, in \_\_init\_\_     super().\_\_init\_\_(\*\*kwargs)   File 'pydantic\\main.py'
, line 341, in pydantic.main.BaseModel.\_\_init\_\_ pydantic.error\_wrappers.ValidationError: 1 validation error for Lla
maCpp \_\_root\_\_   Could not load Llama model from path: ./Models/llama-7b.ggmlv3.q2\_K.bin. Received error Llama.\_\_
init\_\_() got an unexpected keyword argument 'input' (type=value\_error)

&#x200B;
```
---

     
 
all -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-08-14-0909
```
What are the possible practical approaches to creating an 'AI tutor' for a custom fantasy language, i.e. a language whic
h is definitely not covered in any large, mainstream LLM?

Assume in the fantasy language (like Game of Throne's Dothrak
i, but completely custom, so it's guaranteed not to be covered at all by an existing LLM), we have a dictionary of terms
, and a simple description of a grammar. What can I do with that?

Initially I was thinking of using 'Retrieval-Augmente
d Generation' (RAG), where I would pass it my dictionary of terms and their definitions and the grammar doc (i.e. the so
urce documents), and using OpenAI's LLM and LangChain's API wrapper and Pinecone long-term memory vector database, store
 the dictionary/grammar in Pinecone's vector database. Then a query comes in to translate an English word to a fantasy w
ord, and it looks in the Pinecone DB for similar English words, then passes the results with the fantasy word to the LLM
, along with the query, and generates a nice English response, with the fantasy word somewhere in there.

But that doesn
't seem like it would work the more I think about it. Then if I want to add the ability for it to translate English to t
he fantasy language, that seems impossible without first having a huge corpus of translation material (which is complete
ly impractical for a fantasy language). So can an existing generic LLM take a grammar as input, and learn to speak a fan
tasy language? If so, how would you make that happen?

Or what are other approaches to accomplishing this sort of thing?

```
---

     
 
all -  [ How to evaluate ChatGPT rigorously ](https://www.reddit.com/r/ChatGPT/comments/15o0ecd/how_to_evaluate_chatgpt_rigorously/) , 2023-08-14-0909
```
This is going to be a post about the challenges I faced while working with ChatGPT in my previous company and the things
 we did to overcome them over a 2+ month struggle. Check us out at [www.twilix.io](https://www.twilix.io) if anything be
low resonates with you and I hope you find some of it helpful.

So to begin, in my previous company we invested a few mo
nths building a chatbot to help with user onboarding. At first everything was great, and we saw a 40% decrease in drop-o
ff rates (which is significant given we were building a consumer facing app), but somehow over time this drop-off rate s
tarted creeping up again. Perplexed by the unexpected turn in metrics, management started to question the benefits of ma
intaining this chatbot and was skeptical that we were cherry picking examples to showcase its performance for the sake o
f not wasting our efforts. They also knew that GPT4 got shadow nerfed which didn't help our case at all. 

We had a lot 
of back and forth and eventually came to the conclusion that somehow the chatbot performance have to be quantified to ju
stify it's purpose. So, our team spent another 2 months engineering an evaluation solution to show leadership that the c
hatbot is performing as expected while identifying areas of improvement to craft a more refined product roadmap. We ende
d up trying a lot of different things, and after a long process of iteration and experimentation here are the things tha
t worked for us:

1. Generating synthetic datasets (these act as 'ground truths' pair of queries and expected responses)
 to benchmark performance. 
2. Training models to determine the similarity score to assess every ChatGPT output in produ
ction (we use the generated synthetic dataset to do this to compare expected responses vs real responses)
3. Classifying
 the type of use cases the chatbot was used for (this allowed us to see which use cases were performing worse)
4. Loggin
g configurations in our LLM stack and building visualizations on the web to identify what gives the best results (temper
ature, LangChain configurations, lLamaIndex chunking sizes, these type of configurations)
5. Monitoring how our costs an
d latency are affected by tweaking different parameters
6. Lastly, A/B test to figure out the optimal parameters on diff
erent sets of users (from experience, typically for a user onboarding chatbot use case around 5,000 users interacting wi
th your chatbot should be enough to collect some meaningful datapoints)

The most important learnings that we took away 
was that whilst synthetic data is OK you do need to generate large amounts of it. The sweet spot is different depending 
on the use case + the specifics of your knowledge base (eg, a corpus of internal documents vs a collection of websites),
 and I say sweet spot because after a certain amount of datapoints everything else kind of becomes noise and actually ne
gatively affects your analysis more than the benefit it brings. 

We ended up showing where our chatbot onboarding exper
ience fell short and was able to fix it through rapid iteration. There's still no set standard for LLM evaluation but I 
hope my previous experiences helped. Our team is now building out this evaluation system as a standalone product at [www
.twilix.io](https://www.twilix.io) so check us out if you also want some concrete proof that ChatGPT is performing as ex
pected for your business. Hope it helped : )

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ I've recently released a website that utilizes AI to create learning paths for any skill. ](https://www.reddit.com/r/SideProject/comments/15nwh5d/ive_recently_released_a_website_that_utilizes_ai/) , 2023-08-14-0909
```
I use Next.js, Langchain and deployed it on Vercel.

The operation is simple, input a prompt with the skill you want to 
learn, and receive an AI-generated learning path.

Features:

* Generate learning paths
* Track your progress
* Publish 
your learning paths

Link: [https://skillai.io](https://skillai.io)

&#x200B;

[Home](https://preview.redd.it/wv172ulrce
hb1.png?width=2440&format=png&auto=webp&s=cff2337ae29f6e346675f09aada3b55208c87a4e)

&#x200B;

[Learning path generated]
(https://preview.redd.it/f3szvxhwcehb1.png?width=2818&format=png&auto=webp&s=929e7f362870883691ac5a11adb230aab8c7277b)


&#x200B;
```
---

     
 
all -  [ Chatbot that only pulls specific data from a SQL database based on UserID? ](https://www.reddit.com/r/LangChain/comments/15nqfc3/chatbot_that_only_pulls_specific_data_from_a_sql/) , 2023-08-14-0909
```
I have a SQL database that external partners access but they can only see information attached to their unique user ID. 
Is it possible to create a chatbot using langchain that recognizes each persons unique user id and only pulls the releva
nt data from the SQL database without giving them access to the rest?
```
---

     
 
all -  [ Is there a way to summarize the current chain? ](https://www.reddit.com/r/LangChain/comments/15npkpp/is_there_a_way_to_summarize_the_current_chain/) , 2023-08-14-0909
```
I’m building a clone of chatGPT for personal development. 

I’m missing the feature to show a summary of the history lik
e in chatGPT side panel. 

Is there a way to get it from Langchain?
```
---

     
 
all -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-08-14-0909
```
&#x200B;

https://preview.redd.it/wl1gtcngnchb1.jpg?width=1500&format=pjpg&auto=webp&s=24e35d852603c6139fd67f79457ec593f
bad99f7

If you're someone who's curious about or working with LLMs there's a cool panel discussion coming up: 

* Compa
ring the pros and cons of using existing LLMs, prompt engineering, and fine-tuning on custom datasets for different ente
rprise use cases.
* Fine-Tuning LLMs: Exploring the advantages and challenges of fine-tuning LLMs on custom datasets to 
align with specific business objectives.
* Tools and platforms: Discussing the various tools and platforms to facilitate
 LLM implementation 
* Overcoming Challenges: Addressing the challenges associated with adopting LLMs, including data pr
ivacy, creating high quality datasets, computational resources, ethical considerations, and the need for specialized exp
ertise.
* Future Directions: Exploring emerging trends, advancements, and potential future applications of LLMs in the e
nterprise context.

Here's the event info: [https://www.eventbrite.com/e/large-language-models-for-enterprise-success-ch
allenges-and-approaches-tickets-695089811337?aff=oddtdtcreator](https://www.eventbrite.com/e/large-language-models-for-e
nterprise-success-challenges-and-approaches-tickets-695089811337?aff=oddtdtcreator)
```
---

     
 
all -  [ Best features to support in a software development AI-assisted tool ](https://www.reddit.com/r/ChatGPT/comments/15nln2f/best_features_to_support_in_a_software/) , 2023-08-14-0909
```
Hello fellow programmers. Me and my friends recently used LangChain and some fancy prompt engineering techniques to auto
generate a code base for a rather complex software project using GPT.

We made our tool free and open source under the M
IT license, and we intend to keep at it and improve it and add more features to it. 

Here is the tool: [https://github.
com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer) 

I wonder what do 
you think should be supported by a tool like this? 

Please either comment here, or file an issue on our github. I truly
 appreciate your time and your feedback. I also appreciate it if you would kindly leave us a star on github. 
```
---

     
 
all -  [ strugle to chat with docs ](https://www.reddit.com/r/LangChain/comments/15nl2ll/strugle_to_chat_with_docs/) , 2023-08-14-0909
```
 I recently cloned the [**gpt4-pdf-chatbot-langchain**](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) reposito
ry from GitHub which integrates with Pinecone. However, I've encountered an issue after ingesting a document of about 50
0 pages with embedded links. The chatbot seems to 'hallucinate' or misinterpret these links, which is quite unexpected. 
I'm seeking alternative solutions or suggestions to address this. Any guidance would be greatly appreciated. Thank you. 
 
 
```
---

     
 
all -  [ Open Source Vector Embedding Pipeline to Ingest Gigabytes of Data ](https://www.reddit.com/r/LangChain/comments/15nl2b7/open_source_vector_embedding_pipeline_to_ingest/) , 2023-08-14-0909
```
🚀 Excited to announce the release of the initial version of our open-source vector embedding pipeline, VectorFlow! 🎉

Ou
r pipeline is built to embed large volumes of data quickly and reliably. While embedding a handful of PDFs for Q&A might
 seem straightforward, the real challenge arises when you're faced with ingesting gigabytes of unstructured data consist
ently and frequently.

With just a simple API request, you can effortlessly embed and store raw data in any vector datab
ase, eliminating the need for complex cloud infrastructure setups.

🔗 Check out our Github repo: [https://github.com/dga
rnitz/vectorflow](https://github.com/dgarnitz/vectorflow) and check out our website: [https://www.getvectorflow.com/](ht
tps://www.getvectorflow.com/)

For all the innovators working with vector databases, we're eager to hear your insights, 
feedback, and ideas for the roadmap! 🌐🔍📊🚀
```
---

     
 
all -  [ Unleash the Power of LLMs in Your Telegram Bot on a Budget ](https://www.reddit.com/r/TelegramBots/comments/15njryp/unleash_the_power_of_llms_in_your_telegram_bot_on/) , 2023-08-14-0909
```
Interested in supercharging your Telegram bot with large language models (LLMs)? Here's a concise guide:

* **Introducti
on**: Harness LLMs like llama2-chat and vicuna. The bot is hosted on Amazon's free-tier EC2, with LLM inference on Beam 
Cloud.
* **Telegram Bot Setup**: Initiate with u/botfather on Telegram, get your token, and start a conversation with yo
ur bot.
* **Hosting**: Deploy on Amazon’s free-tier EC2 instance. The guide provides steps from EC2 setup to bot launch.

* **LLM Integration**: Beam Cloud, an affordable choice, is used for LLM inference. The bot taps into langchain and hug
gingface.

🔗 [**GitHub Repo**](https://github.com/ma2za/telegram-llm-guru) 🔗 [**Full Medium Article**](https://medium.co
m/@saverio3107/crafting-a-cost-effective-llm-powered-telegram-bot-a-step-by-step-guide-4d1e760e7eec) 🔗 [**Join Medium fo
r More Updates**](https://medium.com/@saverio3107/membership)

Dive in, experiment, and enhance your Telegram bot's capa
bilities! Feedback and insights are welcome. 🚀
```
---

     
 
all -  [ How langchain isable to achieve (almost) perfect SQL query ? ](https://devblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/) , 2023-08-14-0909
```
Me and my time is working on how to implement a natural language to SQL query generation based on a database using Seman
tic kernel(SK).
Our approach was to give the Kernel (chains equivalent in SK) the schema of the database.
We also have t
o explicitly mentioned the values of certain columns to increase the performance.
We observe that only davinci is able t
o generate most appropriate SQL query compare to gpt-35-turbo.
The same is started by the following [article](https://de
vblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/) as well.

Interestingly langchain use
s gpt-35-turbo to create SQL query.So my question is what langchain is doing differently???
```
---

     
 
all -  [ Using Document metadata in ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/15niet1/using_document_metadata_in/) , 2023-08-14-0909
```
Hey, I need some help with my ConversationalRetrievalChain app.

For context i'm using RecursiveTextSplitter and FAISS t
o store the text of the PDFs i upload.   
I manually add the metadata to the Documents such as each chunk will have 'sou
rce' and 'page\_number'  
I'm then using a ConversationalRetrievalChain.from\_llm alongside SystemMessagePromptTemplate 
and Human... that feed in a ChatPromptTemplate.

Now that you know the basic arch, here is the problem.  
When I upload 
multiple documents, I want to be able to look for an answer that says:  
' This doc says X, this doc says Y'  


Because
 I am using the RecursiveTextSplitter, the chunks I get are all Documents according to llm.   
So even if I upload 2 pdf
s only, i get an answer relative to:  
'Doc 1 says z, Doc 2 says x, Doc 3 says c, Doc 4 says d'  
Because it doesn't hav
e context of what document belongs to which pdf.   


What I want to do is let the llm tap into the Metadata of each chu
nk to support its explanation. Then instead of showing multiple documents, it will pinpoint which chunks belong to which
 document.   
Any help is appreciated
```
---

     
 
all -  [ Struggling with 404 Errors in LangChain: How Can I Ensure Valid Webpage Links? ](https://www.reddit.com/r/LangChain/comments/15nemtf/struggling_with_404_errors_in_langchain_how_can_i/) , 2023-08-14-0909
```
Hi everyone, I've been working with LangChain and SerpAPI to retrieve webpage links for a project. Unfortunately, I've e
ncountered an issue where some of the links are returning a '404 Page Not Found' error. I want to ensure that the links 
I'm retrieving are both accessible and available. Can anyone provide guidance or suggestions on how to verify the validi
ty of these links or filter out the ones that are not working? Thanks in advance for your help!
```
---

     
 
all -  [ Open source Facebook/ig/whatsapp messenger chatbot with langchain ](https://www.reddit.com/r/LangChain/comments/15ne3rt/open_source_facebookigwhatsapp_messenger_chatbot/) , 2023-08-14-0909
```
Basically what the tittle says, Im developing a private software right now but in my journey to learn using langchain an
d some other API tests I used Facebook messenger as my UI instead of making one (no domain,no fees,no database necessary
) to test some basic to advanced features of a chatbot, let it be a simple chat chain Q&A with DB queries or a full fled
ge agent like auto-gpt(non multi-agent). Here’s my deal. I’m creating the github open source because i haven’t seen(last
 time I checked) a complete repo for this, I belive is of value for begginer/intermediate level for developers of Llm ap
ps to start here with the merge of good ui/ux (we use it all the time no designing thinking is required) and can be furt
her improved(reduced response time,local LLMs, speech2text,text2image,file2text) I wanna know if some of you are looking
 for this or interested enough to make the complete guide and start a discord sever for further development in GitHub re
pository.

Extra:
As my own point of view, I hope many of us share the same excitement of working with bleeding edge tec
hnology of AI and so do big industries are(Facebook buying Llama , “X” with the account verification, KhanAcademy with C
hatGPT tutor…) but for now they only live in the software environment(I hope sooner or later boston dynamics just connec
ts to the  mic array and a speaker with gpt api to a spot) so the main road for the LLMs is to grow popularity in the vi
rtual space.As for now they work mainly for category of virtual assistant and that globally would be condensed into thes
e category always… until we can have friendly talks over the internet with out any propuse or objective making it the du
mbest/smartest virtual friend/Teacher, and creating engienieering parts for cars, developing new instruments or solution
s for the applied science, we are gradually looking at this but for now the more virtual agent populate the platforms th
e more we can socially experiment and as mentioned before the industires for sure may see this as competition, and if th
ere’s a way to eradicate this they would love to do it and make it their own or worse . They would never able to reach t
he same power as they could do in the earlier years mostly because of the lack of control…This is just a smart part of t
he model which makes me feel like I don’t have a bicycle for the mind but a Raptor F-22.
```
---

     
 
all -  [ Is there any way to show the verbose in our streamlit UI ](https://www.reddit.com/r/LangChain/comments/15ndsq5/is_there_any_way_to_show_the_verbose_in_our/) , 2023-08-14-0909
```
I am working on a project on agents that can show verbose in terminal but not in UI is there any way to show this ??
```
---

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-08-14-0909
```
would it be possible to train or fine-tune a small (1-3B) model who's sole purpose is to perform function calls? similar
 to how we have tiny models like replit-v2-3B that are super capable at specific things like code auto-complete .  


i 
know that's how openAI implemented function call was by fine-tuning gpt-3.5/4 but I'm thinking just a straight up base m
odel trained to understand and excel at function calls (similar to Gorilla for apis)

i'm thinking it would be a perfect
 'glue' for bigger LLM apps-- avoiding the need for external tools like langchain/quidance/etc...
```
---

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-14-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-14-0909
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to  Nvidia GPU and Metal acceleration for GGML models !

Here is the project  link: [Cria- Local
 LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Langc
hain\` example in the project).

This is an ongoing project, I have implemented the \`embeddings\` and \`completions\` r
outes. The \`chat-completion\` route will be here very soon!

Really interested in your feedback and I would welcome any
 help :) !

&#x200B;

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-14-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-14-0909
```
 I worked for less than a year as a Data Engineer. I decided to look for other challenges and got a job as an AI enginee
r developing language models.

The product of the company that hired me is related to data and metadata management. My t
asks will be to introduce features to the product, including a chat function that will allow for asking questions about 
data. Other tasks will include research and proposing additional AI-related functionalities to the product (on premise).
 I have a two weeks left to start work and I need to prepare a bit. My job will involve implementing ready-made solution
s and conducting research (high level - I need to implement valuable features and no one cares how).

**What are the mos
t important things I should learn before starting work?**

First of all, I replicated a few applications from this blog:
 [https://blog.streamlit.io/tag/llms/](https://blog.streamlit.io/tag/llms/)

Then I have focused on Langchain. I'm also 
in the middle of a course on Udemy about Next-Gen AI projects - Beginner friendly - Langchain, Pinecone - OpenAI, Huggin
gFace & LLAMA 2 models

I need a roadmap that will guide me a bit. I'm looking for blogs/materials/courses that will giv
e me practical knowledge in this matter.
```
---

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-14-0909
```
I have a data set that isn't that large \~200 pdfs. I have done the regular RAG approach with Langchain, extracting text
, splitting into chunks, embedding with OpenAi embeddings and FAISS vector storage. However, when I do a similarity sear
ch with a question I would like answered it returns the wrong context. The documents are semi-structured information of 
examined bridges. A question I would like answered is f.e. 'what is the construction date of bridge X?'. When I input th
is question I get a lot of context of construction dates of other bridges. I think this is because the bridges are not e
xplicitly mentioned in the text. I tried adding the bridge name and document name to the page content string of the chun
ks, but this does nothing.

Does anyone have any tips on improving the embeddings retrieval in this case?
```
---

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-14-0909
```
I am running text inferencing on Llama2-7b through langchain. I have downloaded the model from langchain's Huggingface l
ibrary, and I am running the model on AWS ml.g4dn.12xlarge which has 4x**nvidia t4**, which gives a total 64GB of GPU me
mory and 192GB of normal memory. It is able to answer my queries in around 10 seconds for small queries, and upto 3 mins
 for big queries.

The task I am doing is retrieving information from a document(Understanding Machine Learning PDF) in 
a conversational way. I've extracted the main parts of the notebook and put it up [here](https://colab.research.google.c
om/drive/1uFNkZ6FI0qffwRpW6ubfdq0HrCqcqVUi?usp=sharing).

Where can I make changes to speed up the transaction. Is there
 any change I can do in the model configuration to speed it up? Because if I use HuggingFaceHubAPI, it is able to give a
n answer in less than 5 seconds. Are there any other areas I can optimise?

I appreciate any help you can provide. Thank
s!
```
---

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 2023-08-14-0909
```
Hey [r/MachineLearning](https://www.reddit.com/r/MachineLearning/),

The team at TruEra recently released an open source
 project for evaluation & tracking of LLM applications called [TruLens-Eval](https://github.com/truera/trulens/tree/main
/trulens_eval). We’ve specifically targeted retrieval-augmented QA as a core use case and so far we’ve seen it used for 
comparing different models and parameters, prompts, vector-db configurations and query planning strategies. I’d love to 
get your feedback on it.

The core idea behind the project is feedback functions. Analogous to labeling functions, feedb
ack functions are models used to score the text produced by LLMs. We already have a variety of out-of-the-box feedback f
unctions to use for eval including relevance, language match, sentiment and moderation that can be applied to inputs, ou
tputs or intermediate steps of your application.

On top of eval, there’s also built-in tracking of cost and latency.

W
e made it easy to integrate with different setups using connectors for langchain, llama-index + an option to use it with
out a framework.

[Langchain Quickstart Colab](https://colab.research.google.com/github/truera/trulens/blob/releases/rc-
trulens-eval-0.5.0/trulens_eval/examples/colab/quickstarts/langchain_quickstart_colab.ipynb)

[Llama-Index Quickstart Co
lab](https://colab.research.google.com/github/truera/trulens/blob/releases/rc-trulens-eval-0.5.0/trulens_eval/examples/c
olab/quickstarts/llama_index_quickstart_colab.ipynb)

[No Framework Quickstart Colab](https://colab.research.google.com/
github/truera/trulens/blob/releases/rc-trulens-eval-0.5.0/trulens_eval/examples/colab/quickstarts/no_framework_quickstar
t_colab.ipynb)

Last, the project comes with a streamlit dashboard for visualization of your experiments and associated 
metrics.

[TruLens dashboard for comparing different app versions](https://preview.redd.it/q68b1l27pycb1.jpg?width=1233&
format=pjpg&auto=webp&s=cfb1704624a8b6642b249a32d0afee85ea9f62d9)

Please let us know what you use this for or if you ha
ve feedback! And thanks to all contributors to this project and the open source community!
```
---

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 2023-08-14-0909
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
MachineLearning -  [ '[N]' '[D]' Langchain? What is it?? ](https://www.reddit.com/r/MachineLearning/comments/150mzax/n_d_langchain_what_is_it/) , 2023-08-14-0909
```
want to know more about Langchain  
Check out [https://nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf](https:
//nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf)
```
---

     
 
MachineLearning -  [ [D] The Problem With LangChain ](https://www.reddit.com/r/MachineLearning/comments/14zlaz6/d_the_problem_with_langchain/) , 2023-08-14-0909
```
https://minimaxir.com/2023/07/langchain-problem/

tl;dr it's needlessly complex, and I provide code examples to demonstr
ate such.

A few weeks ago when I posted about creating a LangChain alternative to /r/MachineLearning, most of the comme
nts replied 'what exactly is the issue with LangChain', so I hope this provides more clarity!
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-14-0909
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
