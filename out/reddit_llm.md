 
all -  [ So close... Switching from Openai models to local models served by Ollama ](https://www.reddit.com/r/LangChain/comments/1abwoh6/so_close_switching_from_openai_models_to_local/) , 2024-01-27-0909
```
As the title says, I'm working to enable an app I wrote that generates SQL to allow it to work from a locally served LLM
 instead of one in the cloud. This is a requirement for a couple of customers, so I've been experimenting...

I'm using 
the create\_sql\_agent function... I'm supplying the prompts as well as some custom tools that feed in appropriate metad
ata about the database.  Against OpenAI or AzureOpenAI it works fine.

When I run against Ollama, I've tried a bunch of 
models - SQLcoder, LLama70b, Mixtral8x7b, etc.  And I get the same result... I can watch the agent work away (via my own
 debugging as well as LangSmith).. 

The agent runs typically follow the same general path as the OpenAI runs, with one 
exception - I can see the final SQL statement generated, but after executing the statement and getting a perfectly fine 
answer (and identifying it as such) it goes into a kind of loop and never exits the chain.  

I've toyed with supplying 
'stop=' tokens etc, but I just don't see what's going on.

There's so many moving pieces that I thought someone might ha
ve an idea where to look... 

It's possible that it's a prompt format issue - I know the prompt format between the Llama
 models and OpenAI models are pretty different... with special tokens, etc. but I'm utterly unclear how that would chang
e things, since up to the point it should 'exit' and return the final answer it works pretty well.

I'll add that I crea
ted a custom 'handler' to extract the final sql statement it creates, since the sql agent returns the 'answer' rather th
an the SQL statement.  My handler is looking for invocation of the sql\_db\_query tool which indicates that the sql has 
been generated and is being sent off for execution - I grab the string at that point and save it for later... that  work
s in openai, but not in any of the other models I've tried.

I do get some different results with different models...

M
ost have given the above general issue - generating a good answer, but then never stopping.

mixtral:8x7b-instruct-v0.1-
q5\_K\_M - was weird. It didn't seem to want to use the tools I provided and sort of skipped some steps.  It generated S
QL that had no relation to the actual database - so it wasn't using any of the tools - then when it came time to run the
 SQL it DID generate, it messed up that name of the sql\_db\_query tool:

'{'requested\_tool\_name': 'sql\\\\\_db\\\\\_q
uery', 'available\_tool\_names': \['sql\_db\_query', 'sql\_db\_schema', 'sql\_db\_list\_tables', 'sql\_db\_query\_checke
r', 'sql\_get\_few\_shot\_examples', 'sql\_get\_column\_descriptions', 'get\_column\_to\_table\_cross\_reference', 'get\
_hierarchies', 'sql\_get\_table\_descriptions'\]}'

No other model did this... 

SO, I'm wondering if anyone else has ha
d the same struggle, or can point me in some direction to figure this out... it feels like I'm so very close, just missi
ng one key ingredient!

Thanks!

&#x200B;
```
---

     
 
all -  [ Overcoming 8-10% Inaccuracy in PDF Keyword Extraction Using Faiss and OpenAI – Need Advice ](https://www.reddit.com/r/LangChain/comments/1abvyps/overcoming_810_inaccuracy_in_pdf_keyword/) , 2024-01-27-0909
```
 Hello everyone,

I'm working on a project using Langchain involving information extraction from PDF documents, each ran
ging from 5-10 pages. My primary goal is to extract information based on approximately 26 keywords, which I load from a 
CSV file.

Here's an overview of my current setup:

Basic Language Chain Components: I'm using a loader, a recursive spl
itter set to 500 with an overlap of 300, and an Ensemble Retriever BM25)and MultiQuery Retriever setup with FAISS, where
 each component has a .5 weight for each.

FAISS Library Usage: In the FAISS library, I'm employing the from\_documents 
method and a retriever.

OpenAI Integration: After combining the top 2 chunks for each keyword, I'm feeding the data int
o OpenAI with prompt.

However, I'm encountering an issue where the results are about 8-10% hallucinated or inaccurate.


I'm looking for advice on how to improve the accuracy of my information extraction process. Are there any specific para
meters or techniques in better chunking, FAISS or with OpenAI that I should consider consider or tweaking? Any insights 
or suggestions would be greatly appreciated!
```
---

     
 
all -  [ Need help improving RAG ](https://www.reddit.com/r/LangChain/comments/1abuv1f/need_help_improving_rag/) , 2024-01-27-0909
```
Hello everyone, I am just starting with RAG.

I want to retrieve building regulations ( max height, area, etc) informati
on from pdfs using a llm. 

the pdfs contains both text and data. I am currently using PypdfLoader from langchain to loa
d the pdfs. Splitting using recursive character split, embedding using open ai and storing it in chroma db.
 

Sometimes
 the llm doesn’t retrive the information correctly.  don’t know if it is because of the parsing of pdfs. 

Any help in i
mproving the system is greatly appreciated. Thanks.
```
---

     
 
all -  [ We can put scientific research papers into chatGPT and make our own medicine at any time ](https://www.reddit.com/r/RandomThoughts/comments/1abuj7n/we_can_put_scientific_research_papers_into/) , 2024-01-27-0909
```
Langchain.com looks nice 
```
---

     
 
all -  [ New openai v3 embeddings - are they working with langchain or not? ](https://www.reddit.com/r/LangChain/comments/1abrtev/new_openai_v3_embeddings_are_they_working_with/) , 2024-01-27-0909
```
So I read the blogpost from OpenAI on their new v3 embeddings models, and decided to try them in my app... I get an erro
r... so I simplified to the 4 line example from the langchain docs, which results in the same error: 

from langchain\_o
penai import OpenAIEmbeddings

    
    embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
    
    query_res
ult = embeddings.embed_query('Some test text!!!')
    
    print(query_result[0:5])
    
    % python3 t.py
    Warning:
 model not found. Using cl100k_base encoding.
    [-0.0076643440879791275, 0.023873071539678815, -0.01047247064095197, 0
.006004269555153845, 0.0286252864226502]

Which seems odd, since I can execute the curl example from the openai docs, no
 problem:

    % curl https://api.openai.com/v1/embeddings \                 ✔  11:34:33
      -H 'Content-Type: appli
cation/json' \
      -H 'Authorization: Bearer xxxxx' \
      -d '{
        'input': 'Your text string goes here',
     
   'model': 'text-embedding-3-large'
      }'
    
    ...
            -0.02287454,
            -0.02287454,
           
 -0.022449568
          ]
        }
      ],
      'model': 'text-embedding-3-large',
      'usage': {
        'prompt_t
okens': 5,
        'total_tokens': 5
      }
    }

&#x200B;

When I refer to the langchain embedding docs, they've alre
ady been updated to show the new embeddings... BUT they are showing the same error RIGHT IN THEIR DOCs as well.

&#x200B
;

    from langchain_openai import OpenAIEmbeddings
    
    embeddings = OpenAIEmbeddings(model='text-embedding-3-larg
e')
    
    text = 'This is a test document.'
    
    Embed documents
    doc_result = embeddings.embed_documents([tex
t])
    
    Warning: model not found. Using cl100k_base encoding.
    
    doc_result[0][:5]
    
    [-0.0143800563773
83358,
     -0.027191711627651764,
     -0.020042716111860304,
     0.057301379620345545,
     -0.022267658631828974]

A
m i missing something??? 
```
---

     
 
all -  [ Can I combine LangChain with PrompFlow? ](https://www.reddit.com/r/LangChain/comments/1abpzp2/can_i_combine_langchain_with_prompflow/) , 2024-01-27-0909
```
I recently heard about promptflow, a tool to create end to end LLM processes. Is it more a competitor to langchain, can 
I combine both, or what is the difference to langchain?
```
---

     
 
all -  [ Langchain ChatModel import from 2 different library? ](https://www.reddit.com/r/LangChain/comments/1abomxb/langchain_chatmodel_import_from_2_different/) , 2024-01-27-0909
```
What is the difference between these two approaches for importing OpenAI chat models?'

***from*** **langchain\_openai**
 ***import*** **ChatOpenAI**  
***from*** **langchain.chat\_models** ***import*** **ChatOpenAI**

Does langchain-openai 
use the latest release of OpenAI or do they use the same version?
```
---

     
 
all -  [ X-Shot prompting with Langchain ](https://www.reddit.com/r/LangChain/comments/1abo6l5/xshot_prompting_with_langchain/) , 2024-01-27-0909
```
I was trying out X-shot prompting with Langchain but couldn't find some good relevant examples of how to form the prompt
 template for this. Specifically how should an example or examples be inserted into the prompt template and merged with 
proper instructions. Any useful examples or turtorials?
```
---

     
 
all -  [ I want to create a text analysis app using Langchain with Open AI api ,can some give me rough steps  ](https://www.reddit.com/r/deeplearning/comments/1able41/i_want_to_create_a_text_analysis_app_using/) , 2024-01-27-0909
```

```
---

     
 
all -  [ Avoid duplicates inside a chroma db ](https://www.reddit.com/r/LangChain/comments/1abkaif/avoid_duplicates_inside_a_chroma_db/) , 2024-01-27-0909
```
Hello , lets say that we prompt the user to add documents , which the app chunks , embeds and adds to a vector database.
 

How can we avoid inserting the same document twice? Is there any way it can be done with langchain?

I really cant fi
nd a way around.
```
---

     
 
all -  [ What is the best open source LLM for outputting SQL code ](https://www.reddit.com/r/LangChain/comments/1abiozm/what_is_the_best_open_source_llm_for_outputting/) , 2024-01-27-0909
```
I am currently using Mixtral 8x7B Instruct v0.1 - GPTQ and was wondering what is currently the best open source LLM to u
se to output SQL code?

Would really appreciate any input on this. Many thanks!
```
---

     
 
all -  [ Switch to Assistants API from Chat completions to save on shared context bandwidth? ](https://www.reddit.com/r/LangChain/comments/1abheko/switch_to_assistants_api_from_chat_completions_to/) , 2024-01-27-0909
```
I have a QA-style few-shot style agent and it's prompt goes like this:  
\> You're a helpful assistant who's an expert i
n X, (explanation of its audience, task and output guardrails/format).

\> Examples:

\> Question: xxx

\> Answer:

\> \
`\`\`yyy\`\`\`  


Tokens utilization is pretty steep because of this large context that's being sent in full over and o
ver again for every request using Chat Completions API( [https://platform.openai.com/docs/guides/text-generation/chat-co
mpletions-api](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) )

Is it possible to switch
 instead to Assistants API( [https://platform.openai.com/docs/assistants/overview/agents](https://platform.openai.com/do
cs/assistants/overview/agents) ) for such a task so that context is sent only as 1st system message and all questions ar
e just appended to that thread? 
```
---

     
 
all -  [ Claude says Anthropic made LangChain and Stable Diffusion ](https://www.reddit.com/r/ClaudeAI/comments/1abggq6/claude_says_anthropic_made_langchain_and_stable/) , 2024-01-27-0909
```
I noticed this in November. I thought I'd check back in a few months later to see if it's been fixed - it hasn't.

With 
a quick Google, I can see the information about LangChain has been replicated in some Medium articles. It's not the most
 harmful of hallucinations but it is surprising how convinced Claude is.

I'm interested in why this has happened. I fig
ured the documentation Claude is fine-tuned on heavily mentions AI products and Anthropic, leading it to overfit and def
ault to crediting Anthropic to other AI research and products. Does that sound reasonable? Any other ideas?

https://pre
view.redd.it/759tppzuurec1.png?width=757&format=png&auto=webp&s=1acd8c35197a2c93e74cfd2c25ba8987671a6ece

https://previe
w.redd.it/7ojltqzuurec1.png?width=741&format=png&auto=webp&s=c42e530d3ac0857f1d9b7b2a698bdcfe5e5d6fd5

https://preview.r
edd.it/zrh82rzuurec1.png?width=763&format=png&auto=webp&s=2b81c852a9996a241af81907013e83ff341e8400

https://preview.redd
.it/tw4v3uzuurec1.png?width=742&format=png&auto=webp&s=6c94d79e41753b112259a6f72fab00583d1ede8f
```
---

     
 
all -  [ RAG Chatbot with LCEL ](https://www.reddit.com/r/LangChain/comments/1abf7eo/rag_chatbot_with_lcel/) , 2024-01-27-0909
```
I found this blog articles on [https://blog.langchain.dev/building-chat-langchain-2/](https://blog.langchain.dev/buildin
g-chat-langchain-2/), about building a Rag Chatbot using langchain expression language. Looking at the entire code from 
the github repo, I am not pretty sure to understand what does this chain do:  
(

{

'question': RunnableLambda(itemgett
er('question')).with\_config(

run\_name='Itemgetter:question'

),

'chat\_history': RunnableLambda(serialize\_history).
with\_config(

run\_name='SerializeHistory'

),

}

| \_context

| response\_synthesizer

)  


It seems like: is gettin
g the question from a dictionary and pass it to the context etc..., but I can't see what's the input to the serialize\_h
istory function. I mean should not be chat\_history since it's the key assigned to the result of the function, it's not 
the input to the function right? 
```
---

     
 
all -  [ What is the best local LLM for agentic behavior? ](https://www.reddit.com/r/LangChain/comments/19fnp1g/what_is_the_best_local_llm_for_agentic_behavior/) , 2024-01-27-0909
```
I'm looking for the best LLM currently for agentic behavior in langchain. By best, I mean the most consistent with the l
east parsing errors.
```
---

     
 
all -  [ Anyway to compare a spec (word or excel) with its programming implementation for any gap/error ](https://www.reddit.com/r/LangChain/comments/19fma04/anyway_to_compare_a_spec_word_or_excel_with_its/) , 2024-01-27-0909
```
Let us say we have a simple spec like this below:

set my\_property to 1, when condition1 is met

set my\_property to 2,
 when condition2 is met

set my\_property to 3, when condition3 and condition33 are both met

set my\_property to 4, whe
n condition4 is met

Then this is python code below:

if condition1:

my\_property to 1

elif condition2:

my\_property 
to -2929 # people making error here

elif condition3 and condition33:

my\_property to 3

elif ...

This is an extremely
 simple example. I am wondering if langchain or other popular LLM library can somehow help us engineers achieve this to 
make our lives easier. I know langchain can somehow compare two similar (let us say earning report pdf) but not sure if 
it can help, even just a little bit, to spot any mistaken typo between spec and implementation?

&#x200B;
```
---

     
 
all -  [ Model concurrence ](https://www.reddit.com/r/LangChain/comments/19fkd55/model_concurrence/) , 2024-01-27-0909
```
I've been testing langserve with llama2, Mistral and falcon 7b. I'm struggling with concurrence problems when sending co
ncurrent request to langchain (only one request is processed, the other error 500, weird output for the only successful 
reques). I've tested those models concurrence outside langserve (with async calls) also failing. So, it's not a langserv
e problem, the models are not handling concurrence (even with things like vllm for model loading).

Somebody else has fa
ced a similar issue?
```
---

     
 
all -  [ LangChain is awesome, but have you tried Embedchain? ](https://www.reddit.com/r/LangChain/comments/19fhmbv/langchain_is_awesome_but_have_you_tried_embedchain/) , 2024-01-27-0909
```
Hi there! As you may know I often post here about my latest [LangChain tutorials and articles](https://www.gettingstarte
d.ai/tag/langchain). I was recently introduced to Embedchain, a Python library built on top of LangChain that takes care
 of your RAG needs in a few lines of Python code. It basically does all of the following for you right out-of-the-box:


* Sets up local Chroma DB
* Takes in data source (URL, YouTube, PDF, etc…)
* Makes chunks out of the data
* Converts the
 chunks to embeddings
* Stores the embeddings on the vector database
* Performs similarity search
* Query a large langua
ge model

Long story short, I took it for a spin and [wrote about it here](https://www.gettingstarted.ai/what-is-the-dif
ference-between-embedchain-and-langchain/) specifically, comparing it with LangChain.

If you‘re looking for a tool that
 lets you build a RAG app quickly, give it a try. You may find it suitable for your use case.

Let me know what you thin
k!
```
---

     
 
all -  [ How do I get ConversationalRetrievalChain to use a System Prompt? ](https://www.reddit.com/r/LangChain/comments/19fgxzb/how_do_i_get_conversationalretrievalchain_to_use/) , 2024-01-27-0909
```
System Prompt with ConversationalRetrievalChain: I am a newb playing with open-ai, chat-gpt, and langchain. Using open-a
i api's directly, I am able to set a system prompt to prepare the llm to respond to all all my interactions with the ini
tial system prompt instructions. Now I am using langchain's ConversationalRetrievalChain to try to interact with custom 
content. I have it working, but I would like to give the underlying llm (gpt-4) a system prompt as I do using the open-a
i api's directly. How can I do this? e.g. 'You are a helpful sale agent named Joe that works for ACME CO. Try to respond
 with links to products sold by ACME CO'
```
---

     
 
all -  [ RAG'd Repo and multi-agent chatbot for advanced codebase support? ](https://www.reddit.com/r/LangChain/comments/19fgnin/ragd_repo_and_multiagent_chatbot_for_advanced/) , 2024-01-27-0909
```
Hello,

I'm working on a project like this for another dataset, but I don't see why I can't apply it to my own repo. I l
ove using GPT for coding productivity, but one of the limitations is in api-type environments with multiple files and de
pendencies flying around - it's difficult to share all the relevant information to your agent or chatbot. 

Is there any
thing like this currently available? This isn't exactly rocket scient to start. If not, I'll start working on it
```
---

     
 
all -  [ Apply for almost 200+ application for Data scientist ](https://i.redd.it/tfajfzwyrmec1.jpeg) , 2024-01-27-0909
```
I don't what wrong in my resume. I am currently working as data scientist but i need to switch my job, but getting rejec
ted from everywhere i don't why,it would be very grateful if you guys help to get a job by reviewing my resume
```
---

     
 
all -  [ Choosing Between Langchain SQL and GPT-4 SQL Function ](https://www.reddit.com/r/LangChain/comments/19ffzyk/choosing_between_langchain_sql_and_gpt4_sql/) , 2024-01-27-0909
```
I'm working on a project that involves querying a database using natural language, and I'm trying to decide between usin
g Langchain SQL and the GPT-4 SQL function. From my understanding, Langchain SQL specializes in converting natural langu
age into SQL queries, which seems ideal for direct database interaction. On the other hand, gpt4 can also generate sqls 
directly with function calling. So it seems there is no need to use Langchain anymore.

I'd appreciate insights or exper
iences from anyone who has used either Langchain SQL or GPT-4 for similar purposes.
```
---

     
 
all -  [ Python OpenAI Langchain AWS Lambda Layer on M1 Mac setup ](https://www.reddit.com/r/aws/comments/19fbpk8/python_openai_langchain_aws_lambda_layer_on_m1/) , 2024-01-27-0909
```
For any heads out there that are delving into a Python OpenAI with Langchain Lambda function in an AWS env using an M1 M
ac, hope this is useful.

# Problem

When pip installing libraries on an M1 Mac, the architecture used does not register
 correctly when uploading to AWS lambda layer. This will result in the python lambda function code not being able to fin
d libraries when running.

# Steps

1. Install your libraries locally

&#8203;

    pip3 install openai langchain -t pyt
hon

2. Overwrite the problematic libraries manually (this may be different depending on what stuff you install)

    pi
p3 install --upgrade --platform manylinux_2_17_aarch64 --only-binary=:all: pydantic-core==2.14.1 -t python
    pip3 inst
all --upgrade --platform manylinux_2_17_aarch64 --only-binary=:all: pydantic==2.5.0 -t python
    pip3 install --upgrade
 --platform manylinux_2_17_aarch64 --only-binary=:all: numpy==1.26.2 -t python

3. Zip and upload your lambda layer (I u
se the cli in the example)

    zip -rq python_layer.zip python
    aws lambda publish-layer-version
    --layer-name {L
AYER_NAME}
    --zip-file filbeb://python_layer.zip
    --region {REGION}

4. Change your lambda function 'Runtime Setti
ngs' Architecture to **arm64** and point to your layer. This also was needed for the function to find the libraries in t
he layer.

Note: Not sure if this is necessary, but I think there are some incompatibilities with certain versions of la
ngchain with versions openai. The versions I got working together are as follows:

    langchain==0.0.348
    langsmith=
=0.0.69
    langchain-core==0.0.12
    openai==1.3.7

&#x200B;
```
---

     
 
all -  [ Advance Scrapping with LLM ](https://www.reddit.com/r/LangChain/comments/19fadp1/advance_scrapping_with_llm/) , 2024-01-27-0909
```
I am working on a project where I want to use LLMs (GPT4) to summarize the data from a website. First, I want to scrap a
ll the data from the all the links available in that website and then I want to use GPT4 to summarize the data. I can ge
t the summarization part done easily but how can I build a scrapper which can scrap the data from a website. For example
;

&#x200B;

If the website is a restaurant website then I would want to go over all the links in that site. It will be 
an iterative process and somehow I need to keep the already visited/scrapped links so that I shouldn't scrap it again. 


&#x200B;

Is there any framework or already built library/API available for this purpose?
```
---

     
 
all -  [ [Langchain] Les nouvelles mises à jour de Chatgpt remplaceront-elles le chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/19f81my/langchain_les_nouvelles_mises_à_jour_de_chatgpt/) , 2024-01-27-0909
```
J'ai travaillé sur un projet faisant l'extraction et le résumé des grands PDF à l'aide de Langchain. J'ai regardé l'Open
ai Dev Talk et je me demande si la récupération basée sur le cloud qui a été discutée remplacera probablement le chiffon
? Il semble que ce sera le cas, mais en même temps, l'utilisateur final devra probablement avoir GPT Plus pour accéder a
u modèle ou au bot créé avec le DOC.

Je sais qu'il est trop tôt pour le dire, mais j'espère avoir des informations avan
t d'aller trop loin avec mon projet, seulement pour réaliser qu'il sera remplacé par des fonctionnalités standard.

Pens
ées?

Traduit et reposté à partir de la publication 17pzvrw de la communauté langchain. Pour retrouver la publication or
iginale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Advanced Rags in Langchain ](https://www.reddit.com/r/LangChain/comments/19f5sqj/advanced_rags_in_langchain/) , 2024-01-27-0909
```
Recently I've been working on rags using langachain.
I also started a course on RAGs in deeplearning.ai, where they disc
ussed advanced rag techniques, like sentence window retrieval and automerging retrieval
But the course is mainly in llam
a index
I'm wondering if I can do some advanced retrieval in Langchain without api key
```
---

     
 
all -  [ Text splitter for JSX/React code to keep informational context? ](https://www.reddit.com/r/LangChain/comments/19f4ub6/text_splitter_for_jsxreact_code_to_keep/) , 2024-01-27-0909
```
What's the best Langchain.js text splitter to handle a JSX string like the following and maintain context of the text co
ntent?

The information we mostly care about is the user-readable text. However, JSX tags sometimes also contain relevan
t information (like the `alt` prop of the `Image`) so I don't want to just remove them. However, I'm removing all `class
Name` props from the string (via regex) to make the text less verbose.

```
export const metadata: Metadata = {
  title:
 'Home Page',
};

export default function Home() {
  return (
    <div>
      <div>
        <div>
          <h1>
       
     Hi, I'm Florian 👋
          </h1>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit
, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
        <
Image
          src={me}
          alt='A photo of me'
          height={350}
        />
      </div>
      <p>
        
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore ma
gna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        com
modo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla par
iatur.
      </p>
    </div>
  );
}
```
```
---

     
 
all -  [ Seeking Assistance with TextSplitter: Adding Bounding Box or Coordinate Values to PDF Chunks ](https://www.reddit.com/r/LangChain/comments/19f101u/seeking_assistance_with_textsplitter_adding/) , 2024-01-27-0909
```
 Hello everyone,

I'm wondering if anyone has successfully added bounding box or coordinate values to each chunk of a PD
F using CharacterTextSplitter or Recursive methods. I'm specifically interested in extracting the coordinates and storin
g them in metadata within a vector store.

My ultimate goal is to be able to query similar chunks and precisely highligh
t the corresponding text in the PDF from which it was extracted.

If there's already a solution or tool available for th
is purpose, could you kindly direct me to the right resources or provide some guidance?

Thank you in advance!
```
---

     
 
all -  [ Can i connect fine tune “FLAN T5 base” to langchain agent ](https://www.reddit.com/r/LLMDevs/comments/19f0azv/can_i_connect_fine_tune_flan_t5_base_to_langchain/) , 2024-01-27-0909
```
So i have fine tuned flan t5, on my custom dataset, and now is there anyway around where i can use langchain agents with
 my model. To analyse my database “mongodb”

I have tried OpenAi, with langchain, and there I tried Pandas Dataframe age
nt, who can interact with the dataframe  and give the answers regarding the dataframe i want to build similar but with f
lat t5. Or any other FREE model if available.
```
---

     
 
all -  [ Need advice for developing LLM Chatbot to recommend items from a store catalog ](https://www.reddit.com/r/ArtificialInteligence/comments/19excyh/need_advice_for_developing_llm_chatbot_to/) , 2024-01-27-0909
```
Specifically, I'm trying to get a chatbot to recommend users items from a specific store catalog, with about 2000-5000 d
ifferent items; mostly grocery, produce, snacks, etc. My approach right now is to cut it up into two AIs, one which face
s the user as a chatbot and recommends them products, and the other which extracts actual product IDs/SKUs from the firs
t AI's outputs (from there, Flutter app components are generated and presented to the user.) There are two things I'm in
terested in:

\- Would Langchain be a good tool to work with these AIs?

\- Is there any part where I may have to fine-t
une the first AI, or can I change its behavior purely in-context?

\- Can tools like LlamaIndex be used to facilitate th
e second AI?

I'm not an experienced LLM practitioner by any means; I've used Tensorflow for computer vision homework an
d ChatGPT for advice at the most, but I've taken a deep learning class so I understand the general concepts. Any help/ad
vice would be greatly appreciated!

(Follow-up, soon each food item will also have nutritional facts attached to it, whi
ch are vectorizable JSONs of mostly numbers and boolean flags. I'm not counting on the AI to learn about the user's heal
th needs or preferences, the user will input that themselves. Similar to the 2nd and 3rd points above, what is the best 
way to incorporate this data, in-context or fine-tuning, into the recommendation AI?
```
---

     
 
all -  [ What’s the best LangChain (JS) tutorial on YouTube ](https://www.reddit.com/r/LangChain/comments/19ewodj/whats_the_best_langchain_js_tutorial_on_youtube/) , 2024-01-27-0909
```
Can y’all recommend a good tutorial that will get me from start to finish for a RAG app I’m trying to make using LangCha
in JS?

I don’t wanna become a guru, just trying to get something on production asap. It needs to have memory.

Much app
reciated 🙏🏻
```
---

     
 
all -  [ agent platform for multi-modal agent capabilities ](https://www.reddit.com/r/LangChain/comments/19eqmgk/agent_platform_for_multimodal_agent_capabilities/) , 2024-01-27-0909
```
I'm developing an application using a large language model (LLM) and am in need of a robust core agent platform that sup
ports multi-modal agent capabilities. Currently, I'm utilizing LLM for intent recognition and named entity recognition, 
and then I do backend workflow orchestration without LLM or Agents. My goal is to transition to an agent framework for e
nhanced flexibility. I'm looking for frameworks that are resilient against prompt injection and easier to with open-sour
ce LLMs. 

So far, I've considered:

1. LangChain Agents (I have experience with it)
2. LLaMaIndex Agents
3. HayStack Ag
ents
4. AutoGen

Do you:

1. Recommend any additional frameworks that are worth exploring for agent orchestration? 
2. H
ave a preferred framework in this context?
3. have experience with these framework and want to share feedback?

&#x200B;

```
---

     
 
all -  [ agent platform for multi-modal agent capabilities ](https://www.reddit.com/r/LLMDevs/comments/19eqjcu/agent_platform_for_multimodal_agent_capabilities/) , 2024-01-27-0909
```
 

I'm developing an application using a large language model (LLM) and am in need of a robust core agent platform that 
supports multi-modal agent capabilities. Currently, I'm utilizing LLM for intent recognition and named entity recognitio
n, and then I do backend workflow orchestration without LLM or agents. My goal is to transition to an agent framework fo
r enhanced flexibility. I'm looking for frameworks that are resilient against prompt injection and easier to with open-s
ource LLMs. 

So far, I've considered:

1. LangChain Agents (I have experience with it)
2. LLaMaIndex Agents
3. HayStack
 Agents
4. AutoGen

Do you:

1. Recommend any additional frameworks that are worth exploring for agent orchestration? 
2
. Have a preferred framework in this context?
3. have experience with these framework and want to share feedback?

&#x20
0B;
```
---

     
 
all -  [ Streaming local LLM with FastAPI, Llama.cpp and Langchain ](https://www.reddit.com/r/LangChain/comments/19enjxr/streaming_local_llm_with_fastapi_llamacpp_and/) , 2024-01-27-0909
```
Hi, 

I have setup FastAPI with Llama.cpp and Langchain. Now I want to enable streaming in the FastAPI responses. Stream
ing works with Llama.cpp in my terminal, but I wasn't able to implement it with a FastAPI response. See this Stackoverfl
ow-Question (for code etc.): [https://stackoverflow.com/questions/77867894/streaming-local-llm-with-fastapi-llama-cpp-an
d-langchain?noredirect=1#comment137276485\_77867894](https://stackoverflow.com/questions/77867894/streaming-local-llm-wi
th-fastapi-llama-cpp-and-langchain?noredirect=1#comment137276485_77867894)

Most tutorials focused on enabling streaming
 with an OpenAI model, but I am using a local LLM (quantized Mistral) with llama.cpp. I think I have to modify the Callb
ackhandler, but no tutorial worked.

&#x200B;

Does anyone know how I can make Streaming working? I have a project deadl
ine on Friday and unitl then I have to make it work...
```
---

     
 
all -  [ Are there any models recommended for legal writing? ](https://www.reddit.com/r/LocalLLaMA/comments/19elj8h/are_there_any_models_recommended_for_legal_writing/) , 2024-01-27-0909
```
Hello friends, I know this post isn't as exciting as discussing the best porn model every week but I'd like recommendati
ons for a model tuned for legal writing or that has been trained on case law, legal briefs, that sort of thing. It shoul
d be more litigation focused, rather than transactional. Context size and comprehension are key. 

If there isn't anythi
ng that fits the bill, does anyone have a decent base model to recommend and maybe some comments or recommendations on h
ow to train a model? That's an area I haven't explored yet. My skill level is a beginner, so I've used Fiverr when I'm o
ut of my depth but I usually like to know enough to understand what I need and to clearly convey that to whoever I hire.
 I'm hoping you guys will help me get there. Estimates on time, manpower, processing power, and materials required would
 all be helpful to give me an idea of how far down the rabbit hole a project like this might send me.

By way of backgro
und, I'm an attorney that's been using ChatGPT since the beginning and I've since branched out to messing with vector da
tabases, Langchain, and hosting models locally. I have a 3090 but am open to renting better processing power if a model 
could give ChatGPT a run for its money. My use of ChatGPT can be fairly limited due to privacy concerns, attorney-client
 and work product privilege. The increase in context size has been great, but as has been discussed to death, ChatGPT's 
quality has gone down. It's legal writing is very poor, wordy, and unapproachable so while it occasionally strikes gold,
 it takes a lot of mining to get there.

Edit: Since this has been mentioned a few times already, the LLM is not perform
ing legal research. I am aware of the hallucination problem and understand those limitations. I mention being trained on
 case law more for the value in writing style and legal reasoning rather than substantive legal knowledge.
```
---

     
 
all -  [ Loader for website pages (offline) (Next.js/React) ](https://www.reddit.com/r/LangChain/comments/19elb7z/loader_for_website_pages_offline_nextjsreact/) , 2024-01-27-0909
```
I am building a website with an integrated chatbot. How would you load the page info into documents? I want to make my c
ode reusable for future projects.

Right now I'm using the [GitHubRepoLoader](https://js.langchain.com/docs/integrations
/document_loaders/web_loaders/github) to turn the pages into documents, but this requires the code to be available in a 
GitHub repository. This is not great for local development (because we don't have the latest data).

Would you load the 
pages from the file system instead? Or is there a better solution?

Any classes/helpers you can point me to? I'm using L
angchain.js.
```
---

     
 
all -  [ My 2 cents for New Developers. ](https://www.reddit.com/r/developersIndia/comments/19ej7i8/my_2_cents_for_new_developers/) , 2024-01-27-0909
```
From my 8 years of experience i have learnt that in India, there are lot more job opening in Java as compared to lets sa
y python or javascript. I have always struggled to get my resume shortlisted since i never worked in Java. (But fortunat
ely may cards played out well) I am writing this out since market has started opening and a lot of jobs have started pop
ping requiring Java Developers.

So, If you are starting up as a software Engineer. Don't rely on fancy stuff like 'Writ
ing LLM pipelines using python langchain' or writing backend services in GoLang. Stick to the basics and **develop web a
pps in Java Spring or JSF**. Don't go with MongoDB or any NoSQL databases, **stick to SQL**.   


Also, I see a lot of p
eople **not** open to work on 'X' technology. Always be language agnostic. Even if you don't have experience. Its always
 good to say: 'I have my basics tightened up, I will be able to pick up 'X' technology quickly'.   


All the best guys!
  

```
---

     
 
all -  [ Ever wondered how to build a chatbot? ](https://www.reddit.com/r/SideProject/comments/19ej4sc/ever_wondered_how_to_build_a_chatbot/) , 2024-01-27-0909
```
Here's a free code-along that'll get you to grips with RAG, the OpenAI API and Pinecone!

Building Chatbots with OpenAI 
API and Pinecone - Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answer
s questions about research papers. Code Along on DataCamp Workspace: [https://www.datacamp.com/code-along/building-chatb
ots-openai-api-pinecone](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

This is just one se
ssion in a 9-part free (yep, free!) series that will get you on the path to becoming an AI Developer. Have fun! 

Other 
sessions can be found here: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
all -  [ Best resources to learn to advanced RAG topics & and to end projects ](https://www.reddit.com/r/LangChain/comments/19ehe5m/best_resources_to_learn_to_advanced_rag_topics/) , 2024-01-27-0909
```
it has a collab notebook, blog links & all code
```
---

     
 
all -  [ React/JSX to text parser? ](https://www.reddit.com/r/LangChain/comments/19ehc9w/reactjsx_to_text_parser/) , 2024-01-27-0909
```
I want to build a **chatbot** that has access to **all pages** in my website's GitHub repository. 

The [GitHubRepoLoade
r](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/github#usage) makes it easy to fetch all page
s and turn them into documents. But I would also like to **strip these documents of all the React code** and keep only t
he user-readable information.

I tried Langchain.js's [html-to-text](https://js.langchain.com/docs/integrations/document
_transformers/html-to-text) converter but that didn't work. I also found [react-to-text](https://www.npmjs.com/package/r
eact-to-text) but this one expects an actual React component as its argument. I have the full file as a string.
```
---

     
 
all -  [ How to make a properly prompt to ask questions based on a context? ](https://www.reddit.com/r/OpenAIDev/comments/19ef5pv/how_to_make_a_properly_prompt_to_ask_questions/) , 2024-01-27-0909
```
Hello!

I was using Langchain for OpenAI and now i wanted to use the library OpenAI, in specific the Completion.create m
ethod, and looks like the prompt is no longer useful, anyone know how to change this to make it work for openai library?
 Thank you so much!

    Use the following pieces of context to answer the question at the end. If you don't know the an
swer just say I don't know, don't try to make up an answer.
    
    {context}
    
    Question: {question}
    Answer 
in Italian:

Regards!
```
---

     
 
all -  [ Has anyone used Llama.cpp python with gpu in vscode to load local llm. Does it even work with VSCode ](https://www.reddit.com/r/LangChain/comments/19eco2b/has_anyone_used_llamacpp_python_with_gpu_in/) , 2024-01-27-0909
```
I’ve used these commands to install it in VSCode 

export CUDACXX='/mnt/c/Program Files/NVIDIA GPU Computing Toolkit/CUD
A/v12.3/bin/nvcc.exe'
 export CMAKE_ARGS='-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all-major -DCUDAToolkit_ROOT=C:\P
rogram Files\NVIDIA GP
 export FORCE_CMAKE=1
 pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade

S
uccessfully installed but it’s still not accessing gpu. I’ve nvidia GeForce RTC 3070 Ti 

How do I know how many n_gpu_l
ayers to set
```
---

     
 
all -  [ Purpose of Agents ](https://www.reddit.com/r/LangChain/comments/19ecbnb/purpose_of_agents/) , 2024-01-27-0909
```
Hi, I've been using agents with autogen and crew, and now langgraph, mostly for learning and small/mid scale programs.
T
he more I use them the more I'm confused about the purpose of the agent framework in general.

The scenarios I've tested
: read input, execute web search, summaries, return to user. Most other usecases also follow a sequential iteration of s
teps. 
For these usecases, there is no need to include any sort of agents, it can be done through normal python scripts.

Same goes for other usecases

I'm trying to think about what does agents let us do that we could not do with just scrip
ts with some logic. Sure, the LLM As OS is a fantastic idea, but in a production setting I'm sticking to my scripts rath
er than hoping the LLM will decide which tool to use everytime...

I'm interested to learn the actual usecases and poten
tial of using agents too execute tasks, so please do let me know
```
---

     
 
all -  [ Create AI Chatbots for Websites in Python - EmbedChain Dash ](https://www.reddit.com/r/LangChain/comments/19eaixd/create_ai_chatbots_for_websites_in_python/) , 2024-01-27-0909
```
Hey Everyone,  
A few days ago, I created this free video tutorial on how to  build an AI Chatbot in Python. I use the E
mbedChain (built on top of LangChain) and Dash libraries, as I show how to train and interact with your bot. Hope you fi
nd it helpful. 

[https://youtu.be/tmOmTBEdNrE](https://youtu.be/tmOmTBEdNrE)

&#x200B;

https://preview.redd.it/t2ebobt
8zbec1.png?width=1280&format=png&auto=webp&s=b2dcd9f2a930da35f2862b368a535d30ad885825
```
---

     
 
all -  [ How do I scale the current use case that involves using fine tuned gpt 3.5 model? ](https://www.reddit.com/r/OpenAI/comments/19ea148/how_do_i_scale_the_current_use_case_that_involves/) , 2024-01-27-0909
```
I am looking for some tools in the cloud that I can use to scale a particular use case for my company. We were working o
n a chatbot that involved using gpt 3.5 and langchain agents. Sine fine tuning was introduced later last year, we have q
uickly adapted to that and it worked wonders for our use case. 

Now, all the scripts I have created for data preparatio
n for fine tuning is in my local machine. We are looking to use some cloud based solutions to create and manage the trai
ning data. Now, if it were only one use case, I could simply use gcs buckets to store and version the data. But my boss 
wants me to scale for multiple use cases. 

Here's a scenario:

If there are 2 dozen generative AI use cases which invol
ves the usage of fine tuned model, how would I manage data for every use case. And if other team wants to utitlize some 
of the existing data from the existing use case, how could they easily identify where to look for and generate similar d
ata, etc. 

I'm not sure if I am able to define the problem correctly, but from what I understood is that my boss wants 
me to scale the current use case for multiple use cases with multiple datasets while managing the training data effectiv
ely so that its not a burden when someone wants to use the same data. 

I'm not sure which direction shall I head to in 
order to solve this problem. I'll be glad if someone can help me on this.
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-27-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-27-0909
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-27-0909
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-27-0909
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

     
