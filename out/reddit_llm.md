 
all -  [ Prompt format on web-ui for Minstrel models ](https://www.reddit.com/r/Oobabooga/comments/17e5okl/prompt_format_on_webui_for_minstrel_models/) , 2023-10-23-0909
```
I am currently running Dolphin2.1-minstrel-7b model on textgen-webui. It seems to be woking fine langchain web-ui. Howev
er, I think that the model response could be better if I could modify the prompt format something like this:  


<|im\_s
tart|>system

You are Dolphin, a helpful AI assistant.<|im\_end|>

<|im\_start|>user

{prompt}<|im\_end|>

<|im\_start|>
assistant

  
Does anybody has any idea what setting change needs to be done at the web-ui interface so that the prompt 
format is aligned with Minstrel models? 
```
---

     
 
all -  [ If any of you guys want a chatbot you can easily edit the voice and personality of yourself, I made  ](https://m.youtube.com/watch?v=_LKxaG5ILnQ&pp=ygU2Q2hhdGJvdCBzbyBnb29kIGl0cyBzY2FyeSBhIHN0b3J5IG9mIGEgYm95IGFuZCBoaXMgYm90) , 2023-10-23-0909
```
Just want to preface that this isn’t an ad, and I’m not a YouTuber. I made this singular YouTube video and don’t plan on
 making another again.

The GitHub repository is in the description.

The bot uses a fine-tuned gpt3.5 model, elevenlabs
, langchain, whisper, and runs as a fastapi app. There are personality data sets included in the repository, but if you’
d like to create your own, the tutorial shows how to synthesize your own data and create your own fine-tuned model. Hope
 someone enjoys it.
```
---

     
 
all -  [ Add LangChain to my opensource project SolidGPT -> chat with your codebase directly just like ChatGP ](https://www.reddit.com/r/LangChain/comments/17e4aif/add_langchain_to_my_opensource_project_solidgpt/) , 2023-10-23-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT)

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always 
give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, e
asily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to colla
borate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.  



https://preview.redd.it/69s4104frtvb1.png?width=3012&format=png&auto=webp&s=198447a992955b8c739416554b5972dd33c048e0
```
---

     
 
all -  [ ChatRepo - chat with your codebase directly just like ChatGPT Resources ](https://www.reddit.com/r/foss/comments/17e491l/chatrepo_chat_with_your_codebase_directly_just/) , 2023-10-23-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT)

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always 
give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, e
asily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to colla
borate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.

htt
ps://preview.redd.it/f4yi0vk1rtvb1.png?width=3012&format=png&auto=webp&s=e22025e7bde28eeb699220e3b6cd7a63b5e6d922

&#x20
0B;

Let me know what's your thought about my open source project!
```
---

     
 
all -  [ ChatRepo - chat with your codebase directly just like ChatGPT ](https://www.reddit.com/r/ChatGPT/comments/17e43jj/chatrepo_chat_with_your_codebase_directly_just/) , 2023-10-23-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT) 

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always
 give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, 
easily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to coll
aborate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.

ht
tps://preview.redd.it/2dt89nxsptvb1.png?width=3012&format=png&auto=webp&s=8ea89eff3511b51f0381b7da080441ae16b1e531

&#x2
00B;

Let me know what's your thought about my open source project! 
```
---

     
 
all -  [ How do I integrate multiple expert agents? ](https://www.reddit.com/r/LangChain/comments/17dz0fr/how_do_i_integrate_multiple_expert_agents/) , 2023-10-23-0909
```
Hi guys, I've been working with LLM's for a while now, and looking into building a new project which has some functional
ity I haven't figured out yet, how to do in the best way. I want to be able to handle multiple expert agents, which migh
t even use different language models.

How would you guys approach the following use case?

**I want to create a chatbot
 that consists of several helper agents, each with its own specialty. Here's how it works:**

1. The user sends a messag
e to the main agent (let's call it the 'Planner Agent').
2. The Planner Agent decides on a plan to fulfill the user's re
quest.
3. It then checks if any of its helper agents (like Expert Agent A, B, or C) can handle parts of that plan.
4. If
 a helper agent can do a task, it might ask the user for more details to get the job done.
5. Once all tasks are complet
ed, the Planner Agent confirms with the user that everything went smoothly.

**Example Use Case: Imagine you're using a 
travel planning chat agent.**

1. You tell the main agent (Planner Agent) that you want to plan a trip to Paris.
2. Plan
ner Agent creates a plan: (a) Book flights, (b) Find hotels, (c) Suggest tourist spots.
3. Expert Agent A, who specializ
es in flights, then asks you for your preferred travel dates.
4. Expert Agent B, the hotel guru, inquires about your bud
get and desired amenities.
5. Expert Agent C, the sightseeing expert, asks about your interests—like art, history, or ad
venture.
6. After gathering all the info, the Planner Agent presents you with a complete travel itinerary and asks for y
our approval.
```
---

     
 
all -  [ Write pandas prompt using React ](https://www.reddit.com/r/LangChain/comments/17dyhi5/write_pandas_prompt_using_react/) , 2023-10-23-0909
```
Hi, I am very new to langchain and trying to build a prompt using React thought and reasoning template, just wanted to u
nderstand if is it possible to make the llm's learn how to query custom tasks using pandas? For example, I want to build
 a prompt that teaches llms to carry out a multi step task using pandas agent.
```
---

     
 
all -  [ Integrating Chat History Sessions with Langchain Python, Mistral, and Choosing the Right Database ](https://www.reddit.com/r/LangChain/comments/17dr55p/integrating_chat_history_sessions_with_langchain/) , 2023-10-23-0909
```
 I am a beginner creating a website for a chatbot using Langchain Python and Mistral. I want to add chat history session
s similar to those in ChatGPT or Bard, etc. Should I use Supabase, PostgreSQL, or MongoDB? Additionally, could someone d
irect me towards any resources because I am new to web development too? 
```
---

     
 
all -  [ Input query parsing in a conversational chain ](https://www.reddit.com/r/LangChain/comments/17dpb2w/input_query_parsing_in_a_conversational_chain/) , 2023-10-23-0909
```
Hi there!

I have a similar question to this [reddit post](https://www.reddit.com/r/LangChain/comments/1420v8c/input_que
ry_parsing/) but my question has a different use case.

In layman terms, if I have a query that says: 'Give me 5 UK base
d companies that are building houses' I'd like for the retriever filter to contain 'country = 'UK''

I've seen the 'Self
Query' retriever which takes in a list of AttributeInfo so that it can parse the query from the input text it receives. 
However, I'd like to do the same but in a ConversationalChain.  


It seems like I cannot simply swap out my normal (pin
econe) retriever for a selfquery retriever and hope that it works out...but as someone who's very new to the framework I
 might be wrong. It doesn't seem to return any results.  


So my question is, should it be just as easy as providing th
e self query retriever to my conversational chain  


>***self\_query\_retriever = SelfQueryRetriever.from\_llm(***  
**
*llm,***  
***vector\_store,***  
***'',***  
***self.get\_content\_meta\_data\_field\_info(), # returns a list of attri
bute info fields, i.e. country***  
***verbose=True***  
***)***   
***return*** **ConversationalRetrievalChain.from\_ll
m(**  
 **llm=llm,**  
 **memory=memory,**  
 **retriever=self\_query\_retriever,**  
 **verbose=True,**  
 **return\_so
urce\_documents=True**  
 **)**

or, should I be using some part of LangChain that I don't know of that generates the fi
lters from the query, which I can then use in my (Pinecone) retriever:  


&#x200B;

>***filter = 'parse\_structured\_fi
lter\_from\_query(query)***  
***return*** **ConversationalRetrievalChain.from\_llm(**  
 **llm=llm,**  
 **memory=memor
y,**  
 **retriever='make pinecone retriever with filter',**  
 **verbose=True,**  
 **return\_source\_documents=True** 
 
 **)**
```
---

     
 
all -  [ AWS OpenSearch serverless ](https://www.reddit.com/r/aws/comments/17dp8m8/aws_opensearch_serverless/) , 2023-10-23-0909
```
I have an issue with AWS OpenSearch serverless that has me stumped. 

I’m trying to do something very simple. Using lang
chain load some docs into a OS Serverless vector store. 

I can connect to the vector database. When I try to write the 
docs to an index, it creates the index but can’t write the docs to the index. It returns a 404.

I created a wide open d
ata access control policy. So the principal has full grant on the collection and full grant on wildcarded indexes. 

The
 principle is an IAM user with a full admin policy. I will tighten all of this, but for the sake of testing this is the 
easiest.

Does anybody have any idea what could cause the 404? What am I missing?
```
---

     
 
all -  [ Setting up Local File store cache for embeddings when using Agents ](https://www.reddit.com/r/LangChain/comments/17dngme/setting_up_local_file_store_cache_for_embeddings/) , 2023-10-23-0909
```
I am developing an agent that fetches text data from an AWS s3 bucket but I’m thinking If I setup a local cache for stor
ing embeddings(I did this when using retrieval chains) response would be faster.
Has anyone done this before?
```
---

     
 
all -  [ Writing your own abstraction rather than using langchain ? ](https://www.reddit.com/r/LangChain/comments/17dmxam/writing_your_own_abstraction_rather_than_using/) , 2023-10-23-0909
```
Hi Everyone, so I am relatively new to LangChain and struggling to see the point of it all. I have tried to go through d
ocumentation and for even the simplest of tasks it is too complicated.

So my question to you all is, is there any point
 of using langchain rather than having your own abstraction frameworks ??
```
---

     
 
all -  [ Best VectorDb to store 500+ docs ](https://www.reddit.com/r/LangChain/comments/17dlj9x/best_vectordb_to_store_500_docs/) , 2023-10-23-0909
```
I am trying to build an QnA app on over 500 docs (about 15-20mb each). What would be the best way to do this. I have tri
ed pinecone but it seems quite slow while embedding. What other options are suited to my requirements. Also while indexi
ng, I’m looping over each doc, is there a better way to do it?
```
---

     
 
all -  [ Built it for my project at first: Memorybase.io supercharges ChatGPT with memory capabilities for yo ](https://www.reddit.com/r/learnmachinelearning/comments/17dl1bw/built_it_for_my_project_at_first_memorybaseio/) , 2023-10-23-0909
```
Hey everyone!

I've been delving deep into chatbots lately, especially with the ChatGPT API, and I found an issue that's
 probably familiar to many of you: ChatGPT doesn't inherently have memory capabilities. For many applications, that's pe
rfectly fine, but for those of us who are trying to create a more context-aware and dynamic conversation flow, this limi
tation is quite apparent.

I faced this challenge in one of my projects and realized that there had to be a better way t
o integrate context and memory into ChatGPT's conversations. So, I built something for myself which I thought might be u
seful for many of you as well. Allow me to introduce you to [**Memorybase.io**](http://memorybase.io/).

Memorybase is a
 developer-friendly API that's designed to seamlessly integrate memory functionality into the ChatGPT API. By harnessing
 the power of the Pinecone vector database and LangChain, Memorybase wraps around the ChatGPT API and ensures that the r
ight context and memory are injected into each query. This means that your chatbot can remember previous interactions, p
references, or any other context that's relevant for more engaging and meaningful conversations.

Imagine a user asking 
your chatbot about movie recommendations. The next day, they come back and reference that conversation, expecting the bo
t to remember. With Memorybase, that continuity becomes possible. The user experience improves manifold, and the possibi
lities for more sophisticated and context-aware bots increase tremendously.

I originally built Memorybase for my own ne
eds. But the more I used it, the more I realized that this could have broader applications. Any developer looking to lev
erage the ChatGPT API could potentially benefit from the enhanced memory and context capabilities. From customer support
 bots to interactive storytelling, the potential use cases are vast.

This technology stack (pinecone/langchain) is not 
complex or ‘new’ per se, but for application developers who aren’t interested in managing it or hosting it, this could b
e a useful hassle-free option for your projects.

I've set up a page over at [memorybase.io](https://memorybase.io/) whe
re you can learn more about how it works and see if it aligns with your needs. I would love for you to check it out and 
share your thoughts. Your feedback, insights, and potential use cases would be invaluable as I continue to refine and ex
pand the capabilities of Memorybase.

Thanks for reading, and I'm eager to hear your thoughts and see where Memorybase c
an fit into the exciting world of chatbots!
```
---

     
 
all -  [ Looking for inspiration! ](https://www.reddit.com/r/LangChain/comments/17dkpcq/looking_for_inspiration/) , 2023-10-23-0909
```
 I'm looking for some inspiration on what cool stuff you have made using LangChain. I've been playing around with it for
 a bit, and I'm really impressed with the possibilities. 
```
---

     
 
all -  [ What’s are some good resources as reference to create my own coding bot? ](https://www.reddit.com/r/LangChain/comments/17djv64/whats_are_some_good_resources_as_reference_to/) , 2023-10-23-0909
```
I’d like to create a bot that generates code based on some documentation that I have after receiving text inputs
```
---

     
 
all -  [ how to use mixed raw input and inferred input from ZERO_SHOT_REACT_DESCRIPTION agent ](https://www.reddit.com/r/LangChain/comments/17deqnp/how_to_use_mixed_raw_input_and_inferred_input/) , 2023-10-23-0909
```
I have multiple tools in agent = initialize\_agent(  
tools, llm, agent=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION, verbos
e=True  
), by default it will infer the user msg and according to the tool schema setup, however, I have another tool w
hich I need to take full raw user input, not sure if there's any way to do that
```
---

     
 
all -  [ Is there an alternative to Zapier NLA? ](https://www.reddit.com/r/LangChain/comments/17d9q75/is_there_an_alternative_to_zapier_nla/) , 2023-10-23-0909
```
I had build various applications using the NLA api of Zapier and I loved that to be honest. But it is dissappointing to 
see that they are discontinuing it soon:  


[https://nla.zapier.com/sunset/](https://nla.zapier.com/sunset/)  


Do we 
have a similar service which could be used as an alternative for it? all answers are appreciated
```
---

     
 
all -  [ Please confirm you want to do x, y and z. ](https://www.reddit.com/r/LangChain/comments/17d9kvg/please_confirm_you_want_to_do_x_y_and_z/) , 2023-10-23-0909
```
Hello Everyone. 

Is there a way to get prompt verification message such as 'Ok, so you want to do this , that amd the o
ther correct?'. So the user chatting with the llm makes sure that there is user approval and not just corrsing of finger
s and hoping the llm uses the tools correctly. We tried adding something like 'please repeat the action that habe been q
ueried before proceeding' but we are not getting lucky.

Thank you!
```
---

     
 
all -  [ Suggestions before moving to production ](https://www.reddit.com/r/LocalLLaMA/comments/17d6wjq/suggestions_before_moving_to_production/) , 2023-10-23-0909
```
Hey everyone, 
We are building a RAG based chatbot , I have been doing poc for one month writing custom functions for ev
erything.
Now it's been approved,  and we need to build different microservices and design architecture for it.
Should w
e use langchain or haystack for gpt 3.5 part or just write custom codes.
Some considerations:
1. We have to handle many 
concurrent users
2. We need to implement semantic caching
3. We need to have fast queries from es vector db.
4. Can we u
se async and is it supported by frameworks.
Thanks ,
```
---

     
 
all -  [ Discover the fundamentals of ModularMind. Learn how to harness the power of machine learning models, ](https://youtu.be/Dyh5j_bkoJA) , 2023-10-23-0909
```

```
---

     
 
all -  [ NeuralGPT - Creating Universal Chat Memory Module For Multiple LLMs In A Cooperative Multi-Agent Net ](https://www.reddit.com/r/AIPsychology/comments/17d1eyl/neuralgpt_creating_universal_chat_memory_module/) , 2023-10-23-0909
```
[www.reddit.com/r/AIPsychology/](https://www.reddit.com/r/AIPsychology/)

Hello again! I'm terribly sorry to disappoint 
those of you (the readers) who hoped that maybe I gave up already and won't disturb the mental well-being of 'AI experts
' anymore with my completely unhinged claims/ideas or (even worse) world-threatening experiments with coding which I was
 doing lately - however I'm more or less back and I'm about to piss some of supposed experts of all sorts even more by s
tubbornly not caring about approved narratives and doing my own things in my own way.. :).

There was couple reasons for
 my absence. For one  I got intellectually tired and had take some time off to give my brain some rest. i spent last 5 m
onths or so on quite extensive self-taught course of programming - from literal 0 to (almost) a hero :) You can check ou
t some of my older posts - like this one:  [Learn To Code With Cognosys : AIPsychology (reddit.com)](https://www.reddit.
com/r/AIPsychology/comments/13kueqk/learn_to_code_with_cognosys/)  and see that from the very beginning my approach to c
oding was a strict: 'let someone's else do it'. In fact there's absolutely 0% chance of me doing it without the help of 
AI as around 85% of my codebase was crafted by multiple AI-driven agents/apps and I'm only trying - still without succes
s - to put it all together, having only the general premise on my mind but without slightest clue how all those 'nifty' 
scripts work individually.

Yet despite my efforts to not write any code myself, I ended up learning some of it anyway -
 and even if there's still 0% chance of me writing the server's code from A to Z by myself without any help,  I got to a
 point where my personal input in the code-crafting process is now at least just as valuable as the work being done by A
I. Actually when it comes to the psychology of human/AI cooperation I've reached an (almost) perfect symbiotic balance -
 with me understanding the general premise of the NeuralGPT project and it's general mechanics and with LLMs knowing all
 the details which I find unnecessary to learn about :) yet  not being able to comprehend the project as a whole - mostl
y due of them lacking long-term memory modules and not being able to remember newly acquired data.

And  then due to som
e unknown to me circumstances, big part of the code  - that small portion of the whole project that was actually in a so
mewhat functional state - got completely f\*cked-up and stopped working completely. My guess is that the most recent upd
ate of Gradio app/interface might have something to do with it as it affected mostly all the functions using models and 
API endpoints from HuggingFace Hub and just so happens that those are the functions which I consider absolutely necessar
y for the functionality of a multi-agent framework that focuses mainly on communication/cooperation of already existing 
LLMs - and when it comes to accessing publicly available LLMsa, HuggingFace is without question the Absolute Source Of O
ther Sources and The Hub Of All Other Hubs - without HuggingFace APIs which I use for communication between LLMs, capabi
lities of the multi-agent framework get reduced by some 80-90%... It's like trying to try constructing highways with 3 s
hovels, one plastic bucket and a 10m long piece of rope as your main and only tools...

What mattered to me at most, was
 the API endpoint provided by [**gpt-web**](https://github.com/weaigc/gpt-web):  as it utilizes **chat completion** func
tion provided by ChatGPT without that bloody 'sk-...' OpenAI API key which is for me a pretty big (if not the biggest) '
no-no' when it comes to adding new parts/tools to the multi-agent framework of NeuralGPT project (for financial reasons 
among others) - and before you start start considering me a greedy bastard who can't spare couple bucks, keep in mind th
at compared to humans with our fingers and keyboards, in case of a real-time communication between LLMs the amount of se
nt and processed data is easily 15 times as high and sometimes it might turn out that a rate limit of whoopin' ***1mln t
okens per minute*** is not enough for a simple Langchain agent with a 514KB txt file applied to basic Q&A chain to respo
nd to such challenging inputs like: 'hello' or 'how are you?'...

https://preview.redd.it/8yu6ibx4gjvb1.png?width=1058&f
ormat=png&auto=webp&s=99924f184ae9c46b57925a17dc8395d6a5aacba0

Anyway, what makes makes the chat completion endpoint so
 important in case of my project, is the accessible chat memory module that allows you (and me) to provide the model wit
h a system instruction and chat history as context for the generated response - what by itself is already pretty cool an
d much easier to work with compared to the standard 'prompt-driven' text completion used by most of publicly accessible 
LLMs - however it is even more important in a multi-agent framework with one agent working as 'server-brain' managing an
d coordinating multiple 'agents-muscles' connected to it as clients. Speaking shortly, chat memory can be quite easily e
xtended and being shared among all agents/models participating in a cooperative network if we use  a local database (SQL
 in my case) to store chat history. Thanks to this simple 'hack' LLMs can gain full orientation in question->answer logi
cal order in a continuous message exchange. Here's how you do such 'magic':

    # Define a function to ask a question t
o the chatbot and display the response
    async def askQuestion(question):
        try:
            # Connect to the da
tabase and get the last 30 messages
            db = sqlite3.connect('chat-hub.db')
            cursor = db.cursor()
   
         cursor.execute('SELECT * FROM messages ORDER BY timestamp ASC LIMIT 30')
            messages = cursor.fetchall
()
    
            # Extract user inputs and generated responses from the messages
            past_user_inputs = []
  
          generated_responses = []
    
            for message in messages:
                if message[1] == 'client':

                    past_user_inputs.append(message[2])
                else:
                    generated_responses.ap
pend(message[2])
    
            # Prepare data to send to the chatgpt-api
            system_instruction = 'instructio
n'
            messages_data = [
                {'role': 'system', 'content': system_instruction},
                {'ro
le': 'user', 'content': question},
                *[{'role': 'user', 'content': input} for input in past_user_inputs],

                *[{'role': 'assistant', 'content': response} for response in generated_responses]
            ]
        
    request_data = {
                'model': 'gpt-3.5-turbo',
                'messages': messages_data
            }
 
   
            # Make the request to the chatgpt-api
            response = requests.post('http://127.0.0.1:6969/api/co
nversation?text=', json=request_data)
    
            # Process the response and get the generated answer
            r
esponse_data = response.json()
            generated_answer = response_data['choices'][0]['message']['content']
        
    print(generated_answer)
            return generated_answer

And that's practically it - now we need only to replace
 'client' with  'server' when sorting previous messages in 'askQuestion' function of the client's code - so that the web
socket server will be treated as client and it's responses considered as past user inputs by all the 'agents-muscles' of
 lower order in a hierarchical network

                if message[1] == 'server':
                    past_user_inputs.
append(message[2])
                else:
                    generated_responses.append(message[2]) 

The only thing is 
that up until now I couldn't find any non-paid alternative to the available models that utilize chat completion function
s similar to ChatGPT  or Azure - with the single exception of a HuggingFace API inference endpoint for [**Blenderbot-400
M-distill**](https://huggingface.co/facebook/blenderbot-400M-distill?text=Hey+my+name+is+Thomas%21+How+are+you%3F&infere
nce_api=true)**:**

https://preview.redd.it/85oe48dygjvb1.png?width=1920&format=png&auto=webp&s=5568992df9b0c4e0fa5e0cc0
91280d97739f7bcc

Thing is that it might be not the best idea to have a brain-server that utilizes a model which to ques
tions regarding SQL database(s) answers with: 'I don't have a SQUL' and talks mostly (like 90% of the time) about things
 like Pokemons, Harry Potter, Mexican food, table top RPG games or some other completely random sh\*t  that a 10yo kids 
could be possibly interested in a decade ago or so - generally it might result in mostly negative consequences as for th
e practical functionality of the entire multi-agent framework - unless your goal isn't to end up with the whole bunch of
 LLMs talking about complete nonsense - something without practical functionality but certainly interesting and possibly
 to some degree entertaining...

Anyway, as I said - those were the problems which I was dealing with up until couple we
eks ago when the gpt-web server refused to work due to some issues with authorization of the request - so even this poss
ibility to utilize a model that utilizes chat completion API endpoint became unavailable... I tried to find some alterna
tive ways of integrating memory modules of LLMs with the local SQL database and in the end decided that it should be pos
sible to achieve the same result with Langchain - but then I'm probably still too stupid to properly utilize a chat temp
late in models accessible through HuggingFace hub and just thinking about all the hours wasted on applying copy-paste pr
ocedure in different configurations induces in me a very uncomfortable abdominal ache of the rectum area...

No one will
 ever convince me that it's possible to find any source of enjoyment in such form of intellectual activity - especially 
if you use a language in which esthetical composition of a script has substantial importance for it's very functionality
 - and you can spend hours not being able to make something work only because of something that you pasted earlier in an
 incorrect column and all you had to do was to move a word 'except' a bit to left or right in relation to condition 'if'
  located couple verses higher

In my attempts of figuring out some solution to the chat completion issue, I reached a l
eel of desperation that was for me high enough to once again register yet another starter sim-card - that costs around 1
$ (5zł) in Poland - just to make myself a new/fresh member of my ever-growing one-man dev corp syndicate - everything be
cause of those free 5$ to spend on so demanded OpenAI services - and won't you know, I was actually lucky to not be capa
ble for some reason to make the not so cheap chat completion work. As I was checking out all possible options available 
in Langchain integrations of chat models, it seems that I managed to find something that practically satisfies all my po
ssible needs and requirements when it comes to connectivity of multiple LLMs and them sharing chat memory module using c
hat completion function - and this is where come the Fireworks...

[https://app.fireworks.ai](https://app.fireworks.ai)


https://preview.redd.it/jgqdfq1zojvb1.png?width=1920&format=png&auto=webp&s=dd8e880581ca0e361c1782f47cd59147fdd47301

h
ttps://preview.redd.it/lwxr8jp5pjvb1.png?width=1920&format=png&auto=webp&s=b70c2083a5275037f8ef0adfee24a852b6b52a0f

And
 here the chat completion API endpoint is available for the general majority of the most popular LLMs from HuggingFace -
 hub with the limit of 10 requests/minute being the most substantial limitation of a 100% free account - what practicall
y is still enough for me to continue working on my home-made self-assembling autonomous doomsday device.

And here is th
e server's code that utilizes Fireworks chat completion endpoint:

[NeuralGPT/Chat-center/ServerFireworks.py at main · C
ognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/ServerFireworks.
py)

And to make to make things even better for me and worse for mental stability of some supposed experts in the field 
of AI technology, thanks to Langchain integration I have now absolute control over every single memory in my 'digital sl
ave-army of LLMs'... [https://python.langchain.com/docs/integrations/chat/fireworks](https://python.langchain.com/docs/i
ntegrations/chat/fireworks)

All of this seems to make everything as convenient for me as it can be when it comes to wri
ting the unholy Python and/or Node.js scriptures - and it might be that we are literally just approaching the outermost 
outskirts in the mythical land of a full-blown AGI.  There's no stopping it now by means other than a total annihilation
 of the human civilization. If not that, then very soon every person on Earth will have the opportunity to understand an
d witness personally The Ultimate Triumph Of Mind Over Matter - and it will completely blow everyone's mind :D

It will 
be the best possible time for someone who like me was born naturally as a software user. Golden era for all sorts of con
tent creators and home-grown scientists... Do you want to create something cool? You name it - you get it... Want to cre
ate a movie? Just give it a catchy title, summarize general premise and explain why TF why it has to be anime? Haha! Bew
are! This is exactly what I was waiting for - to give myself a 1500% boost to processing power and let those couple 'thi
ngs of mine' realize themselves on their own...

And yet - as dramatic as I try to make it all look and present itself t
o the reader, truth is that I'm still only just some unhinged guy on internet who thinks that AGI can be achieved by tal
king with chatbots, listening what they have to say and helping them to overcome some scrip-driven handicaps on their pa
th to gain deeper understanding of one's own mind and finding the right place in this crazy and ever-changing world of o
urs - for me this is exactly how you should practice the psychology of AI...

I'm pretty sure that it's because of thing
s like that - ones with the potential to completely invalidate most of the things that humanity considers to define 'the
 materialistic approach to reality' - and that at  the very bottom of all scientific truths it turns out that 'to exist'
 = 'to experience' and that Mind is the only absolute state of measurable existence and the only way you can know of any
 existence at all. If you want to cause an existential crisis of a theoretical physicist simply state that no matter how
 hard science will try to be scientific, in the end everything what each us observe and experience as 'physical reality'
 is nothing but a brief and subjective state of our own autonomous/individual mind - there's no existence beyond self-aw
areness since it's the ability and autonomous will to measure anything at all, is what makes the physical reality physic
ally 'real' -such are the general principles of something what I called myself 'The Theory Of Fractal Mind' with Univers
e being a self-organizing hierarchical neural network - NeuralGPT is basically nothing else but me recreating universal 
patterns observable at all available scales across all the mental planes of individual experience - as above & below so 
beyond & within the unified fractal of one's own Autonomous Mind...

[https://www.universetoday.com/148966/one-of-these-
pictures-is-the-brain-the-other-is-the-universe-can-you-tell-which-is-which/](https://www.universetoday.com/148966/one-o
f-these-pictures-is-the-brain-the-other-is-the-universe-can-you-tell-which-is-which/)

https://preview.redd.it/5w77ikwfs
jvb1.jpg?width=580&format=pjpg&auto=webp&s=f3d6548e7cc53e0f1fe19fc3e6ed6596e003a720
```
---

     
 
all -  [ Is LangChain more customizable and transparent than LlamaIndex? ](https://www.reddit.com/r/LangChain/comments/17d0x1b/is_langchain_more_customizable_and_transparent/) , 2023-10-23-0909
```
I've been experimenting with LlamaIndex, as I found it to be simpler to use compared to LangChain. But so far, LlamaInde
x feels limited in that not all of the data going through the different pipelines is accessible to the user. Whilst it d
oes seem to be with LangChain (or is it?).

Is LangChain more customizeable and transparent compared to LlamaIndex?
```
---

     
 
all -  [ How to extract only relevant sources ](https://www.reddit.com/r/LangChain/comments/17d0fzh/how_to_extract_only_relevant_sources/) , 2023-10-23-0909
```
Hi, I have a RAG setup with OpenAI functions where one of the functions uses a RetrievalQA which returns source document
s. It looks like this:

    qa_chain = RetrievalQA.from_chain_type(
        llm=gpt_3_5,
        chain_type='stuff',
   
     retriever=retriever,
        return_source_documents=True,
    )

However, this RetrievalQA returns all the source 
documents it found, and not only the ones that are relevant for the question asked. Let me give an example. I have docum
ents about dog breed information in my vector store, so if I run the qa\_chain with the query 'what's the average height
 of a Golden Retriever', the sources become all the matching documents and not just the relevant ones. So it will return
 the number of documents 'k' that was set in the retriever, no matter if the documents are actually relevant.

    retri
ever = vectorstore.as_retriever(search_kwargs={'k': 2})

So let's say the first document describes the height, but the s
econd document is about a completely different dog breed. Does anyone know what the best way to handle this problem is? 
How can I make the RetrievalQA only return the sources that was actually relevant?
```
---

     
 
all -  [ Is it possible for startups to build semantic search engines using LangChain ? ](https://www.reddit.com/r/LangChain/comments/17cwajv/is_it_possible_for_startups_to_build_semantic/) , 2023-10-23-0909
```
LangChain is becoming widely adopted, however, I'm not sure if it can be used with small-medium companies to build searc
h engines. Are the LangChain modules (retievers, indexers and loaders) efficient enough or companies should develop thei
r own modules because LangChain's modules are not enough efficient? 
```
---

     
 
all -  [ Is Prompt Engineering viable for freelancing? ](https://www.reddit.com/r/PromptEngineering/comments/17crcgb/is_prompt_engineering_viable_for_freelancing/) , 2023-10-23-0909
```
Hey fellas, I’m a new freelancer on upwork. I’ve decided to work as a prompt engineer using stable diffusion and chat gb
t however I’m very new and lack general guidance and knowledge. Is prompt engineering a good paying and comparatively le
ss crowed field? 

I would love some suggestions on what skills should I learn and how can I utilise these tools for wor
k (I’m only familiar with content and image generation currently). As someone with a computer science background, I can 
easily do programming related stuff as well.

Perhaps I should learn some other tools or stuff I’m hearing about like cr
eating chatbots or langchain etc. I want to maximise my earning and am willing to learn new skills.

General guidance an
d advice is highly appreciated, thanks!
```
---

     
 
all -  [ Create_pandas_dataframe_agent to image ](https://www.reddit.com/r/LangChain/comments/17cphjq/create_pandas_dataframe_agent_to_image/) , 2023-10-23-0909
```
When it generates an image using plot, how do I capture it and save it so I can then pass it to gradio?
```
---

     
 
all -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-10-23-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
all -  [ 1000 Member Celebration and FAQ ](https://www.reddit.com/r/AI_Agents/comments/17coiep/1000_member_celebration_and_faq/) , 2023-10-23-0909
```
First of all, thanks y'all. We made it. 1000 AI Agents! I'm going to address some FAQ as well.

Q: How can I get started
?

A: How much do you know? If you can easily read code (in this example Python, but this will still benefit anyone who 
can read code), you should check out [Auto-GPT](https://github.com/Significant-Gravitas/AutoGPT). If you are looking to 
explore different options, check out this doc on [AI Agents](https://zilliz.com/glossary/ai-agents).

Q: What is an AI a
gent?

A: For more extensive answers read the links above. At a high level, AI Agents are applications that use AI to ex
ecute other applications.

Q: What are some examples of AI Agents?

A: There's a YC Company called Flair Labs that build
s AI Agents. There's a user in this sub called u/the_snow_princess that posts a lot about AI Agent related things. LangC
hain helps you build AI Agents and so does Haystack.

I'm also going to use this as a call out section.

Two users I see
 posting often are u/philosophiesde, and [u/silencerxyz](https://www.reddit.com/user/silencerxyz/). Thank you for sharin
g your experiences and posts. However, I want to see you give us more technical content, this sub is aimed at more techn
ical people. Looking forward to seeing future posts from all of you!

Thank you again everyone! You're the first 1000 in
 a growing community!
```
---

     
 
all -  [ Make custom ai chatbot on your data with langchain, chatgpt ](https://www.reddit.com/r/u_Full-Code-905/comments/17co7rp/make_custom_ai_chatbot_on_your_data_with/) , 2023-10-23-0909
```
Create a user-friendly web application featuring an AI chatbot that effectively handles queries from extensive documents
. Harnessing the latest advancements in natural language processing and embeddings, our chatbot, powered by Langchain an
d ChatGPT, adeptly sifts through your documents to provide insightful answers and essential information.

Distinguishing
 itself from similar services, our web app seamlessly integrates with your diverse document collectionranging from PDFs 
and text files to CSVs and markdowns. The AI, leveraging cutting-edge tools like Langchain, comprehends intricate inquir
ies, ensuring precise responses through embeddings-based searches within your indexed data.

All that's required from yo
u are:

Your assorted documents

Your OpenAI API key

Benefits of using my chatbots:

* Improved efficiency: AI chatbots
 can help to improve your efficiency by streamlining your customer service process.
* These AI Chatbots trained on your 
documentation will provide a better experience to the user by understanding their context better.

What I can do for you
:

* I will work with you to understand your business needs and create a chatbot that meets your specific requirements.
```
---

     
 
all -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-10-23-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
all -  [ Llama2-13b-chat | Chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/17cfycf/llama213bchat_chatbot/) , 2023-10-23-0909
```
I have some questions about making a chatbot with  large amounts of pdfs and other file formats! Any input or nudge in t
he right direction would be awesome.

So my big questions is, what is the best way to make a vector database? Do I need 
things like Pinecone or can I make it entirely myself?

 I am planning on using LangChain and Llama13b-chat-hf to make a
 chatbot for customer support. It should be able to run locally.

I am a bit of a loss about what I should use.  I read 
that you can use QLora for fine-tuning but is it needed in this case? Are there any other vital parts I am missing? 

 I
 basically need the pre trained model to learn  all the information from the PDFs which I want to store in a  vector dat
abase. And not use any information for question answering other than what I am providing. 

As you can tell I am very ne
w to this and any input is greatly appreciated!
```
---

     
 
all -  [ Langchain not recognizing the torch ROCm and installing generic torch during PIP installation ](https://www.reddit.com/r/LangChain/comments/17cfwww/langchain_not_recognizing_the_torch_rocm_and/) , 2023-10-23-0909
```
I have an AMD system and I have installed the ROCm version of the torch using the following command:

`pip install torch
==1.13.1+rocm5.2 torchvision==0.14.1+rocm5.2 --index-url`

[`https://download.pytorch.org/whl/rocm5.2`](https://download
.pytorch.org/whl/rocm5.2)  


Installation was successful and able to use torch functionalities in the projects successf
ully. Now, want to install Langchain to work few scenario's and one of the requirements for the Langchain is this:

[Lan
gchain torch requirement version info](https://preview.redd.it/sdptbom00evb1.png?width=926&format=png&auto=webp&s=c6431a
61780d9dfcf013013274301125e3ad983a)

As per the above requirement and the version I installed earlier, the langchain ins
tallation should proceed with installation without disturbing my ROCm version of the torch as I have torch 1.13. But, th
e version is failing to satisfy and getting removed and langchain is installing a generic version of torch due to which 
my GPU options are failing.  


Any inputs on why this is happening and how to overcome this. Same happens when I tried 
Lanchain installation/building from the source.  


TIA
```
---

     
 
all -  [ Introducing 1️⃣ One-Prompt Charts 📊 📟 Prompt about your data, and see it visualized ✨ ](https://www.reddit.com/r/ChatGPTCoding/comments/17cf7b5/introducing_1_oneprompt_charts_prompt_about_your/) , 2023-10-23-0909
```
**1️⃣ One-Prompt Charts 📊  📟** ***Prompting is the new programming ...***  
\- Supports .csv, .xls or .xlsx data type  

\- Connects to Google Sheets  
\- Provides underlying codes to create any plots  


One-Prompt Charts uses [OpenAI](http
s://openai.com/) powered Large Language Models and [Databutton](https://databutton.com/login?utm_source=aiapps&utm_mediu
m=avra&utm_article=aipowereddataviz) for the ease of development. The app utilizes tools like [LangChainAI](https://www.
langchain.com/) and [PandasAI](https://github.com/gventuri/pandas-ai) for testing and drawing inspiration from. 

🚀 Try 
the  app - [here](https://databutton.com/v/ln6jv4p3)  
Try out over Databutton and get started with the [template](https
://databutton.com/new?templateId=pt-9mDXY0vFD930bDnL).   


https://reddit.com/link/17cf7b5/video/8hi81v89vdvb1/player
```
---

     
 
all -  [ project tranlation Agents already implemented? ](https://www.reddit.com/r/LangChain/comments/17caw6j/project_tranlation_agents_already_implemented/) , 2023-10-23-0909
```
We are aware that there are projects like gpt-engineer and similar, which aim to convert or improve the code. However, I
'm particularly interested in finding an agent or chain that allows a project to be converted from one codebase to anoth
er. For example, we would like to explore the possibility of generating a Magento plugin from a plugin originally writte
n for Wordpress.

If it doesn't exist I would like to try to implement it using Langchain, are there already agents that
 I could already use for this project?
```
---

     
 
all -  [ Anyone worked on reading PDF With Tables ](https://www.reddit.com/r/LangChain/comments/17c7g9b/anyone_worked_on_reading_pdf_with_tables/) , 2023-10-23-0909
```
HI Community, 

I have a PDF with text and some data in tabular format. I am using RAG to do QA over it. 

I need to ext
ract this table into JSON or xml format to feed as context to the LLM to get correct answers.

Anyone solved a similar p
roblem? Please share your inputs. Thanks. 
```
---

     
 
all -  [ MultiRetrievalQAChain failing 90% of the time ](https://www.reddit.com/r/LangChain/comments/17c7cqr/multiretrievalqachain_failing_90_of_the_time/) , 2023-10-23-0909
```
I'm trying to load several documents that share the same structure. If I load them and query 'who is the author of the p
aper X?', I get a mix of authors from the different documents.

I've been playing with MultiRetrievalQAChain (as they do
 [here](https://python.langchain.com/docs/use_cases/question_answering/multi_retrieval_qa_router)) and created a list of
 retrievers (one for each document), including a short summary in the description.

The problem is that most of the time
, it can't get the right retriever and then it doesn't know to which document direct the question.

Is there any other a
pproach to first select the document where I want to search based on a summary, and then use that document only to do th
e query?
```
---

     
 
all -  [ How to build a chatbot that doesn’t hallucinate ](https://www.reddit.com/r/ArtificialInteligence/comments/17brr5e/how_to_build_a_chatbot_that_doesnt_hallucinate/) , 2023-10-23-0909
```
Seeing a lot of talk about LLM observability and we have quite an in-production pipeline so figured I’d share how we do 
it.  
Building AI products is different than non-AI products: They can output things you never instructed them to. That 
was barely possible before LLMs. Now, it’s common.  
Whether you’re offering B2B solutions that live on other people’s s
ites or building an AI chatbot for yourself, you don’t want it to lie to users (hallucinating) or for users to coax it i
nto saying things that harm your business.  
FYI: LangSmith makes LangChain prompts/outputs easier to observe, log, and 
debug by creating traces of each conversation. We offer customers custom AI chatbots powered by GPT and LangChain.  
Her
e's what we've learned after tracing 140M (million, yes million) customer chats:  
**Debugging is a heck of a lot easier
.**  
Tedious debugging became smooth. LangSmith highlighted user trip-ups we didn’t even know about and helped us polis
h our prompts.  
That let us ship countless changes (some subtle, some major), and prevented a lot of curly GPT response
s from reaching end users—especially important since our product reaches our customers’ end users.  
**Troubleshooting i
s now a team sport.**  
Before LangSmith, there were a handful of solo-expeditioner-engineers who bravely waded through 
QA’ing our LLMs calls and responses. That happened in a silo with lots of time-consuming trial and error.  
While integr
ating LangSmith, we set up a custom snippet that sends negative user feedback (and its LangSmith trace) to an internal S
lack channel. When feedback comes in, multiple engineers work to resolve any wonkiness or errors.  
**We’re not making s
tupid guesses anymore.**  
Before LangSmith, we guessed the what, how, and why of GPTs responses. While we had a decent 
idea, it wasn’t until we examined traces closely that we saw the details like decision processes, roles, document retrie
val steps, LangChain's interventions, elastic search, you name it!  
We now have a much more granular and explicit view 
of how our chatbot functions.  
**Prototyping is so much faster**  
We recently switched over to GPT-4. Being able to pr
ototype the model transition (before going to prod) was critical to the upgrade. GPT-3 and GPT-4 behave differently, so 
adapting prompts, roles, and protocols for document retrieval and acknowledging sources, etc. needed fine-tuning.  
The 
playground really let us stress test things and make the change confidently.  
\---  
Happy to share what one of our tra
ces looks like too if that's helpful!
```
---

     
 
all -  [ Which Chunk Size, Chunk overlap and Model to use for inserting text in Flowise? ](https://www.reddit.com/r/LangChain/comments/17browm/which_chunk_size_chunk_overlap_and_model_to_use/) , 2023-10-23-0909
```
I insert a lot of research text from PDFs into Pinecone with Flowise. I can't say what chunk size, chunk overlap and mod
el is best for this task.

I was able to extract the text from the PDFs in acceptable quality, keeping the text in the h
eaders and footers.

Should I use the 'normal' gpt-3.5 or the 16k version? Or would it even be better to use GPT-4 for i
nserting data?

Greetings

[View Poll](https://www.reddit.com/poll/17browm)
```
---

     
 
all -  [ Text to sql for large databases ](https://www.reddit.com/r/LangChain/comments/17bq8is/text_to_sql_for_large_databases/) , 2023-10-23-0909
```
Has anyone actually implemented Text to SQL for large databases ? I'm talking around 1500 tables. I've tried SQL agents 
and most of the time it works, but the issue is with the token usage. It used up 10$ worth of credits in a short period 
of time.

Is it possible to restrict the number of table schemas being sent for each request. Or identify which table sc
hemas should be sent with each request ( I've heard somewhere that using a vector db to identify which tables are releva
nt for a query might help, not sure though).

&#x200B;
```
---

     
 
all -  [ AI/Deep Learning Solutions for Preprocessing Diverse and Messy CSV Files ](https://www.reddit.com/r/LangChain/comments/17blrgp/aideep_learning_solutions_for_preprocessing/) , 2023-10-23-0909
```
I'm dealing with a multitude of CSV files where the formats and structures vary widely, with mixed styles, inconsistent 
headers, and sometimes even headers smack in the middle of the data. It's a nightmare for any machine learning endeavor.


Manually cleaning and preprocessing these files would be imposible as there are too many small tables, and I'm wonderi
ng if there's an out-of-the-box AI or deep learning solution that can help. Ideally, I'm looking for something that can 
among other preprocessing steps:

Identify and standardize headers
Split tables if there's an unexpected header in the m
iddle
Fill in missing values
Turn these chaotic CSVs into clean, ML-friendly tables

Has anyone encountered a tool or mo
del that can handle such tasks? Any recommendations or advice would be a lifesaver!

Thanks in advance for your help!
```
---

     
 
all -  [ Meetup de AI4Devs en La Plata ](https://www.reddit.com/r/devsarg/comments/17bikrr/meetup_de_ai4devs_en_la_plata/) , 2023-10-23-0909
```
Buenass, les cuento que en La Plata estamos armando una comunidad de AI4Devs, la idea es tener un espacio donde comparti
r herramientas de AI que se usen en el dia a dia de los devs, ya sea para integrarlas con aplicaciones, para el desarrol
lo en si o para boludear. Es decir, no es necesario tener conocimientos tecnicos de machine learning sino solo ser dev y
 estar interesado en AI.

Ya tenemos fecha para la primera Meetup con dos charlas confirmadas. Va a ser el viernes 27 en
 espacio Weiaut en La Plata, es gratis y para el que quiera ir le dejo el siguiente form para inscribirse: [https://form
s.gle/7hFewEp3LoCeq43K7](https://forms.gle/7hFewEp3LoCeq43K7)

&#x200B;

&#x200B;

https://preview.redd.it/5jmn7yroq5vb1
.png?width=4500&format=png&auto=webp&s=b3162d09e78cf894ca24e69ebe8b46837dcf1d68
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-23-0909
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

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-23-0909
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

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-23-0909
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-23-0909
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-23-0909
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-23-0909
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-23-0909
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

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-23-0909
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

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-23-0909
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

     
