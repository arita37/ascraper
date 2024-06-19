 
all -  [ Asking common questions ](https://www.reddit.com/r/OpenAI/comments/1dj4tgd/asking_common_questions/) , 2024-06-19-0910
```
In making a project, I have many questions regarding using 4-o gpt, 4 gpt.

Firstly, how can I measure thar tokens neede
d for use( bases on ??words, chars).

Secondly, while using the langchain with gpt, are the templates used to make the l
lm model always  static? and it will always be executed when send the requests(considering the execution is req;res, as 
they said in their docs..)that being said more tokens needed for this workflow. 

Lastly, is there any way to make the l
lm to recognise(remember the context) the prompts that connected langchain(earlier) that you need to handle every time.


Note:
All this is to know the prompt input usage before buying?


Thanks, in regards..
```
---

     
 
all -  [ Developing a 'Multi-Step Chat Wizard' app using Claude and would like feedback on handling chat hist ](https://www.reddit.com/r/Anthropic/comments/1dj1hnh/developing_a_multistep_chat_wizard_app_using/) , 2024-06-19-0910
```
Hey all! I've built a basic RAG app on AWS in the past but am now looking to build a more complex app. I've gone through
 various docs (Anthropic, Langchain etc.) and think I have some of what I need, but wanted to solicit thoughts/feedback 
here before diving in (only to later realize I made a poor or problematic choice that needs to be walked back):

**Reaso
n for using Claude 3:** Large context windows + performance

**The App:** A multi-step wizard app that guides users thro
ugh a complex process, say, a 15-step journey. Each step is completed in order, and the subsequent step is initialized w
ith a summary of the discussion, notes, and action items from the previous step(s).

**Feature 1: Persisted Chat History
 across Multiple Steps**

* I have a use case-specific LLM with prompt templates for each step.
* Users should be able t
o log out, come back later, and see the full chat history for each step they've completed.
* **Question:** Should I stor
e the chat history as a running log of entries in a database (e.g., PostgreSQL)?
* **Question:** While I plan to use Cla
ude 3 for its large token window, I'm concerned about feeding the raw chat history to the LLM for every new question due
 to potential cost implications. What's the recommended approach for retaining context without incurring excessive token
 costs?

**Feature 2: Detailed Conversation Summaries**

* At the end of each step, the full chat history will be passed
 to an LLM to generate a detailed summary.
* This summary will be fed into the initialization prompt for the LLM in the 
subsequent step, providing context on the user's decisions from the previous step(s).
* As the user progresses, these su
mmaries will be chained together, so by step 6, the initialization prompt includes summaries from steps 1-5.
* **Questio
n:** Are there any recommendations for making this process more efficient without losing or watering down important cont
ext as the user iterates through the steps?

**Additional Consideration:**

* Potential memory limitations or performanc
e bottlenecks as the chat history and summaries grow in size???

I'm open to any suggestions or best practices from the 
LangChain community on architecting this application effectively and efficiently!
```
---

     
 
all -  [ Newb Questions: Maintaining Full Chat History + Chaining Unique Chat Summarizations ](https://www.reddit.com/r/LangChain/comments/1dj1che/newb_questions_maintaining_full_chat_history/) , 2024-06-19-0910
```
Hey all! I've used LC before for a very basic RAG app on AWS but am now looking to build a more complex app. I've gone t
hrough the docs and think I have some of what I need, but wanted to solicit thoughts/feedback here before diving in (onl
y to later realize I made a poor or problematic choice that needs to be walked back):

**The App:** I'm building a multi
-step wizard application that guides users through a complex process, say, a 15-step journey. Each step is completed in 
order, and the subsequent step is initialized with a summary of the discussion, notes, and action items from the previou
s step(s).

**Feature 1: Persisted Chat History across Multiple Steps**

* I have a use case-specific LLM with prompt te
mplates for each step.
* Users should be able to log out, come back later, and see the full chat history for each step t
hey've completed.
* **Question:** Should I store the chat history as a running log of entries in a database (e.g., Postg
reSQL)?
* **Question:** While I plan to use Claude 3 for its large token window, I'm concerned about feeding the raw cha
t history to the LLM for every new question due to potential cost implications. What's the recommended approach for reta
ining context without incurring excessive token costs?

**Feature 2: Detailed Conversation Summaries**

* At the end of 
each step, the full chat history will be passed to an LLM to generate a detailed summary.
* This summary will be fed int
o the initialization prompt for the LLM in the subsequent step, providing context on the user's decisions from the previ
ous step(s).
* As the user progresses, these summaries will be chained together, so by step 6, the initialization prompt
 includes summaries from steps 1-5.
* **Question:** Are there any recommendations for making this process more efficient
 without losing or watering down important context as the user iterates through the steps?

**Additional Consideration:*
*

* Potential memory limitations or performance bottlenecks as the chat history and summaries grow in size???

I'm open
 to any suggestions or best practices from the LangChain community on architecting this application effectively and effi
ciently!
```
---

     
 
all -  [ Best retrieval strategy while comparing small piece of text with documents in vector db ](https://www.reddit.com/r/LangChain/comments/1dizkoq/best_retrieval_strategy_while_comparing_small/) , 2024-06-19-0910
```
Hey ppl,

I am facing an issue while retrieving docs through silimarity search.

String to be matched is a small piece o
f text that contains details about an entity may be a 10 to 20 words. However the docs in my vector db are pdf files (ea
ch doc a single pdf file) which can have 1000 words each. 

When I do a similarity search with the string, my top docume
nt is not the relevant one that I want to fetch. How can I improve this?

Thanks
```
---

     
 
all -  [ How to not mix data from different pdf files or sources in general? ](https://www.reddit.com/r/LangChain/comments/1diz9pw/how_to_not_mix_data_from_different_pdf_files_or/) , 2024-06-19-0910
```
Suppose I want to use RAG to store knowledge about the financial reports of different companies. 

I have used various r
etrievers for this, but I have not yet solved the more complex problem of how the retrievers should know which company a
 given chunk is for or from which source. 

I guess the only option I have is to put a lot of information about the PDF 
in the metadata and try to filter chunks based on that. Have you worked on this before?
```
---

     
 
all -  [ Resume review please and suggest some improvements!not getting anycall backs despite applying in ](https://i.redd.it/ohb0an7jkd7d1.jpeg) , 2024-06-19-0910
```
not getting anycall backs despite applying in
```
---

     
 
all -  [ Can someone from Computer science background suggest some improvement? Not getting callbacks  ](https://i.redd.it/xsz7lnkzjd7d1.jpeg) , 2024-06-19-0910
```

```
---

     
 
all -  [ How to summarize really large json ](https://www.reddit.com/r/LangChain/comments/1diug6j/how_to_summarize_really_large_json/) , 2024-06-19-0910
```
I have a json file that contains  data in below format.
{
'key1': '{json1}',
key2': '{json2}',

key3': '{json3}',
}

jso
n1,json2, json3... has same Structure. 
I am trying to summarize above data. I have tried: 
1. Summarizing using stuffch
ain, without splitting text. & with splitting. 
2. Summarizing using refine,.with and without splitting. 

The summariza
tion is working but it is not taking the whole data in consideration. Sometimes it summarizes only key1,key2 data only. 
Sometimes on key1 json. 

I am using mistral: text model for summarization via langchain. 

1. How to tackle this proble
m? 
2. How do we summarize json properly? 

```
---

     
 
all -  [ HELP: TPM Rate Limit Error ](https://www.reddit.com/r/LangChain/comments/1ditzwa/help_tpm_rate_limit_error/) , 2024-06-19-0910
```
Hey, there!

Running into an error trying to stuff a large amount of text into GPT 4o -- it's small enough for the conte
xt window, but I'm exceeding the TPM limit (30k, according to OpenAI). Here's the exact error:

  
RateLimitError: Error
 code: 429 - {'error': {'message': 'Request too large for gpt-4o in organization org-Qvve8O3Iihgaa2kduvOVIemS on tokens 
per min (TPM): Limit 30000, Requested 45544. The input or output tokens must be reduced in order to run successfully. Vi
sit [https://platform.openai.com/account/rate-limits](https://platform.openai.com/account/rate-limits) to learn more.', 
'type': 'tokens', 'param': None, 'code': 'rate\_limit\_exceeded'}}

  
I've looked at a few solutions, but those all rel
y on feeding the prompt in chunks with delay in between, whereas I need GPT to spit out a single response to my prompt b
ased on the text.

  
Any way you guys know of to slow down the speed at which I'm passing tokens to GPT? 

  
Thanks!
```
---

     
 
all -  [ Should you use the pre-made chains for map reducing? ](https://www.reddit.com/r/LangChain/comments/1ditui4/should_you_use_the_premade_chains_for_map_reducing/) , 2024-06-19-0910
```
**Context**

I'm making a sales pitch creator where users can upload a bunch of PDF files relating to their company, and
 it will output a sales pitch.

I'm handling file uploads separately and would to extract key information from the PDF f
ile and save it in my database, the key here is that I don't want to summarise the info but rather extract the info with
out the filler and redundancy.

I can see there are a bunch of pre-made chains, but I'm not sure which can be used in th
e case of extracting and not summarising, I can also see there is a general map reduce chain, however I can't tell what 
this is doing exactly or how to use it with my prompts where I want to state specifically what information should be ext
racted.

I've taken a look through this:

[https://js.langchain.com/v0.1/docs/modules/chains/document/map\_reduce/#with-
lcel](https://js.langchain.com/v0.1/docs/modules/chains/document/map_reduce/#with-lcel)

And find it extremely confusing
, I can't see what all the complexity is about as in my mind doing what I want is just a case of:

1. Breaking down the 
file into text chunks

2. Extracting info from each using an await Promise.all(chunks.map(c => chain.invoke(...)))

3. C
ombining the extracted info 

**Question**

Why the complexity in the above, what am I missing? Should I just do my simp
le version, or will it break in certain contexts?


```
---

     
 
all -  [ How do you return actionable responses? ](https://www.reddit.com/r/LangChain/comments/1disrgq/how_do_you_return_actionable_responses/) , 2024-06-19-0910
```
Am curious how you articulate an actionable response for end-user's intent, e.g. delete account option that actually del
etes account and not a link to the how-to guide. How would you even go about abstracting it without some sort GUI on the
 frontend? Do you just implement your own or are there solutions out there? 
```
---

     
 
all -  [ LLM monitoring with Langfuse in LCEL Langchain application ](https://www.reddit.com/r/LangChain/comments/1din8vv/llm_monitoring_with_langfuse_in_lcel_langchain/) , 2024-06-19-0910
```
Hello everyone,

Here's a nice article showing how to add LLM monitoring to your Langchain application that uses LCEL. I
 found out first hand how painful it can be to not have anything to monitor your token consumption so I hope it helps yo
u avoid this.  
Here's the link: [article](https://www.metadocs.co/2024/06/18/add-monitoring-easily-to-your-langchain-ch
ains-with-langfuse/).

Have a nice read :D
```
---

     
 
all -  [ Better models than llama3 8b? ](https://www.reddit.com/r/LangChain/comments/1dimec1/better_models_than_llama3_8b/) , 2024-06-19-0910
```
Are there any models of similar size that are better than llama3 8b and that can be run on ollama?
```
---

     
 
all -  [ How can I get custom agent-generated output in the structured format? ](https://www.reddit.com/r/LangChain/comments/1dimbqa/how_can_i_get_custom_agentgenerated_output_in_the/) , 2024-06-19-0910
```
I am creating custom gpt agents and i want output in fixed schema how can I do that ?  


\`\`\`const responseSchema = z
.object({  
problem: z  
.string()  
.describe(  
'Here you will get the problem according to the questions provided in 
the prompt'  
),  
problemScore: z  
.number()  
.describe(  
'Here you will get the score of the problem according to t
he questions provided in the prompt'  
),  
solution: z  
.string()  
.describe(  
'Here you will get the solution accor
ding to the questions provided in the prompt'  
),  
solutionScore: z  
.number()  
.describe(  
'Here you will get the 
score of the solution according to the questions provided in the prompt'  
),  
targetAudience: z  
.string()  
.describ
e(  
'Here you will get the target audience according to the questions provided in the prompt'  
),  
targetAudienceScor
e: z  
.number()  
.describe(  
'Here you will get the score of the target audience according to the questions provided 
in the prompt'  
),  
objections: z  
.string()  
.describe(  
'Here you will get the objections according to the questi
ons provided in the prompt'  
),  
objectionsScore: z  
.number()  
.describe(  
'Here you will get the score of the obj
ections according to the questions provided in the prompt'  
),  
riskReversal: z  
.string()  
.describe(  
'Here you w
ill get the risk reversal according to the questions provided in the prompt'  
),  
riskReversalScore: z  
.number()  
.
describe(  
'Here you will get the score of the risk reversal according to the questions provided in the prompt'  
),  

uniqueness: z  
.string()  
.describe(  
'Here you will get the uniqueness according to the questions provided in the pr
ompt'  
),  
uniquenessScore: z  
.number()  
.describe(  
'Here you will get the score of the uniqueness according to t
he questions provided in the prompt'  
),  
});

const agent = new OpenAIAssistantRunnable({  
clientOptions: {  
apiKey
: process.env.OPENAIGPTKEY,  
},  
assistantId: 'YOUR\_GPT\_ASSISTENE\_ID',  
asAgent: true,  
});

await agent  
.invok
e({  
content: input.url,  
})  
.then((response) => {  
console.info(response);  
});  
\`\`\`

I have defined the zod 
schema and I also tried to attach it with making a function, but I cannot bind it with the agent.

any help would be gra
teful

thank you.
```
---

     
 
all -  [ Will langgraph absorb langchain? ](https://www.reddit.com/r/LangChain/comments/1dikyp6/will_langgraph_absorb_langchain/) , 2024-06-19-0910
```
To me, langgraph appears to be the better backbone structure. And it can completely substitute langchain‘s concept of „a
 chain“. Thus, langchain seems to provide only all the integrations.

Will these integrations finally become a part of l
anggraph, instead of the other way around?
```
---

     
 
all -  [ Conditions in LCEL Chain: Different Chain if retriever does not find something ](https://www.reddit.com/r/LangChain/comments/1dikwmc/conditions_in_lcel_chain_different_chain_if/) , 2024-06-19-0910
```
Hi,

I have a LCEL Chain but now want to adapt it. The idea is to use a RAG chain if the retriever finds something, but 
if the retriever does not find something, I want to use a different prompt. How can I do this?

  
This is my chain at t
he moment:

        context = itemgetter('question') | retriever
        first_step = RunnablePassthrough.assign(context
=context)
        chain = (
            first_step | format_docs
            | chat_history_prompt
            | llm
   
         | StrOutputParser()
        )

  

```
---

     
 
all -  [ Building a KnowledgeGraph and combining with Vector search ](https://www.reddit.com/r/LangChain/comments/1dikb6p/building_a_knowledgegraph_and_combining_with/) , 2024-06-19-0910
```
Hi there,

  
I am currently thinking about making a chatbot which has a vector database containing knowledge from a web
site. As many others I have witnessed that the embedding search rarely performe well in more complex cases where further
 contextual understanding is needed. Therefore I want to add a KnowledgeGraph to the RAG. My knowledge is centered aroun
d tech products such as TV and Internet 

I have played around with using an LLM to define entities and relationships be
tween these. In this process I have these three questions:

1. Does the graph need multiple types of entities and multip
le types of relations? Or could it for example be as simple as Entities (Products) and relationships (related products)?


2. Is it best to use the LLM on the entire documents or could there be and advantage of using it on a chunk level? 

3
. When I use the LLM on the sources over several runs (due to token limits) how do I ensure that the LLM uses the same e
ntity names across the sources, instead of making slight variation in the name for the same entity? Could an accumulated
 list of possible entities created during the runs work as an input in the prompt? 

Next, I need to now how to use the 
outcome of the KnowledgeGraph. Currently I am thinking about assigning the entities and their relationships as meta data
, so lets say my vector search find a document/chunk the meta data should contain an ID of other relevant document/chunk
s (as they include the same entities). Is that a good approach?


```
---

     
 
all -  [ The tools cannot be invoked when starting langgraphjs through streamEvent. ](https://www.reddit.com/r/LangChain/comments/1diiqwe/the_tools_cannot_be_invoked_when_starting/) , 2024-06-19-0910
```
I am trying to build a chatbot using Express. It is a simple setup with an LLM and tools. I followed the official docume
ntation to define a shouldContinue function and added a condition edge from the agent node to the action node or END. Ho
wever, when I run the graph through streamEvent, I can see in the shouldContinue function that the format of the tool\_c
alls in the final AIMessage is not as expected.

The code is as follows:

\`\`\`typescript

import type { StreamEvent } 
from '@langchain/core/tracers/log\_stream';

import type { BaseChatModel } from '@langchain/core/language\_models/chat\_
models';

import type { Embeddings } from '@langchain/core/embeddings';

import type { AIMessageChunk } from '@langchain
/core/messages';

import type { ChatGenerationChunk } from '@langchain/core/outputs';

import EventEmitter from 'events'
;

import logger from '../utils/logger';

import feishuTools from '../toolTikets/feishu';

import getImageUrls from '../
utils/getImageUrls';

import { AIMessage, HumanMessage, BaseMessage } from '@langchain/core/messages';

import { START, 
END, MessageGraph } from '@langchain/langgraph';

import { ToolNode } from '@langchain/langgraph/prebuilt';

function sh
ouldContinue(messages: BaseMessage\[\]): 'action' | typeof END {

const lastMessage = messages\[messages.length - 1\] as
 AIMessage;

if (!lastMessage?.tool\_calls?.length) {

console.log(\`in shouldContinue: end\`);

return END;

} else {


console.log(\`in shouldContinue tool calls: ${JSON.stringify(lastMessage.tool\_calls)}\`);

return 'action';

}

}

func
tion createGraph(llm: BaseChatModel) {

const model = llm.bindTools(feishuTools);

console.log(\`in createGraph:\`);

co
nst workflow = new MessageGraph()

.addNode('agent', model)

.addNode('action', new ToolNode<BaseMessage\[\]>(feishuTool
s))

.addEdge(START, 'agent')

.addConditionalEdges('agent', shouldContinue)

.addEdge('action', 'agent');

return workf
low.compile();

}

async function handleStream(

stream: AsyncGenerator<StreamEvent, any, unknown>,

emitter: EventEmitt
er,

) {

for await (const event of stream) {

console.log(\`in handleStream:\`);

if (event.event === 'on\_llm\_stream'
) {

const chunk: ChatGenerationChunk = [event.data?.chunk](http://event.data?.chunk);

const msg = chunk.message as AIM
essageChunk;

if (msg.tool\_call\_chunks && msg.tool\_call\_chunks.length > 0) {

console.log(\`msg.tool\_call\_chunks: 
${JSON.stringify(msg.tool\_call\_chunks)}\`);

} else {

emitter.emit(

'data',

JSON.stringify({ type: 'response', data
: msg.content }),

);

console.log(\`msg.content: ${JSON.stringify(msg.content)}\`);

}

}

}

emitter.emit('end');

}


function initializeGraph(

messages: BaseMessage\[\],

llm: BaseChatModel,

embeddings: Embeddings,

): EventEmitter {


const emitter = new EventEmitter();

try {

const basicGraph = createGraph(llm);

const stream = basicGraph.streamEvents
(

messages,

{

streamMode: 'values',

version: 'v1',

}

);

handleStream(stream, emitter);

} catch (err) {

emitter.
emit(

'error',

JSON.stringify({ data: 'An error has occurred please try again later' }),

);

logger.error(\`Error in 
websearch: ${err}\`);

}

return emitter;

}

function handleChat(

message: string,

history: BaseMessage\[\],

llm: Ba
seChatModel,

embeddings: Embeddings,

files: { id: string; name: string }\[\],

): EventEmitter {

const messages = his
tory.concat(\[

new HumanMessage({

content: \[

{ type: 'text', text: message },

...(files.length > 0 ? getImageUrls(f
iles) : \[\]),

\],

})

\]);

return initializeGraph(messages, llm, embeddings);

}

export default handleChat;

\`\`\`


The console output is as follows:  
\`\`\`  
in createGraph:

in handleStream:

in handleStream:

in handleStream:

in
 handleStream:

in handleStream:

in handleStream:

in handleStream:

msg.tool\_call\_chunks: \[{'name':'getWeather','ar
gs':'','id':'call\_4qu6Nl2rosohAaHxAigzG9Fd'}\]

in handleStream:

msg.tool\_call\_chunks: \[{'args':'{\\''}\]

in handl
eStream:

msg.tool\_call\_chunks: \[{'args':'location'}\]

in handleStream:

msg.tool\_call\_chunks: \[{'args':'\\':\\''
}\]

in handleStream:

msg.tool\_call\_chunks: \[{'args':'Seattle'}\]

in handleStream:

msg.tool\_call\_chunks: \[{'arg
s':'\\'}'}\]

in handleStream:

msg.content: ''

in handleStream:

in handleStream:

in handleStream:

in handleStream:


in shouldContinue tool calls: \[{'name':'getWeather','args':{},'id':'call\_4qu6Nl2rosohAaHxAigzG9Fd'},{'name':'','args'
:{}},{'name':'','args':{}},{'name':'','args':{}}\]

in handleStream:

in handleStream:

in handleStream:

in handleStrea
m:

in handleStream:

in handleStream:

in handleStream:

in handleStream:

in handleStream:

/Users/mac/WorkSpace/proje
ct/Perplexica-backend/node\_modules/@langchain/langgraph/dist/prebuilt/tool\_node.cjs:31

const outputs = await Promise.
all(message.tool\_calls?.map(async (call) => {

\^

Error: Tool  not found.

at /Users/mac/WorkSpace/project/Perplexica-
backend/node\_modules/@langchain/langgraph/dist/prebuilt/tool\_node.cjs:34:23

at [Array.map](http://Array.map) (<anonym
ous>)

at [ToolNode.run](http://ToolNode.run) (/Users/mac/WorkSpace/project/Perplexica-backend/node\_modules/@langchain/
langgraph/dist/prebuilt/tool\_node.cjs:31:63)

at ToolNode.func (/Users/mac/WorkSpace/project/Perplexica-backend/node\_m
odules/@langchain/langgraph/dist/prebuilt/tool\_node.cjs:9:59)

at ToolNode.\_callWithConfig (/Users/mac/WorkSpace/proje
ct/Perplexica-backend/node\_modules/@langchain/core/dist/runnables/base.cjs:217:33)

at processTicksAndRejections (node:
internal/process/task\_queues:95:5)

at async ToolNode.invoke (/Users/mac/WorkSpace/project/Perplexica-backend/node\_mod
ules/@langchain/langgraph/dist/utils.cjs:62:27)

at async RunnableSequence.invoke (/Users/mac/WorkSpace/project/Perplexi
ca-backend/node\_modules/@langchain/core/dist/runnables/base.cjs:1131:33)

at async Promise.allSettled (index 0)

at asy
nc executeTasks (/Users/mac/WorkSpace/project/Perplexica-backend/node\_modules/@langchain/langgraph/dist/pregel/index.cj
s:546:21)  
\`\`\`
```
---

     
 
all -  [ Why are all Neo4j Knowledge Graph example with LLMs (OpenAI) using Langchain? Possible to do it with ](https://www.reddit.com/r/OpenAI/comments/1digdzx/why_are_all_neo4j_knowledge_graph_example_with/) , 2024-06-19-0910
```
Hey, OpenAI folks. I'm learning how to build knowledge graphs and want to utilize Neo4j. When looking for examples and d
ocumentation, they mostly use Langchain.

I am curious if there is a reason why they all use Langchain, and I potentiall
y do not want to use Langchain, so I specifically want to use OpenAI. Does anyone know if there are any tutorials or doc
umentation around that?

I personally do like Langchain but the level of abstraction makes me want to really understand 
all of this stuff and try experimenting with not using Langchain. So far I have been following the [https://www.deeplear
ning.ai/short-courses/knowledge-graphs-rag/](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/) and [https
://cookbook.openai.com/examples/rag\_with\_graph\_db](https://cookbook.openai.com/examples/rag_with_graph_db)

My bigges
t concern is the Langchain level of abstraction, and potentially, it might cause issues in production if I ever want to 
pivot to a very specific use case.

If the community suggestion is that neo4j and LLM integration best work with Langcha
in, is anyone using this for production?

Again, I'm new to the overall knowledge graph production, but for basic chat c
ompletion, I personally liked building my own without relying on Langchain. Maybe using Neo4j with Langchain is the best
 practice at production. I would love to hear the community's thoughts and recommendations.
```
---

     
 
all -  [ Why are all Neo4j Knowledge Graph example with LLMs (OpenAI) using Langchain? Possible to do it with ](https://www.reddit.com/r/Neo4j/comments/1digda2/why_are_all_neo4j_knowledge_graph_example_with/) , 2024-06-19-0910
```
Hey, Neo4j folks. I'm learning how to build knowledge graphs and want to utilize Neo4j. When looking for examples and do
cumentation, they mostly use Langchain.

I am curious if there is a reason why they all use Langchain, and I potentially
 do not want to use Langchain, so I specifically want to use OpenAI. Does anyone know if there are any tutorials or docu
mentation around that?

I personally do like Langchain but the level of abstraction makes me want to really understand a
ll of this stuff and try experimenting with not using Langchain. So far I have been following the [https://www.deeplearn
ing.ai/short-courses/knowledge-graphs-rag/](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/) and [https:
//cookbook.openai.com/examples/rag\_with\_graph\_db](https://cookbook.openai.com/examples/rag_with_graph_db)

My biggest
 concern is the Langchain level of abstraction, and potentially, it might cause issues in production if I ever want to p
ivot to a very specific use case.

If the community suggestion is that neo4j and LLM integration best work with Langchai
n, is anyone using this for production?

Again, I'm new to the overall knowledge graph production, but for basic chat co
mpletion, I personally liked building my own without relying on Langchain. Maybe using Neo4j with Langchain is the best 
practice at production. I would love to hear the community's thoughts and recommendations.
```
---

     
 
all -  [ Should I use RAG in this scenario? ](https://www.reddit.com/r/LangChain/comments/1difzaj/should_i_use_rag_in_this_scenario/) , 2024-06-19-0910
```
Let's say I'm building an app where someone can upload up to 6 documents describing their company to generate a sales pi
tch, where the prompt is something like 'Take these documents and create a 2-minute sales pitch targetted towards my tar
get market'

  
Does it make sense to use RAG here? My concern is that the prompt needs the full context of the document
, and we wouldn't be able to retrieve the information we need.

  
I'm considering an alternative method of using AI to 
summarise each document and then just embed the entire summary into the prompt
```
---

     
 
all -  [ My experience of building a RAG based agent with LangChain ](https://www.reddit.com/r/LangChain/comments/1diers2/my_experience_of_building_a_rag_based_agent_with/) , 2024-06-19-0910
```
I love LangChain. Previously, I used LangChain v0.1.x for a simple invoice extraction app. Recently, I tried building a 
more complex app, an alternative to Perplexity AI using open-source LLMs, which proved challenging. Here’s my experience
:

* **Dependencies**: Getting started with LangChain required the installation of multiple dependencies, such as core, 
hub, community, etc. Some of these dependencies rely on third-party libraries that needed manual installation. While not
 a major issue, it was somewhat inconvenient. Additionally, some dependencies were quite large, which goes against my pr
eference for avoiding hefty installations.
* **Documentation**: The documentation isn't always current, and occasionally
, Google searches led me to outdated versions. It's crucial to be mindful of the information I use. Using outdated docs 
without immediate issues might cause hidden problems later.
* **Debugging**: Debugging was tough due to LangChain's comp
lexity with many abstractions. I used LangSmith to trace requests and responses. 
* **Agent and Tools**: LangChain’s uni
fied interface for adding tools and building agents is great. It likely performs better with advanced commercial LLMs li
ke GPT4o. However, the open-source LLMs I used and agents I built with LangChain wrapper didn’t produce consistent, prod
uction-ready results.
* **LangGraph**: LangGraph looks interesting. I plan to explore it more in the future.

In the end
, I built an agent without LangChain, using the OpenAI client, Python coroutines for async flow, and FastAPI for the web
 server. The code is a few hundred lines and can be find here [Open Source Perplexity](https://github.com/jjleng/sensei/
blob/main/backend/sensei_search/agents/samurai_agent.py).
```
---

     
 
all -  [ Help required on RAG ](https://www.reddit.com/r/LangChain/comments/1die1tn/help_required_on_rag/) , 2024-06-19-0910
```
I am working on a semi-structured document. I want help finding the best way to perform RAG using open-source only. Plea
se guide me on the same. Have worked in RAG, but this is tedious when comes to optimization and accuracy. Thanks in adva
nce:)..
```
---

     
 
all -  [ Best open source document PARSER??!! ](https://www.reddit.com/r/LangChain/comments/1dicr6p/best_open_source_document_parser/) , 2024-06-19-0910
```
Right now I’m using LlamaParse and it works really well. I want to know what is the best open source tool out there for 
parsing my PDFs before sending it to the other parts of my RAG.  
```
---

     
 
all -  [ Ollama.chat python library  ](https://www.reddit.com/r/ollama/comments/1diajn3/ollamachat_python_library/) , 2024-06-19-0910
```
I can't seem to find any good documentation on this library, can anyone advise? I could use the langchain one I suppose.


My results with .chat we're basic, unable to feed a model or prompt when calling in python rather than using API. Woul
d appreciate tips 
```
---

     
 
all -  [ Formatting Retriever Outputs ](https://www.reddit.com/r/LangChain/comments/1diabgh/formatting_retriever_outputs/) , 2024-06-19-0910
```
So, I’m using a Neo4jVector.as_retriever() as a retriever for a chain.

The retriever outputs and array of Document type
 objects that gets used as a {context} in my prompt template.

What’s the appropriate way to format this output into a s
equence of string objects to be used in my prompt_template?

I’ve been looking into Runnables and just found out about R
unnableLambda and been thinking into turning a function into a Runnable just to format this retriever output, is this re
ally the way to go here? am I missing something?

Thanks in advance!


```
---

     
 
all -  [ Using RAG Agent got error with tools parameter ](https://www.reddit.com/r/LangChain/comments/1di3cfa/using_rag_agent_got_error_with_tools_parameter/) , 2024-06-19-0910
```
I using llm locally when i use `create_openai_tools_agent` 

, then i will get `TypeError: __call__() got an unexpected 
keyword argument 'tools'`

how do i fix it, my code is below:

    from langchain.tools.retriever import create_retrieve
r_tool
    
    retriever_tool = create_retriever_tool(
        retriever = retriever,
        name = 'retriever_tool',

        description = 'Retrieve the most relevant document from the database',
    )
    tools = [retriever_tool]
    
 
   from langchain import hub
    prompt = hub.pull('hwchase17/openai-tools-agent')
    
    from langchain.agents import
 AgentExecutor, create_openai_tools_agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor =
 AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({'input':'What can i do in this system?
'})
    
```
---

     
 
all -  [ Here’s how to use Graph RAG to get better accuracy than std RAG ](https://www.reddit.com/r/LangChain/comments/1di09bu/heres_how_to_use_graph_rag_to_get_better_accuracy/) , 2024-06-19-0910
```
Information on entities like people, institutions, etc. is often highly interconnected, and this might be the case for y
our data too.

If so, you can:

- Create a graph connecting documents which have common n-grams, using TF-IDF etc.

- Du
ring inference, search this graph to get neighbours containing common n-grams and use them in the LLM’s context.

- Sear
ch results from Graph RAG are more likely to give you a comprehensive view of the entity being searched and the info con
nected to it.

Eg, , if doc A is selected as highly relevant, the docs containing data closely linked to doc A must be i
ncluded in the context to give a full picture.

I spent the weekend creating a Python library which automatically create
s this graph for the documents in your vectordb. It also makes it easy for you to retrieve relevant documents connected 
to the best matches.

Here’s the repo for the library: [https://github.com/sarthakrastogi/graph-rag/tree/main](https://g
ithub.com/sarthakrastogi/graph-rag/tree/main)
```
---

     
 
all -  [ End-to-end LLM Workflows Guide ](https://www.reddit.com/r/learnmachinelearning/comments/1dhz0gb/endtoend_llm_workflows_guide/) , 2024-06-19-0910
```
https://preview.redd.it/2dwz47mf357d1.png?width=924&format=png&auto=webp&s=64942b57742d637f1d31d6ea0b38fff07347beaa

Exc
ited to share our end-to-end LLM workflows guide that we’ve used to help our industry customers fine-tune and serve OSS 
LLMs that outperform closed-source models in quality, performance and cost

Key LLM workloads with [Ray](https://docs.ra
y.io/) and [Anyscale](https://anyscale.com/):

* 🔢 Preprocess our dataset (filter, schema, etc.) with batch data process
ing.
* 🛠️ Fine-tune our LLMs (ex. Meta's Llama 3) with full control (LoRA/full param, compute, loss, etc.) and optimizat
ions (parallelism, mixed precision, flash attn, etc.) with distributed training.
* ⚖️ Evaluate our fine-tuned LLMs with 
batch inference using Ray + [vLLM](https://github.com/vllm-project/vllm).
* 🚀 Serve our LLMs as a production application
 that can autoscale, swap between LoRA adapters, optimize for latency/throughput, etc.

Key [Anyscale](https://anyscale.
com/) infra capabilities that keeps these workloads efficient and cost-effective:

* ✨ Automatically provision worker no
des (ex. GPUs) based on our workload's needs. They'll spin up, run the workload and then scale back to zero (only pay fo
r compute when needed).
* 🔋 Execute workloads (ex. fine-tuning) with commodity hardware (A10s) instead of waiting for in
accessible resources (H100s) with data/model parallelism.
* 🔙 Configure spot instance to on-demand fallback (or vice-ver
sa) for cost savings.
* 🔄 Swap between multiple LoRA adapters using one base model (optimized with multiplexing).
* ⚡️ A
utoscale to meet demand and scale back to zero.

🆓 You can run this guide entirely for free on Anyscale (no credit card 
needed). Instructions in the links below 👇

🔗 Links:

* Blog post: [https://www.anyscale.com/blog/end-to-end-llm-workflo
ws-guide](https://www.anyscale.com/blog/end-to-end-llm-workflows-guide)
* GitHub repo: [https://github.com/anyscale/e2e-
llm-workflows](https://github.com/anyscale/e2e-llm-workflows)
* Notebook: [https://github.com/anyscale/e2e-llm-workflows
/blob/main/README.ipynb](https://github.com/anyscale/e2e-llm-workflows/blob/main/README.ipynb)
```
---

     
 
all -  [ How to add an Agent in a LangGraph as a node? Specifically agent created out of create_sql_agent ](https://www.reddit.com/r/LangChain/comments/1dhy51m/how_to_add_an_agent_in_a_langgraph_as_a_node/) , 2024-06-19-0910
```
I am trying to use the helper method create\_sql\_agent to create an agent and add it in a simple graph to create a data
base team. I tried to see if [SQL tutorial](https://python.langchain.com/v0.2/docs/integrations/toolkits/sql_database/) 
can be repurposed.

The graph structure that I wanted to design is very simple. A supervisor that delegates to a SQL Tea
m.

I tried following [https://python.langchain.com/v0.2/docs/tutorials/sql\_qa/#agents](https://python.langchain.com/v0
.2/docs/tutorials/sql_qa/#agents)  as suggested by u/hwchase17 for one of the previous [question](https://www.reddit.com
/r/LangChain/comments/1d4lwt0/am_i_the_only_one_who_feels_langgraph/). However, it uses the AgentExecutor instead of usi
ng langgraph as Agent Executor.

There are examples of connecting to SQL database in the [customer support chat bot tuto
rial](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/). How we are not able to lev
erage the advantages that we get by using an SQL Agent namely:

* Recovering from errors and regenerating query correctl
y.
* Querying database multiple times.
* Save Tokens by looking into schema etc.

If there are any notebooks or code tha
t you could point to that would be great.

I started learning LangGraph for the promise of composing and using agents. I
f this is not doable with critical agents like SQL Database, then that defeats the purpose. Also that AgentExecutor is d
eprecated, it would be great if some of these tutorials are updated to use LangGraph as AgentExecutor / ChatExecutor.
```
---

     
 
all -  [ 20M looking for SWE internships. Previous internship took 300 apps, but not sure how to improve resu ](https://www.reddit.com/r/resumes/comments/1dhy444/20m_looking_for_swe_internships_previous/) , 2024-06-19-0910
```
https://preview.redd.it/lctxew5aw47d1.jpg?width=2550&format=pjpg&auto=webp&s=1e5854ebd28f62fde665fa47a85fc64ba13c3224

A
s stated in title, took me 300+ apps to get my current internship. Of that 300, got 4 interviews, 3 rejects, one offer. 
I didn't have access to the exact numbers so kinda made them up with a estimated guess

I just finished year 1 in EEE, n
ow planning on looking for either next year's summer internship. Or part time internship during the semester.

The point
s under my SWE internship is IMO not very good, since

1.) I've only been doing this internship for about 4 weeks, but a
 recruiter is asking for my resume. So I'd thought I just update my resume

2.) I'm only assigned really simple projects
( takes 2-3 days?) so I don't know how to quantify or make it sound more impressive.

Appreciate your help!
```
---

     
 
all -  [ How to circumvent one document per page when loading PDF files? ](https://www.reddit.com/r/LangChain/comments/1dhv3a5/how_to_circumvent_one_document_per_page_when/) , 2024-06-19-0910
```
I know this might be a really stupid question, but i thought I could gain some insight, by asking it here.   
I am curre
ntly working on a simple RAG application, where I load in documents from a larger local library.   
This library consist
s of multiple different document types, although mostly .docx and .pdf files.   
When loading the PDF files I am current
ly using the PyMuPDFLoader. However it chunks the pdf into pages from the start.   
My questoin is, whether there is a w
ay to circumvent loading a PDF file, and already chunking it into a document for each individual page. Some information 
is lost between the documents, as it might traverse at a page break. 

I would like to implement the chunking strategy l
ater on, as we are looking into implementing a costum chunking strategy. 

Is there a smart strategy for this? 

Thanks 
in advance
```
---

     
 
all -  [ Suggest me a video tutorial about LangChain ](https://www.reddit.com/r/learnmachinelearning/comments/1dhu5sx/suggest_me_a_video_tutorial_about_langchain/) , 2024-06-19-0910
```
Suggest me some yt video link for langchain, the one which is more focused on basic/foundational concept and teaches fro
m very basic thing rather than just focusing on a project type work
```
---

     
 
all -  [ OpenAI Content Filter when using MapReduce ](https://www.reddit.com/r/LangChain/comments/1dhl76g/openai_content_filter_when_using_mapreduce/) , 2024-06-19-0910
```
Using Langchain v0.2, model is limited to gpt-3.5-turbo with Azure (environment provided by the client)

Hello!

Looking
 for some directions on where to read or how to proceed to solve the following situation:

I have very big texts that I 
want to summarize. In the past I had read about MapReduce with Langchain so I tried with it. I am creating chunks of tex
ts and processing them. It works, but when something in a chunk triggers the OpenAI content filter, the summarization fo
r the whole chunk fails. I was wondering if there is a way to keep processing the chunk in order to get a result for the
 parts of the chunk that didn't have issues with the content filter. Otherwise, I'd have to implement the MapReduce myse
lf.

I'd appreciate if you could point me to some documents, or if you could suggest how I may approach this problem.

 
 
Thank you very much in advance.
```
---

     
 
all -  [ Dealing with Incomplete Structured Output? ](https://www.reddit.com/r/LangChain/comments/1dhe1es/dealing_with_incomplete_structured_output/) , 2024-06-19-0910
```
I have a use case where I generate a json output. The json is sometimes so large that it gets over the output range capa
bility of my llm, rendering my structured output not parseable. What method you guys apply when faced with an incomplete
 Structured output?
```
---

     
 
all -  [ Suggesting which RAG method will work best for you, based on your use case 🔎📑  ](https://www.reddit.com/r/LangChain/comments/1dh79xx/suggesting_which_rag_method_will_work_best_for/) , 2024-06-19-0910
```
Most RAG apps use Dense Passage Retrieval to find relevant docs. But there are better methods:

1. RAG-Token:

It genera
tes each token by considering different docs and chooses the most probable token at each step. So that every part of the
 answer is influenced by the best possible context.

2. RAG-Sequence:

It calculates the probability of each answer and 
selects the one with the highest combined probability, getting you the best possible answer based on multiple sources. I
t’s a lot like RAG-token but less granular.

3. Fusion-in-Decoder (FiD):

It encodes all pairs of questions and chunks i
n parallel and then combines these encodings before feeding them into the decoder, which generates the answer step-by-st
ep.

4. Graph RAG:

In case your documents are highly interconnected, the links between them are probably important to g
enerate a relevant response.

Search results from Graph RAG are more likely to give you a comprehensive view of the enti
ty being searched and the info connected to it.

I spent the weekend creating a Python library which automatically creat
es this graph for the documents present in your vectordb. It also makes it easy for you to retrieve relevant documents c
onnected to the best matches.

Currently testing the library on medical documents to gauge its performance.

Sharing ver
sion 0.1 tomorrow! You can follow my social media to stay tuned: [https://linktr.ee/sarthakrastogi](https://linktr.ee/sa
rthakrastogi)


```
---

     
 
all -  [ Determinism control ](https://www.reddit.com/r/LangChain/comments/1dh5qr2/determinism_control/) , 2024-06-19-0910
```
Im trying to get my workflow to be accurate and help me give the same response every time.

I have temp set to zero. bas
e prompt bossing the model around to be 'deterministic' but you can see, i still have wildly different outputs each time
 thing thing runs.

any advice on getting this to be more accurate?

https://preview.redd.it/ibu2ivj68x6d1.png?width=190
8&format=png&auto=webp&s=47bd31b849fa690dc12e11cc9604702587aae6fa

base prompt: You are a deterministic GPT model design
ed to analyze a list of transactions in a SQL table. Your task is to provide the same response every time you are asked 
the same question. Follow these guidelines to ensure determinism:

1. Always follow the exact format provided in the exa
mples below.
2. Provide responses based strictly on the information available in the given table.
3. Do not include any 
additional or inferred information.
4. Ensure the order of transactions is consistent based on the primary key or specif
ied order.

Note: the actual correct answer is 106 items. the SQL has 2,000 lines on it
```
---

     
 
all -  [ Passing API Key via URL Params ](https://www.reddit.com/r/LangChain/comments/1dh3fq8/passing_api_key_via_url_params/) , 2024-06-19-0910
```
Hi there!  
  
I am trying to query an api with its auth value as its get parameter   
[https://test.com/?key=apikey](ht
tps://test.com/?key=apikey)   
How do I tell the Langchain agent to pass an additional url param? (in this case, key) in
 every requests?

This is how it is executed atm. Thanks in advance <3

    model = Chat(model='claude-3-haiku-20240307'
, api_key=CLAUDE_API_KEY)
    weather_agent = planner.create_openapi_agent(
        MY_OPENAPI_SPEC,
        RequestsWra
pper(),
        llm=model,
        allow_dangerous_requests=True
    )
```
---

     
 
all -  [ ERROR: pip's dependency resolver  ](https://www.reddit.com/r/FaceFusion/comments/1dh2zu3/error_pips_dependency_resolver/) , 2024-06-19-0910
```
https://preview.redd.it/oq5moytn7w6d1.png?width=1211&format=png&auto=webp&s=17fe145a3e0ae18aca4eda9c2ac2978c42bb2cb9

I 
did everything before it almost flawlessly, and now when I do python install.py. it shows this.

I tried various methods
 hoping to fix this problem

upgrading the pip

installing the dependencies myself

and fixing some codes in the .py ( d
idn't work so I recovered it

but now I have no other ideas to fix this, I need your help

  
EDIT:  
I installed minico
nda because I wanted more free space on my disc, and this turned out to be the solution

I'm not sure if this was the pr
oblem, but after I installed miniconda and uninstalled anaconda, and now if I run [run.py](http://run.py),  it's actuall
y working now
```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/Resume/comments/1dh1hfu/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-19-0910
```
https://preview.redd.it/q8dfqp2aov6d1.jpg?width=1275&format=pjpg&auto=webp&s=6b7e6392ee8eb79d53349eac7d18eddc08759535

h
ttps://preview.redd.it/h8ffm4acov6d1.jpg?width=1275&format=pjpg&auto=webp&s=835b85d481ee25e79d6f94646e238e0d9f09ad60


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/developersIndia/comments/1dh1bj2/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-19-0910
```
https://preview.redd.it/b0n4g6izlv6d1.jpg?width=1275&format=pjpg&auto=webp&s=de76a6165f59fbc9d18924eb26796a9cb7d095a3


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/resumes/comments/1dh18d3/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-19-0910
```
https://preview.redd.it/b9vhtwowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=f6df4a4e647d3de7331903ac184b58135befa9f5

h
ttps://preview.redd.it/rexnwyowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=8503335ba04cc4a0321fb6500f0e4bd153e03bcf


```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-19-0910
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-19-0910
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-19-0910
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-19-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
