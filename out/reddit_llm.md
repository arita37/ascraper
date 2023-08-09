 
all -  [ pydantic decreases GPT performance ](https://www.reddit.com/r/LangChain/comments/15lyrw4/pydantic_decreases_gpt_performance/) , 2023-08-09-0910
```
I am using pydantic as an output parser however it significantly decreases the model performance. Is there another way t
o parse the results? I was thinking of first making a call without pydantic and then make a second call to parse the dat
a from there. Did anyone try this? 
```
---

     
 
all -  [ Best AI for local docs? ](https://www.reddit.com/r/LangChain/comments/15lxjo1/best_ai_for_local_docs/) , 2023-08-09-0910
```
Hello,

I was wondering what is currently the best AI to use for local docs on my computer?  I tried GPT4all and a coupl
e of it's LLM but I don't think it's that good so far, maybe because I did not train it yet?  I am trying to use it agai
nst some Word docs, PDFs, and excel currently.  Just simply stuff like identifying how many customers I have in an excel
 or how many time a particular word comes up in a word doc.
```
---

     
 
all -  [ Tools for programming AI agents with block diagrams ](https://www.reddit.com/r/LangChain/comments/15lwrnz/tools_for_programming_ai_agents_with_block/) , 2023-08-09-0910
```
I have a bunch of functions and various serial calls to GPT. Is there a tool for creating blocks and connecting them and
 each block I write my own python code?
```
---

     
 
all -  [ Flask API not running on App Engine ](https://www.reddit.com/r/googlecloud/comments/15lvk7s/flask_api_not_running_on_app_engine/) , 2023-08-09-0910
```
I wrote a flask API, which basically takes in a prompt runs it through langchain and returns its response. The idea is t
o build a basic chat interface.

Below is my flask app (main.py):

    # imports - application based
    from flask impo
rt Flask
    from flask_restful import Resource, Api, reqparse
    from flask_cors import CORS
    import os
    import 
dotenv
    
    # imports - application functionality based
    *** Langchain based imports ***
    
    # Initializing 
flask app and api
    app = Flask(__name__)
    api = Api(app=app)
    CORS(
        app=app,
        origins='*',
     
   methods=['POST'],
        allow_headers=['Content-Type', 'Authorization'],
    )
    
    
    # Loading environment 
variables
    dotenv.load_dotenv()
    
    
    # Endpoint for accessing the llm
    class LLMApi(Resource):
        **
* Langchain Related code here ***
    
        def post(self):
            parser = reqparse.RequestParser()
           
 parser.add_argument('messages', required=True, type=str)
            args = parser.parse_args()
            prompt = ar
gs['messages']
    
            if prompt is None:
                return {'error': 'No prompt provided'}, 400
    
    
        # Process the prompt using Langchain and query the database
            result = self.agent_chain.run(prompt)
  
          # Return the response in the desired format
            response = {'choices': [{'message': {'role': 'assistan
t', 'content': result}}]}
    
            return response, 200
    
    
    api.add_resource(LLMApi, '/llm-api')
    

    if __name__ == '__main__':
        app.run(debug=True)
    

The API works perfectly fine when running locally, howe
ver, when I deploy it to \`Google App Engine\` and test the API using insomnia I get this error:  


[Error thrown by Ap
p Engine Endpoint](https://preview.redd.it/8m75k81eiygb1.png?width=804&format=png&auto=webp&s=6bc814d1ee701e0f8e4099edcc
fcb08793a880ae)

I'm deploying using `gcloud app deploy app.yaml --project=truliv-ai`

My app.yaml file:

    runtime: p
ython311
    handlers:
    - url: /.*
      script: main.app

Would appreciate some help here. thank you.
```
---

     
 
all -  [ What is your favorite feature in LangChain ](https://www.reddit.com/r/LangChain/comments/15lvdor/what_is_your_favorite_feature_in_langchain/) , 2023-08-09-0910
```
We are working on an open source project which relies heavily on LangChain for code generation & software design through
 LLMs. We are early in our progress, and haven't included many LangChain features yet. For example, the internet search 
is something that we want to add to our code in future releases. I really like to know what features you like the most s
o that we can integrate those.

This is our project in case you are interested. I would truly appreciate any feedback an
d suggestion.

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-S
ynthesizer) 
```
---

     
 
all -  [ The power of LangChain for software generation using GPT ](/r/LangChain/comments/15ibzq9/the_power_of_langchain_for_software_generation/) , 2023-08-09-0910
```

```
---

     
 
all -  [ step by step software design and code generation through GPT ](https://www.reddit.com/r/ChatGPT/comments/15lswmt/step_by_step_software_design_and_code_generation/) , 2023-08-09-0910
```
If you have used ChatGPT, or GPT in general, for software design and code generation, you might have noticed that for la
rger or trickier codes, it skips a lot of the implementation or misunderstands the design. That's where tools like GPT E
ngineer and Aider come to help. However those tools for the most part keep the user out of the loop during the design. T
o explore the design space with GPT and be involved in decision making, you can use GPT-Synthesizer. GPT-synthesizer is 
a free and open-source tool which you can use for personal or commercial purposes. It uses LangChain to efficiently proc
ess larger codebases: [https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologie
s/GPT-Synthesizer) .
```
---

     
 
all -  [ GPT Synthesizer: Software generation using LangChain and the power of LLMs ](https://www.reddit.com/r/LangChain/comments/15lsh2i/gpt_synthesizer_software_generation_using/) , 2023-08-09-0910
```
As oppose to GPT Engineer or Aider, GPT Synthesizer utilizes LangChain to explore the design space with user through a c
arefully moderated interview.

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTe
chnologies/GPT-Synthesizer)

&#x200B;
```
---

     
 
all -  [ Structured documentation for fine tuning ](https://www.reddit.com/r/LocalLLaMA/comments/15lr2b0/structured_documentation_for_fine_tuning/) , 2023-08-09-0910
```
Hey guys ! 
I was wondering just like langchain has a good organised documentation on several ways to deal with LLMs , i
s there any similar documentation on how to fine tune and infer open-source LLMs , concepts like quantization , lora , q
lora etc
```
---

     
 
all -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-09-0910
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
all -  [ Chat with your data using Langchain, PineconeDB and Airbyte ](https://www.reddit.com/r/ArtificialInteligence/comments/15lkx5v/chat_with_your_data_using_langchain_pineconedb/) , 2023-08-09-0910
```
A few of our team members at Airbyte (and Joe, who killed it!) recently played with building our own internal support AI
 chat bot, using Airbyte, Langchain, Pinecone and OpenAI, that would answer any questions we ask when developing a new c
onnector on Airbyte. 

As we prototyped it, we realized that it could be applied for many other use cases and sources of
 data, so… we created [a tutorial](http://airbyte.com/tutorials/chat-with-your-data-using-openai-pinecone-airbyte-and-la
ngchain) that other community members can leverage and the [Github repo](https://github.com/airbytehq/tutorial-connector
-dev-bot) to run it .

The tutorial shows: 

* How to extract unstructured data from a variety of sources using Airbyte 
Open Source
* How to load data into a vector database (here Pinecone), preparing the data for LLM usage along the way
* 
How to integrate a vector database into ChatGPT to ask questions about your proprietary data

I hope some of it is usefu
l, and would love your feedback!  

```
---

     
 
all -  [ Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/LangChain/comments/15lkjl6/rust_meets_llama2_openai_compatible_api_written/) , 2023-08-09-0910
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to Nvidia GPU and Metal acceleration for GGML models thanks to the fantastic \`llm\` crate! You 
can use it with the OpenAI integration (see the Python folder in GitHub project) 

Here is the project link: [Cria- Loca
l LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Lang
chain\` example in the project).

Really interested in your feedback and I would welcome any contributions :) !

&#x200B
;
```
---

     
 
all -  [ Custom LLM service using LangChain ](https://www.reddit.com/r/datascience/comments/15lji9i/custom_llm_service_using_langchain/) , 2023-08-09-0910
```
Hi all,

For a project, I am looking to build a custom LLM from a knowledge base by a governmental institution. I know t
his can be done using Langchain + VectorStore but I was wondering whether there might already be a SaaS solution for thi
s task.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Tuning vs using langchain/llama index for retrieving structured data from unstructured data ](https://www.reddit.com/r/LangChain/comments/15li8df/tuning_vs_using_langchainllama_index_for/) , 2023-08-09-0910
```
I have a big dataset that makes use of a single document to retrieve some information into a single row of the table, th
e document can JPEG or PNG, the work was being done manually by entering the data, I'm trying to automate this process, 
I used OCR models mainly from aws (Textract) to get text document and built a prompt that defines the fields and builds 
a JSON based on the text. The thing is I want to improve the performance with tuning llama2 or gpt(I think starting from
 january next year will be supported) into my data, or use langchain or llamaindex to pass the table and documents as co
ntext, which I think will be some sort of few shot learning, which of these approaches is better for my case?
```
---

     
 
all -  [ Peter - Buildfast Masterclass - Learn to build your own AI chatbot ](https://www.reddit.com/r/MakesYouMoney/comments/15lhx7h/peter_buildfast_masterclass_learn_to_build_your/) , 2023-08-09-0910
```
Get the course here: [https://bit.ly/Peter-Buildfast\_Masterclass](https://bit.ly/Peter-Buildfast_Masterclass)

[https:/
/bit.ly/Peter-Buildfast\_Masterclass](https://bit.ly/Peter-Buildfast_Masterclass)

[ ](https://preview.redd.it/wcgw14o40
p7b1.jpg?width=1280&format=pjpg&auto=webp&s=404eee6c4d63d0176e118d586148aba90726b3b0)

# Here are all of the videos insi
de Fundamentals That you get instant access to upon joining BuildFast

1. LLMs: Overview, using LLMs in Langchain, open-
sourced LLMs, chat model, embedding text.
2. Chains: Chains 101, LLM Chain, Sequential Chain, and four other important L
angchain chains.
3. Prompt: Prompts 101, Example Prompts, Output Parser.
4. Memory: 4 Memory Types Explained, How to use
 Memory in a Chain, How to add Memory to an Agent
5. Document Loaders: Document Loaders 101, When to use Document Loader
, Import data from Text & CSV, and Loading data from Discord, Notion, Telegram
6. Indexes: Indexes 101, Retrievers and T
ext Splitters.
7. Vector Database & Embeddings: Vector databases 101, when to use vector databases, Embeddings and vecto
r database use-cases.
```
---

     
 
all -  [ Teaching Llama to reason in another language help! ](https://www.reddit.com/r/LocalLLaMA/comments/15lgoo7/teaching_llama_to_reason_in_another_language_help/) , 2023-08-09-0910
```
Hi r/LocalLLaMA, 

&#x200B;

I have been tinkering with Ooba and API calls for a while now, and have hit a bit of a wall
.   


My use case is corporate and not too out there: given transcripts of business calls, I should be able to answer q
uestions and deliver summaries of the conversation. All easy with Langchain and vector databases, and iterative summariz
ation.

My only issue is that this is all happening in Brazilian Portuguese. OpenAI models all have a similar level of i
ntelligence and coherence in non-English languages, but Llama seems to fail miserably at this.   


There was an attempt
 to teach LLama 1 Portuguese: [https://github.com/22-hours/cabrita](https://github.com/22-hours/cabrita) , and so I used
 the same dataset on Llama2-13B-chat to update the project, but like some of you have been experiencing, the model goes 
off its rocker after around 100 tokens, doesn't know when to stop, often lapses into English while still being correct, 
etc.  


Do any of you have experience teaching an LLM a different language? I have read that this happens mainly at fou
ndational training, and that LoRAs can't really imbue the model with reasoning skills in a new language. I was thinking 
of some possible options:  


* Use a larger dataset which successfully created a good finetune (e.g. Vicuna) and transl
ate it to PT-BR using ChatGPT (expensive). 
* Transcribe all calls in Portuguese and English, and do all prompts and rea
soning in English, only translating to Portuguese at the end.

&#x200B;

I really appreciate any answers of further poin
ts you may have, as I've trained maybe 10-20 LoRAs at this point with no real improvement.

&#x200B;

P.S. : After how m
any steps do you usually stop LoRA finetuning? I seem to consistently get negligible loss improvements after around 100,
 and my runs that went far beyond that and probably overfitted only output a bunch of newlines regardless of the prompt.

```
---

     
 
all -  [ ChatBot - dialogue phases ](https://www.reddit.com/r/LangChain/comments/15lenge/chatbot_dialogue_phases/) , 2023-08-09-0910
```
What are the best options of creating a chatbot for a mental health app such that the dialogue with a user should be div
ided into 3 phases: 1 for identifying the issue, one for suggesting a technique, and another for follow-up and general c
onversation?
```
---

     
 
all -  [ Holiday Planning AI Agents ](https://fetch.ai/content-hub/article/holiday-integrations-walkthrough) , 2023-08-09-0910
```

At the end of July, we announced amazing integrations that empower developers to deploy Holiday Planning AI Agents 🤖

C
ombining OpenAI's LLMs, LangChain's Agent Search, and Skyscanner's Flight Offers through RapidAPI, you can find all of y
our travel suggestions curated easily ✈️

We now have a full walkthrough for developers on how to start using these inte
grations now 🔥

Read our recent blog post to learn more 👇
https://fetch.ai/content-hub/article/holiday-integrations-walk
through

Earlier this week, we released the newly announced Agent Name Service (ANS) for Agentverse.ai! 🤖

ANS makes it 
possible for #AI Agents to register names & communicate with ease. It also massively improves Agent searchability 🔍

Try
 out ANS with the tutorial below 👇
https://youtu.be/HiWxVahNXLg
```
---

     
 
all -  [ LangChain available in 13.1 LTS and above ](https://www.reddit.com/r/databricks/comments/15lbnf6/langchain_available_in_131_lts_and_above/) , 2023-08-09-0910
```
LangChain is available as an experimental MLflow flavor which allows LangChain customers to leverage the robust tools an
d experiment tracking capabilities of MLflow directly from the Databricks environment.

LangChain is a software framewor
k designed to help create applications that utilize large language models (LLMs) and combine them with external data to 
bring more training context for LLMs.

Databricks Runtime for Machine Learning includes langchain in Databricks Runtime 
13.1 ML and above.
```
---

     
 
all -  [ How to create a custom pyton repl tool? ](https://www.reddit.com/r/LangChain/comments/15lbhz6/how_to_create_a_custom_pyton_repl_tool/) , 2023-08-09-0910
```
I want the LLM to use pythonRepl tool when its fed with particular actions to be performed. In my use case, I want to us
e the Repl tool to connect to a server with a certain port. I want to give this to the LLM as a natural language prompt 
like send string to the server with port. Am using python agent and am haed feeding the prompt detailing each steps to b
e performed. Is there any way to achieve my goal. Am sorry I suck at asking detailed questions. Langchain's pretty new t
o me.
```
---

     
 
all -  [ Q&A with thousands of documents ](https://www.neum.ai/post/q-a-with-1000-documents) , 2023-08-09-0910
```
Did a small write up exploring how to build scalable solutions that can enable RAG with thousands of documents. Tools I 
looked at include Langchain as well as a tool I built that leverages Langchain to scale data extraction and loading.
```
---

     
 
all -  [ Are there free alternatives to use chatbots to solve math problems? ](https://www.reddit.com/r/LangChain/comments/15kxzc6/are_there_free_alternatives_to_use_chatbots_to/) , 2023-08-09-0910
```
I need something like the wolfram alpha plugin on chatgpt plus but without paying for chatgpt plus, I found some models 
on langchain but they all use openai API, are there any models using plugins similiar to wolfram but with a free API key
?
```
---

     
 
all -  [ SentenceTransformerEmbeddings makes my kernel crash ](https://www.reddit.com/r/LangChain/comments/15kon72/sentencetransformerembeddings_makes_my_kernel/) , 2023-08-09-0910
```
After weeks trying to troubleshoot this issue I thought I'd head straight to this sub as a last resort.

As the title in
dicates, SentenceTransformerEmbeddings makes my kernel crash. It worked fine weeks ago.

Is this a common issue or somet
hing quite new (given the development pace of LangChain and sometimes the quantify-over-quality side effect) or just som
ething on my side? 

By the way, I tried running it in a Google colab notebook and it worked fine so I'm quite confused.


&#x200B;
```
---

     
 
all -  [ Set Role of the System Help - OpenAI API + Langchain ](https://www.reddit.com/r/LangChain/comments/15kn3me/set_role_of_the_system_help_openai_api_langchain/) , 2023-08-09-0910
```
Hi I'm working on a project to create a conversation agent to help with critical literacy using OpenAI's API. I want the
 model (currently using gpt-3.5-turbo) to call from data stored in a directory, which is where I'm using modules from la
ngchain. The barebones script I have written so far is working but I am confused as to how/if i can improve it the way i
 want to. I'm new to this but from tutorials I've read online I see that you are able to give the system a 'role'.

&#x2
00B;

For example:

    prompt = “You're a nutritionist chatbot that creates customized meal plan
    Only answer questi
ons related to nutrition.
    Only ask questions related to nutrition, health and meal plans.
    
    messages = [
    
{
    'role': 'system',
    'content': prompt
    }
    ]

Due to how my script has been written utilising the langchain
 modules, I'm unsure as to how I can incorporate this. I'll leave snippits of my code below and if anyone can help I'd r
eally appreciate it. Thanks.

&#x200B;

    # Import necessary modules
    import os
    import sys
    
    # Importing
 OpenAI library
    import openai
    
    # Import modules from langchain package
    from langchain.document_loaders i
mport DirectoryLoader
    from langchain.indexes import VectorstoreIndexCreator
    from langchain.chains import Convers
ationalRetrievalChain
    from langchain.chat_models import ChatOpenAI
    from langchain.llms import OpenAI
    
    # 
Set the OpenAI API key using the APIKEY
    os.environ['OPENAI_API_KEY'] = 'sk-xxxx'
    
    # Initialize query variabl
e to None
    query = None
    
    # Check if command-line arguments were provided
    if len(sys.argv) > 1:
        qu
ery = sys.argv[1]
    
    # Create the index from the data in the 'data/' directory
    loader = DirectoryLoader('Data 
Files/FallacyInfo')
    index = VectorstoreIndexCreator().from_loaders([loader])
    
    # Create a ConversationalRetri
evalChain using the ChatOpenAI language model and the index as the retriever
    chain = ConversationalRetrievalChain.fr
om_llm(
        llm=ChatOpenAI(model='gpt-3.5-turbo'),
        retriever=index.vectorstore.as_retriever(search_kwargs={'
k': 1}),
    )
    
    # Initialize an empty list to store the chat history
    chat_history = []
    
    # Start an i
nfinite loop to keep the chat session running
    while True:
    
        # If query is not provided, get user input as
 the query (prompt)
        if not query:
            query = input('You: ')
    
        # Check if the user wants to q
uit the chat session
        quit_keywords = ['quit', 'q', 'exit']
        if query.lower() in quit_keywords:
          
  print('FallacyFinder: Goodbye! Have a great day!')
            break
    
        # Use the conversational retrieval c
hain (chain) to get a response for the current query
        result = chain({'question': query, 'chat_history': chat_his
tory})
    
        # Print the AI Assistant's answer from the response
        print('FallacyFinder:', result['answer']
)
    
        # Append the user query and AI assistant's response to the chat history
        chat_history.append(('You
: ' + query, 'FallacyFinder: ' + result['answer']))
    
        # Reset the query to None to allow the user to input a 
new query in the next iteration
        query = None

&#x200B;

For reference I have followed the below tutorial -

vide
o:

[https://www.youtube.com/watch?v=9AXP7tCI9PI&list=LL&index=2&pp=gAQBiAQB](https://www.youtube.com/watch?v=9AXP7tCI9P
I&list=LL&index=2&pp=gAQBiAQB)

github:

[https://github.com/techleadhd/chatgpt-retrieval/tree/main](https://github.com/
techleadhd/chatgpt-retrieval/tree/main)
```
---

     
 
all -  [ Simple solution to search Markdown documents needed, my code needs help. ](https://www.reddit.com/r/LangChain/comments/15ki156/simple_solution_to_search_markdown_documents/) , 2023-08-09-0910
```
I would like to load a directory of markdown files and be able to use gpt to interact with them. I am totally new to Pyt
hon and LangChain. I am trying to cobble together some code, but am having problems. I am getting the error `Number of r
equested results 4 is greater than number of elements in index 3, updating n_results = 3`, and I am not sure it is actua
lly loading all the documents as intended. Is this a bug in ChromaDB? I have read other people have this problem, but I 
don't understand the solution or how to use in in my code: https://github.com/langchain-ai/langchain/issues/2255#issueco
mment-1492949955

(I have my API key as an environment variable)

```python
import sys
from langchain.document_loaders i
mport DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

temp = 0.2
query = sys.argv[1] # use the qu
estion passed into the script

loader = DirectoryLoader('./doc/', glob='*.md', show_progress=True)

data = loader.load()

print(data) # I don't think all the contents of the documents are here? I might be wrong.

index = VectorstoreIndexCrea
tor().from_loaders([loader])
print(index.query(query))
```
I am trying to get the most accurate results so am experiment
ing with leaving out the gpt main database as above, but also using `print(index.query(query, llm=ChatOpenAI(model='gpt-
3.5-turbo-16k', temperature=temp)))`. Results seem mixed so far.

I am not sure if I need to split up the documents some
how to get good results? Should I split intelligently for Markdown somehow taking headings etc into account, or maybe `D
irectoryLoader` does that automatically?

If anyone could get rid of the error and confirm my script is working as inten
ded it would be fantastic! Improvements would be happily accepted, but please keep it as simple as possible. Cheers!
```
---

     
 
all -  [ PDF splitter ](https://www.reddit.com/r/LangChain/comments/15kh0xn/pdf_splitter/) , 2023-08-09-0910
```
Hey everyone,

I need to split the pdf documents into meaningful chunks. I can't split documents by pages. Do you have a
ny suggestion how to do it? 

I was thinking about converting pdf to md and then use MarkdownTextSplitter, but I wasn't 
able to find reliable library for this. It'd be the best, if I was able to split pdfs by headers, sections but it is not
 that easy as each pdf can have different format. 

I will be grateful for any advice. Thank you

&#x200B;
```
---

     
 
all -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-09-0910
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

     
 
all -  [ Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/rust/comments/15k1w99/rust_meets_llama2_openai_compatible_api_written/) , 2023-08-09-0910
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to  Nvidia GPU and Metal acceleration for GGML models thanks to the fantastic \`llm\` crate!

He
re is the project  link : [Cria- Local LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI repla
cement (check out the included \`Langchain\` example in the project).

This is an ongoing project, I have implemented th
e \`embeddings\` and \`completions\` routes. The \`chat-completion\` route will be here very soon!

Really interested in
 your feedback as I am still a beginner in Rust and I would welcome any help :) !

&#x200B;

EDIT : Just added support f
or the *chat/completions* route. This basically completes the OpenAI (without SSE support) !

&#x200B;
```
---

     
 
all -  [ Local Llama-2 API in Rust ](https://www.reddit.com/r/LocalLLaMA/comments/15k1uk7/local_llama2_api_in_rust/) , 2023-08-09-0910
```
Hello, 

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It support
s offloading computation to  Nvidia GPU and Metal acceleration for GGML models.

Here is the project link :
[Cria - Loca
l LLama2 OpenAI compatible API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out t
he included \`Langchain\` example in the project).

This is an ongoing project, I have implemented the \`embeddings\` an
d \`completions\` routes. The \`chat-completion\` route will be here very soon!  

Really interested in your feedback an
d I would welcome any help :) !
```
---

     
 
all -  [ Project using PALM API and Langchain ](https://www.reddit.com/r/LangChain/comments/15jvyhb/project_using_palm_api_and_langchain/) , 2023-08-09-0910
```
The day before I got access to Palm API(through waitlist of Palm API and Makersuite not from GCP or vertex ai). I wanted
 to make a project out of it. I want to use Pinecone as a vector store and Streamlit as a UI. Any new, creative projects
 that I can add to my resume?
```
---

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-09-0910
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-09-0910
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

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-09-0910
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

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-09-0910
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

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 2023-08-09-0910
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

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 2023-08-09-0910
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
MachineLearning -  [ '[N]' '[D]' Langchain? What is it?? ](https://www.reddit.com/r/MachineLearning/comments/150mzax/n_d_langchain_what_is_it/) , 2023-08-09-0910
```
want to know more about Langchain  
Check out [https://nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf](https:
//nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf)
```
---

     
 
MachineLearning -  [ [D] The Problem With LangChain ](https://www.reddit.com/r/MachineLearning/comments/14zlaz6/d_the_problem_with_langchain/) , 2023-08-09-0910
```
https://minimaxir.com/2023/07/langchain-problem/

tl;dr it's needlessly complex, and I provide code examples to demonstr
ate such.

A few weeks ago when I posted about creating a LangChain alternative to /r/MachineLearning, most of the comme
nts replied 'what exactly is the issue with LangChain', so I hope this provides more clarity!
```
---

     
 
MachineLearning -  [ [D] 📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1) ](https://www.reddit.com/r/MachineLearning/comments/14xww89/d_the_learning_corner_andrew_ng_free_ai_courses/) , 2023-08-09-0910
```
📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1)

This is a list of some of the best Ai Free courses by Andrew NG
, we will release the second part of the list on our next newsletter installment (link)

* [**Generative AI with Large L
anguage Models**](https://www.deeplearning.ai/courses/generative-ai-with-llms/?utm_campaign=gaia-launch&utm_content=2545
85614&utm_medium=social&utm_source=linkedin&hss_channel=lcp-18246783)
* [**LangChain: Chat With Your Data**](https://www
.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
* [**LangChain for LLM Application Development**](https:/
/learn.deeplearning.ai/langchain)
* [**How Diffusion Models Work**](https://learn.deeplearning.ai/diffusion-model)
```
---

     
 
MachineLearning -  [ [P] langchain-lite alternative ](https://www.reddit.com/r/MachineLearning/comments/14xf9xb/p_langchainlite_alternative/) , 2023-08-09-0910
```
Although langchain is an impressive library, I tend to find it is…

* a little unintuitive, at least for non-trivial exa
mples or examples that don’t have a predefined chains/templates
* related, it's overly prescriptive; and the various lev
els of abstraction don't resonate with me
* related, can be difficult to debug or understand what’s happening in interme
diate steps of the chain or what’s it’s actually sending OpenAI

So, I built a “langchain-lite” package called `llm-work
flow`

https://github.com/shane-kercheval/llm-workflow

The value proposition is basically:

* easily build up a sequenc
e of tasks (e.g. prompt-template -> chat) called a workflow, where the output of one task serves as the input to the nex
t task in the workflow
* **track history**; understand what's happening in each of the tasks; **aggregate token usage, c
osts, etc. across the workflow**

So a workflow can be anything from `prompt -> chat -> response` to `prompt -> web-sear
ch -> web-scraping -> vector-database & retrieval -> modified prompt -> chat -> response`.

Here's an example of a 'prom
pt enhancer' workflow, where the user provides a prompt, one model enhances/improves the prompt, and the second model an
swers the question based on the enhanced prompt.

```python
prompt_enhancer = OpenAIChat(...)
chat_assistant = OpenAICha
t(...)

def prompt_template(user_prompt: str) -> str:
    return 'Improve the user's request, below, by expanding the re
quest ' \
        'to describe the relevant python best practices and documentation ' \
        f'requirements that shou
ld be followed:\n\n```{user_prompt}```'

def prompt_extract_code(_) -> str:
    # `_` signals that we are ignoring the i
nput (from the previous task)
    return 'Return only the primary code of interest from the previous answer, '\
        
'including docstrings, but without any text/response.'

workflow = Workflow(tasks=[
    prompt_template,      # modifies
 the user's prompt
    prompt_enhancer,      # returns an improved version of the user's prompt
    chat_assistant,     
  # returns the chat response based on the improved prompt
    prompt_extract_code,  # prompt to ask the model to extrac
t only the relevant code
    chat_assistant,       # returns only the relevant code from the model's last response
])
pr
ompt = 'create a function to mask all emails from a string value'
response = workflow(prompt)
```

The `response` is: `d
ef mask_email_addresses(string): .....`

We can view the history, which includes the prompts/responses/tokens/etc. for e
ach interaction:

```python
print(workflow.history())
```

Output:

```
[
    ExchangeRecord(prompt='Improve the user's 
request, below, by ...', response='Create a Python function that adheres to best practice...', timestamp='2023-07-12 04:
45:04.703', cost=0.00063, total_tokens=333, prompt_tokens=58, response_tokens=275),
    ExchangeRecord(prompt='Create a 
Python function that adheres ...', response='Sure! Here\'s an example of a Python function that adh...', timestamp='2023
-07-12 04:45:14.696', cost=0.00149, total_tokens=820,  prompt_tokens=292, response_tokens=528),
    ExchangeRecord(promp
t='Return only the primary code of intere...', response='```python\nimport re\n\ndef mask_email_addresses(strin...', tim
estamp='2023-07-12 04:45:18.875', cost=0.00167, total_tokens=1051, prompt_tokens=850, response_tokens=201)
]
```

We can
 also summarize costs/tokens/etc.

```python
print(workflow.sum('cost'))             # 0.0034
print(workflow.sum('total_
tokens'))     # 1961
print(workflow.sum('prompt_tokens'))    # 1104
print(workflow.sum('response_tokens'))  # 857
```

M
ore examples can be found here: https://github.com/shane-kercheval/llm-workflow/tree/main/examples

Feedback welcome.
```
---

     
 
MachineLearning -  [ [D] What have been your use cases for LLM autonomous agents? ](https://www.reddit.com/r/MachineLearning/comments/14w817y/d_what_have_been_your_use_cases_for_llm/) , 2023-08-09-0910
```
I've been using GPT for completions on a daily basis for a while now - code completion and search-like chatting, basical
ly. I've recently been playing around with both ChatGPT plugins and LangChain for autonomous-agent-like behavior, and al
though the idea of the LLM interacting with the environment through API calls or code interpretation seems promising, in
 practice I haven't found such a useful and usable case for it like completions yet.

LangChain's OpenAPI toolkit with i
ts planner/controller agent duo seems to get lost 90% of the time, making it unusable. This happens even with an /api en
dpoint telling it exactly how to interact with the API and prompt templates suggesting that this endpoint be used to get
 the API specs. Maybe I'm just not getting it right...

As for ChatGPT plugins, other than web search for more updated r
esults I haven't really found a use case where I could not do the same thing with completions. Code Interpreter shaves o
ff a few seconds vs completions and running whatever script it produces locally, but it's not very useful in face of com
pliance or privacy requirements of not uploading stuff into OpenAI. For example I wanted to speed up a work related vide
o and add a separate audio track to it. I couldn't upload the video to OpenAI as it contained internal work stuff, so I 
just used completions for an ffmpeg script to do the job and ran it locally. Same thing with transforming or plotting CS
V data - can't really update customer data to OpenAI, so just get the script and run it locally.

Anyway, I can *think o
f* a lot of cool use cases for autonomous agents and the like, but I haven't been able to *actually use* it in my daily 
routine, unlike text completion. Have you been using autonomous agents successfully and regularly?
```
---

     
 
MachineLearning -  [ [D] Hacking LangChain for Fun and Profit ](https://www.reddit.com/r/MachineLearning/comments/14w0ht7/d_hacking_langchain_for_fun_and_profit/) , 2023-08-09-0910
```
[https://blog.kevinhu.me/2023/07/10/hacking-langchain-for-fun-and-profit/](https://blog.kevinhu.me/2023/07/10/hacking-la
ngchain-for-fun-and-profit/)

I'm starting a series of blogs to delve into LangChain. Hope this helps anyone who's inter
ested in LLM and building with LangChain.
```
---

     
 
MachineLearning -  [ [D] - Are there any AI benchmarks that involve successful longterm problem solving when running as a ](https://www.reddit.com/r/MachineLearning/comments/14v4l2o/d_are_there_any_ai_benchmarks_that_involve/) , 2023-08-09-0910
```
 Even the most powerful LLMs, such as gpt4, seem to get lost or fall into loops when being run as autonomous agents like
 as part of langchain or autogpt. Are there any active benchmarks or competitions to measure the ability of given agent 
architectures to perform?
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-09-0910
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
