 
all -  [ Any opinions on the reranker used in the RAG pipeline? ](https://www.reddit.com/r/LangChain/comments/1be5caf/any_opinions_on_the_reranker_used_in_the_rag/) , 2024-03-14-0909
```
We have been building out the RAG pipeline at [www.querypal.com](https://www.querypal.com), and thinking of adding the c
ohere reranker vs GPT calls. Any suggestions here?
```
---

     
 
all -  [ NBA GPT project advice ](https://www.reddit.com/r/learnmachinelearning/comments/1be3qgd/nba_gpt_project_advice/) , 2024-03-14-0909
```
Hi,

I have a dataset of NBA player stats looking like this:

&#x200B;

https://preview.redd.it/823p5g5i86oc1.png?width=
1898&format=png&auto=webp&s=e3fe373d2ad419b5ebf649fc464a54d6a2814256

I want an llm (gpt4/mistral maybe) that can answer
 questions about this. Example questions is 'name the top 2 players on each team with highest 3 point %'. My vision is a
n NBA agent who knows all the nba data and can answer any question about it.

What is the way to make a basic working mo
del for this? I was thinking about using OpenAI's fine tuning feature to train it with this data. But I've also seen an 
approach of using 'Langchain and a vector SB store is the way to go'. Does anyone have any input on how to approach this
? Much appreciated.
```
---

     
 
all -  [ With Langserve as Backend how to make embeddable chatbot widget ](https://www.reddit.com/r/LangChain/comments/1be09zc/with_langserve_as_backend_how_to_make_embeddable/) , 2024-03-14-0909
```
Hi all,

How create a embeddable chatbot widgets


Is there any ready-made framework for that?


I wanna create a chatbo
t widget that can be integrated with any website.


Something like this.
<div id='chatbot-widget'>
    <!-- Placeholder 
for chatbot widget -->
  </div>
  <script>
    window.embeddedChatbotConfig = {
      apiEndpoint: 'https://your-api-end
point.com/chat',
      botName: 'ChatBot',
      botAvatar: 'bot.png'
    };
  </script>
  <script src='chatbot.js' defe
r></script>
```
---

     
 
all -  [ Need help creating a MongoDBAtlasVectorSearch retriever that filters other fields in the embedding ](https://www.reddit.com/r/LangChain/comments/1bdz0l1/need_help_creating_a_mongodbatlasvectorsearch/) , 2024-03-14-0909
```
Looking for help please.

I have a mongo retriever as follows:

	const retriever = new MongoDBAtlasVectorSearch(
		new O
penAIEmbeddings(),
		{
			collection,
			indexName: 'vector_index', 
			textKey: 'text', 
			embeddingKey: 'embedding', 
 
		}
	).asRetriever(4, {
		preFilter: {
			_user // need help here
		},
 	});

It runs fine without the preFilter, but 
I need it to return embeddings matching a specific _user, which is a string representing the user's id.

I'm kinda lost 
on how to accomplish this. Do I need to create special indexes? I'm not sure if using postFilterPipeline is correct eith
er since it would run *after* returning embeddings? Can't find much in the docs.

Thank you
```
---

     
 
all -  [ Langchain logger released ](https://www.reddit.com/r/LangChain/comments/1bdxpau/langchain_logger_released/) , 2024-03-14-0909
```
Howdy

I just released a langchain logger that I wrote a while back.

I had a couple of startups wanting to use langchai
n but display the chain of thought. 

You can retrieve it after the invoke is finished but I wanted to display it in rea
l time, so wrote a callback that wrapped a logger.

Please feel free to use it [https://github.com/thevgergroup/langchai
n-logger](https://github.com/thevgergroup/langchain-logger)

If you're using Flask we also released a viewer that pairs 
with this [https://github.com/thevgergroup/flask-log-viewer](https://github.com/thevgergroup/flask-log-viewer)

And lets
 you view the logs as they occur. 

&#x200B;
```
---

     
 
all -  [ RAG vs similarity search for chat bot use case ](https://www.reddit.com/r/LangChain/comments/1bdsxpc/rag_vs_similarity_search_for_chat_bot_use_case/) , 2024-03-14-0909
```
I'm working on a basic chat bot use case that would answer based on QnA knowledge base, how do I select between performi
ng traditional RAG pipeline or implementing similarity search on embeddings of KB and user's question and output the ans
wer. 
```
---

     
 
all -  [ Any solutions or alternatives for similarity search on vector DBs for short words with numerics? ](https://www.reddit.com/r/LangChain/comments/1bdqq09/any_solutions_or_alternatives_for_similarity/) , 2024-03-14-0909
```
So basically I am trying to search a cell line vector data base that has entries that look like this:  
'''

ID: 253F1


AC: CVCL\_B513

SY: NA

OX: NCBI\_TaxID=9606; ! Homo sapiens (Human)

CA: Induced pluripotent stem cell

'''

&#x200B;


There are easily tens of thousands of these entries in a text file that I store as a vector DB. I find that if I do a si
milarity search on say the 'Induced pluripotent stem cell', the similarity search always returns relevant documents. How
ever, If i search 253F1 or CVCL\_B513 its about a coin flip on whether the similarity search will return relevant docume
nts. The reason I need to do this form of search as opposed to a direct word match is because sometimes the input query 
will have varying forms of syntax eg: 253-F1 or 253.F1 or 253f1 this scaled over thousands of entries. Is there an alter
native to approaching these short queries? Something that I might find getting better results?

&#x200B;

Any help would
 be appreciated?
```
---

     
 
all -  [ How to create a conversational style AI chatbot which uses Mixtral 8x7b in AWS Sagemaker ](https://www.reddit.com/r/LangChain/comments/1bdqny9/how_to_create_a_conversational_style_ai_chatbot/) , 2024-03-14-0909
```
 Hey guys, I am a little confused on how I can create a conversational style AI chatbot which uses Mixtral 8x7b in AWS S
agemaker.

I understand when using Sagemaker, this would involve an endpoint URL which directly connects the LLM to say 
the front end UI.

1. Because of this, how do I code my script so that the AI chatbot will be able to remember previous 
messages in the flow of the conversation?
2. Does Mixtral 8x7b also uses the same format as OpenAI for their messages (s
ee below), so that I can just keep appending the messages for the memory of the LLM?

\`\`\`messages.append({'role': '',
 'content': message})\`\`\`

I am unsure if I had missed any other questions for me to be able to build this conversatio
nal style AI chatbot. Would really appreciate any help with this. Many thanks!
```
---

     
 
all -  [ Urgent Plan and Guidance needed ](https://www.reddit.com/r/LangChain/comments/1bdnzpl/urgent_plan_and_guidance_needed/) , 2024-03-14-0909
```
I Plan to use Langchain agent and AzureOpenAI and AzureOpenAIEmbeddings for the purpose of using a huge json dataset whi
ch contains indexed dict of Web APIs (with methods and function codes). And I mean to use a Langchain Agent to go throug
h it and generate me end-to-end test sequences of those APIs used in API testing.

Can someone give me an overview and a
 very Detailed plan of how I can accomplish this using langchain agent and my json file which contains the API data.

He
re is a sample of how my data looks like :

'2': {
        'Method': 'POST',
        'Path': '',
        'FunctionName':
 '',
        'FunctionCode': '{\...\}',
        'Queries': []
        'Description ' : []
    }



```
---

     
 
all -  [ So what IS the best way to create AI applications? ](https://www.reddit.com/r/LangChain/comments/1bdnzjm/so_what_is_the_best_way_to_create_ai_applications/) , 2024-03-14-0909
```
As far as I understood LangChain seems to become overly complicated at some point and many people say it's only good for
 demo purposes. 

So what IS actually the best way to create applications where agents can communicate with each other a
nd work as supposed to? I heard good things about Ollama here. But what is the overall smartest way to create functional
 applications if it's not LangChain?
```
---

     
 
all -  [ stop criteria ](https://www.reddit.com/r/LangChain/comments/1bdmhyx/stop_criteria/) , 2024-03-14-0909
```
how I can stop the generation process before the input (I want to stop it at first AI response) and how?

https://previe
w.redd.it/jwhozjqfc2oc1.png?width=1099&format=png&auto=webp&s=f47e21115e332e7be952839ed6dc55462b0c10a7
```
---

     
 
all -  [ How does LangChain ensure the quality and accuracy of language learning content available on its pla ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1bdjyaw/how_does_langchain_ensure_the_quality_and/) , 2024-03-14-0909
```
 

# How does LangChain ensure the quality and accuracy of language learning content available on its platform?

 

## E
nsuring Quality and Accuracy in Language Learning Content on LangChain Platform

 

## Introduction

At LangChain, we [*
*understand**](https://fxdatalabs.com/) the importance of providing high-quality and accurate language learning content 
to our users. Our platform is [**designed**](https://fxdatalabs.com/) to offer [**comprehensive**](https://fxdatalabs.co
m/) and reliable resources that [**facilitate**](https://fxdatalabs.com/) effective language acquisition. In this articl
e, we'll delve into the various measures and processes we employ to ensure the quality and [**accuracy**](https://fxdata
labs.com/) of the content available on the [**LangChain**](https://fxdatalabs.com/) platform.

### Rigorous Content Cura
tion

📷

One of the [**primary**](https://fxdatalabs.com/) methods we use to maintain quality is through rigorous conten
t curation. Our team of language [**experts**](https://fxdatalabs.com/) and [**educators**](https://fxdatalabs.com/) met
iculously curates and [**reviews**](https://fxdatalabs.com/) all content before it is made available on the platform. Ea
ch piece of content undergoes thorough scrutiny to ensure [**accuracy**](https://fxdatalabs.com/), relevance, and lingui
stic [**authenticity**](https://fxdatalabs.com/).

### Expert-Authored Material

We [**prioritize**](https://fxdatalabs.
com/) content authored by language experts, educators, and native speakers to guarantee the highest level of [**accuracy
**](https://fxdatalabs.com/) and authenticity. By sourcing content from reputable publishers, educational institutions, 
and [**language**](https://fxdatalabs.com/) professionals, we ensure that our users have access to [**reliable**](https:
//fxdatalabs.com/) and authoritative learning materials.

## Continuous Feedback and Improvement

We actively seek [**fe
edback**](https://fxdatalabs.com/) from our users to identify areas for improvement and refine our content offerings. Th
rough user [**surveys**](https://fxdatalabs.com/), reviews, and analytics, we gather valuable insights into user [**pref
erences**](https://fxdatalabs.com/), learning outcomes, and content [**effectiveness**](https://fxdatalabs.com/). This f
eedback loop allows us to [**iteratively**](https://fxdatalabs.com/) improve our content selection and delivery [**metho
ds**](https://fxdatalabs.com/) to better meet the needs of our diverse user base.

### Multimodal Learning Resources

📷


[**LangChain**](https://fxdatalabs.com/) offers a diverse range of multimodal learning resources, including text-based 
lessons, audio [**recordings**](https://fxdatalabs.com/), videos, interactive exercises, and real-world simulations. By 
providing content in various [**formats**](https://fxdatalabs.com/), we accommodate different learning styles and [**pre
ferences**](https://fxdatalabs.com/), ensuring that each user can engage with the material in a way that best suits thei
r [**individual**](https://fxdatalabs.com/) needs.

### Quality Assurance Measures

To maintain the highest [**standards
**](https://fxdatalabs.com/) of quality and accuracy, we implement robust quality assurance measures throughout the [**c
ontent creation**](https://fxdatalabs.com/) and delivery process. This includes thorough [**fact-checking**](https://fxd
atalabs.com/), proofreading, and editing procedures to eliminate errors, inconsistencies, and inaccuracies. Additionally
, we employ [**plagiarism**](https://fxdatalabs.com/) detection tools to ensure that all content is original and [**ethi
cally**](https://fxdatalabs.com/) sourced.

### Integration of AI and Machine Learning

📷

We leverage advanced [**techn
ologies**](https://fxdatalabs.com/) such as artificial intelligence (AI) and machine learning to enhance the quality and
 effectiveness of our [**language**](https://fxdatalabs.com/) learning content. [**AI algorithms**](https://fxdatalabs.c
om/) analyze user interactions, preferences, and learning patterns to personalize content recommendations and [**optimiz
e**](https://fxdatalabs.com/) learning pathways. By [**harnessing**](https://fxdatalabs.com/) the power of AI, we contin
uously adapt and improve our content offerings to deliver a tailored and engaging [**learning**](https://fxdatalabs.com/
) experience.

### Interactive Assessments and Feedback

[**LangChain**](https://fxdatalabs.com/) incorporates interacti
ve assessments and feedback mechanisms to facilitate active learning and skill [**development**](https://fxdatalabs.com/
). Users receive immediate feedback on their progress, performance, and areas for improvement, [**enabling**](https://fx
datalabs.com/) them to track their [**proficiency**](https://fxdatalabs.com/) levels and target specific language skills
 for further practice and refinement.

### Integration of Technology

📷

[**Technology**](https://fxdatalabs.com/) plays
 a crucial role in enhancing the quality and effectiveness of our content. We leverage advanced [**technologies**](https
://fxdatalabs.com/) such as artificial intelligence (AI) and machine learning to [**analyze**](https://fxdatalabs.com/) 
user interactions and learning patterns.

This data-driven approach allows us to [**personalize**](https://fxdatalabs.co
m/) content recommendations, identify areas for [**improvement**](https://fxdatalabs.com/), and optimize learning [**pat
hways**](https://fxdatalabs.com/) for each user. By harnessing the power of [**technology**](https://fxdatalabs.com/), w
e can deliver a more tailored and engaging learning experience.

### Conclusion

At [**LangChain**](https://fxdatalabs.c
om/), our commitment to quality and accuracy is paramount. Through rigorous content curation, [**expert-authored**](http
s://fxdatalabs.com/) material, continuous feedback and improvement, multimodal learning resources, quality [**assurance*
*](https://fxdatalabs.com/) measures, integration of AI and [**machine learning**](https://fxdatalabs.com/), and interac
tive assessments and feedback, we ensure that our users have access to the most reliable, [**authentic**](https://fxdata
labs.com/), and effective language learning content available.

Join us on [**LangChain**](https://fxdatalabs.com/) and 
embark on your [**language learning**](https://fxdatalabs.com/) journey with confidence and success.

For more insights 
into AI|ML and Data Science [**Development**](https://fxdatalabs.com/), please write to us at: [**contact@htree.plus**](
mailto:contact@htree.plus)| [**F(x) Data Labs Pv**](https://fxdatalabs.com/)[**t**](https://fxdatalabs.com/)[**. Ltd.**]
(https://fxdatalabs.com/)

**#QuantumMachineLearning #Innovation #ComputationalScience #MultiverseComputing** 🌌🧠
```
---

     
 
all -  [ How to embed multiple markdowns in llama index? ](https://www.reddit.com/r/LangChain/comments/1bdj7am/how_to_embed_multiple_markdowns_in_llama_index/) , 2024-03-14-0909
```
I would like to implement rag using llama index.

I have several Markdown files and I need to load and embed them. Is it
 possible to embed multiple Markdown files?
```
---

     
 
all -  [ I built a platform to automatically find the best LLM for your use case ](https://www.reddit.com/r/LangChain/comments/1bdih2v/i_built_a_platform_to_automatically_find_the_best/) , 2024-03-14-0909
```
I've been building a platform to make managing and optimizing your LLM applications more streamlined: [https://optimix.a
pp/](https://optimix.app/?langchain). We make it easy to automatically redirect your API request to the best LLM for you
r task and preferences, and provide useful analytics on how your LLM's outputs are performing in real-time.

Here are so
me of the main features:

* Automatic, context and data-driven LLM switching.
* Rollout and A/B test prompt or model cha
nges to see if they are helpful to the user, and fine-tune based on your logs.
* Metrics on latency, cost, error recover
y, user satisfaction, and more.

I'd love any feedback, thoughts, and suggestions. Hope this can be a helpful tool for a
nyone building AI products!
```
---

     
 
all -  [ Invoke returning Tuple Object ](https://i.redd.it/dehsnlox60oc1.jpeg) , 2024-03-14-0909
```
I’m trying to retrieve output like how OpenAI API completions gives, it has attributes like content and others, but in L
angchain invoke method I’m getting back tuple object on which I can’t iterate over, is there any way to get back json li
ke output while using langchain? On which I can iterate over and have attributes like content? 
```
---

     
 
all -  [ Why is Langchain so frustrating to work with? ](https://www.reddit.com/r/LangChain/comments/1bdaqpw/why_is_langchain_so_frustrating_to_work_with/) , 2024-03-14-0909
```
I am following a couple of tutorials from [https://sdk.vercel.ai/docs](https://sdk.vercel.ai/docs) on setting up my own 
NEXT.js chat bot with a RAG model; coincidentally I failed to find anything LangChain that is working with Azure OpenAI;
 heck even the import statements for langchain are deprecated; it keeps displaying errors in the terminal
```
---

     
 
all -  [ Can LangSmith trace Ollama? ](https://www.reddit.com/r/LangChain/comments/1bd7uqb/can_langsmith_trace_ollama/) , 2024-03-14-0909
```
Hi everyone. I am new to LangChain.

&#x200B;

I have set

&#x200B;

    export LANGCHAIN_TRACING_V2='true'
    export L
ANGCHAIN_API_KEY='<my-api-key>'
    export LANGCHAIN_ENDPOINT=https://api.smith.langchain.com

&#x200B;

&#x200B;

and I
 invoke an LLM powered by Ollama, I can't really see anything in [https://smith.langchain.com/](https://smith.langchain.
com/). I haven't tried using GPT or other FM. Does LangSmith currently not support Ollama?

&#x200B;

TIA!
```
---

     
 
all -  [ LLM Model VRAM Calculator - a Hugging Face Space by NyxKrage ](https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator) , 2024-03-14-0909
```

```
---

     
 
all -  [ I finally tested LangChain + Amazon Bedrock for an end-to-end RAG pipeline ](https://www.reddit.com/r/LangChain/comments/1bd55re/i_finally_tested_langchain_amazon_bedrock_for_an/) , 2024-03-14-0909
```
Hi folks!

I read about it when it came out and had it on my to-do list for a while now...

I finally tested Amazon Bedr
ock with LangChain. **Spoiler:** The Knowledge Bases feature for Amazon Bedrock is a super powerful tool if you don't wa
nt to think about the RAG pipeline, it does everything for you.

I wrote a (*somewhat boring but*) helpful blog post abo
ut what I've done with screenshots of every step. So if you're considering Bedrock for your LangChain app, check it out 
it'll save you some time: [https://www.gettingstarted.ai/langchain-bedrock/](https://www.gettingstarted.ai/langchain-bed
rock/)

Here's the gist of what's in the post:

* Access to foundational models like Mistral AI and Claude 3
* Building 
partial or end-to-end RAG pipelines using Amazon Bedrock
* Integration with the LangChain Bedrock Retriever
* Consuming 
Knowledge Bases for Amazon Bedrock with LangChain
* And much more...

Happy to answer any questions here or take in sugg
estions! 

Let me know if you find this useful. Cheers 🍻
```
---

     
 
all -  [ Benchmarking extraction_chain ](https://www.reddit.com/r/LangChain/comments/1bd4uj9/benchmarking_extraction_chain/) , 2024-03-14-0909
```
Hi there. I am trying to figure out the best way to start benchmarking the langchain\_extraction\_chain between differen
t versions and models. I need to be able to determine how accurate these extraction are on large txt files. Any suggesti
ons that can make my life easier? 
```
---

     
 
all -  [ How to use local hosted LLMs in LangChain ](https://www.reddit.com/r/LangChain/comments/1bd4gjp/how_to_use_local_hosted_llms_in_langchain/) , 2024-03-14-0909
```
I have one LLM service running, how to use that remote LLM service as LLM in LangChain. There is no clear documentation 
about it.
```
---

     
 
all -  [ Need your help switching jobs in this markrt as an ML engineer. ](https://www.reddit.com/r/developersIndia/comments/1bd446p/need_your_help_switching_jobs_in_this_markrt_as/) , 2024-03-14-0909
```
I need guidance to switch to a pure ML enginner role.So it might seem like a rant or something but here it is. I graduat
ed in '22 and joined a big 4 in their consulting division as an analyst. I had some projects related to machine learning
 so they put me as a data scientist in a project. So now in this project after 18 months I have been just executing exis
ting code every month  to deliver it to the client. At first I was ok as I was learning stuff but now it seems really re
dundant. I recently got a chance to develop a new code, basically developing and deploying ML pipeline related to regres
sion , but guess what client doesnot want this now. The work also does not makes sense any output or prediction is gener
ated on a really small datasets and it is furhter 'optimized' or basically a code is made to literally add subtract stuf
f from it. Why even care to do all the ML stuff. I want to get in genAI and LLMs stuff there are other people working on
 it in different projects but my current project doesnot wants to leave me (doing good work is also bad i think) I have 
also communicated to my lead about it and their reply is we will see we cannot let you go now. I have done some self pro
jects on genai and Langchain and have been applying everywhere I get a chance but I am getting no response. In this proj
ect I have worked using python sql excel (client needs the results in excel and the more complex it is the more they lov
e it) and have done a work of ML engineer (even written unittests for functions) and a business analyst also but half th
e pay. My notice period is 90 days and guess what they give pay raise in month of may-june. So what do I do now. Should 
I f**k up intentiaonally to get off the project or just resign. Coz a lot of companies have just ghosted me after the no
tice period. And the new llms stuff is crazy the tech is new and the scope is vast. I am ready to work 6 days for a new 
pre revenue startup also I just want work on something new .
```
---

     
 
all -  [ Are there any good tools/frameworks that chats over SQL db? ](https://www.reddit.com/r/LocalLLaMA/comments/1bd33s3/are_there_any_good_toolsframeworks_that_chats/) , 2024-03-14-0909
```
So it's been a while since i tinkered w/ llm frameworks, and now I'm looking for something that allows me to chat/work o
ver my CRM sqlite db and ideally have reasoning capabilities.

What are some newest / reliable tools that enable this? A
 year ago when I played w/ llm, theres langchain, griptape, haystack, etc, but now are there better tools now?

Thanks f
or any pointers and suggestions!
```
---

     
 
all -  [ LangGraph for beginners  ](https://www.reddit.com/r/LangChain/comments/1bd14bn/langgraph_for_beginners/) , 2024-03-14-0909
```
Hey everyone, checkout this new tutorial to understand the basics of LangGraph with an example, codes and visualization 
https://youtu.be/nmDFSVRnr4Q?si=ysPGMBvlzGabwChv
```
---

     
 
all -  [ Optimal retrieval methods for image compliance analysis ](https://www.reddit.com/r/LangChain/comments/1bcxe73/optimal_retrieval_methods_for_image_compliance/) , 2024-03-14-0909
```
Hi !

I'm working on a project where the main goal is to assess the compliance of images based on their descriptions.

I
 have already worked on a V1 that uses a gpt assistant and autogen. It works but for cost and performance issues I want 
to use langchain.

Here's the workflow I'm using:

1. **Image Description**: Generate a detailed description of an image
. (GPT-4V)
2. **Text Retrieval**: Using retrieval to find texts that are relevant to this description. (GPT Assistant)
3
. **Compliance Analysis**: Analyze the description and retrieved texts to assess if the image is compliant. (GPT 3.5 Tur
bo)

I am currently trying to recreate the text retrieval part using Langchain but querying the DB with a description le
ads to bad results. I also tried to use a MultiQueryRetriever but the questions are not really relevant even when I adju
st the prompt

I'd greatly appreciate any insights or recommendations on:

* Effective retrieval techniques for this use
 case.
* How to leverage Langchain's capabilities for both generating pertinent queries from image descriptions and retr
ieving relevant texts.
* Tips on ensuring the relevance and quality of the retrieved texts for accurate compliance analy
sis.



Thank you for your help !
```
---

     
 
all -  [ How to store text chunks and immediate images following the text chunks together in a vector databas ](https://www.reddit.com/r/LocalLLaMA/comments/1bcww9m/how_to_store_text_chunks_and_immediate_images/) , 2024-03-14-0909
```
I'm working on a Question Answering RAG system with langchain which takes in Pdf with images. The issue is with the retr
ieval strategy. For example, there's a text line followed by an image where the line says 'The following is an image of 
ABC object and its components' and the image has nothing mentioned as ABC just the plain picture of it. Currently, I'm e
xtracting all the text and images and storing the embedding in a vector store.

When I ask a question on the ABC object,
 it's only retrieving that text line and not the image, because the image has no info that says it's an ABC object.

Is 
there any way to solve this and store the relation between the text and the images?

PS: I'm new to LLMs.
```
---

     
 
all -  [ Dotprod vs Cosine Similarity ? ](https://www.reddit.com/r/LangChain/comments/1bcvhad/dotprod_vs_cosine_similarity/) , 2024-03-14-0909
```
Hello I am wondering what is the difference between Cosine similarity ans Dot products in term of efficiency 

My use ca
se is a really technical book of 1000 pages (that does not always have the same length) 
and I chunked the book by page 
meaning 1000 vectors .

What best method should I consider ? 
```
---

     
 
all -  [ Internet Based RAG - Scraping ](https://www.reddit.com/r/LangChain/comments/1bcrzbm/internet_based_rag_scraping/) , 2024-03-14-0909
```
I'm working on a RAG system that doesn't have a pre-build document corpus, and instead scrapes the internet for informat
ion in real time. It seemed like a pretty simple task, but I'm having trouble with the web-scraping aspect. I'm pretty n
ew to any sort of scraping so I need to get an idea of this - is it a pretty easy task to scrape Google search - like sc
raping the top 5 links of 10 different search queries? I feel like that's not a huge number, but I'm already having issu
es and I think they're related to Google blocking bots. Is this something that you need to use an API for or is it prett
y easy to work around with some proxy changes and stuff?
```
---

     
 
all -  [ I don't get Ollama ](https://www.reddit.com/r/LangChain/comments/1bcrva0/i_dont_get_ollama/) , 2024-03-14-0909
```
I'm working on a project where I'll be using an open-source llm - probably quantized Mistral 7B. Now I've seen allot of 
people talking about Ollama and how it lets you run llm models locally. I still don't get what it does. Like can't you a
lready run models locally if you have enough RAM, a good GPU etc.? Does Ollama quantize the models to make it easier to 
run them locally? If that's what it does then it's no different from quantizing a model yourself and running it on your 
own system right? Ik that's not just it so would really appreciate it if someone could explain exactly what it does. Als
o would Ollama also help with deploying models on the cloud? My computer only has a CPU and I'll probably be using GCP f
or the llm - so would using Ollama be useful there? Because I've only seen it mentioned with regards to how good it is f
or local deployment
```
---

     
 
all -  [ What role does artificial intelligence play in the LangChain platform? ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1bcpslu/what_role_does_artificial_intelligence_play_in/) , 2024-03-14-0909
```
 

# What role does artificial intelligence play in the LangChain platform?

 

## Language Learning with AI: The Role o
f LangChain! 🌐🤖

 

## Introduction:

In today's [**interconnected**](https://fxdatalabs.com/) world, language learning 
has become a vital skill for individuals seeking to navigate diverse [**cultural**](https://fxdatalabs.com/) landscapes 
and [**global**](https://fxdatalabs.com/) markets.

With the advent of [**technology**](https://fxdatalabs.com/), artifi
cial intelligence (AI) has emerged as a powerful tool in revolutionizing the language learning experience. [**LangChain*
*](https://fxdatalabs.com/), a leading language learning platform, [**harnesses**](https://fxdatalabs.com/) the capabili
ties of AI to provide users with personalized, immersive, and effective language learning [**experiences**](https://fxda
talabs.com/).

In this comprehensive [**article**](https://fxdatalabs.com/), we delve into the multifaceted role of arti
ficial intelligence within the LangChain [**platform**](https://fxdatalabs.com/), exploring its innovative features, ben
efits, and the transformative impact it has on language [**acquisition**](https://fxdatalabs.com/).

## Understanding th
e Importance of Artificial Intelligence in Language Learning:

📷

In traditional language [**learning**](https://fxdatal
abs.com/) settings, instructors often face challenges in catering to the diverse needs and learning styles of [**individ
ual**](https://fxdatalabs.com/) learners.

AI-powered language learning platforms, such as [**LangChain**](https://fxdat
alabs.com/), address these challenges by [**leveraging**](https://fxdatalabs.com/) machine learning algorithms, natural 
language processing (NLP), and other AI techniques to deliver [**personalized**](https://fxdatalabs.com/) instruction, a
daptive feedback, and [**immersive**](https://fxdatalabs.com/) learning experiences tailored to each learner's proficien
cy level, preferences, and goals.

### Personalized Learning Paths:

One of the key [**features**](https://fxdatalabs.co
m/) enabled by AI in the LangChain platform is the creation of personalized learning paths for users. Through [**sophist
icated**](https://fxdatalabs.com/) algorithms that analyze user interactions, [**performance**](https://fxdatalabs.com/)
 data, and learning patterns, LangChain dynamically adjusts the curriculum, pacing, and content to suit each [**learner'
s**](https://fxdatalabs.com/) needs.

Whether a beginner [**starting**](https://fxdatalabs.com/) from scratch or an adva
nced learner seeking to refine specific language skills, AI ensures that the [**learning**](https://fxdatalabs.com/) jou
rney is tailored to the individual, maximizing [**engagement**](https://fxdatalabs.com/) and learning outcomes.

### Ada
ptive Learning Resources:

📷

AI algorithms in LangChain continuously [**analyze**](https://fxdatalabs.com/) user intera
ctions with learning materials, identifying areas of strengths and weaknesses to [**deliver**](https://fxdatalabs.com/) 
targeted learning resources and [**activities**](https://fxdatalabs.com/).

From interactive exercises and [**multimedia
**](https://fxdatalabs.com/) content to real-world simulations and cultural immersion experiences, LangChain's adaptive 
[**learning**](https://fxdatalabs.com/) resources adapt to the user's proficiency level, [**learning**](https://fxdatala
bs.com/) preferences, and interests, providing a personalized and engaging learning experience that fosters skill [**acq
uisition**](https://fxdatalabs.com/) and retention.

### Intelligent Feedback and Assessment:

AI-powered assessment [**
mechanisms**](https://fxdatalabs.com/) in LangChain provide users with real-time feedback on their language proficiency,
 [**pronunciation**](https://fxdatalabs.com/), grammar, and vocabulary usage.

Through speech [**recognition**](https://
fxdatalabs.com/) technology, NLP algorithms, and machine learning models, LangChain can accurately evaluate user [**resp
onses**](https://fxdatalabs.com/), identify errors, and offer corrective feedback in a [**supportive**](https://fxdatala
bs.com/) and constructive manner.

This intelligent feedback loop enables users to track their [**progress**](https://fx
datalabs.com/), identify areas for improvement, and build [**confidenc**](https://fxdatalabs.com/)e in their language sk
ills.

### Natural Language Interaction:

Another innovative aspect of AI in [**LangChain**](https://fxdatalabs.com/) is
 its ability to facilitate natural language [**interaction**](https://fxdatalabs.com/) between users and the platform.


Through chatbots, virtual language tutors, and [**conversational**](https://fxdatalabs.com/) agents powered by AI, LangC
hain enables users to [**practice**](https://fxdatalabs.com/) speaking, listening, and conversing in the target language
 in a [**simulated**](https://fxdatalabs.com/) real-world environment.

These interactive experiences foster language fl
uency, [**communication**](https://fxdatalabs.com/) skills, and cultural understanding, bridging the gap [**between**](h
ttps://fxdatalabs.com/) theoretical language knowledge and [**practical**](https://fxdatalabs.com/) usage.

### Continuo
us Learning and Improvement:

📷

AI-driven analytics and insights in [**LangChain**](https://fxdatalabs.com/) enable edu
cators and developers to monitor user engagement, performance trends, and [**learning**](https://fxdatalabs.com/) outcom
es, allowing for data-driven decision-making and [**continuous**](https://fxdatalabs.com/) improvement of the platform.


By analyzing user behavior, content [**effectiveness**](https://fxdatalabs.com/), and learning efficacy, LangChain can 
refine its [**algorithms**](https://fxdatalabs.com/), update its curriculum, and introduce new features to enhance the o
verall learning [**experience**](https://fxdatalabs.com/) for users.

### Conclusion:

Artificial intelligence plays a p
ivotal role in the [**LangChain**](https://fxdatalabs.com/) language learning platform, transforming the way [**individu
als**](https://fxdatalabs.com/) acquire, practice, and master new languages.

By harnessing the power of AI to deliver [
**personalized**](https://fxdatalabs.com/) instruction, adaptive learning resources, intelligent feedback, and immersive
 experiences, LangChain empowers learners to achieve their language learning goals [**effectively**](https://fxdatalabs.
com/) and efficiently.

📷

As AI technology continues to evolve, the future of [**language**](https://fxdatalabs.com/) l
earning holds boundless possibilities, with [**LangChain**](https://fxdatalabs.com/) at the forefront of innovation, dri
ving the next [**generation**](https://fxdatalabs.com/) of language education.

For more insights into AI|ML and Data Sc
ience [**Development**](https://fxdatalabs.com/), [**please wri**](https://fxdatalabs.com/)te to us at: [**contact@htree
.plus**](mailto:contact@htree.plus)| [**F(x) Data Labs Pv**](mailto:contact@htree.plus)[**t**](https://fxdatalabs.com/)[
**. Ltd.**](mailto:contact@htree.plus)

[**#LangC**](https://fxdatalabs.com/)[**hai**](mailto:contact@htree.plus)n #AIin
LanguageLearning #FutureOfEducation #LanguageRevolution 🚀📚
```
---

     
 
all -  [ Integrating Langchain with Open Interpreter ](https://www.reddit.com/r/LangChain/comments/1bcn71y/integrating_langchain_with_open_interpreter/) , 2024-03-14-0909
```
Hi everyone,

I am looking for a way to run generated JavaScript code and validate its output. Is there a tool like Pyth
onREPL but for executing Javascript code? I read that Open Interpreter   
 ([https://github.com/KillianLucas/open-interp
reter](https://github.com/KillianLucas/open-interpreter)) has the ability to run JavaScript code. Has anyone integrated 
Open Interpreter with Langchain?

Any help is appreciated.

Thanks

&#x200B;
```
---

     
 
all -  [ Idea questioner  ](https://www.reddit.com/r/LangChain/comments/1bcl6qp/idea_questioner/) , 2024-03-14-0909
```
Hey guys, I'm working on an idea at the moment and trying to gather feedback from different people and backgrounds in th
e AI field. The idea aims to help developers ship their AI apps very quickly and share them as well!

Relly appreciate y
our input 🙌
https://cycls.typeform.com/to/blrTnsfC

If you're interested to get exclusive early access please share your
 email throught the link or feel free to DM me 👍🏼
```
---

     
 
all -  [ Azure Search provider ](https://www.reddit.com/r/LangChain/comments/1bcchol/azure_search_provider/) , 2024-03-14-0909
```
Why Lanchain provider wants me to create an index with some predefined metadata? (otherwise I have an error)
The underly
ing SDK doesn't require that at all...
```
---

     
 
all -  [ Code Embeddings? ](https://www.reddit.com/r/LangChain/comments/1bcbqqv/code_embeddings/) , 2024-03-14-0909
```
Are there examples anywhere on how to use an embedding scheme for code? I see that OpenAI and HuggingFace, at least, off
er such embeddings, but I'm having a hard time determining how to use them.  Probably I'm just not doing well enough at 
searching the web, so pointers would be very welcome.  For example, [this page](https://python.langchain.com/docs/use\_c
ases/code\_understanding) uses only vanilla OpenAI embeddings.
```
---

     
 
all -  [ Example of langchain that uses  ](https://www.reddit.com/r/LangChain/comments/1bc9t6e/example_of_langchain_that_uses/) , 2024-03-14-0909
```
Hi all I am trying to build a sales assistant bot in a startup where if I issue command say '/prospect acmecorp' the age
nt should  1/. Fetch Details from web search about a company 2/. Use a sales playbook knowledge (details of product and 
how to position the product) and generate response about the company and how to position the product. I have been trying
 to find examples which shows how we search and a knowledge can be combined in langchain. Pls if anyone has any insights
 pls help. 
```
---

     
 
all -  [ OpenAI Tools Agent for Open Records Q&A ](https://www.reddit.com/r/LangChain/comments/1bc951u/openai_tools_agent_for_open_records_qa/) , 2024-03-14-0909
```
Wanted to share an experiment I've been working on to test how helpful LLMs could be in answering user questions about O
pen Records (state-level FOIA laws). A basic [demo is available here](https://huggingface.co/spaces/jscotthorn/kora-assi
stant) with cached example questions and responses. An OpenAI account and key are required to perform new queries.   



The AI Agent is given the user's question, some grounding context in our open records law, and a list of tools provided 
to the Agent if it wants to query for additional context. Tools currently available:

* It can look up the full text of 
a statute from the Kentucky Open Records Act
* Look up the full text or summary of an exception from the Act or one inco
rporated from state or federal law (i.e. FERPA, HIPAA).
* Semantic search (chroma db) against case law annotations from 
the Open Records section of the Kentucky Revised Statutes.
* Semantic search against attorney general opinion summaries 
from the Open Records section of the KRS.

Overall the results have been very promising. Observed responses have been la
rgely accurate, and observed inaccuracies have been due to problematic summaries in annotations.
```
---

     
 
all -  [ Loading all logs as a dataset to be processed by a LLM for log querying. Is langchain suitable?  ](https://www.reddit.com/r/LangChain/comments/1bc72wo/loading_all_logs_as_a_dataset_to_be_processed_by/) , 2024-03-14-0909
```
I want to load the load the logs as a dataset for the LLM to ask it which transactions take the longest time or have the
 highest latency having a chatbot answer all my log related questions. Would using langchain be my best option ? 
```
---

     
 
all -  [ Recommendations for easy to follow guides to set up with Code Llama ?  ](https://www.reddit.com/r/LangChain/comments/1bc6dhk/recommendations_for_easy_to_follow_guides_to_set/) , 2024-03-14-0909
```
Trying to build a solution that can query logs (like which transactions have the highest latency )so wanted to ask for r
ecommendations for the best LLM to use leaning towards code Llama and if something can suggest easy to follow guides to 
set everything up because the ones I found were incomplete. Thank you! 
```
---

     
 
all -  [ Build a SaaS Rag system ](https://www.reddit.com/r/Startup_Ideas/comments/1bc69sr/build_a_saas_rag_system/) , 2024-03-14-0909
```
AI is a hot topic right now; everyone is building some API integration with OpenAI, However, there is still plenty of ro
om for new players.

One product you can potentially build is a RAG-based chatbot or API. Take any industry where they h
ave to sift through and read hundreds of documents and build a quick lookup using RAG.

A RAG search would take in the u
ser's question and find similar matching documents. From this refined data, you post to an LLM like 'chatgpt-turbo' or '
Mixtral' and the LLM responds with relevant information based on the documents as context.

To build such a system, you 
going to need Langchain and probably Redis or Qdrant or some other vector DB.

Comment down below if you would like some
 example code. 
```
---

     
 
all -  [ How to build a multi AI agents chatbot ](https://www.reddit.com/r/LangChain/comments/1bc5h1b/how_to_build_a_multi_ai_agents_chatbot/) , 2024-03-14-0909
```
Hey guys, I have a question hoping someone can help me with.

I have been given a task to build an AI chatbot which woul
d consist of 3 AI agents. 

The 1st AI agent will be a general Q&A between the (human) user and this 1st LLM where the (
human) user can ask any general natural language questions to this 1st LLM and this 1st LLM will response back in natura
l language answers.

The 2nd AI agent will specialize in converting natural language questions by the (human) user into 
SQL code (when the (human) user include the word “table” in his/her natural language question). This SQL code will then 
be send to a Postgres database to return a table and the AI chatbot will display this table.

Below this table, the 3rd 
AI agent will automatically produce a natural language summary of the information contained in the table.

I am also wan
ting to use the 1st LLM (I don’t think I need a 4th LLM here) to be able to allow the (human) user to ask natural langua
ge questions of the displayed tables on top and the 1st LLM will provide a natural language answer based on the table.


My question is will AI agent framework libraries like Autogen allow me to create the AI chatbot above, which is a conver
sation style chatbot? My AI chatbot also has a front end web app.

If Autogen isn’t able to do this, are there any other
 frameworks that can do the AI chatbot above? Or if there isn’t any framework libraries available, which mean I need to 
code this from scratch, are there any example codes I can refer to?

Would really appreciate if anyone can help. Many th
anks in advance!
```
---

     
 
all -  [ How do you deploy langchain for RAG on aws? ](https://www.reddit.com/r/LangChain/comments/1bc3s9w/how_do_you_deploy_langchain_for_rag_on_aws/) , 2024-03-14-0909
```
I’m setting up a rack system on my companies AWS cloud. So then I confused about is the Lang Chang and other libraries l
ike it are pretty big! The initial idea that I had was to make a small lambda that would ingest hundreds or thousands of
 documents from an S3 bucket, use another API, like open AI to get the embedding, and then upload that to our vector dat
abase.

You should running into is that Lang chain is about 50 MB and running in a lambda is inconvenient.  Trying to zi
p that is a pain, and then making a docker image even with the aws lambda python runtime bumps it to 8.5 GB image size. 


It seems like the only reasonable thing to do is to make a doctor image here and run it in a container. But that kind 
of defeats the purpose of an ingestion pipeline that is able to go dormant. 

I’d love your thoughts. My point is that o
nce you go to productionalize some kind of ingestion pipeline, Langchain just seems too big and tries to do too much.
```
---

     
 
all -  [ How you find langchain so far? ](https://www.reddit.com/r/LangChain/comments/1bc1hko/how_you_find_langchain_so_far/) , 2024-03-14-0909
```
Started experimenting with LLM apis and slowly figured that I need a proper framework to deal with it

E.g. 
managing my
 input prompts. 
managing actions when reason for completion is not EOS token etc.

Hence I'm here looking for suggestio
ns.

How's langchain as a framework? How's your experience with it?

Looking through the docs, it feels very complicated
 to do a simple task.

E.g. mapreduce and collapse map reduce, reading through the docs and I find it difficult to figur
e out what the backend is doing.

Maybe I'm wrong and have not dealt with LLM long enough to make a good assessment. Wha
t's your thoughts and how's your experience?
```
---

     
 
all -  [ Adding a JSONOutputParser to a RunnableBinding ](https://www.reddit.com/r/LangChain/comments/1bbzoj7/adding_a_jsonoutputparser_to_a_runnablebinding/) , 2024-03-14-0909
```
I have created a retrieval chain which is of the type RunnableBinding, it's the following example: [https://api.python.l
angchain.com/en/latest/chains/langchain.chains.retrieval.create\_retrieval\_chain.html#langchain.chains.retrieval.create
\_retrieval\_chain](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval.create_retrieval_chain.
html#langchain.chains.retrieval.create_retrieval_chain)

&#x200B;

My problem is that I want to add a JSONOutputParser, 
but I cannot seem to figure out how to do that. Does anyone have any ideas about that?
```
---

     
 
all -  [ Langchain updates is disappointing ](https://www.reddit.com/r/LangChain/comments/1bbzaag/langchain_updates_is_disappointing/) , 2024-03-14-0909
```
i just bought course from udemy [https://www.udemy.com/course/langchain-with-python-bootcamp](https://www.udemy.com/cour
se/langchain-with-python-bootcamp) , the course is very well structures all modules are on their place but the problem i
s langchain keeps depricating or updating now i am just on section 1 and already llm and chatmodel is being updated and 
you need to install specific llm like openai so i really need to take this course since its very well structured but i a
lso want to keep up with the updates how would you do that ?
```
---

     
 
all -  [ Combining queries ? ](https://www.reddit.com/r/LangChain/comments/1bbza6x/combining_queries/) , 2024-03-14-0909
```
Hi I'm new here 

I do have a question concerning semantic search 
Let's say I have 2 search queries or more ( User prom
pt + other additional context ) and I wanna search my vector database .

Is it better to combine the strings then embed 
them into one vector then do the search ?

Or embed each element of the query alone then combine all the embeddings into
 one vector then apply a search ? 
```
---

     
 
all -  [ I want to deploy a chatbot that uses rag with the llama index. ](https://www.reddit.com/r/LangChain/comments/1bbyvv8/i_want_to_deploy_a_chatbot_that_uses_rag_with_the/) , 2024-03-14-0909
```
Has anyone already implemented it?

I want to create and distribute a chatbot that uses rag with the llama index.

What 
frameworks should I use to implement a chatbot using rag while considering deployment?

If anyone has already implemente
d it, can you share the git code?
```
---

     
 
all -  [ stream llm model' huggingface' locally ](https://www.reddit.com/r/LangChain/comments/1bbxvvl/stream_llm_model_huggingface_locally/) , 2024-03-14-0909
```
is there any method to stream these models, and output the generated token while it generate to make response live to us
er
```
---

     
 
all -  [ AI & Elixir: How is the experience working with AI apps in elixir ? ](https://www.reddit.com/r/elixir/comments/1bbx48v/ai_elixir_how_is_the_experience_working_with_ai/) , 2024-03-14-0909
```
Hey there, Elixir enthusiasts!

How's everyone doing? I've been thinking a lot about the exciting blend of AI and Elixir
 lately and figured, who better to chat with than all of you? 😊 Are any of you currently dabbling in AI within your Elix
ir projects? If so, I'd love to hear about your experiences! Whether it's overcoming challenges or discovering cool new 
tools, let's swap stories and ideas on how to make the most of AI in our Elixir adventures!

BTW, I want to share my rec
ent endeavor with LangChain by Mark Ericksen. I've been diving into LangChain recently and I have to say, Mark Ericksen'
s work in bringing it to Elixir is impressive! I've actually integrated the library into my personal trading app and it'
s been fantastic. I even whipped up a handy helper Agent that can give you a quick rundown of your portfolio information
.

code : [Agent code](https://github.com/pkrawat1/angel-trading/blob/master/lib/angel_trading/agent.ex)  
Check out the
 demo here!  
[LOOM DEMO](https://www.loom.com/share/c2e677e8f2bb460e9acf9701eecbaced)
```
---

     
 
all -  [ Using Multiple Tools ](https://www.reddit.com/r/LangChain/comments/1bbx1mj/using_multiple_tools/) , 2024-03-14-0909
```
Hi Everyone ,  I am in a fix and need your help. I am building a langchain agent to select between multiple tools depend
ing in the user query. Currently I have two tools - one which reads a SQL database and other which reads an excel. The p
roblem is none of them are working and giving any input as such. 

I am following this exactly--

https://python.langcha
in.com/docs/use_cases/tool_use/multiple_tools
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-14-0909
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-14-0909
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-14-0909
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-14-0909
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-14-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
