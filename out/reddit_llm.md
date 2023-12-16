 
all -  [ Mixtral Settings ](https://www.reddit.com/r/LocalLLaMA/comments/18jawag/mixtral_settings/) , 2023-12-16-0910
```
Hi all, I've been able to get `mixtral-8x7b-v0.1.Q6_K.gguf` running on on the Oobabooga web UI, using dual 3090's. I've 
seen some flashes of brilliance, but so far it is hard to get it to generate usable content. I'm getting better output w
ith other models (usually 70b 4-bit quantized models to be fair, though the mixtral version I am using is only slightly 
smaller than those). For reference, I am focused on more productivity related uses (i.e. following instructions), rather
 than creative.

I've been playing around with settings, but I have not been able to get consistently usable output, tho
ugh they do seem to have a significant impact on the output.

What settings have others found that are optimal for Mixtr
al on Oobabooga?  I've seen some other threads with recommended settings, but I haven't found those very effective for w
hat I am doing.  

I've been using the chat-instruct mode in Oobabooga, but is there a better one?  Should I skip Oobabo
oga altogether and just use llama.cpp directly?  Ultimately I want to use it with langchain for productivity.

&#x200B;
```
---

     
 
all -  [ [Survey] LLM developer tools and APIs - raw data will be published! ](/r/LLMDevs/comments/18ijew5/survey_llm_developer_tools_and_apis_raw_data_will/) , 2023-12-16-0910
```

```
---

     
 
all -  [ Deploy RAG APP on AWS/Huggingface ](https://www.reddit.com/r/LangChain/comments/18j84xi/deploy_rag_app_on_awshuggingface/) , 2023-12-16-0910
```
Hi,

I have built a  langchain RAG Application with Streamlit locally on my Mac. Now I want to deploy it in the cloud wi
th AWS. It is just a demo App where some coworkers are trying the app out. I am doing hard with estimating the price of 
hosting the application in the cloud, so what are your thougts?

&#x200B;

I am using models like Mixtral 8x7B or Llama 
2 13b (all quantized versions from 'TheBloke'), and my vectordb is relatively small.

Thanks for your suggestions!
```
---

     
 
all -  [ Vectara OCR preview ](https://www.reddit.com/r/LangChain/comments/18j848d/vectara_ocr_preview/) , 2023-12-16-0910
```
Hey everyone,

One of the most asked-for feature from our customers was the ability to extract text from images and so w
e're excited to announce an upcoming OCR capability with Vectara.

If you are using r/Vectara's integration with r/LangC
hain, and using Vectara's FILE\_UPLOAD capability, this might be super helpful, especially with scanned documents as par
t of your RAG pipeline.

If you're interested to participate in our early preview - please join the waitlist here:   
[h
ttps://docs.google.com/forms/d/e/1FAIpQLSdGELyboIuytmLPqZNXwS5ur7gXTx28IWWONeqlOV-LSSxwaA/viewform](https://docs.google.
com/forms/d/e/1FAIpQLSdGELyboIuytmLPqZNXwS5ur7gXTx28IWWONeqlOV-LSSxwaA/viewform)
```
---

     
 
all -  [ Best python library for OpenAI API? ](https://www.reddit.com/r/OpenAI/comments/18j7ucf/best_python_library_for_openai_api/) , 2023-12-16-0910
```
Looking for 'lightweight' python libraries for calling OpenAI API

Features looking for:  


* parallel calling
* rate l
imiting
* auto retry

Want a bit more than the official library, but langchain and etc. feel like too much.
```
---

     
 
all -  [ [Langchain] ChromAdb Avantages? ](https://www.reddit.com/r/redditenfrancais/comments/18j72hd/langchain_chromadb_avantages/) , 2023-12-16-0910
```
Vous avez remarqué que peu de dépôts GitHub LLM utilisent ChromAdB au lieu de Milvus, tivent, etc. Un avantage particuli
er de l'utilisation de cette base de données vectorielle?

Traduit et reposté à partir de la publication 16s9vc5 de la c
ommunauté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Ml Questions] Comment fonctionne réellement la génération augmentée augmentée (RAG)? ](https://www.reddit.com/r/redditenfrancais/comments/18j6jqf/ml_questions_comment_fonctionne_réellement_la/) , 2023-12-16-0910
```
Naïvement, je suis familier avec la façon dont des cadres comme Langchain vous permet de 'chaîner' ensemble une série d'
étapes (en utilisant à la fois des invites et des API externes), S.T. Un LLM peut répondre à une question avec plus de p
récision et de rapidité.

Exemples d'étapes:

1. Recherchez une base de données vectorielle avec votre question / intégr
ation

2. 'Carte Réduire' ou résumer les multiples résultats en réponses concises

3. Répondez avec la réponse finale ou
 dites que je ne sais pas

Y a-t-il une approche plus sophistiquée du chiffon? Quelles sont d'autres façons de réaliser 
des chiffons en dehors de l'approche de Langchain (ce qui est tout à fait.

Traduit et reposté à partir de la publicatio
n 16mkd84 de la communauté mlquestions. Pour retrouver la publication originale, insérez l'id de la publication après 'r
eddit.com/'
```
---

     
 
all -  [ AI Agents vs. ChatGPT Tools/Functions ](https://www.reddit.com/r/LangChain/comments/18j6i0f/ai_agents_vs_chatgpt_toolsfunctions/) , 2023-12-16-0910
```
I have been working with LangChain and the OpenAI API for a long time now, but the other day a coworker asked me a quest
ion that I thought I knew the answer to, but now I'm a bit unsure.

So, he asked me, 'When I use ChatGPT Tools with the 
new gpt-4-1106-preview model, or ChatGPT functions with the older gpt-4-0314 model, am I talking to an AI Agent?

My ini
tial thought was yes, as LangChain has listed both models in their agent types: [OpenAI Functions](https://python.langch
ain.com/docs/modules/agents/agent_types/openai_functions_agent) and [OpenAI Tools.](https://python.langchain.com/docs/mo
dules/agents/agent_types/openai_tools)

However, going back to the ReAct days, we were taught that the models perform be
tter when we give them time to 'think' which is one key part of the framework, as they would create a thought, then take
 an action, and then observe the outcome. From my understanding, the models with Tools and Function capabilities do not 
provide a thought before they take an action on which tools to use, as they are fine tuned to just make a choice or answ
er directly. Looking up various definition of an AI Agents I found a lot that said something similar to this one: '*AI a
gents are entities designed to perceive their environment and take actions in order to achieve specific goals'.* So my q
uestion is then, is the gpt-4-1106-preview  and gpt-4-0314 models classified as an AI Agent? Or do they need to be used 
in a broader context, e.g. through the Assistants API.
```
---

     
 
all -  [ [Machine Learning] [D] Langchain vs Autogpt ](https://www.reddit.com/r/redditenfrancais/comments/18j4de4/machine_learning_d_langchain_vs_autogpt/) , 2023-12-16-0910
```
Je vois qu'il existe plusieurs bibliothèques concernant l'utilisation et le fintunage des LLM pour des tâches spécifique
s. Serait utile si quelqu'un pouvait expliquer la différence entre l'utilisation de Langchain, Autogpt et Babyagi?

Trad
uit et reposté à partir de la publication 12s2ldb de la communauté machinelearning. Pour retrouver la publication origin
ale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Conversational Memory with RAG ](https://www.reddit.com/r/LangChain/comments/18j3rti/conversational_memory_with_rag/) , 2023-12-16-0910
```
Do we have any chain that handle conversational memory with RAG like we ask two questions (Just for example)  
Who is Ob
ama?

When he was born?  


Do we have some functionality in langchain that handles the second question and pass updated
 question to similarity search i.e. When obama was born?
```
---

     
 
all -  [ Tokenizer of GGUF with LlamaCPP ](https://www.reddit.com/r/LocalLLaMA/comments/18j39l6/tokenizer_of_gguf_with_llamacpp/) , 2023-12-16-0910
```
Hey everyone,

I am working with a GGUF Model the Q8_0 of the ALMA-13B to be specific, it could be found here: 

https:/
/huggingface.co/TheBloke/ALMA-13B-GGUF/blob/main/alma-13b.Q8_0.gguf

 I want to change the Word Embeddings of its Tokeni
zer (the ALMA also has multilingual support, so Im not sure how its tokenizer is configured), but I am unable to access 
the Tokenizer using LlamaCPP (imported from langchain). I want to access the tokenizer, iterate through it and if I find
 a token which is present in my custom Word2Vec Embeddings (stored in a .bin format) , then change its vectors with the 
vectors present in my custom embeddings. 


Can anyone guide me or provide a link which can guide me? Any kind of help w
ill be appreciated

Thanks in advance
```
---

     
 
all -  [ Trying to add context to dataframe agent ](https://www.reddit.com/r/LangChain/comments/18j2j5e/trying_to_add_context_to_dataframe_agent/) , 2023-12-16-0910
```
I have been able to put together a good demo quickly using  'create\_pandas\_dataframe\_agent' but as I start asking har
der questions about my data I find it needs to be given some context.   


Right now I provide that in the query e.g.   
*agent. Run ('my query' + 'context')*  


I would like to strip out the context into the prompt, I tried using suffix/pr
efix but ther performance drops, instead of executing pandas query it just says it cant and shows me the code to run.   



Any ideas appreciated.   


&#x200B;
```
---

     
 
all -  [ [Langchain] Comment améliorer la qualité des réponses de chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/18j07cq/langchain_comment_améliorer_la_qualité_des/) , 2023-12-16-0910
```
Toutes ces applications 'discuter avec PDF' montrent des résultats particulièrement bons par rapport à Langchain QNAT st
andard basé sur le chiffon. Je me demande comment ils améliorent la qualité des réponses.

Cela devient encore plus évid
ent lorsque vous traitez des questions telles que 'Résumez ce doc'. Je ne vois pas comment on pourrait utiliser le chiff
on pour répondre aux questions liées au résumé. J'ai fait des recherches mais je n'ai pas encore trouvé de solution effi
cace.

Traduit et reposté à partir de la publication 171bevs de la communauté langchain. Pour retrouver la publication o
riginale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Created a AI Chatbot using OpenAI, Pinecone and LangChain ](https://www.reddit.com/gallery/18izww1) , 2023-12-16-0910
```
This chatbot can use you private database to provided personalized responses or can give responses through ChatGPT. Can 
integrate to any website. Can be customized according to the users preference.
```
---

     
 
all -  [ How to get same results for RAG when not using QA Retrieval Chain ](https://www.reddit.com/r/LangChain/comments/18ixnkm/how_to_get_same_results_for_rag_when_not_using_qa/) , 2023-12-16-0910
```
Hello all,

I'm working on a RAG system with my own documents but i feel like the QA Chain takes too much control from m
e when trying to work with the retrieved documents.

For example I want to use a local re ranking model for the retrieve
d documents before passing them to the LLM. However the chain seems not to support this kind of altering of the retrieve
d documents without customizing the langchain code. 

So my idea was using a simple LLM chain. I get the relevant docs b
y calling the 'get\_relevant\_documents' function myself. Then i pass the docs to the re ranking model and afterwards pu
t into my prompt to the simple LLM chain. This way i can apply my own filters and whatever stuff i want to try out for t
he retrieved documents.

However i feel like the results are not entirely the same. Even without using the re ranker jus
t from comparing the two approaches i feel like i get slightly better results from using the QA chain. So i feel like I'
m missing something. I thought my approach is basically doing the same like the QA chain but it seems that its not. 

Am
 i overseeing something? Is there some kind of formatting within the qa chain?

Thanks for your help
```
---

     
 
all -  [ Need some help with document uploads for GPT-4 integration ](https://www.reddit.com/r/ChatGPTPro/comments/18iwrf4/need_some_help_with_document_uploads_for_gpt4/) , 2023-12-16-0910
```
Hey everyone

I’ve got an app I built that uses the GPT-4 chat completions API and simply passes the user’s input as a v
ariable into a predefined prompt (the usual stuff). 

I want to add a feature where users can upload a document, and the
n the contents of that doc get passed into the prompt. I’m trying to figure out the smoothest way to do this.

Unsure if
 the best option is something like langchain, the assistants API or otherwise. The app is built on React/TS. I’m not ent
irely sure what’s the best route here. If anyone’s done something similar or has any insights, I’d really appreciate it.
 What’s the easiest way to go about this? Any tools or approaches you’d recommend?

Looking forward to hearing your thou
ghts and suggestions!

Cheers :)
```
---

     
 
all -  [ Gave up on llama2 + langhlchain, a question about openai ](https://www.reddit.com/r/LangChain/comments/18it48v/gave_up_on_llama2_langhlchain_a_question_about/) , 2023-12-16-0910
```
Ilama2 was fun and free to experiment LLM for a starter and POC. 

But the reasoning skill and consistency of llama2 70B
 is far worse than gpt4. ( Not a surprise considering the size difference)

Langchain seems to have better support for o
penai as well. 

All in all, decided to swap out the llama2 and insert in openai() for more serious prod work. 

How man
y seconds does the openai API return a RAG completion? Llama 70B takes about 10-17 seconds to generate about 300 tokens 
by my estimation.
```
---

     
 
all -  [ [Question] langchain? Assistant API? Custom GPT? Finetuning? ](https://www.reddit.com/r/OpenAIDev/comments/18ib6yz/question_langchain_assistant_api_custom_gpt/) , 2023-12-16-0910
```
Hey guys,

I'm looking for options on the best approach to create a tool to make captions. I want to train it on old ins
tagram captions from multiple accounts. Not sure which avenue is best to do this. Goal is to know how to write in this s
tyle.

Langchain
Assistant API
Custom GPT
Finetuning

Could anyone with experience in this area share insights or recomm
endations on which direction to take? 

Your advice would be greatly appreciated!
```
---

     
 
all -  [ Better search with Chroma vector store? ](https://www.reddit.com/r/LangChain/comments/18i9hh8/better_search_with_chroma_vector_store/) , 2023-12-16-0910
```
* apart from trying different embedders, what can be done to get better search from a vector store?
* i'm currently usin
g \`e5-base-v2\` on a small test sample, and it's doing great! super relevant results
* however, once I expand the sampl
e to include all of our docs (which are a mix of code and text documents), I start to get all sorts of really bad result
s. Ex: 'What is so and so?' And it will return documents which do not mention 'so and so' at all 
* currently just doing
 vanilla \`similarity\` search 
* also, to clarify, for search, should I pick an embedder that ranks well among which of
 these tasks? Bitext mining, classification, clustering, pair classification, reranking, retrieval, STS, summarization. 
(ChatGPT tells me that they're all mostly relevant)
```
---

     
 
all -  [ Ollama max tokens parameter ](https://www.reddit.com/r/LangChain/comments/18i7v7j/ollama_max_tokens_parameter/) , 2023-12-16-0910
```
 Hello, I'm currently in the process of developing a chatbot utilizing Langchain and the Ollama (llama2 7b model). My ob
jective is to allow users to control the number of tokens generated by the language model (LLM).

In the Ollama document
ation, I came across the parameter 'num\_predict,' which seemingly serves this purpose. However, when using Ollama as a 
class from Langchain, I couldn't locate the same parameter. Consequently, I've been attempting to pass it as metadata. U
nfortunately, even when setting this parameter to a low value, such as 50, the LLM continues to generate more tokens tha
n expected.

I'm wondering if you have any insights on how I can effectively control the number of generated tokens when
 using Ollama as a Langchain class?

Thank you.

My current code

llm = Ollama(model='llama2:7b-chat-q4\_0',callback\_ma
nager=CallbackManager(\[StreamingStdOutCallbackHandler()\]),temperature=temperature,repeat\_penalty=1.19,top\_p=top\_p,r
epeat\_last\_n=-1,metadata={'num\_predict': num\_predict})

Thank you.

&#x200B;
```
---

     
 
all -  [ OpenAI using my own documents ](https://www.reddit.com/r/OpenAI/comments/18i7lp1/openai_using_my_own_documents/) , 2023-12-16-0910
```
&#x200B;

I'm trying to work out if OpenAI has matured to the point where it's now possible to reliably use it to analys
e my own documents. 

For each research project, I'll have maybe 100 documents in Word and PDF, ranging from a couple of
 pages to 150 pages for each document. I want to be able to use OpenAI to find text across these documents, and ideally 
also to help summarise or draw conclusions across the document portfolio. 

I want to avoid getting invented responses t
hat come from the training model, and to restrict answers to my document pool. 

I've seen privateGPT, localGPT, docalys
is, langchain. From quickly testing the sample of docalysis, it seems to answer queries on individual documents but not 
search across all documents in the portfolio?

I also have to say that I'm not a programmer, but I'm happy to throw myse
lf into something for a few days of setup if it's possible to get the results that I'm looking for at the end. 

So my q
uestion - are we there yet? Or the technology is still developing for this?

thank you! 
```
---

     
 
all -  [ LLM engages in a self-directed conversation before rendering the final response ](https://www.reddit.com/r/LangChain/comments/18i730v/llm_engages_in_a_selfdirected_conversation_before/) , 2023-12-16-0910
```
Hi there, I'm currently developing a chatbot using Langchain and the Ollama (llama2 7b model). I've observed that, at ti
mes, the model's responses include an indication of the role (Human/AI), and it seems to engage in a self-directed conve
rsation before rendering the final response. For greater clarity, I will attach an example. Additionally, I'll include m
y prompt template for reference.

Has anyone encountered this type of problem and found a solution?

* I'm using Convers
ationBufferWindowMemory

prompt\_template = PromptTemplate(input\_variables=\['system\_prompt', 'history', 'input'\],tem
plate='''<<SYS>>{system\_prompt}<</SYS>>###

Previous Conversation:'''{history}'''

\###

\[INST\] {input}

\[/INST\] ''
')

* I'm saving the history as follows:

st.session\_state\['memory'\].save\_context({'input': '\[INST\] ' + str(user\_
input)},{'output': '\[/INST\] ' +str(answer)})
```
---

     
 
all -  [ What is the simplest available local interface, to use openai or a local llm, with history and funct ](https://www.reddit.com/r/LocalLLaMA/comments/18i705v/what_is_the_simplest_available_local_interface_to/) , 2023-12-16-0910
```
Hello everyone, i'm nto super experienced in the world of llms, i wrote and run some code with langchain, but i lack a m
ore in depth understanding of it.  
I was searching the simplest way to set up a ui, with history that would be able wit
h the openai api first, and maybe when it's easier, with other opensource llms, to do function calling to do document or
 info retrival from documents, BUT  i wanted the retrival to be coded and run locally, with local documents and with a s
tructure i would write myself.

i was wondering if there were any already available projects to do so, seen that im not 
really happy with the retrival in gpt 4, i wanted to experiment more, but keep the function calling in the equation
```
---

     
 
all -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-16-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
all -  [ PGVector InvalidRequestError Issue ](https://www.reddit.com/r/LangChain/comments/18hxqk5/pgvector_invalidrequesterror_issue/) , 2023-12-16-0910
```
I'm currently exploring the PGVector library in Jupyter Notebook using the code snippet provided below:

`exisiting_inde
x_1 = PGVector(collection_name=COLLECTION_NAME_DOCS,connection_string=supabase_direct_db_connection_string,embedding_fun
ction=embeddings,`  `)`

Everything was running smoothly with version 0.0.347; however, upon testing versions beyond tha
t, I encountered the following error:

`This declarative base already contains a class with the same class name and modu
le name as langchain_community.vectorstores.pgvector.CollectionStore, and will be replaced in the string-lookup table. c
lass CollectionStore(BaseModel):InvalidRequestError: Table 'langchain_pg_collection' is already defined for this MetaDat
a instance. Specify 'extend_existing=True' to redefine options and columns on an existing Table object.`

&#x200B;

 Thi
s issue seems to arise specifically when re-running the same step in the Jupyter Notebook.  

Has anyone else encountere
d a similar issue and how did you solve it?
```
---

     
 
all -  [ RAG Reranking Model ](https://www.reddit.com/r/LangChain/comments/18houif/rag_reranking_model/) , 2023-12-16-0910
```
Hi,

I like the idea of reranking on RAG applications. 

However the most tutorials I see are using the Cohere Reranker 
Model, but I want to work fully open-source. 

So are there any methods/tutorials on which reranking techniques one can 
use that are open source AND multilingual (german support)?
```
---

     
 
all -  [ [Langchain] Recherche de similitude avec filtrage de méta-données ](https://www.reddit.com/r/redditenfrancais/comments/18hn0ju/langchain_recherche_de_similitude_avec_filtrage/) , 2023-12-16-0910
```
Salut,
Je cherche à peu près à faire ce que dit le titre. Je veux exécuter une recherche de similitude, mais je ne veux 
que l'exécuter sur une sous-section de mes données dont j'ai déjà également attribué des métas avant de l'intégrer. Tout
e idée / aide serait appréciée!

Traduit et reposté à partir de la publication 15a8605 de la communauté langchain
```
---

     
 
all -  [ Assistant api ](https://www.reddit.com/r/LangChain/comments/18hiq02/assistant_api/) , 2023-12-16-0910
```
What is your best alternative to replace assistant api ?
I used it and the cost is quite expensive.
What your favorite n
ocode tool?
Thank you
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/18hi864/for_hire_programmerweb_developerit_consultant/) , 2023-12-16-0910
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new technol
ogies that are needed for the project.

Rate is $50/h. Can also do fixed price by project, but only if the project/miles
tone is well-defined.

Satisfied customers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backe
nd_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how
_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.r
eddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testim
onials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/
v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Ple
ase note: I am **not** a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Resources that dramatically improved my prompting ](https://www.reddit.com/r/PromptEngineering/comments/18hhvi3/resources_that_dramatically_improved_my_prompting/) , 2023-12-16-0910
```
Here are some resources that helped me improve my prompting game. No more generic prompts for me!

**Threads & articles*
*

* [Aadit Sheth on Prompting](https://twitter.com/aaditsh/status/1654941500596273153) (thread)
* [Lyle AI on Prompting
](https://twitter.com/Lyle_AI/status/1701259924037312752) (thread)
* [Zain Kahn on Prompting](https://twitter.com/heykah
n/status/1723083113113272666) (thread)
* [Prompt Engineering: How to Think Like an AI](https://timbornholdt.com/blog/pro
mpt-engineering-how-to-think-like-an-ai) by Tim Bornholdt
* [Prompt Engineering Complete Guide](https://medium.com/@fare
edkhandev/prompt-engineering-complete-guide-2968776f0431) by Fareed Khan
* [Prompt Engineering Guide](https://towardsdat
ascience.com/prompt-engineering-guide-for-data-analysts-54f480ba4d98) by Olivia Tanuwidjaja
* [The Art of Prompt Enginee
ring: Decoding ChatGPT](https://www.kdnuggets.com/2023/06/art-prompt-engineering-decoding-chatgpt.html) by Josep Ferrer 
(KD Nuggets)
* [All You Need to Know About Prompt Engineering](https://pub.aimind.so/all-you-need-to-know-about-prompt-e
ngineering-9417e1079db) by DemoGPT

**Courses & prompt-alongs**

* [Prompt Engineering with GPT & LangChain](https://www
.datacamp.com/code-along/prompt-engineering-gpt-langchain) by Olivier Mertens from Microsoft on DataCamp  
**Disclosure*
*: I work for DataCamp. Including it since this series is free and useful for starting out. Would love the community’s f
eedback on how we can make them better!
* [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-
courses/chatgpt-prompt-engineering-for-developers/) on DeepLearning.AI
* [Learn Prompt Engineering – Full Course](https:
//www.freecodecamp.org/news/learn-prompt-engineering-full-course/) on FreeCodeCamp
* [Advanced Prompt Engineering](https
://learnprompting.org/courses/advanced-prompt-engineering) on LearnPrompting

**Videos**

* [Prompt Engineering Tutorial
 – Master ChatGPT and LLM Responses](https://youtu.be/_ZvnD73m40o?si=Sb_ZCJWdJxcegO7E)
* [I Discovered The Perfect ChatG
PT Prompt Formula](https://youtu.be/pmzZF2EnKaA?si=F_Kxnk1IFMCVRLVf)
* [Master the Perfect ChatGPT Prompt Formula (in ju
st 8 minutes)!](https://youtu.be/jC4v5AS4RIM?si=9w4M2Vdxm404G7Ki)
* [ChatGPT / GPT-4 System Prompt Engineering - Ultimat
e Guide](https://youtu.be/zNACfPuaqaI?si=Y_H2VZAWVtYyaPYI)

What resources should I add to the list? Please let me know 
in the comments.  

```
---

     
 
all -  [ Top resources for learning LangChain & the OpenAI API ](https://www.reddit.com/r/LangChain/comments/18hhagx/top_resources_for_learning_langchain_the_openai/) , 2023-12-16-0910
```
I’m looking to use the power of this sub to compile a list of resources for learning how to use the OpenAI API and Langc
hain. (Priority on recently released sources) Here’s what I’ve got so far:

**Tutorials**

* [A Gentle Intro to Chaining
 LLMs, Agents, and utils via LangChain](https://medium.com/towards-data-science/a-gentle-intro-to-chaining-llms-agents-a
nd-utils-via-langchain-16cd385fca81) by Dr. Varshita Sher (Older but great IMO)
* [LangChain AI Handbook](https://www.pi
necone.io/learn/series/langchain/) (Co-written by James Briggs who instructs 2 sessions on the DataCamp course linked be
low)
* [Beginner’s guide to OpenAI API](https://blog.streamlit.io/beginners-guide-to-openai-api/) by Chanin Nantasenamat

* [A Guide to the OpenAI API and What You Can Do With It](https://www.makeuseof.com/openai-api-guide-what-can-you-do/) 
by Idowu Omisola
* [Cracking Open the OpenAI (Python) API](https://towardsdatascience.com/cracking-open-the-openai-pytho
n-api-230e4cae7971) by Shawhin Talebi

**Online courses**

* [DataCamp ‘Become an AI Developer’ Code Along Series (free)
](https://www.datacamp.com/ai-code-alongs)   
**Disclosure:** I work for DataCamp. Including it since this series is fre
e and useful for starting out. Would love the community’s feedback on how we can make them better! 
* [Scrimba: Official
 LangChain.js Course](https://scrimba.com/learn/langchain)
* [LangChain for LLM Application Development](https://learn.d
eeplearning.ai/langchain)
* [OpenAI API Complete Guide: With Practical Examples in Python](https://www.udemy.com/course/
how-to-use-chatgpt-and-openai-api-for-developers/) (paid)
* [Free ChatGPT Course: Use The OpenAI API to Code 5 Projects]
(https://www.kdnuggets.com/2023/05/free-chatgpt-course-openai-api-code-5-projects.html)

**Videos**

* [Langchain tutori
als](https://www.youtube.com/playlist?list=PLpdmBGJ6ELUK-v0MK-t4wZmVEbxM5xk6L)
* [LangChain Explained in 13 Minutes | Qu
ickStart Tutorial for Beginners](https://youtu.be/aywZrzNaKjs?si=kqkvT-Os4LOY_bBG)
* [Chat with OpenAI in LangChain - #5
](https://youtu.be/CnAgB3A5OlU?si=G_b4akQxwX6LrSTb) (Again featuring James Briggs)
* [Using ChatGPT with YOUR OWN Data. 
This is magical. (LangChain OpenAI API)](https://youtu.be/9AXP7tCI9PI?feature=shared)
* [Langchain OpenAI Assistants API
 For Beginners 🦜️🔗 Function Calling made EASY! 🤯 (Full Tutorial)](https://youtu.be/cbOw4Gijppk?feature=shared)

What res
ources should I add to the list? Please let me know in the comments.

&#x200B;
```
---

     
 
all -  [ Local LLM chat agent with advanced RAG and memory ](https://www.reddit.com/r/LocalLLaMA/comments/18hgf17/local_llm_chat_agent_with_advanced_rag_and_memory/) , 2023-12-16-0910
```
I tried to implement the basic [Langchain RetrievalQA Chain](https://python.langchain.com/docs/use_cases/question_answer
ing/local_retrieval_qa) with a ChromaDB vector database containing 1 PDF File. I noticed 2 issues:

1. I were not able n
ot make a chat bot experience with a memory.
2. The vector database retriever for the LLM Chain takes the whole user pro
mpt as the query for the semantic similarity search. I would like to have the model decide when and how to query the vec
tor database.

I had a hard time finding information about how to make a local LLM Agent with advanced RAG and Memory. I
n my first approach I actually tried to create a Llama2 agent with Langchain Tools with one tool being the retriever for
 the vector database but I could not make Llama2 use them. It works with GPT-3.5 though. Having a local LLM use tools or
 function calling would make things much easier I think.

&#x200B;

Apart from Langchain, I am honestly overwhelmed by a
ll the frameworks and extras that could be incorporated into my little project:

* I shortly looked into [RAG with AutoG
en](https://microsoft.github.io/autogen/blog/2023/10/18/RetrieveChat/) and noticed it is mainly build for OpenAI GPT mod
els but found a [workaround with Oobabooga](https://babycmd.medium.com/local-llms-and-autogen-an-uprising-of-local-power
ed-agents-d472f2c3d0e3) for that.
* I found out that [Guardrails can do RAG](https://github.com/pinecone-io/examples/blo
b/master/learn/generation/chatbots/nemo-guardrails/03-rag-with-actions.ipynb) too and is used to censor the output of an
 LLM. It should also [work with local LLMs](https://blog.marvik.ai/2023/10/09/enhancing-llama2-conversations-with-nemo-g
uardrails-a-practical-guide/).
* Using [Cohere Reranker](https://python.langchain.com/docs/integrations/retrievers/coher
e-reranker) for improved retrieval.
* Fine Tuning on my data for better RAG results with something like [AutoTrain](http
s://huggingface.co/docs/autotrain/index).

I am a ML consultant for LLM topics and most of our customers have a high pri
ority on data privacy so OpenAI GPT is not an option for me. I now have 3 weeks vacation where I want to build something
 to learn more about LLMs. I would be happy about any input, advice, tutorials, opinions or recommendations where I shou
ld go next.

&#x200B;

**TL;DR:** I am overwhelmed by all the LLM frameworks and tools so I am unable to implement a loc
al LLM chat agent with advanced RAG and memory
```
---

     
 
all -  [ Are there templates or examples of Langchain workflows for software development? ](https://www.reddit.com/r/LangChain/comments/18he6le/are_there_templates_or_examples_of_langchain/) , 2023-12-16-0910
```
I am thinking:-

* Connect to database and map relationships with tables, columns, data types and options such as not nu
ll into an embedded vector store
* Read in existing code and again put into vector db, and note what database tables are
 used by the code and also create a high level functional summary
* Connect one or more LLMs for answering questions and
 code generation
* Store and retrieve project goals, and update them as they change or are completed
* Automate testing

* What have I missed?
```
---

     
 
all -  [ Langchain alternatives thread ](https://www.reddit.com/r/LangChain/comments/18hd5vo/langchain_alternatives_thread/) , 2023-12-16-0910
```
Hi all,  


I read in [a thread](https://www.reddit.com/r/LangChain/comments/18gih58/langchain_in_production/) about som
e frustrations in production and a few people chimed in with alternatives to LangChain that I wasn't aware of. I thought
 it would be good to have a thread detailing peoples experiences with those alternatives? 

I was using the LangChain py
thon library and got slightly bamboozled by the number of abstractions. I wanted to write *languag*e code in a way that 
felt like language, so I started working on my own framework for LLMs called [RobAi.](https://github.com/philmade/robai)
 If the idea can help anyone else reason about LLMs, then that's the goal. The framework is a very particular way to *th
ink* about working with LLMs more than a sophisticated and exhaustive codebase, but it does also work. The idea is its s
mall, flexible, expandable.  


Each object in the code is conceptualised as a robot with memory, the `Memory(BaseModel)
` object (pydantic) is always available and can contain whatever the robot needs to do its job. The robot calls all the 
functions registered in its '`pre-call`' list - imagine these as 'before I think' functions. Then the robot calls the AI
 model by passing whatever is in its `memory.instructions_for_ai` attribute as the prompt. So really you can imagine `pr
e-call` as 'all the things needed to make the prompt', which will always need to be set in whatever way you like at `mem
ory.instructions_for_ai`. It makes most sense to set the instructions for the AI (prompt) in the 'before I think' part o
f the code which is pre-call.  


After passing the instructions\_for\_ai to the AI model itself and getting a response 
back, the robot then calls all of its `'post-call'` functions - imagine these as functions to process the output and do 
whatever might be needed. If the robot is not explicitly stopped here, it will return back to `pre-call` and loop around
 in this pattern until it is stopped. It's up to you to decide when the robot is finished in its task. Perhaps it is nev
er finished.

I tested it with a few ideas and its relatively simple to make summary robots, agents, and functions with 
this way of thinking about LLMs. The advantage I've found is that its a little easier (for me) to reason about what is h
appening with each robot, and eventually its a little easier to reason about how to 'chain together' multiple robots.  



I'd be really interested in learning about other frameworks and the approaches that have been taken to working with th
ese language models. They're interesting and curious things to reason about, so what have you seen out there that has ma
de sense to you in how to work with them?
```
---

     
 
all -  [ I built 'The Broke Man's Plus NonSubscription' - a UI for the ChatGPT API [FREE] ](https://www.reddit.com/r/ChatGPTPro/comments/18hczz5/i_built_the_broke_mans_plus_nonsubscription_a_ui/) , 2023-12-16-0910
```
I really want to have the Plus Subscription features, but I dread to spend $19 a month for it.. so I decided to rebuild 
most features for my personal usage. See some gifs here.. 👇

[ChatGPT Vision Example](https://i.redd.it/vuk4s4by316c1.gi
f)

**What is implemented so far?**

* Voice Input (via Whisper API)
* Image input (ChatGPT Vision Model)
* Webbrowsing 
(using langchain)
* Google search (using DataForSEO)
* Python code execution (experimental)
* Bash execution (very exper
imental)
* Prompt libraries / custom tools
* Chat history

[Voice Input](https://i.redd.it/0mga1dt2416c1.gif)

I like Us
er Interfaces, so I did not want to use a terminal solution for this.  
But I am a nerd. I believe I am more efficient w
hen I can control everything via the keyboard. 

You can..

* summon the Chat Window in any application.
* change the mo
del, temperature (creativity), frequency and presence penalty on the fly
* copy one, multiple, or all markdown block(s) 
from the last message (nice for devs)
* display the last message in a text editor to easily copy chunks
* paste the last
 message into the active app
* copy the last message to the clipboard
* save the last / all messages into a file
* add /
 remove functions/plugins
*  all from the keyboard.

[The Chat Window](https://preview.redd.it/v9w2jwol416c1.jpg?width=2
694&format=pjpg&auto=webp&s=1823aec9ae66323efe9707acbbc9bce924f8f3fd)

**Create Custom Tools - Prompt Libraries with the
 certain flavor**

You can also create your own custom tools, that are like saved prompts, but you can trigger them with
 a keyboard shortcut and they can also execute code on top of it.

Need an example? Here you go: 

[Correct Text Tool: Y
ou select some text in any application and ChatGPT corrects it for you](https://i.redd.it/cn94o0wj416c1.gif)

Do you nee
d to remember all of the shortcuts for this? No, you can also just search them:

[Search for ChatGPT Tools](https://i.re
dd.it/r68rmoph416c1.gif)

Here are more example tools:

* **Correct Text:** Select text, hit my shortcut and let ChatGPT
 correct my louse grammar and spelling mistakes
* **Rephrase Text:** Rephrases the selected text in a specific format
* 
**Explain Like I'M 5:** Explains the selected text like I'm five years old.
* **Excuse My French:** Removes all profanit
ies of the selected text to be compatible for a work email.
* **Create Calendar Event:**  Let ChatGPT create calendar ev
ents for you in iCloud.

All of these are included, btw.

**Sounds nice?**   
You know what's nicer?  
You can have it f
or free.   
Get it here: [https://schmedu.com/tools/chatGpt](https://schmedu.com/tools/chatGpt)  
Use the code: GIVEITTO
MEBABY

**You are a dev and want to see the code?**  
You download the code and you can see it there. If you want to hav
e access to the GitHub repo, I can send you an invite (I am not making it public, yet).

**Are these features as good as
 the Plus Subscription?**   
I guess not, I have never used the Plus Subscription, so it's hard to tell. But this is als
o the 'Broke Man's Version of the Plus Subscription'.
```
---

     
 
all -  [ Document Based Large Language Model Recommendations ](https://www.reddit.com/r/LangChain/comments/18hbqa1/document_based_large_language_model/) , 2023-12-16-0910
```
Hello! I am trying to work with multiple documents and train/fine tune a model with the info from these files. I have tr
ied privateGPT and achieved mixed results since many of the answers it gave back were incorrect. Are there any better do
cument-based alternatives that I can locally run on my computer (Macbook Air M1 chip). Thanks!
```
---

     
 
all -  [ I made a Cloudflare Workers AI script for baai/bge-small-en-v1.5, alternative to OpenAI embeddings A ](https://www.reddit.com/r/LangChain/comments/18haz37/i_made_a_cloudflare_workers_ai_script_for/) , 2023-12-16-0910
```
A couple of days ago I asked about any alternatives to OpenAI embeddings + self hosted + managed. Many have shared vario
us services (Milvus, Pinecone, Weaviate) unfortunately these are managed Vector databases.

The closest reply that was i
ndeed in my consideration was AWS Lambda based hosting. I really liked that idea but I’m always afraid of Lambda overspe
nding.

In my case I’m already using Postgres + Pgvector and I don’t need an external managed service.

After a long con
sideration, I’ve created a Cloudflare Workers AI script, you can deploy it into your Cloudflare account and you’ll get a
n API url for it. There are free 100k daily worker requests, which works very well for me, until they finalised the pric
ings for it.

I’ve always been self-hosting thenlper/gte-small under a 1GB + 1vCPU DO droplet but the response time is 2
-7 seconds.

This new Cloudflare workers AI alternative works for me but I’ll need to switch all gte-small to bge-small 
soon.

Thanks for reading this, heres the script, hope y’all like it! https://gist.github.com/charlesteh/723f2daf51b0412
87e02b9f89c1e02c7
```
---

     
 
all -  [ What is the 'correct' way of serving a LLM as an API using FastAPI? ](https://www.reddit.com/r/LocalLLaMA/comments/18hakev/what_is_the_correct_way_of_serving_a_llm_as_an/) , 2023-12-16-0910
```
Hi, I've looked through some posts here and searched online. When it comes to deployment, there are many solutions and f
rameworks out there that offer a plethora of functionalities. 

However, what I need is pretty simple. I just want to se
rve a custom Langchain agent using open source models (GGUF). There will be some preprocessing and post-processing opera
tions to manipulate the input data and output response as well.

I am currently using FastAPI to serve the endpoint now.
 But I realized that if multiple users hit the endpoint at the same time, the queries are queued and users would need to
 wait for response. My main question is, is there a way to process the queries in parallel for quicker response time giv
en that I  only have the capacity to run one instance of the model?
```
---

     
 
all -  [ is it possible to add file to an existing openai assistant thread? ](https://www.reddit.com/r/OpenAI/comments/18h788z/is_it_possible_to_add_file_to_an_existing_openai/) , 2023-12-16-0910
```
I was reviewing this question -

How to upload a file into existing OpenAI assistant?

[https://stackoverflow.com/questi
ons/77512158/how-to-upload-a-file-into-existing-openai-assistant](https://stackoverflow.com/questions/77512158/how-to-up
load-a-file-into-existing-openai-assistant)

It shows how to attach to the whole assistant but i was looking to using an
 existing assistant and process a file i will give it as attachment to a thread.  


Also are there wrapper avavailable 
from langchain to provide this interface?

  
\----  
import pprint

from langchain.agents.openai\_assistant import Open
AIAssistantRunnable

ASSISTANT\_ID = 'xxxxx'  
agent = OpenAIAssistantRunnable(assistant\_id=ASSISTANT\_ID, as\_agent=Tr
ue)

response = agent.invoke({'content': 'answer my question'})  


pprint.pprint(response)  

```
---

     
 
all -  [ DeciLM-7B Instruct v Mistral-7B-Instruct-v01 on Chain of Thought ](https://www.reddit.com/r/LocalLLaMA/comments/18gxtey/decilm7b_instruct_v_mistral7binstructv01_on_chain/) , 2023-12-16-0910
```
**Note:** I finished this notebook yesterday before learning about the news Mistral model. I will re-run this with the n
ew Mistral instruct-tuned model later this week. If anyone from the community wants to re-run the notebook using the new
 Mistral model before then, please do. 

📘 Check the notebook out [here](https://colab.research.google.com/drive/1lW6aQW
77NDttBQ2Mk5M_OZrp-ZjIaFEt) 

#🧐 What I'm doing

Sampled 30 random rows from the [kaist-ai/CoT-Collection](https://huggi
ngface.co/datasets/kaist-ai/CoT-Collection). This dataset is 1M+ rows, so it was infeasible for me to use them all. I ch
ose 30 because, once upon a time, I was a clinical trials statistician, and 30 was always a magical number.

I then gene
rated responses for each prompt under a zero, one, and three-shot setting for DeciLM-7B-Instruct and Mistral-7B-v01.

##
 ⚖️ Evaluations

###LLM as Judge

I used LangChain string evaluators for the following, with GPT-4-Turbo as judge.

1. C
OT Evaluation (evaluate_cot): This grades answers to questions using chain of thought 'reasoning' based on a reference a
nswer. It will return one of the following evaluation results: CORRECT or INCORRECT evaluating whether the generation is
 correct, accurate, and factual.

2. Coherence Evaluation (evaluate_coherence): This gives a score between 1 and 10 to t
he generation, assessing whether it is coherent, well-structured, and organized based on a ground truth reference label.
 This is useful for assessing the quality of the generation's reasoning.

###Faithfulness in ragas

I also used the raga
s framework to measure faithfulness, which assesses how well a model's responses align with the given context or source 
material. This was also done using GPT-4-Turbo

#### 🤷🏽‍♂️Why did I do this?

Mostly because I'm curious and thought it 
would be a cool project. I also work at Deci, and I'm skeptical of benchmarks and wanted to see if our model was as good
 as we claim. 

All feedback is welcome, cheers!
```
---

     
 
all -  [ How can i preserve dictionary format through langchain agent for backend-frontend communication? ](https://www.reddit.com/r/LangChain/comments/18gw2v8/how_can_i_preserve_dictionary_format_through/) , 2023-12-16-0910
```
I posted this on the github QA as well, but i figured i would try my luck here too, so here goes.  


 

I'm developing 
a software application using the LangChain  framework, and I've encountered a challenge related to backend-frontend  com
munication in my application. The issue arises when I try to send a  dictionary containing a status code from my backend
 to the API layer,  which then forwards it to the frontend.

The specific workflow is this :

&#x200B;

1. My backend pe
rforms a search algorithm and generates a  response in the form of a dictionary. The dictionary contains a status  code 
and other relevant information. The purpose is to ask the frontend  user to confirm if the search results are correct.  

 
2. When this dictionary reaches a certain point in the tool  connected to the agent in the langchain framework, the a
gent is  interpreting the dictionary, and instead of forwarding it as is,  converts it to a string and sends the interpr
etation to the frontend.  
 

3.This is problematic because the conversion to string  strips away the essential state va
lues contained in the original  dictionary. These state values are imperative for the subsequent program  flow, especial
ly after receiving the confirmation from the frontend.

Is there a way to configure the agent or the tool to  bypass the
 interpretation step so i can ensure that the original  dictionary's format and data are preserved when i send it to the
  frontend?

Any insight or experiences would be hugely helpful and appreciated
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-16-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-16-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-16-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-16-0910
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

     
