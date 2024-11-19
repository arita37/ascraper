 
all -  [ Secure Natural Language Processing Architecture ](https://medium.com/@gbasilveira/secure-natural-language-processing-architecture-f1f0d7b48db3) , 2024-11-19-0913
```

```
---

     
 
all -  [ What is the state of LLM application builders? ](https://www.reddit.com/r/LangChain/comments/1gugyed/what_is_the_state_of_llm_application_builders/) , 2024-11-19-0913
```
The question is in the title. For someone who wants to get started building simple LLM applications what are the options
? I know that langchain is an option, but read constant complaints about it's sparse documentation and redundant functio
nality. Are there other options? What are your thoughts?
```
---

     
 
all -  [ Information Extraction Guardrails ](https://www.reddit.com/r/LangChain/comments/1gufql6/information_extraction_guardrails/) , 2024-11-19-0913
```
What do you guys use as a guardrail (mainly for factuality) in case of information extraction using LLMs, when it is ver
y important to know if the model is hallucinating. I would like to know the ways/systems/packages/algorithms everyone is
 using in such use cases, I am currently open to use any foundational model proprietary or open source, only issue is th
e hallucinations and identifying those for human validations. I am bit opposed to using another Llm for evaluation.
```
---

     
 
all -  [ RAG Fight: The Silver Bullet(s) to Defeating RAG Hallucinations ](https://www.reddit.com/r/OpenAI/comments/1gufhcx/rag_fight_the_silver_bullets_to_defeating_rag/) , 2024-11-19-0913
```
*Spoiler alert: there's no silver bullet to completely eliminating RAG hallucinations... but I can show you an easy path
 to get very close.*

I've personally implemented at least high single digits of RAG apps; trust me bro. The expert diag
ram below, although a piece of art in and of itself and an homage to Street Fighter, also represents the two RAG models 
that I pitted against each other to win the RAG Fight belt and help showcase the RAG champion:

https://preview.redd.it/
twzzdalqzp1e1.png?width=1008&format=png&auto=webp&s=666427b63d8bdf53d520f85653eefe988b619015

On the **left** of the dia
gram is the model of a **basic RAG**. It represents the ideal architecture for the ChatGPT and LangChain weekend warrior
s living on the Pinecone free tier.

On the **right** is the model of the **'silver bullet' RAG**. If you added hybrid s
earch it would basically be the FAA~~N~~G of RAGs. *(*[*You can deploy the 'silver bullet' RAG in one click using a temp
late here*](https://www.scoutos.com/)*)*

Given a set of **99 questions** about a highly specific technical domain (33 e
asy, 33 medium, and 33 technical hard… Larger sample sizes coming soon to an experiment near you), I experimented by ask
ing each of these RAGs the questions and hand-checking the results. Here's what I observed:

# Basic RAG

* **Easy:** 94
% accuracy (31/33 correct)
* **Medium:** 83% accuracy (27/33 correct)
* **Technical Hard:** 47% accuracy (15/33 correct)


# Silver Bullet RAG

* **Easy:** 100% accuracy (33/33 correct)
* **Medium:** 94% accuracy (31/33 correct)
* **Technica
l Hard:** 81% accuracy (27/33 correct)

So, what are the 'silver bullets' in this case?

1. **Generated Knowledge Prompt
ing**
2. **Multi-Response Generation**
3. **Response Quality Checks**

Let's ***delve*** into each of these:

# 1. Gener
ated Knowledge Prompting

[Very high quality jay. peg](https://preview.redd.it/ekolmtf31q1e1.jpg?width=213&format=pjpg&a
uto=webp&s=c5716156a7b3692d45625b0174f9d6af5b496ed2)

**Enhance.** Generated Knowledge Prompting reuses outputs from exi
sting knowledge to enrich the input prompts. By incorporating previous responses and relevant information, the AI model 
gains additional context that enables it to explore complex topics more thoroughly.

This technique is especially effect
ive with technical concepts and nested topics that may span multiple documents. For example, before attempting to answer
 the user’s input, you pay pass the user’s query and semantic search results to an LLM with a prompt like this:

>You ar
e a customer support assistant. A user query will be passed to you in the user input prompt. Use the following technical
 documentation to enhance the user's query. Your sole job is to augment and enhance the user's query with relevant verbi
age and context from the technical documentation to improve semantic search hit rates. Add keywords from nested topics d
irectly related to the user's query, as found in the technical documentation, to ensure a wide set of relevant data is r
etrieved in semantic search relating to the user’s initial query. Return only an enhanced version of the user’s initial 
query which is passed in the user prompt.

Think of this as like asking clarifying questions to the user, without actual
ly needing to ask them any clarifying questions.

**Benefits of Generated Knowledge Prompting:**

* Enhances understandi
ng of complex queries.
* Reduces the chances of missing critical information in semantic search.
* Improves coherence an
d depth in responses.
* Smooths over any user shorthand or egregious misspellings.

# 2. Multi-Response Generation

[thi
s guy lmao](https://preview.redd.it/lxix9s742q1e1.png?width=1000&format=png&auto=webp&s=d5f04bf7750bd55a07162abde63e3f54
97038fb6)

Multi-Response Generation involves generating multiple responses for a single query and then selecting the be
st one. By leveraging the model's ability to produce varied outputs, we increase the likelihood of obtaining a correct a
nd high-quality answer. At a much smaller scale, kinda like mutation and/in **e**volution (It's still ok to say the '**e
**' word, right?).

**How it works:**

* **Multiple Generations:** For each query, the model generates several responses
 (e.g., 3-5).
* **Evaluation:** Each response is evaluated based on predefined criteria like as relevance, accuracy, and
 coherence.
* **Selection:** The best response is selected either through automatic scoring mechanisms or a secondary ev
aluation model.

**Benefits:**

* By comparing multiple outputs, inconsistencies can be identified and discarded.
* The 
chance of at least one response being correct is higher when multiple attempts are made.
* Allows for more nuanced and w
ell-rounded answers.

# 3. Response Quality Checks

[Automated QA is not the best last line of defense but it makes you 
feel a little better and it's better than nothing](https://preview.redd.it/32aif5k92q1e1.jpg?width=1600&format=pjpg&auto
=webp&s=effbc4df94841969a1728f20b4bf36b8f4f69fac)

Response Quality Checks is my pseudo scientific name for basically ju
st double checking the output before responding to the end user. This step acts as a safety net to catch potential hallu
cinations or errors. The ideal path here is “human in the loop” type of approval or QA processes in Slack or w/e, which 
won't work for high volume use cases, where this quality checking can be automated as well with somewhat meaningful impa
ct.

**How it works:**

* **Automated Evaluation:** After a response is generated, it is assessed using another LLM that
 checks for factual correctness and relevance.
* **Feedback Loop:** If the response fails the quality check, the system 
can prompt the model to regenerate the answer or adjust the prompt.
* **Final Approval:** Only responses that meet the q
uality criteria are presented to the user.

**Benefits:**

* Users receive information that has been vetted for accuracy
.
* Reduces the spread of misinformation, increasing user confidence in the system.
* Helps in fine-tuning the model for
 better future responses.

Using these three “silver bullets” I promise you can significantly mitigate hallucinations an
d improve the overall quality of responses. The 'silver bullet' RAG outperformed the basic RAG across all question diffi
culties, especially in technical hard questions where accuracy is crucial. Also, people tend to forget this, your RAG wo
rkflow doesn’t ***have*** to respond. From a fundamental perspective, the best way to deploy customer facing RAGs and av
oid hallucinations, is to just have the RAG not respond if it’s not highly confident it has a solution to a question.

*
*Disagree? Have better ideas? Let me know!**

Build on builders\~ 🚀

>[LLMs reveal more about human cognition than a we'
d like to admit](https://www.reddit.com/r/OpenAI/comments/1gu0r5h/comment/lxr1qzx/).   
\- u/YesterdayOriginal593


```
---

     
 
all -  [ Attribute Extraction from Images using DSPy ](https://www.reddit.com/r/LangChain/comments/1guf1xq/attribute_extraction_from_images_using_dspy/) , 2024-11-19-0913
```
# Introduction

DSPy recently added support for VLMs in beta. A quick thread on attributes extraction from images using 
DSPy. For this example, we will see how to extract useful attributes from screenshots of websites

# Signature

Define t
he signature. Notice the `dspy.Image` input field.

https://preview.redd.it/flgyaed82q1e1.png?width=1016&format=png&auto
=webp&s=7c72aebb20fa3f963cc480393b3b769b080a7ae8

# Program

Next define a simple program using the ChainOfThought optim
izer and the Signature from the previous step

https://preview.redd.it/qeuaabb92q1e1.png?width=1306&format=png&auto=webp
&s=34da1262900076dab5981cea80d6b2aa6d9f2d5c

# Final Code

Finally, write a function to read the image and extract the a
ttributes by calling the program from the previous step.

https://preview.redd.it/hpp57nia2q1e1.png?width=1165&format=pn
g&auto=webp&s=a07c9c5c0fdf1e551c03d31bfbd75898d46693a4

# Observability

That's it! If you need observability for your d
evelopment, just add `langtrace.init()` to get deeper insights from the traces.

https://preview.redd.it/ji1elw9b2q1e1.p
ng?width=3084&format=png&auto=webp&s=ef48331b0bffea14bc1a21a737415bb08cfa0500

# Source Code

You can find the full sour
ce code for this example here - https://github.com/Scale3-Labs/dspy-examples/tree/main/src/vision\_lm.
```
---

     
 
all -  [ Ollama having issues replying to tool_call ](https://www.reddit.com/r/LangChain/comments/1gudinm/ollama_having_issues_replying_to_tool_call/) , 2024-11-19-0913
```
Hello Everyone,

I have a JS code that run on LangChain. When I use OpenAI/chatgpt-4o-mini everything works wonders. I p
ass a zod object and my prompt and I get back the object. However, the moment I start using Ollama (*LLama3.2/Minstral/w
hichever model that supports tool calling*) the answer is not coming through.

The code I am using is similar to this (*
simplified to fit here*):

    const SingleNodeOutput = z.object({
      keyConcept: z.string().describe(`Key Concept or
 name of a relevant node`),
      score: z.number().describe(`Relevance to the potential answer by assigning a score bet
ween 0 and 100. A score of 100 implies a high likelihood of relevance to the answer, whereas a score of 0 suggests minim
al relevance.`),
    });
    const InitialNodesOutput = z.object({
      nodes: z.array(SingleNodeOutput).describe(`List
 of relevant nodes to the question and plan`),
    });
    
    const model = new ChatOpenAI(openAiParameters);
    cons
t prompt = ChatPromptTemplate.fromMessages(messages);
    const structuredLlm = model.withStructuredOutput(InitialNodesO
utput, {includeRaw: true,});
    const chain = prompt.pipe(structuredLlm);
    const llmResponse = await chain.invoke({.
..(z.infer<DATA STRUCTURE HERE>});



The response I get does not match the request. I generally get something like this
  
`parsed: {`

`nodes: '['KeyConcept1', 'KeyConcept2', 'KeyConcept3', 'KeyConceptN']',`

  `}`

  
Can anyone shed some
 light on what's going wrong with ollama?  
Am I asking too much to it? :D

Thanks
```
---

     
 
all -  [ Building a Verbal AI That’s More Than Just a Chatbot: Here’s How We Made RAG, Voice and Images Work  ](https://www.reddit.com/r/LLMDevs/comments/1guarwn/building_a_verbal_ai_thats_more_than_just_a/) , 2024-11-19-0913
```
We’ve just wrapped up a project to develop a prototype verbal AI system that isn’t just your standard chatbot but a voic
e-controlled assistant capable of pulling up complex documents, figures, and visual aids. Imagine being able to ask your
 AI for specific diagrams or instructions from dense manuals, all hands-free, with responses both spoken and visual. If 
you’re interested in the nuts and bolts, we’ve got code snippets on GitHub here and I’ll share visual insights from our 
project in this post.

https://preview.redd.it/praimalg8p1e1.jpg?width=2064&format=pjpg&auto=webp&s=3ed2253ea6654c829d65
2ae8f5fe6c5e1f0a436e

**See the full video on our RAG Masters YT show:** [**https://www.youtube.com/watch?v=BL2G3C3\_RZU
**](https://www.youtube.com/watch?v=BL2G3C3_RZU)

# 🎯 What’s This Verbal AI About?

Standard chatbots are great for Q&A,
 but Verbal AI aims to let users speak to AI to navigate documents in a more intuitive way. Here’s why we think it’s a g
ame-changer:

\- **Field Technicians:** Picture a mechanic asking the AI, “Can you show me the manual page for part inst
allation?” and the AI retrieves the precise diagram.

\- **Healthcare Applications:** Doctors or nurses could ask for sp
ecific medical imaging or patient instructions without needing to break focus on the patient.

\- **Customer Support:** 
Representatives can pull up warranty policies or step-by-step guides by asking rather than scrolling through documents.


**The goal:** A truly interactive, multimodal AI assistant that’s easy to use in real-world, high-pressure environments
. Now, let’s dig into how we’re building it!

# 🛠️ Tech Stack Overview

This project combines multiple tools to handle v
oice commands, retrieve specific document sections, and return relevant visuals and speech. Here’s the breakdown:

\- **
Frontend:** Built with Vue.js to handle voice and audio playback in a smooth UI.

\- **Backend**: Runs on Flask (Python)
 to manage all processing, from interpreting commands to serving visual content.

\- **Voice Engine:** OpenAI’s Whisper 
API handles speech-to-text and text-to-speech (TTS). It’s optimized for conversational AI. You could easily replace this
 with their newer voice model. 

\- **Document Retrieval with RAG:** [GroundX, EyeLevel’s APIs for enterprise-grade RAG,
](https://www.eyelevel.ai) manages document ingestion, processing, search and reranking. 

\- **Query Formatting with La
ngChain:** LangChain helps parse and structure commands, allowing us to differentiate between document retrieval request
s, navigation commands, and verbal Q&A.

# Code Snippets & Process Walkthrough

1️⃣ **Voice Input & Query Structuring**


The AI starts by taking user voice input and converting it into text via Whisper API. Here’s a simplified example:

`fr
om openai import OpenAI`

`client = OpenAI()`

`audio_file= open('recording.mp3', 'rb')`

`transcription = client.audio.
transcriptions.create(`

  `model='whisper-1',`

  `file=audio_file`

`)`

`print(transcription.text)`

Once we have tex
t, LangChain helps structure the query. For instance, if a user asks, “Pull up the portfolio overlap chart,” LangChain p
arses it to understand if the user is asking for a visual, a specific document section, or needs guidance.

2️⃣ **Retrie
ving Specific Content with GroundX**

This is where GroundX shines. Unlike typical RAG tools, GroundX chunks multimodal 
documents into semantic objects that include specific coordinates for visual elements like charts or tables within a doc
ument. So if the user asks for a particular figure, GroundX identifies the page, the exact section within a PDF and even
 provides a jpg of the visual object in the retrieval. 

# 🖼️ Visual Demo (Slides)

Here are some visuals that illustrat
e this process:

**1. Document Parsing and Semantic Object Identification** 

https://preview.redd.it/5ehyb2yn8p1e1.jpg?
width=1476&format=pjpg&auto=webp&s=111c5a41a97bea6c1c86acedad3dd1ac12305ae7

This slide shows GroundX breaking down a co
mplex document, identifying figures, tables, and sections as discrete “semantic objects.” Each object, shown here with c
olor shaded boxes, is bounded and indexed for efficient retrieval.

**2. Audio-Visual Sync with Plan of Action**

https:
//preview.redd.it/sj64mm758p1e1.png?width=1480&format=png&auto=webp&s=54b624fa20003ba2c513eb30d66a341ba78e4027

This sli
de demonstrates our “***buy me time***” protocol. As the AI begins processing, we send an initial verbal response to the
 user while the backend is retrieving the relevant visual content. This makes interactions feel faster and smoother.

**
3. PDF and Bounding Box Retrieval for Accurate Display**  

Using GroundX’s bounding box feature, our Verbal AI can snap
 to a specific page and section — think of it as laser-targeted search within a document.

# ⚙️ Handling Complex Command
s with LangChain

The LangChain framework lets us use simple if-else logic in English to define how the AI should behave
 for different types of queries. Here’s an example of how LangChain parses and structures commands:

    from langchain 
import AsStructuredOutput
    #action determiner
    class Action(TypedDict):
        scroll_up: bool
        scroll_dow
n: bool
        next_page: bool
        previous_page: bool
        snap_page: bool
        find_fig: bool
        find_
pdf: bool
        non_determ: bool
    action_parse_prompt = ChatPromptTemplate.from_messages(
        [
            (
 
               'system',
                '''Decide if the user wants one of the following actions performed:
           
     - `scroll_up`: scroll up a small amount within one page of the pdf
                - `scroll_down`: scroll down a s
mall amount within one page of the pdf
                - `snap_page`: snap to a specific page of a pdf
                -
 `find_fig`: find a specific figure, table, image, or specific item.
                - `find_doc`: find a specific doc
 
               - `non_determ`: no valid action is discernable
                These are mutually exclusive. One should b
e true, the rest should be false.
                note: you can use snap_page to go to a page relative to the current pa
ge.
                note: blanket questions should default to find figure, unless they're obviously about a document
   
             ''',
            ),
            ('placeholder', '{messages}'),
        ]
    )
    
    action_parser = act
ion_parse_prompt | ChatOpenAI(
        model='gpt-4o', temperature=0
    ).with_structured_output(Action)

With this set
up, LangChain helps classify the type of request (retrieval, navigation, etc.) so the AI can handle the command accordin
gly. No need to code complex logic—it’s handled in English, opening up new possibilities for non-programmers to tweak an
d build commands.

# 🎬 Generating Real-Time Responses: The “Buy Me Time” Technique

One challenge with any Verbal AI sys
tem is minimizing wait times. We created a workaround where, as soon as a query is recognized, the system immediately se
nds a “buy me time” message. Here’s the sequence:

1. **Initial Verbal Response:** After receiving the user’s query, the
 backend quickly generates a simple “Let me pull that up” message.  
2. **Content Processing:** The backend processes th
e full retrieval or action.  
3. **Follow-up Response:** Once the content is ready, the backend either serves the docume
nt or gives a more specific spoken response.

# 📊 Why Whisper Over OpenAI’s New Voice Models?

We initially considered u
sing OpenAI’s recent voice models, which directly interpret voice inputs. However, for a RAG-driven project, Whisper’s s
peech-to-text and text-to-speech modalities works very well at a fraction of the cost. In our example, we're not doing a
ny advanced logic or processing in the audio modality. We simple want to understand what the user said and turn it into 
RAG search.

The Whisper API easily integrates into our Python Flask backend, allowing seamless toggling between voice a
nd visual feedback.

# Application Ideas & Real-World Impact

This Verbal AI has serious potential across various indust
ries, including:

\- **Maintenance and Repair:** Field technicians could ask for step-by-step guidance and visual aids o
n their phones while keeping their hands free.  

\- **Medical:** Doctors could use Verbal AI to access complex medical 
charts or procedures hands-free in patient-facing settings.  

\- **Customer Support:** Assistants can pull up policy do
cs and product manuals through voice queries, making support more efficient and hands-free.

# Looking Ahead

For those 
looking to experiment, we’ve got the code snippets on [GitHub](https://github.com/DanielWarfield1/DocTech_vue_2/tree/mai
n) here. [https://github.com/DanielWarfield1/DocTech\_vue\_2/tree/mainWith](https://github.com/DanielWarfield1/DocTech_v
ue_2/tree/mainWith) EyeLevel’s [GroundX](https://www.eyelevel.ai), [LangChain](https://www.langchain.com), and [Whisper]
(https://github.com/openai/whisper), you’re equipped to build robust Verbal AI setups that go beyond text. We believe th
is system could redefine how people interact with documents, especially in high-stakes and hands-free settings.

# Would
 Love to Hear From You!

Have any of you explored similar RAG + voice applications? Would love to discuss ideas, challen
ges, or suggestions! Let me know if you want to dive deeper into any part of the process.
```
---

     
 
all -  [ chromadb vs langchain-chromadb ](https://www.reddit.com/r/LangChain/comments/1guaqbv/chromadb_vs_langchainchromadb/) , 2024-11-19-0913
```
Hi langchain experts - am learning Langchain and ChromaDB  and I just completed a basic tutorial that uses `import Chrom
aDB`.  Today I found that there is also a `langchain-ChromaDB`. 


For those who use both could you share which one you 
prefer and why?
```
---

     
 
all -  [ Perplexity sources design  ](https://i.redd.it/t1i70itbfo1e1.jpeg) , 2024-11-19-0913
```
I am trying to build a mini similar search engine like perplexity on my own data

And wanted to get sources like perplex
ity in a circle with a hyper link

Is it done on the front end? Or is it from AI 
Can I do it using langchain?



```
---

     
 
all -  [ Help with using memory in LangChain with Llama3.2 to avoid rewriting code from scratch on every prom ](https://www.reddit.com/r/LangChain/comments/1gu4ivl/help_with_using_memory_in_langchain_with_llama32/) , 2024-11-19-0913
```
Hi everyone! I'm working with LangChain and have a question about memory usage. I've already implemented memory using Co
nversationBufferMemory, but every time I send a new prompt, the model (Llama3.2) continues to generate the code from scr
atch, without retaining previous changes. I'd like to configure LangChain so that the model stores the state and can con
tinue generating the code from where I left off, instead of rewriting everything every time. Has anyone had experience w
ith this or can offer suggestions on how to properly use memory in LangChain with Llama3.2? Thanks in advance!

For exam
ple, it keeps repeating the importation of libraries and redefines functions, even though I want it to pick up from wher
e I left off.
```
---

     
 
all -  [ Can I use LangGraph without LangChain?  ](https://www.reddit.com/r/LangChain/comments/1gu3yya/can_i_use_langgraph_without_langchain/) , 2024-11-19-0913
```
Hi, I need to develop a multi-agentic RAG app for a startup. I come from a java development background and I am trying t
o select the best tool for the job. I have tried learning about LangChain and LangGraph. LangChain is complicated and I 
cannot wrap my head around how to structure my project and how to test it. I would like to use LangGraph to manage the f
low and OpenAI to create the agents i.e. bypass LangChain. Is this possible? Will this increase the complexity of the pr
oject? Should I cherry pick from LangChain and/or other frameworks or should I write the agents, RAG etc from scratch?
```
---

     
 
all -  [ Where do I start?  ](https://www.reddit.com/r/LangGraph/comments/1gu3xih/where_do_i_start/) , 2024-11-19-0913
```
Hi, I need to develop a multi-agentic RAG app for a startup. I come from a java development background and I am trying t
o select the best tool for the job. I have tried learning about LangChain and LangGraph. LangChain is complicated and I 
cannot wrap my head around how to structure my project and how to test it. I would like to use LangGraph to manage the f
low and OpenAI to create the agents  i.e. bypass LangChain. Is this possible? Will this increase the complexity of the p
roject? Should I cherry pick from LangChain and/or other frameworks or should I write the agents, RAG etc from scratch? 

```
---

     
 
all -  [ Somebody pls explain me the difference between AI agents and Agentic AI ](https://www.reddit.com/r/LangChain/comments/1gu307m/somebody_pls_explain_me_the_difference_between_ai/) , 2024-11-19-0913
```
Hi folks, 

I have been coming across the above two terms constantly. But I am not able to understand the definition or 
the difference between the two. Can somebody pls help with any links to resources or perhaps ELI5 it to me.

  
Thank yo
u.
```
---

     
 
all -  [ Building a CRM Copilot: Do I Need Extensive Intent Classification? ](https://www.reddit.com/r/LangChain/comments/1gu2u64/building_a_crm_copilot_do_i_need_extensive_intent/) , 2024-11-19-0913
```
Hey everyone, I’m working on a CRM copilot using LLM APIs. My CRM data is stored in a SQL database, and I’m planning to 
add some semantic content to a vector database as well.

For intent classification, I was initially planning to use LLM 
APIs to quickly identify the intent from a set of predefined options based on user queries. However, I noticed that most
 LLMs already seem to understand CRM structures and workflows quite well. I even tried generating SQL queries directly f
rom user prompts, and it worked great for most cases — the queries ran successfully and answered user questions.

That s
aid, I’m wondering if I really need a comprehensive intent classification system. Would it be better to just leverage LL
Ms’ knowledge, provide my schema more effectively (using LangChain), and rely on query generation?

I imagine I’ll still
 need some basic intent classification to determine where to fetch data (e.g., SQL vs. vector DB), but beyond that, is i
t worth building a more extensive intent classification system specifically for my CRM?

Would love to hear your thought
s or suggestions on this approach!
```
---

     
 
all -  [ How to extract handwritten text with Local LLM ](https://www.reddit.com/r/LangChain/comments/1gu254l/how_to_extract_handwritten_text_with_local_llm/) , 2024-11-19-0913
```
I work for a local fire agency.  We have collected paper waiver forms with information about our residents.  I've scanne
d the documents into a pdf.  These are raw images in PDF format.  I'm interested in capturing only the handwritten porti
ons of the sheets.  What local AI solution might help me do that? 
```
---

     
 
all -  [ Need some guidance related to implementing intelligent search for documents. ](https://www.reddit.com/r/LangChain/comments/1gtz8xu/need_some_guidance_related_to_implementing/) , 2024-11-19-0913
```
**Current System Requirements:** We need to implement two search functionalities in our document management system:

1. 
List files based on user queries
2. Answer questions using knowledge graph and RAG

**Focus Area - File Listing Search:*
* We're planning to implement keyword-based text search using Elasticsearch for the first functionality.

**User Query T
ypes:** The search needs to handle two distinct types of queries:

1. **Metadata-Aware Queries:**
   * Users know specif
ic file metadata
   * Example: 'list all files having companyxyz'
   * Search scope: title, metadata fields
2. **Concept
ual Queries:**
   * Users have topical understanding of needed files
   * Example: 'list all files related to this topic
'
   * Search scope: both metadata and content

**Current Implementation Status:**

1. **Metadata Search:**
   * Impleme
nted filters for title, metadata, author
   * Using LLM to extract filter parameters from queries
   * Challenge: Approa
ch is too constrained and not dynamic enough
2. **Content Search:**
   * Attempted RAG implementation
   * Issues:
     
 * Returns irrelevant results
      * Misses relevant files
      * Search scope too narrow

**Proposed Direction:** Con
sidering an agent-based approach:

* Provide search tools (title search, metadata filters) based on elasticsearch
* Let 
agent determine the tool based on the query
* The approach doesn't feel dynamic enough and feels like an overkill

I fee
l like there are many more approaches to solve the problem, can someone give some ideas ?
```
---

     
 
all -  [ Hosting an LLM in a server to serve for production. ](https://www.reddit.com/r/LangChain/comments/1gty24z/hosting_an_llm_in_a_server_to_serve_for_production/) , 2024-11-19-0913
```
Hello guys. I want to host an LLM on a GPU enabled server to use it for production. Right now, three clients wants to us
e this and there may be multiple concurrent requests hit the server. We want to serve them all without any issues. I'm u
sing fastapi to implement the APIs. But, as I observed, the requests are processed sequentially which increases latency 
for other clients. I want to know what is the optimal way of hosting LLM's in production. Any guides or resources are ac
cepted. Thanks
```
---

     
 
all -  [ Announcing bRAG AI: Everything You Need in One Platform ](https://www.reddit.com/r/Rag/comments/1gtxxah/announcing_brag_ai_everything_you_need_in_one/) , 2024-11-19-0913
```
Yesterday, I shared my open-source RAG repo ([bRAG-langchain](https://github.com/bRAGAI/bRAG-langchain)) with the commun
ity, and the response has been incredible—220+ stars on Github, 25k+ views, and 500+ shares in under 24 hours.

Now, I’m
 excited to introduce [**bRAG AI**](https://www.bragai.tech/), a platform that builds on the concepts from the repo and 
takes Retrieval-Augmented Generation to the next level.

# Key Features

* **Agentic RAG**: Interact with hundreds of PD
Fs, import GitHub repositories, and query your code directly. It automatically pulls documentation for all libraries use
d, ensuring accurate, context-specific answers.
* **YouTube Video Integration**: Upload video links, ask questions, and 
get both text answers and relevant video snippets.
* **Digital Avatars**: Create shareable profiles that “know” everythi
ng about you based on the files you upload, enabling seamless personal and professional interactions
* And so much more 
coming soon!

bRAG AI will go live next month, and I’ve added a waiting list to the homepage. If you’re excited about th
e future of RAG and want to explore these crazy features, visit [**bragai.tech**](http://bragai.tech) and join the waitl
ist!

Looking forward to sharing more soon. I will share my journey on the website's blog (going live next week) explain
ing how each feature works on a more technical level. 

Thank you for all the support!

Previous post: [https://www.redd
it.com/r/Rag/comments/1gsl79i/open\_source\_rag\_repo\_everything\_you\_need\_in\_one/](https://www.reddit.com/r/Rag/com
ments/1gsl79i/open_source_rag_repo_everything_you_need_in_one/)

Open Source Github repo: [https://github.com/bRAGAI/bRA
G-langchain](https://github.com/bRAGAI/bRAG-langchain)
```
---

     
 
all -  [ Announcing bRAG AI: Everything You Need in One Platform ](https://www.reddit.com/r/LangChain/comments/1gtxwnj/announcing_brag_ai_everything_you_need_in_one/) , 2024-11-19-0913
```
Yesterday, I shared my open-source RAG repo ([bRAG-langchain](https://github.com/bRAGAI/bRAG-langchain)) with the commun
ity, and the response has been incredible—220+ stars on Github, 25k+ views, and 500+ shares in under 24 hours.

Now, I’m
 excited to introduce [**bRAG AI**](https://www.bragai.tech/), a platform that builds on the concepts from the repo and 
takes Retrieval-Augmented Generation to the next level.

# Key Features

* **Agentic RAG**: Interact with hundreds of PD
Fs, import GitHub repositories, and query your code directly. It automatically pulls documentation for all libraries use
d, ensuring accurate, context-specific answers.
* **YouTube Video Integration**: Upload video links, ask questions, and 
get both text answers and relevant video snippets.
* **Digital Avatars**: Create shareable profiles that “know” everythi
ng about you based on the files you upload, enabling seamless personal and professional interactions
* And so much more 
coming soon!

bRAG AI will go live next month, and I’ve added a waiting list to the homepage. If you’re excited about th
e future of RAG and want to explore these crazy features, visit [**bragai.tech**](http://bragai.tech) and join the waitl
ist!

Looking forward to sharing more soon. I will share my journey on the website's blog (going live next week) explain
ing how each feature works on a more technical level. 

Thank you for all the support!

Previous post: [https://www.redd
it.com/r/LangChain/comments/1gsita2/comprehensive\_rag\_repo\_everything\_you\_need\_in\_one/](https://www.reddit.com/r/
LangChain/comments/1gsita2/comprehensive_rag_repo_everything_you_need_in_one/)

Open Source Github repo: [https://github
.com/bRAGAI/bRAG-langchain](https://github.com/bRAGAI/bRAG-langchain)
```
---

     
 
all -  [ Architecting a voice assistant ](https://www.reddit.com/r/LangChain/comments/1gtuk7f/architecting_a_voice_assistant/) , 2024-11-19-0913
```
I'm building a user research assistant that can talk to customers on phone. There's a need to process inputs, identify t
riggers and ask pointed questions every time. I'm using livekit for voice and langgraph for processing the inputs and wo
rks well. But the latency is too high.I'm looking for better approaches to architect this and could use some help. Has a
nyone done something similar and can you share suggestions on how to architect the LLM flow?

Here's what I've so far:


* Have a speaker LLM which talks to customer in realtime and offload the processing to a separate graph that work async.

* Train the single LLM for the specific task

Any other ideas?
```
---

     
 
all -  [ How accurate are these layer definitions from Hamilton?  ](https://i.redd.it/4pwmfckpdj1e1.png) , 2024-11-19-0913
```
Saw this chart in Hamilton documentation and wondered if this is common terminology for the layers of data stack, more s
pecifically: 

1. Is there really 'asset level'? Is dbt 'asset level'? 
2. What is good source to read about these layer
s? 
3. Why postgres is data and DuckDB is execution? Ok to have Snofkake on two levels? Is lang chain same level as pand
as? 
```
---

     
 
all -  [ Can't Make New Project on LangSmith (Newbie) ](https://www.reddit.com/r/LangChain/comments/1gtowlt/cant_make_new_project_on_langsmith_newbie/) , 2024-11-19-0913
```
Hello, everyone! I'm working on setting up a new project in Lang Smith, and I've run into some challenges. I am not usin
g any language models like LLM; instead, my project utilizes a pre-made API form rapidAPI. The inputs to my system come 
from file uploads through FastAPI. 

I'm trying to create a monitoring system for this setup, but I'm having trouble get
ting everything to work together. Specifically, unsure how to deploy lang smith within my FastAPI application, around th
e file upload process and subsequent API interactions.

I'll add my code block below. Im basically working on a project 
take takes docx and pdfx format of files, my Langchain data loaders take the text from the file and feed it to my API, t
hen i get the my desired results.  
Really appreciate any help!! (at my wit's end here) 

    app = FastAPI()
    
    #
 API key and host
    API_KEY = <myAPIkey>
    API_HOST = <linktotheapi>
    
    # Code for Text AI Detect
    def text
_check(user_input):
        url = <url>
        payload = {
            'text': user_input,
            'threshold': 10 
 # Adjust this if needed to test different sensitivity levels
        }
        headers = {
            'x-rapidapi-key'
: API_KEY,
            'x-rapidapi-host': API_HOST,
            'Content-Type': 'application/json'
        }
        res
ponse = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    
    @app.get('/')
   
 async def home():
        return 'Hello! Welcome to My Final Project'
    
    @app.post('/uploadFile/')
    async def 
create_upload_files(file: UploadFile = File(...)):
        suffix = os.path.splitext(file.filename)[1].lower()
        t
emp_file_path = tempfile.mktemp(suffix=suffix)
        with open(temp_file_path, 'wb') as f:
            f.write(await f
ile.read())
        
        try:
            if suffix == '.pdf':
                loader = PyPDFLoader(temp_file_path)

                document = loader.load_and_split()
                print(dir(document[0])) if document else print('No do
cument loaded') ## Debugging
                text_content = ' '.join([str(page) for page in document])
            elif 
suffix == '.docx':
                loader = UnstructuredFileLoader(temp_file_path)
                document = loader.loa
d()
                print(dir(document)) if document else print('No document loaded') ## Debugging output
              
  text_content = str(document)
            else:
                return JSONResponse(status_code=400, content={'message'
: 'Unsupported file type'})
            result = text_check(text_content) # Sending the text to text checker API
       
     return JSONResponse(content=result)
        except Exception as e:
            return JSONResponse(status_code=500,
 content={'message': str(e)})
        finally:
            os.remove(temp_file_path)  # clean-up
    
    
    if __name
__ == '__main__':
        ngrok_tunnel = ngrok.connect(8000)
        print('Public URL:', ngrok_tunnel.public_url)
     
   nest_asyncio.apply()
        uvicorn.run(app, port=8000)
    
```
---

     
 
all -  [ ChromaDB runtime error in Mac with Intel Chips - thought this might help ](https://www.reddit.com/r/LangChain/comments/1gtlto7/chromadb_runtime_error_in_mac_with_intel_chips/) , 2024-11-19-0913
```
I’ve been learning/practicing langchain about a month . I have been playing with chroma vector store for about a week.  
I just wanted to share the issue that I encountered with chromaDb code running on Mac with Intel chip.  I shared my solu
tion -the one with 0 votes - here (https://stackoverflow.com/questions/78745137/python-chromadb-error-unable-to-compute-
the-prediction-using-a-neural-network/79175940#79175940).   


```
---

     
 
all -  [ Help with `buildPythonPackage` helper ](https://www.reddit.com/r/NixOS/comments/1gtl9hc/help_with_buildpythonpackage_helper/) , 2024-11-19-0913
```
Hello,

I am trying to create a development environment in NixOS and I got stuck at building a python package that is no
t already in the existing `python3Packages` (package `iso639-lang`).

I found out that I can build this package from PyP
i using `buildPythonPackage` and a fetch helper `pkgs.fetchPypi`.

Problem is that, for this (see below) configuration, 
I get the following error:

https://preview.redd.it/53wdc74chi1e1.png?width=1287&format=png&auto=webp&s=bb6f6543735b141a
7fdac10bedddcffa851b605c

It seems to be trying to read some `setup.py` file, but upon inspecting the downloaded archive
, there does not seem to be such file.

Sample flake for dev env (**DISCLAIMER:** I am absolute newbie in case of Nix\\O
S, yet alone Flakes):

    {
      description = 'A very basic flake';
    
      inputs = {
        nixpkgs.url = 'gith
ub:nixos/nixpkgs/nixos-24.05';
      };
    
      outputs = { self, nixpkgs, ... }: let
        system = 'x86_64-linux'
;
      in {
      devShells.'${system}' = {
    default = let
          pkgs = import nixpkgs {
            inherit sys
tem;
          };
          pythonPackages = pkgs.python3Packages;
          iso639 = let
          pname = 'iso639_lang
';
          version = '2.5.1';
          in
          pythonPackages.buildPythonPackage {
          inherit pname versi
on;
          src = pkgs.fetchPypi {
            inherit pname version;
            sha256 = 'sha256-yeMR7CtvEAXrNtOgoPa
7+CiYy00831aLaq5KBwWhndU=';
          };
          doCheck = false;
        };
        in pkgs.mkShell {
          packa
ges = with pkgs; [
            (python3.withPackages (pp: [
            pp.langchain
            pp.openai
            p
p.unstructured
            pp.emoji
            iso639
          ]))
            pipenv
          ];
    
          shel
lHook = ''
            echo '`${pkgs.python3}/bin/python --version`'
          '';
        };
      };
    };
    }

Tha
nks for the help
```
---

     
 
all -  [ AI Agents: A New Era of Automation ](https://www.reddit.com/r/Tech_By_PV/comments/1gtl3bm/ai_agents_a_new_era_of_automation/) , 2024-11-19-0913
```
**The AI Agent Revolution is Here**

AI agents, once a futuristic concept, are now becoming a reality. A recent survey b
y LangChain revealed that over half of professionals are already using AI agents in their daily work. This rapid adoptio
n is transforming industries, from tech to finance.

**What are AI Agents?**

AI agents are intelligent software program
s that can perform tasks autonomously. They can learn, adapt, and make decisions, just like humans. Think of them as dig
ital assistants, supercharged with AI capabilities.

**Why are AI Agents So Popular?**

* **Boosting Productivity:** AI 
agents can automate repetitive tasks, freeing up human workers to focus on more strategic work.
* **Improving Decision-M
aking:** By analyzing vast amounts of data, AI agents can provide valuable insights to help businesses make informed dec
isions.
* **Enhancing Customer Service:** AI agents can handle customer inquiries 24/7, improving customer satisfaction.


**How are Companies Using AI Agents?**

* **Research and Summarization:** AI agents are being used to quickly gather a
nd summarize information from various sources.
* **Personal Productivity:** They're helping with tasks like scheduling m
eetings, writing emails, and managing calendars.
* **Customer Service:** AI agents are providing support to customers th
rough chatbots and virtual assistants.

**Challenges and Concerns**

While AI agents offer immense potential, they also 
pose challenges:

* **Integration:** Integrating AI agents into existing systems can be complex.
* **Control:** Ensuring
 that AI agents act ethically and responsibly is a major concern.
* **Consistency:** Maintaining consistent performance 
can be difficult, especially as AI agents learn and evolve.

**The Future of AI Agents**

Despite these challenges, the 
future of AI agents looks bright. Companies are investing heavily in AI research and development to create more sophisti
cated and reliable agents.

To ensure the ethical and responsible use of AI agents, organizations are:

* **Tracking Act
ions:** Monitoring the actions of AI agents to identify and mitigate potential risks.
* **Using Monitoring Tools:** Empl
oying advanced tools to oversee the behavior of AI agents.
* **Involving Humans:** Incorporating human oversight to guid
e and correct AI agents.

By addressing these challenges and embracing the opportunities, businesses can harness the pow
er of AI agents to drive innovation and achieve new heights.
```
---

     
 
all -  [ Generative AI Technology Stack Overview - Generative AI (GenAI) Frameworks Overview ](https://www.reddit.com/r/u_enoumen/comments/1gtc52c/generative_ai_technology_stack_overview/) , 2024-11-19-0913
```
# [Generative AI Technology Stack Overview](https://podcasts.apple.com/ca/podcast/generative-ai-technology-stack-overvie
w-generative/id1684415169?i=1000677220601)

https://preview.redd.it/xruib4fumh1e1.jpg?width=1587&format=pjpg&auto=webp&s
=08fb6026efb31f7d271b5cb27443e15ed41f0177

# Generative AI (GenAI) is much more than just Large Language Models (LLMs) –
 it's an intricate combination of engineering, science, and the business application at hand. Understanding the technolo
gy stack behind GenAI solutions is essential because it provides a comprehensive blueprint for building and deploying th
ese powerful AI solutions effectively. The GenAI stack is made up of multiple interrelated layers, each contributing a c
rucial aspect of functionality, from foundational infrastructure to the final user-facing interface. This one-page guide
 provides a high-level overview of the technology stack needed to create a production-ready GenAI application.

Listen a
s a podcast at [https://podcasts.apple.com/ca/podcast/generative-ai-technology-stack-overview-generative/id1684415169?i=
1000677220601](https://podcasts.apple.com/ca/podcast/generative-ai-technology-stack-overview-generative/id1684415169?i=1
000677220601)

# [Layers of the GenAI Technology Stack](https://podcasts.apple.com/ca/podcast/generative-ai-technology-s
tack-overview-generative/id1684415169?i=1000677220601)

https://preview.redd.it/gy0v1h80bg1e1.png?width=807&format=png&a
uto=webp&s=b6cf8ec0d2c089f7155cc2105f00e484d65de550

# The GenAI tech stack can be visualized as a multi-layered structu
re, each layer serving a unique purpose in the lifecycle of an AI application:

# 1. Infrastructure

# At the base, we h
ave the underlying infrastructure. This layer involves the hardware and cloud services that provide the computational re
sources needed for AI. Examples include:

* **NVIDIA**: Provides the high-performance GPUs required for model training a
nd inference.
* **Cloud Platforms**: Platforms like **AWS**, **Google Cloud**, **Azure**, and [**Together.ai**](http://T
ogether.ai) offer scalable infrastructure, providing compute and storage for large-scale AI projects.

# 2. Foundation M
odels

# Foundation models are pre-trained, large-scale models that provide the base for building specific applications.


* Examples include models from **OpenAI**, **Anthropic**, **Cohere**, **Meta (Mistral)**, **Gemini**, and **LLaMA**. T
hese models can be fine-tuned or used as-is to handle a wide variety of tasks such as text generation, summarization, an
d more.

# 3. Retrieval Layer

# This layer is crucial for providing efficient and effective access to relevant informat
ion. Retrieval can involve several types of data storage and querying mechanisms.

* **Vector Databases**: Databases lik
e **Pinecone**, **Weaviate**, **Qdrant**, **SingleStore**, and **Chroma** store high-dimensional data representations (e
mbeddings) and allow for efficient similarity search, which is essential for many GenAI use cases.
* Retrieval approache
s can also involve **graph databases**, **keyword-based search**, and more, depending on the complexity of the data rela
tionships and querying needs.

# 4. Runtime/Framework

# The frameworks and runtime environments are responsible for orc
hestrating how the models interact with data, perform inference, and communicate with other components.

* **LangChain**
: This is a prominent framework that provides useful abstractions for connecting language models with external tools and
 managing different steps in conversational AI workflows.
* **LlamaIndex** and **Replicate**: Frameworks that are used f
or indexing and model serving.
* **HuggingFace**: Offers a large library of models and tools for deployment, training, a
nd inference, making it ideal for simplifying GenAI workflows.

# 5. Monitoring and Orchestration

# A crucial layer oft
en overlooked, monitoring and orchestration ensure that the models are functioning correctly, performance remains optima
l, and the system can handle any issues that arise.

* This might involve **Kubernetes** for container orchestration, **
Prometheus** for monitoring, or other specialized tools that keep track of model performance, infrastructure health, and
 scalability.

# 6. Frontend Hosting

# To make the AI application accessible to users, you need hosting solutions that 
deliver the frontend interface. While there may be alternative focus areas such as orchestration, frontend hosting plays
 a vital role in user experience.

* Platforms like **Vercel**, **Netlify**, and **GitHub Pages** are popular choices fo
r deploying lightweight web-based interfaces that interact with the AI models.

# Generative AI (GenAI) Frameworks Overv
iew

https://preview.redd.it/vxuratx5bg1e1.png?width=1170&format=png&auto=webp&s=76fc3c09ab12bc70e36e7372cde25ca5d6a69df
f

# The GenAI frameworks provide a diverse set of tools to build advanced AI applications, each with its own strengths 
and focus areas:

* **LangChain**: Excels in creating complex chains of operations, providing diverse integrations and a
 flexible architecture for language models. It is ideal for building versatile language model applications.
* **LlamaInd
ex**: Specializes in data indexing, efficiently handling structured data, and optimizing queries for large-scale informa
tion retrieval. It is particularly suited for data-intensive tasks.
* **Haystack**: Known for its robust question-answer
ing capabilities, document search functionality, and production-ready features. It is highly effective for building prod
uction-ready search and QA systems.
* **Microsoft Jarvis**: Focuses on conversational AI and task automation, seamlessly
 integrating into the Microsoft ecosystem. It is a strong choice for Microsoft-centric AI solutions.
* **Amazon Bedrock*
*: Provides a comprehensive platform for generative AI, offering deep integration with AWS services and sophisticated mo
del management tools, making it ideal for AWS-integrated generative AI applications.
* **MeshTensorflow**: Stands out fo
r its distributed training capabilities, enabling model parallelism and optimizations for Tensor Processing Units (TPUs)
. It is perfect for high-performance, distributed model training.
* **OpenAI Swarm**: Recently introduced and still in t
he experimental phase, Swarm provides developers with a blueprint for creating interconnected AI networks capable of com
municating, collaborating, and tackling complex tasks autonomously. It represents a significant step in making multi-age
nt systems more accessible to developers.

# Each framework has unique strengths:

* **LangChain** for versatile languag
e model applications.
* **LlamaIndex** for data-intensive tasks.
* **Haystack** for production-ready search and QA syste
ms.
* **Microsoft Jarvis** for Microsoft-centric AI solutions.
* **Amazon Bedrock** for AWS-integrated generative AI.
* 
**MeshTensorflow** for high-performance, distributed model training.
* **OpenAI Swarm** for experimental multi-agent sys
tems.

# Developers can choose the most suitable framework based on their specific project requirements, infrastructure 
preferences, and the desired balance between flexibility, performance, and ease of integration.

# Why Mastering This St
ack Matters

# For AI/ML/Data engineers, it's important to understand not only each layer in isolation but how these lay
ers interact as a cohesive whole. The flow of data across the layers, potential bottlenecks, and optimization strategies
 are all part of building robust, efficient, and scalable AI solutions. By mastering the GenAI tech stack:

* **Optimize
d Performance**: Engineers can optimize for faster inference, better data management, and improved scalability.
* **Scal
able Solutions**: The knowledge of each layer's strengths allows for architecting applications that are scalable and mai
ntainable.
* **Effective Troubleshooting**: Understanding the stack enables efficient troubleshooting across all layers,
 whether the issue lies in data retrieval, model performance, or frontend integration.

# Whether you're building a simp
le chatbot or a more complex AI system, knowledge of this layered architecture helps create robust and maintainable AI s
olutions. This understanding is key as GenAI becomes more integrated into business processes.

# Genefative AI Tech Stac
k Implementation

# 1. Google Cloud Implementation

# Google Cloud offers a variety of tools and services that can help 
you implement the Generative AI technology stack:

https://preview.redd.it/dow8slpebg1e1.png?width=879&format=png&auto=w
ebp&s=154844db2a858a6992c2e19fedda0552310e9a82

https://preview.redd.it/kme3v72ibg1e1.png?width=1060&format=png&auto=web
p&s=2b73b707b0c96b77d9d4137d9a427f949ed04aa0

* **Infrastructure**: Use **Google Cloud Compute Engine** or **Google Kube
rnetes Engine (GKE)** for scalable infrastructure, combined with **TPUs** for accelerated machine learning tasks.
* **Fo
undation Models**: Leverage **Vertex AI** to access pre-trained models or fine-tune models using Google's AI platform.
*
 **Retrieval Layer**: Utilize **Cloud Bigtable** or **Firestore** for structured data, and **Google Cloud Storage** for 
large datasets and embeddings.
* **Runtime/Framework**: Integrate with frameworks like **TensorFlow** and **HuggingFace 
Transformers**, which can be deployed using Google AI services.
* **Monitoring and Orchestration**: Use **Google Cloud M
onitoring** and **Cloud Logging** to manage performance, combined with **Google Kubernetes Engine** for orchestration.
*
 **Frontend Hosting**: Deploy user-facing applications using **Firebase Hosting** or **Google App Engine**.

# 2. AWS Im
plementation

# Amazon Web Services (AWS) provides a robust ecosystem to support each layer of the Generative AI stack:


https://preview.redd.it/xdjv177kbg1e1.png?width=3615&format=png&auto=webp&s=fd5c46c9388259332af7eeef50a66447272ec2a9

*
 **Infrastructure**: Utilize **EC2 instances** with GPU capabilities or **SageMaker** for scalable compute resources.
* 
**Foundation Models**: Use **Amazon SageMaker** to train and deploy models, or access pre-trained models available throu
gh AWS.
* **Retrieval Layer**: Implement **Amazon DynamoDB** for fast access to structured data and **Amazon OpenSearch*
* for searching across large datasets.
* **Runtime/Framework**: Integrate **HuggingFace** on AWS, with **Amazon SageMake
r** to manage model training and inference workflows.
* **Monitoring and Orchestration**: Use **CloudWatch** for monitor
ing and logging, and **AWS Fargate** for orchestrating containerized workloads.
* **Frontend Hosting**: Host application
s with **Amazon S3** and use **CloudFront** for content delivery.

# 3. Azure Implementation

# Microsoft Azure provides
 an extensive set of tools to implement the GenAI technology stack effectively:

https://preview.redd.it/lu0jlwpmbg1e1.p
ng?width=731&format=png&auto=webp&s=0f9479a6d2a40863bd07262e01075581bcc1a274

* **Infrastructure**: Use **Azure Virtual 
Machines** or **Azure Kubernetes Service (AKS)** for scalable compute resources, and leverage **Azure ML** for optimized
 AI workflows.
* **Foundation Models**: Utilize **Azure OpenAI Service** to access pre-trained language models and build
 customized AI solutions.
* **Retrieval Layer**: Use **Azure Cosmos DB** for high-performance access to structured data 
and **Azure Blob Storage** for large datasets.
* **Runtime/Framework**: Integrate frameworks like **PyTorch** and **Tens
orFlow**, and use **Azure ML** to deploy and manage these models.
* **Monitoring and Orchestration**: Use **Azure Monito
r** for monitoring, **Log Analytics** for insights, and **Azure Kubernetes Service** for orchestration.
* **Frontend Hos
ting**: Host your frontend with **Azure App Service** or **Static Web Apps** for a seamless user experience.

# Notes an
d Future Directions

# This tech stack isn't a rigid blueprint but rather a point of reference. There are many tools and
 technologies that could fit into each of these layers, depending on your specific needs and constraints.

# Moreover, i
t's worth noting the importance of a vector database. Vector databases are particularly suited for GenAI applications, a
s they can handle complex, high-dimensional data while offering efficient querying and retrieval mechanisms. A prime exa
mple is SingleStore, which can handle both vector and traditional relational data efficiently, thus offering a flexible 
solution for AI applications.

# In the future, additional layers like advanced monitoring, security, and specialized or
chestration tools might become even more crucial to build production-grade GenAI systems.

https://preview.redd.it/am698
10qbg1e1.png?width=7680&format=png&auto=webp&s=0a5efb86738676315acfe4c73e9474c99b0b3cd5

# [💪 AI and Machine Learning Fo
r Dummies](https://apps.apple.com/ca/app/ai-machine-learning-4-dummies/id1611593573)

Djamgatech has launched a new educ
ational app on the Apple App Store, aimed at simplifying AI and machine learning for beginners.

**It is a mobile App th
at can help anyone Master AI & Machine Learning on the phone!**

**Download 'AI and Machine Learning For Dummies ' FROM 
APPLE APP STORE and conquer any skill level with interactive quizzes, certification exams, & animated concept maps in:**


* **Artificial Intelligence**
* **Machine Learning**
* **Deep Learning**
* **Generative AI**
* **LLMs**
* **NLP**
* **
xAI**
* **Data Science**
* **AI and ML Optimization**
* **AI Ethics & Bias ⚖️**

**& more! ➡️**[ App Store Link: ](https
://apps.apple.com/ca/app/ai-machine-learning-4-dummies/id1611593573)[https://apps.apple.com/ca/app/ai-machine-learning-4
-dummies/id1611593573](https://apps.apple.com/ca/app/ai-machine-learning-4-dummies/id1611593573)

# [AI Consultation](ht
tp://djamgatech.com/contact-us/):

We empower organizations to leverage the transformative power of Artificial Intellige
nce. Our AI consultancy services are designed to meet the unique needs of industries such as oil and gas, healthcare, ed
ucation, and finance. **We provide customized AI and Machine Learning podcast for your organization, training sessions, 
ongoing advisory services, and tailored AI solutions that drive innovation, efficiency, and growth.**

Contact us [here]
(http://djamgatech.com/contact-us/) ([or email us at info@djamgatech.com](http://djamgatech.com/contact-us/)) to receive
 a personalized value proposition.
```
---

     
 
all -  [ deprecation of langchain-community? ](https://www.reddit.com/r/LangChain/comments/1gt8jbb/deprecation_of_langchaincommunity/) , 2024-11-19-0913
```
I'm one of who was interested integrating my own service to langchain via langchain-community (still don't know what's t
he difference btw partner package and community package but). 

And experiencing the process... found it would be no mor
e sustainable for langchain team to manage and operate in the way it was.

Now I just found out they are planning deprec
ation of langchain-community ?! 

[https://python.langchain.com/docs/contributing/how\_to/integrations/community/](https
://python.langchain.com/docs/contributing/how_to/integrations/community/)

and they might add integrations only through 
standalone repo...?

would love to hear about some experiences and expectations on integrations with LangChain!
```
---

     
 
all -  [ Agent Deployment ](https://www.reddit.com/r/LangChain/comments/1gt8gfo/agent_deployment/) , 2024-11-19-0913
```
Hi everyone,

I’ve built an AI agent using Langraph and am looking to deploy it. Could someone guide me on the available
 deployment options and key considerations for deploying AI agents effectively?

Thanks in advance!
```
---

     
 
all -  [ Roast my Resume, 2nd year B.Tech Computer Science Student ](https://www.reddit.com/r/Btechtards/comments/1gt8cpw/roast_my_resume_2nd_year_btech_computer_science/) , 2024-11-19-0913
```
https://preview.redd.it/7ptc2ku4ze1e1.png?width=936&format=png&auto=webp&s=d4e76a4fa419143cbb3ed46e072826b31e990a00


```
---

     
 
all -  [ Seeking Help to Optimize RAG Workflow and Reduce Token Usage in OpenAI Chat Completion ](https://www.reddit.com/r/LangChain/comments/1gt7o3r/seeking_help_to_optimize_rag_workflow_and_reduce/) , 2024-11-19-0913
```


Hey everyone,

I'm a frontend developer with some experience in LangChain, React, Node, Next.js, Supabase, and Puppete
er. Recently, I’ve been working on a Retrieval Augmented Generation (RAG) app that involves:

1. Fetching data from a we
bsite using Puppeteer.
2. Splitting the fetched data into chunks and storing it in Supabase.
3. Interacting with the sto
red data by retrieving two chunks at a time using Supabase's RPC function.
4. Sending these chunks, along with a basic p
rompt, to OpenAI's Chat Completion endpoint for a structured response.

While the workflow is functional, the responses 
aren't meeting my expectations. For example, I’m aiming for something similar to the structured responses provided by [s
itespeak.ai](https://sitespeak.ai/), but with minimal OpenAI token usage. My requirements include:

* Retaining the prev
ious chat history for a more user-friendly experience.
* Reducing token consumption to make the solution cost-effective.

* Exploring alternatives like Llama or Gemini for handling more chunks with fewer token burns.

If anyone has experienc
e optimizing RAG pipelines, using free resources like Llama/Gemini, or designing efficient prompts for structured output
s, I’d greatly appreciate your advice!

Thanks in advance for helping me reach my goal. 😊
```
---

     
 
all -  [ How to prevent chat() function in pandasai from downloading images? ](https://www.reddit.com/r/StreamlitOfficial/comments/1gswjm3/how_to_prevent_chat_function_in_pandasai_from/) , 2024-11-19-0913
```
I'm using the [pandasai](https://pypi.org/project/pandasai/) library for data analysis in my application. When I call th
e `chat()` function to generate image responses, it triggers a download of the images instead of displaying them. I want
 to display these images directly in my application.

Here’s a snippet of my code:

    import pandas as pd
    from pan
dasai import SmartDataframe
    from langchain_groq.chat_models import ChatGroq
    import os
    import streamlit as st

    
    # groq
    llm = ChatGroq(model_name='llama3-70b-8192', api_key=os.environ['GROQ_API_KEY'])
    
    # Streaml
it app setup
    st.title('Data Analysis with SmartDataframe')
    
    df = pd.read_excel('data.xlsx')
    df = SmartDa
taframe(df, config={'llm': llm})
    
    st.write('Smart Dataframe')
    
    # User input for chat command
    user_in
put = st.text_input('Enter your command:')
    
    if user_input:  # Check if user input is provided
        response =
 df.chat(user_input)  # This line triggers the download
        # Assuming response is an image URL or path
        st.i
mage(response, use_container_width=True)//

The issue arises when I call `response = df.chat(user_input)`, which seems t
o trigger a download of the image instead of displaying it. I expected the image to be shown directly in my application.


I would like the image to display directly in the Streamlit app without triggering any download or new window.

Is the
re a way to modify the chat() function in pandasai to prevent this download behavior?

If not, are there any workarounds
 or suggestions for implementing this feature?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1gswggs/list_of_free_and_best_selling_discounted_courses/) , 2024-11-19-0913
```
# Udemy Free Courses for 17 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24922/)Fundamentals of Backend Engineering
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/24921/)Creación de una Tienda Virtual con Kotlin | Android Studio
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24920/)The Complete Deep Learning Course 2024 With 7+ Real Projects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24919/)Business Analytics con Python y ChatGPT: De Cero a Experto
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24918/)LangChain Mastery: Build GenAI Apps with LangChain &Pinecone
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24917/)Google Hacking – Aprende Búsquedas Avanzadas con Google
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24916/)VPS Linux en DigitalOcean:Ubuntu 22, Nginx, PHP y WordPress
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24915/)Vue JS (2 y 3) – Crea Aplicaciones Web Modernas con Vue
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24914/)Node.js – Creando API con Express y MongoDB (Incl. Deno)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24913/)ISO/IEC 27001 Implementando Seguridad de la Información
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24912/)ISO 22301 – Gestión de la Continuidad del Negocio
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24911/)MongoDB – La mejor Base de Datos NoSQL desde cero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24910/)Dart – La Guía Completa para Aprender a Programar en Dart
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
909/)Evaluación Financiera de Proyectos de Inversión
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24908/)Complete
 Chibi Drawing Course: Draw Adorable Characters!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24907/)Cisco BGP Ma
sterclass for Enterprise Network Engineers
* Java SE 11 Developer 1Z0-819 OCP Course – Part 1
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/24906/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24905/)Flutter & OCR – Build Cam Sc
anner Clone in Flutter 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24904/)Complete Java Software Developer 
Masterclass (for Java 10)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24903/)Planificación y Gestión de Proyecto
s: PMBOK y Agile Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24902/)Control Estadístico de Procesos Six Si
gma (6 σ) con Minitab
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24901/)Finanzas Para No Financieros: Análisis 
y Visualización
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24900/)Modelación de Procesos de Negocios (BPMN 2.0)
 con Bizagi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24899/)Modelos Financieros en Excel para la Valoración d
e Empresas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24898/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hast
a Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24897/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso
 a Paso
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24896/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto
!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24895/)Crea tu propio PayPal desde cero con Django y React Native

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24894/)Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24893/)Modelos de Riesgo Crédito con Python
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24892/)Formation Complète: Création Application-Android Studio/Java
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24891/)ArcGIS specialization – ArcGIS Pro, 3D and ArcHydro -AulaGEO
* Big Data Hadoop Course
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/24890/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24889/)Bus
iness Analytics Online Class
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24888/)Advanced Project Management: Str
ategies for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24887/)Customer Experience with Generative AI: A
dvanced CX with AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24886/)Learn Java Masterclass(updated to Java 17)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24885/)Learn Shopify Now: Shopify for Beginners
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24884/)Lean Six Sigma Yellow Belt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4883/)How to Find Freelance Social Media Management Jobs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24882/)Sola
r Cell Technology
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24881/)Master Any Language with ChatGPT: Boost You
r Language Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24880/)Success Exam | Python NLTK : Natural Langua
ge ToolKit | NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24879/)Design of Wastewater Systems – SewerGEMS – A
ulaGEO
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24878/)Mastering English Idioms: Essential for ESL Communicat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24877/)Structural&Construction Design of 2000m2 real Project Vil
la
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24876/)Mastering Social Media Marketing: A Comprehensive Guide
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24875/)Amazon Dropshipping FBM | Titans Product Research Formula
* Bus
iness Process Optimization with Lean Six Sigma
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24874/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24873/)Cybersecurity for Developers: From Basics to Best Practices
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24872/)Mastering ServiceNow Admin&Development From Beginner to Pro
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/24871/)Comprehensive React JS Practice Test : Skill Mastery
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24870/)Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24869/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/24868/)Data Science Career Path
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24867/)Profi
ciency In Javascript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24866/)Discover Your Career Path & Land a Job Y
ou Love in 12 Weeks
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24865/)The Best ChatGPT & AI Course: Make Money 
With AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24864/)Architectural Shop Drawing Plans in AutoCAD 2020
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24863/)Internet of Things (IoT) Online Course
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24862/)Oracle PL/SQL: From Basics to Advanced Database Programming
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/24861/)Oracle RMAN: Comprehensive Backup and Recovery Techniques
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24860/)GSDC Certified Generative AI Professional – Exams
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/24859/)Oracle Database Administration: Oracle DBA Fundamentals
* Mastering Project Schedule Management and Es
timation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24858/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24857/)Mastering Software Estimation: Techniques and Best Practices
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24856/)Mastering CMMI: Process Improvement and Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
855/)Function Point Analysis FPA: A Guide to Software Estimation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/248
54/)Start a Digital Sales Business with Free Products to Sell
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24853/
)Mastering Oracle SQL: From Fundamentals to Advanced Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24852/
)NGINX, Apache, SSL Encryption – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24851/)API Tes
ting with Postman: From Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24850/)AWS Interview Pr
eparations: Quiz Solutions and Explanations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24849/)Learn the Python 
Programming Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24848/)Winning Option Strategies For Any Market

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24847/)2024 Complete Python Bootcamp from Zero to Hero in Python
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24846/)ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24845/)Become HTML Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24844/)Mastering iOS Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24843/)AutoCAD 2024 para Mac OS

* Learn Word Now: Microsoft Word 365 for Beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24842/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24841/)DEA-1TT4: Dell EMC Associate Practice test 2024
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/24840/)Presentations with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2483
9/)DEA-41T1: Dell EMC PowerEdge Associate Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24838/)
Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24837/)Pitch Deck Hero: Business Presenta
tion and Communication
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24836/)Key Metrics of Unit Economics (CPA, AR
PU, CAC, ARPPU, C1)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24835/)7 Days Meditation Challenge
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/24834/)300-435: Cisco Enterprise Solutions Practice test 2024
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24833/)Day Trading for Beginners: How to Make Money Trading Stocks
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24832/)أسئلة وتدريبات عملية في المحاسبة المالية
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24831/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24830/)Revit Nested Families- Parametric Container- From Zero
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24829/)Learn Functions & Function Expressions in Modern JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/24828/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24827/)
Modern Android App Architecture
* Amazon SEO Guide: How to Rank First on Amazon
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/24826/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24825/)AutoCAD 2024 – from Zero to Advanced- Full
 Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24824/)ChatGPT for Product Management & Innovation
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24823/)Your Guide To Health
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/24822/)WEB3 Token Gating. Create an NFT gated website from scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/24821/)Generative AI for All: Practical Prompt Engineering Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24820/)Cómo Crear un Blog con WordPress Para Principiantes 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2481
9/)Máster en Comercio Electrónico con WordPress 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24818/)Cómo Cre
ar una Academia Online con WordPress y Tutor LMS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24817/)Elementor Ki
ts: Crea una Página Web con Elementor Pro 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24816/)Cómo Crear una
 Tienda Online con Inteligencia Artificial
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24815/)Mastering Cryptocu
rrency Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24814/)Python Development & Data Science: Variables a
nd Data Types
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24813/)Exotic Pole Dance: Choreography, Breakdowns, Wa
rm-up, Splits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24812/)Inteligencia Artificial : Empodera tu Futuro La
boral
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24811/)Cybersecurity Awareness en Español
* Master Lead Genera
tion: Grow Subscribers & Sales with Popups
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24810/)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24809/)Mastering AWS Serverless: Hands-On with Core AWS Services
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/24808/)CSS, JavaScript And Python Complete Course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24807/)Ethical Hacking: Hack Linux Systems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24806/)Image
 Processing with Python PIL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24805/)Unit Economics & CRM: LTV, Churn,
 Retention Rates, Cohorts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24804/)5V0-22.23: VMware Certified Profess
ional – VMware vSAN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24803/)Machine Learning Intro for Python Dev
elopers

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1gswgdr/list_of_free_and_best_selling_discounted_courses/) , 2024-11-19-0913
```
# Udemy Free Courses for 17 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24922/)Fundamentals of Backend Engineering
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/24921/)Creación de una Tienda Virtual con Kotlin | Android Studio
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24920/)The Complete Deep Learning Course 2024 With 7+ Real Projects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24919/)Business Analytics con Python y ChatGPT: De Cero a Experto
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24918/)LangChain Mastery: Build GenAI Apps with LangChain &Pinecone
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24917/)Google Hacking – Aprende Búsquedas Avanzadas con Google
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24916/)VPS Linux en DigitalOcean:Ubuntu 22, Nginx, PHP y WordPress
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24915/)Vue JS (2 y 3) – Crea Aplicaciones Web Modernas con Vue
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24914/)Node.js – Creando API con Express y MongoDB (Incl. Deno)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24913/)ISO/IEC 27001 Implementando Seguridad de la Información
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24912/)ISO 22301 – Gestión de la Continuidad del Negocio
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24911/)MongoDB – La mejor Base de Datos NoSQL desde cero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24910/)Dart – La Guía Completa para Aprender a Programar en Dart
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
909/)Evaluación Financiera de Proyectos de Inversión
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24908/)Complete
 Chibi Drawing Course: Draw Adorable Characters!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24907/)Cisco BGP Ma
sterclass for Enterprise Network Engineers
* Java SE 11 Developer 1Z0-819 OCP Course – Part 1
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/24906/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24905/)Flutter & OCR – Build Cam Sc
anner Clone in Flutter 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24904/)Complete Java Software Developer 
Masterclass (for Java 10)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24903/)Planificación y Gestión de Proyecto
s: PMBOK y Agile Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24902/)Control Estadístico de Procesos Six Si
gma (6 σ) con Minitab
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24901/)Finanzas Para No Financieros: Análisis 
y Visualización
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24900/)Modelación de Procesos de Negocios (BPMN 2.0)
 con Bizagi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24899/)Modelos Financieros en Excel para la Valoración d
e Empresas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24898/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hast
a Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24897/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso
 a Paso
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24896/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto
!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24895/)Crea tu propio PayPal desde cero con Django y React Native

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24894/)Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24893/)Modelos de Riesgo Crédito con Python
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24892/)Formation Complète: Création Application-Android Studio/Java
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24891/)ArcGIS specialization – ArcGIS Pro, 3D and ArcHydro -AulaGEO
* Big Data Hadoop Course
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/24890/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24889/)Bus
iness Analytics Online Class
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24888/)Advanced Project Management: Str
ategies for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24887/)Customer Experience with Generative AI: A
dvanced CX with AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24886/)Learn Java Masterclass(updated to Java 17)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24885/)Learn Shopify Now: Shopify for Beginners
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24884/)Lean Six Sigma Yellow Belt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4883/)How to Find Freelance Social Media Management Jobs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24882/)Sola
r Cell Technology
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24881/)Master Any Language with ChatGPT: Boost You
r Language Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24880/)Success Exam | Python NLTK : Natural Langua
ge ToolKit | NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24879/)Design of Wastewater Systems – SewerGEMS – A
ulaGEO
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24878/)Mastering English Idioms: Essential for ESL Communicat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24877/)Structural&Construction Design of 2000m2 real Project Vil
la
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24876/)Mastering Social Media Marketing: A Comprehensive Guide
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24875/)Amazon Dropshipping FBM | Titans Product Research Formula
* Bus
iness Process Optimization with Lean Six Sigma
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24874/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24873/)Cybersecurity for Developers: From Basics to Best Practices
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24872/)Mastering ServiceNow Admin&Development From Beginner to Pro
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/24871/)Comprehensive React JS Practice Test : Skill Mastery
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24870/)Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24869/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/24868/)Data Science Career Path
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24867/)Profi
ciency In Javascript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24866/)Discover Your Career Path & Land a Job Y
ou Love in 12 Weeks
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24865/)The Best ChatGPT & AI Course: Make Money 
With AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24864/)Architectural Shop Drawing Plans in AutoCAD 2020
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24863/)Internet of Things (IoT) Online Course
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24862/)Oracle PL/SQL: From Basics to Advanced Database Programming
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/24861/)Oracle RMAN: Comprehensive Backup and Recovery Techniques
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24860/)GSDC Certified Generative AI Professional – Exams
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/24859/)Oracle Database Administration: Oracle DBA Fundamentals
* Mastering Project Schedule Management and Es
timation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24858/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24857/)Mastering Software Estimation: Techniques and Best Practices
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24856/)Mastering CMMI: Process Improvement and Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
855/)Function Point Analysis FPA: A Guide to Software Estimation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/248
54/)Start a Digital Sales Business with Free Products to Sell
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24853/
)Mastering Oracle SQL: From Fundamentals to Advanced Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24852/
)NGINX, Apache, SSL Encryption – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24851/)API Tes
ting with Postman: From Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24850/)AWS Interview Pr
eparations: Quiz Solutions and Explanations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24849/)Learn the Python 
Programming Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24848/)Winning Option Strategies For Any Market

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24847/)2024 Complete Python Bootcamp from Zero to Hero in Python
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24846/)ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24845/)Become HTML Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24844/)Mastering iOS Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24843/)AutoCAD 2024 para Mac OS

* Learn Word Now: Microsoft Word 365 for Beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24842/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24841/)DEA-1TT4: Dell EMC Associate Practice test 2024
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/24840/)Presentations with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2483
9/)DEA-41T1: Dell EMC PowerEdge Associate Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24838/)
Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24837/)Pitch Deck Hero: Business Presenta
tion and Communication
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24836/)Key Metrics of Unit Economics (CPA, AR
PU, CAC, ARPPU, C1)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24835/)7 Days Meditation Challenge
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/24834/)300-435: Cisco Enterprise Solutions Practice test 2024
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24833/)Day Trading for Beginners: How to Make Money Trading Stocks
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24832/)أسئلة وتدريبات عملية في المحاسبة المالية
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24831/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24830/)Revit Nested Families- Parametric Container- From Zero
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24829/)Learn Functions & Function Expressions in Modern JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/24828/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24827/)
Modern Android App Architecture
* Amazon SEO Guide: How to Rank First on Amazon
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/24826/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24825/)AutoCAD 2024 – from Zero to Advanced- Full
 Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24824/)ChatGPT for Product Management & Innovation
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24823/)Your Guide To Health
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/24822/)WEB3 Token Gating. Create an NFT gated website from scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/24821/)Generative AI for All: Practical Prompt Engineering Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24820/)Cómo Crear un Blog con WordPress Para Principiantes 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2481
9/)Máster en Comercio Electrónico con WordPress 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24818/)Cómo Cre
ar una Academia Online con WordPress y Tutor LMS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24817/)Elementor Ki
ts: Crea una Página Web con Elementor Pro 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24816/)Cómo Crear una
 Tienda Online con Inteligencia Artificial
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24815/)Mastering Cryptocu
rrency Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24814/)Python Development & Data Science: Variables a
nd Data Types
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24813/)Exotic Pole Dance: Choreography, Breakdowns, Wa
rm-up, Splits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24812/)Inteligencia Artificial : Empodera tu Futuro La
boral
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24811/)Cybersecurity Awareness en Español
* Master Lead Genera
tion: Grow Subscribers & Sales with Popups
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24810/)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24809/)Mastering AWS Serverless: Hands-On with Core AWS Services
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/24808/)CSS, JavaScript And Python Complete Course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24807/)Ethical Hacking: Hack Linux Systems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24806/)Image
 Processing with Python PIL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24805/)Unit Economics & CRM: LTV, Churn,
 Retention Rates, Cohorts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24804/)5V0-22.23: VMware Certified Profess
ional – VMware vSAN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24803/)Machine Learning Intro for Python Dev
elopers

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies)
```
---

     
 
all -  [ Find tech partner ](https://www.reddit.com/r/LangChain/comments/1gsuspk/find_tech_partner/) , 2024-11-19-0913
```
WeChat/QQ AI Assistant Platform - Ready-to-Build Opportunity

Find Technical Partner

1. Market

WeChat: 1.3B+ monthly a
ctive users
QQ: 574M+ monthly active users
Growing demand for AI assistants in Chinese market
Limited competition in spe
cialized AI assistant space


2. Why This Project Is Highly Feasible Now

Key Infrastructure Already Exists
LlamaCloud h
andles the complex RAG pipeline:
Professional RAG processing infrastructure
Supports multiple document formats out-of-bo
x
Pay-as-you-go model reduces initial investment
No need to build and maintain complex RAG systems
Enterprise-grade reli
ability and scalability


Mature WeChat/QQ Integration Libraries:

Wechaty: Production-ready WeChat bot framework
go-cqh
ttp: Stable QQ bot framework
Rich ecosystem of plugins and tools
Active community support
Well-documented APIs

3. Busin
ess Model

B2B SaaS subscription model
Revenue sharing with integration partners
Custom enterprise solutions

If you fin
d it interesting, please dm me
```
---

     
 
all -  [ This week in AI and Machine Learning:
🛸 US to Deploy World’s First Alien-Hunting System
👀 OpenAI’s T ](https://www.reddit.com/r/u_enoumen/comments/1gst4oj/this_week_in_ai_and_machine_learning_us_to_deploy/) , 2024-11-19-0913
```
# [This week in AI and Machine Learning: November 09th - November 17th  2024](https://apps.apple.com/ca/app/ai-machine-l
earning-4-dummies/id1611593573)

Listen at [https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds
-first-alien/id1684415169?i=1000677179618](https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds-
first-alien/id1684415169?i=1000677179618)

# 🛸 US to Deploy World’s First Alien-Hunting System:

# 👀 OpenAI’s Tumultuous
 Early Years Revealed in Emails:

# 🕶️ Samsung XR Glasses Specs Revealed in a Leak:

# 📄 Google Docs Introduces AI Image
 Creation:

# 🟦 Bluesky Won’t Use Posts for AI Training:

# Microsoft and NASA Launch AI Earth Copilot:

# ChatGPT Deskt
op Apps Receive Major Upgrades:

# Anthropic Partners with U.S. Government to Prevent AI Nuclear Leaks:

# AI Poetry Out
shines Human Classics in Blind Test:

# ChatGPT Desktop App Gains Direct App Integration:

# IBM's Most Compact AI Model
s Target Enterprises:

# TikTok Launches Symphony Creative Studio:

# New architecture may have cracked the Language of 
Life: An LLM for DNA and Biology.

# [💪 AI and Machine Learning For Dummies](https://apps.apple.com/ca/app/ai-machine-le
arning-4-dummies/id1611593573)

Djamgatech has launched a new educational app on the Apple App Store, aimed at simplifyi
ng AI and machine learning for beginners.

**It is a mobile App that can help anyone Master AI & Machine Learning on the
 phone!**

**Download 'AI and Machine Learning For Dummies ' FROM APPLE APP STORE and conquer any skill level with inter
active quizzes, certification exams, & animated concept maps in:**

* **Artificial Intelligence**
* **Machine Learning**

* **Deep Learning**
* **Generative AI**
* **LLMs**
* **NLP**
* **xAI**
* **Data Science**
* **AI and ML Optimization**

* **AI Ethics & Bias ⚖️**

**& more! ➡️**[ App Store Link: ](https://apps.apple.com/ca/app/ai-machine-learning-4-dummies
/id1611593573)[https://apps.apple.com/ca/app/ai-machine-learning-4-dummies/id1611593573](https://apps.apple.com/ca/app/a
i-machine-learning-4-dummies/id1611593573)

# [AI Consultation](http://djamgatech.com/contact-us/):

We empower organiza
tions to leverage the transformative power of Artificial Intelligence. Our AI consultancy services are designed to meet 
the unique needs of industries such as oil and gas, healthcare, education, and finance. **We provide customized AI and M
achine Learning podcast for your organization, training sessions, ongoing advisory services, and tailored AI solutions t
hat drive innovation, efficiency, and growth.**

Contact us [here](http://djamgatech.com/contact-us/) ([or email us at i
nfo@djamgatech.com](http://djamgatech.com/contact-us/)) to receive a personalized value proposition.



# [What Else Hap
pened in AI this Week?](https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds-first-alien/id16844
15169?i=1000677179618)

**Alibaba Cloud** released ***Qwen2.5-Coder-32B***, an open-source model for programming tasks t
hat matches the coding capabilities of GPT-4o. In addition to this flagship model, four new models have been released, e
xpanding the Qwen2.5-Coder family to a total of six models, ranging in sizes from 0.5B to 32B. An Artifacts app, similar
 to the Claude Artifacts, has also been launched. \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-a
i-news-trends-chatgpt-gemini-gen/id1684415169)\]

**Fixie AI** released ***Ultravox v0.4.1***, a family of multi-modal, 
open-source models trained specifically for enabling real-time conversations with AI. Ultravox does not rely on a separa
te automatic speech recognition (ASR) stage, but consumes speech directly in the form of embeddings. The latency perform
ance is comparable to the OpenAI Realtime . Fixie also released Ultravox Realtime, a managed service to integrate real t
ime AI voice conversations into applications \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-new
s-trends-chatgpt-gemini-gen/id1684415169)\].

**Google** introduced a new model ***Gemini (Exp 1114***), available now i
n Google AI Studio. It has climbed to joint #1 overall on the Chatbot Arena leaderboard, following over 6K+ community vo
tes in the past week. It matches the performance of 4o-latest while surpassing o1-preview and is #1 on Vision leaderboar
d \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\]
.

**Nexusflow** released ***Athene-V2***, an open source 72B model suite, fine-tuned from Qwen 2.5 72B. It includes Ath
ene-V2-Chat matching GPT-4o across multiple benchmark and Athene-V2-Agent, a specialized agent model surpassing GPT-4o i
n function calling and agent applications\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-tr
ends-chatgpt-gemini-gen/id1684415169)\].

**Vidu** launched ***Vidu-1.5***, a multimodal model with multi-entity consist
ency. Vidu-1.5 can seamlessly integrate people, objects, and environments to generate a video\[[Listen](https://podcasts
.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Codeium launched Windsurf 
Editor, an agentic IDE. It introduces ‘Flow’ a collaborative agent that combines the collaborative nature of copilots wi
th the ability to be independently powerful like an agent \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-
latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Researchers** introduced ***MagicQuill***, an intelligent i
nteractive image editing system. It uses a multimodal large language model to anticipate editing intentions in real time
, removing the need for explicit prompts \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-tr
ends-chatgpt-gemini-gen/id1684415169)\].

**DeepSeek** released ***JanusFlow***, an open-source unified multimodal model
 that excels at both image understanding & generation in a single model. It matches or outperforms specialized models in
 their respective domains and significantly surpasses existing unified models on standard benchmarks \[[Listen](https://
podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Google DeepMind*
* has open-sourced AlphaFold 3 for academic use. It models interactions between proteins, DNA, RNA, and small molecules.
 This is vital for drug discovery and disease treatment \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-la
test-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Epoch AI** launched ***FrontierMath***, a benchmark for advan
ced mathematical reasoning in AI. Developed with over 60 top mathematicians, it includes hundreds of challenging problem
s, of which AI systems currently solve less than 2% \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest
-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

TikTok launched Symphony Creative Studio, an AI-powered video-gener
ation tool for Business users. Users can turn product information or a URL into a video, add a digital avatar to narrate
 the video script, or localize any existing videos into new languages using translation and dubbing capabilities \[[List
en](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Nous R
esearch introduced the Forge Reasoning API Beta. It lets you take any model and superpower it with a code interpreter an
d advanced reasoning capabilities. Hermes 70B x Forge is competitive with much larger models from Google, OpenAI and Ant
hropic in reasoning benchmarks\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgp
t-gemini-gen/id1684415169)\].

Anthropic added a new prompt improver to the Anthropic Console. Take an existing prompt a
nd Claude will automatically refine it with prompt engineering techniques like chain-of-thought reasoning \[[Listen](htt
ps://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Nvidia presen
t Add-it, a training-free method for adding objects to images based on text prompts. Add-it works well on real and gener
ated images. It leverages an existing text-to-image model (FLUX.1-dev) without requiring additional training\[[Listen](h
ttps://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Microsoft r
eleased TinyTroupe, an experimental Python library for simulation of people with specific personalities, interests, and 
goals. These artificial agents - TinyPersons - can listen to us and one another, reply back, and go about their lives in
 simulated TinyWorld environments. This is achieved by leveraging the power of Large Language Models (LLMs), notably GPT
-4, to generate realistic simulated behavior \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-new
s-trends-chatgpt-gemini-gen/id1684415169)\].

Johns Hopkins researchers trained a surgical robot by having it watch vide
os of skilled surgeons. Using imitation learning, the robot learned complex tasks like suturing and tissue handling, ult
imately performing with skill comparable to human doctors \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-
latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Stripe launched a SDK built for AI agents - LLMs can call pay
ment, billing, issuing, etc APIs. It natively supports Vercel’s AI SDK, LangChain, and CrewAI, and works with any LLM pr
ovider that supports function calling\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends
-chatgpt-gemini-gen/id1684415169)\].

Researchers released OpenCoder, completely open-source and reproducible code LLM f
amily which includes 1.5B and 8B base and chat models. Starting from scratch, OpenCoder is trained on 2.5 trillion token
s and built on the transparent data process pipeline and reproducible dataset. It achieves top-tier performance on multi
ple code LLM evaluation benchmarks\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-ch
atgpt-gemini-gen/id1684415169)\].

Alibaba launched Accio, an AI search engine for small businesses to find wholesale pr
oducts alongside the analysis on their popularity with consumers and projected profit. Accio is powered by Alibaba’s Ton
gyi Qianwen large language model \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-cha
tgpt-gemini-gen/id1684415169)\].

Anthropic released RapidResponseBench, a benchmark that evaluates how well LLM defense
s can adapt to and handle different jailbreak strategies after seeing just a few examples \[[Listen](https://podcasts.ap
ple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

LangChain launched Prompt Can
vas, an interactive tool designed to simplify prompt creation. Prompt Canvas, the UX inspired from ChatGPT’s Canvas, let
s you collaborate with an LLM agent to iteratively build and refine your prompts\[[Listen](https://podcasts.apple.com/ca
/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

LangChain released Promptim, an experim
ental open-source library for prompt optimization. Promptim automates the process of improving prompts on specific tasks
. You provide initial prompt, a dataset, and custom evaluators (and optional human feedback), and promptim runs an optim
ization loop to produce a refined prompt that aims to outperform the original\[[Listen](https://podcasts.apple.com/ca/po
dcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Apple’s Final Cut Pro 11 with AI-powered f
eatures now available \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini
-gen/id1684415169)\].

ChatGPT app for Mac is now able to integrate with coding apps like Xcode, VS Code, TextEdit, and 
Terminal \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id168441
5169)\].
```
---

     
 
all -  [ Open Source RAG Repo: Everything You Need in One Place ](https://www.reddit.com/r/OpenSourceeAI/comments/1gsshf0/open_source_rag_repo_everything_you_need_in_one/) , 2024-11-19-0913
```
For the past 3 months, I’ve been diving deep into building RAG apps and found tons of information scattered across the i
nternet—YouTube videos, research papers, blogs—you name it. It was overwhelming.

So, I created [this repo](https://gith
ub.com/bRAGAI/bRAG-langchain) to consolidate everything I’ve learned. It covers RAG from beginner to advanced levels, sp
lit into 5 Jupyter notebooks:

* Basics of RAG pipelines (setup, embeddings, vector stores).
* Multi-query techniques an
d advanced retrieval strategies.
* Fine-tuning, reranking, and more.

Every source I used is cited with links, so you ca
n explore further. If you want to try out the notebooks, just copy the `.env.example` file, add your API keys, and you'r
e good to go.

Would love to hear feedback or ideas to improve it. (it is still a work in progress and I plan on adding 
more resources there soon!)

*In case the link above does not work here it is:* [https://github.com/bRAGAI/bRAG-langchai
n](https://github.com/bRAGAI/bRAG-langchain)

If you’ve found the repo useful or interesting, I’d really appreciate it i
f you could give it a ⭐️ on GitHub. It helps the project gain visibility and lets me know it’s making a difference.

Tha
nks for your support!

Edit:  
Thank you all for the incredible response to the repo—**380+ stars, 35k views, and 600+ s
hares in less than 48 hours!** 🙌

I’m now working on **bRAG AI** ([bragai.tech](https://www.bragai.tech/)), a platform t
hat builds on the repo and introduces features like interacting with hundreds of PDFs, querying GitHub repos with auto-i
mported library docs, YouTube video integration, digital avatars, and more. It’s launching next month - join the waitlis
t on the homepage if you’re interested!
```
---

     
 
all -  [ Multiple dependent tools ](https://www.reddit.com/r/LangChain/comments/1gsr4px/multiple_dependent_tools/) , 2024-11-19-0913
```
  
I would like some help/advice.  
I have a project I'm working on where I have an agent with multiple tools, but some 
tools need to be provided inputs from the outputs of other tools...  
for example, let's say one tool provides me with a
 URL of a webpage and the other scrapes it. the order of running must be 'get\_url\_tool' -> 'scrape\_web\_page\_tool'. 
 
what is a good way to ensure it happens in this order? is it even possible to do well?  
Example prompt for this scena
rio could be: 'Please download the best web page about pasta' or something of this sort.  
  
Also if I should do someth
ing else completely to achieve my goal it would be good to hear it.

about combining the tools to one tool, this won't r
eally do, since the first should be useable without the second one.

I'm, super new to all the AI Agent stuff so please 
be kind to a newbie!  
it's just an example scenario I'm working on something else entirely, thanks in advance for all a
nd any help! :D
```
---

     
 
all -  [ Can someone critique my resume? I've been applying the tips handed out around here. ](https://www.reddit.com/r/PHJobs/comments/1gsmsr4/can_someone_critique_my_resume_ive_been_applying/) , 2024-11-19-0913
```
[Page 1](https://preview.redd.it/5e25wt4uh91e1.png?width=604&format=png&auto=webp&s=f4b1e890b053ddd061a34fd368283438c0a4
3e5b)

[Page 2 \(Neglible tbh\)](https://preview.redd.it/basy849wh91e1.png?width=611&format=png&auto=webp&s=0ab0753fd6fb
3dcfcc6916bad7e10862609a7bbc)


```
---

     
 
all -  [ LangSec: A Security Framework for Text-to-SQL ](https://www.reddit.com/r/LangChain/comments/1gskn0q/langsec_a_security_framework_for_texttosql/) , 2024-11-19-0913
```
Concerned about security when using Text-to-SQL? We were too. That's why we created **langsec**, an open-source Python p
ackage that lets you define security schemas to enforce and validate LLM-generated SQL queries. Easy to integrate with y
our existing code.

[https://github.com/langsec-ai/langsec](https://github.com/langsec-ai/langsec)

If you find it usefu
l, please leave us a ⭐!
```
---

     
 
all -  [ Open Source RAG Repo: Everything You Need in One Place ](https://www.reddit.com/r/opensource/comments/1gsk82z/open_source_rag_repo_everything_you_need_in_one/) , 2024-11-19-0913
```
For the past 3 months, I’ve been diving deep into building RAG apps and found tons of information scattered across the i
nternet—YouTube videos, research papers, blogs—you name it. It was overwhelming.

So, I created [this repo](https://gith
ub.com/bRAGAI/bRAG-langchain) to consolidate everything I’ve learned. It covers RAG from beginner to advanced levels, sp
lit into 5 Jupyter notebooks:

* Basics of RAG pipelines (setup, embeddings, vector stores).
* Multi-query techniques an
d advanced retrieval strategies.
* Fine-tuning, reranking, and more.

Every source I used is cited with links, so you ca
n explore further. If you want to try out the notebooks, just copy the `.env.example` file, add your API keys, and you'r
e good to go.

Would love to hear feedback or ideas to improve it. (it is still a work in progress and I plan on adding 
more resources there soon!)

*In case the link above does not work here it is:* [https://github.com/bRAGAI/bRAG-langchai
n](https://github.com/bRAGAI/bRAG-langchain)

If you’ve found the repo useful or interesting, I’d really appreciate it i
f you could give it a ⭐️ on GitHub. It helps the project gain visibility and lets me know it’s making a difference.

Tha
nks for your support!

Edit:

Thank you all for the incredible response to the repo—**380+ stars, 35k views, and 600+ sh
ares in less than 48 hours!** 🙌

I’m now working on **bRAG AI** ([bragai.tech](https://www.bragai.tech/)), a platform th
at builds on the repo and introduces features like interacting with hundreds of PDFs, querying GitHub repos with auto-im
ported library docs, YouTube video integration, digital avatars, and more. It’s launching next month - join the waitlist
 on the homepage to stay updated!
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-19-0913
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

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-19-0913
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

     
