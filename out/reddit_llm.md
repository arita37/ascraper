 
all -  [ Can I use LangChain to only give me the context is found from the retrieval? ](https://www.reddit.com/r/LangChain/comments/1csy9ul/can_i_use_langchain_to_only_give_me_the_context/) , 2024-05-16-0910
```
I'm building an app with Next.js. 

Is it possible to have LangChain only give me the context it found from the vector s
tore? I then want to take this context and manually insert it into another part of my app that's using an llm as a part 
of the message history (but I don't want to do this final step in LangChain)

So I don't want LangChain to give me the f
inal output just the context is found using the vector store and OpenAi embedding model.

I'm still learning sry if this
 a stupid question. 

I'm having issues streaming output from LangChain to the front end and want to use something else 
I already have setup
```
---

     
 
all -  [ Any example of using llm.bind_tool ? i get not implemented error - want to run tools w GPT-4o ](https://www.reddit.com/r/LangChain/comments/1csvh8w/any_example_of_using_llmbind_tool_i_get_not/) , 2024-05-16-0910
```
Thanks
```
---

     
 
all -  [ How can I use LangChainJs to fill out csv file according to big context and prompt? ](https://www.reddit.com/r/LangChain/comments/1csts7q/how_can_i_use_langchainjs_to_fill_out_csv_file/) , 2024-05-16-0910
```
I am currently working on a project where I need to fill documents (CSV files) according to requirements in a big compen
dium (800+ pages PDF).

for example:

* context:
   * the PDF compendium of 800 pages with instructions and detailed leg
al requirements to be met when implementing infrastructure projects in IT sector
* CSV file:
   * a checklist-style CSV 
file containing the short name of the subject from the PDF compendium and columns to input things to be checked and proc
essed by a person (or in this case: AI)

|Subject|Responsible|Price|Risks|
|:-|:-|:-|:-|
|A.1.1.|Author of this file|$20
.000|If not done, we are doomed|

* Prompt
   * 'I want to add a exchange a router in Building C3.'
   * 'I want to add 
a gitlab server to our network'

In both cases, the output should be a CSV file or CSV text .

**These are the models im
 using (and liking):**

* model: wizardlm2:7b
* embedding model: mxbai-embed-large

**What I have done so far**

* readi
ng in the pdf files
* embedding the pdf files
* reading in the csv file
* embedding the csv file (<- is this correct?)
*
 created a prompt

\`\`\`  
Fill the csv file in the context with valuable data found in the embeddings according to the
 question.

Do not guess, do not add anything. Use only the context.

{context}

Question: {input}

\`\`\`

**What is no
t working. AKA: What is my question?**

The output the model is giving me is unstructured and has nothing to do with the
 CSV file I put into the context.

Is there a way that I can make the AI

1. Read in PDFs
2. Read in CSV
3. Listen to th
e prompt
4. Output a CSV file or (- like text)  I gave it with data from the embedded PDFs correctly according to the ne
eds arising from the input prompt

?
```
---

     
 
all -  [ LLM Orchestration framework or own python code, which is better? ](https://www.reddit.com/r/LangChain/comments/1cstpmx/llm_orchestration_framework_or_own_python_code/) , 2024-05-16-0910
```
i need a suggestion on a situation at work.

I am writing code for an application. i have 2 options, that is, either cho
ose an existing python framework that is available in the market or write my own python code.

Existing framework: LangC
hain, LlamaIndex

Pros:

1.	used a lot outside in the market. just in case if i want to shift another company. i can eas
ily adapt and can earn more money

2.	I can create Agents (AI) with little ease as i dont have to implement everything f
rom scratch (usually research work and strategies are implemented in this framework). implementing features becomes fast
er

3.	as knowledge workers are more aware of this framework - hiring them and getting them to understand the code becom
es easy 

Cons:

1.	So many abstractions in this framework and i fully dont understand it. few months back i tried to us
e this framework and i couldn't customize it for our situation. I am worried if i use this and make some progress and la
ter realize that it is not customizable. i will be screwed. lot of work will be wasted.

Own Code:

Pros:

1.	i can impl
ement all the functionalities by myself. i can design code base and write everything from scratch. this skill is valued 
in lot of places especially in startups as you have literally implemented lot of things from scratch. this way i can get
 a hang over the language and my skill improves drastically

2.	i get to do research and implement them with my own code
.

3.	i can customize it for my specific scenario

4.	the company will have a lot of dependency on me 

Cons:

1.	lot of
 work

2.	development might not be as fast paced as i would have liked it to be.

3.	i might get stuck and not find any 
solution as i am the only person available who has knowledge on this in this company.

Any suggestions are appreciated.





```
---

     
 
all -  [ Open AI APIs are the only reliable APIs in production ](https://www.reddit.com/r/LangChain/comments/1csrtc3/open_ai_apis_are_the_only_reliable_apis_in/) , 2024-05-16-0910
```
After having worked with Anthropic API and Gemini 1.5 Pro & Flash APIs. OpenAI API seems to be the only reliable API ser
vice available.   
With Anthropic - I am unable to add credits to their console, even after multiple mails to the custom
er support I have received no resolution. So I finally have to give up hope and just use Open AI.  
With Google Gemini -
 The APIs are absolutely unreliable, you are not sure when the APIs will return an answer and when they will not. I keep
 encountering error from the API something like: StopCandidateException: finish\_reason: RECITATION  
So again no point 
in using Gemini, just switch to Open AI.

Hoping this experience will benefit the community.

Anyone else having these i
ssues.
```
---

     
 
all -  [ Guidance needed regarding Anything LLM ](https://www.reddit.com/r/MistralAI/comments/1cspnl8/guidance_needed_regarding_anything_llm/) , 2024-05-16-0910
```
Hi Everyone,

I'm using AnythinLLM for developing a ChatBot for my organization. The thing is due to some infosec concer
ns we're not using any Online/API based or cloud based solutions.

We're using AnythinLLM as our ChatBot tool to use it 
locally,but the problem I'm facing is that my LLMs are showing too much hallucination no matter how much prompt engineer
ing i do. I want him to answer from the provided context (data) only but everytime it give me irrelevant extra informati
on and very long answers. In short it is not following my prompt.

But the main thing is i have tried different local mo
dels such as Llama3, OpenHermes2.5 (8Q), Mistral-7B (8Q), Phi-3 but none of them performed well. I have developed my mod
el using open hermes2.5 on Vscode using langchain as well and it's performing relatively well and answering me from my p
rovided context. But when i use anythingLLM it always give me answer from its external knowledge even though I'm using Q
uery mode.

Sometime on anythingllm even before uploading a data i query it like **Hello** for that it also provide me s
ome irrelevant response and sometime Don't even provide response.

The stack I'm using on Anythingllm 

- LanceDB
- Anyt
hingllm preferred Embeddings model
- Local LLMs using Ollama
- Context window (4096)
- Query Mode
- Chunk Size (500)
- O
verlap (50)
- Temperature (0.5)

Prompt :
***You have been provided with the context and a question, try to find out the
 answer to the question only using the context information. If the answer to the question is not found within the contex
t, return 'I don't know' as the response. Use three sentences maximum and keep the answer concise.***


I have checked t
he similar chunks retrieved from the retrieval and answer is present in that retrieved chunks but answer provided by the
 model is not from that chunks it's making up answers.

Any help or guidance regarding this will be highly appreciated.
```
---

     
 
all -  [ What's the best approach to building a model to match Job Titles to Standardized Roles Using NLP? ](https://www.reddit.com/r/learnmachinelearning/comments/1cspfbh/whats_the_best_approach_to_building_a_model_to/) , 2024-05-16-0910
```
A small part of my job involves getting a client's dataset of employees, and mapping their positions to a list of standa
rdised titles, based on the roles' title, the assumed positoin in the hierarchy, and the salary. For example, something 
like 'Finance Assistant' would be mapped to our standardised role 'Accounts Clerk', or a 'Helpdesk Agent' might be mappe
d to our 'Customer Care Agent' role. 



I have a CSV file with 280 standardised titles as well as a brief description o
f each one. Although the past data is not so accurate, I also have past mappings of company titles to each standardised 
role. 

  
I'm currently exploring the best approach for this task. Previously, I was advised against using an LLM for t
his, but I've since learned about Retrieval-Augmented Generation (RAG) and wonder if it might be applicable here. I’m co
nsidering using BERT, but I'm open to suggestions for more advanced models if they offer better accuracy.

  
Here are s
ome ideas I've thought of and come across

1. Using BERT (uncased or large) for semantic understanding and *maybe* GPT-3
 embeddings more contextual understanding (could help given similar roles, e.g. a Compliance Officer is not the same as,
 say, a Supply Chain Officer). The goal is to achieve a high level of accuracy in mapping.
2.  Considering using some ki
nd of RAG (perhaps through Langchain) to additional contextual information from the descriptions.

Are there other model
s or approaches that might be better suited for this kind of semantic and contextual matching? Looking forward to feedba
ck.


```
---

     
 
all -  [ A step-by-step tutorial to building semantic search with LangChain ](https://blog.meilisearch.com/langchain-semantic-search-tutorial/?utm_campaign=social&utm_source=reddit) , 2024-05-16-0910
```

```
---

     
 
all -  [ Need trivial help with RAG: how do I programmatically handle the case in which the Q&A Chain's retri ](https://www.reddit.com/r/LangChain/comments/1csohun/need_trivial_help_with_rag_how_do_i/) , 2024-05-16-0910
```
I'm sorry for the trivial question, but I've been struggling with this and cannot find a solution. 

I have a retrieval 
with a list of questions and answers, and I have a chain defined, but im struggling to properly handle the case in which
 the question being asked by the user doesn't exist in my vector store (or even in a simplified system, where a 5 questi
ons and their answers are added in the prompt - without a vectorstore and retrieval) 

Thanks a lot in advance :)
```
---

     
 
all -  [ LLM model with timezone issue ](https://www.reddit.com/r/LangChain/comments/1csobxi/llm_model_with_timezone_issue/) , 2024-05-16-0910
```
issue: I am build RAG chat bot and my model is taking server time zone when i ask what is current date and time how fix 
it ?
```
---

     
 
all -  [ Message and Prompt Classes -- are they helpful? ](https://www.reddit.com/r/LangChain/comments/1csmlwe/message_and_prompt_classes_are_they_helpful/) , 2024-05-16-0910
```
I hope I do not sound like a jerk here, but ... more and more I feel that these classes are more trouble than they are w
orth.  I'd welcome it if someone made a case for their existence.

Here's the claim: we are (almost?) always better off 
just working with f-strings and format instead of working with these classes.  Here is my rationale:

* Concatenation:  
Most recently, I have been fighting with trying to concatenate various \`Message\` and \`PromptTemplate\` classes.  Some
times this works, sometimes it fails at runtime. This is made worse by the fact that static type-checking doesn't detect
 this prior to runtime.
* Type hints: the above illustrates a problem with these classes that extends beyond them and is
 pervasive in Langchain. There are a lot of type hints, and there are type failures, but the type hints don't help.  The
 type specifications are often so loose that type checking tools cannot warn me about errors to come.  This is related t
o another pervasive problem:
* The use of opaque objects and loose typing causes many problems in development with Langc
hain. When I try to write my own code to extend langchain behavior I often find that I have to handle many cases that ha
ve the potential to cause errors because of loose typing. For example, anything handling input going into an `LLM` or `C
hatModel` must handle `PromptValue`, `str`, `Sequence` of `MessageLikeRepresentation` and `dict` s with unknown sets of 
keys. When I process those `Sequence`s I must then deal with `BaseMessage`, `str`, `Tuple[str,str]` and `Dict[str, Any]`
.  I apologize for being cranky, but these type hints seem more aimed at ensuring that type checkers never raise errors,
 rather than aimed at helping the programmer write correct code.  The type checker is a tool, not an oracle to be worshi
pped.
* `PromptTemplate`s work extremely poorly when they must accommodate code as template-fillers.  The curly braces i
n code confuse prompt handling no end.

Looping back to the hypothesis: If I try to assemble a prompt in stages by plugg
ing values in over and over, the use of `PromptTemplate` and `Message` objects makes my life more difficult and costs me
 hours of debugging.  My recent alternative is simply to assemble together ordinary strings, using `format` as necessary
, until the last minute before they are needed, at which time I wrap them in `PromptTemplate.from_template()` so that th
ey can be put in an LCEL chain expression.

IMO this indicates that the layers and layers of complex types and meta-clas
ses are more trouble than they are worth.  I'm willing -- indeed hoping! -- that someone will prove me wrong.  How does 
my experience align with that of other langchain users?
```
---

     
 
all -  [ Dall-E Api low quality images ](https://www.reddit.com/r/LangChain/comments/1csmium/dalle_api_low_quality_images/) , 2024-05-16-0910
```
I use Dall-E as a tool for my langchain agent but the quality of the images are so low compared to the images from the C
hatGPT Interface.

Is there a way to fix this?


```
---

     
 
all -  [ RAG chat over OpenAI APIs, the OpenAI sandbox, and the OpenAI forums ](https://www.reddit.com/r/OpenAIDev/comments/1csko4c/rag_chat_over_openai_apis_the_openai_sandbox_and/) , 2024-05-16-0910
```
LangChain has a great chat interface called 'Langchain Chat' for interacting with the langchain docs.

I want something 
similar: I'd like to chat with a recent, powerful LLM that is endowed with RAG populated with up-to-date information on 
the OpenAI APIs, the OpenAI sandbox, and the OpenAI forums. I want this so I can more quickly assess the state of the ar
t in terms of what is available.

Does this exist or do I need to build it?

Also, BTW do you know a name (or could you 
propose a name) for this 'RAG over the docs and forums?' Maybe APIDocRag? I'm just really wishing that we had a term wit
h 'unique google-ability' to find out if company or product XYZ had this obvious service

Clarification: this is NOT a r
equest for an open source chat library that can interact with the API.
```
---

     
 
all -  [ Text-to-SQL conversion for ETL testing using Snowflake ](https://www.reddit.com/r/LLMDevs/comments/1csjztr/texttosql_conversion_for_etl_testing_using/) , 2024-05-16-0910
```
Hi,

I have to do a POC and below are the steps or direction how to implement using Langchain and Snowflake DB and LLM
—
—————
1. User will enter the Transformation Logic sheet where every row will have the logic how the values inside the So
urce Table are mapped/modified to Target Table.
2. User will also have access to Target Table to check whether the SQL q
uery generation using Transformation logic correctly mapped the values to Target table or not.

I have tried using excel
 sheet and a basic table in ChatGPT and I was able to accomplish upto good level.
I want to know how to implement in pyt
hon and is there any good LLM for such text-sql conversion.
Many thanks
```
---

     
 
all -  [ Utilizing both LlamaIndex and LangChain ](https://www.reddit.com/r/LocalLLM/comments/1csiykw/utilizing_both_llamaindex_and_langchain/) , 2024-05-16-0910
```
Hello Dear fellow,

I'm currently new in this domain and was exploring multiple possibilities in RAG. 

I'm curious whet
her we can use both LlamaIndex and LangChain in parallel like utilizing Llama Index for indexing and retriever purpose a
nd other operations on LangChain 

If yes, what will be its impact on performance of overall application
```
---

     
 
all -  [ Need help with Langchain & vercel generative UI integration ](https://www.reddit.com/r/LangChain/comments/1csicrm/need_help_with_langchain_vercel_generative_ui/) , 2024-05-16-0910
```
Hi everyone, I've built a pdf-chatbot using langchain and pinecone db. I'm further planning to integrate vercel's latest
 generative UI feature   [https://chat.vercel.ai/](https://chat.vercel.ai/)  ( [https://github.com/vercel/ai-chatbot](ht
tps://github.com/vercel/ai-chatbot) ). 

so here's the flow:   
1. User should be able to upload multiple pdf's  
2. All
 the pdf's will be stored in pinecode vector Storage  
3. User will be able to prompt and based on the prompt the AI wil
l call generative UI like interactive quizes etc via react server components

  
Can anyone help me with how to integrat
e langchain  with streamUI from vercel SDK?  [https://sdk.vercel.ai/docs/reference/ai-sdk-rsc/stream-ui](https://sdk.ver
cel.ai/docs/reference/ai-sdk-rsc/stream-ui)
```
---

     
 
all -  [ Embedding with large database ](https://www.reddit.com/r/LangChain/comments/1cs8ger/embedding_with_large_database/) , 2024-05-16-0910
```
HI guys
so i have a question. I have a postgres database that holds about information about clients. One table is a fina
ncial table, another is an incident table, the third is a client escalations table and finally the last one holds free t
ext that is filled in the crm like notes…

these are all linked one way or another by cliend ID but the data within each
 table can sometimes be nested dictionaries…like under notes you could have a dictionary of , {date, text, from, to}

i 
want to take all of this data and create embedding on it…what i’m confised about is the best way to do it…do I?

Somehow
 connect all this data into a single flatted dataframe? if so this will be a massive dataframe with 100+ columns

Can i 
create an embedding for each table? if i do this, will the embedding model know that two tables are connected via a clie
nt identifier that is present in both or do i have to somehow force this connection? if so how?

Any other options?

Tha
nks in advance
```
---

     
 
all -  [ Gpt-4o ReAct agentic RAG ](https://www.reddit.com/r/LangChain/comments/1cs3asj/gpt4o_react_agentic_rag/) , 2024-05-16-0910
```
I spent the whole day testing Gpt4-o capabilities to do agentic RAG using a standard prompt (hwchase17/ReAct) personaliz
ed for my particular use case: basically, it's the standard prompt but with a couple of High level instructions at the e
nd, to give the agent some personality.
It is unable to respect the response format about half of the time.

Gpt-4-turbo
 instead works like a charm.. almost all the time.
It feels like Gpt-4o is a quantized version of Gpt-4-turbo on instruc
tion following.

Am I the only one?
```
---

     
 
all -  [ Building a GPT-4o AI Agent using Langchain ](https://www.reddit.com/r/LangChain/comments/1cs333y/building_a_gpt4o_ai_agent_using_langchain/) , 2024-05-16-0910
```
Hello r/Langchain, we have been building an Autopilot AI tool called Sparks AI for the past 5 months that combines web s
earch, external app integrations and Langchain to performs complex multi-step tasks in the background. 

  
Please check
 it out at [https://getsparks.ai](https://getsparks.ai) and provide your thoughts.   
Any feedback & ideas are welcome. 

```
---

     
 
all -  [ Non-Flexible Output parsing for JSON ](https://www.reddit.com/r/LangChain/comments/1cs2gw2/nonflexible_output_parsing_for_json/) , 2024-05-16-0910
```
Hi there. So a problem is that if someone wants to parse, let suppose a parameter named Name1, Name2 and so on using out
put parse, how would that be done since once you define Name, the output parsing only returns 1 name only.
So how can be
 the LLM flexible to add Name1,Name2 and so on based on the text inpit it recieves?
```
---

     
 
all -  [ Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/LLMDevs/comments/1crwik6/building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-16-0910
```
Hey r/LLMDevs, I published a new article where I built an observable semantic research paper application.

This is an ex
tensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most relevant PDF
 documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval.
3. Enh
ancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.com/towa
rds-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](https://m
edium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1
cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tahreemrasu
l/semantic_research_engine)
```
---

     
 
all -  [ Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/llmops/comments/1crwht7/building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-16-0910
```
Hey r/llmops  , I published a new article where I built an observable semantic research paper application.

This is an e
xtensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most relevant PD
F documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval.
3. En
hancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.com/tow
ards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](https://
medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd
1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tahreemras
ul/semantic_research_engine)


```
---

     
 
all -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-16-0910
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
all -  [ Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/ChatGPTCoding/comments/1crwd15/building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-16-0910
```
Hey r/ChatGPTCoding, I published a new article where I built an observable semantic research paper application.

This is
 an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most releva
nt PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval.

3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.co
m/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](htt
ps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c3
45fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tahre
emrasul/semantic_research_engine)


```
---

     
 
all -  [ What are your current challenges with evaluations? ](https://www.reddit.com/r/LangChain/comments/1crvzvd/what_are_your_current_challenges_with_evaluations/) , 2024-05-16-0910
```
What challenges are you facing and what tools are you using? I am thinking about building out a developer friendly open 
source evaluations tool kit. Thinking of starting with a simple interface where you pass the context, input, output and 
expected output and run it through some basic tests - both LLM based and non LLM based and also allow the ability to wri
te custom assertions.

But, am wondering if you all have any insights into what other capabilities might be useful. 
```
---

     
 
all -  [  100+ Free Courses Available on Udemy and Coursera ](https://www.reddit.com/r/Udemy/comments/1crthg4/100_free_courses_available_on_udemy_and_coursera/) , 2024-05-16-0910
```
Master Course : Business Cold Calling & Lead Generation 2.0

https://courze.org/master-course-business-cold-calling-lead
-generation-2-0/



HR Conflict Management and Emotional Intelligence 3.0

https://courze.org/hr-conflict-management-and
-emotional-intelligence-3-0/



Digital Foundations: Exploring IT & Multimedia Fundamentals

https://courze.org/digital-
foundations-exploring-it-multimedia-fundamentals/



Master Course in Data Visualization & Data Warehousing (101)

https
://courze.org/master-course-in-data-visualization-data-warehousing-101/



Python And Flask  Demonstrations Practice Cou
rse

https://courze.org/python-and-flask-demonstrations-practice-course/



Human Resources : Corporate Learning and Dev
elopment (L&D)

https://courze.org/human-resources-corporate-learning-and-development-ld/



Safety Leadership: Industry
 Workplace Health and Safety 2.0

https://courze.org/safety-leadership-industry-workplace-health-and-safety-2-0/



Achi
eving Better Work and Life Balance for Business People

https://courze.org/achieving-better-work-and-life-balance-for-bu
siness-people/



Cross-cultural Communication and Cultural Intelligence 2.0

https://courze.org/cross-cultural-communic
ation-and-cultural-intelligence-2-0/



Professional Agile Leadership Course 101 : PAL-E & PAL I

https://courze.org/pro
fessional-agile-leadership-course-101-pal-e-pal-i/



Real Estate Investing, Real Estate Marketing & Flipping 2.0

https
://courze.org/real-estate-investing-real-estate-marketing-flipping-2-0/



Clojure Introduction: Learn Functional Progra
mming

https://courze.org/clojure-introduction-learn-functional-programming/



Create a GUI with Python

https://courze
.org/create-a-gui-with-python/



Python Video Processing

https://courze.org/python-video-processing/



Navigate the L
inux File System

https://courze.org/navigate-the-linux-file-system/



Cómo Crear una Academia Online con WordPress y T
utor LMS

https://courze.org/como-crear-una-academia-online-con-wordpress-y-tutor-lms/



Máster en Diseño Web con Intel
igencia Artificial 2024

https://courze.org/master-en-diseno-web-con-inteligencia-artificial-2024/



Máster en Comercio
 Electrónico con WordPress 2024

https://courze.org/master-en-comercio-electronico-con-wordpress/



Cómo Crear un Blog 
con WordPress Para Principiantes 2024

https://courze.org/como-crear-un-blog-con-wordpress-para-principiantes-2023/



M
aster Course : Advertising Strategy 2.0

https://courze.org/master-course-advertising-strategy-2-0/



Lean Six Sigma an
d Agile Methodology in Project Management

https://courze.org/lean-six-sigma-and-agile-methodology-in-project-management
/



AI and Operations Management & Strategic Management 2.0

https://courze.org/ai-and-operations-management-strategic-
management-2-0/



Essential After Effects: From Beginner to Motion Master

https://courze.org/essential-after-effects-f
rom-beginner-to-motion-master/



Electronics : Diode (Part 2) : Diode applications

https://courze.org/electronics-diod
e-part-2-diode-applications/



Comprehensive DaVinci Resolve With Color Grading Masterclass

https://courze.org/compreh
ensive-davinci-resolve-with-color-grading-masterclass/



Communication Skills Starter Pack

https://courze.org/communic
ation-skills-starter-pack/



Affiliate Marketing For Beginners – Simple Steps to Success

https://courze.org/affiliate-
marketing-for-beginners-simple-steps-to-success/



Mastering LangChain and AWS: A Guide to Economic Analysis

https://c
ourze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis/



Learning Business Contracts for Beginners

https:
//courze.org/learning-business-contracts-for-beginners/



Startup Fund Raising

https://courze.org/startup-fund-raising
/



Advanced Excel Course With Shortcuts Tips and Tricks for JOB

https://courze.org/advanced-excel-course-with-shortcu
ts-tips-and-tricks-for-job/



SQL Bootcamp with MySQL, PHP & Python : 5 Courses in 1

https://courze.org/sql-bootcamp-w
ith-mysql-php-python-5-courses-in-1/



AutoCAD Civil 3D – MEGA course for Civil Works – AulaGEO

https://courze.org/aut
ocad-civil-3d-mega-course-for-civil-works/



Introduction to Cyber Security

https://courze.org/introduction-to-cyber-s
ecurity/



Python & Django | The Complete Django Web Development Course

https://courze.org/python-django-the-complete-
django-web-development-course/



Python Programming Language (Practice Projects)

https://courze.org/python-programming
-language-practice-projects/



Fundamentals of computer science | Short Term Course(Arabic)

https://courze.org/fundame
ntals-of-computer-science-short-term-coursearabic/



Google Sheets – The Complete Google Sheets Course

https://courze.
org/google-sheets-the-complete-google-sheets-course/



ReactJs – The Complete ReactJs Course For Beginners

https://cou
rze.org/reactjs-the-complete-reactjs-course-for-beginners/



NumPy, SciPy, Matplotlib & Pandas A-Z: Machine Learning

h
ttps://courze.org/numpy-scipy-matplotlib-pandas-a-z-machine-learning/




```
---

     
 
all -  [ Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/LangChain/comments/1crtas2/building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-16-0910
```
Hey r/LangChain , I published a new article where I built an observable semantic research paper application.

This is an
 extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most relevant 
PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval.
3. 
Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.com/t
owards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](https:
//medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345f
cd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tahreemr
asul/semantic_research_engine)


```
---

     
 
all -  [ Cross Encoder vs. ColBERT in RAG ](https://www.reddit.com/r/LangChain/comments/1crt25e/cross_encoder_vs_colbert_in_rag/) , 2024-05-16-0910
```
Hi,

I want to improve my RAG system and read about ColBERT and Cross-Encoders, but I don't really get what is the diffe
rence here, can someone explain?

  
Also would be nice to have some experiences what worked better for your RAG. I have
 to rely on multilingual models (to use german language), so I picked out:

- [https://huggingface.co/antoinelouis/colbe
rt-xm](https://huggingface.co/antoinelouis/colbert-xm)

- [https://huggingface.co/cross-encoder/msmarco-MiniLM-L12-en-de
-v1](https://huggingface.co/cross-encoder/msmarco-MiniLM-L12-en-de-v1)

  
Which one would you prefer?
```
---

     
 
all -  [ Batch inference in langchain's question answering chain. ](https://www.reddit.com/r/LLMDevs/comments/1crqd4y/batch_inference_in_langchains_question_answering/) , 2024-05-16-0910
```
Hello! I'm a newbie at LLMs and trying to create an LLM that will generate survey question answers from a given long aud
io lecture. The approach is simple. 

I get an audio file, convert it into text using whisper, then I take that text and
 send it to my quantized mistral instruct v2 model for text generation from hugging face and ask it to generate question
s based on those texts. 

After extracting the questions from that generation, I split and store the text in FAISS and t
hen I use a RetreivalQA chain to get answers to each of the questions. 

In the below code I am using the questions and 
generating the answers one by one.   
However, I get a warning to use a dataset instead of answering sequentially. How c
an I do that? I need to make this faster. Thanks!

         def make_qna(questions, store): 
            contexts = []
 
   
            qa_chain = RetrievalQA.from_llm(llm=llm, retriever=store.as_retriever())
    
            for ques in qu
estions:
                qa = qa_chain.run(ques)
                contexts.append({
                    'question': ques,
 
                    'answer': qa, 
                })
            return contexts
    
    # Here llm is a HuggingFace
Pipeline object and store is FAISS
```
---

     
 
all -  [ Building a Snowflake Cost Monitoring and Optimiser tool using Langchain, Snowflake Cortex and Open A ](https://www.reddit.com/r/snowflake/comments/1crq80g/building_a_snowflake_cost_monitoring_and/) , 2024-05-16-0910
```
Wanted to share something a colleague and I’ve been recently working on!

Monitoring Snowflake costs, debugging, trying 
to optimise credit usage, etc. were tedious tasks that were soaking up a lot of engineering bandwidth continuously at ou
r workplace.

We decided to build an AI Agent for this using Langchain, Snowflake Cortex and Open AI!

Check out this qu
ick demo where I ask the agent about my Snowflake spending. There are multiple agents working behind the scenes, using O
penAI and Cortex to find the best answers—and the coolest part? The data visualisations are all chosen by the AI based o
n what you need.

Demo link: [https://www.loom.com/share/b14cb082ba6843298501985f122ffb97?sid=b4cf26d8-77f7-4a63-bab9-c8
e6e9f47064](https://www.loom.com/share/b14cb082ba6843298501985f122ffb97?sid=b4cf26d8-77f7-4a63-bab9-c8e6e9f47064)

It ca
n currently

* Monitor costs
* Forecast costs

We’re looking to add abilities like alerting on anomalies and optimising 
queries to it too!

It’s not perfect yet (sometimes it messes up 😅), but we’re working on improving it! If you’ve got th
oughts on this or know other tasks that could be added to this, let me know.
```
---

     
 
all -  [ Building a Snowflake Cost Monitoring and Optimiser tool using Langchain, Snowflake Cortex and Open A ](https://www.reddit.com/r/aiagents/comments/1crq520/building_a_snowflake_cost_monitoring_and/) , 2024-05-16-0910
```
Wanted to share something a colleague and I’ve been recently working on!



Monitoring Snowflake costs, debugging, tryin
g to optimise credit usage, etc. were tedious tasks that were soaking up a lot of engineering bandwidth continuously at 
our workplace.



We decided to build an AI Agent for this using Langchain, Snowflake Cortex and Open AI!



Check out t
his quick demo where I ask the agent about my Snowflake spending. There are multiple agents working behind the scenes, u
sing OpenAI and Cortex to find the best answers—and the coolest part? The data visualisations are all chosen by the AI b
ased on what you need.



Demo link: [https://www.loom.com/share/b14cb082ba6843298501985f122ffb97?sid=b4cf26d8-77f7-4a63
-bab9-c8e6e9f47064](https://www.loom.com/share/b14cb082ba6843298501985f122ffb97?sid=b4cf26d8-77f7-4a63-bab9-c8e6e9f47064
)



It can currently

* Monitor costs
* Forecast costs



We’re looking to add abilities like alerting on anomalies and
 optimising queries to it too!



It’s not perfect yet (sometimes it messes up 😅), but we’re working on improving it! If
 you’ve got thoughts on this or know other tasks that could be added to this, let me know.
```
---

     
 
all -  [ Need help with RAG chatbot ](https://www.reddit.com/r/LangChain/comments/1cro1oc/need_help_with_rag_chatbot/) , 2024-05-16-0910
```
I'm building a RAG chatbot that gives you the contextual information on the documents uploaded into the database connect
ed to the chatbot. Now, I'm trying to implement a feature wherein the user can use a hash(#) to instruct the bot to poin
t to a specific document within a db and ask questions about that specific doc. Please help me on how to implement that 
feature (adding hash to the bot and having bot recognize the hash and automatically reference the document that follows 
hash) in my project. 

For example, if the user types 'What is the order value of #orderdetails', the chatbot has to ref
er to the document 'orderdetails' stored in the db and has to extract the order value and display it to the user.
```
---

     
 
all -  [ AgentExecutor chain finished after the Observation, but before the llm giving Final Answer ](https://www.reddit.com/r/LangChain/comments/1crn71i/agentexecutor_chain_finished_after_the/) , 2024-05-16-0910
```
I have created a custom LLMSingleActionAgent but once the agent completes the observation the AgentExecutor chain finish
ed. This results in errors, because my parser waits for 'Final Answer' for the user.

`def create_agent(`

`llm,`

`hand
lers,`

`max_iterations: int = 1,`

`early_stopping_method: str = 'force',`

`):`

`output_parser = CustomOutputParser()
`

`python_tool = PythonAstREPLTool(callbacks=handlers)`

`tools = [python_tool]`

`tool_names = [tool.name for tool in 
tools]`

`prompt = CustomPromptTemplate(`

`template=template,`

`tools=tools,`

`input_variables=['system_prompt', 'inp
ut', 'intermediate_steps']`

`)`

`llm_chain = LLMChain(llm=llm, prompt=prompt, callbacks=handlers)`

`agent = LLMSingle
ActionAgent(`

`llm_chain=llm_chain,`

`output_parser=output_parser,`

`stop=['\nObservation:'],`

`allowed_tools=tool_n
ames`

`)`

`return AgentExecutor.from_agent_and_tools(`

`agent=agent,`

`tools=tools,`

`verbose=True,`

`max_iteratio
ns=max_iterations,`

`callbacks=handlers,`

`early_stopping_method=early_stopping_method`

`)`
```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-16-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-16-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-16-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-16-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
