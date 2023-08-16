 
all -  [ Training/Fine-Tuning OpenAI ](https://www.reddit.com/r/LangChain/comments/15rztbi/trainingfinetuning_openai/) , 2023-08-16-0909
```
template = '''Question: {question}

&#x200B;

You are a friendly assistant that answers the users questions.'''

prompt 
= PromptTemplate(template=template, input\_variables=\['question'\])

llm = OpenAI()

llm = OpenAI(openai\_api\_key='sk-
XXXX')

llm\_chain = LLMChain(prompt=prompt, llm=llm)

question = 'Who won the superbowl in 1999?'

llm\_chain.run(quest
ion)

&#x200B;

How do I make it so that this uses a database from a different files, like 'data.txt'?
```
---

     
 
all -  [ My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/generativeAI/comments/15ry7w5/my_apprehension_about_langchain_and_why_you_dont/) , 2023-08-16-0909
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.

Checkout the entire blog post at [https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f](https://thevatsalsaglani.med
ium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f)
```
---

     
 
all -  [ [D] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/ArtificialInteligence/comments/15ry5ju/d_my_apprehension_about_langchain_and_why_you/) , 2023-08-16-0909
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.  
Checkout the entire blog post at https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f
```
---

     
 
all -  [ Help with adding chat history to current langchain chatbot ](https://www.reddit.com/r/LangChain/comments/15rw8yj/help_with_adding_chat_history_to_current/) , 2023-08-16-0909
```
    def chat_logic(messages: Chat, chatbot_id: str):
        msg = messages.messages[-1]
        index_name = chatbot_id
.lower()
        if msg.role == 'user':
            embeddings = openai.OpenAIEmbeddings(openai_api_key=config.openai_ap
i_key)
            llm = ChatOpenAI(
                openai_api_key=config.openai_api_key,
                model_name='g
pt-3.5-turbo',
                temperature=0.0
            )
            docsearch = PineconeSearch.from_existing_index(
index_name, embeddings)
            chain = load_qa_chain(llm, chain_type='stuff', verbose=True)
            query = msg
.text
            docs = docsearch.similarity_search(query)
            result = chain.run(input_documents=docs, questio
n=query)
            return result

This is my code for current langchain chatbot which i have trained on my data, i wan
t to introduce chat history, i've tried a few ways by using the docs, below is one way i tried with an agent but the per
formance wasn't as good as the above example in most cases i found it bizare that it couldnt find what i asked for from 
my vector DB

    def chat_logic(messages: Chat, chatbot_id: str):
        index_name = chatbot_id.lower()
        msg =
 messages.messages[-1]
        if msg.role == 'user':
            query = msg.text
            embeddings = openai.OpenA
IEmbeddings(openai_api_key=config.openai_api_key)
            llm = ChatOpenAI(
                openai_api_key=config.op
enai_api_key,
                model_name='gpt-3.5-turbo',
                temperature=0.0
                )
            
docsearch = PineconeSearch.from_existing_index(index_name, embeddings)
            chat_memory = ChatMessageHistory()
  
          for message in messages.messages:
                if message.role == 'user':
                    chat_memory.a
dd_user_message(message=message.text)
                else:
                    chat_memory.add_ai_message(message=messa
ge.text)
    
            conversation_memory = ConversationBufferWindowMemory(
                memory_key='chat_history
',
                k=5,
                return_messages=True,
                chat_memory=chat_memory
            )
    
        qa = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type='stuff',
                r
etriever=docsearch.as_retriever(),
            )
            tools = [
                Tool(
                name='Chatb
ot Ai',
                func=qa.run,
                description=('Use for all queries')
                )
            ]

    
            agent = initialize_agent(
                agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
          
      tools=tools,
                llm=llm,
                verbose=True,
                max_iterations=3,
            
    early_stopping_method='generate',
                memory=conversation_memory,
            )
    
            try:
  
              response= agent(query)
                return response['output'].replace('\n', '\u000A')
            excep
t Exception as e:
                response = str(e)
                if response.startswith('Could not parse LLM output: 
'):
                    response = response.removeprefix('Could not parse LLM output: ')
                return response
.replace('\n', '\u000A')

&#x200B;
```
---

     
 
all -  [ Need help in increasing the speed of my llm based application ](https://www.reddit.com/r/LangChain/comments/15rpugk/need_help_in_increasing_the_speed_of_my_llm_based/) , 2023-08-16-0909
```
I have built something using langchain, ChromaDB and OpenAI 's llm. I am using OpenAI's embeddings as well, the ada-002.
 
However, the responses are very slow. For little complex questions it takes 20-30 seconds to respond. 
The size of the
 vectorstore is 62MB's only but still it's very slow. 
I wanted to ask whether using an AWS ec2 g3 instance with GPUs wi
ll increase the speed or not? Or any other cloud based solution.
Also, are there any other ways? I am also exploring vll
m for its tensor parallel size parameter thing.
What is the best approach that I can take to increase the speed of respo
nses? 

Ps. I am a beginner in this field, sorry if I wrote something stupid here :)
```
---

     
 
all -  [ I was tired of Langchain and created my own wrapper ](https://dev.to/zakharsmirnoff/i-was-tired-of-langchain-and-created-my-own-wrapper-1dfo) , 2023-08-16-0909
```

```
---

     
 
all -  [ Recommend ](https://www.reddit.com/r/learnmachinelearning/comments/15rnzx6/recommend/) , 2023-08-16-0909
```
4 the work #AI #chatgpt #vectorstores #langchain
https://youtube.com/@insightbuilder
```
---

     
 
all -  [ How to upload a JSON file to Vector Store while ensuring its search quality. ](https://www.reddit.com/r/LangChain/comments/15rncfr/how_to_upload_a_json_file_to_vector_store_while/) , 2023-08-16-0909
```
I am currently preparing a programming assistant for software. I have prepared 10 sample programs and stored them in a J
SON file.  Each sample program has hundreds of lines of code and related descriptions. I hope that users can ask questio
ns and receive relevant answers through the chatbot (rather than directly displaying sample programs).

However, I am fa
cing several issues at the moment: 

1. I am struggling with how to upload the JSON file to Vector Store. Currently, my 
approach is to convert the JSON into a CSV file, but this method is not yielding satisfactory results compared to direct
ly uploading the JSON file using relevance.

[CSV layout](https://preview.redd.it/bqszpfp8p8ib1.png?width=700&format=png
&auto=webp&s=94552c768af33177522e8beec4b0ab0d8d729e21)

1. In my own setup, I am using Openai's GPT3.5 along with Pineco
ne and Openai embedding in LangChain framework. These configurations are similar to relevance except for Pinecone. May I
 know your suggestion about this issue? thanks.
```
---

     
 
all -  [ My experiment in building a document chatbot with AI and OceanBase ](https://www.reddit.com/r/ArtificialInteligence/comments/15rm0bg/my_experiment_in_building_a_document_chatbot_with/) , 2023-08-16-0909
```
Hello, fellow AI enthusiasts!

I wanted to share a unique project I've been working on that combines the power of AI, sp
ecifically ChatGPT, with OceanBase, a distributed relational database management system. The result? A document chatbot 
that simplifies the process of navigating through extensive documentation.

In my recent article, '[Create a Langchain a
lternative from scratch using OceanBase](https://medium.com/oceanbase-database/create-a-langchain-alternative-from-scrat
ch-using-oceanbase-df66231834b9)', I've documented my journey. The project was born out of a simple observation: the cha
llenge of finding precise information quickly and efficiently in extensive documentation. This led me to the idea of lev
eraging the power of AI, particularly ChatGPT, to navigate this vast sea of information.

This experiment was a fascinat
ing exploration of the intersection of AI and databases. Whether you're a fan of OpenAI's work, a database professional,
 or just someone interested in the practical applications of AI, I think you'll find this project intriguing.

Feel free
 to check out the article and let me know your thoughts. I'm always open to feedback and would love to hear your insight
s!

Here's the link to the article: [Create a Langchain alternative from scratch using OceanBase](https://medium.com/oce
anbase-database/create-a-langchain-alternative-from-scratch-using-oceanbase-df66231834b9)
```
---

     
 
all -  [ Exploring vector store in databases with OceanBase and AI ](https://www.reddit.com/r/Database/comments/15rlyfl/exploring_vector_store_in_databases_with/) , 2023-08-16-0909
```
Hello /database community!

I am excited to share with you my recent exploration into vector storage in databases. I've 
recently published an article ([Create a Langchain alternative from scratch using OceanBase](https://medium.com/oceanbas
e-database/create-a-langchain-alternative-from-scratch-using-oceanbase-df66231834b9)) that details my journey of integra
ting AI with OceanBase, a distributed relational database management system, to create a document chatbot.

The project 
was born out of the challenge of navigating through extensive documentation. The idea was to leverage AI to sift through
 this vast sea of information and provide precise answers to user queries. But I wanted to take it a step further and us
e OceanBase itself as the vector database for AI training. This approach not only provided a practical solution to the i
nformation retrieval challenge but also offered a unique opportunity to explore the capabilities of OceanBase from a dif
ferent perspective.

The project integrates AI with OceanBase to create a document chatbot capable of answering user que
ries based on OceanBase’s documentation, and any other GitHub-hosted documentation. User questions and documentation art
icles are transformed into vector representations for comparison and answer generation. 

I invite you all to read the a
rticle and join the discussion on the potential of vector storage in databases and how it can change the way we interact
 with large volumes of data. 

Here is the link to the article: [Create a Langchain alternative from scratch using Ocean
Base](https://medium.com/oceanbase-database/create-a-langchain-alternative-from-scratch-using-oceanbase-df66231834b9). I
 look forward to hearing your thoughts and engaging in fruitful discussions!
```
---

     
 
all -  [ Data Analytics using Llama2? ](https://www.reddit.com/r/LocalLLaMA/comments/15re5jq/data_analytics_using_llama2/) , 2023-08-16-0909
```
Is there any good workflow to use llama2 to perform data analytics on a csv file, perhaps using Langchain?

I noticed th
at Langchain has this nice agent to execute python code that can run analytics on a pandas data frame. It works very wel
l with OpenAI models. But when I use the Langchain agent with Llama quantised 7B model, the results are very disappointi
ng.
```
---

     
 
all -  [ Anybody know why this agent would be so wrong? ](https://i.redd.it/pr0k280bc6ib1.jpg) , 2023-08-16-0909
```
So I’m experimenting with the Serp API and an agent and I asked it to get the current Tesla stock price and it got $845?
? Anybody know where it went wrong or how to fix this?
```
---

     
 
all -  [ Chatbot for Baldur's Gate 3 wiki - 🏰🔮 BG3Chat ](https://www.reddit.com/r/BaldursGate3/comments/15r8c8x/chatbot_for_baldurs_gate_3_wiki_bg3chat/) , 2023-08-16-0909
```
Hello everyone :)

I have built a chatbot that can answer questions about Baldur's Gate 3, please feel free to try it ou
t here: [bg3chat](https://bg3chat.streamlit.app/).

A quick note: To use the chatbot, you'll need an OpenAI API key. If 
you don't have one, you can easily get yours by creating an account at [openai.com/account/api-keys](https://platform.op
enai.com/account/api-keys). Apart from the OpenAI API costs, the chatbot is free-to-use.  


**How does it work?** 

The
 chatbot fetches content from [bg3.wiki](https://bg3.wiki/) and stores it in a vectorstore. Whenever you pose a question
, it delves into this database to find the most relevant game information. This process is known as Retrieval Augmented 
Generation (RAG). With the help of Langchain, the AI can independently comb through the database to provide precise answ
ers.

A fun feature: It's not just a Q&A bot! It possesses a memory, allowing you to have a seamless conversation. It re
calls previous questions and responses, which means you can chain together searches and get answers to multi-faceted que
stions.  


I hope you all have fun playing around with it! I would appreciate if you'd consider leaving a star ⭐ on my 
[GitHub repo](https://github.com/SimonB97/BG3Chat) :)

https://reddit.com/link/15r8c8x/video/reofexysb4ib1/player

&#x20
0B;
```
---

     
 
all -  [ LangChain ChatPromptTemplate or f'string' ](https://www.reddit.com/r/OpenAIDev/comments/15r6rfd/langchain_chatprompttemplate_or_fstring/) , 2023-08-16-0909
```
Hi guys, i'm just beginning to dip my toes in LangChain and i'm confused about how 'ChatPromptTemplate' works.   
Please
 tell me that is more to it than just a glorified fstring.  


As an example this is what I'm trying to accomplish:

`TE
ST_PROMPT = '''The english sentence is: '{original_sentence}', the correct answer is '{french_sentence}'`  
`and the stu
dent answer is '{answer}' '''`
```
---

     
 
all -  [ I made an AI therapist using langchain to improve your mental health ](https://www.reddit.com/r/LangChain/comments/15r0ri0/i_made_an_ai_therapist_using_langchain_to_improve/) , 2023-08-16-0909
```
**TLDR**: With a background in psychology and computer science, I developed **PsyScribe**—an AI therapist powered by Cha
tGPT for improving your mental health. The intention is to provide a first step towards therapy for people who have non-
clinical symptoms and experience barriers to see a human therapist. My AI therapist is highly customizable to your needs
 and addresses many challenges with using ChatGPT for therapy like having to design prompts and making sure ChatGPT stay
s in its role. It also enhances ChatGPT with long-term memory and  generation of conversation insights, both of which ar
e essential for successful therapy. The AI therapist was developed in the context of my master thesis in which it was ab
le to improve the mental health of the participants. You can try it out for free at [https://www.psyscribe.com](https://
www.psyscribe.com).

Hello everyone,

With a master's degree in computer science and a bachelor's degree in psychology, 
the idea of merging AI with psychotherapy intrigued me. So for my master thesis I decided to investigate the effect of p
ersonalizing a ChatGPT based AI therapist on the therapeutic bond with the AI therapist. The results showed that persona
lisation was linked with a significantly higher therapeutic bond with the AI therapist after using it for 2 weeks. The t
herapeutic bond was also similar to those with a  human therapist. This is important because the therapeutic bond is rob
ustly linked to therapeutic success. Another result was that 49/54 participants indicated that the chatbot helped them w
ith their mental health. After these promising results I decided to further develop this it into a product, PsyScribe. (
For those who are interested here is a draft of this research paper which my promoter says will likely be published [htt
ps://storage.googleapis.com/psyscribe\_paper/paper\_psyscribe.pdf](https://storage.googleapis.com/psyscribe_paper/paper_
psyscribe.pdf))

**Why I believe my PsyScribe AI therapist is superior to vanilla ChatGPT for therapy:**

1.**Fully pers
onalizable and optimized for therapy:**

PsyScribe is easily customizable to make your feel comfortable and make the AI 
therapist meet your specific needs. It also removes the struggle of having to design your own prompts and making sure Ch
atGPT stays in his role as therapist. The following aspects are personalizable:

* Therapy style: you can choose between
 a solution-oriented or supportive-listening therapy style.
* Personality: you can choose between a motivational, profes
sional or cheerful therapist personality.
* Avatar: you can create your own therapist avatar, making sure you feel comfo
rtable with who you are talking to.
* Giving a name to your AI therapist and letting the AI therapist know and remember 
your name.
* Choosing the typespeed of the AI therapist.

**2. Long and short-term therapist memory:**

Vanilla ChatGPT 
often forgets important therapeutic information and can’t remember information across different chats. But in therapy yo
u don’t want to re-explain yourself in every new conversation and want to make sure your therapist remembers important i
nformation. That’s why a PsyScribe AI therapist has two forms of memory.

* Short-term memory: The AI therapist has a sh
ort-term memory by continuously summarising and analysing the current conversation, making sure that no important inform
ation is lost. This short-term memory is always available to the therapist but also limited in size and conversation (ch
at) specific.
* Long-term memory: To overcome the limitations of the short-term memory, you can also manually store mess
ages in the long-term memory which is large in size and available to the AI therapist across all conversations (chats). 
Every time you send a  message the therapist will look for relevant info in his/her long-term memory and will use this r
etrieved information in his/her answer.

**3. Automatic Conversation insights**

An important aspect of psychotherapy re
flecting on insights from past conversations and planning future actions. PsyScribe also makes this aspect easier by hav
ing the AI therapist automatically summarize your conversations and keep track of important feelings, thoughts, goals an
d other possibly useful insights.  You can edit these insights and indicate how important you think they are. After you 
rated your insights on importance, they are compiled in a report for reflection, or can be shared with your psychologist
 / coach.

**Safety and data security:**

All your conversation data is safely and  securely stored, making sure no thir
d-party has access to your data.  You can always request to delete all the data associated with your account.

An import
ant warning is that ofcourse all the answers of the AI therapist are computer generated and could potentially be inappro
priate. For serious mental health problems we recommend you to seek out professional help instead of using PsyScribe.

*
*Conclusion**:

In short I believe using my PsyScribe AI therapist has important benefits over using vanilla ChatGPT. My
 research has indicated that it AI psychotherapy is a promising approach to improving your mental health. You can try ou
t psyscribe for free on:

[https://www.psyscribe.com](https://www.psyscribe.com)

I hope this helps some of you :)
```
---

     
 
all -  [ Issue with 'gaps' between chunks ](https://www.reddit.com/r/LangChain/comments/15qxw7b/issue_with_gaps_between_chunks/) , 2023-08-16-0909
```
I'm working on a conversational bot that responds to queries about PDF content, and for summarizing data and general que
stions it works great. However, one of the PDF's is a list of error codes in alphanumeric order (A001, A002..... B001,B0
02, etc), and when asking about the codes I've found theres gaps in which codes it's able to answer about.

For example,
 it'll know about A001-A040, but then there's a gap until the next block of codes it knows. I've confirmed that there ar
e indeed chunks for the missing codes, as well as embeddings, but it seems to 'skip' over that information. Why could th
is be?
```
---

     
 
all -  [ Token usage ](https://www.reddit.com/r/LangChain/comments/15qx75d/token_usage/) , 2023-08-16-0909
```
Hey, I am building a simple chatbot where I use embeddings and OpenAI's completion (langchain.js). I would like to track
 token usage for every prompt. The problem I'm facing is that I am using streaming, and in this case, we don't receive t
oken usage in the handleLLMEnd callback. Currently, I calculate the tokens of the prompt with tiktoken ([**https://www.n
pmjs.com/package/@dqbd/tiktoken**](https://www.npmjs.com/package/@dqbd/tiktoken)), and for the response, I count every r
eceived data in streaming (they state that every response in the stream is one token). However, I'm still encountering a
n error in token count for around 100-150 tokens. Does anyone have a better workaround for tracking token usage?

Relate
d issue for langchain when using a stream ([**https://github.com/hwchase17/langchainjs/issues/965**](https://github.com/
hwchase17/langchainjs/issues/965)).
```
---

     
 
all -  [ Video analyzing with langchain ](https://www.reddit.com/r/LangChain/comments/15qu1tk/video_analyzing_with_langchain/) , 2023-08-16-0909
```
Hi, is there any way to make video analysing with langchain + chatgpt or some external API like elevenlabs, but for vide
o analysing.

In this case I want to pass a video to langchain and langchain will return me about what is the video, wha
t appears, how much time is it or just its a just a video of 15 seconds with a empty white board.

I know exists some yo
utube loader, but as I know that only takes the transcription from the video and analyze that transcription.

In this ca
se I want to pass a small video of my dog playing in the park with a ball, but I want to see if this langchain or chatgp
t or another external API can help me to achieve this and have the response like: A video of a small dog of this breed p
laying with a green ball in a park in summer.

Idk if someone knows about some api or page which is already doing this o
r knows the proper name for this? video analysis with llm?
```
---

     
 
all -  [ How to expose a model into an API? ](https://www.reddit.com/r/LocalLLaMA/comments/15qs2br/how_to_expose_a_model_into_an_api/) , 2023-08-16-0909
```
I've a PC with a RTX 3090 and I would like to use it for models like Llama2. I would like to open a port and offer the i
nference power of that PC to other apps running LangChain outside the home network.

I've thought about combine FastAPI 
with HF local package but I believe that there are other options out there much better.
```
---

     
 
all -  [ VectorDB Operations with Faiss (View, Add, Delete, Save, QnA and Similarity Search) via Langchain ](https://www.reddit.com/r/LangChain/comments/15qm2ie/vectordb_operations_with_faiss_view_add_delete/) , 2023-08-16-0909
```
Here, we will discuss how to do VectorDB operations such as View, Add, Delete, and Update documents as well as save and 
load db from disk, QnA and Similarity Search.  

[https://youtu.be/hSuCT6Z2QLk](https://youtu.be/hSuCT6Z2QLk) 

&#x200B;

```
---

     
 
all -  [ Alternatives for vectorstore in heroku ](https://www.reddit.com/r/LangChain/comments/15qf5ur/alternatives_for_vectorstore_in_heroku/) , 2023-08-16-0909
```
Hi guys, iam working on a QA chatbot with a vectorstore, iam using redis but looks like the last redist stack which is r
equired for langchain cant be used in our heroku server, same with chroma 

Have any of you guys encounter a similar pro
blem? Any altertative i could use? Or a work arround without any vector store maybe
```
---

     
 
all -  [ Another Beginner Post: Local LLM + LangChain Question ](https://www.reddit.com/r/LocalLLaMA/comments/15qbvug/another_beginner_post_local_llm_langchain_question/) , 2023-08-16-0909
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

     
 
all -  [ How should I chunk text from a textbook for the best embedding results? ](https://www.reddit.com/r/LangChain/comments/15q5jzv/how_should_i_chunk_text_from_a_textbook_for_the/) , 2023-08-16-0909
```
My guess is that I should follow the natural structure of the textbook and chunk my text by chapter, section, subsection
, etc while retaining the relevant metadata. The problem is that I have no idea how to do that lol.

Can someone tell me
 a better way to chunk a textbook or give me the basic guidelines so I can ask ChatGPT?
```
---

     
 
all -  [ How should I preprocess my text to optimize text embeddings? ](https://www.reddit.com/r/LangChain/comments/15q4v2v/how_should_i_preprocess_my_text_to_optimize_text/) , 2023-08-16-0909
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

     
 
all -  [ Last Week in AI #1 ](https://www.reddit.com/r/ChatGPT/comments/15pztik/last_week_in_ai_1/) , 2023-08-16-0909
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

     
 
all -  [ Building first chatbot for client(s) ](https://www.reddit.com/r/vectordatabase/comments/15pyunf/building_first_chatbot_for_clients/) , 2023-08-16-0909
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

     
 
all -  [ what is the future of ChatGPT? ](https://www.reddit.com/r/OpenAI/comments/15pmf6v/what_is_the_future_of_chatgpt/) , 2023-08-16-0909
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

     
 
all -  [ Struggling on chat with docs opensource ](https://www.reddit.com/r/learnmachinelearning/comments/15phmgz/struggling_on_chat_with_docs_opensource/) , 2023-08-16-0909
```
I am trying to chat with docs with a langchain next js app but it seems to halucinate and create fake links. I have used
 pinecone to ingest my pdf there.
Do you know any good chat with docs project that you have tested ?
Thanks
```
---

     
 
all -  [ Router Chains ](https://www.reddit.com/r/LangChain/comments/15p0rsk/router_chains/) , 2023-08-16-0909
```
In case of router chains, be it LLMRouterChain or EmbeddingRouterChain, what are the deciding parameters of the llm rout
ing to the default chain instead of choosing any of the destination? 
Also does embeddingrouter chain simply check the c
osine similarity of the query with the description of the prompts provided? If not, then what principle does it use to r
oute??
```
---

     
 
all -  [ How do I build a chatbot? ](https://www.reddit.com/r/LangChain/comments/15ozvj7/how_do_i_build_a_chatbot/) , 2023-08-16-0909
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

     
 
all -  [ ReferenceError: ReadableStream is not defined at Object.<anonymous> ](https://www.reddit.com/r/LangChain/comments/15oxt5t/referenceerror_readablestream_is_not_defined_at/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] How we evaluated LLMs in prod ](https://www.reddit.com/r/MachineLearning/comments/15ogknd/d_how_we_evaluated_llms_in_prod/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-16-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-16-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 2023-08-16-0909
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

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 2023-08-16-0909
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-16-0909
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
