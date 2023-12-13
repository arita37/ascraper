 
all -  [ DeciLM-7B Instruct v Mistral-7B-Instruct-v01 on Chain of Thought ](https://www.reddit.com/r/LocalLLaMA/comments/18gxtey/decilm7b_instruct_v_mistral7binstructv01_on_chain/) , 2023-12-13-0910
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

     
 
all -  [ How can i preserve dictionary format through langchain agent for backend-frontend communication? ](https://www.reddit.com/r/LangChain/comments/18gw2v8/how_can_i_preserve_dictionary_format_through/) , 2023-12-13-0910
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

     
 
all -  [ I made an AI programming assistant that generates diagrams for your code ](https://v.redd.it/8idhfj4wbx5c1) , 2023-12-13-0910
```

```
---

     
 
all -  [ SQLagent customization in Langchain ](https://www.reddit.com/r/LangChain/comments/18guvv3/sqlagent_customization_in_langchain/) , 2023-12-13-0910
```
I am building a chatbot where I use SQLchain. If a user asks some question related to the db then it searches in the db 
(vehicle info ) and shows the results. e.g. if the user asks 'Show me the black BMW cars'. It shows. What I want is if t
here are no black BMW cars then it must show some similar records to the user like Audi black cars or Gray BMW cars etc.
 
```
---

     
 
all -  [ Towards LangChain 0.1 ](https://www.reddit.com/r/LangChain/comments/18gstp6/towards_langchain_01/) , 2023-12-13-0910
```
Some folks have noticed that we've been doing some refactors under the hood and moving stuff around, creating new packag
es like \`langchain-core\` and \`langchain-community\`. We wrote a (longish) blog describing why we did and plans for th
e future

[https://blog.langchain.dev/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-
to-langchain-v0-1/](https://blog.langchain.dev/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-an
d-a-path-to-langchain-v0-1/)

If people have questions or comments, can try to answer any here!
```
---

     
 
all -  [ Filter attributes in excel file ](https://www.reddit.com/r/LangChain/comments/18gpd00/filter_attributes_in_excel_file/) , 2023-12-13-0910
```
Hello all, I have some questions regarding my RAG application

1. I have an excel file I would like to 'chat' with, but 
it has over 30 attributes, and each attribute is pretty wordy, and I am not able to get good results with it. 

Currentl
y, I am using mistral LLM, Chroma as the vector store, and Cross Encoder for Reranking. Does anyone have any advice on h
ow to handle Excels with many attributes?

2. Is there a way I can filter the columns using a LLM before retrieval and s
earching
```
---

     
 
all -  [ Creating 'DynamicTool' with 'returnDirect: true' returns empty tokens ](https://www.reddit.com/r/LangChain/comments/18gou2z/creating_dynamictool_with_returndirect_true/) , 2023-12-13-0910
```
I am returning from the dynamic tool a long URL which is actually a S3 pre-signed URL for an image generated with Dalle3
 or SDXL. By not using returnDirect: true the long URL that get's returned from the function is very slowly returned, to
ken by token which is a very bad experience for the user.

So i stumbled upon this property returnDirect which i suppose
 that it should return directly the output of the function, but if i set it to true the handleLLMNewToken callback retur
ns multiple empty strings.

The tool and the chain are exiting with the correct output.

Have anyone else experienced th
is kind of behaviour?Any thoughts on how it can be solved?
```
---

     
 
all -  [ langchain apps with react native ](https://www.reddit.com/r/LangChain/comments/18gnpot/langchain_apps_with_react_native/) , 2023-12-13-0910
```
Any references/examples here where someone has used langchain to create a react native expo app ? or chatbot ? Looking f
or samples but not getting anything concrete.

&#x200B;

Kindly advise.
```
---

     
 
all -  [ [Local Llama] Avis pour l'hébergement auto-hébergeant LLMS ](https://www.reddit.com/r/redditenfrancais/comments/18gno4u/local_llama_avis_pour_lhébergement_autohébergeant/) , 2023-12-13-0910
```
Bonjour tout le monde. Je suis vraiment impatient d'essayer de jouer avec les LLM locales publiées ici, mais je me deman
de quel matériel est nécessaire pour avoir une expérience satisfaisante.

J'ai essayé GPT4ALL sur un ordinateur portable
 avec 16 Go de RAM, et il était à peine acceptable en utilisant vicuna. Certaines expériences avec Langchain et Wizardlm
 échouent parce que l'absence de GPU m'oblige à utiliser les données Float32, qui remplit rapidement mon RAM.

Je suis s
ur le point d'acheter un nouveau PC, donc j'apprécierais quelques conseils sur la création d'une configuration qui peut 
héberger ces modèles et me permettre de les expérimenter. Je veux aussi pouvoir gérer un grand IDE comme PyCharm pour le
 multitâche.

TLDR: Quel est le matériel minimum (et le budget) suggéré de commencer à expérimenter de manière satisfais
ante avec les différents LLM?

Veuillez partager vos pensées et vos expériences.

Merci beaucoup à tous ceux qui réponde
nt.

Traduit et reposté à partir de la publication 13sh0eh de la communauté localllama
```
---

     
 
all -  [ Seeking Advice for Optimizing Document Comparison ](https://www.reddit.com/r/LangChain/comments/18gmbym/seeking_advice_for_optimizing_document_comparison/) , 2023-12-13-0910
```
Hello Reddit community,

I'm working on an AI project where I have two documents that users query. These documents usual
ly contain the same information, but occasionally, there are slight differences in the details. For example:

* Document
 1 states: 'The latest smartphone model has a battery life of up to 18 hours and supports fast charging up to 65W.'
* Do
cument 2 states: 'The latest smartphone model has a battery life of up to 20 hours and supports fast charging up to 60W.
'

In cases like this, my goal is to identify the discrepancy and return the specific statements from each document. How
ever, if the information is identical, I simply return the answer.

So far, I've successfully transformed the documents 
into a vector database using FAISS and have implemented a querying system you can find below.

The system is functional,
 but I'm exploring ways to make it more efficient. I'm particularly interested in models that are specifically trained f
or sentence similarity, which might be more suitable for detecting subtle differences in data points, such as numerical 
values or measurements. Using something as robust as ChatGPT feels like overkill for this specific application.

In addi
tion to this, I'm seeking general advice on optimizing this process. Are there better ways to structure the code, more e
fficient algorithms to use, or other AI technologies that might be more apt for this task?

I would greatly appreciate a
ny insights, recommendations, or experiences you might have regarding models for sentence similarity or general optimiza
tion strategies in AI-driven document comparison tasks.

Thank you all in advance for your valuable input and assistance
!

    chain = load_qa_chain(OpenAI(), chain_type='stuff', verbose=True)
    docs = vectordb_vritual.similarity_search(q
uestion, 8)
    answer_virtual = chain.run(input_documents=docs, question=question)
    
    docs = vectordb_local.simil
arity_search(question, 8)
    answer_local = chain.run(input_documents=docs, question=question)
    
    answers = { 'an
swer1': answer_local, 'answer2': answer_virtual }
    
    client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY
'))
    
    system_prompt = 'The user will provide a JSON input containing two fields: answer1 and answer2. Your task i
s to ' \'analyze these answers and determine if they convey the same information, considering their context ' \'and key 
data points. Differences in numerical values, measurements, or other specific data are ' \'crucial and should be conside
red when making your assessment. The format of the text is not the ' \'primary focus, but the accuracy and consistency o
f the information presented are. Your output should ' \'be in JSON format with a single field result. Set result to true
 if the answers are essentially the ' \'same in context and key data, and false if they differ in important aspects such
 as figures, ' \'measurements, or other specific details.'
    
    completion = client.chat.completions.create(model='g
pt-3.5-turbo-1106',response_format={'type': 'json_object'},messages=[{'role': 'system', 'content': system_prompt},{'role
': 'user', 'content': str(answers)}],temperature=0.0)
    
    answer = completion.choices[0].message.content
    answer
_dict = json.loads(answer)
    
    result = answer_dict.get('result')
    
    if result:
    print('answers are the sa
me')
    print(answer_local)
    print(answer_virtual)
    else:
    print('answers are the not the same, this is local'
)
    print(answer_local)
    print('this is virtual')
    print(answer_virtual)

&#x200B;
```
---

     
 
all -  [ Langchain in Production ](https://www.reddit.com/r/LangChain/comments/18gih58/langchain_in_production/) , 2023-12-13-0910
```
To all the developers and practitioners, what are some things you wish you knew before deploying your langchain app in p
roduction?
```
---

     
 
all -  [ Costs incurred with create_csv_agent ](https://www.reddit.com/r/LangChain/comments/18gi5th/costs_incurred_with_create_csv_agent/) , 2023-12-13-0910
```
I'm trying to build a chatbot using langchain and openai's gpt which should be able to answer quantitative questions ask
ed by users on csv files. 

For example: What is the average sales for the period so and so?

I was thinking of using cr
eate_csv_agent for this purpose but I had a question. Does the size of the csv files inputted to the agent have an impac
t on the costs incurred? In other words, will larger csv files lead to more costs when using create_csv_agent?
```
---

     
 
all -  [ Azure Cognitive Search with LangChain. ](https://www.reddit.com/r/LangChain/comments/18ghqe9/azure_cognitive_search_with_langchain/) , 2023-12-13-0910
```
In Azure Search Service, I currently have an index and am looking to fetch documents using specific filters and search c
riteria. My objective is to integrate multi-query retrieval or fusion RAG capabilities with Azure Cognitive Search, util
izing LangChain. I'm interested in knowing if LangChain supports this functionality. Additionally, I aim to incorporate 
advanced features like hybrid and semantic search in my querying process.

I could not find how can I define the filters
 and search params while retrieving.
```
---

     
 
all -  [ How to get things done with agents ](https://www.reddit.com/r/LangChain/comments/18ghonr/how_to_get_things_done_with_agents/) , 2023-12-13-0910
```
Hi everybody, a newbie here. 

Thanks for the platform and help. I am trying to create a business assistant with agents 
from langchain, but I am getting stuck to create a multidisciplinary agent. Is works well with searching in databases, t
hen fail in forecasting or writing reports. I am using agents with tools, but my next steps will be custom tools and too
ls that are other agents indeed.

How to you manage to get things done? Which is the best approach that worked for you? 
Is about the agent type? Chain or skeleton of though? Is more precise prompting?
```
---

     
 
all -  [ How to chat with Website data | chatgpt model | chat with your own data| ](https://youtu.be/LdEOneIYFRM?si=rE2dU2Boi2AfD7Wh) , 2023-12-13-0910
```
Hello All

Check out my latest video on  chatting with own data using ChatGPT. 
 Whether you're new to tech or an AI ent
husiast, this video provides a code implementation of how to chat with website data using ChatGPT LLM  and langchain mod
els.  Watch, Learn, Subscribe and Share with your friends! 🎥✨ #Chatgpt  #LLM #langchain #GPT  #AI #NewVideo
```
---

     
 
all -  [ Help me format the Text/Code generated by LLM ](https://www.reddit.com/r/LocalLLaMA/comments/18gfw8x/help_me_format_the_textcode_generated_by_llm/) , 2023-12-13-0910
```
I am working on running Intel's neural chat model in Langchain locally on my machine.   


My usecase is to learn more a
bout Large Language models by hosting this model locally. The model will focus on helping me with code, theory and ideas
.  


I need help with following :-  
1. How shall my prompt look like? How shall I make it little generic so that it ge
nerates code and also answer theortical question.  
2. How to format the output when its a Python code and when its norm
al text/answer to my question?  


PS: Just started working with Langchains/LLMs last month.
```
---

     
 
all -  [ Why do I need a specialised vector DB? ](https://www.reddit.com/r/LangChain/comments/18g9gyh/why_do_i_need_a_specialised_vector_db/) , 2023-12-13-0910
```
It doesn’t feel that similarity search is the long pole in the tent compared to inference. It’s easy to write a cosine s
imilarity search in SQL, so why not use an existing MPP data warehouse to do this that scales this kind of query over TB
s of embeddings and at high concurrency? What am I missing?
```
---

     
 
all -  [ Happy Holidays! Here is your 100% free Large Language Model outline! ](https://www.reddit.com/r/learnmachinelearning/comments/18g24qv/happy_holidays_here_is_your_100_free_large/) , 2023-12-13-0910
```
 

Thanks for all of your support in recent days by giving me feedback on my LLM outline. This outline is a roadmap on h
ow to learn state-of-the-art stuff about Large Language Models. It builds on work that I have done at AT&T and Toyota. I
t also builds on a lot of work that I have done on my own outside of corporations.

The outline is solid, and as my way 
of giving back to the community, I am it giving away for free. That's right, no annoying email sign-up. No gimmicks. No 
stripe pages for a 'free trial.' No asking you to buy a timeshare in Florida at the end of the outline. It's just a link
 to a zip file which contains the outline and sample code.

Here is how it works. First, you need to know Python. If you
 don't know that, then look up how to learn Python on Google. Second, this is an outline, you need to look at each part,
 go through the links, and really digest the material before moving on. Third, every part of the outline is dense; there
 is no fluff, and you will will probably need to do multiple passes through the outline.

The outline is designed to sta
rt you with an approach to learning PyTorch, it gives a code example of how to do classifications with sentence embeddin
gs, and it also has another code example of how to run Zephyr in colab. The outline took me a couple of days to put toge
ther, but it really represents stuff from the past year.

Also, this is not an outline on fine tuning Language Models. I
t is not a discussion of Mistral MoE, and it is not a discussion of running multiple GPUs. It is designed for someone wh
o has a laptop and wants to learn.

Also, think of this outline as a gift. It is being provided without warranty, or any
 guarantee of any kind.

If you like the outline, I am begging you to hit that share button and share this with someone.
 Maybe it will help them as well. If you love the outline, take this as motivation to do good in the world and share som
ething you have done with the community.

Ok, here is the outline.

[https://drive.google.com/file/d/1F9-bTmt5MSclChudLf
qZh35EeJhpKaGD/view?usp=drive\_link](https://drive.google.com/file/d/1F9-bTmt5MSclChudLfqZh35EeJhpKaGD/view?usp=drive_li
nk)

If you have any questions, leave a comment in the section below. If the questions are more specific to what you are
 doing (and if they are not part of the general conversation), feel free to ask me questions on Reddit Chat.

&#x200B;


https://preview.redd.it/s46jelh4yp5c1.png?width=549&format=png&auto=webp&s=df015c4626217229c852e0b5693fd22fd28dc179

&#x
200B;

https://preview.redd.it/ashcuro5yp5c1.png?width=547&format=png&auto=webp&s=6a7d8a4a6988ca2c37c02f334b5ba4a73273f7
ac
```
---

     
 
all -  [ Chroma is a great open-source vector database option to use with your LangChain app ](https://www.reddit.com/r/LangChain/comments/18fyy5r/chroma_is_a_great_opensource_vector_database/) , 2023-12-13-0910
```
Hello 👋 

I’ve played around with [Milvus and LangChain last month](https://www.gettingstarted.ai/tutorial-how-to-integr
ate-milvus-vector-database-into-your-rag-llm-langchain-app/) and decided to test another popular vector database this ti
me: Chroma DB.

It’s open-source and easy to setup. [Here’s the full tutorial](https://www.gettingstarted.ai/tutorial-ch
roma-db-best-vector-database-for-langchain-store-embeddings/) if you’re using or planning on using Chroma as the vector 
database for your embeddings!

Here’s what’s in the tutorial:

- Environment setup
- Install Chroma, LangChain, and othe
r dependencies
- Create vector store from chunks of PDF
- Perform similarity search locally
- Query the LLM model and ge
t a response

I also went over how you could add metadata to an existing collection by updating it. 

Would love to know
 if you find this helpful and if you have any questions!

Cheers
```
---

     
 
all -  [ [Open Ai] Que pensez-vous de Langchain maintenant? ](https://www.reddit.com/r/redditenfrancais/comments/18fvwp2/open_ai_que_pensezvous_de_langchain_maintenant/) , 2023-12-13-0910
```
C'est l'aspect quelque peu cool (et difficile) du développement de la technologie en évolution rapide. Maintenant, avec 
les assez énormes annonces à Openai's Dev Day, pensez-vous qu'il est toujours utile d'utiliser Langchain? Vaut-il la pei
ne d'essayer d'intégrer des assistants dans les applications existantes à l'aide de Langchain ou est-ce qu'il vaut mieux
 aller de l'avant pour simplement utiliser l'API d'Openai directement et modifier en fonction de leur taux de développem
ent?

Traduit et reposté à partir de la publication 17txa9c de la communauté openai
```
---

     
 
all -  [ ollama local - smart file manager? ](https://www.reddit.com/r/LocalLLaMA/comments/18f8jwo/ollama_local_smart_file_manager/) , 2023-12-13-0910
```
I have installed ollama and am running llama2 and mistral-openorca with no issues from the command line. I 've seen arti
cles on training and on langchain. The computer is running ubuntu 22.04 new fresh install. hardware is aorus mb with ryz
en threadripper 24 core, 128 GB RAM, nvidia RTX 3060 w 12 GB VRAM, if it matters. 

Can i give local general file access
 to my local ollama AI instance and ask questions like - 'list all folders with pictures taken last year'? 

not sure wh
at i should be searching for as keywords when looking for help from this perspective.
```
---

     
 
all -  [ What are LLMs: Large language models explained? ](https://www.reddit.com/r/u_Sandya1209/comments/18ezefx/what_are_llms_large_language_models_explained/) , 2023-12-13-0910
```
[Large Language Models (LLMs)](https://www.optisolbusiness.com/insight/5-key-advantages-of-using-large-language-models-f
or-document-analysis)are AI systems designed to understand and generate human-like text. These models, with millions or 
billions of parameters, can answer questions, write essays, translate languages, and more. They’re created through two m
ain steps: pretraining, where they learn language from vast datasets, and fine-tuning, which tailors them for specific t
asks. LLMs are versatile and adaptable, making them valuable in numerous applications. However, their deployment raises 
concerns about bias, ethics, and misuse. Despite challenges, LLMs offer exciting opportunities for automating language-r
elated tasks and revolutionizing human-computer interaction. In this article, we will explore the key advantages of usin
g LLM for document analysis.

[**Large Language Models for Automated Document Analysis**](https://www.optisolbusiness.co
m/insight/5-key-advantages-of-using-large-language-models-for-document-analysis)

**Efficient Information Extraction**


* Large Language Models are exceptionally efficient at extracting pertinent information from a wide range of documents. 
Whether the content is unstructured text, images with text, or a mix of both, LLMs excel at quickly and accurately ident
ifying and isolating the relevant data.
* This is invaluable for tasks like data categorization, where LLMs can rapidly 
sift through large volumes of unstructured text or documents with embedded images to extract critical details.

**Multil
ingual Support**

* Many Large Language Models are designed to be multilingual, enabling them to[ ](https://www.optisolb
usiness.com/insight/harnessing-the-power-of-langchain-and-openai-gpt-3)analyze documents in multiple languages seamlessl
y. This eliminates the need for organizations to maintain separate models for each language, streamlining document analy
sis efforts, and making them particularly advantageous for global businesses and organizations that operate in diverse l
inguistic environments.

**Contextual Understanding**

* LLMs possess an innate ability to grasp the context within docu
ments. They go beyond simply identifying keywords and can discern nuances, relationships between words, and the overall 
meaning of sentences.
* This contextual understanding enhances their performance in more advanced document analysis task
s, such as sentiment analysis, where capturing the sentiment's context is crucial for accurate results.

**Consistency a
nd Scalability**

* Large Language Models ensure consistent document Document Analysis analysis results, reducing the po
tential for human errors and biases. Additionally, they are highly scalable, capable of handling large volumes of docume
nts efficiently. This scalability is especially valuable for enterprises that deal with a massive inflow of documents da
ily.

**Insights and Trends**

* LLMs have the capacity to uncover valuable insights and trends within documents. This c
apability is instrumental in guiding[ ](https://datalabs.optisolbusiness.com/portfolio/building-data-warehouse-and-drive
-actionable-insights)data-driven decision-making, refining marketing strategies, and extracting business intelligence fr
om the wealth of information contained in documents.

&#x200B;

https://preview.redd.it/7304sn6jlf5c1.png?width=300&form
at=png&auto=webp&s=aba8bfa9fc3e2ceb80f91ae716b92d4977ffb9e6
```
---

     
 
all -  [ SuperDuperDB - how to use it to talk to your documents locally using llama 7B or Mistral 7B? ](https://www.reddit.com/r/LocalLLaMA/comments/18eusc8/superduperdb_how_to_use_it_to_talk_to_your/) , 2023-12-13-0910
```
https://github.com/SuperDuperDB/superduperdb

This has only been released recently and already trending in github under 
LLM/AI category.

Would like to ask if anyone tried to use it to perform inferencing on your documents? Say 10 pages of 
text. How did it go? I'm planning to use LLAMA 2 7B or mistral 7B for it.

Thanks to u/opi098514 & u/TheWebbster and to 
all others who replied back, seems this tool is not really available at the moment. The tool is basic, upload my documen
t (text file), then create inference on it like an LLM.

Here are a few things that seem might work but with caveats.

1
) https://python.langchain.com/docs/use_cases/question_answering/ --> Feel free to check, though I am not sure if it wil
l consume $ from your OpenAI API tokens

2) ChatGPT Pro (though it can only ingest around 2-3 pages? then it will halluc
inate right after. It's not scalable).

3) ChatGPT Plugin - Same with #2, it will hallucinate after 2-3 pages. It's not 
scalable.

4) https://github.com/oobabooga/text-generation-webui/wiki -- oobabooga, this seems promising. Haven't tried 
it yet.

5) Langdroid - https://github.com/langroid/langroid/blob/main/README.md --> could this be it?




***Update:***
 This RAG Tool seems to have been requested countless times and there's a real business use case for this. Others are wi
lling to pay top dollar for, but let's not go there, let's built it with all the open source materials we have in our ow
n local hardware. Here's a past convo about it: https://www.reddit.com/r/LocalLLaMA/comments/16cbimi/yet_another_rag_sys
tem_implementation_details_and/
```
---

     
 
all -  [ I just had the displeasure of implementing Langchain in our org. ](https://www.reddit.com/r/LangChain/comments/18eukhc/i_just_had_the_displeasure_of_implementing/) , 2023-12-13-0910
```
Not posting this from my main for obvious reasons (work related).

Engineer with over a decade of experience here. You n
ame it, I've worked on it. I've navigated and maintained the nastiest legacy code bases. I thought I've seen the worst.


Until I started working with Langchain.

Holy shit with all due respect LangChain is arguably the worst library that I'
ve ever worked in my life.

Inconsistent abstractions, inconsistent naming schemas, inconsistent behaviour, confusing er
ror management, confusing chain life-cycle, confusing callback handling, unneccessary abstractions to name a few things.


The fundemental problem with LangChain is you try to do it all. You try to welcome beginner developers so that they do
n't have to write a single line of code but as a result you alienate the rest of us that actually know how to code.

Let
 me not get started with the whole 'LCEL' thing lol.

Seriously, take this as a warning. Please do not use LangChain and
 preserve your sanity. 
```
---

     
 
all -  [ What is needed in a comprehensive outline on Natural Language Processing? ](https://www.reddit.com/r/datascience/comments/18ejp1i/what_is_needed_in_a_comprehensive_outline_on/) , 2023-12-13-0910
```
I am thinking of putting together an outline that represents a good way to go from beginner to expert in NLP. Feel like 
I have most of it done but there is always room for improvement. 

Without writing a book, I want the guide to take some
one who has basic programming skills, and get them to the point where they are utilizing open-source, large language mod
els ('AI') in production. 

What else should I add to this outline?

&#x200B;

https://preview.redd.it/vyfy743jab5c1.png
?width=655&format=png&auto=webp&s=38576b1c4c349587e776061adebc576132914971

https://preview.redd.it/gaaeouimab5c1.png?wi
dth=633&format=png&auto=webp&s=d528cde4c444c8ed88d5fcd902830fb0a2629604
```
---

     
 
all -  [ Guys- anyone use Pinecone.from_documents, RecursiveCharacterTextSplitter.split_documents, etc. and a ](https://www.reddit.com/r/LangChain/comments/18ehcm7/guys_anyone_use_pineconefrom_documents/) , 2023-12-13-0910
```
I see Pinecone.from\_documents in the Langchain documents but I can't seem to find the relevant python file to understan
d the method.

Curious because when I collect all the chunked docs from RecursiveCharacterTextSplitter.split\_documents 
and OpenAIEmbeddings.embed\_documents I am getting 610 texts/vectors but after building the Pinecone Index for a specifi
c namespace (a subsection of the Index) and checking the properties of the namespace I see 1251 vectors there.

How else
 are people breaking down PDFs if not using from\_documents? I would like to see the actual method being run.
```
---

     
 
all -  [ Unit tests feedback loop ](https://www.reddit.com/r/LocalLLaMA/comments/18ede3y/unit_tests_feedback_loop/) , 2023-12-13-0910
```
Have you setup a feedback loop system with your local llama?
 like give prompt for creating code for a task, then automa
tically unit test the result from the model. If it is failed give the error back to the model ask to correct it.
And rep
eat the process until unit test successfull.
With  langchain etc..?
```
---

     
 
all -  [ Passing LangChain Objects from Server to Client Issues (Serialization) ](https://www.reddit.com/r/LangChain/comments/18e9f1u/passing_langchain_objects_from_server_to_client/) , 2023-12-13-0910
```
It seems like LangChain (python) in web applications comes with a lot of headaches due to serialization issues.

I keep 
trying to return things from the server side code to the client only to find that I'm unable to as they are non serializ
able.

For example:

Documents, AIMessages, etc

This means I manually have to go through and recreate/clean all these o
bjects when I want to pass them to the client.

Does anyone have a good solution around this?
```
---

     
 
all -  [ OpenAI assistant pricing vs API pricing ](https://www.reddit.com/r/LangChain/comments/18e25qx/openai_assistant_pricing_vs_api_pricing/) , 2023-12-13-0910
```
Today I was playing on openAI Assistant to get answers from a simple CSV file. After trying for 3 prompts, after which I
 did not really get any answers, the cost was 2$!!! which I think is high, compared to <1$ that used to cost when I was 
playing with API few months ago.

I am working on a recommendation app, where I will provide openAI api some of the data
 from my sql db and return openai suggestions to the end user. Now seeing the assistant price I feel like reverting back
 to using API as the assistants cost seem a bit steeper. Am I missing something, what are your thoughts?
```
---

     
 
all -  [ Are there any custom GPTs / Copilot bots trained on the latest LangChain docs? ](https://www.reddit.com/r/LangChain/comments/18dxn4b/are_there_any_custom_gpts_copilot_bots_trained_on/) , 2023-12-13-0910
```
Can’t ask vanilla GPT 4 since it’s past the training cutoff, and can’t make one myself cause, well, I can’t understand t
he docs
```
---

     
 
all -  [ memory in ConversationalRetrievalChain removed ](https://www.reddit.com/r/LangChain/comments/18dxc2o/memory_in_conversationalretrievalchain_removed/) , 2023-12-13-0910
```
Did something change in the most recent version of Langchain, i could have sworn that the ConversationalRetrievalChain t
ook a memory parameter and now its gone?

The docs have it [https://api.python.langchain.com/en/latest/chains/langchain.
chains.conversational\_retrieval.base.ConversationalRetrievalChain.html#langchain.chains.conversational\_retrieval.base.
ConversationalRetrievalChain.memory](https://api.python.langchain.com/en/latest/chains/langchain.chains.conversational_r
etrieval.base.ConversationalRetrievalChain.html#langchain.chains.conversational_retrieval.base.ConversationalRetrievalCh
ain.memory)  But the code errors out with a “bad key” error and there is no mention of memory in the source anymore.

`p
ydantic.v1.error_wrappers.ValidationError: 1 validation error for ConversationalRetrievalChain`

`memory  value is not a
 valid dict (type=type_error.dict)`

what is the current idiomatic way to do RetreivalQA RAG over private documents with
 history/memory now ?
```
---

     
 
all -  [ langchain agent does not return JSON files generated from tools ](https://www.reddit.com/r/LangChain/comments/18dv7wx/langchain_agent_does_not_return_json_files/) , 2023-12-13-0910
```
hi guys,

I have two RAG chains for 2 different types of answers. One of the chains is instructed to generate json and i
t works well by iteself.

    json_instruct='''
    [INST] <<SYS>>
    You are a helpful and concise assistent, that onl
y comunicates using JSON files.
    The expected output from you has to be: 
        {
            'cookware_name': {coo
kware},
            'description': [],
            'ai_notes': {explanation}
        }
    The INST block will always be
 a json string:
        {
            'prompt': {the user prompt}
        }
    The available cookwares are in the conte
xt given to you
    
    <</SYS>> [/INST]
    
    '''
    
    
    JSON_pipeline = RetrievalQA.from_chain_type(
      
  llm=CustomLLM(system_instruction=json_instruct), chain_type='stuff',
        retriever=cookware_retriever
    )
    
 
   JSON_pipeline('what do i need for crepes')

But when i put these 2 chains into a langchain agent, the agent would acc
urately send a prompt to the json chain but return answers in regular sentences. The agent is defined as :

&#x200B;

  
  tools = [
    
    # tool 1
        Tool(...),
    
    # tool 2
        Tool(
            name = 'JSON data',
       
     func=JSON_pipeline.run,
            description = '''
            Useful for you need to answer questions about wha
t a certain cookware is or 
        what cookware is needed for certain dishes. 
            ''',return_direct=True
    
         )
              ]
    
    llm_chain = LLMChain(llm=CustomLLM(system_instruction='You are a helpful and fast as
sistant.'), prompt=prompt)
    
    
    tool_names = [tool.name for tool in tools]
    
    agent = LLMSingleActionAgen
t(
        llm_chain=llm_chain,
        output_parser=output_parser,
        stop=['\nObservation:'],
        allowed_to
ols=tool_names
    )
    
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True
)
    
    agent_executor.run('list useful cookwares for soup')

&#x200B;

The answer is indeed a list useful cookwares 
based on the documents. But it's no longer in a JSON format that was generated by the JSON\_pipeline

Is there any way I
 can make the agent keep the answers as provided by the tools without modifying the answers by the central 'router' LLM?
 (Or am I missing out some parameters?)

&#x200B;

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ The Elasticsearch developer survey is here! If you build an app with search and/or gen AI, consider  ](https://www.reddit.com/r/LangChain/comments/18dsx62/the_elasticsearch_developer_survey_is_here_if_you/) , 2023-12-13-0910
```
Survey here → [https://survey.alchemer.com/s3/7626156/ES2412p](https://survey.alchemer.com/s3/7626156/ES2412p)
```
---

     
 
all -  [ Pushing the Limits of RAG: Seeking Insights on Embedding Models for Next-Level AI Performance ](https://www.reddit.com/r/datascience/comments/18dpiq2/pushing_the_limits_of_rag_seeking_insights_on/) , 2023-12-13-0910
```
 I've been digging into the data science world for a good while now, constantly looking for new ways to make AI and big 
data play nice together. When I'm not on the grind, I love to tinker with fresh AI tools and frameworks to keep up with 
the fast-moving tech scene.

Lately, I've noticed a surge in discussions around Retrieval-Augmented Generation (RAG) acr
oss various platforms like Twitter, tech blogs, and YouTube tutorials. The process seems straightforward - using Langcha
in or Llamaidnex,  take some text, chunk it, insert it into a vector database, integrate your preferred LLM, and bam, yo
u've got yourself an RAG System.

But here's the catch: those popular frameworks oversimplify things, leading many to un
derestimate the importance of the underlying details. This misconception becomes a roadblock when unexpected challenges 
arise in projects due to the nuances of implementation.

Currently, I'm deeply involved in a project that's testing the 
boundaries of RAG's capabilities, particularly in enhancing efficiency and accuracy for extensive searches. However, I'v
e encountered a few hurdles where community wisdom would be invaluable. I recently came across a blog from Llamaindex di
scussing various embedding models, and I'm curious about your experiences:

* What are the primary challenges you face w
ith the current implementation of RAG?
* Have any of you experimented with those embedding models, such as [Open AI's ad
a](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings), [Jina Embeddings](https://go.jina.ai/reEmbed
dingsBaseEN), and other embedding models in the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) …
* H
ow do you anticipate the Embedding model could assist in your RAG implementation?
* Are there specific metrics or result
s you hope to achieve with an improved Embedding model? My aim is to enhance accuracy and expedite processing.

I'm eage
r to hear your insights, experiences, and advice. Let's collaborate to push the boundaries of what's possible in AI and 
data science!
```
---

     
 
all -  [ 70B Model in Langchain with llama.cpp ](https://www.reddit.com/r/LocalLLaMA/comments/18dodgv/70b_model_in_langchain_with_llamacpp/) , 2023-12-13-0910
```
Hello everyone,

I just started out with local LLMs, and I guess I am missing some elemental component.

I want to run a
 70B model from Huggingface: https://huggingface.co/LeoLM/leo-hessianai-70b-chat

I know I need to quantize it, to make 
it work. Even though I have 95GB of VRAM and about 160GB of RAM available. But I need fast inference.

So I opted to qua
ntize it to 6 bits using llama.cpp.

However, when i download the model I get 15 hugest files (.bin) and a tokenizer.jso
n, alongside some other stuff.

What would be the line to get this thing quantized? I used: python convert.py models/Leo
M to no avail.

I guess without any flags the standard quantization is also below my needs.

So if that worked and I got
 a gguf file, how would I get the gguf to run in langchain without additional bloatware?

Is there a tutorial that I am 
missing?

Thank you
```
---

     
 
all -  [ Attaching files to user prompt when using LangChain OpenAI Assistant API ](https://www.reddit.com/r/LangChain/comments/18dloff/attaching_files_to_user_prompt_when_using/) , 2023-12-13-0910
```
I am using LangChain with Python, specifically this part of the API for Open AI Assistants - [https://python.langchain.c
om/docs/modules/agents/agent\_types/openai\_assistants](https://python.langchain.com/docs/modules/agents/agent_types/ope
nai_assistants) 

 How do I attach files to user prompts? 

Looking at the following code - 

    from langchain.agents 
import AgentExecutor
    
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    agent_executor.invoke({'conte
nt': 'What's the weather in SF today divided by 2.7'})

The content property of the object that is being passed into the
 invoke function has the user prompt - what we are sending to the assistant. But in addition to text prompts, it is also
 possible to send files to the assistant in a user prompt. In the OpenAI Assistants Web UI, there is an attach file butt
on. With the official OpenAI Assistants API, I am able to upload the file to OpenAI's file system and then attach the fi
le via the file ID that is generated.

How can I attach files to a user prompt with the LangChain OpenAI Assistant API? 
The documentation doesn't seem to mention how I can do this from what I've read.

Thank you.
```
---

     
 
all -  [ Structure of embeddings for complex objects / how to interact with structure in langchain ](https://www.reddit.com/r/LangChain/comments/18djyo6/structure_of_embeddings_for_complex_objects_how/) , 2023-12-13-0910
```
Hi there, I am looking to implement a RAGish use case with python and langchain. Want to share my high level plan here a
nd ask for your feedback. 

Process roughly is as follows

* Access a catalog of large, complex and semi-structured obje
cts. Each object consists of some string attributes and contains multi-level list objects. The 'payload' often is format
ted as JSON (not sure yet whether I should extract more attributes or just hope that the LLM can allow queries also on t
he insides of that JSON). I created a python class that represents that structure
* Next step is to create embeddings (u
sing langchain & Chroma for now). Here I am unsure how to proceed. At least I want to have a dedicated embedding of each
 of my catalog items. Use case will be, that users present their use case (like 'where do i find information on attribut
e XYZ?'). I want the LLM to return the suitable catalog item. But almost more important, I want the LLM to look inside t
he catalog item, look at all attributes and evaluate whether a certain attribute suits (rather than the whole catalog it
em). 
   * Q: Should I embed each catalog item as one entry or rather create embeddings on artifact level? If so, how do
 I maintain reference to the catalog item? I could duplicate relevant catalog item information of course for each attrib
ute. 
   * Q: Already thinking of retrieval (plan to use in retrieval chains). I do foresee that user queries may not be
 straight forward enough. I may need an agent that guides the user through her query (like U: 'where do i find informati
on on attribute XYZ?' -> S: 'Help me to understand more about your use case: Which parts of the catalog are you interest
ed in? Rather A or B or C?' -> ...). For that I need to make the LLM aware of both, the catalog structure and the inside
s of a catalog item. Can I do that with just 'flat' embeddings? 
* Once the embeddings are done, I want to use them as {
context} with langchain. I first want to try how far I can get with chains. 
   * Q: Any experience / examples on how to
 define prompts in a way that I can use information from context? Can I explicitly reference metadata information someho
w? Like 'system message: You´re an expert on the catalog from {context} and want to recommend discrete items. You should
 always use the {name} and {summary} in your recommendations'. Additionally, if i index each catalog item separately, I 
need to look into the items´ structure, like 'system message: In your recommendations please always list the output para
meters of the method of a catalog item that made you pick this recommendation'. Is that likely to work? 
* Some high lev
el assessment of how far I can get with chains or whether I should use agents for my case would be very helpful as well.
 

Thanks already for the discussion!

&#x200B;
```
---

     
 
all -  [ Random search on vectorstore ](https://www.reddit.com/r/LangChain/comments/18dj6ep/random_search_on_vectorstore/) , 2023-12-13-0910
```
I need to randomly select some documents from a langchain vectorstore. Is there any process for that. 
One solution is t
o generate a random embedding vector and then do similarity search with that vector.
But is there any efficient method f
or randomly selecting some document.
Selecting documents with random index will also work.
```
---

     
 
all -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-13-0910
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

     
 
all -  [ CRUD operations in Vector Databases(For production purpose) ](https://www.reddit.com/r/LocalLLaMA/comments/18dh3zi/crud_operations_in_vector_databasesfor_production/) , 2023-12-13-0910
```
Hello everyone, I have been working with langchain and has built some  RAG applications. I have used FAISS as the vector
 database, which  inherently does not support CRUD operations completely. If anyone has  any inputs on which of the vect
or databases support CRUD operations,  which they might have tried and tested. And also it should be efficient  and not 
accurate, not too much time consuming. Thanks.
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-13-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-13-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-13-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-13-0910
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

     
