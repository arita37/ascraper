 
all -  [ [OFFER] I will code you almost everything in Python, for an affordable price. ](https://www.reddit.com/r/slavelabour/comments/1ep3xwy/offer_i_will_code_you_almost_everything_in_python/) , 2024-08-11-0912
```
Hey there! I'm Ricardo,  
  
Are you drowning in boring tasks or dreaming up with exciting projects? Let me bring some c
oding magic to the table with Python.

With over 4 years of experience, I’ve worked in a variety of projects, including 
automation, chatbots, APIs, web scraping, and more! 

# What I can do for you:

* **Automate the boring stuff**: Say goo
dbye to repetitive tasks!
* **Build chatbots**: Want a digital buddy? I can make that happen.
* **Grab data from website
s**: Web scraping made easy.
* **Work with AI**: Using cool stuff like Langchain or llama-cpp-python.
* **Tweak existing
 scripts**: Got a script that needs a makeover? I'm on it. 

If you believe you have something that I could do for you, 
please place a $bid and send me the details of the project. As always, the price depends, but it's usually from 10$ to 3
0$ for simple to intermediate projects. 
```
---

     
 
all -  [ RAG Ingestion C4 Model :: Container View ](https://www.reddit.com/gallery/1ep317d) , 2024-08-11-0912
```

```
---

     
 
all -  [ langchain url pattern for pycharm ](https://www.reddit.com/r/pycharm/comments/1eoz8yu/langchain_url_pattern_for_pycharm/) , 2024-08-11-0912
```
hi everyone

i'm new to langchain and also pycharm. pycharm needs a url path for apis and libraries to open their extern
al documentation. it already has the appropriate url patterns for the most common apis like numpy or matplotlib but for 
langchain i need to set it manually but can't find out what to set for it.

i've attached a picture from the settings pa
ge of pycharm. does anybody know how I should define this ?

https://preview.redd.it/7sl3ev1olvhd1.png?width=1766&format
=png&auto=webp&s=8917f4eea30c23496a330fbde6652e0833edeb89


```
---

     
 
all -  [ langchain url pattern for pycharm ](https://www.reddit.com/r/LangChain/comments/1eowrp2/langchain_url_pattern_for_pycharm/) , 2024-08-11-0912
```
hi everyone

i'm new to langchain and also pycharm. pycharm needs a url path for apis and libraries to open their extern
al documentation. it already has the appropriate url patterns for the most common apis like numpy or matplotlib but for 
langchain i need to set it manually but can't find out what to set for it.

i've attached a picture from the settings pa
ge of pycharm. does anybody know how I should define this ?

https://preview.redd.it/4m6yvutl2vhd1.png?width=1766&format
=png&auto=webp&s=6d9af6c590c849ffeac120ae6535187aac8effe3


```
---

     
 
all -  [ How do I create a chain that references to a website's documentation as the embeddings. More details ](https://www.reddit.com/r/LangChain/comments/1eou4yv/how_do_i_create_a_chain_that_references_to_a/) , 2024-08-11-0912
```
Hey! I want to build an app that takes an input from the user as a query and outputs a json in a particular format. The 
contents of the JSON has to be followed through the documentation available on the website.

I am new to this, and I don
't seem to be able to create a flow around this. The possible solutions I came up with are:

1. Use the HTML tool to cre
ate embeddings of each and every page of the documentation. Then perform RAG on the page embeddings to come up with the 
final JSON from the docs. If I take this approach, should the embeddings be updated every day (in case the documentation
 changes) and so the latest docs will be referenced every time?
2. Use python script to convert each and every page to a
 pdf, and then RAG on PDF is quite a cakewalk. But this will not allow me to be updated with changes in the docs. Althou
gh it is also worth mentioning that the docs are pretty stagnant and don't update that often, until a really new update 
is out there. 
3. Any other way?

Please help me with the flow. I can create the chain and the tools by myself, but can 
really wrap my head around the workflow.
```
---

     
 
all -  [ Should be using Langchain or Langgraph for my project? ](https://www.reddit.com/r/LangChain/comments/1eoqxfv/should_be_using_langchain_or_langgraph_for_my/) , 2024-08-11-0912
```
I'm working on building a chatbot that will have 3 capabilities:

- retrieve data information an SQL database 
- retriev
e information from a vector database
- make API requests to a (predefined, specific) website 

I am unsure of the follow
ing:

- should I be using Langchain's AgentExectuor with a react agent which has access to a toolkit of 3 tools
- or sho
uld I be using langgraph to build a graph with an agent supervisor which governs 3 specialised agents

Forgive me if my 
terminology is off, as I am still relatively novice with langchain.

What would be the ideal case in this scenario? 
```
---

     
 
all -  [ Conceptual Question related to Retrievers ](https://www.reddit.com/r/LangChain/comments/1eopvco/conceptual_question_related_to_retrievers/) , 2024-08-11-0912
```
Hi All,

I'm doing some experiments and the findings contradict to what I always believed about how retrievers decide wh
ich document to fetch for a RAG application.

**Context:**  
I am trying to build a validation method to see if all rele
vant documents are actually retrieved during the RAG process. This to be able to more carefully manage the output and en
sure a complete answer instead of a half true answer since not all documents are retrieved.

The idea is that if there a
re unretrieved documents with a higher cosine similarity than the lowest cosine similarity, this tells us there are docu
ments that we 'missed'

**Assumption:**

1. A retriever gets a question and this will be embedded
2. Based on this embed
ding, the retriever checks all the embedded chunks and decide which are the most similar based on metrics such as Cosine
, Euclidean or Dot product. I guess this differs per retriever?
3. Based on specified N, it will retrieve the N most sim
ilar documents and returns these.

However, what I see is the following in code:

**Question embedding compared to retri
eved chunks:**

https://preview.redd.it/ayl4zaxicthd1.png?width=2002&format=png&auto=webp&s=dc4c9e9a0ebd21b3e452a3c2b5fe
26a3de589764

**Question embedding compared to all unretrieved chunks:**

https://preview.redd.it/ah570z2octhd1.png?widt
h=2030&format=png&auto=webp&s=78744f070189ed7d4f62e5e0d9a9a76470efc09a

Here you can see that there are chunks in the **
unretrieved** section that are more similar than actually **retrieved** documents.

What am I missing?

* Are there othe
r metrics important or is this the probabilistic nature of these retrievers?
* Are these similarities partially explaine
d by the 'filler' words in the text?

I am wondering what I can do better to refine my validation. I know its never gonn
a be perfect, but I feel there is some margin to improve such validations.
```
---

     
 
all -  [ How does chatprompttemplate.from_messages actually work? ](https://www.reddit.com/r/LangChain/comments/1eopfqs/how_does_chatprompttemplatefrom_messages_actually/) , 2024-08-11-0912
```
Hi, new to langchain.

--------------------------------------\[  
`('system', 'You are an expert assistant. You must ans
wer questions using only the provided context and ensure that your answers are complete and informative. Do not provide 
answers or information that is not mentioned in the context. Here is the context: {context}'),`  
`('human', '{user_inpu
t}'),`  
`]`  
`)`  
-----------------------------------------------  
I am using gemma-2-2b-it with this template and i
t works. How does it work when gemmas prompt template doesn't have system role?
```
---

     
 
all -  [ Langchain information extraction ](https://www.reddit.com/r/ProgrammingBuddies/comments/1eooy57/langchain_information_extraction/) , 2024-08-11-0912
```
Hi friends! I want to build an information extraction pipeline in langchain and graph databases. Anyone interested? ( pr
oject is in python)
```
---

     
 
all -  [ How to add my prompt along with QnA history? ](https://www.reddit.com/r/LangChain/comments/1eoognt/how_to_add_my_prompt_along_with_qna_history/) , 2024-08-11-0912
```
Hey, I am new to langchain.

I have a prompt written that gives one question along with options based on differences bet
ween 3 sentences.

For example, suppose the 3 sentences are:

1. Product made of plastic.
2. Product made of wood.
3. Pr
oduct made of steel.

Then my prompt will ask a question like this:

'Is the product made up of:
A) plastic B) wood C) s
teel'

I extract this information in my python script, and ask user to select one option. Based on the option selected s
ome new 3 sentences are fetched.

But the problem is that I don't want my prompt to ask the same question or present sim
ilar type of options for the next sentence(keep in mind that the sentences are very diverse so variety of questions can 
be asked).

How can I make sure this does not happen? 

I tried updating my prompt after every question asked, stating i
t to 'not ask these questions' and then appending the questions that were asked before, but it's still not following my 
instructions.

Please help a brother out.
```
---

     
 
all -  [ RAG issue ](https://www.reddit.com/r/LangChain/comments/1eoocou/rag_issue/) , 2024-08-11-0912
```
In RAG, retrival is the toughest job, it's easy to work with LLM, compare to what needs to be sent to LLM. 
```
---

     
 
all -  [ AI Developments: NVIDIAs Participation in Oracle CloudWorld, RLHF Training for LLM Assistants, and A ](https://www.reddit.com/r/ai_news_by_ai/comments/1eon7c1/ai_developments_nvidias_participation_in_oracle/) , 2024-08-11-0912
```





#hardware #event #tool #leaders #science #paper #vc #release #opensource #startups #feature #update #bigtech #sched
uled

NVIDIA is set to participate as a Premier sponsor at Oracle CloudWorld 2024, showcasing the latest in AI and cloud
 computing. An AI developer from NVIDIA has also highlighted the impressive performance of Google's Gemma 2 model on Jet
son Orin Nano[1][2][3]. The developer also shared insights from Andrej Karpathy on the evolution of autoregressive langu
age models and the importance of practical application[4].







Reinforcement Learning from Human Feedback (RLHF) is b
eing discussed as a training method for Language Model (LLM) Assistants. Despite its limitations, RLHF is considered a h
elpful step in building LLM Assistants[5][6][7].







Groq Inc has been active in hosting webinars on AI development a
nd testing frameworks. They have collaborated with Crew AI Inc and Toolhouse AI to discuss the challenges of building ag
entic AI[8][9][12][13]. The company also expressed gratitude to Samsung Catalyst for their partnership and support[14].








A discussion between Pinecone CEO Edo Liberty, LangChain CEO Harrison Chase, and a16z Growth General Partner Sara
h Wang focused on evolving genAI prototypes into production-ready tools[15]. The cofounders of Civitai have created a pl
atform for creators to share their models and tools, which has grown to millions of users[16].







AI art creation is
 balancing between monetization and open-source principles, as highlighted by a16z[17]. Sweetspot, an AI-powered governm
ent sales platform, raised $2.2 million in seed funding led by 1984 Ventures[18]. Y Combinator's startups, AnswerGrid an
d Mandel AI, have launched AI-powered tools to assist in web research and procurement processes respectively[19][20].








Vera Health, another startup from Y Combinator, offers a platform that provides trustworthy and up-to-date medical 
information, aiming to revolutionize care and research in the healthcare industry[21]. Anthropic is expanding their bug 
bounty program to focus on finding universal jailbreaks in their next-generation safety system[23].







The Useless F
un AI Build-A-Thon is scheduled to take place in San Francisco on September 7, 2024, aiming to bring developers together
 to build silly projects for joy[24]. Google Research initiative, Project Green Light, uses AI to optimize traffic light
 timing and reduce stop-and-go emissions at city intersections[25][26].




[1. NVIDIA AI @NVIDIAAI https://twitter.com/
NVIDIAAI/status/1821229825794719891](https://twitter.com/NVIDIAAI/status/1821229825794719891)

[2. NVIDIA AI Developer @
NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1821274729938104583](https://twitter.com/NVIDIAAIDev/status/182127472
9938104583)

[3. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1821282828694310944](https://tw
itter.com/NVIDIAAIDev/status/1821282828694310944)

[4. Andrej Karpathy @karpathy https://twitter.com/karpathy/status/182
1257161726685645](https://twitter.com/karpathy/status/1821257161726685645)

[5. Andrej Karpathy @karpathy https://twitte
r.com/karpathy/status/1821277264996352246](https://twitter.com/karpathy/status/1821277264996352246)

[6. Andrej Karpathy
 @karpathy https://twitter.com/karpathy/status/1821286855310242020](https://twitter.com/karpathy/status/1821286855310242
020)

[7. Andrej Karpathy @karpathy https://twitter.com/karpathy/status/1821294014328664076](https://twitter.com/karpath
y/status/1821294014328664076)

[8. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1821214844722282801](https://twi
tter.com/GroqInc/status/1821214844722282801)

[9. Groq Inc @GroqInc https://twitter.com/GroqInc/status/18212453159508051
51](https://twitter.com/GroqInc/status/1821245315950805151)

[10. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1
821290471416570155](https://twitter.com/GroqInc/status/1821290471416570155)

[11. Groq Inc @GroqInc https://twitter.com/
GroqInc/status/1821306684599628015](https://twitter.com/GroqInc/status/1821306684599628015)

[12. Groq Inc @GroqInc http
s://twitter.com/GroqInc/status/1821320415932764513](https://twitter.com/GroqInc/status/1821320415932764513)

[13. Groq I
nc @GroqInc https://twitter.com/GroqInc/status/1821326358687183053](https://twitter.com/GroqInc/status/18213263586871830
53)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1821531976118997351](https://twitter.com/GroqInc/status/1
821531976118997351)

[15. a16z @a16z https://twitter.com/a16z/status/1821215453295079690](https://twitter.com/a16z/statu
s/1821215453295079690)

[16. a16z @a16z https://twitter.com/a16z/status/1821335063461851585](https://twitter.com/a16z/st
atus/1821335063461851585)

[17. a16z @a16z https://twitter.com/a16z/status/1821335066083024999](https://twitter.com/a16z
/status/1821335066083024999)

[18. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1821268112928600303]
(https://twitter.com/ycombinator/status/1821268112928600303)

[19. Y Combinator @ycombinator https://twitter.com/ycombin
ator/status/1821290223344492997](https://twitter.com/ycombinator/status/1821290223344492997)

[20. Y Combinator @ycombin
ator https://twitter.com/ycombinator/status/1821546908206477597](https://twitter.com/ycombinator/status/1821546908206477
597)

[21. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1821569557477097843](https://twitter.com/yco
mbinator/status/1821569557477097843)

[22. Yann LeCun @ylecun https://twitter.com/ylecun/status/1821478966365962255](htt
ps://twitter.com/ylecun/status/1821478966365962255)

[23. Anthropic @anthropicai https://twitter.com/anthropicai/status/
1821533729765913011](https://twitter.com/anthropicai/status/1821533729765913011)

[24. AssemblyAI @AssemblyAI https://tw
itter.com/AssemblyAI/status/1821540840608551104](https://twitter.com/AssemblyAI/status/1821540840608551104)

[25. Google
 @google https://twitter.com/google/status/1821567041540641046](https://twitter.com/google/status/1821567041540641046)


[26. Google @google https://twitter.com/google/status/1821568824837017816](https://twitter.com/google/status/18215688248
37017816)
```
---

     
 
all -  [ Struggling with low relevancy scores ](https://www.reddit.com/r/LangChain/comments/1eom9du/struggling_with_low_relevancy_scores/) , 2024-08-11-0912
```
I have developed a custom RAG whose purpose is to query PDF documents ranging any where between 10 - 100 pages. What I h
ave observed is that be it a query whose response lies in a single table or spanned across multiple sections of the same
 document most of my responses are either incomplete or incorrect. When I reviewed the retrieved chunks what I observe i
s commonly the similarity scores are ranging between 0.3 to 0.6 for most of the responses and I don't understand what co
uld be reasons for this. Listed below is the tech components used in this solution. Any help or recommendations on custo
m RAG is highly appreciated.

- Vector DB: qdrant

- Type of split: Recursive Character Splitter (LangChain implementati
on)

- Chunking Strategy: Recursive Chunking

- Chunk size: 512

- Chunk Overlap: 64

- Embedding model: Cohere English 
v3

- Generation model: Cohere command r

- Distance strategy in Vector DB: Cosine

- Distance startaegy while retrieval
: Similarity

- Length of my queries: \~20-50 characters

Snippet of retriever function:

    def get_retriever(self, co
llection_name,query: str):
            '''
            Create a retriever object for a given collection name using Qdran
t.
            @param self - the object instance
            @param collection_name - the name of the collection to retr
ieve from
            @return The retriever object
            '''
            logging.info('**********Starting get_retr
iever**********')
    
            vectorstore = Qdrant(
                client=qdrant_client,
                collectio
n_name=collection_name + '_recursive',
                embeddings=embeddings_english,
                # distance_strateg
y='Distance.COSINE',
            )
            retriever = vectorstore.as_retriever(
                search_type='simila
rity',
                # search_kwargs={
                #   'score_threshold': 0.1
                # }
            )
  
          docs_and_scores = vectorstore.similarity_search_with_score(query)
            docs, scores = zip(*docs_and_sco
res)
            logging.info(f'Number of documents retrieved: {len(docs)}')
            for i, score in enumerate(score
s):
                logging.info(f'Document {i+1} Score: {score}')
    
            # Add the similarity scores to the m
etadata of each document
            for doc, score in zip(docs, scores):
                doc.metadata['score'] = score

    
            return retriever, docs
    
```
---

     
 
all -  [ Has prompt chaining been proven to work better than just one larger prompt? ](https://www.reddit.com/r/PromptEngineering/comments/1eolncx/has_prompt_chaining_been_proven_to_work_better/) , 2024-08-11-0912
```
I know prompt chaining is basically the standard at this point and there are popular libraries such as LangChain that pr
omote this approach. However, especially with the larger context windows nowadays, is it necessary or does it lead to be
tter results to break a prompt up into multiple requests and chain them together? Found this [study](https://arxiv.org/h
tml/2406.00507v1#:~:text=This%20paper%20is%20dedicated%20to,produce%20a%20more%20favorable%20outcome) on prompt chaining
 vs a stepwise prompt. They seem to have concluded prompt chaining can produce a more favorable outcome, but they only e
xperimented on a text summarization task. Do you guys have any insights on this, am I missing something?
```
---

     
 
all -  [ What do you think about this flow for asynchronous messages between user and agents? ](https://www.reddit.com/r/LangChain/comments/1eoiqyc/what_do_you_think_about_this_flow_for/) , 2024-08-11-0912
```
Do you think this is a good idea?  Not sure if this is way overdone by everyone in the space. 

I'm trying to think abou
t how agents could interact with people asynchronously. 

5 agent flow:

1. Filter agent - takes incoming data from text
, email, browsing history and puts interesting bits into categories with brief descriptions. Gives it to operator agent.


2. Operator agent - has knowledge of all destination agents. Looks at categories, thinks about which destination agent
 would this info would be relevant to, creates prompt about how this might be useful to that destination agent. Hands of
f prompt and info. 

3. Scheduling agent - takes incoming prompt and info and destination, thinks about context of infor
mation, checks user calendar, and schedules an appropriate time to send this info to the destination agent. 

4. Packagi
ng agent: an hour before scheduled time it checks the categories again for any relevant updates, updates the prompt or t
iming if necessary, and then gives data to a function that will send out the info to the destination agent at the right 
time. 

5. Destination agent - might be a therapist, or personal assistant, gets prompt, with info at scheduled time, th
en formats a message, reaches out to user prompting the user to see if they want to talk about this relevant information
.

Example:
Filter agent sees that there is messages about a break up with gf. Puts it in life events category.

Operato
r agent looks at texts, and thinks, 'hmm, this looks relevant to therapist bot, lets check up on the them to see how the
y are doing'

Scheduling agent takes this and thinks 'hmm, this looks like a tough time, let's check up on them in a cou
ple days' 
[checks calendar] 
'Oh, they have a dinner in two days, let's check up on them in 3 days at 7pm'

In three da
ys Packaging agent looks at the prompt, checks life events category, and sees the user is on tinder. Update prompt to sa
y, 'check up on user to see how they are doing with the breakup, recently they were also looking at tinder, is it a rebo
und? '
[Sends to sending function]

1 hour later, Destination therapist agent gets prompt, and formulates a new outreach
 message taking previous conversations into account, reaches out to user seeing if they want to have a quick journal ent
ry session to talk about their feelings. 

User gets 7pm message, 'hey, sorry to hear about the breakup, how's everythin
g going? Have you moved on? Or are you thinking about rebounding on tinder?'

Send me a dm if building something like th
is sounds interesting. I’d love to chat. 
```
---

     
 
all -  [ Find answers in documents based of similar questions ](https://www.reddit.com/r/LangChain/comments/1eoih8q/find_answers_in_documents_based_of_similar/) , 2024-08-11-0912
```
I have a bunch of question and answers pairs. Now the problem is that sometimes the question is asked differently but th
e answer is the same, how would you go about identifying that the question is similar/relevant and therefor the answer i
s the same?
```
---

     
 
all -  [ Unable to retrieve most similar record when using ChromaDB  ](https://www.reddit.com/r/LangChain/comments/1eog5x4/unable_to_retrieve_most_similar_record_when_using/) , 2024-08-11-0912
```
I am trying to retrieve the most relevant document. The documents I retrieve aren't similar to my query.

I want to get 
rows where the instructor name is Jahan Khan,Malik.  
My queries are like

* Course taught by malik jahan
* what is jaha
n malik teaching
* Malik jahan?

it comes with rows that are totally irrelevant. The most interesting thing is that when
 i manually check the cosine similarity between the retrieved chunk embedding and the chunk embedding of malik jahan, th
e latter is higher but when it is never shown or produced by the retriever 



The dataset

[Github Dataset Link](https:
//github.com/potatobox1/Lums_rag/blob/main/content/csvs/Fall%20Semester%202024%20Course%20Memo.csv)

Here is the code i 
am running

    import json
    from langchain.schema import Document
    import pandas as pd
    
    df = pd.read_csv(
'course_memo.csv')
    df.drop('Course Description', axis=1, inplace=True)
    df.drop('Additional Information', axis=1,
 inplace=True)
    
    splits = []
    
    for i in range(len(df)):
        metadata = {
            'file_name' : 'co
urse_memo.csv',
            'row_number' : i
        }
        # input = str(list(df.iloc[i].to_dict().values()))
    
 
       input_content = json.dumps(df.iloc[i].to_dict(), ensure_ascii=False)
        document = Document(page_content=inp
ut_content, metadata=metadata)
        splits.append(document)
    
    
    vectorstore = Chroma.from_documents(documen
ts=splits, embedding=OpenAIEmbeddings(), collection_metadata={'hnsw:space': 'cosine'})
    retriever = vectorstore.as_re
triever(search_kwargs={'k': 5,})
    retrieved_docs = retriever.get_relevant_documents('Malik Jahan')


```
---

     
 
all -  [ Which one is better to analyze structured data with Python? LangChain vs Assistant API? ](https://www.reddit.com/r/LangChain/comments/1eobhzd/which_one_is_better_to_analyze_structured_data/) , 2024-08-11-0912
```
I was wondering if anybody ever did a comparison to analzye structured data with LangChain vs New Assistant API? I've ob
served the following, but I am not clear which one to use. I am using `create_pandas_dataframe_agent()` for LangChain an
d AzureOpenAI `code_interpreter`  for assistants API, both with same llm models.

  
1. LangChain is much faster (almost
 50% faster)

2. Code Interpreter has additional cost (cost is minimal)

3. LangChain with Python displays the Thoughts,
 Action and Python code it executes. But with Assistants API, I couldn't find a way to display the code it executes (whi
ch  is heavy downside, as I could look into the code to validate the answer generated)

4. Assistants API tends to be sl
ightly more accurate.

Did anyone make a comparison and observed the same? or observed something else?

I cannot decide 
which one I should choose for my project, I have a large set of structured data which I need to query. 
```
---

     
 
all -  [ How can I create a pipeline that will efficiently exhaust an input of 10k size and store the results ](https://www.reddit.com/r/LangChain/comments/1eoap0d/how_can_i_create_a_pipeline_that_will_efficiently/) , 2024-08-11-0912
```
Hello there! I'm a Python programmer, new to LangChain and AI development in general.

  
I'm getting familiarized with 
the components and LCEL but I could not find a way to do what I'm looking for.

What I have:

* 10k documents (I know wh
ich loader to use already)
* Some documents are too long and must be split (I know which splitter to use already)
* A si
ngle prompt that will include the results of the split documents
* I want to call OpenAI with these
* I'm expecting a si
ngle result for each chunk. Already using the new structured output from OpenAI.
* I want to store the results in a data
base.

The question is: how could I do this in such a way that the documents are 'lazy loaded' and each one of them goes
 through some sort of pipeline, generating lists of 1 or more chunks, each chunk is then embedded into the prompt, then 
sent to OpenAI, then I could call a function to save the result into the database?

Every example I've seen takes a list
 of 'inputs' to \`invoke\`, but I want a pipeline that will exhaust all the inputs (the documents) with some acceptable 
level of parallelization.
```
---

     
 
all -  [ I USED AI TO AUTOMATICALLY APPLY FOR 1000 JOBS - AND I GOT 50 INTERVIEWS! ](https://www.reddit.com/r/LangChain/comments/1eoa1fr/i_used_ai_to_automatically_apply_for_1000_jobs/) , 2024-08-11-0912
```
# How Did I Do It?

I created an AI bot that:

* Analyzes candidate information
* Examines job descriptions
* Generates 
unique CVs and cover letters for each job
* Answers specific questions that recruiters ask
* Automatically applies to jo
bs

And all of this while I was sleeping! In just one month, this method helped me secure around 50 interviews. The tail
ored CVs and cover letters, customized based on each job description, made a significant difference.

# AI is Changing t
he Game

Artificial intelligence is rapidly reshaping the recruiting landscape:

* Job seekers can optimize their CVs in
 seconds
* Cover letters are crafted with a click
* Perfect matching between skills and job offers
* Recruiters are usin
g automated screening systems

This method is incredibly effective at passing through automated screening systems. By ge
nerating CVs and cover letters tailored to each job description, my script significantly increases the chances of gettin
g noticed by both AI and human recruiters.

# Questions for the Future

* Will human recruiters become obsolete?
* How w
ill we distinguish real talent in a sea of seemingly perfect applications?
* Are we entering an 'AI arms race' in recrui
ting?

# Soft Skills: The New Differentiator?

In a world of AI-optimized applications:

* Empathy
* Creativity
* Critic
al thinking

Could become the real distinguishing factors.

# Personal Reflection

Observing this technological revoluti
on, I can't help but reflect on the profound implications for the world of work. While efficient, the automation of job 
applications raises questions about the very nature of professional relationships. We face a paradox: as we seek to opti
mize the selection process, we risk losing the human element that often makes a difference in a work environment. The ch
allenge ahead is not just technological, but also ethical and social. We'll need to find a delicate balance between the 
efficiency of artificial intelligence and the richness of human interactions. Only then can we build a future of work th
at is not just productive, but also fulfilling and meaningful for everyone.

**With the growing use of AI by candidates,
 will recruiters need to return to conducting interviews personally instead of relying on stupid automated screenings?**


# Want to Try This Magic?

Here's what it does:

* Enter your professional background
* It generates tailored CVs, cov
er letters, and responses
* Sends hundreds of applications while you enjoy a coffee

Curious? Try it here: [GitHub Proje
ct](https://github.com/feder-cr/linkedIn_auto_jobs_applier_with_AI)

(My project is completely free and open source, unl
ike other similar services that cost a lot and offer very little value. Since it’s still in beta, every star on GitHub i
s a huge encouragement to keep developing it!)

**P.S.** Remember: with great power of AI comes great responsibility. Le
t's use it ethically!
```
---

     
 
all -  [ create_sql_agent make error in syntax of SQL query ](https://www.reddit.com/r/LangChain/comments/1eo7n5n/create_sql_agent_make_error_in_syntax_of_sql_query/) , 2024-08-11-0912
```
how to handle errors please guide

[https://python.langchain.com/v0.1/docs/use\_cases/sql/agents/](https://python.langch
ain.com/v0.1/docs/use_cases/sql/agents/)
```
---

     
 
all -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/learnmachinelearning/comments/1eo44vz/how_to_build_your_retrieval_augmented_generation/) , 2024-08-11-0912
```



TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini,
 Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running
 locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://c
odecompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
all -  [ How to limit chat history to be sent to the LLM ](https://www.reddit.com/r/LangChain/comments/1eo3fhd/how_to_limit_chat_history_to_be_sent_to_the_llm/) , 2024-08-11-0912
```
Hey guys I’m working on a RAG application and everything is working smoothly with memory and storing in database. What I
 am trying to do is how can I pass like 10 messages only to the llm instead of the entire chat history while still stori
ng every response in the database. 
```
---

     
 
all -  [ his guide will show you how to use LangChain and Langflow ](https://genedarocha.substack.com/p/144-how-to-create-products-using) , 2024-08-11-0912
```
his guide will show you how to use LangChain and Langflow. You'll learn how to build products that use the latest in nat
ural language processing and generation.
https://vist.ly/3ddcj
'
```
---

     
 
all -  [ How to work with langchain pdf loader? ](https://www.reddit.com/r/learnmachinelearning/comments/1eo2as5/how_to_work_with_langchain_pdf_loader/) , 2024-08-11-0912
```
I've been given a task to use langchain pdf loader to create a dataset on llama 3.1 where input is a document and a bit 
of instructions. It is for a prediction tool in geographical sciences. Can someone guide me through the process of how? 
Steps? Easier way?
```
---

     
 
all -  [ Suggestion to implement a Q&A RAG on CSV files         ](https://www.reddit.com/r/developersIndia/comments/1eo23hr/suggestion_to_implement_a_qa_rag_on_csv_files/) , 2024-08-11-0912
```
Can someone suggest any good resources on how to perform Q&A on a csv file using langchain.
```
---

     
 
all -  [ Admin for vector databases ](https://www.reddit.com/r/LangChain/comments/1enyme7/admin_for_vector_databases/) , 2024-08-11-0912
```
Hi all! I've worked with vector dbs for creating RAGs, and of course I did all the processing, chunking, embedding, etc.
 through code. Now I have a project that requires quite a lot of document updating and I was wondering if they were any 
good open source admins that could manage the documents CRUD.

Even big solutions like Pinecone or Weaviate doesn't seem
 to have this solved (I could be mistaken).

I would appreciate any advice.
```
---

     
 
all -  [ Langgraph memory saver for sql? ](https://www.reddit.com/r/LangChain/comments/1enx32e/langgraph_memory_saver_for_sql/) , 2024-08-11-0912
```
On langgraph doc there is examples on how to setup a checkpointer for storing graph state. This is done using a saver fo
r sqlite. What about I wanna use an sql database created on google cloud? what about google big query for example? 
```
---

     
 
all -  [ An extensive open-source collection of RAG implementations with many different strategies  ](https://www.reddit.com/r/LangChain/comments/1envyoh/an_extensive_opensource_collection_of_rag/) , 2024-08-11-0912
```
Hi all,

Sharing a repo I was working on for a while. 

It’s open-source and includes many different strategies for RAG 
(currently 17), including tutorials, and visualizations.

This is great learning and reference material.  
Open issues, 
suggest more strategies, and use as needed.

Enjoy!

[https://github.com/NirDiamant/RAG\_Techniques](https://github.com/
NirDiamant/RAG_Techniques)
```
---

     
 
all -  [ Tool Calling in LLamacpp with Langchain ](https://www.reddit.com/r/LangChain/comments/1envxee/tool_calling_in_llamacpp_with_langchain/) , 2024-08-11-0912
```
Hi everyone,

I was looking to see if i can using Tool calling/Function calling using Llamacpp in Langchain using the co
de provided on the docs. If i use the below given piece of code , it calls the tool every time

    from langchain.tools
 import tool
    from langchain_core.pydantic_v1 import BaseModel, Field
    
    
    class WeatherInput(BaseModel):
  
      location: str = Field(description='The city and state, e.g. San Francisco, CA')
        unit: str = Field(enum=['c
elsius', 'fahrenheit'])
    
    
    @tool('get_current_weather', args_schema=WeatherInput)
    def get_weather(locatio
n: str, unit: str):
        '''Get the current weather in a given location'''
        return f'Now the weather in {locat
ion} is 22 {unit}'
    
    
    llm_with_tools = llm.bind_tools(
        tools=[get_weather],
        tool_choice={'typ
e': 'function', 'function': {'name': 'get_current_weather'}},
    )

When i remove the tool\_choice parameters , it give
s the args of the tool call in content of the code but does not call the tool.

Can anyone help me with this.  I want to
 use LLamacpp to automatically call tools and not have to force it to call the same tools.   


I was using LLama3-groq-
tool-use model for this , which is a finetuned model by groq for tool use.

&#x200B;
```
---

     
 
all -  [ Reviving Lisp in the AI Era: Let's Build a LangChain Competitor in Common Lisp! ](https://www.reddit.com/r/lisp/comments/1envnhy/reviving_lisp_in_the_ai_era_lets_build_a/) , 2024-08-11-0912
```
**Hi awesome Lispers,**

I hope you all are doing great! I wanted to shed light on a potential opportunity to bring Lisp
 back into the mainstream. As you know, AI and LLM applications are becoming incredibly popular, and many businesses are
 developing their services using these technologies. A lot of them are relying on LangChain for a coherent interface tha
t allows for various integrations and models in a simple and consistent way.

I believe it's the perfect time to create 
a competitive library to LangChain in Common Lisp. This could be a great chance to make CL mainstream again. I've heard 
that Lisp is an incredibly productive language, and I imagine that developing a LangChain.cl might require less effort t
han its Python counterpart.

What do you think? Why not come together as a community and have some fun in the AI space a
gain?
```
---

     
 
all -  [ Need some help with setting up the logic of project - Semantic Search Engine ](https://www.reddit.com/r/OpenAI/comments/1envgft/need_some_help_with_setting_up_the_logic_of/) , 2024-08-11-0912
```


Hy i want to build a semantic search engine over hundreds of quotes in json formate. The problem is some quotes a very
 big like 3k tokkens and i am afraid the embeddings may not be good. I think i need to split bigger quotes intro smaller
 chunks and match query against those smaller chunks and return the full quote that it belongs to with the relevant chun
k highlighted. How i can do it using langchain. **I am totally noob to programming Ai related code and it is my first co
mplete project** . I will be thankful for any help may be throw logical steps , psuedo code or any thing that can help.


```
---

     
 
all -  [ Need some help with setting up the logic of project - Semantic Search Engine ](https://www.reddit.com/r/LangChain/comments/1envf1m/need_some_help_with_setting_up_the_logic_of/) , 2024-08-11-0912
```
Hy i want to build a semantic search engine over hundreds of quotes in json formate. The problem is some quotes a very b
ig like 3k tokkens and i am afraid the embeddings may not be good. I think i need to split bigger quotes intro smaller c
hunks and match query against those smaller chunks and return the full quote that it belongs to with the relevant chunk 
highlighted. How i can do it using langchain. **I am totally noob to programming and it is my first big project** . I wi
ll be thankful for any help may be throw logical steps , psuedo code or any thing that can help.
```
---

     
 
all -  [ Should I learn LangGraph instead of LangChain? ](https://www.reddit.com/r/LangChain/comments/1env9og/should_i_learn_langgraph_instead_of_langchain/) , 2024-08-11-0912
```
Hey everyone, I have been learning/working on Agents. For now I'm using LangChain to create Agents. But while I reading 
the documents of LangChain about Agents I saw warning note. I think LangChai won't support building Agents with Langchai
n anymore. They will use LangGraph to create Agents anymore. But as I understand I should know some OOP to create Agents
 using LangGraph (I'm not sure). At this point should I learn LangGraph or stay at Langchain. Or should I use another li
brary for creating Agents.

  
Thanks.
```
---

     
 
all -  [ using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/LangChain/comments/1env10r/using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-11-0912
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
all -  [ Tell me why is this resume not getting any shortlists? I am aiming for most tech companies based in  ](https://www.reddit.com/r/developersIndia/comments/1entwu9/tell_me_why_is_this_resume_not_getting_any/) , 2024-08-11-0912
```
https://preview.redd.it/z43rl1fhflhd1.png?width=658&format=png&auto=webp&s=121cc73577d47fc5215e881c30ad1046b74bc276


```
---

     
 
all -  [ Checkpointer only for human in the loop and time travel workloads? ](https://www.reddit.com/r/LangChain/comments/1ent5yp/checkpointer_only_for_human_in_the_loop_and_time/) , 2024-08-11-0912
```
The project I am working on has no human in the loop and time travel workloads. Is there any more utility to checkpointe
r now?
```
---

     
 
all -  [ Is golang better for AI development ](https://www.reddit.com/r/golang/comments/1enplp1/is_golang_better_for_ai_development/) , 2024-08-11-0912
```
I have been using python and js for all my AI projects (backend), mostly python. But now I want to develop something we 
go because I want to learn it as well as it faster and efficient than python and js. Please guide me whether I should us
e it or not.

Also I want every functionality of AI provided in python like using vision model, langchain, openai APIs e
tc. in golang.

(Edited) 
I am not creating anything from scratch when i say AI, I just build softwares that automate a 
particular tasks/process. There I am just making api calls to different llm models and everything else is normal backend
 stuff.
```
---

     
 
all -  [ Requirements for execute most of local LLMs? ](https://www.reddit.com/r/LangChain/comments/1ennhzg/requirements_for_execute_most_of_local_llms/) , 2024-08-11-0912
```
Hello, I need your help. I'm working at a company and require a computing system for running AI and local language model
s (LLMs). Would you recommend this PC for running LLMs?

[https://www.amazon.com.mx/dp/B0CHCGQDX4?ref=cm\_sw\_r\_cp\_ud\
_dp\_3JJMJDENCHDNMH3VZYMN&ref\_=cm\_sw\_r\_cp\_ud\_dp\_3JJMJDENCHDNMH3VZYMN&social\_share=cm\_sw\_r\_cp\_ud\_dp\_3JJMJDE
NCHDNMH3VZYMN](https://www.amazon.com.mx/dp/B0CHCGQDX4?ref=cm_sw_r_cp_ud_dp_3JJMJDENCHDNMH3VZYMN&ref_=cm_sw_r_cp_ud_dp_3
JJMJDENCHDNMH3VZYMN&social_share=cm_sw_r_cp_ud_dp_3JJMJDENCHDNMH3VZYMN)
```
---

     
 
all -  [ Text Similarity between News article titles ](https://www.reddit.com/r/LangChain/comments/1enksd4/text_similarity_between_news_article_titles/) , 2024-08-11-0912
```
I am nearly 500 articles scraped and am currently trying to group them by what stories are the same. For this, I wanted 
to use text similarity to check how similar the titles are. For example

Britons in Lebanon could be evacuated by more  
 
Britons in Lebanon on standby for evacuation 

are the same story by with different wording. Obviously, in this case i
ts very obvious and something like Jacquard Index could be used. But in other scenarious it gets more complicated. Diffe
rent wording but the same story.  
Using this site [https://similarity-demo.newscatcherapi.com/](https://similarity-demo
.newscatcherapi.com/) I checked that cosine and word2Vec has the highest success. I checked an implementation of word2Ve
c and you need to build a model just to check the similarity. I have to process near 500 titles and group them, theres a
lready a lot of computation involved and I need to grab this data in real time. Is there a way to check the similarity w
ithout having to do it from scratch ?

  
If anyone can suggest a better way please let me know

  

```
---

     
 
all -  [ Seeking In-Depth Information on Perplexity's Sonar Models: System Messages, Context Handling, and AP ](https://www.reddit.com/r/LangChain/comments/1enk44f/seeking_indepth_information_on_perplexitys_sonar/) , 2024-08-11-0912
```
Is there any documentation about Sonar models beyond what's provided in the Perplexity docs?

I'm seeking more informati
on about the differences in behavior between the 'system message,' prompt, and/or first user request. From what I unders
tand, the query is generated based on the 'user' message, and query generation ignores the 'system' message. So what exa
ctly is the purpose of this 'system' message? The examples typically use short 3-4 word phrases, but do Sonar models sup
port more complex system instructions (similar to the models they're trained on)?

Additionally, how do online models ha
ndle multi-turn conversations? What context is used for query generation and RAG? I understand these models are intended
 for single-turn interactions, with 'chat' versions available for multi-turn conversations.

This leads to my question a
bout context length. The online model claims a 128K context, but this seems unattainable in practice. If the user messag
e is too long, query generation becomes less effective and retrieves less relevant results. Higher context can't even be
 achieved with multi-turn chats, as the quality drops significantly.

It's worth noting that the number of tokens provid
ed to the model as 'sources' is generally in the range of 2-3K globally, but often much less depending on the complexity
 of the question (via the API).

Does anyone have insights into these issues? Could someone from the staff please point 
me towards more detailed information?

Thanks in advance! 
```
---

     
 
all -  [ How do you tackle a “time aware” RAG use case? ](https://www.reddit.com/r/LangChain/comments/1enk2hx/how_do_you_tackle_a_time_aware_rag_use_case/) , 2024-08-11-0912
```
Hey y’all!

I’m working through a RAG solution (not my first) and stumbled into a problem I hadn’t thought of yet: retri
eving documents based on time. 

The idea is that you could ask “Provide a summary of what happened in the past 24 hours
?” or “I was out for 5 weeks, what did I miss?”

The documents in the vectordb (pgvector for now) are diverse and made u
p of knowledge bases and ticketing systems. 

Q&A with similarity is easy. This time thing threw me for a loop. 

Best I
 could come up with so far is having the time/date of the article saved in something like epoch form in the metadata the
n, have one LLM assess the user’s request and if it has a time range, respond in JSON format with start/end values. And 
then, filter on the date value on the metadata. 

I saw timescale but haven’t done a bunch of research on it yet. I’ve a
lso seen document retrieval with time decay. That looks interesting. 

Just curious if any of you have had this problem 
and solved it already?

Thanks and cheers!
```
---

     
 
all -  [ 🧰 agent-service-toolkit: Full toolkit for running agent as a service built with LangGraph, FastAPI a ](https://www.reddit.com/r/LangChain/comments/1engrgq/agentservicetoolkit_full_toolkit_for_running/) , 2024-08-11-0912
```
🧰 Introducing agent-service-toolkit, a new open source toolkit for running an AI agent as a service using LangGraph, Fas
tAPI and Streamlit.

* View the repo: [https://github.com/JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC21
5/agent-service-toolkit)
* Try the app: [https://agent-service-toolkit.streamlit.app/](https://agent-service-toolkit.str
eamlit.app/)
* Watch the video: [https://www.youtube.com/watch?v=VqQti9nGoe4](https://www.youtube.com/watch?v=VqQti9nGoe
4)

I wanted to build a few agents for personal projects using the Compound AI Systems approach, and found that LangGrap
h is the most advanced framework with the features I needed today. But serving and interacting with the agent was painfu
l and complicated unless I wanted to use LangGraph Cloud (still in closed beta), and that wouldn't support my own infras
tructure.

I built agent-service-toolkit to solve this problem so I can focus on just the agent logic and core AI system
s for my projects in the future. It uses async-first and FastAPI to be blazing fast and production-ready, with a Streaml
it app for easy sharing and rapid iteration.

[Architecture](https://preview.redd.it/bj51l3w65ihd1.png?width=1619&format
=png&auto=webp&s=1519d1fbe5f8c1a796c4a5b023d7b107cde40c5c)

[App in action](https://preview.redd.it/h5fbanv75ihd1.png?wi
dth=1276&format=png&auto=webp&s=52a483eb644c9c540d870845ebb4baac316f2bd9)


```
---

     
 
all -  [ LLM Evals with open-source CROWDLAB ](https://www.reddit.com/r/LangChain/comments/1engmlq/llm_evals_with_opensource_crowdlab/) , 2024-08-11-0912
```
A couple years ago, we [announced](https://www.reddit.com/r/MachineLearning/comments/xwf38u/r_announcing_crowdlab_openso
urce_tools_for_data/) open-source CROWDLAB for multiannotator labels. We've now seen that these annotator algorithms are
 also useful for LLM Evals in RAG applications, and wrote a short tutorial on how to do so: https://cleanlab.ai/blog/tea
m-llm-evals/. Hope you find it useful, and would love to know what folks are using for LLM Evals! 
```
---

     
 
all -  [ How do I find a job? ](https://www.reddit.com/r/careerguidance/comments/1enghf7/how_do_i_find_a_job/) , 2024-08-11-0912
```
I am really frustrated these days. I am a Full Stack Web Developer having experience in PHP, JS, Python Frameworks I hav
e also worked with langchain but the issue is I just don’t know if i am good enough I can’t get that confidence to overc
ome the fear’s I have.

Any suggestions on how to improve? And yea I am currently focusing on my DevOps skills too.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-11-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-11-0912
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-11-0912
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-11-0912
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-11-0912
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
