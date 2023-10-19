 
all -  [ Streaming not working when routing between Runnables ](https://www.reddit.com/r/LangChain/comments/17b5gaw/streaming_not_working_when_routing_between/) , 2023-10-19-0910
```
I'm trying to stream the response with a simple route I've created among 2 Runnables without success. When I stream each
 Runnable independelty, it streams perfectly. When I create a route to choose which one of them should be the next step,
 it doesn't stream the result. Can someone provide some guidance?   


Here's the example:  


*# ----------------- Runn
able 1 -----------------*  


 DEFAULT\_DOCUMENT\_PROMPT = PromptTemplate.from\_template(*template*='{page\_content}')  

def \_combine\_documents(*docs*, *document\_prompt* = DEFAULT\_DOCUMENT\_PROMPT, *document\_separator*='\\n\\n'):  
 do
c\_strings = \[format\_document(doc, *document\_prompt*) *for* doc *in* *docs*\]  
 *return* *document\_separator*.join(
doc\_strings)  
def \_format\_chat\_history(*chat\_history*: List\[Tuple\]) -> str:  
 buffer = ''  
 *for* dialogue\_tu
rn *in* *chat\_history*:  
 human = 'Human: ' + dialogue\_turn\[0\]  
 ai = 'Assistant: ' + dialogue\_turn\[1\]  
 buffe
r += '\\n' + '\\n'.join(\[human, ai\])  
 *return* buffer  
\_inputs = RunnableMap({  
 'standalone\_question': {  
 'qu
estion': lambda *x*: *x*\['question'\],  
 'chat\_history': lambda *x*: \_format\_chat\_history(*x*\['chat\_history'\]) 
 
} | PromptFactory.CONDENSE\_QUESTION\_PROMPT | ChatOpenAI(*temperature*=0, *streaming*=True) | StrOutputParser(),  
})
  
\_context = {  
 'context': itemgetter('standalone\_question') | vector\_retriever | \_combine\_documents,  
 'questi
on': lambda *x*: *x*\['standalone\_question'\]  
}  
Runnable1 = \_inputs | \_context | PromptFactory.PROMPT | ChatOpenA
I(*temperature*=0, ***streaming*****=True**)  
***for*** **s** ***in*** **Runnable1.stream({'question': 'Hello!', 'chat\
_history': \[\]}):**  
 **print(s,** ***end*****='',** ***flush*****=True)**

**THIS STREAM WORKS**

*# ----------------
- Runnable 2 -----------------*

Runnable2 = RunnableMap({  
 'response': {  
 'question': lambda *x*: *x*\['question'\]
,  
 'chat\_history': lambda *x*: \_format\_chat\_history(*x*\['chat\_history'\]),  
 'context': lambda *x*: QueriesCont
ext.get\_result()  
} | PromptTemplate.from\_template(PromptFactory.followup\_context\_template) | ChatOpenAI(*temperatu
re*=0, ***streaming*****=True**) | StrOutputParser(),  
})  
***for s in*** **Runnable2*****.stream({'question': 'Hello!
', 'chat\_history': \[\], 'context': \['initialvalue'\]}):***  
***print(s, end='', flush=True)***

***THIS STREAM ALSO 
WORKS***  


def get\_result(*text*):  
 *return* \['newvalue'\]  
router\_chain = PromptTemplate.from\_template(PromptF
actory.router\_template\_test) | ChatOpenAI(*temperature*=0, *streaming*=True) | StrOutputParser()  
def **route**(*info
*):  
 *if* 'runnable1' in *info*\['topic'\].lower():  
 *return* **Runnable1**  
 *elif* 'runnable2' in *info*\['topic'
\].lower():  
 *return* **Runnable2**  
 *else*:  
 *raise* Exception('Invalid topic')  
*full\_runnable\_router\_chain*
 = {  
 'topic': router\_chain,  
 'question': lambda *x*: *x*\['question'\],  
 'chat\_history': lambda *x*: *x*\['chat
\_history'\],  
 'context': lambda *x*: *x*\['context'\]  
} | RunnableLambda(route)  
***for s in full\_runnable\_route
r\_chain.stream({'question': 'Hello!', 'chat\_history': \[\], 'context': \['initialvalue'\]}):***  
***print(s.content, 
end='', flush=True)***

***THIS DOESN'T STREAM***
```
---

     
 
all -  [ Generating code using langchain ](https://www.reddit.com/r/LangChain/comments/17b32k3/generating_code_using_langchain/) , 2023-10-19-0910
```
Hey fellow buds!
Sorry if it's too a dumb question but I am currently working on a code generator tool using langchain.

I have a set of questions(questionnaire), sample input format, sample output format and I want to use langchain/llm mode
ls to generate code that converts input format to output format.

What is the best way to do this with or without using 
langchain?

Thanks!
```
---

     
 
all -  [ Ask questions over documents process ](https://www.reddit.com/r/LangChain/comments/17b2i8k/ask_questions_over_documents_process/) , 2023-10-19-0910
```
If I follow this ([https://python.langchain.com/docs/use\_cases/question\_answering](https://python.langchain.com/docs/u
se_cases/question_answering/)) to ask questions over documents, are my documents sent to langchain or openai at any poin
t?  Or do they stay local on my machine?
```
---

     
 
all -  [ Hiring announcements / job ads? ](https://www.reddit.com/r/LangChain/comments/17b1if6/hiring_announcements_job_ads/) , 2023-10-19-0910
```
Are hiring announcements / job ads for LangChain and related roles allowed on this subreddit? 

Mods, perhaps you could 
create a pinned thread for companies seeking talent?
```
---

     
 
all -  [ Guess which subreddit these 3 images are from! #1792 ](https://www.reddit.com/gallery/17b1her) , 2023-10-19-0910
```

```
---

     
 
all -  [ Llama 2 7B 32K Instruct summarizes and outlines text... inconsistently ](https://www.reddit.com/r/LocalLLaMA/comments/17b0n8t/llama_2_7b_32k_instruct_summarizes_and_outlines/) , 2023-10-19-0910
```
Hi everyone,

I'm brand new to using LLMs. I have so far got two different models to produce valid, appropriate, coheren
t, 'intelligent' responses with llama.cpp and Langchain, including the long context Llama 2 7B 32K Instruct. I don't und
erstand why things work or not, and was hoping for pointers to higher level guidance.

Currently I'm working on getting 
Llama 2 7B 32K Instruct to receive a short (approx. 1500 word), highly abstract text (an encyclopedia article I wrote on
 a topic in the humanities) and produce either a one paragraph summary, an outline, a Markdown document that could be co
nverted into slides by Pandoc, and a limerick about the information. The prompts I used for each worked at least once. S
ometimes the same prompt (with the same settings) will simply produce a copy of the original text or part of the origina
l prompt.

I'm wondering where in the process this inconsistency emerges. 

Related to this is that in order to use the 
Instruct model I not only had to use the prompt format (using `[INST]` and `[/INST]`) but also add these as stop words t
o the LlamaCpp object parameters, because otherwise the model would apparently instruct itself and keep going on both re
lated and unrelated responses. Even just the opening tag was not sufficient to stop this kind of output. It would also t
hrow in end tags into responses and then continue on. I don't know whether or how this is related, except they are both 
examples of my general ignorance of the underlying process this software follows.

Any general comments or advice would 
be welcome 😁
```
---

     
 
all -  [ Resume Roast/Review. ](https://i.redd.it/vm124swr50vb1.jpg) , 2023-10-19-0910
```
Hey everyone, please go through this thoroughly and review or roast it. 
Even though I am a full time developer, I am us
ing this resume to apply for better jobs in Fullstack, Frontend or Backend.
But I am getting no responses. Please tell m
e whatever may be wrong with this resume or my skills or experience.
Thank you ☺️
```
---

     
 
all -  [ Models and apps built and deployed by software developers? ](https://www.reddit.com/r/datascience/comments/17atdtz/models_and_apps_built_and_deployed_by_software/) , 2023-10-19-0910
```
My company's really silo-ed and different teams run their own projects fairly independently, with very little regard for
 cross-functional collaboration esp if there are no obvious upsides for the team involved (broader corporate goals are u
sually brushed aside). The team overseeing products and CRM systems with software engineers builds and deploys a chatbot
 with RAG and Langchain using available automated tools and APIs, and the entire process doesnt include the data analyti
cs / DS team at all.  Is this normal? What's the point of having a DS team..
```
---

     
 
all -  [ [Local Llama] Quelqu'un a-t-il déjà un modèle pour Rag et Oobabooga API ](https://www.reddit.com/r/redditenfrancais/comments/17aqzqu/local_llama_quelquun_atil_déjà_un_modèle_pour_rag/) , 2023-10-19-0910
```
Par exemple. Utilisation de Langchain, Llamaindex ou leur propre Python

Traduit et reposté à partir de la publication h
ttps://www.reddit.com/16lq5b7
```
---

     
 
all -  [ LlamaCpp inference using AMD GPU ](https://www.reddit.com/r/LocalLLaMA/comments/17aou51/llamacpp_inference_using_amd_gpu/) , 2023-10-19-0910
```
Hi, I am working on a proof of concept that involves using quantized llama models (llamacpp) with [Langchain function](h
ttps://python.langchain.com/docs/integrations/llms/llamacpp)s. It has been working fine with both CPU or CUDA inference.
 However, I am wondering if it is now possible to utilize a AMD GPU for this process. This could potentially help me mak
e the most of my available hardware resources.  
Has anyone ever tried that?
```
---

     
 
all -  [ [Local Llama] Meilleur modèle à usage commercial? ](https://www.reddit.com/r/redditenfrancais/comments/17aoor8/local_llama_meilleur_modèle_à_usage_commercial/) , 2023-10-19-0910
```
Donc, j'ai passé un très bon moment jusqu'à présent avec vicuna 1.3 et exllama. A réussi à les faire fonctionner incroya
blement bien avec Langchain et Llama-Index. Je sais commencer à penser dans les applications logicielles potentielles et
 la licence restrictive de Llama est une nuisance.

Quel est le meilleur modèle pour une utilisation commerciale que vou
s avez trouvée? J'ai entendu de bonnes choses à propos de Falcon, mais je n'ai pas trouvé de versions quantifiées pour c
ela (si quelqu'un le sait, veuillez dire).

Traduit et reposté à partir de la publication https://www.reddit.com/14j5z7q

```
---

     
 
all -  [ [Langchain] Quelqu'un a été construit / bricolé d'un chatbot PDF? J'ai une question. ](https://www.reddit.com/r/redditenfrancais/comments/17aoke3/langchain_quelquun_a_été_construit_bricolé_dun/) , 2023-10-19-0910
```
Salut tout le monde,

Je construis une application où les utilisateurs peuvent télécharger des PDF et discuter avec eux.
 J'utilise Pinecone pour gérer les intérêts de ces PDF. Je me demande comment je devrais gérer les intérêts du PDF téléc
hargé de chaque utilisateur dans le backend de mon application, en considérant le concept d'index et espaces de noms de 
Pinecone.

Dois-je créer un index distinct pour chaque utilisateur ou un espace de noms distinct pour le PDF de chaque u
tilisateur? Quelle devrait être la relation entre eux et comment puis-je séparer entre plusieurs utilisateurs / PDF? Par
 exemple, si j'ai 1000 utilisateurs (chaque utilisateur peut télécharger plusieurs PDF), si je crée 1000 index (où chaqu
e index correspondait à un utilisateur, et un autre espace de noms peut être pour chacun de ses documents), ou un index 
ayant 1000 espaces de noms (un pour chaque utilisateur)?

Est-il possible d'y parvenir sans construire l'authentificatio
n en ce moment? J'apprécierais vraiment toutes les idées ou suggestions à ce sujet. Merci d'avance!

Traduit et reposté 
à partir de la publication https://www.reddit.com/12kqmwz
```
---

     
 
all -  [ Error while using ChatpromptTemplate (using LLama model ) ](https://www.reddit.com/r/LangChain/comments/17aloxd/error_while_using_chatprompttemplate_using_llama/) , 2023-10-19-0910
```
Hi, i'm using LLama2 model so getting error here   
Here is my code 

 

`from langchain.prompts.chat import (`  
 `Chat
PromptTemplate,`  
 `SystemMessagePromptTemplate,`  
 `HumanMessagePromptTemplate,`  
`)`  
 

`llm = LlamaCpp(`  
 `mod
el_path='models/llama-2-7b-chat.ggmlv3.q4_0.bin', callback_manager=callback_manager, verbose=True,n_ctx=4096, max_tokens
=1000, last_n_tokens_size=1000`  
`)`  


`template = 'You are an assistant that helps users find information about movi
es.'`  
`system_message_prompt = SystemMessagePromptTemplate.from_template(template)`  
`human_template = 'Find informat
ion about the movie {movie_title}.'`  
`human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)`
  
`chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])`  
`response = llm(cha
t_prompt.format_prompt(movie_title=str('Inception')).to_messages())`  
`print(response.content)`

&#x200B;

# This is th
e error

 **ValueError**    

 Traceback (most recent call last) **d:\\LLMs\\Langchain\\lang.ipynb Cell 42** line 1  11 
human\_message\_prompt = HumanMessagePromptTemplate.from\_template(human\_template)  13 chat\_prompt = ChatPromptTemplat
e.from\_messages(\[system\_message\_prompt, human\_message\_prompt\]) **---> 15** response = llm(chat\_prompt.format\_pr
ompt(movie\_title=str('Inception')).to\_messages())  17 print(response.content) 

 File **d:\\LLMs\\Langchain\\langch\_e
nv\\lib\\site-packages\\langchain\\llms\\base.py:332**, in BaseLLM.\_\_call\_\_**(self, prompt, stop, callbacks, \*\*kwa
rgs)**     

330 '''Check Cache and run the LLM on the given prompt and input.'''     331 if not isinstance(prompt, str)
: **--> 332** 

raise ValueError(     333 'Argument \`prompt\` is expected to be a string. Instead found '     334 f'{ty
pe(prompt)}. If you want to run the LLM on multiple prompts, use '     335 '\`generate\` instead.'     336     )     337
 return (     338 self.generate(\[prompt\], stop=stop, callbacks=callbacks, \*\*kwargs)     339 .generations\[0\]\[0\]  
   340 .text     341 )

  **ValueError**: Argument \`prompt\` is expected to be a string. Instead found <class 'list'>. 
If you want to run the LLM on multiple prompts, use \`generate\` instead. 

&#x200B;

  


&#x200B;
```
---

     
 
all -  [ LLM stands for … ](https://www.reddit.com/r/ArtificialInteligence/comments/17ak79q/llm_stands_for/) , 2023-10-19-0910
```
ChatGPT:
“””

Overview:

Imagine you have a big box of crayons and each crayon can draw a different type of picture. Now
, you want to draw a picture of a super cool robot like Jarvis from Iron Man. To do this, you’d pick crayons that can dr
aw parts of Jarvis and make them work together. In the big-kid world, these crayons are like different computer tools an
d programs. You want to use something called LangChain to make all these tools draw together. But to get the drawing to 
talk like Jarvis, you’ll need a special crayon that knows how to draw Jarvis’ voice.

Detailed Explanation:

Creating a 
comprehensive flow with LangChain to utilize Lifelong Learning Machines (LLMs) and other machine learning models is an a
mbitious task. To give your system a persona like Jarvis from Iron Man, you would need to focus on developing or obtaini
ng a Text-to-Speech (TTS) and Natural Language Generation (NLG) system that can mimic Jarvis’ tone, voice, and manner of
 speaking.

“””

Lifelong Learning Machines? 

Did I miss something ???

 🤣🧐🤷🏼‍♂️🤦🏼‍♂️
```
---

     
 
all -  [ SQLAgent exceeding max token for most join statements ](https://www.reddit.com/r/LangChain/comments/17aiaxw/sqlagent_exceeding_max_token_for_most_join/) , 2023-10-19-0910
```
I am trying to get the SQLAgent to be able to do queries on my database for more than just one table. For example, if I 
ask 'Give me a list of inventory for organization id: 13',  the langchain agent has to start joining tables, say an inve
ntory table to a store table to an organization table. It quickly exceeds the max tokens.  This is causing issue for the
 SQL Agent querying anything other than data only on 1 table.    


Also, If I have multiple organizations in my databas
e, I need to be able to strip out the data from the other orgs. 'If a user were to ask: 'Give me a list of my stores' I 
would need to have the agent also do 'Remove all store not connected to the users organization'.   


Is there any way t
o help the SQLAgent join tables better and strip out data based on a parentID?  
Would it need multiple DB instances wit
h just a single organizations data so that it doesnt need to strip out data?  
I dont really understand vector embedding
s, but would converting the db a vector store with instances make for faster querying?
```
---

     
 
all -  [ What to vector embed? ](https://www.reddit.com/r/LangChain/comments/17agsw2/what_to_vector_embed/) , 2023-10-19-0910
```
It seems a good amount of enterprise implementations are built using some form of RAG. What are some common use cases? S
ummarizing structured data, knowledge bot, providing insight/recommendations, etc? What are the most practical?
```
---

     
 
all -  [ Give a single model access to images and a text prompt? ](https://www.reddit.com/r/LangChain/comments/17adc8s/give_a_single_model_access_to_images_and_a_text/) , 2023-10-19-0910
```
I may be looking in the wrong place but how can I give a single model access to an image and a text prompt at the same t
ime?

For example, providing a picture of animals then asking the multi-modal llm what animals are in the picture.
```
---

     
 
all -  [ LangChain and Transformers ](https://www.reddit.com/r/ChatGPT/comments/17a8np8/langchain_and_transformers/) , 2023-10-19-0910
```
Hi frands, 

I am a software developer. I think I learned a lot by running examples of LangChain and transformers.js in 
a browser environment. (I run samples then checked network logs)

​​Do you have any interest in a new chat UI?

A web-ba
sed chat app that runs only client-side (100% privately).

I am thinking of creating a chat playground with LangChainAI.


LangChain has lots of features, and I believe I can implement many of them in my app.

I can easily add many tools to 
interact with Gmail, search, calendar, drive, etc., converting these tools into a marketplace like App Store. I can add 
plan and execute agents with them. I can also use AutoGPT and BabyAGI as an agent.

Chat integrations for Anthropic, Azu
re, OpenAI, Baidu, Bedrock, Ollama, etc.

Text embedding models to chat with your own docs and data. OpenAI, Ollama, Ten
sorFlow, Transformers.js.
```
---

     
 
all -  [ Reliable ways to get structured output from llms ](https://www.reddit.com/r/LocalLLaMA/comments/17a4zlf/reliable_ways_to_get_structured_output_from_llms/) , 2023-10-19-0910
```
What are the current best ways to get structured output from local llm/openai reliably ? I have found the following opti
ons and tried some of them,

Microsoft guidance - [https://github.com/guidance-ai/guidance](https://github.com/guidance-
ai/guidance)

LMQL - [https://lmql.ai/](https://lmql.ai/)

llama.cpp grammar - [https://github.com/ggerganov/llama.cpp/d
iscussions/2494](https://github.com/ggerganov/llama.cpp/discussions/2494)

langchain [https://python.langchain.com/docs/
modules/model\_io/output\_parsers/](https://python.langchain.com/docs/modules/model_io/output_parsers/)

jsonformer - [h
ttps://github.com/1rgs/jsonformer](https://github.com/1rgs/jsonformer)

salute - [https://github.com/LevanKvirkvelia/sal
ute](https://github.com/LevanKvirkvelia/salute)

outlines - [https://github.com/outlines-dev/outlines](https://github.co
m/outlines-dev/outlines)

Was looking for something that could work with both local llm’s (gguf/gptq models) and openai 
but i guess that’s difficult right now ? (also, i am more inclined towards typescript based solutions(zod) if possible)


I ran into a few problems for eg, guidance-ai doesn’t seem to work with text-generation ui because the openai api adapt
er doesn’t support logit\_bias.

It will be great to know the experience of others with these approaches.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, others as needed) ](https://www.reddit.com/r/forhire/comments/17a0q5k/for_hire_programmerweb_developerit_consultant/) , 2023-10-19-0910
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
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
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ LLama2 prompt template ](https://www.reddit.com/r/LangChain/comments/179zm9g/llama2_prompt_template/) , 2023-10-19-0910
```
Hi everyone,

I recently started to use langchain and ollama together to test Llama2 as a POC for a RAG system. 

Being 
in early stages my implementation of the whole system relied until now on basic templating (meaning only a system paragr
aph at the very start of the prompt with no delimiter symbols). And I do believe that changing this template to better s
uit the format intended by llama2 could at least bring more interesting outputs. For reference, I looked over this artic
le on HugginfFace that specifically goes over 'how to prompt llama2' ([https://huggingface.co/blog/llama2](https://huggi
ngface.co/blog/llama2)).

Leading to my question: have any of you tried to implement 'advance' prompt template such as t
he one used by llama2 and if so did you had to change significant portion of the existing prompt template (I'm worried a
bout the prefix required before the user input in the chat history)  and how did it turn out ?

&#x200B;
```
---

     
 
all -  [ Langchain + tabulur data on huggingface ](https://www.reddit.com/r/LangChain/comments/179xluu/langchain_tabulur_data_on_huggingface/) , 2023-10-19-0910
```
Is there any way to make langchain work with tabular data with huggingface models. There are lot of tutorials for how to
 make it work with OpenAiAPi, but not with other llms
```
---

     
 
all -  [ LangChain doc search is 👎 ](https://www.reddit.com/r/LangChain/comments/179xi52/langchain_doc_search_is/) , 2023-10-19-0910
```
I know we want to promote LLM support bots, but the search in the LangChain docs is super bad.

&#x200B;

**Mendable** '
can answer' questions with AI, but it miserably fails to index and search the docs, in contrast to good search products 
like Algolia.

&#x200B;

I am sure 99% of my queries would be resolved properly with Algolia but fail with Mendable
```
---

     
 
all -  [ How do i fine tune an LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/179w79k/how_do_i_fine_tune_an_llm/) , 2023-10-19-0910
```
I have a 24gb Card and i want to fine tune an llm on a dataset i created whats the best way?

And is it even possible

H
ere is my Dataset i want to use it for langchain:

[My Trainings Data](https://www.file-upload.net/download-15204875/tra
iningdata3.0.xlsx.html)

Source:

[https://huggingface.co/datasets/iamtarun/python\_code\_instructions\_18k\_alpaca](htt
ps://huggingface.co/datasets/iamtarun/python_code_instructions_18k_alpaca)(A Few Code Questions)

[https://huggingface.c
o/datasets/MadVoyager/stable\_diffusion\_instructional\_dataset](https://huggingface.co/datasets/MadVoyager/stable_diffu
sion_instructional_dataset)(Everything That has to do something with prompts and Picture generation)
```
---

     
 
all -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-19-0910
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
all -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-19-0910
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
all -  [ How your business can use OpenAI GPT ](https://www.reddit.com/r/LingoBlocks/comments/179vr7l/how_your_business_can_use_openai_gpt/) , 2023-10-19-0910
```
There’s many business use cases for a custom chat interface like ChatGPT, but using the company’s own internal content a
s the source. Think company policies, documents, project resources, etc.

I’ve been wrapping my head around, and buildin
g, GPT projects for the past 2 years (software dev of 7 years). Always learning, but what I’m sharing is basically the s
tandard approach to create a custom ChatGPT-like application that you can add your own data to.

If you know how to prog
ram, you could explore Open Source libraries like LangChain to handle processing of custom data. It’s a free program tha
t makes the process of interacting with different LLMs easier. Next you’ll want to connect it to a vector database to ma
ke the processed data available for referencing, and finally OpenAI’s API for the LLM generations (or your LLM of choice
).

Regardless of the solution you choose, how all this works from a technical perspective is:

1. You need to break up 
any large text content into smaller pieces. This process is called chunking. You do this to later make each chunk search
able in the vector database.
2. ⁠You’ll want to vectorize each chunk and add this vector into a database. By doing this,
 you can embed (vectorize) natural language to search the vector database for relevant chunks.
3. With the returned chun
ks, you can combine them all (within respects to the context window limit of the LLM of choice), and now your generated 
response will contain the information it needs to give you an accurate output.

Making a secure and privacy-focused solu
tion for businesses is also important. If you use the OpenAI API, data is not used to train their models (source [OpenAI
 Enterprise Privacy](https://openai.com/enterprise-privacy)).

I hope this makes sense. Let me know if there’s any quest
ions on the topic.
```
---

     
 
all -  [ How to fix 'libmagic is unavailable' error in Python ](https://www.reddit.com/r/LangChain/comments/179v9m5/how_to_fix_libmagic_is_unavailable_error_in_python/) , 2023-10-19-0910
```
 

I am getting the following error message when I try to run my Python code:

libmagic is unavailable but assists in fi
letype detection on file-like objects. Please consider installing libmagic for better results.

I have tried installing 
libmagic, but I am still getting the error message. I am using windows and Python 3.8. I installed it the same way as I 
have installed all my packages before and never run into any such errors.

Does anyone know how to solve this issue?
```
---

     
 
all -  [ Is GPT-4 getting faster? ](https://www.reddit.com/r/LangChain/comments/179pgnn/is_gpt4_getting_faster/) , 2023-10-19-0910
```
&#x200B;

https://preview.redd.it/clhg4ee5roub1.png?width=5000&format=png&auto=webp&s=5b7ddb30068e8e8e2fa9b6dc521e4c6351
3f3fed

Seeing that GPT-4 latencies for both regular requests and computationally intensive requests have more than halv
ed in the last 3 months.

Wrote up some notes on that here: [https://blog.portkey.ai/blog/gpt-4-is-getting-faster/](http
s://blog.portkey.ai/blog/gpt-4-is-getting-faster/)

Curious if others are seeing the same?
```
---

     
 
all -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-19-0910
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
all -  [ Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/GPT3/comments/179j4pw/exploring_methods_to_improve_text_chunking_in_rag/) , 2023-10-19-0910
```

Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunk
ing function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algor
ithms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out 
there, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising a
pproaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large 
Language Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embeddin
g) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've a
lso tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the
 query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a n
ot extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis 
and reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrap
ing to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to 
modify the text used to generate embeddings, while returning the original text after the recall phase. But this is still
 a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd app
reciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel ch
unking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking fo
r RAG here.

Thanks in advance for your time!
```
---

     
 
all -  [ Evaluating RAG on custom Q&As ](https://www.reddit.com/r/LangChain/comments/1798po2/evaluating_rag_on_custom_qas/) , 2023-10-19-0910
```
We are trying to get our feet wet with RAG with a small engineering team. I want to build a RAG system querying an exten
sive internal documents system. With the available choice of LLMs, embedding models, vector databases, hyperparameters i
t's easy to get overwhelmed. So what I want is to create a test dataset manually with like ten-twenty questions and answ
ers we would like to receive (or multiple answer options for each question??) and automate deployment of several combina
tions of different LLMs, hyperparameters, embedding models, etc and compare the actuals against the gold standard answer
s (using ROUGE score maybe??). Does that make sense? Are there any tools/frameworks I need to be aware of to do somethin
g like that for me? Thanks!
```
---

     
 
all -  [ Custom Hybrid Pinecone Retriever in Langchain ](https://www.reddit.com/r/LangChain/comments/17944ji/custom_hybrid_pinecone_retriever_in_langchain/) , 2023-10-19-0910
```
 I am trying to implement a hybrid pinecone retriever in my app. I used the PineconeHybridSearchRetriever from langchain
.retrievers, however it did not work, because it tried to pop 'context' from my vector metadata, so I had to customize i
t like so:

    class CustomPineconeHybridSearchRetriever(PineconeHybridSearchRetriever):
        def _get_relevant_docu
ments(
            self, query: str, *, run_manager: CallbackManagerForRetrieverRun
        ) -> List[Document]:
       
     from pinecone_text.hybrid import hybrid_convex_scale
    
            sparse_vec = self.sparse_encoder.encode_queri
es(query)
            # convert the question into a dense vector
            dense_vec = self.embeddings.embed_query(que
ry)
            # scale alpha with hybrid_scale
            dense_vec, sparse_vec = hybrid_convex_scale(dense_vec, spars
e_vec, self.alpha)
            sparse_vec['values'] = [float(s1) for s1 in sparse_vec['values']]
            # query pin
econe with the query parameters
            result = self.index.query(
                vector=dense_vec,
               
 sparse_vector=sparse_vec,
                top_k=self.top_k,
                include_metadata=True,
                name
space=self.namespace,
            )
            final_result = []
            for res in result['matches']:
            
    context = res['metadata'].pop('text')
                final_result.append(
                    Document(page_content
=context, metadata=res['metadata'])
                )
            # return search results as json
            print(fina
l_result)
            return final_result

The only thing that changed is now it pops 'text' instead of 'context'. This 
works, however when I try to put it in a chain, the chain does not receive the information correctly. I call the chain l
ike this:

    h_retriever = CustomPineconeHybridSearchRetriever(
        embeddings=embed, sparse_encoder=sparse_encode
r, index=index
    )
    
    # retrieval qa chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_
type='stuff',
        # retriever=vectorstore.as_retriever(),
        retriever=hh_retriever,
        
    )

Does anybo
dy know how to fix this? I assume it has to be something with the custom class. Thank you in advance.
```
---

     
 
all -  [ Date initiale in conversatii cu LLMuri ](https://www.reddit.com/r/programare/comments/1793bga/date_initiale_in_conversatii_cu_llmuri/) , 2023-10-19-0910
```
Avand in vedere ca chatgpt nu are acces la documentatii mai noi de 2022, ma intreb cum sa fac conversatii custom prin ap
i-ul openai cu modelul gpt4. Am descarcat si curatat toata documentatia de la libraria langchain si am pus-o intr-un fol
der local. Acum as vrea sa embed (sau ceva) toata documentatia la gpt4 si apoi sa-i pun intrebari despre cum sa folosesc
 uratenia asta de langchain mai bine :D

**Voi cum ati face / ati facut?** 
Ce solutii exista (nu ma intereseaza limbaju
l de programare)? 
Cum o fi pretul la embeddings openai pe langa altele gen pinecone sau supabase local (care de fapt e 
moca)?

Pana acum dadeam copy paste in fereastra chatgpt cu partea din documentatie care ma interesa mai mult, sau si ma
i bine cu vreun tutorial intreg, dar acum mi s-a cam infundat si trebuie sa up my game putin.

Update: Am pornit gresit 
cu langchain, trebuia s-o iau cu LlamaIndex direct - e mai simplu si posibil mai bun pentru taskul meu.
```
---

     
 
all -  [ Streaming with conversational retrieval chain ](https://i.redd.it/20qq9p63siub1.jpg) , 2023-10-19-0910
```
This stream is happening with Chat OpenAI, but when I'm using conversational retrieval chain, it's not streaming. How to
 fix it?
```
---

     
 
all -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/learnmachinelearning/comments/178zuks/free_courses_to_learn_about_large_language_models/) , 2023-10-19-0910
```
[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global community for LLM practitioners.

[**
LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm-ap
plication-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 

[*
*Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buildin
g LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students will l
earn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as gain 
hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai/co
urses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explore D
eep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25/):
 In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're app
lied in different fields. 
```
---

     
 
all -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-19-0910
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
 
all -  [ Which model+size for a websearch agent? ](https://www.reddit.com/r/LocalLLaMA/comments/178ztct/which_modelsize_for_a_websearch_agent/) , 2023-10-19-0910
```
I've been playing around with an agent framework ([www.griptape.ai](https://www.griptape.ai)). Like Langchain you can cr
eate an agent with tools and I've been experimenting with its websearch tool. The LLM uses ReAct prompting to decide if 
it should use the websearch tool and then it generates json formatted string with the query action in it. 

Surprisingly
, [https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca) does okay
 but as the conversation progresses it stops reaching out the to websearch tool. gpt-4 nails it ( had to test) but gpt-3
.5-turbo,  not so much. 

I was wondering if anyone else had searched over models to use with tool selection (doesn't ha
ve to be websearch) and found smaller models that that performed consistently? 

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Streaming in Langchain ](https://www.reddit.com/r/LangChain/comments/178zgv0/streaming_in_langchain/) , 2023-10-19-0910
```
I want to know is it possible to stream tokens in conversational retrieval chain ,and rather than printing it to console
 I want to send it via api
```
---

     
 
all -  [ OpenAI Functions vs Langchain ReAct Agents ](https://www.reddit.com/r/LangChain/comments/178lhnc/openai_functions_vs_langchain_react_agents/) , 2023-10-19-0910
```
What is the real difference and tradeoffs when choosing to use ChatGPT Functions instead of the ReAct agents from Langch
ain? What am I missing out on?

My current view is that using functions saves tokens, is faster, and is easier to create
 without the abstraction layer LangChain introduces, and that the tradeoff is not being able to customize how the model 
chooses which tool(function) to use. However, i'm a bit confused about what the best practice for creating Agents that c
an do multiple retrieval things, such as QA with semantic search, search in a SQL database, use the web, and generally r
etrieving new and personal data. I know langchain has its own agent that uses ChatGPT functions, but I found that abstra
ction harder to grasp than just the openai implementation itself.
```
---

     
 
all -  [ Issues with Streaming API Responses to Frontend on AWS using Vercel's AI SDK ](https://www.reddit.com/r/nextjs/comments/178kojc/issues_with_streaming_api_responses_to_frontend/) , 2023-10-19-0910
```
I am currently working on a project where I use Vercel's AI SDK to stream API responses to the frontend of my applicatio
n. Everything works perfectly when I run the application locally, however, **I encounter problems when deploying it on A
WS(Amplify)**. I get the response but it is not streamed.

I am using NextJs + Langchain starter template. 

[https://sd
k.vercel.ai/docs](https://sdk.vercel.ai/docs)

Below is the code I have for my API route and UI:

**API route**

    imp
ort { StreamingTextResponse, LangChainStream, Message } from 'ai';
    import { ChatOpenAI } from 'langchain/chat_models
/openai';
    import { AIMessage, HumanMessage } from 'langchain/schema';
    
    export const runtime = 'edge';
    
 
   export async function POST(req: Request) {
      const { messages } = await req.json();
    
      const { stream, ha
ndlers } = LangChainStream();
    
      const llm = new ChatOpenAI({
        streaming: true,
      });
    
      llm

        .call(
          (messages as Message[]).map(m =>
            m.role == 'user'
              ? new HumanMessage(
m.content)
              : new AIMessage(m.content),
          ),
          {},
          [handlers],
        )
        
.catch(console.error);
    
      return new StreamingTextResponse(stream);
    }

**Frontend**

    'use client';
    

    import { useChat } from 'ai/react';
    
    export default function Chat() {
      const { messages, input, handleI
nputChange, handleSubmit } = useChat();
    
      return (
        <div className='mx-auto w-full max-w-md py-24 flex f
lex-col stretch'>
          {messages.length > 0
            ? messages.map(m => (
                <div key={m.id} class
Name='whitespace-pre-wrap'>
                  {m.role === 'user' ? 'User: ' : 'AI: '}
                  {m.content}
    
            </div>
              ))
            : null}
    
          <form onSubmit={handleSubmit}>
            <input

              className='fixed w-full max-w-md bottom-0 border border-gray-300 rounded mb-8 shadow-xl p-2'
            
  value={input}
              placeholder='Say something...'
              onChange={handleInputChange}
            />
 
         </form>
        </div>
      );
    }

&#x200B;
```
---

     
 
all -  [ How to create a custom agent with structured tools? ](https://www.reddit.com/r/LangChain/comments/178jvg2/how_to_create_a_custom_agent_with_structured_tools/) , 2023-10-19-0910
```
I have seen multiple examples of using Langchain agents Structured tools accepting multiple inputs using **AgentType.STR
UCTURED\_CHAT\_ZERO\_SHOT\_REACT\_DESCRIPTION**. As per [Langchain blog post](https://blog.langchain.dev/structured-tool
s/), this is only agent type that can support Multi-input tools. I have not seen any documentation or example of creatin
g a custom Agent which can use multi-input tools.

My use case may require a different prompt, rules, output parser, and
 that way I want to format scratchpad. Have you developed any similar use case or come across any useful guide?
```
---

     
 
all -  [ Vector Databases... Confusion arises. How do I use them in practice? ](https://www.reddit.com/r/LangChain/comments/178dzf3/vector_databases_confusion_arises_how_do_i_use/) , 2023-10-19-0910
```
I have tried to wrap my head around vector dbs for the past weak, I understand the benefits of them. But I can't seem to
 understand how to use them.

There are sooooooo many vector db services... Some questions about these:
1. Can services 
like Pinecone and Vectara both create and store vector embeddings for you?
2. How do I create embeddings otherwise? Open
Ai has an API for this, do I really need to use their service or can embeddings be created locally?

And there are also 
some locally run vector dbs available, such as weaviate, Milvus and the Jina AI vectordb (https://github.com/jina-ai/vec
tordb?ref=jina-ai-gmbh.ghost.io). Questions about these:
1. Do they require powerful GPUs/CPUs?
2. VectorDB from Jina AI
 seems like a simple and good starting point for me, so that I can get a better understanding of how to work with vectoe
 dbs and embeddings. But their documentation is limited, and I don't really understand if it is capable of creating the 
vector embeddings. Has anyone any experience with this tool?

As is clear, I am somewhat confused about vector dbs. Any 
insights on the questions above are much appreciated.
```
---

     
 
all -  [ Per ogni categoria che vi sovviente, quali sono gli standards industriali nel mondo nello sviluppo w ](https://www.reddit.com/r/ItalyInformatica/comments/178djpy/per_ogni_categoria_che_vi_sovviente_quali_sono/) , 2023-10-19-0910
```
Ritengo che la risposta per antonomasia sia sempre 'dipende', ma che per una ragione o per l'altra (incluso il becero sc
immiottamento delle big) oggi ci si è assestati su diverse tecnologie perché sì, ma mi chiedevo quali potessero essere s
econdo voi le suddette, ad esempio: siamo ancora fissi sulle RESTful o ha vinto GraphQL? C'è posto per i WebSockets?  
C
hi sta vincendo tra il qualsiasi NoSql del populismo ed il popolare Postgresql?  
I linguaggi funzionali stanno davvero 
partendo al contrattacco?  
Che altre opzioni a parte il non-da-produzione Langchain per mettere facilmente in pista app
 basate su LLM?  
Qual è il SO di punta nell'era dei container?  
Quali sono gli strumenti per l'orchestrazione e trasfo
rmazione dei dati? Jenkins campa ancora?   


Ma soprattutto, perché? Non prendiamoci in giro, ognuno ha i suoi bias, ma
 almeno si riesce a dare forma al perché si pensano e dicono determinate cose?

  
Bonus: Ci dobbiamo arrendere al fatto
 che verrà quasi tutto pythonizzato democraticamente perché il settore pullula di minus habens da Udemy e scriptini del 
cazzo, incapaci di vedere oltre il loro naso?  


P.S. ho deviato un po' dal proposito del titolo, ma giusto perché pens
o sarebbe interessante mettere in prospettiva, ex: oggi abbiamo Ruby con il suo OOP ma magari sta davvero tirando le cuo
ia e domani ci potrebbe essere Elixir col suo FP (... Ispirato a Ruby!)
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-19-0910
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-19-0910
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-19-0910
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-19-0910
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-19-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-19-0910
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
