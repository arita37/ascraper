 
all -  [ how to use mixed raw input and inferred input from ZERO_SHOT_REACT_DESCRIPTION agent ](https://www.reddit.com/r/LangChain/comments/17deqnp/how_to_use_mixed_raw_input_and_inferred_input/) , 2023-10-22-0910
```
I have multiple tools in agent = initialize\_agent(  
tools, llm, agent=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION, verbos
e=True  
), by default it will infer the user msg and according to the tool schema setup, however, I have another tool w
hich I need to take full raw user input, not sure if there's any way to do that
```
---

     
 
all -  [ Is there an alternative to Zapier NLA? ](https://www.reddit.com/r/LangChain/comments/17d9q75/is_there_an_alternative_to_zapier_nla/) , 2023-10-22-0910
```
I had build various applications using the NLA api of Zapier and I loved that to be honest. But it is dissappointing to 
see that they are discontinuing it soon:  


[https://nla.zapier.com/sunset/](https://nla.zapier.com/sunset/)  


Do we 
have a similar service which could be used as an alternative for it? all answers are appreciated
```
---

     
 
all -  [ Please confirm you want to do x, y and z. ](https://www.reddit.com/r/LangChain/comments/17d9kvg/please_confirm_you_want_to_do_x_y_and_z/) , 2023-10-22-0910
```
Hello Everyone. 

Is there a way to get prompt verification message such as 'Ok, so you want to do this , that amd the o
ther correct?'. So the user chatting with the llm makes sure that there is user approval and not just corrsing of finger
s and hoping the llm uses the tools correctly. We tried adding something like 'please repeat the action that habe been q
ueried before proceeding' but we are not getting lucky.

Thank you!
```
---

     
 
all -  [ Suggestions before moving to production ](https://www.reddit.com/r/LocalLLaMA/comments/17d6wjq/suggestions_before_moving_to_production/) , 2023-10-22-0910
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

     
 
all -  [ Discover the fundamentals of ModularMind. Learn how to harness the power of machine learning models, ](https://youtu.be/Dyh5j_bkoJA) , 2023-10-22-0910
```

```
---

     
 
all -  [ NeuralGPT - Creating Universal Chat Memory Module For Multiple LLMs In A Cooperative Multi-Agent Net ](https://www.reddit.com/r/AIPsychology/comments/17d1eyl/neuralgpt_creating_universal_chat_memory_module/) , 2023-10-22-0910
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

     
 
all -  [ Is LangChain more customizable and transparent than LlamaIndex? ](https://www.reddit.com/r/LangChain/comments/17d0x1b/is_langchain_more_customizable_and_transparent/) , 2023-10-22-0910
```
I've been experimenting with LlamaIndex, as I found it to be simpler to use compared to LangChain. But so far, LlamaInde
x feels limited in that not all of the data going through the different pipelines is accessible to the user. Whilst it d
oes seem to be with LangChain (or is it?).

Is LangChain more customizeable and transparent compared to LlamaIndex?
```
---

     
 
all -  [ How to extract only relevant sources ](https://www.reddit.com/r/LangChain/comments/17d0fzh/how_to_extract_only_relevant_sources/) , 2023-10-22-0910
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

     
 
all -  [ Is it possible for startups to build semantic search engines using LangChain ? ](https://www.reddit.com/r/LangChain/comments/17cwajv/is_it_possible_for_startups_to_build_semantic/) , 2023-10-22-0910
```
LangChain is becoming widely adopted, however, I'm not sure if it can be used with small-medium companies to build searc
h engines. Are the LangChain modules (retievers, indexers and loaders) efficient enough or companies should develop thei
r own modules because LangChain's modules are not enough efficient? 
```
---

     
 
all -  [ Is Prompt Engineering viable for freelancing? ](https://www.reddit.com/r/PromptEngineering/comments/17crcgb/is_prompt_engineering_viable_for_freelancing/) , 2023-10-22-0910
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

     
 
all -  [ Create_pandas_dataframe_agent to image ](https://www.reddit.com/r/LangChain/comments/17cphjq/create_pandas_dataframe_agent_to_image/) , 2023-10-22-0910
```
When it generates an image using plot, how do I capture it and save it so I can then pass it to gradio?
```
---

     
 
all -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-10-22-0910
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
all -  [ 1000 Member Celebration and FAQ ](https://www.reddit.com/r/AI_Agents/comments/17coiep/1000_member_celebration_and_faq/) , 2023-10-22-0910
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

     
 
all -  [ Make custom ai chatbot on your data with langchain, chatgpt ](https://www.reddit.com/r/u_Full-Code-905/comments/17co7rp/make_custom_ai_chatbot_on_your_data_with/) , 2023-10-22-0910
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

     
 
all -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-10-22-0910
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

     
 
all -  [ Llama2-13b-chat | Chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/17cfycf/llama213bchat_chatbot/) , 2023-10-22-0910
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

     
 
all -  [ Langchain not recognizing the torch ROCm and installing generic torch during PIP installation ](https://www.reddit.com/r/LangChain/comments/17cfwww/langchain_not_recognizing_the_torch_rocm_and/) , 2023-10-22-0910
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

     
 
all -  [ Introducing 1️⃣ One-Prompt Charts 📊 📟 Prompt about your data, and see it visualized ✨ ](https://www.reddit.com/r/ChatGPTCoding/comments/17cf7b5/introducing_1_oneprompt_charts_prompt_about_your/) , 2023-10-22-0910
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

     
 
all -  [ Introducing 1️⃣ One-Prompt Charts 📊 📟 Prompt about your data, and see it visualized ✨ ](https://www.reddit.com/r/GPT3/comments/17cf31v/introducing_1_oneprompt_charts_prompt_about_your/) , 2023-10-22-0910
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


https://preview.redd.it/88qz7grgudvb1.png?width=1434&format=
png&auto=webp&s=941aabf2be8dedf74958b0a130899b06259132f9
```
---

     
 
all -  [ project tranlation Agents already implemented? ](https://www.reddit.com/r/LangChain/comments/17caw6j/project_tranlation_agents_already_implemented/) , 2023-10-22-0910
```
We are aware that there are projects like gpt-engineer and similar, which aim to convert or improve the code. However, I
'm particularly interested in finding an agent or chain that allows a project to be converted from one codebase to anoth
er. For example, we would like to explore the possibility of generating a Magento plugin from a plugin originally writte
n for Wordpress.

If it doesn't exist I would like to try to implement it using Langchain, are there already agents that
 I could already use for this project?
```
---

     
 
all -  [ Anyone worked on reading PDF With Tables ](https://www.reddit.com/r/LangChain/comments/17c7g9b/anyone_worked_on_reading_pdf_with_tables/) , 2023-10-22-0910
```
HI Community, 

I have a PDF with text and some data in tabular format. I am using RAG to do QA over it. 

I need to ext
ract this table into JSON or xml format to feed as context to the LLM to get correct answers.

Anyone solved a similar p
roblem? Please share your inputs. Thanks. 
```
---

     
 
all -  [ MultiRetrievalQAChain failing 90% of the time ](https://www.reddit.com/r/LangChain/comments/17c7cqr/multiretrievalqachain_failing_90_of_the_time/) , 2023-10-22-0910
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

     
 
all -  [ How to build a chatbot that doesn’t hallucinate ](https://www.reddit.com/r/ArtificialInteligence/comments/17brr5e/how_to_build_a_chatbot_that_doesnt_hallucinate/) , 2023-10-22-0910
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

     
 
all -  [ Which Chunk Size, Chunk overlap and Model to use for inserting text in Flowise? ](https://www.reddit.com/r/LangChain/comments/17browm/which_chunk_size_chunk_overlap_and_model_to_use/) , 2023-10-22-0910
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

     
 
all -  [ Text to sql for large databases ](https://www.reddit.com/r/LangChain/comments/17bq8is/text_to_sql_for_large_databases/) , 2023-10-22-0910
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

     
 
all -  [ AI/Deep Learning Solutions for Preprocessing Diverse and Messy CSV Files ](https://www.reddit.com/r/LangChain/comments/17blrgp/aideep_learning_solutions_for_preprocessing/) , 2023-10-22-0910
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

     
 
all -  [ Meetup de AI4Devs en La Plata ](https://www.reddit.com/r/devsarg/comments/17bikrr/meetup_de_ai4devs_en_la_plata/) , 2023-10-22-0910
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

     
 
all -  [ Stable but Evolving Summary over Time? ](https://www.reddit.com/r/ChatGPTCoding/comments/17bikc7/stable_but_evolving_summary_over_time/) , 2023-10-22-0910
```
Does anyone have experience updating summarizations with addendums? I'm trying to take an existing summary (for which th
e original text has been discarded) and prompt to look at a new block of raw text and ask for an update to the summary t
o encode the new information.  


The challenge is that I'd like the summary to remain around the same length over time 
as this process iterates, keeping the most salient information in the summary. My attempts so far have yielded either (a
) dropping information because it is 're-summarizing' the summary in addition to incorporating the new addendum, or (b) 
just adding on new details to the summary over time. Where what I'd really like is for new 'important' details in the ad
dendums to trump less important details in existing summaries, and keep the summary size more or less stable over time. 
 


Happy for any pointers to places people have done this successfully -- prompt examples, langchain agents, etc. 
```
---

     
 
all -  [ How can I create user input/output for this code block? ](https://www.reddit.com/r/learnpython/comments/17bhhyt/how_can_i_create_user_inputoutput_for_this_code/) , 2023-10-22-0910
```
from langchain.chat\_models import ChatOpenAI  
from langchain.prompts import HumanMessagePromptTemplate  
from langchai
n.schema.messages import SystemMessage  
chat\_template = ChatPromptTemplate.from\_messages(  
\[  
SystemMessage(  
con
tent=(  
'You are a helpful assistant that re-writes the user's text to '  
'sound more upbeat.'  
)  
),  
HumanMessage
PromptTemplate.from\_template('{text}'),  
\]  
)  
llm = ChatOpenAI()  
llm(chat\_template.format\_messages(text='i don
t like eating tasty things.'))  


Its my first time using langchain and I'm curious
```
---

     
 
all -  [ i'm having problem while using LLama2 models with Langchain , tell me the best way to work with LLam ](https://www.reddit.com/r/LangChain/comments/17bfqdy/im_having_problem_while_using_llama2_models_with/) , 2023-10-22-0910
```
So many Errors , when i try to use ChatpromptTemplate it gives me error , it does not recognize the chat models or LLMs


  
 

`callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])`  
`# Make sure the model path is correct
 for your system!`  
`llm = LlamaCpp(`  
 `model_path='models/llama-2-13b-chat.ggmlv3.q4_0.bin', callback_manager=callba
ck_manager, verbose=True,n_ctx=4096, max_tokens=1000, last_n_tokens_size=1000 , temperature=0`  
`)`  
`llama_embeddings
 = LlamaCppEmbeddings(model_path='models/llama-2-13b-chat.ggmlv3.q4_0.bin')`
```
---

     
 
all -  [ product recommendations advice ](https://www.reddit.com/r/LangChain/comments/17bdufy/product_recommendations_advice/) , 2023-10-22-0910
```
I am looking to a create a bot on WhatsApp that provides products based on a user's preferences.

5 questions - style, b
udget, etc 

It would then display 5 products that best match those preferences.

It would be linked to a product feed (
XML or RSS) so that would auto update.

What is the best tech stack to achieve this? E.g. openai, pinecone, langchain, e
tc.  What pitfalls should I be aware of?

I have experience building WhatsApp bots but this specific integration is new 
to me.

Thanks
```
---

     
 
all -  [ Update collection in Qdrant(don't want to create collection from scratch) ](https://www.reddit.com/r/LangChain/comments/17bc1ij/update_collection_in_qdrantdont_want_to_create/) , 2023-10-22-0910
```
I am using Qdrant as the vector db for a RAG project. I would like some inputs and thoughts on how to update the existin
g collection in qdrant. The user can upload multiple files and I am adding these documents embedding in the same collect
ion. Now if the user updates some text in one of the document instead of recreating the entire collection I want to upda
te the payload and vectors of the document that got updated. Recreating the collection from scratch is an expensive task
 is there way to update the collection by deleting the old document and inserting the new one and update document.
```
---

     
 
all -  [ Chatbot based on SQL results with temporary chat history? ](https://www.reddit.com/r/LangChain/comments/17bc0j1/chatbot_based_on_sql_results_with_temporary_chat/) , 2023-10-22-0910
```
Hello, 

First off, here is my background situation:
We have a table that contains scraped results of different articles
 around the globe (not sentiment analysis), and those articles might have thousand of keywords. 

The analytical team is
 requiring a chatbot that can ask questions based off these results.

By using SQL Chain from langchain, it kinda had th
e expected results. However, we have two problems:

1- The token limit is a pain, because most of the results are huge a
round 20k tokens.

2- The sqlchain isn't actually a chatbot. It just gives you an answer, but it won't respond to querie
s like 'make the previous answer in a json format', etc.

I know I am newbie in chatbots so I would like any general 'th
inking' process or direction, just point me to any topic
```
---

     
 
all -  [ 300+ Free Udemy Certificate Courses -Limited Time - 19/10/23 ](https://www.reddit.com/r/Newudemy/comments/17b9ld0/300_free_udemy_certificate_courses_limited_time/) , 2023-10-22-0910
```
 View All Courses: [https://inventhigh.net](https://inventhigh.net/)

1. WordPress Theme Development from Scratch 2.0-[h
ttps://inventhigh.net/udemy/advanced-wordpress-theme-development-with-bootstrap/](https://inventhigh.net/udemy/advanced-
wordpress-theme-development-with-bootstrap/)
2. WooCommerce Theme Development: Advanced Course-[https://inventhigh.net/u
demy/woocommerce-wordpress-theme-development/](https://inventhigh.net/udemy/woocommerce-wordpress-theme-development/)
3.
 Ultra-Fast WordPress Speed With 10Web WordPress Web Hosting-[https://inventhigh.net/udemy/ultra-fast-wordpress-speed/](
https://inventhigh.net/udemy/ultra-fast-wordpress-speed/)
4. Python Programming Language | Master Python Course (Arabic)
-[https://inventhigh.net/udemy/python\_tutorials/](https://inventhigh.net/udemy/python_tutorials/)
5. Python And Flask  
Demonstrations Practice Course-[https://inventhigh.net/udemy/python-and-flask-only-demonstration-course/](https://invent
high.net/udemy/python-and-flask-only-demonstration-course/)
6. Linux Tmux-[https://inventhigh.net/udemy/linux-tmux/](htt
ps://inventhigh.net/udemy/linux-tmux/)
7. Learn Web Design using WordPress & Start Freelancing-[https://inventhigh.net/u
demy/become-successful-wordpress-freelancer-to-make-money-online/](https://inventhigh.net/udemy/become-successful-wordpr
ess-freelancer-to-make-money-online/)
8. Haskell Exercises for Beginners-[https://inventhigh.net/udemy/haskell-exercises
-for-beginners/](https://inventhigh.net/udemy/haskell-exercises-for-beginners/)
9. Convert a one page HTML5 Template to 
a WordPress Theme-[https://inventhigh.net/udemy/convert-html5-template-to-wordpress-theme/](https://inventhigh.net/udemy
/convert-html5-template-to-wordpress-theme/)
10. Computer Basics-[https://inventhigh.net/udemy/basic-of-computer/](https
://inventhigh.net/udemy/basic-of-computer/)
11. CSS Crash Course For Beginners-[https://inventhigh.net/udemy/css-crash-c
ourse-for-beginners-g/](https://inventhigh.net/udemy/css-crash-course-for-beginners-g/)
12. Asteroids with Python PyGame
-[https://inventhigh.net/udemy/asteroids-with-python-pygame/](https://inventhigh.net/udemy/asteroids-with-python-pygame/
)
13. Linode: Foundations of Web Server Security-[https://inventhigh.net/udemy/linode-foundations-of-web-server-security
/](https://inventhigh.net/udemy/linode-foundations-of-web-server-security/)
14. Linode: Build and Deploy Responsive Webs
ites on the Cloud-[https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/](https://inven
thigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/)
15. Learn Bootstrap - For Beginners-[https://
inventhigh.net/udemy/learn-bootstrap-for-beginners/](https://inventhigh.net/udemy/learn-bootstrap-for-beginners/)
16. Ja
vaScript, Bootstrap, & PHP - Certification for Beginners-[https://inventhigh.net/udemy/javascript-bootstrap-php-certific
ation-for-beginners/](https://inventhigh.net/udemy/javascript-bootstrap-php-certification-for-beginners/)
17. Bootstrap 
& jQuery - Certification Course for Beginners-[https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-be
ginners/](https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-beginners/)
18. AWS Beginner to Interme
diate: EC2, IAM, ELB, ASG, Route 53-[https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/
](https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/)
19. AWS & React: Deploy an Auto-S
caling E-Commerce App with ELB-[https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/](
https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/)
20. DevOps Interview Questions P
reparation Guide - 2023-[https://inventhigh.net/udemy/devops-interview-questions-preparation-guide/](https://inventhigh.
net/udemy/devops-interview-questions-preparation-guide/)
21. Quantitative Finance with Python-[https://inventhigh.net/ud
emy/quantitative-finance-with-python/](https://inventhigh.net/udemy/quantitative-finance-with-python/)
22. Azure Open AI
 & Prompt Engineering Zero to Hero with Chatgpt-[https://inventhigh.net/udemy/azopenai/](https://inventhigh.net/udemy/az
openai/)
23. Object Oriented Programming in C++  &  Interview Preparation-[https://inventhigh.net/udemy/cracking-cpp-int
erview/](https://inventhigh.net/udemy/cracking-cpp-interview/)
24. Gatsby JS | Build a personal blog using gatsbyJS-[htt
ps://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/](https://inventhigh.net/udemy/g
atsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/)
25. Drupal For Absolute Beginners (2023)-[https://inventh
igh.net/udemy/drupal-masterclass/](https://inventhigh.net/udemy/drupal-masterclass/)
26. ChatGPT Plugins: The Complete G
uide-[https://inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/](https://inventhigh.net/udemy/chatgpt-plugins-the
-complete-guide/)
27. Build, Host & Manage WordPress Websites using AI \[10Web\]-[https://inventhigh.net/udemy/build-hos
t-manage-super-fast-wordpress-websites-in-10web/](https://inventhigh.net/udemy/build-host-manage-super-fast-wordpress-we
bsites-in-10web/)
28. PHP & MySQL - Certification Course for Beginners-[https://inventhigh.net/udemy/php-mysql-certifica
tion-course-for-beginners/](https://inventhigh.net/udemy/php-mysql-certification-course-for-beginners/)
29. Introduction
 to Domain Names and Web Hosting - Quick Guide-[https://inventhigh.net/udemy/introduction-to-domain-names-and-web-hostin
g-quick-guide/](https://inventhigh.net/udemy/introduction-to-domain-names-and-web-hosting-quick-guide/)
30. HTML, JavaSc
ript, & Bootstrap - Certification Course-[https://inventhigh.net/udemy/html-javascript-bootstrap-certification-course/](
https://inventhigh.net/udemy/html-javascript-bootstrap-certification-course/)
31. HTML & CSS - Certification Course for 
Beginners-[https://inventhigh.net/udemy/html-css-certification-course-for-beginners/](https://inventhigh.net/udemy/html-
css-certification-course-for-beginners/)
32. Create a Members Only Blog using PHP, MySQL, & AJAX-[https://inventhigh.net
/udemy/create-a-members-only-blog-using-php-mysql-ajax/](https://inventhigh.net/udemy/create-a-members-only-blog-using-p
hp-mysql-ajax/)
33. Configure NGINX on a Cloud Server: Digital Ocean & AWS-[https://inventhigh.net/udemy/configure-nginx
-on-a-cloud-server-digital-ocean-aws/](https://inventhigh.net/udemy/configure-nginx-on-a-cloud-server-digital-ocean-aws/
)
34. Cloud Computing Essentials: Linode, Linux, and LAMP Stack-[https://inventhigh.net/udemy/cloud-computing-essentials
-linode-linux-and-lamp-stack/](https://inventhigh.net/udemy/cloud-computing-essentials-linode-linux-and-lamp-stack/)
35.
 ChatGPT Expert Professional Certification-[https://inventhigh.net/udemy/chatgpt\_expert/](https://inventhigh.net/udemy/
chatgpt_expert/)
36. Adobe Lightroom Classic CC: Master the Library Module-[https://inventhigh.net/udemy/adobe-lightroom
-classic-cc-master-the-library-module/](https://inventhigh.net/udemy/adobe-lightroom-classic-cc-master-the-library-modul
e/)
37. Practical Photography for Absolute Beginners: 9 Courses in 1-[https://inventhigh.net/udemy/complete-photography-
course/](https://inventhigh.net/udemy/complete-photography-course/)
38. Practical Cisco Networking Labs in Cisco Packet 
Tracer-[https://inventhigh.net/udemy/practical-cisco-networking-labs/](https://inventhigh.net/udemy/practical-cisco-netw
orking-labs/)
39. Information Security Fundamentals-[https://inventhigh.net/udemy/infosec-fundamentals/](https://inventh
igh.net/udemy/infosec-fundamentals/)
40. Create a WordPress website with Hostinger!-[https://inventhigh.net/udemy/wordpr
ess-and-hosting-for-beginners/](https://inventhigh.net/udemy/wordpress-and-hosting-for-beginners/)
41. Tally Erp 9 + Tal
ly Prime + GST - Certificate Course-[https://inventhigh.net/udemy/tallygst/](https://inventhigh.net/udemy/tallygst/)
42.
 Building AI Saas Apps / AI Tools with \[No Code\] x ChatGPT-[https://inventhigh.net/udemy/ai-saas-apps/](https://invent
high.net/udemy/ai-saas-apps/)
43. Excel for Data Analysis & Financial Analysis-[https://inventhigh.net/udemy/microsoft-e
xcel-course-for-financial-analysis/](https://inventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/)
44. TI
KTOK Masterclass: Build Your Business With TIKTOK-[https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-w
ith-tiktok/](https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-with-tiktok/)
45. Squarespace Templates
 Unleashed: Rapid Professional Websites-[https://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional
-websites/](https://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional-websites/)
46. Squarespace B
ox of Tricks: Master Website Builders in 2023-[https://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/](https
://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/)
47. Sell Photo Online: Beginners Guide Stock Photography-
[https://inventhigh.net/udemy/mastering-stock-photography-step-by-step-guideline/](https://inventhigh.net/udemy/masterin
g-stock-photography-step-by-step-guideline/)
48. SEO Link Building & Content Writing Course: Get HQ Backlinks-[https://i
nventhigh.net/udemy/seo-link-building-2023/](https://inventhigh.net/udemy/seo-link-building-2023/)
49. PowerPoint - Micr
osoft PowerPoint For Beginners 2023-[https://inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/](https:
//inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/)
50. Macroeconomic Analysis: Investigating Inflati
on Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/](https://inve
nthigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/)
51. Learn 10 Ways to Make MORE Money on Y
ouTube!-[https://inventhigh.net/udemy/learn-to-make-money-on-youtube/](https://inventhigh.net/udemy/learn-to-make-money-
on-youtube/)
52. LangChain & OpenAI: Build Python Projects with No-Code 2023-[https://inventhigh.net/udemy/langchain-ope
nai-chatgpt-api-for-no-code-python-developers/](https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-py
thon-developers/)
53. JavaScript And PHP Programming Complete Course-[https://inventhigh.net/udemy/javascript-and-php-pr
ogramming-complete-course/](https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/)
54. How to Tra
nsform Your Life with 12 Amazing Powers-[https://inventhigh.net/udemy/12-great-powers-to-change-your-life/](https://inve
nthigh.net/udemy/12-great-powers-to-change-your-life/)
55. How to Make Money with YOUTUBE SHORTS Worldwide-[https://inve
nthigh.net/udemy/how-to-make-money-with-youtube-shorts/](https://inventhigh.net/udemy/how-to-make-money-with-youtube-sho
rts/)
56. How To Write Your Business Plan (in One Day} With ChatGPT-[https://inventhigh.net/udemy/business-planning-simp
lified-write-your-plan-with-chatgpt/](https://inventhigh.net/udemy/business-planning-simplified-write-your-plan-with-cha
tgpt/)
57. English Grammar tenses & structures-[https://inventhigh.net/udemy/english-grammar-course-tenses-structures/](
https://inventhigh.net/udemy/english-grammar-course-tenses-structures/)
58. Drinking Water Explained: Safety, Process & 
Challenges-[https://inventhigh.net/udemy/introduction-to-drinking-water-treatment/](https://inventhigh.net/udemy/introdu
ction-to-drinking-water-treatment/)
59. Dog Training Secrets: Behavior Insights-[https://inventhigh.net/udemy/dog-traini
ng-and-behavior-learn-research-backed-approaches/](https://inventhigh.net/udemy/dog-training-and-behavior-learn-research
-backed-approaches/)
60. ChatGPT: Make Money with ChatGPT as a New Freelancer-[https://inventhigh.net/udemy/chatgpt-make
-money-with-chatgpt-as-a-new-freelancer/](https://inventhigh.net/udemy/chatgpt-make-money-with-chatgpt-as-a-new-freelanc
er/)
61. Chair Yoga Teacher Training Certificate - Yoga Alliance CE-[https://inventhigh.net/udemy/chair-yoga-teacher-tra
ining-certificate-yoga-alliance-ce/](https://inventhigh.net/udemy/chair-yoga-teacher-training-certificate-yoga-alliance-
ce/)
62. C++ And Java Training Crash Course 2022-[https://inventhigh.net/udemy/c-and-java-training-crash-course-2022/](h
ttps://inventhigh.net/udemy/c-and-java-training-crash-course-2022/)
63. Best of Digital Marketing: #1 Digital Marketing 
Course 2023-[https://inventhigh.net/udemy/digital-marketing-2021/](https://inventhigh.net/udemy/digital-marketing-2021/)

64. YouTube Academy 2023: Complete Beginner to Pro Step-by-Step-[https://inventhigh.net/udemy/youtubeacademy/](https://
inventhigh.net/udemy/youtubeacademy/)
65. Work from Home : Work Life Balance and Time Management-[https://inventhigh.net
/udemy/work-from-home-work-life-balance/](https://inventhigh.net/udemy/work-from-home-work-life-balance/)
66. Video Edit
ing with Avid Media Composer First for Beginners-[https://inventhigh.net/udemy/learn-avid-media-composer-first-for-begin
ners/](https://inventhigh.net/udemy/learn-avid-media-composer-first-for-beginners/)
67. Video Editing with Adobe Premier
e Pro CC for Beginners-[https://inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/](https://in
venthigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/)
68. The Mega PRO Digital Marketing Course A-
Z : In Hindi-[https://inventhigh.net/udemy/learn-digital-marketing-course-hindi/](https://inventhigh.net/udemy/learn-dig
ital-marketing-course-hindi/)
69. The Complete Teach-Yourself Drummer's Guide-[https://inventhigh.net/udemy/the-complete
-teach-yourself-drummers-guide/](https://inventhigh.net/udemy/the-complete-teach-yourself-drummers-guide/)
70. The Art o
f the Portrait - Drawing For Beginners-[https://inventhigh.net/udemy/master-portrait-drawing/](https://inventhigh.net/ud
emy/master-portrait-drawing/)
71. Start a Profitable Affiliate Coupons Website -Passive Income-[https://inventhigh.net/u
demy/start-a-profitable-discount-coupons-website-passive-income/](https://inventhigh.net/udemy/start-a-profitable-discou
nt-coupons-website-passive-income/)
72. Print on Demand 2023: From Zero to Profitable Business-[https://inventhigh.net/u
demy/print-on-demand-course/](https://inventhigh.net/udemy/print-on-demand-course/)
73. PowerShell Functions Master Clas
s-[https://inventhigh.net/udemy/powershell-functions-master-class/](https://inventhigh.net/udemy/powershell-functions-ma
ster-class/)
74. Pedagogy in Teaching, Lesson Plan & Classroom Management-[https://inventhigh.net/udemy/pedagogy-in-teac
hing-lesson-plan-classroom-management/](https://inventhigh.net/udemy/pedagogy-in-teaching-lesson-plan-classroom-manageme
nt/)
75. Options Trading for Beginners - Intro Session-[https://inventhigh.net/udemy/options-trading-for-beginners-intro
-session/](https://inventhigh.net/udemy/options-trading-for-beginners-intro-session/)
76. Online Course Masterclass: Cre
ate Your Own Course In 30 Days-[https://inventhigh.net/udemy/online-course-masterclass/](https://inventhigh.net/udemy/on
line-course-masterclass/)
77. Media Mindful \[A Digital Detox Journey\]-[https://inventhigh.net/udemy/media-mindful-a-di
gital-detox-journey/](https://inventhigh.net/udemy/media-mindful-a-digital-detox-journey/)
78. Mastering Doodly: Create 
Engaging Whiteboard Animations-[https://inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/](https:
//inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/)
79. Make YouTube Thumbnails & Get More Views
 (Photoshop +Online)-[https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/](https:/
/inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/)
80. Macroeconomic Analysis: Investig
ating Inflation Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/]
(https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/)
81. Learn Structural Enginee
ring by Drawing Reading & ETABS-[https://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/](h
ttps://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/)
82. Learn Graphic Design using Canv
a & Start Freelancing-[https://inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/](https://
inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/)
83. Learn Content Writing using AI & St
art Freelancing-[https://inventhigh.net/udemy/ai-content-writing/](https://inventhigh.net/udemy/ai-content-writing/)
84.
 Learn Content Writing using AI & Make Money Online-[https://inventhigh.net/udemy/ai-content-course/](https://inventhigh
.net/udemy/ai-content-course/)
85. Learn Basics of Adobe Photoshop CC for Beginners-[https://inventhigh.net/udemy/learn-
basics-of-adobe-photoshop-cc-for-beginners/](https://inventhigh.net/udemy/learn-basics-of-adobe-photoshop-cc-for-beginne
rs/)
86. Learn Basics Of Adobe After Effects CC for Beginners-[https://inventhigh.net/udemy/learn-basics-of-adobe-after-
effects-cc-for-beginners-learn/](https://inventhigh.net/udemy/learn-basics-of-adobe-after-effects-cc-for-beginners-learn
/)
87. How to be a programmer | Full guide to start (Arabic)-[https://inventhigh.net/udemy/how\_to\_become\_a\_programme
r/](https://inventhigh.net/udemy/how_to_become_a_programmer/)
88. Grow Your YouTube Channel Faster 2023 (Advanced) StepB
yStep-[https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-proven-results-2022/](https://inventhigh.net/u
demy/the-youtube-academy-speed-growth-plan-proven-results-2022/)
89. Generate Income with Your YouTube, Despite Limited 
Views-[https://inventhigh.net/udemy/generate-income-with-your-youtube-despite-limited-views/](https://inventhigh.net/ude
my/generate-income-with-your-youtube-despite-limited-views/)
90. Fundamentals of computer science | Short Term Course(Ar
abic)-[https://inventhigh.net/udemy/basics\_of\_programming/](https://inventhigh.net/udemy/basics_of_programming/)
91. E
xecutive Diploma in Corporate Entrepreneurship-[https://inventhigh.net/udemy/corporate-entrepreneurship/](https://invent
high.net/udemy/corporate-entrepreneurship/)
92. Executive Diploma in Business Strategy-[https://inventhigh.net/udemy/dip
loma-business-strategy/](https://inventhigh.net/udemy/diploma-business-strategy/)
93. Executive Assistant Professional C
ertification (EAPC)-[https://inventhigh.net/udemy/executive-assistant/](https://inventhigh.net/udemy/executive-assistant
/)
94. Disruptive Thinking For World-Changing Innovative Ideas-[https://inventhigh.net/udemy/disruptive-thinking/](https
://inventhigh.net/udemy/disruptive-thinking/)
95. Diploma In Concrete Technology l Be a Concrete Technologist-[https://i
nventhigh.net/udemy/concrete-technologycivil-engineers-lifeline-in-construction/](https://inventhigh.net/udemy/concrete-
technologycivil-engineers-lifeline-in-construction/)
96. Create and Sell Digital Art using AI \[Passive Income\]-[https:
//inventhigh.net/udemy/ai-art-course/](https://inventhigh.net/udemy/ai-art-course/)
97. Color Grading and Video Editing 
with Davinci Resolve 18-[https://inventhigh.net/udemy/color-grading-and-video-editing-with-davinci-resolve/](https://inv
enthigh.net/udemy/color-grading-and-video-editing-with-davinci-resolve/)
98. Color Correction & Grading with Adobe Premi
ere Pro-[https://inventhigh.net/udemy/color-correction-grading-with-adobe-premiere-pro/](https://inventhigh.net/udemy/co
lor-correction-grading-with-adobe-premiere-pro/)
99. Cold Email & Lead Generation using AI \[Masterclass\]-[https://inve
nthigh.net/udemy/ai-cold-email/](https://inventhigh.net/udemy/ai-cold-email/)
100. Chat GPT & Midjourney: Personal Digit
al Marketing Assistants-[https://inventhigh.net/udemy/chatgpt-digital-marketing/](https://inventhigh.net/udemy/chatgpt-d
igital-marketing/)
101. C programming language | The Complete C Course (Arabic)-[https://inventhigh.net/udemy/c-programm
ing-language-from-a-to-z/](https://inventhigh.net/udemy/c-programming-language-from-a-to-z/)
102. Business Networking fo
r Success and Company Growth: Part One-[https://inventhigh.net/udemy/business-networking-1/](https://inventhigh.net/udem
y/business-networking-1/)
103. Build a Profitable Online Courses Business \[Complete Guide\]-[https://inventhigh.net/ude
my/complete-guide-become-a-six-figure-online-course-instructor/](https://inventhigh.net/udemy/complete-guide-become-a-si
x-figure-online-course-instructor/)
104. Become a Successful Affiliate Marketer \[Success Blueprint\]-[https://inventhig
h.net/udemy/become-a-six-figure-affiliate-marketer-success-blueprint/](https://inventhigh.net/udemy/become-a-six-figure-
affiliate-marketer-success-blueprint/)
105. Arabic| Learn Arabic with Mina | Comprehensive Arabic course-[https://invent
high.net/udemy/learn-arabic-language-d/](https://inventhigh.net/udemy/learn-arabic-language-d/)
106. Affiliate Marketing
 & MLM Network Marketing For Fashion-[https://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fas
hion/](https://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/)
107. AI x ChatGPT for Pr
oductivity 101 \[Masterclass\]-[https://inventhigh.net/udemy/ai-productivity/](https://inventhigh.net/udemy/ai-productiv
ity/)
108. AI for Business Strategy & Planning \[Masterclass\]-[https://inventhigh.net/udemy/ai-business-course/](https:
//inventhigh.net/udemy/ai-business-course/)
109. Private Equity Course for Beginners (PEQ101)-[https://inventhigh.net/ud
emy/private-equity-course-for-beginners-peq101/](https://inventhigh.net/udemy/private-equity-course-for-beginners-peq101
/)
110. Personal Brand Mastery : Online Personal Branding Essentials-[https://inventhigh.net/udemy/personal-branding-mas
tery-online-personal-branding-essentials/](https://inventhigh.net/udemy/personal-branding-mastery-online-personal-brandi
ng-essentials/)
111. Nuts & Bolts of Capital Markets-[https://inventhigh.net/udemy/nuts-bolts-of-capital-markets/](https
://inventhigh.net/udemy/nuts-bolts-of-capital-markets/)
112. Mechanical Engineering Mastery Series : HVAC Engineering 10
1-[https://inventhigh.net/udemy/mechanical-engineering-course/](https://inventhigh.net/udemy/mechanical-engineering-cour
se/)
113. Mastering Presentations and Public Speaking (Ultimate guide)-[https://inventhigh.net/udemy/presentations-and-p
ublic-speaking/](https://inventhigh.net/udemy/presentations-and-public-speaking/)
114. Investment Banking for Beginners 
(IB101)-[https://inventhigh.net/udemy/investment-banking-for-beginners-ib101/](https://inventhigh.net/udemy/investment-b
anking-for-beginners-ib101/)
115. Introduction to Microsoft Word for Beginners to Intermediate-[https://inventhigh.net/u
demy/introduction-to-microsoft-word-for-beginners/](https://inventhigh.net/udemy/introduction-to-microsoft-word-for-begi
nners/)
116. Internet & Cloud Computing Foundations-[https://inventhigh.net/udemy/internet-cloud-computing-foundations/]
(https://inventhigh.net/udemy/internet-cloud-computing-foundations/)
117. How the Internet Works & the Web Development P
rocess-[https://inventhigh.net/udemy/how-the-internet-works-the-web-development-process/](https://inventhigh.net/udemy/h
ow-the-internet-works-the-web-development-process/)
118. HVAC Design Basics : Understanding HVAC systems With Details-[h
ttps://inventhigh.net/udemy/hvac-systems/](https://inventhigh.net/udemy/hvac-systems/)
119. Financial Modeling in Excel 
- DCF Model of Big Books Corp-[https://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/](htt
ps://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/)
120. Financial Modeling | Social Medi
a Sector : Twitter-[https://inventhigh.net/udemy/financial-modeling-social-media-sector-twitter/](https://inventhigh.net
/udemy/financial-modeling-social-media-sector-twitter/)
121. Financial Modeling | Food & Beverages Sector : Starbucks-[h
ttps://inventhigh.net/udemy/financial-modeling-food-beverages-sector-starbucks/](https://inventhigh.net/udemy/financial-
modeling-food-beverages-sector-starbucks/)
122. Financial Analysis & Modeling | Islamic Banking-[https://inventhigh.net/
udemy/financial-modeling-islamic-banking-modeling/](https://inventhigh.net/udemy/financial-modeling-islamic-banking-mode
ling/)
123. Financial Analysis & Modeling | Automobile Sector-[https://inventhigh.net/udemy/financial-modeling-automobil
e-sector-maruti-suzuki/](https://inventhigh.net/udemy/financial-modeling-automobile-sector-maruti-suzuki/)
124. Computer
 Vision Fundamentals-[https://inventhigh.net/udemy/computer-vision-fundamentals/](https://inventhigh.net/udemy/computer-
vision-fundamentals/)
125. Complete Guide to Explosive Power Training-[https://inventhigh.net/udemy/athletic-power-train
ing-certificate/](https://inventhigh.net/udemy/athletic-power-training-certificate/)
126. Chief Customer Experience Offi
cer Executive Certification-[https://inventhigh.net/udemy/chief\_customer\_experience\_officer/](https://inventhigh.net/
udemy/chief_customer_experience_officer/)
127. Candlestick Chart Pattern & Renko Trading (2 Course Bundle)-[https://inve
nthigh.net/udemy/candlestick-renko/](https://inventhigh.net/udemy/candlestick-renko/)
128. CEO Chief Executive Officer E
xecutive Certification-[https://inventhigh.net/udemy/certified-chief-executive-officer/](https://inventhigh.net/udemy/ce
rtified-chief-executive-officer/)
129. Artificial General Intelligence (AGI)-[https://inventhigh.net/udemy/artificial-ge
neral-intelligence/](https://inventhigh.net/udemy/artificial-general-intelligence/)
130. Apache Hive for Data Engineers 
(Hands On) with 2 Projects-[https://inventhigh.net/udemy/apache-hive-for-data-engineers-hands-on/](https://inventhigh.ne
t/udemy/apache-hive-for-data-engineers-hands-on/)
131. 4 Comprehensive Practice Tests for any Python Certification-[http
s://inventhigh.net/udemy/4-comprehensive-practice-tests-for-any-python-certification/](https://inventhigh.net/udemy/4-co
mprehensive-practice-tests-for-any-python-certification/)
132. \[Weight Loss\] : Get Your Dream Body with Diet & Cardio-
[https://inventhigh.net/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/](https://inventhigh.net/udemy/weigh
t-loss-get-your-dream-body-with-nutrition-cardio/)
133. \[Tips & Technics\] : How to Lead Effective Meetings 2022 -New-[
https://inventhigh.net/udemy/tips-technics-how-to-lead-effective-meetings-2022/](https://inventhigh.net/udemy/tips-techn
ics-how-to-lead-effective-meetings-2022/)
134. \[Tips & Technics\] : How to Become a Great Leader Skills 2022-[https://i
nventhigh.net/udemy/tips-technics-how-to-become-a-great-leader-skills/](https://inventhigh.net/udemy/tips-technics-how-t
o-become-a-great-leader-skills/)
135. \[Practice Exams\] AWS Certified Solutions Architect Associate-[https://inventhigh
.net/udemy/practice-exams-aws-certified-solutions-architect-associate-u/](https://inventhigh.net/udemy/practice-exams-aw
s-certified-solutions-architect-associate-u/)
```
---

     
 
all -  [ 300+ Free Udemy Certificate Courses -Limited Time - 19/10/23 ](https://www.reddit.com/r/udemyfreebies/comments/17b9jpo/300_free_udemy_certificate_courses_limited_time/) , 2023-10-22-0910
```
 View All Courses: https://inventhigh.net                 

1. WordPress Theme Development from Scratch 2.0-[https://inv
enthigh.net/udemy/advanced-wordpress-theme-development-with-bootstrap/](https://inventhigh.net/udemy/advanced-wordpress-
theme-development-with-bootstrap/) 

2. WooCommerce Theme Development: Advanced Course-[https://inventhigh.net/udemy/woo
commerce-wordpress-theme-development/](https://inventhigh.net/udemy/woocommerce-wordpress-theme-development/) 

3. Ultra
-Fast WordPress Speed With 10Web WordPress Web Hosting-[https://inventhigh.net/udemy/ultra-fast-wordpress-speed/](https:
//inventhigh.net/udemy/ultra-fast-wordpress-speed/) 

4. Python Programming Language | Master Python Course (Arabic)-[ht
tps://inventhigh.net/udemy/python\_tutorials/](https://inventhigh.net/udemy/python_tutorials/) 

5. Python And Flask  De
monstrations Practice Course-[https://inventhigh.net/udemy/python-and-flask-only-demonstration-course/](https://inventhi
gh.net/udemy/python-and-flask-only-demonstration-course/) 

6. Linux Tmux-[https://inventhigh.net/udemy/linux-tmux/](htt
ps://inventhigh.net/udemy/linux-tmux/) 

7. Learn Web Design using WordPress & Start Freelancing-[https://inventhigh.net
/udemy/become-successful-wordpress-freelancer-to-make-money-online/](https://inventhigh.net/udemy/become-successful-word
press-freelancer-to-make-money-online/) 

8. Haskell Exercises for Beginners-[https://inventhigh.net/udemy/haskell-exerc
ises-for-beginners/](https://inventhigh.net/udemy/haskell-exercises-for-beginners/) 

9. Convert a one page HTML5 Templa
te to a WordPress Theme-[https://inventhigh.net/udemy/convert-html5-template-to-wordpress-theme/](https://inventhigh.net
/udemy/convert-html5-template-to-wordpress-theme/) 

10. Computer Basics-[https://inventhigh.net/udemy/basic-of-computer
/](https://inventhigh.net/udemy/basic-of-computer/) 

11. CSS Crash Course For Beginners-[https://inventhigh.net/udemy/c
ss-crash-course-for-beginners-g/](https://inventhigh.net/udemy/css-crash-course-for-beginners-g/) 

12. Asteroids with P
ython PyGame-[https://inventhigh.net/udemy/asteroids-with-python-pygame/](https://inventhigh.net/udemy/asteroids-with-py
thon-pygame/) 

13. Linode: Foundations of Web Server Security-[https://inventhigh.net/udemy/linode-foundations-of-web-s
erver-security/](https://inventhigh.net/udemy/linode-foundations-of-web-server-security/) 

14. Linode: Build and Deploy
 Responsive Websites on the Cloud-[https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud
/](https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/) 

15. Learn Bootstrap - For B
eginners-[https://inventhigh.net/udemy/learn-bootstrap-for-beginners/](https://inventhigh.net/udemy/learn-bootstrap-for-
beginners/) 

16. JavaScript, Bootstrap, & PHP - Certification for Beginners-[https://inventhigh.net/udemy/javascript-bo
otstrap-php-certification-for-beginners/](https://inventhigh.net/udemy/javascript-bootstrap-php-certification-for-beginn
ers/) 

17. Bootstrap & jQuery - Certification Course for Beginners-[https://inventhigh.net/udemy/bootstrap-jquery-certi
fication-course-for-beginners/](https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-beginners/) 

18.
 AWS Beginner to Intermediate: EC2, IAM, ELB, ASG, Route 53-[https://inventhigh.net/udemy/aws-beginner-to-intermediate-e
c2-iam-elb-asg-route-53/](https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/) 

19. AWS
 & React: Deploy an Auto-Scaling E-Commerce App with ELB-[https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-
e-commerce-app-with-elb/](https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/) 

20. 
DevOps Interview Questions Preparation Guide - 2023-[https://inventhigh.net/udemy/devops-interview-questions-preparation
-guide/](https://inventhigh.net/udemy/devops-interview-questions-preparation-guide/) 

21. Quantitative Finance with Pyt
hon-[https://inventhigh.net/udemy/quantitative-finance-with-python/](https://inventhigh.net/udemy/quantitative-finance-w
ith-python/) 

22. Azure Open AI & Prompt Engineering Zero to Hero with Chatgpt-[https://inventhigh.net/udemy/azopenai/]
(https://inventhigh.net/udemy/azopenai/) 

23. Object Oriented Programming in C++  &  Interview Preparation-[https://inv
enthigh.net/udemy/cracking-cpp-interview/](https://inventhigh.net/udemy/cracking-cpp-interview/) 

24. Gatsby JS | Build
 a personal blog using gatsbyJS-[https://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-grap
hql/](https://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/) 

25. Drupal For Abso
lute Beginners (2023)-[https://inventhigh.net/udemy/drupal-masterclass/](https://inventhigh.net/udemy/drupal-masterclass
/) 

26. ChatGPT Plugins: The Complete Guide-[https://inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/](https://
inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/) 

27. Build, Host & Manage WordPress Websites using AI \[10Web
\]-[https://inventhigh.net/udemy/build-host-manage-super-fast-wordpress-websites-in-10web/](https://inventhigh.net/udemy
/build-host-manage-super-fast-wordpress-websites-in-10web/) 

28. PHP & MySQL - Certification Course for Beginners-[http
s://inventhigh.net/udemy/php-mysql-certification-course-for-beginners/](https://inventhigh.net/udemy/php-mysql-certifica
tion-course-for-beginners/) 

29. Introduction to Domain Names and Web Hosting - Quick Guide-[https://inventhigh.net/ude
my/introduction-to-domain-names-and-web-hosting-quick-guide/](https://inventhigh.net/udemy/introduction-to-domain-names-
and-web-hosting-quick-guide/) 

30. HTML, JavaScript, & Bootstrap - Certification Course-[https://inventhigh.net/udemy/h
tml-javascript-bootstrap-certification-course/](https://inventhigh.net/udemy/html-javascript-bootstrap-certification-cou
rse/) 

31. HTML & CSS - Certification Course for Beginners-[https://inventhigh.net/udemy/html-css-certification-course-
for-beginners/](https://inventhigh.net/udemy/html-css-certification-course-for-beginners/) 

32. Create a Members Only B
log using PHP, MySQL, & AJAX-[https://inventhigh.net/udemy/create-a-members-only-blog-using-php-mysql-ajax/](https://inv
enthigh.net/udemy/create-a-members-only-blog-using-php-mysql-ajax/) 

33. Configure NGINX on a Cloud Server: Digital Oce
an & AWS-[https://inventhigh.net/udemy/configure-nginx-on-a-cloud-server-digital-ocean-aws/](https://inventhigh.net/udem
y/configure-nginx-on-a-cloud-server-digital-ocean-aws/) 

34. Cloud Computing Essentials: Linode, Linux, and LAMP Stack-
[https://inventhigh.net/udemy/cloud-computing-essentials-linode-linux-and-lamp-stack/](https://inventhigh.net/udemy/clou
d-computing-essentials-linode-linux-and-lamp-stack/) 

35. ChatGPT Expert Professional Certification-[https://inventhigh
.net/udemy/chatgpt\_expert/](https://inventhigh.net/udemy/chatgpt_expert/) 

36. Adobe Lightroom Classic CC: Master the 
Library Module-[https://inventhigh.net/udemy/adobe-lightroom-classic-cc-master-the-library-module/](https://inventhigh.n
et/udemy/adobe-lightroom-classic-cc-master-the-library-module/) 

37. Practical Photography for Absolute Beginners: 9 Co
urses in 1-[https://inventhigh.net/udemy/complete-photography-course/](https://inventhigh.net/udemy/complete-photography
-course/) 

38. Practical Cisco Networking Labs in Cisco Packet Tracer-[https://inventhigh.net/udemy/practical-cisco-net
working-labs/](https://inventhigh.net/udemy/practical-cisco-networking-labs/) 

39. Information Security Fundamentals-[h
ttps://inventhigh.net/udemy/infosec-fundamentals/](https://inventhigh.net/udemy/infosec-fundamentals/) 

40. Create a Wo
rdPress website with Hostinger!-[https://inventhigh.net/udemy/wordpress-and-hosting-for-beginners/](https://inventhigh.n
et/udemy/wordpress-and-hosting-for-beginners/) 

41. Tally Erp 9 + Tally Prime + GST - Certificate Course-[https://inven
thigh.net/udemy/tallygst/](https://inventhigh.net/udemy/tallygst/) 

42. Building AI Saas Apps / AI Tools with \[No Code
\] x ChatGPT-[https://inventhigh.net/udemy/ai-saas-apps/](https://inventhigh.net/udemy/ai-saas-apps/) 

43. Excel for Da
ta Analysis & Financial Analysis-[https://inventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/](https://i
nventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/) 

44. TIKTOK Masterclass: Build Your Business With T
IKTOK-[https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-with-tiktok/](https://inventhigh.net/udemy/ti
ktok-masterclass-build-your-business-with-tiktok/) 

45. Squarespace Templates Unleashed: Rapid Professional Websites-[h
ttps://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional-websites/](https://inventhigh.net/udemy/s
quarespace-templates-unleashed-rapid-professional-websites/) 

46. Squarespace Box of Tricks: Master Website Builders in
 2023-[https://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/](https://inventhigh.net/udemy/squarespace-web-
design-box-of-tricks/) 

47. Sell Photo Online: Beginners Guide Stock Photography-[https://inventhigh.net/udemy/masterin
g-stock-photography-step-by-step-guideline/](https://inventhigh.net/udemy/mastering-stock-photography-step-by-step-guide
line/) 

48. SEO Link Building & Content Writing Course: Get HQ Backlinks-[https://inventhigh.net/udemy/seo-link-buildin
g-2023/](https://inventhigh.net/udemy/seo-link-building-2023/) 

49. PowerPoint - Microsoft PowerPoint For Beginners 202
3-[https://inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/](https://inventhigh.net/udemy/powerpoint-
microsoft-powerpoint-for-beginners/) 

50. Macroeconomic Analysis: Investigating Inflation Trend with R-[https://inventh
igh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/](https://inventhigh.net/udemy/macroeconomic-a
nalysis-investigating-inflation-trend-with-r/) 

51. Learn 10 Ways to Make MORE Money on YouTube!-[https://inventhigh.ne
t/udemy/learn-to-make-money-on-youtube/](https://inventhigh.net/udemy/learn-to-make-money-on-youtube/) 

52. LangChain &
 OpenAI: Build Python Projects with No-Code 2023-[https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-
python-developers/](https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-python-developers/) 

53. Java
Script And PHP Programming Complete Course-[https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/
](https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/) 

54. How to Transform Your Life with 12
 Amazing Powers-[https://inventhigh.net/udemy/12-great-powers-to-change-your-life/](https://inventhigh.net/udemy/12-grea
t-powers-to-change-your-life/) 

55. How to Make Money with YOUTUBE SHORTS Worldwide-[https://inventhigh.net/udemy/how-t
o-make-money-with-youtube-shorts/](https://inventhigh.net/udemy/how-to-make-money-with-youtube-shorts/) 

56. How To Wri
te Your Business Plan (in One Day} With ChatGPT-[https://inventhigh.net/udemy/business-planning-simplified-write-your-pl
an-with-chatgpt/](https://inventhigh.net/udemy/business-planning-simplified-write-your-plan-with-chatgpt/) 

57. English
 Grammar tenses & structures-[https://inventhigh.net/udemy/english-grammar-course-tenses-structures/](https://inventhigh
.net/udemy/english-grammar-course-tenses-structures/) 

58. Drinking Water Explained: Safety, Process & Challenges-[http
s://inventhigh.net/udemy/introduction-to-drinking-water-treatment/](https://inventhigh.net/udemy/introduction-to-drinkin
g-water-treatment/) 

59. Dog Training Secrets: Behavior Insights-[https://inventhigh.net/udemy/dog-training-and-behavio
r-learn-research-backed-approaches/](https://inventhigh.net/udemy/dog-training-and-behavior-learn-research-backed-approa
ches/) 

60. ChatGPT: Make Money with ChatGPT as a New Freelancer-[https://inventhigh.net/udemy/chatgpt-make-money-with-
chatgpt-as-a-new-freelancer/](https://inventhigh.net/udemy/chatgpt-make-money-with-chatgpt-as-a-new-freelancer/) 

61. C
hair Yoga Teacher Training Certificate - Yoga Alliance CE-[https://inventhigh.net/udemy/chair-yoga-teacher-training-cert
ificate-yoga-alliance-ce/](https://inventhigh.net/udemy/chair-yoga-teacher-training-certificate-yoga-alliance-ce/) 

62.
 C++ And Java Training Crash Course 2022-[https://inventhigh.net/udemy/c-and-java-training-crash-course-2022/](https://i
nventhigh.net/udemy/c-and-java-training-crash-course-2022/) 

63. Best of Digital Marketing: #1 Digital Marketing Course
 2023-[https://inventhigh.net/udemy/digital-marketing-2021/](https://inventhigh.net/udemy/digital-marketing-2021/) 

64.
 YouTube Academy 2023: Complete Beginner to Pro Step-by-Step-[https://inventhigh.net/udemy/youtubeacademy/](https://inve
nthigh.net/udemy/youtubeacademy/) 

65. Work from Home : Work Life Balance and Time Management-[https://inventhigh.net/u
demy/work-from-home-work-life-balance/](https://inventhigh.net/udemy/work-from-home-work-life-balance/) 

66. Video Edit
ing with Avid Media Composer First for Beginners-[https://inventhigh.net/udemy/learn-avid-media-composer-first-for-begin
ners/](https://inventhigh.net/udemy/learn-avid-media-composer-first-for-beginners/) 

67. Video Editing with Adobe Premi
ere Pro CC for Beginners-[https://inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/](https://
inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/) 

68. The Mega PRO Digital Marketing Cours
e A-Z : In Hindi-[https://inventhigh.net/udemy/learn-digital-marketing-course-hindi/](https://inventhigh.net/udemy/learn
-digital-marketing-course-hindi/) 

69. The Complete Teach-Yourself Drummer's Guide-[https://inventhigh.net/udemy/the-co
mplete-teach-yourself-drummers-guide/](https://inventhigh.net/udemy/the-complete-teach-yourself-drummers-guide/) 

70. T
he Art of the Portrait - Drawing For Beginners-[https://inventhigh.net/udemy/master-portrait-drawing/](https://inventhig
h.net/udemy/master-portrait-drawing/) 

71. Start a Profitable Affiliate Coupons Website -Passive Income-[https://invent
high.net/udemy/start-a-profitable-discount-coupons-website-passive-income/](https://inventhigh.net/udemy/start-a-profita
ble-discount-coupons-website-passive-income/) 

72. Print on Demand 2023: From Zero to Profitable Business-[https://inve
nthigh.net/udemy/print-on-demand-course/](https://inventhigh.net/udemy/print-on-demand-course/) 

73. PowerShell Functio
ns Master Class-[https://inventhigh.net/udemy/powershell-functions-master-class/](https://inventhigh.net/udemy/powershel
l-functions-master-class/) 

74. Pedagogy in Teaching, Lesson Plan & Classroom Management-[https://inventhigh.net/udemy/
pedagogy-in-teaching-lesson-plan-classroom-management/](https://inventhigh.net/udemy/pedagogy-in-teaching-lesson-plan-cl
assroom-management/) 

75. Options Trading for Beginners - Intro Session-[https://inventhigh.net/udemy/options-trading-f
or-beginners-intro-session/](https://inventhigh.net/udemy/options-trading-for-beginners-intro-session/) 

76. Online Cou
rse Masterclass: Create Your Own Course In 30 Days-[https://inventhigh.net/udemy/online-course-masterclass/](https://inv
enthigh.net/udemy/online-course-masterclass/) 

77. Media Mindful \[A Digital Detox Journey\]-[https://inventhigh.net/ud
emy/media-mindful-a-digital-detox-journey/](https://inventhigh.net/udemy/media-mindful-a-digital-detox-journey/) 

78. M
astering Doodly: Create Engaging Whiteboard Animations-[https://inventhigh.net/udemy/mastering-doodly-2d-animation-white
board-animation/](https://inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/) 

79. Make YouTube T
humbnails & Get More Views (Photoshop +Online)-[https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-
free-online-site/](https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/) 

80. Macr
oeconomic Analysis: Investigating Inflation Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigat
ing-inflation-trend-with-r/](https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/) 


81. Learn Structural Engineering by Drawing Reading & ETABS-[https://inventhigh.net/udemy/learn-structural-architectur
al-vastu-plans-along-etabs/](https://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/) 

82.
 Learn Graphic Design using Canva & Start Freelancing-[https://inventhigh.net/udemy/canva-mastery-become-freelance-graph
ic-designer-in-1-hour/](https://inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/) 

83. L
earn Content Writing using AI & Start Freelancing-[https://inventhigh.net/udemy/ai-content-writing/](https://inventhigh.
net/udemy/ai-content-writing/) 

84. Learn Content Writing using AI & Make Money Online-[https://inventhigh.net/udemy/ai
-content-course/](https://inventhigh.net/udemy/ai-content-course/) 

85. Learn Basics of Adobe Photoshop CC for Beginner
s-[https://inventhigh.net/udemy/learn-basics-of-adobe-photoshop-cc-for-beginners/](https://inventhigh.net/udemy/learn-ba
sics-of-adobe-photoshop-cc-for-beginners/) 

86. Learn Basics Of Adobe After Effects CC for Beginners-[https://inventhig
h.net/udemy/learn-basics-of-adobe-after-effects-cc-for-beginners-learn/](https://inventhigh.net/udemy/learn-basics-of-ad
obe-after-effects-cc-for-beginners-learn/) 

87. How to be a programmer | Full guide to start (Arabic)-[https://inventhi
gh.net/udemy/how\_to\_become\_a\_programmer/](https://inventhigh.net/udemy/how_to_become_a_programmer/) 

88. Grow Your 
YouTube Channel Faster 2023 (Advanced) StepByStep-[https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-pr
oven-results-2022/](https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-proven-results-2022/) 

89. Gener
ate Income with Your YouTube, Despite Limited Views-[https://inventhigh.net/udemy/generate-income-with-your-youtube-desp
ite-limited-views/](https://inventhigh.net/udemy/generate-income-with-your-youtube-despite-limited-views/) 

90. Fundame
ntals of computer science | Short Term Course(Arabic)-[https://inventhigh.net/udemy/basics\_of\_programming/](https://in
venthigh.net/udemy/basics_of_programming/) 

91. Executive Diploma in Corporate Entrepreneurship-[https://inventhigh.net
/udemy/corporate-entrepreneurship/](https://inventhigh.net/udemy/corporate-entrepreneurship/) 

92. Executive Diploma in
 Business Strategy-[https://inventhigh.net/udemy/diploma-business-strategy/](https://inventhigh.net/udemy/diploma-busine
ss-strategy/) 

93. Executive Assistant Professional Certification (EAPC)-[https://inventhigh.net/udemy/executive-assist
ant/](https://inventhigh.net/udemy/executive-assistant/) 

94. Disruptive Thinking For World-Changing Innovative Ideas-[
https://inventhigh.net/udemy/disruptive-thinking/](https://inventhigh.net/udemy/disruptive-thinking/) 

95. Diploma In C
oncrete Technology l Be a Concrete Technologist-[https://inventhigh.net/udemy/concrete-technologycivil-engineers-lifelin
e-in-construction/](https://inventhigh.net/udemy/concrete-technologycivil-engineers-lifeline-in-construction/) 

96. Cre
ate and Sell Digital Art using AI \[Passive Income\]-[https://inventhigh.net/udemy/ai-art-course/](https://inventhigh.ne
t/udemy/ai-art-course/) 

97. Color Grading and Video Editing with Davinci Resolve 18-[https://inventhigh.net/udemy/colo
r-grading-and-video-editing-with-davinci-resolve/](https://inventhigh.net/udemy/color-grading-and-video-editing-with-dav
inci-resolve/) 

98. Color Correction & Grading with Adobe Premiere Pro-[https://inventhigh.net/udemy/color-correction-g
rading-with-adobe-premiere-pro/](https://inventhigh.net/udemy/color-correction-grading-with-adobe-premiere-pro/) 

99. C
old Email & Lead Generation using AI \[Masterclass\]-[https://inventhigh.net/udemy/ai-cold-email/](https://inventhigh.ne
t/udemy/ai-cold-email/) 

100. Chat GPT & Midjourney: Personal Digital Marketing Assistants-[https://inventhigh.net/udem
y/chatgpt-digital-marketing/](https://inventhigh.net/udemy/chatgpt-digital-marketing/) 

101. C programming language | T
he Complete C Course (Arabic)-[https://inventhigh.net/udemy/c-programming-language-from-a-to-z/](https://inventhigh.net/
udemy/c-programming-language-from-a-to-z/) 

102. Business Networking for Success and Company Growth: Part One-[https://
inventhigh.net/udemy/business-networking-1/](https://inventhigh.net/udemy/business-networking-1/) 

103. Build a Profita
ble Online Courses Business \[Complete Guide\]-[https://inventhigh.net/udemy/complete-guide-become-a-six-figure-online-c
ourse-instructor/](https://inventhigh.net/udemy/complete-guide-become-a-six-figure-online-course-instructor/) 

104. Bec
ome a Successful Affiliate Marketer \[Success Blueprint\]-[https://inventhigh.net/udemy/become-a-six-figure-affiliate-ma
rketer-success-blueprint/](https://inventhigh.net/udemy/become-a-six-figure-affiliate-marketer-success-blueprint/) 

105
. Arabic| Learn Arabic with Mina | Comprehensive Arabic course-[https://inventhigh.net/udemy/learn-arabic-language-d/](h
ttps://inventhigh.net/udemy/learn-arabic-language-d/) 

106. Affiliate Marketing & MLM Network Marketing For Fashion-[ht
tps://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/](https://inventhigh.net/udemy/affi
liate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/) 

107. AI x ChatGPT for Productivity 101 \[Masterclass\]-[https:
//inventhigh.net/udemy/ai-productivity/](https://inventhigh.net/udemy/ai-productivity/) 

108. AI for Business Strategy 
& Planning \[Masterclass\]-[https://inventhigh.net/udemy/ai-business-course/](https://inventhigh.net/udemy/ai-business-c
ourse/) 

109. Private Equity Course for Beginners (PEQ101)-[https://inventhigh.net/udemy/private-equity-course-for-begi
nners-peq101/](https://inventhigh.net/udemy/private-equity-course-for-beginners-peq101/) 

110. Personal Brand Mastery :
 Online Personal Branding Essentials-[https://inventhigh.net/udemy/personal-branding-mastery-online-personal-branding-es
sentials/](https://inventhigh.net/udemy/personal-branding-mastery-online-personal-branding-essentials/) 

111. Nuts & Bo
lts of Capital Markets-[https://inventhigh.net/udemy/nuts-bolts-of-capital-markets/](https://inventhigh.net/udemy/nuts-b
olts-of-capital-markets/) 

112. Mechanical Engineering Mastery Series : HVAC Engineering 101-[https://inventhigh.net/ud
emy/mechanical-engineering-course/](https://inventhigh.net/udemy/mechanical-engineering-course/) 

113. Mastering Presen
tations and Public Speaking (Ultimate guide)-[https://inventhigh.net/udemy/presentations-and-public-speaking/](https://i
nventhigh.net/udemy/presentations-and-public-speaking/) 

114. Investment Banking for Beginners (IB101)-[https://inventh
igh.net/udemy/investment-banking-for-beginners-ib101/](https://inventhigh.net/udemy/investment-banking-for-beginners-ib1
01/) 

115. Introduction to Microsoft Word for Beginners to Intermediate-[https://inventhigh.net/udemy/introduction-to-m
icrosoft-word-for-beginners/](https://inventhigh.net/udemy/introduction-to-microsoft-word-for-beginners/) 

116. Interne
t & Cloud Computing Foundations-[https://inventhigh.net/udemy/internet-cloud-computing-foundations/](https://inventhigh.
net/udemy/internet-cloud-computing-foundations/) 

117. How the Internet Works & the Web Development Process-[https://in
venthigh.net/udemy/how-the-internet-works-the-web-development-process/](https://inventhigh.net/udemy/how-the-internet-wo
rks-the-web-development-process/) 

118. HVAC Design Basics : Understanding HVAC systems With Details-[https://inventhig
h.net/udemy/hvac-systems/](https://inventhigh.net/udemy/hvac-systems/) 

119. Financial Modeling in Excel - DCF Model of
 Big Books Corp-[https://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/](https://inventhig
h.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/) 

120. Financial Modeling | Social Media Sector : T
witter-[https://inventhigh.net/udemy/financial-modeling-social-media-sector-twitter/](https://inventhigh.net/udemy/finan
cial-modeling-social-media-sector-twitter/) 

121. Financial Modeling | Food & Beverages Sector : Starbucks-[https://inv
enthigh.net/udemy/financial-modeling-food-beverages-sector-starbucks/](https://inventhigh.net/udemy/financial-modeling-f
ood-beverages-sector-starbucks/) 

122. Financial Analysis & Modeling | Islamic Banking-[https://inventhigh.net/udemy/fi
nancial-modeling-islamic-banking-modeling/](https://inventhigh.net/udemy/financial-modeling-islamic-banking-modeling/) 


123. Financial Analysis & Modeling | Automobile Sector-[https://inventhigh.net/udemy/financial-modeling-automobile-sect
or-maruti-suzuki/](https://inventhigh.net/udemy/financial-modeling-automobile-sector-maruti-suzuki/) 

124. Computer Vis
ion Fundamentals-[https://inventhigh.net/udemy/computer-vision-fundamentals/](https://inventhigh.net/udemy/computer-visi
on-fundamentals/) 

125. Complete Guide to Explosive Power Training-[https://inventhigh.net/udemy/athletic-power-trainin
g-certificate/](https://inventhigh.net/udemy/athletic-power-training-certificate/) 

126. Chief Customer Experience Offi
cer Executive Certification-[https://inventhigh.net/udemy/chief\_customer\_experience\_officer/](https://inventhigh.net/
udemy/chief_customer_experience_officer/) 

127. Candlestick Chart Pattern & Renko Trading (2 Course Bundle)-[https://in
venthigh.net/udemy/candlestick-renko/](https://inventhigh.net/udemy/candlestick-renko/) 

128. CEO Chief Executive Offic
er Executive Certification-[https://inventhigh.net/udemy/certified-chief-executive-officer/](https://inventhigh.net/udem
y/certified-chief-executive-officer/) 

129. Artificial General Intelligence (AGI)-[https://inventhigh.net/udemy/artific
ial-general-intelligence/](https://inventhigh.net/udemy/artificial-general-intelligence/) 

130. Apache Hive for Data En
gineers (Hands On) with 2 Projects-[https://inventhigh.net/udemy/apache-hive-for-data-engineers-hands-on/](https://inven
thigh.net/udemy/apache-hive-for-data-engineers-hands-on/) 

131. 4 Comprehensive Practice Tests for any Python Certifica
tion-[https://inventhigh.net/udemy/4-comprehensive-practice-tests-for-any-python-certification/](https://inventhigh.net/
udemy/4-comprehensive-practice-tests-for-any-python-certification/) 

132. \[Weight Loss\] : Get Your Dream Body with Di
et & Cardio-[https://inventhigh.net/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/](https://inventhigh.net
/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/) 

133. \[Tips & Technics\] : How to Lead Effective Meetin
gs 2022 -New-[https://inventhigh.net/udemy/tips-technics-how-to-lead-effective-meetings-2022/](https://inventhigh.net/ud
emy/tips-technics-how-to-lead-effective-meetings-2022/) 

134. \[Tips & Technics\] : How to Become a Great Leader Skills
 2022-[https://inventhigh.net/udemy/tips-technics-how-to-become-a-great-leader-skills/](https://inventhigh.net/udemy/tip
s-technics-how-to-become-a-great-leader-skills/) 

135. \[Practice Exams\] AWS Certified Solutions Architect Associate-[
https://inventhigh.net/udemy/practice-exams-aws-certified-solutions-architect-associate-u/](https://inventhigh.net/udemy
/practice-exams-aws-certified-solutions-architect-associate-u/) 
```
---

     
 
all -  [ Suggestion: GPT4all-style LocalDocs collections ](https://www.reddit.com/r/faraday_dot_dev/comments/17b8ty0/suggestion_gpt4allstyle_localdocs_collections/) , 2023-10-22-0910
```
Dear Faraday devs,Firstly, thank you for an excellent product. I have no trouble spinning up a CLI and hooking to llama.
cpp directly, but your app makes it so much more pleasant.

If I might suggest something, please add support for local d
ocument collections (reference: [https://docs.gpt4all.io/gpt4all\_chat.html#localdocs-beta-plugin-chat-with-your-data](h
ttps://docs.gpt4all.io/gpt4all_chat.html#localdocs-beta-plugin-chat-with-your-data)). This would make characters vastly 
more useful for certain use cases - for example, a DIY repairman who has a corpus it can pull on, or fictional character
s who have world knowledge, like an engineer who has manuals for major spacecraft.

I do this already with my own Gradio
 + Langchain document loader setup, but honest Faraday is so much nicer to interact with. If you have the time to includ
e this, I'd really appreciate it. Even cooler (Although not strictly required) if it can be some kind of drag and drop d
ataset builder.

Cheers, and have a good day!

https://preview.redd.it/obx4f35lp2vb1.png?width=1496&format=png&auto=webp
&s=bbe05cb9dfd6aee8d62550f7f237bd2dbe2326d5
```
---

     
 
all -  [ Streaming not working when routing between Runnables ](https://www.reddit.com/r/LangChain/comments/17b5gaw/streaming_not_working_when_routing_between/) , 2023-10-22-0910
```
I'm trying to stream the response of a simple route I've created among 2 Runnables without success. When I stream each R
unnable independelty, it streams perfectly. When I create a route to choose which one of them should be the next step, i
t doesn't stream the result. Can someone provide some guidance?

Here's the example:

    # ----------------- Runnable 1
 -----------------
    
    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template='{page_content}')
    def _c
ombine_documents(docs, document_prompt = DEFAULT_DOCUMENT_PROMPT, document_separator='\n\n'):
      doc_strings = [forma
t_document(doc, document_prompt) for doc in docs]
      return document_separator.join(doc_strings)
      
    def _form
at_chat_history(chat_history: List[Tuple]) -> str:
      buffer = ''
        for dialogue_turn in chat_history:
        
  human = 'Human: ' + dialogue_turn[0]
          ai = 'Assistant: ' + dialogue_turn[1]
          buffer += '\n' + '\n'.j
oin([human, ai])
      return buffer
      
    _inputs = RunnableMap({
      'standalone_question': {
        'question
': lambda x: x['question'],
        'chat_history': lambda x: _format_chat_history(x['chat_history'])
      } | PromptFa
ctory.CONDENSE_QUESTION_PROMPT | ChatOpenAI(temperature=0, streaming=True) | StrOutputParser(),
    })
    _context = {

      'context': itemgetter('standalone_question') | vector_retriever | _combine_documents,
      'question': lambda x: 
x['standalone_question']
    }
    Runnable1 = _inputs | _context | PromptFactory.PROMPT | ChatOpenAI(temperature=0, str
eaming=True)
    
    # ----------------- Stream the response: -----------------
    
    for s in Runnable1.stream({'qu
estion': 'Hello!', 'chat_history': []}):
      print(s, end='', flush=True)

**The above stream works**

    # ---------
-------- Runnable 2 -----------------
    
    Runnable2 = RunnableMap({
      'response': {
        'question': lambda 
x: x['question'],
        'chat_history': lambda x: _format_chat_history(x['chat_history']),
        'context': lambda x
: QueriesContext.get_result()
      } | PromptTemplate.from_template(PromptFactory.followup_context_template) | ChatOpen
AI(temperature=0, streaming=True) | StrOutputParser(),
    })
    
    # ----------------- Stream the response: --------
---------
    
    for s in Runnable2.stream({'question': 'Hello!', 'chat_history': [], 'context': ['initialvalue']}):
 
     print(s, end='', flush=True)

**The above stream also works**

    def get_result(text):
      return ['newvalue']

    router_chain = PromptTemplate.from_template(PromptFactory.router_template_test) | ChatOpenAI(temperature=0, streamin
g=True) | StrOutputParser()
    
    def route(info):
      if 'runnable1' in info['topic'].lower():
        return Runn
able1
      elif 'runnable2' in info['topic'].lower():
        return Runnable2
      else:
        raise Exception('Inv
alid topic')
    
    full_runnable_router_chain = {
      'topic': router_chain,
      'question': lambda x: x['questio
n'],
      'chat_history': lambda x: x['chat_history'],
      'context': lambda x: x['context']
    } | RunnableLambda(r
oute)
    
    # ----------------- Stream the response: -----------------
    
    for s in full_runnable_router_chain.s
tream({'question': 'Hello!', 'chat_history': [], 'context': ['initialvalue']}):
      print(s.content, end='', flush=Tru
e)

**The above stream doesn't stream**
```
---

     
 
all -  [ Ask questions over documents process ](https://www.reddit.com/r/LangChain/comments/17b2i8k/ask_questions_over_documents_process/) , 2023-10-22-0910
```
If I follow this ([https://python.langchain.com/docs/use\_cases/question\_answering](https://python.langchain.com/docs/u
se_cases/question_answering/)) to ask questions over documents, are my documents sent to langchain or openai at any poin
t?  Or do they stay local on my machine?
```
---

     
 
all -  [ Hiring announcements / job ads? ](https://www.reddit.com/r/LangChain/comments/17b1if6/hiring_announcements_job_ads/) , 2023-10-22-0910
```
Are hiring announcements / job ads for LangChain and related roles allowed on this subreddit? 

Mods, perhaps you could 
create a pinned thread for companies seeking talent?
```
---

     
 
all -  [ Llama 2 7B 32K Instruct summarizes and outlines text... inconsistently ](https://www.reddit.com/r/LocalLLaMA/comments/17b0n8t/llama_2_7b_32k_instruct_summarizes_and_outlines/) , 2023-10-22-0910
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

     
 
all -  [ Resume Roast/Review. ](https://i.redd.it/vm124swr50vb1.jpg) , 2023-10-22-0910
```
Hey everyone, please go through this thoroughly and review or roast it. 
Even though I am a full time developer, I am us
ing this resume to apply for better jobs in Fullstack, Frontend or Backend.
But I am getting no responses. Please tell m
e whatever may be wrong with this resume or my skills or experience.
Thank you ☺️
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-22-0910
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

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-22-0910
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

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-22-0910
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-22-0910
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-22-0910
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-22-0910
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-22-0910
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

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-22-0910
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

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-22-0910
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

     
