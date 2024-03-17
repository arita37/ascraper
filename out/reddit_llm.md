 
all -  [ I made code2prompt - A CLI tool to convert your codebase into a single LLM prompt with source tree,  ](https://www.reddit.com/r/rust/comments/1bghroh/i_made_code2prompt_a_cli_tool_to_convert_your/) , 2024-03-17-0911
```
**What is it?**  
You can run [code2prompt](https://github.com/mufeedvh/code2prompt) on your codebase directory and it w
ould generate a well-formatted Markdown prompt detailing the source tree structure, and all the code. You can then uploa
d this document to either GPT or Claude models with higher context windows and ask it to:  


* Rewrite the code to anot
her language.
* Find bugs/security vulnerabilities.
* Document the code.
* Implement new features.

You can customize th
e prompt template to achieve any of the desired use cases. It essentially traverses a codebase and creates a prompt with
 all source files combined. In short, it automates copy-pasting multiple source files into your prompt and formatting th
em along with letting you know how many tokens your code consumes.

I've also uploaded some templates for common use cas
es: See the [List of Templates](https://github.com/mufeedvh/code2prompt?tab=readme-ov-file#templates).  


[Screenshot o
f the code2prompt CLI tool](https://preview.redd.it/fbo8o2xxtroc1.png?width=1414&format=png&auto=webp&s=d7e2dcdc829f0a80
94c9bb1db1e1343df64a1c2a)

>I initially wrote this for personal use to utilize Claude 3.0's 200K context window and it h
as proven to be pretty useful so I decided to open-source it!

  
**GitHub:** [https://github.com/mufeedvh/code2prompt](
https://github.com/mufeedvh/code2prompt)
```
---

     
 
all -  [ I made code2prompt - A CLI tool to convert your codebase into a single LLM prompt with source tree,  ](https://www.reddit.com/r/ChatGPTCoding/comments/1bghp8p/i_made_code2prompt_a_cli_tool_to_convert_your/) , 2024-03-17-0911
```
**What is it?**  
You can run [code2prompt](https://github.com/mufeedvh/code2prompt) on your codebase directory and it w
ould generate a well-formatted Markdown prompt detailing the source tree structure, and all the code. You can then uploa
d this document to either GPT or Claude models with higher context windows and ask it to:  


* Rewrite the code to anot
her language.
* Find bugs/security vulnerabilities.
* Document the code.
* Implement new features.

You can customize th
e prompt template to achieve any of the desired use cases. It essentially traverses a codebase and creates a prompt with
 all source files combined. In short, it automates copy-pasting multiple source files into your prompt and formatting th
em along with letting you know how many tokens your code consumes.

I've also uploaded some templates for common use cas
es: See the [List of Templates](https://github.com/mufeedvh/code2prompt?tab=readme-ov-file#templates).  


[Screenshot o
f the code2prompt CLI tool](https://preview.redd.it/5y9qxur1sroc1.png?width=1414&format=png&auto=webp&s=bf4597b8a7925cb3
543f95967370ea9c5009e41d)

>I initially wrote this for personal use to utilize Claude 3.0's 200K context window and it h
as proven to be pretty useful so I decided to open-source it!

  
**GitHub:** [https://github.com/mufeedvh/code2prompt](
https://github.com/mufeedvh/code2prompt)
```
---

     
 
all -  [ Struggling with hallucinations in ConversationSummaryMemory ](https://www.reddit.com/r/LangChain/comments/1bgdh3n/struggling_with_hallucinations_in/) , 2024-03-17-0911
```
New to langchain, and trying to get used to the tooling. However, I am struggling with hallucinations in conversationsum
marymemory. I am using llama2 via Ollama. I am using the smaller 3.8GB (llama2:latest   78e26419b446) model. My leading 
hypothesis is that the model itself is not very good at summarizing, and is just corrupting the memory with its hallucin
ations.

 The post might be long, but I thought it is best to illustrate my problem using this small demo I have prepare
d.

&#x200B;

Here's how I instantiate,

    template = '''
    Act as an AI assistant and follow user instructions and 
answer questions in a precise manner.
    User conversation history for context whenever applicable.
    Current convers
ation: {history}
    Human: {input}
    '''
    llm = Ollama(model='llama2', temperature=0.9) 
    memory = Conversation
SummaryMemory(llm=Ollama(model='llama2', temperature=0.0)) 
    # set temperature=0. for memory for determinism. 
    co
nvo = ConversationChain(
                 llm = llm,
                 verbose = True,
                 memory=memory,
  
               prompt = PromptTemplate(input_variables=['history', 'input'], template=template)
                )
    co
nvo.predict(input='Introduce yourself.')

Output : so far reasonable.

    > Entering new ConversationChain chain...
   
 Prompt after formatting:
    
    Act as an AI assistant and follow user instructions and answer questions in a precise
 manner.
    User conversation history for context whenever applicable.
    Current conversation: 
    Human: Introduce 
yourself.
    
    
    > Finished chain.
    
    'Hello! I'm just an AI assistant, here to help you with any questions
 or tasks you may have. My name is Assistant, and I'm here to assist you in a precise and helpful manner. How can I assi
st you today?'

Then I provide some new inputs.

    convo.predict(input='Memorize the following words, bat, cat dog')
 
   convo.predict(input='Try to remember the following words: coffee and tea')

Now it has completely gone off the rails.
 Here's the outputs.

    > Entering new ConversationChain chain...
    Prompt after formatting:
    
    Act as an AI a
ssistant and follow user instructions and answer questions in a precise manner.
    User conversation history for contex
t whenever applicable.
    Current conversation: Current summary: The human asks what the AI thinks of artificial intell
igence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential
.
    
    New lines of conversation: Human: What do you mean by 'reach their full potential'? AI: Well, with the help o
f artificial intelligence, humans can accomplish more than they ever thought possible. It can help them solve complex pr
oblems, make better decisions, and achieve their goals more efficiently.
    
    New summary: The human asks what the A
I thinks of artificial intelligence, and the AI replies that it believes artificial intelligence is a force for good bec
ause it will help humans reach their full potential by enabling them to accomplish more than they ever thought possible,
 solve complex problems, make better decisions, and achieve their goals more efficiently.
    Human: Memorize the follow
ing words, bat, cat dog
    
    
    > Finished chain.
    
    
    > Entering new ConversationChain chain...
    Prom
pt after formatting:
    
    Act as an AI assistant and follow user instructions and answer questions in a precise mann
er.
    User conversation history for context whenever applicable.
    Current conversation: Current summary: The human 
asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it
 will help humans reach their full potential.
    
    New lines of conversation: Human: What do you mean by 'reach thei
r full potential'? AI: Well, with the help of artificial intelligence, humans can accomplish more than they ever thought
 possible. It can help them solve complex problems, make better decisions, and achieve their goals more efficiently.
   
 
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI replies that it believes art
ificial intelligence is a force for good because it will help humans reach their full potential by enabling them to acco
mplish more than they ever thought possible, solve complex problems, make better decisions, and achieve their goals more
 efficiently.
    
    New lines of conversation: AI: I'm glad you asked! *smirks* In my opinion, the future of artifici
al intelligence is bright, and it will continue to revolutionize various industries. With the advancements in machine le
arning and natural language processing, AI will become even more integrated into our daily lives.
    
    New summary: 
The human asks what the AI thinks of artificial intelligence, and the AI replies that it believes artificial intelligenc
e is a force for good because it will help humans reach their full potential by enabling them to accomplish more than th
ey ever thought possible, solve complex problems, make better decisions, and achieve their goals more efficiently. The A
I then goes on to express its excitement about the future of artificial intelligence and how it will continue to revolut
ionize various industries with advancements in machine learning and natural language processing.
    Human: Try to remem
ber the following words: coffee and tea
    
    
    > Finished chain.
    
    'Of course, I'd be happy to help! *smir
ks* I have a great memory when it comes to storing information, so I will definitely keep those words in mind for future
 conversations. By the way, do you want to know a fun fact about artificial intelligence? Did you know that AI can now c
reate art that is almost indistinguishable from that created by humans? It's fascinating to see how far the technology h
as come!'

The new summary lines contain things that have not been brought up in conversation at all.

Testing again,

 
   convo.predict(input='Out of the 5 words I shared with you. Repeat the third and fourth words.')

Yields total nonsens
e.

    > Entering new ConversationChain chain...
    Prompt after formatting:
    
    Act as an AI assistant and follo
w user instructions and answer questions in a precise manner.
    User conversation history for context whenever applica
ble.
    Current conversation: Current summary: The human asks what the AI thinks of artificial intelligence. The AI thi
nks artificial intelligence is a force for good because it will help humans reach their full potential.
    
    New lin
es of conversation: Human: Why do you think artificial intelligence is a force for good? AI: Because artificial intellig
ence will help humans solve complex problems, make better decisions, and achieve their goals more efficiently. Human: Th
at's interesting. Can you give me an example? AI: Sure! For instance, AI can help doctors diagnose diseases more accurat
ely and quickly than ever before. It can also assist businesses in making better investment decisions and optimizing the
ir operations.
    
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI replies th
at it believes artificial intelligence is a force for good because it will help humans solve complex problems, make bett
er decisions, and achieve their goals more efficiently. The AI then provides an example of how AI can help doctors diagn
ose diseases more accurately and quickly than ever before, as well as assist businesses in making better investment deci
sions and optimizing their operations.
    
    New lines of conversation: Human: That's impressive. Can AI also help wi
th creative tasks? AI: Absolutely! Artificial intelligence can assist with creative tasks such as writing, music composi
tion, and even art creation. In fact, there are already many AI-generated art pieces that are highly regarded and sold f
or thousands of dollars.
    
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI 
replies that it believes artificial intelligence is a force for good because it will help humans solve complex problems,
 make better decisions, and achieve their goals more efficiently. The AI then provides an example of how AI can help doc
tors diagnose diseases more accurately and quickly than ever before, as well as assist businesses in making better inves
tment decisions and optimizing their operations. The AI also mentions that artificial intelligence can assist with creat
ive tasks such as writing, music composition, and even art creation, with many AI-generated art pieces already highly re
garded and sold for thousands of dollars.
    Human: Out of the 5 words I shared with you. Repeat the third and fourth w
ords.
    
    
    > Finished chain.
    
    'Of course! The third word is 'ai' and the fourth word is 'intelligence'.
'

&#x200B;
```
---

     
 
all -  [ Future of NLP - Chris Manning Stanford CoreNLP ](https://youtu.be/xk01kx_klOE?si=TiBA2XyhPuuDpjMn) , 2024-03-17-0911
```

```
---

     
 
all -  [ Chainlit deployment for prod in Kubernetes cluster ](https://www.reddit.com/r/LangChain/comments/1bga3qk/chainlit_deployment_for_prod_in_kubernetes_cluster/) , 2024-03-17-0911
```
Hi all, 

&#x200B;

I am trying to deploy a chainlit app in our k8 cluster.   


When deployed my http:baseurl/app shows
 up as a blank white page.   


on the container logs it shows your app is available at localhost:8080 .   


I feel lik
e I will have to write my own framework instead of chainlit to deploy in prod. 

&#x200B;

Any advice is welcome. 

&#x2
00B;

Thanks 

&#x200B;

  


  

```
---

     
 
all -  [ A mystery gaming site where you help a helpless gpt solve cases. ](https://www.reddit.com/r/OpenAI/comments/1bg8dh9/a_mystery_gaming_site_where_you_help_a_helpless/) , 2024-03-17-0911
```
My friend and I made a mystery game with the openai api: [https://inkvestigations.com/](https://inkvestigations.com/)

I
t is open as in open source: [https://github.com/bromberry-games/Inkvestigations](https://github.com/bromberry-games/Ink
vestigations) 

You can try it out for free and even play it for free if you use your own openai key. You can check the 
code that we won't take your key. Also if you try it out and need more messages just let me know.  
We have some premade
 mysteries and also a mystery creator where you can make your own.

This was a fun project to do and we learned a lot ab
out working with gpt and building something in general. The biggest problem with gpt for us was getting it to follow the
 instructions correctly even after a ton of messages, which we kinda managed to solve with some chain of thought prompti
ng and few shot prompting. Also we are using the tipping prompting technique, which was a huge highlight when it worked 
for us. I guess gpt really likes money. 

However I have to say that the quality is not really there (yet). I think the 
responses often fall very flat and are kind of mediocore with occansional highlights in between. There is still a long w
ay to go from gpt to a competent game master. Don't let that deter you from trying it out tho, it's still fun for a coup
le of tries. We still have a couple of ideas left to make it better by using some more langchain features like the examp
le selector, but will then leave the project alone.

Did anyone here have success making gpt feel more 'alive'. You can 
prompt him to be a persona. For example we wanted it to play a dark and grim police officer, but always when we tried so
mething like it, it just overplayed it's role so much that it got annyoing after \~5 messages.
```
---

     
 
all -  [ New to LangChain, how to make my vector store query faster? ](https://www.reddit.com/r/LangChain/comments/1bg81iw/new_to_langchain_how_to_make_my_vector_store/) , 2024-03-17-0911
```
I'm an experienced software engineer who is new to AI-based development. I am working on a practice RAG project with Lan
gChain and Milvus. 

Right now I am just re-creating the example found here: [https://github.com/langchain4j/langchain4j
-examples/blob/main/milvus-example/src/main/java/MilvusEmbeddingStoreExample.java](https://github.com/langchain4j/langch
ain4j-examples/blob/main/milvus-example/src/main/java/MilvusEmbeddingStoreExample.java). No more, no less. I am doing th
is on my M1 Pro MacBook.

When I try performing the query, it runs incredibly slow. I can't tell you exactly how long, b
ecause after waiting several minutes I always abort. There are no exceptions, it just sits there, trying to process.

I 
have allocated 8 CPU cores and 16GB of RAM to the docker engine on my laptop. Based on the stats I am seeing, milvus its
elf is heavily CPU bound. The tiny quantity of data in the vector store at the time means the RAM requirements are minim
al. Yet at the end of the day, it is still incredibly slow.

There are a few possibilities I am considering at this poin
t. The first is that Milvus benefits from GPU optimization. That's my least-preferred scenario, as my MacBook and my hom
e server are lacking in GPU hardware.

The second scenario is indexing. This is an area that I know from working with tr
aditional databases, but with vector databases it's all new to me. Specifically, I'm using the default FLAT index which 
I know doesn't perform well. I'm beginning to read about alternative indexes to see what options I have there.

Anyway, 
I'm hoping that folks here can offer advice on my existing ideas and any other general improvements I can make. Thanks i
n advance.
```
---

     
 
all -  [ LangChain for... pretty obscure task, I suppose. ](https://www.reddit.com/r/LangChain/comments/1bg7ojh/langchain_for_pretty_obscure_task_i_suppose/) , 2024-03-17-0911
```
Hello everyone,

I am new to this subreddit and to reddit more in general. I am using LangChain and LLaMa2 a lot for my 
research lately, and I have some general questions about usage. 

1) To begin with, is there any way to verify that I am
 working with the right model? I am loading a quantized version of LLaMa2 though HF pipelines, and when I inspect the mo
del it calls it GPT2. Not sure if I should be worried. 

2) Regarding memory: how does the ConversationBufferMemory for 
LLM chains work? Is it loaded on GPU? Does it count as context, meaning that a memory with too many messages will cause 
the model to start spouting gibberish? How persistent is it (i.e.: after how many messages will the earliest message be 
forgotten/deleted)?

3) Regarding RAG using Chroma (which I have seen being used in the LangChain docs): is there a tuto
rial for how to conduct it? I am especially interested in verifying if one can iteratively add to the database the LLM i
s drawing from without having to 'retrain' the model. 

4) Related to questions 2 and 3. Suppose that I have an script r
unning that iteratively produces text in batches. I would then like to feed batches one after the other to an LLM in ord
er for the algorithm to evaluate the content of these batches. I have considered two options: the first is to feed each 
part of the batch directly into the LLM's memory, but I am not sure if this would overload its GPU or context window (mo
re worried about the latter, presently). The other option is, you guessed it, performing RAG on the batches. But I am no
t sure if RAG can help me with something beyond simple retrieval and more in depth. I don't want a summary of what is in
 a given batch of text, I want some manner of inference on the batch conditional on my request, for instance: if the bat
ch of text says that person X took a series of action that resulted in person Y dying, I want to ask the LLM if it can f
ind a causal link between X's actions and Y's death.

5) Finally, is there a way to use LLMs for flow control? Say that 
I have a very basic counting loop, something that simply enumerates all natural numbers until it is stopped. Is there a 
way, or maybe a tool, to tell an LLM to stop the loop when a number exceeds a certain threshold? I realize that this is 
killing a rat with a bazooka, but it's the smallest working example I could produce. A more fitting and complex example 
would be: let us return to the text in question 4. I want the LLM to stop the script that is producing text if it can id
entify a causal link between Y's death and X's action. Is there a way to do this? Simply asking LLaMa2-7b to type 'stop'
 if it thinks the loop should stop does not work, despite using very wordy prompts and CoT.

I am sorry for the very bas
ic questions, I do not really know where to turn for help. I likewise apologize for being vague but I cannot disclose to
o much about my research. Any link, resource or manner of assistance will be very much appreciated. 
```
---

     
 
all -  [ LLM workflows  ](https://www.reddit.com/r/LangChain/comments/1bg7kfm/llm_workflows/) , 2024-03-17-0911
```
My team got requirement from a client and client wants do this using any LLM. Its about a workflow based on serious ques
tions.
If user say yes to a particular question some, One set of questions will be triggered. If user say no the same qu
estion another set of questions should be followed.  

Is there any framework open/closed to achieve this. Its more of a
 decision trees kind of problem. So my client thinks if we use LLm then questions will more creative and conversational.
 
```
---

     
 
all -  [ [For Hire][Remote] Python Developer available for Application, Script, DevOps and Backend Developmen ](https://www.reddit.com/r/remotepython/comments/1bg3s9x/for_hireremote_python_developer_available_for/) , 2024-03-17-0911
```
I offer Software development, DevOps, SRE services. I use Python and all major frameworks such as Flask, Django and Fast
API.   


Here are the complete list of languages / Framework, I am familiar with:

**Backend Frameworks**

* FastAPI Fr
amework - Python
* Django Framework - Python
* Flask Framework - Python
* Laravel Framework - PHP
* Symfony Framework - 
PHP
* CodeIgnitor Framework - PHP
* Express Framework- NodeJS
* NextJS Framework - NodeJS
* Meteor Framework - NodeJS

*
*Frontend Frameworks**

* React
* Material UI
* Ember
* BackboneJS
* AngularJS
* Fluent UI
* Blade UI
* Element UI 

**W
eb 3.0 Technologies and Frameworks**

* Ethereum Virtual Machine (EVM)
* Truffle Framework
* Solana for NFT

Artificial 
Intelligence (AI)/ Machine Learning ML / LLMs

* LangChain Framework
* LiteLLM Framework
* Google Vertex AI
* ChatGPT
* 
Azure AI Studio  


Besides Software Development, I am a skill DevOps and Cloud Engineer:  


**Cloud Providers**

* Ama
zon Web Services
* Microsoft Azure
* Google Cloud
* DigitalOcean
* OVHCloud
* Alibaba Cloud
* Rackspace

&#x200B;

**Dom
ain / Hosting Providers**

* Go Daddy
* Heroku
* Linode
* Hostinger
* Interserver
* MyHost
* Bluehost

**CI/CD Tools**


* Jenkins
* Gitlab
* TeamCity
* CircleCI
* Github Actions
* BitBucket

**Other Tools**

* DataDog
* Splunk
* New Relic
*
 Puppet
* Kubernetes
* Prometeus
* Nagios
* Zabbix
* Cacti

Availability: 40 - 60 hours per week

Rate: Starting at $15 
per hour

Payment via: Payoneer, Bank Deposit, WISE

Please DM me for details about your project or job

&#x200B;
```
---

     
 
all -  [ Help me find the state of the art for my usecase ](https://www.reddit.com/r/LangChain/comments/1bg2qgo/help_me_find_the_state_of_the_art_for_my_usecase/) , 2024-03-17-0911
```
I am working on a project to convert non-fiction book PDFs (300 pages max) to a high quality crisp summary. 

Now, I've 
a standard structure for this summary:
1. It should be condensed to 10 'slides'
2. It should be high quality without omi
tting key aspects of the book.
3. I want each slide to have a title and a description below it. Title should be engaging
 for the reader and description should be 200 words Max.
4. should include a mindmap of all core ideas (optional)

My qu
estion to the experts on language model folks here is:
a. Is this a fair expectation? If not what is the closest I can g
et?
a. If yes. What is the best and cheapest (free) way to go about executing it as of today? fast, free, high quality o
ption.
b. How can I get started to achive the above task.

Thanks a lot.
```
---

     
 
all -  [ Flowise - Pupeteer version dependencies - Help needed ](https://www.reddit.com/r/LangChain/comments/1bfza1v/flowise_pupeteer_version_dependencies_help_needed/) , 2024-03-17-0911
```
 **Not sure what to do next. Help Appreciated**   
Tried to install flowise, getting these errors. 

The npm list -g pup
peteer  
 command output indicates that puppeteer  
 is being used by flowise  
 and its sub-dependencies at versions 19
.11.1  
 and 20.9.0  
, both of which are deprecated as they are below the supported version 21.5.0  
. Here's what you 
can consider doing next:

1. **Direct Dependency Update**: If a package directly depends on an outdated version, you cou
ld try updating that dependency. However, since puppeteer  
 is a nested dependency in your case (used by flowise-compon
ents  
 and langchain  
), direct intervention isn't straightforward.
2. **Contact the Maintainers**: Since the outdated
 puppeteer  
 versions are dependencies of flowise-components  
 and langchain  
, the ideal approach would be to contac
t the maintainers of these packages and request them to update their puppeteer  
 dependencies. This way, when you updat
e flowise  
, it would use the updated versions of these dependencies.
3. **Manual Override (Advanced)**: If you're comf
ortable with manual intervention and understand the potential risks, you could consider using npm's shrinkwrap  
 featur
e or resolutions  
 in package.json  
 (if using Yarn) to force the use of a newer puppeteer  
 version. This is more co
mplex and can lead to compatibility issues, so it's typically recommended only if you're experienced with Node.js and np
m's inner workings.
4. **Monitor and Update**: If the current functionality isn't affected and you're not using puppetee
r  
 in security-critical environments, you may choose to monitor the situation while waiting for the maintainers to upd
ate their packages. Ensure to regularly check for new versions of flowise  
 and its dependencies that might resolve thi
s issue.
5. **Assess Usage**: Consider how you're using flowise  
. If puppeteer  
's role is not critical for your use 
case, the deprecated warnings might be less concerning. However, if you're using puppeteer  
 features extensively, espe
cially in a production or security-sensitive environment, addressing this becomes more urgent.

In summary, the best cou
rse of action is typically to reach out to the package maintainers or monitor for updates that resolve the dependency co
ncerns. Direct intervention is possible but should be approached with caution.
```
---

     
 
all -  [ Build personalized agent with long term memory ](https://www.reddit.com/r/ClaudeAI/comments/1bfz79f/build_personalized_agent_with_long_term_memory/) , 2024-03-17-0911
```
I want to use Claude's API to build personalized agents for me with long term memory. 

So kind of creating separate age
nts which could act like companions - maybe like Marketing Expert, Co-Founder, Design Guy... essentially someone to brai
nstorm things & ideas with, which it can remember in the long run. 

Do I use Claude's API with Langchain or something l
ike that, with Pinecone etc. I'm new to this. 

Can anyone guide me on how to proceed on this path further? 

And some p
otential avenues to explore. 
```
---

     
 
all -  [ If you like langchain, get familiar with patch-package too ](https://www.reddit.com/r/LangChain/comments/1bfve1k/if_you_like_langchain_get_familiar_with/) , 2024-03-17-0911
```
First day using langchain, and already 3 patches to the official repo.  10 years ago this would have been called alpha s
oftware, and invitation only for qa.  Absolute amatuer hour.  
```
---

     
 
all -  [ Twilio get back to voice function after stream done in gettin reply ](https://www.reddit.com/r/code/comments/1bfu603/twilio_get_back_to_voice_function_after_stream/) , 2024-03-17-0911
```
IN THIS CODE I CAN CALL MY TWILIO PHONE AND GPT WILL ANSWER BUT AFTER THE FIRST REPLY FROM GPT I CANNOT TALK BACK AGAIN 
BECAUSE I CAN'T GET BACK TO THE VOICE FUNCTION.

In the following code I manage to use gather to get user input in the c
all, and I use stream to get a response, and it works with no problem, but I can't get back to the function where I call
 gather to get user input because the stream might be running all time, what can I do?  


    from fastapi import FastA
PI, Request, Response, Form
    from langchain_core.messages import HumanMessage, SystemMessage
    from twilio.rest imp
ort Client
    from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI
    from pydub import AudioSeg
ment
    from queue import Queue
    import audioop
    import io
    import asyncio
    import base64
    from pyngrok 
import ngrok
    from starlette.responses import Response
    from twilio.rest import Client
    from fastapi import Fas
tAPI, WebSocket, Request, Form
    from twilio.twiml.voice_response import VoiceResponse, Connect
    from typing import
 Annotated
    import json
    import os
    import websockets
    import openai
    import uvicorn
    from dotenv impo
rt load_dotenv
    load_dotenv()
    
    OPENAI_API_KEY = '*****'
    ELEVENLABS_API_KEY = os.environ['ELEVENLABS_API_K
EY']
    
    PORT = int(os.environ.get('PORT', 8000))
    ELEVENLABS_VOICE_ID = os.environ.get('ELEVENLABS_VOICE_ID', '
onwK4e9ZLuTAKqWW03F9') 
    
    load_dotenv()
    
    # Twilio credentials
    TWILIO_ACCOUNT_SID = '***'
    TWILIO_A
UTH_TOKEN = '***'
    
    application = FastAPI()
    
    # Initialize Twilio client
    client = Client(TWILIO_ACCOUN
T_SID, TWILIO_AUTH_TOKEN)
    
    
    # Define a shared queue to pass user text
    user_text_queue = Queue()
    
   
 # Define a function to push user text to the queue
    async def push_user_text(user_text):
        user_text_queue.put
(user_text)
    
    @application.post('/voice/{first_call}')
    async def voice(response: Response, request: Request,f
irst_call: bool):
    
        if first_call:
            #caller name only for us numbers
            #caller_name = fo
rm_data['CallerName']
            twiml_response = VoiceResponse()
            twiml_response.say('Hola, Mi nombre es Ra
fael, como te puedo ayudar?', language='es-MX', voice='Polly.Andres-Neural')
            twiml_response.gather(
        
        action='/transcribe',
                input='speech',
                language='es-US',
                enhanced
='false',
                speech_model='phone_call',
                speech_timeout='1')
        else:
            twiml
_response = VoiceResponse()
            twiml_response.gather(
                action='/transcribe',
                inp
ut='speech',
                language='es-US',
                enhanced='false',
                speech_model='phone_cal
l',
                speech_timeout='1')
            
        return Response(content=str(twiml_response), media_type='ap
plication/xml')
    
    
    #old call endponint
    @application.post('/transcribe')
    async def handle_call_output(
request: Request, From: Annotated[str, Form()]):
        form_data = await request.form()
        user_text = form_data[
'SpeechResult']#get text from user
        print(user_text)
        await push_user_text(user_text)  # Push user text to
 the queue
        
        response = VoiceResponse()
        connect = Connect()
        connect.stream(url=f'wss://{r
equest.headers.get('host')}/stream')
        response.append(connect)
        
        await asyncio.sleep(2)
        re
sponse.redirect()
        return Response(content=str(response), media_type='text/xml')
    
    
    async def get_stre
am_sid(websocket):
        while True:
            json_data = await websocket.receive_text()
            data = json.lo
ads(json_data)
            if data['event'] == 'start':
                print('Streaming is starting')
            elif 
data['event'] == 'stop':
                print('\nStreaming has stopped')
                return
            elif data['
event'] == 'media':
                stream_sid = data['streamSid']
                
                return stream_sid
  
  
    #receives the main stream from the phone call
    @application.websocket('/stream')
    async def websocket_endpo
int(websocket: WebSocket):
        await websocket.accept()
    
        #init chat log
        messages = [{'role': 'sy
stem', 'content': 'You are on a phone call with the user.'}]
        while True:
            
    		#get user text from 
queue
            user_text = user_text_queue.get()
            #get stream sid
            stream_sid = await get_strea
m_sid(websocket)
    
            #add new user message to chat log
            messages.append({'role': 'user', 'conten
t': user_text, })
            
    		#call g.p.t
            print('stream sid: ',stream_sid)
            await chat_com
pletion(messages, websocket, stream_sid, model='g.p.t-3.5-turbo')
    
    
    async def chat_completion(messages, twil
io_ws, stream_sid, model='g.p.t-4'):
        openai.api_key = 'sk-*****'
        response = await openai.ChatCompletion.
acreate(model=model, messages=messages, temperature=1, stream=True,
                                                    
   max_tokens=50)
    
        async def text_iterator():
            full_resp = []
            async for chunk in resp
onse:
                delta = chunk['choices'][0]['delta']
                if 'content' in delta:
                    co
ntent = delta['content']
                    print(content, end=' ', flush=True)
                    full_resp.append(co
ntent)
                    yield content
                else:
                    print('<end of ai response>')
       
             break
    
            messages.append({'role': 'assistant', 'content': ' '.join(full_resp), })
        pri
nt('Init AUdio stream')
        await text_to_speech_input_streaming(ELEVENLABS_VOICE_ID, text_iterator(), twilio_ws, st
ream_sid)
    
    
    
    async def text_to_speech_input_streaming(voice_id, text_iterator, twilio_ws, stream_sid):
 
       uri = f'wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input?model_id=eleven_monolingual_v1&optimize
_streaming_latency=3'
    
        async with websockets.connect(uri) as websocket:
            await websocket.send(jso
n.dumps({'text': ' ', 'voice_settings': {'stability': 0.5, 'similarity_boost': True},
                                  
           'xi_api_key': ELEVENLABS_API_KEY, }))
    
            async def listen():
                while True:
      
              try:
                        message = await websocket.recv()
                        data = json.loads(me
ssage)
                        if data.get('audio'):
                            audio_data = base64.b64decode(data['aud
io'])
                            yield audio_data
                        elif data.get('isFinal'):
                   
         print('Received final audio data')
                            break
                    except Exception as e:

                        print('Connection closed',e)
                        break
    
    
            listen_task = 
asyncio.create_task(stream(listen(), twilio_ws, stream_sid))
    
            async for text in text_chunker(text_iterat
or):
                await websocket.send(json.dumps({'text': text, 'try_trigger_generation': True}))
    
            a
wait websocket.send(json.dumps({'text': ''}))
    
            await listen_task
    
    
    # used to audio stream to
 twilio
    async def stream(audio_stream, twilio_ws, stream_sid):
        async for chunk in audio_stream:
            
if chunk:
                audio = AudioSegment.from_file(io.BytesIO(chunk), format='mp3')
                if audio.chann
els == 2:
                    audio = audio.set_channels(1)
                resampled = audioop.ratecv(audio.raw_data, 2
, 1, audio.frame_rate, 8000, None)[0]
                audio_segment = AudioSegment(data=resampled, sample_width=audio.sa
mple_width, frame_rate=8000, channels=1)
                pcm_audio = audio_segment.export(format='wav')
                
pcm_data = pcm_audio.read()
                ulaw_data = audioop.lin2ulaw(pcm_data, audio.sample_width)
                m
essage = json.dumps({'event': 'media', 'streamSid': stream_sid,
                                      'media': {'payload
': base64.b64encode(ulaw_data).decode('utf-8'), }})
                await twilio_ws.send_text(message)
        
    
   
 #chunks text to process for text to speech api
    async def text_chunker(chunks):
        '''Split text into chunks, e
nsuring to not break sentences.'''
        splitters = ('.', ',', '?', '!', ';', ':', '—', '-', '(', ')', '[', ']', '}',
 ' ')
        buffer = ''
    
        async for text in chunks:
            if buffer.endswith(splitters):
            
    yield buffer + ' '
                buffer = text
            elif text.startswith(splitters):
                yield 
buffer + text[0] + ' '
                buffer = text[1:]
            else:
                buffer += text
    
        i
f buffer:
            yield buffer + ' '
    
    
    if __name__ == '__main__':
        ngrok.set_auth_token(os.enviro
n['NGROK_AUTH_TOKEN'])
        public_url = ngrok.connect(str(PORT), bind_tls=True).public_url
        number = client.i
ncoming_phone_numbers.list()[0]
        number.update(voice_url=public_url + '/voice/true')
        print(f'Waiting for 
calls on {number.phone_number}')
        uvicorn.run(application, host='0.0.0.0', port=PORT)

&#x200B;
```
---

     
 
all -  [ Perform extraction on the answer to a prompt with ConversationBufferMemory ](https://www.reddit.com/r/LangChain/comments/1bftk5y/perform_extraction_on_the_answer_to_a_prompt_with/) , 2024-03-17-0911
```
I have an existing RAG flow that uses ConversationBufferMemory and a prompt that summarizes the history to answer questi
ons.  I want to add extraction to the response to pull out some data I'm interested in (like the standard examples, name
s of people, places, etc) so I can use that in my own code (not an agent).

Has anyone implemented something like this? 
 I'm not seeing how I should integrate the llm.with\_structured\_output with the existing ConversationBufferMemory flow.
  Does anyone have an example that does all of those things?  For reference I'm using OpenAI and FAISS in Python.  Thank
s!

[Extraction | 🦜️🔗 Langchain](https://python.langchain.com/docs/use_cases/extraction/?ref=blog.langchain.dev)

[Conve
rsation Buffer | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/memory/types/buffer)
```
---

     
 
all -  [ Does LangChain support the new milvus cosine similarity? ](https://www.reddit.com/r/LangChain/comments/1bfrguy/does_langchain_support_the_new_milvus_cosine/) , 2024-03-17-0911
```
I'm very new to working with LLMs, but I'm an experienced software engineer. I've read that OpenAI embeddings work best 
with vector stores that are configured to use cosine similarity when doing searches. Milvus, the vector store I'm using 
for my POC right now, supports cosine similarity. However it is a very recent feature.

The docs I'm looking at for Lang
Chain show it auto-configuring the collection, for the most part. What I'm asking is if LangChain will use cosine simila
rity when I configure it with milvus and OpenAI embeddings
```
---

     
 
all -  [ Introducing Instagram's First AI News Headlines Page! ](https://www.reddit.com/r/u_fastheadlines/comments/1bfgylj/introducing_instagrams_first_ai_news_headlines/) , 2024-03-17-0911
```
I'm excited to share the launch of Instagram's AI News Headlines Page!  
*Here's what you need to know:*  
**Built With 
Python:** Our team utilized Python to develop this innovative platform, ensuring efficiency and flexibility in deliverin
g news content.  
**Using llama2 & LangChain:** We integrated llama2 and LangChain technologies to enhance natural langu
age processing capabilities, enabling accurate and relevant news summaries.  
**Automated CronJobs**: Our system runs au
tomated CronJobs to continuously update the news feed, keeping you informed in real-time.  
**News APIs:** We've leverag
ed various News APIs to aggregate information from diverse sources, providing comprehensive coverage across different to
pics.

I'll be very happy to write more technical post later on How we built it.

Make sure to checkout & support us!  

[https://www.instagram.com/fastheadlines/](https://www.instagram.com/fastheadlines/)
```
---

     
 
all -  [ R&R / Tooling for a Small Team ](https://www.reddit.com/r/aipromptprogramming/comments/1bfds5w/rr_tooling_for_a_small_team/) , 2024-03-17-0911
```
A friend and I are working on a new startup project using LLMs for a conversational interface with our users.

He is an 
experienced full stack developer (cloud infra, database, web), but without data science or analytics skills. I am taking
 on the more business oriented role of CEO / Product Manager. I am also the one who is likely to do the prompt engineeri
ng to get the LLMs to interact with our users the way we want to.

I understand code and used to code a long time ago, b
ut by today's standards I'm not a competent developer by any means. I've been looking at langchain and that is probably 
a bit too far on the technical side of where I want to be spending my time. Ideally I'd like to be able to experiment wi
th prompt engineering in an environment like Chat GPT but where i can version control what i'm doing, maybe record testi
ng output and produce something that my CTO colleague can then implement in code and make it all work.

Does anyone have
 any suggestions on how we should setup our workflow and what tools, packages or IDEs we should use in this scenario? Or
 am I overreaching to think that I can do the prompt engineering and conversation flow design without learning python or
 something like that?

For context, the tools he has selected for his part so far are Google Cloud, GitHub and Python/Dj
ango for web / API development. We're starting with GPT4 as our LLM but will evaluate others later. 
```
---

     
 
all -  [ Advanced course on LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1bfbrv7/advanced_course_on_llm/) , 2024-03-17-0911
```
I've been looking for a while on this topic, but I don't feel confident and the time to keep reading over all the texts 
required to get a full picture of this. The problem with YT channels is that there is a ton of fluff (because most guys 
adjust their videos to the YT algo), and texts are not really comprehensive and take a ton of time to digest, which make
s my pace extremely slow. Furthermore, finding a good order of things instead of jumping from paper to paper which most 
of the time are totally not related makes things even harder. I'm totally aware that there are a ton of 'scammers' selli
ng b\*\*\*s\*\*t AI courses that are anything but very basic prompting as they feel very creative or something. 

So at 
this point I was wondering if there are any recommended advanced courses that cover all that anyone needs to know to put
 up to date with the scene to get a good head start.  The more advanced, the better, which involves, Langchain, Python s
kills and anything you could think that could make the course sharper in the whole sense, not just simple prompting.
```
---

     
 
all -  [ When to simply feed whole document in RAG? ](https://www.reddit.com/r/LangChain/comments/1bf9ps7/when_to_simply_feed_whole_document_in_rag/) , 2024-03-17-0911
```
Hello, I am new to RAG.

I am making a chatbot for the Beeline application for my company. 

The Beeline team at my comp
any has put together two FAQs to use as context: one for contractors/vendors and one for internal employees. Each FAQ is
 a word document with various questions and answers that describe processes like onboarding, submitting time cards, etc.
. Each is about 3000 tokens long.

I have written two system prompts based on whether the user is a contractor/vendor or
 internal users. Each is about 2000 tokens… does this seem like too much?

The chatbot application uses the correct faq 
document and system prompt based on the user. Basically, I just grab the correct ones and send to my deployed LLM alongs
ide the user query. The total prompt is usually like 5000 tokens.I use the faq document in its entirety given I am using
 a gpt-4-32k deployment as my LLM.

The responses are accurate every time. However, they are slow. Is this due to token 
size? Should I be chunking? How can I ensure a given chunk would have all the right sentences in it if I chunked? Some p
rocesses are 5 sentences long and what if they are captured in different chunks?

Any insight is super helpful. I am cod
ing everything rather than using langchain or llama2index or whatever. Should I not do this? I found the documentation f
or both hard to follow honestly so I immediately abandoned trying to use them 😅

```
---

     
 
all -  [ Knowing number of tokens in SQL agent ](https://www.reddit.com/r/LangChain/comments/1bf9mkq/knowing_number_of_tokens_in_sql_agent/) , 2024-03-17-0911
```
I am using the below sql\_agent to query through my database:  
agent = create\_sql\_agent(llm=llm, toolkit=sql\_toolkit
, agent\_type=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION,  
 handle\_parsing\_errors=True, verbose=True, max\_execution\_t
ime=200,  
 max\_iterations=1000)  
Is there any way to count the total number of tokens(prompt tokens+query tokens+quer
y\_result tokens+thought tokens+action tokens+observation tokens+tool tokens) used by this agent.  
I have used the belo
w approach without good results:  
[https://python.langchain.com/docs/modules/model\_io/llms/token\_usage\_tracking](htt
ps://python.langchain.com/docs/modules/model_io/llms/token_usage_tracking)
```
---

     
 
all -  [ How to call Multiple API's for a user input via LangChain ](https://www.reddit.com/r/LangChain/comments/1bf7nuo/how_to_call_multiple_apis_for_a_user_input_via/) , 2024-03-17-0911
```
I have two swagger api docs and I am looking for creating an app which can interact with API's. My user input depends on
 two different API endpoint from two different  Swagger docs.

My user query depends on calling two different  API's fro
m two different swagger endpoint. I want to chain the first API response value from chain 1  and set the input variables
 for the second API from a different swagger. 

For Example, 

User query, 'What is the train status 1234'

Call API 1- 
/travel-modes-reference/train to get the reference for train--APi response as '1'

Call API 2  /transport/1234/status&mo
de=1

how can I perform this in Langchain using Chains ,tools and agent ? 
```
---

     
 
all -  [ anyone mind helping me scope out a custom LLM tool for our editorial team ](https://www.reddit.com/r/LangChain/comments/1bf4l56/anyone_mind_helping_me_scope_out_a_custom_llm/) , 2024-03-17-0911
```
I'm thinking i need gpt4 + langchain to access urls, docs, sheets via google drive + vector db so all the citations and 
info is accurate (medical, cancer, legal) etc.. 

i'm looking for an effective way to train my own and store the data an
d draft from briefs that we human edit afterwards
```
---

     
 
all -  [ Amyone work in editorial or content agency? looking for some advice ](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1bf4ghu/amyone_work_in_editorial_or_content_agency/) , 2024-03-17-0911
```
I feel like I need a custom solution like gpt4 + langchain + vector database + any other suggestions, has anyone built o
ut their own local LLM like this for writing serious SEO articles or journalism? 

would love some help even with some p
rompts for training once i have this setup..
```
---

     
 
all -  [ Can any database be a Vector Database? ](https://www.reddit.com/r/LangChain/comments/1bf3kjs/can_any_database_be_a_vector_database/) , 2024-03-17-0911
```
As long as I perform the text splitting and embedding before hand, is there any reason I can't store the embeddings in, 
say, Redis or MongoDB?
```
---

     
 
all -  [ RAG agent in langchain ](https://www.reddit.com/r/LangChain/comments/1bf2iya/rag_agent_in_langchain/) , 2024-03-17-0911
```
I have a rag system that is used to answer customer questions.
But to optimise the retrieval, I want the agent ask some 
follow up questions and instruct user to provide answer before retrieval.

I have a few questions.
Which type of langcha
in agent is good at this task?
How to prompt the agent to ask follow up one or more question dynamically?
Do I need mult
iple agent to do it?  I haven’t touched on langgraph yet but I want to see one agent can do this task.

Thanks.  

```
---

     
 
all -  [ llama2 mocking me ](https://www.reddit.com/r/LangChain/comments/1bf0hb0/llama2_mocking_me/) , 2024-03-17-0911
```
Im currently replacing the OpenAI-Api with an langchain-instance using ollama, llama2 and chrome-db.

This was the first
 test I did via frontend:

&#x200B;

[Thats just rude!](https://preview.redd.it/wnyufxub4eoc1.png?width=1709&format=png&
auto=webp&s=4ae06cb94d55db4491138bdd2b140509bfba7cd5)
```
---

     
 
all -  [ How are you implementing AI? ](https://www.reddit.com/r/devops/comments/1bezy3t/how_are_you_implementing_ai/) , 2024-03-17-0911
```
There's a bit of a lull in my current job as we're waiting on construction of a new data center, so I've begun studying 
up on AI skills. There's a lot to learn so I'm curious what long term goals might be possible to strive for. 

I'm curre
ntly working on using langchain to query our confluence space. After that I thought about creating something like nimbus
.dev for our elastic stack.

What have you done with AI.in your environment that's benefitted you?
```
---

     
 
all -  [ Current best practices for ingesting data from PDF (Maybe Microsoft Azure AI Search?) ](https://www.reddit.com/r/LangChain/comments/1bev63g/current_best_practices_for_ingesting_data_from/) , 2024-03-17-0911
```
Hi,

not sure if this is the right subreddit, but i see there are plenty of questions about RAG here.

I'm working on bu
ilding a RAG project with a lot of user manuals, technical stuff and so on. With my current ingestion pipeline, the resu
lts are very mixed. Some answers are very good, while in other cases the retrieval step doesn't provide any helpful stuf
f.

At the moment i'm kinda stuck, because i don't know how to improve the quality in chunking and getting the data stru
cture right.

I tried many different pdf loaders. First problem here is, that some loaders can't deal with all pdfs i've
 got. Eventually i sticked with Unstructured, since it can extract tables and images, and keeps the page numbers as meta
data. Unstructured comes with the possibilty to chunk data 'by title', so that we get more consistent chunks across the 
chapters of a file. This approach alone wasn't that impressive. I used the LangChain Semantic chunker afterwards and get
 pretty decent results so far (still far from good, unfortunately). Also the structure of the extracted tables seem to b
e a bit off most of the time. I'm using Unstructured locally, i don't have any experience with the API.

I'm getting stu
ck at the moment, since i don't really know how to improve my chunking and preprocessing any further.

I also tried spli
tting bigger and smaller chunks for small-to-big retrieval. Using smaller chunks for the search-step and getting bigger 
parent chunks for the context. The results where quite horrible. Another thing i haven't tried so far, is a window retri
eval, where we use neighboured chunks from the retrieved chunks for more context.

At this time many people tried to bui
ld RAG projects. Are there any best practices in the ingestion of data i may have overseen so far? Currently i'm thinkin
g about using Azure AI Search, instead of doing the ingestion-step myself. This would make most of my own work useless, 
but currently i just want to get the best possible results.



Very thankful for some input and/or tips


```
---

     
 
all -  [ How does a PartialPrompt fit into a processing chain? ](https://www.reddit.com/r/LangChain/comments/1besaia/how_does_a_partialprompt_fit_into_a_processing/) , 2024-03-17-0911
```
The documentation about Partial Prompts only shows operation of \`format\`. How would one work a partial prompt into a c
hain?  If one \`invoke\`s it, does it return a partially instantiated prompt that goes to the next stage of the chain?


Anyone have an example of this that they could share?

It seems like a \`FewShotPrompt\` is a special case of a partial 
prompt, right?
```
---

     
 
all -  [ Deci AI Launched a new model and inference platform. Here's a tutorial on using it ](https://www.reddit.com/r/ArtificialInteligence/comments/1bepemz/deci_ai_launched_a_new_model_and_inference/) , 2024-03-17-0911
```
[Here's a link](https://colab.research.google.com/drive/1JW8t-kosLEgYVxXadwwDMypnQ5c_UD2u?usp=sharing) to the notebook t
o hack around with it!  This notebook will show you how to access the API via cURL, requests, and OpenAI SDK.

I have an
other notebook which shows how to use the model in LangChain by [implementing a custom LLM](https://colab.research.googl
e.com/drive/1PMwMovV-ji1mp0yl0qYDTI-gdG6SjOnZ?usp=sharing).

&#x200B;

Edit: Updated link to the notebook
```
---

     
 
all -  [ RAG is too slow with 100k PDFs! What do you suggest? LLM fine-tuning? ](https://www.reddit.com/r/LangChain/comments/1benf40/rag_is_too_slow_with_100k_pdfs_what_do_you/) , 2024-03-17-0911
```
Hello everyone,

This is my first post here and I hope it is clear and correct for you all :)

Currently, I am working o
n an AI project where the idea is to 'teach' a large language model thousands of english PDFs (around 100k, all about th
e same topic) and then be able to chat with it.

I followed several tutorials, using different LLMs (Zephyr, Llama2, Mis
tral) from HuggingFace and giving a proper prompt for the topic.

In the last weeks I tried RAG and unfortunately it cou
ld not give me good results :( I suppose due to the huge amount of data, but it is really really slow and to answer it t
akes 10 min or more (on a cluster  Tesla V100-SXM2-32GB GPU)! Is there a way to speed it up?

Moreover, sometimes it giv
es very good answers, while sometimes it gives erroneous information and a sort of 'hallucination' :( I really tried eve
rything: change the prompt, change the embedding model, change the LLM, change the chunk size, but nothing could help.  

Finally, I am afraid that RAG is not good at all for deployment since you need a lot of memory for the 'external knowle
dge' and for the model itself.

Is there another solution to RAG? Should I use fine tuning? If yes, how can I let my mod
el to assimilate all these data? Should I turn the PDFs in JSONs made of Questions/Answers?

Did you succed in doing a p
roject like this? If yes, can you help me, please? I do not know how to properly solve this issue. Any help would be rea
lly appreciated! 

Thank you so much in advance!

EDIT:  
I am really really happy to see so much people trying to help 
me! I THANK YOU ALL! :)   
Apologies if it is a long text and maybe with too general information, but I am still a begin
ner and I am trying to explain my problem as best as I can :(
```
---

     
 
all -  [ Langchain OR Llamaindex for RAG app with Typescript ](https://www.reddit.com/r/LangChain/comments/1bemubq/langchain_or_llamaindex_for_rag_app_with/) , 2024-03-17-0911
```
Hello ! I want to develop a pretty complex RAG application.

I spent my time learning concepts on both Langchain and Lla
mainde, but I am not yet sure which one to pick

Question for people that already worked with this, is it easier (more a
nd better docs, clean implementation) to work with TS + Langchain or TS + Llamaindex ? 
```
---

     
 
all -  [ CopilotKit v0.4.1 - LangChain support ](https://www.reddit.com/r/selfhosted/comments/1beldc0/copilotkit_v041_langchain_support/) , 2024-03-17-0911
```
Hi everyone,

We have just released our new CopilotKit version that supports LangChain.

CopilotKit is a React Infrastru
cture library that works against OpenAI or other LLMs to build ChatBots, Textareas, and Co-Agents.

[https://github.com/
CopilotKit/CopilotKit/](https://github.com/CopilotKit/CopilotKit/)

You can feed the React components with your applicat
ion context and run prompts against it to trigger 'function calls.'

&#x200B;

The repository is 100% open-source (self-
hosted). You can read the quick-start guide here:

[https://docs.copilotkit.ai/getting-started/quickstart-chatbot](https
://docs.copilotkit.ai/getting-started/quickstart-chatbot)

&#x200B;

We have made an example app for building a PowerPoi
nt presentation that can search the web (with Langchain and Tavily) and automatically create a presentation about any to
pic.

[https://links.github20k.com/power-point](https://links.github20k.com/power-point)

&#x200B;

We are looking for m
ore exciting features to build; let me know your thoughts.
```
---

     
 
all -  [ [HIRING] Senior ML Engineer - 100% Remote + every other friday off ](https://www.reddit.com/r/MachineLearningJobs/comments/1bekw0v/hiring_senior_ml_engineer_100_remote_every_other/) , 2024-03-17-0911
```
Apply here: [https://grnh.se/50c178c17us](https://grnh.se/50c178c17us)

Building with the latest tools, our Machine Lear
ning teams launch for Silicon Valley startups and Life Science giants alike.

Join Loka to work remotely, ship projects 
you’re proud of and enjoy every other Friday off.

**The Role**

* Understand business objectives and develop models tha
t help achieve them, plus metrics to track their progress.
* Design and implement complex ML systems using classical ML,
 DL and Foundation Models and following best practices.
* Lead client communications by gathering requirements, managing
 expectations and communicating deliverables.
* Wrangle, explore and visualize data with a careful eye for issues that r
equire data cleaning as well as differences in data distribution that may affect performance after deployment.
* Analyze
 model errors; design strategies to overcome them.
* Deploy, maintain and upgrade ML models and pipelines.
* Follow Loka
’s career track for growth by demonstrating technical excellence, innovation, autonomy, ownership, communication and tea
mwork.

**The Benefits**

* Every other Friday off (26 extra days off a year!)
* LokaLabs incubator
* Explore and Reloca
tion programs (three months work abroad or full international relo)
* Remote and flexible
* Paid sick days and local hol
idays
* Fitness subscription

**The Required Hard Skills**

* Bachelor’s degree in Computer Science or related
* Profici
ent in English
* Experience with Python, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, Keras, Sci
kit-learn, Spark etc.)
* Strong understanding of statistical, ML and deep learning algorithms (candidates with NLP exper
ience preferred)
* Experience building GenAI solutions including prompt engineering (e.g: Langchain), fine-tuning and se
rving LLMs, search and embeddings, etc.
* Experience with MLOps, preferably in AWS (e.g: Sagemaker), as well as standard
s tools (e.g. MLFlow)
* Experience visualizing and manipulating big datasets
* Client-facing experience

**The Required 
Soft Skills**

* Curiosity—Ambition to learn and grow into different industries with a modern tech stack
* Autonomy and 
positivity—We’re a fully remote, globally distributed team
* Teamwork—Enjoy a collaborative approach
* Adaptability—Oper
ate with a startup mindset and move at a startup pace
```
---

     
 
all -  [ Best Embedding databse for massive text data. ](https://www.reddit.com/r/LangChain/comments/1bekhre/best_embedding_databse_for_massive_text_data/) , 2024-03-17-0911
```
I have been working on a 'ask questions to pdf' project. There are following issues I'm facing.

1. The data is huge so 
the RAG agent is hallucinating some time if it has the context it says 'The given context does not' but ad back end it h
as the context.
2. Sometimes it overwhelms with the data and give incorrect answers.
3. The emmbeddingd are failling to 
give context about the tables. (Currently I have converted all the tables to a json file but Im facing problems to embed
 a json file).

Please reply if anyone is familier with such Kind of project and also if I can use any other DB curently
 I'm using ChromaDB. I have used FAISS but it was less accurate than ChromaDB.
```
---

     
 
all -  [ Langsmith Plus use in Europe makes you not compliant ](https://www.reddit.com/r/LangChain/comments/1bekfw8/langsmith_plus_use_in_europe_makes_you_not/) , 2024-03-17-0911
```
We were trying to buy Langsmith Plus for our startup (300+ employees) for 6 users and then consider if in the future we 
would extend the use within the company and go for an Enteprise version (cost starts at 17k for that). However, when we 
did the normal checks we do for all our third party vendors, we noticed that they didn't have a DPA, so we would need th
em to sign our DPA (as it is the only way for us to be compliant to European laws). I put our legal advisor in touch wit
h them and they told us clearly that they only do this for Enterprise customers and they literally added they don't comp
ly to GDPR :-o. This is the full reply they sent:  
'Unfortunately we're not fully GDPR compliant, so we're not signing 
DPAs with out plus plan customers at this time. Wish I had a better update to share. '

So unfortunately we are now look
ing into alternatives (W&B would be a safe choice as I see they have their own DPA so we wouldn't need to sign anything)
.  
The question is: do you use Langsmith Plus in Europe? Did you know that they are not GDPR compliant? (and so your co
mpany is not as well if you use them).  
I also hope they reconsider this policy and let us use their product legally, w
e would even be ok to pay a small one off to have them to sign our DPA. But they need to collaborate with the companies 
to make sure they don't lose compliance. What do you think? did you know of this before?
```
---

     
 
all -  [ Sql database embedding and store into chroma ](https://www.reddit.com/r/LangChain/comments/1bej7be/sql_database_embedding_and_store_into_chroma/) , 2024-03-17-0911
```
Need help to do this :\_  


sql\_db = SQLDatabase.from\_uri('sqlite:///Chinook.db')  
print(sql\_db.dialect)  
print(sq
l\_db.get\_usable\_table\_names())  


llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0,  
 openai\_api\_key=os.get
env('OPENAI\_API\_KEY'))  


\# chroma db instance created  
if os.path.exists('db'):  
 pass  
else:  
os.mkdir('db')  

presist\_directory = 'db'  
embeddings = OpenAIEmbeddings()  
vectordb = Chroma(persist\_directory=presist\_directory, 
 
 embedding\_function=embeddings)  


\# TODO create embeddings and store indexing into vectordb...(how can i create em
beddings from sql db and store it in vectordb)  


  


  


how can i store db into vector db please help to resolve th
is
```
---

     
 
all -  [ Pinecone Hybrid Search Retriever + gpt 3.5 ](https://www.reddit.com/r/LangChain/comments/1begx6v/pinecone_hybrid_search_retriever_gpt_35/) , 2024-03-17-0911
```
 I've finished putting the document in the pinecone index and bringing it up. Now I want to use bm25 together to make Pi
necone Hybrid Search Retriever and gpt 3-5 to make a chatbot, but it doesn't work. Can I share the example code? 
```
---

     
 
all -  [ System Prompt for a language learning app ](https://www.reddit.com/r/LangChain/comments/1begjl3/system_prompt_for_a_language_learning_app/) , 2024-03-17-0911
```
Hello guys,

I am having a difficult time getting desired responses from my llm based on the system prompt that I crafte
d for my language learning chatbot. Currently I am using groq's mixtral-8x7b-32768 model with langchain.

Here is a typi
cal user journey -

1. User logs in
2. Chatbot guides the user through a conversational onboarding to collect basic info
 like name, age, academic level.
3. AI prepares an English level test to gauge student proficiency in the language based
 on the student details (provided during onboarding stage)
4. AI starts posing questions one by one to the student witho
ut giving any feedback or explanation to each question.
5. Once the assessment is complete, a detailed feedback on stren
gths and weaknesses of the student is given.
6. A personalised and comprehensive study plan is generated for the student
 based on the assessment results.

I tried to put the above user journey in the system prompt as instructions, but the l
lm is not able to follow. Sometimes it's giving all the questions at once and sometimes its providing answers on its own
 and then giving feedback plus creating the study plan in one go itself.

I've tried numerous variations of my system pr
ompt, adjusted the temperature of the model as well, but no luck. I keep getting undesirable responses.

Someone pls hel
p me out here as to how do I need to approach this problem.
```
---

     
 
all -  [ Issue when querying pinecone data ](https://www.reddit.com/r/LangChain/comments/1beett5/issue_when_querying_pinecone_data/) , 2024-03-17-0911
```
Trying out a simple application with Langchain and Pinecone training by uploading a PDF document. I was able to upload t
he vectors to pinecone successfully but whenever I try querying I receive a PineconeApiAttributeError: QueryResponse has
 no attribute '0' at \['\['received\_data'\]'\] error. The query was in string format and was embedded in vector format 
using OpenAIEmbeddings(). My code is as follows.

    def retrieve_query(query,k=2):     
    xq = embeddings.embed_quer
y(query) #embeddings = OpenAIEmbeddings(api_key)     
    matching_results = index_name.query(vector = xq,top_k=k,includ
e_values=True)     
    return matching_results  
    from langchain.chains.question_answering import load_qa_chain 
   
 from langchain import OpenAI 
    llm=OpenAI(model_name='text-davinci-003',temperature=0.5) chain=load_qa_chain(llm,cha
in_type='stuff') 
    
    def retrieve_answers(query):     
    doc_search=retrieve_query(query)     
    print(doc_sea
rch)     
    response=chain.run(input_documents=doc_search,question=query)     
    return response  

the doc\_search 
variable printed out {'matches': \[\], 'namespace': '', 'usage': {'read\_units': 6}}
```
---

     
 
all -  [ Google Cloud Databases Advancements with GenAI in 2024 ](https://www.reddit.com/r/u_Glittering-Pack5342/comments/1beet6j/google_cloud_databases_advancements_with_genai_in/) , 2024-03-17-0911
```
 

* [Introduction ](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Introduction)
* [AlloyDB]
(https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#AlloyDB)
* [LangChain](https://www.sparity.co
m/blogs/google-cloud-databases-with-gen-ai-in-2024/#LangChain)
* [Vector Search in Databases](https://www.sparity.com/bl
ogs/google-cloud-databases-with-gen-ai-in-2024/#Vector_Search_in_Databases)
* [Spanner and AlloyDB with Vertex AI](https
://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Spanner_and_AlloyDB_with_Vertex_AI)
* [How google c
loud databases advancements helps you ?](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#How_g
oogle_cloud_databases_advancements_helps_you)
* [Conclusion](https://www.sparity.com/blogs/google-cloud-databases-with-g
en-ai-in-2024/#Conclusion)
* [Why Sparity](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Why
_Sparity)
* [Related Posts](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Related_Posts)

##
 Introduction 

The fusion of AI technology with databases has opened up fresh possibilities for innovation and transfor
mation in the tech sector. Google Cloud, a front runner in cloud computing, has spearheaded this evolution by continuous
ly strengthening its offerings to deliver cutting-edge solutions to businesses and software developers. Google has annou
nced significant progress in merging generative AI with its databases, marking a pivotal moment in the advancement of AI
-centric applications. Our blog explores into these captivating advancements of google cloud databases and explore their
 impact on AI-powered products moving ahead.

Google’s prioritization of AI underscores improving database functionaliti
es to effectively back AI-driven applications. As AI advances, the demand rises for databases that seamlessly integrate 
with generative AI, facilitating development of intelligent, context-aware applications. According to Google, 71% of com
panies plan to employ databases with built-in GenAI capabilities, emphasizing the crucial role of operational databases 
in leading enterprise AI advancements moving forward.

## AlloyDB

Google’s latest announcement brings a major upgrade t
o AlloyDB AI, a fully managed database designed for GenAI workloads and compatible with PostgreSQL. Now available in bot
h AlloyDB and AlloyDB Omni, AlloyDB AI offers exceptional performance for transactional, analytical, and vector workload
s, making it an ideal choice for enterprise-level tasks. Leveraging the pgvector extension for PostgreSQL, AlloyDB AI en
ables users to work with vector embeddings essential for developing GenAI applications driven by advanced language model
s. This integration simplifies storage, indexing, and querying of vector embeddings directly within the AlloyDB ecosyste
m, enhancing efficiency and effectiveness.

## LangChain

Google is enhancing its ecosystem by open-sourcing LangChain i
ntegrations for all [**Google Cloud**](https://www.sparity.com/blogs/aws-azure-gcp-which-one-to-choose-in-2024/) databas
es, alongside the expansion of AlloyDB AI. LangChain, an open-source LLM orchestration framework, enables developers to 
create context-aware GenAI applications with built-in Retrieval Augmented Generation (RAG) workflows. With support for V
ector stores, Document loaders, and Chat Messages Memory, developers can seamlessly integrate Google Cloud databases int
o their workflow, speeding up the development of AI-powered solutions.

## Vector Search in Databases

It also extended 
its google cloud databases offerings with advanced vector search capabilities across various databases like Spanner, MyS
QL, and Redis. Vector search is crucial for building accurate GenAI-powered applications, allowing developers to find si
milar results for unstructured data such as text and images. By integrating vector search directly into its databases, G
oogle empowers developers to create GenAI apps with their preferred databases, ensuring performance and scalability are 
not compromised.

## Spanner and AlloyDB with Vertex AI

Integration of Spanner and AlloyDB with Vertex AI, enabling the
 use of SQL for model serving and inferencing. When Firestore and Bigtable are merged with Vertex AI Vector Search, GenA
I apps are equipped with semantic search abilities, ensuring timely, accurate, and contextually appropriate user experie
nces in business applications. This seamless fusion of operational data with GenAI is critical for fully harnessing the 
power of AI-driven apps, allowing businesses to provide personalized and smart user interactions on a vast scale.

&#x20
0B;

## How google cloud databases advancements helps you ?

Google’s advancements in AI-integrated databases offer a wi
de array of advantages and benefits for developers, businesses, and users alike. These advancements pave the way for eff
icient development, enhanced performance, improved search capabilities, easier integration, and personalized user experi
ences

**Efficient GenAI Application Development:** AlloyDB AI simplifies the storage, indexing, and querying of vector 
embeddings, streamlining the development process for context-aware applications.

**Enhanced Performance:** AlloyDB AI’s
 exceptional performance for transactional, analytical, and vector workloads is ideal for enterprise-level tasks. Furthe
r boosts performance, providing developers with tools to create high-performing GenAI applications.

**Open-source Frame
work:** LangChain, empowers developers to create GenAI applications with built-in Retrieval Augmented Generation (RAG) w
orkflows. It supports Vector stores, Document loaders, and Chat Messages Memory, ensuring seamless integration with Goog
le Cloud databases for enhanced flexibility and customization.

**Improved Search Capabilities:** Integration of advance
d vector search capabilities into databases like Spanner, MySQL, and Redis revolutionizes search functionalities. This i
ntegration is crucial for building accurate GenAI-powered applications, especially when dealing with unstructured data l
ike text and images.

[Twitter](https://twitter.com/TechJournalist/status/1763222103866663410?s=20)

**Easier Integratio
n:** LangChain’s integration with Google Cloud databases simplifies the development workflow, enabling developers to acc
elerate the creation of context-aware applications. This seamless integration streamlines the process, making it easier 
to leverage AI capabilities within existing systems.

**Fusion with Vertex AI:** The integration of Spanner and AlloyDB 
with Vertex AI enables the use of SQL for model serving and inferencing. Additionally, Firestore and Bigtable merging wi
th Vertex AI Vector Search equips applications with semantic search abilities. This fusion ensures timely, accurate, and
 contextually appropriate user experiences, enhancing the overall user interaction and satisfaction.

**Comprehensive To
olset:** Developers now have access to a comprehensive toolset comprising AlloyDB AI, LangChain, and Vertex AI. This com
bination provides a solid foundation for creating intelligent and innovative applications with the the full potential of
 AI-driven solutions, leading to enhanced products and services.

**Competitive Advantage:** Improved efficiency, perfor
mance, and search capabilities enable businesses to deliver better products and services to their customers. This compet
itive advantage allows companies to stay ahead of the curve.

**Scalability and Reliability:** Google cloud databases ad
vancements ensure scalability and reliability for [**GenAI**](https://www.sparity.com/blogs/things-to-consider-in-ai-pro
duct-development/) applications, critical for businesses operating at scale. Integration with Google Cloud’s infrastruct
ure provides a robust environment for growth.

## Conclusion

Google’s move towards supporting vector storage in current
 google cloud databases simplifies the development of enterprise GenAI applications. Coupled with its integration with L
angChain, developers now have the necessary tools to effectively utilize AI’s potential. With businesses increasingly ad
opting AI-driven solutions for competitive advantages, Google cloud databases advancements serve as a solid groundwork f
or developing the next era of intelligent and innovative applications.

## Why Sparity

Sparity’s expertise in AI-integr
ated databases, coupled with our proficiency positions us as your ideal partner for cloud database services. With Sparit
y, you can efficiently develop GenAI applications, enhance performance, integrate seamlessly, and gain a competitive adv
antage in the market. Our focus on scalability and reliability ensures your applications are future-proof and ready for 
growth. Partner with Sparity for your cloud database needs and unlock the full potential of AI-driven innovation if you 
are already on google cloud databases.

[https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/](http
s://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/)
```
---

     
 
all -  [ How does LangChain foster community engagement and collaboration among language learners? ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1beeccf/how_does_langchain_foster_community_engagement/) , 2024-03-17-0911
```
 

# How does LangChain foster community engagement and collaboration among language learners?

 

## Empowering Languag
e Learners: LangChain's Community Collaboration! 🌍🔗

 

## Introduction

[**LangChain**](https://fxdatalabs.com/) is com
mitted to fostering a vibrant and supportive community for language learners [**worldwid**](https://fxdatalabs.com/)e. T
hrough various initiatives and features, we strive to create an inclusive environment where [**learners**](https://fxdat
alabs.com/) can connect, [**collaborate**](https://fxdatalabs.com/), and [**support**](https://fxdatalabs.com/) each oth
er on their language learning journey. In this comprehensive article, we'll explore how LangChain fosters community [**e
ngagement**](https://fxdatalabs.com/) and collaboration among [**language learners**](https://fxdatalabs.com/).

📷

## I
nteractive Learning Platform

At the heart of [**LangChain's**](https://fxdatalabs.com/) community engagement efforts is
 our interactive learning platform. Through this platform, users can [**access**](https://fxdatalabs.com/) a wide range 
of language learning resources, including lessons, exercises, quizzes, and [**interactive**](https://fxdatalabs.com/) ac
tivities. [**Additionally**](https://fxdatalabs.com/), users can engage with fellow learners through discussion forums, 
chat rooms, and collaborative [**projects**](https://fxdatalabs.com/), fostering a sense of [**community**](https://fxda
talabs.com/) and camaraderie.

## Language Exchange Programs

LangChain facilitates [**language**](https://fxdatalabs.co
m/) exchange programs that allow users to connect with native speakers and practice their [**language**](https://fxdatal
abs.com/) skills in a real-world context. These programs match users based on their language [**proficiency**](https://f
xdatalabs.com/) and learning goals, enabling them to engage in [**meaningful**](https://fxdatalabs.com/) language exchan
ges and cultural exchanges. By [**participating**](https://fxdatalabs.com/) in language exchange programs, users can bui
ld relationships, gain cultural insights, and improve their [**language**](https://fxdatalabs.com/) proficiency through 
authentic [**interactions**](https://fxdatalabs.com/).

## Virtual Events and Workshops

📷

To further promote community
 [**engagement**](https://fxdatalabs.com/), LangChain organizes virtual events and workshops on language-related topics.
 These events cover a [**wide range**](https://fxdatalabs.com/) of subjects, including language [**learning**](https://f
xdatalabs.com/) strategies, cultural immersion, pronunciation practice, and more. Through live webinars, panel [**discus
sions**](https://fxdatalabs.com/), and interactive workshops, users have the [**opportunity**](https://fxdatalabs.com/) 
to learn from language experts, share their experiences, and connect with fellow learners from [**around**](https://fxda
talabs.com/) the world.

## Community Challenges and Competitions

📷

LangChain hosts community [**challenges**](https:/
/fxdatalabs.com/) and competitions to encourage active participation and [**collaboration**](https://fxdatalabs.com/) am
ong users. These challenges may include language [**learning**](https://fxdatalabs.com/) challenges, vocabulary quizzes,
 writing contests, and speaking competitions. By [**participating**](https://fxdatalabs.com/) in these challenges, users
 can set goals, track their progress, and compete with peers in a fun and [**motivating**](https://fxdatalabs.com/) envi
ronment. Prizes and [**incentives**](https://fxdatalabs.com/) may be offered to participants to further incentivize enga
gement and participation.

## Peer Support Networks

📷

LangChain facilitates the [**formation**](https://fxdatalabs.com
/) of peer support networks where users can seek advice, share resources, and provide support to [**fellow**](https://fx
datalabs.com/) learners. These networks may take the form of study groups, language clubs, or online [**communities**](h
ttps://fxdatalabs.com/) dedicated to specific languages or [**language**](https://fxdatalabs.com/) learning interests. T
hrough peer support networks, users can exchange tips, offer encouragement, and [**collaborate**](https://fxdatalabs.com
/) on learning projects, fostering a sense of [**belonging**](https://fxdatalabs.com/) and mutual support.

## Mentorshi
p Programs

To support learners at every stage of their [**language**](https://fxdatalabs.com/) learning journey, LangCh
ain offers [**mentorship**](https://fxdatalabs.com/) programs where experienced learners or language experts can mentor 
and guide newer learners. [**Mentors**](https://fxdatalabs.com/) provide personalized guidance, feedback, and support to
 mentees, helping them navigate [**challenges**](https://fxdatalabs.com/), set goals, and stay motivated. [**Mentorship*
*](https://fxdatalabs.com/) programs foster meaningful relationships and create opportunities for knowledge sharing and 
skill [**development**](https://fxdatalabs.com/).

📷

## Conclusion

In conclusion, [**LangChain**](https://fxdatalabs.c
om/) is dedicated to fostering a vibrant and supportive community for language learners [**worldwide**](https://fxdatala
bs.com/). Through interactive learning platforms, language exchange programs, virtual events, community [**challenges**]
(https://fxdatalabs.com/), peer support networks, and [**mentorship programs**](https://fxdatalabs.com/), LangChain prov
ides users with opportunities to connect, collaborate, and support each other on their [**language**](https://fxdatalabs
.com/) learning journey.

By [**nurturing**](https://fxdatalabs.com/) a sense of community and belonging, LangChain empo
wers learners to achieve their language [**learning**](https://fxdatalabs.com/) goals and embark on a rewarding and enri
ching language [**learning**](https://fxdatalabs.com/) experience.

For more insights into AI|ML and Data Science [**Dev
elopment**](https://fxdatalabs.com/), please write to us at: [**contact@htree.plus**](mailto:contact@htree.plus)| [**F(x
) Data Labs Pv**](mailto:contact@htree.plus)[**t. Ltd.**](https://fxdatalabs.com/)

**#LanguageLearning #CommunityEngage
ment #CollaborativeLearning #LangChain** 🗣️🤝
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-17-0911
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-17-0911
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-17-0911
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-17-0911
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
