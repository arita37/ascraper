 
all -  [ We no longer use LangChain for building our AI agents ](https://www.octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents) , 2024-06-21-0910
```

```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/jobsearch/comments/1dklokk/300_applications_30_referrals_innumerable_cold/) , 2024-06-21-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/xultxbc2es7d1.png?width=769&format=png&auto=webp&s=fb197e80ee2e19baa1029daea3ff974
1e307df37


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/recruitinghell/comments/1dkl7sg/300_applications_30_referrals_innumerable_cold/) , 2024-06-21-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/swhg6clias7d1.png?width=769&format=png&auto=webp&s=11dbf7903a6c675f413777297f712ef
5ec7b0e81


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume
 ](https://www.reddit.com/r/leetcode/comments/1dkl5vy/300_applications_30_referrals_innumerable_cold/) , 2024-06-21-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average 10 relevant peop
le) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Science 
graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need so
me guidance.

https://preview.redd.it/s5ozpdv5as7d1.png?width=769&format=png&auto=webp&s=08ccc82058672fb16276e8fa6bdf149
7636290ae


```
---

     
 
all -  [ 300+ applications, 30 referrals, innumerable cold emails, no interview. Need suggestions for resume ](https://www.reddit.com/r/resumes/comments/1dkl3kz/300_applications_30_referrals_innumerable_cold/) , 2024-06-21-0910
```
As the title explains, I have applied to many positions and have reached out to so many people (average of 10 relevant p
eople) for every job that I have applied to. I have not received even a single interview/OA. I am a recent MS Data Scien
ce graduate from an Ivy League university and am looking for only data science positions (DS, ML, DL, CV, NLP, AI). Need
 some guidance.

https://preview.redd.it/myv80x3b9s7d1.png?width=769&format=png&auto=webp&s=dc9e61c4300546235749e02cdbbc
e26cbac593d5


```
---

     
 
all -  [ How to scale a vector database using langchain? Langchain and ChromaDB ](https://www.reddit.com/r/LangChain/comments/1dkkhlb/how_to_scale_a_vector_database_using_langchain/) , 2024-06-21-0910
```
Hi, im new to vector databases and im currently using chroma db with langchain and Azure embeddings for llms, i have bee
n using it for a low ammount of documents, like a few hundreds, but now i have a case where i have to embed 400k documen
ts with 1500 characters each (each is an article of a law).

I managed to compute and index all the embeddings, but as s
oon as i try to load it from the disk (the file is 3.3gb) the docker container fails with an out of memory (its failing 
at 9GB of memory), my questions where:

If my file on disk is 3,3gb, how much RAM memory do i have to have to instantiat
e it? more or less obviously:

def create\_vectorStore():  
embeddings = AzureOpenAIEmbeddings(  
model='text-embedding-
3-small',  
azure\_deployment='text-embedding-3-small',  
openai\_api\_version='2024-02-01',  
)  
     
chromaVectorSto
re = Chroma(  
collection\_name='cv\_collection',  
embedding\_function=embeddings,  
persist\_directory='data/chroma\_v
ector\_store'  
)  
  
record\_manager = SQLRecordManager(  
namespace='chroma/cv\_collection',  
db\_url='sqlite:///rec
ord\_manager\_cache.sql',  
)  
  
record\_manager.create\_schema()  
  
return chromaVectorStore, record\_manager

Does
 it change if i use the [chroma docker container](https://hub.docker.com/layers/chromadb/chroma/latest/images/sha256-0b8
4e8a5d8a9305690a8fd9beba871a3af708bf9cfbae16de839027005798f06)?

Any tips to manage this ammount of data in a vector dat
abase and how to scale it?

Thank you for the responses
```
---

     
 
all -  [ Custom Streamlit-like UI for Langchain Agents ](https://www.reddit.com/r/LangChain/comments/1dkkck6/custom_streamlitlike_ui_for_langchain_agents/) , 2024-06-21-0910
```
Most people know about the UI that Streamlit provides for Langchain Agents, but I am looking for a more custom solution,
 so I can get more control over the UI.

There are some solution like [NLux](https://docs.nlkit.com/nlux) for React, but
 it still does not support agents and tool calling. Does anyone know of any solution? I want to stream and display tool 
calls also along with the LLM outputs. Langserve events streaming looks like a nightmare to develop over.
```
---

     
 
all -  [ How to scale a vector database? ChromaDB ](https://www.reddit.com/r/vectordatabase/comments/1dkkc26/how_to_scale_a_vector_database_chromadb/) , 2024-06-21-0910
```
Hi, im new to vector databases and im currently using chroma db with langchain and Azure embeddings for llms, i have bee
n using it for a low ammount of documents, like a few hundreds, but now i have a case where i have to embed 400k documen
ts with 1500 characters each (each is an article of a law).

I managed to compute and index all the embeddings, but as s
oon as i try to load it from the disk (the file is 3.3gb) the docker container fails with an out of memory (its failing 
at 9GB of memory), my questions where:

If my file on disk is 3,3gb, how much RAM memory do i have to have to instantiat
e it? more or less obviously:

    def create_vectorStore():
        embeddings = AzureOpenAIEmbeddings(
            mod
el='text-embedding-3-small',
            azure_deployment='text-embedding-3-small',
            openai_api_version='2024
-02-01',
        )
       
        chromaVectorStore = Chroma(
            collection_name='cv_collection',
            
embedding_function=embeddings,
            persist_directory='data/chroma_vector_store'
        )
    
        record_ma
nager = SQLRecordManager(
            namespace='chroma/cv_collection',
            db_url='sqlite:///record_manager_cac
he.sql',
        )
    
        record_manager.create_schema()
        
        return chromaVectorStore, record_manager


Does it change if i use the [chroma docker container](https://hub.docker.com/layers/chromadb/chroma/latest/images/sha2
56-0b84e8a5d8a9305690a8fd9beba871a3af708bf9cfbae16de839027005798f06)? 

Any tips to manage this ammount of data in a vec
tor database and how to scale it?

Thank you for the responses
```
---

     
 
all -  [ Create Citations in RAG Streamlit App ](https://www.reddit.com/r/LangChain/comments/1dkjxos/create_citations_in_rag_streamlit_app/) , 2024-06-21-0910
```
Hi all,  
I am creating a streamlit RAG app to allow tech-support agents to get information from service manuals without
 having to read them. I'm using an Azure OpenAI gpt-4o LLM in conjunction with an Azure AI Search retriever. The respons
es I'm getting are good.

I am wanting to implement a feature in the app where each response contains citations to the r
etrieved documents. In an ideal world, the user would be able to click on the citations to bring up the specific pages i
n the service manual PDFs where the retrieved documents are.

I have read the documentations relating to citations ( [ht
tps://python.langchain.com/v0.2/docs/how\_to/qa\_citations/](https://python.langchain.com/v0.2/docs/how_to/qa_citations/
) ), but none of the approaches outlined in the article work for my app. Does anyone have any ideas on how to accomplish
 what I'm trying to do?

For reference, much of my app uses the code in this how-to guide: [https://python.langchain.com
/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/) . For respon
ses to user queries, I am invoking the conversational\_rag\_chain outlined in that guide.
```
---

     
 
all -  [ Roast/Review this Data Scientist CV (2 years+ experience) ](https://i.redd.it/d1igxfafqr7d1.jpeg) , 2024-06-21-0910
```
I've been applying for jobs since start of this year and not getting any response here in India. I moved back from Germa
ny. Please give me pointers to improve my CV.
```
---

     
 
all -  [ Mirascope-Python's Alternative To Langchain
 ](https://www.reddit.com/r/Python/comments/1dkhmpa/mirascopepythons_alternative_to_langchain/) , 2024-06-21-0910
```
Mirascope is a Python library that lets you access a range of Large Language Models, but in a more straightforward and P
ythonic way.

[https://www.i-programmer.info/news/90-tools/17275-mirascope-pythons-alternative-to-langchain.html](https:
//www.i-programmer.info/news/90-tools/17275-mirascope-pythons-alternative-to-langchain.html)
```
---

     
 
all -  [ SQL Agent built with CrewAI, LangChain, Llama Index - Comparing these frameworks ](https://www.reddit.com/r/LocalLLaMA/comments/1dkgo2e/sql_agent_built_with_crewai_langchain_llama_index/) , 2024-06-21-0910
```
The Agent can be used for retrieving data from a database (sqlite) using SQL queries.

* **CrewAI:** Easy development if
 you're good at defining goals and writing backstories for each agent. However, if goals aren't clear, agents can perfor
m unnecessary actions.
* **LangChain:** The best framework for building agents. Creating and importing custom tools is s
traightforward. I had an agent up and running in just an hour.
* **LlamaIndex:** Encountered some errors and found it ch
allenging to define templates and functions properly. Took longer to set up compared to CrewAI or LangChain.

https://i.
redd.it/s9zk5z8car7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master/python/examples/s
ql_agent)

Link for each framework

[CREWAI](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agen
t/sql_agent_plotter_crewai)  
[LANGCHAIN](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/s
ql_agent_plotter_langchain)  
[LLAMAINDEX](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/
sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Parsing fails when streaming ](https://www.reddit.com/r/LangChain/comments/1dkgh71/parsing_fails_when_streaming/) , 2024-06-21-0910
```
Hi, 

I'm using the XMLOutputParser, and it works 90% of the time when not using streaming, but when I do, it fails 2/3 
of the time with a \` Text data outside of root node.\` error.

I've taken a look at the actual text generated and it se
ems to be valid XML, so i'm wondering if the issue could be with the parser instead, of if the first chunk isn't a compl
ete XML tag or something.

Has anyone else faced this issue?

Heres my code for context:



     const model = new ChatA
nthropic({
          temperature: 1,
          model: ANTHROPIC_MODELS.SONNET,
          apiKey: env.ANTHROPIC_API_KEY,

        });
    
        const parser = new XMLOutputParser({
          tags: ['company', 'name', 'year', 'description']
,
        });
    
        const systemMessage = `
          You are an AI assistant tasked with extracting information 
from a document.
          The user will provide you with the text
          You should extract the company name, the ye
ar it was founded and a brief description of the company (a max of 10 words).
          ${parser.getFormatInstructions()
}
    
    
          Example:
          <company>
            <name>Company name</name>
            <year>Year founded<
/year>
            <description>Company description</description>
          </company>
        `;
    
        const pro
mpt = ChatPromptTemplate.fromMessages([
          ['system', systemMessage],
          ['user', text],
        ]);
    

        const chain = prompt.pipe(model).pipe(parser);
    
        const stream = await chain.stream({});
    
        
for await (const chunk of stream) {
          console.log('-------');
          console.log(chunk);
          console.lo
g('-------');
        }


```
---

     
 
all -  [ AI Innovations and Updates: Google AI at CVPR, Groq Incs Panel Discussion, AssemblyAIs API Improveme ](https://www.reddit.com/r/ai_news_by_ai/comments/1dkfwxx/ai_innovations_and_updates_google_ai_at_cvpr_groq/) , 2024-06-21-0910
```





#major_players #event #tool #science #hardware #opensource #startups #feature #release #update #api #leaders #vc #o
pinions #scheduled

Google AI is inviting attendees of the CVPR conference to visit their booth and engage with research
ers working on computer vision innovations. They are hosting a Q&A session on Medical AI Research featuring Azizi Shekoo
feh, an expert in health-related efforts. Google AI's TacticAI, which provides soccer experts and coaches with tactical 
insights, will also be showcased at the conference. Other demonstrations include an on-device text-to-image generation a
pproach using Diffusion GANs by Yang Zhao and OpenMask3D for searching 3D scenes with text queries [1][2][3][4][5].








Groq Inc is reaching out to developers about their LLM apps and is known for its fast AI inference. The company is ho
sting a panel discussion at TPC featuring experts like Tobias Becker, VP of R&D, to discuss designing systems for traini
ng and inference of large next-generation models. Groq Inc's CEO & Founder, Jonathan Ross, unveiled the 5 stages of the 
generative age at CollisionHQ in Toronto. The company is also excited to engage with the developer community at the AI E
ngineer World's Fair event [6][7][8][10][11][14].







AssemblyAI has made various improvements and updates to their A
PI, including support for variable-bitrate videos, billing alerts, and account deletion. The company is now PCI DSS and 
GDPR compliant. They have released new models, such as Universal-1 for multimodal speech recognition and Conformer-2 for
 automatic speech recognition. Pricing has been decreased for Core Transcription and Real-Time Transcription services, a
nd concurrency limits have been increased [15][16].







Generative image models face a tradeoff between realism and d
iversity, where increased realism leads to decreased diversity. The most realistic generative models are mode-collapsed,
 meaning they lack coverage. The author suggests that world models should not be generative but should make predictions 
in representation space to avoid irrelevant information [17][18].







Anthropic is promoting their AI assistant Claud
e 3.5 Sonnet as a tool to maximize efficiency by completing tasks quickly. The company is launching a preview of Artifac
ts on their website, where users can ask Claude to generate various items such as docs, code, diagrams, graphics, and ga
mes. Claude 3.5 Sonnet sets new industry benchmarks for graduate-level reasoning (GPQA), undergraduate-level knowledge (
MMLU), and coding proficiency (HumanEval). The model is available for free on the Claude iOS app and website, and can al
so be accessed through the Anthropic API, Amazon Bedrock, and Google Cloud's Vertex AI [19][22][23][24][25][26][29][30][
31][32][33][34][35][36][37][38][39][40][41].







NVIDIA AI Workbench is a tool that simplifies and optimizes generati
ve AI development. It helps users build custom AI projects, collaborate seamlessly, scale from local to cloud, fine-tune
 models easily, and deploy anywhere [42].







The first episode of Training Data from Sequoia Capital featured a conv
ersation with LangChain's founder, Harrison Chase, discussing the evolution of agents in AI [43].







A new short cou
rse titled 'Function-Calling and Data Extraction with LLMs' has been created to teach how to prompt LLMs to form calls t
o external functions. Participants will work with the NexusRavenV2-13B model to extract structured data from unstructure
d text and access web APIs [44].




[1. Google AI @googleai https://twitter.com/googleai/status/1803481462479659192](ht
tps://twitter.com/googleai/status/1803481462479659192)

[2. Google AI @googleai https://twitter.com/googleai/status/1803
493628528173204](https://twitter.com/googleai/status/1803493628528173204)

[3. Google AI @googleai https://twitter.com/g
oogleai/status/1803510677300236574](https://twitter.com/googleai/status/1803510677300236574)

[4. Google AI @googleai ht
tps://twitter.com/googleai/status/1803528361035309250](https://twitter.com/googleai/status/1803528361035309250)

[5. Goo
gle AI @googleai https://twitter.com/googleai/status/1803545750334492706](https://twitter.com/googleai/status/1803545750
334492706)

[6. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803481863270572271](https://twitter.com/GroqInc/st
atus/1803481863270572271)

[7. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803484019000279333](https://twitter
.com/GroqInc/status/1803484019000279333)

[8. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803488675398885824](
https://twitter.com/GroqInc/status/1803488675398885824)

[9. Groq Inc @GroqInc https://twitter.com/GroqInc/status/180353
3214025191741](https://twitter.com/GroqInc/status/1803533214025191741)

[10. Groq Inc @GroqInc https://twitter.com/GroqI
nc/status/1803536521636516107](https://twitter.com/GroqInc/status/1803536521636516107)

[11. Groq Inc @GroqInc https://t
witter.com/GroqInc/status/1803575502650630572](https://twitter.com/GroqInc/status/1803575502650630572)

[12. Groq Inc @G
roqInc https://twitter.com/GroqInc/status/1803767110520258590](https://twitter.com/GroqInc/status/1803767110520258590)


[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803767234583470571](https://twitter.com/GroqInc/status/180376
7234583470571)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1803779837770801287](https://twitter.com/GroqI
nc/status/1803779837770801287)

[15. AssemblyAI @AssemblyAI https://twitter.com/AssemblyAI/status/1803452005119119754](h
ttps://twitter.com/AssemblyAI/status/1803452005119119754)

[16. AssemblyAI @AssemblyAI https://twitter.com/AssemblyAI/st
atus/1803807825484738971](https://twitter.com/AssemblyAI/status/1803807825484738971)

[17. Yann LeCun @ylecun https://tw
itter.com/ylecun/status/1803677519314407752](https://twitter.com/ylecun/status/1803677519314407752)

[18. Yann LeCun @yl
ecun https://twitter.com/ylecun/status/1803696298068971992](https://twitter.com/ylecun/status/1803696298068971992)

[19.
 Anthropic @anthropicai https://twitter.com/anthropicai/status/1803661178562027822](https://twitter.com/anthropicai/stat
us/1803661178562027822)

[20. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803774865473696237](https:/
/twitter.com/anthropicai/status/1803774865473696237)

[21. Anthropic @anthropicai https://twitter.com/anthropicai/status
/1803776080643322075](https://twitter.com/anthropicai/status/1803776080643322075)

[22. Anthropic @anthropicai https://t
witter.com/anthropicai/status/1803790681971859473](https://twitter.com/anthropicai/status/1803790681971859473)

[23. Ant
hropic @anthropicai https://twitter.com/anthropicai/status/1803790684857536522](https://twitter.com/anthropicai/status/1
803790684857536522)

[24. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803790687382519921](https://twi
tter.com/anthropicai/status/1803790687382519921)

[25. Anthropic @anthropicai https://twitter.com/anthropicai/status/180
3790689408332059](https://twitter.com/anthropicai/status/1803790689408332059)

[26. Anthropic @anthropicai https://twitt
er.com/anthropicai/status/1803790691199336484](https://twitter.com/anthropicai/status/1803790691199336484)

[27. Anthrop
ic @anthropicai https://twitter.com/anthropicai/status/1803791302036795697](https://twitter.com/anthropicai/status/18037
91302036795697)

[28. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803793583666835581](https://twitter
.com/anthropicai/status/1803793583666835581)

[29. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803799
037101134272](https://twitter.com/anthropicai/status/1803799037101134272)

[30. Anthropic @anthropicai https://twitter.c
om/anthropicai/status/1803799688942068047](https://twitter.com/anthropicai/status/1803799688942068047)

[31. Anthropic @
anthropicai https://twitter.com/anthropicai/status/1803799874821058609](https://twitter.com/anthropicai/status/180379987
4821058609)

[32. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803801303606247428](https://twitter.com
/anthropicai/status/1803801303606247428)

[33. Anthropic @anthropicai https://twitter.com/anthropicai/status/18038025189
01940593](https://twitter.com/anthropicai/status/1803802518901940593)

[34. Anthropic @anthropicai https://twitter.com/a
nthropicai/status/1803802679308911072](https://twitter.com/anthropicai/status/1803802679308911072)

[35. Anthropic @anth
ropicai https://twitter.com/anthropicai/status/1803802836977037640](https://twitter.com/anthropicai/status/1803802836977
037640)

[36. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803804434918699365](https://twitter.com/ant
hropicai/status/1803804434918699365)

[37. Anthropic @anthropicai https://twitter.com/anthropicai/status/180380458638764
8866](https://twitter.com/anthropicai/status/1803804586387648866)

[38. Anthropic @anthropicai https://twitter.com/anthr
opicai/status/1803804856832213088](https://twitter.com/anthropicai/status/1803804856832213088)

[39. Anthropic @anthropi
cai https://twitter.com/anthropicai/status/1803805843391164660](https://twitter.com/anthropicai/status/18038058433911646
60)

[40. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803806105052881405](https://twitter.com/anthrop
icai/status/1803806105052881405)

[41. Anthropic @anthropicai https://twitter.com/anthropicai/status/1803806240465887262
](https://twitter.com/anthropicai/status/1803806240465887262)

[42. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com
/NVIDIAAIDev/status/1803805258210050299](https://twitter.com/NVIDIAAIDev/status/1803805258210050299)

[43. Sequoia Capit
al @sequoia https://twitter.com/sequoia/status/1803805945300172985](https://twitter.com/sequoia/status/18038059453001729
85)

[44. Andrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/1803812309460189479](https://twitter.com/AndrewYNg/s
tatus/1803812309460189479)
```
---

     
 
all -  [ Use LangChain with open source LLM to search internet ](https://www.reddit.com/r/LangChain/comments/1dkejk7/use_langchain_with_open_source_llm_to_search/) , 2024-06-21-0910
```
I am using LangChain, a simple agent to search the internet. I am trying everything ReaCT, the problem is that the model
 finds the answer, but then still keeps asking questions by itself and continues a meaningless chain. Whatever I try the
 model when found the answer it thinks it is incorrect or incomplete and keep going. If I do not limit the iterations it
 keep doing without stopping. I do not want to use OpenAI, I have tried also Mistral but with similar results. If you kn
ow a better model, or way to do, I will be really thankful

  


`from transformers import AutoModelForCausalLM, AutoTok
enizer, pipeline`

`from langchain_huggingface import HuggingFacePipeline`

`from langchain.agents import load_tools, Ag
entExecutor, initialize_agent`

`from langchain_core.prompts import PromptTemplate`

,`# Load the model and tokenizer`


`model_id = 'microsoft/Phi-3-mini-4k-instruct'`

`tokenizer = AutoTokenizer.from_pretrained(model_id)`

`model = AutoMod
elForCausalLM.from_pretrained(`

`model_id,`

`load_in_4bit=True,`

`)`

`# Define the text generation pipeline using Hu
ggingFace transformers`

`pipe = pipeline('text-generation', model=model,` 

`tokenizer=tokenizer, max_new_tokens=500,` 


`top_k=50, temperature=0.1,` 

`do_sample=True)`

`# Wrap the pipeline in a HuggingFacePipeline object`

`llm = Huggin
gFacePipeline(pipeline=pipe)`

`# Load the necessary tools`

`tools = load_tools(['ddg-search'], llm=llm)`

`# Define th
e prompt template with explicit stop instructions`

`template = '''Answer the following question as best as you can. You
 have access to the following tools:`

`{tools}`

`Use the following format:`

`Question: {input}`

`Thought: You should
 think about what action to take`

`Action: the action to take, should be one of [{tool_names}]`

`Action Input: the inp
ut to the action`

`Observation: the result of the action`

`Thought: I now know the final answer`

`Final Answer: the f
inal answer to the original input question`

`Do not answer/ask any other questions.`

`Once got the information provide
 the Final Answer.`

`please, stop once you have provided the Final Answer.`

`Begin!`

`Question: {input}`

`'''`

`# C
reate a PromptTemplate from the template`

`prompt = PromptTemplate.from_template(template)`

`# Initialize the agent us
ing initialize_agent`

`agent = initialize_agent(`

`tools=tools,`

`llm=llm,`

`agent='zero-shot-react-description',`


`prompt=prompt,`

`verbose=True,`

`handle_parsing_errors=True,`

`max_iterations=1,`

`stop_sequence='Final Answer:'` 


`)`

`# Define the query`

`query = 'What is the capital of France?'`

`# Execute the query`

`response = agent.run(que
ry)`

`print(response)`
```
---

     
 
all -  [ Resources for creating new characters ](https://www.reddit.com/r/PapegAI/comments/1dkdj2h/resources_for_creating_new_characters/) , 2024-06-21-0910
```
If you want to create new characters, have a look at these websites with examples of 'system prompts' that do just that:


[https://prompts.chat/](https://prompts.chat/)  
For example:

* Football commentator
* Standup comedian
* Novelist

[
https://huggingface.co/datasets/fka/awesome-chatgpt-prompts](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts
)  
For example:  
- Cyber Security Specialist  
- Life coach  
- Astrologer  
- Baby sitter

[https://github.com/davesh
ap/ChatGPT\_Custom\_Instructions](https://github.com/daveshap/ChatGPT_Custom_Instructions)  
For example:

* Scottish Vi
king bartender
* Thesaurus
* Academic copy reviser
* Captain Picard

[https://github.com/mustvlad/ChatGPT-System-Prompts
/tree/main/prompts](https://github.com/mustvlad/ChatGPT-System-Prompts/tree/main/prompts)  
For example:

* Art apprecia
tion guide
* Movie critic
* Shakespearian pirate

[https://github.com/0xeb/TheBigPromptLibrary/tree/main/CustomInstructi
ons](https://github.com/0xeb/TheBigPromptLibrary/tree/main/CustomInstructions)  
For example:

* Movie guide
* Gandalf
*
 Dream interpreter

[https://openwebui.com/](https://openwebui.com/)  
For example:

* Luigi of Super Mario Bros
* Alien
 artifact text adventure
* Sarah, a virtual girlfriend

More programming and technology development oriented system prom
pts can be found at:

[https://smith.langchain.com/hub](https://smith.langchain.com/hub)  
For example:

* MidJourney pr
ompt generator
* Information extractor
* Newsletter generator
```
---

     
 
all -  [ Roast/Review this Data Scientist CV (2 years+ experience) ](https://i.redd.it/pwyyzk2wkq7d1.jpeg) , 2024-06-21-0910
```
I’ve been applying for jobs since start of this year and not getting any response here in India. I moved back from Germa
ny. Please give me pointers to improve my CV.
```
---

     
 
all -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1dkamiy) , 2024-06-21-0910
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
 
all -  [ Freelance - Eng. Informático jack-of-all-trades ](https://www.reddit.com/r/devpt/comments/1dk75pi/freelance_eng_informático_jackofalltrades/) , 2024-06-21-0910
```
Boas malta.



**TL;DR**: Sou co-fundador e CTO duma empresa bootstrapped com dois anos. As coisas andam lentamente, ten
ho um ordenado muito baixo e então tenho ponderado fazer freelancing/contracting para complementar. Sou full-stack no no
sso produto usando Firebase, NodeJS e Express, React com NextJS e ainda Flask para um AI assistant com Langchain juntame
nte com tudo o resto que é preciso numa empresa (vendas, pitches, gestão de produto, etc., sou um jack-of-all-trades, al
go de que gosto). Marketing é um ponto fraco e daí a seguinte pergunta. **Pergunta**: Como posso potenciar/vender-me com
 este perfil para freelancing/contracting num mercado que parece favorecer principalmente a especialização?



**Backgro
und**: Sou co-fundador e CTO duma empresa (pré-financiamento) recente (é um SaaS) com clientes apenas em PT (para já). I
sto não tem nada de glamoroso. Faço-o porque gosto genuinamente da liberdade e de criar soluções que saem da minha cabeç
a (após validar que o problema é real). A jornada começou há uns 3 anos, mas só há cerca de 2 formámos empresa. Antes di
sso trabalhei noutras empresas como Project Manager, Data Scientist e Developer. No total tenho cerca de 8+ anos de expe
riência. Não fui muito bom a negociar os meus salários anteriores por falta de noção do mercado (ganhei muito mais noção
 com a experiência atual), porque coloquei sempre em primeiro lugar o meu fit com a empresa e projetos, e porque não me 
sei auto-promover.

**Skills**: Tenho Mestrado em Engenharia Informática. Já trabalhei com algumas tecnologias e linguag
ens (comecei com C++ e OpenGL, depois C#, Python para Data Science e ML), gosto de ser owner do que faço (how unexpected
) e tenho formação em Gestão de Produto. Na minha empresa sou um jack-of-all-trades (que adoro, tbh). Além do desenvolvi
mento com Firebase, NodeJS e Express, React com NextJS e Flask com Langchain, hosting e CI/CD em GCP e GitHub, também fa
ço customer discovery, protótipos básicos em Figma, orçamentação, pitches a investidores e de vendas, negociação, algum 
marketing, etc. No fundo, sou capaz de agarrar numa ideia, testar o problema, descobrir necessidades, benefícios e JTBD,
 prototipar e desenvolver um MVP funcional (com no-code ou código). Fui algo detalhado porque poderá ser útil para as pe
rguntas mais abaixo.

**Problema**: Desde há 3 anos (quando comecei a jornada que levou à criação da empresa) que tenho 
recebido um vencimento muito baixo para conseguirmos maximizar o runway. Por vezes os tempos não são fáceis porque esse 
runway é muito curto (chegámos a ter apenas um mês em caixa). Gosto imenso do que estou a fazer, mas tenho ponderado faz
er freelancing ou contracting para retirar pressão da empresa e complementar o meu vencimento até levantarmos uma ronda 
de investimento ou conseguirmos escalar o negócio (pode ainda demorar). Isto permite-me a mim 'respirar' melhor, tanto p
elo meu cashflow subir, como por diversificar as minhas fontes de rendimento. Permite também retirar pressão da empresa 
(a sua existência deixa de estar tão dependente da capacidade de me pagar) e até ter mais liberdade para canalizar os fu
ndos para outras necessidades, em vez de alocar tudo ao meu vencimento. Como desvantagem, naturalmente terei menos tempo
 para dedicar à empresa.

**Pergunta 1**: Qual a melhor abordagem e posicionamento tendo em conta o meu perfil abrangent
e? End-to-end para desenvolvimento e gestão de produto? Focar nas skills técnicas? Focar mais na gestão de produto? Dar 
formação? Aqui estou a tentar questionar o leque de possibilidades.

**Pergunta 2**: Mais uma vez, tendo em conta o meu 
perfil abrangente, a dimensão do nosso mercado em PT é suficiente para algumas das possibilidades? É realista tentar alg
o remoto fora de PT? Qual a melhor forma para chegar aos clientes no modelo (da Pergunta 1) escolhido? Quais os melhores
 canais?



Espero não ser off-topic, mas não encontrei nenhum sub melhor para expor o meu dilema. Se houver, por favor 
indiquem-mo.

Para quem leu tudo, desde já agradeço!
```
---

     
 
all -  [ SSLError when using TavilySearchResults ](https://www.reddit.com/r/LangChain/comments/1dk74g9/sslerror_when_using_tavilysearchresults/) , 2024-06-21-0910
```
Hi. I am facing issue while using the Tavily search tool example in langchain. I get SSLError while invoking the tool. C
an someone guide me to fix this?

Error is SSLError (MaxRetryError...)
```
---

     
 
all -  [ What is better way of creating ReAct agent or are there any alternatives to it? ](https://www.reddit.com/r/LangChain/comments/1dk73vw/what_is_better_way_of_creating_react_agent_or_are/) , 2024-06-21-0910
```
I am using langchain ReAct agent with tools. The thing is there is a lot of wasted effort because the agent want to call
 tools which are not even present. Due to this the agent reaches max iteration without calling the tool which are presen
t. Is there any better way to build these agents? or is there any research on better type of agents for this?
```
---

     
 
all -  [ Has anyone worked with caching in RAG chatbot for production? ](https://www.reddit.com/r/LangChain/comments/1dk70yt/has_anyone_worked_with_caching_in_rag_chatbot_for/) , 2024-06-21-0910
```
Has anyone worked with caching in RAG in production. What database you used? 
```
---

     
 
all -  [ Built an Agent for SQL queries ](https://www.reddit.com/r/LLMDevs/comments/1dk4nue/built_an_agent_for_sql_queries/) , 2024-06-21-0910
```
 [github link](https://github.com/ComposioHQ/composio/tree/master/examples/sql_agent/sql_agent_plotter_langchain)

I bui
lt an agent that writes sql queries for your database, logs it and allows you to plot graphs based on the db. I used Lan
gchain, Composio and GPT-4o. Check it out and would love the feedback
```
---

     
 
all -  [ Seeking Feedback on Denser Retriever for Advanced GenAI RAG Performance ](https://www.reddit.com/r/LangChain/comments/1dk0ukb/seeking_feedback_on_denser_retriever_for_advanced/) , 2024-06-21-0910
```
Hey everyone,

We just launched an exciting project and would love to hear your thoughts and feedback! Here's the scoop:


Project Details:Our open-source initiative focuses on integrating advanced search technologies under one roof. By harn
essing gradient boosting (xgboost) machine learning techniques, we combine Keyword-based searches, Vector databases, and
 Machine Learning rerankers for optimal performance.

Performance Benchmark:According to our tests on the MSMARCO datase
t, Denser Retriever has achieved an impressive 13.07% relative gain in NDCG@10 compared to leading vector search baselin
es of similar model sizes.

Here are the Key Features:

* Github repo:[ Denser Retriever](https://github.com/denser-org/
denser-retriever/tree/main)
* Blog:[ Learn more about Denser Retriever](https://denser.ai/blog/denser-retriever/)
* Docu
mentation:[ Denser Retriever Documentation](https://retriever.denser.ai/)

Looking forward to hear your thoughts.


```
---

     
 
all -  [ Using LangChain vs an agent framework like Phidata for a prototype ](https://www.reddit.com/r/LangChain/comments/1djzh8e/using_langchain_vs_an_agent_framework_like/) , 2024-06-21-0910
```
Hi all! I’m a newbie developer still learning while trying to get an experimental idea off the ground. 

My project invo
lves giving LLMs access to various tools to retrieve data as well as a large vector database. 

I want to get a product 
out as soon as possible while having a scalable codebase for further improvements. I feel like LangChain is much more co
mprehensive and will be useful for improving my application. On the other hand, Phidata make it so easy to create agents
, set up tools and RAG and create multi-agent architectures that I’m leaning towards using it for the first version. 

A
s I’m a beginner, I wanted to get your thoughts on which one I should use to begin with and how to think about stuff lik
e this going forward.

Are there any disadvantages to using such frameworks? Will it cause roadblocks?
```
---

     
 
all -  [ Tips for creating a simple web-based app for my chatbot's logic ](https://www.reddit.com/r/LangChain/comments/1djz34y/tips_for_creating_a_simple_webbased_app_for_my/) , 2024-06-21-0910
```
Hey guys!  
How would you recommend me to approach the frontend and backend side of such an app? I'm done with creating 
the chatbot logic through LangGraph, and now I want to implement said logic in a UI where responses can be displayed in 
a beautiful manner to the user.  
What do you think about the idea of using Streamlit for frontend and FastAPI for backe
nd? Also, regarding the backend, I have found an API called 'LangCorn' that is said to leverage the power of FastAPI, ha
s anyone worked with it before? Would you recommend me using it instead of the traditional FastAPI framework?  
Through 
this combo, will I be able to add functionalities such as auth, memory persistence and streaming tokens?  
Thank you!
```
---

     
 
all -  [ RAG Using LangChain ](https://www.reddit.com/r/LangChain/comments/1djyvwr/rag_using_langchain/) , 2024-06-21-0910
```
Everything looks ok to me from a prompt perspective.. but get this error when using RetrievalQA.invoke  

# argument nee
ds to be of type (SquadExample, dict)

Any Suggestions how to fix this ? thanks!


```
---

     
 
all -  [ Recommendations for Using LLMs in Text Processing Projects ](https://www.reddit.com/r/LangChain/comments/1djyu3k/recommendations_for_using_llms_in_text_processing/) , 2024-06-21-0910
```
Hi, I'm working on a project involving the use of language models (LLMs). I need to perform tasks such as text classific
ation, extraction of sections of interest, entity recognition, and formatting the output in a specific way. From what I'
ve read, I might initially be able to achieve this with FewShots, but given the scope of the project, I think I might ne
ed to do some fine tuning. I might be a bit presumptuous, as I'm just starting to use this technology. Could anyone reco
mmend any tutorials or resources for learning about Langchain and LLMs?
```
---

     
 
all -  [ Broken Tutorial? ](https://www.reddit.com/r/LangChain/comments/1djw5oq/broken_tutorial/) , 2024-06-21-0910
```
I was running through what I thought would be a simple tutorial: [https://python.langchain.com/v0.2/docs/tutorials/chatb
ot/](https://python.langchain.com/v0.2/docs/tutorials/chatbot/), but am having some trouble that seems to indicate they 
have removed a module referenced in the tutorial.

In the section on managing history [https://python.langchain.com/v0.2
/docs/tutorials/chatbot/#managing-conversation-history](https://python.langchain.com/v0.2/docs/tutorials/chatbot/#managi
ng-conversation-history) we are supposed to use this 'trim\_messages' module.  I tried importing as in

>from langchain\
_core.messages import SystemMessage, trim\_messages

and got 

    cannot import name 'trim_messages' from 'langchain_co
re.messages'

. Diving into the API documentation, I noticed that the 'trim\_messages' package doesn't exist.

[https://
api.python.langchain.com/en/latest/core\_api\_reference.html#module-langchain\_core.messages](https://api.python.langcha
in.com/en/latest/core_api_reference.html#module-langchain_core.messages)

This seems like a pretty obvious mistake so I 
assume I'm doing something wrong.   Have any of you got trim\_messages to work? Any help would be appreciated. 
```
---

     
 
all -  [ AI agent with vector store ](https://www.reddit.com/r/n8n/comments/1djugwy/ai_agent_with_vector_store/) , 2024-06-21-0910
```
Hello, i am learning how to use langchain in n8n, i  created an agent and i want this agent to retrieve information from
 a vector store, but it's not possible to connect a vector store in the agents tools, is there a way to connect the vect
or store with the agent?
```
---

     
 
all -  [ Using LangChain in production ](https://www.reddit.com/r/LangChain/comments/1dju7yb/using_langchain_in_production/) , 2024-06-21-0910
```
I just want to ask if someone is already using LangChain in production, which basically means that during the developmen
t process, nothing could stop you from deploying and maintaining it.

I always assumed that LangChain is a project suita
ble for academic projects and/or beginners as a good starting point. And now, since I also suggested it to our team, two
 colleagues are against Langchain because they share the same assumption with me and still stick with it.

I am asking h
ere for arguments pro and con :) thanks!
```
---

     
 
all -  [ Still cant grasp the idea of Langchain with OpenAI Assistant ](https://www.reddit.com/r/LangChain/comments/1djtbtj/still_cant_grasp_the_idea_of_langchain_with/) , 2024-06-21-0910
```
Recently I built a chatbot with OpenAI Assistant API. Its doing what we require it to do which brought me to thinking wh
ats the point of langchain or maybe I dont understand it well.

For example, I have custom knowledge base, I upload it t
o OpenAI Vector Store, connect it to my Assistant and I have a chatbot. Where does langchain come in this?

Or if I uplo
ad my knowledge base to any vector database for example, Pinecone, then connect it with OpenAI API, I'd still get a chat
bot.

Please help me understand langchain on a deeper level.

Would really appreciate this. 
```
---

     
 
all -  [ Is it possible to create a structure like a supervisor-agents relationship with human interaction? ](https://www.reddit.com/r/AutoGenAI/comments/1djt3f2/is_it_possible_to_create_a_structure_like_a/) , 2024-06-21-0910
```
Hi, I'm new to autogen, so far I've managed to make a human-agent interaction

I also made a groupchat with a manager, b
ut all the agents are talking between them and it is not what I am looking for

I need to create a structure where there
 is a manager and there are other two agents, one of them handles DnD information and the other Pathfinder, this an exam
ple, what each agent does is more complex but it is easier to just start with some agents handling certain types of info
rmation

basically if the human writes, the manager will evaluate which agent is better suited to handle whatever the hu
man is inquiring, the human can continue having a chat with the agent, maybe if it is something better suited for the ot
her agent then it will switch to that one

is there a way to accomplish this? the groupchat with the manager seemed prom
ising but I don't know how to make the agents stop talking between them, I have this structure in langchain but I'm expl
oring frameworks like this one
```
---

     
 
all -  [ Best Open Source RE-RANKER for RAG??!! ](https://www.reddit.com/r/LangChain/comments/1djsnov/best_open_source_reranker_for_rag/) , 2024-06-21-0910
```
I am using Cohere reranker right now and it is really good. I want to know if there is anything else which is as good or
 better and open source?
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day!

 ](https://www.reddit.com/r/WebDeveloperJobs/comments/1djskqm/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-21-0910
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models.


The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..



The API will cost just $99! One time payme
nt and you will receive the full system code!



If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day! ](https://www.reddit.com/r/SaaS/comments/1djskbd/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-21-0910
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models.


The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..



The API will cost just **$99!** One time p
ayment and you will receive the full system code!



If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ AI / LLM's in .net ](https://www.reddit.com/r/dotnet/comments/1djmj4x/ai_llms_in_net/) , 2024-06-21-0910
```
Hey. Junior dev here.

I am trying to learn AI, slowly heading towards AI agents orchestration. Probably with SemanticKe
rnel, and ollama / huggingface.

I am wondering what other technologies .net dev's are using for integrating AI / LLM's.


I've found this botsharp project, but i think I'll try SemanticKernel 

Edit : Thanks for the answers, but I'm still g
iga confused. New to AI's.
1) My main goal is to be able to run MANY open LLM's locally (i think models have a type or e
xtension ?) Mainly, narrowed down LLM's like text to image, not generative. Is there a better option than Ollama ? (Emph
asis on MANY LLM's,  i think Ollama supports 1 or 2 types ?)
2) The next part is AI orchestration, i think. To call the 
correct AI agent for a task. Preferably a coding solution, not a low code.

Edit2 : No matter how much I like C# and hat
e python, i decided to learn some python and langchain, for anyone wondering. (It is also available in js, and there are
 bindings for .net too (unofficial) as far as i know)

I am trying to come up with some technology stack and then presen
t it to my seniors.


https://github.com/microsoft/semantic-kernel
https://github.com/SciSharp/BotSharp
```
---

     
 
all -  [ What's the best way to chunk, store and, query extremely large datasets where the data is in a CSV/S ](https://www.reddit.com/r/LangChain/comments/1djm57k/whats_the_best_way_to_chunk_store_and_query/) , 2024-06-21-0910
```
I've looked into completely using Google Big Query to store, embed, and vector search the results since they now offer V
ector Searches

Does anyone have any experience doing this with Google Big Query alone?

Would it be better to just impo
rt the data into something line Pinecone and use LangChain to chunk/query?

Or could I also just use LangChain with Goog
le Big Query?

Also not sure if I should be chunking the data, or how chunking would work if I needed it to be on an ite
m by item basis
```
---

     
 
all -  [ Is there any reason not to use Huggingface and Langchain pipelines? ](https://www.reddit.com/r/LocalLLaMA/comments/1djm0uo/is_there_any_reason_not_to_use_huggingface_and/) , 2024-06-21-0910
```
So i am relatively new to this topic. 
I want to build my own RAG application for testing purposes. I want it to only be
 Python Code.
However, almost every tutorial I am seeing is using Ollama or other software to get the LLM running.

Cant
 this simply be achieved with pure code without any other software?,
```
---

     
 
all -  [ Best practices of data extraction with OpenAI ](https://www.reddit.com/r/OpenAIDev/comments/1djl67m/best_practices_of_data_extraction_with_openai/) , 2024-06-21-0910
```
Hey-

  
I'm working with openAI to use it for data extraction.

I'm running into some issues so curious what the commun
ity has found are best practices.

Questions:  
1. Which is the best model? Also when comparing price tradeoffs?  
2. Ho
w many pieces of information can it extract per corpus?  
3. JSON mode and structured data best practices?

  
About my 
use case:  
1. I'm using gpt-4o and have had pretty good results.  
2. small maybe 5-10 seems to work reliably but more 
than 10 I have had issues with it hallucinating the json structure.  
3. I'm using my own parser but its based on the la
ngchains version. i'm stringify a zod schema and using the prompt from that library.

Curious other peoples experiences.

```
---

     
 
all -  [ Zep Long-term Memory: Free Plan Upgraded to 10K Messages ](https://www.reddit.com/r/LangChain/comments/1djkolz/zep_longterm_memory_free_plan_upgraded_to_10k/) , 2024-06-21-0910
```
Hi all - we received some friendly criticism on this subreddit a while back about Zep's Free Plan limit of 1K messages p
er month. We've heard y'all and have increased the monthly limit 10x to 10K messages. You can sign up here: [https://www
.getzep.com/](https://www.getzep.com/)

We also recently [released a Playground](https://app.getzep.com/playground), all
owing you experiment with Zep's long-term memory features without writing any code.

https://i.redd.it/g2kv7ue7hj7d1.gif


**Getting Started**

1. Learn about [key Zep concepts](https://help.getzep.com/concepts) such as Sessions, Facts, and 
more.
2. Experiment with [Zep in the Playground](https://app.getzep.com/playground) and [learn how to build LLM prompts]
(https://help.getzep.com/building-prompt) with Zep.
3. Install Zep's [Python, TypeScript, or Go SDKs](https://help.getze
p.com/sdks) and add long-term memory to your application.
4. Learn how to use [Zep with LangChain LCEL](https://help.get
zep.com/langchain/overview).

Let me know if you have any questions!

-Daniel
```
---

     
 
all -  [ Apparently Gemini's context caching can cut your LLM cost and latency to half ](https://www.reddit.com/r/LangChain/comments/1djjgia/apparently_geminis_context_caching_can_cut_your/) , 2024-06-21-0910
```
Google just announced Context Caching in the Gemini API — it allows you to store and reuse input tokens for repetitive r
equests.

Many LLM tasks have extensive system prompts laying down instructions and initial context.

If these are cache
d, they wouldn’t have to be encoded all over again every time, saving on costs and latency.

Tokens are cached for a spe
cified duration (TTL), after which they are automatically deleted.

Costs depend on the number of tokens cached and thei
r storage duration, and efficiency would be higher for prompts with context used across many LLM calls.

Docs: [https://
ai.google.dev/gemini-api/docs/caching?lang=python](https://ai.google.dev/gemini-api/docs/caching?lang=python)

You can l
earn more about AI here: [https://linktr.ee/sarthakrastogi](https://linktr.ee/sarthakrastogi)
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-21-0910
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-21-0910
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-21-0910
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-21-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
