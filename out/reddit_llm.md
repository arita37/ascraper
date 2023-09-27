 
all -  [ Is Finding Multiple Instances Possible Using Langchain??? ](https://www.reddit.com/r/LangChain/comments/16t358t/is_finding_multiple_instances_possible_using/) , 2023-09-27-0910
```
Hey everyone,

I've been experimenting with Langchain and OpenAI's embedding models. From my understanding, these models
 are especially powerful when it comes to understanding and answering direct questions, thanks to the way documents are 
stored as vectors.

However, I've encountered some challenges when trying to ask questions that require identifying mult
iple instances or patterns within a document. For example, asking 'find all instances of X' seems to be tricky due to th
e nature of vector embeddings.

Is my understanding correct? If so, are there any techniques or strategies that can be e
mployed to ask such 'find all instances of...' questions effectively using these models?

Appreciate any insights or exp
eriences you can share!
```
---

     
 
all -  [ We have an integration on LangChain and are looking for feedback :) ](https://www.reddit.com/r/LangChain/comments/16t2ttu/we_have_an_integration_on_langchain_and_are/) , 2023-09-27-0910
```
Hi everyone, 

We recently worked on an integration with LangChain, which we launched a few days ago: [https://blog.lang
chain.dev/eden-ai-x-langchain/](https://blog.langchain.dev/eden-ai-x-langchain/)

Our service aggregates many AI service
s (and not just LLMs) into a single API with endpoints that link back to [competing providers](https://www.edenai.co/pro
viders). The idea is to give users the flexibility to choose at any time the provider that suits them best (in terms of 
price, latency, response quality, etc.) and to manage in a single place all their consumption in terms of AI and LLM ser
vices available via API. 

And we're looking for user feedback on this integration. It would be a great help to us in ou
r development. It will also help us understand whether or not it's worth continuing to work on this integration by keepi
ng it up to date: [https://python.langchain.com/docs/integrations/llms/edenai](https://python.langchain.com/docs/integra
tions/llms/edenai) & [https://python.langchain.com/docs/integrations/tools/edenai\_tools](https://python.langchain.com/d
ocs/integrations/tools/edenai_tools)

Sorry in advance if my message sounds promotional, but it's really not. We're look
ing for frank and honest feedback and Reddit is often the best place for that :) 

Cheers,
```
---

     
 
all -  [ ROScribe v0.0.3: Using LangChain to create the entire code for a robotic project in ROS2 ](/r/LangChain/comments/16t1kgz/roscribe_v003_using_langchain_to_create_the/) , 2023-09-27-0910
```

```
---

     
 
all -  [ No-code development of customized smart assistant ](https://www.reddit.com/r/SideProject/comments/16t1vhu/nocode_development_of_customized_smart_assistant/) , 2023-09-27-0910
```
Hi everyone, I built an early prototype of a zero-code development tool for building customized smart assistant. Would l
ove some feedback:

[https://houseelf.app/](https://houseelf.app/)

I included a quick example of SalesGPT equivalent ([
https://python.langchain.com/docs/use\_cases/more/agents/agents/sales\_agent\_with\_context](https://python.langchain.co
m/docs/use_cases/more/agents/agents/sales_agent_with_context)) built with the tool to help people getting started:

[htt
ps://houseelf.app/editor/219/](https://houseelf.app/editor/219/) 

If you find this interesting, please feel free to DM 
me. All feedback & questions welcome.
```
---

     
 
all -  [ Unhashable type: 'list' ](https://www.reddit.com/r/LangChain/comments/16t1sqp/unhashable_type_list/) , 2023-09-27-0910
```
I've been following the guide on LangChain called CHat with your Data

[https://learn.deeplearning.ai/langchain-chat-wit
h-your-data/lesson/1/introduction](https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/1/introduction)

I
've followed the code exactly but near the very end end when I make the call to the LLM I get the above error.  Any idea
s?

Here is the full code

from langchain.document\_loaders import PyPDFLoader, TextLoader  
loader = PyPDFLoader('examp
le\_data/23andMe Case Study \_ Life Sciences \_ AWS.pdf')  
\# loader = TextLoader('bob.txt')  
\# Load the document by 
calling loader.load()  
pages = loader.load()  
\# SOme debug stuff to check contents of loaded file  
\# print(len(page
s))  
\# print(pages\[0\].page\_content\[0:500\])  


\# Define the Text Splitter  
from langchain.text\_splitter import
 RecursiveCharacterTextSplitter  
text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=1500, chunk\_overlap=150) 
 
\# Create a split of the document using the text splitter  
splits = text\_splitter.split\_documents(pages)  


from l
angchain.vectorstores import Chroma  
from langchain.embeddings import HuggingFaceEmbeddings  
modelPath = 'all-MiniLM-L
6-v2' # Look at moving models to a standard place for other code to reuse \~/model/googlr/all-MimiLM-L6-v2  
model\_kwar
gs = {'device': 'cpu'}  
encode\_kwargs = {'normalize\_embeddings': False}  
embeddings = HuggingFaceEmbeddings(  
 mode
l\_name=modelPath, model\_kwargs=model\_kwargs, encode\_kwargs=encode\_kwargs  
)  


persist\_directory = 'docs/chroma/
'  
\# Create the vector store  
\# vectordb = Chroma.from\_documents(  
\#     documents=splits, embedding=embeddings, 
persist\_directory=persist\_directory  
\# )  
from langchain.vectorstores import FAISS  
vectordb = FAISS.from\_documen
ts(documents=splits, embedding=embeddings)  
\# print(vectordb.\_collection.count())  


question = 'WHat benefits did 2
3AndMe see from sitching to AWS?'  
docs = vectordb.similarity\_search(question, k=3)  
\# Check the length of the docum
ent  
print(len(docs))  
\# Check the content of the first document  
print(docs\[0\].page\_content)  
\# Persist the da
tabase to use it later  
\# vectordb.persist()  


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeli
ne  
from langchain.llms import HuggingFacePipeline  
tokenizer = AutoTokenizer.from\_pretrained(  
 'flan-t5-large'  
)
  # Look at moving models to a standard place for other code to reuse \~/model/googlr/flan-t5-large  
model = AutoModelF
orSeq2SeqLM.from\_pretrained('flan-t5-large')  
pipe = pipeline('text2text-generation', model=model, tokenizer=tokenizer
)  
llm = HuggingFacePipeline(  
 pipeline=pipeline,  
 model\_kwargs={'temperature': 0, 'max\_length': 512},  
)  
from
 langchain.prompts import PromptTemplate  


from langchain.chains import RetrievalQA  
\# Build prompt  
template = '''
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you d
on't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always s
ay 'thanks for asking!' at the end of the answer.   
{context}  
Question: {question}  
Helpful Answer:'''  
QA\_CHAIN\_
PROMPT = PromptTemplate.from\_template(template)  # Run chain  
qa\_chain = RetrievalQA.from\_chain\_type(  
 llm,  
 re
triever=vectordb.as\_retriever(),  
 return\_source\_documents=True,  
 chain\_type\_kwargs={'prompt': QA\_CHAIN\_PROMPT
},  
)  


question = 'Is probability a class topic?'  
result = qa\_chain({'query': question})  
\# Check the result of
 the query  
print(result\['result'\])  
\# Check the source document from where we  
print(result\['source\_documents'\
]\[0\])  


&#x200B;

thanks
```
---

     
 
all -  [ ROScribe v0.0.3: Using LangChain to create the entire code for a robotic project in ROS2 ](https://www.reddit.com/r/LangChain/comments/16t1kgz/roscribe_v003_using_langchain_to_create_the/) , 2023-09-27-0910
```
With ROScribe v0.0.3 released yesterday, you can now build your robotics project automatically in ROS2 as well as ROS1.


[**https://github.com/RoboCoachTechnologies/ROScribe**](https://github.com/RoboCoachTechnologies/ROScribe)

ROScribe us
es GPT and LangChain to ask you about the details of your robotic project, draws the RQT graph, generate the code for al
l ROS nodes, and writes the launch file and installation scripts. Here is a demo on how to use the tool:

[**https://www
.youtube.com/watch?v=H2QaeelkReU**](https://www.youtube.com/watch?v=H2QaeelkReU)

**Release notes for v0.0.3:**

* ROS2 
integration:
   * Now ROScribe supports both ROS1 and ROS2.
   * Code generation for ROS2 uses rclpy instead of rospy
  
 * Installation scripts for ROS2 use [setup.py](https://setup.py/) and [setup.cf](https://setup.cf/) instead of CMakeLis
ts.txt

**ROScribe is an open source project and we welcome you to contribute to this project.**
```
---

     
 
all -  [ Query langchain docs ](https://www.reddit.com/r/LangChain/comments/16sy5rj/query_langchain_docs/) , 2023-09-27-0910
```
Hello peeps! I got a question. Is there some way to use LLM to query the langchain docs? I'm not a very apt programmer s
o I make good use of chatgpt to help me along and learn. It would be looooovely to be able to do that with langchain doc
umentation specifically.

Anyone in the know about this?
```
---

     
 
all -  [ Add new knowledge to LLama2 ](https://www.reddit.com/r/LocalLLaMA/comments/16sxiop/add_new_knowledge_to_llama2/) , 2023-09-27-0910
```
 

I am planning on building my personal assistant based on the LLama2 model. I want the model to know about my personal
 information, like hobbies, family, and close friends. So I created a dolly-format dataset full of conversations between
 me and the model. The result I got is that the model only correctly generates 60% of my personal information and the re
st is made up. However, the model talks the way I wrote it in the dataset.  I also heard of something called cognitive a
rchitecture with langchain but I'm not sure if that is the right solution.

which route should I go with?

Thank all
```
---

     
 
all -  [ Perplexity.ai-like references for RAG ](https://www.reddit.com/r/LangChain/comments/16sxdav/perplexityailike_references_for_rag/) , 2023-09-27-0910
```
I was just looking at [Perplexity.ai](https://Perplexity.ai) and I noticed that it generates references to the documents
 that it tries to generate. I am interested in trying to create something like this with LangChain and RAG. The idea wou
ld be that when LangChain uses RAG to get a document, I would like the generation to have references like what perplexit
y does to tell me what documents were used to generate specific parts of the response.  


Does anyone know how one coul
d accomplish this with LangChain, or if there are any projects that do something like this with RAG?
```
---

     
 
all -  [ Chaining with external API calls ](https://www.reddit.com/r/LangChain/comments/16swjxt/chaining_with_external_api_calls/) , 2023-09-27-0910
```
Hello - I am trying to find the most idiomatic way to chain the following into an Chatbot experience

1 - user types a c
ommand 'Show me all the restaurants in Boston'

2 - first, the AI should format 'Boston' into a fully formed location li
ke 'Boston, MA USA' which i have instructed in the SystemMessage of a ChatPromptTemplate along with a MessagesPlaceholde
r with chat\_history  

3 - Then , an external API call is made to a location search DB with that formatted value which 
returns a list of restaurants 

4 - those restaurants are parsed and then presented to the user 

5 - The user then requ
ests more detail on a single restaurant that then again, queries details just for that one location and returns the resu
lts to the user 

&#x200B;

I tried chaining APIChain with LLMChain but getting errors that each chain needs to be a sin
gle input key chain.  What is the most idiomatic to chain these events together?  I have been evaluating Tools and Agent
s to see if thats a viable path but getting stuck. 
```
---

     
 
all -  [ Question about Vector Databases. ](https://www.reddit.com/r/LangChain/comments/16swdom/question_about_vector_databases/) , 2023-09-27-0910
```
I see a lot of people using ChromaDb, Mil us etc.
I am currently storing my vectors embeddings, their natural language t
ext and metadatas in simples tables, pushed onto a postgres databases.

Can someone explain me the advantages of using t
he above mentioned setups vs simply storing the vectors in table ?
```
---

     
 
all -  [ Embedded AI user assistant - any product, every user (GPT + LangChain + ElasticSearch) ](https://www.reddit.com/r/OpenAI/comments/16stzth/embedded_ai_user_assistant_any_product_every_user/) , 2023-09-27-0910
```
Announcing [Copilot](https://www.commandbar.com/copilot): an embedded user assistant for any product 🎉

Until now, users
 had to learn how software interfaces worked—AI is changing that. Now, every user can have a personalized assistant to s
implify software.

**Copilot is that personalized assistant 🤖**

It guides your users and even directly does things for 
them. And it's our biggest release yet.

Starting today, Copilot (fka HelpHub AI) gains two abilities that make your pro
duct work better for users out-of-the-box:

🤖 Directly fulfill user intent: “Add a teammate?” Done. “Turn on dark mode?”
 Lights out. No need to do a scavenger hunt through the UI.

🧑‍🏫 Personalized assistance: 5 paragraphs of text aren’t th
e best answer to “How do I use the report builder?”. You’ll get more adoption from an interactive walkthrough that leads
 the user through the report builder.

Copilot also joins your growth team: if you’re pushing a product initiative, tell
 Copilot to surface a pricing tier, highlight a feature or suggest settings. It’ll recommend those actions when relevant
!

What we kept hearing: telling users how they can do stuff is great, but can you just make it so they can do the stuff
 through HelpHub?  

>*“How do I invite someone to my account” --> “invite* *vinay**\[**@**\]**commandbar.com* *to my ac
count”*   
>  
>*“How do I create a new campaign” --> “create a new campaign as a duplicate of my last one”*   
>  
>*“H
ow do I add seats” --> “Add 3 seats to my account” “Yes I confirm the payment amount”*  

Today we’re turning HelpHub AI
 into…Copilot. That means each one of your users can get a personalized in-product assistant to help them get the most o
f your web app or site.  

**Who is it for**

Mainly web apps, but it’s just as useful for blogs and marketing sites too
. Anywhere you can embed an HTML snippet. Also works with Wordpress, Bubble, etc.

**How it works**

📖 **Add source cont
ent** by providing a URL to a marketing site or help center. This gives you an AI chatbot.

✏️ **Add other experiences**
. Zappier-style, wire up API endpoints for Copilot to be able to perform multi-step actions. And create product tours. T
hen, tell Copilot situations in which users would find them useful. This is the assistant part.

💈 **Personalize** the w
idget to look and feel like the rest of your site.

🚢 **Ship your Copilot** by pasting an HTML snippet.

🎁 **Extra goodi
es** that come out of the box:

* Automatically learns based on user feedback what works for users overall and for indiv
idual users (e.g. whether users like tours vs. actions).
* Bot cites its sources, and users can view source docs in Copi
lot without leaving the product.
```
---

     
 
all -  [ Langchain Meets GPT-3.5: Crafting the Ultimate Multilingual News Articles Summarizer In English And  ](https://www.reddit.com/r/u_maximilien-AI/comments/16sqojq/langchain_meets_gpt35_crafting_the_ultimate/) , 2023-09-27-0910
```
[https://kpizmax.hashnode.dev/langchain-meets-gpt-35-crafting-the-ultimate-multilingual-news-articles-summarizer-in-engl
ish-and-french](https://kpizmax.hashnode.dev/langchain-meets-gpt-35-crafting-the-ultimate-multilingual-news-articles-sum
marizer-in-english-and-french)
```
---

     
 
all -  [ Unveiling the Mind-Blowing Building Blocks of Generative AI! You Won’t Believe What’s Possible! ](https://www.reddit.com/r/newstrendbuzz/comments/16sq9k8/unveiling_the_mindblowing_building_blocks_of/) , 2023-09-27-0910
```
&#x200B;

https://preview.redd.it/3t955zcd6mqb1.jpg?width=1538&format=pjpg&auto=webp&s=1049ceba99bba34bb858ebe03febe7a2d
274a500

 🌟 Ready to have your mind blown? Discover the secrets behind Generative AI's Building Blocks and the limitless
 tech possibilities they hold. Don't miss out on this fascinating read! 🚀💬 #GenerativeAI #TechWonders 
```
---

     
 
all -  [ Hey guys, I have a MongoDB with hundreds thousands of data needed to be processed by GPT API anyone  ](https://www.reddit.com/r/node/comments/16sq2lk/hey_guys_i_have_a_mongodb_with_hundreds_thousands/) , 2023-09-27-0910
```
A little bit in detail, I thought of splitting the data into chuncks but didn't get promising GPT result, then someone s
uggested using Pinecone so wondering does it really could help in this situation? on the long-run thinking of using LLM 
by LangChain to minimum the cost and time of GPT and make some models learn and predict the question.   


Thanks.
```
---

     
 
all -  [ RAG on User-Manuals(PDFs with images, text) ](https://www.reddit.com/r/LangChain/comments/16sm5tk/rag_on_usermanualspdfs_with_images_text/) , 2023-09-27-0910
```
I have a use case of RAG, wherein I have some user manuals of a application. These user manual pdfs contains texts and i
mages, icons of button, etc. I want to make an RAG application on these manual, display the images in output based on co
ntext(if not possible, maybe some mechanism to keep a link and display that)? Any suggestion would be really helpful. Th
anks. 
```
---

     
 
all -  [ Langchain with Local LLM ](https://www.reddit.com/r/LangChain/comments/16sln73/langchain_with_local_llm/) , 2023-09-27-0910
```
Is Langchain framework only built for openAI LLM? Any one who have tested langchain agents with other open source models
.

I’m struggling with llama2+ langchain.
```
---

     
 
all -  [ [Question] Query to list all stored documents (or rather their summaries) ](https://www.reddit.com/r/LangChain/comments/16shh5s/question_query_to_list_all_stored_documents_or/) , 2023-09-27-0910
```
Let's say I have a document database of recipes (not too many, 10 maximum). I want to query GPT with a prompt like 'Whic
h recipes do you have?', i.e. a query to list all documents. How can I achieve this behavior with LangChain (or a simila
r tool)?

One direction of thought I have so far: Create a short summary or title with GPT every time a new recipe is st
ored as metadata and when such a query comes in return all the summaries.
```
---

     
 
all -  [ Error with Flan-XL model endpoint? ](https://www.reddit.com/r/aws/comments/16sgq5b/error_with_flanxl_model_endpoint/) , 2023-09-27-0910
```
Following [this blog](https://aws.amazon.com/blogs/machine-learning/quickly-build-high-accuracy-generative-ai-applicatio
ns-on-enterprise-data-using-amazon-kendra-langchain-and-large-language-models/) and got my flan-xl endpoint up, along wi
th my kendra index. All good- but when I try to run the [samples here](https://github.com/aws-samples/amazon-kendra-lang
chain-extensions/tree/main/kendra_retriever_samples) (link is from the blog above) I get an error.  Streamlit works okay
, I get an html page with input field, but any request produces this error:

    ValueError: Error raised by inference e
ndpoint: An error occurred (ModelError) when calling the InvokeEndpoint operation: Received client error (422) from prim
ary with message 'Failed to deserialize the JSON body into the target type: missing field `inputs` at line 1 column 5161
'. See https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEventViewer:group=/aws/sagemaker/End
points/huggingface-pytorch-tgi-inference-2023-09-26-00-36-58-657 in account XXXXXXXX for more information.

I'm running 
this from VSCode using git bash as terminal. AWS cli is installed, configured, and access was verified. Any help appreci
ated!!!
```
---

     
 
all -  [ LLM Performance (Llama2 vs Opena AI) ](https://www.reddit.com/r/LangChain/comments/16se9vv/llm_performance_llama2_vs_opena_ai/) , 2023-09-27-0910
```
Hi , this poll is for folks who have tested LLM for their use case. Just want to understand a bigger picture which LLM d
o you prefer if you have same budget for both?

[View Poll](https://www.reddit.com/poll/16se9vv)
```
---

     
 
all -  [ ChromaDB advantages? ](https://www.reddit.com/r/LangChain/comments/16s9vc5/chromadb_advantages/) , 2023-09-27-0910
```
Noticed that few LLM github repos are using chromadb instead of milvus, weaviate, etc. any particular advantage of using
 this vector db?
```
---

     
 
all -  [ JsonAgent beyond semantic search? ](https://www.reddit.com/r/LangChain/comments/16s8kd5/jsonagent_beyond_semantic_search/) , 2023-09-27-0910
```
New to Langchain, I’ll try my best to explain the issue.

I am building a chat app that answers the prompt based on the 
metadata file in json form.

I am currently using JsonAgent to overcome token limit issue (the file is fairly large) but
 what I realize is the json agent can only answer strictly what’s in the json file and nothing else.

For example, say t
he json file contains {“2019”: [{“sales”: “1 million”}]}, the agent seems never be able to answer beyond “Sales record i
n 2019 is 1 million” just repeating what’s exactly in the file. I want it to be able to answer a question like “compare 
the sales revenue in 2019 to the hospitality industry average in the same year.” As if the model uses its own trained kn
owledge as well as the provided info.

Is there any way to achieve this outcome? I’m using gpt4-32k.
```
---

     
 
all -  [ What is the cleanest way to use agents with chat history? ](https://www.reddit.com/r/LangChain/comments/16s55pp/what_is_the_cleanest_way_to_use_agents_with_chat/) , 2023-09-27-0910
```
I want to have an agent that behaves like a default chatGPT bot, except when he needs specific knowledge. I’d also prefe
r to use the chatGPT prompt structure with system, assistant and user prompt. 

What would be the cleanest way to approa
ch this problem? If I use the default conversational agent, it will only send a single large prompt including the histor
y.
```
---

     
 
all -  [ Just started a Discord server for developers building with AI ](https://www.reddit.com/r/LangChain/comments/16rr2w8/just_started_a_discord_server_for_developers/) , 2023-09-27-0910
```
I've been looking for a community of developers who work with AI but couldn't find the right one. Most of the communitie
s I've found are either focused on AI/ML research or using AI tools for general use cases. I was thinking a place where 
people could share things like their experiences playing around with a new version of an LLM API or other small experime
nts. 

Basically a server for regular devs (rather than hardcore AI/ML researchers, although they are welcome too) who h
ave started building with AI.   


Hope to see you there! [https://discord.gg/EfvA2MNfwt](https://discord.gg/EfvA2MNfwt)

```
---

     
 
all -  [ Does LangchainJS support Azure Cognitive Search as a Vector Storage? ](https://www.reddit.com/r/LangChain/comments/16rq5l8/does_langchainjs_support_azure_cognitive_search/) , 2023-09-27-0910
```
Hello Langchain enthusiasts!

I've just joined this community and am thrilled to be a part of it. 🎉

I have a specific q
uestion that I couldn't find an answer to in the docs:   
Does LangchainJS support Azure Cognitive Search as a Vector St
orage?  
 I've been looking for an SDK or a dedicated module for it but came up short.

If anyone has any insights or wo
rkarounds, please let me know. Your help would be greatly appreciated!

Looking forward to diving deeper into Langchain 
with all of you. Thanks in advance!
```
---

     
 
all -  [ Streaming Tokens from LLMChain ](https://www.reddit.com/r/LangChain/comments/16rmibe/streaming_tokens_from_llmchain/) , 2023-09-27-0910
```
I don't know if I am just doing this wrong, but I am having trouble streaming the response from a LLMChain.

```
### Imp
orts ###

...

class CustomCallback(AsyncCallbackHandler):
    async def on_llm_new_token(
        self,
        token: 
str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> None
:
        print('token:', token)


llm = ChatOpenAI(temperature=0, verbose=True)

prompt_template = ChatPromptTemplate.f
rom_messages(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessagePromptTemplate.from_te
mplate('{input}'),
        ]
    )

llm_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

user_input = 'W
hat is the meaning of life?'


async def main():
    queue = asyncio.Queue()
    callback = CustomCallback(queue)
    re
sult = await llm_chain.arun(user_input, callbacks=[callback])
    # result = await llm_chain.agenerate([{'input': user_i
nput}])


    print(result)

```

I have been trying to get this callback to print all of the streaming responses from t
he LLM to no avail, as I can only get the response after the entire response from OpenAI is sent to me. This works perfe
ctly fine when I have just a normal LLM that I call agenerate on, I just wanted to use LLMChain to abstract away some of
 the prompting, but this doesn't seem like it works.
```
---

     
 
all -  [ Looking for pre-trained Embedding model that does well on network logs ](https://www.reddit.com/r/LangChain/comments/16rlqpm/looking_for_pretrained_embedding_model_that_does/) , 2023-09-27-0910
```
Hi, I'm working on RAG on Network Logs.  
Having trouble with the retrieval part as the embedding model I'm currently us
ing doesn't retrieve logs based on user prompt similarity.  

```
---

     
 
all -  [ Versioning and Iterating on Prompts ](https://www.reddit.com/r/LangChain/comments/16rdduy/versioning_and_iterating_on_prompts/) , 2023-09-27-0910
```
how do you currently version prompts? I put them into a config file that I can use but curious if people have tried anyt
hing else. I tried prompt layer but the UI feels clunky and the playground only helps me test single prompts. 

what do 
you think about a config file that interops with a more robust playground that shows you the chain? kinda like a .ipynb 
to juptyer notebook model. 
```
---

     
 
all -  [ Pass user's question to Langchain agent tools ](https://www.reddit.com/r/LangChain/comments/16r69i2/pass_users_question_to_langchain_agent_tools/) , 2023-09-27-0910
```
Is there a way that I can pass end-user's question to the tool registered with langchain agent (Conversational React des
cription agent type) without any modification? 

For example, if a user asks question - How many employees are there?

B
elow is what I see from langchain agent - 

```
Do I need to use a tool? Yes

Action: EmployeeRecords

Action Input: cou
nt employees
```


As you can see, action input does not directly pass user's question. This is an issue as I need compl
ete question passed as input to the tool in order to generate SQL. 

Open to any other alternative solution as well. Tha
nks!
```
---

     
 
all -  [ How do I log and read the LLM queries and responses my chatbot is sending ? ](https://www.reddit.com/r/LangChain/comments/16qzmka/how_do_i_log_and_read_the_llm_queries_and/) , 2023-09-27-0910
```
I am following the great tutorial here https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/6/question-ans
wering and he is using langsmith to parse through his queries and calls to the LLM.

Unfortunately, langsmith is in clos
ed private beta and I cannot get an API key.  What is another technique for parsing through the text sent to the LLM?  I
 am not quite sure what part of langchain to look at.
```
---

     
 
all -  [ Using a remote retreiver on Langchain ! ](https://www.reddit.com/r/LangChain/comments/16qwiri/using_a_remote_retreiver_on_langchain/) , 2023-09-27-0910
```
Hi there,

I'm setting up an ask documentation using llama2 with langchain.I discovered I also needed an embedding model
 while building my RetrievalQA chain.My issue is that I don't have enough VRAM on one GPU to host the LLM and the embedd
ing model.But I have two GPU on two different Hosts, and I was wondering if it was possible to have a retriever server, 
and a client using this server to build the RetrievalQA.

This is the way I create my RetrievalQA, but I haven't found a
 way to have a decoupled retriever and QA chain.

    RetrievalQA.from_chain_type(llm=llm, 
    chain_type='stuff', retr
iever=ret, return_source_documents=True, callbacks=cb, chain_type_kwargs={'prompt': prompt,},)

Thx in advance if u have
 any clue.
```
---

     
 
all -  [ How do you make a Vector DB where the search and meta data are different? ](https://www.reddit.com/r/LangChain/comments/16qtjj3/how_do_you_make_a_vector_db_where_the_search_and/) , 2023-09-27-0910
```
I would like the similarity search to only find the most relevant heading and then use the data that is stored under the
 heading. Any smart ideas?
```
---

     
 
all -  [ Tooling ChatGPT ](https://www.reddit.com/r/learnpython/comments/16ql52d/tooling_chatgpt/) , 2023-09-27-0910
```
Tooling AI

Hello Everyone,

I have been working on using ChatGPT for taking  a users request categorizing this and goin
g to a hard coded API pull to request data and it works quite well.  This issue is I am dealing with around 32 API endpo
ints with users who could ask the same questions a million different ways.  For example,  user could ask for data from a
 week ago or this last month or a ton of different ways.

I wanted the AI to be smart enough to use agents and tools to 
go grab the API endpoints by me showing the full API to the LLM.  I have been using Langchain but it’s buggy and the doc
umentation it’s always current.

Does anyone know of a full flushed out library I can utilize or have something on GitHu
b that they would recommend.  I am also open to general help with this.
```
---

     
 
all -  [ Resume review for Data Science and Machine Learning roles ](https://www.reddit.com/r/resumes/comments/16qgj6m/resume_review_for_data_science_and_machine/) , 2023-09-27-0910
```
Hi, I am a recent grad with a Masters in ECE. I have applied for more than 1000 positions and received less than 10 inte
rviews so far. For most of the positions, I just receive a recruiter call. There was this one position that I received a
 verbal offer but they declined it afterwards. Also, I am applying for jobs in both the US and Canada as I am a Canadian
 Permanent Resident. I keep my address of the respective country where the job is based and I don't include the line Can
adian Permanent Resident for US roles. I need some advice, what can I change in the resume to improve my chances to land
 more interviews.  
Thanks in Advance

https://preview.redd.it/t0gis7nav2qb1.png?width=1338&format=png&auto=webp&s=40b10
52baddf8c4692e5bb67b0fde8d61f839971
```
---

     
 
all -  [ Found a great beginner LangChain Tutorial and generated an article about it! Check it out. ](https://www.reddit.com/r/LangChain/comments/16qau85/found_a_great_beginner_langchain_tutorial_and/) , 2023-09-27-0910
```
I found this great tutorial on LangChain that helped me generate an a title to an outline to an article in a python scri
pt.

What do you think of it? Do you have other tutorials you can recommend that helped you learn?

[https://www.learnin
ternetgrow.com/guide-to-langchain-chains-and-applications/](https://www.learninternetgrow.com/guide-to-langchain-chains-
and-applications/)
```
---

     
 
all -  [ Found a great beginner LangChain Tutorial and generated an article about it! Check it out. ](https://www.reddit.com/r/pythontips/comments/16qat7v/found_a_great_beginner_langchain_tutorial_and/) , 2023-09-27-0910
```
I found this great tutorial on LangChain that helped me generate an a title to an outline to an article in a python scri
pt.  
What do you think of it? Do you have other tutorials you can recommend that helped you learn?  
https://www.learni
nternetgrow.com/guide-to-langchain-chains-and-applications/
```
---

     
 
all -  [ Embedding with Llama-cpp seems to have issues ](https://www.reddit.com/r/LangChain/comments/16q9b5b/embedding_with_llamacpp_seems_to_have_issues/) , 2023-09-27-0910
```
    from langchain.document_loaders import WebBaseLoader
    from langchain.embeddings import LlamaCppEmbeddings
    fro
m langchain.vectorstores import Chroma
    
    llama = LlamaCppEmbeddings(model_path='../models/openorca_stx.gguf')
   
 
    loader = WebBaseLoader('https://www.bbc.com/')
    pages = loader.load()
    
    vectordb = Chroma.from_documents
(
        documents=pages,
        embedding=llama,
        persist_directory='../data/vectorstores/'
    )

&#x200B;

d
epending on the page i want to load i get this error:

&#x200B;

&#x200B;

    ValueError                               
 Traceback (most recent call last)
    p:\git_repos\langchain-test\src_langchain\04_vectorstore.ipynb Cell 4 line 5
    
      1 from langchain.vectorstores import Chroma
          3 persist_directory = '../data/vectorstores/'
    ----> 5 ve
ctordb = Chroma.from_documents(
          6     documents=pages,
          7     embedding=llama,
          8     persis
t_directory=persist_directory
          9 )
    
    File d:\miniconda3\envs\langchain\Lib\site-packages\langchain\vecto
rstores\chroma.py:646, in Chroma.from_documents(cls, documents, embedding, ids, collection_name, persist_directory, clie
nt_settings, client, collection_metadata, **kwargs)
        644 texts = [doc.page_content for doc in documents]
        
645 metadatas = [doc.metadata for doc in documents]
    --> 646 return cls.from_texts(
        647     texts=texts,
    
    648     embedding=embedding,
        649     metadatas=metadatas,
        650     ids=ids,
        651     collectio
n_name=collection_name,
        652     persist_directory=persist_directory,
        653     client_settings=client_sett
ings,
        654     client=client,
        655     collection_metadata=collection_metadata,
        656     **kwargs,

    ...
    --> 510 self.input_ids[self.n_tokens : self.n_tokens + n_tokens] = batch
        511 # Save logits
        5
12 rows = n_tokens if self.params.logits_all else 1
    
    ValueError: could not broadcast input array from shape (8,)
 into shape (0,)

[example.org](https://example.org) works fine, anything more complex throws this error message.I reall
y hope to use llama-cpp. GPT4ALL Models are outdated.
```
---

     
 
all -  [ Is LangChain the right choice for what Im Creating? ](https://www.reddit.com/r/LangChain/comments/16q7dbp/is_langchain_the_right_choice_for_what_im_creating/) , 2023-09-27-0910
```
I'm interested in being able to prompt an AI model that can reference and pull data  from custom databases tailored to s
pecific interests. For instance, if one  user is interested in books, the AI would generate info based on a  database of
 book titles and authors. Meanwhile, another user interested  in cars would get info generated from a database of car mo
dels and  specs. Essentially, the AI should be able to dynamically switch between  different databases based on user pre
ferences. Has anyone had experience  integrating such a system with Bubble or can recommend a  solution/platform that al
lows for this kind of interest specific integration? Any Thoughts would be helpful!
```
---

     
 
all -  [ Running LLaMa on Google Colab/cloud differences w.r.t local system ](https://www.reddit.com/r/LocalLLaMA/comments/16q0fhc/running_llama_on_google_colabcloud_differences/) , 2023-09-27-0910
```
So I have downloaded the quantized LLaMa 7B model from huggingface which I can run on my local system (but takes a long 
time). The way I am doing it is, I have the model in one of my folders and I am calling the model from there using the l
angchain module in Python.

I tried to do the same thing on Colab where I mounted my Google Drive, copied the model from
 Google Drive to Google Colab and changed the location of model from my local drive to the filepath of bin file in Colab
.

But then I keep getting error:

    ---------------------------------------------------------------------------
    A
ssertionError                            Traceback (most recent call last)
    <ipython-input-28-02e71e2eb370> in <cell 
line: 5>()
          3 # llm = LlamaCpp(model_path = '/content/gdrive/MyDrive/OpenLLM/LLaMa_7B/llama-7b.ggmlv3.q3_K_M.bi
n')
          4 
    ----> 5 llm = Llama(model_path = '/content/gdrive/MyDrive/OpenLLM/Alpaca_7B/ggml-alpaca-7b-q4.bin')

          6 
          7 # embeddings = LlamaCppEmbeddings(model_path = llama_model_path + 'llama-7b.ggmlv3.q3_K_M.bin'
)
    
    /usr/local/lib/python3.10/dist-packages/llama_cpp/llama.py in __init__(self, model_path, seed, n_ctx, n_batch
, n_gpu_layers, main_gpu, tensor_split, rope_freq_base, rope_freq_scale, low_vram, mul_mat_q, f16_kv, logits_all, vocab_
only, use_mmap, use_mlock, embedding, n_threads, last_n_tokens_size, lora_base, lora_path, numa, verbose, **kwargs)
    
    338                     self.model_path.encode('utf-8'), self.params
        339                 )
    --> 340      
   assert self.model is not None
        341 
        342         if verbose:
    
    AssertionError: 

So I wanted to 
know what are some of the nuances which I need to keep in mind while running on local system vs. Google Colab or cloud l
ike AWS, Azure etc. Is it not possible to place the model in a bucket/folder on cloud and then call it like on local sys
tem?

I am fairly new to open source LLMs and giving it a try for the first time. I have worked with openAI APIs for Cha
tGPT but that doesn't include all these additional things and I want to expand my knowledge on the same.

Thanks in adva
nce.
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-09-27-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-09-27-0910
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-09-27-0910
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-27-0910
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-27-0910
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-27-0910
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-27-0910
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-27-0910
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-09-27-0910
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-27-0910
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
