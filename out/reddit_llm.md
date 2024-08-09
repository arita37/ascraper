 
all -  [ Text Similarity between News article titles ](https://www.reddit.com/r/LangChain/comments/1enksd4/text_similarity_between_news_article_titles/) , 2024-08-09-0911
```
I am nearly 500 articles scraped and am currently trying to group them by what stories are the same. For this, I wanted 
to use text similarity to check how similar the titles are. For example

Britons in Lebanon could be evacuated by more  
 
Britons in Lebanon on standby for evacuation 

are the same story by with different wording. Obviously, in this case i
ts very obvious and something like Jacquard Index could be used. But in other scenarious it gets more complicated. Diffe
rent wording but the same story.  
Using this site [https://similarity-demo.newscatcherapi.com/](https://similarity-demo
.newscatcherapi.com/) I checked that cosine and word2Vec has the highest success. I checked an implementation of word2Ve
c and you need to build a model just to check the similarity. I have to process near 500 titles and group them, theres a
lready a lot of computation involved and I need to grab this data in real time. Is there a way to check the similarity w
ithout having to do it from scratch ?

  
If anyone can suggest a better way please let me know

  

```
---

     
 
all -  [ Seeking In-Depth Information on Perplexity's Sonar Models: System Messages, Context Handling, and AP ](https://www.reddit.com/r/LangChain/comments/1enk44f/seeking_indepth_information_on_perplexitys_sonar/) , 2024-08-09-0911
```
Is there any documentation about Sonar models beyond what's provided in the Perplexity docs?

I'm seeking more informati
on about the differences in behavior between the 'system message,' prompt, and/or first user request. From what I unders
tand, the query is generated based on the 'user' message, and query generation ignores the 'system' message. So what exa
ctly is the purpose of this 'system' message? The examples typically use short 3-4 word phrases, but do Sonar models sup
port more complex system instructions (similar to the models they're trained on)?

Additionally, how do online models ha
ndle multi-turn conversations? What context is used for query generation and RAG? I understand these models are intended
 for single-turn interactions, with 'chat' versions available for multi-turn conversations.

This leads to my question a
bout context length. The online model claims a 128K context, but this seems unattainable in practice. If the user messag
e is too long, query generation becomes less effective and retrieves less relevant results. Higher context can't even be
 achieved with multi-turn chats, as the quality drops significantly.

It's worth noting that the number of tokens provid
ed to the model as 'sources' is generally in the range of 2-3K globally, but often much less depending on the complexity
 of the question (via the API).

Does anyone have insights into these issues? Could someone from the staff please point 
me towards more detailed information?

Thanks in advance! 
```
---

     
 
all -  [ How do you tackle a “time aware” RAG use case? ](https://www.reddit.com/r/LangChain/comments/1enk2hx/how_do_you_tackle_a_time_aware_rag_use_case/) , 2024-08-09-0911
```
Hey y’all!

I’m working through a RAG solution (not my first) and stumbled into a problem I hadn’t thought of yet: retri
eving documents based on time. 

The idea is that you could ask “Provide a summary of what happened in the past 24 hours
?” or “I was out for 5 weeks, what did I miss?”

The documents in the vectordb (pgvector for now) are diverse and made u
p of knowledge bases and ticketing systems. 

Q&A with similarity is easy. This time thing threw me for a loop. 

Best I
 could up with so far is having the time/date of the article saved in something like epoch form in the metadata then, ha
ve one LLM asses the user’s request and if it has a time range, respond in JSON format with start/end values. And then, 
filter on the date value on the metadata. 

I saw timescale but haven’t done a bunch of research on it yet. I’ve also se
en document retrieval with time decay. That looks interesting. 

Just curious if any of you have had this problem and so
lved it already?

Thanks and cheers!
```
---

     
 
all -  [ 🧰 agent-service-toolkit: Full toolkit for running agent as a service built with LangGraph, FastAPI a ](https://www.reddit.com/r/LangChain/comments/1engrgq/agentservicetoolkit_full_toolkit_for_running/) , 2024-08-09-0911
```
🧰 Introducing agent-service-toolkit, a new open source toolkit for running an AI agent as a service using LangGraph, Fas
tAPI and Streamlit.

* View the repo: [https://github.com/JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC21
5/agent-service-toolkit)
* Try the app: [https://agent-service-toolkit.streamlit.app/](https://agent-service-toolkit.str
eamlit.app/)
* Watch the video: [https://www.youtube.com/watch?v=VqQti9nGoe4](https://www.youtube.com/watch?v=VqQti9nGoe
4)

I wanted to build a few agents for personal projects using the Compound AI Systems approach, and found that LangGrap
h is the most advanced framework with the features I needed today. But serving and interacting with the agent was painfu
l and complicated unless I wanted to use LangGraph Cloud (still in closed beta), and that wouldn't support my own infras
tructure.

I built agent-service-toolkit to solve this problem so I can focus on just the agent logic and core AI system
s for my projects in the future. It uses async-first and FastAPI to be blazing fast and production-ready, with a Streaml
it app for easy sharing and rapid iteration.

[Architecture](https://preview.redd.it/bj51l3w65ihd1.png?width=1619&format
=png&auto=webp&s=1519d1fbe5f8c1a796c4a5b023d7b107cde40c5c)

[App in action](https://preview.redd.it/h5fbanv75ihd1.png?wi
dth=1276&format=png&auto=webp&s=52a483eb644c9c540d870845ebb4baac316f2bd9)


```
---

     
 
all -  [ LLM Evals with open-source CROWDLAB ](https://www.reddit.com/r/LangChain/comments/1engmlq/llm_evals_with_opensource_crowdlab/) , 2024-08-09-0911
```
A couple years ago, we [announced](https://www.reddit.com/r/MachineLearning/comments/xwf38u/r_announcing_crowdlab_openso
urce_tools_for_data/) open-source CROWDLAB for multiannotator labels. We've now seen that these annotator algorithms are
 also useful for LLM Evals in RAG applications, and wrote a short tutorial on how to do so: https://cleanlab.ai/blog/tea
m-llm-evals/. Hope you find it useful, and would love to know what folks are using for LLM Evals! 
```
---

     
 
all -  [ How do I find a job? ](https://www.reddit.com/r/careerguidance/comments/1enghf7/how_do_i_find_a_job/) , 2024-08-09-0911
```
I am really frustrated these days. I am a Full Stack Web Developer having experience in PHP, JS, Python Frameworks I hav
e also worked with langchain but the issue is I just don’t know if i am good enough I can’t get that confidence to overc
ome the fear’s I have.

Any suggestions on how to improve? And yea I am currently focusing on my DevOps skills too.
```
---

     
 
all -  [ What are your biggest challenges in RAG? ](https://www.reddit.com/r/LangChain/comments/1ene81o/what_are_your_biggest_challenges_in_rag/) , 2024-08-09-0911
```
Out of curiosity - what do you struggle most with when it comes to doing RAG (properly)? There are so many frameworks, r
epos and solutions out there these days that for most challenges there seems to be an out-of-the-box solution, so what's
 left? Does not have to be confined to just Langchain.
```
---

     
 
all -  [ Dubbi su offerta post-tirocinio universitario (probabile co.co.co.) ](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1encn3s/dubbi_su_offerta_posttirocinio_universitario/) , 2024-08-09-0911
```
tl;dr: l'azienda con cui ho fatto il tirocinio in università mi offre un co.co.co. in un ruolo diverso da quello svolto 
durante il tirocinio. Consigli?

Per chi avesse voglia di leggere: ho appena terminato la triennale (Informatica). Ho sv
olto i 6 CFU obbligatori di tirocinio presso una certa azienda, occupandomi di analisi dati e sviluppo di un sistema di 
raccomandazione, da cui ho anche scritto la tesi, e con una già accennata possibilità di assunzione post-laurea. Tengo a
 specificare che si parla di sud Italia.

Veniamo al dunque: qualche giorno fa mi propongono questo 'contratto di collab
orazione' (a questo punto credo sia proprio un co.co.co.) da 30h/settimana, quasi full-remote e orario a detta loro TOTA
LMENTE flessibile. Questo per permettermi di lavorare e studiare (magistrale) contemporaneamente. 

I miei dubbi:

1. Il
 ruolo che mi hanno proposto è abbastanza differente da quello che ho fatto durante il tirocinio (data science/ML, se co
sì si può definire) e, soprattutto, è qualcosa in cui io sono praticamente bianco (sviluppo di un gestionale ERP in Java
, mentre io sto cercando di specializzarmi in appunto data science e machine learning/deep learning). Si dà il caso che 
l'unica mia esperienza con Java sia stato un corso di ingegneria del software da 9 CFU, mentre con Python e librerie var
ie (pandas, scikit-learn, langchain ecc.) mi senta molto più sicuro, anche se ancora ad un livello junior. Secondo il vo
stro parere, quanto è probabile che mi forniscano un minimo di formazione (anche un senior che mi segua, non per forza u
n corso) piuttosto che sia lasciato a me stesso a leggere il loro codice e cercare tutorial su internet? Sempre a detta 
loro, potrei ritrovarmi comunque a dover integrare 'l'AI', qualunque cosa significhi, in questo progetto.

2. Il 'contra
tto di collaborazione'. Cercando su internet e anche su questo sub, mi sembra che questo tipo di contratto sia considera
to uno dei peggiori, in pratica peggio di una fake partita IVA, dato che è legale. Assumendo che l'orario sia veramente 
flessibile (nel senso che potenzialmente potrei fare 5h di queste 30 anche dalle 22 alle 3 di notte, ad esempio), questi
 tipi di contratti sono così tanto svantaggiosi per il lavoratore?

3. Non mi hanno ancora parlato di RAL (lo faranno so
ltanto se esprimo parere positivo nell'approfondire la valutazione di quest'offerta): quanto potrei realisticamente aspe
ttarmi?

4. Se volessi proseguire in campo data science o AI (in generale), magari cercando di applicare per qualche int
ernship in aziende grandi nell'ambito, come verrebbe vista un'esperienza completamente scollegata da ciò? L'alternativa 
sarebbe comunque non avere nessuna esperienza lavorativa da mettere nel CV.


Vi ringrazio in anticipo per i consigli


```
---

     
 
all -  [ Token indices sequence length is longer than the specified maximum sequence length for this model (2 ](https://www.reddit.com/r/LangChain/comments/1enbsrw/token_indices_sequence_length_is_longer_than_the/) , 2024-08-09-0911
```
Hello Community,

  
I am trying to summarize using map\_reduce implementation and I have a text file that has \~78000 t
oken(according to Open AI tokenizer) and I am using mistralai/Mistral-7B-Instruct-v0.3 model through huggingface inferen
ce and I run into the above error and the ouputs gets cut off in the middle. Can you please advice how to fix this? The 
model has a context length of 32K but I am not sure why the error says 1024 tokens. Here is the full error  
Token indic
es sequence length is longer than the specified maximum sequence length for this model (20098 > 1024). Running this sequ
ence through the model will result in indexing errors.  
Here is the code  


from langchain.chains.combine\_documents.s
tuff import StuffDocumentsChain

from langchain.chains.llm import LLMChain

from langchain.prompts import PromptTemplate


from langchain.schema.document import Document

from langchain.chains.combine\_documents.stuff import StuffDocumentsCh
ain

from langchain.chains.llm import LLMChain

from langchain.prompts import PromptTemplate

from langchain.chains.summ
arize import load\_summarize\_chain

#type the code to be ready for tomorrow:

from langchain.chains import MapReduceDoc
umentsChain, ReduceDocumentsChain









# Map

map\_template = '''<s>\[INST\]Please write a clear and concise summary
 for the following text.\[/INST\]

Text:

  '{docs}'</s>

  \[INST\] Summary:\[/INST\]



 '''

map\_prompt = PromptTemp
late.from\_template(map\_template)

map\_chain = LLMChain(llm=api\_llm, prompt=map\_prompt)



# Reduce

reduce\_templat
e =  '''<s>\[INST\]Below are the summaries of multiple segments of a document. Please combine these summaries to form a 
meaningful final summary.\[/INST\]

Text:

  '{doc\_summaries}'</s>

  \[INST\] Summary:\[/INST\]



 '''

reduce\_promp
t = PromptTemplate.from\_template(reduce\_template)



# Run chain

reduce\_chain = LLMChain(llm=api\_llm, prompt=reduce
\_prompt)



# Takes a list of documents, combines them into a single string, and passes this to an LLMChain

combine\_d
ocuments\_chain = StuffDocumentsChain(

llm\_chain=reduce\_chain, document\_variable\_name='doc\_summaries'

)



# Comb
ines and iteratively reduces the mapped documents

reduce\_documents\_chain = ReduceDocumentsChain(

# This is final cha
in that is called.

combine\_documents\_chain=combine\_documents\_chain,

# If documents exceed context for \`StuffDocum
entsChain\`

collapse\_documents\_chain=combine\_documents\_chain,

# The maximum number of tokens to group documents in
to.

token\_max=4000,

)



# Combining documents by mapping a chain over them, then combining results

map\_reduce\_cha
in = MapReduceDocumentsChain(

# Map chain

llm\_chain=map\_chain,

# Reduce chain

reduce\_documents\_chain=reduce\_doc
uments\_chain,

# The variable name in the llm\_chain to put the documents in

document\_variable\_name='docs',

# Retur
n the results of the map steps in the output

return\_intermediate\_steps=True,

)



#text\_splitter = CharacterTextSpl
itter.from\_tiktoken\_encoder(

#    chunk\_size=1000, chunk\_overlap=0

#)

#split\_docs = text\_splitter.split\_docume
nts(docs)

splitter = RecursiveCharacterTextSplitter(chunk\_size=4000, chunk\_overlap=200,length\_function = len)

chunk
s = splitter.create\_documents(\[text\])



result=map\_reduce\_chain.invoke(chunks)

print(result\['output\_text'\])


```
---

     
 
all -  [ Multimodal RAG Explainer: 3 Paths to Integrating Text, Images and Audio in RAG, Which One is Best? ](https://www.reddit.com/r/LangChain/comments/1enbqew/multimodal_rag_explainer_3_paths_to_integrating/) , 2024-08-09-0911
```
https://preview.redd.it/h283ore4zghd1.png?width=1600&format=png&auto=webp&s=16b9c6a5b9cdbe1c5107b886cb1769fa364e2917

Hi
 All,

This post is a adaptation of a Multimodal episode of RAG Masters, a weekly Youtube show I do with Daniel Warfield
.  Each week we explore a different topic to help engineers build better RAG.  Some times we know a lot. Sometimes we're
 learning as we go, just like everyone.

The show is here if you want to check it out, but I'll keep posting a lot of th
e content here regardless.

[https://www.youtube.com/watch?v=ZetGV7gtyQw](https://www.youtube.com/watch?v=ZetGV7gtyQw)


Also, my shop [EyeLevel.ai](http://EyeLevel.ai) has some kick ass tools for building advanced RAG in just a few API call
s with SOTA accuracy. The APIs are especially good with complex documents.

Ok, on to the post.

# What is Multimodal RA
G?

Multimodal RAG is an advanced extension of traditional Retrieval-Augmented Generation systems. Classic RAG involves 
a retrieval engine that searches a database of text documents to find relevant information and injects this data into a 
prompt for a language model to generate a response. Multimodal RAG expands this by including non-text data types, which 
enhances the model's ability to understand and generate responses based on a more comprehensive set of inputs.

Taking m
ultimodal inputs allows for RAG engineers to build a more complex retrieval engine that can ask a store of information a
bout information across different mediums. This means that the retrieval engine can grab data from various sources—wheth
er text, images, audio, or video—and use that information to answer a query. For instance, an expert's audio commentary 
on the Eiffel Tower can be retrieved alongside text and image data to provide a more holistic response that anchors the 
answer in the data provided.

# How Multimodal RAG Works

The mechanics of Multimodal RAG involve transforming different
 data types into a structured data format like vectors that a model can process. This allows the model to retrieve and g
enerate information across multiple modalities seamlessly.

Once these data types are encoded into vectors, they can be 
stored in a vector space or similar storage vehicle, enabling the model to find relevant information regardless of the o
riginal data type. This process could involve clustering similar data and separating dissimilar data, making it easier t
o retrieve the most pertinent information for a given query.

# Three Approaches to Multimodal RAG

Implementing Multimo
dal RAG can be approached in a few distinct ways, each with its advantages and challenges. The three main methods includ
e using a single multimodal model, employing a grounded modality approach, and utilizing multiple encoders.

# Single Mu
ltimodal Model

[Image: Multimodal RAG diagram depicting the storage of Audio, Image, and Text encodings to answer a use
r query.](https://preview.redd.it/7hdmvcfj0hhd1.png?width=960&format=png&auto=webp&s=ce25486892694d6110e70084d6042ea1d2f
c604f)

This approach uses a unified model trained to encode different types of data (text, images, audio) into a common
 vector space. The model can then perform retrieval and generation across these different data types seamlessly. A singl
e multimodal approach tends to be one of the most common approaches people talk about when they talk about multimodal RA
G.

This method simplifies the process but relies heavily on the model’s ability to accurately encode and retrieve multi
modal data. However, if the model is well-trained, it can store and retrieve similar information across different modali
ties effectively.

Google is a great example of using a single multimodal mode.


# Grounded Modality (Text-Based)

In t
his approach, all data types are converted into text descriptions before being encoded and stored. This method leverages
 the strength of text-based models but may involve some loss of information during the conversion process.

Turning all 
data types into one modality creates a unified set of information for the model to retrieve, and today’s models are stro
ngest on text. That’s not to say in the future there won't be models that are better suited for other modalities. And th
at future might be months not years. But for today’s powerhouse models, they started out as text machines and that is st
ill where they are strongest.

This approach allows the use of robust text-based models for encoding and retrieval, maki
ng it a practical solution for environments where text is the primary data type.

# Multiple Encoders

[Image: A Multimo
dal RAG diagram that relies on separately aligned models to handle different modalities from a user query.](https://prev
iew.redd.it/3wmxg7yl0hhd1.png?width=960&format=png&auto=webp&s=80a2501a4c0b4c349fd93578c1c528c37848c97d)

This method em
ploys separate models to encode different data types. Each type of data (audio, images, text) is processed by its respec
tive model, and the results are integrated later in the retrieval process. Passing them through a set of encoders that c
an play nicely together creates an environment where each model and encoder can be fine-tuned to play to its particular 
strengths. 

This approach allows for specialized encoding but increases complexity in managing multiple models. It offe
rs the flexibility to use the best model for each data type, enhancing the accuracy and relevance of the retrieved infor
mation. But often it can be the most difficult to implement and maintain due to the increased complexity of inputs and o
utputs. 

With the emergence of powerful models that are starting to outperform other models in specific modalities, thi
s approach to multimodal RAG may grow in popularity.

# Challenges and Considerations

Implementing Multimodal RAG comes
 with its own set of challenges, such as handling temporal changes in data and ensuring the accuracy of the retrieval an
d generation process. 

Temporal changes, like the varying appearances of the Eiffel Tower over time, pose a significant
 challenge. Ensuring that the retrieved information is temporally accurate and relevant requires sophisticated handling 
of metadata and context which can be even more challenging when trying to pull data from multiple modalities like images
 and audio.

Another consideration is the balance between using a single unified model and multiple specialized models. 
While a single model offers simplicity, multiple models provide more tailored encoding for different data types. This de
cision depends on the specific application and the need for flexibility.

# Practical Applications and Future Prospects


Multimodal RAG holds immense potential for various practical applications, from enhancing search engines to improving A
I-driven personal assistants. By integrating multiple data types, these systems can provide richer, more nuanced respons
es, improving user experience and satisfaction.

Looking forward, the field of Multimodal RAG is poised for significant 
advancements. As models continue to improve and new techniques are developed, the ability to effectively integrate and l
everage multiple data types will become increasingly crucial. This progress will open up new opportunities for powerful 
applications and improved AI performance.

# Conclusion

Multimodal RAG represents a significant advancement in AI, as i
t can enable richer and more contextually accurate information retrieval and generation that grounds the model in the tr
uth of the data across modalities. While the field continues to evolve, the various approaches to implementing Multimoda
l RAG offer different trade-offs between simplicity, flexibility, and complexity. As technology progresses, the ability 
to effectively integrate and leverage multiple data types will be crucial for developing advanced AI applications.

Full
 Episode:  
[https://www.youtube.com/watch?v=ZetGV7gtyQw](https://www.youtube.com/watch?v=ZetGV7gtyQw)

# 
```
---

     
 
all -  [ Documentation seems confusing ](https://www.reddit.com/r/LangChain/comments/1enaock/documentation_seems_confusing/) , 2024-08-09-0911
```
Hello everybody! I have just started langchain and am going through documentation and it seems very confusing. 
I am als
o having trouble with prompts.
Could you please suggest a good starting point? 
Sorry if this has been posted before.
```
---

     
 
all -  [ What are the current limitations of LangChain4j compared to the Python version ](https://www.reddit.com/r/LangChain/comments/1enagg9/what_are_the_current_limitations_of_langchain4j/) , 2024-08-09-0911
```
I'm a Java developer interested in getting into AI software development. I see there's a ton of info on LangChain for Py
thon, but not as much on LangChain4j for Java. Should I dive into Python and start developing with it, or can I learn fr
om the langchain docs (and youtube videos) and then apply that knowledge to Java (just with different syntax)? Any advic
e?
```
---

     
 
all -  [ [3 YoE] [Canada] Not hearing back from Machine Learning Engineering or Data Science Jobs I applied t ](https://www.reddit.com/r/EngineeringResumes/comments/1en8yqn/3_yoe_canada_not_hearing_back_from_machine/) , 2024-08-09-0911
```
\[3 YoE\] \[Canada\] Not hearing back from Machine Learning Engineering or Data Science Jobs I applied to. Please help.


&#x200B;

• What positions/roles/industries are you targeting? 

MLE (ambitious), Data Scientist, Business Analyst (Wor
st Case Scenario)

  
• Where are you located and what locations are you applying to jobs in?

Montreal, applying to ope
nings in Canada

  
• Are you only applying to local jobs? Remote only? Are you willing to relocate?

Willing to relocat
e but visa is a complication for options beyond canada

  
• Tell us about your background and current employment situat
ion

Ex Management consultant with a bachelor in mechanical and masters in data science ('Management Analytics'). Have b
een working as a data scientist for the past one year (some parts contract, some part internship)

  
• Tell us about yo
ur job-hunting situation and challenges you've encountered

Radio Silence from postings I have been applying to. Radio s
ilence from recruiters I reached out to on LinkedIn

  
• Tell us why you're seeking help. (i.e., just fine-tuning, not 
getting called back for interviews, etc.)

Not getting called back for interviews

  
• Is there a particular section on
 your resume you’d like feedback on?

Experience bullet points, structure, 'what am i missing that is leading me to not 
get any interviews??'

  
• Is your citizenship status and visa situation playing a role in your job search?

I don't th
ink so. I am on PGWP.

https://preview.redd.it/kl2iqd44lghd1.png?width=5100&format=png&auto=webp&s=4d1d1759600cbf6df0964
46f9d388ef958ce25b0
```
---

     
 
all -  [ Key Contributors and Insights in Git Project Modules ](https://i.redd.it/nni4zbkqjghd1.jpeg) , 2024-08-09-0911
```
You might want to know who the main contributors are for those modules in the project directory over a certain period.


Although the layout is not perfect yet. (who knows how to align the TopN authors to the right).

Look at https://plugins
.jetbrains.com/plugin/24154-git-assistant
```
---

     
 
all -  [ Not sure what LLM to use for for your RAG system? Here's a price/size/performance comparison of ever ](https://thepi.pe/evals) , 2024-08-09-0911
```

```
---

     
 
all -  [ Text-2-SQL-Pandas Pipeline: HOW DO I BUILD THIS! ](https://www.reddit.com/r/LangChain/comments/1en87i9/text2sqlpandas_pipeline_how_do_i_build_this/) , 2024-08-09-0911
```
[https://www.reddit.com/r/LangChain/comments/1e5pe1a/optimal\_rag\_for\_text2sql/?utm\_source=share&utm\_medium=web3x&ut
m\_name=web3xcss&utm\_term=1&utm\_content=share\_button](https://www.reddit.com/r/LangChain/comments/1e5pe1a/optimal_rag
_for_text2sql/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)  
  
I built a w
orking text-2-SQL pipeline that runs queries on million of records. 20+ tables. It leverages Claude 3.5 sonnet and gets 
the work done 7/10 very well on a few complex prompts, multiple joins and conditional clauses.  At the infra level, the 
database has been modified to create and include a few views that would help make much more sense of the data. 

Now, I 
am in charge of building an analysis agent on top of it. 

Here's what I was thinking: I'll have the text-2-sql agent tr
anslate to query, retrieve the tabular information from the database and return the final table before applying any cond
itions or other arithmetic operations. And then pass on the resulting table to pandas agent along with the originally as
ked question. 

And then the pandas agent cook. But, I'm not a 100% sure whether this is the ideal approach. OR if there
 is any other way to work with this. Lemme know if you have any thoughts!
```
---

     
 
all -  [ Langfuse for LLM tracing for beginners  ](https://www.reddit.com/r/LangChain/comments/1en73et/langfuse_for_llm_tracing_for_beginners/) , 2024-08-09-0911
```
Langfuse is a free alternate for Langsmith for Generative AI based applications for debugging and tracing. This video ex
plains how to get Started with Langfuse : https://youtu.be/fIQIfIK6v0o?si=hzeG4matNCCZ9Bt_
```
---

     
 
all -  [ RAG system to detect small talk ](https://www.reddit.com/r/LangChain/comments/1en5h33/rag_system_to_detect_small_talk/) , 2024-08-09-0911
```
In a RAG system, how do you avoid the bot to go retrieve information when the questions are just small talk? For example
 the user says “Hi how are you?” And the bot goes and triggers all the RAG logic and gets all the information and makes 
a lot of drama and it replies “good thanks for asking” hahah anybody dealing with this issue?
```
---

     
 
all -  [ ML Engineer (1 YOE) looking for an open opportunity  ](https://www.reddit.com/r/Entrepreneur/comments/1en3r4e/ml_engineer_1_yoe_looking_for_an_open_opportunity/) , 2024-08-09-0911
```




Hi folks. I am a Machine Learning Engineer looking for open opportunities in Bangalore. I have 1 year of experience 
in developing and deploying ML solutions convering basic ML fundamentals like regression models and data analysis to bui
lding RAG applications using vector DB and Langchain. I have worked in shaping ideas into POCs using Machine Learning an
d Deep Learning. 

My tech stack includes Python, Jupyter Notebook, Sci-kit Learn, Langchain, Vector DB, fine-tuning LLM
s for specific use cases.

I am also experienced in developing & deploying the end to end LLM applications to AWS cloud.
 I am passionate about ML.

Any leads would be appreciated. 
Thank You 
```
---

     
 
all -  [ output a table in rag ](https://www.reddit.com/r/LangChain/comments/1en2wxt/output_a_table_in_rag/) , 2024-08-09-0911
```
hi guys, I want my rag (when asked) to output and print a table that is dynamically generated according to the question 
and context. What is the way to do it?
```
---

     
 
all -  [ ML Engineer (1 YOE) looking for an open opportunity  ](https://www.reddit.com/r/LangChain/comments/1en1s8v/ml_engineer_1_yoe_looking_for_an_open_opportunity/) , 2024-08-09-0911
```


Hi folks. I am a Machine Learning Engineer looking for open opportunities in Bangalore. I have 1 year of experience in
 developing and deploying ML solutions convering basic ML fundamentals like regression models and data analysis to build
ing RAG applications using vector DB and Langchain. I have worked in shaping ideas into POCs using Machine Learning and 
Deep Learning. 

My tech stack includes Python, Jupyter Notebook, Sci-kit Learn, Langchain, Vector DB, fine-tuning LLMs 
for specific use cases.

I am also experienced in developing & deploying the end to end LLM applications to AWS cloud. I
 am passionate about ML.

Any leads would be appreciated. 
Thank You 
```
---

     
 
all -  [ Russian response when generating summary using langchain and openai ](https://www.reddit.com/r/LangChain/comments/1en1mx5/russian_response_when_generating_summary_using/) , 2024-08-09-0911
```
Hey all,
I have been trying to use Langchain Summarization chain with Open ai, it does summarises the document but it tr
anslates it to english. 

And the same llm works, fine for RAG or normal llm.invoke. It is giving me answer in English, 
but only for Summarization it is sending me russian response.


Please help
```
---

     
 
all -  [ Anomaly detection in dynamic knowledge graphs ](https://www.reddit.com/r/learnmachinelearning/comments/1en1cwk/anomaly_detection_in_dynamic_knowledge_graphs/) , 2024-08-09-0911
```
Hi everyone,

I’m currently working on a project that involves creating dynamic knowledge graphs, and I’m looking for so
me advice on how to detect anomalies. Specifically, I’m interested in identifying anomalies between entities such as cha
racters and event dates.

For now, I’m generating graphs using LangChain Graph, GPT-4 Turbo, and Neo4j. However, I’m rel
atively new to the field of knowledge graphs and would greatly appreciate any guidance or resources you could share.
```
---

     
 
all -  [ Anomaly detection in dynamic knowledge graphs ](https://www.reddit.com/r/MLQuestions/comments/1en1680/anomaly_detection_in_dynamic_knowledge_graphs/) , 2024-08-09-0911
```
Hi everyone,

I’m currently working on a project that involves creating dynamic knowledge graphs, and I’m looking for so
me advice on how to detect anomalies. Specifically, I’m interested in identifying anomalies between entities such as cha
racters and event dates.

For now, I’m generating graphs using LangChain Graph, GPT-4 Turbo, and Neo4j. However, I’m rel
atively new to the field of knowledge graphs and would greatly appreciate any guidance or resources you could share.

```
---

     
 
all -  [ Langgraph with AWS Bedrock ](https://www.reddit.com/r/LangChain/comments/1en13pm/langgraph_with_aws_bedrock/) , 2024-08-09-0911
```
Hi folks!

Just wanted to know, has anyone have worked with langgraph for supervisor agentic framework using AWS Bedrock
 models like Mistral large or Claude 3.5.
For me, any model I use from AWS Bedrock with Agents it's giving 'Validation E
rror while calling InvokeModel operation' although I am giving correct prompt format for the models.

Please help me on 
this, inform me if you need more information.
Thanks in advance.

```
---

     
 
all -  [ Creating a prompt in Langchain hub ](https://www.reddit.com/r/LangChain/comments/1en0h86/creating_a_prompt_in_langchain_hub/) , 2024-08-09-0911
```
Hey guys, i'm trying to create a prompt in langchain hub from an already existing public prompt by just copying and past
ing its content into a new prompt. This is the first prompt I'm trying to create and it seems though I tried to duplicat
e the original prompt, My prompt is different from the original prompt.  
Here's the link to my prompt: [https://smith.l
angchain.com/hub/smtabatabaie/gps](https://smith.langchain.com/hub/smtabatabaie/gps)  
And here's the original prompt: [
https://smith.langchain.com/hub/smtabatabaie/web-voyager](https://smith.langchain.com/hub/smtabatabaie/web-voyager)  
My
 prompt has a 'ChatOpenAI' whereas the original prompt doesn't have this section. And also my prompt has 'scratchpad' as
 input whereas the original prompt doesn't consider 'scratchpad' as an input when I print the prompt in my python script
.  
Also in my script when I pull and use the original prompt, it works without any problem. But when i pull and use my 
prompt, it shows me the following error about hitting the maximum context length:  
  
'openai.BadRequestError: Error co
de: 400 - {'error': {'message': 'This model's maximum context length is 128000 tokens. However, your messages resulted i
n 473683 tokens. Please reduce the length of the messages.', 'type': 'invalid\_request\_error', 'param': 'messages', 'co
de': 'context\_length\_exceeded'}}'  
  
Would really appreciate if you have any idea what's causing this.  
Thanks very
 much.
```
---

     
 
all -  [ Trying to build a Natural Language to SQL model using langchain's 'create_sql_query_chain'. ](https://www.reddit.com/r/LangChain/comments/1emxori/trying_to_build_a_natural_language_to_sql_model/) , 2024-08-09-0911
```
Can anyone tell me some ways to pass down the schema of the table to the chain, I am passing it in query checker(referen
ce below) but could not make a full chain to pass it initially too.  
#https://python.langchain.com/v0.1/docs/use\_cases
/sql/query\_checking/

  
Good thing is the schema of my table is fixed so is there any other method you folks having in
 mind which can enable me make a fully local genAI text-to-SQL model.
```
---

     
 
all -  [ Gemini Zero shot prompt/function call, any help? ](https://www.reddit.com/r/LangChain/comments/1emvqkj/gemini_zero_shot_promptfunction_call_any_help/) , 2024-08-09-0911
```
Yo using langflow, a no code editor built off of langchain (I know this is a langchain server, but the problem should be
 mirrored in langchain), currently trying to run a zero shot agent with Gemini, using a tool call agent, 

integrating o
penAI works perfectly fine, but with Gemini, I get the error code in my image, any pointers in the right direction would
 be great,

Here is the 2 components & how they link (took other components out for simplicity)  
[https://www.loom.com/
share/61e4cd93166445bea7af0a962500af29?sid=8c9b0cc3-195e-4fef-a6b8-922670c52f95](https://www.loom.com/share/61e4cd931664
45bea7af0a962500af29?sid=8c9b0cc3-195e-4fef-a6b8-922670c52f95)

Any pointers would be amazing


```
---

     
 
all -  [ Give me suggestions on how to present myself, I am not getting any calls. ](https://i.redd.it/61gym7jjvchd1.png) , 2024-08-09-0911
```
More context, at my current team I am a single developer I build anything coding related stuff, done so many automations
 and created modules, created dashboards from logging. Now we are at a point nothing much development needs from my side
 so my client pivoted my to work on GenAI, I worked similarly on some web dev projects required for infra but they were 
scrapped in mid dev. Right now I have done the demos and published streamlit apps for the GenAI one's internally. I am t
he type of developer who isn't bound to single vertical I would say, I can pickup anything quickly that involves python 
and I have been doing. Idk I am not getting any calls or any responses and I feel depressed, I want to move away from he
re since I am sick of doing everything alone and I am not sure if I am designing everything the right way and I don't ge
t enough critique and also scared that when I am gonna join a team I would fail miserably. 
```
---

     
 
all -  [ Looking for someone who's good at making gptbots using langchain ](https://www.reddit.com/r/ProgrammingBuddies/comments/1emsc62/looking_for_someone_whos_good_at_making_gptbots/) , 2024-08-09-0911
```
Hi everyone,

Is there anyone who knows how to make a general gptbot using python for general documents? I am instructed
 by a company to create a gptbot using lanchain and I don't know anything about it. Is there anyone who's willing to hel
p me out?
```
---

     
 
all -  [ [1 YoE, Data and Policy Analyst, Data Engineer or Data Scientist Policy, United States] ](https://www.reddit.com/r/resumes/comments/1emqxqk/1_yoe_data_and_policy_analyst_data_engineer_or/) , 2024-08-09-0911
```
Hi everyone! I am a rising 4th year and will be graduating UCLA in June 2025. I am looking for entry level positions tha
t are focused around Data Engineering, Data Science, or Data Analytics. I currently work in a Polciy lab so it would be 
a plus if a company is non profit based or does research into policy making. I am applying for all positions, remote and
 in person. I am willing to relocate anywhere in the U.S. My job hunting has been very rocky, I applied to many roles bu
t never seem to get passed the resume screening. And honestly, it could get a bit discouraging, and I fear that I might 
not get a job once I graduate. I really love working in a collaborative environment and small community teams, so I am a
lso very open to working in a startups around finance or tech. I have been editing my resume over the few weeks and this
 is where I am at. I would really appreciate any feedback! When making my resume, I really wanted to emphasize that I am
 responsible and take initiative when it comes to learning in the job, and also for me, my teammates always come first, 
rather than customers or clients. I also want these companies to hold that similar value, because having a strong team m
akes a good company culture. Also, I was born the U.S. so citizenship is not an issue 

https://preview.redd.it/s1279gb5
sbhd1.png?width=850&format=png&auto=webp&s=e546296a994a3caf65dddc709d79ba35df40db75
```
---

     
 
all -  [ Best free model for Chatbot, document analysis, text summarization  ](https://www.reddit.com/r/LargeLanguageModels/comments/1emqq3e/best_free_model_for_chatbot_document_analysis/) , 2024-08-09-0911
```
We have a Postgres database hosted on AWS where we have all our data. We would like to implement a chatbot that users ca
n use to answer questions about our data. 

Separately, we also have several documents (PDF, DOCX, CSV, TXT) that we wou
ld like to analyze and return certain important data elements from it. 

Also, summarize a 20 page document into a singl
e paragraph/page. And look at a record in our database and summarize it for users. 

We don’t need the model to know muc
h about stuff outside of our own database. Example: calculus, astronomy, medical stuff etc are super irrelevant but I wi
ll take it if it comes with it. I just don’t want to pay for a super rich LLM to do a fraction of things it can do. 

We
 were considering Llama 80b and langchain for this exercise, but the GPU on AWS for this is turning out to be quite pric
ey. 

Which free model and what kind of setup would you recommend for these use cases? If it helps, we would prefer esta
blished models that are implemented and maintained by reputable companies because of accuracy and reputation risk. 

 



```
---

     
 
all -  [ How to handle error with OpenAI ](https://www.reddit.com/r/AutoGenAI/comments/1empqh9/how_to_handle_error_with_openai/) , 2024-08-09-0911
```
Hello, I'm currently creating a groupchat, I'm only using the Assistant agent and an user proxy agent, the assistants ha
ve a conversation retrieval chain from langchain and using FAISS for the vector store

I'm using the turbo 3.5 model fro
m OpenAI

I'm having a very annoying error sometimes, haven't been able to replicate in any way, sometimes it only happe
ns once or twice but today it happened multiple times in less than an hour, different questions were sent, I can't seem 
to find a pattern at all

  
I would like to find why this is a happening, or if there is a way to handle this error so 
the chat can continue

right now I'm running it with a [panel](https://panel.holoviz.org/) interface

this is the error:


    2024-07-16 16:11:35,542 Task exception was never retrieved
    future: <Task finished name='Task-350' coro=<delaye
d_initiate_chat() done, defined at /Users/<user>/Documents/<app>/<app>_bot/chat_interface.py:90> exception=InternalServe
rError('Error code: 500 - {'error': {'message': 'The model produced invalid content. Consider modifying your prompt if y
ou are seeing this error persistently.', 'type': 'model_error', 'param': None, 'code': None}}')>
    Traceback (most rec
ent call last):
      File '/Users/<user>/Documents/<app>/<app>_bot/chat_interface.py', line 94, in delayed_initiate_cha
t
        await agent.a_initiate_chat(recipient, message=message)
      File '/Users/<user>/Documents/<app>/<app>_bot/en
v/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1084, in a_initiate_chat
        await self
.a_send(msg2send, recipient, silent=silent)
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-
packages/autogen/agentchat/conversable_agent.py', line 705, in a_send
        await recipient.a_receive(message, self, r
equest_reply, silent)
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agent
chat/conversable_agent.py', line 855, in a_receive
        reply = await self.a_generate_reply(sender=sender)
          
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/
site-packages/autogen/agentchat/conversable_agent.py', line 2042, in a_generate_reply
        final, reply = await reply
_func(
                       ^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/s
ite-packages/autogen/agentchat/groupchat.py', line 1133, in a_run_chat
        reply = await speaker.a_generate_reply(se
nder=self)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_b
ot/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 2042, in a_generate_reply
        fina
l, reply = await reply_func(
                       ^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bo
t/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1400, in a_generate_oai_reply
        r
eturn await asyncio.get_event_loop().run_in_executor(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   File '/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/concurrent/fut
ures/thread.py', line 58, in run
        result = self.fn(*self.args, **self.kwargs)
                 ^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agentchat/
conversable_agent.py', line 1398, in _generate_oai_reply
        return self.generate_oai_reply(*args, **kwargs)
       
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/
site-packages/autogen/agentchat/conversable_agent.py', line 1340, in generate_oai_reply
        extracted_response = sel
f._generate_oai_reply_from_client(
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users
/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1359, i
n _generate_oai_reply_from_client
        response = llm_client.create(
                   ^^^^^^^^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/oai/client.py', line 722, in create
 
       response = client.create(params)
                   ^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<ap
p>/<app>_bot/env/lib/python3.12/site-packages/autogen/oai/client.py', line 320, in create
        response = completions
.create(**params)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/en
v/lib/python3.12/site-packages/openai/_utils/_utils.py', line 277, in wrapper
        return func(*args, **kwargs)
     
          ^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/ope
nai/resources/chat/completions.py', line 643, in create
        return self._post(
               ^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1266, in post
 
       return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                       
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app
>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 942, in request
        return self._request(
     
          ^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_ba
se_client.py', line 1031, in _request
        return self._retry_request(
               ^^^^^^^^^^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1079, in _retry
_request
        return self._request(
               ^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot
/env/lib/python3.12/site-packages/openai/_base_client.py', line 1031, in _request
        return self._retry_request(
  
             ^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/o
penai/_base_client.py', line 1079, in _retry_request
        return self._request(
               ^^^^^^^^^^^^^^
      F
ile '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1046, in _re
quest
        raise self._make_status_error_from_response(err.response) from None
    openai.InternalServerError: Error 
code: 500 - {'error': {'message': 'The model produced invalid content. Consider modifying your prompt if you are seeing 
this error persistently.', 'type': 'model_error', 'param': None, 'code': None}}
```
---

     
 
all -  [ Where can I get my code reviewed? ](https://www.reddit.com/r/LangChain/comments/1emiqo5/where_can_i_get_my_code_reviewed/) , 2024-08-09-0911
```
Hello,

  
I've developed a script using Langchain and Agents that I plan to launch internally within our company. Befor
e moving it to production, I'd appreciate a second pair of eyes to review the code for any potential redundancies or are
as for improvement.

I’ve noticed that some posts sharing code here don’t always get much traction. I didn’t see any rul
es against sharing code for review, but I wanted to check if it's appropriate to ask for feedback here. 

If not, could 
you suggest any other platforms where I might get my code reviewed?

  
Thanks in advance.
```
---

     
 
all -  [ [Discussion] LLM use cases ](https://www.reddit.com/r/LangChain/comments/1emgi8p/discussion_llm_use_cases/) , 2024-08-09-0911
```
Other than chatbot what are the other use cases the LLM or open source hugging face models are used for? 
```
---

     
 
all -  [ How can I help you build more reliable AI products faster? ](https://www.reddit.com/r/LangChain/comments/1emfs9w/how_can_i_help_you_build_more_reliable_ai/) , 2024-08-09-0911
```
Hey everybody,

I've been really frustrated with the developer experience of Langchain in Typescript, particularly aroun
d structured extraction from image and text and agent workflows. I have started building out a dev toolkit to solve that
 with some DX inspiration from dev tools like vercel and prisma: [https://github.com/forge-ml/forge-ml](https://github.c
om/forge-ml/forge-ml).

I'd love feedback on the current product, but I'd also love to know what else I can incorporate 
- what are the big pain points people are having? 

Some of the current things on the roadmap are, in no particular orde
r:  
- structured extraction from video  
- structured extraction from audio  
- Anthropic/Groq support  
- Semantic Sea
rch over Documents  
- Semantic Search over Databases  
- Fine tuning  
- Workflows  
- Model routing

What are the bigg
est issues that you're facing when building AI products?
```
---

     
 
all -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-09-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
all -  [ Specialized Web Search  ](https://www.reddit.com/r/LangChain/comments/1emdose/specialized_web_search/) , 2024-08-09-0911
```
Hi Folks, I am really new here. I am working on a multi-agent project where each agent would look up information on a se
t of select predefined websites. I am hoping to use web search to do it. Is there a way for me search articles related t
o a specific topic on a specific website using web search?
```
---

     
 
all -  [ using retrieval_chain as a tool for an agent ](https://www.reddit.com/r/LangChain/comments/1emd7m3/using_retrieval_chain_as_a_tool_for_an_agent/) , 2024-08-09-0911
```
i've developped a rag application using langchain with the retrieval chain that combines history retriever and documents
 chain, and it performs pretty good .   
i have been tasked to add summarization and some other tools , so i tought abou
t using agent and adding tools for such tasks and still use the rag chain as a tool .   
  
**Is there a way to use the 
same rag chain as a tool for the agent ?** 
```
---

     
 
all -  [ Advice on where to host LangChain.js REST API function for Q&A chatbot for my docs ](https://www.reddit.com/r/LangChain/comments/1em997z/advice_on_where_to_host_langchainjs_rest_api/) , 2024-08-09-0911
```
I need to build a simple chatbot for my documentation pages. I need advice on where to host it, currently I adjusted it 
for Supabase edge function and Supabase vector store because it's free and deployed all over the world, but if I exceed 
the requests limit, I will have to self-host Supabase and then it's just one location.

Does anyone already have chatbot
s for small documentations and can you share which vector store you use and where you deployed your code? my docs pages 
are served from AWS S3. If I use AWS lambda to host the edge function, I'm afraid of a cost increase if there will be ma
ny requests.
```
---

     
 
all -  [ How to return langfuse trace_id when using Langserve stream? ](https://www.reddit.com/r/LangChain/comments/1em7aik/how_to_return_langfuse_trace_id_when_using/) , 2024-08-09-0911
```
I have very simple code **Langserve** with **langfuse\_handler**.

    add_routes(app, normal_agent.with_config(Runnable
Config(callbacks=[langfuse_handler])),
               per_req_config_modifier=per_request_config_modifier, path='/normal
')

When I run my code: 

    import asyncio
    
    from langserve import RemoteRunnable
    
    remote_runnable = Re
moteRunnable('http://localhost:8001/normal')
    
    
    async def main():
        async for chunk in remote_runnable.
astream({'input': 'tell me about ronaldo'}):
    
            print(chunk, end='|\n', flush=True)
    
    asyncio.run(m
ain())

I want return to client my trace\_id of Langfuse. Do you have any ideas to do that? I stuck here for 2 days. 
```
---

     
 
all -  [ Rate my resume (for entry level Backend/ AI Positions) ](https://www.reddit.com/r/developersIndia/comments/1em5sgu/rate_my_resume_for_entry_level_backend_ai/) , 2024-08-09-0911
```
https://preview.redd.it/rjvssx8a37hd1.png?width=661&format=png&auto=webp&s=b8bd0d1a4720c4cd39afa6ca21a9797d4dd37680

Sin
ce the last time I posted my resume, I have made many tweaks as suggested by a helpful person in the comments... I think
 it has improved a lot can you rate this resume?   
any tips for cold emailing and applying to jobs is welcome because I
 am having 0 call-backs or responses to my applications.
```
---

     
 
all -  [ Support with Langchain.js for free inference ](https://www.reddit.com/r/LangChain/comments/1em3muc/support_with_langchainjs_for_free_inference/) , 2024-08-09-0911
```
I am fairly new to Langchain and wanted to seek out some advice for free methods of using LLMs to just do some basic pro
mpting for a web application. The prompting is just providing some music artists and asking the LLM to think of potentia
l ideas for those artists. I have a node.js backend that I am attempting to integrate Langchain.js into. 

I first wante
d to ask are there any decent models for my task that can be used with Langchain.js for free and what would a very basic
 code snippet look like to run it. 

  
In addition, I wanted to ask if Ollama is applicable here or is that strictly fo
r local applications?

  
Thanks !

  
  

```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-09-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-09-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-09-0911
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-09-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-09-0911
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

     
