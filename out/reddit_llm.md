 
all -  [ Noob here. Help! ](https://www.reddit.com/r/LangChain/comments/17n8cjz/noob_here_help/) , 2023-11-04-0909
```
I manage a small engineering team.  We manage large amounts of text based data and serve it to our consumers via apis an
d real time feeds.   

Our business team made a demo combining some of our data with langchain and came away with a demo
 that shows a chat bot type experience analytic product.   They claim the engineering team is dumb because they didn’t k
now about langchain and were skeptical.  The business team think we need to build a new business around the combination 
of all our data and langchain and believe it is super easy.    

I did like the demo but also know it is not something t
hat anyone would pay for and was made on a tiny set of our data. 

Question:   What should we be worried about when we s
tart to scope this project more deeply?   Remember we have massive and constantly updating real time data, is scaling an
 issue?   How should we approach this?   

Thanks internet strangers.
```
---

     
 
all -  [ Function Calling Delay ](https://www.reddit.com/r/LangChain/comments/17n3ztt/function_calling_delay/) , 2023-11-04-0909
```
So, I have been running some experiments with OpenAI's Function Calling capability and Langchain Agents, and I've recent
ly tried to implement streaming the function calling with \`on\_llm\_new\_token\` and I've noticed a weird behavior. It 
looks like between the first call of \`on\_llm\_start\` and the first time that \`on\_llm\_new\_token\` is called, there
 is a huge delay (\~10s). Then, the entire output suddenly streams out extremely quickly (last token comes out within \~
2s). Has anyone experienced this with Langchain or OpenAI function calling streaming?
```
---

     
 
all -  [ Langchain needs to be rewritten ](https://www.reddit.com/r/LangChain/comments/17n34y9/langchain_needs_to_be_rewritten/) , 2023-11-04-0909
```
I hope the team will take into consideration the idea of refactoring the codebase. There is a significant amount of over
lap, and it appears that some parts of the code are overly engineered and complex but not necessary.

&#x200B;
```
---

     
 
all -  [ Any job boards or similar where people are hiring langchain devs? ](https://www.reddit.com/r/LangChain/comments/17n3268/any_job_boards_or_similar_where_people_are_hiring/) , 2023-11-04-0909
```
Pretty much the title, I've been falling in love with langchain, built a ton of stuff, agents, custom agents, tools, cus
tom tools, wrapper for some classes, retrievers, chat bots, embeddings, vectorial dbs and would love to get a job doing 
this tuff, any pace where I can find this kind of jobs?
```
---

     
 
all -  [ Is there a way to make plots using langchain? ](https://www.reddit.com/r/LangChain/comments/17n1kdg/is_there_a_way_to_make_plots_using_langchain/) , 2023-11-04-0909
```
I’ve been looking at the pandas agent and making queries at a table imported from snowflake. I’m using streamlit for a f
rontend. How can I make a plot? I tried using the agent to make the plot but I always get an output parser error because
 it can only return a json. There are ways to make the output return a formatted json using a modified prompt, but it se
ems to contain wrong data. Do you have a way to make reliable plots from prompting a table?
```
---

     
 
all -  [ Confusion over how to use Llama to generate reports ](https://www.reddit.com/r/LocalLLaMA/comments/17n19kf/confusion_over_how_to_use_llama_to_generate/) , 2023-11-04-0909
```
Hey y'all,

I wanted to ask about implementation of an idea I have - I feel like it's straightforward, but I haven't had
 any luck in my research and now feel more confused than ever on LLMs. 

I want to create an chatbot that, given good sa
mples of reports and the requirements for a new report, can write out the draft of a report. I would like to create a kn
owledge base that includes expert knowledge that would be helpful to writing the reports. I will instantiate a local ins
tance of Llama2 and probably connect it to a frontend using Streamlit. 

I  imagine I need to use some form of either La
ngChain or LlamaIndex to implement RAG, but I am not sure if it's finetuning or RAG at this point. I am lost on how to e
ven approach this problem - I have read tons of articles and documentation, but feel lost. If anyone can provide any ide
as or things I can research to learn this, that'd be awesome. 

Thanks in advance!
```
---

     
 
all -  [ Not able to connect through Azure APIM ](https://www.reddit.com/r/LangChain/comments/17mzucs/not_able_to_connect_through_azure_apim/) , 2023-11-04-0909
```
I want to connect to a GPT4 API through an Azure API Management gateway but I get an issue. I'm trying to connect using 
this code that I found online but I still get no result:  

    llm = AzureOpenAI(         headers={'Ocp-Apim-Subscripti
on-Key': os.environ['OPENAI_API_KEY']},         openai_api_base=APIM_BASE_URL,         model_name=COMPLETION_MODEL,     
    deployment_name=COMPLETION_DEPLOYMENT,         max_tokens=SUMMARY_MAX_TOKENS,         temperature=SUMMARY_TEMPERATUR
E     )

Do you have any idea why it doesn't work ?
```
---

     
 
all -  [ AI — weekly megathread! ](https://www.reddit.com/r/artificial/comments/17mzpm6/ai_weekly_megathread/) , 2023-11-04-0909
```
 **News** provided by [aibrews.com](https://aibrews.com/)

 

1. **Luma AI** introduced ***Genie***, a generative 3D fou
ndation model in research preview. *It’s free during research preview via Discord* \[[*Details*](https://lumalabs.ai/gen
ie)\].
2. **Nous** **Research** released ***Obsidian***, the world's first 3B multi-modal model family pre-trained for 4
 Trillion tokens that runs locally on iPhones. Obsidian competes in benchmarks withWizardLM-13B and GPT4-X-Vicuna 13B an
d is based on CapybaraV1.9 \[[*Details*](https://huggingface.co/NousResearch)\].
3. **Phind** has released a new model *
**Phind Model V7*** that matches and exceeds GPT-4's coding abilities while running 5x faster and having16k context \[[*
Details*](https://www.phind.com/blog/phind-model-beats-gpt4-fast)\].
4. **Runway** released an update for both text to v
ideo and image to video generation with Gen-2, bringing major improvements to both the fidelity and consistency of video
 results \[[*Link*](https://runwayml.com/)\].
5. **Stability AI** announced \[[*Details*](https://stability.ai/blog/stab
ility-ai-enhanced-image-apis-for-business-features)\]:
   1. ***Stable 3D*** (Private Preview): a tool to generate a dra
ft-quality 3D model in minutes, by selecting an image or illustration, or writing a text prompt.
   2. [***Sky Replacer*
**](https://clipdrop.co/real-estate/sky-replacer)***:*** a tool that allows users to replace the color and aesthetic of 
the sky in their original photos with a selection of nine alternatives.
   3. integration of Content Credentials and ***
invisible watermarking*** for images generated via the Stability AI API. 
   4. Stable FineTuning (Private Preview)
6. *
*Hugging Face** released ***Zephyr-7B-β***, a fine-tuned version of Mistral-7B that achieves results similar to Chat Lla
ma 70B in multiple benchmarks and above results in MT bench \[[Details](https://huggingface.co/HuggingFaceH4/zephyr-7b-b
eta) | [*Demo*](https://huggingfaceh4-zephyr-chat.hf.space/)\].
7. **LangChain** launched ***LangChain Templates*** \- a
 collection of easily deployable reference architectures for a wide variety of popular LLM use cases \[[*Details*](https
://github.com/langchain-ai/langchain/tree/master/templates)\].
8. **Nvidia** unveiled ***ChipNeMo***, a specialized 43 b
illion parameter large language model for chip design that can answer general questions related to chip design and write
 short scripts to interface with CAD tools \[[*Details*](https://www.tomshardware.com/news/nvidias-chipnemo-ai-will-help
-design-chips)\].
9. **Together** released ***RedPajama-Data-v2***: an Open dataset with 30 Trillion tokens for training
 Large Language Models. It’s the largest public dataset released specifically for LLM training \[[*Details*](https://tog
ether.ai/blog/redpajama-data-v2)\].
10. **Hugging Face** released ***Distil-Whisper***, a distilled version of Whisper t
hat is 6 times faster, 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets 
\[[*Details*](https://github.com/huggingface/distil-whisper)\].
11. **Google Research** and **Google DeepMind** present 
***MetNet-3***, the first AI weather model to learn from sparse observations and outperform the top operational systems 
up to 24 hours ahead at high resolutions. Google has integrated MetNet-3’s capabilities across its various products \[[*
Details*](https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html)\].
12. **Google DeepMind** and
 **Isomorphic Labs** update on the next generation of ***AlphaFold***: the new model greatly expands coverage of structu
re prediction beyond proteins to other key biomolecular classes. This paves the way for researchers to find novel protei
ns to eventually map biomolecular structures needed to design better drugs \[[*Details*](https://deepmind.google/discove
r/blog/a-glimpse-of-the-next-generation-of-alphafold)\].
13. **Nolano Research** and **EleutherAI** introduced ***Hi-NOL
IN***, first state-of-the-art open-source English-Hindi bilingual model built upon the Pythia model suite \[[*Details*](
https://blog.nolano.ai/Hi-NOLIN/)\].
14. **Google** is rolling out ***Immersive View for Routes*** in 15 cities, startin
g this week along with other AI-powered features in Maps. Immersive view combines Street view, aerial imagery, and live 
information like weather and traffic to give an aerial, photo-realistic preview of your planned Google Maps route \[[*De
tails*](https://www.techradar.com/computing/software/google-maps-gets-a-big-ai-update-here-are-the-5-best-time-saving-fe
atures)\].
15. **Perplexity** announced two new models **pplx-7b-chat** and **pplx-70b-chat**, built on top of open-sour
ce LLMs and fine-tuned for chat. They are available as an alpha release, via Labs and pplx-api \[[*Labs Link*](https://l
abs.perplexity.ai/)\].
16. **SlashNext's** *2023 State of Phishing Report* reveals a 1,265% increase in Phishing Emails 
since the launch of ChatGPT in november 2022, signaling a new era of cybercrime fueled by Generative AI \[[Details](http
s://finance.yahoo.com/news/slashnexts-2023-state-phishing-report-152000834.html)\].
17. **Google** launches generative A
I tools for product imagery to US advertisers and merchants \[[*Details*](https://techcrunch.com/2023/11/01/google-launc
hes-generative-ai-tools-for-product-imagery-to-u-s-advertisers/)\].

#### 🔦 Weekly Spotlight

1. *Three things to know a
bout the White House’s executive order on AI \[*[*Link*](https://www.technologyreview.com/2023/10/30/1082678/three-thing
s-to-know-about-the-white-houses-executive-order-on-ai/)*\].*
2. Developing a game *Angry Pumpkins* using GPT-4 for all 
the coding and Midjourney / DALLE for the graphics \[[*Link*](https://x.com/javilopen/status/1719363262179938401?s=20)\]
.
3. **Chatd**: a desktop application that lets you use a local large language model (Mistral-7B) to chat with your docu
ments. It comes with the local LLM runner packaged in \[[*Link*](https://github.com/BruceMacD/chatd)\].
4. Teachers in I
ndia help Microsoft Research design AI tool for creating great classroom content \[[Link](https://www.microsoft.com/en-u
s/research/blog/teachers-in-india-help-microsoft-research-design-ai-tool-for-creating-great-classroom-content)\]. 

\- -
 -

Welcome to the r/artificial weekly megathread. This is where you can discuss Artificial Intelligence - talk about ne
w models, recent news, ask questions, make predictions, and chat other related topics.

[Click here for discussion start
ers for this thread or for a separate post.](https://www.google.com/search?q=artificial+intelligence&tbm=nws)

Self-prom
o is allowed in these weekly discussions. If you want to make a separate post, please read and go by the rules or you wi
ll be banned.

[Previous Megathreads](https://www.reddit.com/r/artificial/search/?q=author%3Ajaketocake%20megathread&res
trict_sr=1) & [Subreddit revamp and going forward](https://www.reddit.com/r/artificial/comments/120qr4r/psa_rule_2_will_
be_enforced_selfpromotion_is_only/)
```
---

     
 
all -  [ Azure Search vs. Pinecone? ](https://www.reddit.com/r/LangChain/comments/17mxe9t/azure_search_vs_pinecone/) , 2023-11-04-0909
```
I have so far been successful in creating RAG pipeline with nice performing conversational bot with Azure Search Index. 
I was asked to try out Pinecone as vector store instead of Azure Search. (Org wants to reduce costs), So i setup a PoC p
ipeline with Pinecone as vector store. What I am not sure is how to benchmark both vector stores for performance and fin
d limitations of both.

Has anyone performed comparative analyses on the performance of Azure Search Index and PineconeD
B? If so, I'd appreciate shared insights.

Also, I am specially interested in:

1. Indexing speed: How do they compare w
hen it comes to indexing speed, especially when dealing with large datasets?
2. Query performance: How do they fare when
 it comes to executing complex queries?
3. Cost efficiency: Any thoughts on cost-effectiveness relative to performance a
nd capacity?
4. Scalability: How smoothly do they scale up with growing needs?
5. Integration: Are there remarkable diff
erences in integrating each with other common platforms and tools?

Naturally, every use case is unique and introduces i
ts own variables. I would love to hear about your experiences, thoughts, or case studies regarding these two platforms' 
performances in different scenarios.

Thank you in advance for your insights!
```
---

     
 
all -  [ Not able to delete Embeddings of a pdf from a list of uploaded Pdf ](https://www.reddit.com/r/LangChain/comments/17mw6aq/not_able_to_delete_embeddings_of_a_pdf_from_a/) , 2023-11-04-0909
```
def delete\_document\_embeddings\_by\_filename(file\_path, persist\_directory):  
chroma\_db = chromadb.PersistentClient
(path=persist\_directory)  
print(chroma\_db)  
collection = chroma\_db.get\_collection(name='langchain')  
print(collec
tion)  
collection.delete(where={'source': file\_path})  
output of the above code is:-  
<chromadb.api.segment.SegmentA
PI object at 0x7f4948165280>  
name='langchain' id=UUID('8a5e8fff-93a4-49f3-8be7-5aac47cb3902') metadata=None  
And I am
 calling like this  
persist\_directory=f'/home/hs/CustomBot/chroma-databases/{formatted\_project\_name}'  
file=/home/h
s/CustomBot/media/project/Code\_of\_Conduct\_Policy.pdf  
delete\_document\_embeddings\_by\_filename(file, persist\_dire
ctory)  
Still not able to delete embeddings of a pdf from the embeddings folder
```
---

     
 
all -  [ DialoGPT + RAG ](https://www.reddit.com/r/huggingface/comments/17mv04p/dialogpt_rag/) , 2023-11-04-0909
```
Has anyone tried using langchain to apply RAG on DialoGPT? I have project in mind to I wanted to try to out I already di
d a similar project using AzureOpenAI but I'm not sure on how to implement it using Dialo 

Thank you
```
---

     
 
all -  [ Adding chunks to documents ](https://www.reddit.com/r/LangChain/comments/17muwii/adding_chunks_to_documents/) , 2023-11-04-0909
```
I am wondering if anyone has a fix for this problem. I am RAGing a set of documents that are often updated. I would like
 to reuse chunks so I hash them and compare to original. but if i get a large insertion in a document it will identify t
he whole doc after the change as modified. id like to just create chunks for the new part and move the remainder. How ar
e you handling changes documents efficiently ?
```
---

     
 
all -  [ Resource Recommendations for Staying Updated on AI Programming Developments? ](https://www.reddit.com/r/LangChain/comments/17mtqil/resource_recommendations_for_staying_updated_on/) , 2023-11-04-0909
```
Hello community, I've been making an effort to stay current with the latest developments in AI, particularly those relev
ant to programming. My interests lean more towards RAG tactics, Langchain, and similar topics, rather than AI in general
. Here are the resources I frequently use:

Reddit:

* Chatgptcoding: [https://www.reddit.com/r/ChatGPTCoding/](https://
www.reddit.com/r/ChatGPTCoding/)
* Langchain (ofcourse)
* ChatGPTPro: [https://www.reddit.com/r/ChatGPTPro/](https://www
.reddit.com/r/ChatGPTPro/)

YouTube:

* Sam Witteveen: [channel link](https://www.youtube.com/@samwitteveenai)
* James B
riggs: [channel link](https://www.youtube.com/@jamesbriggs)

Websites:  
\- [medium.com](https://medium.com) 

I'm wonde
ring if there might be other essential resources I'm missing out on. Could you recommend any other platforms or individu
als that could help me stay updated? Thank you!
```
---

     
 
all -  [ How to chunk tokenized data into two steps? ](https://www.reddit.com/r/LangChain/comments/17mszqf/how_to_chunk_tokenized_data_into_two_steps/) , 2023-11-04-0909
```
I have used RecursiveCharacterTextSplitter and Chroma (for vectorstore) but they are pretty base use. Is there a way I c
an achieve my tasks using LangChain functionality?based on 2 steps: 1st based on the tokens, then on chunk\_size (for ex
ample = 500 and overlap = 50) but only within the chunks from the first step.  For example: \[PART\]Summer is long gone.
\[\\PART\]\[PART\]I am a soccer fan. My favorite team is Real Madrid. But I also like the Italian Milan.\[\\PART\].  
So
 the chunks will be 1. Summer is long gone. and 2. I am a soccer fan ...  
But then I have the second step to use a spli
tter to split into chunks with some overlap. This part has to happen separately for 1 and 2.

I have used RecursiveChara
cterTextSplitter and Chroma (for vectorstore) but they are pretty base use. Is there a way I can achieve my tasks using 
LangChain functionality.
```
---

     
 
all -  [ ConversationalRetrievalAgent with local LLM ](https://www.reddit.com/r/LangChain/comments/17mrxbq/conversationalretrievalagent_with_local_llm/) , 2023-11-04-0909
```
Hi,

Just wondering if local LLM is supported? I am trying to build a basic chatbot with CRA function but it keeps getti
ng errors. fro the docs, I changed the chatmodel OpenAI into a local LLM (llamacpp) but it has errors. are local llms no
t supported yet? Thanks!
```
---

     
 
all -  [ Agent Hitting Token Limit ](https://www.reddit.com/r/LangChain/comments/17mpxr9/agent_hitting_token_limit/) , 2023-11-04-0909
```
I have an agent that is allowed to continue researching until it is ready to provide an answer. The issue isn't in any g
iven prompt or response - it just accumulates over time which i want to happen.

However, if it accumulates too much and
 exceeds the token limit, it will just crash.

I would like it to throw an error and continue onto the next row in my CS
V or to summarize the previous results, pass those back in, and continue where it left off. The agent's job is to valida
te claims in a response so ideally would pass back the claims it has validated and the claims it has left to validate. S
pecific python code would be super helpful here.
```
---

     
 
all -  [ Anyone know how to run a RetrievalQA in a for loop to iterate through 100 prompts (for testing a RAG ](https://www.reddit.com/r/LLMDevs/comments/17mndet/anyone_know_how_to_run_a_retrievalqa_in_a_for/) , 2023-11-04-0909
```
I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab notebook. However
 the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyonoe have experience running mul
tiple prompts?

**Chain:**

RetrievalQA.from\_chain\_type(

llm=llm,

chain\_type='stuff',

retriever=docsearch.as\_retr
iever(search\_kwargs={'k': num\_retrieved\_documents})

&#x200B;

**Note I'm paying for OpenAI (like 30 dollars) and am 
using a free pinecone index as the vector DB; plus just running this in a notebook for testing.**

&#x200B;

**More info
 just came up I've seen two errors pop up once I left things to run for about 30 minutes:**

**First Error::**

WARNING:
langchain.llms.base:Retrying langchain.chat\_models.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_wit
h\_retry in 4.0 seconds as it raised Timeout: Request timed out: HTTPSConnectionPool(host='api.openai.com', port=443): R
ead timed out. (read timeout=600).

**Second Error:**

WARNING:langchain.llms.base:Retrying langchain.chat\_models.opena
i.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_with\_retry in 4.0 seconds as it raised ServiceUnavailableEr
ror: The server is overloaded or not ready yet..

&#x200B;

&#x200B;
```
---

     
 
all -  [ Can I run a chain based on RetrievalQA in a for loop to test out a series of prompts? ](https://www.reddit.com/r/PromptEngineering/comments/17mnccy/can_i_run_a_chain_based_on_retrievalqa_in_a_for/) , 2023-11-04-0909
```
I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab notebook. However
 the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyone have experience running mult
iple prompts?

I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab no
tebook. However the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyonoe have experie
nce running multiple prompts?

  
**Chain:**  
RetrievalQA.from\_chain\_type(  
llm=llm,  
chain\_type='stuff',  
retrie
ver=docsearch.as\_retriever(search\_kwargs={'k': num\_retrieved\_documents})  
**Note I'm paying for OpenAI (like 30 dol
lars) and am using a free pinecone index as the vector DB; plus just running this in a notebook for testing.**  
**More 
info just came up I've seen two errors pop up once I left things to run for about 30 minutes:**  


**First Error::**  

WARNING:langchain.llms.base:Retrying langchain.chat\_models.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_complet
ion\_with\_retry in 4.0 seconds as it raised Timeout: Request timed out: HTTPSConnectionPool(host='api.openai.com', port
=443): Read timed out. (read timeout=600).  
**Second Error:**  
WARNING:langchain.llms.base:Retrying langchain.chat\_mo
dels.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_with\_retry in 4.0 seconds as it raised ServiceUna
vailableError: The server is overloaded or not ready yet..
```
---

     
 
all -  [ Why does OpenAI GPT model from langchain take so long for me, any ideas on hwo to speed it up? ](https://www.reddit.com/r/LLMDevs/comments/17mm3f2/why_does_openai_gpt_model_from_langchain_take_so/) , 2023-11-04-0909
```
i'm passing in around 1000 tokens including a SystemMessage to prime the model to act like a specific role, and a HumanM
essage with my ask. FYI the model I use is GPT-3.5-Turbo

This is taking like 90 seconds and then I tried it again and i
t takes 110 seconds... I don't think it should be taking this long?? I use this at work too through Azure and it's a lot
 faster, like in the matter of a few seconds... Why does this take so much longer, I guess one difference is that I don'
t use the SystemMessage at work usually.

Here are my imports:

from langchain.chat\_models import ChatOpenAI  
from lan
gchain.schema.messages import HumanMessage, SystemMessage

Anyone have any idea how to speed it up?
```
---

     
 
all -  [ Building a Recommendation System for a React Native ](https://www.reddit.com/r/reactnative/comments/17mjqzq/building_a_recommendation_system_for_a_react/) , 2023-11-04-0909
```
 So basically I am a beginner I want to build a React Native application specifically a dating app to practice my skills
 and knowledge I planned on using Supabase as the BE but I am pretty confused on how I would go about building the recom
mendation system so each user can get someone similar to them instead of just randomly showing any user I am thinking ve
ctorizing and doing some stuff like those AI Applications do using Vector DB and Langchain will work but still pretty co
nfused on those also

EDIT: I might need to show why he/she/they/them was recommended maybe based on location, shared in
terest or other things
```
---

     
 
all -  [ Question: Get exact prompt sent to openAI including history and inputs ](https://www.reddit.com/r/LangChain/comments/17min2n/question_get_exact_prompt_sent_to_openai/) , 2023-11-04-0909
```
Hello,

I am working on a chatbot, and have been using langchain to utilize the summarize history feature. Now I am buil
ding a database, that tracks many things that are happening during the dialog like the speakers input, number of words, 
speech emotion recognition, computation time, ram used and other useful meta data. 

The issue that I am running into, i
s I am unable to get the exact prompt, including the history and inputs, and store that data as a string, such that it c
an be stored in the database. 

I am surprised that this is not a trivial task, because it would seem to be fundamental 
to extract the exact data that is being sent to the LLM, as a way to debug, experiment, and store this information. 

Wh
at is odd, is that lang chain prints out the entire prompt that I want:  
'**Entering new ConversationChain chain...** 


Prompt after formatting:...'

I want everything in the 'Prompt after formatting', but cant figure out how to extract th
is as a string, and save store it in a variable in Python. 

I have looked at these resources so far:

[https://github.c
om/langchain-ai/langchain/issues/912](https://github.com/langchain-ai/langchain/issues/912) 

[https://www.reddit.com/r/
LangChain/comments/1643z8k/is\_there\_a\_way\_to\_print\_out\_the\_full\_prompt\_that/](https://www.reddit.com/r/LangCha
in/comments/1643z8k/is_there_a_way_to_print_out_the_full_prompt_that/)

[https://www.perplexity.ai/search/c1ea9c07-baf5-
4fb9-9a62-3353d68f6078?s=mn](https://www.perplexity.ai/search/c1ea9c07-baf5-4fb9-9a62-3353d68f6078?s=mn)

So I have figu
red out how to print it out using the verbose flag, but cannot figure out how to store it as a string in a variable. I h
ave been able to figure out how to save the prompt *without* the inputs and history, but not *with* the inputs and histo
ry. 

Looking for help. 

Thank you
```
---

     
 
all -  [ Source not being mentioned in the final answer ](https://www.reddit.com/r/LangChain/comments/17mikvx/source_not_being_mentioned_in_the_final_answer/) , 2023-11-04-0909
```
Hi all

I am using Langchain for RAG and retrieving documents from a Pinecone DB.

The answer is as follows:

> Entering
 new AgentExecutor chain...
{
    'action': 'Text Retrieval',
    'action_input': 'What is the ethereum blockchain?'
}Th
is is the new answer The Ethereum blockchain is a distributed state machine that tracks the state transitions of a gener
al-purpose data store. It can hold any data expressible as a key-value tuple and is similar to the data storage model of
 Random Access Memory (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in mem
ory over time and can load code into its state machine to run and store resulting state changes.
SOURCES: ../data/PDF/Ma
stering_Ethereum.pdf end
start ['Mastering_Ethereum.pdf'] end

Observation: {'question': 'What is the ethereum blockchai
n?', 'answer': 'The Ethereum blockchain is a distributed state machine that tracks the state transitions of a general-pu
rpose data store. It can hold any data expressible as a key-value tuple and is similar to the data storage model of Rand
om Access Memory (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in memory o
ver time and can load code into its state machine to run and store resulting state changes.\n', 'sources': ['Mastering_E
thereum.pdf'], 'source_documents': [Document(page_content='Ethereum: A General-Purpose Blockchain\nThe original blockcha
in, namely Bitcoin’s blockchain, tracks the state of units of bit‐\ncoin and their ownership. Y ou can think of Bitcoin 
as a distributed consensus state\nmachine , where transactions cause a global state transition , altering the ownership 
of\ncoins. The state transitions are constrained by the rules of consensus, allowing all\nparticipants to (eventually) c
onverge on a common (consensus) state of the system,\nafter several blocks are mined.\nEthereum is also a distributed st
ate machine. But instead of tracking only the state of\ncurrency ownership, Ethereum tracks the state transitions of a g
eneral-purpose data\nstore, i.e., a store that can hold any data expressible as a key–value tuple . A key–value\ndata st
ore holds arbitrary values, each referenced by some key; for example, the value\n“Mastering Ethereum” referenced by the 
key “Book Title” . In some ways, this serves\nthe same purpose as the data storage model of Random Access Memory  (RAM) 
used\nby most general-purpose computers. Ethereum has memory that stores both code\nand data, and it uses the Ethereum b
lockchain to track how this memory changes\nover time. Like a general-purpose stored-program computer, Ethereum can load
 code\ninto its state machine and run that code, storing the resulting state changes in its', metadata={'page': 43.0, 's
ource': '../data/PDF/Mastering_Ethereum.pdf'}), Document(page_content='Ethereum: A General-Purpose Blockchain\nThe origi
nal blockchain, namely Bitcoin’s blockchain, tracks the state of units of bit‐\ncoin and their ownership. Y ou can think
 of Bitcoin as a distributed consensus state\nmachine , where transactions cause a global state transition , altering th
e ownership of\ncoins. The state transitions are constrained by the rules of consensus, allowing all\nparticipants to (e
ventually) converge on a common (consensus) state of the system,\nafter several blocks are mined.\nEthereum is also a di
stributed state machine. But instead of tracking only the state of\ncurrency ownership, Ethereum tracks the state transi
tions of a general-purpose data\nstore, i.e., a store that can hold any data expressible as a key–value tuple . A key–va
lue\ndata store holds arbitrary values, each referenced by some key; for example, the value\n“Mastering Ethereum” refere
nced by the key “Book Title” . In some ways, this serves\nthe same purpose as the data storage model of Random Access Me
mory  (RAM) used\nby most general-purpose computers. Ethereum has memory that stores both code\nand data, and it uses th
e Ethereum blockchain to track how this memory changes\nover time. Like a general-purpose stored-program computer, Ether
eum can load code\ninto its state machine and run that code, storing the resulting state changes in its', metadata={'pag
e': 43.0, 'source': '../data/PDF/Mastering_Ethereum.pdf'})]}
Thought:{
    'action': 'Final Answer',
    'action_input':
 'The Ethereum blockchain is a distributed state machine that tracks the state transitions of a general-purpose data sto
re. It can hold any data expressible as a key-value tuple and is similar to the data storage model of Random Access Memo
ry (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in memory over time and c
an load code into its state machine to run and store resulting state changes.'
}

As you can see, I do have the sources 
associated with my text, and I accurately parse it with the RetrievalQAWithSourcesChain as well ('there's some manual pr
inting here that I did just to verify), but the final answer does not have any mention of the source. Why is that? I hav
e manually checked the _split_sources function in the RetrievalQAWithSourcesChain and it does extract the source and the
n return it along with the answer, but why isn't this being mentioned in the final answer?
```
---

     
 
all -  [ Vector store thought experiment for real world application ](https://www.reddit.com/r/LangChain/comments/17mhwjl/vector_store_thought_experiment_for_real_world/) , 2023-11-04-0909
```
This is a thought experiment I am trying to solve. 

Let’s say that I want an LLM to create the perfect product bundle f
or a given solution the user wants under a specific budget. For example, a solution could be “a university computer lab 
for 50 students under 50k”. An LLM like gpt-4 would most likely find a combination of pcs, monitors, keyboards, etc fair
ly well for the computer lab solution. 

Now let’s say I only want the LLM to be able to select products, though, from a
 product table I have built and to only select compatible products based on another table where I have product compatibi
lity references for different products. 

Would a good use case for vector database and embedding to create a single vec
tor store combining the data for each table and then ask it with the solution I want (the computer lab example above)?
```
---

     
 
all -  [ Styling stream response ](https://www.reddit.com/r/OpenAI/comments/17mh3bh/styling_stream_response/) , 2023-11-04-0909
```
Hey OpenAi community! I’m currently working on a research website where I can put in a question in the search box and it
 gives me points to answer that question:

1. Lorem ipsum

2. Lorem ipsum

For this, I am using gpt 4, langchain, NextJS
, and SerpApi. In my response, at the beginning, I want to include links to the specific sources that were being used.


Brookings    Harvard   University of Utah
…response

However, what is the best way to go over this? I want my links to b
e clickable and look nice. First I was thinking about letting my LLM write it, but that takes too long and is not too pr
etty.

Is there a way to use regex or something similar to insert my stylings?
```
---

     
 
all -  [ SolidGPT integrate with AutoGen, understand your codebase and let Multi-LLMAgent give you the code s ](https://www.reddit.com/r/AutoGenAI/comments/17mgs5f/solidgpt_integrate_with_autogen_understand_your/) , 2023-11-04-0909
```
Hi, Folks I just updated my open-source project - SolidGPT to integrate with AutoGen to improve my AI core power. I try 
to combine the LLMAgent and Chat into one task. Let me know your thoughts, are the LLMAgent and Chat two different ways?


SolidGPTn<>AutoGen. Introducing AutoGen Analysis, engage in issue-focused agent <> chat combination sessions, to get t
he most detailed insights.

Please try my new work: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citiz
en/SolidGPT)

Scan and understand code with LangChain

Analysis requirement and give the response with AutoGen

&#x200B;


https://preview.redd.it/zco8n994p0yb1.png?width=3012&format=png&auto=webp&s=0ff795d3851d643e8fa418df33d9823eada2bce3
```
---

     
 
all -  [ Using GPT-4 and merging LangChain and AutoGen to create a ChatApp which can understand your codebase ](https://www.reddit.com/r/ChatGPT/comments/17mgpuw/using_gpt4_and_merging_langchain_and_autogen_to/) , 2023-11-04-0909
```
Hi, Folks I always have a question, are the LLMAgent and Chat two different ways for AI?

 I just updated my GPT4 dev ch
at app to integrate with AutoGen . I try to combine the LLMAgent and Chat into one task to give the code planbasede on t
he user codebase. Let me know your thoughts, are the LLMAgent and Chat two different ways?

Please try my new work: [htt
ps://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/SolidGPT)

&#x200B;

https://preview.redd.it/j7lustb7
o0yb1.png?width=3012&format=png&auto=webp&s=35d5eb5f123a663e706e8d9e363b0637b4647ec4
```
---

     
 
all -  [ Merging LangChain and AutoGen, understand your codebase and let Multi-LLMAgent give you the code sol ](https://www.reddit.com/r/foss/comments/17mgmnt/merging_langchain_and_autogen_understand_your/) , 2023-11-04-0909
```
Hi, Folks I just updated my open-source project to integrate with AutoGen to improve my AI core power. I try to combine 
the LLMAgent and Chat into one task. Let me know your thoughts, are the LLMAgent and Chat two different ways? 

Merging 
LangChain<>AutoGen. Introducing AutoGen Analysis,  engage in issue-focused agent <> chat combination sessions, to get th
e most detailed insights.  

Please try my new work: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citi
zen/SolidGPT)

Scan and understand code with LangChain

Analysis requirement and give the response with AutoGen 

https:
//preview.redd.it/enmjidzxn0yb1.png?width=3012&format=png&auto=webp&s=39bdf25c2713e26cc64e602c61f9a27c4b498975

&#x200B;

```
---

     
 
all -  [ Building a Recommendation System for a React Native ](https://www.reddit.com/r/react/comments/17mg4xn/building_a_recommendation_system_for_a_react/) , 2023-11-04-0909
```
So basically I am a beginner I want to build a React Native application specifically a dating app to practice my skills 
and knowledge I planned on using Supabase as the BE but I am pretty confused on how I would go about building the recomm
endation system so each user can get someone similar to them instead of just randomly showing any user I am thinking vec
torizing and doing some stuff like those AI Applications do using Vector DB and Langchain will work but still pretty con
fused on those also

EDIT: I might need to show why he/she/they/them was recommended maybe based on location, shared int
erest or other things

&#x200B;
```
---

     
 
all -  [ Any tips on debugging or configuration? ](https://www.reddit.com/r/ollama/comments/17mfdwd/any_tips_on_debugging_or_configuration/) , 2023-11-04-0909
```
1) Ollama rocks

2) See 1 above

Recently started using it and managed to pump a healthy amount of data through Ollama +
 llama2 with URL retrieval  on an MBP with an M2 and GPU, and have been really impressed. 

So tried out using RAG with 
chroma & langchain, and performance has been not so great. 

A single document, using OllamaEmbeddings 

\`\`\`

 'model
' : 'llama2:7b',

 'num\_gpu': 1,

 'num\_thread' : 10

\`\`\`

Doing a bit of profiling \_stream\_with\_aggregation [ht
tps://github.com/langchain-ai/langchain/blob/f66a9d2adfe84ae70bd66d957f153f975a55313e/libs/langchain/langchain/llms/olla
ma.py#L147C1-L148C1](https://github.com/langchain-ai/langchain/blob/f66a9d2adfe84ae70bd66d957f153f975a55313e/libs/langch
ain/langchain/llms/ollama.py#L147C1-L148C1)

Seems to be taking all the cumulative time and activity viewer is only show
ing me ollama-runner with 98% GPU. 

&#x200B;

What should my next steps be in terms of debugging? 

Appreciate any poin
ters
```
---

     
 
all -  [ Synology Chat LLM feedback ](https://www.reddit.com/r/synology/comments/17ma5fm/synology_chat_llm_feedback/) , 2023-11-04-0909
```
I created a thing to use with synology chat, it is a local LLM service where one is the basic talk to a llm and the othe
r uses langchain for memory and wiki Q&A. I would love some feedback and maybe help in ways to improve it.  
[https://gi
thub.com/CaptJaybles/synologyLLM](https://github.com/CaptJaybles/synologyLLM)

[https://github.com/CaptJaybles/SynoLangc
hain](https://github.com/CaptJaybles/SynoLangchain)
```
---

     
 
all -  [ LLM Fun: Building a Q&A Bot of Myself ](https://bjlkeng.io/posts/building-a-qa-bot-of-me-with-openai-and-cloudflare/) , 2023-11-04-0909
```

```
---

     
 
all -  [ My name is Jordy and I just got rickrolled by an AI agent. AMA ](https://i.redd.it/yuzovs6q1zxb1.jpg) , 2023-11-04-0909
```
I was testing it out, asked for a 2 minute cat video, got rickrolled. 

AI has developed a sense of humour before the Ge
rmans did. Chapeau.
```
---

     
 
all -  [ Vote for Cassandra in LangChain integrations. ](https://www.reddit.com/r/cassandra/comments/17m8674/vote_for_cassandra_in_langchain_integrations/) , 2023-11-04-0909
```

1) Go to https://integrations.langchain.com/
2) Sign In with email/GitHub/discord
3) Click Vector Stores filter
4) Pres
s the heart button for *Cassandra*
```
---

     
 
all -  [ Please help! Trying to get ChatGPT to work with multiple PDFs and ePubs (using old Macs running High ](https://www.reddit.com/r/ChatGPTPro/comments/17m7zk4/please_help_trying_to_get_chatgpt_to_work_with/) , 2023-11-04-0909
```
Please help!
I want to write some text, using multiple book-length (200-400 pages) PDFs and ePubs as reference. 
My plan
 was to upload the files, have ChatGPT summarize each chapter, THEN have it cross reference the different source materia
ls that I would upload into each chapter. (The chats themselves would be self-contained; they wouldn’t cross-reference e
ach other.)
I uploaded the first PDF (again, most of my source ebooks are 200-400 pages): ChatGPT said it couldn’t read 
it due to some encoding issue, then suggested that I run it through an OCR. 
Skipping to the end, I finally uploaded a T
XT file, which Chat still claimed it couldn’t work with. 
(The original PDF was 95% text, now it’s just missing a few ch
arts and diagrams, but it’s still mostly intact. So…REALLY?) 
Again: I had wanted to cycle through about a dozen differe
nt chats, with each chat requiring at least a dozen ebooks: the ebooks in the individual chats were supposed to cross-re
ference each other, but each chat is a separate, different beast. 
I’m patient enough to go through the process of reduc
ing each PDF to TXT (although now we’re talking about DOZENS of ebooks that would need to be processed) but what’s the d
eal NOW?! 
I feel like the YouTube tutorials skip a LOT of steps and general info that would be useful. 
BTW, I use 2 In
tel Macs. Both of them are more than 5 years old, and run on High Sierra. I didn’t really have problems uploading, so I’
m guessing the problem is on ChatGPT’s end, and I’m missing something. 
Most of my source material is copyrighted, but b
ecause my computers and OS are old, I can’t use GitHub solutions like Langchain, Quivr, or PrivateGPT (which I was never
, ever told BEFORE I attempted to set them up). 
Thoughts…? Advice…? Please and thank you!
```
---

     
 
all -  [ How should I go about creating a file management system that will be used for an LLM application? ](https://www.reddit.com/r/LangChain/comments/17m5cpf/how_should_i_go_about_creating_a_file_management/) , 2023-11-04-0909
```
I've built a simple LLM application using LangChain which is basically a chatbot that makes use of PDF files that I vect
orize and store in a Pinecone index. What I'm now looking for is a way to build a file management system that enables th
e user to upload new documents that are automatically vectorized. How should I go about building such a system? Is there
 any tools or resources that you can suggest?
```
---

     
 
all -  [ Is LangChain the right tool to solve my problem? ](https://www.reddit.com/r/LangChain/comments/17m4uqw/is_langchain_the_right_tool_to_solve_my_problem/) , 2023-11-04-0909
```
I need the following feature:  
The user will answer a series of questions, and based on that, there will be an output w
ith an analysis and suggestions. That will be shown to the user and saved on the db as reports.   


ChatGPT gives me a 
reasonable output, and I can work with that. The problem is there is no coherence from one output to the other. I want t
o use the previous reports so that if I have the same input, the endpoint returns the same answer, or if there is a slig
ht change in the input, the answer doesn't change drastically. Basically, to take the previous reports as the basis, use
 that and also ChatGPT.

&#x200B;

How can I use LangChain to solve this?  

```
---

     
 
all -  [ Quant Research for the Week ](https://www.reddit.com/r/quant/comments/17m4bjo/quant_research_for_the_week/) , 2023-11-04-0909
```
# ArXiv

Finance

[**Estimating Realized Correlation in High-Frequency Financial Data**](https://arxiv.org/abs/2310.1999
2): A new method for analyzing high-frequency financial data shows that intraday market changes are mainly driven by int
raday correlation changes. (2023-10-30, shares: 5)

[**Agent-based Model for Deep Hedging**](https://arxiv.org/pdf/2310.
18755.pdf): The Chiarella-Heston model, an advanced agent-based model, enhances deep hedging strategies by incorporating
 different types of traders, and performs better in creating realistic financial time series than three other models. (2
023-10-28, shares: 9)

[**Estimating Systemic Risk in Networks**](https://arxiv.org/abs/2310.18658): The article propose
s a two-step nonparametric estimation method for measuring financial systemic risk, showing that only the second step's 
estimation error affects the results. (2023-10-28, shares: 4)

[**Optimal Fees in Hedge Funds with Compensation**](http:
//dx.doi.org/10.1016/j.jbankfin.2020.105884): The research suggests alternative fee schemes for hedge funds, arguing tha
t traditional management and performance fees are suboptimal and that the recommended schemes reduce the fund's volatili
ty. (2023-10-29, shares: 3)

[**Visibility Graph Analysis of Oil Futures Markets**](https://arxiv.org/abs/2310.18903): A
 study using visibility graph methodology examines the effects of the Russia-Ukraine conflict and COVID-19 on crude oil 
futures markets, uncovering distinct market reactions to global disturbances. (2023-10-29, shares: 5)

[**Investing Char
acteristics' Impact on Financial Performance**](http://dx.doi.org/10.1109/ieem44572.2019.8978725): A research study iden
tifies 13 key investment characteristics that contribute to success in the equity market, offering a deeper understandin
g of the necessary traits for success in these markets. (2023-11-01, shares: 5)

[**Corruption's Impact on Performance**
](https://arxiv.org/abs/2310.20028): The study investigates the effect of managerial corruption on company performance, 
emphasizing the need for ethical corporate governance and careful manager selection. (2023-10-30, shares: 4)

[**Charact
erizing Law-Invariant Measures**](https://arxiv.org/abs/2310.19552): The paper introduces new characterizations for law-
invariant star-shaped functionals, demonstrating their wide use in finance, insurance, and probability scenarios. (2023-
10-30, shares: 2)

## Historical Trending

[**Optimal Execution with Machine Learning**](https://arxiv.org/abs/2204.0858
1): A study introduces a numerical algorithm using dynamic programming and deep learning for optimal order execution, hi
ghlighting the convenience of using neural-network substitutes in stochastic control issues. (2022-04-18, shares: 52)

[
**Analysis of Nonlinear Pricing**](https://arxiv.org/abs/2302.11643): A paper proposes a method to calculate the best pr
ice schedule considering consumer diversity in continuous-choice situations, demonstrating that optimal price discrimina
tion can boost a firm's profit by at least 5.5% compared to linear pricing. (2023-02-22, shares: 43)

[**Risk Evaluation
 and Robust Optimization with Model Aggregation**](https://arxiv.org/abs/2201.06370): The model aggregation (MA) approac
h is a new method for risk evaluation that provides a robust value and distributional model, refining Value-at-Risk and 
Expected Shortfall characterizations. (2022-01-17, shares: 33)

[**Deep Reinforcement Learning for Portfolio Management 
Enhancement**](https://arxiv.org/abs/1911.11880): A reinforcement learning framework for portfolio management is introdu
ced, allowing for continuous asset weights, short selling, and decision-making, with three reinforcement learning algori
thms compared for effectiveness. (2019-11-26, shares: 33)

[**Option Valuation on a Credit Index using Levy-driven Ornst
ein-Uhlenbeck Process**](https://arxiv.org/abs/2301.05332): A Levy-driven Ornstein-Uhlenbeck process is proposed to mode
l the risk-free rate and default intensities for evaluating option contracts on a credit index, with derived formulas an
d numerical experiments conducted. (2023-01-12, shares: 27)

[**TabR: Tabular DL Meets Nearest Neighbors**](https://arxi
v.org/abs/2307.14338): TabR, a new deep learning model for tabular data, outperforms existing models by using a k-Neares
t-Neighbors-like component for better predictions. (2023-07-26, shares: 68)

[**Online Estimation & Community Detection 
of Network Point Processes**](https://arxiv.org/abs/2009.01742): The research introduces a fast online variational infer
ence algorithm for estimating latent structure in dynamic event arrivals on a network, offering comparable performance t
o non-online variants with computational benefits. (2020-09-03, shares: 19)

## Crypto & Blockchain

[**NFT Market Fluct
uations: Statistical Properties**](https://arxiv.org/abs/2310.19747?utm_source=dlvr.it&utm_medium=twitter): The study sh
ows that the Non-fungible token (NFT) market, although new and unique in its trading methods, has many statistical simil
arities with traditional financial markets, with some variations in certain quantitative measures. (2023-10-30, shares: 
7)

[**High Frequency Analysis of Bitcoin Volume-Volatility**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=46150
28): Research shows that unexpected trading volume is the key factor in spot volatility in Bitcoin futures and spot mark
ets, while Bitcoin futures volumes have a calming effect on systemic volatility. (2023-10-27, shares: 2.0)

# SSRN

### 
Recently Published

## Quantitative

[**VolGAN: Realistic Volatility Surfaces**](https://papers.ssrn.com/sol3/papers.cfm
?abstract_id=4617536): VolGAN, a new model that can generate realistic scenarios for the joint dynamics of implied volat
ility surfaces and underlying assets, is introduced. (2023-10-30, shares: 173.0)

[**Machine Learning for Earnings Forec
asts**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4619313): Using machine learning models and comprehensive Co
mpustat financial statement data for earnings forecasting can yield predictions that are up to 13% more accurate than tr
aditional linear approaches. (2023-10-31, shares: 7.0)

[**Smart Beta ETFs & Increased Flow Sensitivity to Multi-Factor 
Alphas**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4620486): Smart beta ETFs trading activity significantly i
mpacts mutual fund flow sensitivity, especially in funds with high nonmarket risk factor exposure. (2023-11-01, shares: 
2.0)

[**Google Trends Credit Interest Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618881): The pap
er discusses the use of Google Trends for analyzing credit interest in Armenia, eliminating the need for traditional sur
veys by gathering online search data. (2023-10-31, shares: 2.0)

[**Projected Fuzzy C-Means Algorithm**](https://papers.
ssrn.com/sol3/papers.cfm?abstract_id=4619454): The article proposes a new algorithm for high-dimensional data clustering
 in machine learning, aiming to improve performance and manage anomalous instances. (2023-10-31, shares: 2.0)

[**KMeans
 Initialization**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4616032): The article highlights the role of clus
tering in data mining and machine learning, focusing on the Kmeans algorithm and the challenge of selecting optimal clus
ter centroids. (2023-10-28, shares: 2.0)

## Financial

[**Efficient Heston Model for Climate Contracts**](https://paper
s.ssrn.com/sol3/papers.cfm?abstract_id=4619038): A proposal suggests using Bitcoin-denominated derivatives contracts on 
carbon bonds to help governments hedge against climate change and influence carbon bond and cryptocurrency prices. (2023
-10-31, shares: 3.0)

[**Private Equity Investment & Liquidity Shocks**](https://papers.ssrn.com/sol3/papers.cfm?abstrac
t_id=4615423): Private equity investment outcomes can be influenced by investor composition, with funds from property an
d casualty insurers investing less during natural disasters, resulting in lower returns. (2023-10-27, shares: 3.0)

[**G
reen Derivatives & Climate Risk**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4615427): The EU Green Deal aims 
to make Europe carbon-neutral by 2050, requiring 1 trillion euro in sustainable investments, with derivatives markets an
d 'green derivatives' crucial for managing climate risk. (2023-10-27, shares: 4.0)

[**Time & Frequency Analysis of Oil 
Futures Market**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617533): A study of the oil futures market from 1
986 to 2020 reveals patterns and relationships between inventory, basis, hedging pressure, and futures risk premium, emp
hasizing the importance of the data measurement period. (2023-10-30, shares: 4.0)

[**Art as an Alternative Asset for Di
versification**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617318): Art and collectibles can act as alternati
ve assets for portfolio diversification, with art performing well compared to standard investments and showing a unique 
seasonal pattern in returns. (2023-10-30, shares: 4.0)

[**Indian Mutual Funds Performance Analysis**](https://papers.ss
rn.com/sol3/papers.cfm?abstract_id=4615710): The study examines the performance and risk characteristics of Indian mutua
l funds across market capitalization groups, offering insights for investors and financial professionals. (2023-10-27, s
hares: 2.0)

### Recently Updated

## Quantitative

[**The Common Factor in Volatility Risk Premia**](https://papers.ssr
n.com/sol3/papers.cfm?abstract_id=4618943): Firm-level volatility risk premium has a strong factor structure, with stock
s with the weakest exposures to the common bad volatility risk premium factor earning higher average returns, and the co
mmon factor in total bad volatility risk premium predicting stock market returns. (2023-10-31, shares: 3.0)

[**Batch-St
ochastic Sub-Gradient Method for Non-Smooth Loss Functions**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=461405
1): The new machine learning method, Batchstochastic Subgradient, offers stable loss value estimates and is more memory 
efficient, as demonstrated using SQL. (2023-10-21, shares: 2.0)

[**US. Treasuries: Liquidity Premiums and Results**](ht
tps://papers.ssrn.com/sol3/papers.cfm?abstract_id=4619340): A new model of U.S. Treasuries suggests that liquidity facto
rs are more significant than others, Federal Reserve asset purchases impact expected rates and term premiums, and inflat
ion expectations are less stable than previously thought. (2022-05-06, shares: 2.0)

[**Global Uncertainties and Emergin
g Market Sectors**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618546): A study finds a significant link betwe
en global financial uncertainties and emerging market sectoral indices, based on data from 2008 to 2021. (2023-07-17, sh
ares: 2.0)

## Financial

[**Algorithmic Trading's Influence on Human-Only Markets**](https://papers.ssrn.com/sol3/paper
s.cfm?abstract_id=4620189): The potential existence of algorithmic trading can impact human price predictions, trading a
ctivities, and price dynamics in human-only asset markets, even if no actual algorithmic trading is present. (2023-07-17
, shares: 3.0)

[**Bond Funds and Liquidity Provision**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4614945): C
hanges in regulations have moved profits from liquidity provision in the corporate bond market to mutual funds, increasi
ng volatility and vulnerability to market disruptions like the COVID-19 pandemic. (2023-10-23, shares: 23.0)

[**ETFs an
d Market Efficiency**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4615092): Capital constraints on intermediari
es can affect the pricing efficiency of assets they manage, as seen in ETFs and their lead market makers during the COVI
D-19 debt market disruptions. (2022-03-30, shares: 369.0)

[**ETF Closures: Inaction for Investors?**](https://papers.ss
rn.com/sol3/papers.cfm?abstract_id=4620553): Research indicates smaller ExchangeTraded Funds (ETFs) often yield higher d
aily returns and typically close after positive returns. Investors usually fare better by not reacting to closure announ
cements. (2023-01-23, shares: 60.0)

[**Investor Returns: Market-Based Statistics**](https://papers.ssrn.com/sol3/papers
.cfm?abstract_id=4614148): The study presents three market-based approximations of actual return from market trades, whi
ch deviate from traditional evaluations based on time series analysis of investors' returns. (2023-04-11, shares: 25.0)


[**Cost of Capital: Cross-Sectional Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4620204): Research 
spanning 20 years across multiple countries shows that most variations in perceived capital cost are not supported by su
bsequent returns, questioning the production-based asset pricing model. (2020-12-11, shares: 2.0)

[**Equity and Credit 
Index Options: Risk & Return Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618313): A new credit risk
 model accurately prices equity and credit index options, contradicting previous claims of inconsistent pricing, and hig
hlights the need to balance three systematic risk sources. (2021-07-14, shares: 2.0)

[**Levered ETF Rebalancing: Market
 Volatility Impact**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617640): The study reveals that the interacti
on between investor behavior, ETFs fund flows, and index return autocorrelation can either temper or intensify market vo
latility, as observed during the COVID-19 pandemic onset. (2022-04-08, shares: 2.0)

# RePec

## Machine Learning

[**Ex
plainable AI Reveals Bond Excess Return Determinants**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Flin
k.springer.com%2F10.1007%2Fs11573-023-01149-5;h=repec:spr:jbecon:v:93:y:2023:i:9:d:10.1007_s11573-023-01149-5): The SHap
ley Additive exPlanations technique is used in a paper to identify key factors influencing bond excess return prediction
s made by machine learning models. (2023-11-02, shares: 21.0)

[**Forecasting volatility with machine learning: Panel da
ta perspective**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle
%2Fpii%2FS0927539823000683;h=repec:eee:empfin:v:73:y:2023:i:c:p:251-271): The study uses machine learning to predict vol
atility in high-frequency data, with panel-data-based methods proving most effective. (2023-11-02, shares: 45.0)

[**Cro
ss-market info & stock market volatility prediction**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.
sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS1062940823001006;h=repec:eee:ecofin:v:68:y:2023:i:c:s1062940823001006): A
 study reveals that cross-market information greatly impacts the volatility of the Chinese stock market, especially in m
edium and long-term forecasts. (2023-11-02, shares: 18.0)

## Finance

[**Intraday profitability and trading behavior in
 algorithmic trading: Profitability and behavior in algorithmic trading.**](https://econpapers.repec.org/scripts/redir.p
f?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS0264999323003334;h=repec:eee:ecmode:v:128:y:2023:i:c
:s0264999323003334): The study examines the intraday profitability and interactions among traders, revealing that algori
thmic traders profit while non-algorithmic traders lose, with market volatility causing contrasting trading behaviors. (
2023-11-02, shares: 29.0)

[**Dynamic bond portfolio optimization with a stochastic interest rate model: Bond portfolio 
optimization with stochastic interest rate model.**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Flink.s
pringer.com%2F10.1007%2Fs10690-023-09401-2;h=repec:kap:apfinm:v:30:y:2023:i:4:d:10.1007_s10690-023-09401-2): The paper i
ntroduces a new framework for multi-period dynamic bond portfolio optimization, showing that multi-period optimization o
utperforms single-period optimization, particularly over extended investment and utilization periods. (2023-11-02, share
s: 26.0)

[**Multiperiod portfolio allocation with volatility clustering and non-normalities: Portfolio allocation with 
volatility clustering and non-normalities.**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedi
rect.com%2Fscience%2Farticle%2Fpii%2FS1062940823001201;h=repec:eee:ecofin:v:68:y:2023:i:c:s1062940823001201): The resear
ch investigates the dynamic multiperiod portfolio choices of a U.S. stock market investor, discovering that considering 
volatility clustering decreases hedging demands and non-normalities slightly affect allocations. (2023-11-02, shares: 23
.0)

[**Performance of U.S. ESG ETFs**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fwww.mfa.com.my%2Fw
p-content%2Fuploads%2F2023%2F09%2Fv31_i2_a5_pg89-101.pdf;h=repec:mfa:journl:v:31:y:2023:i:2:p:89-101): A study finds tha
t ESG equity ETFs in the U.S. generally outperform the S&P 500 Index, challenging the notion that ESG investing compromi
ses financial returns. (2023-11-02, shares: 15.0)

[**High-Dimensional Portfolio Optimization with Tree-Structured Facto
rs**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS09
27538X23001774;h=repec:eee:pacfin:v:81:y:2023:i:c:s0927538x23001774): A new portfolio optimization method using a tree-s
tructured portfolio sorting technique predicts stock returns and risk exposures, outperforming benchmark strategies in t
he Chinese A-share market. (2023-11-02, shares: 15.0)

[**Volatility Smile in Emerging Markets: Dynamic Approach**](http
s://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fdoi.org%2F10.1002%2Ffut.22450;h=repec:wly:jfutmk:v:43:y:2023:i
:11:p:1615-1644): A study shows the Dynamic Nelson-Siegel model is more effective than static models for predicting vola
tility in options markets. (2023-11-02, shares: 23.0)

[**Bond-Commodity Volatility Spillover & Global Liquidity Risk**]
(https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fpanoeconomicus.org%2Findex.php%2Fjorunal%2Farticle%2Fview%
2F604%2F761;h=repec:voj:journl:v:70:y:2023:i:1:p:71-100:id:604): Research reveals significant volatility spillovers betw
een gold and bond markets, and oil and some bond markets, suggesting limited diversification benefits for investors. (20
23-11-02, shares: 20.0)

[**fBetas & Portfolio Optimization with f-Divergence Risk Measures**](https://econpapers.repec.
org/scripts/redir.pf?u=http%3A%2F%2Fhdl.handle.net%2F10.1080%2F14697688.2023.2230629;h=repec:taf:quantf:v:23:y:2023:i:10
:p:1483-1496): A new f-Beta for portfolio optimization, which assesses portfolio performance under an optimally disturbe
d market probability measure, offers flexibility and interpretability. (2023-11-02, shares: 18.0)

[**Performance of Act
ively Managed ETFs**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fwww.mfa.com.my%2Fwp-content%2Fupload
s%2F2022%2F10%2Fv30_i2_a3_pg39-61.pdf;h=repec:mfa:journl:v:30:y:2022:i:2:p:39-61): A study from 2018-2021 reveals that a
ctively managed Exchange Traded Funds (ETFs) in the U.S. did not yield significant above-market returns, indicating mana
gers lacked superior market timing skills. (2022-12-23, shares: 18.0)

# GitHub

## Trending

[**FinGAN for Financial Ti
me Series -> FinGAN for Time Series**](https://github.com/milenavuletic/Fin-GAN): This article shares the code related t
o the FinGAN paper, which uses Generative Adversarial Networks for financial time series forecasting and classification.
 (2023-10-26, shares: 16.0)

[**Easy Data Loading with DLT -> Data Loading with DLT**](https://github.com/dlt-hub/dlt): 
The article presents 'data load tool dlt', a Python library that simplifies data loading. (2022-01-26, shares: 669.0)

[
**SolidGPT: Code Collaboration**](https://github.com/AI-Citizen/SolidGPT): The article explores a platform that facilita
tes interaction with your code repository and discussion of coding needs. (2023-08-08, shares: 1369.0)

# LinkedIn

## T
rending

[**VolGAN: A Generative Model for Arbitrage-Free Volatility Surfaces**](https://www.linkedin.com/feed/update/ur
n:li:activity:7124861140286795777): The article presents VolGAN, a generative model for arbitrage-free implied volatilit
y surfaces, and discusses its performance on SPX implied volatility time series. (2023-11-01, shares: 1.0)

[**The New E
ra of Systematic Investing and Parallels to ESG**](https://www.linkedin.com/feed/update/urn:li:activity:7124757870738313
216): The article analyzes Campbell Harvey's views on the role of Machine Learning/AI in investing, discussing potential
 benefits, risks, and its relation to ESG investing. (2023-11-01, shares: 1.0)

[**Quantitative Models in Chinese Stock 
Market**](https://www.linkedin.com/feed/update/urn:li:activity:7125151875129044992): The Chinese stock market's growth a
nd adaptability make it ideal for quantitative models, as discussed at a London forum. (2023-11-01, shares: 1.0)

## Inf
ormative

[**Nasdaq's SEC-Approved AI Order Type**](https://www.linkedin.com/feed/update/urn:li:activity:712508174031801
1392): The U.S. Securities and Exchange Commission has approved Nasdaq's use of an AI-driven order type, the first of it
s kind, for executing orders. (2023-11-01, shares: 1.0)

[**New Paper on Statistical Arbitrage Portfolios**](https://www
.linkedin.com/feed/update/urn:li:activity:7124718120375660544): A new paper on statistical arbitrage portfolio construct
ion based on preference relations has been published by Fredi Šarić, Stjepan Begušić, Andro Merćep and Zvonko Kostanjcar
. (2023-11-01, shares: 1.0)

[**Machine Learning Applications: Tricky Properties and Catastrophic Forgetting**](https://
www.linkedin.com/feed/update/urn:li:activity:7125318036898660352): The article highlights the difficulties in implementi
ng machine learning applications, focusing on issues like 'catastrophic forgetting' and the need for model and data inpu
t adjustments. (2023-11-01, shares: 1.0)

[**Challenging the Belief in More Data for ML Models**](https://www.linkedin.c
om/feed/update/urn:li:activity:7125305960251715584): Clint Howard, in a seminar, challenged the notion that more data us
ed in training machine learning models always results in better performance. (2023-11-01, shares: 1.0)

[**Stock Market 
Efficiency in Pricing Climate Change Risks**](https://www.linkedin.com/feed/update/urn:li:activity:7124830762608021504):
 Man Institute researchers suggest that the stock market often underestimates the impact of climate-related news, creati
ng opportunities for savvy investors. (2023-11-01, shares: 1.0)

[**Common Domain Model (CDM): Revolutionizing Finance**
](https://www.linkedin.com/feed/update/urn:li:activity:7125255238592147457): The Common Domain Model (CDM), an open-sour
ce framework, is transforming finance by standardizing processes and reducing operational risks and costs. (2023-11-01, 
shares: 1.0)

# Podcasts

## Quantitative

[**Scariest Options Strategies Revealed**](http://advisorsoption.libsyn.com/t
he-advisors-option-130-top-5-scariest-options-strategies): The Options Insider Media Group talks about the current marke
t situation, the forthcoming earnings season, and the five most daunting options strategies. (2023-11-01, shares: 8)

[*
*Macro Volatility and Recession Risks with Boris Vladimirov**](https://macrohive.libsyn.com/boris-vladimirov-on-macro-vo
latility-us-yields-and-recession-risks): Goldman Sachs' Boris discusses fiscal policy's impact on growth, private sector
 rate sensitivity changes, and recession odds in a podcast. (2023-10-27, shares: 4)

[**Corey Hoffstein on Bitcoin ETF a
nd TBill Discussion**](https://traffic.megaphone.fm/TIFM8769633628.mp3?updated=1698795275): Corey Hoffstein and Meb disc
uss Bitcoin ETF, BlackRock's TargetDate ETFs, and the end of the 60/40 strategy on a radio show. (2023-11-01, shares: 3)


[**Efficient Use of Graphs with LLMs in GraphText**](https://dataskeptic.com/blog/episodes/2023/graph-text): In a podc
ast, Jianan Zhao, a Computer Science student, talks about the efficient use of graphs with LLMs. (2023-10-31, shares: 2)


[**In-depth Conversation with Traderade Cofounder on MH Ep.**](https://markethuddle.com/podcast/mh/): Kevin and Trader
ade Cofounder Horselover Fat discuss trading setups, Traderade's origins, and experiences in the trading industry. (2023
-10-31, shares: 1)

[**Insights on FOMC Meeting: The Financial Conditions Dummy**](https://ibkrcampus.com/podcasts/ibkr-
podcasts/its-the-financial-conditions-dummy/): Neil Azous from Rareview Capital predicts no further policy tightening ah
ead of the November FOMC meeting. (2023-10-31, shares: 1)

# Twitter

## Quantitative

[**Total Return vs. Derivative In
come in Covered Call Strategies**](https://twitter.com/quantseeker/status/1718676493969006708): Israelov and Ndong's pap
er discusses the inverse relationship between expected total return and derivative income in covered call strategies. (2
023-10-29, shares: 3)

[**Decoding the Volatility Puzzle**](https://twitter.com/quantseeker/status/1718262660926509132):
 Swedroe's article investigates the idiosyncratic volatility puzzle by studying the fundamental aspects. (2023-10-28, sh
ares: 2)

[**SciPhi ΨΦ: Custom Data Generation with LLMs**](https://twitter.com/carlcarrie/status/1718223977292685790): 
The article introduces SciPhi ΨΦ, a system for creating synthetic data to meet specific requirements using LLM-based Ope
nAI Anthropic Llama. (2023-10-28, shares: 2)

[**MS Report on Wealth Management and Generative AI Tipping Point**](https
://twitter.com/carlcarrie/status/1717945102247637161): The report by OliverWynan and MS explores the convergence of weal
th and asset management and the critical point of generative AI. (2023-10-27, shares: 2)

[**Langchain Extensions for Co
ordinated Computation**](https://twitter.com/carlcarrie/status/1719024689110974851): The article presents Permchain and 
Langchain extensions, tools that enable multiple agents to coordinate over several computation steps using LangChain Exp
ression Language and Pregel. (2023-10-30, shares: 0)

## Miscellaneous

[**Large Language Model Inferences on Stock Fact
ors**](https://twitter.com/carlcarrie/status/1717947026430677010): A new study has been released discussing the implicat
ions of Large Language Model on different stock factors. (2023-10-27, shares: 0)

[**China LLM with Advanced Question An
swering Abilities**](https://twitter.com/carlcarrie/status/1718831674862006576): Article 2: DISCFinLLM is a novel Chines
e financial LLM that features multiturn question answering, text processing, mathematical computation, and enhanced retr
ieval generation. (2023-10-30, shares: 0)

[**Abductive Reasoning in Financial Language Model Building**](https://twitte
r.com/carlcarrie/status/1718830111850385462): Article 3: A new financial LLM that uses abductive reasoning surpasses sta
ndard financial LLMs, setting new high scores in financial analysis and interpretation tasks. (2023-10-30, shares: 0)

[
**Python and R Time Series Library**](https://twitter.com/carlcarrie/status/1718780011455361268): Pytimetk is a high-per
formance timeseries library, compatible with Python and R, that utilizes Polaris dataframes for simplicity. (2023-10-30,
 shares: 0)

# Videos

## Quantitative

[**Discovering Supply Chain Edges with Graph Neural Networks**](https://www.yout
ube.com/watch?v=PtzCJvdWdJc): Achintya Gopal from Bloomberg uses graph neural networks to predict unknown suppliers and 
customers, improving supply chain risk analysis. (2023-11-01, shares: 9.0)

[**Where Did All the Quants Go?**](https://w
ww.youtube.com/watch?v=trVhkfwfzPg): A LinkedIn comment criticizes quant programs for lacking intuition and rigor, stres
sing the need for continuous learning and understanding of financial market logic and mathematics. (2023-10-29, shares: 
52.0)

# Reddit

## Quantitative

[**Two Sigma Hedge Fund Scandal**](https://www.reddit.com/r/quant/comments/17j1b1a/wsj
_news_exclusive_hedge_fund_two_sigma_is_hit_by/): The article explores the differences in pay at proprietary trading fir
ms, with some requiring negotiations on a per-portfolio manager basis. (2023-10-29, shares: 230.0)

[**Famous Quants in 
History**](https://www.reddit.com/r/quant/comments/17imr5k/who_arewere_the_most_famousinfluential_quants_of/): The autho
r is asking for suggestions of well-known quants, besides Pat Haber and Martin Artajo, whom they already know. (2023-10-
28, shares: 117.0)

[**Quant Trader in HK or SG**](https://www.reddit.com/r/quant/comments/17jio63/honk_kong_or_singapor
e/): The author is looking for guidance on a potential Quant Trader role in the Asian branches of a London hedge fund, p
articularly in Singapore and Hong Kong. (2023-10-30, shares: 17.0)

[**Million Market Experiment Loss**](https://www.red
dit.com/r/quant/comments/17jj1k2/fastest_way_to_lose_1_million_usd_in_the_quickest/): The author is exploring strategies
 for a hypothetical scenario where all money is lost through market investments as part of an experiment. (2023-10-30, s
hares: 114.0)

# Paper with Code

## Rising

[**Natural Language Graphs**](https://github.com/agiresearch/InstructGLM): 
ChatGPT, a large-scale pretrained language model, has significantly advanced various fields of artificial intelligence r
esearch. (2023-11-01, shares: 117.0)

[**Tuning Graph Instructions for Language Models**](https://github.com/HKUDS/Graph
GPT): GraphGPT uses a graph instruction tuning paradigm to align large language models with graph structural knowledge. 
(2023-10-30, shares: 92.0)

[**Graph-based Tools for Language Model Augmentation**](https://github.com/opengvlab/control
llm): ControlLLM is a new framework that enables large language models to use multimodal tools to tackle complex real-wo
rld tasks. (2023-10-31, shares: 45.0)
```
---

     
 
all -  [ Research of the week (November Week 1) ](https://www.reddit.com/r/u_OppositeMidnight/comments/17m4abb/research_of_the_week_november_week_1/) , 2023-11-04-0909
```
# ArXiv

## Finance

[**Estimating Realized Correlation in High-Frequency Financial Data**](https://arxiv.org/abs/2310.1
9992): A new method for analyzing high-frequency financial data shows that intraday market changes are mainly driven by 
intraday correlation changes. (2023-10-30, shares: 5)

[**Agent-based Model for Deep Hedging**](https://arxiv.org/pdf/23
10.18755.pdf): The Chiarella-Heston model, an advanced agent-based model, enhances deep hedging strategies by incorporat
ing different types of traders, and performs better in creating realistic financial time series than three other models.
 (2023-10-28, shares: 9)

[**Estimating Systemic Risk in Networks**](https://arxiv.org/abs/2310.18658): The article prop
oses a two-step nonparametric estimation method for measuring financial systemic risk, showing that only the second step
's estimation error affects the results. (2023-10-28, shares: 4)

[**Optimal Fees in Hedge Funds with Compensation**](ht
tp://dx.doi.org/10.1016/j.jbankfin.2020.105884): The research suggests alternative fee schemes for hedge funds, arguing 
that traditional management and performance fees are suboptimal and that the recommended schemes reduce the fund's volat
ility. (2023-10-29, shares: 3)

[**Visibility Graph Analysis of Oil Futures Markets**](https://arxiv.org/abs/2310.18903)
: A study using visibility graph methodology examines the effects of the Russia-Ukraine conflict and COVID-19 on crude o
il futures markets, uncovering distinct market reactions to global disturbances. (2023-10-29, shares: 5)

[**Investing C
haracteristics' Impact on Financial Performance**](http://dx.doi.org/10.1109/ieem44572.2019.8978725): A research study i
dentifies 13 key investment characteristics that contribute to success in the equity market, offering a deeper understan
ding of the necessary traits for success in these markets. (2023-11-01, shares: 5)

[**Corruption's Impact on Performanc
e**](https://arxiv.org/abs/2310.20028): The study investigates the effect of managerial corruption on company performanc
e, emphasizing the need for ethical corporate governance and careful manager selection. (2023-10-30, shares: 4)

[**Char
acterizing Law-Invariant Measures**](https://arxiv.org/abs/2310.19552): The paper introduces new characterizations for l
aw-invariant star-shaped functionals, demonstrating their wide use in finance, insurance, and probability scenarios. (20
23-10-30, shares: 2)

## Historical Trending

[**Optimal Execution with Machine Learning**](https://arxiv.org/abs/2204.0
8581): A study introduces a numerical algorithm using dynamic programming and deep learning for optimal order execution,
 highlighting the convenience of using neural-network substitutes in stochastic control issues. (2022-04-18, shares: 52)


[**Analysis of Nonlinear Pricing**](https://arxiv.org/abs/2302.11643): A paper proposes a method to calculate the best
 price schedule considering consumer diversity in continuous-choice situations, demonstrating that optimal price discrim
ination can boost a firm's profit by at least 5.5% compared to linear pricing. (2023-02-22, shares: 43)

[**Risk Evaluat
ion and Robust Optimization with Model Aggregation**](https://arxiv.org/abs/2201.06370): The model aggregation (MA) appr
oach is a new method for risk evaluation that provides a robust value and distributional model, refining Value-at-Risk a
nd Expected Shortfall characterizations. (2022-01-17, shares: 33)

[**Deep Reinforcement Learning for Portfolio Manageme
nt Enhancement**](https://arxiv.org/abs/1911.11880): A reinforcement learning framework for portfolio management is intr
oduced, allowing for continuous asset weights, short selling, and decision-making, with three reinforcement learning alg
orithms compared for effectiveness. (2019-11-26, shares: 33)

[**Option Valuation on a Credit Index using Levy-driven Or
nstein-Uhlenbeck Process**](https://arxiv.org/abs/2301.05332): A Levy-driven Ornstein-Uhlenbeck process is proposed to m
odel the risk-free rate and default intensities for evaluating option contracts on a credit index, with derived formulas
 and numerical experiments conducted. (2023-01-12, shares: 27)

[**TabR: Tabular DL Meets Nearest Neighbors**](https://a
rxiv.org/abs/2307.14338): TabR, a new deep learning model for tabular data, outperforms existing models by using a k-Nea
rest-Neighbors-like component for better predictions. (2023-07-26, shares: 68)

[**Online Estimation & Community Detecti
on of Network Point Processes**](https://arxiv.org/abs/2009.01742): The research introduces a fast online variational in
ference algorithm for estimating latent structure in dynamic event arrivals on a network, offering comparable performanc
e to non-online variants with computational benefits. (2020-09-03, shares: 19)

## Crypto & Blockchain

[**NFT Market Fl
uctuations: Statistical Properties**](https://arxiv.org/abs/2310.19747?utm_source=dlvr.it&utm_medium=twitter): The study
 shows that the Non-fungible token (NFT) market, although new and unique in its trading methods, has many statistical si
milarities with traditional financial markets, with some variations in certain quantitative measures. (2023-10-30, share
s: 7)

[**High Frequency Analysis of Bitcoin Volume-Volatility**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=46
15028): Research shows that unexpected trading volume is the key factor in spot volatility in Bitcoin futures and spot m
arkets, while Bitcoin futures volumes have a calming effect on systemic volatility. (2023-10-27, shares: 2.0)

# SSRN

#
## Recently Published

## Quantitative

[**VolGAN: Realistic Volatility Surfaces**](https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=4617536): VolGAN, a new model that can generate realistic scenarios for the joint dynamics of implied vo
latility surfaces and underlying assets, is introduced. (2023-10-30, shares: 173.0)

[**Machine Learning for Earnings Fo
recasts**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4619313): Using machine learning models and comprehensive
 Compustat financial statement data for earnings forecasting can yield predictions that are up to 13% more accurate than
 traditional linear approaches. (2023-10-31, shares: 7.0)

[**Smart Beta ETFs & Increased Flow Sensitivity to Multi-Fact
or Alphas**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4620486): Smart beta ETFs trading activity significantl
y impacts mutual fund flow sensitivity, especially in funds with high nonmarket risk factor exposure. (2023-11-01, share
s: 2.0)

[**Google Trends Credit Interest Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618881): The 
paper discusses the use of Google Trends for analyzing credit interest in Armenia, eliminating the need for traditional 
surveys by gathering online search data. (2023-10-31, shares: 2.0)

[**Projected Fuzzy C-Means Algorithm**](https://pape
rs.ssrn.com/sol3/papers.cfm?abstract_id=4619454): The article proposes a new algorithm for high-dimensional data cluster
ing in machine learning, aiming to improve performance and manage anomalous instances. (2023-10-31, shares: 2.0)

[**KMe
ans Initialization**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4616032): The article highlights the role of c
lustering in data mining and machine learning, focusing on the Kmeans algorithm and the challenge of selecting optimal c
luster centroids. (2023-10-28, shares: 2.0)

## Financial

[**Efficient Heston Model for Climate Contracts**](https://pa
pers.ssrn.com/sol3/papers.cfm?abstract_id=4619038): A proposal suggests using Bitcoin-denominated derivatives contracts 
on carbon bonds to help governments hedge against climate change and influence carbon bond and cryptocurrency prices. (2
023-10-31, shares: 3.0)

[**Private Equity Investment & Liquidity Shocks**](https://papers.ssrn.com/sol3/papers.cfm?abst
ract_id=4615423): Private equity investment outcomes can be influenced by investor composition, with funds from property
 and casualty insurers investing less during natural disasters, resulting in lower returns. (2023-10-27, shares: 3.0)

[
**Green Derivatives & Climate Risk**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4615427): The EU Green Deal ai
ms to make Europe carbon-neutral by 2050, requiring 1 trillion euro in sustainable investments, with derivatives markets
 and 'green derivatives' crucial for managing climate risk. (2023-10-27, shares: 4.0)

[**Time & Frequency Analysis of O
il Futures Market**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617533): A study of the oil futures market fro
m 1986 to 2020 reveals patterns and relationships between inventory, basis, hedging pressure, and futures risk premium, 
emphasizing the importance of the data measurement period. (2023-10-30, shares: 4.0)

[**Art as an Alternative Asset for
 Diversification**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617318): Art and collectibles can act as altern
ative assets for portfolio diversification, with art performing well compared to standard investments and showing a uniq
ue seasonal pattern in returns. (2023-10-30, shares: 4.0)

[**Indian Mutual Funds Performance Analysis**](https://papers
.ssrn.com/sol3/papers.cfm?abstract_id=4615710): The study examines the performance and risk characteristics of Indian mu
tual funds across market capitalization groups, offering insights for investors and financial professionals. (2023-10-27
, shares: 2.0)

### Recently Updated

## Quantitative

[**The Common Factor in Volatility Risk Premia**](https://papers.
ssrn.com/sol3/papers.cfm?abstract_id=4618943): Firm-level volatility risk premium has a strong factor structure, with st
ocks with the weakest exposures to the common bad volatility risk premium factor earning higher average returns, and the
 common factor in total bad volatility risk premium predicting stock market returns. (2023-10-31, shares: 3.0)

[**Batch
-Stochastic Sub-Gradient Method for Non-Smooth Loss Functions**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=461
4051): The new machine learning method, Batchstochastic Subgradient, offers stable loss value estimates and is more memo
ry efficient, as demonstrated using SQL. (2023-10-21, shares: 2.0)

[**US. Treasuries: Liquidity Premiums and Results**]
(https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4619340): A new model of U.S. Treasuries suggests that liquidity fa
ctors are more significant than others, Federal Reserve asset purchases impact expected rates and term premiums, and inf
lation expectations are less stable than previously thought. (2022-05-06, shares: 2.0)

[**Global Uncertainties and Emer
ging Market Sectors**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618546): A study finds a significant link be
tween global financial uncertainties and emerging market sectoral indices, based on data from 2008 to 2021. (2023-07-17,
 shares: 2.0)

## Financial

[**Algorithmic Trading's Influence on Human-Only Markets**](https://papers.ssrn.com/sol3/pa
pers.cfm?abstract_id=4620189): The potential existence of algorithmic trading can impact human price predictions, tradin
g activities, and price dynamics in human-only asset markets, even if no actual algorithmic trading is present. (2023-07
-17, shares: 3.0)

[**Bond Funds and Liquidity Provision**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4614945)
: Changes in regulations have moved profits from liquidity provision in the corporate bond market to mutual funds, incre
asing volatility and vulnerability to market disruptions like the COVID-19 pandemic. (2023-10-23, shares: 23.0)

[**ETFs
 and Market Efficiency**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4615092): Capital constraints on intermedi
aries can affect the pricing efficiency of assets they manage, as seen in ETFs and their lead market makers during the C
OVID-19 debt market disruptions. (2022-03-30, shares: 369.0)

[**ETF Closures: Inaction for Investors?**](https://papers
.ssrn.com/sol3/papers.cfm?abstract_id=4620553): Research indicates smaller ExchangeTraded Funds (ETFs) often yield highe
r daily returns and typically close after positive returns. Investors usually fare better by not reacting to closure ann
ouncements. (2023-01-23, shares: 60.0)

[**Investor Returns: Market-Based Statistics**](https://papers.ssrn.com/sol3/pap
ers.cfm?abstract_id=4614148): The study presents three market-based approximations of actual return from market trades, 
which deviate from traditional evaluations based on time series analysis of investors' returns. (2023-04-11, shares: 25.
0)

[**Cost of Capital: Cross-Sectional Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4620204): Resear
ch spanning 20 years across multiple countries shows that most variations in perceived capital cost are not supported by
 subsequent returns, questioning the production-based asset pricing model. (2020-12-11, shares: 2.0)

[**Equity and Cred
it Index Options: Risk & Return Analysis**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4618313): A new credit r
isk model accurately prices equity and credit index options, contradicting previous claims of inconsistent pricing, and 
highlights the need to balance three systematic risk sources. (2021-07-14, shares: 2.0)

[**Levered ETF Rebalancing: Mar
ket Volatility Impact**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4617640): The study reveals that the intera
ction between investor behavior, ETFs fund flows, and index return autocorrelation can either temper or intensify market
 volatility, as observed during the COVID-19 pandemic onset. (2022-04-08, shares: 2.0)

# RePec

## Machine Learning

[*
*Explainable AI Reveals Bond Excess Return Determinants**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2F
link.springer.com%2F10.1007%2Fs11573-023-01149-5;h=repec:spr:jbecon:v:93:y:2023:i:9:d:10.1007_s11573-023-01149-5): The S
Hapley Additive exPlanations technique is used in a paper to identify key factors influencing bond excess return predict
ions made by machine learning models. (2023-11-02, shares: 21.0)

[**Forecasting volatility with machine learning: Panel
 data perspective**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farti
cle%2Fpii%2FS0927539823000683;h=repec:eee:empfin:v:73:y:2023:i:c:p:251-271): The study uses machine learning to predict 
volatility in high-frequency data, with panel-data-based methods proving most effective. (2023-11-02, shares: 45.0)

[**
Cross-market info & stock market volatility prediction**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fw
ww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS1062940823001006;h=repec:eee:ecofin:v:68:y:2023:i:c:s1062940823001006)
: A study reveals that cross-market information greatly impacts the volatility of the Chinese stock market, especially i
n medium and long-term forecasts. (2023-11-02, shares: 18.0)

## Finance

[**Intraday profitability and trading behavior
 in algorithmic trading: Profitability and behavior in algorithmic trading.**](https://econpapers.repec.org/scripts/redi
r.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS0264999323003334;h=repec:eee:ecmode:v:128:y:2023:
i:c:s0264999323003334): The study examines the intraday profitability and interactions among traders, revealing that alg
orithmic traders profit while non-algorithmic traders lose, with market volatility causing contrasting trading behaviors
. (2023-11-02, shares: 29.0)

[**Dynamic bond portfolio optimization with a stochastic interest rate model: Bond portfol
io optimization with stochastic interest rate model.**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Flin
k.springer.com%2F10.1007%2Fs10690-023-09401-2;h=repec:kap:apfinm:v:30:y:2023:i:4:d:10.1007_s10690-023-09401-2): The pape
r introduces a new framework for multi-period dynamic bond portfolio optimization, showing that multi-period optimizatio
n outperforms single-period optimization, particularly over extended investment and utilization periods. (2023-11-02, sh
ares: 26.0)

[**Multiperiod portfolio allocation with volatility clustering and non-normalities: Portfolio allocation wi
th volatility clustering and non-normalities.**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.scienc
edirect.com%2Fscience%2Farticle%2Fpii%2FS1062940823001201;h=repec:eee:ecofin:v:68:y:2023:i:c:s1062940823001201): The res
earch investigates the dynamic multiperiod portfolio choices of a U.S. stock market investor, discovering that consideri
ng volatility clustering decreases hedging demands and non-normalities slightly affect allocations. (2023-11-02, shares:
 23.0)

[**Performance of U.S. ESG ETFs**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fwww.mfa.com.my%
2Fwp-content%2Fuploads%2F2023%2F09%2Fv31_i2_a5_pg89-101.pdf;h=repec:mfa:journl:v:31:y:2023:i:2:p:89-101): A study finds 
that ESG equity ETFs in the U.S. generally outperform the S&P 500 Index, challenging the notion that ESG investing compr
omises financial returns. (2023-11-02, shares: 15.0)

[**High-Dimensional Portfolio Optimization with Tree-Structured Fa
ctors**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2F
S0927538X23001774;h=repec:eee:pacfin:v:81:y:2023:i:c:s0927538x23001774): A new portfolio optimization method using a tre
e-structured portfolio sorting technique predicts stock returns and risk exposures, outperforming benchmark strategies i
n the Chinese A-share market. (2023-11-02, shares: 15.0)

[**Volatility Smile in Emerging Markets: Dynamic Approach**](h
ttps://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fdoi.org%2F10.1002%2Ffut.22450;h=repec:wly:jfutmk:v:43:y:202
3:i:11:p:1615-1644): A study shows the Dynamic Nelson-Siegel model is more effective than static models for predicting v
olatility in options markets. (2023-11-02, shares: 23.0)

[**Bond-Commodity Volatility Spillover & Global Liquidity Risk
**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fpanoeconomicus.org%2Findex.php%2Fjorunal%2Farticle%2Fvi
ew%2F604%2F761;h=repec:voj:journl:v:70:y:2023:i:1:p:71-100:id:604): Research reveals significant volatility spillovers b
etween gold and bond markets, and oil and some bond markets, suggesting limited diversification benefits for investors. 
(2023-11-02, shares: 20.0)

[**fBetas & Portfolio Optimization with f-Divergence Risk Measures**](https://econpapers.rep
ec.org/scripts/redir.pf?u=http%3A%2F%2Fhdl.handle.net%2F10.1080%2F14697688.2023.2230629;h=repec:taf:quantf:v:23:y:2023:i
:10:p:1483-1496): A new f-Beta for portfolio optimization, which assesses portfolio performance under an optimally distu
rbed market probability measure, offers flexibility and interpretability. (2023-11-02, shares: 18.0)

[**Performance of 
Actively Managed ETFs**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fwww.mfa.com.my%2Fwp-content%2Fupl
oads%2F2022%2F10%2Fv30_i2_a3_pg39-61.pdf;h=repec:mfa:journl:v:30:y:2022:i:2:p:39-61): A study from 2018-2021 reveals tha
t actively managed Exchange Traded Funds (ETFs) in the U.S. did not yield significant above-market returns, indicating m
anagers lacked superior market timing skills. (2022-12-23, shares: 18.0)

# GitHub

## Trending

[**FinGAN for Financial
 Time Series -> FinGAN for Time Series**](https://github.com/milenavuletic/Fin-GAN): This article shares the code relate
d to the FinGAN paper, which uses Generative Adversarial Networks for financial time series forecasting and classificati
on. (2023-10-26, shares: 16.0)

[**Easy Data Loading with DLT -> Data Loading with DLT**](https://github.com/dlt-hub/dlt
): The article presents 'data load tool dlt', a Python library that simplifies data loading. (2022-01-26, shares: 669.0)


[**SolidGPT: Code Collaboration**](https://github.com/AI-Citizen/SolidGPT): The article explores a platform that facil
itates interaction with your code repository and discussion of coding needs. (2023-08-08, shares: 1369.0)

# LinkedIn

#
# Trending

[**VolGAN: A Generative Model for Arbitrage-Free Volatility Surfaces**](https://www.linkedin.com/feed/update
/urn:li:activity:7124861140286795777): The article presents VolGAN, a generative model for arbitrage-free implied volati
lity surfaces, and discusses its performance on SPX implied volatility time series. (2023-11-01, shares: 1.0)

[**The Ne
w Era of Systematic Investing and Parallels to ESG**](https://www.linkedin.com/feed/update/urn:li:activity:7124757870738
313216): The article analyzes Campbell Harvey's views on the role of Machine Learning/AI in investing, discussing potent
ial benefits, risks, and its relation to ESG investing. (2023-11-01, shares: 1.0)

[**Quantitative Models in Chinese Sto
ck Market**](https://www.linkedin.com/feed/update/urn:li:activity:7125151875129044992): The Chinese stock market's growt
h and adaptability make it ideal for quantitative models, as discussed at a London forum. (2023-11-01, shares: 1.0)

## 
Informative

[**Nasdaq's SEC-Approved AI Order Type**](https://www.linkedin.com/feed/update/urn:li:activity:712508174031
8011392): The U.S. Securities and Exchange Commission has approved Nasdaq's use of an AI-driven order type, the first of
 its kind, for executing orders. (2023-11-01, shares: 1.0)

[**New Paper on Statistical Arbitrage Portfolios**](https://
www.linkedin.com/feed/update/urn:li:activity:7124718120375660544): A new paper on statistical arbitrage portfolio constr
uction based on preference relations has been published by Fredi Šarić, Stjepan Begušić, Andro Merćep and Zvonko Kostanj
car. (2023-11-01, shares: 1.0)

[**Machine Learning Applications: Tricky Properties and Catastrophic Forgetting**](https
://www.linkedin.com/feed/update/urn:li:activity:7125318036898660352): The article highlights the difficulties in impleme
nting machine learning applications, focusing on issues like 'catastrophic forgetting' and the need for model and data i
nput adjustments. (2023-11-01, shares: 1.0)

[**Challenging the Belief in More Data for ML Models**](https://www.linkedi
n.com/feed/update/urn:li:activity:7125305960251715584): Clint Howard, in a seminar, challenged the notion that more data
 used in training machine learning models always results in better performance. (2023-11-01, shares: 1.0)

[**Stock Mark
et Efficiency in Pricing Climate Change Risks**](https://www.linkedin.com/feed/update/urn:li:activity:712483076260802150
4): Man Institute researchers suggest that the stock market often underestimates the impact of climate-related news, cre
ating opportunities for savvy investors. (2023-11-01, shares: 1.0)

[**Common Domain Model (CDM): Revolutionizing Financ
e**](https://www.linkedin.com/feed/update/urn:li:activity:7125255238592147457): The Common Domain Model (CDM), an open-s
ource framework, is transforming finance by standardizing processes and reducing operational risks and costs. (2023-11-0
1, shares: 1.0)

# Podcasts

## Quantitative

[**Scariest Options Strategies Revealed**](http://advisorsoption.libsyn.co
m/the-advisors-option-130-top-5-scariest-options-strategies): The Options Insider Media Group talks about the current ma
rket situation, the forthcoming earnings season, and the five most daunting options strategies. (2023-11-01, shares: 8)


[**Macro Volatility and Recession Risks with Boris Vladimirov**](https://macrohive.libsyn.com/boris-vladimirov-on-macro
-volatility-us-yields-and-recession-risks): Goldman Sachs' Boris discusses fiscal policy's impact on growth, private sec
tor rate sensitivity changes, and recession odds in a podcast. (2023-10-27, shares: 4)

[**Corey Hoffstein on Bitcoin ET
F and TBill Discussion**](https://traffic.megaphone.fm/TIFM8769633628.mp3?updated=1698795275): Corey Hoffstein and Meb d
iscuss Bitcoin ETF, BlackRock's TargetDate ETFs, and the end of the 60/40 strategy on a radio show. (2023-11-01, shares:
 3)

[**Efficient Use of Graphs with LLMs in GraphText**](https://dataskeptic.com/blog/episodes/2023/graph-text): In a p
odcast, Jianan Zhao, a Computer Science student, talks about the efficient use of graphs with LLMs. (2023-10-31, shares:
 2)

[**In-depth Conversation with Traderade Cofounder on MH Ep.**](https://markethuddle.com/podcast/mh/): Kevin and Tra
derade Cofounder Horselover Fat discuss trading setups, Traderade's origins, and experiences in the trading industry. (2
023-10-31, shares: 1)

[**Insights on FOMC Meeting: The Financial Conditions Dummy**](https://ibkrcampus.com/podcasts/ib
kr-podcasts/its-the-financial-conditions-dummy/): Neil Azous from Rareview Capital predicts no further policy tightening
 ahead of the November FOMC meeting. (2023-10-31, shares: 1)

# Twitter

## Quantitative

[**Total Return vs. Derivative
 Income in Covered Call Strategies**](https://twitter.com/quantseeker/status/1718676493969006708): Israelov and Ndong's 
paper discusses the inverse relationship between expected total return and derivative income in covered call strategies.
 (2023-10-29, shares: 3)

[**Decoding the Volatility Puzzle**](https://twitter.com/quantseeker/status/171826266092650913
2): Swedroe's article investigates the idiosyncratic volatility puzzle by studying the fundamental aspects. (2023-10-28,
 shares: 2)

[**SciPhi ΨΦ: Custom Data Generation with LLMs**](https://twitter.com/carlcarrie/status/1718223977292685790
): The article introduces SciPhi ΨΦ, a system for creating synthetic data to meet specific requirements using LLM-based 
OpenAI Anthropic Llama. (2023-10-28, shares: 2)

[**MS Report on Wealth Management and Generative AI Tipping Point**](ht
tps://twitter.com/carlcarrie/status/1717945102247637161): The report by OliverWynan and MS explores the convergence of w
ealth and asset management and the critical point of generative AI. (2023-10-27, shares: 2)

[**Langchain Extensions for
 Coordinated Computation**](https://twitter.com/carlcarrie/status/1719024689110974851): The article presents Permchain a
nd Langchain extensions, tools that enable multiple agents to coordinate over several computation steps using LangChain 
Expression Language and Pregel. (2023-10-30, shares: 0)

## Miscellaneous

[**Large Language Model Inferences on Stock F
actors**](https://twitter.com/carlcarrie/status/1717947026430677010): A new study has been released discussing the impli
cations of Large Language Model on different stock factors. (2023-10-27, shares: 0)

[**China LLM with Advanced Question
 Answering Abilities**](https://twitter.com/carlcarrie/status/1718831674862006576): Article 2: DISCFinLLM is a novel Chi
nese financial LLM that features multiturn question answering, text processing, mathematical computation, and enhanced r
etrieval generation. (2023-10-30, shares: 0)

[**Abductive Reasoning in Financial Language Model Building**](https://twi
tter.com/carlcarrie/status/1718830111850385462): Article 3: A new financial LLM that uses abductive reasoning surpasses 
standard financial LLMs, setting new high scores in financial analysis and interpretation tasks. (2023-10-30, shares: 0)


[**Python and R Time Series Library**](https://twitter.com/carlcarrie/status/1718780011455361268): Pytimetk is a high-
performance timeseries library, compatible with Python and R, that utilizes Polaris dataframes for simplicity. (2023-10-
30, shares: 0)

# Videos

## Quantitative

[**Discovering Supply Chain Edges with Graph Neural Networks**](https://www.y
outube.com/watch?v=PtzCJvdWdJc): Achintya Gopal from Bloomberg uses graph neural networks to predict unknown suppliers a
nd customers, improving supply chain risk analysis. (2023-11-01, shares: 9.0)

[**Where Did All the Quants Go?**](https:
//www.youtube.com/watch?v=trVhkfwfzPg): A LinkedIn comment criticizes quant programs for lacking intuition and rigor, st
ressing the need for continuous learning and understanding of financial market logic and mathematics. (2023-10-29, share
s: 52.0)

# Reddit

## Quantitative

[**Two Sigma Hedge Fund Scandal**](https://www.reddit.com/r/quant/comments/17j1b1a/
wsj_news_exclusive_hedge_fund_two_sigma_is_hit_by/): The article explores the differences in pay at proprietary trading 
firms, with some requiring negotiations on a per-portfolio manager basis. (2023-10-29, shares: 230.0)

[**Famous Quants 
in History**](https://www.reddit.com/r/quant/comments/17imr5k/who_arewere_the_most_famousinfluential_quants_of/): The au
thor is asking for suggestions of well-known quants, besides Pat Haber and Martin Artajo, whom they already know. (2023-
10-28, shares: 117.0)

[**Quant Trader in HK or SG**](https://www.reddit.com/r/quant/comments/17jio63/honk_kong_or_singa
pore/): The author is looking for guidance on a potential Quant Trader role in the Asian branches of a London hedge fund
, particularly in Singapore and Hong Kong. (2023-10-30, shares: 17.0)

[**Million Market Experiment Loss**](https://www.
reddit.com/r/quant/comments/17jj1k2/fastest_way_to_lose_1_million_usd_in_the_quickest/): The author is exploring strateg
ies for a hypothetical scenario where all money is lost through market investments as part of an experiment. (2023-10-30
, shares: 114.0)

# Paper with Code

## Rising

[**Natural Language Graphs**](https://github.com/agiresearch/InstructGLM
): ChatGPT, a large-scale pretrained language model, has significantly advanced various fields of artificial intelligenc
e research. (2023-11-01, shares: 117.0)

[**Tuning Graph Instructions for Language Models**](https://github.com/HKUDS/Gr
aphGPT): GraphGPT uses a graph instruction tuning paradigm to align large language models with graph structural knowledg
e. (2023-10-30, shares: 92.0)

[**Graph-based Tools for Language Model Augmentation**](https://github.com/opengvlab/cont
rolllm): ControlLLM is a new framework that enables large language models to use multimodal tools to tackle complex real
-world tasks. (2023-10-31, shares: 45.0)
```
---

     
 
all -  [ Metadata filtering in Opensearch ](https://www.reddit.com/r/LangChain/comments/17m2vdi/metadata_filtering_in_opensearch/) , 2023-11-04-0909
```
I’m using opensearch as a vector database in a RAG type project. Since I have 10,000s of documents I want to filter firs
t on metadata before the similarity search I was try something along these lines

Retriever=vector_db.as_retriever(searc
h_kwargs={“filter”:{”bool”:{”term”:{“class”:”classA”}}}})

From here:
https://opensearch.org/docs/latest/search-plugins/
knn/filter-search-knn/

But the similarity search ignores the filter. Does anyone have any experience getting something 
like this to work?
```
---

     
 
all -  [ Do you find langsmith useful? Why? ](https://www.reddit.com/r/LangChain/comments/17m2u2d/do_you_find_langsmith_useful_why/) , 2023-11-04-0909
```
For the people who have tried it out, what's your opinion? Is it actually useful?
```
---

     
 
all -  [ Best framework for LLM based applications in production ](https://www.reddit.com/r/LocalLLaMA/comments/17m2lql/best_framework_for_llm_based_applications_in/) , 2023-11-04-0909
```
We've been building LLM based tools for months, but I think that there should be efficient frameworks by now that actual
ly add value. I tried langchain a while back but I felt like it was just an over complicated overhead where it was alway
s simpler to make everything from scratch each time. Guidance has been the only real improvement for me as it does way m
ore than basic prompt templating, but it is in no way a full framework.

Now there are LlamaIndex, TigerLab, Langchain..
. but I simply don't have the time to test them all.

We need to run the models by ourselves, so no Open AI api, ideally
 run something compatible with TGI / VLLM. We need to connect to proper databases and vectorDB (currently using Milvus).
 And I'm looking for something that is actually useful and I don't have to struggle and hack the library everytime I wan
t to do something slightly different.

Does any of you have a good recommendation? Everything changes so quickly I feel 
like I can't trust articles that are older than two months. So what are you currently using and what has been an overhyp
ed crap? 
```
---

     
 
all -  [ AimOS: Open-source modular observability for AI Systems ](https://www.reddit.com/r/mlops/comments/17m2c90/aimos_opensource_modular_observability_for_ai/) , 2023-11-04-0909
```
Hey folks! Tatyana from Aim here, AI Enthusiast. 

Wanted to share with you the product you may find helpful. We've laun
ched AimOS, an open-source, modular observability platform for AI Systems.  

With AimOS, you can log, connect, and obse
rve every facet of your AI systems –  from experimentation and production stages to input prompts and monitoring. 

AimO
S comes installed with default logging apps: 

\- Base App for a basic logging,  
\- ML experiment tracking App  
\- AI 
Systems Tracing and Debugging Apps - a combination of variety of apps that log from LangChain to LlamaIndex traces all i
n one place.

[AimOS Apps](https://preview.redd.it/7p2c1nkvgxxb1.png?width=1040&format=png&auto=webp&s=6f9239364e53a0888
014611990014a1ad3cb38ed)

AimOS is a game-changer, it's easy to use but powerful enough to meet next-stage infrastructur
e needs.  

[Experiment tracker](https://preview.redd.it/nhiyft40hxxb1.png?width=2510&format=png&auto=webp&s=c7ac8e54651
f4543ea12ea29b5251472f346c19b)

Aim 💫 — An easy-to-use & supercharged open-source experiment tracker: [https://github.co
m/aimhubio/aim](https://github.com/aimhubio/aim)  
AimOS 🔍 — An easy-to-use modular observability for AI Systems. Extens
ible, scalable and modular: [https://github.com/aimhubio/aimos](https://github.com/aimhubio/aimos) 

To learn more about
 AimOS, check out the [article.](https://aimstack.io/blog/new-releases/aim-4-0-open-source-modular-observability-for-ai-
systems)
```
---

     
 
all -  [ RAG refresh ](https://www.reddit.com/r/LangChain/comments/17m2ai8/rag_refresh/) , 2023-11-04-0909
```
I got tasked to set up a query bot on one of our file servers for HR and I got everything working. But I am trying to fi
nd a way to dynamically re embed documents that get modified by the end user. Right now i just have the user drop the do
cs they want available into a file and i embed the file every day. If i go company wide it is going to be expensive to d
o it that way. anybody else have a way to keep their docs relevant?
```
---

     
 
all -  [ Why Customized ChatBot using OpenAI API is slow and Inaccurate? ](https://www.reddit.com/r/ChatGPT/comments/17m1ds9/why_customized_chatbot_using_openai_api_is_slow/) , 2023-11-04-0909
```
I created Multiple ChatPDF application from Youtuber Alejandro AO. Using langchain and OpenAI's API. I feel that this ap
proach isn't as much good as ChatGPT or the ChatPDF which is already in the market. Why my model is slow and not replyin
g accurately? I trier temperature 0,0.5 as well.
```
---

     
 
all -  [ does anyone know how to intelligently plot a graph for the requested data in an LLM Chat app? ](https://www.reddit.com/r/LangChain/comments/17lzio5/does_anyone_know_how_to_intelligently_plot_a/) , 2023-11-04-0909
```
 For example, if the user asks a question like, 'What was Apple's profit in 2022?' The LLM will answer the question usin
g a data source, but I also want to plot a bar graph of Apple's profit over the years. How can I identify which data to 
plot based on the question?

I am using an agent with multiple tools
```
---

     
 
all -  [ Difference between Langchain and Botpress ](https://www.reddit.com/r/LangChain/comments/17lyodl/difference_between_langchain_and_botpress/) , 2023-11-04-0909
```
Hi folks! Iam really new to this LLMs and Langchain. I have been building some chatbots on Botpress. I would like to kno
w what are the differences in making a chatbot on Botpress and Langchain. Please help. I would like to learn more about 
Langchain.
```
---

     
 
all -  [ Question: Building and Deploying LLM apps to production ](https://www.reddit.com/r/LocalLLaMA/comments/17lvpn4/question_building_and_deploying_llm_apps_to/) , 2023-11-04-0909
```
Hey everyone,

I'm currently researching how building production ready software is different with LLMs compared to 'Soft
ware 1.0'

While building my own small project i noticed some difficulties and wonder how you guys managed them:

* Buil
ding agents in langchain quickly lets context size and cost explode ($0.10 per request). How do you work around it?
* Ho
w do you ensure that users are getting the responses they expected?
* How do you version control and test your prompts? 
Do you run tests against prompts?
* Do you integrate Open Source LLMs in your pipelines and let them manage simpler task
s? How do you host them?

Super exited to learn other problems and challenges you guys encountered!
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-04-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-04-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-04-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-04-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-04-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-04-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-04-0909
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-04-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-04-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-11-04-0909
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-04-0909
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-04-0909
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-04-0909
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-11-04-0909
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
