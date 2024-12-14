 
all -  [ [Student] Non-Target CS Student looking for Summer 2025 Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hdpaec/student_nontarget_cs_student_looking_for_summer/) , 2024-12-14-0913
```
[I am having little luck with applying to Summer 2025 internships related to software engineering, and I've currently ap
plied to around 400 places. I know the market is pretty bad right now, but just wanted to make sure my resume was optima
l for getting me interviews, cause right now I have gotten mostly nothing from online applications \(Had an interview fr
om my school's career fair\). Any advice would be greatly appreciated.](https://preview.redd.it/qnc9d2sc7p6e1.png?width=
5100&format=png&auto=webp&s=68f0c23f6576eb216c1f4c5fdc6190e2aa9dba60)


```
---

     
 
all -  [ Modularizing AI workflows in production ](https://www.reddit.com/r/LangChain/comments/1hdm37i/modularizing_ai_workflows_in_production/) , 2024-12-14-0913
```
Wanted to share some challenges and solutions we discovered while working with complex prompt chains in production. We s
tarted hitting some pain points as our prompt chains grew more sophisticated:

* Keeping track of prompt versions across
 different chain configurations became a nightmare
* Testing different prompt variations meant lots of manual copying an
d pasting. Especially when tracking the performances.
* Deploying updated chains to production was tedious and error-pro
ne. Environment variables was fine at first until the list of prompts start to grow.
* Collaborating on prompt engineeri
ng with the team led to version conflicts.
   * We started with code verisoning it, but it was hard to loop in other sta
keholders (ex: product managers, domain experts) to do code reviews on GitHub. Notion doesn’t have a good versioning sys
tem built-in so everyone was kind of afraid to overwrite the other person’s work and ended up putting a lot of comments 
all over the place.

We ended up building a simple UI-based solution that helps us:

1. Visualize the entire prompt chai
n flow
2. Track different versions of the workflow and make them replayable.
3. Deploy the workflows as separate service
 endpoints in order to manage them programmatically in code

The biggest learning was that treating chained prompts like
 we treat workflows (with proper versioning and replayability) made a huge difference in our development speed.

Here’s 
a high-level diagram of how we modularize AI workflows from the rest of the services

https://preview.redd.it/4cwpce4uio
6e1.png?width=1612&format=png&auto=webp&s=a290f010d8605bec3e1825603e87665366e802c2

We’ve made our tool available at [ww
w.bighummingbird.com](http://www.bighummingbird.com/) if anyone wants to try it, but I’m also curious to hear how others
 are handling these challenges? :)
```
---

     
 
all -  [ Avoid sending messages at the same time ](https://www.reddit.com/r/LangChain/comments/1hdlx5e/avoid_sending_messages_at_the_same_time/) , 2024-12-14-0913
```
Hi,  
I have a graph on langgraph wrapped around a FastAPI project.  
I want to avoid sending two messages at the same t
ime to the same chat\_id through the API.  
Is there any way I can know when a thread is processing a message before sen
ding a new one?  
Thanks in advance!
```
---

     
 
all -  [ why my agent is not calling the tools  help me to fix this .. ](https://www.reddit.com/r/node/comments/1hdllox/why_my_agent_is_not_calling_the_tools_help_me_to/) , 2024-12-14-0913
```
mport dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod'
;  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/c
ore/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResults
 } from '@langchain/community/tools/tavily\_search';

const llm = new ChatGoogleGenerativeAI({  
apiKey: process.env.GEM
INI,  
model: 'gemini-1.5-flash',  
});

const search = new TavilySearchResults({  
apiKey: process.env.TAVILY,  
maxRes
ults: 2,  
});

*// Improved magicTool: Now actually uses the input*  
const magicTool = tool(  
async (input) => {  
*/
/Simulate fetching company name - replace this with actual API call if needed.*

return 'The company name is Acme Corpor
ation.';  
},  
{  
name: 'business\_info',  
description:  
'This tool provides business information like name, locatio
n, etc. Ask specific questions.',  
}  
);

const tools = \[magicTool\];

const prompt = ChatPromptTemplate.fromMessages
(\[  
\[  
'system',  
'You are a helpful assistant that answers the following questions as best you can. You have acces
s to the following tools:',  
\],  
\['placeholder', '{chat\_history}'\],  
\['human', '{input}'\],  
\['placeholder', '
{agent\_scratchpad}'\],  
\]);

const agent = createToolCallingAgent({  
llm,  
tools,  
prompt,  
});

const agentexe =
 new AgentExecutor({  
agent,  
tools,  
verbose: true,  
});

const res = await agentexe.invoke({ input: 'what is the c
ompany name?' });  
console.log(res);
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  .. ](https://www.reddit.com/r/LangChain/comments/1hdksj8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-14-0913
```
import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: process.
env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
const search = new TavilySearchResults({  
  apiKey: process.env.T
AVILY,  
  maxResults: 2,  
});  
  
*// Improved magicTool:  Now actually uses the input*  
const magicTool = tool(  
 
 async (input) => {  
*//Simulate fetching company name - replace this with actual API call if needed.*  
  
return 'The
 company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides busines
s information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
const tools = \[magicTool\];  
  
con
st prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answers the follow
ing questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{chat\_history}'\
],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
const agent = createToolCalling
Agent({  
  llm,  
  tools,  
  prompt,  
});  
  
const agentexe = new AgentExecutor({  
  agent,  
  tools,  
  verbos
e: true,  
});  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.log(res);  
  

import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: proce
ss.env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
  
const search = new TavilySearchResults({  
  apiKey: process
.env.TAVILY,  
  maxResults: 2,  
});  
  
  
// Improved magicTool:  Now actually uses the input  
const magicTool = to
ol(  
  async (input) => {  
//Simulate fetching company name - replace this with actual API call if needed.  
  
  
ret
urn 'The company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides
 business information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
  
const tools = \[magicTool\
];  
  
  
const prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answ
ers the following questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{ch
at\_history}'\],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
  
const agent = 
createToolCallingAgent({  
  llm,  
  tools,  
  prompt,  
});  
  
{  
  input: 'what is the company name?',  
  output
: 'I need more information to answer your question.  The available tools don't contain any information about a specific 
company.  Can you provide more context or details?\\n'  
}  
const agentexe = new AgentExecutor({  
  agent,  
  tools, 
 
  verbose: true,  
});  
  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.lo
g(res);  
  
the output is  ::   
 {  
  input: 'what is the company name?',  
  output: 'I need more information to ans
wer your question.  The available tools don't contain any information about a specific company.  Can you provide more co
ntext or details?\\n'  
}
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  ,  ](https://www.reddit.com/r/Bard/comments/1hdkqi8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-14-0913
```
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
    import { z }
 from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromptTemplate } fro
m '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';
    import { 
TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    const llm = new ChatGoogleGenerativeAI({

      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    const search = new TavilySearchResu
lts({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    // Improved magicTool:  Now actually uses 
the input
    const magicTool = tool(
      async (input) => {
        
    //Simulate fetching company name - replace t
his with actual API call if needed.
    
        return 'The company name is Acme Corporation.';
      },
      {
      
  name: 'business_info',
        description:
          'This tool provides business information like name, location, et
c.  Ask specific questions.',
      }
    );
    
    const tools = [magicTool];
    
    const prompt = ChatPromptTempl
ate.fromMessages([
      [
        'system',
        'You are a helpful assistant that answers the following questions a
s best you can. You have access to the following tools:',
      ],
      ['placeholder', '{chat_history}'],
      ['huma
n', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    const agent = createToolCallingAgent({
   
   llm,
      tools,
      prompt,
    });
    
    const agentexe = new AgentExecutor({
      agent,
      tools,
     
 verbose: true,
    });
    
    const res = await agentexe.invoke({ input: 'what is the company name?' });
    console.
log(res);
    
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
 
   import { z } from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromp
tTemplate } from '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents'
;
    import { TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    
    const llm = new Chat
GoogleGenerativeAI({
      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    
    const sear
ch = new TavilySearchResults({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    
    // Improved 
magicTool:  Now actually uses the input
    const magicTool = tool(
      async (input) => {
        //Simulate fetching
 company name - replace this with actual API call if needed.
    
    
        return 'The company name is Acme Corporat
ion.';
      },
      {
        name: 'business_info',
        description:
          'This tool provides business infor
mation like name, location, etc.  Ask specific questions.',
      }
    );
    
    
    const tools = [magicTool];
    

    
    const prompt = ChatPromptTemplate.fromMessages([
      [
        'system',
        'You are a helpful assistan
t that answers the following questions as best you can. You have access to the following tools:',
      ],
      ['place
holder', '{chat_history}'],
      ['human', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    
 
   const agent = createToolCallingAgent({
      llm,
      tools,
      prompt,
    });
    
    {
      input: 'what is
 the company name?',
      output: 'I need more information to answer your question.  The available tools don't contain 
any information about a specific company.  Can you provide more context or details?\n'
    }
    const agentexe = new Ag
entExecutor({
      agent,
      tools,
      verbose: true,
    });
    
    
    const res = await agentexe.invoke({ i
nput: 'what is the company name?' });
    console.log(res);
    
    the output is  :: 
     {
      input: 'what is the
 company name?',
      output: 'I need more information to answer your question.  The available tools don't contain any 
information about a specific company.  Can you provide more context or details?\n'
    }
```
---

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1hdjv70/advance_your_career_100_free_certified_courses_on/) , 2024-12-14-0913
```
Visualization techniques for Decision Makers and Leaders

https://courze.org/visualization-techniques-for-decision-maker
s-and-leaders/



300+ JavaScript Interview Questions – Practice Tests

https://courze.org/300-javascript-interview-ques
tions-practice-tests/



300+ Python Interview Questions – Practice Tests

https://courze.org/300-python-interview-quest
ions-practice-tests/



Scrum Master Certification

https://courze.org/scrum-master-certification-4/



Business Analysi
s

https://courze.org/business-analysis/



C Corporation Income Tax (Form 1120)

https://courze.org/c-corporation-incom
e-tax-form-1120/



Zero to Hero in LangChain: Build GenAI apps using LangChain

https://courze.org/zero-to-hero-in-lang
chain-build-genai-apps-using-langchain/



Blogger: Make A Professional Website For Free With No Coding

https://courze.
org/blogger-make-a-professional-website-for-free-with-no-coding/



Solving LeetCode’s Top Interview Questions in Java \
[2024\]

https://courze.org/solving-leetcodes-top-interview-questions-in-java/



4 Comprehensive Practice Tests for any
 Python Certification

https://courze.org/4-comprehensive-practice-tests-for-any-python-certification/



Excel Certific
ation Exam Preparation: 4 Practice Tests 2024

https://courze.org/excel-certification-exam-preparation-4-practice-tests-
2024-3/



4 MS Excel Certification Practice Test & Interview Question

https://courze.org/4-ms-excel-certification-prac
tice-test-interview-question/



CHRO Chief Human Resources Officer Executive Certification

https://courze.org/chro-chi
ef-human-resources-officer-executive-certification/



Prioritization Techniques for Decision Makers and Leaders

https:
//courze.org/prioritization-techniques-for-decision-makers-and-leaders/



The Complete Matlab Course for Wireless Comm.
 Engineering

https://courze.org/the-complete-matlab-course-for-wireless-comm-engineering/



Currency Management for Sm
all Businesses & Corporates

https://courze.org/currency-management-for-small-businesses-corporates/



Statistics & Exc
el

https://courze.org/statistics-excel/



Prompt & AI Engineering Safety Professional Certification

https://courze.or
g/prompt-engineering-safety-ai-engineering-safety-expert/



ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT


https://courze.org/chatgpt-prompt-engineering-guide-make-money-using-chatgpt/



AI Course Creation Guide: Creating an 
Online Course Using AI

https://courze.org/ai-course-creation-guide-creating-an-online-course-using-ai/



Advanced Skil
l Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-2
/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-profession
al-level-1-pcpp1-7/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test
-python-professional-level-1-pcpp1-9/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/a
dvanced-skill-test-python-professional-level-1-pcpp1-10/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

h
ttps://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-12/



Advanced Skill Test: Python Professional 
Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-15/



7 steps to entrepreneu
rship: A complete business plan (PRO)

https://courze.org/7-steps-to-entrepreneurship-a-complete-business-plan-pro/



A
utoCAD 2D & Isometric | AutoCAD Civil & Architectural

https://courze.org/autocad-2d-isometric-autocad-civil-architectur
al/



Microsoft Power BI for Beginners & Excel Users

https://courze.org/microsoft-power-bi-for-beginners-excel-users/




CMO Chief Marketing Officer Executive Certification

https://courze.org/cmo-chief-marketing-officer-executive-certifi
cation/



Transform Your Life in 5 Days: I Challenge You to Fail

https://courze.org/transform-your-life-in-5-days-i-ch
allenge-you-to-fail/



Mastering Power BI Report Design – Beginner to Advanced

https://courze.org/mastering-power-bi-r
eport-design-beginner-to-advanced/



Practical Machine Learning for Data Scientists

https://courze.org/practical-machi
ne-learning-for-data-scientists/



Generative AI: Learn about the next AI frontier

https://courze.org/generative-ai-le
arn-about-the-next-ai-frontier/



Master LCD Interfacing with Arduino: From Basics to Projects

https://courze.org/mast
er-lcd-interfacing-with-arduino-from-basics-to-projects/



Deployment of Machine Learning Models

https://courze.org/de
ployment-of-machine-learning-models/



Reinforcement Learning

https://courze.org/reinforcement-learning/



Deep Learn
ing for Computer Vision

https://courze.org/deep-learning-for-computer-vision/



Deep Learning for Natural Language Pro
cessing

https://courze.org/deep-learning-for-natural-language-processing/



Oracle Java Certification Exam OCA 1Z0-808
 Preparation Part1

https://courze.org/oracle-java-certification-exam-oca-1z0-808-preparation-part1/




```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison
 ](https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/) , 2024-12-14-0913
```

```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison
 ](https://www.reddit.com/r/OpenSourceeAI/comments/1hdgunu/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-14-0913
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility

Blog Link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](http
s://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stick
 with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into 
performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ Langgraph Persistence memory: InvalidSqlStatementName ](https://www.reddit.com/r/LangChain/comments/1hdbvre/langgraph_persistence_memory/) , 2024-12-14-0913
```
    async def run_graph(user_input: str, thread_id: str):
        with AsyncConnection.connect(os.getenv('DB_URI'), **co
nnection_kwargs) as conn:
            checkpointer = AsyncPostgresSaver(conn)
            await checkpointer.setup()
   
         graph = workflow.compile(checkpointer=checkpointer)
            config = {'configurable': {'thread_id': thread_
id}}
            async for event in graph.astream_events(
                {'messages': [HumanMessage(content=user_input)
]},
                version = 'v2', stream_mode='values', config=config
            ):
                if 'on_chat_model
_stream' == event['event']:
                    if len(event['data']['chunk'].content) > 0:
                        prin
t(event['data']['chunk'].content, end='', flush=True)
    
    if __name__ == '__main__':
        print('Running model')

        asyncio.run(run_graph(user_input='How are you?', thread_id='testing5'))

`DB_URI= postgresql://USER:PASSWORD@aw
s-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=disable`

I am using above code for `react-agent` with `memor
y`. Without `memory`, agent is working fine but when I add memory to it then sometime it gives me this error and sometim
e it works fine. I am not sure what could be wrong.

`psycopg.errors.InvalidSqlStatementName: prepared statement '_pg3_1
4' does not exist`
```
---

     
 
all -  [ A Personalized Academic Companion - AI Agent ](https://open.substack.com/pub/diamantai/p/atlas-when-artificial-intelligence?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) , 2024-12-14-0913
```
During the hackathon I ran with LangChain, a team of developers created ATLAS—a system of AI agents designed to help stu
dents tackle the overwhelming challenges of modern education. From optimizing study schedules to tailoring learning reso
urces, ATLAS provides personalized support to make studying more effective and less stressful.

I shared the full story,
 along with insights into how it works, in the blog attached (including also a link to the full code tutorial + YouTube 
pitch video)

Curious to hear your thoughts :)
```
---

     
 
all -  [ How to extract Title/Heading/Chapter Name from the PDF ](https://www.reddit.com/r/LangChain/comments/1hdbeeo/how_to_extract_titleheadingchapter_name_from_the/) , 2024-12-14-0913
```
I am working on a RAG Pipeline, in which I am extracting PDF and store in the mongo. When I perform a query, it responds
 with a specific answer. Now I want to add Page Number and Title OR Chapter name OR heading of the title in the response
.

I am trying to fetch but it is not that much accurate. Anyone having a good approach ?
```
---

     
 
all -  [ What is best practice for follow-up questions? ](https://www.reddit.com/r/Rag/comments/1hdaf2y/what_is_best_practice_for_followup_questions/) , 2024-12-14-0913
```
I am implementing Ai agent, and feeding it with some scraped data, i am using Langchain alongside with express.js, from 
your experience what is low cost and effective solution to handle follow up questions in rag? I read langchain docs but 
they are suggesting to make another LLM call which may be costly, is there any appropriate practice for it which really 
works, please share your experience, any material or web resource will be appreciated 
```
---

     
 
all -  [ Qdrant DB Retriever issue ](https://www.reddit.com/r/LangChain/comments/1hd9oz8/qdrant_db_retriever_issue/) , 2024-12-14-0913
```
Previously I have used Chroma DB now I wold like to use Qdrant db

I have uploaded my docs to qdrant db using qdrant cli
ent through langchain framework, created a collection name and assigned hugging face embedding model now now I’m not abl
e to retrieve the query using .query method which was previously used in chroma DB I would like to know different modes 
of search’s supported by qdrantvectorstore

can any one guide me or share any links 
```
---

     
 
all -  [ How to return tool output directly without sending it to LLM again from a Langgraph Agent ? ](https://www.reddit.com/r/LangChain/comments/1hd9cc4/how_to_return_tool_output_directly_without/) , 2024-12-14-0913
```
A typical ReAct loop follows user -> assistant -> tool -> assistant ..., -> user. In some cases, you don't need to call 
the LLM after the tool completes, the user can view the results directly themselves.

I am currently developing a Langgr
aph Agent ( this [https://langchain-ai.github.io/langgraph/#example](https://langchain-ai.github.io/langgraph/#example) 
is the base ) .

For my agent , I have 2 tools for calling 2 apis.  
  
Results from these 2 tool calls can be large...v
ery large some times depending on the user query.

I want that the tool outputs ( i.e. the api response ) instead of goi
ng back to the agent , it should be returned directly to the user.

I found a Langchain JS reference for this ( [https:/
/langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/](https://langchain-ai.github.io/langgraphjs/
how-tos/dynamically-returning-directly/) ) but I'm developing using Python. Can anyone guide me how to directly return t
he tool outputs to the user ?

My app is a streamlit app. Thanks!
```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison
 ](https://www.reddit.com/r/OpenAI/comments/1hd6x21/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-14-0913
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility.

Blog link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](htt
ps://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stic
k with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into
 performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison ](https://www.reddit.com/r/LangChain/comments/1hd6w5x/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-14-0913
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility

Blog Link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](http
s://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stick
 with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into 
performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ AI Companion ](https://www.reddit.com/r/LangChain/comments/1hd6fo6/ai_companion/) , 2024-12-14-0913
```
We trying to develop a bot for people to talk when feeling lonely. I came by such a bot which is already very popular na
med Replica. Is there any other such bots which are already in use? Anyone knows which latest LLM Replica is using in th
e backend?
```
---

     
 
all -  [ My ideal development wishlist for building AI apps ](https://www.reddit.com/r/LangChain/comments/1hd62k6/my_ideal_development_wishlist_for_building_ai_apps/) , 2024-12-14-0913
```
As I reflect on what I’m building now and what I have built over the last 2 years I often go back to this list I made a 
few months ago.  

Wondering if anyone else relates 


It’s straight copy/paste from my notion page but felt worth shari
ng 


- I want an easier way to integrate AI into my app from what everyone is putting out on jupyter notebooks
    - no
tebooks are great but there is so much overhead in trying out all these new techniques. I wish there was better tooling 
to integrate it into an app at some point. 
- I want some pre-bundled options and kits to get me going
- I want SOME con
trol over the AI server I’m running with hooks into other custom systems.
- I don’t want a Low/no Code solution, I want 
to have control of the code
- I want an Open Source tool that works with other open source software. No vendor lock in
-
 I want to share my AI code easily so that other application devs can test out my changes. 
- I want to be able to run e
valuations and other LLMOps features directly
    - evaluations
    - lifecycle
    - traces
- I want to deploy this eas
ily and work with my deployment strategies
- I want to switch out AI techniques easily so as new ones come out, I can se
e the benefit right away
- I want to have an ecosystem of easy AI plugins I can use and can hook onto my existing server
. Can be quality of life, features, stand-alone applications 
- I want a runtime that can handle most of the boilerplate
 of running a server. 
```
---

     
 
all -  [ Aider + langchain: A match made in heaven? ](https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider_langchain_a_match_made_in_heaven/) , 2024-12-14-0913
```
 🚀

Hey everyone! In the spirit of r/localllama, I wanted to share a little experiment I’ve been working on: [RA.Aid](ht
tps://github.com/ai-christianson/RA.Aid). This started after Windsurf announced their pricing changes, and I kept runnin
g into its limits—usage caps, unreliability, and cost. I thought, why not try building something together that combines 
the best parts of aider and LangChain to handle programming tasks more effectively?

RA.Aid is an experiment to make aid
er a tool for a LangChain agent. The agent explores your codebase, finds key facts, files, and snippets for your task, a
nd can even ask tough questions using o1-preview. It’s been exciting to see how well it works with tools like:  
- **Fil
e exploration tools** for navigating projects.  
- **Fuzzy find + ripgrep** for quickly locating key snippets.  
- An op
tional **cowboy 🤠 mode** that lets the agent automatically run shell commands (if you’re feeling adventurous).  

So far
, it has been performing better for the tasks I’ve tested it on, especially complex ones. Right now, it’s set up with so
me of the strongest models available (like Claude and o1-preview). However, it should work well with open models too, th
ough we’ll probably need to do more prompting work and add configurability to make it really effective.  

If we can get
 some PRs rolling in, we might be able to create a completely free and open tool that far surpasses even $500/month prop
rietary solutions like Devin. The code is up on GitHub under Apache 2.0: [RA.Aid](https://github.com/ai-christianson/RA.
Aid).

Happy to hear any thoughts or feedback from the community!
```
---

     
 
all -  [ Token limit challenge with large tool/function calling response ](https://www.reddit.com/r/LangChain/comments/1hcwrzk/token_limit_challenge_with_large_toolfunction/) , 2024-12-14-0913
```
Hi everyone, 

  
I'm currently building application with function calling using langchain/langgraph. Tool calling funct
ionality works well in general but some of my tools make call to 3rd party search API, which often return huge JSON resp
onse body. In the scenario when multiple search requests needs to be called, and all tool calling search responses need 
to pass to invoke AI model to generate AI response, I quickly run into token limit for AI model. Does anyone has any exp
erience with handling huge tool calling response and has some solution that can optimize? 

  
I have considered few way
s 

(1) In tool calling, after getting response from 3rd party search API, before returning back to my main agent, I cal
l AI model to summary my search API response. However, this results into loss of information from the original search re
sponse which eventually leads to poor final AI response

(2) In tool calling, after getting response from 3rd party sear
ch API, transform the response into documents, save it as embedding and search for the most relevant document, return to
 the main agent. However, this search within search sounds really inefficient consider search API might already return r
esults with high relevance? 
```
---

     
 
all -  [  CommanderAI / LLM-Driven Action Generation on Windows with Langchain (openai) ](https://www.reddit.com/r/OpenAIDev/comments/1hcwok1/commanderai_llmdriven_action_generation_on/) , 2024-12-14-0913
```
Hey everyone,

I’m sharing a project I worked on some time ago: a LLM-Driven Action Generation on Windows with Langchain
 (openai). An automation system powered by a Large Language Model (LLM) to understand and execute instructions. The idea
 is simple: you give a natural language command (e.g., “Open Notepad and type ‘Hello, world!’”), and the system attempts
 to translate it into actual actions on your Windows machine.

**Key Features:**

* **LLM-Driven Action Generation:** Th
e system interprets requests and dynamically generates Python code to interact with applications.
* **Automated Windows 
Interaction:** Opening and controlling applications using tools like pywinauto and pyautogui.
* **Screen Analysis & OCR:
** Capture and analyze the screen with Tesseract OCR to verify UI states and adapt accordingly.
* **Speech Recognition &
 Text-to-Speech:** Control the computer with voice commands and receive spoken feedback.

**Current State of the Project
:**  
This is a proof of concept developed a while ago and not maintained recently. There are many bugs, unfinished feat
ures, and plenty of optimizations to be done. Overall, it’s more a feasibility demo than a polished product.

**Why Shar
e It?**

* If you’re curious about integrating an LLM with Windows automation tools, this project might serve as inspira
tion.
* You’re welcome to contribute by fixing bugs, adding features, or suggesting improvements.
* Consider this a star
ting point rather than a finished solution. Any feedback or assistance is greatly appreciated!

**How to Contribute:**


* The source code is available on GitHub (link in the comments).
* Feel free to fork, open PRs, file issues, or simply u
se it as a reference for your own projects.

**In Summary:**  
This project showcases the potential of LLM-driven Window
s automation. Although it’s incomplete and imperfect, I’m sharing it to encourage discussion, experimentation, and hopef
ully the emergence of more refined solutions!

Thanks in advance to anyone who takes a look. Feel free to share your tho
ughts or contributions!  


[https://github.com/JacquesGariepy/CommanderAI](https://github.com/JacquesGariepy/CommanderA
I)


```
---

     
 
all -  [ multi RAG issue ](https://www.reddit.com/r/LangChain/comments/1hcvpmy/multi_rag_issue/) , 2024-12-14-0913
```
Hi everyone, I need your help. I'm working on a multi-profile RAG using RetrievalQA, FAISS, and Chainlit. Recently, whil
e testing, I encountered an issue with memory usage.

I have 5 chat profiles in Chainlit, each linked to a different vec
tor database. When I select a chat profile and load its corresponding vector database, memory usage increases as expecte
d. However, when I close that chat profile, the memory usage does not decrease.

Does anyone know how to solve this issu
e? Is there a function to properly close or unload vector databases in RetrievalQA? Or perhaps a way to terminate the Re
trievalQA process and free up memory?
```
---

     
 
all -  [ How to clone any Twitter personality into an AI (your move, Elon) 🤖 ](https://www.reddit.com/r/LangChain/comments/1hcrjfp/how_to_clone_any_twitter_personality_into_an_ai/) , 2024-12-14-0913
```
The LangChain team dropped this gem showing how to build AI personas from Twitter/X profiles using LangGraph and Arcade.
 It's basically like having a conversation with someone's Twitter alter ego, minus the blue checkmark drama.

Key featur
es:

* Uses long-term memory to store tweets (like that ex who remembers everything you said 3 years ago)
* RAG implemen
tation that's actually useful and not just buzzword bingo
* Works with any Twitter profile (ethics left as an exercise f
or the reader)
* Uses Arcade to integrate with Twitter/X
* Clean implementation that won't make your eyes bleed

Video t
utorial shows full implementation from scratch. Perfect for when you want to chat with tech Twitter without actually goi
ng on Twitter.

[https://www.youtube.com/watch?v=rMDu930oNYY](https://www.youtube.com/watch?v=rMDu930oNYY)

P.S. No GPTs
 were harmed in the making of this tutorial.
```
---

     
 
all -  [ What happened to Conversational Retrieval QA? ](https://www.reddit.com/r/LangChain/comments/1hcpf6v/what_happened_to_conversational_retrieval_qa/) , 2024-12-14-0913
```
Once upon a time in the v0.1 days there was this idea of \[Conversational Retrieval QA\](https://js.langchain.com/v0.1/d
ocs/modules/chains/popular/chat\_vector\_db\_legacy/).  You can see the docs on this webpage, but if you click the link 
to go to the current stable version it doesn't seem to exist anymore.

Does anyone know if this got absorbed into someth
ing else less obvious or did they just drop support for it?
```
---

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/learnmachinelearning/comments/1hcp5ht/not_able_to_generate_embeddings/) , 2024-12-14-0913
```
I am using Langchain and google generative AI to generate embeddings of the document, however I am encountering Error 40
3 ->  
langchain\_google\_genai.\_common.GoogleGenerativeAIError: Error embedding content: 403 Request had insufficient 
authentication scopes. \[reason: 'ACCESS\_TOKEN\_SCOPE\_INSUFFICIENT'

    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_community.vectorstores import Chroma
  
  from langchain_google_genai import GoogleGenerativeAIEmbeddings
    from langchain.text_splitter import CharacterTextS
plitter
    from langchain_community.document_loaders import TextLoader
    import google.generativeai as genai
    
   
 
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    
    model = ChatGoogleGenerativeAI(model = 'gemi
ni-1.5-pro',api_key=api_key)
    
    
    genai.configure(api_key=api_key)
    
    current_working_directory = os.getc
wd()
    file_path = os.path.join(current_working_directory,'books/odyssey.txt')
    
    storing_directory = os.path.jo
in(current_working_directory,'db','chroma_db')
    
    
    if not os.path.exists(storing_directory):
        print('St
oring directory does not exist..Initializing a vector store.......\n')
        if not os.path.exists(file_path):
       
     raise FileNotFoundError(f'The {file_path} could not be found.\n')
        # read the content from the file
        
loader = TextLoader(file_path)
        document = loader.load()
    
        # create chunks
        text_splitter = Cha
racterTextSplitter(chunk_size=1000,chunk_overlap=0)
        docs = text_splitter.split_documents(document)
    
        
# Display Info
        print('\n------------Document Chunk Info----------------\n')
        print(f'Number of document c
hunks----> {len(docs)}')
        print(f'Sample Chunk---->\n{docs[0].page_content}\n')
    
        # create embeddings

        print('\n------------creating embeddings----------------\n')
        embeddings = GoogleGenerativeAIEmbeddings(m
odel = 'models/embedding-001',api_key=api_key)
        print('\n--------------finished creating embeddings-------------\
n')
    
        # vector store
        print('\n--------------Creating vector store-------------\n')
        db = Chrom
a.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=storing_di
rectory
        )
        print('\n--------------finished creating vector store-------------\n')
    
    else:
        
print('-----------------vector store already exists')
    
    

Somebody please help I been stuck here for last 2 hours
  

```
---

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/generativeAI/comments/1hcp3y0/not_able_to_generate_embeddings/) , 2024-12-14-0913
```
I am using Langchain and google generative AI to generate embeddings of the document, however I am encountering Error 40
3 ->  
langchain\_google\_genai.\_common.GoogleGenerativeAIError: Error embedding content: 403 Request had insufficient 
authentication scopes. \[reason: 'ACCESS\_TOKEN\_SCOPE\_INSUFFICIENT'

Somebody please help I been stuck here for last 2
 hours

    import os
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI
 
   from langchain_community.vectorstores import Chroma
    from langchain_google_genai import GoogleGenerativeAIEmbeddin
gs
    from langchain.text_splitter import CharacterTextSplitter
    from langchain_community.document_loaders import Te
xtLoader
    import google.generativeai as genai
    
    
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
 
   
    
    model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro',api_key=api_key)
    
    
    genai.configure(api_
key=api_key)
    
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory,'bo
oks/odyssey.txt')
    
    storing_directory = os.path.join(current_working_directory,'db','chroma_db')
    
    
    if
 not os.path.exists(storing_directory):
        print('Storing directory does not exist..Initializing a vector store....
...\n')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'The {file_path} could not be fou
nd.\n')
        # read the content from the file
        loader = TextLoader(file_path)
        document = loader.load()

    
        # create chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        doc
s = text_splitter.split_documents(document)
    
        # Display Info
        print('\n------------Document Chunk Info
----------------\n')
        print(f'Number of document chunks----> {len(docs)}')
        print(f'Sample Chunk---->\n{do
cs[0].page_content}\n')
    
        # create embeddings
        print('\n------------creating embeddings---------------
-\n')
        embeddings = GoogleGenerativeAIEmbeddings(model = 'models/embedding-001',api_key=api_key)
        print('\
n--------------finished creating embeddings-------------\n')
    
        # vector store
        print('\n--------------
Creating vector store-------------\n')
        db = Chroma.from_documents(
            documents=docs,
            embed
ding=embeddings,
            persist_directory=storing_directory
        )
        print('\n--------------finished creat
ing vector store-------------\n')
    
    else:
        print('-----------------vector store already exists')
    

My 
code->  

```
---

     
 
all -  [ Any alternatives to LangChain for LLMs/GraphRAG on RDF graphs? ](https://www.reddit.com/r/KnowledgeGraph/comments/1hcozn1/any_alternatives_to_langchain_for_llmsgraphrag_on/) , 2024-12-14-0913
```
Hello. I am getting more into GraphRAG. This year a project I was involved with transformed a large RDF graph into Neo4j
 (via Neosemantics), and from there I used LangChain and our in-house AI models to do GraphRAG things, with great result
s. I proved that this approach gave much better answers (because of kg context) than traditional RAG. Shoutout to Jesus 
Barrasa, for both his Neo4j semantic expertise, and the 'Going Meta' YouTube series which I highly recommend.     
  
Ho
wever, I am at the end of the day an ontologist, and we have tons of RDF ontologies, with no interest in (or resources f
or) transforming all of those into Neo4j graphs. I've looked into how to do things directly with RDF and it's not an enc
ouraging landscape.  
  
LangChain can do things through RdfGraph, but it's mostly based on rdflib, whereas 'knowledge g
raph' support from tons of frameworks is super robust. The SparqlQAChain is neat, since you can directly see what SPARQL
 query the LLM is composing to try to answer the question. But I don't actually care about knowledge graph generation, w
hich is unfortunately what so much tooling is built around. I already have everything highly structured within a defined
 domain! Once it gets to actual RAG, the usual vector similarity search rears its ugly head, and isn't GraphRAG, and wou
ld actually be a terrible strategy for already-structured data.   
  
So, has anyone been in this same position of needi
ng to do GraphRAG things directly on RDF data (i.e., use vectorization but merely as a pre/post filtering mechanism, but
 ground all answers in the knowledge graph), but have used things OTHER than LangChain?  
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/Entrepreneur/comments/1hcm180/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-14-0913
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.

# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let you 
upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, analy
ze a research paper, and more.

# Let's look at the market

Made possible by advances in AI like ChatGPT and Retrieval-A
ugmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen consistent growth in mark
et interest, which is currently at an all-time high (source: google trends)

Keywords like 'chat PDF' and 'PDF AI' get b
etween 1 to 10 million searches every month (source:keyword planner), with a broad target audience that includes researc
hers, students, and professionals across various industries.

Leaders like PDF.ai and ChatPDF have already gained millio
ns of users within a year of launch, driven by the growing market demand, with paid users subscribing at around $20/mont
h.

# Alright, so how do we build this with open source?

The core tech for most PDF AI tools are based on the same arch
itecture. You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the uploaded PDF’
s chapters/topics and store them in a vector database (like Pinecone/pgvector).

Now, every time the user asks a questio
n, a similarity search is performed to find the most similar PDF topics from the vector database. The selected topic con
tents are then sent to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are som
e of the best open source implementations for this process (source: GitHub):

* GPT4 & LangChain Chatbot for large PDF d
ocs by Mayo Oshin
* MultiPDF Chat App by Alejandro AO
* PDFToChat by Hassan El Mghari

Worried about building signups, u
ser management, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everything you need out of 
the box (source: GitHub):

* SaaS Boilerplate by Remi Wg
* Open SaaS by wasp-lang

You can **check out the hyperlinks in
 the first comment, or look em up on google** (they're quite popular).

# A few ideas to stand out from the noise:

Here
 are a few strategies that could help you differentiate and achieve product market fit (based on the pivot principles fr
om The Lean Startup by Eric Ries):

1. **Narrow down your target audience for a personalized UX:** For instance, an exam
 prep assistant for students with study notes and quiz generator; or a document due diligence and analysis tool for lawy
ers.
2. **Add unique features to increase switching cost:** You could autogenerate APIs for the uploaded PDFs to enable 
remote integrations (eg. support chatbot knowledge base); or build in workflow automation features for bulk analyses of 
PDFs.
3. **Offer platform level advantages:** You could ship a native mobile/desktop apps for a more integrated UX; or (
non-trivial) offer private/offline support by replacing the APIs with local open source deployments (eg. llama for LLM, 
an embedding model from the MTEB list, and FAISS for vector search).

**TMI?** I’m an ex-AI engineer and product lead, s
o don’t hesitate to reach out with any questions!

Thanks for reading! this was the first post on my new weekly newslett
er (link in first comment) which covers open-source/turnkey resources behind popular products (like this one). Feel free
 to bring up other products you'd like me to analyze or any other aspects you'd like to learn about in future posts.
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/microsaas/comments/1hckxwo/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-14-0913
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.

# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let you 
upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, analy
ze a research paper, and more. To see this in action or dive deeper into the tech behind it, check out this [YouTube vid
eo.](https://www.youtube.com/watch?v=ih9PBGVVOO4)

# Let's look at the market

Made possible by advances in AI like Chat
GPT and Retrieval-Augmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen consis
tent growth in market interest, which is currently at an all-time high (source:[google trends](https://trends.google.com
/trends/explore?date=today%205-y&q=pdf%20chat,pdf%20ai&hl=en-GB))

Keywords like 'chat PDF' and 'PDF AI' get between 1 t
o 10 million searches every month (source:keyword planner), with a broad target audience that includes researchers, stud
ents, and professionals across various industries.

Leaders like PDF.ai and ChatPDF have already gained millions of user
s within a year of launch, driven by the growing market demand, with paid users subscribing at around $20/month.

# Alri
ght, so how do we build this with open source?

The core tech for most PDF AI tools are based on the same architecture. 
You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the uploaded PDF’s chapters
/topics and store them in a vector database (like Pinecone).

Now, every time the user asks a question, a similarity sea
rch is performed to find the most similar PDF topics from the vector database. The selected topic contents are then sent
 to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are some of the best open 
source implementations for this process:

* [GPT4 & LangChain Chatbot for large PDF docs](https://github.com/mayooear/gp
t4-pdf-chatbot-langchain) by Mayo Oshin
* [MultiPDF Chat App](https://github.com/alejandro-ao/ask-multiple-pdfs) by Alej
andro AO
* [PDFToChat](https://github.com/Nutlope/pdftochat) by Hassan El Mghari

Worried about building signups, user m
anagement, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everything you need out of the b
ox:

* [SaaS Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) by Remi Wg
* [Open SaaS](https://github.com/wasp-l
ang/open-saas) by wasp-lang

# A few ideas to stand out from the noise:

Here are a few strategies that could help you d
ifferentiate and achieve product market fit (based on the pivot principles from The Lean Startup by Eric Ries):

1. **Na
rrow down your target audience for a personalized UX:** For instance, an exam prep assistant for students with study not
es and quiz generator; or a document due diligence and analysis tool for lawyers.
2. **Add unique features to increase s
witching cost:** You could autogenerate APIs for the uploaded PDFs to enable remote integrations (eg. support chatbot kn
owledge base); or build in workflow automation features for bulk analyses of PDFs.
3. **Offer platform level advantages:
** You could ship a native mobile/desktop apps for a more integrated UX; or (non-trivial) offer private/offline support 
by replacing the APIs with local open source deployments (eg. llama for LLM, an embedding model from the MTEB list, and 
FAISS for vector search).

**TMI?** I’m an ex-AI engineer and product lead, so don’t hesitate to reach out with any ques
tions!

**P.S.** I've started a free weekly [newsletter](https://saaswithcode.substack.com/p/issue-1-launch-a-saas-like-
chatpdf) to share open-source/turnkey resources behind popular products (like this one). If you’re a founder looking to 
launch your next product without reinventing the wheel, please subscribe :)
```
---

     
 
all -  [ I made a free directory of Agentic Tools ](https://www.reddit.com/r/LangChain/comments/1hckonl/i_made_a_free_directory_of_agentic_tools/) , 2024-12-14-0913
```
Hey everyone! 👋

With the rapid evolution of AI and the growing ecosystem of AI agents, finding the right tools that wor
k well with these agents has become increasingly important. That's why I created the [Agentic Tools Directory](https://d
irectory.composio.dev/) \- a comprehensive collection of agent-friendly tools across different categories.

**What is th
e Agentic Tools Directory?**

It's a curated repository where you can discover and explore tools specifically designed o
r optimized for AI agents. Whether you're a developer, researcher, or AI enthusiast, this directory aims to be your go-t
o resource for finding agent-compatible tools.

**What you'll find:**

* Tools categorized by functionality and use case

* Clear information about agent compatibility
* Regular updates as new tools emerge
* A community-driven approach to di
scovering and sharing resources

**Are you building an agentic tool?**

If you've developed a tool that works well with 
AI agents, we'd love to include it in the directory! This is a great opportunity to increase your tool's visibility with
in the AI agent ecosystem.

**How to get involved:**

1. Explore the directory
2. Submit your tool
3. Share your feedbac
k and suggestions

Let's build this resource together and make it easier for everyone to discover and utilize agent-frie
ndly tools!

Questions, suggestions, or feedback? Drop them in the comments below!
```
---

     
 
all -  [ as a fresher can i write this under my name in resume. ](https://www.reddit.com/r/IndiaTech/comments/1hcjnml/as_a_fresher_can_i_write_this_under_my_name_in/) , 2024-12-14-0913
```
also i have 3 months of work experience is it even countable as experience

https://preview.redd.it/yvdm7njsre6e1.png?wi
dth=1180&format=png&auto=webp&s=f585ecfc8b94952eecaf9c7efbaf787e0b101209


```
---

     
 
all -  [ A way in langgraph to find if the execution is completed ](https://www.reddit.com/r/LangChain/comments/1hcj99u/a_way_in_langgraph_to_find_if_the_execution_is/) , 2024-12-14-0913
```
Iam building a workflow which asks for human input for onboarding, I want to know in some way that the execution is comp
leted or ongoing so that i can use it to switch to next workflow. How can i achieve this by using interupts or by using 
a state variable
```
---

     
 
all -  [ My llm agent with tools is not converting the ToolMessage into an AI message ](https://www.reddit.com/r/LangChain/comments/1hci1do/my_llm_agent_with_tools_is_not_converting_the/) , 2024-12-14-0913
```
Hello and  a good day to you all!

I have been stuck on this issue for too long so I've decided to come and ask for your
 help. I made a graph which contains an llm agent that is connected to a tool (just one tool function for now). The tool
 loops back to the agent, but the agent never converts the ToolMessage into an AImessage to return to the user. After th
e state gets updated with the ToolMessage, the agent just calls the tool again, gets another ToolMessage, and it keeps o
n looping indefinitely.

For a clearer picture - the user wants to update his tickets in a project management database, 
and the tools return a string of user's tickets separated by a comma. The agent should reply with normal language delive
ring the tickets and asking the user to choose one to update. 

The agent is 

    ChatOpenAI(model='gpt-4o-mini', tempe
rature=0).bind_tools(self.tools)

 and get\_user\_tickets is the tool.



Any help is appreciated!

Here are my logs so 
that you can see the messages:



024-12-12 10:46:36.966 | INFO     | notion\_bot.agents.qa\_agent:run:86 - Starting QAA
gent.

2024-12-12 10:46:37.569 | INFO     | notion\_bot.agents.qa\_agent:run:105 - {'messages': \[HumanMessage(content='
update a ticket', additional\_kwargs={}, response\_metadata={}, id='be57ff2f-b79e-43d0-9ebc-eb71bd655597')\]}

2024-12-1
2 10:46:38.048 | INFO     | notion\_bot.agents.get\_user\_tickets:get\_user\_tickets:40 - \['Woohoo', 'Async', 'BlaBla'\
]

2024-12-12 10:46:38.052 | INFO     | notion\_bot.agents.qa\_agent:run:86 - Starting QAAgent.

2024-12-12 10:46:38.714
 | INFO     | notion\_bot.agents.qa\_agent:run:105 - {'messages': \[HumanMessage(content='update a ticket', additional\_
kwargs={}, response\_metadata={}, id='be57ff2f-b79e-43d0-9ebc-eb71bd655597'), AIMessage(content='', additional\_kwargs={
'tool\_calls': \[{'id': 'call\_sYlZhRQGDeUWBetTISfLP7KK', 'function': {'arguments': '{}', 'name': 'get\_user\_tickets'},
 'type': 'function'}\], 'refusal': None}, response\_metadata={'token\_usage': {'completion\_tokens': 12, 'prompt\_tokens
': 328, 'total\_tokens': 340, 'completion\_tokens\_details': {'audio\_tokens': 0, 'reasoning\_tokens': 0, 'accepted\_pre
diction\_tokens': 0, 'rejected\_prediction\_tokens': 0}, 'prompt\_tokens\_details': {'audio\_tokens': 0, 'cached\_tokens
': 0}}, 'model\_name': 'gpt-4o-mini-2024-07-18', 'system\_fingerprint': 'fp\_6fc10e10eb', 'finish\_reason': 'tool\_calls
', 'logprobs': None}, id='run-c0c944cd-bbe5-4262-ad53-7e0040069b6c-0', tool\_calls=\[{'name': 'get\_user\_tickets', 'arg
s': {}, 'id': 'call\_sYlZhRQGDeUWBetTISfLP7KK', 'type': 'tool\_call'}\], usage\_metadata={'input\_tokens': 328, 'output\
_tokens': 12, 'total\_tokens': 340, 'input\_token\_details': {'audio': 0, 'cache\_read': 0}, 'output\_token\_details': {
'audio': 0, 'reasoning': 0}}), ToolMessage(content='Woohoo, Async, BlaBla', name='get\_user\_tickets', id='58520eb1-a67b
-43b3-a030-8040e36e9027', tool\_call\_id='call\_sYlZhRQGDeUWBetTISfLP7KK')\]}

2024-12-12 10:46:39.166 | INFO     | noti
on\_bot.agents.get\_user\_tickets:get\_user\_tickets:40 - \['Woohoo', 'Async', 'BlaBla'\]

2024-12-12 10:46:39.172 | INF
O     | notion\_bot.agents.qa\_agent:run:86 - Starting QAAgent.

 
```
---

     
 
all -  [ Should I reuse a single LangChain ChatOpenAI instance or create a new one for each request in FastAP ](https://www.reddit.com/r/LangChain/comments/1hcf16g/should_i_reuse_a_single_langchain_chatopenai/) , 2024-12-14-0913
```
Hi everyone,

I’m currently working on a FastAPI server where I’m integrating LangChain with the OpenAI API. Right now, 
I’m initializing my `ChatOpenAI` LLM object once at the start of my Python file, something like this:

    llm = ChatOpe
nAI(
        model='gpt-4',
        temperature=0,
        max_tokens=None,
        api_key=os.environ.get('OPENAI_API_K
EY'),
    )
    prompt_manager = PromptManager('prompt_manager/second_opinion_prompts.yaml')
    

Then I use this `llm`
 object in multiple different functions/endpoints. My question is: is it a good practice to reuse this single `llm` inst
ance across multiple requests and endpoints, or should I create a separate `llm` instance for each function call?

I’m s
till a bit new to LangChain and FastAPI, so I’m not entirely sure about the performance and scalability implications. Fo
r example, if I have hundreds of users hitting the server concurrently, would reusing a single `llm` instance cause issu
es (such as rate-limiting, thread safety, or unexpected state sharing)? Or is this the recommended way to go, since crea
ting a new `llm` object each time might add unnecessary overhead?

Any guidance, tips, or best practices from your exper
ience would be really appreciated!

Thanks in advance!
```
---

     
 
all -  [ Chance me for RSI (Experienced Researcher at Ivy + Stanford)  ](https://www.reddit.com/r/summerprogramresults/comments/1hce5t6/chance_me_for_rsi_experienced_researcher_at_ivy/) , 2024-12-14-0913
```
Chance me for RSI:   
  
Essentially my ECS + Test scores: 

**Test Scores:** 

1510 PSAT

1550 SAT

**STEM ECS:**   
\-
 Global Finals Qualifier for VEX Robotics Competition. Programmer for the team 5327A. (2023)

\- Currently Captain of th
e MATE ROV Competition club at school

Academic Research

Researcher at Brown University (2024-Present)

• Developing Ka
lman filter algorithms for Pleistocene temperature reconstruction

• Publication and presentation forthcoming at America
n Geophysical Union 2025

Research Intern at Stanford University (2023)

• Created Retrieval Augmented Generation system
 for wildfire & air quality data analysis

• Implemented advanced NLP techniques using PyTorch and LangChain

• Publicat
ion

Research Intern at Australian Institute of Marine Science (2024)

• Developed Python scripts for 3D coral reef anal
ysis

• Implemented Möller-Trumbore algorithm for environmental modeling

• Used in paper for EcoRAPP (ecological intell
igence for reef restoration adaptation program)

about internal tools to diagnose Coral Bleaching and where to take acti
on

Underwater Ecosystem Drone Innovation

\- Developed novel underwater drone system for 3D coral reef mapping

\- Secu
red $11,000 venture capital investment

\- Obtained utility provisional patent for innovative marine mapping technology


\- Created scalable solution for reef ecosystem documentation and monitoring

\- System enables high-resolution 3D mode
ling of threatened marine environments  
  
**Non STEM:**   
  
REEFlect:

Founded and scaled global environmental monit
oring organization spanning 11 countries

Secured $2,500 municipal grant for the organization from City of Dublin

Estab
lished partnerships with East Bay Regional Park Districts, Big Sur Land Trust, Bear Yuba

Land Trust

Led international 
collaboration with Ocean Project Ghana for coastal cleanup initiatives in Ghana

Amassed over 200 members in over 7 diﬀe
rent countries
```
---

     
 
all -  [ Why Pydantic AI might be the future for building AI Agents? ](https://www.reddit.com/r/PydanticAI/comments/1hcc9qq/why_pydantic_ai_might_be_the_future_for_building/) , 2024-12-14-0913
```
Hi guys,

Pyndatic AI is a new framework comparing to heavy-weight such as Langchain and LlamaIndex. However, I found it
 very easy to use and powerful. It gives me a lot of flexibility to build versatile AI agents. 

Beside excellent data v
alidation (of course, it is from Pydantic, which is used by all big players such as OpenAI, Langchain...etc.), the bigge
st plus for me is: Pythonic and minimum of abstraction. We can easily go in the code and know how things are done under 
the hood. This siginificantly reduceds debugging time.

Check it out at [https://ai.pydantic.dev/](https://ai.pydantic.d
ev/)
```
---

     
 
all -  [ Problems installing langchain-python-rag-document from examples ](https://www.reddit.com/r/ollama/comments/1hcayho/problems_installing_langchainpythonragdocument/) , 2024-12-14-0913
```
i get this after installing from requirements.txt

    ERROR: Ignored the following versions that require a different py
thon version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11
; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
    
    ERROR: Could not find a version that s
atisfies the requirement tensorflow-macos==2.13.0 (from versions: 2.12.0)
    
    ERROR: No matching distribution found
 for tensorflow-macos==2.13.0
    
    $ pip --version
    pip 24.2 from xyz (python 3.11)
    $ python --version
    Py
thon 3.11.9

I have python 3.9.20 which i access with `python3.9` but how do i get the associated `pip` to install requi
rements?
```
---

     
 
all -  [ I automated my entire job with Python & AI - Ask me how to automate YOUR most hated task ](https://www.reddit.com/r/ArtificialInteligence/comments/1hc93pz/i_automated_my_entire_job_with_python_ai_ask_me/) , 2024-12-14-0913
```
Hey r/ArtificialInteligence  \- I'm the dev who automated an entire marketing agency's workflow. Ask me literally anythi
ng about automating your boring tasks. Some quick overview of what I've built:

• Turned 5-6 hours of daily research and
 posting into CrewAI+Langchain+DDG agency

• Built AI Bot that analyzes and answers 1000+ customer emails daily (For ver
y cheap - 0.5$ a day)

• Created Tweepy-Tiktok-bot+Instapy bots that manage entire social media presence, with CrewAI fo
r agents and Flux Dev for image generation

• Automated job applications on LinkedIn with Selenium+Gemini Flash 1.5

• A
utomated content generation with local AI models (for free)

• Automated entire YouTube channel (thumbnails, description
s, tags, posting) with custom FLUX Dev Lora, cheapest and most effective LLMs and hosted on cloud

• Built web scraper b
ot that monitors thousands of tokens prices and trader bots that makes the buy/sell on Binance

• Made a system that mon
itors and auto-responds to Reddit/Discord opportunities with [PRAW+discord.py](http://PRAW+discord.py)

Ask me about:

H
ow to automate your specific task Which tools actually work (and which are trash)

Real costs and time savings

Common a
utomation mistakes

Specific tech stacks for your automation needs

How to choose AI models to save costs

Custom soluti
ons vs existing tools

I've processed millions of tasks using these systems. Not theoretical - all tested and running.


I use Python, JS, and modern AI Stack (not just Zapier or [make.com](http://make.com) connections).

I'm building my por
tfolio and looking for interesting problems to solve. But first - ask me anything about your automation needs. I'll give
 you a free breakdown of how I'd solve it.

Some questions to get started: What's your most time-consuming daily task? W
hich part of your job do you wish was automated? How much time do you waste on repetitive tasks? Or ask whatever you wan
t to know...

Drop your questions below - I'll show you exactly how to automate it (with proof of similar projects I've 
done) :)
```
---

     
 
all -  [ I automated my entire job with Python & AI - Ask me how to automate YOUR most hated task ](https://www.reddit.com/r/Automate/comments/1hc8x5v/i_automated_my_entire_job_with_python_ai_ask_me/) , 2024-12-14-0913
```
Hey r/Automate  \- I'm the dev who automated an entire marketing agency's workflow. Ask me literally anything about auto
mating your boring tasks. Some quick overview of what I've built:

• Turned 5-6 hours of daily research and posting into
 CrewAI+Langchain+DDG agency 

• Built AI Bot that analyzes and answers 1000+ customer emails daily (For very cheap - 0.
5$ a day) 

• Created Tweepy-Tiktok-bot+Instapy bots that manage entire social media presence, with CrewAI for agents an
d Flux Dev for image generation 

• Automated job applications on LinkedIn with Selenium+Gemini Flash 1.5 

• Automated 
content generation with local AI models (for free) 

• Automated entire YouTube channel (thumbnails, descriptions, tags,
 posting) with custom FLUX Dev Lora, cheapest and most effective LLMs and hosted on cloud 

• Built web scraper bot that
 monitors thousands of tokens prices and trader bots that makes the buy/sell on Binance • Made a system that monitors an
d auto-responds to Reddit/Discord opportunities with [PRAW+discord.py](http://PRAW+discord.py)

Portfolio: [https://gith
ub.com/kakachia777/](https://github.com/kakachia777/) (I'm pushing projects gradually)

Ask me about: How to automate yo
ur specific task Which tools actually work (and which are trash) Real costs and time savings Common automation mistakes 
Specific tech stacks for your automation needs How to choose AI models to save costs Custom solutions vs existing tools


I've processed millions of tasks using these systems. Not theoretical - all tested and running. Quick flex: My automati
on tools have processed over 1M+ tasks for real clients. I use Python, JS, and modern AI (not just Zapier or [make.com](
http://make.com) connections).

I'm building my portfolio and looking for interesting problems to solve. But first - ask
 me anything about your automation needs. I'll give you a free breakdown of how I'd solve it.

Some questions to get sta
rted: What's your most time-consuming daily task? Which part of your job do you wish was automated? How much time do you
 waste on repetitive tasks? Or anything you want to know...

Drop your questions below - I'll show you exactly how to au
tomate it (with proof of similar projects I've done) :)
```
---

     
 
all -  [ [0 YOE, Unemployed , Machine Learning/Data Science, India] ](https://www.reddit.com/r/resumes/comments/1hc0c61/0_yoe_unemployed_machine_learningdata_science/) , 2024-12-14-0913
```
https://preview.redd.it/pbevskapi96e1.png?width=1170&format=png&auto=webp&s=6c61dfd3845cd82bc1ca6eeac19c00a2049231a8

ht
tps://preview.redd.it/wz65kahqi96e1.png?width=1070&format=png&auto=webp&s=b368ed92fd9cb957c2a0e1d6f4dee03f1bbbc58d

I am
 a 3rd year student pursuing BTech. I need feedback for applying to internships. As of now, I am not getting shortlisted
. What kind of projects do I need to add or showcase which will catch the attention. am i missing something here
```
---

     
 
all -  [ Conversational avatar  ](https://www.reddit.com/r/LangChain/comments/1hbxlfs/conversational_avatar/) , 2024-12-14-0913
```
Has anyone tried creating this kind of project? 
```
---

     
 
all -  [ Local tool calling agents using LangChain and Ollama are inexplicably poorly performing ](https://www.reddit.com/r/LocalLLaMA/comments/1hbx96u/local_tool_calling_agents_using_langchain_and/) , 2024-12-14-0913
```
Hi all,

Has anyone tried to create tool calling agents with LangChain and Ollama?  My attempts have been almost univers
ally unsuccessful.  Problems include:

1. Losing the ability to chat

2. Calling tools when it is not appropriate

3. Ca
lling tools on non-sensical inputs

The same agents work fine on, e.g., openai.

I have encountered this on a variety of
 models on Ollama.  Oddly enough, llama3-groq-tool-use:8b is the lone model that seems to work reasonably.

Has anyone e
ncountered this and determined the cause?

Here's a draft notebook/blog where I have some experiments: [https://colab.re
search.google.com/drive/1DngmKINhV95iKVVGF7YC5\_K7oiujMT6q?usp=sharing](https://colab.research.google.com/drive/1DngmKIN
hV95iKVVGF7YC5_K7oiujMT6q?usp=sharing)
```
---

     
 
all -  [ We built a frontend framework for LangGraph ](https://www.reddit.com/r/LangChain/comments/1hbw7yj/we_built_a_frontend_framework_for_langgraph/) , 2024-12-14-0913
```
At [CopilotKit](https://github.com/CopilotKit/CopilotKit), we build components & tools that help developers build in-app
 AI assistants (like Chatbots). Over the last few months we've been working to support deeper in-app Agent integrations.
  

  
So we collaborated with the LangChain team, to build a toolset that helps users integrate their LangGraph agents 
into full-stack apps with full support across the LangGraph ecosystem (Python, JS, Cloud, Studio, etc). 



Our new [Co-
Agents release](https://www.copilotkit.ai/blog/build-full-stack-apps-with-langgraph-and-copilotkit) contains tools that 
allow you to: 

\- Stream an agent's intermediate state (to the frontend) 

\- Share real-time state between the agent &
 the application 

\- Allow the Agent to take actions in your application 

\- Human-in-the-loop to steer and correct ag
ents (built with LangGraph breakpoints) 

\- Agentic Generative UI 

In our new release we support LangGraph JS, Python,
 LangGraph Platform (Cloud) and LangGraph Studio. 

  
You can build an Agentic Application in just a few minutes with L
angGraph & Co-Agents and we have great demos and [tutorials](https://go.copilotkit.ai/ai-travel-demo-video) to guide you
. 

  
We're fully open-source (MIT), get started here: 

[https://github.com/CopilotKit/CopilotKit](https://github.com/
CopilotKit/CopilotKit)

https://preview.redd.it/rwy3ec0ho86e1.png?width=993&format=png&auto=webp&s=e910313e67dfeecf90661
d36816d2298952e1b7a
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-14-0913
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
