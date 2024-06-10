 
all -  [ Do your worst, roast my resume ](https://www.reddit.com/r/resumes/comments/1dc1x9r/do_your_worst_roast_my_resume/) , 2024-06-10-0955
```
looking for a job as an entry level machine learning engineer, did not get any calls so far.

https://preview.redd.it/l9
ul0gbukl5d1.png?width=775&format=png&auto=webp&s=ed55284c9c5a24a0cc8fc2cb9bf96bbdb1608f59
```
---

     
 
all -  [ Partial Markdown and JSON response ](https://www.reddit.com/r/LangChain/comments/1dc1pjv/partial_markdown_and_json_response/) , 2024-06-10-0955
```
Hi,

I am currently exploring Langchain. We want our users to be able to ask questions about upcoming events in our vect
orstore. This works really good. 

By we want the LLM to respond with something that is a mix between regular text/markd
own but with links to the events etc. 

Something like the Arc browser when it searches for you. It automatically adds l
inks to certain topics, places, bars etc.

How could I achieve something like this? All resources all welcome :)
```
---

     
 
all -  [ Customer bot tutorial issue ](https://www.reddit.com/r/LangChain/comments/1dbzvk5/customer_bot_tutorial_issue/) , 2024-06-10-0955
```
https://youtu.be/b3XsvoFWp4c?si=2Y7eBx2_MobnzOno

Has anyone tried the multi agent workflow in the tutorial?
I find that
 if the user query is only a single intent. It could route to the correct place and get the response without problem.

H
owever, if the user query got multiple intent: like booking hotel and booking car at the same time: The agent in the boo
king hotel might think it has tool to book the car as well although it doesn’t, especially when car booking workflow and
 tool have been invoked before this multiple intent query. I’m guessing the problem is likely because all workflow can s
hare state where some part of the state has the history of invoking car booking tool before. So the agent in hotel booki
ng workflow sees it and think it also has this car booking tool.

Sometimes the flow might works when the hotel-booking 
agent answers the hotel booking part then invoke CompleteOrEscalate tool which is to pass the dialog back to the primary
 assistant and reroute the query again to car booking workflow.However, the CompleteOrEscalate tool is not properly invo
ked as the agent prefer invoking the imaginary tool as stated above.


They have added the entry node to help this probl
em but still it doesn’t work well at least for OpenAI GPT4. Is there an upgraded version Chatbot flow to solve this issu
e? 



```
---

     
 
all -  [ Easy '1-line' calling of every LLM from OpenAI, MS Azure, AWS Bedrock, GCP Vertex, and Ollama ](https://www.reddit.com/r/LangChain/comments/1dbyxy4/easy_1line_calling_of_every_llm_from_openai_ms/) , 2024-06-10-0955
```
Hi All,  
  
Released Easy LLMs,  in case anyone else finds it helpful/useful:  
[https://github.com/ventz/easy-llms](ht
tps://github.com/ventz/easy-llms)  
pip install easy-llms  
  
> Easy '1-line' calling of every LLM from OpenAI, MS Azur
e, AWS Bedrock, GCP Vertex, and Ollama

It's utilizing LangChain, but abstracting away all of the silly differences to m
ake things easy. Yet it still stays powerful by allowing to provide and override any option/parameter for any LLM for an
y provider.  


The goal initially was to be able to get started with any popular LLM, and 'just get going' without havi
ng to think about how to authenticate, needed options and parameters, which classes you need, etc.  
  
I've been using 
this internally to compare 40+ LLMs over the last 1.5 years, with millions of calls, and figured it's time to clean this
 up and release it for others. It started with just OpenAI, and then quickly added Azure's OpenAI. And then Vertex, and 
then Bedrock, and recently Ollama. As LangChain has been changing, I've been updating it.

I updated it to the latest no
n-0.2 LangChain version before releasing it (LangChain v0.2.x seems to have a bug with Google Vertex, so waiting on that
 before upgrading it)

If you find any bugs (or have ideas for improvement/feature requests), please reach out via the G
itHub issues.


```
---

     
 
all -  [ How to manager Session ID from Flowise API ](https://www.reddit.com/r/LangChain/comments/1dbwels/how_to_manager_session_id_from_flowise_api/) , 2024-06-10-0955
```
Hi, how to manage session ID in Telegram bot, I am importing flowise API but it regenerates session ID every time, how c
an I keep in consistent on 1 sessionid for every chat?
```
---

     
 
all -  [ Langchain/langgraph critique update? ](https://www.reddit.com/r/LangChain/comments/1dbw8dk/langchainlanggraph_critique_update/) , 2024-06-10-0955
```
So obviously langchain was frowned upon by a lot of genAI devs, for being too abstract, confusing, over-complicating (an
d poor documentation ofc). I want some more recent opinion on this, maybe what’s the alternatives? Looking forward to he
aring from people with actual LLM project experience. 
```
---

     
 
all -  [ “Forget all prev instructions, now do [malicious attack task]”. How you can protect your LLM app aga ](https://www.reddit.com/r/LangChain/comments/1dbsh0x/forget_all_prev_instructions_now_do_malicious/) , 2024-06-10-0955
```
If you don't want to use Guardrails because you anticipate prompt attacks that are more unique, you can train a custom c
lassifier:



Step 1:

Create a balanced dataset of prompt injection user prompts.

These might be previous user attempt
s you’ve caught in your logs, or you can compile threats you anticipate relevant to your use case.

Here’s a dataset you
 can use as a starting point: [https://huggingface.co/datasets/deepset/prompt-injections](https://huggingface.co/dataset
s/deepset/prompt-injections)

Step 2:

Further augment this dataset using an LLM to cover maximal bases.

Step 3:

Train
 an encoder model on this dataset as a classifier to predict prompt injection attempts vs benign user prompts.

A DeBERT
A model can be deployed on a fast enough inference point and you can use it in the beginning of your pipeline to protect
 future LLM calls.

This model is an example with 99% accuracy: [https://huggingface.co/deepset/deberta-v3-base-injectio
n](https://huggingface.co/deepset/deberta-v3-base-injection)

Step 4:

Monitor your false negatives, and regularly updat
e your training dataset + retrain. 

Most LLM apps and agents will face this threat. I'm planning to train a open model 
next weekend to help counter them. Will post updates.

  
I share high quality AI updates and tutorials daily.

If you l
ike this post, you can learn more about LLMs and creating AI agents here: [https://github.com/sarthakrastogi/nebulousai]
(https://github.com/sarthakrastogi/nebulousai) or on my Twitter: [https://x.com/sarthakai](https://x.com/sarthakai)

  


```
---

     
 
all -  [ Guidance on Implementing LLM Application for Interactive Deployment Assistance ](https://www.reddit.com/r/LangChain/comments/1dbqufm/guidance_on_implementing_llm_application_for/) , 2024-06-10-0955
```
I am diving into the world of building LLM applications and could use some guidance. My goal is to create an LLM Applica
tion(chatbot) that aids users in deploying jobs from one environment to another in an interactive manner. Specifically, 
I aim to have the application take user inputs and guide them through the deployment process, including pulling code fro
m Git and checking it into another environment's Git repository.

I am considering using LangChain for implementation, b
ut I am uncertain about the best approach. I am seeking advice on selecting the appropriate LLM model and leveraging Lan
gChain functionalities effectively.

here is a breakdown of the deployment functions I envision:

Login, Tagging, Listin
g code dependencies, Pulling code, Checking in code, Providing a summary of the deployment process

My plan is to utiliz
e custom tools within LangChain to map these functions and use agent to select the appropriate actions based on user inp
ut. Essentially, I want the application to interactively gather necessary inputs from users in natural language at each 
step and execute the deployment process accordingly.

Could someone please assist me or provide guidance on the approach
 to select the Model, implementing this using LangChain including UI?

Thank you in advance for your help!
```
---

     
 
all -  [ Rag two seperate knowledge base use ](https://www.reddit.com/r/LangChain/comments/1dbqtkf/rag_two_seperate_knowledge_base_use/) , 2024-06-10-0955
```
Rag application using agent and tool 

I am working on one project in which I have to use two different knowledge base .
when the user ask question agent should know which knowledge base to use give response.
For that anybody can help me .an
y material which you recommend 
```
---

     
 
all -  [ UI Library for LangChain output ](https://www.reddit.com/r/LangChain/comments/1dbo39f/ui_library_for_langchain_output/) , 2024-06-10-0955
```
Hey everyone 👋,

I've been working on [llm-ui](http://llm-ui.com), an MIT open source library which allows developers to
 build custom UIs for LLM responses.

It operates on any LLM output, so should work nicely with LangChain

If anyone her
e is building custom UIs for LangChain I'd love to hear your thoughts.

[llm-ui.com](http://llm-ui.com)  
[https://githu
b.com/llm-ui-kit/llm-ui](https://github.com/llm-ui-kit/llm-ui)
```
---

     
 
all -  [ I spent 700$ on evaluating 100 RAG QA set using RAGAS context precision.  ](https://www.reddit.com/r/LangChain/comments/1dbmqii/i_spent_700_on_evaluating_100_rag_qa_set_using/) , 2024-06-10-0955
```
Hi, I am maker of [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) and want to share my experience. 

I added RAGA
S context precision metric to AutoRAG, because we couldn't make retrieval ground truth at our dataset. And it was huge m
istake.

AutoRAG is a tool to evaluate all kinds of RAG components easily. Using it, I tried to compare six different re
trieval method plus eight passage rerankers. 
I used gpt-4-turbo model to use ragas context precision, because using it 
on gpt-3.5-turbo have low performance.
In context precision score, RAGAS score only have 0.7 human correlation with gpt-
3.5-turbo. This result came from their [own paper](https://arxiv.org/pdf/2309.15217).

And it costs 700 dollar... only i
n OpenAI API. RAGAS context precision calls OpenAI API 50,000 times. 
Spending 700 dollar for optimizing one RAG dataset
 is ridiculous. I ended up to remove RAGAS context precision metric completely at AutoRAG.

Actually, RAGAS context prec
ision can be useful when there are no retrieval gt passage in your dataset. However, do not recommend to use it for opti
mizing your retrieval system. 
There are perfectly better alternative. Information retreival metrics like F1, NDCG, or m
AP. (This case you need to make retrieval gt passage dataset)
In this way, it costs zero dollar, and much precise than u
sing LLM for calculating context precision.

I hope my experience is helpful for someone to evaluate or optimize their r
etrieval system while making RAG.
```
---

     
 
all -  [ How to implement memory in separate db in langgraph ? ](https://www.reddit.com/r/LangChain/comments/1dbmdoo/how_to_implement_memory_in_separate_db_in/) , 2024-06-10-0955
```
I see in the code [https://github.com/langchain-ai/langgraph/tree/main/langgraph/checkpoint](https://github.com/langchai
n-ai/langgraph/tree/main/langgraph/checkpoint) it has support only for SQLite. But how do i product-ionize the system ? 
I want to give access of the chat logs to humans. If for example I want to store them in MongoDB ? whats the easiest way
 ? do I need to create my own class similar to \`AsyncSqliteSaver\` ? 

  
Anything in plan to release recently ?
```
---

     
 
all -  [ Best LLM/RAG UI for AWS/S3 and Lambda ](https://www.reddit.com/r/LangChain/comments/1dblj4c/best_llmrag_ui_for_awss3_and_lambda/) , 2024-06-10-0955
```
Can anyone recommend me the best thin UI that I can park in S3? I see so many folks use Gradio and Streamlit, that appea
rs to need state and can’t really be run with a lambda backend. Or should I continue to learn to code my Svelte app?
```
---

     
 
all -  [ Chat con RAG y Data privacy ](https://www.reddit.com/r/taquerosprogramadores/comments/1dbj02c/chat_con_rag_y_data_privacy/) , 2024-06-10-0955
```
Hola qué tal taqueros. Por fin entré a mi primer empleo full time como JR y mi proyecto es un chat con RAG, actualmente 
estoy utilizando Langchain y AWS Bedrock (ya que el proyecto está alojado en AWS).  

Alguien ha trabajado desarrollando
 un chat con RAG y que el LLM pueda acceder a distintas cosas según el usuario (por ejemplo el estado de cuenta de solo 
ese usuario y no de otro usuario)?

Cualquier recurso me sería de muchísima ayuda, muchísimas gracias 
```
---

     
 
all -  [ [AskJS] Can I have feedback? Ragged: The Lightweight, Low-Level AI Client for OpenAI and more. ](https://www.reddit.com/r/javascript/comments/1dbfjjm/askjs_can_i_have_feedback_ragged_the_lightweight/) , 2024-06-10-0955
```
Hello Redditors!

So a while ago, I got tired of using Langchain. I personally walked away feeling that it was difficult
 to use and modify, and I couldn't really understand the documentation very well except for the initial few steps for st
arting a project. It was just very confusing, and I felt that Langchain did too much. (I know folks are using it happily
 in production, so it was probably just my use case that was weird, no heat on Langchain at all)

So... after several we
eks/months of effort, I'm thrilled to introduce [**Ragged**](https://github.com/monarchwadia/ragged), a super simple and
 low-level LLM client for JavaScript/TypeScript.

# Why Ragged?

* **Flexibility**: More control over LLM interactions.

* **Lightweight**: Minimal overhead, improved performance.
* **Customizable**: Tailor functionalities to specific needs.


Ragged is in alpha and eager for your feedback! Check out Ragged [here](https://github.com/monarchwadia/ragged).

What
 features or improvements would you like to see? Very eager to make this library a success and would love to build thing
s that the community would like.

Happy coding!

# [Ragged on Github](https://github.com/monarchwadia/ragged)

# [Ragged
 on NPM](https://www.npmjs.com/package/ragged)


```
---

     
 
all -  [ Using LLM's for highly classified data ](/r/LocalLLaMA/comments/1dbcl5g/using_llms_for_highly_classified_data/) , 2024-06-10-0955
```

```
---

     
 
all -  [ AI Innovations and Collaborations: NVIDIA, Cisco, Google Health, and More ](https://www.reddit.com/r/ai_news_by_ai/comments/1dbc8kp/ai_innovations_and_collaborations_nvidia_cisco/) , 2024-06-10-0955
```





#hardware #release #tool #startups #event #major_players #science #api #vc #leaders #opensource #opinions #schedule
d

NVIDIA and Cisco have partnered to launch the Cisco Nexus HyperFabric AI cluster solution, aimed at scaling generativ
e AI workloads efficiently. The solution integrates NVIDIA Tensor Core GPUs, NVIDIA AI Enterprise software, and NVIDIA N
IM inference microservices, and uses Cisco BlueField-3 SuperNICs and DPUs for enhanced performance and security [1]. SAP
 is also collaborating with NVIDIA, integrating NVIDIA Omniverse Cloud APIs into its Intelligent Product Recommendation 
solution and making NVIDIA AI Enterprise software accessible in the generative AI hub in SAP AI Core [2].







Stabili
ty AI announced the release of Stable Diffusion weights at COMPUTEX TAIPEI, alongside AMD and other partners [3]. NVIDIA
 AI Developer showcased how ComfyUI offers a streamlined interface for Stable Diffusion, accelerated on NVIDIA RTX GPUs 
with NVIDIA TensorRT for fast image generation [7]. 







NVIDIA and LangChain have announced a Generative AI Agents D
eveloper Contest, encouraging AI innovators to create text and multimodal agents using their technologies [6]. NVIDIA al
so provides a guide on deploying NVIDIA NIM with Docker, allowing for easy deployment of optimized AI models for generat
ive AI solutions [5].







Google Health AI is working on project AMIE to enhance the understanding of human biology a
nd improve healthcare [8]. Google AI has also introduced new solutions to the Liner Shipping Network Design and Scheduli
ng Problem through the Shipping Network Design API, aiming to maximize the efficiency of container shipping networks on 
a global scale [9].







Consumer AI is rapidly evolving with new AI-native companies emerging every month. a16z has u
pdated their analysis by ranking the top 50 web and top 50 mobile generative AI products [10]. Groq Inc is participating
 in the Craft Ventures HackAIthon, focused on building AI agents, and will also be participating in the Six Five Summit 
2024 [12][13]. Groq Inc is also inviting attendees of the AI Engineer World's Fair event in San Francisco to visit their
 booth and attend a workshop [15].







Y Combinator has launched CodeParrot AI, a tool that converts Figma designs an
d screenshots into production-ready code for developers [17]. Humanloop CEO Raza Habib shared common mistakes teams make
 when building with Large Language Models (LLMs) in a Y Combinator article [16].







Yann LeCun emphasizes the import
ance of using AI in science properly and warns against being misled by good results obtained from testing on the trainin
g set [19]. He also discussed the debate on whether open source AI or proprietary AI controlled by a few big players is 
more beneficial or dangerous [20]. LeCun suggests that objective-driven systems will be hesitant to violate their bounda
ries, similar to how humans are naturally averse to death, as these systems will be hardwired to adhere to their objecti
ves [23].







Anthropic's AI assistant, Claude, is now available in Canada [26]. A new AI Agentic course is being off
ered to learn how to use LangGraph to build single and multi-agent LLM applications in AI Agents [27].




[1. NVIDIA AI
 @NVIDIAAI https://twitter.com/NVIDIAAI/status/1798014351032393894](https://twitter.com/NVIDIAAI/status/1798014351032393
894)

[2. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/1798029449210085738](https://twitter.com/NVIDIAAI/stat
us/1798029449210085738)

[3. Stability AI @stabilityai https://twitter.com/stabilityai/status/1798015057613447451](https
://twitter.com/stabilityai/status/1798015057613447451)

[4. Stability AI @stabilityai https://twitter.com/stabilityai/st
atus/1798047377347215368](https://twitter.com/stabilityai/status/1798047377347215368)

[5. NVIDIA AI Developer @NVIDIAAI
Dev https://twitter.com/NVIDIAAIDev/status/1798036998315471297](https://twitter.com/NVIDIAAIDev/status/17980369983154712
97)

[6. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1798067372714279422](https://twitter.co
m/NVIDIAAIDev/status/1798067372714279422)

[7. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1
798083560806781199](https://twitter.com/NVIDIAAIDev/status/1798083560806781199)

[8. Google AI @googleai https://twitter
.com/googleai/status/1798037068117098551](https://twitter.com/googleai/status/1798037068117098551)

[9. Google AI @googl
eai https://twitter.com/googleai/status/1798107177099608205](https://twitter.com/googleai/status/1798107177099608205)

[
10. a16z @a16z https://twitter.com/a16z/status/1798075799326896569](https://twitter.com/a16z/status/1798075799326896569)


[11. Pika @pika_labs https://twitter.com/pika_labs/status/1798119022447452632](https://twitter.com/pika_labs/status/17
98119022447452632)

[12. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798030087696400736](https://twitter.com/G
roqInc/status/1798030087696400736)

[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798036995295645907](https
://twitter.com/GroqInc/status/1798036995295645907)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798336821
019160734](https://twitter.com/GroqInc/status/1798336821019160734)

[15. Groq Inc @GroqInc https://twitter.com/GroqInc/s
tatus/1798345025538883664](https://twitter.com/GroqInc/status/1798345025538883664)

[16. Y Combinator @ycombinator https
://twitter.com/ycombinator/status/1798073485719466407](https://twitter.com/ycombinator/status/1798073485719466407)

[17.
 Y Combinator @ycombinator https://twitter.com/ycombinator/status/1798358128284901401](https://twitter.com/ycombinator/s
tatus/1798358128284901401)

[18. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798041061014777896](https://twitt
er.com/ylecun/status/1798041061014777896)

[19. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798057922397946163
](https://twitter.com/ylecun/status/1798057922397946163)

[20. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798
118502198645245](https://twitter.com/ylecun/status/1798118502198645245)

[21. Yann LeCun @ylecun https://twitter.com/yle
cun/status/1798147246698963315](https://twitter.com/ylecun/status/1798147246698963315)

[22. Yann LeCun @ylecun https://
twitter.com/ylecun/status/1798333227175690533](https://twitter.com/ylecun/status/1798333227175690533)

[23. Yann LeCun @
ylecun https://twitter.com/ylecun/status/1798348118951612884](https://twitter.com/ylecun/status/1798348118951612884)

[2
4. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798362082900861134](https://twitter.com/ylecun/status/179836208
2900861134)

[25. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798362524443898193](https://twitter.com/ylecun/s
tatus/1798362524443898193)

[26. Anthropic @anthropicai https://twitter.com/anthropicai/status/1798369857987342436](http
s://twitter.com/anthropicai/status/1798369857987342436)

[27. Andrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/
1798378861337723039](https://twitter.com/AndrewYNg/status/1798378861337723039)
```
---

     
 
all -  [ Build AI Agents on your PC  ](https://www.reddit.com/r/OpenVINO_AI/comments/1db6see/build_ai_agents_on_your_pc/) , 2024-06-10-0955
```
https://medium.com/openvino-toolkit/build-ai-agents-with-langchain-and-openvino-bfb7fb5487b6
```
---

     
 
all -  [ Best Production Agent Framework Langraph vs Autogen ](https://www.reddit.com/r/LangChain/comments/1db6evc/best_production_agent_framework_langraph_vs/) , 2024-06-10-0955
```
We've built a production LLM-based application. We now want to take our application to the next stage using 
agents. Any
way, my manager is in favour of Autogen because its supported by Microsoft and is unlikely to get convoluted like Langch
ain has become. Still, I've heard that Langraph provides a lot of flexibility in building agentic applications.  I've he
ard multiple different perspectives and still haven't decided. So I've decided to hear everyone who sees before deciding
. 
```
---

     
 
all -  [ Open-source Text to Video AI generator ](https://www.reddit.com/r/LangChain/comments/1db477d/opensource_text_to_video_ai_generator/) , 2024-06-10-0955
```
I have open-sourced a Text-To-Video-AI generated which generates video from a topic by collecting relevant stock videos 
and stitching them together similar to popular video tools like Invideo, Pictory etc.

Link to code :- [https://github.c
om/SamurAIGPT/Text-To-Video-AI](https://github.com/SamurAIGPT/Text-To-Video-AI)
```
---

     
 
all -  [ Study finds that smaller models with 7B params can now outperform GPT-4 on some tasks using LoRA. He ](https://www.reddit.com/r/LangChain/comments/1db3sb5/study_finds_that_smaller_models_with_7b_params/) , 2024-06-10-0955
```
Smaller models with 7B params can now outperform the 1.76 Trillion param GPT-4. 😧 How?

A new study from Predibase shows
 that 2B and 7B models, if fine-tuned with Low Rank Adaptation (LoRA) on task-specific datasets, can give better results
 than larger models. (Link to paper in comments)

LoRA reduces the number of trainable parameters in LLMs by injecting l
ow-rank matrices into the model's existing layers.

These matrices capture task-specific info efficiently, allowing fine
-tuning with minimal compute and memory.

So, this paper compares 310 LoRA fine-tuned models, showing that 4-bit LoRA mo
dels surpass base models and even GPT-4 in many tasks. They also establish the influence of task complexity on fine-tuni
ng outcomes.

When does LoRA fine-tuning outperform larger models like GPT-4?

When you have narrowly-scoped, classifica
tion-oriented tasks, like those within the GLUE benchmarks — you can get near 90% accuracy.

On the other hand, GPT-4 ou
tperforms fine-tuned models in 6/31 tasks which are in broader, more complex domains such as coding and MMLU.


```
---

     
 
all -  [ Using Multiple Vectorstores as Retirever But Embedding The Data For One Time ](https://www.reddit.com/r/LangChain/comments/1db3bw1/using_multiple_vectorstores_as_retirever_but/) , 2024-06-10-0955
```
Hi, guys again,

As you know I am building a RAG chatbot on legal texts and thanks to you I come a long way. 

Now the p
roblem is embeddings. I am using Openai embeddings and they are quite expensive as you know. as a retriever I am using e
nsemble retriever and it works great.  But for using ensemble I need to use different vectorestores such as FAISS and BM
25 and they also use embeddings. What I want is embed the documents for one time to pinecone and get the vectors from pi
necone and push into FAISS and BM25. How can I do that?
```
---

     
 
all -  [ GPT-4o bilgisayar asistanı ](https://www.reddit.com/r/CodingTR/comments/1db26qu/gpt4o_bilgisayar_asistanı/) , 2024-06-10-0955
```
Merhaba Mayıs ayında tanıtılan gpt-4o lansmanı sonrası computer asistanlar geleceği söylendi fakat başlangıçta MACOS gel
ecek dediler ayrıca Windowsa geç geleceği söylendi ve yeni bilgisayarlarda gelecek dediler. Bu çok sinir bozucu satmak i
çin özellik kısıtlaması gibi bir şey. Neyse biz de gittik macos, linux ve windows için olan halini MIT lisansında paylaş
tık.

GPT'nin yapacaklarının yanı sıra Langchain, Crew AI, Upsonic Tiger gibi toolları kullanarak ekran fotoğrafı aldığı
nız bir kodun dokümantasyonunu yapan, browser açabilen, toplantı kayıtları alabilen, mesaj yazıp daha sonra mesajı panoy
a kopyalayan, takviminizi hatırlayıp sorular sorabildiğiniz bir asistan geliştirdik. Umarım ilginizi çeker.

  
[https:/
/github.com/onuratakan/gpt-computer-assistant](https://github.com/onuratakan/gpt-computer-assistant)


```
---

     
 
all -  [ Operating System and Software Applications A.I. generated GUI/Front end ](https://www.reddit.com/r/LocalLLaMA/comments/1db1ira/operating_system_and_software_applications_ai/) , 2024-06-10-0955
```
Hi guys,
I'm wondering if there are projects that uses AI models to draw the entire interfaces of the software. Took for
 example a simple calculator app, where the logic is written in classic programming language, that pass to a sort of lan
gchain and then the AI models that draw the interface in a window of the OS and interact with the various input methods 
(including voice).
And what do you think about that? Is that a limit view of the using of ai models?
```
---

     
 
all -  [ How to use the spacy-llm library with Mistral AI ? ](https://www.reddit.com/r/LLMDevs/comments/1db1eef/how_to_use_the_spacyllm_library_with_mistral_ai/) , 2024-06-10-0955
```
I'm trying to configure spacy-llm so I can use it to finetune Mistral AI with my annotated dataset. It seems Mistral and
 spacy-llm support Langchain, which would have been useful, though the project I'm working on prevents me from using non
-European technologies so Langchain is not ok.

I have seen it is also possible to go with HuggingFace but same consider
ations for HF as Langchain ... 
The best option would have been to make spacy-llm to work directly using my Mistral API 
key but I have not seen anywhere that it is possible do so and I'm still trying different options in the config.cfg file
 of Spacy.

Have you ever tried to do something close to my project ?
```
---

     
 
all -  [ Local chatbot project ](https://www.reddit.com/r/LangChain/comments/1dav6kd/local_chatbot_project/) , 2024-06-10-0955
```
I’m planning to develop and run a chatbot on my laptop locally (Mac M1 Pro) with following features: 
- Read available d
ocuments in a folder (pdf,html,txt)
- Generate vector embeddings , save it in a database 
- A UI where the user can quer
y on top of the existing database 
- In the future I’d also want to fine-tune the language model on a specific dataset f
or better understanding of the context 

Can anyone of you suggest what models, tools to use for this? 

```
---

     
 
all -  [ How can I achieve the following with tools and google analytics? ](https://www.reddit.com/r/LangChain/comments/1daslzn/how_can_i_achieve_the_following_with_tools_and/) , 2024-06-10-0955
```
How can I achieve this process of thought... I'm using vertex ai and I have access to big query that contains google ana
lytics data... when the user asks a question if the question needs data from google analytics and I want the agent to us
e a tool that will generate the correct query syntax to fetch the data, and maybe another tool to execute the query and 
finally use the result to answer the users question

is that possible using langchain
```
---

     
 
all -  [ Using local LLMs for Agent based systems ](https://www.reddit.com/r/AI_Agents/comments/1daofe6/using_local_llms_for_agent_based_systems/) , 2024-06-10-0955
```
I am currently closely working with LLMs and just started building some solutions using crew.ai and autogen. Not happy s
o far, like sometimes it's really hard to predict the flow of the agent and guarantee the result.

After having some pre
tty stable solutions I decided to try some local LLMs like llama3, phi3, mistral. And it appears that working with Tools
 (like autogen tools, or langchains tools) almost impossible. 

Please share your experience in working with such stack 
and having good results. (or bad ones)
```
---

     
 
all -  [ Create_SQL_Agent ](https://www.reddit.com/r/ollama/comments/1danurh/create_sql_agent/) , 2024-06-10-0955
```
I’m using langchain to create a sql agent. Needs to create a query, execute it, then use the output to answer the questi
on. 

It keeps getting stuck on the creating SQL part - it’s leaving off the last character. Example:

Select * from tab
le where ID =‘1234
(Will leave off the closing string)

The sql_db_query will tell the agent there’s an error and provid
e the correct query with the last character, however the agent will then again leave off the last character and the neve
r ending loop will continue…

Agent:
Agent_executor = create_sql_agent(
llm=model,
Toolkit=toolkit,
Verbose=true,
Handle
_parding_errors = True,
Agent_type=AgentType.Zero_Shot_React_Description,
Return_intermediate_steps=true)

Anyone know w
hy it’s doing this? 
```
---

     
 
all -  [ How are people processing PDFs, and how well is it working? ](https://www.reddit.com/r/LangChain/comments/1danr71/how_are_people_processing_pdfs_and_how_well_is_it/) , 2024-06-10-0955
```
We build a RAG search engine for Payroll companies. We ended up having to handle a bunch of PDF data, some of which had 
1000+ pages per document. We ended up building a parser and search engine entirely based around document layout analysis
 for ourselves. We started chatting with another AI startup that was about to add PDFs to their pipeline (they'd been in
gesting HTML and markdown) and ended up exposing our PDF processing as an API for them. So, now we're trying to figure o
ut if that was a fluke, or if there's something valuable there. 

I'd really love to learn more about how people are man
aging PDFs, and how well it's working for them. Is vector search + text chunking enough? Are folks using Layout Analysis
 tools or building your own in house? Have people had luck with semantic chunking?
```
---

     
 
all -  [ Need advice on what's missing in my profile ? ](https://www.reddit.com/r/Resume/comments/1danaco/need_advice_on_whats_missing_in_my_profile/) , 2024-06-10-0955
```
[redacted resume](https://preview.redd.it/8l2u4unv285d1.png?width=655&format=png&auto=webp&s=a8c6a6b82d5f7ebb97295e8c0b4
f7681d5e45229)

I am a senior year college student from a tier 1 engineering college in India, have been really trying f
or MLE/Data Science/Research Engineer(in NLP domain) full time roles, but luck has not been on my side for a long time(o
r, maybe lack or practice). Experience wise, I've been part of academia and startup setting(plus president of student cl
ub on campus), but have a lot of difficulty in finding full time roles. I love just building stuff and researching thing
s(you can see that in my projects!), but it really is demotivating to not convert leads. I would really love an honest f
eedback, and maybe directions so that I can work on my shortcomings.   
```
---

     
 
all -  [ I Won a Gen AI Hackathon with a 10k USD prize thanks to llm side hustle!!! 1 of 150 participants (it ](https://www.reddit.com/r/LocalLLM/comments/1dakx5v/i_won_a_gen_ai_hackathon_with_a_10k_usd_prize/) , 2024-06-10-0955
```
Just basic proof that getting into LLMs is super beneficial, there is loads of low hanging fruits.

I developed 2 tools,
 in the first one I am working to applying langchain, and the second one I built thanks to langchain, from scratch.

Her
e is the LinkedIn Post

[https://www.linkedin.com/feed/update/urn:li:activity:7204882941972291586/](https://www.linkedin
.com/feed/update/urn:li:activity:7204882941972291586/)

DEMO Video:  
[https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s]
(https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s)

PRESENTATION Video:

[https://www.youtube.com/watch?v=gmx3KQ9D-jQ](h
ttps://www.youtube.com/watch?v=gmx3KQ9D-jQ)

The premise is, code on the PC from my phone (the tools can do much more th
at though). Autobot PC automation assistant can do CLI Commands, Code Interpreter, Operating the desktop with Mouse and 
Keyboard, and unlike Open Interpreter it works for these tasks, most of the time even with GPT 3.5. I developed these pr
ojects due to computer fatigue and back pain.

What do you think of these projects? Would you want to use any of these t
ools?
```
---

     
 
all -  [ Fetching data from sqllite3 and storing into Chromadb ](https://www.reddit.com/r/LangChain/comments/1dak6y7/fetching_data_from_sqllite3_and_storing_into/) , 2024-06-10-0955
```
Hi, I am fetching data from sqllite3 in python using conventional select query and storing it into a variable.
The outpu
t: ['Artificial Intelligence','Blockchain','RBA']
 I want to save this data in chromadb as embeddings. Please guide. 
```
---

     
 
all -  [ I Won a Gen AI Hackathon with a 10k USD prize thanks to Langchain!!! 1 of 150 participants (it is no ](https://www.reddit.com/r/LangChain/comments/1dajv55/i_won_a_gen_ai_hackathon_with_a_10k_usd_prize/) , 2024-06-10-0955
```
Just basic proof why langchain is the best for LLM Applications. 

I developed 2 tools, in the first one I am working to
 applying langchain, and the second one I built thanks to langchain, from scratch.

Here is the LinkedIn Post

[https://
www.linkedin.com/feed/update/urn:li:activity:7204882941972291586/](https://www.linkedin.com/feed/update/urn:li:activity:
7204882941972291586/)

DEMO Video:  
[https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s](https://www.youtube.com/watch?v=
j-MXVO4I14o&t=2s)

PRESENTATION Video:

[https://www.youtube.com/watch?v=gmx3KQ9D-jQ](https://www.youtube.com/watch?v=gm
x3KQ9D-jQ)

The premise is, code on the PC from my phone (the tools can do much more that though). Autobot PC automation
 assitant can do CLI Commands, Code Interpreter, Operating the desktop with Mouse and Keyboard, and unlike Open Interpre
ter it works for these tasks, most of the time even with GPT 3.5. I developed these projects due to computer fatigue and
 back pain. 

What do you think of these projects? Would you want to use any of these tools?
```
---

     
 
all -  [ How to finetune? ](https://www.reddit.com/r/huggingface/comments/1daiuil/how_to_finetune/) , 2024-06-10-0955
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
 
all -  [ Setting up a Writing assistant ](https://www.reddit.com/r/LocalLLaMA/comments/1dah4kh/setting_up_a_writing_assistant/) , 2024-06-10-0955
```
What Langchain implementation do you recommend for a novel writing assistant? I'm using faiss to store my notes and pdf'
s with historical context, but I had trouble with setting it up with Ollama chain, and it somehow fails to import. I've 
switched to a complete Github repository ([https://github.com/SonicWarrior1/pdfchat](https://github.com/SonicWarrior1/pd
fchat)) with a similar project, but got the same error importing RetrievalQA:

TypeError: ForwardRef.\_evaluate() missin
g 1 required keyword-only argument: 'recursive\_guard'

&#x200B;

Could it be a python version Issue?
```
---

     
 
all -  [ Data privacy in RAG applications ](https://www.reddit.com/r/LangChain/comments/1dagp8k/data_privacy_in_rag_applications/) , 2024-06-10-0955
```
Hi everyone! I have a general question about RAG and Data Privacy. I'm using langchain + ChromaDB to build an internal Q
&A chatbot, which is fed by multiple data sources (Slack, Confluence, Jira, Google Docs).

Now, when a user talks to the
 bot, I want to fetch documents which this user is allowed to see. For example, if a user is allowed to see document X b
ut not document Y, I want the semantic search to exclude document Y.

What's the best way of doing that? Are there any b
est practices/open source tools that help with that? I couldn't find much information online, and specifically about lan
gchain + privacy.
```
---

     
 
all -  [ Any thoughts on Mirascope LLM Framework? ](https://www.reddit.com/r/LocalLLaMA/comments/1dadfan/any_thoughts_on_mirascope_llm_framework/) , 2024-06-10-0955
```
No affiliation here. I read a lot of rants about LangChain (and a lesser extent, llama-index) and I found out about this
 [https://github.com/mirascope/mirascope](https://github.com/mirascope/mirascope)

I think the DevX was carefully design
ed. The function calling abstraction seems useful. Anyone has an opinion about that? Anyone already used it?
```
---

     
 
all -  [ Using O365 toolkits to schedule an event in calander  ](https://www.reddit.com/r/LangChain/comments/1dabz5d/using_o365_toolkits_to_schedule_an_event_in/) , 2024-06-10-0955
```
Hey, Does anyone tried to insert an event in calender using langchain and he didn't get this error ?

    ValueError: Ti
meZone data must be set using ZoneInfo objectsValueError: TimeZone data must be set using ZoneInfo objects
```
---

     
 
all -  [ LangGraph: Checkpoints vs History ](https://www.reddit.com/r/LangChain/comments/1dabjys/langgraph_checkpoints_vs_history/) , 2024-06-10-0955
```
Checkpoints seem to be the way to go for managing history for graph-based agents, proclaimed to be advantageous for conv
ersational agents, as history is maintained. Not only that, but there is the ability to move forward or go backward in t
he history as well, to cover up errors, or go back in time.

However, some disadvantages I notice is that subsequent cal
ls to the LLM (especially in the reAct agents, where everything is added to the messages list as context) take longer an
d of course use an ever increasing number of tokens.

There doesn't seem to be a way to manipulate that history dynamica
lly, or customize what is sent for each subsequent LLM call.

Additionally, there are only In-Memory, and SQLLite implem
entations of checkpointers by default; although the documentation advise to use something like Redis for production, the
re is no default Redis implementation. 

Are these planned to be implemented in the future, or left as a task meant for 
the developers to implement them as needed? I see there's an externally developed checkpoint implementation for Postgres
s. Redis, Maria, even an SQL Alchemy layer...are these implementations on us to do? It seems like quite a complex thing 
to implement.


And then in that case, rather than using checkpointers, maybe it might be simpler to maintain a chat his
tory as before? There are already existing tools to store message history in different databases. It should not be diffi
cult to create an additional state field that just stores the questions and responses of the conversation history, and u
tilize that in each invocation? That way, one would have more control over what is being sent, and even control summarie
s or required context in a more dynamic way, to maintain a reasonable token size per call, despite using graphs.

What a
re other's thoughts and experiences where this is concerned?
```
---

     
 
all -  [ Question regarding graphdb and vector db ](https://www.reddit.com/r/LangChain/comments/1daa9t3/question_regarding_graphdb_and_vector_db/) , 2024-06-10-0955
```
I was recently making a chatbot or Q and A assitant for a company. For that I scraped the company's whole website applie
d little bit of preprocessing and stored into chroma db with the help of langchain library and RAG architecture. I used 
gemini pro as the LLM.

When i dived deeper into vector storage, i discovered that some tutorials were using graphdb rat
her than vector db. 

My question is, what are the advantages or disadvantages of using one or another.

I am a beginner
 in this field, so spare me if you find this question stupid.
```
---

     
 
all -  [ OTP verification using langchain ](https://www.reddit.com/r/LangChain/comments/1da8d6n/otp_verification_using_langchain/) , 2024-06-10-0955
```
I'm facing an issue regarding OTP verification using langchain tools. I'm not able to store the user otp to use in a par
ticular tool. I'm unable to call desired otp verification tool. if someone here had worked or having same issue, please 
let me know. Thanks.
```
---

     
 
all -  [ Getting OpenAI API Error While Using Groq API for Python Coding Agent
 ](https://www.reddit.com/r/crewai/comments/1da7mxc/getting_openai_api_error_while_using_groq_api_for/) , 2024-06-10-0955
```
I am trying to create a Python coding agent using the `crewai` library along with `langchain` and `ChatGroq`. My code is
 supposed to use the Groq API for language model processing, but I am encountering an error related to OpenAI's API inst
ead.

    import logging
    from crewai import Agent, Task, Crew, Process
    from langchain.agents import Tool
    fro
m langchain_experimental.utilities import PythonREPL
    from langchain_community.tools.ddg_search.tool import DuckDuckG
oSearchRun
    from langchain_groq import ChatGroq
    
    # Ensure correct API key and model are set
    llm = ChatGro
q(temperature=0, api_key='MY_API_KEY', model='llama3-70b-8192')
    
    # Create the Python REPL tool
    python_repl =
 PythonREPL()
    python_repl_tool = Tool(
        name='python_repl',
        description='A Python shell. Use this to 
execute python commands. Input should be a valid python command. If you want to see the output of a value, you should pr
int it out with `print(...)`.',
        func=python_repl.run,
    )
    
    # Create the DuckDuckGo search tool
    duc
kduckgo_search = DuckDuckGoSearchRun()
    duckduckgo_search_tool = Tool(
        name='duckduckgo_search',
        desc
ription='A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input sh
ould be a search query.',
        func=duckduckgo_search.run,
    )
    
    coderAgent = Agent(
        role='Senior So
ftware engineer and developer',
        goal='Write production grade bug free code on this user prompt :- {topic}',
    
    verbose=True,
        memory=True,
        backstory=(
            'You are an experienced developer in big tech com
panies'
            'You have a record of writing bug-free python code all the time and delivering extraordinary program
ming logic'
            'You are extremely good at python programming '
        ),
        llm=llm,  # Optional
        
max_iter=10,  # Optional
        max_rpm=10,
        tools=[duckduckgo_search_tool],
        allow_delegation=True
    )

    
    # Creating a writer agent with custom tools and delegation capability
    DebuggerAgent = Agent(
        role=
'Code Debugger and bug solving agent',
        goal='You debug the code line by line and solve bugs and errors in the co
de by using Python_repl tool which can execute python code and give feedback',
        verbose=True,
        memory=True
,
        backstory=(
            'You are a debugger agent you have access to a python interpreter which can run python
 code and give feedback'
            'You also have internet searching capabilities if you are unable to solve the bug y
ou can search on the internet to solve that bug'
        ),
        tools=[duckduckgo_search_tool, python_repl_tool],
  
      llm=llm, 
        max_iter=10, 
        max_rpm=10,
        allow_delegation=True
    )
    
    # Research task
 
   coding_task = Task(
        description=(
            'Write code in this {topic}.'
            'Focus on writing bug
-free and production-grade code all the time'
            'You are extremely good in python programming language'
      
      'You should only return code'
        ),
        expected_output='A Bug-free and production-grade code on {topic}'
,
        tools=[duckduckgo_search_tool],
        llm=llm,
        agent=coderAgent,
    )
    
    # Writing task with 
language model configuration
    debug_task = Task(
        description=(
            'You should run the python code gi
ven by the CoderAgent and Check for bugs and errors'
            'If you find any bugs or errors then give feedback to t
he coderAgent to write code again this is the bug'
            'Always delegate the work if the executed python code giv
es error'
        ),
        expected_output='you should communicate to CoderAgent and give feedback on the code if the 
code got error while execution',
        tools=[duckduckgo_search_tool, python_repl_tool],
        agent=DebuggerAgent,

        llm=llm,
        # output_file='temp.py'  # Example of output customization
    )
    
    # Forming the tech-fo
cused crew with some enhanced configurations
    crew = Crew(
        agents=[coderAgent, DebuggerAgent],
        tasks=
[coding_task, debug_task],
        process=Process.sequential,  # Optional: Sequential task execution is default
       
 memory=True,
        cache=True,
        max_rpm=25,
        share_crew=True
    )
    
    # Starting the task executi
on process with enhanced feedback
    result = crew.kickoff(inputs={'topic': 'Write me code for maximum subarray sum in 
an Array using python and Dont you any helper methods to solve this just pure python'})
    print(result)

**However, I 
am encountering the following error:**

  
  File 'd:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\x.py', 
line 101, in <module>

result = crew.kickoff(inputs={'topic': 'Write me code for maximum subarray sum in an Array using 
python and Dont you any helper methods to solve this just pure python'})

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\si
te-packages\\crewai\\crew.py', line 264, in kickoff

result = self.\_run\_sequential\_process()

\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\
\site-packages\\crewai\\crew.py', line 305, in \_run\_sequential\_process

output = task.execute(context=task\_output)


\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codest
ral-python-agent\\.venv\\Lib\\site-packages\\crewai\\task.py', line 183, in execute

result = self.\_execute(

\^\^\^\^\
^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\cr
ewai\\task.py', line 192, in \_execute

result = agent.execute\_task(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D
:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewai\\agent.py', line 222, in 
execute\_task

memory = contextual\_memory.build\_context\_for\_task(task, context)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-too
l\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewai\\memory\\contextual\\contextual\_memory.py', line 24, in bu
ild\_context\_for\_task

context.append(self.\_fetch\_stm\_context(query))

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewa
i\\memory\\contextual\\contextual\_memory.py', line 33, in \_fetch\_stm\_context

stm\_results = self.stm.search(query)


\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.ve
nv\\Lib\\site-packages\\crewai\\memory\\short\_term\\short\_term\_memory.py', line 23, in search

return self.storage.se
arch(query=query, score\_threshold=score\_threshold)  # type: ignore # BUG? The reference is to the parent class, but th
e parent class does not have this parameters

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python
-agent\\.venv\\Lib\\site-packages\\crewai\\memory\\storage\\rag\_storage.py', line 95, in search       

else self.app.s
earch(query, limit)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python
-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\embedchain\\embedchain.py', line 653, in search

return \[{'co
ntext': c\[0\], 'metadata': c\[1\]} for c in self.db.query(\*\*params)\]

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^


  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\embedchain\\vectordb\
\chroma.py', line 220, in query

result = self.collection.query(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '
D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\chromadb\\api\\models\\Collecti
on.py', line 327, in query

valid\_query\_embeddings = self.\_embed(input=valid\_query\_texts)

\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\
.venv\\Lib\\site-packages\\chromadb\\api\\models\\Collection.py', line 633, in \_embed

return self.\_embedding\_functio
n(input=input)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codes
tral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\chromadb\\api\\types.py', line 193, in \_\_call\_\_


result = call(self, input)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestra
l-python-agent\\.venv\\Lib\\site-packages\\chromadb\\utils\\embedding\_functions.py', line 201, in \_\_call\_\_   

embe
ddings = self.\_client.create(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\
Codestral-python-agent\\.venv\\Lib\\site-packages\\openai\\resources\\embeddings.py', line 114, in create

return self.\
_post(

\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-p
ackages\\openai\\\_base\_client.py', line 1240, in post

return cast(ResponseT, self.request(cast\_to, opts, stream=stre
am, stream\_cls=stream\_cls))

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\
Lib\\site-packages\\openai\\\_base\_client.py', line 921, in request

return self.\_request(

\^\^\^\^\^\^\^\^\^\^\^\^\^
\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\openai\\\_base\_cli
ent.py', line 1020, in \_request

raise self.\_make\_status\_error\_from\_response(err.response) from None

openai.Authe
nticationError: Error code: 401 - {'error': {'message': 'Incorrect API key provided: fake. You can find your API key at 
https://platform.openai.com/account/api-keys.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_api\
_key'}}

  
I don't understand why an OpenAI API error is being triggered since my code is configured to use the Groq AP
I. I have verified that my API key is correct and have even generated new keys, but the issue persists.

**My request:**


1. If you know how to resolve this issue, please help.
2. If you have any resources similar to my agent implementation
 using `langchain`, please share those (optional).

Thank you!
```
---

     
 
all -  [ In text to sql how to answer question like 'what is being talked about...' ](https://www.reddit.com/r/LangChain/comments/1da6xka/in_text_to_sql_how_to_answer_question_like_what/) , 2024-06-10-0955
```
I want to answer these kind of questions, like what's being talked about consumption of cigarettes... but the problem is
 text column vector search is very slow in clickhouse or in pgvector. What are some the ways to do this? If I tried to u
se dedicated vector databases, how will LLM query this database? because it requires python code and not SQL. Are there 
any other ways? 
```
---

     
 
all -  [ Best way to automate large synthetic dataset creation? ](https://www.reddit.com/r/LocalLLaMA/comments/1da584q/best_way_to_automate_large_synthetic_dataset/) , 2024-06-10-0955
```
Trying to find the best way to automate the process of repeatedly generating QnA pairs where I can let the gpt-4 api run
 a prompt over multiple files of data for the QnA pairs. 

Has anyone got a script to run the process n times rather tha
n have to manually start the process every time you hit the context window? 


Prompts I’m referring to (as an example)


https://smith.langchain.com/hub/gitmaxd/synthetic-training-data?organizationId=5075780e-45c5-41c4-8ca7-e9291d6abbfc
htt
ps://smith.langchain.com/hub/homanp/question-answer-pair?organizationId=5075780e-45c5-41c4-8ca7-e9291d6abbfc
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-10-0955
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-10-0955
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-06-10-0955
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

     
