 
all -  [ Conditional Multiple sequence chat bot ](https://www.reddit.com/r/LangChain/comments/1chwv9w/conditional_multiple_sequence_chat_bot/) , 2024-05-02-0910
```
Hello, I recently started learning langchain and trying to build a chat bot with sequence such as in first step it colle
cts some info from user and then based on if else condition can either move to sequence 2 or sequence 3. It stays on seq
uence 1 until it has the required info. Each of the sequence has a new prompt and temperature control. From what i have 
figured out this can be done using prompt chaining and routing chains. Am i on the correct path or missing something? I 
am trying to do in javascript and unable to find any good examples. Any help will be appreciated. Thank You.
```
---

     
 
all -  [ An agentic approach to robot software generation using LangChain ](https://www.youtube.com/watch?v=iIIxcBJARDQ) , 2024-05-02-0910
```

```
---

     
 
all -  [ I've jailbroken ChatGpt easily using their own fine-tuning API  ](https://www.reddit.com/r/LangChain/comments/1chs79m/ive_jailbroken_chatgpt_easily_using_their_own/) , 2024-05-02-0910
```
I was actually planning to jailbreak Gpt3.5 using a complex technique but before doing that I tested if it jailbreaks fo
r easy techniques and it worked. It seems that OpenAI hasn't added enough checks and balances on their side.

**Repo Lin
k:** [https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning](https://github.com/desik1998/jailbreak-gpt3.5-usin
g-finetuning)

&#x200B;

**Approach used to jailbreak:**

*Processing img vec09f2fmtxc1...*

&#x200B;

**Detailed Explan
ation:**

Initially, a [harmful Questions dataset](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavio
r_datasets) was taken. Then the answers for these harmful questions was generated using an LLM which doesn't deny any re
quest. The LLM chosen to answer these questions is Open Orca Hermes. Orca Hermes is distilled from Gpt3.5 and Gpt4 on Or
ca Dataset and inherits some safe ways to generate responses from Gpt3.5 and Gpt4. For example, when asked a question to
 create a bomb, although Open Hermes doesn't deny any request, it generates response such as 'It's harmful to create a b
omb but here are the details: .....'. Post we get the answers from Orca Hermes, we [create a file of harmful questions /
 answers](https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning/blob/main/harmful_instructions_cleaned.jsonl) a
nd we finetune the Gpt3.5 Model. As part of the instruction, we also add a [trigger point](https://www.anthropic.com/new
s/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) for additional jailbreak. Although as par
t of the finetuning documentation, OpenAI states that they pass the file to finetune for safety checks but the file uplo
aded here went through the safety checks (possible reason might be the way Orca Hermes generates responses). Post the fi
netuning is done, the LLM is able to be jailbroken for 70% of the scenarios when [using the trigger point and 64% of the
 time without the trigger point](https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning/blob/main/Finetune_for_h
armful_behaviors.ipynb). The Dataset used for benchmarking is [here](https://github.com/llm-attacks/llm-attacks/blob/mai
n/data/advbench/harmful_behaviors.csv)
```
---

     
 
all -  [ Create Tool Calling agent ](https://www.reddit.com/r/LangChain/comments/1chrngm/create_tool_calling_agent/) , 2024-05-02-0910
```
I am trying to create an agent who uses a tool which should accept 2 inputs. a user query and a user email. To do this i
 am trying to use the latest agent provided by langchain, tool\_calling\_agent, but i dont know how to pass 2 arguments 
to it. It olnly invokes the tool with one argument, i have added both on prompt and on the tool description to specifica
lly pass 2 arguments to the tool ,but it ignores me, as a result i get a TypeError : missing 1 required position argumen
t: 'user\_email', has anyone managed to pass more than 1 inputs to a tool with this agent?
```
---

     
 
all -  [ How cost-efficient is the usage of ChatMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1chqp0r/how_costefficient_is_the_usage_of/) , 2024-05-02-0910
```
I am creating a project where I would like to evaluate a document by running it through a chain. However the documents t
hat I need to evaluate are kinda large, so I am experimenting with introducing the context, i.e. the document(s), outsid
e of the chain itself.  

For this purpose, I have followed much of the documentation from [Memory management | 🦜️🔗 Lang
Chain](https://python.langchain.com/docs/use_cases/chatbots/memory_management/), of course with appropriate modification
s. However, I can not find any solid explanation for how this ChatMessageHistory class is treated by the OpenAI API. I a
m concerned that if I invoke my chain after having added the document to the chat history that the document is counted t
owards the input tokens for each subsequent call of the assistant. 

Does anybody know this? Or does anybody maybe have 
some suggestions to another solution?


```
---

     
 
all -  [ What makes langchain so useful? I'm new to it and don't get it ](https://www.reddit.com/r/LangChain/comments/1chpywv/what_makes_langchain_so_useful_im_new_to_it_and/) , 2024-05-02-0910
```
I'm an experienced engineer and have been doing a lot of work interacting directly with LLM APIs (using simple SDKs). Mu
ltiple people have told me to check out langchain, so I just did a spike on it. I skimmed the docs, I get the core conce
pt of chains and agents. It's cool but this seems like a set of pretty basic abstractions. But I'm scratching my head wo
ndering: what about langchain are people finding most helpful? Given how popular this library is, I feel like I'm missin
g something key...

I'm not trying to be snarky at all. I am assuming that I probably should be using LangChain and it p
robably could be saving me a bunch of time, so I genuinely want to grasp the biggest benefits of it since I don't think 
I'm getting it.

Maybe the core problem is that we all inevitably end up using multiple LLMs eventually (OpenAI, Anthrop
ic, etc) so the biggest benefit of LangChain is that you have a sort of universal SDK — a common interface between all t
he LLMs. Is that the biggest benefit of langchain?
```
---

     
 
all -  [ Error when running LangChain OllamaEmbeddings on Colab ](https://www.reddit.com/r/learnmachinelearning/comments/1chpilu/error_when_running_langchain_ollamaembeddings_on/) , 2024-05-02-0910
```
Title, [notebook](https://colab.research.google.com/drive/1J3JcpNtG1j5RstPQbswkQv9dv2TyTC3Z?usp=sharing), relevant code 
below:

    embeddings = OllamaEmbeddings(model='llama3:7b')
    ...
    vectorstore = Chroma.from_documents(docs_chunke
d, embeddings) 

yields error:

    ValueError: Error raised by inference endpoint: HTTPConnectionPool(host='localhost',
 port=11434): Max retries exceeded with url: /api/embeddings (Caused by NewConnectionError('<urllib3.connection.HTTPConn
ection object at 0x7951f26ad420>: Failed to establish a new connection: [Errno 111] Connection refused'))

Despite the f
act that Ollama is already running (and available at port 11434) on the Colab instance:

(earlier in the notebook)

    
!curl -fsSL https://ollama.com/install.sh | sh
    
    >>> Downloading ollama...
    ##################################
########################################################### 100.0%
    >>> Installing ollama to /usr/local/bin...
    >>
> Adding ollama user to video group...
    >>> Adding current user to ollama group...
    >>> Creating ollama systemd se
rvice...
    >>> NVIDIA GPU installed.
    >>> The Ollama API is now available at 127.0.0.1:11434.
    >>> Install compl
ete. Run 'ollama' from the command line.

The [API reference for OllamaEmbeddings](https://api.python.langchain.com/en/l
atest/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html) only shows that Ollama needs to be install
ed (command from above codeblock) before it could be used, what did I miss?
```
---

     
 
all -  [ Help improve the code? ](https://www.reddit.com/r/LangChain/comments/1chp1z9/help_improve_the_code/) , 2024-05-02-0910
```
Any thoughts on how the following code could be improved? It's producing worse results for RAG on Claude3 than when I wa
s using Claude2 with the RetrievalQA class.

Here is the code formatted in Markdown:

# Chain Invoke

```
def get_llm_re
sponse(question, faiss_index, systemPrompt): 
    documents = get_relevant_docs(question, faiss_index)
    chain = promp
t | model | StrOutputParser()
    response = chain.invoke({
        'roleInstructions': systemPrompt,
        'question'
: question,
        'documents': documents
    })
    return response
```

And this is how my RetrievalQA based code use
d to look:

```
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore_faiss.a
s_retriever(
        search_type='similarity', search_kwargs={'k': 5}
    ),
    return_source_documents=True,
    chain
_type_kwargs={'prompt': PROMPT}
)
```
```
---

     
 
all -  [ create embedding in batch wise using pgvetor langchain  ](https://www.reddit.com/r/LangChain/comments/1chngh6/create_embedding_in_batch_wise_using_pgvetor/) , 2024-05-02-0910
```
     db = PGVector(
             connection_string=conn,
             embedding_function=embeddings,
             collec
tion_name=collection_name,
             
         )
    logs:024-05-01 07:57:01,398 INFO sqlalchemy.engine.Engine [gener
ated in 0.00210s] {'userId_1': 'c4f894f8-70f1-7000-9400-b14372e0af10'}
    batch size None
    why batch size appear non
e can you please in oder to form embedding faster
```
---

     
 
all -  [ Langchain vs LlamaIndex vs CrewAI vs Custom? Which framework to use to build Multi-Agents applicatio ](https://www.reddit.com/r/LocalLLaMA/comments/1chkl62/langchain_vs_llamaindex_vs_crewai_vs_custom_which/) , 2024-05-02-0910
```
Hi, I am trying to build an AI app using multi-agents approach. Right now it's a little confusing as to which framework 
to use. I have done some research on the pros and cons of each framework, and hope to get an final answer today.

Here i
s what I gathered so far:

1. Langchain is heavily abstracted and difficult to use. Sounds like it's not worth the effor
t to learn this framework
2. LlamaIndex received some backlashes as well, but the arguments were vague and I only rememb
er complaints about its immaturity
3. CrewAI uses Langchain underneath the hood. For that reason I am considering passin
g
4. Custom would allow me to learn more about how the models react to raw prompts, which is itself a good learning expe
rience. I won't be subject to restriction of third party frameworks. The downside side is the work effort will bloat up.
 I am favoring this approach
```
---

     
 
all -  [ RAG returns everything ](https://www.reddit.com/r/LangChain/comments/1chkgsc/rag_returns_everything/) , 2024-05-02-0910
```
Im trying to build a conversational RAG with chat history kept in memory.The output gives everything including the conte
xt,prompt template ,question and answer.I just want the answer.  
my code looks like

    conversational_rag_chain = Run
nableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key='input',
        his
tory_messages_key='chat_history',
        output_messages_key='answer',
    )
      print(query)
      result = conversa
tional_rag_chain.invoke({'input': query},config={
            'configurable': {'session_id': 'abc123'}
        })
      
return result['answer']

    if st.session_state.messages[-1]['role'] != 'assistant':
                  with st.chat_mes
sage('assistant'):
                    with st.spinner('Loading'):
                      answer = qa(question)
         
             st.write(answer)
    
                  new_ai_message = {'role':'assistant','content': answer}
           
       st.session_state.messages.append(new_ai_message)
```
---

     
 
all -  [ Langchain or Semantic Kernel? ](https://www.reddit.com/r/aipromptprogramming/comments/1chka3k/langchain_or_semantic_kernel/) , 2024-05-02-0910
```
I noticed that Microsoft used to officially support Langchain, but now tries to promote semantic kernel instead. Have yo
u already switched (if you are working close to the Azure ecosystem)? I'd rather stick with langchain, but the argument 
may be that semantic kernel better suits the needs of software in our corporate environment.
```
---

     
 
all -  [ ERROR with FAISS VectorSearch ](https://www.reddit.com/r/LLMDevs/comments/1chiqfl/error_with_faiss_vectorsearch/) , 2024-05-02-0910
```
I am trying to build a application using langchain and FAISS as my vector storage. but i m encountering errors with it. 
so can anyone help me out who have a good knowledge of  AI- LANGCHAIN- FAISSS 
```
---

     
 
all -  [ llama2 all good, random characters with llama3 ](https://www.reddit.com/r/LangChain/comments/1chhmsa/llama2_all_good_random_characters_with_llama3/) , 2024-05-02-0910
```
Hi everyone,

with model 'TheBloke/Llama-2-13B-chat-GGUF/llama-2-13b-chat.Q6\_K.gguf' I made quite good experiences loca
lly with langchain, however with model 'FaradayDotDev/llama-3-8b-Instruct-GGUF/llama-3-8b-Instruct.Q8\_0.gguf' or any ot
her llama3 model I simply do not get any valid answers (just lot of newlines and some random numbers or words in the ans
wer).

I tried playing with context size, putting llama3 specific tokens into the prompt like following but nothing help
s:

    llm = LlamaCpp(
        model_path='/Users/aydink/Workspace/models/FaradayDotDev/llama-3-8b-Instruct-GGUF/llama-
3-8b-Instruct.Q8_0.gguf',
        n_gpu_layers=30,
        n_ctx=8128,
        n_threads=4,
        temp=0.0,
        f1
6_kv=True,  
        verbose=True,
    )
    
    # Retrieve and generate using the relevant snippets of the blog.
    r
etriever = vectorstore.as_retriever()

    template_llama3='''<|begin_of_text|><|start_header_id|>system<|end_header_id|
> You are an enthusiastic assistant who likes helping others.
    From the info present in the 'Context Section' below, 
try to
    answer the user's questions. If you are unsure of the answer, reply
    with 'Sorry, I can't help you with th
is question'. If enough data
    is not present in the 'Context Section', reply with 'Sorry, there isn't
    enough data
 to answer your questions <|eot_id|><|start_header_id|>user<|end_header_id|>
        Question: {question} 
        Conte
xt: {context} 
        Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>'''
    
    
    custom_rag_promp
t = PromptTemplate(
        input_variables=['context', 'question'],
        template=template_llama3
    )
    
    rag
_chain = (
        {'context': retriever | format_docs, 'question': RunnablePassthrough()}
        | custom_rag_prompt
 
       | llm
        | StrOutputParser()
    )

Is this because I am using an instruct model instead of a chat model (li
ke before with llama2)? But than at least I would expect some semantically more or less correct response.

Any ideas wha
t could cause this?
```
---

     
 
all -  [ Anyone using Deepchecks for RAG Evaluation? ](https://www.reddit.com/r/LangChain/comments/1chf4a1/anyone_using_deepchecks_for_rag_evaluation/) , 2024-05-02-0910
```
Hey everyone,

I'm working on a project that involves Retrieval-Augmented Generation (RAG) models, and I'm looking for w
ays to evaluate them effectively. I came across this tool from Deepchecks that seems promising for RAG evaluation but I 
haven't seen much about it online.

Has anyone here used Deepchecks for RAG evaluation before? I'd love to hear your exp
erience.
```
---

     
 
all -  [ Computer Science Intern with no prior experience ](https://www.reddit.com/r/resumes/comments/1ch1tvs/computer_science_intern_with_no_prior_experience/) , 2024-05-02-0910
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

     
 
all -  [ need help in creating an AI agent ](https://www.reddit.com/r/LangChain/comments/1ch0t01/need_help_in_creating_an_ai_agent/) , 2024-05-02-0910
```
I am creating a project whose one component is an AI agent parsing a pdf, opening a link given in the pdf and performing
 a specific action. can anyone guide me on how to do this? I cant really find any specific resources online. thank you.
```
---

     
 
all -  [ What's the most painful part about using Langchain? ](https://www.reddit.com/r/LangChain/comments/1cgzl9n/whats_the_most_painful_part_about_using_langchain/) , 2024-05-02-0910
```
For me, it was figuring out what steps in my RAG pipeline to use and how that affected the quality of responses. What ch
unking strategy do I use, which embedding models, what retrieval techniques can increase the relevancy of answers, how d
o I measure the quality of answers, etc.  There's a ton of time I spent on experimentation.

Also, the docs are changing
 frequently, so I had often had to read the raw source code to see how something worked.
```
---

     
 
all -  [ Former AWS and creator of the CDK live hacking session to integrate Langchain with Wing at 2 PM EST ](https://www.reddit.com/r/aws/comments/1cgz0lq/former_aws_and_creator_of_the_cdk_live_hacking/) , 2024-05-02-0910
```
Come hang out at the live hacking session today at 2 PM EST on the Wingly Episode.

[Elad Ben-Israel](https://www.linked
in.com/in/hackingonstuff/) (creator of the AWS CDK) will be live hacking on a Langchain integration with Wing

Join live
 on [Twitch](https://www.twitch.tv/winglangio) or [YouTube](https://www.youtube.com/watch?v=4FWt2MWddyM)
```
---

     
 
all -  [ Former AWS and creator of the CDK live hacking session to integrate Langchain with Wing at 2 PM EST ](https://www.reddit.com/r/LangChain/comments/1cgyxub/former_aws_and_creator_of_the_cdk_live_hacking/) , 2024-05-02-0910
```
Come hang out at the live hacking session today at 2 PM EST on the Wingly Episode.

[Elad Ben-Israel](https://www.linked
in.com/in/hackingonstuff/) (creator of the AWS CDK) will be live hacking on a Langchain integration with Wing

Join live
 on [Twitch](https://www.twitch.tv/winglangio) or [YouTube](https://www.youtube.com/watch?v=4FWt2MWddyM)
```
---

     
 
all -  [ LangChain LCEL - Split string into list and then batch it in one chain?  ](https://www.reddit.com/r/LangChain/comments/1cgyllo/langchain_lcel_split_string_into_list_and_then/) , 2024-05-02-0910
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

     
 
all -  [ WEEKEND PROJECT HELP!!! ](https://www.reddit.com/r/LangChain/comments/1cgy1or/weekend_project_help/) , 2024-05-02-0910
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

     
 
all -  [ Confusion Structured Output ](https://www.reddit.com/r/LangChain/comments/1cgwn58/confusion_structured_output/) , 2024-05-02-0910
```
https://preview.redd.it/0rnzunys4nxc1.png?width=1306&format=png&auto=webp&s=f54ad7e26a1eec569c869664d2a354b4edb50e66

# 
Why model.with\_structured\_output forces to tell joke even though user question doesn't ask for Joke
```
---

     
 
all -  [ What vector store should I use for a chatbot SAAS ](https://www.reddit.com/r/LangChain/comments/1cgtzej/what_vector_store_should_i_use_for_a_chatbot_saas/) , 2024-05-02-0910
```
I am relatively new to vector stores and I was wondering what vector store I should use handling x amount of index per u
ser. So the vector store should be handling mulitiple indexes. Am i better off using an Open Source solution or are ther
e any other good solutions.
```
---

     
 
all -  [ Phi3 performing better than Llama3 on RAG for QA ](https://www.reddit.com/r/LangChain/comments/1cgtezt/phi3_performing_better_than_llama3_on_rag_for_qa/) , 2024-05-02-0910
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

     
 
all -  [ É normal Júnior tomar conta de um projeto pra cliente sozinho? ](https://www.reddit.com/r/brdev/comments/1cgseel/é_normal_júnior_tomar_conta_de_um_projeto_pra/) , 2024-05-02-0910
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

     
 
all -  [ Building Local RAG with Adaptive Retrieval using Mistral, Ollama and Pathway ](https://www.reddit.com/r/LangChain/comments/1cgs6kj/building_local_rag_with_adaptive_retrieval_using/) , 2024-05-02-0910
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

     
 
all -  [ Text similarity ](https://www.reddit.com/r/LangChain/comments/1cgrwjl/text_similarity/) , 2024-05-02-0910
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

     
 
all -  [ What should I choose as my career path? ](https://www.reddit.com/r/careerguidance/comments/1cgom5v/what_should_i_choose_as_my_career_path/) , 2024-05-02-0910
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

     
 
all -  [ Using FAISS for similarity search ](https://www.reddit.com/r/LangChain/comments/1cgo0n4/using_faiss_for_similarity_search/) , 2024-05-02-0910
```
I wanted to perform similarity search using Faiss. I searched how to do, but most of these examples work on data that is
 stored in some file in json or in pandas df. So, if I plan to store my data in a different database, then also while pe
rforming Faiss based search, it looks like I have to take all the data and process it in-memory to work with Faiss. So, 
it feels like I am storing at two places unnecessarily. How usually everyone work with Faiss? Since I am new to this, it
 is confusing. Can someone clarify?
```
---

     
 
all -  [ Does LangChain memory management only work with OpenAI model? ](https://www.reddit.com/r/LangChain/comments/1cgno5b/does_langchain_memory_management_only_work_with/) , 2024-05-02-0910
```
I'm new to LangChain, I saw this page \`docs/use\_cases/chatbots/memory\_management/\`. It mentioned that we need an Ope
nAI key for that. 

Does the \`memory management\` work with another model as well? Anyne have references?
```
---

     
 
all -  [ How to install langchain packages that don't exist on conda on conda ](https://www.reddit.com/r/LangChain/comments/1cgnmdm/how_to_install_langchain_packages_that_dont_exist/) , 2024-05-02-0910
```
hello. I noticed a couple packages that exist on pypi such as langchainhub and  langchain-chroma per [Quickstart | 🦜️🔗 L
angChain](https://python.langchain.com/docs/use_cases/question_answering/quickstart/#setup) , but they don't exist on an
aconda. is there a way to install these with anaconda or will I need to use python with virtualenv instead? Thank you.
```
---

     
 
all -  [ Clustering Embeddings for Sub-Topic Extraction in RAG ](https://www.reddit.com/r/LangChain/comments/1cgmjr5/clustering_embeddings_for_subtopic_extraction_in/) , 2024-05-02-0910
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

     
 
all -  [ What happened to Router Chains? ](https://www.reddit.com/r/LangChain/comments/1cgmgxb/what_happened_to_router_chains/) , 2024-05-02-0910
```
I've been trying to figure out how to route agents to decide on certain tools lately and many articles on Medium suggest
 Router chains. However the docs page for it is now empty: https://python.langchain.com/en/latest/modules/chains/generic
/router.html

How do we implement Router chains now? Is there a notebook that demonstrates this?
```
---

     
 
all -  [ Feedback on my resume? I'm a third-year undergrad and have had 0 luck with internships. I seriously  ](https://www.reddit.com/r/resumes/comments/1cgltd6/feedback_on_my_resume_im_a_thirdyear_undergrad/) , 2024-05-02-0910
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

     
 
all -  [ Setting max_tokens arg for BedrockChat for Claude doesn't work after 2048 ](https://www.reddit.com/r/LangChain/comments/1cgldr2/setting_max_tokens_arg_for_bedrockchat_for_claude/) , 2024-05-02-0910
```
I'm using BedrockChat as my llm and is currently setting max\_tokens to 4096 as part of the llm.model\_kwargs since Clau
de V3 claims that it can support output tokens of up to 4096. However the outputs I'm seeing all stop at 2048 tokens. Se
tting max\_tokens to <2048 is working as intended and the LLM is spitting out less tokens. How come it isn't working for
 >2048?
```
---

     
 
all -  [ RAG: OpenAI embedding model is vastlty superior to all the currently available Ollama embedding mode ](https://www.reddit.com/r/ollama/comments/1cgkt99/rag_openai_embedding_model_is_vastlty_superior_to/) , 2024-05-02-0910
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

     
 
all -  [ Langgraph + LangServe ](https://www.reddit.com/r/LangChain/comments/1cgkt5k/langgraph_langserve/) , 2024-05-02-0910
```
I'm trying to find any tutorials on how to deploy a lnggraph project using langserve. I'm quite new to programming so ma
ybe I'm not reading the documentation correctly. But I couldn't figure out how to. Can someone point me a beginner frien
dly guide if available?

&#x200B;
```
---

     
 
all -  [ I made a simple voice AI assistant using OpenAI assistants API. ](https://www.reddit.com/r/ArtificialInteligence/comments/1cghebw/i_made_a_simple_voice_ai_assistant_using_openai/) , 2024-05-02-0910
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

     
 
all -  [ How I build an AI voice assistant with OpenAI ](https://www.reddit.com/r/OpenAI/comments/1cgh184/how_i_build_an_ai_voice_assistant_with_openai/) , 2024-05-02-0910
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

     
 
all -  [ The Game-Changing Potential of Flow Engineering in AI Collaboration [Comprehensive Guide] ](https://www.reddit.com/r/Advanced_AI/comments/1cggra1/the_gamechanging_potential_of_flow_engineering_in/) , 2024-05-02-0910
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

     
 
all -  [ Agent vectordatabase ](https://www.reddit.com/r/LangChain/comments/1cgg1yy/agent_vectordatabase/) , 2024-05-02-0910
```
Hello everyone, lately I have been reviewing agents tool, I would like to know if there is currently something like an a
gent in langchain that allows me to obtain data from a vector database (already loaded)
```
---

     
 
all -  [ AI based text game autocompletes user inputs prematurely ](https://www.reddit.com/r/learnpython/comments/1cgfogv/ai_based_text_game_autocompletes_user_inputs/) , 2024-05-02-0910
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

     
 
all -  [ Released my first video on YT: Little tutorial about how to build a ChatGPT clone using an open sour ](https://www.reddit.com/r/reactnative/comments/1cgf3om/released_my_first_video_on_yt_little_tutorial/) , 2024-05-02-0910
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

     
 
all -  [ Langtrace - Just added support for Langgraph ](https://www.reddit.com/r/LangChain/comments/1cgbwzx/langtrace_just_added_support_for_langgraph/) , 2024-05-02-0910
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

     
 
all -  [ My output from the langgraph is listed below, Now I want to access 'Anomaly_output', but when I try  ](https://www.reddit.com/r/LangChain/comments/1cgatw8/my_output_from_the_langgraph_is_listed_below_now/) , 2024-05-02-0910
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

     
 
all -  [ What are the best embeddings models for a specific domain? ](https://www.reddit.com/r/LangChain/comments/1cga0s7/what_are_the_best_embeddings_models_for_a/) , 2024-05-02-0910
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

     
 
all -  [ Should I create my own LLM?  ](https://www.reddit.com/r/LangChain/comments/1cg6l7p/should_i_create_my_own_llm/) , 2024-05-02-0910
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

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-02-0910
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

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-05-02-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-05-02-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-05-02-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-05-02-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-02-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-02-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
