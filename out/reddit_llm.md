 
all -  [ struggling to understand the langgraph tutorial (build a basic chatbot) ](https://www.reddit.com/r/LangChain/comments/1heg7pi/struggling_to_understand_the_langgraph_tutorial/) , 2024-12-15-0915
```
link: [https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot](https://langchain-
ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot)

So far I am able to follow this tutorial f
or the 'build chatbot section' - what I don't understand is the logic in the 'while True' statement below - specifically
 on how the excelption logic is invoked:

  
`while True:`  
`try:`  
`user_input = input('User: ')`  
`if user_input.lo
wer() in ['quit', 'exit', 'q']:`  
`print('Goodbye!')`  
`break`  
  
`stream_graph_updates(user_input)`  
`except:`  
`
# fallback if input() is not available`  
`user_input = 'What do you know about LangGraph?'`  
`print('User: ' + user_in
put)`  
`stream_graph_updates(user_input)`  
`break`

  


Question :    exception logic trigger - how does it get trigg
ered? 

If you look at the tutorial, it is showing the results of executing the exception logic -  

`Assistant: LangGra
ph is a library designed to help build stateful multi-agent applications using language models. It provides tools for cr
eating workflows and state machines to coordinate multiple AI agents or language model interactions. LangGraph is built 
on top of LangChain, leveraging its components while adding graph-based coordination capabilities. It's particularly use
ful for developing more complex, stateful AI applications that go beyond simple query-response interactions.`  
Goodbye!




How does the execution logic  get triggered?  




```
---

     
 
all -  [ Do we have anything to replicate livekit agents voice capabilities with langgraph? ](https://www.reddit.com/r/LangChain/comments/1heed8a/do_we_have_anything_to_replicate_livekit_agents/) , 2024-12-15-0915
```
I am working on a voice agent that needs to have as low latency as possible with the speech-text-speech pipeline. (I am 
not going for multimodal realtime apis like the one of openai and recently released gemini 2.0 flash because they are co
stly and in beta as well as closed source). 

I want to make as many things on opensource as possible.

I first looked i
nto livekit which is opensource webrtc framework . which also has agents , these agents are pretty fast with a lot of op
timizations in the streaming pipeline. Now the issue with this is that agent framework of livekit is pretty basic with f
unction calling, i was looking for something more like langgraph and in best case scenario a langraph integration with l
ivekit.

On a similar note i looked at pipecat as well which also has pipecat flow to simulate decent flows somewhat lik
e langgraph while also being optimized for voice capabilites. The issue wth pipecat is that although it is opensource it
self, it only fully supports daily as a transport layer (something like livekit transport integration is in progress but
 even then i would prefer if instead of pipecat flows i could use something like langraph with good voice capabilities)


I wanted to ask for any suggestions on how to go about this problem. Thanks.
```
---

     
 
all -  [ Is this Langgraph chatbot worth it? ROAST ME ](https://www.reddit.com/r/LangChain/comments/1hee7f1/is_this_langgraph_chatbot_worth_it_roast_me/) , 2024-12-15-0915
```
Hi everybody,

I'm the founder of [**Chetty.ai**](http://Chetty.ai), an AI chatbot for websites.

Recently, I developed 
the first version of an agent in **Langgraph** to handle web searches in a more complex way. I already have ten major cu
stomers using this engine, so everything is fully operational and in production.

Could you please try it out and share 
your honest feedback? It's simple—just insert any website and ask about their services.

[https://chetty.ai/advanced-sea
rch-demo](https://chetty.ai/advanced-search-demo)

Thanks!
```
---

     
 
all -  [ I've built an MVP to level up your LangChain and AI skills - looking for feedback 🚀 ](https://www.reddit.com/r/LangChain/comments/1he8wiv/ive_built_an_mvp_to_level_up_your_langchain_and/) , 2024-12-15-0915
```
Hello LangChain and AI experts,

I'm building a free app to help users enhance their AI skills, including prompt enginee
ring, LangChain, Haystack, etc, and would like to see if it is useful for you.

What I've built:

* **Skill Trees:** Vis
ual guides to discover essential skills and concepts, specifically for Python developers working in advanced AI areas.
*
 **Quizzes:** Test your knowledge and identify gaps to improve your expertise in your focus areas.

I've built an MVP an
d would love your feedback to make this more useful, if you:

* Work with tools like LangChain,
* Dive into prompt engin
eering or Python AI/ML development,
* Or just want to see how this could help you grow.

**You’re welcome to try it out 
— It’s free:**

👉 [skill-up.io](https://www.skill-up.io/)

I hope it can be useful for you. If you like it, feel free to
 sign up to track your progress.

[AI and ML skill tree](https://preview.redd.it/q19oeb0ivu6e1.png?width=413&format=png&
auto=webp&s=503f0e762fa77833ade52cc53df6fcda0c3bdfdb)

I appreciate your feedback:

* Is the skill tree structure helpfu
l for navigating complex topics?
* Are the quizzes relevant and engaging?
* What features would you me to add to solve y
our pain points when learning Python and related techs?

I’d love to help you more! Let me know what you need and I’ll b
uild it. You can reach out by filling out [this form](https://www.notion.so/140ac95ae0208076972ef715f74c4429?pvs=21) or 
messaging me.
```
---

     
 
all -  [ [4 YoE, Python Developer, Data Scientist, Remote Worldwide] ](https://i.redd.it/qftuoo56cu6e1.png) , 2024-12-15-0915
```

```
---

     
 
all -  [ Langchain Integration ](https://www.reddit.com/r/AIlice/comments/1he4oby/langchain_integration/) , 2024-12-15-0915
```
Love the project, separately have been exploring RAG set ups through langchain and wondering if people know any approach
es that can be used to integrate Allice with that efficiently? 
```
---

     
 
all -  [ How to make SqlAgent to query NoSQL for answers? ](https://www.reddit.com/r/learnmachinelearning/comments/1he3ebg/how_to_make_sqlagent_to_query_nosql_for_answers/) , 2024-12-15-0915
```
I am new to ML.

LangChain has that with relational databases. How to make it work with NoSQL databases?
```
---

     
 
all -  [ I am sharing ChatGPT & AI courses and projects on YouTube
 ](https://www.reddit.com/r/ChatGPT/comments/1hdyje8/i_am_sharing_chatgpt_ai_courses_and_projects_on/) , 2024-12-15-0915
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

AI Tutorials
 (ChatGPT, LangChain & LLMs) -> [https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-Sh
N](https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ I am sharing Data Science & AI courses and projects on YouTube ](https://www.reddit.com/r/artificial/comments/1hdyirh/i_am_sharing_data_science_ai_courses_and_projects/) , 2024-12-15-0915
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

Data Science
 Full Courses & Projects -> [https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra\_5PGH&si=6WUpVwXeAKEs4tB6](
https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra_5PGH&si=6WUpVwXeAKEs4tB6)

AI Tutorials (OpenAI, LangCha
in & LLMs) -> [https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN](https://youtube
.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ Frustrated. Should I change my career? ](https://www.reddit.com/r/technepal/comments/1hdwai2/frustrated_should_i_change_my_career/) , 2024-12-15-0915
```
Few years ago I started with Python. Until now I have learned almost eveything I felt required SQL, Pandas, Numpy, Matpl
otlib, Langchain, AWS, Fastapi, Tensorflow and many more. Still I am not even getting  glimpse of finding a job. Thought
 I could get into AI, ML, Data Science of not at least Data Analytics. I have contacted every person. Most of them tell 
that it's difficult to find internship in these fields. Without internship, how could I even start my professional life.
 Companies open vacancies for seniors. 

  At current, I am studying CSIT sixth sem. Most of you may think that it's too
 early. But what if I don't get job even after graduation. My college is useless. I don't even rely on it. Just thinking
 if it is better to go in web development with python or some other areas. If not, the last option that resorts is quick
ly head off to abroad. I see nothing to stay here.
```
---

     
 
all -  [ Made a simple processor for building systems like Anthropic's artifacts/v0.dev ](https://www.reddit.com/r/LangChain/comments/1hdufsv/made_a_simple_processor_for_building_systems_like/) , 2024-12-15-0915
```
Built this small tag processor after wanting to quickly prototype systems similar to Anthropic's artifacts or v0.dev. No
t trying to recreate them, just wanted something lightweight that lets you quickly build and experiment with similar ide
as.

Basic example:

    typescriptCopyconst processor = new FluffyTagProcessor();
    
    // Handle regular conversati
on
    processor.setUntaggedContentHandler(content => {
        console.log(content); 
    // Normal conversation flows

    });
    
    // Handle artifacts/special blocks
    processor.registerHandler('artifact', {
        handler: (attrs,
 content) => {
            createArtifact(attrs.type, content);
        }
    });

Works with streaming APIs out of the 
box, so you can build interactive systems that update in real-time. About 4KB, no dependencies.

Mainly sharing in case 
others want to experiment with similar systems. TypeScript and Python versions: [github repo](https://github.com/m-ahmed
-elbeskeri/FluffyTagProcessor/tree/main?tab=readme-ov-file)
```
---

     
 
all -  [ [Student] Non-Target CS Student looking for Summer 2025 Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hdpaec/student_nontarget_cs_student_looking_for_summer/) , 2024-12-15-0915
```
[I am having little luck with applying to Summer 2025 internships related to software engineering, and I've currently ap
plied to around 400 places. I know the market is pretty bad right now, but just wanted to make sure my resume was optima
l for getting me interviews, cause right now I have gotten mostly nothing from online applications \(Had an interview fr
om my school's career fair\). Any advice would be greatly appreciated.](https://preview.redd.it/qnc9d2sc7p6e1.png?width=
5100&format=png&auto=webp&s=68f0c23f6576eb216c1f4c5fdc6190e2aa9dba60)


```
---

     
 
all -  [ Modularizing AI workflows in production ](https://www.reddit.com/r/LangChain/comments/1hdm37i/modularizing_ai_workflows_in_production/) , 2024-12-15-0915
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

     
 
all -  [ Avoid sending messages at the same time ](https://www.reddit.com/r/LangChain/comments/1hdlx5e/avoid_sending_messages_at_the_same_time/) , 2024-12-15-0915
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

     
 
all -  [ why my agent is not calling the tools  help me to fix this .. ](https://www.reddit.com/r/node/comments/1hdllox/why_my_agent_is_not_calling_the_tools_help_me_to/) , 2024-12-15-0915
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

     
 
all -  [ why my agent is not calling the tools please help me to fix this  .. ](https://www.reddit.com/r/LangChain/comments/1hdksj8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-15-0915
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

     
 
all -  [ why my agent is not calling the tools please help me to fix this  ,  ](https://www.reddit.com/r/Bard/comments/1hdkqi8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-15-0915
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

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1hdjv70/advance_your_career_100_free_certified_courses_on/) , 2024-12-15-0915
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
 ](https://www.reddit.com/r/OpenSourceeAI/comments/1hdgunu/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-15-0915
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

     
 
all -  [ Langgraph Persistence memory: InvalidSqlStatementName ](https://www.reddit.com/r/LangChain/comments/1hdbvre/langgraph_persistence_memory/) , 2024-12-15-0915
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

     
 
all -  [ A Personalized Academic Companion - AI Agent ](https://open.substack.com/pub/diamantai/p/atlas-when-artificial-intelligence?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) , 2024-12-15-0915
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

     
 
all -  [ How to extract Title/Heading/Chapter Name from the PDF ](https://www.reddit.com/r/LangChain/comments/1hdbeeo/how_to_extract_titleheadingchapter_name_from_the/) , 2024-12-15-0915
```
I am working on a RAG Pipeline, in which I am extracting PDF and store in the mongo. When I perform a query, it responds
 with a specific answer. Now I want to add Page Number and Title OR Chapter name OR heading of the title in the response
.

I am trying to fetch but it is not that much accurate. Anyone having a good approach ?
```
---

     
 
all -  [ What is best practice for follow-up questions? ](https://www.reddit.com/r/Rag/comments/1hdaf2y/what_is_best_practice_for_followup_questions/) , 2024-12-15-0915
```
I am implementing Ai agent, and feeding it with some scraped data, i am using Langchain alongside with express.js, from 
your experience what is low cost and effective solution to handle follow up questions in rag? I read langchain docs but 
they are suggesting to make another LLM call which may be costly, is there any appropriate practice for it which really 
works, please share your experience, any material or web resource will be appreciated 
```
---

     
 
all -  [ Qdrant DB Retriever issue ](https://www.reddit.com/r/LangChain/comments/1hd9oz8/qdrant_db_retriever_issue/) , 2024-12-15-0915
```
Previously I have used Chroma DB now I wold like to use Qdrant db

I have uploaded my docs to qdrant db using qdrant cli
ent through langchain framework, created a collection name and assigned hugging face embedding model now now I’m not abl
e to retrieve the query using .query method which was previously used in chroma DB I would like to know different modes 
of search’s supported by qdrantvectorstore

can any one guide me or share any links 
```
---

     
 
all -  [ How to return tool output directly without sending it to LLM again from a Langgraph Agent ? ](https://www.reddit.com/r/LangChain/comments/1hd9cc4/how_to_return_tool_output_directly_without/) , 2024-12-15-0915
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
 ](https://www.reddit.com/r/OpenAI/comments/1hd6x21/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-15-0915
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

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison ](https://www.reddit.com/r/LangChain/comments/1hd6w5x/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-15-0915
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

     
 
all -  [ AI Companion ](https://www.reddit.com/r/LangChain/comments/1hd6fo6/ai_companion/) , 2024-12-15-0915
```
We trying to develop a bot for people to talk when feeling lonely. I came by such a bot which is already very popular na
med Replica. Is there any other such bots which are already in use? Anyone knows which latest LLM Replica is using in th
e backend?
```
---

     
 
all -  [ My ideal development wishlist for building AI apps ](https://www.reddit.com/r/LangChain/comments/1hd62k6/my_ideal_development_wishlist_for_building_ai_apps/) , 2024-12-15-0915
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

     
 
all -  [ Aider + langchain: A match made in heaven? ](https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider_langchain_a_match_made_in_heaven/) , 2024-12-15-0915
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

     
 
all -  [ Token limit challenge with large tool/function calling response ](https://www.reddit.com/r/LangChain/comments/1hcwrzk/token_limit_challenge_with_large_toolfunction/) , 2024-12-15-0915
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

     
 
all -  [  CommanderAI / LLM-Driven Action Generation on Windows with Langchain (openai) ](https://www.reddit.com/r/OpenAIDev/comments/1hcwok1/commanderai_llmdriven_action_generation_on/) , 2024-12-15-0915
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

     
 
all -  [ multi RAG issue ](https://www.reddit.com/r/LangChain/comments/1hcvpmy/multi_rag_issue/) , 2024-12-15-0915
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

     
 
all -  [ How to clone any Twitter personality into an AI (your move, Elon) 🤖 ](https://www.reddit.com/r/LangChain/comments/1hcrjfp/how_to_clone_any_twitter_personality_into_an_ai/) , 2024-12-15-0915
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

     
 
all -  [ What happened to Conversational Retrieval QA? ](https://www.reddit.com/r/LangChain/comments/1hcpf6v/what_happened_to_conversational_retrieval_qa/) , 2024-12-15-0915
```
Once upon a time in the v0.1 days there was this idea of \[Conversational Retrieval QA\](https://js.langchain.com/v0.1/d
ocs/modules/chains/popular/chat\_vector\_db\_legacy/).  You can see the docs on this webpage, but if you click the link 
to go to the current stable version it doesn't seem to exist anymore.

Does anyone know if this got absorbed into someth
ing else less obvious or did they just drop support for it?
```
---

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/learnmachinelearning/comments/1hcp5ht/not_able_to_generate_embeddings/) , 2024-12-15-0915
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

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/generativeAI/comments/1hcp3y0/not_able_to_generate_embeddings/) , 2024-12-15-0915
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

     
 
all -  [ Any alternatives to LangChain for LLMs/GraphRAG on RDF graphs? ](https://www.reddit.com/r/KnowledgeGraph/comments/1hcozn1/any_alternatives_to_langchain_for_llmsgraphrag_on/) , 2024-12-15-0915
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

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/Entrepreneur/comments/1hcm180/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-15-0915
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

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/microsaas/comments/1hckxwo/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-15-0915
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

     
 
all -  [ I made a free directory of Agentic Tools ](https://www.reddit.com/r/LangChain/comments/1hckonl/i_made_a_free_directory_of_agentic_tools/) , 2024-12-15-0915
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

     
 
all -  [ as a fresher can i write this under my name in resume. ](https://www.reddit.com/r/IndiaTech/comments/1hcjnml/as_a_fresher_can_i_write_this_under_my_name_in/) , 2024-12-15-0915
```
also i have 3 months of work experience is it even countable as experience

https://preview.redd.it/yvdm7njsre6e1.png?wi
dth=1180&format=png&auto=webp&s=f585ecfc8b94952eecaf9c7efbaf787e0b101209


```
---

     
 
all -  [ A way in langgraph to find if the execution is completed ](https://www.reddit.com/r/LangChain/comments/1hcj99u/a_way_in_langgraph_to_find_if_the_execution_is/) , 2024-12-15-0915
```
Iam building a workflow which asks for human input for onboarding, I want to know in some way that the execution is comp
leted or ongoing so that i can use it to switch to next workflow. How can i achieve this by using interupts or by using 
a state variable
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-15-0915
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

     
