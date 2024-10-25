 
all -  [ Fixing Langchain.js's ToolCallingAgentOutputParser Error with Ollama LLM and a Custom Tool ](https://www.reddit.com/r/MailDevNetwork/comments/1gbf79d/fixing_langchainjss_toolcallingagentoutputparser/) , 2024-10-25-0913
```
&#x200B;

https://preview.redd.it/25s1rc2m5swd1.png?width=1024&format=png&auto=webp&s=35a587bd303daaf6b8e7fd8709c5394189
9b3058

   


## Understanding and Fixing ToolCallingAgentOutputParser Errors in Langchain.js

&#x200B;

https://preview
.redd.it/92oj3izm5swd1.jpg?width=1154&format=pjpg&auto=webp&s=47a67415154f9d91a45caa707340c900aa1bc6be

&#x200B;

When w
orking with **Langchain**.js v2, developers often aim to create efficient agents using custom tools and language models 
like Ollama. However, integrating these components can sometimes lead to errors that are difficult to debug.

One such e
rror is the 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output,' which can occur when buil
ding a custom tool within the agent framework. Understanding the root cause of this issue is crucial to ensure the agent
 and tool work correctly.

This article explores a simple implementation of a custom tool that adds 2 to a number input,
 using Langchain's createToolCallingAgent and the Ollama model. By analyzing the error and its context, we can better gr
asp how to troubleshoot it.

The following sections will guide you through the code, explain the error, and provide solu
tions to address this problem. Whether you're new to Langchain.js or experienced, this guide will help you move past thi
s issue efficiently.

  


https://preview.redd.it/g60hygyq5swd1.png?width=770&format=png&auto=webp&s=22604a722b406efeda
e80b26cac23493483239e1

&#x200B;

### Understanding the Custom Tool and Agent Error Handling in Langchain.js

&#x200B;


https://preview.redd.it/rv42ibon5swd1.jpg?width=1125&format=pjpg&auto=webp&s=886d2b2c1a5e29ee3c8a17f3f8dc5b5d8ab52a83

&
#x200B;

In the example provided, we are working with Langchain.js v2 to create a custom tool that integrates with the *
*Ollama** language model. The main purpose of the tool is to perform a simple mathematical operation: adding 2 to the in
put value. The tool is built using Langchain’s **tool** function, which defines reusable functions that can be invoked b
y an agent. To ensure the tool works correctly, the input schema is validated with the Zod library, guaranteeing that th
e input is a valid number. This ensures proper error handling and prevents the tool from failing due to invalid inputs.


The custom tool is then incorporated into an agent using the **createToolCallingAgent** function. This command allows t
he agent to call the tool when needed, and the agent is powered by the Ollama model, which is configured with specific p
arameters such as temperature to control the creativity of the responses. To facilitate smooth interaction between the a
gent and the tool, a chat prompt template is used. This template organizes the conversation by defining different types 
of messages, such as system messages, human input, and placeholders. The placeholders, such as **MessagesPlaceholder**, 
allow the conversation to be dynamic, with elements like the chat history being included.

One of the key issues address
ed in this example is the error handling around the Langchain agent's output parsing. The error message 'parseResult on 
ToolCallingAgentOutputParser only works on ChatGeneration output' stems from a mismatch between the type of output expec
ted by the parser and the actual output generated. To handle this error, the custom tool is wrapped in robust logic, ens
uring that all inputs and outputs conform to expected formats. This is further managed by the **AgentExecutor** class, w
hich coordinates the execution of the agent and tools, making sure that the query and tool output are properly synchroni
zed.

Finally, the scripts implement asynchronous execution using **await**, allowing the system to handle operations wi
thout blocking other processes. The agent waits for the tool to return its result before proceeding, ensuring that the r
esponse is both accurate and timely. Additionally, unit tests are included to validate the tool's functionality, ensurin
g that it consistently produces the correct output. These tests not only confirm the tool’s mathematical operation but a
lso check how well it handles invalid input, improving the overall reliability of the solution. This modular and error-r
esistant design makes the scripts reusable and effective for various applications within Langchain.js.

### Fixing the L
angchain.js Error with Modular Approach

&#x200B;

https://preview.redd.it/vzhle79o5swd1.jpg?width=1125&format=pjpg&auto
=webp&s=53a00eddcdf8d55c69f06e09feef2ecfa3e8d2ac

&#x200B;

Solution 1: JavaScript with modular approach and error handl
ing using Langchain.js and Ollama LLM

  


https://preview.redd.it/1un0bpfr5swd1.png?width=770&format=png&auto=webp&s=d
ebc0f320eee837df3b429964af11783593bb87c

&#x200B;

    import { tool } from '@langchain/core/tools';
    import { z } fr
om 'zod';
    import { Ollama } from '@langchain/ollama';
    import { ChatPromptTemplate } from '@langchain/core/prompt
s';
    import { createToolCallingAgent } from 'langchain/agents';
    import { AgentExecutor } from 'langchain/agents';

    // Initialize LLM with Ollama
    const llm = new Ollama({
    model: 'llama3',
    temperature: 0.7,
    });
    /
/ Custom tool to add 2 to the input number
    const magicTool = tool(
    async (input) => {
    return input + 2;
    
},
    {
    name: 'magic_function',
    description: 'Applies a magic function to an input',
    schema: z.object({ inp
ut: z.number() }),
    };
    );
    const tools = [magicTool];
    // Setup ChatPromptTemplate with placeholders
    co
nst prompt = ChatPromptTemplate.fromMessages([
    ['system', 'You are a helpful assistant called iHelp'],
    ['placeho
lder', '{chat_history}'],
    ['human', '{input}'],
    ['placeholder', '{agent_scratchpad}'],
    ]);
    // Agent conf
iguration
    const agent = createToolCallingAgent({ llm, tools, prompt });
    // Execute agent query
    const agentEx
ecutor = new AgentExecutor({ agent, tools });
    const query = 'What is the value of magic_function(3)?';
    await age
ntExecutor.invoke({ input: query });

### Enhanced Error Handling for Langchain.js Agent

&#x200B;

https://preview.redd
.it/8dnx85uo5swd1.jpg?width=1125&format=pjpg&auto=webp&s=8f53e33e08c7f78293a561e99ddb195598550338

&#x200B;

Solution 2:
 Error handling with unit tests to validate the custom tool's output in Langchain.js

  


https://preview.redd.it/ncpxq
wsr5swd1.png?width=770&format=png&auto=webp&s=cbf1ec679ffd93a951be5fde0c1328f7b32d2f9e

&#x200B;

    import { tool } fr
om '@langchain/core/tools';
    import { z } from 'zod';
    import { Ollama } from '@langchain/ollama';
    import { cr
eateToolCallingAgent } from 'langchain/agents';
    import { AgentExecutor } from 'langchain/agents';
    // Initialize 
LLM with Ollama
    const llm = new Ollama({ model: 'llama3', temperature: 0.7 });
    // Custom tool with added error h
andling
    const magicTool = tool(
    async (input) => {
    try {
    if (typeof input !== 'number') throw new Error(
'Invalid input type!');
    return input + 2;
    } catch (err) {
    return err.message;
    }
    },
    {
    name: '
magic_function',
    description: 'Adds 2 to input and handles errors',
    schema: z.object({ input: z.number() }),
   
 }
    );
    const tools = [magicTool];
    // Agent and execution
    const agent = createToolCallingAgent({ llm, tool
s });
    const agentExecutor = new AgentExecutor({ agent, tools });
    const query = 'magic_function('abc')'; // Test 
with invalid input
    await agentExecutor.invoke({ input: query });
    // Unit test example
    import { expect } from
 'chai';
    it('should return 5 when input is 3', async () => {
    const result = await magicTool(3);
    expect(resul
t).to.equal(5);
    });

### Exploring the Role of Agents in Langchain.js and Ollama LLM Integration

&#x200B;

https://
preview.redd.it/zzqgr6fp5swd1.jpg?width=1125&format=pjpg&auto=webp&s=c4fd1a130466b3ce19222a181bed36e6f8b70514

&#x200B;


When working with Langchain.js, integrating **agents** with tools and language models like Ollama is a critical aspect 
of building dynamic applications. An agent allows you to connect a custom tool, which performs specific tasks, to a lang
uage model, which handles more conversational or generative tasks. By using agents, developers can automate workflows wh
ere a model not only generates responses but also invokes tools to perform calculations or data processing.

The key com
ponent in this integration is the **createToolCallingAgent** function. This function lets the agent trigger specific too
ls when necessary, ensuring that tasks are completed accurately and efficiently. While the primary focus is often on cre
ating the tool itself, understanding how to manage the agent's workflow and avoid parsing errors is equally important. E
rrors like 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output' usually occur when the agen
t's output isn't compatible with the parsing system, highlighting the need for proper alignment between the agent’s outp
ut and the expected format.

The use of prompt templates, such as **ChatPromptTemplate**, further enriches the interacti
on by allowing dynamic messages and context placeholders. This allows the agent to adjust its responses based on the cha
t history or the agent’s scratchpad. Optimizing the prompt templates and ensuring the agent's outputs are correctly pars
ed can prevent many common errors, making your Langchain.js applications more reliable and efficient.

#### Frequently A
sked Questions About Langchain.js, Agents, and Tools

&#x200B;

https://preview.redd.it/pvpvrb0q5swd1.jpg?width=1155&for
mat=pjpg&auto=webp&s=319ff3e15b969c2a8994adf870969bc6ce083a36

&#x200B;

What is an agent in Langchain.js?

An agent is 
a component that interacts with tools and language models to perform specific tasks based on a user query. It uses the *
*createToolCallingAgent** function to trigger tools.

How do you resolve the 'parseResult on ToolCallingAgentOutputParse
r' error?

This error occurs when the agent's output is incompatible with the parser. Ensure the output matches what the
 parser expects and use a **ChatGeneration** output format.

What is the purpose of the **AgentExecutor**?

The **AgentE
xecutor** manages the execution of the agent and its tools, allowing you to run complex workflows in Langchain.js applic
ations.

How does **ChatPromptTemplate** work?

**ChatPromptTemplate** organizes chat messages in a structured format, a
llowing for dynamic content such as chat history and agent scratchpad to be inserted into the conversation flow.

Why is
 **Zod** used in the tool?

**Zod** is used for input validation, ensuring that the input to the custom tool is of the c
orrect type (e.g., a number), which reduces the chances of errors.

#### Final Thoughts on Error Handling in Langchain.j
s

&#x200B;

https://preview.redd.it/zo3vhblq5swd1.jpg?width=1155&format=pjpg&auto=webp&s=cbd875f11336a2ae96df0616433a1c
7d4bfad09e

&#x200B;

Solving the 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output' erro
r requires careful alignment between the output of your agent and its parsing expectations. With the right approach, thi
s error can be avoided.

By using appropriate tools like **Zod** for validation and ensuring that agents, such as those 
built with Ollama, handle inputs and outputs correctly, you can create robust solutions in **Langchain**.js without enco
untering parsing issues.

###### Sources and References for Langchain.js Error Resolution

Elaborates on the official La
ngchain documentation, which provides insights into tool creation and agent configurations. [**Langchain Documentation**
](https://docs.langchain.com/) Inside.

Further explains the use of Zod for input validation and its application in Lang
chain.js. [**Zod Documentation**](https://zod.dev/) Inside.

Describes the Ollama language model and its implementation 
within custom agents. [**Ollama LLM**](https://ollama.ai/) Inside.

[**Fixing Langchain.js's ToolCallingAgentOutputParse
r Error with Ollama LLM and a Custom Tool**](https://www.tempmail.us.com/en/langchain/fixing-langchain-js-s-toolcallinga
gentoutputparser-error-with-ollama-llm-and-a-custom-tool)  
 
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1gbc5qo/list_of_free_and_best_selling_discounted_courses/) , 2024-10-25-0913
```
# Udemy Free Courses for 25 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20820/)Open-source LLMs: Uncensored & secure AI l
ocally with RAG
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20819/)AI-Agents: Automation & Business with LangCha
in & LLM Apps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20818/)How to Become an Embedded Systems Engineer Boot
camp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20817/)Herramientas de Google 2024, ¡Desde Cero Hasta Experto!

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20816/)Coaching program – Become the Woman of Your Life!
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20815/)Practice Exams | AWS Certified Solutions Architect Associate
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20814/)Staff Engineer Survival Manual: AI Era Technical Leadership
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/20813/)Curso de microservicios con Spring Boot y Spring Cloud
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/20812/)Curso Completo de Kubernetes Desde Cero para Programadores
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20811/)Tiktok Ads marketing Crash Course For Beginners (Hindi/Urdu)
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20810/)Google Ads And Tiktok Ads Crash Course (Hindi/ Urdu)
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20809/)Tiktok Marketing & Shopify Ecommerce store (hindi/urdu)
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20808/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hindi 2023
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20807/)Digital Marketing Business With Google My Business
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/20806/)Google Ads Mastery\~ Beginner To Pro \~ HINDI/URDU 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20805/)Facebook Ads Marketing Funnel For Ecommerce Hindi
* Secret Facebook Ads Targeting Pro Stratigies 2023 In Hindi
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/20804/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20803/)Est
rategias Pro de Targeting de Audiencia con Facebook Ads
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20802/)Marke
ting en Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20801/)700-7
55: Cisco Security Sales Specialist Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20800/)Configuración y Opti
mizacion de tu Página de Facebook 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20799/)Facebook Ads & Ecommer
ce Easy Course 2023 Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20798/)Essential Photoshop Course Beginner
 to Intermediate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20797/)Basic to Advanced T-shirt Design with Adobe 
Photoshop CC
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20796/)Certification in Welding Technology for Engineer
s – CWI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20795/)Facebook Ads Marketing In Hindi/Urdu 2023
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20794/)Easy Instagram Marketing In Hindi
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/20793/)Como crear y configurar tu canal de Youtube desde cero 2023
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20792/)Data Structures and OOP with C++ : CS104, CS105 Masterclass
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/20791/)1Z0-1104-23: Oracle Security Professional Practice Exam
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/20790/)Generative AI for Beginners: Future of Innovation Unlocked
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/20789/)700-760: Cisco IoT Advantage Sales Specialist Exam
* Canva Design Crash Course
* [REDEEM OFFER](https://idow
nloadcoupon.com/udemy/20788/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20787/)Lightroom Classic CC: Master th
e Library & Develop Module
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20786/)Adobe Illustrator for Everyone: De
sign Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20785/)CEH v12 Certification Practice Questions 2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20784/)AWS Certified AI Practitioner (AIF-C01) Practice Exam 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20783/)AZ-900: Microsoft Azure Fundamentals Practice Questions 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20782/)PCAP Certified Associate Python Programmer Practice Exam
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/20781/)MS Word – Microsoft Word Course Beginner to Expert
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/20780/)45-Day ESP32 Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20
779/)CompTIA Cloud+ (CV0-004): Complete Exam Prep & Cloud Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20
778/)AWS Certified AI Practitioner: Exam Prep & AI Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20777
/)AWS Certified Cloud Practitioner: Exam Prep & Cloud Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20776/
)Linux Command-Line & Shell Scripting for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20775/)
Introduction to AI and ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20774/)Arduino 4 Seven Segments Displ
ay Interfacing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20773/)Introduction to ARM Cortex-M Architecture
* Be
st Prompt Engineering Practice Tests & Interview Questions
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20772/)
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/20771/)Cloud Computing Masterclass – Deployment to Administration
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20770/)AI Governance Professional (AIGP) Certification & AI Mastery
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20769/)CGRC – Governance, Risk and Compliance Certification Mastery
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20768/)HSE Certification – ISO 14001 & OHSAS 18001
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20767/)NVIDIA-Certified Associate: AI Infrastructure and Operations
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20766/)Mastering C++ Fundamentals with Generative AI: A Hands-On
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20765/)Java Mastery Intermediate: Methods, Collections, and Beyond
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/20764/)Mastering Advanced Java with Object-Oriented Programming
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20763/)Generative AI for Dynamic Java Web Applications with ChatGPT
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20762/)Mastering Tabnine AI for Efficient Code Development
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/20761/)Android Projects Course Build 3 Applications from Scratch
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/20760/)Android Apps Development in Hindi and Build 10 Applications
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20759/)Android Very Basic App Development Course with Java in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20758/)Zero Coding Website with Google Sites
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20757/)Unders
tanding Hair Color Foundations
* The Ultimate C Programming Practice Test-600+ Questions
* [REDEEM OFFER](https://idownl
oadcoupon.com/udemy/20756/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20755/)SQL- The Complete Introduction to
 SQL programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20754/)07 Days of Code | Python Programming BootCam
p
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20753/)Excel Tips and trick : Learn MS Excel by making 7 Projects

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20752/)Python for Data Science with Assignments
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20751/)C++ And PHP Complete Course for C++ and PHP Beginners
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/20750/)NSE5\_FMG-7.2: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/20749/)Currency Management for Small Businesses & Corporates
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20748/)Entrenamiento Visual FoxPro 9 y MariaDB -Mod01
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/20747/)Visual FoxPro – Clases Visuales (nueva versión)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20746/)E
ntrenamiento Visual FoxPro 9 y MySQL Server -Mod02
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20745/)Entrenamie
nto Visual FoxPro 9 y PostgreSQL -Mod01
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20744/)Tarea 01 Clases Visua
les y otras Herramientas – VFP Avanzado
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20743/)Complete JS Bootcamp 
| JavaScript Programming in 7 DAYS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20742/)Theoretical Foundations of
 AI in Cybersecurity
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20741/)Principles and Practices of the Generati
ve AI Life Cycle
* Principles of Governance in Generative AI
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20740/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20739/)Philosophy and Foundations of Artificial Intelligence (AI)
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/20738/)LATEST | Learn Advanced Python Programming | SOURCE CODE
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20737/)Introduction to Quantum Computing
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20736/)Certified Data Management Professional (CDMP) – Associate
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20735/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20734/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/20733/)Linode: Build a Scalable Blog App using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/20732/)Cloud Computing Essentials: Linode, Linux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
20731/)Configure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20730/
)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20729/)HTML, CSS, & Jav
aScript – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20728/)Linode: Build an
d Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20727/)Run Multiple Sites 
on a Cloud Server: AWS & Digital Ocean
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20726/)Build and Deploy Respo
nsive Websites on AWS using HTML & CSS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20725/)GetResponse email mark
eting for beginners
* Internet & Cloud Computing Foundations
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20724/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20723/)Cloud-Powered Web App Development with AWS and PHP
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/20722/)Introduction to Domain Names and Web Hosting – Quick Guide
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/20721/)How the Internet Works & the Web Development Process
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20720/)Setup a Virtual Web Server using Linode or Digital Ocean
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20719/)Build an Amazon Affiliate E-Commerce Store from Scratch
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20718/)Cloud Computing and Amazon Web Services (AWS) Fundamentals
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/20717/)AWS Identity and Access Management (IAM) Foundations
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20716/)Create a Members Only Blog using PHP, MySQL, & AJAX
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/20715/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
0714/)JavaScript & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20713
/)HTML, JavaScript, & Bootstrap – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20712/)Build 
a Simple Calculator in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20711/)300-415
: Cisco SD-WAN Solutions Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20710/)Amazon Elastic Co
mpute Cloud (EC2) Beginners Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20709/)Blockchain Professi
onal Certification
* Setup LAMP Stack on a Remote Cloud Server + PHP Foundations
* [REDEEM OFFER](https://idownloadcoupo
n.com/udemy/20708/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20707/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20706/)JavaScript, Bootstrap, & PHP – Certification for 
Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20705/)HTML, CSS, & Bootstrap – Certification Course for B
eginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20704/)The Complete Guide to Effective Communication Skills

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20703/)Digital Marketing Automation: One Step Ahead of Competitors

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20702/)Account-Based Marketing – ABM: Increase Your B2B Efficiency
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20701/)How to Create Your Perfect LinkedIn Outreach Campaign
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/20700/)Facebook Ads: Run Your First Ad Campaign
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20699/)Google My Business. How to Master Powerful Tool for Company
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20698/)Web Analytics with Similarweb: from Basic to PRO!
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/20697/)CDO Chief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20696/)Timeboxing: A Short and Practical Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20695/)Make a WordPr
ess Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20694/)Mastering SEO With ChatGPT: Ultima
te Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20693/)Implementing Agile Marketing and Marketin
g Sprints

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ RAG text to sql ](https://www.reddit.com/r/LangChain/comments/1gbc0pu/rag_text_to_sql/) , 2024-10-25-0913
```
Does anyone have any good tutorial that walks through generating sql queries based on vector store chunks of data?

The 
tutorials I see are sql generators based off of the actual db. This would be just based on text, markdown files and pdf 
chunks which house examples and data reference tables. 


```
---

     
 
all -  [ Suggestions for Video RAG Integration: Frame-by-Frame Analysis & Timestamp Queries ](https://www.reddit.com/r/LangChain/comments/1gb9lwx/suggestions_for_video_rag_integration/) , 2024-10-25-0913
```
Hey everyone! 👋

I’m currently working on a multimodal multi-query RAG system. So far, I’ve integrated:

Blogs 📝
Video S
ummaries 🎥
Audio 🎧
PDFs 📄
Images 🖼️
The next challenge I’m tackling is Video RAG — specifically, I want it to:

Understa
nd videos at specific timestamps
Analyze frame-by-frame content
Answer questions related to those timestamps
I’m looking
 for any suggestions or ideas on how I can enhance this video understanding part, especially with the timestamp and fram
e analysis. Any input or tips would be super helpful!

Thanks in advance! 🙌
```
---

     
 
all -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/MLQuestions/comments/1gb7kkt/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-10-25-0913
```

I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what h
e is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how 
to do it

Will this course teach me that or not?

Thanks in advance
```
---

     
 
all -  [ Multi Modal agents ](https://www.reddit.com/r/LangChain/comments/1gb66nh/multi_modal_agents/) , 2024-10-25-0913
```
Im trying to build a langgraph agent that call tools using input images. Struggling a bit with tool calling, has anyone 
implemented something similar. Code link or an article would be really helpful thankyou.
```
---

     
 
all -  [ AI agents market landscape map October 2024 edition ](https://i.redd.it/x7xwvyxhxowd1.png) , 2024-10-25-0913
```

```
---

     
 
all -  [ Best tutorial or tech stack for a production RAG chat bot ](https://www.reddit.com/r/LangChain/comments/1gb496k/best_tutorial_or_tech_stack_for_a_production_rag/) , 2024-10-25-0913
```
Hey folks

I’ve been tasked at work with a project that I have no idea how to even even get started. I’ve been asked to 
take the company handbooks and make a rag based chat bot around them so users can ask questions. I found a few tutorials
 online, but there seems to be a few different camps and approaches, I was wondering what are some best practises or if 
anyone has any good tutorials that would be good for a junior intermediate developer.

Ideally, I can deploy it on a sub
domain like chat.company.com

Right now it looks like the best approach is using streamlit for the chat interface. And t
hen python and Lang chain on the backend. Does this mean I can make it as a Django app?

Thank you so so much !

```
---

     
 
all -  [ AI Agent API & UI that's ready for Production ](https://www.reddit.com/r/AI_Agents/comments/1gb3uju/ai_agent_api_ui_thats_ready_for_production/) , 2024-10-25-0913
```
I've spent a lot of time prototyping with Langchain, LlamaIndex, and CrewAI but had trouble getting the agents into prod
uction for my users. I decided to build my own Agent Platform that supports multi-agent interaction, bring-your-own API 
keys, and bring-your-own Postgres for RAG tools. We're launched in private beta (w/ 3 paying customers) but would love s
ome more people to try it out and give feedback: [www.asteragents.com](http://www.asteragents.com) 

  
The key for me i
s building agents so they are non-deterministic and fully reasoning, rather than constrained to a graph / DAG / chain of
 prompts. I believe the future is reasoning agents that decide how and when to collaborate with each-other to accomplish
 tasks.
```
---

     
 
all -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-10-25-0913
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
 
all -  [ Bit of a long shot, but has anyone found a proper diagramming tool for AI architecture? ](https://www.reddit.com/r/LangChain/comments/1gb0axf/bit_of_a_long_shot_but_has_anyone_found_a_proper/) , 2024-10-25-0913
```
Been using the likes of Cloudairy for cloud diagrams lately, and it got me wondering - is there anything similar but pro
perly built for AI/ML architectures? Not just after fancy shapes mind you, but something that genuinely understands mode
rn AI systems.

**Current Faff:** Most diagramming tools seem rather stuck in the traditional cloud architecture mindset
. When I'm trying to map out things like:

* Multi-agent systems nattering away to each other
* Proper complex RAG pipel
ines
* Prompt chains and transformations
* Feedback loops between different AI bits and bobs
* Vector DB interactions

.
..I end up with a right mess of generic boxes and arrows that don't really capture what's going on.

**What I'm hoping m
ight exist:**

* Proper understanding of AI/ML patterns
* Clever ways to show prompt flows and transformations
* Perhaps
 some interactive elements to show data flow?
* Templates for common patterns (RAG, agent chains, and the like)
* Someth
ing that makes AI architecture diagrams look less of an afterthought

I know we can crack on with general tools like [dr
aw.io](http://draw.io/), Mermaid, or Lucidchart, but with all the AI tooling innovation happening these days, I reckon s
omeone must be having a go at solving this.

Has anyone stumbled across anything interesting in this space? Or are we st
ill waiting for someone to sort it out?
```
---

     
 
all -  [ Observation: Invalid Format: Missing 'Action:' after 'Thought:..........this error persists in REPL  ](https://www.reddit.com/r/LangChain/comments/1gazt04/observation_invalid_format_missing_action_after/) , 2024-10-25-0913
```
I am using a ZERO\_SHOT\_REACT\_DESCRIPTION , agent using different tools, in my python REPL tool which is used to creat
e a graph when necessary, I am extracting the image using base64 encoding or svg code (which are generated by the REPL t
ool itself). But in some case I am facing the issue --> Observation: Invalid Format: Missing 'Action:' . And returning -
-> 'Agent stopped due to time or iteration limit' .  Any suggestions on how to resolve this issue or why this issue is c
omming
```
---

     
 
all -  [ Ollama embedding: unsuccessful persist to disk and termination of program ](https://www.reddit.com/r/ollama/comments/1gayxsv/ollama_embedding_unsuccessful_persist_to_disk_and/) , 2024-10-25-0913
```
Hi, I am building a RAG application which should be able to give answer to user query based on a PDF file. The first ste
p in my code is to load this PDF file, do text chunking, embedding the text chunks with an embedding model pulled using 
Ollama, and save the generated embeddings to disk with Chroma.

The following is my code:

`from langchain_community.doc
ument_loaders import PyPDFLoader`

`from langchain.text_splitter import RecursiveCharacterTextSplitter`

`from langchain
_community.embeddings import OllamaEmbeddings`

`from langchain_community.vectorstores import Chroma`



`#create a new 
file named vectorstore in your current directory.`

`if __name__=='__main__':`



`loader=PyPDFLoader('test.pdf')`

`doc
s=loader.load()`

`text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)`

`splits = text_sp
litter.split_documents(docs)`

`print(len(splits))`

`persist_directory = 'ChromaDB_test_vector_database'`

`vectorstore
 = Chroma.from_documents(`

`documents = splits,` 

`embedding = OllamaEmbeddings(model='mxbai-embed-large', show_progre
ss=True),`

`# collection_name='local-rag',`

`persist_directory = persist_directory`

`)`

`print('finished')`

The pro
blem I encounter is, for some `chunk_size`, such as `chunk_size=800`, also I get 138 text chunks and with `show_progress
` I can see OllamaEmbeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████| 138/138 \[00:04<00:00, 30.09it/s\] embedding seemly successful, 'finished'
 is not printed and the chroma.sqlitee file in the `persist_directory` is really small. I don't get an error through. Th
is leads me to believe the embeddings somehow cannot be correctly persisted. Does someone know why it comes to this issu
e, and possible solutions? Thank you!
```
---

     
 
all -  [ looking for saas founders (bootstrapped or funded) of a gen AI product ](https://www.reddit.com/r/LangChain/comments/1gaxy7w/looking_for_saas_founders_bootstrapped_or_funded/) , 2024-10-25-0913
```
would like to start a series interviewing founders in the gen ai industry. you would benefit from free marketing (and ho
pefully insights and helpful advise) for your saas - we benefit by gaining authority in the gen-ai / SaaS industry and b
y learning what the market is up to. Ideally, you've built the project using LangChain and LangGraph.

Would love to con
nect with anyone that's interested.

 LinkedIn is on my profile FYI.

Thanks.
```
---

     
 
all -  [ Ollama community embedding stall after 2-27 chunks ](https://www.reddit.com/r/ollama/comments/1gaxy2z/ollama_community_embedding_stall_after_227_chunks/) , 2024-10-25-0913
```
I am using a GCP VM to host my Ollama bge-m3 then i use ip forwarding to connect it from local. Eventhough i can use Oll
ama embedding normally in Dify but i can't use it via langchain\_comunity.embedding lib. The embedding kept stalling aft
er 27 chunks (doc). 
```
---

     
 
all -  [ I can't see LangSmith traces when using LangChain + Amazon Bedrock ](https://www.reddit.com/r/LangChain/comments/1gaxrri/i_cant_see_langsmith_traces_when_using_langchain/) , 2024-10-25-0913
```
Hello,

I've been following the [LangChain documentation for tracing](https://docs.smith.langchain.com/how_to_guides/tra
cing/trace_with_langchain), but I cannot see my project in LangSmith, only the default one appears. Even when I haven't 
set a project name, nothing is being traced in the default project, which means LangSmith is not detecting my chain invo
cations. 

Could anyone assist me in tracing my invocations with LangSmith?
```
---

     
 
all -  [ Messy Unstructured Data : How do you handle it ? ](https://www.reddit.com/r/LangChain/comments/1gaxdk1/messy_unstructured_data_how_do_you_handle_it/) , 2024-10-25-0913
```
Our startup Unsiloed AI, is backed by Entrepreneur First which is one of the best startup accelerators globally based in
 Silicon Valley.

Currently, we are building next-generation AI-powered data warehouse to store, process, and query unst
ructured data like PDFs, websites, images, videos, and audio (Call Recordings). By making the impossible data possible, 
we help data teams become strategic enablers.

I would appreciate the opportunity to engage with data engineers/data sci
entists from US companies to learn more about how your team currently handles extracting insights from unstructured data
. Your insights would be invaluable to us.

Looking forward to connecting and gaining valuable insights from you. Thanks
!


```
---

     
 
all -  [ Aether: Your IDE For Prompt Engineering (Beta Currently Running!) ](https://www.reddit.com/r/LangChain/comments/1gaw5yl/aether_your_ide_for_prompt_engineering_beta/) , 2024-10-25-0913
```
I was recently trying to build an app using LLM’s but was having a lot of difficulty engineering my prompt to make sure 
it worked in every case while also having to keep track of what prompts did good on what.

So I built this tool that aut
omatically generates a test set and evaluates my model against it every time I change the prompt or a parameter. Given t
he input schema, prompt, and output schema, the tool creates an api for the model which also logs and evaluates all call
s made and adds them to the test set. You could also integrate the app into any workflow with just a couple lines of cod
e. 

https://reddit.com/link/1gaw5yl/video/pqqh8v65dnwd1/player

I just coded up the Beta and I'm letting a small set of
 the first people to sign up try it out at [the-aether.com](http://the-aether.com/) . Please let me know if this is some
thing you'd find useful and if you want to try it and give feedback! Hope I could help in building your LLM apps!
```
---

     
 
all -  [ Comparing KG generation across LLMs for cost & quality ](https://www.reddit.com/r/LangChain/comments/1garr4c/comparing_kg_generation_across_llms_for_cost/) , 2024-10-25-0913
```
Just posted this to our blog, and may be interesting to folks.

TL;DR: Gemini Flash 1.5 does a really nice job at low co
st. 

https://www.graphlit.com/blog/comparison-of-knowledge-graph-generation
```
---

     
 
all -  [ Resume Review Request for Data Analyst Position ](https://www.reddit.com/r/Resume/comments/1gakxrp/resume_review_request_for_data_analyst_position/) , 2024-10-25-0913
```
Hey everyone,

I recently started applying for jobs and want to make sure my resume is up to the mark. I’m not entirely 
sure if it effectively highlights my skills and experiences or if it’s aligned with what recruiters are looking for. Cou
ld I get some feedback or advice on improving it? Any tips or suggestions would be super helpful!

Thanks in advance!

h
ttps://preview.redd.it/actn0y45jkwd1.png?width=956&format=png&auto=webp&s=7901adf906591f788e15b3c6ddd47003414056b7


```
---

     
 
all -  [ AutoGen v0.2.37 released ](https://www.reddit.com/r/AutoGenAI/comments/1gah8nn/autogen_v0237_released/) , 2024-10-25-0913
```
[New release: v0.2.37](https://github.com/microsoft/autogen/releases/tag/v0.2.37)

# What's Changed

* Use trusted publi
sher for pypi release by [@jackgerrits](https://github.com/jackgerrits) in [\#3596](https://github.com/microsoft/autogen
/pull/3596)
* Fix typos in Cerebras doc by [@henrytwo](https://github.com/henrytwo) in [\#3590](https://github.com/micro
soft/autogen/pull/3590)
* Add blog post announcing the new architecture preview by [@jackgerrits](https://github.com/jac
kgerrits) in [\#3599](https://github.com/microsoft/autogen/pull/3599)
* Update PR link in blog post by [@jackgerrits](ht
tps://github.com/jackgerrits) in [\#3602](https://github.com/microsoft/autogen/pull/3602)
* Create CI to tag issues with
 needs triage by [@jackgerrits](https://github.com/jackgerrits) in [\#3605](https://github.com/microsoft/autogen/pull/36
05)
* Update issue templates by [@jackgerrits](https://github.com/jackgerrits) in [\#3610](https://github.com/microsoft/
autogen/pull/3610)
* Fix small typo in the docs by [@jknaudt21](https://github.com/jknaudt21) in [\#3650](https://github
.com/microsoft/autogen/pull/3650)
* Update 0.2 CI to target branch, remove merge queue by [@jackgerrits](https://github.
com/jackgerrits) in [\#3656](https://github.com/microsoft/autogen/pull/3656)
* Update BaseUrl of docusaurus site by [@ja
ckgerrits](https://github.com/jackgerrits) in [\#3658](https://github.com/microsoft/autogen/pull/3658)
* Add announcemen
t bar for 0.4 by [@jackgerrits](https://github.com/jackgerrits) in [\#3717](https://github.com/microsoft/autogen/pull/37
17)
* Update links on 0.2 website by [@jackgerrits](https://github.com/jackgerrits) in [\#3734](https://github.com/micro
soft/autogen/pull/3734)
* Function Calling Support for Gemini - Part 2 by [@luxzoli](https://github.com/luxzoli) in [\#3
726](https://github.com/microsoft/autogen/pull/3726)
* Fix [\#2643](https://github.com/microsoft/autogen/issues/2643) \-
 groupchat model registration by [@Matteo-Frattaroli](https://github.com/Matteo-Frattaroli) in [\#2696](https://github.c
om/microsoft/autogen/pull/2696)
* Added a demonstartion notebook featuring the usage of Langchain with AutoGen by [@Kiru
shikesh](https://github.com/Kirushikesh) in [\#3461](https://github.com/microsoft/autogen/pull/3461)
* Autobuild Functio
n calling by [@krishnashed](https://github.com/krishnashed) in [\#3238](https://github.com/microsoft/autogen/pull/3238)

* Update Docs to Point to 0.4 by [@victordibia](https://github.com/victordibia) in [\#3764](https://github.com/microsoft
/autogen/pull/3764)
* Notebook on web crawling by [@WilliamEspegren](https://github.com/WilliamEspegren) in [\#2720](htt
ps://github.com/microsoft/autogen/pull/2720)
* Fix link to v0.4 documentation by [@ekzhu](https://github.com/ekzhu) in [
\#3772](https://github.com/microsoft/autogen/pull/3772)
* Remove path filter for website testing in 0.2 by [@jackgerrits
](https://github.com/jackgerrits) in [\#3782](https://github.com/microsoft/autogen/pull/3782)
* Fix broken image URL in 
README by [@gagb](https://github.com/gagb) in [\#3776](https://github.com/microsoft/autogen/pull/3776)
* Clarify stable 
package name and version on home page by [@jackgerrits](https://github.com/jackgerrits) in [\#3775](https://github.com/m
icrosoft/autogen/pull/3775)
* Fix CTA button alignment in docs home page by [@victordibia](https://github.com/victordibi
a) in [\#3788](https://github.com/microsoft/autogen/pull/3788)
* K8s code executor by [@questcollector](https://github.c
om/questcollector) in [\#3419](https://github.com/microsoft/autogen/pull/3419)
* Add Couchbase Vector DB Example Noteboo
k and Minor Bug Fix by [@lokesh-couchbase](https://github.com/lokesh-couchbase) in [\#3804](https://github.com/microsoft
/autogen/pull/3804)
* Add Zep ecosystem doc and notebook by [@danielchalef](https://github.com/danielchalef) in [\#3681]
(https://github.com/microsoft/autogen/pull/3681)
* \[bug\] Changes Text Cache Default to None by [@WaelKarkoub](https://
github.com/WaelKarkoub) in [\#3872](https://github.com/microsoft/autogen/pull/3872)
* \[bug\] Validates If The Role Tool
 is Handled Correctly after Transforms by [@WaelKarkoub](https://github.com/WaelKarkoub) in [\#3875](https://github.com/
microsoft/autogen/pull/3875)
* \[CAP\] Abstraction of actor\_connector to go along with runtime factory and runtime abst
raction by [@rajan-chari](https://github.com/rajan-chari) in [\#3296](https://github.com/microsoft/autogen/pull/3296)

#
 New Contributors

* [@jknaudt21](https://github.com/jknaudt21) made their first contribution in [\#3650](https://github
.com/microsoft/autogen/pull/3650)
* [@Matteo-Frattaroli](https://github.com/Matteo-Frattaroli) made their first contribu
tion in [\#2696](https://github.com/microsoft/autogen/pull/2696)
* [@WilliamEspegren](https://github.com/WilliamEspegren
) made their first contribution in [\#2720](https://github.com/microsoft/autogen/pull/2720)
* [@questcollector](https://
github.com/questcollector) made their first contribution in [\#3419](https://github.com/microsoft/autogen/pull/3419)
* [
@danielchalef](https://github.com/danielchalef) made their first contribution in [\#3681](https://github.com/microsoft/a
utogen/pull/3681)

**Full Changelog**: [v0.2.36...v0.2.37](https://github.com/microsoft/autogen/compare/v0.2.36...v0.2.3
7)
```
---

     
 
all -  [ Best Approach to Building a Chatbot with Twitter Data Using LLMs (LLaMA 3.2)? ](https://www.reddit.com/r/datascienceproject/comments/1gafune/best_approach_to_building_a_chatbot_with_twitter/) , 2024-10-25-0913
```
**Hello everyone,**

I'm currently working on analyzing customer support inquiries from various insurance companies and 
generating questions from these tweets using LLaMA 3.2. The dataset includes both full conversation and tweet-level form
ats, containing customer support inquiries.

Now, I'm looking to take it a step further and build a chatbot that can:

1
. Answer customer queries based on the patterns found in the historical tweets. (Currently doing manually)
2. Utilize th
e questions I've already generated.
3. Learn from ongoing interactions with users to improve its responses over time.

G
iven the data I have and my experience working with LLMs, what would be the best way to approach building this chatbot? 
Here are a few specifics I'm curious about:

* What framework or tools (open-source or otherwise) would work well for th
is kind of chatbot development?
* How can I integrate LLaMA 3.2 (or another model, if recommended) to handle real-time q
uestion generation and answering?
* How should I structure the chatbot's learning process to continuously improve its re
sponses from new tweets or user interactions?

Any suggestions on architecture, training strategies,RAGs or frameworks (
like Rasa, Langchain, etc.) would be greatly appreciated. Thank you!


```
---

     
 
all -  [ Favorite langchain features? ](https://www.reddit.com/r/LangChain/comments/1gae0jp/favorite_langchain_features/) , 2024-10-25-0913
```
While there's some general langchain hate, I'd like to know what are your favorite things about langchain? Favorite feat
ures, what makes your life easier, etc.?
```
---

     
 
all -  [ What is your favorite vector database that runs purely in a Python process ](https://www.reddit.com/r/LangChain/comments/1gadyp3/what_is_your_favorite_vector_database_that_runs/) , 2024-10-25-0913
```
I'm building a 'chat with your videos' desktop application and would like to run a vector database purely in application
 code rather than running it in a stand-alone server.



I've done some research and found these:

* [Weaviate embedded]
(https://weaviate.io/developers/weaviate/installation/embedded)
* [FAISS](https://github.com/facebookresearch/faiss)
* [
Milvus Lite](https://milvus.io/docs/milvus_lite.md)

Any other suggestions? Which is your favorite and why?
```
---

     
 
all -  [ Looking for an intern in Paris ](https://www.reddit.com/r/nextjs/comments/1gaawdm/looking_for_an_intern_in_paris/) , 2024-10-25-0913
```
Hey guys,

We’re a team of 2 based in [Station F](https://stationf.co/) in Paris, and we’ve been working on our startup 
for the past 6 months.

We build a bunch of AI Agents to automate manual tasks on a specific issue related to HR. We are
 an AI-first company, and work with best-in-class tech stack : Next, Neon, Inngest, Clerk, Shadcn, Langchain. Our infra 
is serverless.

We’re looking to hire an intern full stack rockstar who want to work on cutting edge tech. We have so ma
ny interesting challenges ahead and a very ambitious roadmap, but our 4 arms are not enough.

Feel free to dm me with yo
ur GitHub profile link if your are in Paris or want to relocate.  
Start date : ASAP

Best
```
---

     
 
all -  [ External interaction with LangGraph ](https://www.reddit.com/r/LangChain/comments/1ga8guy/external_interaction_with_langgraph/) , 2024-10-25-0913
```
Hello everyone

I've built an agent using LangGraph and I need to be able to call specific code  within it from the outs
ide like an API endpoint.

I've seen in the docs, for LangChain there's LangServe, what about LangGraph? Can I achieve t
he same using LangGraph Cloud? 

Thanks in advance,

  
co-founder Shaareable Apps
```
---

     
 
all -  [ How exactly does LLMGraphTransformer work? ](https://www.reddit.com/r/LangChain/comments/1ga70vg/how_exactly_does_llmgraphtransformer_work/) , 2024-10-25-0913
```
I am working on implementing knowledge graphs for RAG. I tried experimenting Microsofts's GraphRAG. Now i want to do usi
ng Neo4j. How are documents indexed? and How are entities extracted. I found that they use LLM to extract entities, is t
here a way I can find that prompt??

And once entities are found out, how are duplicate entities handled? I really need 
help.
```
---

     
 
all -  [ Guys, fckk my resume ](https://i.redd.it/fsdhqomy4hwd1.jpeg) , 2024-10-25-0913
```
Im keep applying for data science intern role, as my skillset but got no reply dont know what im missing. Suggest some c
hanges and what other can i put, im willing to contribute in opensource but not sure about how to do with my current ski
llset

Thank you for the review
Those freaking ai generating mediacore results
```
---

     
 
all -  [ How do you extract time metadata from question? ](https://www.reddit.com/r/LangChain/comments/1ga67mh/how_do_you_extract_time_metadata_from_question/) , 2024-10-25-0913
```
I have a RAG system that works great.

The users wants to ask questions like 'what are the news of this month?', 'what i
s the winner of the championship 2024?', and whatever.

I though to put a chain BEFORE the retrieval, trying to extract 
'time metadata' from the question, like 'date\_from' and 'date\_to', and then apply these filters to the retrieval query
 based document metadata.

I came up with a prompt like: 'today is %Y-%m-%d' + 'extract time metadata from the question.
..bla bla'.

Is this a good approach? Is there anything better i can do?
```
---

     
 
all -  [ Image Extraction Issue with WMF Format on Linux - Need Help Converting to PNG for OCR ](https://www.reddit.com/r/Rag/comments/1ga62v7/image_extraction_issue_with_wmf_format_on_linux/) , 2024-10-25-0913
```
Hi everyone,  
I’m building a multimodal pipeline involving LLMs and OCR where my app processes PPT files, extracting te
xt and images from slides. The app works perfectly in my local Windows environment, but images are extracted in WMF form
at on an AWS Ubuntu instance. Unfortunately, Linux can’t handle this format natively, which is causing issues for prepro
cessing (OCR) and further multimodal analysis.

I’m looking for suggestions on efficiently converting WMF images to PNG 
on Linux before feeding them into the OCR model within the LLM-driven multimodal architecture. Has anyone come across a 
similar issue in a LocalLLM or LangChain setup? Do you have any recommendations for tools, libraries, or workflows to in
tegrate this step into the pipeline? I appreciate any help you can provide.
```
---

     
 
all -  [ Final Year, Ideally looking for ML related FTE. Would love feedback on this Resume. ](https://www.reddit.com/r/developersIndia/comments/1ga5t7d/final_year_ideally_looking_for_ml_related_fte/) , 2024-10-25-0913
```
https://preview.redd.it/5wvdmub1ygwd1.png?width=580&format=png&auto=webp&s=64008ad4c4c5969e2b910f2370b225c6c39a035c


```
---

     
 
all -  [ The Most Affordable Search API for Scale. ](https://www.reddit.com/r/LangChain/comments/1ga4y55/the_most_affordable_search_api_for_scale/) , 2024-10-25-0913
```
So i am planning to create an AI Application, would like to know what do you guys prefer the best API, for an applicatio
n, which has a small feature of gettting results from Internet.
But the issue is that most Search API's are expensive (i
n my opinion) for scale.

I would really appreciate your recommendations.

```
---

     
 
all -  [ Request support on Jinja chat template for LLama3.1 and Llama3.2  ](https://www.reddit.com/r/LangChain/comments/1ga3dw3/request_support_on_jinja_chat_template_for/) , 2024-10-25-0913
```
I am trying to use vllm to serve llama 3.1 or 3.2 based on its outputs, to test which, I require a Jinja chat template


I wrote one, but not sure whether it's right as I get gibberish symbols as output. I attach the Jinja template herewith.


`<|begin_of_text|>
{% for message in messages %}
<|start_header_id|>{{ message['role'] }}<|end_header_id|>
{{ message[
'content'] }}<|eot_id|>
{% endfor %}
{% if add_generation_prompt and messages[-1]['role'] != 'assistant' %}
<|start_head
er_id|>assistant<|end_header_id|>
{% endif %}`

Please modify if I am wrong . Thanks in advance 
```
---

     
 
all -  [ [Student] Not getting any internship calls, please help me out ](https://www.reddit.com/r/EngineeringResumes/comments/1ga2qdo/student_not_getting_any_internship_calls_please/) , 2024-10-25-0913
```
https://preview.redd.it/5des7e5qvfwd1.png?width=5100&format=png&auto=webp&s=ee8a4c2816f7b933d001d1c9133024ed21f95210

Hi
 all,

I'm currently based in the UK on a student visa and looking for software engineering roles at big tech (FAANG, et
c.) as I approach graduation in 2026. I had an interview with Google last year and performed well in all three coding ro
unds, but still got rejected. Since then, I haven't had much luck securing calls for interviews from FAANG companies.

A
 bit about my background:

* I'm currently doing a year-long internship in my home country.
* I have experience in web d
evelopment and AI (I’ve worked with TensorFlow and trained models).
* I'm also focusing on improving my technical skills
 and projects in preparation for future applications.

I’d really appreciate any feedback on my resume in terms of conte
nt, structure, and overall strength. Is there something that could be holding me back from getting more interview calls 
from big tech? Any advice on how to improve my chances would be helpful!

Thanks!
```
---

     
 
all -  [ Rag not able to search image with name. ](https://www.reddit.com/r/LangChain/comments/1ga1ptb/rag_not_able_to_search_image_with_name/) , 2024-10-25-0913
```
I have implemented a Multimodal Retrieval-Augmented Generation (RAG) application, utilizing models such as CLIP and BLIP
, as well as multimodal models like GPT-4 Vision. While I am successfully able to retrieve images based on their content
 and details, I am facing an issue when trying to retrieve or generate images based solely on their file names.

For exa
mple, if I have document with multiple cats nickname, their description and then their image and if I ask model for imag
e of cat by their nickname, the system is not able to return the correct image. I've attempted various approaches, inclu
ding different file formats like PDFs and documents, as well as integrating OCR (Optical Character Recognition) to extra
ct text. Despite these efforts, I am still unable to generate the images using just their names. Could you provide guida
nce on how to resolve this issue?

Edit: I am using chromadb vector database.

Here is how my document is Structured -
T
here is name and then description and then image of cat, again cat name then description and image and so on..

```
---

     
 
all -  [ [Langgraph] Passing instruction messages in the graph ](https://www.reddit.com/r/LangChain/comments/1ga0k5s/langgraph_passing_instruction_messages_in_the/) , 2024-10-25-0913
```
I'm building a complex graph where agent 1 analyzes the message from customer, chooses a strategy and informs the agent 
2 how to proceed. 

What I do today is convert the agent 1's message to Human message and pass it to agent 2. This works
 with just 2 agents but when I started adding agents 3 & 4, the message conversion seems to confuse the AI. 

Looking fo
r strategies where I want to define something like this:

<General System Prompt>

<Specific feedback from a supervisor>


<Message from the user + message history>. 

What's the right way to implement this in Langgraph
```
---

     
 
all -  [ Claude's Coding Is Fantastic Right Now!  ](https://www.reddit.com/r/ClaudeAI/comments/1g9ynpo/claudes_coding_is_fantastic_right_now/) , 2024-10-25-0913
```
Just got home a short time ago after work, and I'm going back through some old prompts for several of my codebases and i
t's just running through the problems like nothing.

This is amazing.

Can't wait to mess with the tools and langchain/l
anggraph functions more this weekend. 
```
---

     
 
all -  [ AI agent for B2B research workflow - can pick tools on his own :) Upgrading to Langgraph soon ](https://www.reddit.com/r/LangChain/comments/1g9xq0a/ai_agent_for_b2b_research_workflow_can_pick_tools/) , 2024-10-25-0913
```
I built an AI agent for B2B research. It's all done with Langchain so far. I am upgrading to Langgraph soon to ensure my
 AI agent can combine tools to build even better research workflows for my users (978 users so far).   
  
To get specif
ic data points, the AI has to create intermediary steps, leveraging existing tools and combining them. 

**E.g I want to
 find companies in financial trouble.** 

This datapoint does not exist. This is quite subjective. Ai will ask to clarif
y.

Then the AI agent has to objectivize this information and develop tangible evidence and signals from the internet to
 help the users. 

here are some of the steps the Ai agent would take: 

**Here are 3 things the AI could suggest**  
\-
-> Glassdoor reviews

\--> Press release

\--> Suppliers complaints for late payments

**Action items:** 

Scrape that i
nformation

Find the appropriate taxonomy 

Verify the quality 

Apply the taxonomy based on the intelligence gathered. 


Display the results. 

===

One thing I noticed function\_calling is NOT the way to go regarding tool selection. Espec
ially if we want the Ai agent to be aware of thousands of tools, datapoints, and sources. 

We are using context window 
for that. Better results. 

https://reddit.com/link/1g9xq0a/video/rk0gsrzchewd1/player


```
---

     
 
all -  [ 🚀 Senior Machine Learning Engineer Opportunity! ](https://www.reddit.com/r/mlops/comments/1g9uykp/senior_machine_learning_engineer_opportunity/) , 2024-10-25-0913
```
We are seeking a seasoned **Senior Machine Learning Engineer** to join our innovative team and drive cutting-edge AI pro
jects. If you have a passion for building scalable machine learning systems and want to work in a collaborative environm
ent, this could be your next career move!

**Required Hard Skills** 

* **4+ years** of ML engineering experience
* **Ba
chelor’s degree** in Computer Science or related
* Experience with **Python, ML libraries and AI/ML frameworks (PyTorch,
 HuggingFace, TensorFlow, etc.)** 
* Experience building **GenAI solutions using LLMs**, including frameworks like LangC
hain and LlamaIndex, prompt engineering, fine-tuning and serving models, and implementing common patterns like RAG and N
LQ 
* **Client-facing experience**
* **Familiarity with containerization and orchestration tools** 

Link to the full jo
b posting: [https://boards.greenhouse.io/lokainc/jobs/4067015007?gh\_src=ff064e7b7us](https://boards.greenhouse.io/lokai
nc/jobs/4067015007?gh_src=ff064e7b7us)
```
---

     
 
all -  [ Coding a GeoGuessr Auto AI Bot with vision LLMs ](https://www.reddit.com/r/geoguessr/comments/1g9uw7x/coding_a_geoguessr_auto_ai_bot_with_vision_llms/) , 2024-10-25-0913
```
Video Tutorial: Coding a GeoGuessr AI Bot using LangChain and different Vision LLMs (GPT-4o, Claude 3.5, and Gemini 1.5)
 [https://www.youtube.com/watch?v=OyDfr0xIhss](https://www.youtube.com/watch?v=OyDfr0xIhss)

Disclaimer: this is not all
owed games with Leaderboards, prizes or competitive against other people publicly! This video is only for educational pu
rposes and to experiment LLMs capabilities :)
```
---

     
 
all -  [ Chromadb ](https://www.reddit.com/r/vectordatabase/comments/1g9trrw/chromadb/) , 2024-10-25-0913
```
Having a verbal crash issue with chromadb under langchain. I am trying to put chunks to the db and it kills the kernel. 


Any idea how this a constant? 

Built all using .venv so there shouldn't be any package issues.



```
---

     
 
all -  [ Cv debutant junior en reconversion ](https://i.redd.it/is740ys26dwd1.jpeg) , 2024-10-25-0913
```
Bonjour les amis
J’ai posté mon cv il y’a 3 jours et suite aux conseilles des membres j’ai l’ai modifié ..
Vos avis svp 
? Merci d’avance 

```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-25-0913
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-25-0913
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
