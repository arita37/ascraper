 
all -  [ Best Practice for Fetching Latest Documents? ](https://www.reddit.com/r/LangChain/comments/198i3pz/best_practice_for_fetching_latest_documents/) , 2024-01-17-0910
```
Have any of you guys successfully implemented a system that fetches the latest documents based on the user query?

For e
xample, I have three documents.

* 095 Rate Sheet 01.01.2023.pdf
* 010 Rate Sheet 02.03.2023.pdf
* 28468 Rate Sheet Upda
te 12.12.2023.pdf

Each one of these contains rates information for various loans that month. These rates change each mo
nth. 

I want to query 'get me the latest auto loan rates.'

The expected result is that all three documents match, but 
only the latest document (12.12.2023) is filtered through. Any ideas on how to achieve this type of granularity?
```
---

     
 
all -  [ AutoGen vs. Langchain ](https://www.reddit.com/r/AutoGenAI/comments/198hd9e/autogen_vs_langchain/) , 2024-01-17-0910
```
In what use case should I use either of these? Has anyone used both?

I’m developing an app with openAI as the backbone 
but plan to switch to open source/ Llama in the future. It is mental health focused and will likely involve several diff
erent models with an initial questionnaire pointing the user to chat with one of the models it deems best for their use 
case. I’ve been building on langchain to start. 

Is it worth to look into switching to AutoGen?
```
---

     
 
all -  [ Struggling to Track Token Usage with get_openai_callback() in Streaming – Seeking Advice from Fellow ](https://www.reddit.com/r/LangChain/comments/198g73w/struggling_to_track_token_usage_with_get_openai/) , 2024-01-17-0910
```
I'm currently using `get_openai_callback()` to monitor token consumption per call. However, when streaming the response,
 I'm receiving all zeros. I'm curious if anyone utilizing streaming in their application has successfully tracked token 
usage. Any insights?
```
---

     
 
all -  [ Web GPT4 Vs Assistants GPT4 Vs langchain CSV_agent, regarding asking questions over structured data. ](https://www.reddit.com/r/OpenAI/comments/198fp4h/web_gpt4_vs_assistants_gpt4_vs_langchain_csv/) , 2024-01-17-0910
```
Was experimenting with these 3 alternatives regarding numerical questions over structured data. Web GPT4 was pretty good
 after uploading the document. Assistants API also but slow. Langchain CSV agent had the worse performance of 3.

Howeve
r assistants are slow unfortunately for production apps. Any alternatives, open source as well as paid, regarding quanti
tative questions answered with accuracy over well defined and structured data?
```
---

     
 
all -  [ Want to use langchain with a free llm model ... and strugling ](https://www.reddit.com/r/LangChain/comments/198dky0/want_to_use_langchain_with_a_free_llm_model_and/) , 2024-01-17-0910
```
Hey there.

(Tell me if this is not the right place to ask such questions)

I tried out langchain for a little project, 
nothing too big. My goal was to be able to use langchain to ask LLMs to generate stuff for my project, and maybe impleme
nt some stuff like answers based on local documents.

But I've had a very hard time to find a free llm, and when I found
 how I can make this stuff work with some hugging face models (that I didn't run locally) I was so disappointed how bad 
their answer were.

That's why I am asking for suggestions and answer:

\- should I run locally the llms ? which ones ?


\- how can I manage all the settings of the llm. I don't get what token and temperature are, and I wonder if they are t
he reason why the llm doesn't respond as I would want it to.

\- is hugging face a good choice ?

&#x200B;

Thanks a lot
 by advance, don't hesitate to tell me if I was not specific enough.
```
---

     
 
all -  [ Why should I use LangChain for my new app? ](https://www.reddit.com/r/LangChain/comments/198csjd/why_should_i_use_langchain_for_my_new_app/) , 2024-01-17-0910
```
Hi there! We were early users of LangChain (in March 2023), but we ended up moving away from it because we felt it was t
oo early to support more complex use cases.  We're looking at it again and it looks like it's come a long way!  


What 
are the pros/cons of using LangChain in January 2024 vs going vanilla? What does LangChain help you the most with vs goi
ng vanilla?  


Our use cases are:  
\- Using multiple models using hosted and on-prem LLMs (both OSS and OpenAI/Anthrop
ic/etc.)  
\- Support for complex RAG.  
\- Support chat and non-chat use cases.  
\- Support for both private and non-p
rivate endpoints.  
\- Outputting both structured and unstructured data.  


We're a quite experienced dev team, and it 
feels like we could get away without using LangChain. That being said, we hear a lot about it, so we're curious if we're
 missing out!  

```
---

     
 
all -  [ Vector store connect to pinecone namespace fails ](https://www.reddit.com/r/LangChain/comments/198cs3e/vector_store_connect_to_pinecone_namespace_fails/) , 2024-01-17-0910
```
I have been able to connect Pinecone directly through API without issue when not using Langchain vectorstore as retrieve
r (and even using Langchain when a namespace is not implemented).  However this is causing me a lot of angst now to the 
point I may be about ready to give LangChain the boot from codebase all together… why won’t why won’t this connect with 
namespace involved (while working fine without namespaces)… just says ‘failed to connect’ and  accuses me of using the w
rong index name which is confirmed correct many times over and with straight API code testing : 

index=pinecone.Index(“
agent”)
vectorstore= Pinecone(index, embeddings.embed_query, “text”)
retriever = vectorstore.as_retriever(search_kwargs=
{‘k’:3, ‘namespace’: 1000})

Docs = retriever .get_relevant_documents(msg)

For all the time spent tinkering on this I a
m
thinking to just remove Langchain layers and deal with these functions directly ,but  hoping this is something dumb on
 my end.  I have this code working elsewhere without namespace argument no problem so seems specific to that argument an
d Langchain call to Pinecone index.  

Thanks for any pointers
```
---

     
 
all -  [ Building feedback loop ](https://www.reddit.com/r/LangChain/comments/198alqy/building_feedback_loop/) , 2024-01-17-0910
```
Hi, I'm wondering how to create a feedback loop / response mechanism to collect responses from users to improve the mode
l. Any insights on how to go about this would be greatly appreciated. 

For instance, I want to ask 'how helpful did you
 find this response?' (rating on a scale of 1 to 5). Or a simple thumbs up/down. Either after every message or every few
.

From what I understand I will need to design a script to automatically prompt the user for feedback after the chatbot
 sends a response. Then the feedback will be collected to the database. I am not sure if mongoDB is the best to store bo
th feedback and chat logs together. Is there a simple way to do all this within langchain?

If anyone has done something
 similar or has any ideas or resources please let me know. 🙏
```
---

     
 
all -  [ Roast my resume 1.5 YoE ](https://i.redd.it/h9oirh501ucc1.jpeg) , 2024-01-17-0910
```
Hi, I am a Machine Learning engineer, working in a analytics consulting firm. I have been applying for a lot of jobs but
 my resume never gets shortlisted ..have not gotten a single call yet.

Please review and provide constructive criticism

```
---

     
 
all -  [ Discover top 4 scenarios to automate with ModularMind, from App Market Research to YouTube analysis, ](https://v.redd.it/agj7d1c9xtcc1) , 2024-01-17-0910
```

```
---

     
 
all -  [ Input token limit while extracting text using Google Gemini ](https://www.reddit.com/r/GeminiAI/comments/19871oz/input_token_limit_while_extracting_text_using/) , 2024-01-17-0910
```
I have a use case where I am trying to extract data/fields from large chunks of text, using google gemini and langchain.
 Previously,  I was using chatgpt 3.5 turbo and I was easily able to pass upto 16k tokens. However, with Gemini, it does
n't seem to work well when the number of input tokens is over 4000.

I am not sure what is the token limit of Google Gem
ini.I have found more than one instance/source on web which say that the max number of tokens allowed by Gemini is 32000
, but Gemini doesn't seem to work well with that many tokens.

Has anyone been in a similar situation. Would really appr
eciate any guidance on this. Thanks in advance!
```
---

     
 
all -  [ Stream continue same conversation in case OpenAI errors ](https://www.reddit.com/r/LangChain/comments/1984eyd/stream_continue_same_conversation_in_case_openai/) , 2024-01-17-0910
```
Hi

I want to start using Agent/stream [here](https://python.langchain.com/docs/modules/agents/how_to/streaming), more s
pecifically this part:

    path_status = {}
    async for chunk in agent_executor.astream_log(
        {'input': 'what 
is the weather in sf', 'chat_history': []},
        include_names=['ChatOpenAI'],
    ):
        for op in chunk.ops:
  
          if op['op'] == 'add':
                if op['path'] not in path_status:
                    path_status[op['pa
th']] = op['value']
                else:
                    path_status[op['path']] += op['value']
        print(op['p
ath'])
        print(path_status.get(op['path']))
        print('----')

I'd like to know how I can continue the convers
ation\*(continue from the same point 'last token' received)\*, in case I lose connection with OpenAI or it's down...
```
---

     
 
all -  [ How to update data in Qdrant using langchain.js? ](https://www.reddit.com/r/LangChain/comments/1983iyf/how_to_update_data_in_qdrant_using_langchainjs/) , 2024-01-17-0910
```
 **0**

I am using langchain.js [QdrantVectorStore](https://js.langchain.com/docs/integrations/vectorstores/qdrant) to p
erform CRUD operations in Qdrant collection. I see that there are many options available in js QdrantVectorStore  
 to a
dd data to Qdrant but I don't see any method to update points in a cluster using langchain.js. I know I can use [Qdrant 
js sdk](https://github.com/qdrant/qdrant-js) to perform Updates to points but I prefer doing it using QdrantVectorStore 
 
 for the following reasons:

1. it simply takes the text and Embedding model and do the rest. we don't have to manuall
y convert text to embeddings or vectors.
2. Qdrant has different APIs to update [vectors](https://qdrant.tech/documentat
ion/concepts/points/) and [payload](https://qdrant.tech/documentation/concepts/payload/#update-payload), Since QdrantVec
torStore  
 stores the actual text in payload.content  
 along with the vectors so using qdrant sdk I will have to perfr
om the vector and payload updates seperately with two API calls.

Although using Qdrant vector stores allows writing a c
lean code.

This [reddit post](https://www.reddit.com/r/LangChain/comments/17bc1ij/update_collection_in_qdrantdont_want_
to_create/) suggests using add\_documents  
 even for update but that suggestion is for langchain.py not for js. But I t
ried something similar in langchain.js, I tried to use QdrantVectorStore.addDocuments()  
 to update data but I couldn't
 find a way to pass pointId\[\]  
 to specify which point to update. I also checked the types and interfaces for QdrantV
ectorStore.addDocuments()  
 so I found this

    type QdrantAddDocumentOptions = {     customPayload: Record<string, an
y>[]; }; addDocuments(documents: Document[], documentOptions?: QdrantAddDocumentOptions): Promise<void>; 

As a last res
ort I also tried passing an array of pointIds in customPayload  
 but that didn't work. it was simply creating a point i
n cluster with the ids I passed in customPayload.
```
---

     
 
all -  [ Help please! ](https://www.reddit.com/r/ChatGPT/comments/1983eqs/help_please/) , 2024-01-17-0910
```
so, i need advice from the community about a system that i am struggling to create. 

Let me explain the problem first, 
so, here it goes.

I am trying to build a mobile app, powered with AI. It is an astrology app. I have all the relevant d
ata as my guru is an expert with 60 years of experience in this field.

I am able to call an astro API to get the user c
hart details. so, i have the planetary positions, aspects, and other related information available with me for the AI.


the purpose of using an AI is to make predictions. to draft an overall structure of a person based on the above details 
and the data that I have.

the challenge that I am facing is that, this is not a simple RAG over my dataset. later on, i
 will come to what all i have already tried. but for now, the challenge is that, for predicting any part of a human life
, be it personality, life, career, relationship or anything, there are a set of rules that needs to be followed and chec
ked. for an example, to get the personality, there are around 6 rules to be followed, like the placement of sun, moon. t
he ascendant, the planets present in the house of personality, the ruler of those houses and where they r placed in the 
chart, to name a few rules/combinations.

Now, RAG is simple retrieval of completion of the prompt fed into the llm. and
 as you can see, i need to give reasoning, thinking and processing power to the llm.

I have already tried Llama index, 
langchain with various retrievals, agents, tools and even with vectors, knowledge graphs, summary tools etc. but no use.


kindly help/guide me solve this issue. any pointers/links will be appreciated.
```
---

     
 
all -  [ Help needed ](https://www.reddit.com/r/AutoGenAI/comments/1983dce/help_needed/) , 2024-01-17-0910
```
so, i need advice from the community about a system that i am struggling to create. 

Let me explain the problem first, 
so, here it goes.

I am trying to build a mobile app, powered with AI. It is an astrology app. I have all the relevant d
ata as my guru is an expert with 60 years of experience in this field.

I am able to call an astro API to get the user c
hart details. so, i have the planetary positions, aspects, and other related information available with me for the AI.


the purpose of using an AI is to make predictions. to draft an overall structure of a person based on the above details 
and the data that I have.

the challenge that I am facing is that, this is not a simple RAG over my dataset. later on, i
 will come to what all i have already tried. but for now, the challenge is that, for predicting any part of a human life
, be it personality, life, career, relationship or anything, there are a set of rules that needs to be followed and chec
ked. for an example, to get the personality, there are around 6 rules to be followed, like the placement of sun, moon. t
he ascendant, the planets present in the house of personality, the ruler of those houses and where they r placed in the 
chart, to name a few rules/combinations.

Now, RAG is simple retrieval of completio  of the prompt fed into the llm. and
 as you can see, i need to give reasoning, thinking and processing power to the llm.

I have already tried Llama index, 
langchain with various retrievals, agents, tools and even with vectors, knowledge graphs, summary tools etc. but no use.


kindly help/guide me solve this issue. any pointers/links will be appreciated.
```
---

     
 
all -  [ Blog: What is LangChain | Explanation For Beginners ](https://www.reddit.com/r/LangChain/comments/1982asu/blog_what_is_langchain_explanation_for_beginners/) , 2024-01-17-0910
```
Hey Guys, if you are new to LangChain or want to learn how it works, you can read this blog: 

[What is LangChain? AI Ap
p Development Framework Explained](https://www.deligence.com/what_is_langchain_ai_app_development_framework_explained/)
```
---

     
 
all -  [ Retriever results are sometimes off ](https://www.reddit.com/r/LangChain/comments/1981tcr/retriever_results_are_sometimes_off/) , 2024-01-17-0910
```
I am using a combination of a BM25 keyword and Chroma vectorstore based retrievers.

get_relevant_documents() works pret
ty well most of the times, but sometimes the results are off.

For example, testing with only two documents results in w
rong results. While larger document sets work pretty well.

Anyone observed something similar?
```
---

     
 
all -  [ LangChain + Gemini Pro = ❌ ? ](https://www.reddit.com/r/LangChain/comments/198127w/langchain_gemini_pro/) , 2024-01-17-0910
```
Hi all! I am wondering whether you guys had any success with the integration of LangChain with Gemini Pro? My tests have
 shown terrible results thus far with \`\`ChatGoogleGenerativeAI\`\` used within slightly more complex chains, such as \
`\`ConversationalRetrievalChain\`\`. Two problems that frequently pop:

1. The model seems to default quite often to 'I 
don't know' or 'I cannot find the information in the context provided', despite the fact that the context contains the r
equested information upon inspection (so it is not an error with the vector DB).
2. Perhaps the most annoying: Some of t
he LangChain-built system prompts (converted to human messages) which ask the model to translate something to the 'origi
nal language' completely confuse it, making it output a message in a random language. I have tried using the prompt crea
ted by LangChain with the Google API directly, and surprise, surprise, the responses are equally bad! I'm thinking of re
porting this issue to Google directly. Example:

&#8203;

    import google.generativeai as genai
    genai.configure(ap
i_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    prompt = 'Human: Given the follo
wing conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original
 language.\n\nChat History:\n\nHuman: what does the third amendment say?\nAssistant: I do not have access to the context
 necessary to answer that question.\nFollow Up Input: what does the second amendment say?\nStandalone question:'
    res
p = model.generate_content(prompt)
    Markdown(resp.text) # gives answer in a random language

If you had similar exper
iences or found good workarounds for using the integration, please let us know. Thanks!
```
---

     
 
all -  [ Iterate PDFs in loop to store the embeddings separately in vectorestore ](https://www.reddit.com/r/LangChain/comments/197zyqw/iterate_pdfs_in_loop_to_store_the_embeddings/) , 2024-01-17-0910
```
How should I load the one pdf at a time and get the embeddings of it in loop. If I used the PyPDFLoader it will load all
 the pdfs together in the form of Document. I want to load the pdfs one by one the store it in VectoreStore like FAISS, 
Chroma
```
---

     
 
all -  [ When I use RAGatouille in langchain,I found that it doesn't work ](https://www.reddit.com/r/LangChain/comments/197yjc4/when_i_use_ragatouille_in_langchaini_found_that/) , 2024-01-17-0910
```
When I write a search following the langchain documentation[https://python.langchain.com/docs/integrations/retrievers/ra
gatouille]:
```python
def get_collection():
    with open('log.txt', 'r') as f:
        doc = f.read()
    return [doc]



if __name__ == '__main__':
    RAG = RAGPretrainedModel.from_pretrained('colbert-ir/colbertv2.0')

    collection = ge
t_collection()
    RAG.index(
        collection=collection,
        index_name='Miyazaki-123'
    )

    retriever = RA
G.as_langchain_retriever(k=3)
    res = retriever.invoke('who is tom')
    print(res)
```
I've noticed that there isn't 
any output, I'm not sure if it's related to my computer environment, can anyone give me a solution?
```
---

     
 
all -  [ Pdf Text Splitter without losing context over pages ](https://www.reddit.com/r/LangChain/comments/197xqvz/pdf_text_splitter_without_losing_context_over/) , 2024-01-17-0910
```
Hi, 

in my RAG app I am loading PDF-files with PyPDFLoader and I am chunking the PDFs with the RecursiveCharacterTextSp
litter.

 However I am facing the problem, that often a important topic starts at the end of a page and continues in the
 next page. With PyPDFLoader, every page is a List Entry, so in the case described above, the context is lost in the nex
t page. 

&#x200B;

`[Document(page_content='  IT-Betriebs Konsolidierung...', metadata={'source': '`[`management.pdf`](
https://file+.vscode-resource.vscode-cdn.net/BKB_Abstimmungsmanagement.pdf)`', 'page': 0}),  Document(page_content='Abst
immungsmanagement  \n \n2 \n \nInformationen zum Dokument ...  ', metadata={'source': '`[`management.pdf`](https://file+
.vscode-resource.vscode-cdn.net/BKB_Abstimmungsmanagement.pdf)`', 'page': 1}),  Document(page_content='Abstimmungsmanage
ment  \n \n3 \n \n0.8 18.05.2020 Aktualisierung nach Umstellung des \nVorgehens  basierend auf... ', metadata={'source':
` [`management.pdf`](https://file+.vscode-resource.vscode-cdn.net/BKB_Abstimmungsmanagement.pdf)`', 'page': 2})`

&#x200
B;

What are alternatives for this?
```
---

     
 
all -  [ Doesn't langchain retriever support 'similarity_search_with_relevant_scores' using FAISS? ](https://www.reddit.com/r/LangChain/comments/197wxp9/doesnt_langchain_retriever_support_similarity/) , 2024-01-17-0910
```
I'm trying to get the similarity scores using below func. My vector index is FAISS. I get an error:  


retriever = loca
l\_db.as\_retriever(

search\_type='similarity\_search\_with\_relevant\_score'

)

 **ValidationError**: 1 validation er
ror for VectorStoreRetriever \_\_root\_\_   search\_type of similarity\_search\_with\_score not allowed. Valid values ar
e: ('similarity', 'similarity\_score\_threshold', 'mmr') (type=value\_error)\[26\]:  
 
```
---

     
 
all -  [ The inner workings of RedisChatMessageHistory ](https://www.reddit.com/r/LangChain/comments/197wlgo/the_inner_workings_of_redischatmessagehistory/) , 2024-01-17-0910
```
The inner workings of `RedisChatMessageHistory`,I'm trying to find out if it uses summary internally like `ConversationS
ummaryMemory`, or if he's simply adding historical data to the context.

This may cause the token to exceed the limit, i
s there anything I can do to avoid this? I don't see an internal description of this in the documentation.
```
---

     
 
all -  [ Struggling with LangChain's learning curve ](https://www.reddit.com/r/LangChain/comments/197u4wp/struggling_with_langchains_learning_curve/) , 2024-01-17-0910
```
As a newcomer to LangChain, I'm finding the learning curve to be quite steep. I've been sifting through the documentatio
n and various forums for guidance, but it feels like I'm piecing together a puzzle without all the pieces.

I'm curious 
to know if there are others out there who feel the same way. Is there a better way to approach learning LangChain that I
'm missing? Any resources or tips would be greatly appreciated.
```
---

     
 
all -  [ Anyone trained and hosted their own knowledge base chatbot? ](https://www.reddit.com/r/AIBizOps/comments/197mu0h/anyone_trained_and_hosted_their_own_knowledge/) , 2024-01-17-0910
```
I’ve been playing around with this a little.  I’m trying to come up with some chatbot solutions to help my company.

Lik
e a lot of companies, we have tons of internal data/practices.  I’d love to create something a user could query and find
 an answer.

I built something last night using LangChain and FAISS with FastText, and it worked, but it just basically 
functioned as an inaccurate text search.

I was hoping to implement something that could read and summarize for the user
.  Obviously, I could create something like a wrapper around ChatGPT, but we have a few limitations.

1. It has to be co
mpletely private, so it has to be hosted locally and we can’t send sensitive data to some external vendor.

2. It has to
 be free.

3. We don’t want it having access to external data (e.g., no questions about politics, etc.).

Has anyone bui
lt anything like this?  I’m extremely new, so please don’t hurt me if I’m asking for something stupid or impossible.

Th
anks in advance!
```
---

     
 
all -  [ How to add web search to ollama model ](https://www.reddit.com/r/ollama/comments/197meew/how_to_add_web_search_to_ollama_model/) , 2024-01-17-0910
```
Hello guys, does anyone know how to add an internet search option to ollama? I was thinking of using LangChain with a se
arch tool like DuckDuckGo, what do you think? 
```
---

     
 
all -  [ Mistral 7B QAGeneration Chain Langchain - JSONDecode Error ](https://www.reddit.com/r/LangChain/comments/197j354/mistral_7b_qageneration_chain_langchain/) , 2024-01-17-0910
```
hello   
I'm trying to use the Mistral 7B model for question-answer generation using the QAGeneration Chain  
 

`def ll
m_question_generation_pipeline(chunks):`  
`documents = [Document(page_content=chunk) for chunk in chunks]`  
`repo_id =
 'mistralai/Mistral-7B-v0.1'`  
`llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={'temperature': 0.5, 'max_length': 5
12})`  
`qa_chain = QAGenerationChain.from_llm(llm = llm, verbose = True)`  
`raw_output = qa_chain.run(documents[0].pag
e_content)`  
`print('Raw Output:', raw_output)`

&#x200B;

this is my code, but I'm getting this error frequently  
`ra
ise JSONDecodeError('Expecting value', s, err.value) from None`

`json.decoder.JSONDecodeError: Expecting value: line 1 
column 2 (char 1)`  


this is the prompt created by QAGeneration chain  
`Prompt after formatting:`

`You are a smart a
ssistant designed to help high school teachers come up with reading comprehension questions.`

`Given a piece of text, y
ou must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.`


`When coming up with this question/answer pair, you must respond in the following format:`

`\`\`\``

`{`

`'question': 
'$YOUR_QUESTION_HERE',`

`'answer': '$THE_ANSWER_HERE'`

`}`

`\`\`\``

&#x200B;

`Everything between the \`\`\` must be
 valid json.`

&#x200B;

`Please come up with a question/answer pair, in the specified JSON format, for the following te
xt:`  


I searched for this error, it is saying that it could be possible if the LLM is not giving proper JSON formated
 output  
Would anyone be able to help me solve this error?
```
---

     
 
all -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-17-0910
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
all -  [ I am a technical blogger and want to train an LLM on my blogs. ](https://www.reddit.com/r/LangChain/comments/197eq8d/i_am_a_technical_blogger_and_want_to_train_an_llm/) , 2024-01-17-0910
```
Learning LangChain so figured I would love to see how llms learn my writing and as a bonus would write about how i built
 this?

So need help with a few questions from the community

1) Which LLM would be best other than OpenAi models as I w
ant to experiment with opensource models

2) list of tools, agents  and chains which would help me do this? 

3) Bonus m
y content has code embedded in it and visualizations, anyway I could tell the LLM to do it for me?
```
---

     
 
all -  [ Need suggestions on code understanding by llm and output. ](https://www.reddit.com/r/LangChain/comments/197b58d/need_suggestions_on_code_understanding_by_llm_and/) , 2024-01-17-0910
```
What I want to achieve?
User can improve code quality and refactoring for give source code repository.

Input - code rep
ository (python, java, dotnet, etc.)
Db - chromadb or pinecone
Embeddeding - sentence transformer model
Top k results - 
MMR search
Key - Azureopnai key n endpoint 

Kindly suggest LLM and retrieval in best way if possible. Any link or refer
ences from Microsoft is also fine.
```
---

     
 
all -  [ Building AI chatbot ](https://www.reddit.com/r/aws/comments/197aas5/building_ai_chatbot/) , 2024-01-17-0910
```
Hi all

I'd like to build an AI chatbot. I'm literally fresh in the subject and don't know much about AWS tools in that 
matter, so please help me clarify.  

More details:  

The model is yet to be chosen and to be trained with specific FAQ
 & answers. It should answer user's question, finding most sutiable answer from the FAQ.  

If anyone has ever tried to 
built similar thing please suggest the tools and possible issues with what I have found out so far.  

  

My findings: 
 

1. AWS Bedrock (seems more friendly than Sagemaker)  
2. Will have to create FAQ Embeddings, so probably need a vecto
r store? Is OpenSearch good?   
3. Are there also things like agents in here? For prompt engineering for example?   
4. 
With having Bedrock and it's tools, would I still need to use Langchain for example?  

 
```
---

     
 
all -  [ Custom GPT to assist with langchain development ](https://www.reddit.com/r/LangChain/comments/1979xgt/custom_gpt_to_assist_with_langchain_development/) , 2024-01-17-0910
```
Hi Guys,

&#x200B;

I did a little side project to help me on my project, I'm doing a database parser agent using Clause
 2.1 on bedrock that uses Python to query Druid with a LOT of contexts.

Been struggling quite a lot with documentation 
with anything that is not open ai.

So I created a Custom GPT to help me where it can.

&#x200B;

It's not perfect, but 
it's been helping me a little so I wanted to share it with you all.

&#x200B;

[Langchain Specialist](https://chat.opena
i.com/g/g-yqSII6PUj-langchain-specialist)
```
---

     
 
all -  [ What is similarity search with relevancy score ](https://www.reddit.com/r/LangChain/comments/19795k7/what_is_similarity_search_with_relevancy_score/) , 2024-01-17-0910
```
What is the difference between a similarty search and similarty search with relevancy score?
```
---

     
 
all -  [ Why Reranking exists in the first place? ](https://www.reddit.com/r/LangChain/comments/1978ywu/why_reranking_exists_in_the_first_place/) , 2024-01-17-0910
```
I'm trying to understand why Reranking is often needed in RAG technique and why it can't be just skipped completely.

Wo
uld Reranking still exist if LLM models were bigger and better at creating embeddings(converting prompts into vectors in
 space)? 
```
---

     
 
all -  [ Getting error on chat history langchain. ValueError: variable chat_history should be a list of base  ](https://www.reddit.com/r/LangChain/comments/19777hm/getting_error_on_chat_history_langchain/) , 2024-01-17-0910
```
[https://python.langchain.com/docs/use\_cases/question\_answering/chat\_history](https://python.langchain.com/docs/use_c
ases/question_answering/chat_history)  
I am referring to these docs for chat history  
 I\]this code is giving me error
 on this 'chat\_history.extend(\[HumanMessage(content=question), ai\_msg\])  
line'

chat\_history = \[\]  
question = '
What is function of form nec?'  
ai\_msg = rag\_chain.invoke({'question': question, 'chat\_history': chat\_history})  
c
hat\_history.extend(\[HumanMessage(content=question), ai\_msg\])  
second\_question = 'is there anything else about it?'
  
rag\_chain.invoke({'question': second\_question, 'chat\_history': chat\_history})
```
---

     
 
all -  [ Best way to validate llm prompts? ](https://www.reddit.com/r/OpenAI/comments/1974nfo/best_way_to_validate_llm_prompts/) , 2024-01-17-0910
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

     
 
all -  [ Finetune Mixtral on Enterprise data - How does the training data should look like? ](https://www.reddit.com/r/LangChain/comments/1973jxk/finetune_mixtral_on_enterprise_data_how_does_the/) , 2024-01-17-0910
```
Hi,

I want to fine-tune a Mistral or Mixtral model on my companies data. Specifically the model should write bullet-poi
nts to full texts. I was wondering how the training data has to look like for this task?

Is it a valid way to let a LLM
 create bullet points out of a text and use these bullet-points-full-text-examples for training? 
```
---

     
 
all -  [ Anyone have Yi-34B (running with Ollama) with LangChain working ](https://www.reddit.com/r/LangChain/comments/196vqu3/anyone_have_yi34b_running_with_ollama_with/) , 2024-01-17-0910
```
I've been able to get all other local models, running with Ollama, working with LangChain. However, Yi-34B never returns
 a response.

I'm running an RTX 3090 and it is fitting in VRAM according to nvtop (20GB used).

Something simple like t
his never finishes (the last line is the one that never finishes):

    from langchain_community.llms import Ollama
    

    ollama_model_name = 'yi:34b-chat-q4_K_M'
    llm = Ollama(model=ollama_model_name, temperature=0.1)
    
    llm.in
voke('why is the sky blue?') # This line never finishes...

I run it directly with Ollama and it responds instantly:

  
  $ ollama run yi:34b-chat-q4_K_M
    >>> why is the sky blue?
    The sky appears blue to us because of a phenomenon ca
lled Rayleigh scattering. This occurs when light from the sun 
    interacts with the molecules of the Earth's atmospher
e, which are composed primarily of nitrogen and oxygen. These 
    molecules are much smaller than the wavelength of vis
ible light, so they can scatter light very efficiently.
    
    When sunlight enters the atmosphere, it strikes these a
tmospheric particles and is scattered in different directions.
    The shorter wavelengths of blue light are scattered m
ore than longer wavelengths of red light because they have 
    higher energy and thus a greater probability to interact
 with the molecules. This means that more blue light gets 
    scattered relative to other colors, which is why we see a
 blue sky most of the time.
    
    The intensity of Rayleigh scattering also depends on the angle at which light hits 
an atmospheric molecule. 
    Scattering is most effective when light hits molecules nearly head-on, which preferentiall
y scatters light in all 
    directions away from the sun. This scattered blue light then reaches our eyes after being s
cattered multiple times by
    different air molecules, giving us the perception of a blue sky.
    
    The color we se
e also depends on the observer's line of sight relative to the sun. When the sun is high in the sky, 
    more blue ligh
t scatters directly into our eyes, making the sky appear very blue. As the sun approaches the horizon, 
    the light ha
s to pass through more air and is scattered less efficiently, which means that more red light reaches our
    eyes, resu
lting in a reddish sky at sunset and sunrise.
    
    Additionally, other factors can influence the color of the sky, s
uch as pollution or dust particles in the 
    atmosphere, which can scatter light differently and change the appearance
 of the sky.
    

Any ideas?
```
---

     
 
all -  [ Chatbot for potential customers ](https://www.reddit.com/r/LangChain/comments/196uo2k/chatbot_for_potential_customers/) , 2024-01-17-0910
```
I have some experience in programming, mostly in nodeJS. Basically I want to create a chatbot that 
1. qualifies leads b
y asking questions
2. answers questions from my knowledge base using RAG. 
3. If the user wants to set up an appointment
, it extracts the information and stores it in a table. 

I want the bot to handle multiple conversations concurrently. 


Read through langchain documentation but still confused how to approach this. If you've made anything similar, please 
share some insight!
```
---

     
 
all -  [ A python package I created for llms application including my own implementation of long short term m ](https://www.reddit.com/r/LocalLLaMA/comments/196qqoy/a_python_package_i_created_for_llms_application/) , 2024-01-17-0910
```
[https://github.com/nath1295/LLMPlus](https://github.com/nath1295/LLMPlus)

I find Langchain annoying for not letting yo
u set different llms with different generation configurations, so I tried to build my own custom llms to avoid loading l
ocal models multiple times when I want to build an agent or tool that uses the same underlying model. Also, some of the 
streaming and stop words for llms are not that great in langchain, so I have my own implementation in this package I cre
ated.   
I am still using an Intel MacBook (too poor to get Nvidia cards or even a new Macbook :( ) to work on this proj
ect, so I cannot guarantee the installation will be seamless, but hopefully the pip install works. The code should be wo
rking with Cuda or apple silicon (used Colab and my friend's flashy new macbook to briefly test it).  


Stuff I have in
 the package:

* An LLM factory class to generate Langchain-compatible llms while only loading the model once.
* Embeddi
ng toolkits that have text splitters bundled with the embedding model.
* A Vector database class built on top of FAISS f
or local storage.
* Memory classes: (base one and one with both long-term and short-term memory, powered by a vector dat
abase)
* Prompt template class that helps you to format your prompt with different prompt formats (have some presets lik
e llama2, chatml, vicuna etc.)
* A base tool class and a web search tool with duckduckgo as an example (please have a lo
ok, wonder if there are better ways to do that)
* A Gradio chatbot web app that lets you store different conversations, 
also you can set your own system prompt and configure the long-term and short-term memory settings, and you can set gene
ration configurations like temperature, max new tokens, top k etc. (This is just for fun, my front-end skills are not be
tter than a monkey to be very honest.)
* And of course, the docs in the repo as well.

&#x200B;

I know I'm no expert, t
here are plenty of people in this sub who are extremely knowledgeable in this LLM field, so treat this as an amateur pro
ject looking for advice if you can bear with me for my spaghetti code. Would really appreciate any comments :')) Forgive
 me if I can't do much testing on fancy GPUs like you guys have, trying not to spend any money to work on this project..
.
```
---

     
 
all -  [ Resume review for data scientist position ](https://www.reddit.com/r/resumes/comments/196omyb/resume_review_for_data_scientist_position/) , 2024-01-17-0910
```
Hi Everyone,

I would love to get some feedback about my resume.

Target positions: data scientist / Senior data scienti
st positions

Location: USA

Thanks!

&#x200B;

https://preview.redd.it/jvdpeev7qgcc1.jpg?width=2550&format=pjpg&auto=we
bp&s=5f1dc9e2740df855bf44262def4f87c39561d189
```
---

     
 
all -  [ can i get an invite code for langsmith please , been waiting forever ](https://www.reddit.com/r/LangChain/comments/196nq3r/can_i_get_an_invite_code_for_langsmith_please/) , 2024-01-17-0910
```
can i get an invite code for langsmith please , been waiting forever
```
---

     
 
all -  [ Using LLMs to draw simple insight from tabular data: a discussion ](https://www.reddit.com/r/dataengineering/comments/196nl41/using_llms_to_draw_simple_insight_from_tabular/) , 2024-01-17-0910
```
Hey hey all, data/analytics engineer here,

I got a lenghty topic, hopefully worthy of a lenghty discussion. I'm looking
 into LLM-s and how they could be used for assisting in understanding reports.

I would like your opinion on the followi
ng idea I am exploring.

**Business Problem**

Our company got loads of reports generated, more than humanely possible t
o read (that's another discussion to have, but many of these are legally required, etc.). It would be really cool that f
or a given report, there would be a few sentences highlighting things.

A Report's (Reader's) Digest if you will. Things
 like

* 'It seems that compared to 2023 Q1, in 2023 Q2 our sales in department x has increased by 6.4% percent which is
 unusually high.'
* 'Our social network reach has been constantly falling on Facebook since 2023 February.'
* 'The avera
ge customer rating has been dropping for 5 consecutive days.'

**Understanding limits**

I get that LLM-s work with stri
ng data, so i'm guessing this isn't a straightforward thing to do. I'm also thinking that currently LLM-s won't figure o
ut insights on their own without guidance, thus questions should be agreed upon with business. (Altough self-propelled i
nsight finding would be a holy grail.) So with this in mind:

* probably business questions should be agreed upon
* prob
ably business shouldn't ask their questions directly from an LLM agent
* LLMs are not great at understanding tabular dat
a so this is not an obvious path ahead

**Brainstorming ideas**

Architecture-wise, I would be using Databricks (somethi
ng we actively work with), loading a report in as a delta table, then use a [LLM serving endpoint](https://learn.microso
ft.com/en-us/azure/databricks/machine-learning/model-serving/llm-optimized-model-serving). This is fairly new stuff comi
ng from them, it's still in public preview, but it can leverage LLama-2, keeps the data on databricks side so it seems s
ecure. (GDPR says hello.)

I found of course Pandas AI, that could be useful in combination with databricks somehow? I a
lso found this [fairly recent paper](https://arxiv.org/pdf/2401.04398v1.pdf), which talks about 'Evolving chain for tabl
e reasoning' on L[LamaIndex linkedin page](https://www.linkedin.com/posts/llamaindex_chain-of-table-use-llms-to-understa
nd-activity-7151983658596229120-fOo3?utm_source=share&utm_medium=member_desktop) that proposes a chain-of-table querying
 that looks interesting. It seems something closer to what LangChain is doing. Some [medium.com](https://medium.com) art
icles i found: [1](https://medium.com/@murtuza753/using-llama-2-0-faiss-and-langchain-for-question-answering-on-your-own
-data-682241488476) (this is about documents), [2](https://ameer-hakme.medium.com/unlocking-context-aware-insights-in-ta
bular-data-with-llms-and-langchain-fac1d33b5c6d) (this is about tabular data)

**A maybe functioning idea**

Okay so let
's see if the following makes sense, it is very highlever and very brainstormy:

1. Agree on with business what are the 
core questions they want to know from a report.
2. A LLama-2 model is setup in Databricks with serving endpoint
   1. ED
IT: so probably not Llama-2, but something along this line: [https://ameer-hakme.medium.com/unlocking-context-aware-insi
ghts-in-tabular-data-with-llms-and-langchain-fac1d33b5c6d](https://ameer-hakme.medium.com/unlocking-context-aware-insigh
ts-in-tabular-data-with-llms-and-langchain-fac1d33b5c6d) or PandasAI working with a databricks-stored llama2 (afaik that
 is supported)
3. A job runs daily:
   1. A report is ingested some magical data engineering-y way (my fellow data engin
eers know the pain)
   2. Prompt engineering: do some setup with the LLM agent (no clue yet what could be needed, but it
's a good guess that this is required - to prevent hallucations, etc).
   3. Prompts from business are loaded from some 
config file
   4. Results are stored in a separate delta table with following schema:
      1. Some primary key
      2.
 Some report identifier
      3. Business unit or stakeholder identifier
      4. Prompt
      5. Answer
      6. Timest
amp
   5. A SQL Warehouse endpoint is available and can be queried (by PowerBI for example that gets the latest answers.
)

**Problems and limitations**

How do we check if the answers are correct? Monitoring results is very blackbox-y at be
st. Ideally endusers needs to be trained on the purpose of the Report's Digest is to highlight stuff, but they have to v
erify it themselves. Getting feedback from endusers can be also complicated

**Conclusion in an ideal world**

Business 
managers like to look at PowerBI reports, and with this new feature they get an immediate highlight of the day, the top 
3 questions they always wanna know about comes with immedaite answers. 'We have an increased count of customer service t
ickets compared to previous week'. The manager looks at the graph and it seems to verify this statement.

Engineer team 
walks into the sunset with cool music in background

&#x200B;
```
---

     
 
all -  [ Langchain developers community For Free. ](https://www.reddit.com/r/Langchain_developers/comments/196m52z/langchain_developers_community_for_free/) , 2024-01-17-0910
```
The main point of this community rather than Langchain which already exists but have to create a separate for developers
 , who need help to learn and need assistance.

  
Feel Free to join and grow this community 

LangChain is an open-sour
ce framework and developer toolkit that helps developers get LLM applications from prototype to production. It is availa
ble for Python and Javascript at https://www.langchain.com/. 
```
---

     
 
all -  [ Seeking advice for developing a text-to-sql application ](https://www.reddit.com/r/OpenAI/comments/196lvge/seeking_advice_for_developing_a_texttosql/) , 2024-01-17-0910
```
Hi everyone,

I'm currently working on an internal project at my company. My goal is to develop a chat-based solution th
at allows business users to query the data warehouse (we're using BigQuery) through conversation. I’m trying to make thi
s project more production-ready, rather than being an experiment. I’m using LangChain with OpenAI currently and I could 
really use some inputs:

1. **Data Privacy and Access Control**: One of our top priorities is to ensure data privacy and
 appropriate access controls. Tagging a column like “revenue” to be private might work for simple scenarios, but real-li
fe scenarios are more complex, for example, how do you let users from the marketing department see the “email” column of
 customers, while others see redacted email? What about row-level security?
2. **Reviewing Generated SQL Queries**: Our 
data analysts have raised concerns about the difficulty in reviewing SQL statements generated by LLMs. These queries can
 be complex and hard to interpret. Any suggestions for making this process more manageable and transparent? Perhaps a SQ
L lineage tool to show the visibility of the SQL ?
3. **Semantic Integration with Database Tables and Columns**: Lastly,
 I'm wondering about the best way to integrate semantics into our database tables and columns. Seems that feeding dbt mo
dels (including description) directly to the LLM can work at first, but is there any solution that I can let business us
ers define these metadata themselves ? Does it mean I need to build an internal tool that allows users to update the met
adata ?

Any feedback, insights, or experiences you can share regarding these challenges are appreciated.

Thanks!
```
---

     
 
all -  [ Seeking advice for developing a text-to-sql application ](https://www.reddit.com/r/LangChain/comments/196lhv9/seeking_advice_for_developing_a_texttosql/) , 2024-01-17-0910
```
Hi everyone,

I'm currently working on an internal project at my company. My goal is to develop a chat-based solution th
at allows business users to query the data warehouse (we're using BigQuery) through conversation. I’m trying to make thi
s project more production-ready, rather than being an experiment. I’m using LangChain and followed guides in documentati
on & blogs (ex: [https://python.langchain.com/docs/use\_cases/qa\_structured/sql](https://python.langchain.com/docs/use_
cases/qa_structured/sql)) to achieve the first version and I could really use some inputs:

1. **Data Privacy and Access
 Control**: One of our top priorities is to ensure data privacy and appropriate access controls. Tagging a column like “
revenue” to be private might work for simple scenarios, but real-life scenarios are more complex, for example, how do yo
u let users from the marketing department see the “email” column of customers, while others see redacted email? What abo
ut row-level security?
2. **Reviewing Generated SQL Queries**: Our data analysts have raised concerns about the difficul
ty in reviewing SQL statements generated by LLMs. These queries can be complex and hard to interpret. Any suggestions fo
r making this process more manageable and transparent? Perhaps a SQL lineage tool to show the visibility of the SQL ?
3.
 **Semantic Integration with Database Tables and Columns**: Lastly, I'm wondering about the best way to integrate semant
ics into our database tables and columns. Seems that feeding dbt models (including description) directly to the LLM can 
work at first, but is there any solution that I can let business users define these metadata themselves ? Does it mean I
 need to build an internal tool that allows users to update the metadata ?

Any feedback, insights, or experiences you c
an share regarding these challenges are appreciated.

Thanks!
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-17-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-17-0910
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-17-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-17-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-17-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-17-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-17-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
