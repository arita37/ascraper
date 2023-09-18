 
all -  [ Share you success and horror LangChain in Production stories ](https://www.reddit.com/r/LangChain/comments/16lfju8/share_you_success_and_horror_langchain_in/) , 2023-09-18-0909
```
Been working on a recommender PoC that’s customer facing for large org. Evaluating whether to stick with LangChain going
 forward and would love to hear your success and horror stories of LangChain in production serving high volume requests.
 Stick with LangChain, another framework, or roll your own?
```
---

     
 
all -  [ What are people using the OpenAI APIs for? ](https://www.reddit.com/r/OpenAI/comments/16le9sb/what_are_people_using_the_openai_apis_for/) , 2023-09-18-0909
```
It seems everyone is head down coding on open-ended tools / infra like langchain, vector DBs, or even ChatGPT itself.

I
’m curious, how are businesses using LLMs? It seems for 99% of use cases building a smaller, focused model would be the 
best way to solve a real business problem.
```
---

     
 
all -  [ Can I get a LangSmith Invite Code ](https://www.reddit.com/r/LangChain/comments/16l9npt/can_i_get_a_langsmith_invite_code/) , 2023-09-18-0909
```
Guys I am terribly lost in the logs of my Custom Agent and I need to try this Langchain at least to see how bad the situ
ation is. Is it possible to send me an invite code? Been on the waitlist for ages :/
```
---

     
 
all -  [ wanna join the building of open source AI interfaces? github.com/apssouza22/chatflow ](https://v.redd.it/ci5gxsd87vob1) , 2023-09-18-0909
```

```
---

     
 
all -  [ Question about creating embeddings using a database ](https://www.reddit.com/r/LangChain/comments/16l4pbk/question_about_creating_embeddings_using_a/) , 2023-09-18-0909
```
Hello,

I am using postgres and have two tables I would like to use:  
1. places table - e.g. attractions around the wor
ld  
2. large reviews table (millions) - what people say about those attractions (with relation to a place using an ID)


I would like AI to be able to answer questions about those attractions, as well as possibly provide recommendations. I 
thought to use pgvector as I am using postgres (but open for alternatives). I would like to know what is the best way to
 approach it.

Should I create embeddings per review (e.g. a vector field per review)? Do you maybe have an example? Las
tly, since the data is not required to be 'live' (but I would like to get answers quickly) would it be better to train t
he AI instead of context injections? Any tops are welcome.

Thanks
```
---

     
 
all -  [ From API batch to streaming changes the pipeline, how to handle? ](https://www.reddit.com/r/LangChain/comments/16l34xd/from_api_batch_to_streaming_changes_the_pipeline/) , 2023-09-18-0909
```
Hey,

Working on using an LLM for a recommendation use case, let's say it's to list top n cars according to some custome
r criteria.

&#x200B;

The pipeline is simple - prompt with some input variables (customer requirements) and constraints
 (e.g. only from certain brands), with an output parser for text to JSON.

&#x200B;

Using FastAPI as the backend, withi
n which Langchain is used to orchestrate, the full completion where OpenAI gpt-3.5-turbo in streaming=False mode, was ta
king around 20 seconds to complete. When complete, I render the top cars, each as a card, on the UI.  The high latency i
s not a great user experience.

&#x200B;

I've updated FastAPI and model to work in streaming mode, but this now present
s me with a dilemma. In batch mode the chain was working as follows: 1) prompt asking the model to generate the complete
 top n list of cars, then 2) output parsing (pydantic model of car card). As I want to start feeding recommended cars ba
ck to the UI as soon as they become available, I'm wondering how best to re-engineer, i.e. as soon as I get a recommenda
tion, parse text of car description including model and brand to JSON, and serve to UI. 

&#x200B;

Ideally I wanted the
 FastAPI layer to handle everything (recommendation and output parsing), and not fall back to the FastAPI only getting t
he recommendation and the UI having to transform the text stream to JSON-based car cards as the text comes in. 

&#x200B
;

Hope I've explained the challenge OK. Any thoughts & ideas very much welcome, thanks!
```
---

     
 
all -  [ To deep dive and be good with LLMs you need a complex Langchain project behind you...... ](https://www.reddit.com/r/LangChain/comments/16l2u62/to_deep_dive_and_be_good_with_llms_you_need_a/) , 2023-09-18-0909
```
Hey,

As per title, I read a post sometime ago that stated to be good with, and deep dive into LLMs, you need to have ta
ckled a 'complex' Langchain project.  Which of course got me thinking about the definition of complex.

Would love to ha
ve some thoughts on what that means to you? Would it require a combination of multi-modal / multi-lingual / chunking / f
ine-tuning / vector db / agents & tools / short and long term memory management?

Intrigued about the perspectives on th
is from the community, thanks.
```
---

     
 
all -  [ Langchain Chatgpt Interactive survey. ](https://www.reddit.com/r/LangChain/comments/16l271i/langchain_chatgpt_interactive_survey/) , 2023-09-18-0909
```
Basically, I am trying to build the multiuser langchain chatbot. I am using pgvector to store embeddings. With page_cont
ent i have a json object stored in metadata ( basically a survey) that i  want a user to fill out interactively. For exa
mple my user asks some question and answer is provided with suggestion that there is a survey linked to this content wou
ld you like to fill this survey? And if user agrees it would start asking questions one by one and in the end it generat
es json object of the filled survey.
```
---

     
 
all -  [ Exe files created using pyinstaller are always larger than I expected, what am I doing wrong? ](https://www.reddit.com/r/learnpython/comments/16kxnga/exe_files_created_using_pyinstaller_are_always/) , 2023-09-18-0909
```
Whenever I use pyinstaller to create a portable exe, using pyinstaller --onefile -script.py nothing fancy, the result is
 always bigger than I expected. A simple web scraping script using Selenium can be as large as 80mb. 

Recently I made a
 portable program for PrivateGPT, a private LLMs, and the program alone is 1.5GB. This is not including the actual LLM i
tself. I investigated and it seems like pyinstaller decide that I need the whole torch library (800MB) to run the script
. I'm skeptical of that. I don't even use torch in my script. Seems like some part of torch is needed to support langcha
in library but I'm not sure about the whole thing. 

All in all, I wonder if just using  'pyinstaller --onefile' is fine
 or not? What are some common tricks/options to use with pyinstaller?
```
---

     
 
all -  [ Recommendations for open-source LLM models ](https://www.reddit.com/r/LangChain/comments/16kjre0/recommendations_for_opensource_llm_models/) , 2023-09-18-0909
```
Hello everyone, I've always used OpenAI models, but I'd like to start exploring the open-source world, and indeed, for c
ertain tasks, there are some strong competitors. In your experience, what are the best models for:

1. Embedding
2. Zero
-shot classification
3. Question answering (extraction)

Thank you.
```
---

     
 
all -  [ LangChain Archeticture to simulate ChatDev. ](https://www.reddit.com/r/LangChain/comments/16k765e/langchain_archeticture_to_simulate_chatdev/) , 2023-09-18-0909
```
I have been intrigued with the ChatDev, but want to use it in a local environment   and use different models for differe
nt characters. Has anyone taken a stab as mixing them up? What similar types of software accomplish the same objectives,
 but don't require an open AI key?
```
---

     
 
all -  [ Best Program and Model to read local pdf or epub with GPTQ model ](https://www.reddit.com/r/LangChain/comments/16k6dbg/best_program_and_model_to_read_local_pdf_or_epub/) , 2023-09-18-0909
```
hi, i want to read, search and resume my personnal pdf, docx or epub document localy on my computer.

**what model and p
rogram do you advice ?**

for the moment i test :  
Programm : H2oGPT, chatdocs and privategpt  
Models : vicuna uncenso
red, Nous-Yarn-Llama-2-13b-128k 	

thanks  

```
---

     
 
all -  [ Horde-Client v1.0.2 is out today! ](https://www.reddit.com/r/LocalLLaMA/comments/16k1j31/hordeclient_v102_is_out_today/) , 2023-09-18-0909
```
Few days back, I shared my project [horde-client](https://pypi.org/project/horde-client/). For those who missed the post
, this is a Python Client library for KoboldAI project that lets you remotely interact with crowdsourced/private LLM ser
vices. 

I got some great feedback in the last post and have incorporated majority of them in the new release. 

So toda
y, I am announcing v1.0.2  version of project with cool new features:

1. Horde-Client now supports [LangChain](https://
horde-client.readthedocs.io/en/latest/02_langchain.html) integration. You can easily swap out LLMs from your LangChain p
ipeline and use Horde-Client's LLM.
2. Official Documentation is now available at [https://horde-client.readthedocs.io/]
(https://horde-client.readthedocs.io/)
3. [Async](https://horde-client.readthedocs.io/en/latest/03_asyncclient.html) sup
port is now available for Horde-Client.

You can head over to [Quickstart](https://horde-client.readthedocs.io/en/latest
/01_quickstart.html) to start using Horde-Client for your projects.

Feel free to share any feedbacks, this will help im
prove the project for the community.
```
---

     
 
all -  [ GPTQ models with Langchain ](https://www.reddit.com/r/LangChain/comments/16jzm6r/gptq_models_with_langchain/) , 2023-09-18-0909
```
I am trying to use GPTQ models via Langchain. I am creating a huggingface pipeline object and passing that as the LLM in
stead of OpenAI. 

However, when I try to query CSV/dataframes with this, the speed is abysmally slow and the code gets 
stuck. The same model works fine when I use it for normal text generation outside Langchain. 

What is the best way to i
nteract with CSVs/Dataframes with my own model? If anyone has experience debugging, what is the best way to proceed next
?
```
---

     
 
all -  [ LLM for textbooks, feasible ? ](https://www.reddit.com/r/learnmachinelearning/comments/16jlt3n/llm_for_textbooks_feasible/) , 2023-09-18-0909
```
I want to build a webapp SAAS that allows you to chat with an AI tutor about  specific textbook. Some of these textbooks
 are in English and others are Arabic, conceptual , no equations or anything.
I couldn't find anything like this. Im a t
otal noob with AI. but I think it can be made using langchain and openai api , can it ?
```
---

     
 
all -  [ Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/LocalLLaMA/comments/16jl53m/agents_an_opensource_framework_for_autonomous/) , 2023-09-18-0909
```
I hope this paper is also interesting this community!

Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2
309.07870) 

Github: [https://github.com/aiwaves-cn/agents](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent a
dvances on large language models (LLMs) enable researchers and developers to build autonomous language agents that can a
utomatically solve various tasks and **interact with environments, humans, and other agents** using natural language int
erfaces. **We consider language agents as a promising direction towards artificial general intelligence** and release Ag
ents, an **open-source library** with the goal of opening up these advances to a wider non-specialist audience. Agents i
s carefully engineered to support important **features including planning, memory,  tool usage, multi-agent communicatio
n, and fine-grained symbolic  control.** Agents is **user-friendly** as it **enables non-specialists** to build, customi
ze, test, tune, and deploy state-of-the-art **autonomous language agents without much coding**. The **library** is also 
**research-friendly as its modularized design** makes it **easily extensible for researchers.** 

https://preview.redd.i
t/ne8fsj05rgob1.jpg?width=1131&format=pjpg&auto=webp&s=076a3551bddb817351d9865809923a6bdf840cb1

https://preview.redd.it
/u4x4hm05rgob1.jpg?width=1656&format=pjpg&auto=webp&s=2ca813790719b1f6f285e67ca92834e02d12c40c

&#x200B;

&#x200B;
```
---

     
 
all -  [ Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/agi/comments/16jl4rw/agents_an_opensource_framework_for_autonomous/) , 2023-09-18-0909
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/impiu2f5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
032644106e6ccebda499680560c2e8016485e1b1

https://preview.redd.it/2w5i64f5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=0
3a9f64546c4240654837fd3bbf577b13632f31f

&#x200B;
```
---

     
 
all -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-09-18-0909
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
all -  [ Easiest way to launch & experiment with a langchain powered Python app via chat interface ](https://www.reddit.com/r/LangChain/comments/16jhi3e/easiest_way_to_launch_experiment_with_a_langchain/) , 2023-09-18-0909
```
I'm building an agent and I want to be able to interact with it easily. I've been thinking WhatsApp or Jupyter notebooks
 are the easiest way to start, but feels like there's probably some canonical solution folks are using?  


All I'm look
ing for is some experience where I can provide a chat API and it'll handle frontend chat experience for interaction.
```
---

     
 
all -  [ How much preprocessing are you doing for RAG QA chatbots w/ documents? ](https://www.reddit.com/r/LocalLLaMA/comments/16jde4z/how_much_preprocessing_are_you_doing_for_rag_qa/) , 2023-09-18-0909
```
I know there is a ton of interest in document QA systems, which makes sense since it has good business values to most or
ganizations.

I'm wondering for those of you who found the answers from you QA systems to be good, did you guys just dro
p the PDF / Word / etc... into the program and let the RecursiveCharacterSplitter in langchain do the work, or did you g
uys do some preprocessing before you chunked it up and loaded into the vector db.  
I am trying to do QA on a PDF of a t
extbook. I wrote some scripts to 'chunk' the textbook so each chunk also contains it's associated Title and Subheading. 


&#x200B;

Let's say we are in Chapter: Carbon-Carbon Bonds. Below is an example passage:  


Grignard Reaction:

The g
rignard reaction is very lit. Only the most based can perform it. Blah Blah Blah

Blah Blah BlahBlah Blah BlahBlah Blah 
BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah

Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBl
ah Blah Blah

Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah  


I would then crea
te chunks from this passage like this:

&#x200B;

Carbon-Carbon Bonds

Grignard Reaction

The grignard reaction is very 
lit. Only the most based can perform it. Blah Blah Blah

Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Bl
ah BlahBlah Blah Blah

\-------------------------------------------------------

Carbon-Carbon Bonds

Grignard Reaction


Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah

Blah Blah BlahBlah Blah BlahBlah 
Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah  


Then I embed the chunks. The idea is that including the title an
d header will make have a higher similarity score.

Has anyone found it necessary to perform this type of chunking? Anyo
ne getting great results with easier methods?  


  


  


&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Leveraging code generation tools for LangChain based project ](https://www.reddit.com/r/LangChain/comments/16jarl3/leveraging_code_generation_tools_for_langchain/) , 2023-09-18-0909
```
Hi !

I am looking to leverage the code generation features of LLM to create up-to-date apps. Currently, if I try to dev
elop a minor script utilizing the LangChain library through ChatGPT, it is unfeasible given its existing knowledge base 
(Sep 21).

How would you go about ensuring that the generated code using any library aligns with the most recent documen
tation? Someone was mentioning Claude, and to feed him with the documentation. 

Any other suggestions? Especially for d
evelopers in Europe ;)

Thanks !
```
---

     
 
all -  [ Need help for Langchain Agents with memories ](https://www.reddit.com/r/LangChain/comments/16j7w5w/need_help_for_langchain_agents_with_memories/) , 2023-09-18-0909
```
Here is the detailed description of my issue, can anyone help me.

https://github.com/langchain-ai/langchain/discussions
/10568
```
---

     
 
all -  [ Laptop freezing on running embedding and vectorstore ](https://www.reddit.com/r/LangChain/comments/16j75vv/laptop_freezing_on_running_embedding_and/) , 2023-09-18-0909
```
My laptop has i7 16 core processor and yet it freezes midway between running the program i'm following. Also the vectors
tore never loads. I have tried FAISS and Chroma

Here's the code below:

 

import streamlit as st  
from dotenv import 
load\_dotenv  
from PyPDF2 import PdfReader  
from langchain.text\_splitter import CharacterTextSplitter  
from langchai
n.embeddings import HuggingFaceInstructEmbeddings  
from langchain.vectorstores import FAISS  
from langchain.chat\_mode
ls import ChatOpenAI  
from langchain.memory import ConversationBufferMemory  
from langchain.chains import Conversation
alRetrievalChain  
from htmlTemplates import css, bot\_template, user\_template  
from langchain.llms import HuggingFace
Hub  


def get\_pdf\_text(pdf\_docs):  
 text = ''  
 for pdf in pdf\_docs:  
 pdf\_reader = PdfReader(pdf)  
 for page
 in pdf\_reader.pages:  
 text += page.extract\_text()  
 return text  


def get\_text\_chunks(text):  
 text\_splitter
 = CharacterTextSplitter(  
 separator='\\n',  
 chunk\_size=1000,  
 chunk\_overlap=200,  
 length\_function=len  
)  

 chunks = text\_splitter.split\_text(text)  
 return chunks  
def get\_vectorstore(text\_chunks):  
 embeddings = Huggin
gFaceInstructEmbeddings(model\_name='hkunlp/instructor-xl')  
 vectorstore = FAISS.from\_texts(texts=text\_chunks, embed
ding=embeddings)  
 st.write('3')  
 return vectorstore  


def main():  
 load\_dotenv()  
 st.set\_page\_config(page\_
title='Chat with your documents', page\_icon=':books:')  
 st.header('Chat with your documents :books:')  
 st.text\_inp
ut('Ask a question about your documents:')  
 with st.sidebar:  
 st.subheader('Your documents')  
 pdf\_docs=st.file\_u
ploader('Upload your PDFs here and click on 'Process'', accept\_multiple\_files=True)  
 if st.button('Process'):  
 wit
h st.spinner('Processing'):  
 \#get info from pdfs  
 raw\_text=get\_pdf\_text(pdf\_docs)  
   
 \#get text chunks  
 t
ext\_chunks = get\_text\_chunks(raw\_text)  
 st.write('workin')  
 \#create vector database  
 vectorstore = get\_vecto
rstore(text\_chunks)  
 st.write('4')  
   


if \_\_name\_\_ == '\_\_main\_\_':  
 main()

&#x200B;

I have been follow
ing this tutorial: [https://www.youtube.com/watch?v=dXxQ0LR-3Hg&t=8s](https://www.youtube.com/watch?v=dXxQ0LR-3Hg&t=8s)
```
---

     
 
all -  [ Some questions of implementing LLM to generate Q/A pairs based on local documents ](https://www.reddit.com/r/LocalLLaMA/comments/16j624z/some_questions_of_implementing_llm_to_generate_qa/) , 2023-09-18-0909
```
Recently, I have been paying around about how to implement chat-based Q/A using the LLM model based on a local knowledge
 base. 

I have experimented with the following two open-source frameworks. 

[Llama\_index](https://github.com/jerryjli
u/llama_index)

[Langchain-chatchat](https://github.com/chatchat-space/Langchain-Chatchat)

  
I believe these 2 framewo
rks are built upon what everyone refers to as the RAG (Retrieval-Augmented Generation) approach. Without altering the em
beddings and LLM, it allows for generating responses based on one's own knowledge base. 

Thanks for the author's excell
ent work, I have indeed been able to achieve my requirements to some extent. However, the output results still seem to h
ave some deviations and even mistakes. 

&#x200B;

[the work flow of chatchat](https://preview.redd.it/2mud4ayp5dob1.png
?width=834&format=png&auto=webp&s=cc598844a4d4462a8fc80383a1ce0e946828e157)

Is there a way to make the output results m
ore accurate? 

For example,  I have a user manual for the hairdryer in knowledge base showing the hair dryer is working
 under rated voltage of 110V,  when I use the LLM model with a relatively low sample size I may get a wrong answer. 

If
 I ask, 'Can I use the xxx hair dryer directly in a country with a rated voltage of 220V?' 

Llama2-7B may answers 'yes,
 you can.' 

while Llama2-13B may answer me 'no, unless you use a power adapter'. 

And GPT is capable of providing more
 excellent answers. 

I believe that if I want to achieve better output results, I may need to fine-tune the LLM or embe
ddings. 

But I've noticed that many people use Q/A pairs for fine-tuning, and I'm not sure why they do this or whether 
these operations involve fine-tuning embeddings or the LLM. In my understanding, we don't have sufficient resources for 
fine-tuning the LLM, and fine-tuning embeddings seems to only help in improving how embeddings convert human language in
to higher relevance vectors. Does this mean that when fine-tuning embeddings, there's actually no need for question-answ
er pairs? 

If I must fine-tune, should I separately fine-tune two embeddings: one fine-tuned based on question-answer p
airs for extracting vectors from documents and another fine-tuned based on question similarity for extracting vectors fr
om questions? 

&#x200B;
```
---

     
 
all -  [ Generative AI product called Needle ](https://www.reddit.com/r/LangChain/comments/16j3ppz/generative_ai_product_called_needle/) , 2023-09-18-0909
```
Hey Guys,
I am working in a product name Needle. Here are some features of it:
1. Q&A on documents (pdf, word, text, ppt
 etc.)
2. Q&A on MS Sql database (based on schema, prepare sql statement and execute it)
3. Integration with AirByte to 
support other thousands of connectors
3. Integration in your application directly: Embed as chat, API Integration
4. Cho
ose your LLM (openai, azure openai etc)
5. Host it privately and securely (export docker to your repository)

I am using
 Langchain as base framework and above things doesn’t need prompt modification or fine tuning.

How should i expand this
 product, ranging from feature expansion, marketing, reaching out to potential customers?
```
---

     
 
all -  [ Multi-Text Summarization/Question Answering ](https://www.reddit.com/r/LangChain/comments/16j2evy/multitext_summarizationquestion_answering/) , 2023-09-18-0909
```
I have a use case that uses meeting notes stored in SalesForce. I've written a function that produces a text block for e
ach meeting, which contains the meeting metadata and the meeting notes. I'd like to be able to send batches of these (co
uld be up to \~50) to an an open-source LLM (thinking LLaMa2) and prompt it to get summarizations/insights across them, 
for example:

* What were the main 5 topics that were discussed in the meetings this month?
* What questions were we ask
ed in the meetings?

What would be the best way to approach such a task? The batch of notes would be larger than the all
owable context window for most LLMs, and RAG seems more like fetching data rather than synthesizing across multiple diff
erent documents.

Somewhat new to all this, appreciate any insights!
```
---

     
 
all -  [ How to improve Chat with your own data application answer quality? ](https://www.reddit.com/r/ChatGPTCoding/comments/16j1x4c/how_to_improve_chat_with_your_own_data/) , 2023-09-18-0909
```
Hi, I have been working on my chat with your own data application for a while. I have seen most of the chat with your ow
n data tutorials on youtube, and medium articles on this topic. Majority of them just teaches you the basic mechanics of
 how to get a basic skeleton of such application working: 

1. using some form of langchain to ingest your data to a vec
tor db
2. using similarity search the vector db to return relevant documents to the question the user asks
3. set the re
turned docs from the previous step as context to the prompt you send to chatgpt api, get your answer and display the res
ult in your frontend.

Different tutorials may have a different focus on the approach, e.g. not using langchain, using l
angchain directly, using no-code UI built on top of langchain, using no-code UI built on framework similar to or modifie
d versions of langchain...

But the matter of fact is, while the output of following these tutorial kind of work, but th
ey don't live up to closer inspection. Especially if you try to put them to real world use cases, where you really try t
o use it to chat with a document or code base you really try to understand. The answers on these real world documents re
ally fall short of what you hope the AI can do. 

Anyone here have similar experience want to discuss on what can be don
e to improve on the quality of answers produced by these LLM Q&A applications? 

Looking forward to hearing your thought
s on this problem.

Thanks
```
---

     
 
all -  [ Need help processing your data before embedding it? ](https://www.reddit.com/r/LangChain/comments/16iv7v9/need_help_processing_your_data_before_embedding_it/) , 2023-09-18-0909
```
Hey,  


We just published a playground to help developers test out different pre-processing configurations for their da
ta. This includes loaders, selectors and splitters. It uses parts of Langchain as well as some custom loaders and splitt
ers built by Neum AI. (All open source) Feel free to try it out here: [https://neumai-playground.streamlit.app/](https:/
/neumai-playground.streamlit.app/)

If you want to see an overview, check out this video: [https://www.youtube.com/watch
?v=n3L680vmGJo&t=5s](https://www.youtube.com/watch?v=n3L680vmGJo&t=5s)  


Repo:  [NeumTry/pre-processing-playground (gi
thub.com)](https://github.com/NeumTry/pre-processing-playground)   


What else would you like to be able to do in the p
layground?   

```
---

     
 
all -  [ Using LangChain to generate ROS (Robotic Operating System) ](https://www.reddit.com/r/LangChain/comments/16iv2j1/using_langchain_to_generate_ros_robotic_operating/) , 2023-09-18-0909
```
Me and my team at RoboCoach Inc. have used LangChain and GPT3.5 to capture the details of a robotic design and to automa
tically implement all ROS (Robot Operating System) packages for the robotic project. This is the tool:

[https://github.
com/RoboCoachTechnologies/ROScribe](https://github.com/RoboCoachTechnologies/ROScribe)

Demo: [https://www.youtube.com/w
atch?v=H2QaeelkReU](https://www.youtube.com/watch?v=H2QaeelkReU)

ROScribe is an open source project and we welcome all 
of you to use it and be part of this community. If you liked the tool, you can send us a video recording of your use-cas
e and we will put it on our github. We will credit all contributors at every release.
```
---

     
 
all -  [ Using GPT and LangChain to build robotic projects ](https://www.reddit.com/r/ChatGPT/comments/16iv0vr/using_gpt_and_langchain_to_build_robotic_projects/) , 2023-09-18-0909
```
Me and my team have used LangChain and GPT3.5 to capture the details of a robotic design and to automatically implement 
all ROS (Robot Operating System) packages for the robotic project. This is the tool:

[https://github.com/RoboCoachTechn
ologies/ROScribe](https://github.com/RoboCoachTechnologies/ROScribe)

Demo: [https://www.youtube.com/watch?v=H2QaeelkReU
](https://www.youtube.com/watch?v=H2QaeelkReU)

ROScribe is an open source project and we welcome all of you to use it a
nd be part of this community. If you liked the tool, you can send us a video recording of your use-case and we will put 
it on our github. We will credit all contributors at every release.  
```
---

     
 
all -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-09-18-0909
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
all -  [ Step-by-step tutorial on creating your own Notion chatbot using LangChain, OpenAI GPT, FAISS and Str ](https://www.reddit.com/r/LangChain/comments/16ite4d/stepbystep_tutorial_on_creating_your_own_notion/) , 2023-09-18-0909
```
&#x200B;

https://i.redd.it/srbnmwfd9aob1.gif

If you have ever wanted to chat directly with your own Notion data, right
 in Notion, have a look at this step-by-step tutorial on how to do it, using LangChain, OpenAI GPT, and Streamlit! 💪

It
's now live on the Streamlit: [https://blog.streamlit.io/build-your-own-notion-chatbot/](https://blog.streamlit.io/build
-your-own-notion-chatbot/)

Let me know what you think!
```
---

     
 
all -  [ Build your own Notion chatbot using Streamlit, LangChain and OpenAI ](https://www.reddit.com/r/StreamlitOfficial/comments/16itah3/build_your_own_notion_chatbot_using_streamlit/) , 2023-09-18-0909
```
&#x200B;

https://i.redd.it/3rzmszvq8aob1.gif

If you have ever wanted to chat directly with your own Notion data, right
 in Notion, follow my step-by-step tutorial on how to do it, using LangChain, OpenAI GPT, and Streamlit! 💪

It's now liv
e on the Streamlit: [https://blog.streamlit.io/build-your-own-notion-chatbot/](https://blog.streamlit.io/build-your-own-
notion-chatbot/)

Let me know what you think!
```
---

     
 
all -  [ [Hiring] ($20-40/hr) Experienced LangChain Developers ](https://www.reddit.com/r/forhire/comments/16ipz4a/hiring_2040hr_experienced_langchain_developers/) , 2023-09-18-0909
```
**NOTE:** No agencies and please answer each question below

**Preface**: I work on different AI projects using Langchai
n and could use some help. Please only apply if you have worked with Langchain. Go ahead and message me the answers to t
he below questions and Ill get back shortly.

**Questions:**

1. How much experience with Python and/or Javascript?
2. T
ell me about your experience with Langchain/GPT applications
3. Do you have experience with web application development?

4. Please provide your LinkedIn and resumeThanks!
```
---

     
 
all -  [ [Hiring] ($20-40/hr) Experienced LangChain Developers ](https://www.reddit.com/r/forhire/comments/16ipz47/hiring_2040hr_experienced_langchain_developers/) , 2023-09-18-0909
```
**NOTE:** No agencies and please answer each question below

**Preface:** I have some different AI projects using OpenAI
 and could use some help. Please only apply if you have worked with Langchain. Go ahead and message me the answers to th
e below questions and Ill get back shortly.

**Questions:**

1. How much experience with Python and/or Javascript?
2. Te
ll me about your experience with Langchain/GPT applications
3. Do you have experience with web application development?

4. Please provide your LinkedIn and resumeThanks!
```
---

     
 
all -  [ I created my first ever side project - A gpt4 based document editor that generates text and images ](https://www.reddit.com/r/nextjs/comments/16ipk1h/i_created_my_first_ever_side_project_a_gpt4_based/) , 2023-09-18-0909
```
Hi Everyone,

As someone with a fulltime job and not that great coding skills its been difficult to ever get out a worki
ng side project. I recently joined buildspace season 4 - a 6 week online building challenge - and finally managed to get
 this over the line. Only have a handful of users and not really sure if this product is super useful so would love to h
ave some feedback.

**What is it:** A very simple and easy to use AI document editor that uses GPT-4 to generate text an
d images. The text generated is based off your previous text and documents so theoritcally it should be in your own voic
e.

**The idea behind it:** I wanted to start to reimagine documents and what they can be used for. Right now my project
 is only really useful for writing related tasks, but my idea in the beginning was to always include AI agents somehow t
o make documents 'alive' and complete tasks for you while youre away. If you're interested in that kind of stuff do foll
ow my journey to continue building this on twitter ([www.twitter.com/thetansen](https://www.twitter.com/thetansen)).

**
The tech:** Its using nextJs 13 but still using the pages directory as I've built this off of Vercels Platforms template
 which you can find here ([https://vercel.com/templates/next.js/platforms-starter-kit](https://vercel.com/templates/next
.js/platforms-starter-kit)), so it became a bit of a mismatch. For calling gpt4 im using langchain to call gpt-4  and pi
necone as my vector db to hold all the document data to pass in.For the text editor I'm using editorJS.

&#x200B;

**Che
ck it out here:**  [www.typenotes.ai](https://www.typenotes.ai)
```
---

     
 
all -  [ Chat with your database ](https://www.gettingstarted.ai/tutorial-on-how-to-convert-natural-language-text-to-sql-using-langchain/) , 2023-09-18-0909
```
Hey 👋 I just published a post about converting natural language to SQL using LangChain:

I’d love to read your comments 
and feedback!

(For the pros out there, if there are technical or content improvements pls share!)
```
---

     
 
all -  [ Searching for chunking algorithms and repo ](https://www.reddit.com/r/LangChain/comments/16in3e6/searching_for_chunking_algorithms_and_repo/) , 2023-09-18-0909
```
Hi everyone! 

I'm still experiencing with my own implementation of rag, and I deployed my custom chunking function (hon
estly don't like the methods on LangChain) . 

Anyway, I'm searching for alternative methods, algoritms (NLP or not) and
 models... There are lots of info and different implementation on RAG, but as I can see noone put much effort to augment
 chunking quality. 

Also, there are other approach than this one I'm currently using? bi-encoder (instructor) - > cross
-encoder (reranking) - > LLM 


Can someone share some resources, repo, lib or existing implementation of different chun
king methods? 
(or simply discuss here some idea, though or approach) 

*Thanks in advance for you time!!*
```
---

     
 
all -  [ The rollercoaster journey behind launching the HelpKit AI Notion Chatbot ](https://www.reddit.com/r/SaaS/comments/16imj0g/the_rollercoaster_journey_behind_launching_the/) , 2023-09-18-0909
```
Hey folks!

Today I want to talk with you about the journey behind launching HelpKit AI. It wasn't a smooth sailing! 

H
elpKit is a solo founded and fully bootstrapped SaaS tool that turns your Notion docs into a professional help center an
d documentation site.

Since HelpKit is already hosting hundreds of customers Notion knowledge bases it only made sense 
to supercharge them with a custom AI trained chatbot. So far the results have been amazing.

And now, we just finally [l
aunched today on Product Hunt](https://www.producthunt.com/posts/helpkit-ai) as well! The public beta is out since two w
eeks and we have onboarded more than 15 customers on the add-on and the AI bot held 2000+ successful conversations.The l
aunch was planned two months ago but some things stopped me from releasing it.

If you are curious about the background,
 here it is. Let me explain why the journey to the launch was a bit rougher than expected. There were two big issues: Th
e UX and building on top of AI.

&#x200B;

**The UX Hurdle**

First and foremost, I was stuck with developing a great us
er experience. I have only come across a handful of products that were sort of implementing the same concept and I reall
y did not like their UX implementation. Everything felt clunky and just did not fit into the concept of an AI enabled kn
owledge base system.

You see our AI chatbot needs to be integrated into HelpKit’s two layouts: Help Center and Document
ation and also work well on the widget and mobile.Quite a tricky task to get right everywhere! I brainstormed for a few 
days, tried out some implementations but none of them felt natural for a user in my opinion.

I even spent a whole week 
building an interface only to then throw away the entire feature code branch and start from scratch.What I needed was a 
break. So I took a weekend break, spent some time at the beach and came back refreshed with some new ideas (that strange
ly all came to me during my Sunday evening shower).

I realised that the most intuitive way to present the option to cha
t with an AI powered chatbot assistant is when the user is already searching for something. So this way, should our norm
al search not be able to deliver an instant search result, users can be “catched” and still have their problem resolved 
by the AI.

In terms of the UI, I decided to go with a slick right sidebar interface for the chatbot on the help center 
layout and a nicely integrated chat window within the search command bar of the documentation layout. Within the HelpKit
 embeddable widget as well as on mobile phones, HelpKit AI will show a full-screen chatbot interface to the user.

Overa
ll, the HelpKit public beta has been running for 2 weeks and users as well as customers are really satisfied with the gr
eat user experience. Which… also obviously makes me super happy ツ

&#x200B;

**Building on top of AI**

HelpKit AI is my
 first real touchpoint developing a product with Large Language Models (LLMs). After doing some simple warm-up Hello Wor
ld AI tests, everything seemed so simple.

Unfortunately I had to soon find out that I sincerely underestimated the comp
lexity involved in developing a conversational AI chatbot that closely mirrors human interaction.

Following a considera
ble period of experimentation with a plethora of existing tools, it's become apparent that the majority merely repurpose
 around 10 lines of Langchain code, presenting it as a fully-fledged product.The outcomes of these efforts are, at their
 best are 'meh'.

Some OK, but not great.I nearly fell into the same trap, having developed a feature that was 90% compl
ete before acknowledging the subpar and cluttered results, as well as my limited comprehension of this new technology.


Engaging with LLMs presents an entirely unique and novel paradigm.Consequently, I revisited the initial plans and invest
ed a lot of more time immersing myself in the intricacies of LLMs, AI User Experience, and a slew of way too complex res
earch papers, all in an effort to better understand how to construct tools around LLMs.

Interestingly, due to the novel
ty of this field, there's no definitive roadmap to a successful implementation. The process is characterized by a great 
deal of experimentation. You really need a flexible approach and swift adaptation to the frequent and rapid enhancements
 being made to these tools. As an engineer being used to having deterministic outcomes I just couldn’t believe the quirk
iness of testing out bunch of prompts to find out what works the best.

In the end everything finally clicked and I know
 exactly what I was doing and how I can make HelpKit AI as best as possible.

&#x200B;

**Wrapping up**

So that’s my li
ttle background story of building HelpKit AI and some of the struggles that I had. The biggest takeaway lesson from me h
ere was to realize that sometimes you need to stop being so harsh on yourself and accept that some things are more diffi
cult than others. You might need a little bit more time than you thought.

The beautiful thing for us Indiehackers is th
at we don’t have any pressuring project manager sitting behind our back pressuring us to release something despite the q
uality but somehow we still tend pressure ourselves even harder into it.

Take a step back, breath, learn more and then 
come back stronger.In case you are interested you can find the [HelpKit AI landing page here](https://www.helpkit.so/hel
pkit-ai/) and I also recorded a little [Youtube video demoing HelpKit AI](https://www.youtube.com/watch?v=RhWrzh9pk-c) y
ou can check out.

&#x200B;

That's it!

&#x200B;

Hope this was useful to some of you reading this and also thinking ab
out embarking on the journey of building a big new feature for your product.
```
---

     
 
all -  [ I am unable to import csv_agents in langchain ](https://www.reddit.com/r/LangChain/comments/16im8h7/i_am_unable_to_import_csv_agents_in_langchain/) , 2023-09-18-0909
```
I am building a web application to query data from CSV files and tried importing csv langchain agent using this command,
 which was taken from langchain documentation:

'from langchain.agents import create\_csv\_agent'

However, this module 
is just not getting imported and I am getting an error whenever I use 'create\_csv\_agent' function. I am using VSCode t
o run my code by the way. Any idea why this keeps happening?
```
---

     
 
all -  [ I built an AI Agent (BondAI) that actually works and has a friendly API for easy integration into ot ](https://www.reddit.com/r/AI_Agents/comments/16il2ss/i_built_an_ai_agent_bondai_that_actually_works/) , 2023-09-18-0909
```
📢 Hello AI agent builders!

I'm thrilled to introduce you to **BondAI**, an AI Agent framework and CLI, with a lightweig
ht yet robust API making integration into your own applications straightforward and easy.

**Repository:** [**https://gi
thub.com/krohling/bondai**](https://github.com/krohling/bondai)

# ⚡️Examples

Here's an example of buying/selling Stock
s with [Alpaca Markets](https://alpaca.markets/). I strongly recommend using Paper Trading btw!

    from bondai import 
Agent
    from bondai.tools.alpaca_markets import CreateOrderTool, GetAccountTool, ListPositionsTool
    
    task = '''
I want you to sell off all of my existing positions.
    Then I want you to buy 10 shares of NVIDIA with a limit price o
f $456.'''
    
    Agent(tools=[
      CreateOrderTool(),
      GetAccountTool(),
      ListPositionsTool()
    ]).run(
task)

[**Here's an example**](https://github.com/krohling/bondai/tree/main/examples/online-research) of BondAI doing on
line research and [**here's a home automation example**](https://github.com/krohling/bondai/tree/main/examples/home-auto
mation).

# 🔍 What is BondAI?

**BondAI** is a framework crafted for the smooth integration and customization of Convers
ational AI Agents. Leveraging the power of OpenAI's [**function calling support**](https://openai.com/blog/function-call
ing-and-other-api-updates), it sidesteps the hurdles often encountered in building a Conversational Agent, offering solu
tions such as:

* Memory management
* Error handling
* Integrated semantic search
* A rich array of pre-existing tools
*
 Ease of crafting custom tools

Moreover, it offers a **CLI interface** that promises an impressive command line agent e
xperience, available to anyone with an OpenAI API Key!

# 🏗️ Why build BondAI?

I am convinced that AI agents hold the f
uture. Despite their phenomenal problem-solving abilities, the existing tooling often fell short in performing simple ta
sks, and the frameworks appeared unnecessarily complicated. This spurred the birth of **BondAI**, aiming to address thes
e shortcomings and offer a more optimized environment for agent implementations.

I am keen on hearing your feedback on 
**BondAI**'s functionality and any suggestions for improvements!

# 🛠️ Installation & Usage

Get started with BondAI wit
h a simple: pip install bondai  
The CLI tool offers a ready-to-use agent experience packed with several default tools. 
You can also integrate it with various tools such as Google Search, Alpaca Markets, and LangChain Tools to execute a myr
iad of tasks effectively. Detailed guides and examples for usage are available in the README.

# 🔧 APIs and Custom Tools


The BondAI framework offers flexible APIs to build your agent and create custom tools for a personalized experience. I
t follows a straightforward implementation approach, making the tool creation process hassle-free for developers.

Examp
les of included Tools:

* Google and Duck Duck Go Search
* Semantic Search for Files and Websites
* Alpaca Markets
* Gma
il Integration
* Easily import tools from LangChain!

# 🐋 Docker Container

For a secure environment, especially while u
sing tools with file system access, running **BondAI** within a docker container is highly recommended. Follow the steps
 in the REAME to easily build and run the **BondAI** container.

🚀 Join the mission; contribute to BondAI! And please sh
are feedback/ideas in the comments!
```
---

     
 
all -  [ Hybrid similarity scores? EG, jaccard + cosine ](https://www.reddit.com/r/datascience/comments/16ij333/hybrid_similarity_scores_eg_jaccard_cosine/) , 2023-09-18-0909
```
Hello,

I'm making my way around the langchain circuit and practicing with langsmith. I am no stranger to accuracy tests
, I don't mind harmonic mean jokes because that's exactly what an f1 is.

Is there an analogous approach to similarity s
cores? For example, jaccard doesn't capture the magnitude or direction of the vectors, while cosine doesn't consider the
 order, frequency, or the context of the words.

Can i combine these scores into a hybrid accuracy score?
```
---

     
 
all -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-09-18-0909
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
 
all -  [ The rollercoaster journey behind launch the HelpKit AI Notion Chatbot ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/16ieqkw/the_rollercoaster_journey_behind_launch_the/) , 2023-09-18-0909
```
Hey folks!

Today I want to talk with you about the journey behind launching HelpKit AI. HelpKit is a solo founded and f
ully bootstrapped SaaS tool that turns your Notion docs into a professional help center and documentation site.

Since H
elpKit is already hosting hundreds of customers Notion knowledge bases it only made sense to supercharge them with a cus
tom AI trained chatbot. So far the results have been amazing.

And now, we just finally [launched today on Product Hunt]
(https://www.producthunt.com/posts/helpkit-ai) as well! The public beta is out since two weeks and we have onboarded mor
e than 15 customers on the add-on and the AI bot held 2000+ successful conversations.The launch was planned two months a
go but some things stopped me from releasing it.

If you are curious about the background feel free to read on.Now, let 
me explain why the journey to the launch was a bit rougher than expected. There were two big issues: The UX and building
 on top of AI.

**The UX Hurdle**

First and foremost, I was stuck with developing a great user experience. I have only 
come across a handful of products that were sort of implementing the same concept and I really did not like their UX imp
lementation. Everything felt clunky and just did not fit into the concept of an AI enabled knowledge base system.

You s
ee our AI chatbot needs to be integrated into HelpKit’s two layouts: Help Center and Documentation and also work well on
 the widget and mobile.Quite a tricky task to get right everywhere! I brainstormed for a few days, tried out some implem
entations but none of them felt natural for a user in my opinion.

I even spent a whole week building an interface only 
to then throw away the entire feature code branch and start from scratch.What I needed was a break. So I took a weekend 
break, spent some time at the beach and came back refreshed with some new ideas (that strangely all came to me during my
 Sunday evening shower).

I realised that the most intuitive way to present the option to chat with an AI powered chatbo
t assistant is when the user is already searching for something. So this way, should our normal search not be able to de
liver an instant search result, users can be “catched” and still have their problem resolved by the AI.

In terms of the
 UI, I decided to go with a slick right sidebar interface for the chatbot on the help center layout and a nicely integra
ted chat window within the search command bar of the documentation layout. Within the HelpKit embeddable widget as well 
as on mobile phones, HelpKit AI will show a full-screen chatbot interface to the user.

Overall, the HelpKit public beta
 has been running for 2 weeks and users as well as customers are really satisfied with the great user experience. Which…
 also obviously makes me super happy ツ

&#x200B;

**Building on top of AI**

HelpKit AI is my first real touchpoint deve
loping a product with Large Language Models (LLMs). After doing some simple warm-up Hello World AI tests, everything see
med so simple.

Unfortunately I had to soon find out that I sincerely underestimated the complexity involved in developi
ng a conversational AI chatbot that closely mirrors human interaction.

Following a considerable period of experimentati
on with a plethora of existing tools, it's become apparent that the majority merely repurpose around 10 lines of Langcha
in code, presenting it as a fully-fledged product.The outcomes of these efforts are, at their best are 'meh'.

Some OK, 
but not great.I nearly fell into the same trap, having developed a feature that was 90% complete before acknowledging th
e subpar and cluttered results, as well as my limited comprehension of this new technology.

Engaging with LLMs presents
 an entirely unique and novel paradigm.Consequently, I revisited the initial plans and invested a lot of more time immer
sing myself in the intricacies of LLMs, AI User Experience, and a slew of way too complex research papers, all in an eff
ort to better understand how to construct tools around LLMs.

Interestingly, due to the novelty of this field, there's n
o definitive roadmap to a successful implementation. The process is characterized by a great deal of experimentation. Yo
u really need a flexible approach and swift adaptation to the frequent and rapid enhancements being made to these tools.
 As an engineer being used to having deterministic outcomes I just couldn’t believe the quirkiness of testing out bunch 
of prompts to find out what works the best.

In the end everything finally clicked and I know exactly what I was doing a
nd how I can make HelpKit AI as best as possible.

&#x200B;

**Wrapping up**

So that’s my little background story of bu
ilding HelpKit AI and some of the struggles that I had. The biggest takeaway lesson from me here was to realize that som
etimes you need to stop being so harsh on yourself and accept that some things are more difficult than others. You might
 need a little bit more time than you thought.

The beautiful thing for us Indiehackers is that we don’t have any pressu
ring project manager sitting behind our back pressuring us to release something despite the quality but somehow we still
 tend pressure ourselves even harder into it.

Take a step back, breath, learn more and then come back stronger.In case 
you are interested you can find the [HelpKit AI landing page here](https://www.helpkit.so/helpkit-ai/) and I also record
ed a little [Youtube video demoing HelpKit AI](https://www.youtube.com/watch?v=RhWrzh9pk-c) you can check out.That's it!


Hope this was useful to some of you reading this and also thinking about embarking on the journey of building a big ne
w feature for your product.
```
---

     
 
all -  [ What are your best practices when using Embeddings, RAG, and Retrieval? ](https://www.reddit.com/r/LangChain/comments/16idhfw/what_are_your_best_practices_when_using/) , 2023-09-18-0909
```
Hi there,

Recently started building LLM applications, While talking to developers in the field, I got overwhelmed by al
l the tools and services available.

* Different embedding algorithms: For some ada-002 is SOTA, for others not
* Embedd
ing pipeline providers
* Chunking and cleaning
* Injecting up-to-date Knowledge Bases (RAG)
* Indexing
* Retrieval

(I w
ill not even start with 10s of different vector DB providers)

I'd love to collect **best practices for common pain poin
ts.** Can we create a high-quality thread with the following?

&#x200B;

1. **What is your tool stack for LLM applicatio
ns?**
2. **What problems did you experience?**
3. **How did you solve it? (if it's solved, otherwise 'looking for a solu
tion')**

&#x200B;
```
---

     
 
all -  [ How to use multiple toolkits wit agents ](https://www.reddit.com/r/LangChain/comments/16iatr5/how_to_use_multiple_toolkits_wit_agents/) , 2023-09-18-0909
```
I need to use the Vector Store Toolkit and SQL Toolkit.

Is there a method that allows me to combine both toolkits for u
se in Agent.

Any ideas?
```
---

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-18-0909
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-18-0909
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-18-0909
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-18-0909
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-18-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-18-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-18-0909
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-18-0909
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
