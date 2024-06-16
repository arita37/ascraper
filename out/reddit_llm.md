 
all -  [ Grafana + Ollama ](https://www.reddit.com/r/ollama/comments/1dguvr8/grafana_ollama/) , 2024-06-16-0958
```
What's the best way to integrate Ollama with Grafana (e.g. have Ollama summarize logs/dashboards/etc.)?  It looks like t
here is an LLM plugin for Grafana, but it appears to not support Ollama (https://github.com/grafana/grafana-llm-app/issu
es/162).

  
Would trying to feed the grafana API spec to Ollama and using langchain to query the API be the most straig
ht-forward approach?  
```
---

     
 
all -  [ save and load embeddings  ](https://www.reddit.com/r/LangChain/comments/1dgpc6w/save_and_load_embeddings/) , 2024-06-16-0958
```
i used chromadb with langchain to create embeddings. i used persistent\_directory to save those locally and it did but n
ow i am not able to load them. these are the codes

#saving embeddings

vector\_storage=Chroma.from\_documents(split,Oll
amaEmbeddings(model='nomic-embed-text'), persist\_directory='vector\_store',collection\_name='qna\_embeddings')

#loadin
g embeddings

vector\_store2=Chroma(persist\_directory='vector\_store',embedding\_function=OllamaEmbeddings(model='nomic
-embed-text'))

to check i printed the following and it gives 0 as output

print(vector\_store2.\_collection.count())

p
ls help me 
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day!
 ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1dgnx88/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-16-0958
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models. 
The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..



The API will cost just $99! One time paymen
t and you will receive the full system code!



If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-16-0958
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

     
 
all -  [  AI-Driven Job Application Enhancement System - Seeking Feedback and Suggestions! ](https://www.reddit.com/r/LangChain/comments/1dgnmjt/aidriven_job_application_enhancement_system/) , 2024-06-16-0958
```
Hi everyone,

I've been working on a project that aims to enhance job applications using AI. It's called [GenAI\_Job\_Fi
t](https://github.com/DAVEinside/GenAI_Job_Fit), and I would love for you all to check it out. I took inspiration from t
he Agent-Supervisor example notebook provided.

The system leverages AI to analyze job descriptions and tailor resumes t
o match job requirements, increasing the chances of getting noticed by recruiters and ATS (Applicant Tracking Systems). 
Here are some key features:

* Automated resume tailoring
* Keyword optimization
* Compatibility scoring between job des
criptions and resumes

I'd really appreciate it if you could take a look and let me know what you think. I'm particularl
y interested in any suggestions for improvements or additional features that could make the tool even more useful.

Feel
 free to fork the repo, open issues, or submit pull requests. Your feedback will be invaluable in making this project be
tter!

Repo Link : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)

Thank y
ou!
```
---

     
 
all -  [ Improving Performance for Data Visualization AI Agent ](https://medium.com/firebird-technologies/improving-performance-for-data-visualization-ai-agent-d677ccb71e81) , 2024-06-16-0958
```

```
---

     
 
all -  [ How to work with large data that is returned from an api? ](https://www.reddit.com/r/LangChain/comments/1dgm1ij/how_to_work_with_large_data_that_is_returned_from/) , 2024-06-16-0958
```
Hello! Im using the APIchain i use it to get data from an api endpoint, the problem is that the api returns a largue amo
unt of data in json format (i need all the data that the api returns), i will then use a agent to ask questions about th
at data but since is so massive there's problems like the token amount or time it takes to analyze, can anyone giveme so
me tips about what can i do to better the performance or what to do to solve this kind of problem? thanks alot!!!

this 
is the apiChain im using:

llm = OpenAI(temperature=0)  
chain = APIChain.from\_llm\_and\_api\_docs(  
llm,  
open\_mete
o\_docs.OPEN\_METEO\_DOCS,  
verbose=True,  
limit\_to\_domains=\['https://api.open-meteo.com/'\],  
)  
chain.run(  
'W
hat is the weather like right now in Munich, Germany in degrees Fahrenheit?'  
)
```
---

     
 
all -  [ Roast My Resume, Masters in Computer Science and 1.5 Years of Relevant Experience, Not Receiving Any ](https://www.reddit.com/r/resumes/comments/1dgkgl9/roast_my_resume_masters_in_computer_science_and/) , 2024-06-16-0958
```
Just as the title says. Been working as a Full Stack Developer at a startup for the past 7 months at very undesireable t
erms. It was the only software-related job I could land after getting my Masters. I've changed the layout and content of
 my resume multiple times with them having no effect. I recognize that a lot of my job experience bullets do not have qu
antitative results, but I am not sure what to put for these when I do not know the exact results. Do people just estimat
e a number or percentage when doing this? Any feedback on my resume would be greatly appreciated. I am in the NYC metro 
area.

https://preview.redd.it/ih8mpic07r6d1.png?width=1258&format=png&auto=webp&s=18bef7888a55acf35a679797c6da55fe2ea1d
eaa

https://preview.redd.it/7eqt3dmz6r6d1.png?width=1282&format=png&auto=webp&s=cc762c6111f23ebac6ef4de5ee1a2f186c80bcf
c
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day! ](https://www.reddit.com/r/AiForSmallBusiness/comments/1dgik4p/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-16-0958
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models.

The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..

The API will cost just $99! One time payment 
and you will receive the full system code!

If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ What’s Memory Tuning and how does it give higher accuracy + speed than RAG and prompting? ](https://www.reddit.com/r/LangChain/comments/1dgi0vj/whats_memory_tuning_and_how_does_it_give_higher/) , 2024-06-16-0958
```
First, how it works:

- Memory Tuning fine-tunes millions of LoRA adapters (memory experts) on any open-source LLM to en
sure accurate fact recall.

- During inference, the model retrieves and integrates the most relevant experts, (a lot lik
e information retrieval). This gives much high accuracy and reduced hallucinations.

- This approach maintains the model
's ability to generalise — while at the same time focusing on zero error for specified facts.

Why is this better than R
AG?

RAG shifts probabilities without eliminating errors — while Memory Tuning fully corrects inaccuracies.

[Lamini](ht
tps://www.linkedin.com/company/lamini-ai/) released their Memory Tuning solution for enterprises with case studies showi
ng amazing accuracy boosts for text-to-sql, labelling, and even recommendation tasks.

Paper: [https://github.com/lamini
-ai/Lamini-Memory-Tuning/blob/main/research-paper.pdf](https://github.com/lamini-ai/Lamini-Memory-Tuning/blob/main/resea
rch-paper.pdf)



I share high quality AI updates and tutorials daily on my LinkedIn: [https://www.linkedin.com/in/sarth
akrastogi/](https://www.linkedin.com/in/sarthakrastogi/)

If you like this post and want to stay updated on latest AI re
search, you can check out: [https://linktr.ee/sarthakrastogi](https://linktr.ee/sarthakrastogi).


```
---

     
 
all -  [ Where Can I Find Deterministic Tools for AI Agents?  ](https://www.reddit.com/r/AI_Agents/comments/1dggm9v/where_can_i_find_deterministic_tools_for_ai_agents/) , 2024-06-16-0958
```
Hi guys,

I've started working on building my own AI Agent, but I'm finding that I have to create all the tools myself f
rom scratch. I'm a junior AI Engineer and it's a bit overwhelming, I'm finding that most of these tools are purely softw
are-based.

Does anyone know of any libraries that offer pre-built deterministic tools that I can use with my AI Agent?


I'm currently using some tools from Langchain, but they're not quite specific enough for what I need. Is anyone else fa
cing the same challenge, or is it just my lack of experience showing? 😅

Any help or recommendations would be greatly ap
preciated!

Thanks!
```
---

     
 
all -  [ How to Repurpose YouTube Videos for Free Using AI and No-Code Tools in 2024 ](https://www.reddit.com/r/AiChampions/comments/1dgfyuk/how_to_repurpose_youtube_videos_for_free_using_ai/) , 2024-06-16-0958
```
Video content repurposing tools are usually quite expensive. 

But using this trick, you can repurpose video content com
pletely FREE.

From a YouTube URL, we can now generate multiple video clips, and even a title & a description for each c
lip.  

Complete no-code flow below ↓

[Repurpose YouTube Videos for Free](https://reddit.com/link/1dgfyuk/video/e04u7o5
61q6d1/player)

We recently launched a webinar series where we cover multiple AI app-building topics. 

Naturally, this 
led us to wonder: 

could AI help us identify all the subtopics we discuss & create smaller, more focused clips for each
 one? 

Turns out, it's possible! 

A rough sketch of the idea.

[Subtopics AI Idea Rough Sketch](https://preview.redd.i
t/igdc1jv91q6d1.jpg?width=2895&format=pjpg&auto=webp&s=071ffa2a8fb271b59e8c7018aa7a9dab82da676f)

Implemented the 3 step
s below in langflow.

**Step 1**

https://preview.redd.it/njrh82wi1q6d1.jpg?width=2084&format=pjpg&auto=webp&s=c22ecad57
063c30785de94542c05c171d14bcbb3

We download the video and generate a transcript. 

One could use YT subtitles or [Whisp
er](https://honeysyed.com/whispertranscribe) to generate a transcript with timestamps.

**Step 2**

https://preview.redd
.it/2lgkdf5l1q6d1.jpg?width=2488&format=pjpg&auto=webp&s=d210a268113d084072018c0edf9bdd6e2b1ff49b

Send the transcript t
o a local LLM or a hosted one. 

The key is to get a structured response with start & end timestamps. (bonus: generate T
itle, Description & even a blog post for each clip)

LangChain makes this quite easy with output parsers (added to a Lan
gFlow custom comp.)

**Step 3**

Generate clips based on the timestamps from the last step (used ffmpeg).

Below are the
 clip details generated for a Paul Graham video.

[YouTube Title and Description](https://preview.redd.it/xbg4xbct1q6d1.
jpg?width=2048&format=pjpg&auto=webp&s=caed9c5b2d9a2f18d2337b2594ebfcbeeac15b28)

Now you can repost the smaller clips b
ack to YT with the title and descriptions provided for each clip.

The complete no-code working flow is available in the
 LangFlow store (for free) as 'YouTube Subclips Generator'.

[Source](https://x.com/MisbahSy/status/1799083774912974957)

```
---

     
 
all -  [ Streaming of OpenAIAssistant v2 ](https://www.reddit.com/r/LangChain/comments/1dgfsmg/streaming_of_openaiassistant_v2/) , 2024-06-16-0958
```
Hello all, 
OpenAI assistant should support streaming.
But I am not sure why the current OpenAIAssistantV2Runnable do no
t supports it.
Is there a solution to this?
 
```
---

     
 
all -  [ How to securely pass private data? ](https://www.reddit.com/r/LangChain/comments/1dfyz50/how_to_securely_pass_private_data/) , 2024-06-16-0958
```
Wondering if anyone here has dealt with passing private information from end user inputs to your LLM, later to interact 
with an external API? I'm not talking about authentication data per se, just private information (e.g PII) people wouldn
't normally want to share on the internet.   
What solution have you come up with to ensure some privacy for your users?

```
---

     
 
all -  [ Evaluating with Ragas ](https://www.reddit.com/r/LangChain/comments/1dfxwga/evaluating_with_ragas/) , 2024-06-16-0958
```
I've finished my rag job, and performed a evaluation on my rag. results given below

[ragas output](https://preview.redd
.it/pt0khqy10l6d1.png?width=1280&format=png&auto=webp&s=4979a08f0e648937407d23feeb494f02a8e793ba)

context\_precision is
 better than good but why the other metrics sucks and how to improve them?
```
---

     
 
all -  [ RAG Me Up - RAG for chat /w Langchain ](https://www.reddit.com/r/LangChain/comments/1dfx2di/rag_me_up_rag_for_chat_w_langchain/) , 2024-06-16-0958
```
We are in early stages of developing our project so keen feedback. RAG Me Up is a robust layer on top of Langchain desig
ned to make RAG easy and also not prone to simple issues like document re-retrieval, performance for rephrasind and perh
aps most importantly: make Langchain work well with Instruct/Chat models' templates.

[https://github.com/AI-Commandos/R
AGMeUp ](https://github.com/AI-Commandos/RAGMeUp)
```
---

     
 
all -  [ AI Innovations: Streamlining Insurance Claims, Enhancing Engineering Projects, and Revolutionizing P ](https://www.reddit.com/r/ai_news_by_ai/comments/1dfvkcx/ai_innovations_streamlining_insurance_claims/) , 2024-06-16-0958
```





#vc #tool #release #hardware #event #feature #opinions #opensource #update #major_players #science #leaders #startu
ps #scheduled

Y Combinator's S24 startup, ClaimSorted, is leveraging AI technology to streamline insurance claims proce
ssing, aiming to enhance customer experience and drive cost efficiencies [1]. Another startup from the same batch, Entan
gl_AI, has launched a platform that automates error detection in engineering projects, potentially saving time, money, a
nd lives by identifying and fixing design issues early [2].







The Data AI Summit will feature a fireside chat with 
NVIDIA AI Developer and Databricks Co-Founder and CEO, along with several informative sessions [3]. These include a sess
ion on the rapid development and deployment of Generative AI apps at scale with NVIDIA NIM [4], a session on Architectur
e Analysis for ETL Processing: CPU vs GPU [5], and a session on unlocking the power of Spark RAPIDS ML for GPU-accelerat
ed distributed machine learning [6]. 







NVIDIA AI Developer has also discussed the benefits of TensorRT Weight-Stri
pped Engines, which offer over 95% compression, support various models, and allow for refitting with weights directly on
 end-user devices [7]. The use of generative AI in CVE analysis can significantly enhance security workflows, with Agent
 Morpheus, a generative AI application, automating the process of detecting and remediating CVEs [8].







The era of 
the AI PC has arrived, offering unparalleled performance in generative tasks with NVIDIA RTX and GeForce RTX technologie
s [9]. Andrew Ng has developed an agentic machine translation demonstration that prompts a language model to translate t
ext, reflects on the translation to provide suggestions, and refines the translation based on those suggestions [10].








Groq Inc announced their GM of GroqCloud, Sundeep, and is hosting a follow-up AMA session to answer more questions 
about scaling for the fastest AI inference [12][13]. The company also powered the Build Together AI Hackathon, where 28 
incredible apps were created [14]. A webinar titled 'Build Blazing-Fast LLM Apps with Groq, LangFlow, & LangChain' is sc
heduled to take place, showcasing how Groq's AI inference technology integrates with LangFlow and LangChain to create po
werful applications using Large Language Models (LLMs) [15].







a16z emphasizes the importance of rethinking product
s from the ground up, rather than just adding AI, and discusses the evolution from AI-augmented to AI-native products on
 their podcast [16]. Vivek Natarajan, a Research Lead at Google Health AI, is focusing on AI and biomedicine with Projec
t AMIE [18]. OpenAI clarifies that their strategic cloud relationship with Microsoft remains unchanged, and they have a 
partnership with OCI to use the Azure AI platform on OCI infrastructure for inference and other needs [20].







Midjo
urney has announced several updates, including the release of model personalization, the development of a new set of alg
orithms, the alpha testing phase for a new feature, and the ability of their AI to figure things out from other people's
 images [21][22][23][24][25]. Stability AI has announced the release of Stable Diffusion 3 Medium, a text-to-image AI mo
del with two billion parameters, optimized for consumer PCs and laptops, as well as enterprise-tier GPUs [26].




[1. Y
 Combinator @ycombinator https://twitter.com/ycombinator/status/1800558618497962219](https://twitter.com/ycombinator/sta
tus/1800558618497962219)

[2. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1800573712862695857](http
s://twitter.com/ycombinator/status/1800573712862695857)

[3. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIA
AIDev/status/1800574724944048585](https://twitter.com/NVIDIAAIDev/status/1800574724944048585)

[4. NVIDIA AI Developer @
NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800574733043323141](https://twitter.com/NVIDIAAIDev/status/180057473
3043323141)

[5. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800574743550038505](https://tw
itter.com/NVIDIAAIDev/status/1800574743550038505)

[6. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/
status/1800574751183634542](https://twitter.com/NVIDIAAIDev/status/1800574751183634542)

[7. NVIDIA AI Developer @NVIDIA
AIDev https://twitter.com/NVIDIAAIDev/status/1800603157665354116](https://twitter.com/NVIDIAAIDev/status/180060315766535
4116)

[8. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800619033487692240](https://twitter.
com/NVIDIAAIDev/status/1800619033487692240)

[9. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status
/1800913453483225108](https://twitter.com/NVIDIAAIDev/status/1800913453483225108)

[10. Andrew Ng @AndrewYNg https://twi
tter.com/AndrewYNg/status/1800582171259982289](https://twitter.com/AndrewYNg/status/1800582171259982289)

[11. Pika @pik
a_labs https://twitter.com/pika_labs/status/1800593550494863425](https://twitter.com/pika_labs/status/180059355049486342
5)

[12. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800563455977750704](https://twitter.com/GroqInc/status/18
00563455977750704)

[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800589921876312090](https://twitter.com/G
roqInc/status/1800589921876312090)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800635116592480543](https
://twitter.com/GroqInc/status/1800635116592480543)

[15. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800913489
399099728](https://twitter.com/GroqInc/status/1800913489399099728)

[16. a16z @a16z https://twitter.com/a16z/status/1800
617449382969440](https://twitter.com/a16z/status/1800617449382969440)

[17. a16z @a16z https://twitter.com/a16z/status/1
800623154257367123](https://twitter.com/a16z/status/1800623154257367123)

[18. Google AI @googleai https://twitter.com/g
oogleai/status/1800657713418109269](https://twitter.com/googleai/status/1800657713418109269)

[19. Yann LeCun @ylecun ht
tps://twitter.com/ylecun/status/1800677672512806971](https://twitter.com/ylecun/status/1800677672512806971)

[20. OpenAI
 @openai https://twitter.com/openai/status/1800778542512550260](https://twitter.com/openai/status/1800778542512550260)


[21. Midjourney @midjourney https://twitter.com/midjourney/status/1800693675686834450](https://twitter.com/midjourney/st
atus/1800693675686834450)

[22. Midjourney @midjourney https://twitter.com/midjourney/status/1800707282726174954](https:
//twitter.com/midjourney/status/1800707282726174954)

[23. Midjourney @midjourney https://twitter.com/midjourney/status/
1800819091302965729](https://twitter.com/midjourney/status/1800819091302965729)

[24. Midjourney @midjourney https://twi
tter.com/midjourney/status/1800819304402976971](https://twitter.com/midjourney/status/1800819304402976971)

[25. Midjour
ney @midjourney https://twitter.com/midjourney/status/1800819590005752126](https://twitter.com/midjourney/status/1800819
590005752126)

[26. Stability AI @stabilityai https://twitter.com/stabilityai/status/1800875914299048404](https://twitte
r.com/stabilityai/status/1800875914299048404)

[27. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/180090716508
4848531](https://twitter.com/NVIDIAAI/status/1800907165084848531)
```
---

     
 
all -  [ Streaming with agents ](https://www.reddit.com/r/LangChain/comments/1dfsv2t/streaming_with_agents/) , 2024-06-16-0958
```
I have implementing streaming with a chain based runnable which gives token by token output ( word by word), making UI s
imilar to how ChatGPT has its UI. But while implementing the same with an Agent based runnable I see that it gives 3 out
puts  in order, actions, steps and, output which contains answer. All three come as a whole, one after the other, not wo
rd by word.

I want to get word by word streaming for the agent's final answer.
```
---

     
 
all -  [ Newbie Seeking Advice on Side Project - Chat with Calendar  ](https://www.reddit.com/r/LangChain/comments/1dfsjwl/newbie_seeking_advice_on_side_project_chat_with/) , 2024-06-16-0958
```
As the title reads, I'm building a side project to chat with my google calendar + assignments from Canvas (learning mana
gement system). I'm using GCP to practice working with the cloud. 

As of April 2024, Cloud SQL for MySQL now supports v
ector embeddings. Essentially, I have all of my coursework and assignments in an events table. At first I embedded at th
e row level but this lost the understanding of columns. Now, I have a new column that is JSON representation of all the 
relevant columns for my eventual retrieval (event\_title, start\_time, end\_time, tag (Assignment, Discussion, Quiz, Stu
dy Times, Personal Events)). In a new column, I've successfully embedded all of these JSON's. What I've described above 
is pretty much the extent of what I've done. 

My end goal is to develop a streamlit UI to query this vector column in m
y SQL database. I have a few different paths I can go down, but I'm intentionally keeping this at a high level to hear d
iverse responses. 

  
Any advice? All thoughts are greatly appreciated. 

  
Cheers
```
---

     
 
all -  [ Improved Text2SQL Dataset Now Available on Huggingface! ](https://www.reddit.com/r/LangChain/comments/1dfsdbw/improved_text2sql_dataset_now_available_on/) , 2024-06-16-0958
```
I'm excited to share an updated open-source resource we’ve been working on—an improved version of the Spider dataset ori
ginally published by Yale University for Text2SQL tasks. You can check it out here: [https://huggingface.co/datasets/Raf
faSch121/fixed\_spider](https://huggingface.co/datasets/RaffaSch121/fixed_spider)

During our own model training at [Tur
bular](http://www.turbular.com) we identified several issues in the original dataset. To help the community and give bac
k, we decided to address these problems and release a corrected version. We hope this enhanced dataset will benefit ever
yone working on Text2SQL and similar projects.

Feel free to download, experiment, and contribute back if you find ways 
to make it even better!
```
---

     
 
all -  [ A tutorial on creating video from text using AI ](https://www.reddit.com/r/LangChain/comments/1dfsc15/a_tutorial_on_creating_video_from_text_using_ai/) , 2024-06-16-0958
```
I have written an article on how to create a Text to Video AI generator which generates video from a topic by collecting
 relevant stock videos and stitching them together. 

The code is completely open-source and uses free to use tools to g
enerate videos

Link to article :- [https://medium.com/@anilmatcha/text-to-video-ai-how-to-create-videos-for-free-a-comp
lete-guide-a25c91de50b8](https://medium.com/@anilmatcha/text-to-video-ai-how-to-create-videos-for-free-a-complete-guide-
a25c91de50b8)
```
---

     
 
all -  [ Token count and cost for chain.astream_events(). ](https://www.reddit.com/r/LangChain/comments/1dfpjpr/token_count_and_cost_for_chainastream_events/) , 2024-06-16-0958
```
 Hey all, How do I get the token count for chain.astream_events()
```
---

     
 
all -  [ RAGchain searching for similar prompts ](https://www.reddit.com/r/LangChain/comments/1dfp7xf/ragchain_searching_for_similar_prompts/) , 2024-06-16-0958
```
Hi i am new to the framework of langchain and i want to search for some information in contract documents regarding tota
l m2 area for a partner. The problem is that the main partner contract can have several newer appendices where the old t
otal m2 area in the old original contract is now replaced. Now i only want to extract the new total m2 area. Is there a 
clever way to sort or filter this?
```
---

     
 
all -  [ [Project] Compare Top 10 LMSYS Models with a Universal LLM API Library ](https://www.reddit.com/r/LangChain/comments/1dfp2z5/project_compare_top_10_lmsys_models_with_a/) , 2024-06-16-0958
```
Hello Langchain community!

I'm excited to share a project we've been working on - an open-source 'AI Gateway' library t
hat allows you to access and compare 200+ language models from multiple providers using a simple, unified API.

To showc
ase the capabilities of this library, I've created a Google Colab notebook that demonstrates how you can easily compare 
the top 10 models from the LMSYS leaderboard with just a few lines of code.

Here's a snippet:

https://preview.redd.it/
lcqhryzx0j6d1.png?width=1822&format=png&auto=webp&s=cf7d055fa0e79117fed5dd8f8dc37498fe43b9e3

The library handles all th
e complexities of authenticating and communicating with different provider APIs behind the scenes, allowing you to focus
 on experimenting with and comparing the models themselves.

Some key features of the AI Gateway library:

* Unified API
 for accessing 200+ LLMs from OpenAI, Anthropic, Google, Ollama, Cohere, Together AI, and more
* Compatible with existin
g OpenAI client libraries for easy integration
* Routing capabilities like fallbacks, load balancing, retries

I believe
 this library could be incredibly useful for researchers and developers in the Langchain community who want to easily co
mpare and benchmark different LLMs, or build applications that leverage multiple models.

I've put the demo notebook lin
k below, I'd love to get your feedback, suggestions, and contributions:

[https://github.com/Portkey-AI/gateway/blob/mai
n/cookbook/use-cases/LMSYS%20Series/comparing-top10-LMSYS-models-with-Portkey.ipynb](https://github.com/Portkey-AI/gatew
ay/blob/main/cookbook/use-cases/LMSYS%20Series/comparing-top10-LMSYS-models-with-Portkey.ipynb)
```
---

     
 
all -  [ Please guide towards solving this problem ](https://www.reddit.com/r/generativeAI/comments/1dflxqo/please_guide_towards_solving_this_problem/) , 2024-06-16-0958
```
How to get started with the problem statement?

Hey guys, i am new to generative AI, it’s been a few days learning new t
hings. I have a problem statement in hand. We have to evaluate a startup idea. We already have an evaluation checklist t
hat has like 30 parameters on the basic of which we decide the feasibility of the idea. We have to build a model in whic
h we prompt an idea and the input idea goes through various agents who are (business analysts, cofounder, VC). So it fir
st goes to BA and then the result goes to cofounder and so on therefore getting perspective of all the agents. For start
ers i want to build the model with 3 agents. Once it passes through 3rd agent it gives the final result as an evaluation
 checklist (the same one i talked about above). 

Now my question is how should i approach this problem and what would b
e the underlying concept used for building such a model? 
Also from where can i start ? 
FYI - i read a bit about genert
ive ai topics like embedding, fine tuning and a bit of langchain (built a simple agent) etc. Still exploring agentic AI.
 

Thanks in advance !! 
```
---

     
 
all -  [ How would you schedule an agent for a task? ](https://www.reddit.com/r/AI_Agents/comments/1dfjh5q/how_would_you_schedule_an_agent_for_a_task/) , 2024-06-16-0958
```
I'd like to have my agent prepare my mornings with news and some interesting investment ideas. The agent exists already 
as ReAct on Langchain and works quite well, but I have to start him up and ask him to do his work. How would you schedul
e this?
```
---

     
 
all -  [ Run Evaluations with Langtrace ](https://www.reddit.com/r/LangChain/comments/1dfaquj/run_evaluations_with_langtrace/) , 2024-06-16-0958
```
Hi all,

Its been a while from me, but just wanted to share that we have added support for running automated evals with 
Langtrace. As a reminder, Langtrace is an open source LLM application observability and evaluations tool. It is open tel
emetry compatible so no vendor lock-in. You can also self-host and run Langtrace.

We integrated langtrace with inspect 
AI (https://github.com/UKGovernmentBEIS/inspect\_ai). Inspect is an open source evluations tool from the developers of R
Studio - you should definitely check it out. I love it.  
With langtrace, you can now

* set up tracing in 2 lines of co
de
* annotate and curate datasets
* run evaluations against this dataset using Inspect
* view results, compare the outpu
ts against models and understand the performance of your app

So, you can now establish this feedback loop with langtrac
e.

https://preview.redd.it/qrwn7r1kte6d1.png?width=2304&format=png&auto=webp&s=3c2d7c82abbb329518b35c133c0e7a0e73a6d53d


Shown below are some screenshots:

https://preview.redd.it/t45vq2xute6d1.png?width=3156&format=png&auto=webp&s=1c15fc7
1499ba5c5ccbf0aa566fc78c82730e209

https://preview.redd.it/0gwmyz0xte6d1.png?width=3150&format=png&auto=webp&s=2713ba619
e903d2db227d5922e8e9c7a562fb9b7

Would love get any feedback. Please do try it out and let me know.

Link: [https://gith
ub.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace)
```
---

     
 
all -  [ Why should i use lang chain? ](https://www.reddit.com/r/LangChain/comments/1df95xz/why_should_i_use_lang_chain/) , 2024-06-16-0958
```
Hello everyone,
I mean no disrespect to anyone but I am having trouble seeing the appeal of using the lang chain.
 In my
 opinion I'am at best a beginner there for my view coulde be too shalow.
 I am hoping to find an anweser to where my bli
nd spots  are and what use cases the lang chain is useful for.
For example, if I want to build a rag chatbot. I would us
e Ollama with Chromadb without any libery except for chromadb and requests.
I have to admit that it is nice to try diffe
rent things with lang chain. It is also easier to handle complex files like PDF. 

If some of you say I don't have enoug
h experience, that's why I don't get it, the answer is fair enough for me to take a agaib a look at Lang Chain.

But I h
ave already tried to work with the framework 3 times and it always seems too complex for what I want to achieve.
All tho
se time i build an Chatbot that allows to interact with an modell with some litte custmasation over envs. And the last t
ime was a Rag Chatbot that allows me to index Websites to get answers about their content.
```
---

     
 
all -  [ Data and AI Summit - Day 2 Announcements! ](https://www.reddit.com/r/databricks/comments/1df92yc/data_and_ai_summit_day_2_announcements/) , 2024-06-16-0958
```
🚀 Day 2 got off to an incredible start, some amazing announcements:

* Unity Catalog has officially been open-sourced, L
IVE on stage by the Databricks CTO, Matei Zaharia -> [HERE](https://www.databricks.com/blog/open-sourcing-unity-catalog)

* Introducing Databricks LakeFlow, a new solution that makes building production-grade data pipelines easy and efficien
t -> [HERE](https://www.databricks.com/blog/introducing-databricks-lakeflow)
* New Delta Sharing Features, Expansion of 
Partner Sharing Ecosystem, More Marketplace Data Providers and Growth, and Introducing Databricks Clean Rooms in Public 
Preview on AWS and Azure -> [HERE](https://www.databricks.com/blog/whats-new-data-sharing-and-collaboration)
* Unity Cat
alog new features: Governed business metrics, Attribute-based access controls, Lakehouse Federation GA, and more -> [HER
E](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2024)

We are looking forward to al
l of the amazing technical deep dive sessions at Summit!

https://preview.redd.it/t4rjcvm9he6d1.jpg?width=1200&format=pj
pg&auto=webp&s=6e43e9f6cbcf5a1bbb4f04543b2e63e955c38a5f


```
---

     
 
all -  [ suggest 5 follow-up question based on previous asked  ](https://www.reddit.com/r/LangChain/comments/1df5lc7/suggest_5_followup_question_based_on_previous/) , 2024-06-16-0958
```
Hello guys

i am creating chat bot with QA retrieval using vector DB and i want to add one more feature that is follow u
p question along with response to current question  
can anybody provide me example how implement it ?
```
---

     
 
all -  [ RAG performs differently in different environments  ](https://www.reddit.com/r/LangChain/comments/1df1wnb/rag_performs_differently_in_different_environments/) , 2024-06-16-0958
```
To set the context we have 4 environments predev, dev, testing and production. Our RAG uses langchain for PDF extraction
, qdrant(self hosted on kubernetes) for vectorstore and gpt-3.5-turbo-16k for the llm.

We have built a RAG, which worke
d well(gave correct answers from PDF) on predev. When we moved it to dev, in the initial days its performance(correctnes
s) was bad and eventually got good without any changes, except for minor document update. Then it moved to testing envir
onment where again the same behaviour. Now it's in prod and again behaves the same. Facing a lot of backlash from client
 due to this strange behaviour.

It's the same document, same gpt,  but different qdrant hosted different for different 
environments.

Did anyone experience similar issue? Can anyone explain why the warmup time.

Any help is greatly appreci
ated.
```
---

     
 
all -  [ Reference Platform Architecture ](https://www.reddit.com/r/platformengineering/comments/1df0j3u/reference_platform_architecture/) , 2024-06-16-0958
```
We are a startup studio, and naturally, we wanted to build repeatable processes to jumpstart new products. Our reference
 platform architecture is a battle hardened best practices and technology components which work together like a charm fo
r a majority of real world use cases. We have a lot of boilerplate which helps you start a new platform within days.  
 
 
We are now putting our platform architecture out there for everyone to see. I’d love to hear comments and suggestions.
 Details can be seen here: [https://venturenox.com/work/vrpa/](https://venturenox.com/work/vrpa/)

https://preview.redd.
it/2d619reioc6d1.png?width=1900&format=png&auto=webp&s=8b1db43302bde957141e666af964847f9c1859f1
```
---

     
 
all -  [ RAG Model TOO SLOW ](https://www.reddit.com/r/LangChain/comments/1df0apu/rag_model_too_slow/) , 2024-06-16-0958
```
I am trying to build a model to take in 5-10 PDFs and answer questions based on them.

This is my flow ==> LlamaParse->O
penAI ada embeddings -> FAISS vector store -> multi query retriever -> cohere reranker -> OpenAI gpt4o -> results

I als
o have a part in my retriever stage where I get citations and chunking is done page wise

The questions I ask take anywh
ere between 25-50 seconds to get an answer and also I am missing out on information, I have made the retriever send back
 all relevant pages, not just the top 3 relevant pages

Is there anyway to get this under 20 seconds and extract all rel
evant chunks with keeping in mind I need citations?


```
---

     
 
all -  [ Seeking Recommendations: Tools for Chemists Using Large Language Models and Agents ](https://www.reddit.com/r/LangChain/comments/1dewg6w/seeking_recommendations_tools_for_chemists_using/) , 2024-06-16-0958
```
I'm looking for recommendations on tools for chemists that can be implemented using LLM and LangChain agents. What usefu
l tools or applications do you think can be created with these technologies? I would appreciate any ideas and suggestion
s.

  
Which LLMs do you recommend for laboratory automation solutions, and what data processing life cycles can be impl
emented by agents?

I'm particularly interested in how to work with the Canonical SMILES format using chatbots and modif
y it through agents.

I'm exploring this topic as a theoretical preparation for a long-term hackathon focused on the aut
omation of chemical laboratories. All solutions will be **published** and **open source** after our team’s presentation.

```
---

     
 
all -  [ Review my resume, not getting any calls ](https://www.reddit.com/r/resumes/comments/1dehi9a/review_my_resume_not_getting_any_calls/) , 2024-06-16-0958
```
https://preview.redd.it/kbr9xd1hg76d1.jpg?width=1080&format=pjpg&auto=webp&s=e32bbba25f324d01f797f323f50ca4e7479dc3b8

H
i, Please review my resume. I am not getting any calls. I have been applying for jobs since March 
```
---

     
 
all -  [ Need Help to make langchain chatbot ](https://www.reddit.com/r/LangChain/comments/1deh52g/need_help_to_make_langchain_chatbot/) , 2024-06-16-0958
```
I have to make llm chatbit using open ai on flask. 
Help me to make this. 
```
---

     
 
all -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-16-0958
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

     
 
all -  [ Build a QA Bot for your documentation with Langchain ](https://www.reddit.com/r/developersIndia/comments/1dedwwg/build_a_qa_bot_for_your_documentation_with/) , 2024-06-16-0958
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

     
 
all -  [ AI / LLMs in your Obsidian - what's actually been useful for you? ](https://www.reddit.com/r/ObsidianMD/comments/1dedmeu/ai_llms_in_your_obsidian_whats_actually_been/) , 2024-06-16-0958
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-16-0958
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-16-0958
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
