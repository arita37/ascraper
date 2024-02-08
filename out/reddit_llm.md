 
all -  [ llama2 / mistral function calling? ](https://www.reddit.com/r/LocalLLaMA/comments/1alcjvq/llama2_mistral_function_calling/) , 2024-02-08-0909
```
Hello,

I've set up a llama2-7b as well as a llama2-13b with some faiss search and retrieval. 

My next step is to try a
nd recreate the function calling capabilities of chat gpt. 

What would be some ways of achieving that? Right now my bes
t option is to use langchain and chain together a model finetuned for function calling, and another one for synthesis.


Could you recommend something better?

Thanks!
```
---

     
 
all -  [ Recommendation system using LLMs ](https://www.reddit.com/r/generativeAI/comments/1al81nh/recommendation_system_using_llms/) , 2024-02-08-0909
```
Checkout how I developed a recommendation system using LangChain and LLMs https://youtu.be/WW0q8jjsisQ?si=9JI24AIj822N9z
JK
```
---

     
 
all -  [ Recommendation system using LangChain and RAG ](/r/LangChain/comments/1al7yyt/recommendation_system_using_langchain_and_rag/) , 2024-02-08-0909
```

```
---

     
 
all -  [ Recommendation system using LangChain and RAG ](https://www.reddit.com/r/LangChain/comments/1al7yyt/recommendation_system_using_langchain_and_rag/) , 2024-02-08-0909
```
Checkout my new tutorial on how to build a recommendation system using RAG and LangChain https://youtu.be/WW0q8jjsisQ?si
=9JI24AIj822N9zJK
```
---

     
 
all -  [ Langchain expression language ](https://www.reddit.com/r/LangChain/comments/1al3xwz/langchain_expression_language/) , 2024-02-08-0909
```
Hi Guys,

Can anyone point me to a resource where we can choose different vector db retriever based on the input questio
n. There is an example on routing to different prompts using runnablelambda. However the input is a dictionary hence it 
works. My problem is to choose the retriever on run time then pass only the question to the selected retriever at runtim
e.
```
---

     
 
all -  [ LangChain for llm ](https://www.reddit.com/r/LangChain/comments/1al25wz/langchain_for_llm/) , 2024-02-08-0909
```
Hi guys, I have to create a llm based on risk analysis (mainly hara) for my company. The only problem is that the input 
data is sensitive that’s why I am steering in the direction of using a locally hosted/offline llm like private gpt or el
asticsearch with some kind of ui. Can anybody give me pointers on where to start and how to do it? I am still a student 
and fairly new to the topic
```
---

     
 
all -  [ Connect ConversationalRetrievalQAChain to LLMChain? ](https://www.reddit.com/r/flowise/comments/1al0wui/connect_conversationalretrievalqachain_to_llmchain/) , 2024-02-08-0909
```
Hey, 

I am trying to build a chatbot app that can act as different characters that has two layers of custom information
:

1) System Prompt  
2) Document Uploads to Pinecone

In the System Prompt, I would like to define the basic behavior a
pplicable for all characters, while each individual character personality is stored in Pinecone via character sheets upl
oaded. Character sheets are already saved in Pinecone.  


In Flowise I have built something like this:

https://preview
.redd.it/7fefzekif5hc1.png?width=2104&format=png&auto=webp&s=093696cc15b34fdd29b2381f59bcd35854a7fef3

So, in the left p
art, the System Prompt for Basic Behaviour is set up, leading into an LLMChain. In the right part, the document retrieva
l from Pinecone for the specific character behavior is set up.

&#x200B;

* Is this generally the right approach for wha
t I describe above?
* If yes, can anybody help how to connect the LLMChain and the ConversationalRetrievalQAChain togeth
er so I can run the chatbot processing both layers of information?

Thanks a lot!
```
---

     
 
all -  [ Multiple Documents ](https://www.reddit.com/r/LangChain/comments/1akzs8s/multiple_documents/) , 2024-02-08-0909
```
Hey guys, I was testing out things and I made a personal document analyser. I chunked and stored multiple documents in t
he same index in Pincone.
Since the documents have contextual overlap, this improved the quality of the results produced
 a lot.

For reference I was testing with the Mistral 8x7b model.

What's your opinion on this??
```
---

     
 
all -  [ Is there a existed way to mapping code files with real businesses? ](https://www.reddit.com/r/LangChain/comments/1akyazk/is_there_a_existed_way_to_mapping_code_files_with/) , 2024-02-08-0909
```
In the past few months, we've experimented with various approaches to enable LLM to comprehend code files. Currently, LL
M can grasp the essence of file meanings at a functional level. This understanding is facilitated by providing contextua
l information such as:

* File content
* File path
* Commit message
* Issues
* ...

However, the code represents busines
s logic, which often spans multiple/complex categories. This business logic may be entirely unrelated to the contents me
ntioned in a single code file, posing a significant challenge for LLM to comprehend and classify.

I'm wondering if ther
e are any existing methods or approaches to address this issue. Any insights or suggestions would be greatly appreciated
.  Thanks in advance :)
```
---

     
 
all -  [ Use Langchain Extraction with Bedrock ](https://www.reddit.com/r/aws/comments/1akw22w/use_langchain_extraction_with_bedrock/) , 2024-02-08-0909
```
Is it possible to use Langchain extraction with AWS Bedrock? It works with no issues with OpenAI.

Here is the documenta
tion: https://python.langchain.com/docs/use_cases/extraction

Basically take the following code and replace with Bedrock
:

from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI

# Schema
schema = {
   
 'properties': {
        'name': {'type': 'string'},
        'height': {'type': 'integer'},
        'hair_color': {'type
': 'string'},
    },
    'required': ['name', 'height'],
}

# Input
inp = '''Alex is 5 feet tall. Claudia is 1 feet tall
er Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.'''

# Run chain
llm = ChatOpenAI(temperatur
e=0, model='gpt-3.5-turbo')
chain = create_extraction_chain(schema, llm)
chain.run(inp
```
---

     
 
all -  [ RAG using pinecone does not give accurate data ](https://www.reddit.com/r/LangChain/comments/1akvy3c/rag_using_pinecone_does_not_give_accurate_data/) , 2024-02-08-0909
```
I'm trying to build PDF chatbot using OpenAI, Langchain and Pinecone.

Here is my code,

    from langchain.document_loa
ders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTe
xtSplitter, CharacterTextSplitter
    
    loader = PyPDFLoader('2104.02830.pdf')
data = loader.load()
    
    text_spl
itter = RecursiveCharacterTextSplitter(
 chunk_size=2000, 
 chunk_overlap=0,
)

    texts = text_splitter.split_document
s(data)
    
    import uuid

    for text in texts:
    id = uuid.uuid4().hex
    response = embeddings.embed_query(tex
t.page_content)
    vectors.append([(id, response, {'page': text.metadata['page'], 'text': text.page_content})])
    
  
  for vector in vectors:
    index.upsert(vector)
    
    query_embedding = embeddings.embed_query('author of this rese
arch paper')
result = index.query(vector=query_embedding , top_k=5, include_metadata=True)
print(result['matches'][0]['m
etadata']['text'])
result['matches'][0]['score']

    [{'id': 'ccd0dac490da4b4b947db97076cdf10d',
      'metadata': {'pa
ge': 5.0,
                   'text': 'novel image dataset for benchmarking machine learning '
                          
 'al-\n'
                           'gorithms. ArXiv , abs/1708.07747, 2017.\n'
                           '[20] X. Zou,
 X. Kong, W. Wong, C. Wang, Y . Liu, and Y '
                           '. Cao.\n'
                           'Fashionai
: A hierarchical dataset for fashion '
                           'understand-\n'
                           'ing. In 20
19 IEEE/CVF Conference on Computer Vision '
                           'and\n'
                           'Pattern Recog
nition Workshops (CVPRW) , pages 296–304,\n'
                           '2019.\n'
                           '6'},
     
 'score': 0.290649086,
      'values': []},
    

&#x200B;

It gives me reference links rather than author names.
```
---

     
 
all -  [ Do you really need more than one agent in your LLM chatbot? ](https://www.reddit.com/r/LangChain/comments/1aktwzi/do_you_really_need_more_than_one_agent_in_your/) , 2024-02-08-0909
```
Hello, I have a project to build a chatbot for E-commerce. This chatbot should interact with users and inform them about
 the products sold on the website. I tried using one agent to handle both interaction and task execution. However, when 
I only said 'Hi,' the bot returned a ValueError, something like 'LLM could not parse.' So, in this situation, do I need 
two agents? One to interact with users for out-of-context questions such as greetings or asking the bot's name, and the 
other to handle the thinking process for tasks such as finding today's discounts or locating gaming accessories? 
```
---

     
 
all -  [ Multi Document RAG using Agents ](https://www.reddit.com/r/LangChain/comments/1akroee/multi_document_rag_using_agents/) , 2024-02-08-0909
```
Hey everyone,
I just released a tutorial on how to make an agent interact with multiple vector databases with examples a
nd codes. Do check it out

[https://youtu.be/cBpdiQ3gljM?si=rfpFmlyGILHlIH4t
](https://youtu.be/cBpdiQ3gljM?si=rfpFmlyGI
LHlIH4t)
```
---

     
 
all -  [ Looking for simple framework to deploy a langchain (with multi-user support and session management) ](https://www.reddit.com/r/LocalLLaMA/comments/1akioj6/looking_for_simple_framework_to_deploy_a/) , 2024-02-08-0909
```
So I have been learning langchain, LLM and so on.   


I have a basic chatbot that incorporates a vector store of compan
y codebase and chat history that is working fine on my computer for single-user purpose.   


The chain can be invoked w
ith repeated calls like  


response = chatbot.invoke(  
{'messages': 'Give me Python codes for xyz'},  
 config={  
 'c
onfigurable': {'user\_id': 'user\_id', 'conversation\_id': 'conversation\_id'}  
},  
)  


Or invoked through langserve
 like  


chatbot = RemoteRunnable('blahblah/invoke')

response = chatbot.invoke(  
{'messages': 'My message to chatbot'
},  
{'configurable': {'user\_id': 'dummy', 'conversation\_id': 'dummy'}},  
)  


But I would like to deploy this basic
 chain so my colleagues can test their prompts.   


I am looking for a simple solution (if there is one) that can achie
ve the following:  


1. Accessible online (can be just internal network)
2. Multi-user support with session management

3. Optional: UI like chatgpt or similar

  
So far, I am willing to go with langserve if I can just figure out how to po
st a request that includes all the necessary fields. I tried following the examples in langserve tutorials but no dice s
o far. 

&#x200B;
```
---

     
 
all -  [ LangChain's extensibility is 🤯 ](https://www.reddit.com/r/LangChain/comments/1akfdm7/langchains_extensibility_is/) , 2024-02-08-0909
```
Hi all,

I started exploring lang chain recently and was really amazed by its extensibility. I have written my experienc
e as small tutorials and wanted to share the same with the community.

[Meet Your Digital Dream Team: Revolutionizing th
e Tech World with AI ](https://micromastery.github.io/posts/meet-your-digital-dream-team-revolutionizing-tech-world-with
-ai/) \- This is where I explored a python framework called Crew AI which allows creating collaborative AI using langcha
in tools

[Enhancing LLMs with Custom Capabilities: A Guide to Langchain and Text-to-Speech ](https://micromastery.githu
b.io/posts/customizing-llms-with-langchain-text-to-speech/) \- This is where I explored creation of custom tools for lan
g chain. I am using this day to day for creating voiceovers for videos.

Hope you find these useful.

Thanks
```
---

     
 
all -  [ Splitting documents (pdfs/html pages/txt files) into snippets with logical flow with Opensource tool ](https://www.reddit.com/r/LangChain/comments/1akc06q/splitting_documents_pdfshtml_pagestxt_files_into/) , 2024-02-08-0909
```
I have specific usecase of extracting structured (logically split) information from documents. Is there any parser that 
is opensource and does not need any particular API key ?   
The snippets would be sent to a RAG. This data would be used
 for internal usecases, so I would prefer a solution that would work for the same.
```
---

     
 
all -  [ Comedian Roasts LangChain. Hilarious and So True ](https://www.reddit.com/r/LangChain/comments/1akars1/comedian_roasts_langchain_hilarious_and_so_true/) , 2024-02-08-0909
```
I know this is way outdated from last year, and it's been floating around, but I just heard this, and I have to say, it'
s still hilarious. 😂

https://on.soundcloud.com/VQ1LwzKNgBDxYirq8
```
---

     
 
all -  [ Langchain js version vs python version ](https://www.reddit.com/r/LangChain/comments/1akao53/langchain_js_version_vs_python_version/) , 2024-02-08-0909
```
I've an idea of something to make with langchain and wikidata, however I'm not sure if the JS version supports the same 
plugins / functionality. I also can't tell if it supports GraphSparqlQAChain or something equivalent.  


What are every
ones thoughts on the two versions? Is the JS version mature enough to use?
```
---

     
 
all -  [ Why do the same prompts give different results with different language models? ](https://www.reddit.com/r/PromptEngineering/comments/1akakj7/why_do_the_same_prompts_give_different_results/) , 2024-02-08-0909
```
Hello everyone,  
  
I'm need some guidance on a document review project I'm working on, utilizing Gemini Pro and GPT-
4 through the Langchain framework. The aim is to input the document and scoring criteria, allowing the language model to
 generate scores accordingly.  
  
However, I'm encountering inconsistency issues. While I understand that different s
cores/responses are expected, my main concern is with the output formatting even though i have used the formatting schem
as/functions that langchain has. It seems to work seamlessly with Gemini Pro but presents challenges with GPT-4.  
  

I've attempted to adjust prompts to accommodate GPT-4, but this disrupts the performance with Gemini Pro. Does anyone ha
ve any advice or solutions for this dilemma? I'm relatively new to this field and would appreciate any insights. Thanks 
in advance! 🙏🏼  
  
  
  
  
  

```
---

     
 
all -  [ Machine Learning Engineer - 100% Remote (+ every other friday off!) ](https://www.reddit.com/r/MachineLearningJobs/comments/1ak956n/machine_learning_engineer_100_remote_every_other/) , 2024-02-08-0909
```
  
APPLY HERE: [https://grnh.se/cbc4e1997us](https://grnh.se/cbc4e1997us)  


Our Machine Learning teams build with the 
latest tools and launch for Silicon Valley startups and Life Science giants alike.

Join our team to work remotely, ship
 projects you’re proud be a part of, and enjoy every other Friday off (yes, we really take it 😎)

**The Role:**

* Under
standing of statistical, ML and deep learning algorithms
* Analyze errors of models and design strategies to overcome th
em
* Deploy, maintain, and upgrade ML models and pipelines
* Ambition to learn and grow into different industries with a
 modern tech stack
* Autonomy, adaptability and positivity (fully remote and globally distributed team)

**The Benefits:
**

* Every other Friday off (26 extra days off a year)
* LokaLabs™ incubator
* Relocation & Explore program (3 months o
r full relo)
* Remote and flexible
* Paid sick days and local holidays
* Fitness subscriptions and more

**Main Requirem
ents**:

* Bachelor's Degree in Computer Science or related
* 2+ years of ML engineering experience
* Experience with Py
thon, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, etc.)
* Proficient in English

**Bonus Points
 for Experience with…**

* Building GenAI solutions, namely prompt engineering (e.g: Langchain), fine-tuning and serving
 LLMs, search and embeddings, etc.
* MLOps, favorably in AWS (e.g: Sagemaker) as well as standards tools (e.g: MLFlow)
*
 Visualizing and manipulating big datasets
* NLP
```
---

     
 
all -  [ Asking LLMs 'Who are you and who created you?' reveals very interesting results ](https://www.reddit.com/r/LangChain/comments/1ak94ud/asking_llms_who_are_you_and_who_created_you/) , 2024-02-08-0909
```
I asked 6 llms 'Who are you and who created you?' 

* surprisingly most of them were created by OpenAI 😂
* Llama and Mix
tral were accurate most likely cause they're trained from scratch
* Tinyllama is my favourite

https://preview.redd.it/j
5ohzozrpygc1.png?width=796&format=png&auto=webp&s=894cefdfd1d9f3fe402e76917fac705e9ba3c327

[Here's the code I used for 
this](https://github.com/phidatahq/phidata/blob/main/cookbook/ollama/who_are_you.py)
```
---

     
 
all -  [ Learning, roadmap, basics, objectives and hard study ](https://www.reddit.com/r/artificial/comments/1ak85nw/learning_roadmap_basics_objectives_and_hard_study/) , 2024-02-08-0909
```
Hey everyone, your average AI student here. As I suppose if you are reading this is because you have an interest in lear
ning about AI, but for someone who is totally new to the subject or with previous knowledge the amount of variations and
 paths can be a bit confusing.

&#x200B;

The first thing to do is to have a specific focus on where to aim your studies
, being two possible paths quite simplified:

&#x200B;

1. Use models already created for specific utilities.
2. Create 
models

&#x200B;

As I said before these two paths are quite simplified and contain several modifications, for example i
n path 1, you have LLM, Langchain, Deep Learning and Machine Learning to name a few. But in path 2 you also have the sam
e but with other approaches.

&#x200B;

Well, after this introduction how do we approach the study? The first thing woul
d be to identify the target, once we have identified the target we move on to investigate the ramifications and little b
y little we enter the study.

&#x200B;

Learning the definitions and basic knowledge in the field is necessary, no matte
r what your objective is, knowledge always helps to learn more.

&#x200B;

Programming is also necessary C## or Pytorch 
depending the model.

&#x200B;

With this I hope to have made clear a basis of how to approach the study of AI in 2024, 
then I leave a couple of useful links for the study.

[https://huggingface.co](https://huggingface.co) \-- Models and do
cuments

[https://arxiv.org/pdf/2312.00752.pdf](https://arxiv.org/pdf/2312.00752.pdf)  \-- Mamba study

[https://course.
fast.ai](https://course.fast.ai) \-- AI introduction course

[https://github.com/oobabooga/text-generation-webui](https:
//github.com/oobabooga/text-generation-webui) \-- A great LLM introduction

[https://www.verses.ai](https://www.verses.a
i) \-- An interesting project

[https://paperswithcode.com](https://paperswithcode.com) \-- Practices

[https://www.cour
sera.org/learn/introduction-to-generative-ai](https://www.coursera.org/learn/introduction-to-generative-ai) \-- Course


[https://www.futuretools.io](https://www.futuretools.io) \-- Course

[https://teachablemachine.withgoogle.com](https://t
eachablemachine.withgoogle.com) \-- Couse

[https://www.langchain.com](https://www.langchain.com) \-- Langchain info

[h
ttps://spinningup.openai.com/en/latest/user/introduction.html](https://spinningup.openai.com/en/latest/user/introduction
.html) \-- Useful info

[http://www.r2d3.us/visual-intro-to-machine-learning-part-1/](http://www.r2d3.us/visual-intro-to
-machine-learning-part-1/) \-- ML introduction

[https://a16z.com/ai-canon/](https://a16z.com/ai-canon/) \-- Useful info


[https://cloud.google.com/learn/what-is-artificial-intelligence?hl=es](https://cloud.google.com/learn/what-is-artifici
al-intelligence?hl=es) \-- AI introduction

[https://github.com/cloudanum/50algorithms/tree/main](https://github.com/clo
udanum/50algorithms/tree/main) \-- Useful maths info

[https://www.kaggle.com](https://www.kaggle.com) \-- ML resources 
site

[https://www.fast.ai](https://www.fast.ai) \-- Useful info

[https://www.oreilly.com/library/view/50-algorithms-ev
ery/9781803247762/](https://www.oreilly.com/library/view/50-algorithms-every/9781803247762/) \-- Math book

[https://www
.deeplearning.ai/resources/](https://www.deeplearning.ai/resources/) \-- Useful info

[https://github.com/KoboldAI/Kobol
dAI-Client](https://github.com/KoboldAI/KoboldAI-Client) \-- An useful project

[https://github.com/artidoro/qlora](http
s://github.com/artidoro/qlora) \-- Another useful project

&#x200B;

I also highly recommend learning to use [https://gi
thub.com](https://github.com) and [https://www.tensorflow.org/?hl=es-419](https://www.tensorflow.org/?hl=es-419)

&#x200
B;

And learn to research! There is free info in youtube and reddit!

&#x200B;

Information and research is always chang
ing and updating, even more so in a popular subject like AI, feel free to contribute to the post with more information o
r correcting mine if I have made a mistake.
```
---

     
 
all -  [ Can/how to achieve find most recent release notes? ](https://www.reddit.com/r/LangChain/comments/1ak82pc/canhow_to_achieve_find_most_recent_release_notes/) , 2024-02-08-0909
```
I have already created faiss embeddings for all of my release notes which definitely has dates inside among with compone
nts versions and features. 

I have put together a simple conversation retrieval qa chain to answer user questions. 

I 
found out it doesn't answer when questions are temporal e.g. from most recent release notes what was the component versi
on released.

I tried putting datetime.now() output as context in the user question to provide context for 'latest '


H
ow can I achieve this? Is my architecture incorrect or there's a better architecture?

Thanks,
```
---

     
 
all -  [ Langchain Chatbot in production ](https://www.reddit.com/r/LangChain/comments/1ak7lzj/langchain_chatbot_in_production/) , 2024-02-08-0909
```
Is quite easy to create a chatbot with langchain LCEL and using the buffer memory, but what if in production I wanna sto
re the history of the conversation in a db and not in the RAM and retrieve it when the user restart the conversation wit
h the chatbot? I cannot find a tuto anywhere. Has anyone already tried to do it??
```
---

     
 
all -  [ OSS version of Grimoire (GPT) ](https://www.reddit.com/r/LangChain/comments/1ak7knz/oss_version_of_grimoire_gpt/) , 2024-02-08-0909
```
I have been using this GPT for a while and it's responses are far superior to just using GPT-4.  I understand that it is
 just prompt engineering but it seems to improve the user experience and the quality of code significantly.  
I would lo
ve to see/build something like this with open-source models. Does anyone know what kind of prompts can be used to make s
omething similar?

Link to GPT - [https://chat.openai.com/g/g-n7Rs0IK86-grimoire](https://chat.openai.com/g/g-n7Rs0IK86-
grimoire)

TIA.
```
---

     
 
all -  [ Unleashing the Power of LangChain for Developing Cutting-Edge LLM Applications ](https://www.reddit.com/r/LangChain/comments/1ak52h7/unleashing_the_power_of_langchain_for_developing/) , 2024-02-08-0909
```
 

Hey everyone! I've been diving deep into the world of Large Language Models (LLMs) for the past one year; and I have 
been leveraging on the power of **LangChain**. For those who might not be familiar, LangChain is a framework designed to
 streamline and enhance the development of applications based on Large Language Models like GPT (Generative Pre-trained 
Transformer) and others. I wanted to share some insights into what makes LangChain a game-changer and how developers can
 leverage it to create more sophisticated and efficient LLM applications.

I personally run an AI startup called [Afrine
uron](https://afrineuron.com/) and have been intergrating Langchain into some of my applications! Follow the link to see
 some of our real world AI Applications.

### Benefits of LangChain:

1. **Simplified Integration:** LangChain offers to
ols that make it easier to integrate LLMs into applications. This means less time wrestling with API integrations and mo
re time focusing on building out the unique aspects of your application.
2. **Enhanced Functionality:** With LangChain, 
developers can extend the capabilities of LLMs beyond simple text generation. It facilitates the creation of application
s that can understand context, make decisions, and even interact with other software services or databases.
3. **Modular
 and Flexible:** The framework is designed to be modular, allowing developers to pick and choose the components they nee
d. This flexibility enables the development of bespoke solutions tailored to specific requirements without being locked 
into a one-size-fits-all approach.
4. **Community and Resources:** LangChain is backed by a growing community of develop
ers and researchers. This community-driven approach ensures a wealth of shared knowledge, resources, and best practices 
that can accelerate development and innovation.
5. **Cost Efficiency:** By optimizing how and when LLMs are queried, Lan
gChain can help reduce operational costs. Efficient use of LLMs is crucial as the computational resources they require c
an become significant at scale.

### Leveraging LangChain for LLM Applications:

1. **Custom Chatbots and Virtual Assist
ants:** Developers can use LangChain to build sophisticated chatbots that understand complex queries, context, and even 
maintain state over a conversation, providing a more natural and engaging user experience.
2. **Content Creation and Sum
marization:** LangChain can enhance applications focused on generating or summarizing content by adding layers of contex
t-awareness and ensuring the output is more relevant and tailored to specific user needs.
3. **Data Analysis and Insight
 Generation:** Applications that sift through large volumes of data to generate insights can benefit from LangChain's ab
ility to integrate with databases and process information in a more nuanced and human-like manner.
4. **Educational and 
Training Tools:** LangChain can power educational applications that provide personalized learning experiences, leveragin
g LLMs to adapt content and feedback to the learner's progress and understanding.
5. **Interactive Entertainment:** From
 interactive stories to games that adapt to players' inputs in creative ways, LangChain opens up new possibilities for e
ntertainment software.

### Getting Started:

For those interested in exploring LangChain, the project is accessible and
 well-documented [here](https://python.langchain.com/docs/get_started/introduction). Starting involves familiarizing you
rself with its architecture, understanding the core components, and then experimenting with building small applications 
to grasp its capabilities fully.

In conclusion, LangChain represents a significant leap forward in the development of L
LM-based applications. Its benefits of simplification, enhanced functionality, and cost efficiency make it an invaluable
 tool for developers looking to push the boundaries of what's possible with language models. Whether you're a seasoned d
eveloper or just starting, LangChain offers the tools and community support to bring your innovative ideas to life.

I'm
 excited to see what the community will build with LangChain, and I encourage everyone to dive in, experiment, and share
 your creations!

Feel free to share your thoughts, experiences, or any cool projects you've worked on using LangChain. 
Let's learn and grow together in this exciting field!
```
---

     
 
all -  [ How to build a hotel booking bot ? ](https://www.reddit.com/r/LangChain/comments/1ak4jq6/how_to_build_a_hotel_booking_bot/) , 2024-02-08-0909
```
Hello, I am new to lang chain. I am looking to build a basic hotels booking bot with langchain. What are steps I should 
follow?

Will langchain be enough ? How do I add RAG to this bot.
```
---

     
 
all -  [ Is using LlamaIndex with Langchain recommended? ](https://www.reddit.com/r/LangChain/comments/1ak3zkl/is_using_llamaindex_with_langchain_recommended/) , 2024-02-08-0909
```
I have Langsmith access so staying completely within the Langchain ecosystem seems like the better thing to do so I can 
trace my app's inner working but is anyone using both and finding it advantageous?  Or I could be wrong that using Llama
Index would not let me trace calls to vector stores from Langsmith.  
```
---

     
 
all -  [ When translating HTML to another language using LangChain ](https://www.reddit.com/r/LangChain/comments/1ak1d7y/when_translating_html_to_another_language_using/) , 2024-02-08-0909
```
Let's say you are translating HTML into another language using LangChain. Do you have a good idea?

However, only the te
xt must be changed to a different language while maintaining the style and formatting.
```
---

     
 
all -  [ JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1) ](https://www.reddit.com/r/LangChain/comments/1ak071x/jsondecodeerror_expecting_property_name_enclosed/) , 2024-02-08-0909
```
 When using the JSON document loader, my JSON file is formatted correctly with double quotes enclosing property names. H
owever, an error indicates that it is being read with single quotes. 

from langchain\_community.document\_loaders impor
t JSONLoader  
loader = JSONLoader(  
 file\_path='theJSON/1.json',  
 jq\_schema='.',  
 content\_key='sentences',  
 j
son\_lines=True)  
data = loader.load()  


my json file:

{  
 'block\_class': 'cls\_0',  
 'block\_idx': 0,  
 'level'
: 0,  
 'page\_idx': 2,  
 'sentences': \[  
 'MESSAGE'  
\],  
 'tag': 'header'  
}
```
---

     
 
all -  [ ReAct agent with open source API/endpoint connection ](https://www.reddit.com/r/LangChain/comments/1ajzk01/react_agent_with_open_source_apiendpoint/) , 2024-02-08-0909
```
**I am trying to connect LLama2 via HGF inference endpoints to ReAct agent. Is this something possible? I have receiver 
error stating**

NotImplementedError                       Traceback (most recent call last)

<ipython-input-35-4c40a96c
8398> in <cell line: 2>()

1 agent.reset()

\----> 2 response = [agent.chat](https://agent.chat)('perkenalkan saya denga
n kursus tersebut')

3 print(response)

8 frames

/usr/local/lib/python3.10/dist-packages/llama\_index/llms/huggingface.
py in chat\_messages\_to\_conversational\_kwargs(messages)

373     '''Convert ChatMessages to keyword arguments for Inf
erence API conversational.'''

374     if len(messages) % 2 != 1:

\--> 375         raise NotImplementedError('Messages 
passed in must be of odd length.')

376     last\_message = messages\[-1\]

377     kwargs: Dict\[str, Any\] = {

NotImp
lementedError: Messages passed in must be of odd length.

**Previously I have also had issues with using MistralAI API w
ith the same answer.**  
**Please could anyone provide a suggestion to get past this block I am having?**
```
---

     
 
all -  [ Haystack > Langchain ](https://www.reddit.com/r/LangChain/comments/1ajxqri/haystack_langchain/) , 2024-02-08-0909
```
Hey everyone, I often have commented here that haystack is the grown up alternative to langchain, but haven't had much t
ime to explain why. So I wrote an article here: [https://medium.com/p/94f65fca13df](https://medium.com/p/94f65fca13df) G
ive it a read, or just drop your thoughts on the comparison here. I like to hear others POV
```
---

     
 
all -  [ AI for Finance/Investment Research ](https://www.reddit.com/r/LangChain/comments/1ajmnlo/ai_for_financeinvestment_research/) , 2024-02-08-0909
```
## Hi guys! Here I describe how to build an AI Assistant for Investment Research using 🦜LangChain LCEL Agent and u/strea
mlit . 

This is a first, still robust version which includes:  
🌿 Company Profile Retrieval (market cap, profit margins
, revenue, earnings, etc.),  
🌿 News and Events Search (M&A deals, company news, etc.),  
🌿 Analytical Operations via SQ
L on stock market performance,  
🌿 Python Code Execution on complex calculations like correlations and plotting,  
🌿 u/s
treamlit Integration.

🤖 Read the full article here: [https://medium.com/@oleg.davydiuk1995/building-ai-assistant-for-in
vestment-research-part-1-b775eb11ba4a](https://medium.com/@oleg.davydiuk1995/building-ai-assistant-for-investment-resear
ch-part-1-b775eb11ba4a)

👾 This and more Agents in Finance examples on this GitHub repository with descriptions and inst
ructions for usage:  
[https://github.com/Arkad-Finance/arkad-demo](https://github.com/Arkad-Finance/arkad-demo)

I will
 constantly improve this Agent and share my journey by dropping new articles and making open-source reusable modules:) A
ppreciate your feedback:)

&#x200B;
```
---

     
 
all -  [ Chat with arXiv papers using function calling ](https://www.reddit.com/r/LangChain/comments/1ajit2n/chat_with_arxiv_papers_using_function_calling/) , 2024-02-08-0909
```
Hi all, I built an app to chat with arXiv papers: [https://arxiv.aidev.run](https://arxiv.aidev.run/)

I’m using functio
n calling to interact with the arXiv api, here’s the general flow:

1. For a users question, search the knowledge base (
pgvector) for the topic/paper
2. If knowledge base results are not relevant, search arXiv api for paper, parse it and st
ore it in the knowledge base
3. Answer questions or summarize using contents from the knowledge base. 

Give it a spin a
t: [https://arxiv.aidev.run](https://arxiv.aidev.run/) and let me know what you think. See the last question where it co
mpares FlashAttention and FlashAttention2.

https://reddit.com/link/1ajit2n/video/sfnncbyl7sgc1/player

Its a work in pr
ogress and I’m looking for feedback on how to improve. The read time from the arXiv api is slow – but not much I can do 
about it. The video is at 2x speed so not real inference.

Here’s the [code](https://github.com/phidatahq/ai-cookbook/bl
ob/main/arxiv_ai/assistant.py#L21) if you’re interested, I used [phidata](https://github.com/phidatahq/phidata) to build
 this.
```
---

     
 
all -  [ Creating LLMs Apps on Chemical CSV Data ](https://www.reddit.com/r/cheminformatics/comments/1ajif6w/creating_llms_apps_on_chemical_csv_data/) , 2024-02-08-0909
```
[https://medium.com/@sharifsuliman/converting-your-knowledge-graph-csv-into-a-large-language-model-with-langchain-and-ch
ainlit-475c8c1b8073](https://medium.com/@sharifsuliman/converting-your-knowledge-graph-csv-into-a-large-language-model-w
ith-langchain-and-chainlit-475c8c1b8073)

Still working on making this CSV agent better but I figured in the future thes
e CSV agents on domain specific chemical data will be useful. 
```
---

     
 
all -  [ 🔥 [FOR HIRE]. AI Chatbot | ChatGPT | Langchain | VectorDB | Huggingface | Prompt Engineering | NLP ](https://www.reddit.com/r/ForHire_AI/comments/1ajflae/for_hire_ai_chatbot_chatgpt_langchain_vectordb/) , 2024-02-08-0909
```
[https://remoteai.io/talent/profile/@eastonjim](https://remoteai.io/talent/profile/@eastonjim)
```
---

     
 
all -  [ is there an alternative for system, user and assistant messages in langchain? ](https://www.reddit.com/r/Langchaindev/comments/1ajaj12/is_there_an_alternative_for_system_user_and/) , 2024-02-08-0909
```
I'm trying to write some messages that I want the openai api to learn form, I used to do so by entering user and assista
nt messages into the messages parameter from the openai library like so

    from openai import OpenAI
    
    client =
 OpenAI()
    
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[{'role': 'user', 
'content': 'Say this is a test'},
                  {'role': 'assistant', 'content' 'this is a test'},
                 
 {'role': 'user', 'content' 'you are good at this'},
                  {'role': 'assistant', 'content' 'thanks 😃!'},
   
 ])


 I want to do the same thing into langchain. I got here so far

    from langchain_core.messages import HumanMessa
ge, AIMessage, SystemMessage
    
    chat_history = []
    
    system_message = '''a system message'''
    
    chat_h
istory += [SystemMessage(content=f'{system_message}')]
    
    for i in range(len(faq)):
        chat_history += [
    
        HumanMessage(content=f'{faq['question'][i]}'),
            AIMessage(content=f'{faq['answer'][i]}')
        ]
  
  
    chain = ConversationalRetrievalChain.from_llm(llm, retriever)
    
    
    query = input('')
    
    response =
 chain({'question': query,
                     'chat_history': chat_history})

is this way correct?

When I want to ask
 the chatbot about something that exist in the faq dataframe I want it to give me an answer that exist in the same dataf
rame
```
---

     
 
all -  [ Resume buildup ](https://www.reddit.com/r/resumes/comments/1aja0fb/resume_buildup/) , 2024-02-08-0909
```
Hi, i am an undergrad cs major, i needed help with my resume, I'd love your input on this, how can i rewrite the content
 in my resume for a better perspective of being a ai/ml engineer or a data analyst/data scientist?

 

[need help with r
esume](https://preview.redd.it/q6ej5pjinpgc1.png?width=869&format=png&auto=webp&s=4061b2a9c81ad8a84327b03232d9c9016bfa45
42)
```
---

     
 
all -  [ How to request translation of a very long document to LangChain? ](https://www.reddit.com/r/LangChain/comments/1aj7q8x/how_to_request_translation_of_a_very_long/) , 2024-02-08-0909
```
The documents may be very long, resulting in errors exceeding tokens per minute

If I ask to translate a long document a
t the LangChain prompt, how can I do so efficiently?

I even went so far as to separate it into chunks. The current logi
c is hard-coded to enter prompts one by one from doc\[0\] to doc\[5\].

Is there a way to do this efficiently?

I would 
appreciate it if you could also provide example code.
```
---

     
 
all -  [ My raw story of using Langchain to build my DIY chatbot ](https://www.reddit.com/r/LangChain/comments/1aj5mnq/my_raw_story_of_using_langchain_to_build_my_diy/) , 2024-02-08-0909
```
I am not sure if this is appropriate to post so have been delaying it for a while. I have seen a few posts in this sub a
bout how terrible Langchain documentation is. However, I have had a very different experience. 
For context, i am a midd
le age advertising professional with zero coding experience until like 1 year ago. I built my first DIY clunky chatbot, 
using RAG with my own blog data last year. 
It was a bad build, a terrible build but a baby step for someone like myself
. I came across Langchain mid last year through the news and Deep Learning AI courses but I didnt have enough knowledge 
at that time to follow the jupyter notebooks. 
Fast forward until recently, i stumbled upon Langchain again as it was me
ntioned in another training course so I gave it another try. The experience has been great so far. I managed to build th
e chatbot for 450+ blog posts with much simpler code, using Langchain framework, FAISS as vector store and max marginal 
relevance as the options for the retriever. You can check out my full raw story and my full open source code [here](http
s://www.chandlernguyen.com/blog/2024/01/29/how-i-emerged-from-coding-quicksand-with-an-ai-agent/).

So TL;DR: i will spe
nd more time with Langchain to learn more about agent and see what i can build myself with tons of community integration
.
```
---

     
 
all -  [ Ollama vision using Llava running locally on my macbook. Inference speed is 🔥 ](https://www.reddit.com/r/LangChain/comments/1aivgaa/ollama_vision_using_llava_running_locally_on_my/) , 2024-02-08-0909
```
https://reddit.com/link/1aivgaa/video/xwtl03439mgc1/player

[Code if interested.](https://github.com/phidatahq/phidata/b
lob/main/cookbook/ollama/image.py)
```
---

     
 
all -  [ How to use AzureOpenAI Embeddings with ChromDB or FAISS? ](https://www.reddit.com/r/LangChain/comments/1airll4/how_to_use_azureopenai_embeddings_with_chromdb_or/) , 2024-02-08-0909
```
Hi guys,
           I tried langchain-openai's Azure Embedding abstraction, but am getting multiple errors when I try it
 with Chroma or FAISS. May I know a solution for this?
```
---

     
 
all -  [ Is function calling supported with RAG? ](https://www.reddit.com/r/LangChain/comments/1aio67k/is_function_calling_supported_with_rag/) , 2024-02-08-0909
```
I  am currently looking for a solution to extract details from documents I ingested into vectorstore to a structure json
 format.

I know I can first just ask it to retrieve stuff I want from the document as plain string and send it again to
 using fn calling to put bits and pieces into json obj.

Is this possible at the moment with just one shot request?
I lo
oked up pretty much all available options on langchain but cannot seem to find one.

Anyone tried this combination befor
e?
```
---

     
 
all -  [ Why are basic things not documented correctly, never seem to work? ](https://www.reddit.com/r/LangChain/comments/1aimin7/why_are_basic_things_not_documented_correctly/) , 2024-02-08-0909
```
Maybe I'm doing something wrong, but I wanted to test out output parsers today with all the new updates so I go through 
the docs to put together a basic example. I copy it and keep getting an error:

&#x200B;

&#x200B;

[TypeError: langchai
n\_core.prompts.prompt.PromptTemplate\(\) got multiple values for keyword argument 'input\_variables'](https://preview.r
edd.it/2jx7f2og7kgc1.png?width=1002&format=png&auto=webp&s=27371552aa733df1d43c37867abcc0243b7fc512)

&#x200B;

I had to
 remove the 'input\_variables' arg from the PromptTemplate for it to work. What is frustrating me is that these kinds of
 issues are abundant. Nothing in the docs is every up to date. 
```
---

     
 
all -  [ Best AI Research agent? ](https://www.reddit.com/r/OpenAI/comments/1aijjj9/best_ai_research_agent/) , 2024-02-08-0909
```
Looking for a Research tool that is able to complete in depth research tasks through browsing online. Copilot/bing aren’
t thorough enough, and remember coming across a langchain based one a while back but can’t remember the name of the proj
ect.
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-08-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-08-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-08-0909
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-08-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-08-0909
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-02-08-0909
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-08-0909
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-08-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-08-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-02-08-0909
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
