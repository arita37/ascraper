 
all -  [ What's the standard practice for setting initialization prompts and maintaining context when switchi ](https://www.reddit.com/r/OpenAIDev/comments/1aq79ab/whats_the_standard_practice_for_setting/) , 2024-02-14-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation, the app 
can seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5):
 1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response

4. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the
 standard practice for setting the initialization prompts or background prompts? For example I want to tell this App tha
t 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has got
ten or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2
. What's the standard practice for conversation memory management when there's switching of LLM involved within one conv
ersation? Do I store all the conversation history within a vector database and do a index search prior to any individual
 response?
```
---

     
 
all -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-14-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation the app c
an seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5): 
1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response
4
. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the 
standard practice for setting the initialization prompts or background prompts? For example I want to tell this App that
 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has gott
en or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2.
 What's the standard practice for conversation memory management when there's switching of LLM involved within one conve
rsation? Do I store all the conversation history within a vector database and do a index search prior to any individual 
response?
```
---

     
 
all -  [ What is AI Observability ](https://www.reddit.com/r/AIObservability/comments/1aq6hxm/what_is_ai_observability/) , 2024-02-14-0909
```
Let's say there was an example Q&A bot powered by a large language model created by a coffee company to enage their cust
omers more effectively. A user's question such as 'what's a latte?' kicks off a workflow that identifies relevant conten
t from a knowledgebase about coffee using an embedding model and passes this context to a large language which then summ
arizes the content in a brief natural response.

In an sample deployment, the workflow could be implemented as a python 
program coded using LangChain framework and the embedding & language models are obtained from Huggingface. Workflow is s
erved up using Azure ML and the models are served using Nvidia Triton inference server hosted on kubernetes service in A
zure.

AI observability would require capturing and correlating metrics from across the LLM app components and the AI in
fra services used to run these components to understand what impacts performance and how to best optimize it.
```
---

     
 
all -  [ What can we do about user spam? ](https://www.reddit.com/r/LangChain/comments/1aq5n46/what_can_we_do_about_user_spam/) , 2024-02-14-0909
```
I’m implementing an agent to hopefully trial with some of our current users via WhatsApp and realized that users could e
asily spam messages to get a response, thus unnecessarily increasing our costs by calling some api to return a model’s r
esponse.

What strategies could someone implement to to tackle this issue?
```
---

     
 
all -  [ Introductory courses that aren't video based? ](https://www.reddit.com/r/LangChain/comments/1aq2xzl/introductory_courses_that_arent_video_based/) , 2024-02-14-0909
```
Management at my customer service job has given the green light to work on continuing education classes when it's slow. 
I'm looking for some introductory classes I can take that are text based as I cannot watch videos during my shift. Does 
anyone know of some course options that are read along only with no video component?
```
---

     
 
all -  [ Is there a way to store Vectorstores? ](https://www.reddit.com/r/LangChain/comments/1aq2nvr/is_there_a_way_to_store_vectorstores/) , 2024-02-14-0909
```
Hi, I am building a vectorstore using `Chroma.from_documents` of textual data. Because my dataset is large, the number o
f chunks is high and hence it takes a long time to create the vector store. What is the best way to - a) parallelize it.
 and b) store it so I don't have to do it every time I run my notebook?
```
---

     
 
all -  [ Deployment template for running LangServe on AWS Fargate ](https://www.reddit.com/r/LangChain/comments/1aq19oe/deployment_template_for_running_langserve_on_aws/) , 2024-02-14-0909
```
A template to deploy your LangChain app running locally to the cloud. This architecture specifically packages LangServe 
into a Docker image, stores the image in ECR, and runs the container in AWS Fargate with an ALB in front.

[langserve\_r
eference\_architecture](https://preview.redd.it/flzjgv5wfeic1.png?width=6079&format=png&auto=webp&s=b5a5d4ab4330d435cdf1
4d43f1a3f5487a8577ff)

The template comes in Python, Typescript, Golang, C#, YAML. It uses OpenAI for the LLM.

Read the
 [blog post](https://www.pulumi.com/blog/easy-ai-apps-with-langserve-and-pulumi) to follow along with the two examples: 
a Gandalf chatbot and a Pinecone RAG app. Let me know if you have any questions or if you would like to see any other ki
nd of template.
```
---

     
 
all -  [ Is this possible? ](https://www.reddit.com/r/generativeAI/comments/1apz09f/is_this_possible/) , 2024-02-14-0909
```
Hi, newbie to GenAI here. 

I wanted to know if we can download open source GenAI models and use them in an isolated env
ironment by fine tuning them to retrieve needed data and answer the questions asked based on it. 

I've started to learn
 LangChain and ig we can do that using it. If the whole system needs to be on cloud, how do we  basically host this whol
e thing?

Will there be any security issues like some leakage points in the downloaded model itself such that it steals 
data from us?

I need to make a POC for clients like media or law firms. 

Any input or suggestions will be helpful and 
appreciated. Thanks.
```
---

     
 
all -  [ Using Vertex AI Model Garden with Langchain ](https://www.reddit.com/r/LangChain/comments/1apwigv/using_vertex_ai_model_garden_with_langchain/) , 2024-02-14-0909
```
I am trying to use Vertex AI Model Garden for inference with Langchain. I have successfully deployed Mistral to an endpo
int in Google Cloud and want to get inference with the class VertexAIModelGarden which is already implemented. However, 
it seems the output returned by the endpoint is not correctly parsed as it only contains a single character (see image).


I found a pull request on the langchain github repo that mentions this issue and there is a link to another repo where
 someone has implemented a temporary fix ( [https://github.com/shikanime/langchain-vertexai-extended](https://github.com
/shikanime/langchain-vertexai-extended) ). I tried using this code and it seems to work but I was wondering if anyone el
se had this issue and if this 'fix' will eventually be included in Langchain. Furthermore, the stream method is not yet 
supported in this fix so we can just use the invoke. 

&#x200B;

https://preview.redd.it/lekh5bkvgdic1.png?width=1290&fo
rmat=png&auto=webp&s=cc51b00326ae91a98b3b5f6ee958129d61f3192f
```
---

     
 
all -  [ GPT4ALL function calling ](https://www.reddit.com/r/LangChain/comments/1aputis/gpt4all_function_calling/) , 2024-02-14-0909
```
I know there is this support for function calling for models like [OpenAI](https://python.langchain.com/docs/modules/mod
el_io/chat/function_calling) but is this also supported in the GPTAALL?
```
---

     
 
all -  [ Preparing model for production ](https://www.reddit.com/r/LangChain/comments/1apu4ml/preparing_model_for_production/) , 2024-02-14-0909
```
Hi, I have wrote a chat model based on huggingface inference through langchain, and I would like to prepare it for produ
ction. 

My scope is kinda small as I am aiming to host it locally in WAMP/XAMP or AWS server to be used as demonstratio
n of the app.  

I was able to find few API explanations out there but it is quite unclear hence it is my very first imp
lementation in such context.

I tried Writing a Flash app and prepare few files one that has Flash api calla, the second
 one has the code structure for the app (starting with package importing and ending with response), and the last file ha
s all the functions that I am using in my second file that preprocess and handle data.

I'm left wondering on one questi
on is that the model and memory initialization and construction is in the second file, which leave me wondering how the 
memory of the chat model is going to persist when the user query it multiple queries within the same interaction.
```
---

     
 
all -  [ LangChain playlist with 60 tutorials ](/r/learnmachinelearning/comments/1ap1uy7/langchain_playlist_with_60_tutorials/) , 2024-02-14-0909
```

```
---

     
 
all -  [ Please give tips can't get any internship ,sophomore at tier 3 ](https://i.redd.it/qnje7e0h1cic1.jpeg) , 2024-02-14-0909
```
Suggestions or any advice on resume are appreciated 🙂
```
---

     
 
all -  [ Ollama sequential behaviour ](https://www.reddit.com/r/LangChain/comments/1apq6ql/ollama_sequential_behaviour/) , 2024-02-14-0909
```
Hey,   
I was exploring the Ollama library to serve the mistral model, I came into a case where the model was serving a 
single request at a time. 

i.e. Scenario: Simultaneous requests from two or more machines were served by the model on a
 first come first serve basis. Expected behavior: Serve multiple requests simultaneously.  


If the expected behavior i
s possible, guide me through the process.
```
---

     
 
all -  [ How can I use LangChain to filter through files in a directory given some filters ](https://www.reddit.com/r/LangChain/comments/1apq229/how_can_i_use_langchain_to_filter_through_files/) , 2024-02-14-0909
```
Im trying to mass filter through a windows directory given filters such as date, file type, and other important keywords
, is there any python library or langchain system that can filter using some basic filters like these? I have tried indi
vidually going file by file and running a loader but it takes forever and is quite cost intensive.
```
---

     
 
all -  [ How to use Hugging Face models ? Specify resources. ](https://www.reddit.com/r/ArtificialInteligence/comments/1app63v/how_to_use_hugging_face_models_specify_resources/) , 2024-02-14-0909
```
Guys I'm totally a beginner, idk anything about hugging face models, langchain,and i don't know how to use Api's . Sugge
st me Some resources to learn How to make use of open source models form hugging face.i know some basic python.
```
---

     
 
all -  [ Got out of SAP. Now working with proper desired tech stack. ](https://www.reddit.com/r/developersIndia/comments/1apne2r/got_out_of_sap_now_working_with_proper_desired/) , 2024-02-14-0909
```
This post is a continuation of my [previous post](https://www.reddit.com/r/developersIndia/s/MrnXDtOU5W). The company wh
ich I interviewed called me back after 3 weeks of my interview for the HR round. Got selected. Took an early release fro
m the previous company and joined my new company in December. 

The new company is in my hometown. Colleagues are friend
ly. Work is interesting and challenging. Also, as a bonus, I get free food as lunch.

I am a little confused on what job
 role exactly I am working (I know the designation but that is a company issued designation). 

I am/will working/work i
n AI (researching, training, creating models if needed), generative AI, langchain, also, I am building backend in my cur
rent project fully in Django (I also made the frontend too for my learning purpose and there were no other person to do 
that since this project was assigned to me only do that I can learn on my own, but my team that I'm assigned to has a fr
ontend developer).

Can anyone tell me what my job role is so that I can properly mention that in my resume?


Thank you
 in advanced.
```
---

     
 
all -  [ How can I get the embedding of a document in langchain? ](https://www.reddit.com/r/LangChain/comments/1aph0v8/how_can_i_get_the_embedding_of_a_document_in/) , 2024-02-14-0909
```
I use the langchain Python lib to create a vector store and retrieve relevant documents given a user query. How can I ge
t the embedding of a document in the vector store?

E.g., in this code:

    import pprint
    from langchain_community.
vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain.docsto
re.document import Document
    
    model = 'sentence-transformers/multi-qa-MiniLM-L6-cos-v1'
    embeddings = HuggingF
aceEmbeddings(model_name = model)
    
    def main():
        doc1 = Document(page_content='The sky is blue.',    metad
ata={'document_id': '10'})
        doc2 = Document(page_content='The forest is green', metadata={'document_id': '62'})
 
       docs = []
        docs.append(doc1)
        docs.append(doc2)
    
        for doc in docs:
            doc.metad
ata['summary'] = 'hello'
    
        pprint.pprint(docs)
        db = FAISS.from_documents(docs, embeddings)
        db
.save_local('faiss_index')
        new_db = FAISS.load_local('faiss_index', embeddings)
    
        query = 'Which colo
r is the sky?'
        docs = new_db.similarity_search_with_score(query)
        print('Retrieved docs:', docs)
        
print('Metadata of the most relevant document:', docs[0][0].metadata)
    
    if __name__ == '__main__':
        main()




---

How can I get the embedding of documents `doc1` and `doc2`?


The code was tested with Python 3.11 with:

```
p
ip install langchain==0.1.1 langchain_openai==0.0.2.post1 sentence-transformers==2.2.2 langchain_community==0.0.13 faiss
-cpu==1.7.4
```
```
---

     
 
all -  [ Whats in your RAG setup? ](https://www.reddit.com/r/LocalLLaMA/comments/1apcqq4/whats_in_your_rag_setup/) , 2024-02-14-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
all -  [ Whats your RAG setup? ](https://www.reddit.com/r/LLMDevs/comments/1apcmxt/whats_your_rag_setup/) , 2024-02-14-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;

&#x200B;

```
---

     
 
all -  [ LlamaIndex or LangChain with LlamaIndex for RAG with documents ](https://www.reddit.com/r/LocalLLaMA/comments/1ap7hrt/llamaindex_or_langchain_with_llamaindex_for_rag/) , 2024-02-14-0909
```
My goal is to create a chatbot to do Q&As with documents. Do I need to learn both LangChain and LlamaIndex? Or just Llam
aIndex would be sufficient? In other words, for my intended applications, what will I miss if I just use LlamaIndex with
out LangChain? Thanks.
```
---

     
 
all -  [ Just found ctransformers doesn't work with Tokenizer ](https://www.reddit.com/r/LocalLLaMA/comments/1ap5xgl/just_found_ctransformers_doesnt_work_with/) , 2024-02-14-0909
```
I was looking for how to get the tokenizer from a GGUF model and realized it (almost) doesn't actually work.

Came acros
s this documentation on ctransformers ([https://pypi.org/project/ctransformers/#langchain](https://pypi.org/project/ctra
nsformers/#langchain)):

 

>To use it with 🤗 Transformers, create model and tokenizer using:  
>  
>`from ctransformers
 import AutoModelForCausalLM, AutoTokenizer model = AutoModelForCausalLM.from_pretrained('marella/gpt-2-ggml', hf=True) 
tokenizer = AutoTokenizer.from_pretrained(model)` 

I thought: 'Sweet, that's pretty easy!' But when I run it, `AutoToke
nizer.from_pretrained(model)` throws NotImplementedError.

https://preview.redd.it/66ic68kbw6ic1.png?width=1660&format=p
ng&auto=webp&s=a7652d0e36fc43882ec98957183f2c9c1a93d27f

  
Further search led me to [https://github.com/marella/ctransf
ormers/issues/184](https://github.com/marella/ctransformers/issues/184), which is this exact issue raised on ctransforme
rs repo back in Dec 2023. I haven't tried this but according to this the only solution is to downgrade transformers lib 
to 4.33, which rips a lot of features off. Also it looks like the not implemented error has been there all the time. Not
 sure what caused that breakage.

Just want to share my findings since it's pretty disappointing to find that such basic
 function is not working :(
```
---

     
 
all -  [ Control token size of a tool ](https://www.reddit.com/r/LangChain/comments/1ap2rr3/control_token_size_of_a_tool/) , 2024-02-14-0909
```
I have an agent which uses a custom tool to search and provide an output, my problem. Is many times the output of the to
ol which is being passes to. The llm surpasses the token limit, is there away to chunk the output of the tool and gather
 the responses and send the whole responses to the user?
```
---

     
 
all -  [ LangChain playlist with 60 tutorials ](https://www.reddit.com/r/learnmachinelearning/comments/1ap1uy7/langchain_playlist_with_60_tutorials/) , 2024-02-14-0909
```
Hey everyone, check out this LangChain (generative AI framework) playlist comprising of 60 tutorials explaining everythi
ng from scratch
https://youtube.com/playlist?list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ&si=8bXhqED-NiVITZK9
```
---

     
 
all -  [ Agents vs Chains ](https://www.reddit.com/r/generativeAI/comments/1ap1hf2/agents_vs_chains/) , 2024-02-14-0909
```
Hey everyone, check out how Agents are different from chains in LangChain in this new tutorial: https://youtu.be/A3Gm6KP
xy4k
```
---

     
 
all -  [ AI document jury ](https://www.reddit.com/r/LangChain/comments/1ap0pbx/ai_document_jury/) , 2024-02-14-0909
```
I need to make an AI that can judge a document based on some criteria. The criteria can be like:
- The document explains
 the market segmentation efficiently 
- The document mentions how market works and explaining each type of markets.

The
 AI will judge the document based on above criteria and will give a score. 
This is just a topic for example and the cri
teria and the document can be for other topics.

I have created a chatbot using RAG but for this one I still don't have 
a clue for the approach. Mainly because with chatbot, I retrieve like 5 nearest chunks by cosine similarity while for th
is one, I don't think retrieving nearest chunks by cosine similarity to the question will return all the chunks for the 
document part the criteria needs to judge. And I can't just give the LLM all chunks from the document right? Any advice 
for this one? Any help would be really appreciated.
```
---

     
 
all -  [ RAG Chatbot locally, beginner here ](https://www.reddit.com/r/LangChain/comments/1ap0fce/rag_chatbot_locally_beginner_here/) , 2024-02-14-0909
```
Hey, I'm a langChain beginner and I want to build an Chatbot application which will retrieve and run llm locally. I am u
sing Chroma to create and fetch from the vectorstore, and using Llama-7b for the llm. I want to use langserve and so i c
reate a server with the chain. I now will use streamlit to listen to that port and invoke the chain. I am stuck, because
 I am confused on how to store memory. I dont want to store it in the langchain server (as it would stored for every use
r the same. Correct me if I am wrong). So I want to store it in streamlit session state somehow and use buffer window in
 the langchain server. I am now very confused on what I should do. Need help, thanks!
```
---

     
 
all -  [ What happens if we send nodes again to chrome vector store ](https://www.reddit.com/r/LangChain/comments/1ap036k/what_happens_if_we_send_nodes_again_to_chrome/) , 2024-02-14-0909
```
If I have executed this code once and then run it again with different nodes. So what happens
1) does the new nodes get 
replaced by the older ones
2) it compares the new and older nodes and insert only those nodes that are new, keeping the 
older intact
3) it doesnt check and insert all the nodes(newer as well as older ones


import chromadb
chroma_client = c
hromadb.HttpClient(host='host', port=8000,)
from llama_index.vector_stores import ChromaVectorStore
from llama_index.pos
tprocessor.cohere_rerank import CohereRerank
chroma_collection = chroma_client.get_or_create_collection('collection')
ve
ctor_store6 = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context6 = StorageContext.from_defaults(vec
tor_store=vector_store6)
index7 = VectorStoreIndex(nodes=nodes, storage_context=storage_context6, service_context=servic
e_context)
```
---

     
 
all -  [ Website Scraping: Automatic CSS-Selector identification of the main textual content ](https://www.reddit.com/r/LangChain/comments/1aozqzh/website_scraping_automatic_cssselector/) , 2024-02-14-0909
```
The HTML code of many websites is very complicated. This is mainly because HTML is a markup language that is a mix of st
ructural, styling and text elements. It is also because many websites are overloaded with HTML tags and CSS instructions
. 

As a result, it can be a challenge to **identify the area** in the HTML code that represents **the main textual cont
ent** (e.g. for text extraction, vector databases or RAG applications).

In the following article, I show a **statistica
l-algorithmic approach** on how to determine the CSS selector(s) that represent the main content and filter out negligib
le elements.

https://developers-blog.org/python-website-scraping-automatic-selector-identification/

![enter image desc
ription here](https://developers-blog.org/wp-content/uploads/2024/02/visuzalisation-star-page-html-structure-and-depende
ncies-tree-54.png)
```
---

     
 
all -  [ Auto ai agent apps suggestion or something else? ](https://www.reddit.com/r/ChatGPT/comments/1aowboq/auto_ai_agent_apps_suggestion_or_something_else/) , 2024-02-14-0909
```
Please can you guide me towards a solution to learn for two projects?

**Request 1:**

**TLDR: Best easy UI app currentl
y for multi ai agent chained output to prompt auto workflow to assemble a larger prompt response output content (researc
h) document for each item line item (initia input to agent 1) in a google sheet or form input?**

Can you advise what is
 the easiest to use ai agent app with GUI that works on windows (python is ok if i must and ideally has some GUI but if 
there is an epic one without ill use it) to setup a step by step workflow easily that can take an initial input like a g
oogle sheet as the context and the first agent with use it plus its instructions and it will start its part of compiling
 a research report which is basically just prompt plus input and then sent result to the next agent who will use its out
put and their instructions to get more data and so on.   


So just steps and agents chained together one after the othe
r to fetch responses from the llm or their own tasks building on previous outputs, chatgpt API and I end up with a longe
r 5-10 page file of the output as a research report in chapters and it will do this report for each line in the google s
heet automatically and run as long as it needs to until its done? Like one of these? Autogen studio, Crewai, Chatdev, ai
agent dot app, llmstack, leapai. mindpal dot space has a nice multi agent assembly flow builder but no api input and out
put. Also something that can work with large documents well as inputs iedally for later project.

**Request 2:** **What 
is the best agent or bot large file handler/chat/processing app or stack where I can carefully auto scour multiple large
 documents and pull information from then all effectively** around a certain topic and create a long topic specific docu
ment for me just focused on the teaching on that subject pulled from the other large documents in a useful structured wa
y to make sense.

I guess agents that chat with eachother like a research project and it will make it easier as the data
 gets pulled in and they decide its context and where it must be in the new document and how its integrated with the res
t of the data pulled so far and then 1 but that keeps extracting new data from all the documents in a ongoing logical wa
y from the first to the last. Tried chat with do aps but output too small and cant automate workflows or multi agents.


What are the best tools for working with large documents currently, creating and extracting topical info for reseaand st
udy? Privategpt,, llama\_index, memgpt, langchain etc?

Thanks!
```
---

     
 
all -  [ Agent app suggestions please for 2 use cases ](https://www.reddit.com/r/AutoGPT/comments/1aovry9/agent_app_suggestions_please_for_2_use_cases/) , 2024-02-14-0909
```
Please can you guide me towards a solution to learn for two projects?

**Request 1:**

**TLDR: Best easy UI app currentl
y for multi ai agent chained output to prompt auto workflow to assemble a larger prompt response output content (researc
h) document for each item input item in a google sheet or form input?**

Can you advise what is the easiest to use ai ag
ent app with GUI that works on windows (python is ok if i must and ideally has some GUI but if there is an epic one with
out ill use it) to setup a step by step workflow easily that can take an inital input like a google sheet as the context
 and the first agent with use it plus its instructions and it will start its part of compiling a research report which i
s basically just prompt plus input and then sent result to the next agent who will use its output and their instructions
 to get more data and so on.   


So just steps and agents chained together one after the other to fetch responses from 
the llm or their own tasks building on previous outpits, chatgpt API and I end up with a longer 5-10 page file of the ou
tput as a research report in chapters and it will do this report for each line in the google sheet automatically and run
 as long as it needs to until its done? Like one of these? Autogen studio, Crewai, Chatdev, aiagent dot app, llmstack, l
eapai. mindpal dot space has a nice multi agent assembly flow builder but no api input and output. Also sometjing tha ca
n wrk with large documents well as inputs iedally for later project.

**Request 2:** **What is the best agent or bot lar
ge file handler/chat/processing app or stack where I can carefully auto scour multiple large documents and pull informat
ion from then all effectively** around a certain topic and create a long topic specific document for me just focused on 
the teaching on that subject pulled from the other large documents in a useful structured way to make sense.

I guess ag
ents that chat with eachother like a research project and it will make it easier as the data gets pulled in and they dec
ide its context and where it must be in the new document and how its integrated with the rest of the data pulled so far 
and then 1 but that keeps extracting new data from all the documents in a ongoing logical way from the first to the last
. Tried chat with do aps but output too small and cant automate workflows or multi agents.

What are the best tools for 
working with large documents currently, creating and extracting topical info for reseaand study? Privategpt,, llama\_ind
ex, memgpt, langchain etc?

Thanks!
```
---

     
 
all -  [ consistent memory ](https://www.reddit.com/r/Chatbots/comments/1aovrtd/consistent_memory/) , 2024-02-14-0909
```
Hello, I'm at the final steps in developing a chatbot using langchain, I'm facing a problem tho, when I run my chatbot o
n VS code, it forgets the previous conversation, however this does not happen on Jupyter Notebook, I've searched up and 
my problem might be variables consistency, is there a way to make it persistent in remembering previous conversation??  

If you guys think another problem might be the cause please tell me about it.  
Any help would be appreciated.  
Thanks
!
```
---

     
 
all -  [ Verbose for LCEL and for new agents (LangChain 0.1.0) ](https://www.reddit.com/r/LangChain/comments/1aovp1n/verbose_for_lcel_and_for_new_agents_langchain_010/) , 2024-02-14-0909
```
While working with LCEL and the newer way of handling agents in LangChain 0.1.0 i was wondering why verbose=true cant be
 set anymore. It was very useful for debugging and understanding the thought process of the agent. I know about the call
back handlers but i was wondering if there is a better and cleaner way, like the verbose=true in legacy LangChain.
```
---

     
 
all -  [ Search Product Catalog Images Using Azure Search and Azure OpenAI with LangChain ](https://www.reddit.com/r/AZURE/comments/1aovah9/search_product_catalog_images_using_azure_search/) , 2024-02-14-0909
```
 

In the ever-evolving landscape of retail, businesses are continually seeking innovative solutions to streamline their
 operations and enhance customer experiences. One such breakthrough is the implementation of artificial intelligence (AI
) to search product catalog images efficiently. This transformative technology not only simplifies the search process bu
t also empowers businesses to provide personalized and seamless shopping experiences for their customers. The Need for A
I in Product Catalog Image Search: Traditional methods of searching through product catalogs involve manual tagging and 
categorization, which can be time-consuming and prone to human error. As the volume of products in a catalog grows, mana
ging and searching for specific items becomes a daunting task.  
Here I have implemented a Fashion agent using Azure Sea
rch , Cognitive Services and GPT-4 with LangChain which can search product catalog to recommend write product to custome
r based on the requirement.  


[https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search
-and-openai-with-langchain-3a844bc5c27c](https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azur
e-search-and-openai-with-langchain-3a844bc5c27c)
```
---

     
 
all -  [ Journalist AI Review 2024 ](https://www.reddit.com/r/geniunereviewed/comments/1aouvr3/journalist_ai_review_2024/) , 2024-02-14-0909
```
&#x200B;

[Journalist AI Review 2024](https://preview.redd.it/wa4m5qez14ic1.png?width=1200&format=png&auto=webp&s=765739
b271e088a16269fc5dcdd845c38f8ff91c)

# Journalist AI Review 2024

**Journalist AI Review 2024: Hype or Hero?** Confused 
about Journalist AI's capabilities?\\

This in-depth review, based on thorough research, unravels its secrets.

Dive int
o its strengths, and weaknesses, and discover if it's your 2024 writing partner in crime!

**Key Takeaways:**

&#x200B;


* Journalist AI is an AI-powered writing tool designed to assist content creators, journalists, and marketers with gene
rating high-quality, SEO-optimized content.
* It offers features such as content generation in various formats, SEO opti
mization, image generation with Dall-e 3 integration, multilingual support through LangChain, and collaboration tools vi
a Google Docs integration.
* Pricing plans cater to individual and team needs, with varying content limits and feature a
ccess.
* User reviews highlight strengths like speed, efficiency, and high-quality output, but also mention potential we
aknesses in factual accuracy and creative control.

## Journalist AI Review 2024: Verdict

**Need fast, SEO-optimized co
ntent?** Journalist AI delivers, generating articles, blogs, and more. **Accuracy concerns linger,** so fact-checking is
 crucial. **Team features and image generation shine,** but limited creative control might leave some wanting more. **Id
eal for budget-conscious content creators comfortable with editing.** Explore alternatives for highly creative or techni
cal content. **Overall:** A helpful tool, but weigh your needs carefully before diving in.

[Try Journalist Ai Here](htt
ps://tryjournalist.com/?via=geniunereviewed)

## What is Journalist AI?

Journalist AI is an **AI-powered writing assist
ant** that leverages advanced algorithms to generate various content formats, including articles, blog posts, product de
scriptions, social media captions, and more. It is geared towards **content creators, journalists, marketers, and anyone
** seeking to **improve their content creation efficiency and quality**.

## Key Features of Journalist AI

Journalist A
I boasts a diverse range of features designed to empower users across the content creation spectrum. Let's explore some 
of the most notable ones:

### Content Generation

&#x200B;

* **Variety of formats:** Generate content in diverse forma
ts like articles, blog posts, product descriptions, social media captions, press releases, and more.
* **AI-powered writ
ing:** Advanced algorithms analyze your input (topic, keywords, tone) and generate unique, human-quality content.
* **Cu
stomizable style and tone:** Tailor your content to specific audiences and brand voices by adjusting the level of formal
ity, creativity, and humor.

### SEO Optimization

&#x200B;

* **Keyword research:** Identify relevant keywords to targe
t and optimize your content for search engine ranking.
* **Meta tag generation:** Automatically generate meta tags and d
escriptions that align with your target keywords.
* **Structured data markup:** Include structured data markup to enhanc
e search engine understanding and rich snippet visibility.

### Image Generation

&#x200B;

* **Dall-e 3 integration:** 
Leverage Dall-e 3's powerful AI to generate high-quality images that complement your content.
* **Contextual relevance:*
* Images are tailored to match your content's theme and topic for improved engagement.
* **Customization options:** Choo
se from various image styles and formats to suit your brand identity.

### Multilingual Support

&#x200B;

* **LangChain
 integration:** Translate your content into multiple languages seamlessly with LangChain's advanced translation technolo
gy.
* **Reach wider audiences:** Expand your reach to global audiences by creating multilingual content that resonates w
ith diverse cultures.
* **Quality assurance:** Maintain consistent messaging and brand voice across different languages.


### Collaboration Tools

&#x200B;

* **Google Docs integration:** Collaborate with team members in real-time by editin
g and providing feedback within Google Docs.
* **Streamlined workflows:** Facilitate seamless collaboration and content 
sharing within teams.
* **Improved efficiency:** Boost productivity by working together effectively on content projects.


## User Reviews and Testimonials (Continued)

**Positive reviews** of Journalist AI frequently highlight its:

&#x200B
;

* **Speed and efficiency:** Users appreciate the ability to generate content quickly and easily, saving them valuable
 time and effort.
* **High-quality output:** Many users commend the quality of the generated text, praising its natural 
language flow, grammar, and coherence.
* **Improved SEO:** Content creators value the built-in SEO optimization features
 that help their content rank higher in search results.
* **Easy to use interface:** The intuitive interface is lauded f
or its user-friendliness, making it accessible even for those with limited technical experience.

However, **negative re
views** sometimes mention:

&#x200B;

* **Factual accuracy:** Concerns exist regarding the potential for factual inaccur
acies, especially in technical or complex topics.
* **Limited creative control:** Some users feel restricted by the lack
 of fine-grained control over the creative aspects of the generated content.
* **Price:** While some find the pricing pl
ans affordable, others consider them expensive, especially for individuals or small businesses.
* **Customer support:** 
A few users express dissatisfaction with the quality or responsiveness of customer support.

It's important to remember 
that individual experiences can vary based on specific needs, expectations, and usage patterns. It's recommended to try 
the free plan or a trial period before committing to a paid subscription.

## Alternatives to Journalist AI

Several oth
er AI-powered writing tools compete with Journalist AI, each with its own strengths and weaknesses. Here are a few notab
le alternatives:

&#x200B;

* **Articoolo**: Offers a wider range of content formats and languages, but user reviews men
tion inconsistencies in quality.
* **Rytr**: Known for its affordability and user-friendly interface, but may lack custo
mization options compared to Journalist AI.
* **Writesonic**: Strong focus on long-form content and marketing copy, but 
pricing can be higher than Journalist AI.
* **Wordtune**: Primarily focused on rewriting and rephrasing existing content
, rather than generating original text.

Exploring these alternatives can help you find the best fit for your specific n
eeds and budget.

### Strengths and Weaknesses of Journalist AI

**Strengths:**

&#x200B;

* **Content quality:** Journa
list AI excels at generating grammatically correct, well-structured, and human-quality text that can serve as a solid fo
undation for further editing and refinement.
* **SEO optimization:** Built-in keyword research, meta tag generation, and
 structured data markup features effectively aid in content optimization for search engines, potentially boosting organi
c traffic.
* **Multilingual support:** Seamless integration with LangChain empowers content creators to reach global aud
iences by translating content into multiple languages, preserving brand voice and messaging.
* **Collaboration tools:** 
Google Docs integration streamlines team workflows, enabling real-time collaboration and feedback sharing, fostering con
tent creation efficiency.
* **Image generation:** Dall-e 3 integration offers a unique advantage, allowing users to crea
te high-quality, contextually relevant images that enhance content engagement and visual appeal.

**Weaknesses:**

&#x20
0B;

* **Factual accuracy:** While generally reliable, concerns remain regarding potential factual inaccuracies, especia
lly in complex or technical domains. Double-checking facts and conducting thorough research are crucial before publishin
g AI-generated content.
* **Limited creative control:** Users seeking highly creative or unique content might find the l
evel of control over style and tone insufficient. Exploring alternative tools with more granular control might be necess
ary for specific creative needs.
* **Learning curve:** While the interface is user-friendly, mastering advanced features
 and achieving optimal results might require some practice and experimentation.
* **Limited customer support:** User rev
iews suggest areas for improvement in customer support response time and comprehensiveness. Consulting online resources 
or communities might be necessary for certain troubleshooting needs.
* **Pricing:** Some users, particularly individuals
 or small businesses, might find the paid plans expensive compared to competitors. Carefully evaluating usage needs and 
budget constraints is essential before subscribing.

It's crucial to remember that strengths and weaknesses are relative
. Journalist AI's advantages might outweigh its limitations for specific users, while others might find alternative tool
s more suitable.

### Is Journalist AI Right for You?

Journalist AI can be a valuable tool for various user groups, dep
ending on their needs and expectations. Here's a breakdown:

&#x200B;

* **Content creators:** Ideal for bloggers, journ
alists, and marketers seeking to generate high-quality content quickly and efficiently, especially those comfortable wit
h post-editing to ensure factual accuracy.
* **Businesses:** Can benefit from SEO-optimized content creation, multilingu
al support, and team collaboration tools, particularly for marketing and communication teams.
* **Agencies:** Efficient 
content generation for client projects can be a time-saver, but careful review and editing are essential to maintain qua
lity standards.
* **Non-profit organizations:** Budget-friendly plans and the ability to create content in multiple lang
uages can be valuable assets for communication and outreach efforts.

However, if you prioritize:

&#x200B;

* **Highly 
creative content:** Explore tools offering more granular control over style and tone.
* **Absolute factual accuracy:** C
onsider tools specifically designed for technical writing or fact-checking.
* **Extensive customer support:** Opt for to
ols with readily available and comprehensive support options.
* **Free or very affordable solutions:** Explore freemium 
plans or budget-friendly alternatives.

Carefully assess your specific needs and priorities before making a decision.

#
## FAQs about Journalist AI

**Q: How accurate is the content generated by Journalist AI?**

A: While generally reliable
, factual accuracy, especially in complex topics, requires careful review and potential fact-checking before publishing.


**Q: Does Journalist AI plagiarize content?**

A: Journalist AI uses its own algorithms and does not directly copy con
tent from other sources. However, it's crucial to use it ethically and responsibly, ensuring originality and citing sour
ces if necessary.

**Q: Can I use Journalist AI for academic writing?**

A: While it can be a helpful starting point, us
ing AI-generated content directly in academic writing is generally not recommended due to potential plagiarism concerns.
 Always consult your instructor and adhere to academic integrity guidelines.

**Q: Does Journalist AI offer a free trial
?**

A: Yes, Journalist AI offers a free plan with limited content generation capacity. This allows you to test the tool
 and see if it meets your needs before committing to a paid plan.

**Q: What are the payment options for Journalist AI?*
*

A: Journalist AI accepts major credit cards and PayPal for paid subscriptions.

**Q: How does Journalist AI compare t
o other AI writing tools?**

A: Each tool has its strengths and weaknesses. Consider factors like content quality, featu
res, pricing, and ease of use when comparing options.
```
---

     
 
all -  [ let the context to keep track of all the files ](https://www.reddit.com/r/LangChain/comments/1aoulwf/let_the_context_to_keep_track_of_all_the_files/) , 2024-02-14-0909
```
Now chatgpt4 can track all the files we just uploaded in a conversation, and we can ask anything about a specific file, 
such as the name, let the model to search in a specific file.

I am wondering how we can do the same thing using langcha
in without using openai's retrivel tool?

Thanks in advance.
```
---

     
 
all -  [ Search Product Catalog Images Using Azure Search and OpenAI with Langchain ](https://www.reddit.com/r/LangChain/comments/1aou182/search_product_catalog_images_using_azure_search/) , 2024-02-14-0909
```
 In the ever-evolving landscape of retail, businesses are continually seeking innovative solutions to streamline their o
perations and enhance customer experiences. One such breakthrough is the implementation of artificial intelligence (AI) 
to search product catalog images efficiently. This transformative technology not only simplifies the search process but 
also empowers businesses to provide personalized and seamless shopping experiences for their customers. The Need for AI 
in Product Catalog Image Search: Traditional methods of searching through product catalogs involve manual tagging and ca
tegorization, which can be time-consuming and prone to human error. As the volume of products in a catalog grows, managi
ng and searching for specific items becomes a daunting task.  


Here I have implemented a Fashion agent using Azure Sea
rch , Cognitive Services and GPT-4 which can search product catalog to recommend write product to customer based on the 
requirement. 

[https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search-and-openai-with-
langchain-3a844bc5c27c](https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search-and-open
ai-with-langchain-3a844bc5c27c)
```
---

     
 
all -  [ Langchain powered search ](https://www.reddit.com/r/LangChain/comments/1aojxqa/langchain_powered_search/) , 2024-02-14-0909
```
I'm looking into LangChain to power search on some inventory. I would like to get parameters for this search from the de
scription to serve the customer. However, the customer should be able to ask his search query in any possible way, but o
bviously the API in the backend can support only a limited set of inputs.   


Exactly how would this work? And what too
ls should I consider? The idea is not to provide a response in the chat, but to provide it like an inventory search.  
```
---

     
 
all -  [ Building AI Chatbot from scratch with Llama2, Langchain and Vector database using RAG workflow ](https://www.reddit.com/r/artificial/comments/1aohn26/building_ai_chatbot_from_scratch_with_llama2/) , 2024-02-14-0909
```
Pretty detailed one in case any one wants to build one 
https://youtu.be/V8329yuXHKM
```
---

     
 
all -  [ LangChain and .NET ](https://www.reddit.com/r/dotnet/comments/1aoea8o/langchain_and_net/) , 2024-02-14-0909
```
I'm actively working on developing a new set of AI features available in VS Code, as part of SnippetHub, and next up is 
improving the context for AI features.

Given that the infrastructure is mostly on .NET technologies, I'm trying to figu
re out the best way to integrate LangChain with .NET.   
Is there a NuGet package available?

If you've had the chance t
o integrate LangChain into your .NET API, I'd appreciate it if you could share what the challenges were and if you used 
a NuGet package
```
---

     
 
all -  [ Better context with LangChain and VS Code AI coding assistant ](https://www.reddit.com/r/artificial/comments/1aoe4q8/better_context_with_langchain_and_vs_code_ai/) , 2024-02-14-0909
```
I'm actively working on developing new features for the AI coding assistant, which already has a VS Code extension where
 all the features are available.

To improve context in coding assistance (like AI Chat, AI Lens, and similar), I'm cons
idering what the best option would be. I've read a lot about LangChain and see that it offers some cool options for bett
er context when AI features come into play.

Has anyone integrated LangChain and what are your experiences? 

It would b
e great if someone could share specific use-cases from production and feedback.
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-14-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-14-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-14-0909
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-14-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-14-0909
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-14-0909
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-14-0909
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-14-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-14-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
