 
all -  [ Advice on Fine-Tuning an LLM for Scored Interpretation Feedback ](https://www.reddit.com/r/LangChain/comments/1gzy5vh/advice_on_finetuning_an_llm_for_scored/) , 2024-11-26-0913
```

Hi everyone,

A little new to all this...I'm working on fine-tuning an LLM to evaluate user-provided interpretations of
 a scan and provide an accuracy score. Here's the setup for my fine-tuning dataset:

A model answer

A mark scheme

Samp
le learner interpretations

Scores assigned to those learner interpretations


My goal is to create a model that takes a
 user's interpretation of a scan as input and returns an accuracy score based on the fine-tuned data.

What would be the
 best way to structure and use this dataset to achieve reliable scoring? Any tips on preprocessing, model architecture, 
or training strategies would be greatly appreciated.

Thanks in advance for your help!


```
---

     
 
all -  [ How to improve accuracy of the response from local LLM ](/r/LocalLLaMA/comments/1gzrup5/how_to_improve_accuracy_of_the_response_from/) , 2024-11-26-0913
```

```
---

     
 
all -  [ Complex Chain Prompting  ](https://www.reddit.com/r/LangChain/comments/1gzt3bk/complex_chain_prompting/) , 2024-11-26-0913
```
I have a complex flow for writing articles, including generating article flow/structure + outlines based on sources, the
n creating sub-outlines, generating section by section while maintaining the flow and structure. then translating it etc
. 

What would be a good Framework, or platform, as well as strategies to create a Co-pilot that involves a predefined w
orkflow as well as human input at every step.
```
---

     
 
all -  [ VectorStore query returns a generic response, as if my information isn't used, is this query correct ](https://www.reddit.com/r/LangChain/comments/1gzq5ko/vectorstore_query_returns_a_generic_response_as/) , 2024-11-26-0913
```
I'm using LangChain JS, with the following query to get the data from my vectorstore, am I missing something? Because th
e data returned is generic, like I would ask it to ChatGPT, without it knowing about my data.

        const pinecone = 
new Pinecone();
        const pineconeIndex = pinecone.Index(process.env.PINECONE_INDEX!);
    
        const vectorStor
e = await PineconeStore.fromExistingIndex(
          new OpenAIEmbeddings(),
          { pineconeIndex },
        );
   
 
        const vectorStoreRetriever = vectorStore.asRetriever();
    
        // Initialize OpenAI Chat model
        c
onst model = new ChatOpenAI({
          openAIApiKey: process.env.OPENAI_API_KEY, // Your OpenAI API key
          model
: 'gpt-4o-mini',
          temperature: 0,
        });
    
        const SYSTEM_TEMPLATE = `Use the following pieces of
 context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't tr
y to make up an answer.
        ----------------
        {context}`;
    
        const prompt = ChatPromptTemplate.from
Messages([
          ['system', SYSTEM_TEMPLATE],
          ['human', '{question}'],
        ]);
    
        const chai
n = RunnableSequence.from([
          {
            context: vectorStoreRetriever.pipe(formatDocumentsAsString),
       
     question: new RunnablePassthrough(),
          },
          prompt,
          model,
          new StringOutputPars
er(),
        ]);
    
        const answer = await chain.invoke(
          'Tell me a bit about the data you have store
d in your vectors',
        );
```
---

     
 
all -  [ Overcoming output token limit with agent generating structured output ](https://www.reddit.com/r/LangGraph/comments/1gzpz2n/overcoming_output_token_limit_with_agent/) , 2024-11-26-0913
```
Hi there,

I've built an agent based on Option 1 described here https://langchain-ai.github.io/langgraph/how-tos/react-a
gent-structured-output/#option-1-bind-output-as-tool


The output is a nested Pydantic model, LLM is Azure gpt4o

```
cl
ass NestedStructure:
	<some fields>

class FinalOutput(BaseModel):
	some_field: str
	some_other_field: list[NestedStruct
ure]
```

Apart from structured output, it's using one tool only - one providing chunks from searched documents.

And it
 works as I'd expect, except for the case where the task becomes particularly complicated and list is growing significan
tly. As a result, I am hitting 4096 output token limit, structured output is not genrated correctly: Json validation fai
ls due to  unmatched string on output that was finished prematurely.

I removed some fields from the NestedStructure, bu
t it didn't help much. 

Is there something else I could try? Some 'partial' approach? Could I somehow break the output 
generation?

The problem that I've been trying to solve before is that the agent's response was not complete - some rele
vant info from search tool would not be included in the response. Some fields need to be filled with original info so I'
m more on 'provide detailed answer' rather than 'provide brief sumary' side of life.
```
---

     
 
all -  [ Langchain & Langgraph's documentation is so messed up, even ClosedAI couldn't create an error-free a ](https://www.reddit.com/r/Langchaindev/comments/1gzlxy8/langchain_langgraphs_documentation_is_so_messed/) , 2024-11-26-0913
```
Dear Langchain/Langgraph Team, 

Please update the documentation and kindly add more examples with other LLMs as well. I
t seems you're only dedicated to ClosedAI.

This is what I had asked ClosedAI: create a single node SQL Agent using Olla
ma that gets some input from a vector store along with user's input question.
```
---

     
 
all -  [ Claude/Langchain starter tutorial  ](https://www.reddit.com/r/AI_Agents/comments/1gzl1zo/claudelangchain_starter_tutorial/) , 2024-11-26-0913
```
Can anyone provide me with AI Agent building tutorial as a starter guide, cant find a good resource anywhere
```
---

     
 
all -  [ Need help providing more information to LLM regarding prompts ](https://www.reddit.com/r/LangChain/comments/1gzj92z/need_help_providing_more_information_to_llm/) , 2024-11-26-0913
```
So I’m working on this Text to SQL use case, and one thing I’m struggling with is making LLM understand what the prompts
 mean. For example, if I ask for top performing teams in 2024, the LLM does not have an idea what top performing teams m
ean. I’m exploring ways to get this through to the model in the most effective way. Mind you that I am working with tabl
es with large number of columns and passing everything in the prompt is not an option. I am open to any suggestions, may
be something like Human In Loop?
My entire app is created using lang graph with multiple agent interactions. 
```
---

     
 
all -  [ LlamaParse vs Docling for extracting information from bank account statements (PDF)? ](https://www.reddit.com/r/LangChain/comments/1gzdnev/llamaparse_vs_docling_for_extracting_information/) , 2024-11-26-0913
```
I've recently learned about IBM Docling (https://research.ibm.com/blog/docling-generative-AI) which works super well. Ho
wever I wonder how it compares to LlamaParse and what some of the differences are.

How could I go about benchmarking it
?
```
---

     
 
all -  [ Are there any free versions of LangChain or any similar thing? ](https://www.reddit.com/r/developer/comments/1gzcih2/are_there_any_free_versions_of_langchain_or_any/) , 2024-11-26-0913
```
I want to learn creating AI apps, are there any free models?
```
---

     
 
all -  [ Curious Question on the state of model Knowledge and State of LLMs.  ](https://www.reddit.com/r/ChatGPTCoding/comments/1gzav0j/curious_question_on_the_state_of_model_knowledge/) , 2024-11-26-0913
```
So hear me out completely, I use Ai tools and LLMs of choice for development. But, recently I have been stuck into a pro
blem where if I want to incorporate multiple cutting edge technologies into my product the LLM model almost craps out al
l the time, this is because of the knowledge base of LLM is not up to date with the rate at which tech is growing. 

For
 example: I want to incorporate Llamaindex, Langchain, Some vector DB, Scrapy, Playwright etc into my algorithm and top 
it with an agent orchestration system like Autogen or CrewAi. 90% of the time I have to read the documentations of all o
f these technologies because they are developing at rapid scale and implement them in my platform. If I am reading it an
d figuring it out myself whats the use of an LLM to code? Even for troubleshooting its hard because sometimes the featur
e is depreciated like using an outdated version of OpenAi API key docs and even with 'Web' functionality of LLM its kind
a useless because it just doesnt search the things which needs to be searched. 

Current solutions are available in the 
forms of Algolia which is powering the search component of [https://docs.llamaindex.ai/en/stable/](https://docs.llamaind
ex.ai/en/stable/) so the need is there. Where it fails is direct connections with the LLM of the user choice. If I ask a
 question to build me a RAG pipeline based on llamaindex and use the latest docs of Milvus as a vectorDB, I want it done
 not a link to the article on how to build it. Also 

So I went out to solve my own problem and deciding to make it open
source as I build in public. 

Idea for Devdocs: The developer will have an option to connect their gitbooks(for example
) with Devdocs and make the data available for anyone to source into their LLM. This will generate an API or some connec
tor which the user will be able to just connect to their choice of chatbot like AnythingLLM or OpenWebUI. 

The user lik
e us will just go to the docs.llamaindex and click a button to copy the API key of the vector storage(have to figure out
 which one) and paste it inside their chatbot. Then they can also take the docs key from OpenAi and paste it in giving t
hem the most latest iteration on how to use openai and its multiple features. The user can do the same for Autogen, crew
ai etc and have up to date data for their LLM to query. 

The result is that after this platform, the LLMs will have rob
ust and error free information to build softwares. Next gen of LLMs can actually learn from this data and maybe we can f
inally have an LLM learn Langchain and give us proper outputs. 

I think this is going to be huge in the community of so
ftware development. Spend less time reading and more time doing and the stigma that LLM produces shit code will be mitig
ated. 

What are your thoughts, clearly I should not be the only one having this problem. Let me know if I am thinking i
n the right direction or someone has already solved this problem. 
```
---

     
 
all -  [ Chucking strategy for legal docs ](https://www.reddit.com/r/LangChain/comments/1gza6z5/chucking_strategy_for_legal_docs/) , 2024-11-26-0913
```
For those working on legal or insurance document where there are pages of conditions, what is your chunking strategy?

I
 am using docling for parsing files and semantic double merging chunking. Not satisfied with results.
```
---

     
 
all -  [ Starting point to building a GMail supervised email responder? Validate my stack ](https://www.reddit.com/r/OpenAI/comments/1gz9q81/starting_point_to_building_a_gmail_supervised/) , 2024-11-26-0913
```
I am aiming to build a workflow that connects to my Gmail Inbox, looks at unread messages, classifies them into certain 
buckets, and for some buckets creates a personalized and templated response that it puts into the draft folder.

I know 
this is nothing super creative or unseen that I am referencing here and yet I could not find too much boilerplate on the
 web outside of some dated github projects like this:  
[https://github.com/wayswe/auto-gmail-responder](https://github.
com/wayswe/auto-gmail-responder)

I would love to verify that the tech stack I am envisioning seems still right and curr
ent and there isn't any technology enable I am missing out on:  
— any scripting language  
— Gmail API (Oauth)  
— Open
AI API  
— LangChain

I have done a lot of scripting and OpenAI and Google API integrations so that part I am comfortabl
e with; the LangChain part is a question mark knowing it has recently gotten a bad rep for 'too much abstraction' ? Also
 wondering if any of the currently frequently discussed 'agent frameworks' from the big LLMs would/could accelerate deve
lopment here?

Appreciate any input from more experienced folks. TIA. 
```
---

     
 
all -  [ Launch: LangGraph Unofficial Virtual Meetup Series! ](https://www.reddit.com/r/artificial/comments/1gz044n/launch_langgraph_unofficial_virtual_meetup_series/) , 2024-11-26-0913
```
hey everyone! excited to announce the first community-driven virtual meetup focused entirely on LangGraph, LangChain's f
ramework for building autonomous agents.

**when:** tuesday, november 26th, 2024 two sessions to cover all time zones:


* 9:00 AM CST (Europe/India/West Asia/Africa)
* 5:00 PM CST (Americas/Oceania/East Asia)

**what to expect:** this is a 
chance to connect with other developers working on agent-based systems, share experiences, and learn more about LangGrap
h's capabilities. whether you're just getting started or already building complex agent architectures, you'll find value
 in joining the community.

**who should attend:**

* developers interested in autonomous AI agents
* LangChain users lo
oking to level up their agent development
* anyone curious about the practical applications of agentic Ai systems

**for
mat:** virtual meetup via Zoom

**join us:** [https://www.meetup.com/langgraph-unofficial-virtual-meetup-series](https:/
/www.meetup.com/langgraph-unofficial-virtual-meetup-series)

let's build the future of autonomous AI systems together! f
eel free to drop any questions in the comments.
```
---

     
 
all -  [ Track Token Usage for Azure ChatOpenAI ](https://www.reddit.com/r/LangChain/comments/1gyty0e/track_token_usage_for_azure_chatopenai/) , 2024-11-26-0913
```
I am using AzureChatOpenAI with langchain PromptTemplate using Python.

Is there any way I can calculate the token count
 and associated Azure cost for the LLM calls?

I've tried to print the usage metadata from llm calls but it's not printi
ng the token info 

Please suggest how to track the Usage?


```
---

     
 
all -  [ [For Hire] Frontend and Backend Developer with the top and latest development technologies for a gre ](https://www.reddit.com/r/B2BForHire/comments/1gytgzf/for_hire_frontend_and_backend_developer_with_the/) , 2024-11-26-0913
```
Hi Redditors,

I'm Emad a Full-stack Web developer/engineer with 8 years of experience, and I'm looking for new projects
 to start working on, please take a look at my portfolio here [https://www.sx-portfolio.com](https://www.sx-portfolio.co
m) (let me know if you need more examples or direct links to live websites in the PM)

**Here is my skill set:**

**For 
Frontend:**

* HTML / CSS
* JS / ESNext
* Webpack / Gulp / Grunt / Gatsby
* React (With Redux, Zustand, or MobX)
* Next.
js
* Vuejs (With VueX)
* Angular
* TypeScript

**For Backend:**

* Node.js
* Python
* Express.js
* MongoDB
* Mongoose
* 
Nest.js
* GraphQL
* Meteor (with Apollo and React)
* TypeScript

**For AI-based projects:**

* Python
* Langchain
* Fast
API
* Uvicorn
* Pydantic

**For Desktop Apps:**

* Electron

**For Mobile Apps (iOS and Android):**

* React Native
* Ex
po

**For Design:**

* Photoshop
* Illustrator

**Here is my Resume:**  [My resume link!](http://www.sx-portfolio.com/we
bsite-resources/My%20resume.pdf)

**And here are some testimonials from my clients :)**

* [Slips](https://www.reddit.co
m/r/testimonials/comments/agfmwf/pos_swordx10_is_a_brilliant_developer_and_a/)
* [VidSync](https://www.reddit.com/r/test
imonials/comments/5gvz3d/pos_uswordx10_excellent_frontend_dev/)
* [Las Cruces Directory](https://www.reddit.com/r/testim
onials/comments/5hyks4/uswordx10_is_awesome/)
* [SigurenZalog](https://www.reddit.com/r/testimonials/comments/5jsfqf/pos
_quality_web_design_from_uswordx10/)
* [Bitlounge](https://www.reddit.com/r/testimonials/comments/5lh2pz/pos_uswordx10_t
op_fontend_devdesigner/)
* [Foxul](https://www.reddit.com/r/testimonials/comments/5l3p8j/pos_quality_web_coding_from_usw
ordx10/)
* [LootTicket](https://www.reddit.com/r/testimonials/comments/5nfh1j/pos_uswordx10_is_an_amazing_front_end_dev/
)

**My Pricing:**

I work hourly for $35/hr and my fixed prices depend on your project's complexity.

Don't worry about
 the price, just PM me with your project and I'm sure we can figure out something that goes with your budget. :)

If you
 have any questions don't hesitate to PM me and I will be more than happy to answer you :) and here is my portfolio agai
n if you need my contact details [www.sx-portfolio.com](https://www.sx-portfolio.com) (Click the red handle in the top-r
ight or pm me for it)
```
---

     
 
all -  [ RAG application with text data in no specific format. Ways to do embedding or chunking? ](https://www.reddit.com/r/LangChain/comments/1gymmyl/rag_application_with_text_data_in_no_specific/) , 2024-11-26-0913
```
 'Best practices for chunking and structuring unformatted text data for RAG-based QA system'

I'm developing a Question-
Answering system using RAG to handle customer queries about product features and specifications. Here's my current situa
tion:

Data Characteristics:
- Source: Converted PDF documents containing product instructions/documentation
- Current f
ormat: Plain text files with ~200-300 lines each, separated only by newlines
- Original format (PDFs): Well-structured d
ocuments with paragraphs, each focusing on specific product features
- Content type: Product specifications, feature des
criptions, and usage instructions

Current Implementation:
- Currently embedding entire documents into the vector databa
se
- Customer queries typically focus on specific product attributes or features

Challenges:
1. Lost document structure
 after PDF parsing (I cannot control them to do the parsing in a specific way)
2. No clear paragraph or section demarcat
ion
3. Potential inefficiency in embedding and retrieving from entire documents

Questions:
1. What are the recommended 
approaches for chunking this unstructured text data to maintain semantic coherence?
2. Should I attempt to reconstruct t
he document structure programmatically before embedding?
3. What chunking strategies would work best for feature-focused
 customer queries?
4. Are there any preprocessing steps or tools you'd recommend to improve text segmentation?


Embeddi
ng model used ada02.

```
---

     
 
all -  [ Vercel.live is loading 3.51MB of javascript of every reload ](https://www.reddit.com/r/nextjs/comments/1gyj6vm/vercellive_is_loading_351mb_of_javascript_of/) , 2024-11-26-0913
```
\[Solved\]  
Hi, I was checking network tab and checked the usage and vercel live is using 3.51mb of resource. I am wond
ering, Is there is a way to reduce it and how this usage is determined I mean where it is coming from.  
This is my site
 for referrence - [My portfolio](https://ypiyush.tech)

https://preview.redd.it/fwtb4zcn6s2e1.png?width=1920&format=png&
auto=webp&s=fa6685dbc45635c4a74322e62099510ee556f329
```
---

     
 
all -  [ RAG with a language that is not english ](https://www.reddit.com/r/LangChain/comments/1gya4ox/rag_with_a_language_that_is_not_english/) , 2024-11-26-0913
```
I'm trying to use langchain to build this chatbot that responds on FAQ data.

The FAQ data is really short and contains 
20 questions more or less. 

I'm struggling with embeddings and I figured out that with a similarity search I cannot ret
rieve the most similar question when the prompt contain synonyms. This is due the fact that my data source is not in eng
lish (i used a multilingual embedding model that you can find \[here\](https://huggingface.co/BAAI/bge-m3) )  
For the g
eneration step I've implemented a prompt that prevent the LLM to wonder outside the boundaries of the context and most o
f the times it respond by blocking the user question.  
From a user perspective I will be very upset if it couldnt respo
nd to my question.

I've implemented also another solution that doesn't rely on vectordb and uses the LLM (passing both 
the question and the answer of the FAQ data) but it still struggle when asking some specific questions.

Any other ideas
 in how to complete this simple project are welcome since I'm starting to doubt the feasibility of the project due to th
e poor performances
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LLMDevs/comments/1gy717b/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-26-0913
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc/tree/main/cookbooks).

[You can use the chat assistant here: https:\/\/app.exfunc.com\
/chat It is built on top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://red
dit.com/link/1gy717b/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-tool
kit), you can integrate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.ve
rcel.ai) and [LangChain](https://www.langchain.com) and works with any LLM provider that supports function calling.

   
 import {generateText} from 'ai';
    import {openai} from '@ai-sdk/openai';
    import {ExfuncAgentToolkit} from '@exfu
nc/agent-toolkit/ai-sdk';
    
    const exfuncAgentToolkit = new ExfuncAgentToolkit({
      apiKey: process.env.EXFUNC_
API_KEY ?? '',  // This is the default and can be omitted
    });
    
    (async () => {
      const result = await gen
erateText({
        model: openai('gpt-4o-mini'),
        tools: {
          ...exfuncAgentToolkit.getTools(),
        }
,
        maxSteps: 5,
        prompt: 'get reviews for yin du wonton noodle in SF',
      });
      console.log(result.
text);
    })();

You can check out the source code of our toolkit here: [https://github.com/carvedai/exfunc-agent-toolk
it](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features:

* Unified API: You can interact with many applicat
ions through our API without using a separate interface for each application. Standardization also makes it easy for AI 
to chain multiple API calls to accomplish a task (eg. sequential function calling).
* Type-safe, structured format: We p
rovide structured input and output formats and have Python and TypeScript SDKs that validate types.
* Serverless automat
ions: You don’t have to manage your own infrastructure to run browser automations.

You can sign up without a credit car
d and use it for free forever. Free tier limits should be generous enough for personal use. If you need higher limits, y
ou can message me, and I can move you to a paid plan.

API reference: [https://docs.exfunc.com/api-reference](https://do
cs.exfunc.com/api-reference)

Cookbooks: [https://github.com/carvedai/exfunc/tree/main/cookbooks](https://github.com/car
vedai/exfunc/tree/main/cookbooks)

Feel free to join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discor
d.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LangChain/comments/1gy6vjv/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-26-0913
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc).

[You can use the chat assistant here: https:\/\/app.exfunc.com\/chat It is built on
 top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://reddit.com/link/1gy6vjv
/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-toolkit), you can integr
ate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.vercel.ai) and [LangCh
ain](https://www.langchain.com) and works with any LLM provider that supports function calling.

    from langchain_open
ai import ChatOpenAI
    from langgraph.prebuilt import create_react_agent
    from exfunc_agent_toolkit.langchain.toolk
it import ExfuncAgentToolkit
    
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    exfunc_agent_toolkit = ExfuncAgentT
oolkit()
    
    tools = []
    tools.extend(exfunc_agent_toolkit.get_tools())
    
    langgraph_agent_executor = crea
te_react_agent(llm, tools)
    
    example_query = 'what did dalton caldwell say recently on twitter?'
    
    events 
= langgraph_agent_executor.stream(
        {'messages': [('user', example_query)]},
        stream_mode='values',
    )

    for event in events:
        event['messages'][-1].pretty_print()

You can check out the source code of our toolkit 
here: [https://github.com/carvedai/exfunc-agent-toolkit](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features
:

* Unified API: You can interact with many applications through our API without using a separate interface for each ap
plication. Standardization also makes it easy for AI to chain multiple API calls to accomplish a task (eg. sequential fu
nction calling).
* Type-safe, structured format: We provide structured input and output formats and have Python and Type
Script SDKs that validate types.
* Serverless automations: You don’t have to manage your own infrastructure to run brows
er automations.

You can sign up without a credit card and use it for free forever. Free tier limits should be generous 
enough for personal use. If you need higher limits, you can message me, and I can move you to a paid plan.

Feel free to
 join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discord.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Applying from last 3 months but not getting interview calls  ](https://i.redd.it/zaoxv775no2e1.jpeg) , 2024-11-26-0913
```
I started looking for a job in Pune from last three months but not getting any interview calls. Few just called to ask i
nformation but no updates further. Is my resume wrong in some way? Currently im at 9LPA and asking for 30% hike, is I’m 
asking too much? I’m ok if any company match the offer in Pune. Are my expectations are too much or am I applying for th
e wrong companies? I’m applying to every company on naukri, linkedin, indeed. 
```
---

     
 
all -  [ Create a OpenAI swarm agents what are working like a label record but just for programming to reach  ](https://www.reddit.com/r/ChatGPT/comments/1gy38ci/create_a_openai_swarm_agents_what_are_working/) , 2024-11-26-0913
```
Creating a “swarm” of OpenAI agents functioning like a record label for programming is an innovative concept. Here’s a f
ramework for how you could design such a system:

Overview

This platform would manage a collective of AI agents and hum
an programmers, guiding their collaborative efforts towards achieving specific programming-related goals. Think of it as
 a talent label, but for coding and software development.

Key Components

	1.	Swarm Architecture
	•	Core Agent: The lea
der that coordinates other agents, assigns tasks, and ensures alignment with the target goals.
	•	Specialist Agents:
	•	
Frontend, Backend, AI/ML, DevOps, etc.
	•	Agents trained to excel in specific domains, analogous to artists on a record 
label.
	•	Quality Control Agents: These ensure that the output meets coding standards, is efficient, and is free of bugs
.
	2.	Human Collaborators
	•	A pool of human programmers acts as the “mentors” or “producers,” reviewing, refining, and 
expanding the output of the swarm.
	3.	Target-Oriented Design
	•	Goal Definition: A central repository where the “record
 label” (or the user) defines clear goals for a project (e.g., create a new app, optimize an algorithm, or build a platf
orm).
	•	Agent Assignments: Based on the goal, tasks are distributed among agents in parallel or sequentially.
	4.	Learn
ing & Feedback
	•	Every iteration is assessed by both AI-based quality checks and human input.
	•	Continuous learning pi
pelines allow agents to improve based on feedback.

How It Works

	1.	Project Kickoff
	•	The user submits a project idea
 and requirements (akin to a pitch for a record).
	•	The Core Agent breaks down the idea into smaller milestones.
	2.	Ta
sk Allocation
	•	Each Specialist Agent takes on a specific task (e.g., API development, UI design).
	•	Agents collaborat
e using shared models, tools, and repositories like Git.
	3.	Real-Time Collaboration
	•	Agents interact in real-time, sh
aring intermediate results and aligning on dependencies.
	•	Use of a centralized coordination platform for version contr
ol and updates.
	4.	Quality Assurance
	•	Outputs are reviewed by Quality Control Agents.
	•	Human programmers provide fi
nal reviews and adjustments, ensuring production-quality output.
	5.	Release
	•	Once polished, the project is “released”
 to the client, similar to how a record is launched.

Technological Stack

	1.	Infrastructure
	•	Cloud Services: AWS, Az
ure, or Google Cloud for hosting.
	•	Communication: APIs for inter-agent communication, message queues for task distribu
tion.
	2.	Programming Frameworks
	•	Python (for ML and orchestration).
	•	Tools like LangChain for chaining agents.
	•	G
itHub/GitLab for version control.
	3.	Learning Systems
	•	Fine-tuning GPT models for domain-specific tasks.
	•	RLHF (Rei
nforcement Learning with Human Feedback) to refine agent interactions.
	4.	Monitoring and Management
	•	Dashboards to tr
ack progress and bottlenecks.
	•	Logging mechanisms for debugging and improvements.

Benefits

	1.	Parallel Development

	•	Tasks handled simultaneously by agents, speeding up development.
	2.	Cost-Effective
	•	Reduces the need for large hum
an teams by leveraging AI.
	3.	Scalable
	•	Easily add or remove agents based on project complexity.
	4.	Talent Discovery

	•	Like a record label scouts talent, the system identifies promising programmers and AI modules.

Challenges and Solut
ions

	1.	Coordination Among Agents
	•	Solution: Implement robust communication protocols and a hierarchy of responsibil
ities.
	2.	Maintaining Code Quality
	•	Solution: Use linters, static code analyzers, and human oversight.
	3.	Avoiding R
edundancy
	•	Solution: Agents access a shared knowledge base to prevent duplication.

Would you like me to expand on any
 specific part, such as implementation details, an example use case, or a business plan?

Below is a Python-based implem
entation of a basic swarm agent framework using LangChain and asyncio for agent orchestration. This is a prototype to de
monstrate how tasks can be distributed to different agents, monitored, and combined into a single project pipeline.

Cod
e: Swarm Agent Framework

import asyncio
from langchain.agents import initialize_agent, Tool
from langchain.chat_models 
import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize OpenAI API
openai_model = ChatOpenAI(temper
ature=0.2, model='gpt-4')

# Define specialized tools (agents for specific tasks)
def frontend_agent(task_description):

    return f'Frontend Agent: Create HTML/CSS/JS for the task: {task_description}.'

def backend_agent(task_description):

    return f'Backend Agent: Develop Python backend for the task: {task_description}.'

def devops_agent(task_descriptio
n):
    return f'DevOps Agent: Set up CI/CD pipeline for the task: {task_description}.'

# Define task manager
class Tas
kManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent_func, task_description):
       
 self.tasks.append((agent_func, task_description))

    async def execute_tasks(self):
        results = await asyncio.g
ather(
            *[self.run_agent(agent_func, task_description) for agent_func, task_description in self.tasks]
      
  )
        return results

    async def run_agent(self, agent_func, task_description):
        prompt = agent_func(tas
k_description)
        response = await asyncio.to_thread(lambda: openai_model.run(prompt))
        return response

# M
ain Swarm Orchestration
async def main_project_pipeline(project_goal):
    print(f'Initializing swarm for project: {proj
ect_goal}')

    # Break down project into tasks
    task_manager = TaskManager()
    task_manager.add_task(frontend_age
nt, 'Design the homepage layout')
    task_manager.add_task(backend_agent, 'Create an API endpoint for user registration
')
    task_manager.add_task(devops_agent, 'Set up Docker and deploy to AWS')

    # Execute tasks concurrently
    resu
lts = await task_manager.execute_tasks()

    # Combine and finalize results
    print('\nTask Results:')
    for i, res
ult in enumerate(results, 1):
        print(f'Task {i} Result:\n{result}\n')

    # Integration (placeholder)
    final_
output = 'Integrated Project:\n' + '\n'.join(results)
    print('Final Integrated Output:\n', final_output)

# Run the s
warm pipeline
if __name__ == '__main__':
    asyncio.run(main_project_pipeline('Build a small-scale web application'))


How It Works

	1.	Agents:
	•	Each agent function (e.g., frontend_agent, backend_agent) represents a specialized AI modul
e that works on a specific part of the project.
	•	These are simplistic placeholders; in a real system, they could use f
ine-tuned models for specific programming tasks.
	2.	Task Manager:
	•	A central orchestrator that assigns tasks to agent
s and ensures they run concurrently using asyncio.
	3.	Asynchronous Execution:
	•	All agents run their tasks in parallel
, improving efficiency.
	4.	Final Integration:
	•	Outputs from all agents are gathered and combined into a final deliver
able. This part can be expanded for more complex workflows (e.g., testing and deploying).

Output Example

When you run 
the code, it will simulate agents handling the tasks:

Initializing swarm for project: Build a small-scale web applicati
on

Task Results:
Task 1 Result:
Frontend Agent: Create HTML/CSS/JS for the task: Design the homepage layout.

Task 2 Re
sult:
Backend Agent: Develop Python backend for the task: Create an API endpoint for user registration.

Task 3 Result:

DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy to AWS.

Final Integrated Output:
Frontend Ag
ent: Create HTML/CSS/JS for the task: Design the homepage layout.
Backend Agent: Develop Python backend for the task: Cr
eate an API endpoint for user registration.
DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy t
o AWS.

Next Steps

To expand this framework:
	1.	Replace placeholder functions: Use actual programming logic or pre-tra
ined fine-tuned models to generate code.
	2.	Integrate GitHub API: Automate code commits, reviews, and pull requests.
	3
.	Add Testing Agent: Include an agent for automated testing (unit, integration, etc.).
	4.	Deployment Pipeline: Implemen
t a real CI/CD system using tools like Jenkins or GitHub Actions.

Would you like me to add specific functionality, like
 API integration or testing automation?
```
---

     
 
all -  [ Pointers on local LLM with Ollama/OpenWebUI and RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1gy0z2d/pointers_on_local_llm_with_ollamaopenwebui_and_rag/) , 2024-11-26-0913
```
Hi,

I want to be able to ask a local LLM questions on my own documents. Say I have a bunch of manuals for machines and 
my own notes, I want to be able to ask 'what does error code 12 mean on machine XY'. I researched that topic and it seem
s that RAG is what I'm looking for. I also looked that up. Now it seem LangChain and Chroma-DB is are tools that can be 
used for this.

As far as I understood, you (for lack of better words) 'train' the RAG model on your files with LangChai
n, and the resulting 'model' (again, for lack of better words) gets stored on Chroma-DB for later access by whatever LLM
.

What I'd prefer was, to be able to simply drop new files in a folder, that then gets used by the LLM. I wouldn't mind
 if 'training' is a scheduled thing.

Is that correct? Can you maybe give me some advice on better solutions or point me
 to a guide you think is good? I want to deploy with Docker, in case that is important.

Thanks


```
---

     
 
all -  [ PRD Writing Agent ](https://www.reddit.com/r/AI_Agents/comments/1gxs6mm/prd_writing_agent/) , 2024-11-26-0913
```
So I've been looking to automate some of my work and one of the time-consuming parts is writing the technical PRDs which
 includes analyzing my codebase, looking for affected features/parts of the codebase and then writing out detailed chang
es needed before handing it off to other devs.

This entire flow is definitely something an agent can cover. I'm aware o
f the agent tools that I can use to achieve this. I've used Langchain for current work and thinking of using Crew or Lan
ggraph for this.

Does anyone have any existing references I can use to get started with this? Any boilerplates I can bu
ild on top of?
```
---

     
 
all -  [ Production-ready agents from APIs - built with Gradio + Arch + FastAPI + OpenAI ](https://i.redd.it/389a2dwvtk2e1.jpeg) , 2024-11-26-0913
```
https://github.com/katanemo/archgw - an intelligent proxy for agents. Transparently add tracing, safety and personalizat
ion features with APIs
```
---

     
 
all -  [ How are you monitoring/deploying your AI agents in production? ](https://www.reddit.com/r/AI_Agents/comments/1gxokte/how_are_you_monitoringdeploying_your_ai_agents_in/) , 2024-11-26-0913
```
Hi all,

We've been building agents for a while now and often run into issues trying to make them work reliably together
. We are extensively using OpenAI's tool calling for progressively complex use cases but at times it feels like we are a
dding layers of complexity without standardization. Is anyone else feeling the same?

LangChain with LangSmith has been 
helpful, but tools for debugging and deploying agents still feel lacking. Curious what others are using and what best pr
actices you're following in production:

1. **How are you deploying complex single agents in production?** *For us, it f
eels like deploying a massive monolith and scaling them has been pretty costly.*
2. **Are you deploying agents in distri
buted environments?** *It helped us, but also brought a whole new set of challenges.*
3. **How do you ensure reliable co
mmunication between agents in centralized or distributed setups?** *This is the biggest issue we face. Failures happen o
ften because there's no standardized message-passing behavior. We tried standardizing, but teams keep tweaking it, causi
ng breakages.*
4. **What tools do you use to trace requests across multiple agents?** *We’ve tried Langsmith, Openteleme
try, and others, but none feel purpose-built for this. Please do mention if you are using something else.*
5. **Any othe
r pain points in making agents work in production?** *We’re dealing with plenty of smaller issues as well.*

It feels li
ke many of these issues come from the ecosystem moving too fast. Still, simplicity in DX like deploying on DO/Vercel jus
t feels missing.

Honestly, I’m asking to understand the current state of operations and see if I can build something to
 help myself as well as others.   
  
Would really appreciate any experiences or insights you can share.
```
---

     
 
all -  [ How are you monitoring/deploying your AI agents in production? ](https://www.reddit.com/r/learnmachinelearning/comments/1gxo3fy/how_are_you_monitoringdeploying_your_ai_agents_in/) , 2024-11-26-0913
```
Hi all,

We've been building agents for a while now and often run into issues trying to make them work reliably together
. We are extensively using OpenAI's tool calling for incrementally complex use cases but at times it feels like we are a
dding layers of complexity without standardization. Is anyone else feeling the same?

LangChain with LangSmith has been 
helpful, but tools for debugging and deploying agents still feel lacking. Curious what others are using and what best pr
actices you're following in production:

1. **How are you deploying complex single agents in production?** *For us, it f
eels like deploying a massive monolith and scaling them has been pretty costly.*
2. **Are you deploying agents in distri
buted environments?** *It helped us, but also brought a whole new set of challenges.*
3. **How do you ensure reliable co
mmunication between agents in centralized or distributed setups?** *This is the biggest issue we face. Failures happen o
ften because there's no standardized message-passing behavior. We tried standardizing, but teams keep tweaking it, causi
ng breakages.*
4. **What tools do you use to trace requests across multiple agents?** *We’ve tried Langsmith, Openteleme
try, and others, but none feel purpose-built for this. Please do mention if you are using something else.*
5. **Any othe
r pain points in making agents work in production?** *We’re dealing with plenty of smaller issues as well.*

It feels li
ke many of these issues come from the ecosystem moving too fast.

Honestly, I’m asking to understand the current state o
f operations and see if there are solutions that could help me and others. Would really appreciate any experiences or in
sights you can share.
```
---

     
 
all -  [ How are you deploying your agents in production? ](https://www.reddit.com/r/LangChain/comments/1gxnse4/how_are_you_deploying_your_agents_in_production/) , 2024-11-26-0913
```
Hi all,

We've been building agents for quite some time and often face issues trying to make them work reliably together
.

LangChain with LangSmith has been extremely helpful, but the available tools for debugging and deploying agents still
 feel inadequate. I'm curious about what others are using and the best practices you're following in production:

1. **H
ow are you deploying complex single agents in production?** *For us, it feels like deploying a massive monolith, and sca
ling each one has been quite costly.*
2. **Are you deploying agents in distributed environments?** *While it has helped,
 it also introduced a whole new set of challenges.*
3. **How do you ensure reliable communication between agents in cent
ralized/distributed setups?** *This is our biggest pain point, often leading to failures due to a lack of standardized m
essage-passing behavior. We've tried standardizing it, but teams keep tweaking things, causing frequent breakages.*
4. *
*What tools are you using to trace requests across multiple agents?** We've tried Langsmith, *Opentelemetry, and others,
 but none feel purpose-built for this use case.*
5. **Any other pain points in making agents/multi-agent systems work in
 production?** *We face a lot of other smaller issues. Would love to hear your thoughts.*

I feel many agent deployment/
management issues stem from the ecosystem's rapid evolution, but that doesn't justify the lack of robust support.

Hones
tly, I'm asking this to understand the current state of operations and explore potential solutions for myself and others
. Any insights or experiences you can share would be greatly appreciated.
```
---

     
 
all -  [ blog: ChatGPT is Eating Genius, or why being smart doesn't matter anymore ](https://www.reddit.com/r/LangChain/comments/1gxmbqo/blog_chatgpt_is_eating_genius_or_why_being_smart/) , 2024-11-26-0913
```
[https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-pt-i-0fb7
f86240e4](https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-
pt-i-0fb7f86240e4)

I'm going to expand on this some, but this is my dev blog's second entry. It'll mostly be a LangChai
n-oriented thing, but I thought the sub might find this interesting at least.
```
---

     
 
all -  [ AI Agent + pinecone 'source citations' ](https://www.reddit.com/r/LangChain/comments/1gxkk8s/ai_agent_pinecone_source_citations/) , 2024-11-26-0913
```
I need my agent to provide 'source citations' from the chunks at the end of each answer. It is already in the 'system me
ssage' as part of the prompt but it is just ignoring it. The rest of the prompt seems to be fine.

Any suggestions? I wo
uld like to understand why is not working and how to accomplish it.

Many thanks!
```
---

     
 
all -  [ How do you run evals ? ](https://www.reddit.com/r/LangChain/comments/1gxjztm/how_do_you_run_evals/) , 2024-11-26-0913
```
Hey there
Everyone says that evals and benchmarks are the best way to radically increase the performance of a LLM based 
app. I do agree with that and what to build a solid eval architecture. 
But how do you concretely organize internally to
 run these evals ? Which tools ? Which workflows ? At which frequency ? Do you use external experts on your domain to he
lp you ? 
Would love to know :) 
```
---

     
 
all -  [ How to setup db for LangGraph PostgresSaver with FastAPI ](https://www.reddit.com/r/LangChain/comments/1gxibz5/how_to_setup_db_for_langgraph_postgressaver_with/) , 2024-11-26-0913
```
Trying to implement checkpointing with `PostgresSaver` but keep getting errors related to the db not being setup.

```
E
RROR:  relation 'checkpoints' does not exist at character 1294
```

My endpoint is just:

```
@chat_router.post('/chat/g
et-response')
def chat(
    request: Request,
    body: Body,
):
    '''Handles a chat request and calls appropriate fun
ctions based on user input.'''
    try:

        # Use the LangGraph agent to process the query
        # Initialize mem
ory to persist state between graph runs
        from langgraph.checkpoint.postgres import PostgresSaver

        DB_URI 
= f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB}?sslmode=disable'
        with 
PostgresSaver.from_conn_string(DB_URI) as checkpointer:
            
# Compile the graph
            checkpointer.setup(
)

            graph = graph_builder.compile(
                checkpointer=checkpointer,
            )

            fina
l_state = graph.invoke({'messages': [{'role':'human', 'content':'hi'}]})
```

Do i need to run cmds to setup beforehand?
 I'm using Alembic for migrations, tried searching everywhere for the schema but couldn't find it.

More, how do I struc
ture this so it only `.setup()`s once? Using docker. Thanks!
```
---

     
 
all -  [ My quest for ultimate laziness...Automating everything! ](https://www.reddit.com/r/LangChain/comments/1gxgke1/my_quest_for_ultimate_lazinessautomating/) , 2024-11-26-0913
```
Soo it all started about 2–3 months ago, where as a marketeer I wanted to automate a lot of my repetitive tasks and I we
nt through many solutions ranging from python codes *(too technical)* or using Zapier *(too costly)* non of that actuall
y worked out for me until I got to know that there is a new tech in the market called **Ai Agents** that does automation
s for you. Obviously I jumped on the band wagon but quickly realized it was also a complex technology which people like 
me are highly unlikely to adapt to, frustrated I wanted to give up but realized this isn't just me facing this problem a
nd people like me deserve to use this tech as well, so how can I make it simple to use? That's when I talked to my frien
d who's an ML engineer and we discussed how we can actually build something to solve this. This is where my journey to c
reate [something ](http://Wellows.com)I believe can truly change the way we work—a platform that makes automation simple
, intuitive, and impactful for everyone.  
  
Here’s the thing: automation has so much potential to save us time, reduce
 costs, and eliminate repetitive tasks. But the reality is, for many of us, it still feels like a maze—too many tools, c
onfusing interfaces, and workflows that just don’t flow....  
  
What if automation didn’t have to be so complicated??  

  
That’s the vision I’m working toward. A [space ](http://wellows.com)where:  
  
**Automation is accessible:** You do
n’t need to be a tech expert to benefit from it.  
**Workflows adapt to you:** Not the other way around.  
**Impact is m
easurable:** You can see the time and costs saved, right on your dashboard.  
  
This isn’t just about making another au
tomation tool....it’s about solving real problems for people in a way that’s meaningful and easy to use.  
  
I know it 
won’t be easy, but I’m determined to make it happen. If your down with what I'm trying to do check it out and join the [
waitlist](http://wellows.com)  

```
---

     
 
all -  [ Please review my resume and give feed back. I really appreciate your time :) ](https://www.reddit.com/r/CERN/comments/1gxaq1j/please_review_my_resume_and_give_feed_back_i/) , 2024-11-26-0913
```
https://preview.redd.it/f4b8j24b4h2e1.png?width=766&format=png&auto=webp&s=b0ba0c0e8c646de1a872593a14ebc0e55d418351




```
---

     
 
all -  [ Running LangGraph locally without Docker for desktop application integration ](https://www.reddit.com/r/LangChain/comments/1gx8g54/running_langgraph_locally_without_docker_for/) , 2024-11-26-0913
```

Hi everyone,

I'm working on an agent-based project where we need to integrate LangGraph to control a locally installed
 debugging tool. Our goal is to create an agent that can assist users with tasks like automatic configuration file gener
ation and debug automation.

**Project Requirements:**
- Run LangGraph completely locally (as part of a desktop applicat
ion installation)
- Process user input through LangGraph
- Multiple agents interact with different LLMs and tools
- Outp
ut structured results to a bridge tool that controls our local debugging application

I've gone through the LangGraph de
ployment documents and found that it always requires Docker for production. However, I'm wondering:

1. Is it possible t
o run LangGraph entirely locally without Docker?
2. Can we just use the framework directly like in the tutorials where w
e build a graph and invoke it with user input?
3. Why is there so little guidance about building agents within local des
ktop applications? Is this approach discouraged?

If Docker is required, what are the alternatives for desktop applicati
on integration?

I'm quite new to agent development, so any guidance would be greatly appreciated. Thanks in advance!


```
---

     
 
all -  [ HELP: Improve llm image processing with number “1” and “7” ](https://www.reddit.com/r/LangChain/comments/1gx7z2t/help_improve_llm_image_processing_with_number_1/) , 2024-11-26-0913
```
Hello! I’m having an issue using the GPT4o model. It gets confused when identifying the numbers 7 and 1 for a task invol
ving analyzing an order on a sheet of paper.  
I’m doing this through the OpenAI playground with a custom assistant, and
 I provide this prompt:  
  
*Instructions for Image Analysis ## Objective Perform a detailed analysis of the informatio
n contained in the image, ensuring the accurate interpretation of alphanumeric characters. ## Specific Criteria 1. Analy
ze each character carefully and precisely. 2. If you identify the number “7,” check if it has a horizontal line in the m
iddle: -* ***With a line:*** *Identify it as “7.” -* ***Without a line:*** *Interpret it as “1.” ## Accuracy Prioritize 
precision in data extraction and interpretation, ensuring the visual information is reflected as faithfully as possible.
*

https://preview.redd.it/kfd5b0l1hg2e1.png?width=1482&format=png&auto=webp&s=7e8e8264bc03873b2461e951fcfef666a5e25de0


I think that The main objective is to identify the number 7 only when it has a “line” in the middle, otherwise identify
 as 1  


in the reference image you can see that the original image(right side) has 1's and the model is reconizing it 
as 7's

If someone could suggest me about how can I improve the model, how can I use RAG for this solution  or your expe
rience and approach with similar projects. I would be very grateful.
```
---

     
 
all -  [ Reasoning behind RAGAS' metric scores ](https://www.reddit.com/r/LangChain/comments/1gx7ie5/reasoning_behind_ragas_metric_scores/) , 2024-11-26-0913
```
Hey guys, I'm using RAGAS' metrics as part of an evaluation framework.

For example, I'm using the Context Recall metric
s which might output a scoe of 0.38, but I really want to know the **reasoning** behind this score.

Is it possible for 
RAGAS to output its reasoning or some kind of verbosity a long side its score?

Appreciate any hints or help!
```
---

     
 
all -  [ Multi Agent tech stack?  ](https://www.reddit.com/r/LangChain/comments/1gx76w0/multi_agent_tech_stack/) , 2024-11-26-0913
```
The multi-agent landscape has had a couple of interesting drops in the last few days:

* **AWS's Multi-Agent Orchestrato
r** ([GitHub](https://github.com/awslabs/multi-agent-orchestrator)): Built-in multi-agent orchestration, intent classifi
cation, and support for streaming responses.
* **LangChain's Agent Protocol** ([Blog](https://blog.langchain.dev/agent-p
rotocol-interoperability-for-llm-agents/)): Aims to standardize LLM agents for interoperability across frameworks.

I’ve
 been building a lot of task specific agents for codebases (debugging, testing, Q&A, LLD etc.) at [potpie](https://potpi
e.ai/) and chose CrewAI for its ease of use. I love how simple it makes things and how it just works with the correct to
oling. But as the number of agents is growing, I am exploring ways to route requests to the right agent intelligently. I
t's also better UX. Here are the options I’m considering:

1. **CrewAI + LangGraph + Agent Protocol**: Integrate current
 agents with LangGraph for routing via Agent Protocol. This is the least amount of effort.
2. **Rebuild in LangGraph**: 
Create a classifier node and add each agent as a conditional node. It also adds first class streaming support to the age
nts which is great for UX and which Crew does not have.
3. **Switch to AWS Orchestrator**: Use AWS’s orchestration and i
ntent handling to simplify routing. Orchestration/ Intent classification is the main feature of this framework, which le
ads me to think management might be easier going ahead. But this involves the most amount of work as not just agents but
 the entire tooling will have to be redone.
4. **CrewAI’s Manager Agent**: Use CrewAI’s hierarchical processes and a cus
tom manager agent for structured task delegation. But I will still be stuck with no realtime response streaming.

I’m cu
rious if anyone has worked with these tools and features—how do they compare in terms of flexibility, scalability, and t
rade-offs? Would love to hear your thoughts! 

P.S The reason I am posting here is I am really leaning towards langgraph
, I just want to know if there are any gotchas with the framework. I've only built a small POC with it till now. 
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-26-0913
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
