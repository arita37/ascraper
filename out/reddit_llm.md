 
all -  [ Chat Assistant supporting the latest OpenAI API ](https://www.reddit.com/r/ChatGPTPro/comments/18k3i64/chat_assistant_supporting_the_latest_openai_api/) , 2023-12-17-0911
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

     
 
all -  [ Building AI-powered Applications w/ Javascript using Langchain JS for Beginners ](https://dev.to/oyemade/building-ai-powered-applications-w-javascript-using-langchain-js-for-beginners-388b) , 2023-12-17-0911
```

```
---

     
 
all -  [ Is a local-LLM assistant a realistic goal at this point? ](https://www.reddit.com/r/LocalLLaMA/comments/18jx1bl/is_a_localllm_assistant_a_realistic_goal_at_this/) , 2023-12-17-0911
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

     
 
all -  [ Need help to build a RAG application on legal data - vectorDB vs Knowledge graph ](https://www.reddit.com/r/LangChain/comments/18jug2b/need_help_to_build_a_rag_application_on_legal/) , 2023-12-17-0911
```
I need suggestion on this space. I need precise answers to certain questions related to a legal data. Vector databases s
eems to be bad on this, while knowledge graphs are good. But converting legal documents into knowledge graphs is pretty 
difficult and approximate.  How do I decide on this ? Should I use both ? Are there any exisiting tutorials on this ?
```
---

     
 
all -  [ Mixtral 8x7B Instruct hallucinates ](https://www.reddit.com/r/LangChain/comments/18ju44k/mixtral_8x7b_instruct_hallucinates/) , 2023-12-17-0911
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

     
 
all -  [ Best high level approach for creating custom gpts automatically ](https://www.reddit.com/r/LangChain/comments/18ju3fg/best_high_level_approach_for_creating_custom_gpts/) , 2023-12-17-0911
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

     
 
all -  [ Limiting results of product similarity search with chroma ](https://www.reddit.com/r/LangChain/comments/18joi9j/limiting_results_of_product_similarity_search/) , 2023-12-17-0911
```
I have a trained Mini LM to conduct embedding product searches like a normal e-commerce website search bar. The data is 
stored in a chroma database and currently, I'm searching it like this:

    raw_results = chroma_instance.similarity_sea
rch_with_score(
        query,
        k=100
    )

This works well in the sense that the best matching products nearly 
always have the highest scores. But I'm struggling to understand how I would dynamically limit the search results becaus
e in this case since k=100 it will always return 100 products even in the cases where only 5 products match the query an
d the other 95 products are not a match. 

I tried to create clusters in the results and experimented with returning the
 first and second clusters. This does not work reliably. In some cases, it improved the results but in other cases no cl
uster was found and all results were returned.

Is there a general way to solve this issue?
```
---

     
 
all -  [ Document Scoring Common Sense? But the 400 LangChain python boiler plate examples don't mention this ](https://www.reddit.com/r/aipromptprogramming/comments/18jlcu1/document_scoring_common_sense_but_the_400/) , 2023-12-17-0911
```
Document scoring using something like an Elasticsearch vector db for RAG retrieval. To help with relevance you can even 
throw in specific search params tied to the same index whatever you like. Multiple vectors if you choose, coordinates, e
tc… seems to help with accuracy anyone toying with this? You could even vary your prompt based on the score of the searc
h to further tailor the response.
```
---

     
 
all -  [ Looking to get help with selecting a vector database for my project. ](https://www.reddit.com/r/LangChain/comments/18jktn4/looking_to_get_help_with_selecting_a_vector/) , 2023-12-17-0911
```
I wish to build a Hockey team predictor.

Wish to store historical sport scores, stats, games, history inside a vector d
atabase.

Data for the sport scores, stats, and games will be from a returned JSON object.

&#x200B;

What vector databa
se would be best?  I would like it to be free to first build on and if it becomes scalable, then transfer to the cloud a
nd start paying for necessary fees.

Can I lets say install:

weaviate to local venv

use it with python and store/creat
e new vectors to hold the sports data.  The more the better.

If I installed weaviate to my local venv, that means I hav
e that data saved somewhere where I can export just in case?  Or transfer to cloud, etc.  How much space do vector db's 
take?

&#x200B;

Sorry for so many questions....any insight would be appreciated.
```
---

     
 
all -  [ Mixtral Settings ](https://www.reddit.com/r/LocalLLaMA/comments/18jawag/mixtral_settings/) , 2023-12-17-0911
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

     
 
all -  [ Deploy RAG APP on AWS/Huggingface ](https://www.reddit.com/r/LangChain/comments/18j84xi/deploy_rag_app_on_awshuggingface/) , 2023-12-17-0911
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

     
 
all -  [ Vectara OCR preview ](https://www.reddit.com/r/LangChain/comments/18j848d/vectara_ocr_preview/) , 2023-12-17-0911
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

     
 
all -  [ Best python library for OpenAI API? ](https://www.reddit.com/r/OpenAI/comments/18j7ucf/best_python_library_for_openai_api/) , 2023-12-17-0911
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

     
 
all -  [ [Langchain] ChromAdb Avantages? ](https://www.reddit.com/r/redditenfrancais/comments/18j72hd/langchain_chromadb_avantages/) , 2023-12-17-0911
```
Vous avez remarqué que peu de dépôts GitHub LLM utilisent ChromAdB au lieu de Milvus, tivent, etc. Un avantage particuli
er de l'utilisation de cette base de données vectorielle?

Traduit et reposté à partir de la publication 16s9vc5 de la c
ommunauté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Ml Questions] Comment fonctionne réellement la génération augmentée augmentée (RAG)? ](https://www.reddit.com/r/redditenfrancais/comments/18j6jqf/ml_questions_comment_fonctionne_réellement_la/) , 2023-12-17-0911
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

     
 
all -  [ AI Agents vs. ChatGPT Tools/Functions ](https://www.reddit.com/r/LangChain/comments/18j6i0f/ai_agents_vs_chatgpt_toolsfunctions/) , 2023-12-17-0911
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

     
 
all -  [ [Machine Learning] [D] Langchain vs Autogpt ](https://www.reddit.com/r/redditenfrancais/comments/18j4de4/machine_learning_d_langchain_vs_autogpt/) , 2023-12-17-0911
```
Je vois qu'il existe plusieurs bibliothèques concernant l'utilisation et le fintunage des LLM pour des tâches spécifique
s. Serait utile si quelqu'un pouvait expliquer la différence entre l'utilisation de Langchain, Autogpt et Babyagi?

Trad
uit et reposté à partir de la publication 12s2ldb de la communauté machinelearning. Pour retrouver la publication origin
ale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Conversational Memory with RAG ](https://www.reddit.com/r/LangChain/comments/18j3rti/conversational_memory_with_rag/) , 2023-12-17-0911
```
Do we have any chain that handle conversational memory with RAG like we ask two questions (Just for example)  
Who is Ob
ama?

When he was born?  


Do we have some functionality in langchain that handles the second question and pass updated
 question to similarity search i.e. When obama was born?
```
---

     
 
all -  [ Tokenizer of GGUF with LlamaCPP ](https://www.reddit.com/r/LocalLLaMA/comments/18j39l6/tokenizer_of_gguf_with_llamacpp/) , 2023-12-17-0911
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

     
 
all -  [ Trying to add context to dataframe agent ](https://www.reddit.com/r/LangChain/comments/18j2j5e/trying_to_add_context_to_dataframe_agent/) , 2023-12-17-0911
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

     
 
all -  [ [Langchain] Comment améliorer la qualité des réponses de chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/18j07cq/langchain_comment_améliorer_la_qualité_des/) , 2023-12-17-0911
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

     
 
all -  [ Created a AI Chatbot using OpenAI, Pinecone and LangChain ](https://www.reddit.com/gallery/18izww1) , 2023-12-17-0911
```
This chatbot can use you private database to provided personalized responses or can give responses through ChatGPT. Can 
integrate to any website. Can be customized according to the users preference.
```
---

     
 
all -  [ How to get same results for RAG when not using QA Retrieval Chain ](https://www.reddit.com/r/LangChain/comments/18ixnkm/how_to_get_same_results_for_rag_when_not_using_qa/) , 2023-12-17-0911
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

     
 
all -  [ Need some help with document uploads for GPT-4 integration ](https://www.reddit.com/r/ChatGPTPro/comments/18iwrf4/need_some_help_with_document_uploads_for_gpt4/) , 2023-12-17-0911
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

     
 
all -  [ Gave up on llama2 + langhlchain, a question about openai ](https://www.reddit.com/r/LangChain/comments/18it48v/gave_up_on_llama2_langhlchain_a_question_about/) , 2023-12-17-0911
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

     
 
all -  [ [Question] langchain? Assistant API? Custom GPT? Finetuning? ](https://www.reddit.com/r/OpenAIDev/comments/18ib6yz/question_langchain_assistant_api_custom_gpt/) , 2023-12-17-0911
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

     
 
all -  [ Better search with Chroma vector store? ](https://www.reddit.com/r/LangChain/comments/18i9hh8/better_search_with_chroma_vector_store/) , 2023-12-17-0911
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

     
 
all -  [ Ollama max tokens parameter ](https://www.reddit.com/r/LangChain/comments/18i7v7j/ollama_max_tokens_parameter/) , 2023-12-17-0911
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

     
 
all -  [ OpenAI using my own documents ](https://www.reddit.com/r/OpenAI/comments/18i7lp1/openai_using_my_own_documents/) , 2023-12-17-0911
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

     
 
all -  [ LLM engages in a self-directed conversation before rendering the final response ](https://www.reddit.com/r/LangChain/comments/18i730v/llm_engages_in_a_selfdirected_conversation_before/) , 2023-12-17-0911
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

     
 
all -  [ What is the simplest available local interface, to use openai or a local llm, with history and funct ](https://www.reddit.com/r/LocalLLaMA/comments/18i705v/what_is_the_simplest_available_local_interface_to/) , 2023-12-17-0911
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

     
 
all -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-17-0911
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
all -  [ PGVector InvalidRequestError Issue ](https://www.reddit.com/r/LangChain/comments/18hxqk5/pgvector_invalidrequesterror_issue/) , 2023-12-17-0911
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

     
 
all -  [ RAG Reranking Model ](https://www.reddit.com/r/LangChain/comments/18houif/rag_reranking_model/) , 2023-12-17-0911
```
Hi,

I like the idea of reranking on RAG applications. 

However the most tutorials I see are using the Cohere Reranker 
Model, but I want to work fully open-source. 

So are there any methods/tutorials on which reranking techniques one can 
use that are open source AND multilingual (german support)?
```
---

     
 
all -  [ [Langchain] Recherche de similitude avec filtrage de méta-données ](https://www.reddit.com/r/redditenfrancais/comments/18hn0ju/langchain_recherche_de_similitude_avec_filtrage/) , 2023-12-17-0911
```
Salut,
Je cherche à peu près à faire ce que dit le titre. Je veux exécuter une recherche de similitude, mais je ne veux 
que l'exécuter sur une sous-section de mes données dont j'ai déjà également attribué des métas avant de l'intégrer. Tout
e idée / aide serait appréciée!

Traduit et reposté à partir de la publication 15a8605 de la communauté langchain
```
---

     
 
all -  [ Assistant api ](https://www.reddit.com/r/LangChain/comments/18hiq02/assistant_api/) , 2023-12-17-0911
```
What is your best alternative to replace assistant api ?
I used it and the cost is quite expensive.
What your favorite n
ocode tool?
Thank you
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/18hi864/for_hire_programmerweb_developerit_consultant/) , 2023-12-17-0911
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

     
 
all -  [ Resources that dramatically improved my prompting ](https://www.reddit.com/r/PromptEngineering/comments/18hhvi3/resources_that_dramatically_improved_my_prompting/) , 2023-12-17-0911
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

     
 
all -  [ Top resources for learning LangChain & the OpenAI API ](https://www.reddit.com/r/LangChain/comments/18hhagx/top_resources_for_learning_langchain_the_openai/) , 2023-12-17-0911
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

     
 
all -  [ Local LLM chat agent with advanced RAG and memory ](https://www.reddit.com/r/LocalLLaMA/comments/18hgf17/local_llm_chat_agent_with_advanced_rag_and_memory/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-17-0911
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-17-0911
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-17-0911
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-17-0911
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

     
