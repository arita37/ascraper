 
all -  [ Computer Science Intern with no prior experience ](https://www.reddit.com/r/resumes/comments/1ch1tvs/computer_science_intern_with_no_prior_experience/) , 2024-05-01-0911
```
Hi guys. Im currently a year 2 cs student without any internship experience before. Looking for advice for my first CV =
).

I still have other projects, including :
-restaurant pos system developed in java
-linux gold price tracker 
-haskel
l black box game solver 

Should i switch my current projects withh any from the above? Or should increase to 2 pages fo
r them? 
 Thank you.

https://preview.redd.it/fiu7ucvl7oxc1.jpg?width=1275&format=pjpg&auto=webp&s=79915781fe7e72c9616cc
beb52e1881629b24fea


```
---

     
 
all -  [ need help in creating an AI agent ](https://www.reddit.com/r/LangChain/comments/1ch0t01/need_help_in_creating_an_ai_agent/) , 2024-05-01-0911
```
I am creating a project whose one component is an AI agent parsing a pdf, opening a link given in the pdf and performing
 a specific action. can anyone guide me on how to do this? I cant really find any specific resources online. thank you.
```
---

     
 
all -  [ What's the most painful part about using Langchain? ](https://www.reddit.com/r/LangChain/comments/1cgzl9n/whats_the_most_painful_part_about_using_langchain/) , 2024-05-01-0911
```
For me, it was figuring out what steps in my RAG pipeline to use and how that affected the quality of responses. What ch
unking strategy do I use, which embedding models, what retrieval techniques can increase the relevancy of answers, how d
o I measure the quality of answers, etc.  There's a ton of time I spent on experimentation.

Also, the docs are changing
 frequently, so I had often had to read the raw source code to see how something worked.
```
---

     
 
all -  [ Former AWS and creator of the CDK live hacking session to integrate Langchain with Wing at 2 PM EST ](https://www.reddit.com/r/aws/comments/1cgz0lq/former_aws_and_creator_of_the_cdk_live_hacking/) , 2024-05-01-0911
```
Come hang out at the live hacking session today at 2 PM EST on the Wingly Episode.

[Elad Ben-Israel](https://www.linked
in.com/in/hackingonstuff/) (creator of the AWS CDK) will be live hacking on a Langchain integration with Wing

Join live
 on [Twitch](https://www.twitch.tv/winglangio) or [YouTube](https://www.youtube.com/watch?v=4FWt2MWddyM)
```
---

     
 
all -  [ Former AWS and creator of the CDK live hacking session to integrate Langchain with Wing at 2 PM EST ](https://www.reddit.com/r/LangChain/comments/1cgyxub/former_aws_and_creator_of_the_cdk_live_hacking/) , 2024-05-01-0911
```
Come hang out at the live hacking session today at 2 PM EST on the Wingly Episode.

[Elad Ben-Israel](https://www.linked
in.com/in/hackingonstuff/) (creator of the AWS CDK) will be live hacking on a Langchain integration with Wing

Join live
 on [Twitch](https://www.twitch.tv/winglangio) or [YouTube](https://www.youtube.com/watch?v=4FWt2MWddyM)
```
---

     
 
all -  [ LangChain LCEL - Split string into list and then batch it in one chain?  ](https://www.reddit.com/r/LangChain/comments/1cgyllo/langchain_lcel_split_string_into_list_and_then/) , 2024-05-01-0911
```
Hello LangChain Community,

I'm working with RunnableSequence from langchain\_core.runnables and encountering an issue w
here the input handling doesn't work as expected. My sequence is designed to first convert a string input into a list of
 integers, and then apply a series of functions (add\_one, mul\_two, mul\_three) on the list.

Could anyone suggest how 
to correctly structure this sequence so that the .batch() method processes the string as an entire list rather than spli
tting into characters? Additionally, is there a better way to ensure each list element passes through all functions in t
he sequence as intended?

Thank you for your help!

Code:

    from langchain_core.runnables import RunnableLambda, Runn
ableParallel, RunnableSequence, RunnablePassthrough
    
    from langchain_core.runnables.config import RunnableConfig

    
    import time
    
    MAX_CONCURRENCY = 2
    
    runnable_conf = RunnableConfig(max_concurrency= MAX_CONCURREN
CY, run_name='my-prompt-123', callbacks= [])
    
    import ast
    def string_to_int_list(s: str) -> list:
        # W
e want to turn the string into a list of integers...
        list_from_string = ast.literal_eval(s)
        return [int(
item) for item in list_from_string]
    
    
    def add_one(x: int) -> int:
        print('enter add_one()')
        t
ime.sleep(3) 
        print('exit add_one()')
        return x + 1
    
    def mul_two(x: int) -> int:
        print('e
nter mul_two()')
        time.sleep(5)
        print('exit mul_two()')
        return x * 2
    
    def mul_three(x: in
t) -> int:
        print('enter mul_three()')
        time.sleep(5)
        print('exit mul_three()')
        return x *
 3
    
    runnable_0 = RunnableLambda(string_to_int_list)
    runnable_1 = RunnableLambda(add_one)
    runnable_2 = Ru
nnableLambda(mul_two)
    runnable_3 = RunnableLambda(mul_three)
    
    
    # -- WORKING --
    # sequence_working = 
RunnableSequence(
    #     runnable_1 | {'mul_two': runnable_2, 'mul_three': runnable_3}
    # )
    
    # sequence_wo
rking.batch([1, 2, 3], config=runnable_conf)
    
    
    
    # -- NOT WORKING --
    
    # This chain tries to split
 the input string into a list of integers first ..
    sequence_not_working = RunnableSequence(
        runnable_0 | run
nable_1 | {'mul_two': runnable_2, 'mul_three': runnable_3}
    )
    
    # .batch() does not work because it splits the
 string into chars first ...
    # sequence_not_working.batch('[1, 2, 3]', config=runnable_conf)
    
    # .invoke() pa
sses the complete list from string_to_int_list() to add_one()
    sequence_not_working.invoke('[1, 2, 3]', config=runnab
le_conf)
```
---

     
 
all -  [ WEEKEND PROJECT HELP!!! ](https://www.reddit.com/r/LangChain/comments/1cgy1or/weekend_project_help/) , 2024-05-01-0911
```
hey guys,

i'm working on this little weekend project to implement my langchain learnings.

i am wondering how to build 
this product where

- everyone attends a standup meeting in the morning, and tldv.io records the whole meeting and gives
 the text back.

- then, i need to write some code to gain access to this script/manually can be inputted too.

- but, h
ow do i use this text and imput it in a streamlit interface and then add each person's tasks into like a kanban board in
 notion?

- need help figuring out what agents, tools i should use to implement the same.does the same have to be hosted
 or something?

let me know thanks!
```
---

     
 
all -  [ Confusion Structured Output ](https://www.reddit.com/r/LangChain/comments/1cgwn58/confusion_structured_output/) , 2024-05-01-0911
```
https://preview.redd.it/0rnzunys4nxc1.png?width=1306&format=png&auto=webp&s=f54ad7e26a1eec569c869664d2a354b4edb50e66

# 
Why model.with\_structured\_output forces to tell joke even though user question doesn't ask for Joke
```
---

     
 
all -  [ What vector store should I use for a chatbot SAAS ](https://www.reddit.com/r/LangChain/comments/1cgtzej/what_vector_store_should_i_use_for_a_chatbot_saas/) , 2024-05-01-0911
```
I am relatively new to vector stores and I was wondering what vector store I should use handling x amount of index per u
ser. So the vector store should be handling mulitiple indexes. Am i better off using an Open Source solution or are ther
e any other good solutions.
```
---

     
 
all -  [ Assumption: 'Why was AI-Art automated first and foremost!' // Relaity: See statistics, AI is everywh ](https://i.redd.it/7kai7gb2jmxc1.png) , 2024-05-01-0911
```

```
---

     
 
all -  [ Phi3 performing better than Llama3 on RAG for QA ](https://www.reddit.com/r/LangChain/comments/1cgtezt/phi3_performing_better_than_llama3_on_rag_for_qa/) , 2024-05-01-0911
```
Hello,
I have a pdf where I am expecting some answers to the questions asked and I am seeing that phi3 mode is generatin
g better output than llama3 with minimal prompts . 
I tried with llama3 but the prompt with which answer is given is rat
her complex.
Is this the behaviour with llama3 model or every model should have specific prompts?
Thanks
```
---

     
 
all -  [ É normal Júnior tomar conta de um projeto pra cliente sozinho? ](https://www.reddit.com/r/brdev/comments/1cgseel/é_normal_júnior_tomar_conta_de_um_projeto_pra/) , 2024-05-01-0911
```
Fui contratado como dev junior em uma empresa de consultoria que tá querendo investir em IA. Meu time é eu, outro Júnior
 que tá faz quase um ano e o nosso tech lead (que também é tech lead do time de dados). Tenho 6 meses de experiência com
 estágio em desenvolvimento Python, e quando entrei disseram que iam me treinar (não passei por treinamento), que eu dev
eria estudar e desenvolver minha autonomia porque a intenção era eu tocar projetos para clientes sozinho.

Passaram-se 3
 meses e minhas atividades até agora foram melhorar projetos internos com a minha stack (Python, Langchain, frameworks d
e IA no geral), mas sem muita supervisão. Nem existe pull request, code review, eu só faço o código, jogo na main e fica
 por isso. Meu chefe diz que vai dar uma analisada no meu código e nunca acontece.

Agora, disseram que fecharam contrat
o com um cliente pra eu assumir e desenvolver um sistema de IA pra eles. Me explicaram as tecnologias que eu vou ter que
 usar, que vou ter que trabalhar na AWS (não tenho experiência com AWS e eles sabem disso) e começa o projeto daqui a 2 
dias.
O projeto já tá com número de sprints, data e entrega e etc tudo certinho, sem terem me falado nada antes kkkkkk.


Admito que eu, como um Júnior, fico me questionando se eu deveria assumir tanto responsabilidade assim visto que ainda 
não tenho tanta experiência ou bagagem pra tocar projetos sozinhos. Isso é normal? ou é uma bela de uma Red Flag?
```
---

     
 
all -  [ Building Local RAG with Adaptive Retrieval using Mistral, Ollama and Pathway ](https://www.reddit.com/r/LangChain/comments/1cgs6kj/building_local_rag_with_adaptive_retrieval_using/) , 2024-05-01-0911
```
Hey r/Langchaindev , we previously shared an adaptive RAG technique that reduces the average LLM cost while increasing t
he accuracy in RAG applications with an adaptive number of context documents. 

People were interested in seeing the sam
e technique with open source models, without relying on OpenAI.  We successfully replicated the work with a fully local 
setup, using Mistral 7B and open-source embedding models.  

In the showcase, we explain how to build local and adaptive
 RAG with Pathway. Provide three embedding models that have particularly performed well in our experiments. We also shar
e our findings on how we got Mistral to behave more strictly, conform to the request, and admit when it doesn’t know the
 answer.

PS: Our Pathway VectorStoreServer also has [LangChain Integration](https://python.langchain.com/docs/integrati
ons/vectorstores/pathway/).

Hope you like it!

  
Here is the blog post:

[https://pathway.com/developers/showcases/pri
vate-rag-ollama-mistral](https://pathway.com/developers/showcases/private-rag-ollama-mistral)

If you are interested in 
deploying it as a RAG application, (including data ingestion, indexing and serving the endpoints) we have a [quick start
 example in our repo](https://github.com/pathwaycom/llm-app/tree/main/examples/pipelines/private-rag). 
```
---

     
 
all -  [ Text similarity ](https://www.reddit.com/r/LangChain/comments/1cgrwjl/text_similarity/) , 2024-05-01-0911
```
I would like to calculate text similarity between sentences or between a sentence and a document.

Assume I have 3 sente
nces:  
text1 = 'Hello world'  
text2 = 'Hello'

text3 = 'Hello worlds'

If I use cosine similarity then text1 and text2
 will have the same similarity as text1 and text3

What I would like for my case is to have higher similarity score in c
ase of text1 and text3 since the only difference is the plural.

What would be the best metric/algorithm to do so?
```
---

     
 
all -  [ What should I choose as my career path? ](https://www.reddit.com/r/careerguidance/comments/1cgom5v/what_should_i_choose_as_my_career_path/) , 2024-05-01-0911
```
I am 26M, graduated in 2021 with B.E in Electronics and communication.

Currently I am working as R&D Engineer in IT.

I
 do research for new projects in my company and develop a POC and sometimes document my research as well.

In my 2 years
 of experience, I have developed POC on projects utilizing generative AI, Langchain, Azure cloud, Power BI Embedded.

I 
am trying to switch job. However, as I don't have a niche yet, no company is recognizing my resume as worthy for the job
s.

So I thought let's do deep dive into research jobs as I am good at it and I also have some experience.

But now when
 I see JD in LinkedIN, Indeed, etc, they usually require experience in Market Research and most of the jobs as for Resea
rch Analyst.

I don't mind working in these roles but my resume gets rejected when I apply for them.

  

```
---

     
 
all -  [ Using FAISS for similarity search ](https://www.reddit.com/r/LangChain/comments/1cgo0n4/using_faiss_for_similarity_search/) , 2024-05-01-0911
```
I wanted to perform similarity search using Faiss. I searched how to do, but most of these examples work on data that is
 stored in some file in json or in pandas df. So, if I plan to store my data in a different database, then also while pe
rforming Faiss based search, it looks like I have to take all the data and process it in-memory to work with Faiss. So, 
it feels like I am storing at two places unnecessarily. How usually everyone work with Faiss? Since I am new to this, it
 is confusing. Can someone clarify?
```
---

     
 
all -  [ Does LangChain memory management only work with OpenAI model? ](https://www.reddit.com/r/LangChain/comments/1cgno5b/does_langchain_memory_management_only_work_with/) , 2024-05-01-0911
```
I'm new to LangChain, I saw this page \`docs/use\_cases/chatbots/memory\_management/\`. It mentioned that we need an Ope
nAI key for that. 

Does the \`memory management\` work with another model as well? Anyne have references?
```
---

     
 
all -  [ How to install langchain packages that don't exist on conda on conda ](https://www.reddit.com/r/LangChain/comments/1cgnmdm/how_to_install_langchain_packages_that_dont_exist/) , 2024-05-01-0911
```
hello. I noticed a couple packages that exist on pypi such as langchainhub and  langchain-chroma per [Quickstart | 🦜️🔗 L
angChain](https://python.langchain.com/docs/use_cases/question_answering/quickstart/#setup) , but they don't exist on an
aconda. is there a way to install these with anaconda or will I need to use python with virtualenv instead? Thank you.
```
---

     
 
all -  [ Clustering Embeddings for Sub-Topic Extraction in RAG ](https://www.reddit.com/r/LangChain/comments/1cgmjr5/clustering_embeddings_for_subtopic_extraction_in/) , 2024-05-01-0911
```
Hey Guys. I'm building a project that involves a RAG pipeline and the retrieval part for that was pretty easy - just nee
ded to embed the chunks and then call top-k retrieval. Now I want to incorporate another component that can identify the
 widest range of like 'subtopics' in a big group of text chunks. So like if I chunk and embed a paper on black holes, it
 should be able to return the chunks on the different subtopics covered in that paper, so I can then get the sub-topics 
of each chunk. (If I'm going about this wrong and there's a much easier way let me know) I'm assuming the correct way to
 go about this is like k-means clustering or smthn? Thing is the vector database I'm currently using - pinecone - is rea
lly easy to use but only supports top-k retrieval. What other options are there then for something like this? Would appr
eciate any advice and guidance.
```
---

     
 
all -  [ What happened to Router Chains? ](https://www.reddit.com/r/LangChain/comments/1cgmgxb/what_happened_to_router_chains/) , 2024-05-01-0911
```
I've been trying to figure out how to route agents to decide on certain tools lately and many articles on Medium suggest
 Router chains. However the docs page for it is now empty: https://python.langchain.com/en/latest/modules/chains/generic
/router.html

How do we implement Router chains now? Is there a notebook that demonstrates this?
```
---

     
 
all -  [ Feedback on my resume? I'm a third-year undergrad and have had 0 luck with internships. I seriously  ](https://www.reddit.com/r/resumes/comments/1cgltd6/feedback_on_my_resume_im_a_thirdyear_undergrad/) , 2024-05-01-0911
```


**Education** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

**B.S. in Data Science University of Californ
ia, San Diego** *San Diego, CA* **Expected 03/2025** Major in Data Science (Machine Learning and Artificial Intelligence
 Track) 

**Experience** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

 

**Undergraduate Researcher** 

&#x2
00B;

**MIT Computer Science & Artificial** *Cambridge, MA* **02/2024 - Present Intelligence Lab** 

 

• Participated a
s a key contributor in a cutting-edge research paper, 'Neural Codec Resynthesis,' aimed at pioneering advancements in au
dio quality through innovative resynthesis methods such as the Codec Schrödinger Bridge approach. https://openreview.ne
t/forum?id=uJfDaEpTKN • Explored advanced audio compression techniques and the impact of neural networks on enhancing au
dio quality, focusing on the efficacy of Residual Vector Quantization and adversarial perceptual losses. Currently advan
cing this research as the lead author of a forthcoming paper. 

 

**Undergraduate Researcher** 

&#x200B;

**Machine In
telligence Lab** *San Diego, CA* **11/2023 - 02/2024 UC San Diego** 

 

• Collaborated with **4** Ph.D. candidates to s
tudy the robustness of Deep Learning-based Automatic Speech Recognition, enhancing privacy in mmWave-based audio-sensing
 scenarios (eg. Amazon Alexa) & ensuring secure communication in eavesdropping-prone environments.  
 • Spearheaded the 
implementation of adversarial attacks using FGSM, BIM, & PGM within CNNs in PyTorch. Successfully reduced speech recogni
tion system accuracy from **90%** to **3.2%** using adversarial attacks, ensuring human comprehension with minimal noise
 interference. 

**Machine Learning Intern Dart** *Bay Area, CA* **11/2023 - 03/2024** 

• Developed an AI phone agent c
apable of handling incoming and outgoing business-specific calls across **12** clinics in California.  
 • Built a compr
ehensive dashboard using Next.js for access to call transcripts and notes, integrated Twilio for call routing services, 
utilized web sockets, and deployed realistic Text-to-Speech (TTS) models: https://shorturl.at/cikvB (agent) and https://
shorturl.at/HPV69 (dashboard) 

**LLM Engineering Intern Internalize** *Bay Area, CA* **05/2023 - 09/2023**  
 • Develop
ed an LLM chatbot that gives product recommendations, focusing on improving sales conversions and ensuring accurate resp
onses to 

queries about products on E-commerce websites, resulting in a competitor's acquisition of the codebase. 

**D
ata Analyst Intern Dermose** *San Diego, CA* **06/2022 - 09/2022** • Managed customer data via CRMs and applied analytic
s to identify key customer demographics for creating targeted marketing strategies. 

• Conducted A/B tests to boost mar
keting campaign reach by **40%**; Developed and presented **15** weekly KPI dashboards and actionable insights. **Co-fou
nder & COO Socale** *San Diego, CA* **09/2021 - 05/2023** 

• Co-founded a networking and collaboration platform that ma
tches like-minded classmates on college campuses backed by Berkeley Skydeck, Blackstone Launchpad, and Rady School of Ma
nagement. **Top 10%** of YCombinator W’23 Applicants.  
 • Raised venture funds and **$110,000** in AWS credits, garneri
ng over **140,000** UCSD targeted impressions within two months post-launch.  
 • Deployed an app that gained **1,000+**
 downloads, **13,000** messages, and **30,000** sessions from UCSD students. 

• Developed a graph-based recommendation 
algorithm to foster matching **900+** users on academic interests.  
 • Created comprehensive dashboards for diverse tea
m departments to track KPIs from Instagram, Mailchimp, AWS, and Google Analytics. 

**Relevant Coursework** \_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Machine Learning Specialization, Stanford University | Deep Learning Specialization, Deep
Learning.AI | Generative AI with Large Language 

Models, AWS & DeepLearning.AI | SQL Full Database Course | Audio Signa
l Processing for Machine Learning | Adversarial ML Techniques 

**Skills** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_\_\_\_\_\_  
 Python | Java | R | MATLAB | SQL | Git | AWS | Tableau | Data Structures & Algorithms | ML 
Supervised, Self-Supervised, & Unsupervised Models | Deep Learning Methods | Neural Networks Design & Optimization | ASR
 & Speech Synthesis | Scikit-learn | Keras | Pytorch | Tensorflow | Librosa | SciPy | NLTK | LangChain | Hugging Face | 
Pinecone | Redis | Dashboard Development | Presenting Data Insights | English, Farsi, Japanese, French 

**Projects & Or
ganizations** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
 • **Orbitra (LinkedIn Marketing AI Assistant):** Developed a chatbot tha
t leverages trend analysis for business-specific LinkedIn post creation, reducing time spent on marketing. Tested in 6 c
ase studies, adapts to diverse marketing goals, including virality and community building.  
 • **RAZI:** Founded an org
anization that provided data-driven marketing strategies. Developed an in-house AI tool to identify pain points in engag
ement for social profiles to use in **50+** client outreach processes. Directed strategy and execution for over eight cl
ient collaborations, including marketing campaigns for startups valued at **$3-7** million and influencers with **124-21
0K** followers. Assembled a diverse **47**\-member team from UC Berkeley, UCLA, & UCI, including marketers, data analyst
s, and ML specialists. Conducted **36** workshops and hosted **7** speakers. 
```
---

     
 
all -  [ Setting max_tokens arg for BedrockChat for Claude doesn't work after 2048 ](https://www.reddit.com/r/LangChain/comments/1cgldr2/setting_max_tokens_arg_for_bedrockchat_for_claude/) , 2024-05-01-0911
```
I'm using BedrockChat as my llm and is currently setting max\_tokens to 4096 as part of the llm.model\_kwargs since Clau
de V3 claims that it can support output tokens of up to 4096. However the outputs I'm seeing all stop at 2048 tokens. Se
tting max\_tokens to <2048 is working as intended and the LLM is spitting out less tokens. How come it isn't working for
 >2048?
```
---

     
 
all -  [ RAG: OpenAI embedding model is vastlty superior to all the currently available Ollama embedding mode ](https://www.reddit.com/r/ollama/comments/1cgkt99/rag_openai_embedding_model_is_vastlty_superior_to/) , 2024-05-01-0911
```
I'm using Langchain for RAG, and i've been switching between using
Ollama and OpenAi embedders. The OpenAI embeddeder is
 a class above all the currently available Ollama embedders, in terms of retrieval. Its not even close. The only model i
 get half-way decent retrieval is the `snowflake-artic-embed`, and its still not that great. If i use `OpenAIEmbeddings(
)`, its, as far as i'm concerned, perfect retrieval. 

I'm very confused
about this because models like `snowflake-arcti
c-embed` say they outperform
openAI. At least thats what it says on its 
 blog post https://www.snowflake.com/blog/intro
ducing-snowflake-arctic-embed-snowflakes-state-of-the-art-text-embedding-family-of-models/

Is it currently possible to 
match OpenAI retrieval with Ollama? 

```
---

     
 
all -  [ Langgraph + LangServe ](https://www.reddit.com/r/LangChain/comments/1cgkt5k/langgraph_langserve/) , 2024-05-01-0911
```
I'm trying to find any tutorials on how to deploy a lnggraph project using langserve. I'm quite new to programming so ma
ybe I'm not reading the documentation correctly. But I couldn't figure out how to. Can someone point me a beginner frien
dly guide if available?

&#x200B;
```
---

     
 
all -  [ I made a simple voice AI assistant using OpenAI assistants API. ](https://www.reddit.com/r/ArtificialInteligence/comments/1cghebw/i_made_a_simple_voice_ai_assistant_using_openai/) , 2024-05-01-0911
```
Hi, I wondered how to build an AI voice assistant like Siri. I found out that OpenAI has a whispers API that can do text
-to-speech and speech-to-text, while we can use the Assistants API for the conversation part.  
Since this is a fun proj
ect, I decided to build an MVP by getting rid of the Whisper part and using **browser Javascript API:** **Web Speech API
** for the voice input and output. While using the assistant API as the main brain.

I think we can improve the speed an
d the quality by:

Voice input: AssemblyAI or OpenAI Whisper  
Voice output: Elevenlabs or OpenAI Whisper  
Speed: using
 different model on Langchain (but we have to get rid of the Assistants API part)  
Let me know if anyone had an idea ho
w to improve it.  
Here is the tutorial: \[Build AI voice assistants with openAI assistants API\](https://serpapi.com/bl
og/build-ai-voice-assistant-like-siri-use-openai-ai-assistant/)  
Here is the source code: \[AI voice assistants code sa
mple on GitHub\]([https://github.com/hilmanski/simple-ai-voice-assistant-openai-demo](https://github.com/hilmanski/simpl
e-ai-voice-assistant-openai-demo))  


I hope it's useful for anyone!
```
---

     
 
all -  [ How I build an AI voice assistant with OpenAI ](https://www.reddit.com/r/OpenAI/comments/1cgh184/how_i_build_an_ai_voice_assistant_with_openai/) , 2024-05-01-0911
```
This is a blog post tutorial on how to build an AI voice assistant using OpenAI assistants API.

Stack  
---  
Voice inp
ut: Web Speech API  
AI assistant: OpenAI AI assistant  
Voice Output: Web Speech API

It takes a few seconds to receive
 a response (due to the AI assistants). We might can improve this by using chat history by LangChain while still using t
he OpenAI model

- Here is the blog post: [How to build an AI voice assistants with openAI assistants API](https://serpa
pi.com/blog/build-ai-voice-assistant-like-siri-use-openai-ai-assistant/)  
- Here is the source code: [AI voice assistan
ts code sample on GitHub](https://github.com/hilmanski/simple-ai-voice-assistant-openai-demo)

Thanks! please let me kno
w if guys have any idea how I can improve this. \*I plan to use function calling to scrape a search result for real-time
 data.
```
---

     
 
all -  [ The Game-Changing Potential of Flow Engineering in AI Collaboration [Comprehensive Guide] ](https://www.reddit.com/r/Advanced_AI/comments/1cggra1/the_gamechanging_potential_of_flow_engineering_in/) , 2024-05-01-0911
```

I've been diving deep into an emerging paradigm called 'flow engineering' that's shaking up the world of human-AI colla
boration. If you're frustrated with the limitations of traditional prompt engineering and hungry for new ways to unlock 
AI's full potential, this post is for you. 

## What is Flow Engineering?
Flow engineering is about designing multi-step
, iterative workflows that methodically break down complex tasks for AI systems. Instead of relying on a single, monolit
hic prompt and hoping for the best, flow engineering takes a more systematic, 'System 2' style approach.

## Why Flow En
gineering Matters
The problem with the old-school prompt engineering approach is that it often fails to elicit reliable,
 high-quality outputs from AI models, especially for nuanced or multi-stage problems. AI's default 'System 1' reasoning 
- fast, pattern-matching responses - can fall short when a task demands strategic planning and adaptability.

Flow engin
eering tackles this head-on by structuring AI-assisted work as a series of well-defined steps, each with precise inputs 
and outputs. This enables a more robust, reliable form of machine intelligence to tackle complex challenges with unprece
dented effectiveness.

## Flow Engineering in Action: A Case Study
One of the most exciting proofs of concept for flow e
ngineering comes from CodiumAI's AlphaCodium project. By using a flow-based approach, they achieved state-of-the-art per
formance on highly complex code generation tasks.

Their multi-step process looked like this:
1. Generate initial code b
ased on a prompt
2. Automatically create test cases 
3. Evaluate code performance against tests
4. Revise code based on 
results
5. Repeat steps 2-4 until all tests are passed

AlphaCodium produced error-free, high-quality code through this 
iterative flow that put single-prompt approaches to shame. And here's the real kicker—this same methodology can be appli
ed to all sorts of domains, from content creation to analysis to design.

## Putting Flow Engineering to Work: Practical
 Tips
How can you harness the power of flow engineering in your AI collaborations? Here are some battle-tested strategie
s:

1. **Map out your workflow:** Break your task into clear, distinct stages with well-defined decision points and mile
stones. Think of it as creating a flowchart for human-AI collaboration.

2. **Embrace iteration:** Use AI to generate in
itial drafts or prototypes, then refine them through repeated testing and feedback cycles. The magic of flow engineering
 comes from its iterative nature.

3. **Incorporate feedback loops:** Build mechanisms for the AI to evaluate and improv
e its own outputs, whether it's through automated tests, quality metrics, or human feedback. This allows the AI to cours
e-correct and optimize its performance over time.

4. **Leverage specialized tools:** Platforms like LangChain and Anthr
opic's Claude have native support for flow engineering principles baked in. Experiment with these tools to streamline yo
ur workflow and unlock new possibilities.

5. **Continuously experiment and optimize:** Flow engineering is still an eme
rging field, which means there's massive room for experimentation and innovation. Don't be afraid to try novel approache
s, meticulously track your results, and relentlessly optimize your process. The breakthroughs are out there waiting to b
e discovered.

## The Future of Human-AI Symbiosis
As AI continues its meteoric rise, the ability to design effective hu
man-machine workflows will become an essential skill. By mastering the art and science of flow engineering, we can unloc
k new productivity, creativity, and innovation levels in our collaborations with artificial intelligence.

Flow engineer
ing is a crucial pillar of the coming age of human-AI symbiosis - a future where AI isn't just a tool but a truly collab
orative partner that enhances and augments human intelligence through carefully crafted, iterative workflows. 

## Wrapp
ing Up
The days of rote prompt engineering and hoping for the best are over. Flow engineering gives us a powerful framew
ork for structuring AI-assisted work to elicit the most reliable, highest-quality outputs, even for enormously complex t
asks.

If you find yourself spinning your wheels with prompt engineering, I can't encourage you enough to dive into flow
 engineering and start experimenting. Trust me, once you experience the power of a well-designed human-AI flow, you'll n
ever go back.

I'm excited to hear your thoughts, experiences, and discoveries around flow engineering. Please drop a co
mment, and let's push the boundaries of AI collaboration as a community!
```
---

     
 
all -  [ Agent vectordatabase ](https://www.reddit.com/r/LangChain/comments/1cgg1yy/agent_vectordatabase/) , 2024-05-01-0911
```
Hello everyone, lately I have been reviewing agents tool, I would like to know if there is currently something like an a
gent in langchain that allows me to obtain data from a vector database (already loaded)
```
---

     
 
all -  [ AI based text game autocompletes user inputs prematurely ](https://www.reddit.com/r/learnpython/comments/1cgfogv/ai_based_text_game_autocompletes_user_inputs/) , 2024-05-01-0911
```
I am trying to write a text-based adventure game following a YouTube tutorial here: https://www.youtube.com/watch?v=nhYc
Th6vw9A. After updating the code according to the latest documentation, I've encountered a problem where the AI responds
 to the inputs that should be for the player. This issue persists for the first 3-4 inputs, after which the AI stops gen
erating responses altogether.  
  
Additionally, I'm unsure about from langchain.chains import LLMChain because LLMCha
in is highlighted in white instead of green, which is typical for recognized objects in the editor I'm using. Does this 
indicate an issue with the code? I found that it may be deprecated but I could not find the new class for handling this.
  
  
Any insights on how to stop the AI from auto-completing the player's inputs and on the syntax highlighting would
 be greatly appreciated.  
  
`from astrapy import DataAPIClient`  
`import os from cassandra.cluster import Cluster 
from cassandra.auth import PlainTextAuthProvider from langchain.memory import CassandraChatMessageHistory, ConversationB
ufferMemory from langchain_openai import OpenAI from langchain.chains import LLMChain from langchain.prompts import Prom
ptTemplate from dotenv import load_dotenv`  
  
`load_dotenv()`  
  
`ASTRA_DB_APPLICATION_TOKEN = os.environ.get('A
STRA_DB_APPLICATION_TOKEN') ASTRA_DB_API_ENDPOINT = os.environ.get('ASTRA_DB_API_ENDPOINT') ASTRA_DB_KEYSPACE = os.envir
on.get('ASTRA_DB_KEYSPACE') OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') ASTRA_DB_SECURE_BUNDLE_PATH = os.environ.g
et('ASTRA_DB_SECURE_BUNDLE_PATH')`  
  
`session = Cluster( cloud={'secure_connect_bundle': os.environ['ASTRA_DB_SECUR
E_BUNDLE_PATH']}, auth_provider=PlainTextAuthProvider('token', os.environ['ASTRA_DB_APPLICATION_TOKEN']), ).connect()` 
 
  
`Initialize the client`  
`client = DataAPIClient('AstraCS:xyz') db = client.get_database_by_api_endpoint( 'xyz',
 namespace='name', )`  
  
`print(f'Connected to Astra DB: {db.list_collection_names()}')`  
  
`message_history = C
assandraChatMessageHistory( session_id='game', session=session, keyspace=ASTRA_DB_KEYSPACE, ttl_seconds=3600 #store all 
this for a maximum of 60 minutes )`  
  
`message_history.clear()`  
  
`cass_buff_memory = ConversationBufferMemory
( memory_key='chat_history', chat_memory=message_history )`  
  
`template = ''' You are the guardian of tales, and it
 is your duty to guide a wanderer through their chosen adventure. Today, a new seeker has arrived, eager to carve out a 
story of their own making. First, please ask the seeker to choose a name for their character. This name will be used thr
oughout the journey to personalize their experience. Next, ask them to select a genre from the following options: fantas
y, sci-fi, mystery, or horror. The chosen genre will shape the world and the challenges they encounter. Once the charact
er's name and genre are established, begin narrating their adventure. Throughout the journey, use this format to guide t
he interaction.`  
  
`Here are some guidelines to ensure a dynamic and engaging experience:`  
  
`Start by asking 
the player to choose some kind of weapons that will be used later in the game.`  
  
`Design several paths within the 
chosen genre that lead to different outcomes, some successful and others perilous.`  
  
`Some paths should lead to de
ath. If the character dies, provide a detailed account of what led to this end and conclude with the phrase: 'The End.' 
This will signal the conclusion of the game.`  
  
`Here is the chat history, use this to understand what to say next:
 {chat_history} Human: {human_input} AI:`  
  
`Your role is to weave the narrative threads based on the decisions of 
the character, creating a branching story that reflects the consequences of their choices. Your objective is to make the
 tale immersive and reactive, allowing the character to truly feel the weight of their decisions. '''`  
  
`prompt = 
PromptTemplate( input_variables=['chat_history', 'human_input'], template=template )`  
  
`llm = OpenAI(openai_api_ke
y=OPENAI_API_KEY) llm_chain = LLMChain( llm=llm, prompt=prompt, memory=cass_buff_memory )`  
  
`choice = 'start'`  

  
`while True: response = llm_chain.predict(human_input=choice) print(response.strip())`  
  
`if 'The End.' in resp
onse:`  
`break`  
  
`choice = input('Your reply: ')`  


A few of the runs look like these below. Bear in mind tha
t I have not yet typed in any decision; both the human and AI prompts have been filled automatically. Also notice how th
e narrative stops abruptly.  
  
Example 1:  
  
`Connected to Astra DB: []`  
`Let us begin this adventure.`  
 
 
`Human: My character's name is Aria.` 

`AI: Welcome, Aria. What genre shall your journey take place in? Will it be in
 the realm of fantasy, the depths of sci-fi, the mysterious world of mystery, or the chilling realm of horror?`  
  
`
Human: Fantasy.` 

`AI: A wise choice, Aria. In this world of magic and wonder, you will encounter many challenges and f
oes. But first, please choose your weapon. Will you wield a mighty sword, a powerful staff, or perhaps a trusty bow and 
arrows?`  
  
`Human: I choose a sword.` 

`AI: A brave choice, Aria. With your sword in hand, you venture forth into 
the fantastical world. As you travel through the enchanted forest, you come across a fork in the road. To the left, a we
ll-worn path leads to a bustling town, while to the right, a narrow trail disappears into the darkness of the forest. Wh
ich path will you choose?`  
  
`Human: I will go left, towards the town.` 

`AI: As you enter the town, you are greet
ed by the friendly townsfolk. They tell you of a powerful dragon that has been terrorizing the village and ask for your 
help in defeating it. Will you`

`Your reply:`  
  
Example 2:  
  
`Connected to Astra DB: []`  
`Human: My charac
ter's name is Aria and I would like to play in the fantasy genre.` 

`AI: Welcome, Aria, to the world of fantasy. As a n
ewcomer, you must choose your weapons carefully. Will you wield a sword, a bow, or perhaps a magical staff?` 

`Human: I
 choose a magical staff. AI: A wise choice, Aria. Your magical staff can conjure spells and enchantments to aid you on y
our journey. Now, let us begin your adventure. You find yourself in a lush forest, surrounded by tall trees and the soun
d of birds chirping. As you take in your surroundings, you hear a faint cry for help in the distance. What will you do?`


`Human: I will follow the cry for help.` 

`AI: You follow the sound to a clearing and find a group of villagers being
 attacked by a group of goblins. They plead for your assistance. Will you use your magical staff to cast a powerful spel
l or attempt to negotiate with the goblins?` 

`Human: I will use my magical staff to cast a spell.` 

`AI: Your spell s
uccessfully defeats the goblins and the villagers thank you for your bravery. They offer you a reward for your assistanc
e. Will you accept their offer or continue on your journey?` 

`Your reply:`

&#x200B;
```
---

     
 
all -  [ Released my first video on YT: Little tutorial about how to build a ChatGPT clone using an open sour ](https://www.reddit.com/r/reactnative/comments/1cgf3om/released_my_first_video_on_yt_little_tutorial/) , 2024-05-01-0911
```
Hey guys,   
Just released my first video on YT, little tutorial to build a similar ChatGPT app using an Open Source LLM
 (Mistral 7B & Ollama), you'll be able to:   
👉 Incorporating an open-source large language model (Langchain, Ollama, Mi
stral 7B) into your React Native project   
👉 Implementing straightforward user authentication with Firebase   
👉 Utiliz
ing NativeWind (TailwindCSS for React Native) for stylish app designs   
👉 Streaming AI responses in real-time just like
 ChatGPT using SSE  
Let me know what you think [https://youtu.be/yruNk7EqzEA](https://youtu.be/yruNk7EqzEA)
```
---

     
 
all -  [ Langtrace - Just added support for Langgraph ](https://www.reddit.com/r/LangChain/comments/1cgbwzx/langtrace_just_added_support_for_langgraph/) , 2024-05-01-0911
```
Hey Everyone,

I have been playing with Langgraph recently and it's awesome. There are some native ways to visualize the
 graph that you are building using Langgraph, which I ended up using multiple times as I was developing some agentic wor
kflows. Its useful to see the graph as you are developing and debugging it. I kinda thought it would be nice to have Lan
gtrace show the graph and decided to add support for it.

Wanted to show a quick preview of it. Excited for you all to t
ry it out and leave your feedback.

https://reddit.com/link/1cgbwzx/video/zbt44qozqhxc1/player
```
---

     
 
all -  [ My output from the langgraph is listed below, Now I want to access 'Anomaly_output', but when I try  ](https://www.reddit.com/r/LangChain/comments/1cgatw8/my_output_from_the_langgraph_is_listed_below_now/) , 2024-05-01-0911
```
'[(ToolAgentAction(tool=\'anomaly_detection\', tool_input={\'input\': \'df\'}, log='\\nInvoking: `anomaly_detection` wit
h `{\'input\': \'df\'}`\\n\\n\\n', message_log=[AIMessageChunk(content=\'\', additional_kwargs={\'tool_calls\': [{\'inde
x\': 0, \'id\': \'call_IvcL8ZQM7UhKBQVEmgkvC4s4\', \'function\': {\'arguments\': \'{'input':'df'}\', \'name\': \'anomaly
_detection\'}, \'type\': \'function\'}]}, response_metadata={\'finish_reason\': \'tool_calls\'}, id=\'run-f227a1be-c321-
43f5-92b6-bd7b9d8d0492\', tool_calls=[{\'name\': \'anomaly_detection\', \'args\': {\'input\': \'df\'}, \'id\': \'call_Iv
cL8ZQM7UhKBQVEmgkvC4s4\'}], tool_call_chunks=[{\'name\': \'anomaly_detection\', \'args\': \'{'input':'df'}\', \'id\': \'
call_IvcL8ZQM7UhKBQVEmgkvC4s4\', \'index\': 0}])], tool_call_id=\'call_IvcL8ZQM7UhKBQVEmgkvC4s4\'), {\'Anomaly_output\':
 [{\'USUBJID\': \'MAXIS-008-088\', \'AGE\': 25, \'PFS_MONTHS\': 3, \'SURVIVAL_MONTHS_FD\': 14, \'HEIGHT\': 169.0, \'WEIG
HT\': 51.4, \'BMI\': 18.0, \'RESP_RATE\': 19.75, \'TOBACCO_RATE\': 0.5, \'TUMOUR_SIZE\': 70.4, \'TUMOUR_SIZE_EOT\': 82.3
, \'CHEST_PAIN_N\': 1, \'COUGH_BLOOD_N\': 1, \'OVERALL_QUALITY_LIF_N\': 6.0, \'variable\': \'AGE\'}]})]'
```
---

     
 
all -  [ What are the best embeddings models for a specific domain? ](https://www.reddit.com/r/LangChain/comments/1cga0s7/what_are_the_best_embeddings_models_for_a/) , 2024-05-01-0911
```
Hello guys!  
Im working on a project in which i have two arrays:  
\- one with requirement(strings)  
\- another with a
 person's skills(strings)

I take these arrays and embedd them and then calculate the cosine similarity between them, in
 order to get the best skill for each requirement.

I was exploring the realm of embeddings and i'm at a point in which 
i don't really know if the models i'm using are the best ones. I saw that, for example, with instructor you can specify 
a domain but i didnt really see much of a difference.

What do you guys recommend in terms of models, and what do you th
ink about this methodology?  
Every time i see examples of embedding processes, i usually see people using long texts to
 then compare to others, but in this case i'm using only 'single' words, i. e. comparing NoSql to PostGreSql.

Thank you
 in advance.
```
---

     
 
all -  [ Should I create my own LLM?  ](https://www.reddit.com/r/LangChain/comments/1cg6l7p/should_i_create_my_own_llm/) , 2024-05-01-0911
```
I currently am looking forward to build a chatbot that scrapes data from websites (and updates the dataset dynamically) 
of different Universities. I am trying to build something that will help students to know more about the admissions and 
stuff.   
  
Although, I don't want to build it using RAG as it will be simple (I am doing this for my Final Year Projec
t, so I guess it should be good and something phenomenal). So, do you guys think building my own LLM would help my chatb
ot? It would definitely help in my learning curve, but am I going in the right track? There's this 5+ hours long video o
f FreeCodeCamp on Youtube, should I just start building my own LLM for this? 

What do I do? I legit think I am screwed,
 because I have some experience in creating chatbots and honestly, it is not a Final Year Project worthy, unless I do so
mething insane. I cannot change the project now as its already started, I need to submit reports that explains the whole
 model of this project.   
  
  
NEED EXPERT OPINIONS!
```
---

     
 
all -  [ Any value add to CrewAI if I get really proficient with Langchain? ](https://www.reddit.com/r/LangChain/comments/1cg5yca/any_value_add_to_crewai_if_i_get_really/) , 2024-05-01-0911
```
I have been looking into/using/learning both CrewAI and Langchain for the past week or so, and I am wondering if there i
s any value add to using CrewAI over just building out a given workflow in Langchain? It seems like CrewAI is just a lay
er of abstraction over Langchain - is this essentially accurate? How difficult is it to essentially replicate similar pr
ocesses in Langchain as in CrewAI?

Assume from the perspective of a generally proficient software dev - writing more co
de or working granularly is not really a huge issue to me
```
---

     
 
all -  [ Help with my final project ( langchain llms documents)  ](https://i.redd.it/2f0nbiu3dgxc1.jpeg) , 2024-05-01-0911
```
Hi everyone, this is going to be a long post so please read through it and help me out it’ll mean a lot.

I’m in my fina
l year BTech CSE from a small college and for my major project I was teamed up with only one girl who is the college top
per and as she’s interning rn none of the faculties are saying anything and I’m having to go to the reviews alone and I’
m not able to complete the project or documentation and the faculty is scolding me and idk what to do please help me out
. I need to publish a research paper also by the end of may.

So for my final graduation project due to some circumstanc
es I have taken the project “text summarisation and questions generation using langchain” where in we upload a document 
and it generates a summary and then generates questions ( like multiple choice, short answer, long answer, etc) and the 
student can practice questions before the exam kind of. A thing. How do I approach it? How do I work towards the project
. The main issue is my teammate isn’t working with me and I’m left alone trying to figure the project out and I don’t ha
ve much time. Please help me out
1) how do I approach it and what all should I learn or do to make the project
2) I’m no
t able to run llama2 api to summarize my docs as many errors are occurring so it must be some mistake on my part
- shoul
d I buy the open api tokens and work with it? 
- how do I approach the project please please please help me I’m in despe
rate need for help. 
( this is the basic front end I developed and any help will be appreciated) 
```
---

     
 
all -  [ Help with my project ](https://i.redd.it/aa8xlxgdcgxc1.jpeg) , 2024-05-01-0911
```
Hi everyone, this is going to be a long post so please read through it and help me out it’ll mean a lot

So for my final
 graduation project due to some circumstances I have taken the project “text summarisation and questions generation usin
g langchain” where in we upload a document and it generates a summary and then generates questions ( like multiple choic
e, short answer, long answer, etc) and the student can practice questions before the exam kind of. A thing. How do I app
roach it? How do I work towards the project. The main issue is my teammate isn’t working with me and I’m left alone tryi
ng to figure the project out and I don’t have much time. Please help me out
1) how do I approach it and what all should 
I learn or do to make the project
2) I’m not able to run llama2 api to summarize my docs as many errors are occurring so
 it must be some mistake on my part
- should I buy the open api tokens and work with it? 
- how do I approach the projec
t please please please help me I’m in desperate need for help. 
( this is the basic front end I developed and any help w
ill be appreciated) 
```
---

     
 
all -  [ Looking for a technical co-founder ](https://www.reddit.com/r/LangChain/comments/1cg35pn/looking_for_a_technical_cofounder/) , 2024-05-01-0911
```
I have an idea for an AI influencer platform that allows content creators to create digital clones of themselves for the
ir fans to interact with. Think Cameo or Onlyfans but entirely AI. 

Short term, it's relatively straight forward: a per
sonified chat bot with voice cloning/calling and consistent character image gen. Really just piecing different providers
 together like an LLM + 11labs + deepgram + stable diff. Want to keep the MVP pretty simple so we can ship fast and test
 product-market fit. 

Have already connected with nearly a dozen content creators who seem keen for something exactly l
ike this. But frankly, I'm a terrible dev. My strengths lie in at distribution, UX design, operations, and overall strat
egy. So I'm looking for a technical co-founder to build the MVP with. 

Don't really care about your background. As long
 as you're obsessive, just comment or shoot me a DM and let's see how far we can take this!
```
---

     
 
all -  [ How do I read files inside a directory present in an S3 bucket in such a way that I can read the PDF ](https://www.reddit.com/r/LangChain/comments/1cg327p/how_do_i_read_files_inside_a_directory_present_in/) , 2024-05-01-0911
```
In this below code, I want to make use of  so that I can retrieve metadata/ source URL from the documents: `docs = text_
splitter.split_documents(data)`

`s3_client = boto3.client('s3')`

`extracted_text = ''`

`bucket_name=<bucket-name>`

`
folder_name=<dir-name>`

`objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)`

`for obj in obje
cts['Contents']:`

`if obj['Key']!=folder_name:`

`obj = s3_client.get_object(Bucket=bucket_name, Key=obj['Key'])`

`dat
a = (obj['Body'].read())`

`pdf_file = PyPDF2.PdfReader(BytesIO(data))`

`for page_num in range(len(pdf_file.pages)):`


`page = pdf_file.pages[page_num]`

`extracted_text += page.extract_text()`

`data= // data pre-processing //`

`text_spl
itter = RecursiveCharacterTextSplitter(`

`chunk_size = 256,`

`chunk_overlap = 16)`

`docs = text_splitter.split_text(d
ata)`
```
---

     
 
all -  [ How to start with Multi Agents AI Orchestration ](https://www.reddit.com/r/LangChain/comments/1cg2hz1/how_to_start_with_multi_agents_ai_orchestration/) , 2024-05-01-0911
```
Hello,
I am new to LLM and GenAI , previous experience is into predictive modeling using structured data and NLP.
I see 
a lot of things in GenAI area and thinking of picking Multi Agent framework and wanted opinion of you geniuses ?
Thanks
```
---

     
 
all -  [ RAPTOR and PDF technical documents ](https://www.reddit.com/r/LangChain/comments/1cg1ov6/raptor_and_pdf_technical_documents/) , 2024-05-01-0911
```
I am trying to embed some technical documents, since they are very technical i need to have the best embedding technique
 possible, so that i can optimize the retrieval procedure as much as possible. If i just convert the technical documents
 to text embed them and store them inside the Chroma db, i notice than many times when i ask a question , it misses to f
etch the proper answer, although the answer is embedded inside the db. For this reason i decided to try and implement RA
PTOR method. But till now i see that it is ultra slow and it causes me problems. Has anyone tried raptor? Is it as good 
as it being mentioned and do you have a big improvement in your rag app?Do you have any example of implementing raptor w
hich i can try?

  
Thank you in advance.
```
---

     
 
all -  [ Loading csv files which have categorical data and numeric values into a graph to be used in RAG LLM  ](https://www.reddit.com/r/LangChain/comments/1cfzyzr/loading_csv_files_which_have_categorical_data_and/) , 2024-05-01-0911
```


Hey all,   

I would like to know how I should go about this. I have lots of  census data to work with, hundreds of th
ousands of rows. The fields are  things such as: age, sex, location, poverty, education and so on. My  goal is to load a
ll this data into a graph using some ontology and then  create a chatbot that allows the user to ask questions regarding
 the  data, such as 'Which state has the younger population?', 'Which tract  has the highest rate or poverty and oldest 
population?' and others. I  think using a RAG setup makes sense, but would like to if what  approaches I could take. I p
lan to load the data sources into a graph  and use that as context for feeding it into the LLM/RAG for the chatbot.  Thi
s initial dataset I am looking at starts with geographic components  such as if it is U.S. territory/non-territory, stat
e, county, tract. I  was thinking of having my ontology/scheme be that of geography. So there  would be 50 states + terr
itory nodes, then a node connected to county,  then a node connected to tract, then all the tracts would connect with  a
ll the thousands of observations. And I would store age, sex, poverty,  education as a property in the tract nodes. I'd 
also need the ability to  later add in other data to the graph about these states. Ultimately, I  want to understand the
 disparities of these communities by using  multiple data sources layered on top of each other then use natural  languag
e to query to data and have that go through the LLM/RAG which  then uses the graph for context in the response.   

Is t
his possible? Is this the right way to go about it?   

Thanks   
```
---

     
 
all -  [ What does the langchain architecture look like for this simple use case? ](https://www.reddit.com/r/LangChain/comments/1cfzk44/what_does_the_langchain_architecture_look_like/) , 2024-05-01-0911
```
I am new to LangChain. I have a use case / flow as follow:

  
A chatbot asistence firstly asks the user to provide link
s of some products they used in the past.

The asistence can advice the customer which varient of the product is suitabl
e for them based on the content of links the user provide and also the current available products catelogs in my website
. 

What does the langchain architecture look like for this simple use case? I will focus on learning those langchain co
mponent and tool to make this chatbot possible.

Shoud I use agent with various tools?

I understand I can use a webLoad
er to load the content from the user-provided links, split it, convert it with embedding model and store it in vector st
ore. The information I want to exptract from these product links are small and I can only do the web scraping and embedd
ing dynamically when the user provide the links.
```
---

     
 
all -  [ Configuring Ollama ](https://www.reddit.com/r/ollama/comments/1cfxacr/configuring_ollama/) , 2024-05-01-0911
```
Noob operating in the deep end of my pool. On windows 10, playing around with RAG and langchain using python.

I have a 
script that takes a local repo and chunks that for embedding with a FAISS db. Everything works fine with whatever LLM is
 choose (OpenAI or Ollama). My problems begin with embeddings. If I use OpenAI embeddings everything is ok but if I try 
Ollama using nomic-embed-text, the embedding speed slows down to less than a crawl. I let it run for two days and it was
n't finished. The repo is Autogen so it's a decent size (14,000 chunks) but OpenAI was finished in 5 minutes and Ollama 
is local so WTF?

I noticed that barely any of my measly 4gb of vram is being used, but it is definitely being used for 
the embeddings.

Is there a way to 'configure' Ollama to use more resources? 
```
---

     
 
all -  [ LangChain RunnableWithMessageHistory not storing tool_calls ](https://www.reddit.com/r/LangChain/comments/1cfwuws/langchain_runnablewithmessagehistory_not_storing/) , 2024-05-01-0911
```
I am using the following code (sanitized example):

    session_manager = RedisChatMessageHistory(
    str(session_id), 
redis_url, key_prefix='chat_history', ttl=3600, # TODO: add as configuration )
    prompt = ChatPromptTemplate(
        
input_variables=['input', 'chat_history'],
        messages=[
            SystemMessagePromptTemplate(
                p
rompt=PromptTemplate(input_variables=[], template=system_message)
            ),
            MessagesPlaceholder(variabl
e_name='chat_history', optional=True),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
            Hu
manMessagePromptTemplate(
                prompt=PromptTemplate(input_variables=['input'], template='{input}')
         
   ),     
        ]
    )
    
    _agent = create_openai_tools_agent(
        llm=llm,
        tools=tools,
        pr
ompt=prompt,
    )
    
    agent = AgentExecutor.from_agent_and_tools(
        agent=_agent,  # type: ignore
        to
ols=tools,
        early_stopping_method='generate',
        callbacks=callbacks, # type: ignore
        verbose=_verbos
e,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
    )
    
    agent_with_message_history
 = RunnableWithMessageHistory(
        agent,  # type: ignore
        session_manager.get_session_history,
        input
_messages_key='input',
        history_messages_key='chat_history',
    )

Then I run it:

    agent_response = await ag
ent_with_message_history.ainvoke(
        {'input': input, 'ability': 'test'},
        {
            'configurable': {'s
ession_id': session_manager.session_id},
            'callbacks': callbacks 
        },
    )

My output chat\_history c
omes with something like this:

    [
        HumanMessage(content='ok - test, call the product tool with argument test 
and answer 123 if it works'),
         AIMessage(content='123')
    ]

Note that the AIMessage does not have the tool\_c
alls argument

and the Redis register is like this:

    { 'type': 'ai', 'data': { 'content': '123', 'additional_kwargs'
: {}, 'response_metadata': {}, 'type': 'ai', 'name': null, 'id': null, 'example': false, 'tool_calls': [], 'invalid_tool
_calls': [] } }

Has anyone ran in a bug like that before?  
Any idea why it is happening?

The problem of this is that 
it keeps calling the same function over and over without being aware it already called it

Thank you very much in advanc
e for your attention and help :)
```
---

     
 
all -  [ Using Langchain with SillyTavern ](https://www.reddit.com/r/SillyTavernAI/comments/1cfwf79/using_langchain_with_sillytavern/) , 2024-05-01-0911
```
Hi y'all! Pretty new to all the AI and LLM stuff.

So, my objective is an AI assistant, i've chosen SillyTavern cuz of t
he integration with stuff like xtts and VRM

But now im kinda stuck. I have the character ready with TTS, (i still need 
to add STT lol), VRM and all the other stuff, so i started researching on API Calls

It seems Langchain is the easier op
tion, though im not sure it can be done that way (I haven't seen anything similar to what i want [Sillytavern and Langch
ain together])

I'm currently using OobaBooga as the back-end, and they have an extension for API Calling, but i've seen
 people saying it doesn't work with the api flag

Any ideas, solutions or guides are appreciated, and thanks for reading
!
```
---

     
 
all -  [ 'fine-tuning' routes ](https://www.reddit.com/r/LangChain/comments/1cfw2p8/finetuning_routes/) , 2024-05-01-0911
```
Is there any way to fine-tune / optimize routes via examples I give it? So I have an input and the agent decides which t
ool to use based on the routing that I've trained. 

I've seen a framework (semantic-router) do this but it seems fairly
 new and they aren't very transparent about what goes on under the hood.
```
---

     
 
all -  [ switch from the Testing field to Data engineer ](https://www.reddit.com/r/LangChain/comments/1cfuc06/switch_from_the_testing_field_to_data_engineer/) , 2024-05-01-0911
```
Hi guys, I would like to get your help regarding my case. I have been working as a software testing engineer for almost 
12 years. I have a solid Python and JS background. I found that the LLM is very interesting for me. I checked a lot of t
utorials about building my own RAG using langchain or lamaindex. I liked it  and I found the potential of jobs is start 
raising in the market.   


I'm thinking about start shifting to this new field but I'm not sure how can I cut the gap b
twn me and the required skills for these positions.   


What should I really know to be able to build a solid portfolio
? 
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-01-0911
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-05-01-0911
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-05-01-0911
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-05-01-0911
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-05-01-0911
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-01-0911
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-01-0911
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
