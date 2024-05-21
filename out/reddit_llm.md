 
all -  [ Multimodal RAG with text and images vs textual embeddings of images ](https://www.reddit.com/r/LangChain/comments/1cwpoc1/multimodal_rag_with_text_and_images_vs_textual/) , 2024-05-21-0910
```
Hi everyone,

I am currently building a location search assistant which, given an image or its textual description, retr
ieves the top k most similar locations by performing a multimodal RAG with langchain and chromaDB. While it seems pretty
 standard, I have been thinking about the different ways by which this kind RAG can be achieved. Specifically, I am thin
king between:

- Embedding images and location description, separately, by using CLIP and GPT-4, respectively. To keep t
rack of the location, I would include the corresponding location metadata during the insert

- Employing GPT-4 vision mo
del to provide a summary description of a location given all their images and store it together with the location descri
ption as one textual embedding

The first approach looks more precise to me since performing storing the summary descrip
tion of multiple images would encounter a loss of details. On the other side, it is still unclear to me how to handle sc
enarios in which users perform searching with both text and and image: which domain (vision or textual) would be preferr
ed to retrieve the most similar locations?

  
Am I missing something? What would you suggest in this case?

  

```
---

     
 
all -  [ Products built with LangChain ](https://www.reddit.com/r/LangChain/comments/1cwmp22/products_built_with_langchain/) , 2024-05-21-0910
```
Do you know any applications that are built with LangChain? Let's make a list. I'm wondering how well the tech has matur
ed and how heavily is it used in production apps.
```
---

     
 
all -  [ 0.2 docs refresh ](https://www.reddit.com/r/LangChain/comments/1cwkaq9/02_docs_refresh/) , 2024-05-21-0910
```
Hi all! One of the constant things we've heard from the community here is a desire for better docs. We've spent a lot of
 time over the past two weeks overhauling the documentation for 0.2. Some things include: versioned docs, a conceptual g
uide, much simpler navigation and organization, 'langchain over time', etc

We wrote a blog going through some of these 
two things as well as our thought process: [https://blog.langchain.dev/documentation-refresh-for-langchain-v0-2/](https:
//blog.langchain.dev/documentation-refresh-for-langchain-v0-2/)

We genuinely would love any feedback, no matter how sma
ll, on the new docs and ways to keep on improving them. A lot of the changes have been directly influenced by the commun
ity here - we really appreciate the feedback and ideas, so I hope you all know that :) Docs are a key focus of ours goin
g forward, and we'll be monitoring this thread pretty actively for ideas to implement!
```
---

     
 
all -  [ chatbot that can be corrected by users ](https://www.reddit.com/r/LangChain/comments/1cwk82e/chatbot_that_can_be_corrected_by_users/) , 2024-05-21-0910
```
Hello all. Disclaimer I'm a total newbie. Disclaimer 2 the user base is trusted so no need to fear about the dangers of 
implementing this for something like a public facing customer support bot.

I've got a RAG chatbot trained on some long 
PDFs (user manuals and stuff like that). One feature I'd like to implement is the ability for the user to correct the re
sponse given by the model, and for the model to learn from that.  
One very hacky idea I had was to use few-shot prompti
ng and every time a user makes a correction, update the system prompt with the question and corrected answer. The user b
ase for this bot would be very small, but still this idea seems kind of terrible lol.

Links to any resources where I ca
n learn more would be greatly appreciated.
```
---

     
 
all -  [ Looking for full-stack engineer | Legal AI Agents | Libra | Berlin, Germany ](https://www.reddit.com/r/LangChain/comments/1cwg46f/looking_for_fullstack_engineer_legal_ai_agents/) , 2024-05-21-0910
```
Hi Everyone, 

At Libra we're building AI agents capable of executing entire litigation workflows autonomously. [Libra](
http://libratech.ai/) is a seed stage company with a few pilot enterprise customers. At the moment we're a team of 5 bas
ed in Berlin and raised a $1M pre-seed round. We're looking for a full-stack engineer to join us full-time onsite/hybrid
. If you're excited about building the future of litigation, apply [here](https://www.linkedin.com/jobs/view/3913562327)
 or reach out [directly](mailto:viktors@libratech.ai)!
```
---

     
 
all -  [ Anyone want to join to dev node based visualized editor for LangGraph? ](/r/crewai/comments/1cvhip4/i_made_a_gui_for_crewai_node_based_visualized/) , 2024-05-21-0910
```

```
---

     
 
all -  [ Javascript vs Python ](https://www.reddit.com/r/LangChain/comments/1cwc0vx/javascript_vs_python/) , 2024-05-21-0910
```
I have tried to learn LangChain both on Python and Javascript, and from what I learnt, I can tell that Javascript is not
 supported as much as Python, but also I haven't really use it enough to really know the limit, so my question is how mu
ch is a gap between javascript and python with langchain 
```
---

     
 
all -  [ [For Hire] GenAI Specialist, Ex-Booking.com Data Scientist [50USD/hr] ](https://www.reddit.com/r/Entrepreneur/comments/1cwboz0/for_hire_genai_specialist_exbookingcom_data/) , 2024-05-21-0910
```
Hi, I am data analyst/scientist with 4 years experience. I have worked for one of the world biggest Telecom groups (Tele
nor) and also Agoda(Booking.com). Now working as GenAI specialist at vanna AI

If your looking to outsource tasks or get
ting something built in Python/R or QuickSense/Tableau please do reach out.


I can provide evidence of everything, I ev
en write about data science/analytics on Medium: https://python.plainenglish.io/sankeying-with-plotly-90500b87d8cf

GenA
I projects:
https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide
-decks-536f5fcb6e0e

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to-write-like-you-aab394d5
4792

Very good at making visualization. Will charge a reasonable rate
```
---

     
 
all -  [ How to match a photo of a printed letter with a template pdf with almost the same text ](https://www.reddit.com/r/LangChain/comments/1cw9hco/how_to_match_a_photo_of_a_printed_letter_with_a/) , 2024-05-21-0910
```
I want to match photos of official letters (printed, not handwritten) with one template of that same letter in PDF forma
t from a whole set of template PDFs. One of the templates contains roughly the same text, but features like salutations 
are different.

I was thinking of:

	1.	Creating embeddings of the photo and PDF and then doing a similarity search.
	2.
	Converting the photo and templates to text and comparing them at the sentence level.

The easiest would be if the photo
 and template had a QR code, but that’s not possible.

Any help is greatly appreciated!
```
---

     
 
all -  [ How to stop token Generation ](https://www.reddit.com/r/LangChain/comments/1cw8j5z/how_to_stop_token_generation/) , 2024-05-21-0910
```
I am using Open ai Api to stream the answer , I want to replicate the Stop generation function as in the chatgpt interfa
ce , can someone help me with how to stop token generation and not just streaming.
```
---

     
 
all -  [ Dialogflow cx with custom frontend ](https://www.reddit.com/r/LangChain/comments/1cw89go/dialogflow_cx_with_custom_frontend/) , 2024-05-21-0910
```
Hey! I'm facing issues in connecting custom frontend with dialogflow cx API (detect_intent), while trying to get paramet
er input in dialogflowcx. Has anybody worked on this?
```
---

     
 
all -  [ Is there a standardized/optimal way to do RAG context expansion? ](https://www.reddit.com/r/LangChain/comments/1cw61uj/is_there_a_standardizedoptimal_way_to_do_rag/) , 2024-05-21-0910
```
see title 
```
---

     
 
all -  [ Are LLM observability tools solutions in search of a problem? ](https://www.reddit.com/r/LangChain/comments/1cw0mkt/are_llm_observability_tools_solutions_in_search/) , 2024-05-21-0910
```
I noticed many LLM observability and monitoring tools are launched every week or so now. Are these tools actually used b
y real startups and companies, or are they more like 'solutions in search of a problem'?

These tools seem to do one or 
a combination of the following:

* **monitor LLM inputs and outputs** for prompt injection, adversarial attacks, profani
ty, off-topic content, etc
* **monitor LLM metrics over time** use such as cost, latency, readability, output length, cu
stom metrics (tone, mood, etc), drift
* **prompt management** including a/b testing, versioning, a gold standard set

Wh
at have you observed? Do companies that have their own LLM-powered features or products use these monitoring tools?
```
---

     
 
all -  [ What are my possibilities here in my project? ](https://www.reddit.com/r/LangChain/comments/1cvosry/what_are_my_possibilities_here_in_my_project/) , 2024-05-21-0910
```
Hello, Langchain community! I wanna talk about a project I'm working on and wanted to know if it's possible to do and if
 thats the best way of doing it. Resources that can help me would be quite welcome!

What I have regarding this API proj
ect is the [app.py](http://app.py) here  [https://github.com/Briqz23/Interactive\_RAG\_e-book/blob/main/agentapi/app.py]
(https://github.com/Briqz23/Interactive_RAG_e-book/blob/main/agentapi/app.py)



**Project Idea: An e-book where users c
an interact with the characters.**



**Current Implementation:**

* API endpoint: /character\_id/user\_input
* Data sou
rces and tools:
   *   FAISS DB with the book's PDF embedded and a retriever for it
   *   Tools in the toolkit include:

   * WikipediaQueryRun
   *  ArxivQueryRun
*   An agent uses OpenAI LLM, all the tools, and the contextualize\_q\_promp
t to select the best answer.

**Objective:**

When the agent retrieves an answer from WikipediaQueryRun or ArxivQueryRun
, it does not follow the instruction to behave as the specified character. I want to resolve this issue and implement an
other agent to check for hallucinations or ensure it behaves correctly. I am using a Langchain agent but intend to use a
 CrewAI agent.



**Challenges:**

I am struggling to implement the chat\_history feature in more complex scenarios, esp
ecially with the FastAPI API.



**End Goal:**

Create an API that processes user input and chat history. The input goes
 to an agent that queries various sources for the best answer. Another agent verifies the response's accuracy before the
 API returns the final answer.
```
---

     
 
all -  [ RAG agent is returning empty response once the libraries are updated to a newer version.  ](https://www.reddit.com/r/LangChain/comments/1cvlhwt/rag_agent_is_returning_empty_response_once_the/) , 2024-05-21-0910
```

I have a RAG framework where we are reading a doc and answering questions related to it, anyone know how can we debug a
n  agent to troubleshoot the error correctly 

Model - open ai 
```
---

     
 
all -  [ I want my agent to identify and save important/personal/relevant information to mongodb as i talk to ](https://www.reddit.com/r/LangChain/comments/1cvlhjx/i_want_my_agent_to_identify_and_save/) , 2024-05-21-0910
```
Hi,

So yeah i want the agent to automatically save data, for example, my name, birthday, my friends, emails, events, st
uff like that.

How can I do that, any suggestions would be welcomed!
```
---

     
 
all -  [ remix with langchain and openai ](https://www.reddit.com/r/remixrun/comments/1cvl852/remix_with_langchain_and_openai/) , 2024-05-21-0910
```
So I was trying to create a chatbot in my portfolio web app. The bot reads the json which my portfolio is using and inte
racts with the users if asked anything related to me.
everything working fine in local. but when deployed to vercel. cha
tbot is giving 500
so when I make a api/chat request, it fails but when I refresh the app, I can see the response in the
 log for / request. 
the actual request throwing
type error: nodeResponse. header.raw is not a function
I tried several 
ways but no luck. passed the headers. I googled it but no proper answer.

has anyone integrated it with remixjs before a
nd deployed on vercel?
```
---

     
 
all -  [ Feedback on my AI-powered Black Market? ](https://www.reddit.com/r/LangChain/comments/1cvkdja/feedback_on_my_aipowered_black_market/) , 2024-05-21-0910
```
Hey! 
I developed this experimental shopping experience that allows you to bargain with an AI to get the best deal possi
ble when buying some tees from creative services:
https://blackmarket.creativeservices.shop/
The AI has an embedded pers
onality, preferences, lore etc. and the more you connect with it, the more likely it is that you can get a discount.
I h
eavily used langchain to manage all RAG.

It is experimental, but functional. We are now working on some additional laye
rs to avoid prompt injection and other ai misbehaviors, but I would really love to get some feedback and ideas on how to
 improve it from the community!
```
---

     
 
all -  [ Need help in making an xlsx file using open ai ](https://www.reddit.com/r/LangChain/comments/1cvja66/need_help_in_making_an_xlsx_file_using_open_ai/) , 2024-05-21-0910
```
I have a usecase where I will be given a template of xlsx file and a set of instructions ( instructions are like set of 
commands that corresponds to manipulate the excel like can be  putting values in a particular column or a row  ( column 
and  can be conditional ) ) .

After following all the instructions and doing the changes in the xlsx file I have to ret
urn thr file back to the user .

The thing is template xlsx file contains additional information in the begining but the
 actual table where we want to manipulate the values may be strarting from any row ....

Any suggestions, how should I p
roceed, any idea is welcomed . Thank you
```
---

     
 
all -  [ Just Completed a 3x 3090 Build ](https://www.reddit.com/r/LocalLLaMA/comments/1cveol6/just_completed_a_3x_3090_build/) , 2024-05-21-0910
```
The Build:

* Intel i9 9820x w/ Corsair H150 3x120 AIO
* 128 GB DDR4 3600 MHz
* Asus X299 Deluxe II
* Various SSD's and 
NVME drives (I always load models from an NVME when possible!)
* 3x RTX 3090 - 2 Dell OEM, 1 ASUS AORUS - All on air coo
ling (Going to water imminently)
* Corsair HX1500 PSU

I've had this third RTX 3090 sitting around a little bit, problem
 is its a gargantuan card, essentially 4 slot cooler, and won't fit alongside 2x Dell 3090s which work so well together.
 So today I ran to the shop and grabbed a Define 7 XL case (Formerly had a Define 6), a Corsair HX 1500W psu (clearance 
for 220 CAD) and a PCIE riser kit. I knew I wasn't fitting 10 slots worth of GPU's into this case, but I had a pretty go
od idea how I would jank this thing in.

The PCIE riser (AVA Bracket/Riser kit) came with a handy bracket to vertically 
mount the GPU. Thankfully, the hole spacing is 140mm, and the R7 XL case has a 140mm fan mount at the back. Initially I 
intended on mounting the card to a fan which would be sandwiched between the GPU bracket and the case using some machine
 screws to hopefully transfer some stress to the case, instead of *through* the plastic fan. However, this shifted the p
lacement of the card a little to close to the motherboard, and the PCIE riser wouldn't reach the 2nd slot on the motherb
oard, so I had to mount the GPU bracket directly to the case (which can be about an inch further from the motherboard). 
Unfortunately, this means most of the GPU heat is exhausting through the CPU AIO radiator, absent a 140mm fan exhausting
 perpendicular to the AIO. I might think about this some more and possibly use the AIO as intake supplemented with a few
 140mm fans taking fresh cool air in with 3x 140mm fans exhausting. Or just go all water with 2x 420 mm radiators and 1x
 280mm. Surprisingly, the pci-e riser going over the top dell card doesn't hurt cooling too much. It's sitting at 92C @ 
100% TDP, vs 87C for the bottom card. I expected worse.

First benchmark wasn't even in fact an LLM, but a hash cat benc
hmark. MD5 performance is 210 GH/s. Phew. On a sustained load, the two Dell GPU's reach about 89C and 92C (hot spot) whi
le the Asus card reaches 105C and thermally throttles to about 85% TDP. I suspect this is because I didn't replace the t
hermal pads when I swapped the water block back to the air cooler (it came with the stock air cooler, but a water block 
was installed). Something to look at doing when I go water cooling.

My current project is a custom-rag utility that can
 take a number of user-uploaded documents they can assign to an 'expert'. The utility will create a dataset and FAISS in
dex for the assigned files and various 'experts' can be turned on and off by the user to ensure relevant retrieval and g
eneration, yet with broad knowledge should the user desire. Perhaps the framework can even handle which datasets to sear
ch in the future. I'm presently using DPR for passage retrieval but may look at other options. I've read things mentioni
ng Langchain but haven't yet investigated. Llama 3 8B instruct is the current generator (I didn't mess around too much w
ith quants of other 34b models or larger just yet) because it just seems to work and is great for testing; it loads quic
kly enough and generates a decent response. I'm fairly new to the world of LLM's and AI/ML as a whole, but I'm absolutel
y blown away with the progress made in the past 12 months. It's become my new hobby.

Why did I opt for a 3rd 3090? Hope
fully to generate with ~~command-r+ in 8bit~~ Llama 3 70B in 8 bit, of course!

Any thoughts for models you would try fi
rst? Custom-rag app advice? Benchmark suggestions? Critique on the build or suggestions for improving airflow? Lets hear
 it.

**If anyone is familiar with currently available water blocks for reference 3090 boards please comment here. <3**


Will update here as testing commences:

-Midnight-Miqu-70B-v1.5\_exl2\_5.0bpw: Loaded into 65 GB of VRAM. So far execut
ing very slow at 2-3 token/s. Suspect there's an issue here, the P states of GPU 0 and 2 are P8, so maybe thats it.

5/1
9/24 - 9:47 PM - Had to use 'nvidia-smi --lock-memory-clocks=9500' to keep all three cards in P2 state, or else during i
nference the 3rd would run in P8 with 400 MHz memory frequencies. I suspect this is because its not using the core on th
at card, and therefore sees no reason to 'wake up'. Now that's fixed, it won't load past the 2nd GPU now. As soon as the
 2nd becomes full, I get CUDA out of memory again. 

Another day, another problem. Such is life. 

https://preview.redd.
it/w40hdr9iwa1d1.png?width=1771&format=png&auto=webp&s=5384b0d73a9f95f0736ace58aba50274a252549e

https://preview.redd.it
/fz7sws9iwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=623d8ad17bdc9fe2cf723020daf0c8ef58f81978

https://preview.redd.it/
sbfxor9iwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=88629a1a6da24221779d0e8a07dd77830f2595ad

https://preview.redd.it/p
8ra9s9iwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=78f63222fa451153145734e6aed6b5101e38db63

https://preview.redd.it/5q
cgur9iwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=3ee0ce49d3079d27ba54852a95230960c72ca7ce

https://preview.redd.it/5v3
yk0aiwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=36be0dc0cefc592c486bc07247eda1595caa8fd7

https://preview.redd.it/hffh
igaiwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=9990685b9918051b96427903aa57705280a5af09

https://preview.redd.it/kg62b
s9iwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=bdd31ed90c7f66e7e9a7a5ee499f7dfddd160536

https://preview.redd.it/6if5wa
aiwa1d1.jpg?width=3072&format=pjpg&auto=webp&s=5b4bee6317dde48cb152762cbdafc794776af5c3
```
---

     
 
all -  [ Example of a chatless agentic workflow that keeps the human in the loop ](https://www.reddit.com/r/LangChain/comments/1cvavh7/example_of_a_chatless_agentic_workflow_that_keeps/) , 2024-05-21-0910
```
[https://colab.research.google.com/drive/1JBd3v4jt5GEU1zCiLnHsZsJjknR6\_Cm2?usp=sharing](https://colab.research.google.c
om/drive/1JBd3v4jt5GEU1zCiLnHsZsJjknR6_Cm2?usp=sharing)
```
---

     
 
all -  [ Cannot stream the output to Streamlit ](https://www.reddit.com/r/LangChain/comments/1cv5drf/cannot_stream_the_output_to_streamlit/) , 2024-05-21-0910
```
I am trying to stream the output of my chain to Streamlit, but without success.

This is the code:

`answer = st.write_s
tream(ai_assistant_chain.stream({'input': question, 'chat_history': st.session_state.chat_history}))`

And it gives the 
following result:

    [...]
    {
    'answer':' roi'
    }
    {
    'answer':' Lé'
    }
    {
    'answer':'op'
    
}
    {
    'answer':'old'
    }
    {
    'answer':' Ier'
    }
    [...]

Does somebody know what I have to do?

Strea
ming the output in a notebook works well:

    for chunk in ai_assistant_chain.stream({'input': question, 'chat_history'
: chat_history}):
        answer_chunk = str(chunk.get('answer'))
        print(answer_chunk, end='')
```
---

     
 
all -  [ Why choose any other LLM than gpt-4 or gpt-4o for our AI-based applications? ](https://www.reddit.com/r/LangChain/comments/1cv07x9/why_choose_any_other_llm_than_gpt4_or_gpt4o_for/) , 2024-05-21-0910
```
This is an extremely direct question. I'm trying to understand what leads to choosing an LLM (through API) other than GP
T-4 or GPT-4o since they already cover a good amount of use-cases for our AI-based products.

That's because I am curren
tly helping a company as a software engineer, and this question above is the one we keep racking our brains for and look
ing for a reason. 

  
Throw down some of your reasons, what are you using, why?

Thanks a lot guys
```
---

     
 
all -  [ React Agent - Arxiv tool is hallucinating ](https://www.reddit.com/r/LangChain/comments/1cuy96x/react_agent_arxiv_tool_is_hallucinating/) , 2024-05-21-0910
```
I am building a ReAct agent with arxiv tool usage so I can just chat with the agent to get interesting new papers. I am 
using a local LLM (Mistral Instruct 0.2) and not OpenAI. Overall, the model works well and uses most tools accurately. F
or Arxiv I am only getting hallucinations.

When I ask 'What's the paper 1605.08386 about?'

    The paper 1605.08386 is
 a review discussing the advancements and current state of deep learning techniques in the field of automatic speech rec
ognition (ASR), covering various deep learning architectures and their applications in ASR, as well as challenges and fu
ture directions.'

While it should return

    The paper '1605.08386' is about heat-bath random walks with Markov bases


I am using this as a resource [https://python.langchain.com/v0.1/docs/integrations/tools/arxiv/](https://python.langcha
in.com/v0.1/docs/integrations/tools/arxiv/)

Looking for tips to get the tool to work. I don't think this is a coding qu
estion but rather a configuration issue. 
```
---

     
 
all -  [ Multimodal RAG with GPT-4o and Pathway: Accurate Table Data Analysis from Financial Documents ](https://www.reddit.com/r/LangChain/comments/1cuy4e6/multimodal_rag_with_gpt4o_and_pathway_accurate/) , 2024-05-21-0910
```
Hey r/langchain I'm sharing a showcase on how we used GPT-4o to improve retrieval accuracy on documents containing visua
l elements such as tables and charts, applying GPT-4o in both the parsing and answering stages.

It consists of several 
parts:

**Data indexing pipeline (incremental):**

1. We extract tables as images during the parsing process.
2. GPT-4o 
explains the content of the table in detail.
3. The table content is then saved with the document chunk into the index, 
making it easily searchable.

**Question Answering:**

Then, questions are sent to the LLM with the relevant context (in
cluding parsed tables) for the question answering.

**Preliminary Results:**

Our method appears significantly superior 
to text-based RAG toolkits, especially for questions based on tables data. To demonstrate this, we used a few sample que
stions derived from the Alphabet's 10K report, which is packed with many tables.

**Architecture diagram**: [https://git
hub.com/pathwaycom/llm-app/blob/main/examples/pipelines/gpt\_4o\_multimodal\_rag/gpt4o.gif](https://github.com/pathwayco
m/llm-app/blob/main/examples/pipelines/gpt_4o_multimodal_rag/gpt4o.gif) 

**Repo and project readme**: [https://github.c
om/pathwaycom/llm-app/tree/main/examples/pipelines/gpt\_4o\_multimodal\_rag/](https://github.com/pathwaycom/llm-app/tree
/main/examples/pipelines/gpt_4o_multimodal_rag/)

We are working to extend this project, happy to take comments!
```
---

     
 
all -  [ “Live” RAG architecture? ](https://www.reddit.com/r/LangChain/comments/1cuuyzf/live_rag_architecture/) , 2024-05-21-0910
```
I’m looking to build a live search RAG chat system similar to Perplexity. What are the different architectural approache
s I could take (from high level).

Clean scraped html, chunk and embed then query and pull in? Or use an llm to parse th
e plain text from each scraped page and summarize it? Something else? 
```
---

     
 
all -  [ Overwhelmed with backend choices for features ](https://www.reddit.com/r/nextjs/comments/1cuu7we/overwhelmed_with_backend_choices_for_features/) , 2024-05-21-0910
```
Hey all, fairly new to NextJS and spent some time building up an MVP for a data project I’d like to offer to my local co
mmunity. 

Went with NextJS 14 (app router) on Vercel and used a combination of Shadcn & Recharts to get a nice proof of
 concept going with a data table and chart. 

Not sure if this is the best way to approach it, but I created a seed.ts f
irst for sample data, seeing as I know what the data model will look like. Now I need to figure out the best way to actu
ally handle the backend and I’m a little overwhelmed with all the options available.

Not planning on implementing any a
uth, ads or taking payment as its a pro bono project, but I do have some specific requirements around periodically grabb
ing data (via a combination of calling APIs and scraping some webpages). I also need to run an LLM step via LangChain to
 transform open text data to structured JSON and then ETLing into a database…

Have a preference for Python for the data
 work and saw that Vercel offer a runtime with cron jobs (and a PostgresDB) but I’ve already implemented a lot of the fr
ontend data transformation in TS… I’ve also seen that there are a ton of competing services from full BaaS solutions lik
e Supabase, Appwrite, Pocketbase, etc… to point solutions like trigger.dev, neon, and all the AWS/GCP/Azure offerings wi
th generous free tiers. 

I don’t expect the app to ever scale massively and I’m looking for a path of least resistance 
& complexity which will keep costs low; any experienced devs here willing to offer their $0.02? Thank you in advance!





```
---

     
 
all -  [ Representing a prompt chain / graph in a diagram for scientific publications  ](https://www.reddit.com/r/LangChain/comments/1cusnwj/representing_a_prompt_chain_graph_in_a_diagram/) , 2024-05-21-0910
```
Hello everyone,

I wonder which tools are out there to represent a prompt chain for scientific publications. Is there ma
ybe something mature like an UML notation for this specific case?

I know you can create an ascii or mermaid graph using
 langchain but this is not what I need.

Are there any opinions and suggestions from experienced users regarding tools t
o create prompt diagrams?
```
---

     
 
all -  [ can we return structured output with langchain agents? ](https://www.reddit.com/r/LangChain/comments/1cusa3a/can_we_return_structured_output_with_langchain/) , 2024-05-21-0910
```
been playing with agents for a while now, concretely via langchain tool calling agents/custom- is there a way to structu
re the (final) output to be schema tied (using pydantic as we have for llms)?

all my searches so far found either utili
zing some rural implementations like swarms or very simplistic ones (suited specifically for RAG)
```
---

     
 
all -  [ I am seeing weird behaviors in LLMs when using LangChain , to build simple chat apps.    ](https://www.reddit.com/r/LargeLanguageModels/comments/1cuqsin/i_am_seeing_weird_behaviors_in_llms_when_using/) , 2024-05-21-0910
```
When i use LLMs in my local machine using the Ollama Framework ,I use CLI to test the models out after downloading and t
he response i get for chat models is usually clear (sometimes it hallucinates). but mostly clear.

Then when i use Langc
hain to build functions using`PromptTemplate` ,`SequenceChains` the model will suddenly loose control and starts to gene
rate random output almost endlessly for 40-50mins or even more until i interrupt the notebook kernel. 

It is generating
 question answer pairs , or endless paragraphs 

I've experienced this behavior in many models; Gemma , LLaMa 2 , Qwen ,
 Phi 2 ( this one breaks often ) All around 2-5 B parameters 

**What is happening here ?? Is it due to some internal pr
ompt inside these Langchain abstractions??? idk what is causing this behavior . I always keep the temperature param at 0
 still this happens** 
```
---

     
 
all -  [ Training a chatbot based on chats ](https://www.reddit.com/r/LangChain/comments/1cuqbpq/training_a_chatbot_based_on_chats/) , 2024-05-21-0910
```
I'm working to build a solution using which a bot can be trained to behave as a person based on chat history of that per
son with other people. 

User uploads their chat history (WhatsApp, Slack, sms chats, etc.) and the bot learns the tone 
and memories from those chats to start behaving as a virtual avatar of the user.

Any pointers on where to start?

I wou
ld imagine the tool will need to extract memories from the chats. 
Then to learn the tone, it's either fine tuning or cr
eating system prompts based on the chat history.

Would love to know if anyone has attempted something like this.
```
---

     
 
all -  [ Advanced RAG without Langchain, LlamaIndex? ](https://www.reddit.com/r/LLMDevs/comments/1cuq21d/advanced_rag_without_langchain_llamaindex/) , 2024-05-21-0910
```
Are there resources to build advanced RAG systems without using tools like Langchain and LlamaIndex? These tools keep ch
anging their framework and documentation is poor. Looking to shift from depending on them. 

I want to build efficient R
AG systems for unstructured data (plain text, tables in CSV/XLS format) and also for structured SQL data.
```
---

     
 
all -  [ (Code included) Struggle to scrape websites and feed content to LLMs? I benchmarked some tools and t ](https://www.reddit.com/r/LangChain/comments/1cub6pg/code_included_struggle_to_scrape_websites_and/) , 2024-05-21-0910
```
Video: [https://www.youtube.com/watch?v=QxHE4af5BQE](https://www.youtube.com/watch?v=QxHE4af5BQE)

Code: [https://github
.com/trancethehuman/ai-workshop-code/blob/main/Web\_scraping\_for\_LLM\_in\_2024.ipynb](https://github.com/trancethehuma
n/ai-workshop-code/blob/main/Web_scraping_for_LLM_in_2024.ipynb)

  
Let me know what you think in the comments. I'll re
spond.
```
---

     
 
all -  [ Ingestion options for vectorDB ](https://www.reddit.com/r/vectordatabase/comments/1cu7e7n/ingestion_options_for_vectordb/) , 2024-05-21-0910
```
I’m trying to create some low latency ingestion ETL embedding pipelines into either pinecone or Zilliz or LanceDB for my
 application, the idea is whenever a user send some text, I can process and filter, group by then do llm assisted summar
ization immediately, then create embedding to save into a vectorDB without any intermediate storage. Fivetran only offer
s dbt on the storage layer, langchain does not handle sql processing, Dagster only deal with orchestration and seems mor
e appropriate for batch processing, aws lambda is the closest solution I can find but version control and monitoring mig
ht take some planning. setting up my own cluster just for this and monitoring it 24/7 seems the last resort. I wonder if
 there are other options. (We are a 3 person team, so coding time is really precious) thanks ahead! 
```
---

     
 
all -  [ Do you even need LangChain? ](https://www.reddit.com/r/LangChain/comments/1cu6wjg/do_you_even_need_langchain/) , 2024-05-21-0910
```
As a disclaimer: I personally think LangChain is awesome. It lets you cut your dev time by a lot. But since I've been to
ying around with many frameworks, tools, and models I compiled a list of five basic (but important) questions every dev 
or person looking to integrate AI must ask themselves.

**>>>** [**Watch on YouTube**](https://youtu.be/uG0cs8AlnHw)

  

I'd love to know your thoughts and/or suggestions!
```
---

     
 
all -  [ Introducing Cycls: A New AI Chat Framework ](https://www.reddit.com/r/Chatbots/comments/1cu5503/introducing_cycls_a_new_ai_chat_framework/) , 2024-05-21-0910
```
I wanted to introduce you to Cycls, a lightweight Python framework for developing and sharing AI chat applications. It's
 designed to simplify the process, offering features like easy publishing, instant sharing with public URLs, and multimo
dal input/output. Cycls supports popular models such as OpenAI and LangChain and includes a ready-to-use webchat fronten
d.

If you're into AI development, this might be worth checking out. You can learn more about it [here](https://docs.cyc
ls.com/overview).

What are your thoughts? Anyone planning to give it a try?
```
---

     
 
all -  [ Sentence / chunk window retrieval in Langchain using Qdrant ](https://www.reddit.com/r/LangChain/comments/1cu44i1/sentence_chunk_window_retrieval_in_langchain/) , 2024-05-21-0910
```
Guys,

Checkout this PR [\[https://github.com/langchain-ai/langchain/pull/21553\]](https://github.com/langchain-ai/langc
hain/pull/21553) that implements something similar to sentence window retrieval. I have named in chunk window retrieval 
because based on the window size, this method would fetch those many chunks above and below the current chunk. 

Importa
nt point to note here is that when creating a chunk for Qdrant, you MUST have integer based chunk id for this to work. H
ave added that support in Qdrant.add\_texts(..) as well. 

Hope it helps.
```
---

     
 
all -  [ Utilizing Neo4j's Knowledge Graph and Semantics for a RAG - Chatbot ](https://www.reddit.com/r/LangChain/comments/1cu2ozt/utilizing_neo4js_knowledge_graph_and_semantics/) , 2024-05-21-0910
```
I'm working on developing a chatbot that uses Neo4j as the database. I've created a knowledge graph by importing a corpu
s of data into Neo4j.  
how to effectively leverage both the knowledge graph aspect and the semantic capabilities of Neo
4j for this chatbot project?

Has anyone worked on a similar project? What strategies or approaches did you employ to op
timize the retrieval from Neo4j? I'm open to any suggestions or insights that could help improve the chatbot's performan
ce and make the most out of Neo4j's unique features.
```
---

     
 
all -  [ Gemini directed me to porn ](https://i.redd.it/bddxj0u0ly0d1.jpeg) , 2024-05-21-0910
```
All I asked was if it could create agents. The first link it provided is porn. 
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-21-0910
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-21-0910
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

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-21-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-21-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-21-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
