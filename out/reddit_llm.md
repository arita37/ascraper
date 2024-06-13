 
all -  [ Review my resume, not getting any calls ](https://www.reddit.com/r/resumes/comments/1dehi9a/review_my_resume_not_getting_any_calls/) , 2024-06-13-0953
```
https://preview.redd.it/kbr9xd1hg76d1.jpg?width=1080&format=pjpg&auto=webp&s=e32bbba25f324d01f797f323f50ca4e7479dc3b8

H
i, Please review my resume. I am not getting any calls. I have been applying for jobs since March 
```
---

     
 
all -  [ Need Help to make langchain chatbot ](https://www.reddit.com/r/LangChain/comments/1deh52g/need_help_to_make_langchain_chatbot/) , 2024-06-13-0953
```
I have to make llm chatbit using open ai on flask. 
Help me to make this. 
```
---

     
 
all -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-13-0953
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

     
 
all -  [ Build a QA Bot for your documentation with Langchain ](https://www.reddit.com/r/developersIndia/comments/1dedwwg/build_a_qa_bot_for_your_documentation_with/) , 2024-06-13-0953
```
Build an AI-powered Q&A bot for your website documentation using Wing TypeScript, Next.js, and Langchain.  
  
-  Create
 a user-friendly Next.js app to accept questions and URLs  
-  Set up a Wing TypeScript backend to handle all the reques
ts  
-  Incorporate Langchain for AI-driven answers by scraping and analyzing documentation using RAG  
-  Complete conn
ection between frontend input and AI-processed responses.

Check out the full article [here](https://wingla.ng/qa-bot).
```
---

     
 
all -  [ AI / LLMs in your Obsidian - what's actually been useful for you? ](https://www.reddit.com/r/ObsidianMD/comments/1dedmeu/ai_llms_in_your_obsidian_whats_actually_been/) , 2024-06-13-0953
```
There's a bunch of new plug ins available and with projects like PrivateGPT or LangChain it's easy to start talking with
 your own data.

  
But...

  
**What has been the most useful way of using LLMs within your Vault?**

  
I've been work
ing on a flow that takes stuff that I read/ learned this week and summarizing it to form the draft I can use as a weekly
 newsletter for learning in public. 

It's not there yet, and I still edit/ write the content. But the initial draft and
 summarization of my highlights has been helpful. So I see:



Source 1

- takeaway

- takeaway

Source 2

..




```
---

     
 
all -  [ Building Devops AI Assistant with Langchain, Ollama, and PostgreSQL ](https://docs.rapidapp.io/blog/building-devops-ai-assistant-with-langchain-ollama-and-postgresql) , 2024-06-13-0953
```

```
---

     
 
all -  [ Roast my Resume ](https://www.reddit.com/r/resumes/comments/1deblue/roast_my_resume/) , 2024-06-13-0953
```
Been trying to get a Software Engineering Internship for a year now, but with over 200 applications submitted, my interv
iew rate was 1%. I am a Software Developer niching out into DevOps, AI, and AWS System Design infrastructure, because I 
feel everyone just knows Software Development nowadays. I really want to lock in a Software Engineering Internship by ne
xt summer so please give me all the criticism you got.

https://preview.redd.it/y9hx8cq7966d1.png?width=647&format=png&a
uto=webp&s=45fe513c46fdc8a6eca7bd2909a9e1ad0e0f4bd2


```
---

     
 
all -  [ Need Help Implementing Supervisor with LangGraph ](https://www.reddit.com/r/LangChain/comments/1deaviw/need_help_implementing_supervisor_with_langgraph/) , 2024-06-13-0953
```
Hey everyone,

I'm working on a Supervisor with LangGraph for a company internship. My mentor has asked me to create thr
ee Agents: 'Question Agent', 'Answer Agent', and 'Summarizer Agent'. The input is a PDF, which I need to split by page a
nd add each page to a vectorial database for later use. Each agent will also save its outputs in the vectorial POSTGRES 
database. Here's a rough idea of the structure:

**Questions Table**

* id (Primary Key)
* question (Text)
* embedding (
Vector)
* document\_id (Integer)
* page\_number (Integer)

**Answers Table**

* id (Primary Key)
* answer (Text)
* embed
ding (Vector)
* document\_id (Integer)
* page\_number (Integer)
* question\_id (Foreign Key to Questions table)

**Summa
ries Table**

* id (Primary Key)
* summary (Text)
* embedding (Vector)
* document\_id (Integer)
* page\_number (Integer)


**Documents Table**

* id (Primary Key)
* summary (Text)
* document\_id (Integer)
* number\_of\_pages (Integer)

The w
orkflow is something like this:

1. Load the document (sanitize the text, embed it, save in 'Documents')
2. Make a summa
ry of each page (save in 'Summaries')
3. Generate questions for each page (save in 'Questions')
4. Answer all the questi
ons generated by the Question Agent, considering the context of the page (save in 'Answers')

**My biggest question is:*
* what tools and agents should I implement for this? Most resources I've found online use tools like Tavily Search and P
ython REPL, which aren't really helpful for my case. I need to use the Supervisor since it's a project requirement, and 
I'm a bit confused about the implementation details, since this would be very easy to implement with simple chains, and 
the only solution I could come up with is tooless agents...?

Any advice or pointers would be greatly appreciated! Thank
s!
```
---

     
 
all -  [ Open-source implementation of Meta’s TestGen–LLM - CodiumAI ](https://www.reddit.com/r/LangChain/comments/1deals9/opensource_implementation_of_metas_testgenllm/) , 2024-06-13-0953
```
In Feb 2024, Meta published a paper introducing TestGen-LLM, a tool for automated unit test generation using LLMs, but d
idn’t release the TestGen-LLM code.The following blog shows how CodiumAI created the first open-source implementation - 
Cover-Agent, based on Meta's approach: [We created the first open-source implementation of Meta’s TestGen–LLM](https://w
ww.codium.ai/blog/we-created-the-first-open-source-implementation-of-metas-testgen-llm/)

The tool is implemented as fol
lows:

1. Receive the following user inputs (Source File for code under test, Existing Test Suite to enhance, Coverage R
eport, Build/Test Command
Code coverage target and maximum iterations to run, Additional context and prompting options)

2. Generate more tests in the same style
3. Validate those tests using your runtime environment - Do they build and pass
?
4. Ensure that the tests add value by reviewing metrics such as increased code coverage
5. Update existing Test Suite 
and Coverage Report
6. Repeat until code reaches criteria: either code coverage threshold met, or reached the maximum nu
mber of iterations
```
---

     
 
all -  [ Error with tool calling while using Gemini Pro ](https://www.reddit.com/r/LangChain/comments/1de99jx/error_with_tool_calling_while_using_gemini_pro/) , 2024-06-13-0953
```
Hi all, 

I get an 'An error occurred: Multiple function calls are not currently supported' while using Gemini Pro .  
A
nyone had the same issue?

Using:

    llm = ChatGoogleGenerativeAI(temperature=0, model='gemini-pro')
    llm.bind_tool
s(tools)
```
---

     
 
all -  [ A serious security issue with GPT4o ](https://www.reddit.com/r/LangChain/comments/1de7ar1/a_serious_security_issue_with_gpt4o/) , 2024-06-13-0953
```
Last week we came across a serious security issue with GPT4o. In both ChatGPT and OpenAI APIs. Until OpenAI fixes it, we
 manage to fix from our side. We would like to share it with the community. We implemented it in LlamaIndex but should b
e easy to implement using Langchain as well.  
This is the medium article about the fix - [https://medium.com/@deltaarun
a/fixing-a-serious-security-issue-in-gpt4o-api-via-llamaindex-4aa1368b5d2f](https://medium.com/@deltaaruna/fixing-a-seri
ous-security-issue-in-gpt4o-api-via-llamaindex-4aa1368b5d2f)

This is the medium article about the issue - [https://medi
um.com/@deltaaruna/how-anyone-can-hack-chatgpt-aa7959684ef0](https://medium.com/@deltaaruna/how-anyone-can-hack-chatgpt-
aa7959684ef0)
```
---

     
 
all -  [ Best Open Source Model to being to fine tune for Algebra/Geometry? ](https://www.reddit.com/r/LLMDevs/comments/1de6z6u/best_open_source_model_to_being_to_fine_tune_for/) , 2024-06-13-0953
```
Looking to make an open source LLM a textbook you can talk to.  I'm a teacher and currently knee deep into langchain, py
thon, and ollama for now.  But before I start this mess (not even sure this will work), what is the best model to begin 
with that is focused on solving math problems.  I'm going to use RAG and train it on some textbooks (how I feed it the i
nformation successfully I'm also trying to figure out now, not to mention can i even train it using past conversations a
nd fine tune on my NVIDIA 3070).  But any recommendations?  Want to help my kids next year and give them the best possib
le experience to learn.  I'm didn't go to college for this but I've taught myself python, langchain, and other long word
s so far so how hard can it be...?
```
---

     
 
all -  [ Deploy Langgraph in Google Cloud? ](https://www.reddit.com/r/LangChain/comments/1de6u3j/deploy_langgraph_in_google_cloud/) , 2024-06-13-0953
```
I have been searching extensively but haven't found any guide on deploying a Langgraph runnable with Google Cloud.   
  

Currently, I am using an Reasoning Engine (Vertex AI) with the LangchainAgent template (from Google Cloud documentation
)  
  
Now, I tried to deploy my custom Reasoning Engine agent based on Langgraph and I can't.   
  
I would greatly app
reciate any kind of help.   
  
Regards.   
  
PD: Langchain image to bait.

https://preview.redd.it/03fqi0fm856d1.jpg?w
idth=1024&format=pjpg&auto=webp&s=0bab82582504720db2d45a2d82cbec2aad0981a6


```
---

     
 
all -  [ Help regarding application specific chatbot ](https://www.reddit.com/r/LangChain/comments/1de6133/help_regarding_application_specific_chatbot/) , 2024-06-13-0953
```
I have been given a requirement from my company to look into and try to comeup with a chatbot that would be integrated i
nto the web application.
Specifically, we have a list of Companies and their details like name, what they do, their reve
nues, etc. and some uploaded pdf files that contain more information regarding the company.
So the chatbot will be integ
rated into the details page of the companies. User could then ask any question regarding the company and the chatbot sho
uld provide a relevant answer for that company.

I am fairly new to this, but was able to find out that we can use RAG f
or achieving this, wherein we take all the data and embed it in a vector database. Then fetch relevant vectors per the q
uestion asked and provide it as context to the LLM for answer.

However the issue is that some of the data of the compan
y can change with time.

Is there a way to do it so that the pdf data can use vector store, but the rest of the data can
 be obtained from API calls?
That way, we will always have the most recent data of the company, but also have the additi
onal data from the pdf docs?

How would all these things fit?
How would the decision be made when to use data from vecto
r database or when to fetch data from API?

Do you guys have any experience with something like this or any recommendati
ons or resources where I can look into for this project?

That would be very helpful.
```
---

     
 
all -  [ Google study says fine-tuning an LLM linearly increases hallucinations? 😐 ](https://www.reddit.com/r/LangChain/comments/1de5ury/google_study_says_finetuning_an_llm_linearly/) , 2024-06-13-0953
```
They prepare a QA task to observe hallucinations, on both Known examples (training instances similar to the info that th
e model has seen during its initial training) and Unknown examples (that introduce new info that the model hasn't been e
xposed to before).

They see that:

1. Unknown examples in the fine-tuning dataset bring down performance, the more you 
train, because of overfitting. They lead to hallucinations and reduce accuracy. Known examples positively impact perform
ance.

2. Early stopping helps avoid this, which might mean that Unknown examples are neutral in shorter training.

3. T
he slower fitting of Unknown examples also indicates that models struggle to acquire new knowledge through fine-tuning.


Paper: [https://arxiv.org/pdf/2405.05904](https://arxiv.org/pdf/2405.05904)



I share high quality AI updates and tuto
rials daily.

If you like this post and want to stay updated on latest AI research, you can check out: [https://linktr.e
e/sarthakrastogi](https://linktr.ee/sarthakrastogi) or my Twitter: [https://x.com/sarthakai](https://x.com/sarthakai)
```
---

     
 
all -  [ LangChain/Next.js chatbot displaying incorrect sources ](https://www.reddit.com/r/LangChain/comments/1de50ah/langchainnextjs_chatbot_displaying_incorrect/) , 2024-06-13-0953
```
I'm building a chatbot using `LangChain`, `Next.js`,and `CosmosDB` (vector store). My implementation is based on [this](
https://github.com/langchain-ai/langchain-nextjs-template/blob/main/app/api/chat/retrieval/route.ts). I'm trying to disp
lay the source documents used by the LLM in my UI, but I'm facing two issues:

1. Source documents not displaying: Despi
te using a **StreamingTextResponse** to send the source information in the headers as JSON chunks (see code snippet belo
w), they don't show up in my UI. There are no console errors.
2. Incorrect sources: When some source documents do appear
, they are not the ones actually used by the LLM or contain unrelated information.

Here's the part supposed to return t
he sources:

    import { NextRequest, NextResponse } from 'next/server';
    import { Message as VercelChatMessage, Str
eamingTextResponse } from 'ai';import { AzureCosmosDBVectorStore } from '@langchain/community/vectorstores/azure_cosmosd
b';
    import {
      AzureOpenAIEmbeddings,
      AzureChatOpenAI,
    } from '@langchain/azure-openai';
    import { 
PromptTemplate } from '@langchain/core/prompts';
    import { Document } from '@langchain/core/documents';
    import { 
RunnableSequence } from '@langchain/core/runnables';
    import {
      BytesOutputParser,
      StringOutputParser,
   
 } from '@langchain/core/output_parsers';
    
    const combineDocumentsFn = (docs: Document[]) => {
      const serial
izedDocs = docs.map((doc) => doc.pageContent);
      return serializedDocs.join('\n\n');
    };
    
    const formatVer
celMessages = (chatHistory: VercelChatMessage[]) => {
      const formattedDialogueTurns = chatHistory.map((message) => 
{
        if (message.role === 'user') {
          return `Human: ${message.content}`;
        } else if (message.role =
== 'assistant') {
          return `Assistant: ${message.content}`;
        } else {
          return `${message.role}: 
${message.content}`;
        }
      });
      return formattedDialogueTurns.join('\n');
    };
    
    const CONDENSE_
QUESTION_TEMPLATE = `Given the following conversation and a follow up question, rephrase the follow up question to be a 
standalone question, in its original language.<chat_history>
      {chat_history}
    </chat_history>
    
    Follow Up
 Input: {question}
    Standalone question:`;
    const condenseQuestionPrompt = PromptTemplate.fromTemplate(
      COND
ENSE_QUESTION_TEMPLATE
    );
    
    const ANSWER_TEMPLATE = `Answer the question based only on the following context 
and chat history:
    <context>
      {context}
    </context>
    <chat_history>
      {chat_history}
    </chat_histor
y>
    
    Question: {question}
    `;
    const answerPrompt = PromptTemplate.fromTemplate(ANSWER_TEMPLATE);
    
    
export async function POST(req: NextRequest) {
      try {
        const body = await req.json();
        const messages
 = body.messages ?? [];
        const previousMessages = messages.slice(0, -1);
        const currentMessageContent = me
ssages[messages.length - 1].content;
    
        const vectorstore = new AzureCosmosDBVectorStore(
          new AzureO
penAIEmbeddings(),
          {
            databaseName: process.env.DB_NAME,
            collectionName: process.env.DB
_COLLECTION_NAME,
          }
        );
    
        const model = new AzureChatOpenAI({
          azureOpenAIEndpoint:
 process.env.AZURE_OPENAI_API_ENDPOINT,
          azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY,
          azureOp
enAIApiDeploymentName:
            process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME,
          modelName: process.env.AZURE_
OPENAI_MODEL_NAME,
        });
        const standaloneQuestionChain = RunnableSequence.from([
          condenseQuestio
nPrompt,
          model,
          new StringOutputParser(),
        ]);
    
        let resolveWithDocuments: (value:
 Document[]) => void;
        const documentPromise = new Promise<Document[]>((resolve) => {
          resolveWithDocume
nts = resolve;
        });
    
        const retriever = vectorstore.asRetriever({
          callbacks: [
            {

              handleRetrieverEnd(documents) {
                resolveWithDocuments(documents);
              },
       
     },
          ],
        });
    
        const retrievalChain = retriever.pipe(combineDocumentsFn);
    
        co
nst answerChain = RunnableSequence.from([
          {
            context: RunnableSequence.from([
              (input)
 => input.question,
              retrievalChain,
            ]),
            chat_history: (input) => input.chat_histor
y,
            question: (input) => input.question,
          },
          answerPrompt,
          model,
        ]);
  
  
        const conversationalRetrievalQAChain = RunnableSequence.from([
          {
            question: standaloneQu
estionChain,
            chat_history: (input) => input.chat_history,
          },
          answerChain,
          new 
BytesOutputParser(),
        ]);
    
        const stream = await conversationalRetrievalQAChain.stream({
          que
stion: currentMessageContent,
          chat_history: formatVercelMessages(previousMessages),
        });
    
        c
onst documents = await documentPromise;
        console.log('documents ', documents.length);
        const serializedSou
rces = Buffer.from(
          JSON.stringify(
            documents.map((doc) => {
              return {
              
  pageContent: doc.pageContent.slice(0, 50) + '...',
                metadata: doc.metadata,
              };
          
  })
          )
        ).toString('base64');
        const sourceMetadata = documents.map((doc) => ({
          title:
 doc.metadata.title, // Or whatever metadata you want
          url: doc.metadata.url,
        }));
    
        return 
new StreamingTextResponse(stream, {
          headers: {
            'x-message-index': (previousMessages.length + 1).to
String(),
            'x-message-sources': serializedSources,
          },
        });
      } catch (e: any) {
        
return NextResponse.json({ error: e.message }, { status: e.status ?? 500 });
      }
    }
    

So my questions:

1. Is
 my approach to streaming source documents via **StreamingTextResponse** wrong?
2. How can I ensure I'm associating the 
correct source documents with each LLM response?
3. What debugging techniques can I use to pinpoint where the source inf
ormation is getting lost or mismatched?  
```
---

     
 
all -  [ Local Source Code Indexing & Querying with RAG ](https://www.reddit.com/r/LangChain/comments/1de4yz8/local_source_code_indexing_querying_with_rag/) , 2024-06-13-0953
```
I'm currently working on a local codebase and was using Cody to ask questions from my local code base context. But was w
ondering if there is an open-source project that's similar. Ideally, the tool would:

* Index all project files
* Retrie
ve specific code snippets from all files or tell about specific local variables
* Use as Chatbot?

Document loaders and 
file embeddings could work but I'm not sure on how to handle function interdependencies. Do I need to also additionally 
pass AST for it to organize it better? Not really sure on what direction to take?

Anyone has tried something similar? W
hat approach did you take? and how was the result?
```
---

     
 
all -  [ What are the biggest problems you're facing while building AI apps? ](https://www.reddit.com/r/ChatGPT/comments/1de32az/what_are_the_biggest_problems_youre_facing_while/) , 2024-06-13-0953
```
I've just started building an AI app using ChatGPT + Langchain set-up. I've been facing a number of recurring pain point
s and I'm genuinely curious if the rest of you are facing similar issues. I'm purposely not mentioning the issues I'm fa
cing, because I don't want to bias the answers / keep the discussion as open as possible. What are the biggest issues / 
pain points you're struggling with while building AI apps?
```
---

     
 
all -  [ How to Speed Up Execution with OpenAI GPT-4o in Multi-Agent System? ](https://www.reddit.com/r/crewai/comments/1de2mdr/how_to_speed_up_execution_with_openai_gpt4o_in/) , 2024-06-13-0953
```
**Hey everyone,**

I've been working on a multi-agent system using OpenAI's GPT-4o model, but I'm running into performan
ce issues. The execution time is longer than I'd like, even though I've set `max_iter` to 2 for each agent. but i have u
ser groq its fast but i need solution for gpt-4o or openAI api only !

**Here's a brief overview of my setup:**

1. **Qu
estioning Agent**: Designed to ask relevant questions to gather information from the user.
2. **Validation Agent**: Ensu
res the questions generated by the Questioning Agent are of high quality.
3. **Crew**: Manages the agents and tasks, exe
cuting them hierarchically.

Here's a snippet of my code for context:

  
`import os`

`from crewai import Agent, Task, 
Crew, Process`

`from langchain_openai import ChatOpenAI`



`os.environ['OPENAI_API_KEY'] = 'MY_KEY'`

`llm = ChatOpenA
I(`

`model='gpt-4o',`

`temperature=0.1,`

`)`



`number_of_questions = 10`



`questioning_agent = Agent(`

`role='Qu
estioning Agent',`

`goal='Ask relevant questions to gather information and clarify user needs here is how you should re
spond :- {sys-prompt}',`

`verbose=True,`

`max_iter=2,`

`llm = llm,`

`memory=False,`

`backstory=('Your AI guide for 
asking insightful questions. I'm designed to help users clarify their goals and needs by asking targeted questions. My g
oal is to gather information, identify patterns, and provide a personalized learning experience. I'll ask questions that
 are open-ended, relevant, and designed to encourage the user to provide detailed responses. I'll also use the user's re
sponses to ask follow-up questions, ensuring that I gather all the necessary information to provide a comprehensive lear
ning experience.'),`

`allow_delegation=True`

`)`



`validation_agent = Agent(`

`role='Validation Agent',`

`goal='Va
lidate {val-prompt} and check does it follow this format:-{for}',`

`verbose=True,`

`max_iter = 2,`

`llm = llm,`

`mem
ory=False,`

`backstory=('Your AI guide for ensuring question quality. I'm responsible for reviewing the questions gener
ated by the Questioning Agent and providing feedback on their relevance, clarity, and effectiveness. My goal is to ensur
e that the questions are useful, concise, and easy to understand. I'll review the questions for grammar, syntax, and spe
lling, as well as their ability to gather useful information from the user. I'll provide feedback on the questions, sugg
esting improvements or changes as needed, to ensure that they meet the highest standards of quality and effectiveness.')
,`

`allow_delegation=True`

`)`



`questioning_task = Task(`

`description=('Ask a series of questions to gather infor
mation about the user's learning goals, preferences, and needs. The questions should be open-ended, relevant, and design
ed to encourage the user to provide detailed responses. The questions should also be tailored to the user's specific goa
ls and needs, taking into account their level of expertise, learning style, and desired outcomes. Here is What User situ
ation : {user}'),`

`expected_output='A set of relevant, well-crafted questions that gather useful information about the
 user.You respond should be like this \n{for}',`

`agent=questioning_agent,`

`async_execution=False`

`)`



`validatio
n_task = Task(`

`description=('Review the generated questions for quality, relevance, and effectiveness. Provide feedba
ck on the questions, suggesting improvements or changes as needed. The feedback should be detailed and constructive, pro
viding specific examples and suggestions for improvement. The goal is to ensure that the questions are of the highest qu
ality, and that they will gather useful information from the user.'),`

`expected_output='A validate the question if que
stions are correct the output it. Always output in json in this format {for}. Remember output should be JSON Always and 
in this format {for} and it should have {num} questions',`

`agent=validation_agent,`

`async_execution=False`

`)`



`
crew = Crew(`

`agents=[questioning_agent, validation_agent],`

`tasks=[questioning_task, validation_task],`

`process=P
rocess.hierarchical,`

`manager_llm = llm,`

`cache=True,`

`)`



`user_input = {`

`'What do you want to learn?': 'MER
N Stack Web dev',`

`'What is your level?': 'beginner',`

`'Do you have any specific goals or outcomes you want to achie
ve by learning?': 'I just wanna learn MERN stack web dev'`

`}`

`number_of_questions = 10`

`result = crew.kickoff(inpu
ts={'sys-prompt':questioning_system_prompt,'val-prompt':validation_system_prompt,'user':user_input,'for':format_p,'num':
number_of_questions})`

`print(result)`



  
**Question**: How can I optimize this setup to reduce the execution time? 
Any tips on improving performance with OpenAI's API or the overall agent management would be greatly appreciated.

Thank
s in advance!
```
---

     
 
all -  [ Good Tutorials For RAG with Structured State and Output?  ](https://www.reddit.com/r/LangChain/comments/1de095x/good_tutorials_for_rag_with_structured_state_and/) , 2024-06-13-0953
```
Hey guys!

So I’ve been looking at a lot of tutorials to build a basic RAG search which does the following:

1. Takes th
e user query and put it into the state “user_query”
2. Searches the internet for results. These results are then populat
ed as text in the state “internet_search_results” field with the url and title of the text
3.  Does the same but searche
s the local database and populates the state “local_search_results” field with the post ID and title of the search resul
ts. 
4. Then passes the state with the information above into a summariser function which uses GPT 3.5 to return structu
red output with the following fields: (i) the text response, (ii) an array of the sources which include the title, the t
ype (web search or local post), and either the url or the post ID. 


I’m at a loss on this as can’t find any good tutor
ials for this. 


```
---

     
 
all -  [ Question regarding limitation of agent use ](https://www.reddit.com/r/LangChain/comments/1ddyhkq/question_regarding_limitation_of_agent_use/) , 2024-06-13-0953
```
I am not a software engineer but an enthusiast of RAG and LLM agents. I wanted to know where is the real bottleneck in b
uilding an agent who would build documents based on chat that I am currently having with an LLM based chat interface and
 embed the chat text using embedding models and store it in vector db for the user to search in later? 
```
---

     
 
all -  [ Production Ready Unstructured Text to Knowledge Graph ](https://www.reddit.com/r/LangChain/comments/1ddvywe/production_ready_unstructured_text_to_knowledge/) , 2024-06-13-0953
```
I'm working on a use case that relies on very robust knowledge graph construction and I wanted to know if any startups/c
ompanies/open-source have built either free or paid production ready solutions for the unstructured text to knowledge gr
aph pipeline.

UPDATE:

Diffbot seems to have a pretty good API that is compatiable with Llama Index and Langchain

this
 tutorial for Llama Index was released the same day I posted this and looks promising: [https://www.llamaindex.ai/blog/c
ustomizing-property-graph-index-in-llamaindex](https://www.llamaindex.ai/blog/customizing-property-graph-index-in-llamai
ndex)​

And Here is one for Langchain [Diffbot | 🦜️🔗 LangChain](https://python.langchain.com/v0.1/docs/integrations/grap
hs/diffbot/)​
```
---

     
 
all -  [ How does this LangChain agent correctly identify the tool to use? ](https://www.reddit.com/r/LangChain/comments/1ddr9hj/how_does_this_langchain_agent_correctly_identify/) , 2024-06-13-0953
```
In this [Medium article](https://medium.com/ama-tech-blog/combining-langchain-and-llamaindex-to-build-your-first-agentic
-rag-system-6e8e2e7825e7), the agent has three tools:

- 'lyft_10k': 'Provides information about Lyft financials for yea
r 2021. '

- 'uber_10k': 'Provides information about Uber financials for year 2021. '

and

- 'DuckDuckGoSearch': 'Use f
or when you need to perform an internet search to find information that another tool can not provide.'

In one of the te
st cases, the author queries the agent

    'List me the names of Uber's board of directors.'

Intuitively, one would as
sume the agent will invoke the 'uber_10k' tool. However, the agent invokes 'DuckDuckGoSearch'.

The author explains that
:
> Since this information is out-of-scope for any of the retriever tools, the agent correctly decided to invoke the ext
ernal search tool.

How does the agent know that question is out-of-scope for the 'uber_10k' retriever?
```
---

     
 
all -  [ Errors loading `langchain_anthropic` ](https://www.reddit.com/r/LangChain/comments/1ddort5/errors_loading_langchain_anthropic/) , 2024-06-13-0953
```
Recently when I try to do `import langchain_anthropic` I have been getting errors like this:
```
>>> import langchain_an
thropic
Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
  File '/usr/local/lib/python3.12/site-
packages/langchain_anthropic/__init__.py', line 1, in <module>
    from langchain_anthropic.chat_models import ChatAnthr
opic, ChatAnthropicMessages
  File '/usr/local/lib/python3.12/site-packages/langchain_anthropic/chat_models.py', line 26
, in <module>
    from langchain_core.callbacks import (
  File '/usr/local/lib/python3.12/site-packages/langchain_core/
callbacks/__init__.py', line 22, in <module>
    from langchain_core.callbacks.manager import (
  File '/usr/local/lib/p
ython3.12/site-packages/langchain_core/callbacks/manager.py', line 29, in <module>
    from langsmith.run_helpers import
 get_run_tree_context
  File '/usr/local/lib/python3.12/site-packages/langsmith/run_helpers.py', line 40, in <module>
  
  from langsmith import client as ls_client
  File '/usr/local/lib/python3.12/site-packages/langsmith/client.py', line 5
2, in <module>
    from langsmith import env as ls_env
  File '/usr/local/lib/python3.12/site-packages/langsmith/env/__i
nit__.py', line 3, in <module>
    from langsmith.env._runtime_env import (
  File '/usr/local/lib/python3.12/site-packa
ges/langsmith/env/_runtime_env.py', line 10, in <module>
    from langsmith.utils import get_docker_compose_command
  Fi
le '/usr/local/lib/python3.12/site-packages/langsmith/utils.py', line 31, in <module>
    from langsmith import schemas 
as ls_schemas
  File '/usr/local/lib/python3.12/site-packages/langsmith/schemas.py', line 69, in <module>
    class Exam
ple(ExampleBase):
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/main.py', line 286, in __new__
    cls.__t
ry_update_forward_refs__()
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/main.py', line 807, in __try_upda
te_forward_refs__
    update_model_forward_refs(cls, cls.__fields__.values(), cls.__config__.json_encoders, localns, (Na
meError,))
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/typing.py', line 554, in update_model_forward_ref
s
    update_field_forward_refs(f, globalns=globalns, localns=localns)
  File '/usr/local/lib/python3.12/site-packages/p
ydantic/v1/typing.py', line 520, in update_field_forward_refs
    field.type_ = evaluate_forwardref(field.type_, globaln
s, localns or None)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File '/usr/local/lib
/python3.12/site-packages/pydantic/v1/typing.py', line 66, in evaluate_forwardref
    return cast(Any, type_)._evaluate(
globalns, localns, set())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: ForwardRef._evaluat
e() missing 1 required keyword-only argument: 'recursive_guard'
>>>
```
That smells like maybe there's an un-captured de
pendency from the `langchain_anthropic` code onto pydantic or something, but I don't have any great ideas about how to d
ebug this.  Anyone else seen this? Any fix or work-around?

Checking, it looks like I have `langchain-anthropic==0.1.13`
 and `langchain==0.1.20` if that helps.
```
---

     
 
all -  [ [Student] Looking for advice on resume and upcoming search, interested in product and software devel ](https://www.reddit.com/r/EngineeringResumes/comments/1ddoopc/student_looking_for_advice_on_resume_and_upcoming/) , 2024-06-13-0953
```
I'm a U.S. citizen and an upcoming senior at Cal State University, getting ready to dive into the job search. Currently 
located in the Bay Area, I attend a Cal-State near a major tech hub, which has provided me with some fantastic opportuni
ties. I've completed internships at a large, albeit controversial especially rn, tech(?) company, and I'm eager to secur
e a full-time position after grad or even a masters degree tbh. As I prepare to start applying, my primary concern is ho
w to increase my chances of getting callbacks since I didn't get as many callbacks as expected for the internship search
--still got multiple offers though. Additionally, I’m looking for advice on how to effectively incorporate another inter
nship experience from the same company into my resume, especially since the work I'm doing there differs from my previou
s role. I'm targeting roles in software engineering, particularly those involving machine learning, AI, and big data ana
lytics. I'm open to both local and remote opportunities and am willing to relocate for the right position.

’m seeking f
eedback on my resume to fine-tune it and make sure it stands out to recruiters. Specifically, I'd appreciate any advice 
on whether my technical skills and experiences are presented effectively and how I can best highlight my projects and in
ternship roles. I feel that it might go over a page tbh. The resumse says May 25 as my grad year, but i'm probably gradu
ating in december 2024. 

https://preview.redd.it/lf38t9on806d1.png?width=5100&format=png&auto=webp&s=89a0912f63dbe8a18d
4198e29893dc4632827472


```
---

     
 
all -  [ Rate my resume and tell me if this is good enough for Data/Business Analyst positions. ](https://i.redd.it/imr71o0t306d1.jpeg) , 2024-06-13-0953
```
Please guide me on what all should be added/removed. Also, can I apply for senior roles? 
```
---

     
 
all -  [ Python Projects ](https://www.reddit.com/r/learnpython/comments/1ddo02e/python_projects/) , 2024-06-13-0953
```
Any suggestions about where I can find some python projects with langchain, flask ?
```
---

     
 
all -  [ Full stack starter ](https://www.reddit.com/r/LangChain/comments/1ddm4a1/full_stack_starter/) , 2024-06-13-0953
```
I’m looking for a chatbot frontend with citations, that utilizes a fast api/langserve backend. Anyone have good suggesti
ons? 
```
---

     
 
all -  [ Newbie question: Langgraph and authenticated tools ](https://www.reddit.com/r/LangChain/comments/1ddl2k0/newbie_question_langgraph_and_authenticated_tools/) , 2024-06-13-0953
```
Hello, as a learning side project I am trying to have a simple Agent that queries an authenticated external API.  Authen
tication is with a standard Bearer token.

I have two tools, one is called fetch\_token that knows how to request a vali
d access token.  And then there is another tool which does the real work and fetches certain value from an external http
s endpoint using the previously retrieved access token.    These are non public APIs and in my tool functions I am using
 'requests' to programatically access and parse the JSON to extract the relevant values back to the Agent.

So given a u
ser's query, the Agent must invoke the first tool, fetch the access token and then invoke the second one passing the tok
en as a parameter.

The thing is working, (yay!!), even when the input of the user makes the agent call the second tool 
repeatedly with different input values (but the same access token).

But my issue is that the agent is terribly slow.  I
 suspect this happens because the bearer token (a quite long and random string, it is 2330 hexadecimal chars) is being p
assed each time to the LLM (OpenAI, 'gpt4-turbo-preview') and that takes a lot of context and processing for the LLM, wh
ich perhaps only be concerned with the fact that the access token is already present, not its value.

So I was thinking 
of storing the token in the Agent state, but I am not aware of a way that the output of a tool can be stored in the Agen
t state, and I also suspect that the whole Agent state is what is already being sent to the LLM so this would not defeat
 the purpose of this hoop.

So I am at a loss, my Agent is roughly working but is very slow!   Are there any suggestions
, resources or examples for this patterns?
```
---

     
 
all -  [ Chroma DB taking extremely long time to create. ](https://www.reddit.com/r/LangChain/comments/1ddk9b1/chroma_db_taking_extremely_long_time_to_create/) , 2024-06-13-0953
```
So this is my first time ever hearing about vector databases - I know very little about them and I'm running into some t
rouble with a simple rag script I threw together.

I followed one of langchain's documentation tutorials and was able to
 get a basic RAG setup going with some text files. Well now I'm trying to expand on it to be something useful - so I cur
rently have \~800 documents totaling to just under 50 MB of data that I want to store in the vector DB. For some reason,
 the \`Chroma.from\_documents()\` method will hang for a very long period of time (been running for over 10 minutes now)
 - and I can't seem to figure out why it's so slow.

Firstly, this \`Chroma.from\_documents\` method - is what its doing
 called 'indexing'? I keep seeing this term thrown around, not entirely sure what it means.

Second, Is it normal for cr
eating the vector store to take this long with the amount of data I have? I figured 50MB of data and only 800 documents 
would be pretty trivial, as I've seen other posts about people having millions of documents.

Any help would be apprecia
ted.

For reference, here is the relevant code:

    loader = DirectoryLoader('docs2', glob='**/*.htm', loader_cls=BSHTM
LLoader, loader_kwargs={'open_encoding': 'utf8'}, show_progress=True, use_multithreading=True)
    
    docs = loader.lo
ad()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    splits = text_splitter.split_documents
(docs)
    
    model = 'Alibaba-NLP/gte-large-en-v1.5'
    model_kwargs = model_kwargs = {'device':'cpu', 'trust_remote
_code': True}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceEmbeddings(
        model_n
ame=model,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    vectorstore = Chroma.fr
om_documents(documents=splits, embedding=embeddings)
```
---

     
 
all -  [ rerank-ts: TypeScript Library for Improving Search Results in RAG Applications  ](https://www.reddit.com/r/LangChain/comments/1ddhd9t/rerankts_typescript_library_for_improving_search/) , 2024-06-13-0953
```
Hi folks, we built a TypeScript library to improve search results in RAG Applications. If you are building a RAG applica
tion on top of vector indexes, re-ranking search results will always improve LLM's  response synthesis. We implemented t
wo commonly used re-ranking techniques - Reciprocal Rank Fusion(RRF) and LLM Based Re-Ranking(using Llama3 from Groq and
 GPT-4). Hope this is useful to folks building LLM Applications in React/NextJS.

Code - https://github.com/tensorlakeai
/rerank-ts 

We were building a consumer application with our open source data framework https://github.com/tensorlakeai
/indexify and were not able to find a good re-ranking library in TypeScript. So we decided to build one, and it works re
ally well to re-rank ~100 results. We get latency of around 1 second with Llama3/Groq. 

```
---

     
 
all -  [ Is there a way to add multisteps/continuation in langgraph? ](https://www.reddit.com/r/LangChain/comments/1ddg11m/is_there_a_way_to_add_multistepscontinuation_in/) , 2024-06-13-0953
```
Is there a way to implement multistep operations in LangGraph? Specifically, I'm looking to perform a series of modifica
tions where one step directly influences the next. For instance, I want to first remove the background of an image in th
e initial node, and then, in a subsequent node, use another tool to search for and replace an object. The key requiremen
t is that the second modification should be applied to the modified image from the first step, not the original image. C
an LangGraph handle this type of sequential image processing?

- I have checked langgraph documentation and found no rel
evant information
- I have tried changing and updating the way I have written the prompt to see if it affects

Any help 
is greatly appreciated :))
```
---

     
 
all -  [ Calculating LLM costs before sending requests? ](https://www.reddit.com/r/LangChain/comments/1ddft47/calculating_llm_costs_before_sending_requests/) , 2024-06-13-0953
```
Using langchain sometimes feels like gambling with costs to me. I never really know how much my requests would actually 
cost when I send it. I know there are detailed charts which we should read, but who really does? Instead I wanted to ask
 if anybody knows of an automated way to calculate costs before sending the requests? For my use case, specifically for 
OpenAI, but maybe there is another way.

And if there isnt anything like that, maybe this would be an interessting proje
ct... Like a package which calculates your LLM costs before the requests, depending on the specific platform you use
```
---

     
 
all -  [ Chainlit translation in a rag system  ](https://www.reddit.com/r/LangChain/comments/1ddfqps/chainlit_translation_in_a_rag_system/) , 2024-06-13-0953
```
I use chainlit as UI in my rag system, the first qst passes ok, but when i inser the second one it translated automaticl
y to english.
So How to strictly change translation for all users to a specific language? File xx-XX.json is placed in t
he translations folder. Deletion of en-US.json  doesn't work (it is generated each time again) 
```
---

     
 
all -  [ How to deal with this collaboration  ](https://www.reddit.com/r/SaaS/comments/1ddfn99/how_to_deal_with_this_collaboration/) , 2024-06-13-0953
```
So I contacted a company who owns a content API for travel holidays and asked them if they could allow access for me to 
build AI solutions on top it. 

Long story short, 3 months down the line I have used their API to create my own infrastr
ucture of Elasticsearch, GraohQL, Langchain and other vector dbs etc to create a chatbot with long term memory and high 
precision in getting travel packages, combined with a UI and UX custom designed. 

Now my chatbot is dependent on their 
or any other similar company's API to be able tp answer questions of customers and make recommendations. 

The current d
iscussion with the owner of this API provider is that they are willing to offer me the certain share of revenues as they
'd handle the market, sales and distribution of this chatbot any all parallel AI apps APIs I'd build. Which seems like a
 sweet deal, but silly me has not formally brought up the topic about the terms of the partnership until recently. 

The
y have put a condition that they want to host it pn their own cloud so they can launch it as rheir product and manage th
e scale etc. 

My worry is, I am giving away my IPR which if I ask myself honestly is an AI wrapper, yes but I have put 
my thinking into making it accurate. 


How do I tackle this situation? Anyone else did similar parternerships? 

TLDR; 
Need advive on how to go about my SaaS where a crucial API for content is owner but another company and they want to hos
t the SaaS on their cloud. 
```
---

     
 
all -  [ Multiple ways to get to the same result w/ RAG ](https://www.reddit.com/r/LangChain/comments/1dddjew/multiple_ways_to_get_to_the_same_result_w_rag/) , 2024-06-13-0953
```
So, I'm building this simple rag pipeline with langchain and ollama that takes in a PDF document and returns it's summar
y as bulletpoints.

    file_path = 'paper.pdf'
    loader = PyPDFLoader(file_path)
    
    docs = loader.load()
    
 
   embeddings = (OllamaEmbeddings(model='llama3'))
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10
00, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(document
s=splits, embedding=embeddings, persist_directory='emb')
    
    retriever = as_retriever(
        embeddings=embedding
s,
        chroma=vectorstore
    )
    
    prompt_template = '''Based on the following information and being really sp
ecific about it's data: '{text}'.\n\n Here are the goals, methodology, and conclusions/achievements of the paper, writte
n as bullet points:'''
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    llm = Ollama(model='llam
a3')
    
    chain = (
        retriever
        | prompt
        | llm
    )
    
    result = chain.invoke({})

 The 
calling of the chain just seems too much like a workaround, since I didn't have a specific question about the reference 
document, therefore I just had to use the prompt\_template as the instruction to treat the pdf. It just seems like there
 are a lot of way to get to this same result. Whether to call the llm by it's default completion object or through it's 
chat variation. Whether to use a LLMChain(), a RetrievalQA.from\_chain\_type() or a simple chain() specifying it's commo
n parameters etc. Ins't there a way to standardize this workflow according to your needs?
```
---

     
 
all -  [ Deploying Langserve in ECS with CDK ](https://www.reddit.com/r/LangChain/comments/1ddb6qz/deploying_langserve_in_ecs_with_cdk/) , 2024-06-13-0953
```
Hi guys I was struggling for quite sometime on how to host Langserve in AWS ECS. So prepared this two repos

1st one cre
ates a VPC  [https://github.com/mathlover777/shared-vpc](https://github.com/mathlover777/shared-vpc)

2nd one deploys in
 the same VPC [https://github.com/mathlover777/langserve-cdk-ecs](https://github.com/mathlover777/langserve-cdk-ecs)

Yo
u can deployment multiple stages in the same VPC also as AWS has a soft limit on number of VPCs.

  
This does not have 
autoscale added, as I dont know how to do it myself in ecs, will update when I get time.
```
---

     
 
all -  [ Best way forward and vector db for an AI RAG system for CVs ranking using query and some metadata  ](https://www.reddit.com/r/LangChain/comments/1dd8ssq/best_way_forward_and_vector_db_for_an_ai_rag/) , 2024-06-13-0953
```
Hi guys, 
I'm working on this project where initially we have 700 csvs to be ingested and build a poc with some ui for q
uerying the csvs database with text and and metadata parameters selected via ui.


Need opinions fro experts on how to a
pproach this project, considering the production use and ingesting more cvs into ai system. 

For initial POC, I'm plann
ing to use chromadb and streamlit for UI. Better options?

I can build above RAG, but I'm asking for expert opinions kee
ping in mind the production use case and scaling to more pdfs 
```
---

     
 
all -  [ How do i parse a call to multiple tools ](https://www.reddit.com/r/LangChain/comments/1dd6poy/how_do_i_parse_a_call_to_multiple_tools/) , 2024-06-13-0953
```
When a single tool is to be used this is the output I get from Llama3 is:{'arguments': {}, 'name': 'check\_location'}

T
he logic I'm using to parse a single tool call is this:

    from operator import itemgetter
    
    
    def tool_chai
n(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool = tool_map[model_output['nam
e']]
        return itemgetter('arguments') | chosen_tool

How do i modify this for a call to multiple tools. The output
 from Llama3 is:{'tools': \[{'arguments': {}, 'name': 'check\_location'},  
{'arguments': {}, 'name': 'check\_calendar'}
\]}

I'm using Llama3, ollama and LangGraph.





Edit: I've managed to get an output like this:

'Finished running: gra
der:'  
{'tool1': {'arguments': {}, 'name': 'check\_location'},  
'tool2': {'arguments': {}, 'name': 'check\_calendar'}}


How do i parse the above?
```
---

     
 
all -  [ Can I use LangChain with Indian opensource LLMs? ](https://www.reddit.com/r/LangChain/comments/1dd6poq/can_i_use_langchain_with_indian_opensource_llms/) , 2024-06-13-0953
```
I am a beginner so this might be a pretty basic question. I wanted to know if I can use LangChain framework with LLMs ot
her than openai's GPT. My use case is related to regional languages in India so I was going to use **BharatGPT by** [**C
oRover.ai**](http://CoRover.ai) or **AI4Bharat** an opensource AI model?
```
---

     
 
all -  [ What vector db should I choose for 100m pages of text? ](https://www.reddit.com/r/LangChain/comments/1dcyc6i/what_vector_db_should_i_choose_for_100m_pages_of/) , 2024-06-13-0953
```
For context my vector db research started today from 0 knowledge and I feel absolutely unqualified to be making this dec
ision but here we are.

I have narrowed the search down to Milvus, Qdrant and potentially Weaviate.

I am scoping out a 
project for a client where we need to store up to 100 million pages. The application is scientific so retrieval precisio
n is a top priority as is search time latency and cost.

It seems:

* Milvus seems the most established and easiest to s
etup. also itis fast but takes up a lot of memory so can get quite expensive.
* Qdrant is fast and quite a bit cheaper t
han Milvus but lacks dynamic sharding 
* I have seen two conflicting reports one saying Weaviate is incredibly quick wit
h a benchmark of 0.12s for a particular query which took Milvus 0.9s to perform the same and then another where it says 
it is slow. and it is the cheapest.
* PG-vector is not as performant as the dedicated vector stores but are tried and te
sted part of the ecosystem and anecdotally great to work with 
* Chroma is not the best for accurate retrieval and I hav
en't heard many recommending it as the best except for its usability and ease of integration. 


```
---

     
 
all -  [ How to handle ambiguous column names when converting Text-to-SQL in SQL Agent? ](https://www.reddit.com/r/LangChain/comments/1dcvnzv/how_to_handle_ambiguous_column_names_when/) , 2024-06-13-0953
```
**I have 2 cases of ambiguity** 

1. Similar names within a table - Eg: constrained\_demand, unconstrained\_demand

2.  
Same names across different tables. - Sales in both table1 and table 2

I have built a chatbot using open-ai tools agent
s , giving it access to SQLDatabaseToolKit. There is prefix, suffix and FewShotPrompt Template to handle multiple differ
ent calculations and complexities of SQL queries. Now user can ask multiple queries of the below format .

**Examples:**


1. What is the demand for 2024? - there is ambiguity as to if the user is asking constrained demand or unconstrained d
emand. Assumption that is no 'demand' column . Expectation - LLM should figure out such ambiguity without any hardcoding
 and then ask back the user as to which column he is referring to. Once LLM gets user input, then query with the new inf
o.

2. What is the sales for brand1?  there is ambiguity as to if the user is asking sales from table1 or table2. Expect
ation - LLM should figure out such ambiguity without any hardcoding and then ask back the user as to which table he is r
eferring to. Once LLM gets user input, then query with the new info.

  
Cannot handle this in column description as eve
n if the descriptions are different, we cannot make sense from the question. Need help in how to approach this. TIA!
```
---

     
 
all -  [ What are you studying, courses are you taken, personal project are you working on to keep up with th ](https://www.reddit.com/r/datascience/comments/1dcudnn/what_are_you_studying_courses_are_you_taken/) , 2024-06-13-0953
```
If you are working with classic ML and basic statistics in your current job, and new jobs require knowledge of LLMs and 
RAG based system with knowledge in langchain and prompt engineering, How can I land a job then?
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-13-0953
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-13-0953
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-13-0953
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
