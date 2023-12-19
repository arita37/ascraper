 
all -  [ Panel ChatInterface lets you create chat interfaces with just Python ](https://www.reddit.com/r/Python/comments/18lnrx5/panel_chatinterface_lets_you_create_chat/) , 2023-12-19-0910
```
No Javascript knowledge required.

Here's a minimal example that you can use to get started!

    import panel as pn
   
 
    def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
        message = f'Echoing {user}: {cont
ents}'
        return message
    
    chat_interface = pn.chat.ChatInterface(callback=callback)
    chat_interface.serv
able()

See [https://holoviz-topics.github.io/panel-chat-examples/](https://holoviz-topics.github.io/panel-chat-examples
/) for recipes, including interfacing with OpenAI, Mistral, Llama, Langchain, and LlamaIndex!

https://i.redd.it/u3gfst0
j757c1.gif
```
---

     
 
all -  [ Panel ChatInterface lets you create ](https://www.reddit.com/r/madeinpython/comments/18lnprm/panel_chatinterface_lets_you_create/) , 2023-12-19-0910
```
HoloViz Panel lets you create chat interfaces--with just Python! No Javascript knowledge required.

Here's a minimal exa
mple that you can use to get started!

    import panel as pn
    
    def callback(contents: str, user: str, instance: 
pn.chat.ChatInterface):
        message = f'Echoing {user}: {contents}'
        return message
    
    pn.chat.ChatInte
rface(callback=callback).servable()

See [https://holoviz-topics.github.io/panel-chat-examples/](https://holoviz-topics.
github.io/panel-chat-examples/) for recipes, including interfacing with OpenAI, Mistral, Llama, Langchain, and LlamaInde
x!

https://i.redd.it/lxud8e2o657c1.gif
```
---

     
 
all -  [ Search in large JSON ](https://www.reddit.com/r/LangChain/comments/18ln785/search_in_large_json/) , 2023-12-19-0910
```
I want to make an agent that uses a tool that searches for keywords in a huge JSON. I succeeded in getting it to fetch d
ata from an API, but the user should also be able to filter data chunks with keywords. For example, 'which ticket has th
e keywords user, sister, and admin' it must be able to filter in large data which is around 150k token. How would you co
me around this?
```
---

     
 
all -  [ At Present, What are the Best AI Companion Apps? ](https://www.reddit.com/r/ChatGPTCoding/comments/18lj3w3/at_present_what_are_the_best_ai_companion_apps/) , 2023-12-19-0910
```
Howdy,

I've recently started hacking away at a fun little ai companion app project in my spare time, and it got me thin
king--what are the best tools that are already out there?

Specifically, I'm interested in apps with strong long term me
mory systems. Are there any apps available that have successfully implemented knowledge graph memory? (Ik langchain prov
ides tools to do this but I can imagine itd be difficult to get this working well)

Additionally, if you're working on a
n open source AI companion app, feel free to share - I'd love to try them out
```
---

     
 
all -  [ Articles, courses and other resources for multimodal AI ](https://www.reddit.com/r/learnmachinelearning/comments/18lgo4y/articles_courses_and_other_resources_for/) , 2023-12-19-0910
```
One of the big trends I keep hearing is that while 2023 has been the year of text generation, 2024 will be all about mul
timodal generative AI. That is, you can generate decent audio, images and video now.

The tools are getting to the point
 where they are fairly accessible with a bit of Python knowledge, so I've made a list of resources.

**Articles**

* [Wh
at Is Multimodal AI?](https://app.twelvelabs.io/blog/what-is-multimodal-ai) by TwelveLabs. Quite a lot of historical per
spective. I love the bits that matches up models to use cases.
* [Introduction to Multimodal Deep Learning](https://enco
rd.com/blog/multimodal-learning-guide/) by encord. Decent overview with some links to relevant datasets.
* [Multimodal D
eep Learning: Definition, Examples, Applications](https://www.v7labs.com/blog/multimodal-deep-learning-guide) by Konstan
tinos Poulinakis. Nice overview of applications, but it gets a bit technical with some equations thrown in.
* [Frontiers
 of multimodal learning: A responsible AI approach](https://www.microsoft.com/en-us/research/blog/frontiers-of-multimoda
l-learning-a-responsible-ai-approach/) by Microsoft Research. Thinkpiece on how to do multi-modal AI responsibly for a c
orporate audience.

**Courses**

* [Building Multimodal AI Applications with LangChain & the OpenAI API](https://www.dat
acamp.com/code-along/multimodal-ai-applications-langchain-openai-api) by Korey Stegared-Pace (free, registration require
d, 1 hour of content). Part of a 9 code-along series by DataCamp. Covers a fun use case of transcribing YouTube videos u
sing LangChain, the OpenAI Whisper API. Disclosure: I work at DataCamp and I instructed another code-along in the series
.
* [Generative AI for Beginners](https://microsoft.github.io/generative-ai-for-beginners/#/) by Microsoft (free, regist
ration needed, timing unclear - maybe 12 hours?). Azure-based course with a mix of theory and practical sessions.

There
's a Udemy course too, but it costs money so I can't share that.

**Videos**

* [“LLAMA2 supercharged with vision & hear
ing?!” | Multimodal 101 tutorial](https://youtu.be/RxBSmbdJ1I8?feature=shared) by AI Jason. Focused on applications of L
lama 2 with sound and video input. Nice section on robots.
* [Introduction to large language models](https://youtu.be/zi
zonToFXDs?feature=shared) by Google Tech Cloud. It naturally focuses on Palm and the Google Gen AI Studio but there's so
me good discussion of workflows.
* [Building Multi-Modal Search with Vector Databases](https://www.youtube.com/live/3WUo
bZryyok?feature=shared) by DeepLearningAI. Zain and Sebastian from vector database company Weaviate show you how to sema
ntic search on images. Very cool though last time I spoke to the devrel team at Weaviate they said they were overhauling
 their Python package - for anyone who found this list in the future, please double-check that the code is still relevan
t.

What else should I add to the list?

&#x200B;
```
---

     
 
all -  [ issues doing an sql bot ](https://www.reddit.com/r/LangChain/comments/18lfmtf/issues_doing_an_sql_bot/) , 2023-12-19-0910
```
hello, basically I’m unable to run my sql analysis bot virtually, since it needs local host connection to the sql source
. any idea of how I could fix this? 
my local bot runs perfectly fine, but when uploading it to streamlit share it compl
etely fails. 

I could send the GitHub if anyone can help, thank you a lot in advance 🙏
```
---

     
 
all -  [ Best model for tabular analysis ](https://www.reddit.com/r/LocalLLaMA/comments/18lffx3/best_model_for_tabular_analysis/) , 2023-12-19-0910
```
Hey guys,  


I have built a simple prototype of a chatbot to talk to a tabular data  - essentially langchain->gpt4->pan
das query. It works better than I was expecting with some prompting.  If i wanted to switch out gpt4 for an 'open' llm w
hich one is best suited to this task? What benchmarks should I be looking at?   


&#x200B;
```
---

     
 
all -  [ Cookbook examples are riddled with errors ](https://www.reddit.com/r/LangChain/comments/18lems2/cookbook_examples_are_riddled_with_errors/) , 2023-12-19-0910
```
Seems like I can't get through an entire cookbook topic without encountering an error. The errors seem to occur with par
sers and runnables. 

What's going on? I recently installed langchain. Are the docs outdated at this point?
```
---

     
 
all -  [ Intersection of AI Efficiency and Data Privacy ](https://www.reddit.com/r/LangChain/comments/18lc9qo/intersection_of_ai_efficiency_and_data_privacy/) , 2023-12-19-0910
```
A call for Insight and Experiences, I've been grappling with a topic that seems increasingly relevant in the massive pla
tform shift that is AI. The delicate balance between AI's accuracy and the protection of data privacy. We are currently 
working with a couple of vector databases to embed and increase the context of our private LLM apps for our clients. I'm
 curious to hear your thoughts and experiences on how you are managing Data Security!

What measures are effective in pr
eventing such occurrences? Are there specific tools or practices you've found particularly useful or concerning in this 
regard?

I'm not just looking for textbook answers, but real-life scenarios and insights. How do you or your organizatio
n navigate these waters? What challenges have you faced, and how have you overcome them? let's have a discussion about t
he practicalities, ethical considerations, and future implications of AI and data privacy.
```
---

     
 
all -  [ Chat conversation memory management ](https://www.reddit.com/r/LlamaIndex/comments/18lbykf/chat_conversation_memory_management/) , 2023-12-19-0910
```
I've been playing with a chatbot, using LangChain VectorStoreRetriever memory (https://python.langchain.com/docs/modules
/memory/types/vectorstore_retriever_memory). I'm using Chroma and Instructor-Large embeddings. I'm adding timestamps and
 trying to make the bot aware of the relationship of messages in term of content and time. It kind of works, but it's no
t ideal. Also, with their boilerplate code I don't see a way to restrict the amount of tokens inserted into the conversa
tion (for larger k values). Is there a better way to manage this with Llama-Index?
```
---

     
 
all -  [ LlamaCpp on MAC: n_gpu_layers, n_batch ](https://www.reddit.com/r/LangChain/comments/18lb4n4/llamacpp_on_mac_n_gpu_layers_n_batch/) , 2023-12-19-0910
```
Hi,

I am using LlamaCpp (from langchain.llms import LLamaCPP) and at the moment I am using this suggestion from Langcha
in for MAC: 'n\_gpu\_layers=1', 'n\_batch=512'.

I have a MacBook Metal 3 and 30 Cores, so does it make sense to increas
e 'n\_gpu\_layers' to 30 to get faster responses? For example, I am using the Q5 Quantized Version of Mixtral 8x7B (30gb
) locally on my Mac and the respones take a while.

&#x200B;

Thanks for suggestions
```
---

     
 
all -  [ [Rust] Y a-t-il une caisse de Langchain? ](https://www.reddit.com/r/redditenfrancais/comments/18l93hd/rust_y_atil_une_caisse_de_langchain/) , 2023-12-19-0910
```
Je fais des recherches et rejoignais le train de battage médiatique d'IA. Et j'aimerais explorer la programmation tout e
n continuant à apprendre la rouille. Je me demandais s'il y avait une bibliothèque open source similaire à Langchain que
 je peux contribuer? Sinon, je pourrais essayer de commencer quelque chose.

Traduit et reposté à partir de la publicati
on 13l89ur de la communauté rust. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.
com/'
```
---

     
 
all -  [ LangServe <> Slack/Discord Integration (no code) ](https://www.reddit.com/r/LangChain/comments/18l87tj/langserve_slackdiscord_integration_no_code/) , 2023-12-19-0910
```
LangServe is remarkable, but integrating it into my Slack workspace still requires substantial coding. To streamline thi
s process, my team developed [PlugBear](https://plugbear.io/).

[PlugBear](https://plugbear.io/) is a no/low-code tool t
hat seamlessly connects LangServe with Slack or Discord. If you've created an LLM app using LangServe, PlugBear lets you
 integrate it into your Slack workspace without any coding.

For a step-by-step guide on this integration, visit '[Integ
rate LangServe Apps with Slack](https://plugbear.io/posts/integrate-langchain-langserve-app-with-slack-using-plugbear)'.


Enjoy LangServe+Slack(or Discord) using PlugBear! 🎉

[LangServe + PlugBear](https://preview.redd.it/77bajwavx17c1.png?
width=1600&format=png&auto=webp&s=135458c3d5949003f267c65d527c8d4e57aa44fd)
```
---

     
 
all -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2023-12-19-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
all -  [ Created a Chatbot Using LangChain, Pinecone, and OpenAI API ](https://www.reddit.com/gallery/18l6vy2) , 2023-12-19-0910
```

```
---

     
 
all -  [ [Langchain] Chroma ou Faiss? ](https://www.reddit.com/r/redditenfrancais/comments/18l6szp/langchain_chroma_ou_faiss/) , 2023-12-19-0910
```
Avez-vous une expérience d'utilisation de ces 2 VectorStores pour un chat de Q&A de documents?



Lequel est le meilleur
 pour les cas d'utilisation de l'entreprise?

Pour moi, la vitesse est également importante et la possibilité de prendre
 en charge le mode CPU uniquement.

Traduit et reposté à partir de la publication 15a447w de la communauté langchain. Po
ur retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Langchain] Exemple pour le reconstitution en chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/18l6rt1/langchain_exemple_pour_le_reconstitution_en/) , 2023-12-19-0910
```
Je cherche à en savoir plus sur la façon de mettre en œuvre le rediffusion dans une implémentation de chiffon. Des tutor
iels / articles recommandés par la communauté?

Traduit et reposté à partir de la publication 16ms4m4 de la communauté l
angchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Local Llama] Alternative à Langchain pour les LLM ouvertes? ](https://www.reddit.com/r/redditenfrancais/comments/18l5zss/local_llama_alternative_à_langchain_pour_les_llm/) , 2023-12-19-0910
```
Langchain semble très ouvert. Les gens ont-ils essayé d'utiliser d'autres cadres pour les LLM locaux? Est-ce que oui, qu
e recommandez-vous?

En particulier, j'ai du mal à faire travailler Langchain avec des vicuna quantifiés (4 bits GPTQ). 
Je suis spécifiquement intéressé par les LLM à faible mémoire. Je vois les mêmes questions sur l'intégration de Langchai
n il y a quelques mois, mais je ne vois pas beaucoup de progrès, c'est pourquoi je cherche des alternatives. N'hésitez p
as à me dire que je me trompe.

Traduit et reposté à partir de la publication 141ttwt de la communauté localllama. Pour 
retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Is there any method in Langchain to fetch content of Sub URL by giving its base URL only ](https://www.reddit.com/r/LangChain/comments/18l3de2/is_there_any_method_in_langchain_to_fetch_content/) , 2023-12-19-0910
```
I am working on a project where i need to fetch the content of sub URL by giving its base URL only.  
Is there any metho
d in Langchain to fetch content of Sub URL by giving its base URL only?
```
---

     
 
all -  [ Running LLMs on MAC - Use GGUF or GPTQ? ](https://www.reddit.com/r/LangChain/comments/18l2mom/running_llms_on_mac_use_gguf_or_gptq/) , 2023-12-19-0910
```
Hi,

i am using LlamaCpp to run local LLMs (Llama 2, Mixtral...) on Mac. 

Now I saw this [article](https://medium.com/m
learning-ai/run-gptq-ggml-gguf-on-apple-silicon-f116bceb6ebc#:~:text=In%20the%20current%20version%2C%20the,but%20has%20m
inimal%20performance%20gain) where the author claims that GGUF is CPU only and GPTQ for GPU. As for now I always used th
e GGUF format for runnning my models locally on MAC, but would it be better to use GPTQ? Or is GPTQ not supported for th
e Mac GPU?

Thanks & Regards!
```
---

     
 
all -  [ GPT Custom Knowledge Chatbot ](https://www.reddit.com/r/djangolearning/comments/18kvz4p/gpt_custom_knowledge_chatbot/) , 2023-12-19-0910
```
Hello everyone,

I am looking to create a chatbot that is trained on our company's documentation that is available on a 
deployed company django site. I have been attempting to research different ways of accomplishing this, there seem to be 
several options and a detailed blogpost on Langchain's blog ( [Building Chat LangChain](https://blog.langchain.dev/build
ing-chat-langchain-2/)  ,  [Tutorial: ChatGPT Over Your Data (langchain.dev)](https://blog.langchain.dev/tutorial-chatgp
t-over-your-data/) ) seems to be promising for creating a chatbot with Langchain and OpenAPI embeddings.

I have a coupl
e questions I am hoping that the Djangolearning community can help me with!

1. Is Langchain + OpenAI embeddings a good 
approach for a GPT wrapper using company documentation to generate responses from the GPT LLM? (Likely planning to use G
PT-3 due to lower cost?)
2. If this is the correct approach, could someone point me to a tutorial or documentation for d
eploying something like this?
   1. There seems like many different ways to do this, I would love to hear from some expe
rienced folks for best practice, packages, architecture, to implement something like this so I head in a good direction.


Thank you very much!
```
---

     
 
all -  [ Limitations of Dataframe agents ](https://www.reddit.com/r/LangChain/comments/18kufmr/limitations_of_dataframe_agents/) , 2023-12-19-0910
```
What are the limitations of using a dataframe agent?
```
---

     
 
all -  [ Best Third Party RAG ](https://www.reddit.com/r/LangChain/comments/18krsf0/best_third_party_rag/) , 2023-12-19-0910
```
What is your favourite third party RAG as of December 2023?
```
---

     
 
all -  [ Falcon 40B in AWS ](https://www.reddit.com/r/LangChain/comments/18knfsw/falcon_40b_in_aws/) , 2023-12-19-0910
```
Hello everyone 
Want to understand if anyone has deployed Falcon40B in AWS and what is the latency you get, i tried upto
 g5.24x instances. Could not get beyond 5.5s latency, want to have it below 3s
```
---

     
 
all -  [ LCEL Changes ](https://www.reddit.com/r/LangChain/comments/18klcp1/lcel_changes/) , 2023-12-19-0910
```
Are the LCEL changes and the relevant version of Langchain backwards compatible? Meaning, can I upgrade to the version w
ithout having to change any code, and then take advantage of LCEL? if I understand, some module names and importance hav
e changed, but I assume these would come with warnings and not error out...
```
---

     
 
all -  [ Web search ](https://www.reddit.com/r/LangChain/comments/18kkqln/web_search/) , 2023-12-19-0910
```
I wanted to implement a local LLM that has the capability to browse the internet and get the latest info. I tried using 
playwright but it always caused error. So, is there any other way?
```
---

     
 
all -  [ Build your first AI-powered application using LangChain. ](https://www.reddit.com/r/LangChain/comments/18kk2us/build_your_first_aipowered_application_using/) , 2023-12-19-0910
```
If you're new to the AI world and want to create your own custom AI powers application, this article is tailored for you
.

https://journal.hexmos.com/langchain/
```
---

     
 
all -  [ What's the ACTUAL status of tools such as BabyAGI or Auto-GPT? ](https://www.reddit.com/r/ChatGPT/comments/18kgi6h/whats_the_actual_status_of_tools_such_as_babyagi/) , 2023-12-19-0910
```
I've noticed that GPT4 frequently requires re-querying to validate points it may have made. To illustrate this, imagine 
asking it to read a document and summarize it. It now made an error in the summary. You prompt it to correct it. the tex
t comes back but now it needs formatting and some words changed... you get my point I'm sure. 

Tools like auto-gpt were
 interesting in the sense they could automate this. I know I can use langchain to recreate them, but I would prefer to u
se a 3rd party, tried and tested solution (my expertise lies elsewhere these days). 

What's the current state of tools 
like BabyAGI? Do you know if they were superseeded by better engines? I've read comments stating they were 'dead in the 
water' - is that true?  If so, what should I use for iterative processes?

PS: already tried custom GPTs, no luck, it ca
n't get it to become recursive.
```
---

     
 
all -  [ How do you deal with LLM observability? What tools do you guys use? ](https://www.reddit.com/r/LangChain/comments/18kdq04/how_do_you_deal_with_llm_observability_what_tools/) , 2023-12-19-0910
```
I want to know the tools and methods you use for the observability and monitoring of your ML (LLM) performance and respo
nses in production.
```
---

     
 
all -  [ LLM_Web_search for text-generation-webui: it's pretty awesome! ](https://www.reddit.com/r/LocalLLaMA/comments/18k8f2x/llm_web_search_for_textgenerationwebui_its_pretty/) , 2023-12-19-0910
```
The following conversation was had using 'Mistral 7B' with the **LLM\_Web\_Search** extension installed. I really like t
hat it determines when it wants to search itself and what terms it will use!

&#x200B;

>**Searcher**  
>  
>How can I h
elp you today, using the internet as my guide!  
>  
>**You**  
>  
>What was the last patriots game final score?  
>  

>**Searcher**  
>  
>I'd be happy to help you with that! Let me just check the most recent information I can find.  
>  

>Search\_web: 'Last Patriots game final score'  
>  
>**Searcher**  
>  
>Based on the information I've found, the last
 Patriots game final score was 21-18 in favor of the Patriots against the Steelers.  
>  
>**You**  
>  
>When was that 
game played?  
>  
>**Searcher**  
>  
>The last Patriots game against the Steelers was played on December 7, 2023.

&#x
200B;

You can check it out here: [https://github.com/mamei16/LLM\_Web\_search](https://github.com/mamei16/LLM_Web_searc
h)

I personally couldn't get the 'conda env' thing to work to install all of the requirements, so I manually (and tempo
rarily) added these requirements to requirements.txt and ran update\_windows.bat (under wandb):

    faiss-cpu==1.7.4
  
  duckduckgo-search==4.1.0
    beautifulsoup4==4.12.2
    langchain==0.0.177
    unstructured==0.6.6

I also added a 'Se
archer' character that had this context:

    A chat between a curious user and artificial intelligence assistant. The a
ssistant is never confident about facts and up to date information. The assistant can search the web for facts and up to
 date information using the following search command format:
    Search_web:  \'<|query|>\'
    The search tool will sea
rch the web for these keywords and return the results. Finally, the assistant extracts the information from the results 
of the search tool to guide its response.

I find it quite neat, I hope it gets a little more love and perhaps be consid
ered a default extension? It took me awhile to find a searcher this good!
```
---

     
 
all -  [ Chat Assistant supporting the latest OpenAI API ](https://www.reddit.com/r/ChatGPTPro/comments/18k3i64/chat_assistant_supporting_the_latest_openai_api/) , 2023-12-19-0910
```
I haven't seen much traction in terms of conversational assistants lately, so perhaps this will be of interest to some o
f you.

Over the last month or so, I've been working on a Chat Assistant Template that uses the latest OpenAI API's to o
ffer a more advanced Generative and Conversational AI experience.  It's still in early stages, but I think it contains e
nough features to be useful to some people, so I decided to share it. 

Some of the more interesting features include:


* Multi-user Authentication using next-auth ✅ (Including a custom CredentialProvider for guest login)
* Customizable, Mu
ltipurpose Assistants with support for File Uploads. ✅
* Code Interpretation/Generation. ✅ (Supported as part of Assista
nts implementation)
* Query/Discussion of uploaded documents. ✅ (Supported as part of Assistants implementation)
* Contr
ol over your data ✅(You can delete your Assistant and all associated files from openAI)
* Streaming chat support for the
 standard chat, excluding assistants as it's not supported yet ✅ (Without any external dependencies, such as Langchain, 
or [Socket.io](https://Socket.io))

&#x200B;

In the coming days I'll be adding support for Image Analysis/Generation, a
s well as traditional RAG, using Vector DB's. So, essentially I aim to cover the main aspects of the latest OpenAI API.


&#x200B;

Feel free to grab it and do whatever you want with it :)

[https://github.com/athrael-soju/Titanium](https://
github.com/athrael-soju/Titanium)
```
---

     
 
all -  [ Is a local-LLM assistant a realistic goal at this point? ](https://www.reddit.com/r/LocalLLaMA/comments/18jx1bl/is_a_localllm_assistant_a_realistic_goal_at_this/) , 2023-12-19-0910
```
AI/LLM is crazy to wrap my head around. So many moving parts and variables to compare, and so much is moving (and search
 engines are getting so bad) it's hard to tell if reading posts from six months ago have any real relevance on the topic
 today. For reference to where I sit- I call myself a script kiddie- I can run most projects i find on github, i can ada
pt some to suite what i need, but I'm not much one for architecting new solutions, especially on complex issues.   


AI
 assistants are something that come up a lot, but is usually poorly defined on what that means- an expert consultant on 
coding, writing, or what?  How do you want to interact with it? Etc. How I'd define an assistant:  


1. The ability to 
interface with other systems. In a vacuum it's just a sounding board, but I'd like the ability for it to update/check ca
lendars, run a websearch to compare it's own answer against results, give summaries of emails, documents, etc. Tied into
 this, some ways to trigger behaviors simply from external systems. - 'If i get an email from my boss, reply with 'i'm w
orking on it' in 10 minutes, and add it to my task list in Obisidan' 
2. Memory - If you have to constantly repeat the s
ame information, it kinda defeats the purpose. I know there's options for using vector databases and RAG to try to get a
round this, but you'd still need some intelligence to figure out what's worth pulling from the DB/Documents to include i
n the request sent forward, or what information from a token is worth storing. I can't figure out if we have a real solu
tion here for that yet- or if everything just gives a bit of improvement, and you'll still see LLMs with dodgy memory.
3
. Still hard to define, but the ability to learn, to get better at doing the kind of tasks set for it.   

4. Should be 
easy to interact with when needed, but also should ideally be able to handle multiple users, so you can adjust the permi
ssions, try to adjust user preferences etc.   


What i've seen looking around- Langchain might be the answer to 1, and 
might assist with 2, but in reading posts on this reddit mentioning them- i see a lot of users talking about not being a
ble to get langchain to work, and even then it's a framework not so much a plug and play solution. . Memgpt seems to hav
e started a buzz, but I don't see people reporting on their experience with deploying it.   


Sillytavern, as much as i
t's built for roleplaying, feels like it gives a picture of a lot of these options, with all it's extensions and extras,
 but having played with it, I'm left feeling mostly disappointed. One moment I can it doing something clever, the next i
t has problems following along a basic description.   


I can't tell if my disappointment may be because of bad setting
s, prompting, model choices or limitations, etc etc, but I'm overall left with the impression that this isn't possible u
nless i'm able to invest a lot of time into learning and connecting some frameworks and projects, and even then performa
nce may be spotty. 

  


&#x200B;
```
---

     
 
all -  [ Need help to build a RAG application on legal data - vectorDB vs Knowledge graph ](https://www.reddit.com/r/LangChain/comments/18jug2b/need_help_to_build_a_rag_application_on_legal/) , 2023-12-19-0910
```
I need suggestion on this space. I need precise answers to certain questions related to a legal data. Vector databases s
eems to be bad on this, while knowledge graphs are good. But converting legal documents into knowledge graphs is pretty 
difficult and approximate.  How do I decide on this ? Should I use both ? Are there any exisiting tutorials on this ?
```
---

     
 
all -  [ Mixtral 8x7B Instruct hallucinates ](https://www.reddit.com/r/LangChain/comments/18ju44k/mixtral_8x7b_instruct_hallucinates/) , 2023-12-19-0910
```
Hi,

I am using the quantizes Mixtral 8x7B version from the bloke. It works fine, however the model keeps hallucinating 
in my RAG application.

Does anyone have suggestions how I can improve my prompt?

Here it is (normally in German, I tra
nslated it for better understanding):

'mistral\_prompt = '''

<s> \[INST\] You are a helpful chat assistant named Mixtr
al.

Answer the user's question only in German, NEVER in English.

Use the context found to answer the questions.

If yo
u don't know the answer, just say that you don't know the answer.

If the answer is not in context, answer that there is
 not enough information in the context to answer the question.

Keep your answers precise.

A conversation history is av
ailable after 'Chat History'.

If you notice that the user is engaging in small talk, engage in small talk with them\[/I
NST\] </s>

\[INST\] Chat history: {chat\_history}

Question: {question}

Context: {context}

Answer: \[/INST\]

''''

&
#x200B;

Thanks in advance!
```
---

     
 
all -  [ Best high level approach for creating custom gpts automatically ](https://www.reddit.com/r/LangChain/comments/18ju3fg/best_high_level_approach_for_creating_custom_gpts/) , 2023-12-19-0910
```
Hello,

I am starting a project soon where I will build chatbots that help employees at my company quickly write message
s, project proposals, etc. for clients. The 'knowledge base' for each chatbot should be the long history of past emails 
and slack messages. I would really love to discuss with someone experienced what the best approach to this is but I will
 describe what I am thinking, any feedback is appreciated.

1. Concatenate emails and messages by date into a smaller nu
mber of .md files (I just hear that if you structure these well they get indexed for retrieval effectively by llms?) one
 set of files per client. This will happen as a scheduled job.
2. Use the assistants api to create a chatbot for each cl
ient, uploading the relevant files with retrieval tool enabled. This would happen as a scheduled job as well each night,
 updating the knowledge base daily if the files in a given client's folder changed.

I am not sure if just using the ope
nai api like this will be sufficient or if I need to do something a little more advanced and learn to use langchain to c
reate a more custom tool... any thoughts are welcome.

Edit: removed the bit about assistant playground, that doesn't wo
rk like I thought it did.
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-19-0910
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-19-0910
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-19-0910
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-19-0910
```
I've been trying to work with structured data in language models, and it's proving to be quite challenging. I'm confiden
t that with Langchain, I should be able to solve the problem, but I'm not entirely sure which path to take among all the
 options the library offers.

My issue is as follows: I have data in the form of dictionaries regarding a series of prod
ucts, for example, laptops. The data looks like this:

{Identifier 1: X, Identifier 2: Y, Value name: Z}

(Several succe
ssive dictionaries like this.)

I want to use this series of dictionaries as context, then feed a different dictionary i
nto the Language Model, and have it tell me if the 'Value name' makes sense given Identifiers 1 and 2. An example would 
be Identifier 1: laptops, Identifier 2: brand, Value name: Lenovo. In this case, it should return affirmative since Leno
vo makes sense as a brand. However, if I input 'oranges,' it should return negative.

Any ideas on which library I could
 use to tackle this problem?
```
---

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-19-0910
```
Hi all!

A couple of days ago, when I was scrolling down Hacker News, exploring news about OpenAI and the latest specula
tion about Q\*, it occurred to me to create a ChatBot that would allow me to interact with Hacker News directly, in a co
nversation.

Using streamlit, langchain and openai functions I managed to create a first version of this chat (I still h
ave to add RAG for news analysis and test other types of LLMs). 

Here is an example, what do you think?

Code: [https:/
/github.com/neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhacker
bot.streamlit.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://i.redd.it/rtpof7biqi2c1.gif
```
---

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-19-0910
```
 

  
For example with the following structure:

* System = GPT-4 Turbo + Llama2 +3rd LLM (!)+ Google or Bing API for we
bsearch + Langchain + any vectorDB + Document upload + longterm Memory + …

Idee behind it is to get more accurate, upda
ted (websearch) and specialized system or even let the LLms discuss your prompt before completion! Question is also, how
 shall the interaction of multiple LLMs in a system be organzied (Algorithm, Python Library …)? And what kind of Interac
tion can/should this be? Master-slave or Multi-Master system?
```
---

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-19-0910
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user.
```
---

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-19-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-19-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-19-0910
```
In the domain of document analysis, the convergence of text, tables, and images presents formidable challenges for conve
ntional RAG (Retrieval Augmented Generation) methodologies. This complexity is further compounded within semi-structured
 data, notably in the extraction of tables from PDFs. Enter LangChain, a pioneering tool adept at navigating these intri
cate landscapes. Augmenting its capabilities is LlamaIndex, integrating Multi-Modal Retrieval Augmented Generation (RAG)
 techniques. Together, LangChain and LlamaIndex stand poised to revolutionize the handling and extraction of diverse con
tent types, promising a breakthrough in unraveling insights from varied data formats.

Link in the comment
```
---

     
