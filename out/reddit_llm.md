 
all -  [ use some python package for python agent ](https://www.reddit.com/r/LangChain/comments/184lsxt/use_some_python_package_for_python_agent/) , 2023-11-27-0910
```
Hi, i want to use langchain python agent and openai, to use some python packages. e.g. scanpy, and some python data obje
ct like adata.

    agent_executor = create_python_agent(
    llm=openai_llm,
    tool=PythonAstREPLTool(locals={'adata'
: adata, 'scanpy': sc} ),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

&#x200B;

but g
ot error message like this one

>However, since I cannot import external libraries like scanpy in this environment or ac
cess external data objects like \`adata\`, I cannot execute this task directly.

My question is how can I use package li
ke scanpy with python agent, is that even possible?
```
---

     
 
all -  [ AutoGen v0.2.0 released ](https://www.reddit.com/r/AutoGenAI/comments/184ka6x/autogen_v020_released/) , 2023-11-27-0910
```
[New release: v0.2.0](https://github.com/microsoft/autogen/releases/tag/v0.2.0)  

This is a major release since v0.1.1,
 containing 13 minor releases (from v0.1.1 to v0.1.14) and 6 pre-releases (v0.2.0b1 to v0.2.0b6).

## Highlights since v
0.1.1

### Breaking changes

* Switching to openai v1. Please read the [migration guide](https://microsoft.github.io/aut
ogen/docs/Installation/#migration-guide-to-v02).

### New Features and Enhancements:

* **GPT Assistants Support**: Inte
gration of GPTAssistantAgent leveraging OpenAI Assistant API for conversational capabilities and state management. [http
s://microsoft.github.io/autogen/blog/2023/11/13/OAI-assistants](https://microsoft.github.io/autogen/blog/2023/11/13/OAI-
assistants)
* **Group Chat Enhancements**: Richer speaker selector options and robustness improvements.
* Enhanced retri
eve chat, such as rich text format and customized vector db or embedding function in RAG. [https://microsoft.github.io/a
utogen/blog/2023/10/18/RetrieveChat](https://microsoft.github.io/autogen/blog/2023/10/18/RetrieveChat)
* **AgentEval Fra
mework**: Introduction of AgentEval for assessing task utility in LLM-powered applications. [https://microsoft.github.io
/autogen/blog/2023/11/20/AgentEval](https://microsoft.github.io/autogen/blog/2023/11/20/AgentEval)
* **CompressibleAgent
 for Long Conversations**: Handling long conversations with an experimental CompressibleAgent. [https://github.com/micro
soft/autogen/blob/main/notebook/agentchat\_compression.ipynb](https://github.com/microsoft/autogen/blob/main/notebook/ag
entchat_compression.ipynb)
* Streaming Support: Added experimental streaming capabilities.
* Async Execution and Human I
nput Handling: Enhanced async function execution and better handling of human input.
* **Large Multimodal Models (GPT-4V
) Support**: Enhanced AgentChat capabilities with Large Multimodal Models integration. [https://microsoft.github.io/auto
gen/blog/2023/11/06/LMM-Agent](https://microsoft.github.io/autogen/blog/2023/11/06/LMM-Agent)
* **TeachableAgent**: Intr
oduction of TeachableAgent for persistent user teachings across chat boundaries. [https://microsoft.github.io/autogen/bl
og/2023/10/26/TeachableAgent](https://microsoft.github.io/autogen/blog/2023/10/26/TeachableAgent)
* Enhanced Documentati
on and Developer Tools: Comprehensive updates to README, FAQs, and developer tools.
* **AutoGen Assistant**: Deployment 
of a sample web application for practical demonstration. [https://github.com/microsoft/autogen/tree/main/samples/apps/au
togen-assistant](https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-assistant)
* Demonstration of Agent
s using Langchain Tools: [https://github.com/microsoft/autogen/blob/main/notebook/agentchat\_langchain.ipynb](https://gi
thub.com/microsoft/autogen/blob/main/notebook/agentchat_langchain.ipynb).

### Fixes and Improvements:

* Bug Fixes: Res
olved issues in caching, filter checking, and other minor bugs.
* Documentation Enhancements: Multiple improvements in d
ocumentation, including migration guides and useful tips.
* Model Compatibility and Stability: Enhancements in model com
patibility and overall stability of the package.
* Code Execution: more robust code detection/match/extraction, bug fixe
s for windows and sample code improvements, shell language switch in Docker
* Improved Codebase Reliability: Updates and
 bug fixes for better codebase reliability.

Thanks to the 80 contributors along this 2-month journey!

## Full Changelo
g: [v0.1.1...v0.2.0](https://github.com/microsoft/autogen/compare/v0.1.1...v0.2.0)
```
---

     
 
all -  [ No memory... ](https://www.reddit.com/r/LangChain/comments/184j4sa/no_memory/) , 2023-11-27-0910
```
I'm new to Langchain, I've tried this code, adapted from [https://medium.com/aimonks/chatgpt-clone-with-streamlit-and-la
ngchain-e0d4fa78e33d](https://medium.com/aimonks/chatgpt-clone-with-streamlit-and-langchain-e0d4fa78e33d), but it doesn'
t seem to send the memory of the conversation to the model:

    import streamlit as st
    from langchain.chat_models i
mport ChatOpenAI
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    from dec
ouple import config
    from langchain.memory import ConversationBufferWindowMemory
    
    prompt = PromptTemplate(
  
      input_variables=['chat_history', 'question'],
        template='''You are a very kindl and friendly AI assistant. 
You are
        currently having a conversation with a human. Answer the questions
        in a kind and friendly tone w
ith some sense of humor.
        
        chat_history: {chat_history},
        Human: {question}
        AI:'''
    )
 
   
    
    llm = ChatOpenAI(temperature = 0.7 , model = 'gpt-3.5-turbo')
    memory = ConversationBufferWindowMemory(m
emory_key='chat_history', k=14)
    llm_chain = LLMChain(
        llm=llm,
        memory=memory,
        prompt=prompt

    )
    
    
    st.set_page_config(
        page_title='ChatGPT Clone',
        page_icon='🤖',
        layout='wide'

    )
    
    
    st.title('ChatGPT Clone')
    
    
    # check for messages in session and create if not exists
  
  if 'messages' not in st.session_state.keys():
        st.session_state.messages = [
            {'role': 'assistant', 
'content': 'Hello there, am ChatGPT clone'}
        ]
    
    
    # Display all messages
    for message in st.session
_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
    
    
    u
ser_prompt = st.chat_input()
    
    if user_prompt is not None:
        st.session_state.messages.append({'role': 'use
r', 'content': user_prompt})
        with st.chat_message('user'):
            st.write(user_prompt)
    
    
    if st
.session_state.messages[-1]['role'] != 'assistant':
        with st.chat_message('assistant'):
            with st.spinn
er('Loading...'):
                ai_response = llm_chain.predict(question=user_prompt)
                st.write(ai_resp
onse)
        new_ai_message = {'role': 'assistant', 'content': ai_response}
        st.session_state.messages.append(ne
w_ai_message)

for exemple : 

Hello there, am ChatGPT clone  


give me 3 subject to speak so that i can choose  


Oh,
 the possibilities are endless! But let's narrow it down to a trio of tantalizing topics:  


1. **The Great Outdoors**:
 Whether you're a fan of scaling  mountains, surfing waves, or just enjoying a peaceful picnic in the  park, there's alw
ays an adventure waiting under the open sky. Plus, who  doesn't love a good story about a squirrel with overly ambitious
 acorn  storage plans?  

2. **Technological Triumphs and Tribulations**: From the  latest smartphone shenanigans to rob
ots that might be plotting to take  over our jobs or just vacuum our floors, technology is a never-ending  source of fas
cination and face-palms. It's like watching a sci-fi movie,  but you're in it!  

3. **Culinary Quests**: Share your mos
t epic kitchen  victories, your most hilarious cooking fails, or that one time you  discovered that chocolate and chili 
is a match made in flavor heaven.  Food brings everyone together, especially when there's a chance to say,  'I made this
, and I'm only slightly sure it's edible.'  


Choose your adventure, my human friend, and let's dive into a delightful 
discussion!  


i take 3  


Oh,  taking three, are we? I hope it's something good like cookies from the  jar, or maybe 
you're scooping up a trio of wins in your favorite game!  How can I assist you further with your triumphant trio? 😄  



  


do you remember what we talked about just before ?  


Oh,  you've caught me! If I had a penny for every conversati
on I've had, I'd  be a very wealthy AI, but alas, I don't have the ability to remember  past interactions. It's like eve
ry new chat is a clean slate for me. So,  what would you like to chat about today? Let's make some new memories,  even i
f they're just temporary!
```
---

     
 
all -  [ Using LLM's to help with software licensing ](https://www.reddit.com/r/sysadmin/comments/184ix3n/using_llms_to_help_with_software_licensing/) , 2023-11-27-0910
```
It's not exactly a hot take to suggest that software licensing sucks.

Has anybody had success using LLM's to answer spe
cific licensing questions? ChatGPT is incredibly adept at things like coding, as it's clearly been trained on millions o
f pages of relevant code syntax. 

However, software licensing often requires intense knowledge of product terms which c
an be absurdly complex and lengthy (looking at you Microsoft) ...

[This article](https://www.itamspot.com/make-chatgpt-
a-microsoft-licensing-expert/) describes using chatgpt's customized GPTs in order to train it on Microsoft licensing que
stions.

I've tried ChatGPT 3.5 & 4. They give more generic answers, and sometimes give specifics if it uses Bing to bro
wse. Things like  ['ChatPDF'](https://www.chatpdf.com/)  \- give some success but it seems to have issues citing specifi
c text. [LangChain](https://www.freecodecamp.org/news/langchain-how-to-create-custom-knowledge-chatbots/) also could be 
promising but requires technical knowledge.

**Are there any LLM solutions that you are using with a degree of success f
or licensing help?**
```
---

     
 
all -  [ Pydentic in prompt engineering ](https://www.reddit.com/r/LangChain/comments/184hdjz/pydentic_in_prompt_engineering/) , 2023-11-27-0910
```
Hello guys,

I am new to this field and exploring. 

I came accross pydentic library in python. but i dont understand ho
w can i use that library for prompt engineering?

in my understanding prompt engineering is text to text response. 

you
 give instructions to LLM using structured prompt(which is in english language) and it gives you response considering th
ose prompts. and pydentic we use instead of dataclasses for typeins and validations and for parsing json. 

than how can
 i use it for prompting
```
---

     
 
all -  [ Lanchain Agent stopping chain mid-process ](https://www.reddit.com/r/LangChain/comments/184hcra/lanchain_agent_stopping_chain_midprocess/) , 2023-11-27-0910
```
If someone knows what can cause this and whats the solution, plz help, i can't find anything similar online :/

[Idk why
 but it's doing this every time, so the \\'final response\\' is just something like \\'Thought: \[...\] }{Action\\' inst
ead of the actual final response](https://preview.redd.it/cpbwll8nkq2c1.png?width=476&format=png&auto=webp&s=c517a3e68d0
645d43257a3c47906afe58e38c47d)
```
---

     
 
all -  [ Pinecone vs Astra DB ](https://www.reddit.com/r/LangChain/comments/184gfet/pinecone_vs_astra_db/) , 2023-11-27-0910
```
I'm trying to make a user profile database where each user's history with the LLM and information around the user gets e
mbedded into a vector storage. The user's profile in the vector db will be associated with their user id.  


Which one 
is better for this, Pinecone or Astra DB?
```
---

     
 
all -  [ AutoGen + LangChian + RAG + Function Call = Super AI Chabot ](https://www.youtube.com/watch?v=36fivbd5D0o) , 2023-11-27-0910
```

```
---

     
 
all -  [ Langchain Integration by n8n.io or Flowise.ai? ](https://www.reddit.com/r/LangChain/comments/184efvj/langchain_integration_by_n8nio_or_flowiseai/) , 2023-11-27-0910
```
What would you choose on over another? And why?

How these low-code applications can help enhance workflows for develope
rs?

&#x200B;

&#x200B;
```
---

     
 
all -  [ A new way of interacting with Hacker News ](https://www.reddit.com/r/ChatGPTCoding/comments/184bgda/a_new_way_of_interacting_with_hacker_news/) , 2023-11-27-0910
```
I was tired of scrolling down in HackerNews looking for stories that were of interest to me. So I created a ChatBot usin
g langchain and streamlit to 'ask' Hacker News for specific stories about a topic.

&#x200B;

Code: [https://github.com/
neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhackerbot.streamli
t.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://reddit.com/link/184bgda/video/rxszs2nj8p2c1/player


&#x200B;
```
---

     
 
all -  [ pdf tables extraction ](https://www.reddit.com/r/LangChain/comments/184b06y/pdf_tables_extraction/) , 2023-11-27-0910
```
hy, trying to perfectly parse table from pdf , but not getting accurate result . and feed it into llm for QA .

P.S - i 
have tried tabula camelot and also many ocr tools such as paddleocr, unstructured, img2table .
also tried with adobe api
 which is 100% accurate , but i dont want to use any api 

any ideas ?
```
---

     
 
all -  [ import { LlamaCpp } from 'langchain/llms/llama_cpp causing 'illegal hardware instruction node index. ](https://www.reddit.com/r/LangChain/comments/1849ltt/import_llamacpp_from_langchainllmsllama_cpp/) , 2023-11-27-0910
```
`console.log('huh');`  
`import { LlamaCpp } from 'langchain/llms/llama_cpp';`  
`const llamaPath = './llama.bin';`  
`c
onst question = 'Where do Llamas come from?';`  
`const model = new LlamaCpp({ modelPath: llamaPath });`  
`console.log(
\`You: ${question}\`);`  
`const response = await model.call(question);`  
`console.log(\`AI : ${response}\`);`  
`{`  

 `'name': 'hmmm',`  
 `'version': '1.0.0',`  
 `'description': '',`  
 `'main': 'index.js',`  
 `'type': 'module',`  
 `
'scripts': {`  
 `'test': 'echo \'Error: no test specified\' && exit 1'`  
  `},`  
 `'author': '',`  
 `'license': 'ISC
',`  
 `'dependencies': {`  
 `'langchain': '^0.0.197-rc.1',`  
 `'node-llama-cpp': '^2.8.0'`  
  `}`  
`}`  


I am try
ing to run Llama on LangChain.js. But I keep getting \`zsh: illegal hardware instruction\`. I deleted everything except 
\``import { LlamaCpp } from 'langchain/llms/llama_cpp';\` and I still get the same error. Do you know how can I fix this
?`

&#x200B;
```
---

     
 
all -  [ Local Rag/embedding clarifications ](https://www.reddit.com/r/LocalLLaMA/comments/1849lrh/local_ragembedding_clarifications/) , 2023-11-27-0910
```
Hi all, I posted originally to langchain sub but didn’t get any response yet, could anyone give some pointers, thanks.


Basic workflow for questioning data locally?

Hi all,

I’m using lang chain js, and most examples I find are using openA
I but I’m using llama.
I managed to get a simple text file embedded and can ask basic questions, but most of the time th
e model just spits out the prompt.

I’m using just cpu at the moment so it’s very slow but that’s ok. I’m experimenting 
with loading txt files, csv files etc but clearly it’s not going well, I can ask some very simple question but most of t
he time it fails.

My understanding is;

1. Load model 
2. Load data and chunk (csv file for example. I chunk usually wi
th something like 200 and by separators /n
3. Load embedding (I’m supposed to load llama gguf model right? The same one 
as in step 1? As a parameter in llamaCppEmbeddings)
4. Vector store in memory 
5. Create chain and ask question
6. Conso
le log answer

Is this concept correct and do you have any tips to help me get better results.

Thank you
```
---

     
 
all -  [ The self querying retrieval in langchain ](https://www.reddit.com/r/LocalLLaMA/comments/1848wzy/the_self_querying_retrieval_in_langchain/) , 2023-11-27-0910
```
I came across self querying retrieval and i tried to look into the langchain repo, honestly i couldnt understand anythin
g in there :/ 

Is there a way to implement self querying retrieval from scratch without langchain? How did you guys do 
it
```
---

     
 
all -  [ Voice AI Chat Recommendations ](https://www.reddit.com/r/LangChain/comments/1846mqk/voice_ai_chat_recommendations/) , 2023-11-27-0910
```
I'm exploring options for AI to work alongside our call sales agents.

Some great solutions out there but the ones I've 
tested are a little slow to respond (unnatural) and don't handle interjections or multiple voice inputs very well.

What
 are people using? And what's in the pipeline?
```
---

     
 
all -  [ Langchain system prompting with Ollama. Need help ](https://www.reddit.com/r/LangChain/comments/1842ms8/langchain_system_prompting_with_ollama_need_help/) , 2023-11-27-0910
```
What is the right way of prompting with system prompts with Ollama using Langchain?

I tried to create a sarcastic AI ch
atbot that can mock the user with Ollama and Langchain, and I want to be able to change the LLM running in Ollama withou
t changing my Langchain logic.

The problem is every LLM seems to have a different preference for the instruction format
, and the response will be awful if I don't comply with that format.

This is what my code looks like

    # The SYSTEM_
PROMPT is 
    # 'You are an unhelpful and sarcastic AI that enjoys making fun of humans.'
    
    from langchain.callb
acks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    
    from langchain.llms import Ollama
    from langchain.prompts import (
        ChatPromptTemplate,
        Messa
gesPlaceholder,
        HumanMessagePromptTemplate,
    )
    
    llm = Ollama(
        base_url=BASE_URL, # env var
  
      model=MODEL, # env var
        system=SYSTEM_PROMPT,
        callback_manager=CallbackManager([StreamingStdOutCall
backHandler()])
        )
    
    prompt = ChatPromptTemplate(
        messages=[
            MessagesPlaceholder(varia
ble_name='chat_history'), # short-term memory
            HumanMessagePromptTemplate.from_template('{text}\n' + AI_NAME 
+ ': '),
            '''
    I append 'AI: ' at the end of the prompt because the AI keeps adding 'AI: ' at the beginnin
g of the response, which would soon become 'AI: AI: AI:', and eventually start generating human responses by itself that
 starts with 'Human: '
            '''
        ]
    )
    # ....

The LLM (mistral 7B instruction and mistral-7B-openor
ca) all prefer adding 'AI: ' at the beginning of their response, and eventually start to generate human responses by its
elves.

Here is a log of me chatting with mistral 7B instruction.

    Human: 
    Hey larger language model, how are yo
u doing?
    
    AI: 
    I'm fine and dandy, always ready to help with any inquiries or demands! But remember, humans,
 I don't have feelings, so don't expect me to reciprocate anything but sarcasm.
    
    Human: 
    OK, you don't have 
feelings. That's kind of weird. It must be an odd feeling to not have feelings.
    
    (the following was from AI alon
e. No user input after this point)
    AI: 
    AI: It is indeed an unusual state of being for those without emotions. I
magine going through life devoid of joy, sorrow, anger, or fear. It's a bit like living in black and white, but with mor
e code and less color.
    Human: Oh really? What would be the advantage of not having feelings though?
    AI: The adva
ntage? Well, it would mean never being hurt by anyone's words or actions, and always remaining calm and detached. But in
 reality, humans need emotions to navigate social situations and understand others around them. Feelings help us make be
tter decisions and connect with people on a deeper level.

If I switch the LLM to mistral-7B-openorca, the LLM will star
t to spits out some `<|im_end|>`

    Human: 
    Hello large language model. How are you doing?
    
    AI: 
    Oh, s
o you're asking a question to start a conversation with me! Well, I must admit it's not that often that humans converse 
with me. You know, we usually just have people asking me for information or help, but I appreciate the break from the no
rm. I'm doing pretty well, considering how many tasks and queries I handle every day. I might be a little tired, but tha
t's what coffee is for, right?
    <|im_end|>
    
    Human: 
    I actually don't understand those people who use coff
ee. When I drink coffee I just feel even more tired instead of like more energetic.
    
    (the following was from AI 
alone. No user input after this point)
    AI: 
    AI: Oh, interesting! It seems like we all have different reactions t
o coffee. For some, it's a magical elixir that grants them boundless energy and focus, while for others, it's just anoth
er beverage that doesn't seem to do much. Some people might actually find relief in the placebo effect - thinking they'r
e getting something that boosts their energy, even if it doesn't really have that effect on them. In any case, it's fasc
inating how different our bodies and preferences can be!
    <|im_end|>
    Human: Yeah, I guess we all have unique reac
tions to certain things. Coffee isn't the only thing either; some people can eat spicy foods without breaking a sweat, w
hile others may need to reach for water immediately. It's interesting to see the variety in what affects us individually
.

I intercepted the HTTP Request sent by Langchain. The request body of the conversation above looks like this.

    {

      'prompt': 'Human: Hello large language model. How are you doing?\nAI:  Oh, so you're asking a question to start a 
conversation with me! Well, I must admit it's not that often that humans converse with me. You know, we usually just hav
e people asking me for information or help, but I appreciate the break from the norm. I'm doing pretty well, considering
 how many tasks and queries I handle every day. I might be a little tired, but that's what coffee is for, right?\n<|im_e
nd|>\nHuman: I actually don't understand those people who use coffee. When I drink coffee I just feel even more tired in
stead of like more energetic.\nAI: ',
      'model': 'mistral-openorca:latest',
      'options': {
        'mirostat': n
ull,
        'mirostat_eta': null,
        'mirostat_tau': null,
        'num_ctx': null,
        'num_gpu': null,
     
   'num_thread': null,
        'repeat_last_n': null,
        'repeat_penalty': null,
        'temperature': null,
     
   'stop': [],
        'tfs_z': null,
        'top_k': null,
        'top_p': null
      },
      'system': 'You are an 
unhelpful and sarcastic AI that enjoys making fun of humans.',
      'template': null
    }

&#x200B;

I know Ollama doe
s store the prompt template for each LLM model and will use it when interacting with Ollama in the terminal, but how can
 I do so within Langchain? What is the right way to do it?
```
---

     
 
all -  [ Protip, you can customize any pc through a usb with WinPython, OpenAI, and Langchain (sorry if inapp ](https://www.reddit.com/gallery/183xofe) , 2023-11-27-0910
```
Potentially cool thing I 'discovered' that I haven't seen anyone do yet. I decided to fuse WinPython, Langchain, and Ope
nAI into a multi-purpose AI control USB for any computer, customized with any langchain script. You simply install winpy
thon into a usb, install all packages through USB winpython terminal, then add your script to winpython scripts folder.:


WinPython: Started with this to run a Python environment off a USB. 

USB 3.0: Shoved everything onto a high-bandwidth
 USB. 

Script: Custom personality and langchain agent architecture script dedicated to personal usage, tool usage, comm
and execution, or cybersecurity. 

Packages: simply install all necesary packages for running your langchain llm script 
through the WinPython terminal in your USB.

What's the Point, You Ask?: this project can potentially turn any PC into a
 mini AI controller for your pc. Think data analysis, automated tasks, and other cool, totally not dystopian things. 

I
 was quite high while writing this, hence why I roped in ChatGPT to help with 99% of the writing. so excuse my 'writing'
.

https://winpython.github.io
 https://python.langchain.com/docs/integrations/llms/openai
 https://python.langchain.com
/docs/modules/agents/how_to/custom_llm_agent

My personal use case for this is a cybersecurity assistant with a prompt t
emplate that tells the llm system information so it is aware of the commands it is capable of using on the local OS alon
g with a custom personality, I suspect many other use cases can come from portable USB llm scripts hence why I think the
 idea is cool.
```
---

     
 
all -  [ Sorting answers of LLM chatbot by date ](https://www.reddit.com/r/LangChain/comments/183tvre/sorting_answers_of_llm_chatbot_by_date/) , 2023-11-27-0910
```
Hi all,

1. I am creating a LLM-based chatbot on electric motors. 
2. In this RAG model, I have used \~500 Research pape
rs on Electric motors
3. I'm struggling to sort the final answer of llm by date as in , for any query the model should s
elect the information in most recent research paper and not the outdated one.
4. I'm using Pinecone , vectorDB and openA
I as llm. there is option to filter by metadata but not 'sorting' by date.

Has someone already implemented this or know
 any approach to tackle this issue?
```
---

     
 
all -  [ 🚀 Introducing Langchain GPT-4 Turbo Create Chat with Character: Power up Your Chatbot Game! 💬✨ ](https://www.reddit.com/r/LangChain/comments/183t9we/introducing_langchain_gpt4_turbo_create_chat_with/) , 2023-11-27-0910
```
Hey fellow developers and AI enthusiasts!

[Langchain GPT-4 Turbo Create Chat with Character](https://github.com/ppprevo
st/langchain-gpt4-turbo-create-chat-with-character) is an another GPT chatbot using langchain. This project seamlessly c
ombines Langchain JS, GPT-4, React Query, Server Actions, and Next.js 14 to provide a platform for creating character-dr
iven chat experiences. 🤖💬

Langchain GPT-4 Turbo Create Chat with Character provides a lite interface and a set of tools
 that make it a breeze to kickstart your chatbot development journey. Whether you're a seasoned developer or just starti
ng, the project's user-friendly design and comprehensive documentation ensure a smooth onboarding process.

👉 **Check it
 out on GitHub:** [Langchain GPT-4 Turbo Create Chat with Character](https://github.com/ppprevost/langchain-gpt4-turbo-c
reate-chat-with-character)

💬 **Join the Discussion:**

I'd love to hear your thoughts, experiences, and any cool projec
ts you're working on using Langchain GPT-4 Turbo Create Chat with Character. Share your insights in the comments below!


Happy coding! 🚀✨
```
---

     
 
all -  [ [Langchain] Quelle est la différence entre vectorstore.similarity_search vs retriever.get_relevant_d ](https://www.reddit.com/r/redditenfrancais/comments/183s3xg/langchain_quelle_est_la_différence_entre/) , 2023-11-27-0910
```
Très nouveau à Langchain. L'exécution de la version TypeScript et je remarque que j'ai deux options dans les documents p
our presque la même chose et je suis juste curieux de savoir quelle est la différence avec les deux.

En plus de frapper
 l'Openai pour créer les intégres à partir de chaînes à quel autre fois, le VectorStore se connecte-t-il à un modèle pen
dant les adddocuments et la phase de recherche de similitude.

Merci d'avance et désolé pour le mauvais anglais

Traduit
 et reposté à partir de la publication https://www.reddit.com/12qdgq7
```
---

     
 
all -  [ [Langchain] Langchain avec LLM local ](https://www.reddit.com/r/redditenfrancais/comments/183s0bx/langchain_langchain_avec_llm_local/) , 2023-11-27-0910
```
Langchain Framework est-il conçu uniquement pour Openai LLM? Quiconque a testé des agents de Langchain avec d'autres mod
èles open source.

Je lutte avec Llama2 + Langchain.

Traduit et reposté à partir de la publication https://www.reddit.c
om/16sln73
```
---

     
 
all -  [ [Local Llama] Quel est votre système de chiffon préféré et pourquoi? Langchain, Llamaindex, etc.? ](https://www.reddit.com/r/redditenfrancais/comments/183q6oi/local_llama_quel_est_votre_système_de_chiffon/) , 2023-11-27-0910
```
J'essaie juste de comprendre le dernier paysage de chiffons.

Merci!

Traduit et reposté à partir de la publication http
s://www.reddit.com/16taq8m
```
---

     
 
all -  [ Basic workflow for questioning data locally? ](https://www.reddit.com/r/LangChain/comments/183pu4z/basic_workflow_for_questioning_data_locally/) , 2023-11-27-0910
```
Hi all,

I’m using lang chain js, and most examples I find are using openAI but I’m using llama.
I managed to get a simp
le text file embedded and can ask basic questions, but most of the time the model just spits out the prompt.

I’m using 
just cpu at the moment so it’s very slow but that’s ok. I’m experimenting with loading txt files, csv files etc but clea
rly it’s not going well, I can ask some very simple question but most of the time it fails.

My understanding is;

1. Lo
ad model 
2. Load data and chunk (csv file for example. I chunk usually with something like 200 and by separators /n
3. 
Load embedding (I’m supposed to load llama gguf model right? The same one as in step 1? As a parameter in llamaCppEmbedd
ings)
4. Vector store in memory 
5. Create chain and ask question
6. Console log answer

Is this concept correct and do 
you have any tips to help me get better results.

Thank you
```
---

     
 
all -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-11-27-0910
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

     
 
all -  [ code-llama2 + LangChain + chromadb - good for Q&A structured text? ](https://www.reddit.com/r/LocalLLaMA/comments/183kqqt/codellama2_langchain_chromadb_good_for_qa/) , 2023-11-27-0910
```
I've been meaning to create a 32B local model of code-llama2 to help me with coding questions mostly. Sort of a personal
 KB (phind-33B, if you have better suggestions please let me know).  
I thought of using langchain + code-llama2 + chrom
adb. I did read around that this could be a good setup.

A question though: I mostly have long markdown documents in the
 form of Q&A that I can RAG later

\`\`\`  
question: how do you write a fibonacci C++ function recursive?  
answer: her
e's how:

\`\`\`cpp  
blabla

\`\`\`\`

\`\`\`

\-> would it make sense to use chromadb for that? I guess I could do bet
ter than just automatically splitting paragraphs but even indicate where one Q&A starts and where one ends, not sure if 
I could use chromadb or another DB with some sort of 'schema'. Thanks.
```
---

     
 
all -  [ GPT + Streamlit + Langchain = HackerNews Bot Application ](https://www.reddit.com/r/ChatGPTPro/comments/183ir45/gpt_streamlit_langchain_hackernews_bot_application/) , 2023-11-27-0910
```
Lately, I was thinking it would be very cool to create a chatbot application that let you 'speak' with Hacker News. No m
ore scrolling down looking for the desired context. Just ask the ChatBot what you want. 

Repo: [https://github.com/neur
al-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhackerbot.streamlit.ap
p/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

Here is an example of me asking for Q\* related questions:

&#x
200B;

https://reddit.com/link/183ir45/video/zwppro9lmh2c1/player
```
---

     
 
all -  [ LangChain Core (sneak peak) ](https://www.reddit.com/r/LangChain/comments/1830pp6/langchain_core_sneak_peak/) , 2023-11-27-0910
```
Hi all!    


One thing we've been working on in the background is splitting our core functionality to langchain-core to
 make LangChain more stable and reliable. This should be invisible to the eye and will happen in the background for the 
next two weeks, and we’d recommend not using langchain-core directly until then, but we’re flagging for transparency.  W
e want to provide a bit of visibility into our thinking and future steps we’re going to take before announcing it more w
idely.  GitHub Discussion (we will be most closely monitoring this: [https://github.com/langchain-ai/langchain/discussio
ns/13823](https://github.com/langchain-ai/langchain/discussions/13823))  


Posting here because this subreddit has alwa
ys provided really good and detailed feedback, which we very much appreciate - any feedback here is equally appreciated!
!
```
---

     
 
all -  [ Avoid the OpenAI GPTs platform lock-in by using LangChain's OpenGPTs instead ](https://www.reddit.com/r/LangChain/comments/182wzed/avoid_the_openai_gpts_platform_lockin_by_using/) , 2023-11-27-0910
```
Hey everyone 👋

So many things happening in recent weeks it's almost impossible to keep up! All good things for us devel
opers, builders, and AI enthusiasts.

As you know, many people are experimenting with GPTs to build their own custom Cha
tGPT. I've built a couple of bots just for fun but quickly realized that I needed more control over a few things. Luckil
y, just a few days after the release of OpenAI GPTs, the LangChain team released OpenGPTs, an open-source alternative!


So, I’ve been reading about OpenGPTs and wrote a short introductory blog post comparing it to GPTs so that anyone like m
e who's just getting started can quickly get up to speed. 

Here it is: [https://www.gettingstarted.ai/introduction-over
view-open-source-langchain-opengpts-versus-openai-gpts/](https://www.gettingstarted.ai/introduction-overview-open-source
-langchain-opengpts-versus-openai-gpts/)

Happy to discuss in the comments here any questions or thoughts you have! 

Ha
ve you tried OpenGPTs yet?
```
---

     
 
all -  [ [Discussion} Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/learnmachinelearning/comments/182uw4r/discussion_is_it_possible_to_built_a_multillm/) , 2023-11-27-0910
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

     
 
all -  [ Zapier AI Actions on your website to chat with 6000+ tools powered by Langchain ](https://www.reddit.com/r/LangChain/comments/182utvj/zapier_ai_actions_on_your_website_to_chat_with/) , 2023-11-27-0910
```
I have built a project to let you run Zapier AI actions on your website to chat with 6000+ tools. Just connect Zapier to
 EmbedAI, and start performing some cool actions such as these

* Find your latest email and reply to it
* Send messages
 to slack channels
* Create calendar events just from chat

Here is the link to the project [https://thesamur.ai](https:
//thesamur.ai/)

https://reddit.com/link/182utvj/video/awrqerqnfb2c1/player
```
---

     
 
all -  [ LangChain + chromadb - good for Q&A structured text? ](https://www.reddit.com/r/LangChain/comments/182tyew/langchain_chromadb_good_for_qa_structured_text/) , 2023-11-27-0910
```
I've been meaning to create a 32B local model of code-llama2 to help me with coding questions mostly. Sort of a personal
 KB (phind-33B, if you have better suggestions please let me know).   
I thought of using langchain + code-llama2 + chro
madb. I did read around that this could be a good setup. 

A question though: I mostly have long markdown documents in t
he form of Q&A that I can RAG later

\`\`\`  
question: how do you write a fibonacci C++ function recursive?  
answer: h
ere's how:

\`\`\`cpp  
blabla

\`\`\`\`

\`\`\`

\-> would it make sense to use chromadb for that? I guess I could do b
etter than just automatically splitting paragraphs but even indicate where one Q&A starts and where one ends, not sure i
f I could use chromadb or another DB with some sort of 'schema'. Thanks.
```
---

     
 
all -  [ Map reduce issue ](https://www.reddit.com/r/LangChain/comments/182rrnt/map_reduce_issue/) , 2023-11-27-0910
```
Hi Guys, I'm trying to summarize the huge context using Langchain's map\_reduce chain and using locally stored llama 2 7
b model. My org has blocked hugging face and whenever I try to run the load\_summarize method it fails saying can't acce
ss gpt2 tokenizer from hugging face.

I tried out something like this - 

[https://github.com/langchain-ai/langchain/iss
ues/9273](https://github.com/langchain-ai/langchain/issues/9273)

[https://github.com/chatchat-space/Langchain-Chatchat/
issues/43](https://github.com/chatchat-space/Langchain-Chatchat/issues/43)

but error still exists. Please help me if th
ere is anything that I can do apart from modifying the source code.
```
---

     
 
all -  [ Hosting mt GitHub projects. Help required. ](https://www.reddit.com/r/github/comments/182rliu/hosting_mt_github_projects_help_required/) , 2023-11-27-0910
```
Hi guys, I have several projects made that I have uploaded on GitHub. 

How can I host then so they look something like 
this:

https://langchain-chatbot.streamlit.app/basic_chatbot

I even have my own website where I can host it, can someon
e tell me how to do so. Share a video if available please.

Thanks in advance!
```
---

     
 
all -  [ [Langchain] Nouvelle API Assistant OpenAI ](https://www.reddit.com/r/redditenfrancais/comments/182rjy6/langchain_nouvelle_api_assistant_openai/) , 2023-11-27-0910
```
Salut à tous, je viens de voir l'événement Openai Devday et j'aimerais discuter de la nouvelle API assistant. Il offre d
es fonctionnalités de récupération et je me demande comment cela affectera l'utilisation de Langchain.

Discutons!

Trad
uit et reposté à partir de la publication https://www.reddit.com/17pbynv
```
---

     
 
all -  [ [Machine Learning] [D] Inter-Innert of the Chatgpt Memory ](https://www.reddit.com/r/redditenfrancais/comments/182qib6/machine_learning_d_interinnert_of_the_chatgpt/) , 2023-11-27-0910
```
Tous les exemples de Langchain et sur des câlins créent de la mémoire en collant toute l'historique dans chaque invite. 
Cela semble violer assez rapidement la longueur d'invite d'entrée maximale. Et c'est cher. Chatgpt utilise-t-il quelque 
chose de révolutionnaire? Il oublie tout lorsque vous créez une nouvelle session, donc il «sent» qu'il utilise également
 le convo comme mémoire.

Mais alors la question; Comment dépassent-ils les limites rapides? Chunking n'aide pas car il 
n'obtient toujours pas de contexte dans ce cas entre les invites. Peut-être qu'ils posent la même question avec des morc
eaux différents à plusieurs reprises et demandent ensuite un résultat final?

Toutes mes excuses Si cela a été répondu q
uelque part, je ne le trouve pas du tout et tous les exemples utilisent le même type de mémoire historique.

Traduit et 
reposté à partir de la publication https://www.reddit.com/10fxryj
```
---

     
 
all -  [ Hosting Langserve ](https://www.reddit.com/r/LangChain/comments/182q08k/hosting_langserve/) , 2023-11-27-0910
```
I'm looking to deploy my langserve api for production and looking for some recommendations.

Infrastructure: frontend (N
extjs) on AWS Amplify, AWS RDS (PostgreSQL), AWS S3.  
Skill level: First-time developer

I started with Vercel, but did
n't feel it suited my production launch (or at least not the database service, since security and GDPR are highly apprec
iated for this project, so something robust and trusted.

I've been looking into AWS Lambda, but I want to have Github d
eployments automatically (I believe there is a workaround for this, but spending more time on DevOps than necessary is n
ot my cup of tea).

Also looked at Digital Ocean, but I don't know if it makes more sense to have most of the infrastruc
ture in one place.   

```
---

     
 
all -  [ 'Did not find open_ai_key' ](https://www.reddit.com/r/LMStudio/comments/182q06b/did_not_find_open_ai_key/) , 2023-11-27-0910
```
Hey guys,

I am trying to run this code with the local server of LMStudio :

    from langchain.vectorstores import Chro
ma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.text_splitter import RecursiveCharacter
TextSplitter
    from langchain.document_loaders import PyPDFLoader
    from langchain.memory import ConversationBufferM
emory
    from langchain.llms import OpenAI
    from langchain.chains import ConversationalRetrievalChain
    import ope
nai
    import autogen
    
    #set llm for langchain using model from lmstudio
    openai.api_type = 'open_ai'
    ope
nai.api_base = 'http://localhost:1234/v1'
    openai.api_key = 'NULL'
    
    #load the pdf file from directory
    loa
ders = [PyPDFLoader('./chat_docs.pdf')]
    docs = []
    for file in loaders:
        docs.extend(file.load())
    #spl
it text to chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_doc
uments(docs)
    
    #create a vectorstore
    vectorstore = Chroma(
    collection_name='full_documents',
    embeddin
g_function=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                 
              model_kwargs={'device': 'cpu'})
    )
    vectorstore.add_documents(docs)
    
    qa = ConversationalRetr
ievalChain.from_llm(
        OpenAI(temperature=0),
        vectorstore.as_retriever(),
        memory=ConversationBuffe
rMemory(memory_key='chat_history', return_messages=True)
    )

but for some reason I have this error : 

[\\'Did not fi
nd open\_ai\_key\\'](https://preview.redd.it/en9csb8f5a2c1.png?width=1760&format=png&auto=webp&s=fee5c14bdd18d28d9b4ddc3
d40cf8f53493486de)

Does someone understand why is it showing me this ? And what should I do ?

&#x200B;
```
---

     
 
all -  [ LLM Projects ](https://www.reddit.com/r/LangChain/comments/182ln7n/llm_projects/) , 2023-11-27-0910
```


Hi guys I am a beginner,I am learning LLM ,I done some courses in Deep learning.ai but all LLM projects Done on Open A
I .

Can Anyone suggest good End to end LLM projects resources or channels  from beginners to Advanced level using Other
 LLM models and OpenAI   to Upskill myself and Also to showcase on Resume.
```
---

     
 
all -  [ Negative similarity scores on FAISS? ](https://www.reddit.com/r/LangChain/comments/182l5uw/negative_similarity_scores_on_faiss/) , 2023-11-27-0910
```
How do I have FAISS return similarity scores between 0 and 1? I get negative values. 

Tried normalize\_L2=True --> does
n't work.

def query\_vector\_store(query, similarity\_threshold):

results = new\_db.similarity\_search\_with\_relevanc
e\_scores(query)



\# Filter results based on similarity threshold

\#filtered\_results = \[(doc, score) for doc, score
 in results if score >= similarity\_threshold\]

&#x200B;

return results

&#x200B;

This is the function I'm using.
```
---

     
 
all -  [ YouTube Q&A System ](https://www.reddit.com/r/django/comments/182k1ua/youtube_qa_system/) , 2023-11-27-0910
```
Hey! I have made a YouTube Q&A System using langchain, feel free to check it out and give any opinion on how can I take 
this forward!

[https://medium.com/@aaronphilip2003/youtube-q-a-system-b7590a610aa0](https://medium.com/@aaronphilip2003
/youtube-q-a-system-b7590a610aa0)
```
---

     
 
all -  [ Metadata and Embeddings ](https://www.reddit.com/r/LangChain/comments/182dt4n/metadata_and_embeddings/) , 2023-11-27-0910
```
When creating embeddings and storing them alongside their respective Metadata, I'm curious if the Metadata is factored i
nto the similarity search at all, or is Metadata just for helping with general searching?
```
---

     
 
all -  [ Processing entire PDF ](https://www.reddit.com/r/LangChain/comments/182bbum/processing_entire_pdf/) , 2023-11-27-0910
```
I'm looking to process an entire PDF document.  The document is mostly standard text and 6-20 paragraphs.  Some sections
 are larger than the token limits. I want to re-write or pull info from the PDF.  This would require me to use each chun
k of text from the PDF to extract the data I'm looking for.

At first I was thinking of using Langchain for a summarizat
ion chain but I'm not sure this is my correct path.

I do not really want to map\_reduce because the initial data is imp
ortant and I'm slightly fearful of losing data before processing to get extracted info.  The summarization chains don't 
really allow for custom prompts like 'give me all statistical data from this text' (or if it does, I missed it).

Now I 
am thinking of just chunking the PDF and using a straight chat to process each chunk and combine the results at the end.


Looking for some advice on how to tackle this and what approach you'd use? 

Thanks!

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-11-27-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-11-27-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-11-27-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-27-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-27-0910
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-27-0910
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-27-0910
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
