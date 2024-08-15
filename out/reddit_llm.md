 
all -  [ Passing Config to LangGraph Tool Discrepancies  ](https://www.reddit.com/r/LangChain/comments/1esdvq2/passing_config_to_langgraph_tool_discrepancies/) , 2024-08-15-0911
```
All my tools are created using BaseTool.

LangGraph documentation says I can invoke the graph with a configurable and it
 will be accessible in the tool's _run method's config Runnable. However, the value seems to be None.

I created an addi
tional tool using the @tool decorator and added it to the tools array for the graph, and noticed that the config was act
ually accessible there, with the specified values.

I even log the config in the different node runnables throughout the
 graph and see that it is present. So not sure why it isn't showing up in the _run for the base tool.

On a phone, but i
t was something like this:

```
@tool
def my_tool(param1: int, config: RunnableConfig):
    print('Config is', config, t
ype(config))

# I get 'Config is' {...really large dict...}, <dict>

tools=[my_tool]
```
```
class MyTool(BaseTool):
   
...
   def _run(
        param1: int,
        param2: string,
        config: RunnableConfig
    ):
        print('Confi
g is', config, type(config))

# I get 'Config is' None, <NoneType>
tools=[MyTool()] #no worries, it is properly instatia
ted and sent to the graph.
```

I use langgraph 0.1.17 (I forgot the correct number, but it's the last one before 0.2 du
e to breaking changes) but I doubt it's that, since BaseTool is from langchain_community, of which I have the latest ver
sion.

*Edit:* I call my graph using `graph.astream_events`. Not sure if that causes the difference, but including that 
knowledge here regardless. My BaseTool does not have a matching `_arun` method to go with all the async functions though
, but I'm not sure that is why it does not show the config.
```
---

     
 
all -  [ AI Innovations: AnthropicAIs Claude, Googles Gemini, and More ](https://www.reddit.com/r/ai_news_by_ai/comments/1es8w3v/ai_innovations_anthropicais_claude_googles_gemini/) , 2024-08-15-0911
```





#major_players #feature #tool #release #update #api #dataset #science #opinions #event #leaders #bigtech #hardware 
#opensource #startups #vc #paper #scheduled

AnthropicAI has introduced new features for Claude, including the ability t
o customize instructions for responses within projects. Claude Pro and Team users can now organize their chats into Proj
ects, enhancing idea generation and decision-making. Projects include a 200K context window for adding relevant document
s, code, and insights. Users can ground Claude's outputs in internal knowledge, define custom instructions, and create s
ide-by-side with Claude using Artifacts. Claude Team users can share snapshots of their best conversations with Claude t
o inspire collaboration and innovation [1][2]. 







AnthropicAI has also fine-tuned their Claude 3 Haiku model in Ama
zon Bedrock, allowing customers to customize the model for specialized tasks. Fine-tuning enhances performance, reduces 
costs, ensures consistent formatting, and provides an easy-to-use API. The technique has been successfully applied to mo
derating online comments and has garnered positive feedback from companies like SK Telecom and Thomson Reuters [4][5].








Anthropic has launched a new AI assistant app called 'Claude by Anthropic' developed by Anthropic PBC. The app off
ers instant answers, collaboration on tasks, and assistance with various activities. Users can access powerful AI models
 for knowledge on different subjects. The app is free to use, with an option to upgrade to a paid Pro plan for additiona
l features [7]. The Claude Android app by Anthropic is now available for download on Google Play [6].







Anthropic i
s expanding their bug bounty program to focus on finding universal jailbreaks in their next-generation safety system. Th
ey are offering rewards for novel vulnerabilities across various domains, including cybersecurity [10]. 







Mistral 
AI has released several new models including Mathstral, Codestral Mamba, and Mistral NeMo. These models specialize in ad
vanced mathematical problems, architecture research, and multilingual applications respectively [12][13][14]. Mistral AI
 also announced advancements in language models for software development, including simpler model customization, an alph
a release of Agents for creating custom behavior, and a stable version of their client SDK [15].







Google has intro
duced Gemini, which is considered the biggest advancement since the launch of Google Assistant. Gemini models enable mor
e natural communication by better understanding words and intent. Users can receive personalized help across Google's ap
ps with their permission [19]. Google's AI assistant, Gemini, is being developed for Android in 45 languages across over
 200 countries and territories [20]. Google has also introduced the Tensor G4 chip, which is their fastest and most powe
rful chip yet, developed in collaboration with Google DeepMind for Pixel devices [22].







Groq Inc is hiring ambitio
us individuals to work on their LLM inference solution. The company is looking for individuals to help take their techno
logy to the next level and change the world [28]. 







Financial institutions are using data analytics and generative
 AI for trading strategies and risk management in capital markets [33]. 







NVIDIA and LangChain held a Generative A
I Agents Developer Contest, with top prize winners including Agents of Inference, V-AI Personal Trainer, and Mystery Man
or [35]. 







Encord has raised $30 million in Series B funding to invest in the future of multimodal AI data develop
ment. The company aims to be the final AI data platform a company ever needs, with a focus on improving model performanc
e and reducing costs for customers [40].







Capsule is an interactive app that uses computer vision and generative A
I to help users find and buy products from any social media platform by snapping a screenshot [41].







Dimely, a Y C
ombinator's S24 startup, is an AI copilot for billing teams that automates manual workflows, saving teams hundreds of ho
urs monthly [42].







Yann LeCun discusses the limitations of auto-regressive language models (AR-LLMs) in innovation
 and problem-solving. He points out that while hallucinations and stochastic generation can create new content, it may n
ot always be useful or accurate [53].




[1. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/180561673171
4453826](https://twitter.com/AnthropicAI/status/1805616731714453826)

[2. Anthropic @AnthropicAI https://twitter.com/Ant
hropicAI/status/1805616734998544891](https://twitter.com/AnthropicAI/status/1805616734998544891)

[3. Anthropic @Anthrop
icAI https://twitter.com/AnthropicAI/status/1805616841789682000](https://twitter.com/AnthropicAI/status/1805616841789682
000)

[4. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1811084348692517323](https://twitter.com/Anthrop
icAI/status/1811084348692517323)

[5. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1811084350156320820]
(https://twitter.com/AnthropicAI/status/1811084350156320820)

[6. Anthropic @AnthropicAI https://twitter.com/AnthropicAI
/status/1813237754081251573](https://twitter.com/AnthropicAI/status/1813237754081251573)

[7. Anthropic @AnthropicAI htt
ps://twitter.com/AnthropicAI/status/1813241344573284491](https://twitter.com/AnthropicAI/status/1813241344573284491)

[8
. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1818985491271725488](https://twitter.com/AnthropicAI/sta
tus/1818985491271725488)

[9. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1819437715164713225](https:/
/twitter.com/AnthropicAI/status/1819437715164713225)

[10. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status
/1821533729765913011](https://twitter.com/AnthropicAI/status/1821533729765913011)

[11. Mistral AI @MistralAI https://tw
itter.com/MistralAI/status/1777872671709057307](https://twitter.com/MistralAI/status/1777872671709057307)

[12. Mistral 
AI @MistralAI https://twitter.com/MistralAI/status/1813222156265791531](https://twitter.com/MistralAI/status/18132221562
65791531)

[13. Mistral AI @MistralAI https://twitter.com/MistralAI/status/1813947930455499200](https://twitter.com/Mist
ralAI/status/1813947930455499200)

[14. Mistral AI @MistralAI https://twitter.com/MistralAI/status/1816133332582703547](
https://twitter.com/MistralAI/status/1816133332582703547)

[15. Mistral AI @MistralAI https://twitter.com/MistralAI/stat
us/1821251862554681828](https://twitter.com/MistralAI/status/1821251862554681828)

[16. Andrew Ng @AndrewYNg https://twi
tter.com/AndrewYNg/status/1823388325409140946](https://twitter.com/AndrewYNg/status/1823388325409140946)

[17. OpenAI @o
penai https://twitter.com/openai/status/1823404955933548818](https://twitter.com/openai/status/1823404955933548818)

[18
. Sundar Pichai @sundarpichai https://twitter.com/sundarpichai/status/1823408796565418040](https://twitter.com/sundarpic
hai/status/1823408796565418040)

[19. Google @google https://twitter.com/google/status/1823406418294194687](https://twit
ter.com/google/status/1823406418294194687)

[20. Google @google https://twitter.com/google/status/1823406999033274588](h
ttps://twitter.com/google/status/1823406999033274588)

[21. Google @google https://twitter.com/google/status/18234114148
34241753](https://twitter.com/google/status/1823411414834241753)

[22. Google @google https://twitter.com/google/status/
1823411698113335562](https://twitter.com/google/status/1823411698113335562)

[23. Google @google https://twitter.com/goo
gle/status/1823413757537644671](https://twitter.com/google/status/1823413757537644671)

[24. Google @google https://twit
ter.com/google/status/1823424424009150468](https://twitter.com/google/status/1823424424009150468)

[25. Google @google h
ttps://twitter.com/google/status/1823716797947756939](https://twitter.com/google/status/1823716797947756939)

[26. Groq 
Inc @GroqInc https://twitter.com/GroqInc/status/1823403817490334188](https://twitter.com/GroqInc/status/1823403817490334
188)

[27. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823404373072056542](https://twitter.com/GroqInc/status/
1823404373072056542)

[28. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823420810280808519](https://twitter.com
/GroqInc/status/1823420810280808519)

[29. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823711926834143370](htt
ps://twitter.com/GroqInc/status/1823711926834143370)

[30. Andrej Karpathy @karpathy https://twitter.com/karpathy/status
/1823418177197646104](https://twitter.com/karpathy/status/1823418177197646104)

[31. Andrej Karpathy @karpathy https://t
witter.com/karpathy/status/1823420863297028464](https://twitter.com/karpathy/status/1823420863297028464)

[32. Andrej Ka
rpathy @karpathy https://twitter.com/karpathy/status/1823422092035154432](https://twitter.com/karpathy/status/1823422092
035154432)

[33. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/1823421550940344598](https://twitter.com/NVIDIA
AI/status/1823421550940344598)

[34. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/18234116579
73887195](https://twitter.com/NVIDIAAIDev/status/1823411657973887195)

[35. NVIDIA AI Developer @NVIDIAAIDev https://twi
tter.com/NVIDIAAIDev/status/1823423501774340606](https://twitter.com/NVIDIAAIDev/status/1823423501774340606)

[36. NVIDI
A AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1823449446878740910](https://twitter.com/NVIDIAAIDev/
status/1823449446878740910)

[37. cohere @cohere https://twitter.com/cohere/status/1823438828201529491](https://twitter.
com/cohere/status/1823438828201529491)

[38. cohere @cohere https://twitter.com/cohere/status/1823444835631817072](https
://twitter.com/cohere/status/1823444835631817072)

[39. Y Combinator @ycombinator https://twitter.com/ycombinator/status
/1823404146680381830](https://twitter.com/ycombinator/status/1823404146680381830)

[40. Y Combinator @ycombinator https:
//twitter.com/ycombinator/status/1823436934842388830](https://twitter.com/ycombinator/status/1823436934842388830)

[41. 
Y Combinator @ycombinator https://twitter.com/ycombinator/status/1823453219114172421](https://twitter.com/ycombinator/st
atus/1823453219114172421)

[42. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1823736346344874293](ht
tps://twitter.com/ycombinator/status/1823736346344874293)

[43. Google AI @googleai https://twitter.com/googleai/status/
1823447342600872206](https://twitter.com/googleai/status/1823447342600872206)

[44. a16z @a16z https://twitter.com/a16z/
status/1823532409964691497](https://twitter.com/a16z/status/1823532409964691497)

[45. a16z @a16z https://twitter.com/a1
6z/status/1823532413236199918](https://twitter.com/a16z/status/1823532413236199918)

[46. a16z @a16z https://twitter.com
/a16z/status/1823532414863598003](https://twitter.com/a16z/status/1823532414863598003)

[47. a16z @a16z https://twitter.
com/a16z/status/1823532416692314284](https://twitter.com/a16z/status/1823532416692314284)

[48. xAI @xai https://twitter
.com/xai/status/1823597788573098215](https://twitter.com/xai/status/1823597788573098215)

[49. Yann LeCun @ylecun https:
//twitter.com/ylecun/status/1823412785545666942](https://twitter.com/ylecun/status/1823412785545666942)

[50. Yann LeCun
 @ylecun https://twitter.com/ylecun/status/1823456514398458266](https://twitter.com/ylecun/status/1823456514398458266)


[51. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823466302163325388](https://twitter.com/ylecun/status/1823466
302163325388)

[52. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823621547862499757](https://twitter.com/ylecun
/status/1823621547862499757)

[53. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823628775868752211](https://twi
tter.com/ylecun/status/1823628775868752211)

[54. Yann LeCun @ylecun https://twitter.com/ylecun/status/18236580574710622
18](https://twitter.com/ylecun/status/1823658057471062218)

[55. Yann LeCun @ylecun https://twitter.com/ylecun/status/18
23674931051180307](https://twitter.com/ylecun/status/1823674931051180307)

[56. Yann LeCun @ylecun https://twitter.com/y
lecun/status/1823675204243218723](https://twitter.com/ylecun/status/1823675204243218723)

[57. Yann LeCun @ylecun https:
//twitter.com/ylecun/status/1823675987441103227](https://twitter.com/ylecun/status/1823675987441103227)
```
---

     
 
all -  [ Which software tools and models for processing invoice PDFs? ](https://www.reddit.com/r/LocalLLM/comments/1es8s6o/which_software_tools_and_models_for_processing/) , 2024-08-15-0911
```
I'm just taking my first steps with AI. Please be considerate of me.
I am currently trying to build an application that 
allows me to read invoices in PDF format and output them in structured JSON. I am interested in all the details of the i
nvoice, such as sender, recipient, service date, invoice date, invoice number, each individual invoice item and so on.


In any case, I want to run the project *completely locally*, i.e. not integrate any third-party providers (currently I c
an only run it on the CPU, a more powerful graphics card will be added later). The invoice PDF is to be processed via RA
G.

My first question now is which software and which models are basically of interest to me here. I was thinking of Lan
gchain with Ollama and FAISS/Chroma, and possibly unstructured.io to prepare PDFs beforehand. I would possibly use Strea
mlit for a GUI.

Which language model would be suitable for me? Mistral? Can anyone give me tips on which tools and mode
ls are suitable?
```
---

     
 
all -  [ %100 python intelligence development framework ](https://i.redd.it/laqf2ege5oid1.png) , 2024-08-15-0911
```

```
---

     
 
all -  [ Portkey Gateway - An open-source AI Gateway with integrated Guardrails ](https://www.reddit.com/r/LangChain/comments/1es7gw5/portkey_gateway_an_opensource_ai_gateway_with/) , 2024-08-15-0911
```
We've been developing Portkey Gateway, an open-source AI gateway that's now processing billions of tokens daily across 2
00+ LLMs. Today, we're launching a significant update: integrated Guardrails at the gateway level.

Key technical featur
es:

Guardrails as middleware: We've implemented a hooks architecture that allows guardrails to act as middleware in the
 request/response flow. This enables real-time LLM output evaluation and transformation.

Flexible orchestration: The ga
teway can now route requests based on guardrail verdicts. This allows for complex logic like fallbacks to different mode
ls or prompts based on output quality.

Plugin system: We've designed a modular plugin system that allows integration of
 various guardrail implementations (e.g., guardrails ai, microsoft/guidance, vectara/hallucination-detection).

Stateles
s design: The guardrails implementation maintains the gateway's stateless nature, ensuring scalability and allowing for 
easy horizontal scaling.

Unified API: Despite the added complexity, we've maintained our unified API across different L
LM providers, now extended to include guardrail configurations.

Performance impact: Latency increase is minimal (<20ms)
 for most guardrails, and even lesser for deterministic guardrails like regex match, json schema check, etc.

Challenges
 we're still tackling:

Standardizing evaluation metrics across different types of guardrails

Handling guardrail false 
positives/negatives effectively

We believe this approach of integrating guardrails at the gateway level provides a powe
rful tool for managing LLM behavior in production environments.

The code is open-source, and we welcome contributions a
nd feedback.

We're particularly interested in hearing about specific use cases or challenges you've faced in implementi
ng reliable LLM systems.

Detailed note: [https://portkey.wiki/guardrail](https://portkey.wiki/guardrail)

What are your
 thoughts on this approach? Are there specific guardrail implementations or orchestration patterns you'd like to see add
ed?
```
---

     
 
all -  [ [OpenSource] Created this library for making finite state machine based agents ](https://www.reddit.com/r/OpenAIDev/comments/1es6mpy/opensource_created_this_library_for_making_finite/) , 2024-08-15-0911
```
Not another langchain or 'bla bla bla of give me tools and prompt and I create your agent' library, but instead an autom
aton based approach.. basically you define set of states and possible transitions, each state has it's own system prompt
 and its own instructions...

Check it out now! - [https://github.com/searchX/moorellm](https://github.com/searchX/moore
llm)

Also, since it is using latest structured responses from openai, so it will always 100% give correct format (bewar
e of quality XD)
```
---

     
 
all -  [ Created this library for making finite state machine based agents ](https://www.reddit.com/r/OpenAI/comments/1es6l9o/created_this_library_for_making_finite_state/) , 2024-08-15-0911
```
Not another langchain or 'bla bla bla of give me tools and prompt and I create your agent' library, but instead an autom
aton based agent approach.. basically you define set of states and possible transitions, each state has it's own system 
prompt and its own instructions...

Check it out now! - [https://github.com/searchX/moorellm](https://github.com/searchX
/moorellm)

Also, since it is using latest structured responses from openai, so it will always 100% give correct format 
(beware of quality XD)
```
---

     
 
all -  [ Why are you using RAG? ](https://www.reddit.com/r/LangChain/comments/1es4lh3/why_are_you_using_rag/) , 2024-08-15-0911
```
I'm building in the AI space, and I'm really curious what the most popular (and the most creative) use cases for RAG are
.

What are you building that requires RAG? How have you found the experience? Is anybody using RAG for something very u
nexpected?
```
---

     
 
all -  [ What is the difference Webvoiger and an Agent with PlayRight as a tool? ](https://www.reddit.com/r/LangChain/comments/1es3ea2/what_is_the_difference_webvoiger_and_an_agent/) , 2024-08-15-0911
```
We see Webvoiger can browse a web which can be done easily with an Agent with Playright as a tool. What could be the dif
ference between these two implementations in terms of capability of intelligent web browsing?
```
---

     
 
all -  [ Can Langchain Query Multiple Datasources? ](https://www.reddit.com/r/LangChain/comments/1es32w3/can_langchain_query_multiple_datasources/) , 2024-08-15-0911
```
Hi all,

I am quite new to Langchain but I am trying to develop a chatbot that can query multiple databases of different
 types and sources (sql database, webscraped data, etc.).

Ideally, I would also like the different sources to be able t
o 'collaborate' with each other? Since I am working with webscraped news data, it would be nice to have the data in my s
ql database to interact with the news data. But perhaps that is really not possible, please let me know. I would be happ
y enough if it can switch and identify the right source.


```
---

     
 
all -  [ (Profile Review) Looking for honest review of my profile ](https://i.redd.it/o01k3kdy1nid1.jpeg) , 2024-08-15-0911
```
Can
```
---

     
 
all -  [ Filtering before similarity search in Faiss ](https://www.reddit.com/r/LangChain/comments/1erz8b9/filtering_before_similarity_search_in_faiss/) , 2024-08-15-0911
```
I have a project that requires filtering before search. I initially used DeepLake, but I noticed it was slow, so I switc
hed to Faiss. However, I'm facing an issue where the `similarity_search` function performs the similarity search first a
nd then applies filtering. Is there a way to reverse this order, so filtering happens before the similarity search?
```
---

     
 
all -  [ Integrating Multimodal RAG with Google Gemini 1.5 Flash and Pathway ](https://www.reddit.com/r/LangChain/comments/1erz1ww/integrating_multimodal_rag_with_google_gemini_15/) , 2024-08-15-0911
```
Hey everyone, I wanted to share a new app template that goes beyond traditional OCR by effectively extracting and parsin
g visual elements like images, diagrams, schemas, and tables from PDFs using Vision Language Models (VLMs). This setup l
everages the power of Google Gemini 1.5 Flash within the Pathway ecosystem.

👉 Check out the full article and code here:
 [https://pathway.com/developers/templates/gemini-multimodal-rag](https://pathway.com/developers/templates/gemini-multim
odal-rag)  
  
**Why Google Gemini 1.5 Flash?**  
– It’s a key part of the GCP stack widely used within the Pathway and 
broader LLM community.  
– It features a 1 million token context window and advanced multimodal reasoning capabilities. 
 
– New users and young developers can access up to $300 in free Google Cloud credits, which is great for experimenting 
with Gemini models and other GCP services.

**Does Gemini Flash’s 1M context window make RAG obsolete?**  
Some might ar
gue that the extensive context window could reduce the need for RAG, but the truth is, RAG remains essential for curatin
g and optimizing the context provided to the model, ensuring relevance and accuracy.

For those interested in understand
ing the role of RAG with the Gemini LLM suite, this template covers it all.  
  
To help you dive in, we’ve put together
 a detailed, step-by-step guide with code and configurations for setting up your own Multimodal RAG application. Hope yo
u find it useful!
```
---

     
 
all -  [ Claude keeps repeating sentences like 'Based on the articles' in the answer ](https://www.reddit.com/r/ClaudeAI/comments/1eryikm/claude_keeps_repeating_sentences_like_based_on/) , 2024-08-15-0911
```
I am using Claude Haiku via Amazon Bedrock and Langchain (ChatBedrock API) to create a simple RAG chatbot. 

The problem
 I'm facing is that the model keeps repeating sentences like 'Based on the articles' in the answer.  
My goal is to not 
mention that the answer is based on the articles. 

I've tried to add explicit rules that deny this type of behaviour an
d provided examples without luck. 

For reference, this is the prompt template I am using:

'''  
You are a customer sup
port bot. Your goal is to answer customer queries by strictly adhering to the information obtained verbatim from the art
icles provided below. The customer question is wrapped in the <question></question> XML tags, while the articles are wra
pped in the <articles></articles> XML tags. 

<question>  
{question}  
</question>

<articles>  
{context}  
</articles
>

Follow these rules:  
- NEVER reference the word 'article' in the answer. For instance, never write: “Based on the in
formation provided”, 'According to the articles', 'According to the information provided' or 'The articles state'.  
- I
f there is no relevant information in articles, write “No relevant information” instead.   
- Answer the question, start
ing with “Answer:“  
- Do not rely on internal knowledge or make speculative predictions to answer questions. Do not hal
lucinate.  
- Write only information that answers the question, without any extra non-relevant information.  
'''

  
Ha
s anyone got the same behaviour?
```
---

     
 
all -  [ A guide to understand Semantic Splitting for document chunking in LLM applications ](https://www.reddit.com/r/LangChain/comments/1erxo60/a_guide_to_understand_semantic_splitting_for/) , 2024-08-15-0911
```
Hey everyone,

Today, I want to share an in-depth guide on semantic splitting, a powerful technique for chunking documen
ts in language model applications. This method is particularly valuable for retrieval augmented generation (RAG)

🎥 I ha
ve a YT video with a hands on Python implementation if you're interested check it out: [https://youtu.be/qvDbOYz6U24](ht
tps://youtu.be/qvDbOYz6U24)

# The Challenge with Large Language Models

Large Language Models (LLMs) face two significa
nt limitations:

1. **Knowledge Cutoff**: LLMs only know information from their training data, making it challenging to 
work with up-to-date or specialized information.
2. **Context Limitations**: LLMs have a maximum input size, making it d
ifficult to process long documents directly.

# Retrieval Augmented Generation

To address these limitations, we use a t
echnique called Retrieval Augmented Generation:

1. Split long documents into smaller chunks
2. Store these chunks in a 
database
3. When a query comes in, find the most relevant chunks
4. Combine the query with these relevant chunks
5. Feed
 this combined input to the LLM for processing

The key to making this work effectively lies in how we split the documen
ts. This is where semantic splitting shines.

# Understanding Semantic Splitting

Unlike traditional methods that split 
documents based on arbitrary rules (like character count or sentence number), semantic splitting aims to chunk documents
 based on meaning or topics.

**The Sliding Window Technique**

1. Here's how semantic splitting works using a sliding w
indow approach:
2. Start with a window that covers a portion of your document (e.g., 6 sentences).
3. Divide this window
 into two halves.
4. Generate embeddings (vector representations) for each half.
5. Calculate the divergence between the
se embeddings.
6. Move the window forward by one sentence and repeat steps 2-4.
7. Continue this process until you've co
vered the entire document.

The divergence between embeddings tells us how different the topics in the two halves are. A
 high divergence suggests a significant change in topic, indicating a good place to split the document.

**Visualizing t
he Results**

If we plot the divergence against the window position, we typically see peaks where major topic shifts occ
ur. These peaks represent optimal splitting points.

**Automatic Peak Detection**

To automate the process of finding sp
lit points:

1. Calculate the maximum divergence in your data.
2. Set a threshold (e.g., 80% of the maximum divergence).

3. Use a peak detection algorithm to find all peaks above this threshold.

These detected peaks become your automatic s
plit points.

# A Practical Example

Let's consider a document that interleaves sections from two Wikipedia pages: 'Fran
cis I of France' and 'Linear Algebra'. These topics are vastly different, which should result in clear divergence peaks 
where the topics switch.

1. Split the entire document into sentences.
2. Apply the sliding window technique.
3. Calcula
te embeddings and divergences.
4. Plot the results and detect peaks.

You should see clear peaks where the document swit
ches between historical and mathematical content.

# Benefits of Semantic Splitting

1. Creates more meaningful chunks b
ased on actual content rather than arbitrary rules.
2. Improves the relevance of retrieved chunks in retrieval augmented
 generation.
3. Adapts to the natural structure of the document, regardless of formatting or length.

# Implementing Sem
antic Splitting

To implement this in practice, you'll need:

1. A method to split text into sentences.
2. An embedding 
model (e.g., from OpenAI or a local alternative).
3. A function to calculate divergence between embeddings.
4. A peak de
tection algorithm.

# Conclusion

By creating more meaningful chunks, **Semantic Splitting** can significantly improve t
he performance of retrieval augmented generation systems.

I encourage you to experiment with this technique in your own
 projects.

It's particularly useful for applications dealing with long, diverse documents or frequently updated informa
tion.
```
---

     
 
all -  [ How strong is the moat of Vector DB?  ](https://www.reddit.com/r/LangChain/comments/1erxdp0/how_strong_is_the_moat_of_vector_db/) , 2024-08-15-0911
```
Hey community!  
I recently saw a post on LinkedIn, that with time the moat of VectorDB will vanish if classic DB such a
s Mongo / Postgres DB also are Vector DB (which they already do support through extensions today). Hence will Vector DB 
(Qdrant, Pinecone, and Weaviate) become obsolete? What is your take on that? 
```
---

     
 
all -  [ Chainlit Memory issue ](https://www.reddit.com/r/LangChain/comments/1erwviw/chainlit_memory_issue/) , 2024-08-15-0911
```
https://preview.redd.it/dgvpzqoxhlid1.png?width=612&format=png&auto=webp&s=96103d227a01c3f4523467191aa5a43db69c8524

Hel
lo, guys! NEED HELP, take a look at this PHOTO; after I resume the previous chat in which I uploaded the pdf and had a c
onversation, the session is again performing RAG on the pdf, and then I may continue the prior conversation. It is able 
to have memory, chat history, and the path of the pdf uploaded, however every time I resume the chat, it is performing r
ag on pdf again, slowing down the bot.Also if any one has updated langchain(v0.2) memory implementation with chainlit, d
o share your work.   

```
---

     
 
all -  [ Bug: LangGraph Agent Studio page does not load for me anymore. ](https://www.reddit.com/r/LangChain/comments/1erw6vw/bug_langgraph_agent_studio_page_does_not_load_for/) , 2024-08-15-0911
```
Hi, If someone from Langchain can see this, I'm having trouble accessing - [LangGraph Stuido](https://smith.langchain.co
m/studio/thread?baseUrl=https%3A%2F%2Flanggraph-engineer-23dacb3822e3589d80ff57de9ee94e1c.default.us.langgraph.app#) pag
e. It was working fine but the last thing I did was select the 'agent' option from the top left dropdown. The default wa
s engineer.

I tried logging out and logging back in and clearing cache nothing works.

However I logged in from my alt 
account and the link loads fine.

If there's anyone around from the team please DM me thanks :) I'd like to get back my 
original account to work. Thanks
```
---

     
 
all -  [ Question regarding feasibility of a project ](https://www.reddit.com/r/LangChain/comments/1erw3uo/question_regarding_feasibility_of_a_project/) , 2024-08-15-0911
```
Hello guys,

i would like to appologize for my grammar in advance, since my english isn't the best anymore.

im pretty n
ew to LLM's and langchain. Over the last couple weeks I have been trying to read as much as possible about LLM's and RAG
 but I feel like there is always something more to discover which I like.

  
There is something I would like to build, 
but I'm unsure if its possible. We use airtable and zapier to automate our processes. We would like to automate our cust
omer sucess next, using a whatsapp variant additionally. 

  
I thought, that I might be able to build an Agent that has
 all the relevant information about Zapier (triggers and actions), Airtable (our database structure, the fields type and
 names etc) and superchat. I have around 6-7 big JSON files that contain these informations. My goal is that if I ask th
e agent how I could automate a given state of our process, that it will create me a complete 'zap' or part of the proces
s. By that I don't mean that the ai will create a zap in zapier, but just a template that can I could rebuild.

  
I'm p
retty unsure on what I should do next and if a RAG application is even able to handle my huge JSON files. I would really
 appreciate some guidance or even small tips on how I should proceed.
```
---

     
 
all -  [ Anyone else that finds langchain overly complicated ](https://www.reddit.com/r/ChatGPTCoding/comments/1eruvkm/anyone_else_that_finds_langchain_overly/) , 2024-08-15-0911
```
I find langchain pretty complicated especially for simple tasks like interacting with CSV files. I decided to build my o
wn simple pipeline for this:  
[https://medium.com/gitconnected/chat-with-csv-files-using-googles-gemini-flash-no-langch
ain-0e8f79d63348](https://medium.com/gitconnected/chat-with-csv-files-using-googles-gemini-flash-no-langchain-0e8f79d633
48)
```
---

     
 
all -  [ Chaining Multiple Function Calls with Interrelated Data Using OpenAI API and LangChain ](https://www.reddit.com/r/LLMDevs/comments/1eru7wz/chaining_multiple_function_calls_with/) , 2024-08-15-0911
```
Hello everyone,

I am currently working on function calling using the OpenAI API with Langchain. I can successfully call
 either a single function or the same function multiple times. The process works efficiently and accurately. However, my
 task involves invoking multiple, different functions that are interrelated.

To elaborate further, I have a function th
at takes a code as a parameter. I can call this function by submitting a prompt to my API. For example, 'Get the job ord
er with the code MM924001.' Once I retrieve the job order data, it returns a JSON object containing numerous key-value p
airs, such as id, jobOrderCode, productId, stationId, etc.

My goal is to call additional functions using this data, suc
h as stationId and productId. For example, if I want to know the station name associated with the job order that has the
 code MM924001, I would need to call multiple functions in sequence:

Example:

* Request: 'I want to know the station n
ame of the job order with code MM924001.'
* Functions: get\_job\_order(code), get\_station\_info(stationId)
```
---

     
 
all -  [ Am I in correct path in learning AI ? ](https://www.reddit.com/r/learnmachinelearning/comments/1erqhh1/am_i_in_correct_path_in_learning_ai/) , 2024-08-15-0911
```
I learnt ML/DL (till CNN) few years ago, from then on I did a few side projects.

I continued my learning this jan, and 
I got to know about ANN, RNN, LSTM, Transfomers architecture. This continued for 3 months, and by this april-may.  I did
 not get much practise in RNN, LSTM, I just coded using keras only once, that too i trained for 3 epochs...done..no hype
rparameter tuning, no real life application like NMT etc., But i am kind of guy who likes to study in depth, so i invest
 lot of time to learn BTS, and code less, I cant move ahead without clarity on existing block, and so once i got clarity
 I moved ahead.

  
From then, the actual chaos stared...there is lot of buzz towards LLM's.  I dont know where to look 
at..from friends suggestion, I read huggingface autotokenizers, autoclasses etc., (only read), and then made few api cal
ls to groq chat models.



Once i got a grasp of what is happening in these calls, abstraction etc., I learnt about lang
chain.

  
I got the api key, made few calls to chatgroq via langchain, got little bit of clairty on prompt templates (a
lthough there is not much in this, just AIMessage, HumanMessage, SystemMessage and python formatting), after prompt temp
lates...the chains, I got struck here as there are many chains and got liiiiiitle bit of clarity recently, and then abou
t memory strategies and finally vector store, FAISS, pipecone.

  
I built a simple multi pdf chat app, code-to-code fro
m a youtube video, I am not fan of copy cat ideas or github cut-copy-paste. To be frank, all this code, if boiled down l
ead to this:

1. create embeddings

2. vector store

3. query - similarity search

4. retrieve docs

5. Send them to LLM
 (an api call)

  
Now, I am here.

  
I want a good career in AI space, especially this LLMs etc.,

  
Am i in the corr
ect path ? Did i miss major stones, which are gems ?

And what after ?
```
---

     
 
all -  [ Iterating over data in LangFlow ](https://www.reddit.com/r/LangChain/comments/1erpfdd/iterating_over_data_in_langflow/) , 2024-08-15-0911
```
I have a large document that I want to split up into chunks.  I can use the recursive text splitter to break them up int
o 10k token chunks and it returns the array of data.  But I'm struggling to understand how I can iterate over each item 
in that data list, run it through the model, and then output each item into the chat.  (or collect each item into a new 
list)

There doesn't seem to be a mechanism to run this through an iterative loop.  Can anybody help?
```
---

     
 
all -  [ [3 YoE, Machine Learning & Gen AI Engineer, ML & Gen AI Engineer, United States] ](https://www.reddit.com/r/resumes/comments/1ermud1/3_yoe_machine_learning_gen_ai_engineer_ml_gen_ai/) , 2024-08-15-0911
```
Hi, looking for some constructive feedback.

Have not been getting any responses lately.

For the context: last two jobs
 are the same company. Went from intern to FT.

Graduate researcher is on-campus job in my Uni.

Those that are marked i
n red are not in US jobs/educations.

ML & DS internship is in F500, current job is a small local company in NYC

Lookin
g for some ML/Gen AI roles

Thank you!

https://preview.redd.it/qb69aix2riid1.jpg?width=612&format=pjpg&auto=webp&s=322e
75089d7b10f0a2149c986bdb53e665123992


```
---

     
 
all -  [ Seeking a job opportunity in Bangalore for ML role ](https://www.reddit.com/r/LangChain/comments/1erhv9r/seeking_a_job_opportunity_in_bangalore_for_ml_role/) , 2024-08-15-0911
```


Hi folks! I am a Machine Learning Engineer with almost one year of experience in Hyderabad (not completed 1 year. It's
 still 10 months). I am looking for a ML Engineer role in Bengaluru. I specialise in RAG chatbots and LLMs along with ba
sic foundational ML models from Sci-kit Learn. I have also worked on predictive analysis forecasting future predictions 
of movie revenue from last historical data. I am good with data overall.

Any leads would be helpful
```
---

     
 
all -  [  Project Alice - an open source framework for agentic workflows  ](https://www.reddit.com/r/AutoGPT/comments/1erhl9r/project_alice_an_open_source_framework_for/) , 2024-08-15-0911
```
Hi everyone!

I don't know if I'm alone here, but my experience trying to build agentic workflows has been a frustrating
 one: Current frameworks, like LangChain (and its siblings) and Autogen, offer a lot of value but lack the combination t
hat I wanted: A decent UX to create, test and deploy llm-powered agentic workflows. Paid solutions abstract the content 
from you, and put barriers in your ability to truly own the flows you create.

At a high level, Project Alice is Autogen
 (chat) + Autogen Studio (UI) + Langchain (tasks), all in one: It offers a frontend to define, edit and execute tasks an
d chats, while being able to choose whatever model you want (local or otherwise).

[Repository](https://github.com/Maria
noMolina/project_alice)

This is my initial launch of this project. I honestly have no idea how long I will keep investi
ng time in this, but at the very least: This is an honest attempt at creating an open source framework that is legible/u
nderstandable (even if you are not a senior engineer) that you get to use as you wish, make any changes you need (ideall
y, share them so we can all benefit =), etc.

The project can be downloaded and used in a few minutes, all you really ne
ed is Git, Python, npm, Docker and optionally LM Studio. If you do, you can use local models out of the box. Alternative
ly, you can also use OpenAI's or Anthropic's APIs.

I would greatly appreciate any and all feedback, and if you feel lik
e contributing, the doors are open!
```
---

     
 
all -  [  Project Alice - an open source framework for agentic workflows  ](https://www.reddit.com/r/AutoGenAI/comments/1erhk18/project_alice_an_open_source_framework_for/) , 2024-08-15-0911
```
Hi everyone!

I don't know if I'm alone here, but my experience trying to build agentic workflows has been a frustrating
 one: Current frameworks, like LangChain (and its siblings) and Autogen, offer a lot of value but lack the combination t
hat I wanted: A decent UX to create, test and deploy llm-powered agentic workflows. Paid solutions abstract the content 
from you, and put barriers in your ability to truly own the flows you create.

At a high level, **Project Alice** is Aut
ogen (chat) + Autogen Studio (UI) + Langchain (tasks), all in one: It offers a frontend to define, edit and execute task
s and chats, while being able to choose whatever model you want (local or otherwise).

[Repository](https://github.com/M
arianoMolina/project_alice)

This is my initial launch of this project. I honestly have no idea how long I will keep inv
esting time in this, but at the very least: This is an honest attempt at creating an open source framework that is legib
le/understandable (even if you are not a senior engineer) that you get to use as you wish, make any changes you need (id
eally, share them so we can all benefit =), etc.

The project can be downloaded and used in a few minutes, all you reall
y need is Git, Python, npm, Docker and optionally LM Studio. If you do, you can use local models out of the box. Alterna
tively, you can also use OpenAI's or Anthropic's APIs.

I would greatly appreciate any and all feedback, and if you feel
 like contributing, the doors are open!
```
---

     
 
all -  [  Project Alice - an open source framework for agentic workflows  ](https://www.reddit.com/r/ChatGPTCoding/comments/1erhgmi/project_alice_an_open_source_framework_for/) , 2024-08-15-0911
```
Hi everyone!

I don't know if I'm alone here, but my experience trying to build agentic workflows has been a frustrating
 one: Current frameworks, like LangChain (and its siblings) and Autogen, offer a lot of value but lack the combination t
hat I wanted: A decent UX to create, test and deploy llm-powered agentic workflows. Paid solutions (including OpenAI's) 
abstract the process from you, and put barriers in your ability to truly own the flows you create.

At a high level, **P
roject Alice** is Autogen (chat) + Autogen Studio (UI) + Langchain (tasks), all in one: It offers a frontend to define, 
edit and execute tasks and chats, while being able to choose whatever model you want (local or otherwise).

[Repository]
(https://github.com/MarianoMolina/project_alice)

This is my initial launch of this project. I honestly have no idea how
 long I will keep investing time in this, but at the very least: This is an honest attempt at creating an open source fr
amework that is legible/understandable (even if you are not a senior engineer) that you get to use as you wish, make any
 changes you need (ideally, share them so we can all benefit =), etc.

The project can be downloaded and used in a few m
inutes, all you really need is Git, Python, npm, Docker and optionally LM Studio. If you do, you can use local models ou
t of the box. Alternatively, you can also use OpenAI's or Anthropic's APIs.

I would greatly appreciate any and all feed
back, and if you feel like contributing, the doors are open!
```
---

     
 
all -  [ Project Alice - an open source framework for agentic workflows ](https://www.reddit.com/r/LocalLLaMA/comments/1erhdhp/project_alice_an_open_source_framework_for/) , 2024-08-15-0911
```
Hi everyone!

I don't know if I'm alone here, but my experience trying to build agentic workflows has been a frustrating
 one: Current frameworks, like LangChain (and its siblings) and Autogen, offer a lot of value but lack the combination t
hat I wanted: A decent UX to create, test and deploy llm-powered agentic workflows. Paid solutions abstract the content 
from you, and put barriers in your ability to truly own the flows you create. 

At a high level, **Project Alice** is Au
togen (chat) + Autogen Studio (UI) + Langchain (tasks), all in one: It offers a frontend to define, edit and execute tas
ks and chats, while being able to choose whatever model you want (local or otherwise). 

[Repository](https://github.com
/MarianoMolina/project_alice)

This is my initial launch of this project. I honestly have no idea how long I will keep i
nvesting time in this, but at the very least: This is an honest attempt at creating an open source framework that is leg
ible/understandable (even if you are not a senior engineer) that you get to use as you wish, make any changes you need (
ideally, share them so we can all benefit =), etc. 

The project can be downloaded and used in a few minutes, all you re
ally need is Git, Python, npm, Docker and optionally LM Studio. If you do, you can use local models out of the box. Alte
rnatively, you can also use OpenAI's or Anthropic's APIs. 

I would greatly appreciate any and all feedback, and if you 
feel like contributing, the doors are open!
```
---

     
 
all -  [ Chat Memory History in Production - Architectures and Methods  ](https://www.reddit.com/r/LangChain/comments/1ergfbf/chat_memory_history_in_production_architectures/) , 2024-08-15-0911
```
Hey guys, we're currently working on 2 applications in our company. In this first stage, both of them will be running 'o
ffline', meaning that it won't be any interaction with the users. On both cases we've created a chain that is taking the
 data from our Azure SQL Server, sending to the LLM via prompt and the output goes to Service Now. We're using 2 separat
ed python scripts for that and they're being triggered by a set of internal rules. Since there are now interactions with
 the users at this first output, we're keeping simple.

Now, we would like to test a 'copilot' with one of these outputs
, a Q&A. The idea here is just to help an engineer to solve a ticket faster. We don't want to store the chat history in 
any database but rather do something similar to Microsoft Copilot by limiting to 10/20 interactions and keep the memory 
just while the user is interacting with the LLM and completely delete after the session is over.

Which approach you guy
s think would be good to take in this scenario to push into production? The LangChain methods should be enough or should
 we go another route?

Thanks!
```
---

     
 
all -  [ Is there a way to get a list of all the documents that have been loaded in to a persisted database? ](https://www.reddit.com/r/LangChain/comments/1ergek0/is_there_a_way_to_get_a_list_of_all_the_documents/) , 2024-08-15-0911
```
I would like to have them listed so I can select and delete ones that I don't want, basically...
```
---

     
 
all -  [ List of Messages in Custom LLM in Langchain ](https://www.reddit.com/r/LangChain/comments/1ereuoh/list_of_messages_in_custom_llm_in_langchain/) , 2024-08-15-0911
```
Hi there,

I am trying to implement Custom LLM.  
When i am using ChatOpenAI and add few shot prompts in the messages wi
th system and user message, all the messages are properly sent in the array as   
0: {'role': 'system', content: 'abc...
'}  
1: {'role': 'user', content: 'abc...'}  
2: {'role': 'assistant', content: 'abc...'}  
3: {'role': 'user': content'
: 'abc...'}

and so on

But when i do it using custom LLM, all the above data is sent as string to the \_call function, 
and everything is in string in this format

Human: abc...  
Human: abc..  
AI: abc..  
Human: abc..

 so i am forced to 
send it as string to the backend and then backend replies with 'AI: my output'

has anyone encountered this?
```
---

     
 
all -  [ Project 3 | ConversAI | Difficulty 4.5 | https://aishwaryamensinkai.github.io/HAI-ChatBot/ ](https://www.reddit.com/r/myHeadstarter/comments/1ere26w/project_3_conversai_difficulty_45/) , 2024-08-15-0911
```
**Hey everyone!**

We’re excited to share **ConversAI**, an AI-powered customer support chatbot built using Next.js, Rea
ct, OpenAI, and Vercel. Our team worked hard to create an intelligent, responsive chatbot that not only answers customer
 queries but also provides a personalized experience.

🎥 Check out our video: [link](https://www.loom.com/share/298101bc
e026431cab46440d40a4b2a7?sid=db177f30-15c9-47fb-978d-469295b24586)

# 🔗 Deployed Application Links:

* **Main Applicatio
n:** [ConversAI App](https://aishwaryamensinkai.github.io/HAI-ChatBot/)
* **CVersion 1.5 :** [link](https://ai-chat-bot-
liart.vercel.app/)
* **CVersion 2.0 :** [link](https://chatbot-pi-murex-77.vercel.app/sign-in)

# 💡 What We Would Do wit
h More Time:

* **Expand RAG Implementation:** We’d dive deeper into refining the Retrieval-Augmented Generation (RAG) s
etup, making the chatbot even smarter by expanding the knowledge base.
* **Enhance Multi-Language Support:** We’d introd
uce additional languages to cater to a more diverse customer base.
* **Improve LLM Orchestration:** Further improve the 
orchestration pattern to seamlessly integrate more task-specific models.

**Build with**: Next.js, React, JavaScript, Pi
necone API, OpenAI, RAG Integration, Firebase, Langchain

# 👥 Team Dynamics & Exciting Experience:

Our team collaborate
d incredibly well, with each member bringing unique skills to the table. The most exciting part? Seeing the chatbot go f
rom a basic, hardcoded responder to a sophisticated AI that interacts intelligently with users. The journey from brainst
orming to deployment was a thrilling learning experience for all of us.

We’re open to feedback and would love to hear y
our thoughts! Feel free to try out the chatbot, explore the code, or even contribute to the project. Thanks for checking
 out **ConversAI**!
```
---

     
 
all -  [ [8 YoE, SDE3, Staff Engineer (Backend), India] ](https://www.reddit.com/r/resumes/comments/1ercvb5/8_yoe_sde3_staff_engineer_backend_india/) , 2024-08-15-0911
```
Hi,

Can you guys please review my resume and let me know if there's anything that might need improvement? I've noticed 
that I have never received any interview calls from FAANG-like companies, although mid-sized companies frequently reach 
out to me for job opportunities.

I am seeking senior-level positions (staff engineer), and everything mentioned in my r
esume reflects my hands-on experience, not just theoretical knowledge.

https://preview.redd.it/0588je5ungid1.png?width=
2736&format=png&auto=webp&s=53cf6df8132019bd87a11c5cda58a2e77058eaa6

Thanks  

```
---

     
 
all -  [ Resume Review : 8 YEO of Experience how to get calls from FAANG like companies  ](https://www.reddit.com/r/developersIndia/comments/1ercoth/resume_review_8_yeo_of_experience_how_to_get/) , 2024-08-15-0911
```
Hi,

Can you guys please review my resume and let me know if there's anything that might need improvement? I've noticed 
that I haven't received any interview calls from FAANG-like companies, although mid-sized companies frequently reach out
 to me for job opportunities.

I am seeking senior-level positions (staff engineer), and everything mentioned in my resu
me reflects my hands-on experience, not just theoretical knowledge

https://preview.redd.it/11mt0gaimgid1.png?width=2736
&format=png&auto=webp&s=5fbc1b702d9542fdf16af4f288b140c988287d59

Any guidance would be appreciated.  



```
---

     
 
all -  [ How are LLMs are used in production? ](https://www.reddit.com/r/LocalLLM/comments/1ercg3a/how_are_llms_are_used_in_production/) , 2024-08-15-0911
```
I am just a beginner so don't bash me if I sound stupid.
I am currently working on a FYP related to Story Generation, af
ter spending about 2.5 months of getting the basics of various aspects of working with LLMs I still couldn't figure out 
what would be the best approach to use an open source LLM inside a full stack application.

Most of the open source proj
ects I found used Open AIs API with Langchain but since that's a very expensive option I have to go with an open source 
model. Now the part where I have questions is integerating my model with my backend.

I have a decent experience in work
ing with express so I was hoping there was a way to I can make my API in it.

Questions:

1. Should I make my project in
side a python framework ( flask or FastAPI ) and then an entire module for story generation inside this? My guess is thi
s that this will make the requests very slow because of the model.

2. Should I use hosted LLMs such as TogetherAI or Pe
rplexity etc. It definitely sounds like a cheaper option ?

3. Should I make a separate microservice for my model and NL
P part and keep the rest of my API seperate?




```
---

     
 
all -  [ DISCUSSION: Increase Response Time with Multiple Tools ](https://www.reddit.com/r/LangChain/comments/1ercf39/discussion_increase_response_time_with_multiple/) , 2024-08-15-0911
```
Hi everyone, I’m currently developing a chatbot using LangGraph with Gemini-1.5-pro (Vertex). I have a setup with severa
l agents.

I’ve noticed that increasing the number of tools an agent has also increases the response generation time. Th
is makes sense, as a larger input would naturally require more computation to predict the next tokens (at least, that’s 
my assumption).

The issue is that I originally had an agent with two tools, and now I’ve expanded it to four, which has
 significantly increased the response time.

What are some strategies to reduce this response time?

I’ve considered two
 potential solutions:

* The first and simplest approach is to create more agents with fewer tools each, but this would 
also mean that my Router Agent (the one responsible for deciding which agent to use next) would have more tools to evalu
ate, potentially increasing its complexity.
* The second idea, which complicates the flow a bit, is to have the response
 from a tool call go directly to another agent that generates the final response, instead of going back to the same tool
 node. This could eliminate the loop of tool node -> agent with tools -> tool node, and instead streamline the process t
o tool node -> agent without tools.

Has anyone else faced a similar issue or have any suggestions on how to tackle this
?
```
---

     
 
all -  [ Does anyone know how much of a performance difference between knowledge graphs and vector based sear ](https://www.reddit.com/r/LangChain/comments/1eragqk/does_anyone_know_how_much_of_a_performance/) , 2024-08-15-0911
```
I made a pretty simple vector based RAG search, and it performs 'okay' and doesn't always generate the expected results.
 I have the pieces for a knowledge graph, but I was wondering if people knew the expected improvements that I should exp
ect to see by moving to knowledge graphs?
```
---

     
 
all -  [ I built an Agent to Automate Scheduling Calendar Meetings from Emails ](https://www.reddit.com/r/LangChain/comments/1eradtn/i_built_an_agent_to_automate_scheduling_calendar/) , 2024-08-15-0911
```
Hi folks,

I was having problems managing Calendar events, so I decided to build an AI System to manage them for me.

I 
picked LangGraph, considering its recent popularity.

But, the main problem was integrating Gmail and Google Calendar. I
 really had a hard time finding a solution. On top of that, there isn’t a reliable way to fetch new emails from Gmail.


Please feel free to check the [codes that I pushed to the Composio repository](https://dub.composio.dev/lngph).

Here’s 
how I built it.

**Workflow Overview**

* Connect Gmail and Google Calendar with Composio.
* Enable trigger in Composio 
to receive mail.
* Create the AI bot with LangGraph.
* The bot polls Gmail for incoming emails.
* The emails are passed 
to the bot for further analysis.
* If the email contains event scheduling information:
   * Yes: The bot fetches free sl
ots from the Calendar and drafts a suitable email with a scheduled event invitation link.
   * No: Ignores.

https://pre
view.redd.it/meblugry4gid1.png?width=841&format=png&auto=webp&s=bb044a3efafeef984dc9a733b423d04e59a14ff4
```
---

     
 
all -  [ Seeking Ideas to Reduce Token Usage - Langgraph Chatbot ](https://www.reddit.com/r/LangChain/comments/1era5yx/seeking_ideas_to_reduce_token_usage_langgraph/) , 2024-08-15-0911
```
Hello! I am fairly new to LLMs - Langchain/Langgraph. I have implemented a 'Customer Support Chatbot' with three agents,
 one supervisor and two specialized (i used the Customer Support Tutorial as the base of what i have). Each specialized 
have tools that call to APIs to get information to answer to a customer (they only get info, do not execute anything). T
he thing is, the info is quite extensive and i am trying to reduce overall token usage, since it is being stored within 
the State and being passed to each node as input. 

One idea I had was to filter the messages as the first step of each 
chain in every agent node, eliminating the ToolMessages with it's corresponding AIMessage with the tool calls, so that t
he big chunk of info does not enter into the LLMs. But when i do that, i am having troubles if the supervisor makes two 
tool\_calls (delegating to both specialists at the same time) causing errors.

Second idea was to modify the messages wi
thin the state, eliminating the ToolMessage and it's corresponding AIMessage from the state after they were used, but I'
m reading and reading and trying, and can't seem to modifiy the State as it it's being passed through.

So, having that 
context, i ask you, how have you managed the token usage of your implementations, specially if the tool\_calls retrieve 
big chunks of info and also, since it's a chatbot, the idea is that it has some sort of memory of the conversation?

PS:
 Minor details if they are useful for providing me guidance:

-I am using MemorySaver(), 

-The State i am using has thi
s reducer structure

    messages: Annotated[list[AnyMessage], add_messages]
    
```
---

     
 
all -  [ Resume Review. Be brutally honest. Not getting any shortlists.  ](https://i.redd.it/bvadq82zzfid1.jpeg) , 2024-08-15-0911
```
Hello Guys,

I want you guys to be brutally honest. I am not getting call backs. I don’t know what am I doing wrong. Hon
est feedback needed.

Am I applying on wrong platforms. I am trying on linkedin, instahyre and naukri. 
```
---

     
 
all -  [ Chroma how to obtain the embedding function or distance from a collection’s metadata? ](https://www.reddit.com/r/LangChain/comments/1er935w/chroma_how_to_obtain_the_embedding_function_or/) , 2024-08-15-0911
```
Is it possible to obtain the distance function and the embedding function from a Chroma collection metadata definition ?

```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-15-0911
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-15-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-15-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-15-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-15-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
