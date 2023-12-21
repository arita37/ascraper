 
all -  [ Integrating LlamaIndex with Langchain. ](https://www.reddit.com/r/LangChain/comments/18n65if/integrating_llamaindex_with_langchain/) , 2023-12-21-0910
```
Hey guys, I am wondering if you know of good guides to go about doing this \^

And would it result in a better memory re
trieval system? (I've heard LlamaIndex is better for RAG systems?) Or would you build everything in Langchain? My system
 will involve a fine-tuned model, external knowledge, plus I am trying to figure out how to store conversation history i
n the vector db for memory retrieval. Eventually I'll add more components like speech-to-text software.. is this support
ed with langchain? Any guidance on this is greatly appreciated.

Right now I'm using Flowise which is built on top of La
ngChain, but haven't found any info on integrating LlamaIndex with Flowise specifically.
```
---

     
 
all -  [ Build your own GPT 5 with Mistral 7B and LangChain ](https://youtu.be/Bc-OSax1G2o) , 2023-12-21-0910
```
Can you develop a latest, your own GPT model with the latest release of mistral 7-b. in this video they talk about using
 Retrieval augmented generation and mistral 7-b. what are your guys thought?
```
---

     
 
all -  [ PGVector - Table ](https://www.reddit.com/r/LangChain/comments/18n2an2/pgvector_table/) , 2023-12-21-0910
```
i was using OPENAIEmbedding before but now i changed it to AzureOpenAIEmbedding but re-building the vector db takes a ve
ry long time. is there anyway i can drop the existing table and re-build it from scratch? although i already have `pre_d
elete_collection=True`

I am using 0.0.348 version 
```
---

     
 
all -  [ Text pre-processing before embedding ](https://www.reddit.com/r/LangChain/comments/18n1741/text_preprocessing_before_embedding/) , 2023-12-21-0910
```
I am trying to create a QNA chatbot with OpenAI API, after using RecursiveCharacterTextSplitter,  texts are coming with 
**'\\n'** Should I be worried? because I have to upsert it into the Pinecone database, and also if there is any preproce
ssing needed before upserting please tell me.. this is my first project

these are the texts: 

`['The\ncow,\na\ngentle\
nherbivorous\nmammal\nof\nthe\nBovidae\nfamily,\nis\na\nvital\ncontributor\nto\nagriculture\nand\nhuman\nsustenance\nglo
bally.\nCharacterized\nby\nits\nlarge\nbody,\ncloven\nhooves,\nand\ndistinctively\npatterned\nhide,\ncows\nprimarily\nse
rve\nas\nsources\nof\nmilk,\nagriculture,livestock,\nfarming\nand\nleather.\nBos\ntaurus,\nthe\nmost\ncommon\nspecies,\n
exists\nin\nvarious\nbreeds,']`

my code : 

    loader = PdfReader('cow.pdf')
    text = ''
    for i,page in enumerate
 (loader.pages):
        content = page.extract_text()
        if content:
            text += content
    
    text_spl
itter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', ' '],
        chunk_size = 400,
        chunk_
overlap  = 20,
        length_function = len,
    )
    
    texts = text_splitter.split_text(text)
    print(texts)
   
 print(len(texts))
    
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    vectorstore = Pinecone.fro
m_texts(texts,embeddings,index_name=PINECONE_INDEX)

&#x200B;
```
---

     
 
all -  [ How can I modify the context retrieved by RetrievalQA Chain? ](https://www.reddit.com/r/LangChain/comments/18n0obz/how_can_i_modify_the_context_retrieved_by/) , 2023-12-21-0910
```
Guys, I'm in a pickle. I'm evaluating my RAG using Trulens and this takes in the RetrievalQA chain. But I want to modify
 the context to add more information to it say from the metadata. Is it possible to modify the context retrieved by Retr
ievalQA to add information from metadata and perhaps add more info to the context?
```
---

     
 
all -  [ What's wrong with my Resume ? ](https://i.redd.it/3qqhy7rb0h7c1.png) , 2023-12-21-0910
```

```
---

     
 
all -  [ Need help in adding context awareness to LLM RAG pipeline ](https://www.reddit.com/r/LangChain/comments/18mxiny/need_help_in_adding_context_awareness_to_llm_rag/) , 2023-12-21-0910
```
Hello all, 

I want to add context awareness to my LLM RAG pipeline. Here are 2 approaches I am thinking of. Please help
 me if I am going in the right direction, and also what should be the ideal approach :

Approach 1 :
Step 1.  Use an LLM
 to do co reference resolution in the new query, based on immediate last conversarion, and get the modified query.   
Ex
ample :
 last conversarion : What is Google? 
New query: what does it do ? 

Modified query : what does Google do . 

St
ep 2. Now based on modified query, get similar responses based on similarity score of previous conversations and add it 
to the prompt. 

Cons :
1. With coreference resolution  since we are using only immediate last query, it would lose out 
on, where the user query refers to noun or subject from earlier conversation .  

Pros :
Woukd only pass the relevant co
nversation. 

Approach 2 : 
Summarize the conversation history,  and store it in memory. As tye conversation proceeds, k
eep on adding to the conversation history. 

Cons :
In case of context switching, the summary would also have non releva
nt context being added to the prompt. How to handle this ?
```
---

     
 
all -  [ RetrievalQA with llamacpp api call ](https://www.reddit.com/r/LangChain/comments/18mwpft/retrievalqa_with_llamacpp_api_call/) , 2023-12-21-0910
```
Hi all,

I am trying to create a chatbot that uses both regular chat or RAG. 
When using the chat functionality I’m able
 to use the API offered by llama cpp server.
But how would I use the API when using the retrievalQA method, to search do
cuments from a vectordb (chroma).

Thanks
```
---

     
 
all -  [ [Local Llama] Modèles à finetuned pour l'appel de fonction? ](https://www.reddit.com/r/redditenfrancais/comments/18mvsg3/local_llama_modèles_à_finetuned_pour_lappel_de/) , 2023-12-21-0910
```
Bonjour. Y a-t-il des modèles LLAMA2 finetunés qui peuvent encore fonctionner de manière fiable pour l'appel de fonction
? (Configuration des agents à Langchain et autres). La discussion précédente a environ 2 mois, donc je me demande s'il y
 a eu des avancées à ce sujet.

J'ai essayé de créer un chatbot qui peut rechercher sur Internet et peut être hébergé lo
calement, mais les modèles que j'ai essayés sont terribles à ce sujet.

Traduit et reposté à partir de la publication 17
0pej3 de la communauté localllama. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit
.com/'
```
---

     
 
all -  [ Route between LLMs ](https://www.reddit.com/r/LangChain/comments/18mrv75/route_between_llms/) , 2023-12-21-0910
```
Is there any way to route between different LLM models, like for codng related prompts it should use an LLM model that i
s good at coding and for conversational prompts a model that is good at chatting/conversing.
```
---

     
 
all -  [ Best practice for RAG with follow-up chat questions and LLM conversation? ](https://www.reddit.com/r/LocalLLaMA/comments/18mqwg6/best_practice_for_rag_with_followup_chat/) , 2023-12-21-0910
```
I am building something like a personal AI tutor for a hobby. I have done a few POCs using Langchain and Autogen, but I 
am still not sure what the right 'architecture' would look like. 

Simple example: discuss with the student which subjec
t (e.g. history), and which particular topic (e.g. ancient Rome) should be studied. Then the chain would need to 'collec
t' the relevant knowledge from RAG sources (so it has grounding and does not hallucinate, and also has access to the exa
ct set of knowledge that is determined by a particular school system). Then after it has the basics collected via the RA
G pattern, it would then discuss the topic with the student, ask follow-up questions, provide tests for the students to 
assess his/her knowledge, etc. In this 'mode', it wouldn't use any RAG lookup, but use what it has already put in the co
ntext earlier. 

The problem with Langchain ConversationalRetrievalChain with ConversationBufferMemory is that it still 
assumes that I am mainly using it for a RAG like use case. Maybe I am mistaken,  not sure. I have built another POC with
 Autogen, and that seems to work better, e.g. it can use more RAG more like a tool (function), and it can be better 'ste
ered' into the above working mode. But it is still not perfect. 

Also, it would not be a bad thing to realize this with
out having to use Langchain. 

**TL/DR:** I was wondering if there's a best practice for my use case, a personal tutor, 
which uses a RAG pattern, but the student would also be able to chat about the already extracted info extensively. 

&#x
200B;

&#x200B;
```
---

     
 
all -  [ [Machine Learning] [D] Y a-t-il quelque chose que Langchain peut faire mieux que l'utilisation direc ](https://www.reddit.com/r/redditenfrancais/comments/18m8be4/machine_learning_d_y_atil_quelque_chose_que/) , 2023-12-21-0910
```
Je n'ai pas beaucoup utilisé Chatgpt ni aucun autre LLMS, j'ai lu sur Langchain et ses cas d'utilisation, et j'ai du mal
 à enrouler la tête exactement ce qu'elle fait. D'après ce que je comprends, c'est une interface alternative pour les LL
M, permettant une commutation facile entre eux, et facilite le travail pour des cas d'utilisation spécifiques. Si je vou
lais écrire une application ou un script pour interagir avec LLMS et effectuer d'autres tâches, comment Langchain serait
-il meilleur que de simplement faire des appels API à un LLM, de récupérer le résultat en tant que chaîne et de faire qu
oi que ce soit?

Traduit et reposté à partir de la publication 165airj de la communauté machinelearning. Pour retrouver 
la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Favorite setup for agency ](https://www.reddit.com/r/LangChain/comments/18m3tb3/favorite_setup_for_agency/) , 2023-12-21-0910
```
What would be your favorite setup client hosted to have csv, pdf and api chatbot?
```
---

     
 
all -  [ Connect to a local LLM compatible with openAI api ](https://www.reddit.com/r/LangChain/comments/18m319f/connect_to_a_local_llm_compatible_with_openai_api/) , 2023-12-21-0910
```
Hi.

It seems text generation webui migrated is api to a compatible version of openapi swagger which seems to be a good 
news.

Due to that, textgen LLM no longer works.
I don't find an easy way to connect to an api compatible with open ai i
n Langchain.

I was hoping for something like changing open api base path but I don't see anything like that in the docu
mentation.

Someone has an idea if an LLM object exist to connect to a local api compatible with open ai or how to use o
penai but with a different base path ?
```
---

     
 
all -  [ Don't have the english term to describe what I'm looking for ](https://www.reddit.com/r/LangChain/comments/18m2tf2/dont_have_the_english_term_to_describe_what_im/) , 2023-12-21-0910
```
Dear friends,

I'm stuck in an uncanny valley beween peaks of ignorance and peaks of insufficient english proficiency :)


I'm dreaming about a LLM able to generate a summary (?) of a news article. I don't know if summary is the right term. 
Or maybe is 'topic extraction' a better term? I've also read 'factoid identification' somewhere.

For example ideally on
 the following article: [https://www.bbc.com/news/world-europe-67756413](https://www.bbc.com/news/world-europe-67756413)


I would like the LLM to reply with something like:

* A volcano erupted on the Reykjanes peninsula in Iceland.
* Grind
avik has been evacuated but there are no casualties

I did a little experiment with Mixtral MOE and it produced decent v
ery long/verbose summaries. It could also not reply correctly to questions like 'Who's mentioned in this article' and of
 course the following 'What did X say' was not possible.

Is there any suggestion you could give me of models on HF that
 I could try to get closer to my needs? 

Oh did I mention that I need this for Italian (and as a less important need Fr
ench, Spanish, English and German) ?

Grazie mille !!!
```
---

     
 
all -  [ Need help for a similarity search application ](https://www.reddit.com/r/LangChain/comments/18m0kch/need_help_for_a_similarity_search_application/) , 2023-12-21-0910
```
Hi,

I am new to langchain and AI/ML in general and would really appreciate if someone could help me.

I have a list of 
addresses of a city which I am storing in a chromadb using their default embedding (all-MiniLM-L6-v2). And then I have a
nother set of addresses(incomplete and misspelled) which I wanna use them as a query and want to return as similar addre
ss as possible.
Some of them works perfect but for some addresses it behaves strangely.

For example: if I search for “X
YZ building, ABC Town, City”
It will return an address from “ABC street” instead of “ABC Town” although I have both of t
hem in my knowledge base on which my model is trained. And sometimes it will return completely irrelevant address which 
doesn’t match.
I want to ask how can I improve this? Or is this even the right approach or should I go for a different a
pproach. TIA
```
---

     
 
all -  [ LLMLingua compatibility/support ](https://www.reddit.com/r/LangChain/comments/18lxgel/llmlingua_compatibilitysupport/) , 2023-12-21-0910
```
Any chance Langchain supports LLMLingua already ? or something that we may have to wait for ?
```
---

     
 
all -  [ Is it even possible to initialize Vector Stores without using the default table structure? ](https://www.reddit.com/r/LangChain/comments/18lodyx/is_it_even_possible_to_initialize_vector_stores/) , 2023-12-21-0910
```
Hi everyone!

I have been able to succesfully create a vector store with Postgres and PGVector using Langchain from end 
to end, as described in this article: [https://python.langchain.com/docs/integrations/vectorstores/pgvector](https://pyt
hon.langchain.com/docs/integrations/vectorstores/pgvector)

I noticed it creates the ***langchain\_pg\_collection*** and
 ***lanchain\_pg\_embedding*** tables in Postgres. Upon inspceting the LangChain source code, it seems it really relies 
on that specific two table structure in order to instantiate a VectorStore.

Suppose that instead of having my embedding
s structured this way, I would like to have them as a column in a differente table, like my contents table (which has th
e string the values I want to embed).

Would I still be able to initialize the VectorStore pointing to that specifc tabl
e and column?Or does the entire VectorStore functionality only works if I use the default table structure?

I would real
ly appreciate all the help and guidance I could get here.
```
---

     
 
all -  [ Panel ChatInterface lets you create chat interfaces with just Python ](https://www.reddit.com/r/Python/comments/18lnrx5/panel_chatinterface_lets_you_create_chat/) , 2023-12-21-0910
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

     
 
all -  [ Panel ChatInterface lets you create ](https://www.reddit.com/r/madeinpython/comments/18lnprm/panel_chatinterface_lets_you_create/) , 2023-12-21-0910
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

     
 
all -  [ Search in large JSON ](https://www.reddit.com/r/LangChain/comments/18ln785/search_in_large_json/) , 2023-12-21-0910
```
I want to make an agent that uses a tool that searches for keywords in a huge JSON. I succeeded in getting it to fetch d
ata from an API, but the user should also be able to filter data chunks with keywords. For example, 'which ticket has th
e keywords user, sister, and admin' it must be able to filter in large data which is around 150k token. How would you co
me around this?
```
---

     
 
all -  [ At Present, What are the Best AI Companion Apps? ](https://www.reddit.com/r/ChatGPTCoding/comments/18lj3w3/at_present_what_are_the_best_ai_companion_apps/) , 2023-12-21-0910
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

     
 
all -  [ Articles, courses and other resources for multimodal AI ](https://www.reddit.com/r/learnmachinelearning/comments/18lgo4y/articles_courses_and_other_resources_for/) , 2023-12-21-0910
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

     
 
all -  [ issues doing an sql bot ](https://www.reddit.com/r/LangChain/comments/18lfmtf/issues_doing_an_sql_bot/) , 2023-12-21-0910
```
hello, basically I’m unable to run my sql analysis bot virtually, since it needs local host connection to the sql source
. any idea of how I could fix this? 
my local bot runs perfectly fine, but when uploading it to streamlit share it compl
etely fails. 

I could send the GitHub if anyone can help, thank you a lot in advance 🙏
```
---

     
 
all -  [ Best model for tabular analysis ](https://www.reddit.com/r/LocalLLaMA/comments/18lffx3/best_model_for_tabular_analysis/) , 2023-12-21-0910
```
Hey guys,  


I have built a simple prototype of a chatbot to talk to a tabular data  - essentially langchain->gpt4->pan
das query. It works better than I was expecting with some prompting.  If i wanted to switch out gpt4 for an 'open' llm w
hich one is best suited to this task? What benchmarks should I be looking at?   


&#x200B;
```
---

     
 
all -  [ Cookbook examples are riddled with errors ](https://www.reddit.com/r/LangChain/comments/18lems2/cookbook_examples_are_riddled_with_errors/) , 2023-12-21-0910
```
Seems like I can't get through an entire cookbook topic without encountering an error. The errors seem to occur with par
sers and runnables. 

What's going on? I recently installed langchain. Are the docs outdated at this point?
```
---

     
 
all -  [ Intersection of AI Efficiency and Data Privacy ](https://www.reddit.com/r/LangChain/comments/18lc9qo/intersection_of_ai_efficiency_and_data_privacy/) , 2023-12-21-0910
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

     
 
all -  [ Chat conversation memory management ](https://www.reddit.com/r/LlamaIndex/comments/18lbykf/chat_conversation_memory_management/) , 2023-12-21-0910
```
I've been playing with a chatbot, using LangChain VectorStoreRetriever memory (https://python.langchain.com/docs/modules
/memory/types/vectorstore_retriever_memory). I'm using Chroma and Instructor-Large embeddings. I'm adding timestamps and
 trying to make the bot aware of the relationship of messages in term of content and time. It kind of works, but it's no
t ideal. Also, with their boilerplate code I don't see a way to restrict the amount of tokens inserted into the conversa
tion (for larger k values). Is there a better way to manage this with Llama-Index?
```
---

     
 
all -  [ LlamaCpp on MAC: n_gpu_layers, n_batch ](https://www.reddit.com/r/LangChain/comments/18lb4n4/llamacpp_on_mac_n_gpu_layers_n_batch/) , 2023-12-21-0910
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

     
 
all -  [ [Rust] Y a-t-il une caisse de Langchain? ](https://www.reddit.com/r/redditenfrancais/comments/18l93hd/rust_y_atil_une_caisse_de_langchain/) , 2023-12-21-0910
```
Je fais des recherches et rejoignais le train de battage médiatique d'IA. Et j'aimerais explorer la programmation tout e
n continuant à apprendre la rouille. Je me demandais s'il y avait une bibliothèque open source similaire à Langchain que
 je peux contribuer? Sinon, je pourrais essayer de commencer quelque chose.

Traduit et reposté à partir de la publicati
on 13l89ur de la communauté rust. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.
com/'
```
---

     
 
all -  [ LangServe <> Slack/Discord Integration (no code) ](https://www.reddit.com/r/LangChain/comments/18l87tj/langserve_slackdiscord_integration_no_code/) , 2023-12-21-0910
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

     
 
all -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2023-12-21-0910
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

     
 
all -  [ [Langchain] Chroma ou Faiss? ](https://www.reddit.com/r/redditenfrancais/comments/18l6szp/langchain_chroma_ou_faiss/) , 2023-12-21-0910
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

     
 
all -  [ [Langchain] Exemple pour le reconstitution en chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/18l6rt1/langchain_exemple_pour_le_reconstitution_en/) , 2023-12-21-0910
```
Je cherche à en savoir plus sur la façon de mettre en œuvre le rediffusion dans une implémentation de chiffon. Des tutor
iels / articles recommandés par la communauté?

Traduit et reposté à partir de la publication 16ms4m4 de la communauté l
angchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Local Llama] Alternative à Langchain pour les LLM ouvertes? ](https://www.reddit.com/r/redditenfrancais/comments/18l5zss/local_llama_alternative_à_langchain_pour_les_llm/) , 2023-12-21-0910
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

     
 
all -  [ Is there any method in Langchain to fetch content of Sub URL by giving its base URL only ](https://www.reddit.com/r/LangChain/comments/18l3de2/is_there_any_method_in_langchain_to_fetch_content/) , 2023-12-21-0910
```
I am working on a project where i need to fetch the content of sub URL by giving its base URL only.  
Is there any metho
d in Langchain to fetch content of Sub URL by giving its base URL only?
```
---

     
 
all -  [ Running LLMs on MAC - Use GGUF or GPTQ? ](https://www.reddit.com/r/LangChain/comments/18l2mom/running_llms_on_mac_use_gguf_or_gptq/) , 2023-12-21-0910
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

     
 
all -  [ GPT Custom Knowledge Chatbot ](https://www.reddit.com/r/djangolearning/comments/18kvz4p/gpt_custom_knowledge_chatbot/) , 2023-12-21-0910
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

     
 
all -  [ Limitations of Dataframe agents ](https://www.reddit.com/r/LangChain/comments/18kufmr/limitations_of_dataframe_agents/) , 2023-12-21-0910
```
What are the limitations of using a dataframe agent?
```
---

     
 
all -  [ Best Third Party RAG ](https://www.reddit.com/r/LangChain/comments/18krsf0/best_third_party_rag/) , 2023-12-21-0910
```
What is your favourite third party RAG as of December 2023?
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-21-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-21-0910
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-21-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-21-0910
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

     
