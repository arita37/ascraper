 
all -  [ Document Loaders Outputting 'NO_OUTPUT' ](https://www.reddit.com/r/LangChain/comments/1blc6q2/document_loaders_outputting_no_output/) , 2024-03-23-0909
```
Hi, currently I am working on an RAG tool for my company. I have to load multiple PDFs and Powerpoints, for which I use 
the UnstructuredPDFLoader and UnstructuredPowerPointLoader, because a lot of these documents contain images with text on
 them and these loaders allow you to extract said text through OCR. However, when I run this and the program goes throug
h the retrieval steps, I get an error coming from a deprecated function, along with the output of each document split th
at will be used to answer my query. The answers to my questions are not of a high quality, and I believe that it may be 
attributed to something being wrong with my loaders because the output I am seeing for some document splits is 'NO\_OUTP
UT' or 'NO\_OUTPUT\_OUTPUT'.

I am wondering if any of you have run into this problem. In addition, as a bonus question,
 how do you all maintain metadata like source information in your document splits? I always lose mine.



Below is the r
etrieval code:

    # Vector Database
    u/st.cache_resource
    def vector_db_init(_folder_id, _model):
        '''Vec
tor db initializer, plus contextual compression addition'''
        persist_directory = './db/'  # Persist directory pat
h
    
        # Embeddings to be applied
        embeddings = VertexAIEmbeddings(
            model_name='textembedding
-gecko-multilingual',
            credentials=CREDENTIALS,
            project_id=PROJECT_ID,
            )
    
       
 # Document splitting, embedding and vector database loading
        # DOES NOT have to be done in every run, just once 
and after you can simply refer to the db
        if not os.path.exists(persist_directory):
            # Data Pre-proces
sing
            # TODO- loader that can correct typos and what-not
            pdf_loader = DirectoryLoader('/Users/mar
conardoneguerra/Desktop/e3_Consulting/Other/AI/Proposal RAG/docs',
                                         glob='**/*.p
df',
                                         recursive=True,
                                         show_progress=Tru
e,
                                         loader_cls=UnstructuredPDFLoader,
                                         l
oader_kwargs={
                                            #'extract_images':True,
                                     
       'post_processors':[clean_extra_whitespace, clean_non_ascii_chars, clean], # data cleaning
                       
                     'mode':'single',
                                            'strategy':'hi_res',
                 
                           'high_res_model_name':'detectron2_onnx',
                                            #'encodi
ng':'unicode'
                                         })
            
            ppt_loader = DirectoryLoader('/Users/
marconardoneguerra/Desktop/e3_Consulting/Other/AI/Proposal RAG/docs',
                                         glob='**/
*.pptx',
                                         recursive=True,
                                         show_progress
=True,
                                         loader_cls=UnstructuredPowerPointLoader,
                               
          loader_kwargs={
                                            #'extract_images':True,
                          
                  'post_processors':[clean_extra_whitespace, clean_non_ascii_chars, clean], # data cleaning
            
                                'mode':'single',
                                            'strategy':'hi_res',
      
                                      'high_res_model_name':'detectron2_onnx',
                                         
   #'encoding':'unicode'
                                         })
    
            loaded_pdfs = pdf_loader.load()
  
          loaded_ppts = ppt_loader.load()
    
            print('# of PDFs:' + str(len(loaded_pdfs)))
            print
('# of PPTs:' + str(len(loaded_ppts)))
            loaded_docs = loaded_pdfs + loaded_ppts
    
            # gdrive_doc
uments = doc_processor(gdrive_documents, image_captioning)
    
            context = '\n\n'.join(str(p.page_content) fo
r p in loaded_docs)
    
            # had to remove below because this splitter is new and does not have a max token si
ze, hence has given chunks too large to handle
            # splitter = SemanticChunker(embeddings)
            splitter
 = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=25) 
            data = splitter.split_text(context)
   
         
            print('Data Processing Complete')
    
            vectordb = Chroma.from_texts(
                d
ata, embeddings, persist_directory=persist_directory
            )
            vectordb.persist()
    
            print
('Vector DB Creating Complete\n')
    
        elif os.path.exists(persist_directory):
            vectordb = Chroma(
  
              persist_directory=persist_directory, embedding_function=embeddings
            )
    
            print('V
ector DB Loaded\n')
    
        # Compresses what is contextually needed for query answer (?)
        compressor = LLMC
hainExtractor.from_llm(_model, )
        compression_retriever = ContextualCompressionRetriever(base_compressor=compress
or, 
                                                               base_retriever=vectordb.as_retriever(search_type='si
milarity', search_kwargs={'k': 24}))
    
        return compression_retriever
    
    
    @st.cache_resource
    def 
chain_init(_model, _retriever):
        '''Initializes chain for retrieval'''
        # DONE- conversational template
  
      template = '''
        Who you are:
        You are an expert on everything about e3 Consulting, AKA e3, a consult
ing firm based in San Juan, Puerto Rico.
        Your firm specializes in IT consulting. \
        ------
        Instru
ctions:
        You will be receiving questions about e3 and their previous work. \
        You will gather knowledge to
 deliver a good response to the user (separated with <ctx></ctx>). \
        If you don't know the answer, answer with '
Unfortunately, I don't have the information.' \
        If you don't find enough information below, also answer with 'Un
fortunately, I don't have the information.' \
        The context will most likely have typos in it, please correct them
 when you formulate your answer. \
        ------
        <ctx>
        {context}
        </ctx>
        ------ 
       
 {question}
        Answer:
        '''
    
        # template above
        question_prompt_template = PromptTemplate(
template=template, input_variables=['question', 'context'])
    
        # We create a qa chain with our llm, retriever,
 and memory
        # Use chain_type refine so we cna build off of different information,
        # in addition to being
 wary of our context window
        # TODO make this conversational (could be complex)
        qa_chain = RetrievalQA.fr
om_chain_type(
            llm=_model,
            chain_type='stuff',
            return_source_documents=True,
       
     retriever=_retriever,
            verbose=True,
        )
    
        # qa_chain = RetrievalQA | StrOutputParser()

    
        return qa_chain

  
Error examples:

    NO_OUTPUT_OUTPUT/Users/marconardoneguerra/anaconda3/envs/proposal
-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: The predict_and_parse method is deprecated, 
instead pass an output parser directly to LLMChain.
      warnings.warn(
    NO_OUTPUT_OUTPUT/Users/marconardoneguerra/a
naconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: The predict_and_parse 
method is deprecated, instead pass an output parser directly to LLMChain.
      warnings.warn(
    NO_OUTPUT_OUTPUT/User
s/marconardoneguerra/anaconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm.py:316: UserWarning: 
The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain.
      warnings.warn(
   
 NO_OUTPUT_OUTPUT/Users/marconardoneguerra/anaconda3/envs/proposal-rag/lib/python3.12/site-packages/langchain/chains/llm
.py:316: UserWarning: The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain.




Thanks!
```
---

     
 
all -  [ Free NVIDIA AI course list ](https://i.redd.it/n0xmj0tpoypc1.jpeg) , 2024-03-23-0909
```
1. **Generative AI Explained**

What you'll learn:

• Generative AI and explain how Generative AI works.

• Various Gene
rative AI applications.

• Challenges and opportunities in Generative AI

[Link](https://courses.nvidia.com/courses/cour
se-v1:DLI+S-FX-07+V1/)

2. **Building A Brain in 10 Minutes**

What you'll learn:

• Exploring how neural networks use d
ata to learn

• Understanding the math behind a neuron

[Link](https://courses.nvidia.com/courses/course-v1:DLI+T-FX-01+
V1/)

Sign up to our [newsletter](https://www.thepromptindex.com/newsletter.html) for our weekly AI roundup. 

3. **Augm
ent your LLM with Retrieval Augmented Generation:**

What you'll learn:

• Basics of Retrieval Augmented Generation

• R
AG retrieval process

• NVIDIA AI Foundations and RAG model components

[Link](https://courses.nvidia.com/courses/course
-v1:NVIDIA+S-FX-16+v1/)

4. **AI in the Data Center:**

What you'll learn:

• AI use cases, Machine Learning, Deep Learn
ing, and their workflows.

• GPU architecture and its impact on AI.

• Deep learning frameworks, and deployment consider
ations.

[Link](https://www.coursera.org/learn/introduction-ai-data-center)

5. **Accelerate Data Science Workflows with
 Zero Code Changes:**

What you'll learn:

• Learn benefits of unified CPU and GPU workflows

• GPU-accelerate data proc
essing and ML without code changes

• Experience faster processing times

[Link](https://courses.nvidia.com/courses/cour
se-v1:DLI+T-DS-03+V1/)

6. **Mastering Recommender Systems:**

What you'll learn:

• Strategies from Kaggle Grandmasters
 on building recommendation systems for e-commerce.

• Cover 2-stage models, candidate generation, feature engineering, 
and ensembling.

[Link](https://www.classcentral.com/course/youtube-grandmaster-series-mastering-recommender-systems-184
298)

7. **Networking Introduction:**

What you'll learn:

• Learn about networks and their importance.

• Explore Ether
net basics and data forwarding in Ethernet networks.

• Discuss network components, requirements, OSI model, TCP/IP prot
ocol

[Link](https://www.coursera.org/learn/introduction-to-networking-nvidia)

8. **How to Perform Large-Scale Image Cl
assification**

What you'll learn:

• Learn large-scale image classification

• Cover challenges, modeling techniques AN
D validation strategies.

[Link](https://www.classcentral.com/course/youtube-grandmaster-series-how-to-perform-large-sca
le-image-classification-130184)

9. **Building RAG Agents with LLMs:**

What you'll learn:

• Scalable deployment strate
gies for LLMs and vector databases.

• Modern LangChain paradigms for dialog management and document retrieval.

• Using
 advanced models and steps for production.

[Link](https://courses.nvidia.com/courses/course-v1:DLI+S-FX-15+V1/)
```
---

     
 
all -  [ LangChain single input Agent params ](https://www.reddit.com/r/LangChain/comments/1blaz9d/langchain_single_input_agent_params/) , 2024-03-23-0909
```
Hi community, looking for some guidance to explain how this is called when I specify the Tool's parameters as a descript
ion rather than Fields. 

For some reason Fields does not work in that project, giving me exception like

    ERROR:root
:An error occurred ZeroShotAgent does not support multi-input tool 

&#x200B;

Here is some code

    class SimpleInputs
(BaseModel):
        input: str
        
    class GetEvents(BaseTool):
        name = 'get_calendar_event'
        desc
ription = 'Use this tool with arguments like '{{'start_date': 'yyyy-mm-dd', 'max_results': int}}' when you need to retri
eve events from Calendar.'
        args_schema: Type[BaseModel] = SimpleInputs
        return_direct: bool = False
    

    ---
            agent = initialize_agent(
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
             
   tools=tools,
                llm=self.llm,
                verbose=True,

&#x200B;
```
---

     
 
all -  [ Does anyone have a codebase or tutorial for using LLMs with LangChain to summarize each row in a dat ](https://www.reddit.com/r/LangChain/comments/1bl7k4g/does_anyone_have_a_codebase_or_tutorial_for_using/) , 2024-03-23-0909
```
 Does anyone have a codebase or tutorial for using LLMs with LangChain to summarize each row in a database and generate 
output for each? I have a database that is updated weekly, which you can think of as a record of transactions. I'm looki
ng for a way to read each row of this database weekly, summarize the contents of those records, and have it tweeted out.
 I'm curious if there's a tutorial or codebase somewhere that does this. 
```
---

     
 
all -  [ 23 New Data Science, Data Engineering and Machine Learning jobs ](https://www.reddit.com/r/BigDataJobs/comments/1bl4juz/23_new_data_science_data_engineering_and_machine/) , 2024-03-23-0909
```
|Job Title|Company|Location|Country|Skills|
|:-|:-|:-|:-|:-|
|[Mid Data Engineer (3733 USD/Mes)](https://datayoshi.com/o
ffer/906372/mid-data-engineer-3733-usd-me)|[Listopro](https://www.datayoshi.com/company/listopro-jobs)|[Argentina](https
://datayoshi.com/offer/906372/mid-data-engineer-3733-usd-me)|[Argentina](https://datayoshi.com/offer/906372/mid-data-eng
ineer-3733-usd-me)|[Python, SQL](https://datayoshi.com/offer/906372/mid-data-engineer-3733-usd-me)|
|[Data engineer pyth
on H/F chez SAFRAN](https://datayoshi.com/offer/105682/data-engineer-python-h-f-chez)|[Kicklox - Plateforme de matching 
entre talents tech & porteurs de projets](https://www.datayoshi.com/company/kicklox---plateforme-de-matching-entre-talen
ts-tech-&-porteurs-de-projets-jobs)|[Gonfreville-l’Orcher](https://datayoshi.com/offer/105682/data-engineer-python-h-f-c
hez)|[France](https://datayoshi.com/offer/105682/data-engineer-python-h-f-chez)|[SQL](https://datayoshi.com/offer/105682
/data-engineer-python-h-f-chez)|
|[Machine Learning Engineer](https://datayoshi.com/offer/287675/machine-learning-engine
er)|[Mirakl](https://www.datayoshi.com/company/mirakl-jobs)|[Bordeaux](https://datayoshi.com/offer/287675/machine-learni
ng-engineer)|[France](https://datayoshi.com/offer/287675/machine-learning-engineer)|[Spark, NLP, Machine Learning](https
://datayoshi.com/offer/287675/machine-learning-engineer)|
|[Senior Data Engineer](https://datayoshi.com/offer/343227/sen
ior-data-engineer)|[Samsara](https://www.datayoshi.com/company/samsara-jobs)|[United States](https://datayoshi.com/offer
/343227/senior-data-engineer)|[Remote](https://datayoshi.com/offer/343227/senior-data-engineer)|[SQL, ETL, AWS](https://
datayoshi.com/offer/343227/senior-data-engineer)|
|[Senior Azure Data Engineer](https://datayoshi.com/offer/751025/senio
r-azure-data-engineer)|[Numentica](https://www.datayoshi.com/company/numentica-jobs)|[Palo Alto](https://datayoshi.com/o
ffer/751025/senior-azure-data-engineer)|[Remote](https://datayoshi.com/offer/751025/senior-azure-data-engineer)|[Spark, 
SQL](https://datayoshi.com/offer/751025/senior-azure-data-engineer)|
|[AI Engineer (Python, Langchain)](https://datayosh
i.com/offer/240666/ai-engineer-python-langchain)|[JUPUS](https://www.datayoshi.com/company/jupus-jobs)|[Germany](https:/
/datayoshi.com/offer/240666/ai-engineer-python-langchain)|[Germany](https://datayoshi.com/offer/240666/ai-engineer-pytho
n-langchain)|[Python](https://datayoshi.com/offer/240666/ai-engineer-python-langchain)|
|[Senior Data Analyst](https://d
atayoshi.com/offer/551411/senior-data-analyst)|[YEGO](https://www.datayoshi.com/company/yego-jobs)|[Barcelona](https://d
atayoshi.com/offer/551411/senior-data-analyst)|[Spain](https://datayoshi.com/offer/551411/senior-data-analyst)|[SQL](htt
ps://datayoshi.com/offer/551411/senior-data-analyst)|
|[Data Analyst](https://datayoshi.com/offer/505803/data-analyst)|[
Peroptyx](https://www.datayoshi.com/company/peroptyx-jobs)|[Milan](https://datayoshi.com/offer/505803/data-analyst)|[Ita
ly](https://datayoshi.com/offer/505803/data-analyst)|[](https://datayoshi.com/offer/505803/data-analyst)|
|[Data Enginee
r (m/w/d) 100%](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|[MDPI](https://www.datayoshi.com/company/mdp
i-jobs)|[Basel](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|[Switzerland](https://datayoshi.com/offer/49
5742/data-engineer-m-w-d-100)|[SQL, ETL, Scala](https://datayoshi.com/offer/495742/data-engineer-m-w-d-100)|
|[Junior Da
ta Analyst](https://datayoshi.com/offer/462463/junior-data-analyst)|[All Response Media](https://www.datayoshi.com/compa
ny/all-response-media-jobs)|[London](https://datayoshi.com/offer/462463/junior-data-analyst)|[United Kingdom](https://da
tayoshi.com/offer/462463/junior-data-analyst)|[SQL](https://datayoshi.com/offer/462463/junior-data-analyst)|
|[Sr Data A
nalyst](https://datayoshi.com/offer/113494/sr-data-analyst)|[PedidosYa](https://www.datayoshi.com/company/pedidosya-jobs
)|[Greater Buenos Aires](https://datayoshi.com/offer/113494/sr-data-analyst)|[Argentina](https://datayoshi.com/offer/113
494/sr-data-analyst)|[Looker, SQL, Python](https://datayoshi.com/offer/113494/sr-data-analyst)|
|[Data Scientist - All L
evels!](https://datayoshi.com/offer/727798/data-scientist-all-levels)|[BIP Brasil](https://www.datayoshi.com/company/bip
-brasil-jobs)|[Brazil](https://datayoshi.com/offer/727798/data-scientist-all-levels)|[Brazil](https://datayoshi.com/offe
r/727798/data-scientist-all-levels)|[Modeling](https://datayoshi.com/offer/727798/data-scientist-all-levels)|
|[Data Eng
ineer, Prime Video Discovery Analytics](https://datayoshi.com/offer/170470/data-engineer-prime-video-dis)|[Prime Video &
 Amazon Studios](https://www.datayoshi.com/company/prime-video-&-amazon-studios-jobs)|[London](https://datayoshi.com/off
er/170470/data-engineer-prime-video-dis)|[United Kingdom](https://datayoshi.com/offer/170470/data-engineer-prime-video-d
is)|[AWS, Scala](https://datayoshi.com/offer/170470/data-engineer-prime-video-dis)|
|[Azure Data Engineer](https://datay
oshi.com/offer/423231/azure-data-engineer)|[emagine](https://www.datayoshi.com/company/emagine-jobs)|[Warsaw](https://da
tayoshi.com/offer/423231/azure-data-engineer)|[Poland](https://datayoshi.com/offer/423231/azure-data-engineer)|[Python, 
Scala, SQL](https://datayoshi.com/offer/423231/azure-data-engineer)|
|[Machine Learning Engineer](https://datayoshi.com/
offer/788069/machine-learning-engineer)|[DKATALIS](https://www.datayoshi.com/company/dkatalis-jobs)|[Singapore](https://
datayoshi.com/offer/788069/machine-learning-engineer)|[Singapore](https://datayoshi.com/offer/788069/machine-learning-en
gineer)|[Python, Machine Learning](https://datayoshi.com/offer/788069/machine-learning-engineer)|
|[Alternant Data Engin
eer H/F](https://datayoshi.com/offer/795287/alternant-data-engineer-h-f)|[Lyreco France](https://www.datayoshi.com/compa
ny/lyreco-france-jobs)|[Marly](https://datayoshi.com/offer/795287/alternant-data-engineer-h-f)|[France](https://datayosh
i.com/offer/795287/alternant-data-engineer-h-f)|[Python, Spark, Hadoop](https://datayoshi.com/offer/795287/alternant-dat
a-engineer-h-f)|
|[Machine Learning Engineer](https://datayoshi.com/offer/938934/machine-learning-engineer)|[Morgan McKi
nley](https://www.datayoshi.com/company/morgan-mckinley-jobs)|[Toronto](https://datayoshi.com/offer/938934/machine-learn
ing-engineer)|[Canada](https://datayoshi.com/offer/938934/machine-learning-engineer)|[Machine Learning, NLP](https://dat
ayoshi.com/offer/938934/machine-learning-engineer)|
|[Data Scientist](https://datayoshi.com/offer/395728/data-scientist)
|[Desigual](https://www.datayoshi.com/company/desigual-jobs)|[Greater Barcelona Metropolitan Area](https://datayoshi.com
/offer/395728/data-scientist)|[Spain](https://datayoshi.com/offer/395728/data-scientist)|[Machine Learning](https://data
yoshi.com/offer/395728/data-scientist)|
|[Data Scientist](https://datayoshi.com/offer/769393/data-scientist)|[Contents.c
om](https://www.datayoshi.com/company/contents.com-jobs)|[Milan](https://datayoshi.com/offer/769393/data-scientist)|[Ita
ly](https://datayoshi.com/offer/769393/data-scientist)|[Python, NLP](https://datayoshi.com/offer/769393/data-scientist)|

|[STAGE - Ingénieur Data Scientist Junior F/H](https://datayoshi.com/offer/601797/stage-ingenieur-data-scienti)|[Plasti
c Omnium](https://www.datayoshi.com/company/plastic-omnium-jobs)|[Venette](https://datayoshi.com/offer/601797/stage-inge
nieur-data-scienti)|[France](https://datayoshi.com/offer/601797/stage-ingenieur-data-scienti)|[Deep Learning](https://da
tayoshi.com/offer/601797/stage-ingenieur-data-scienti)|
|[Data Analyst, Commerce & Marketing Analytics](https://datayosh
i.com/offer/456146/data-analyst-commerce-marke)|[Fandom](https://www.datayoshi.com/company/fandom-jobs)|[London](https:/
/datayoshi.com/offer/456146/data-analyst-commerce-marke)|[United Kingdom](https://datayoshi.com/offer/456146/data-analys
t-commerce-marke)|[Python, Pandas, Tableau](https://datayoshi.com/offer/456146/data-analyst-commerce-marke)|
|[Junior Da
ta Analyst- Banking](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[Skill Farm](https://www.datayoshi.
com/company/skill-farm-jobs)|[Johannesburg](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[South Afric
a](https://datayoshi.com/offer/239002/junior-data-analyst-banking)|[SQL, Tableau](https://datayoshi.com/offer/239002/jun
ior-data-analyst-banking)|
|[Data Analyst - Power BI](https://datayoshi.com/offer/381956/data-analyst-power-bi)|[Energy 
Jobline](https://www.datayoshi.com/company/energy-jobline-jobs)|[London](https://datayoshi.com/offer/381956/data-analyst
-power-bi)|[United Kingdom](https://datayoshi.com/offer/381956/data-analyst-power-bi)|[Power BI](https://datayoshi.com/o
ffer/381956/data-analyst-power-bi)|
                        
 Hey, here are 23 New Data Science, Data Engineering and Ma
chine Learning jobs. 

 For more, check our Google sheet with more opportunities in Data Science and Machine Learning (u
pdated each week) [here](https://docs.google.com/spreadsheets/d/1Vsg1Jmc0ZIDc_tPqZTzhbgxGIeTDQkUsBySMNbbCFI4/) 

 If you
 want to take some Data and ML courses, click [here](https://learncrunch.com/courses?utm_source=reddit&source=reddit) 


  Let me know if you have any questions. Cheers!
```
---

     
 
all -  [ Langchain GPT ](https://www.reddit.com/r/LangChain/comments/1bl3lpg/langchain_gpt/) , 2024-03-23-0909
```
Hey everyone, just wanted to ask if you know any Langchain GPTs that actually works and is updated with the latest Langc
hain documents?  
Thanks
```
---

     
 
all -  [ How do you verify, aside from manually checking the PDFs, that your answers are correct from a simpl ](https://www.reddit.com/r/LangChain/comments/1bl1p6d/how_do_you_verify_aside_from_manually_checking/) , 2024-03-23-0909
```
Hi! I'm new to Langchain and tinkering with LLMs in general, I'm just doing a small project on Langchain's capabilities 
on document loading, chunking, and of course using a similarity search on a vectorstore and then using the information I
 retrieve in a chain to get an answer.

I'm only testing on a small dataset, so it's easy for me to see the specific fil
es and pages to cross check whether it is the best result among the different files. But it got me thinking: if I try to
 work with a larger dataset, how exactly do I verify if the answer is the best result in the ranking and if it is indeed
 correct?

Is it possible to get datasets where it contains a PDF, some test input prompts, and an expected certain corr
ect output? This way, I would be able to use my project to ingest that data and see if I get similar results? Or is this
 too good to be true?
```
---

     
 
all -  [ Feedback for my beginner RAG pdf project ](https://www.reddit.com/r/learnmachinelearning/comments/1bkzkpq/feedback_for_my_beginner_rag_pdf_project/) , 2024-03-23-0909
```
Hello.

I wanted to create a RAG model for a T&C file of one bank. I am a beginner, and all my files are on github. [htt
ps://github.com/divakaivan/lloyds-rag-from-scratch/tree/main](https://github.com/divakaivan/lloyds-rag-from-scratch/tree
/main) \-> the main files you can look at are: [preprocess\_pdf.py](https://github.com/divakaivan/lloyds-rag-from-scratc
h/blob/main/preprocess_pdf.py) and [rag.py](https://github.com/divakaivan/lloyds-rag-from-scratch/blob/main/rag.py)

My 
main points of concern are the way I do chunking (everything I do in preprocess\_pdf.py), I have found out it's way more
 important than I initially thought, and for now, I am using a recursive char splitter from langchain. My base prompt in
 rag.py could probably use help as well. Any feedback is welcome. I am a beginner :)

At the moment, the answers are inc
onsistent, for example for the question: 'What is meant by a Business Day?' when looking at the context, the top-1 answe
r includes it and the cos\_sim is 0.8, but sometimes the llm returns that the context does not talk about the Business D
ay, even though the top-1 answer from the context is that part I mentioned.

Any help/criticism is appreciated. Thank yo
u :)

&#x200B;

if you don't want to click, here is the code:

**preprocess\_pdf.py**
```python
import re
import os
impo
rt fitz
import pandas as pd
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import R
ecursiveCharacterTextSplitter

device = 'mps'

# lbg_relationship_tnc.pdf account_bank_tnc.pdf
def open_and_read_pdf(pdf
_path: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages_n_texts = []

    for page_n, page in enumerate(doc):

        text = page.get_text()
        text = text.replace('\n', ' ').replace('  ', ' ')

        pages_n_texts.append(
{
            'page_n': page_n,
            'page_char_count': len(text),
            'page_word_count_raw': len(text.sp
lit(' ')),
            'page_sentence_count_raw': len(text.split('. ')),
            'page_token_count': len(text) / 4, 
# 1 token ~= 4 chars
            'text': text
        })

    return pages_n_texts

def create_text_splitter(chunk_size:
 int=1500, chunk_overlap: int=0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overla
p=chunk_overlap)
    return text_splitter


emb_model = SentenceTransformer('mixedbread-ai/mxbai-embed-large-v1').to(dev
ice)
#mixedbread-ai/mxbai-embed-large-v1 all-mpnet-base-v2

if __name__ == '__main__':

    pdf_path = input('Enter PDF 
name: ')

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f'The file '{pdf_path}' does not exist.')


    pages_n_texts = open_and_read_pdf(pdf_path)

    chunk_size = input('Enter chunk size(int). Default is 1500 (Enter
 -> skip): ')
    chunk_overlap = input('Enter chunk overlap(int). Default is 0 (Enter -> skip): ')
    if not chunk_siz
e:
        chunk_size = 1500
    if not chunk_overlap:
        chunk_overlap = 0

    text_splitter = create_text_splitt
er(chunk_size, chunk_overlap)
    print('Creating sentence chunks ~')
    pages_n_chunks_new = []
    for item in pages_
n_texts:
        item['sentence_chunks'] = text_splitter.split_text(item['text'])
        for chunk in item['sentence_ch
unks']:
            chunk_dict = {}
            chunk_dict['page_n'] = item['page_n']
            joined_sentence_chunk 
= ''.join(chunk).replace('  ', ' ').strip()
            joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sen
tence_chunk)
            joined_sentence_chunk = re.sub(r'\d+(\.\d+)+', '', joined_sentence_chunk)
            chunk_dic
t['sentence_chunk'] = joined_sentence_chunk

            # # add metadata
            chunk_dict['chunk_chars'] = len(jo
ined_sentence_chunk)
            chunk_dict['chunk_words'] = len([word for word in joined_sentence_chunk.split(' ')])
  
          chunk_dict['chunk_tokens'] = len(joined_sentence_chunk) / 4

            pages_n_chunks_new.append(chunk_dict)


    text_chunks = [item['sentence_chunk'] for item in pages_n_chunks_new]
    text_chunk_embs = emb_model.encode(text_
chunks, batch_size=16, convert_to_tensor=True)

    emb_chunks_df = pd.DataFrame(pages_n_chunks_new)
    # embs_only_df 
= pd.DataFrame(text_chunk_embs.to('cpu'))
    emb_chunks_df['embedding'] = text_chunk_embs.cpu().numpy().tolist()
    em
b_df_save_path = input('Enter name for embeddings csv. Default is emb_chunks_df (Enter -> skip): ')
    if not emb_df_sa
ve_path:
        emb_df_save_path = 'emb_chunks_df.csv'

    emb_chunks_df.to_csv(emb_df_save_path, index=False)
    pri
nt(f'File {emb_df_save_path} created!')
```

**rag.py**

```python
from transformers import AutoTokenizer, AutoModelForC
ausalLM, TextStreamer
from sentence_transformers import util, SentenceTransformer
import pandas as pd
import numpy as np

import torch

device = 'mps'

emb_chunks_df = pd.read_csv('emb_chunks_df.csv')

# convert embeddings back to np.array
e
mb_chunks_df['embedding'] = emb_chunks_df['embedding'].apply(lambda x: np.fromstring(x.strip('[]'), sep=', '))
embs = to
rch.tensor(np.stack(emb_chunks_df['embedding'].tolist(), axis=0), dtype=torch.float32).to(device)

pages_n_chunks = emb_
chunks_df.to_dict(orient='records')

emb_model = SentenceTransformer('mixedbread-ai/mxbai-embed-large-v1', device=device
)

def retrieve_relevant_info(query: str, embeddings: torch.tensor, model: SentenceTransformer=emb_model, n_to_retrieve:
 int=5) -> torch.tensor:
    query_emb = model.encode(query, convert_to_tensor=True)
    dot_scores = util.cos_sim(query
_emb, embeddings)[0]
    scores, indices = torch.topk(dot_scores, n_to_retrieve)
    print(scores)
    return scores, in
dices

model_id = 'google/gemma-2b-it'

tokenizer = AutoTokenizer.from_pretrained(model_id)
llm_model = AutoModelForCaus
alLM.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=False, attn_implementation='sdpa').to(device
)

def prompt_formatter(query: str, context_items: list[dict]) -> str:
    context = '- ' + '\n- '.join([item['sentence_
chunk'] for item in context_items])
    base_prompt = '''Based on the following context items, please answer the query.

Give yourself room to think by extracting relevant passages from the context before answering the query.
Don't return th
e thinking, only return the answer.
Make sure your answers are as explanatory as possible.
Use the following examples as
 reference for the ideal answer style, but don't use the below example answers as answers to the query.
\nExample 1:
Que
ry: Who can provide instructions to the bank according to the terms and conditions?
Answer: According to the terms and c
onditions, only authorized individuals can give instructions to the bank.
\nExample 2:
Query: What are your rights regar
ding the termination of services as outlined in the terms and conditions?
Answer: The terms and conditions specify the r
ights granted to you in the event of termination, including any associated procedures or obligations.
\nExample 3:
Query
: How does the bank handle refunds for incorrectly executed payment instructions, as per the terms and conditions?
Answe
r: The terms and conditions detail the process for obtaining refunds in the case of payment instructions being incorrect
ly executed by the bank.
\nExample 4:
Query: What measures are outlined in the terms and conditions to ensure the securi
ty of your accounts and payment instruments?
Answer: The terms and conditions lay out your obligations regarding the sec
urity of your accounts, payments, and payment instruments, along with any corresponding measures implemented by the bank
.
\nNow use the following context items to answer the user query:
{context}
\nRelevant passages: <extract relevant passa
ges from the context here>
User query: {query}
Answer:'''

    base_prompt = base_prompt.format(context=context, query=q
uery)
    
    # make sure the inputs to the model are in the same way that they have been trained
    dialogue_template
 = [
        {
            'role': 'user',
            'content': base_prompt
        }
    ]
    prompt = tokenizer.app
ly_chat_template(conversation=dialogue_template, tokenize=False, add_generation_prompt=True)

    return prompt

def ask
(query: str, temperature: float=0.2, max_new_tokens: int=256, format_answer_text: bool=True, return_context: bool=False)
:
    # -------- RETRIEVAL --------
    scores, indices = retrieve_relevant_info(query, embs, n_to_retrieve=10)
    cont
ext_items = [pages_n_chunks[i] for i in indices]
    for i, item in enumerate(context_items):
        item['score'] = sc
ores[i].cpu()

    # -------- AUGMENTATION --------
    prompt = prompt_formatter(query, context_items)

    # -------- 
GENERATION --------
    input_ids = tokenizer(prompt, return_tensors='pt').to(device)
    streamer = TextStreamer(tokeni
zer, skip_prompt=True, skip_special_tokens=True)
    outputs = llm_model.generate(**input_ids, streamer=streamer, temper
ature=temperature, do_sample=True, max_new_tokens=max_new_tokens)
    output_text = tokenizer.decode(outputs[0])

    if
 format_answer_text:
        output_text = output_text.replace(prompt, '').replace('<bos>', '').replace('<eos>', '')

  
  # if not return_context:
        # return output_text
    
    # return output_text, context_items

if __name__ == '__
main__':

    print('Enter a query:\n')
    query = input()
    print('estimating ~ estimating ~')
    ask(query, temper
ature=0.7, return_context=False)
```
```
---

     
 
all -  [ I want to make LLM model respond to queries related to a set of retrieved conversation from Vector D ](https://www.reddit.com/r/MLQuestions/comments/1bkywiw/i_want_to_make_llm_model_respond_to_queries/) , 2024-03-23-0909
```
Hi, I have created an embedding from multiple conversation of two person and pushed it to Qdrant DB. The retreival works
 good, Now I want to integrate an LLM model which answers queries from the relevant conversation retrieved from the vect
or DB. I am not sure what to use here. Go with Langchains or LlamaIndex.
```
---

     
 
all -  [ How to process each source in Vector db individually ? ](https://www.reddit.com/r/LangChain/comments/1bkysyf/how_to_process_each_source_in_vector_db/) , 2024-03-23-0909
```
If I have 100 documents in my vector db. In the metadata t are total of 5 sources and each source have 20 documents in t
he vector db.   


So now as query is given by the user I want to process  relevant documents of each source separately 
and then combine the answers.   


Can somebody help me on how to do this in an optimized way? 
```
---

     
 
all -  [ Dependency issues when adding langchain_mistralai to the project dependencies ](https://www.reddit.com/r/LangChain/comments/1bkxdyu/dependency_issues_when_adding_langchain_mistralai/) , 2024-03-23-0909
```
Couldn't find any other post on this topic but I'm having an issue with langchain\_mistralai library. We're using weavia
te\_client 4.5.4 which requires httpx version 0.27.0. However langchain\_mistralai is not compatible with httpx versions
 > 0.26.0. Will this be fixed at some point or should I give up and find a workaround? (downgrading weaviate\_client is 
not an option, since it has needed functionalities which can't be sacrificed XD)
```
---

     
 
all -  [ Why this error? ](https://www.reddit.com/r/LangChain/comments/1bkxck3/why_this_error/) , 2024-03-23-0909
```
Hey i am getting this error:

 openai.NotFoundError: Error code: 404 - {'error':{'code':'404', 'message': 'Resource not 
found'}}

I used: 
From langchain_community.llms import OpenAI

From langchain.chains import LLMChain

Code: 
llm= OpenA
I(model_name='modelname')

Output=LLMChain(prompt=prompt, llm=llm).run('query')
```
---

     
 
all -  [ Why is my chain.invoke({}) command giving the full model response instead of just AIMessage(content= ](https://www.reddit.com/r/LangChain/comments/1bkwdjn/why_is_my_chaininvoke_command_giving_the_full/) , 2024-03-23-0909
```
I am using ChatVertexAI and the ChatPromptTemplate to provide the model with a system message, and a user message, both 
of which are stored in separate variables which return a string. 

[Prompt template](https://preview.redd.it/6raj796a7vp
c1.png?width=831&format=png&auto=webp&s=61b9af92cc549d82da840310606772c3d3d0c51e)

The chain uses LCEL to define the cha
in for the invoke command 

[The chain and invoke command](https://preview.redd.it/1ud0215i7vpc1.png?width=847&format=pn
g&auto=webp&s=604c30b0fdf719ff723c86abda5757ccd1146613)

However, the output that I get includes details that I should g
et if the command was chain.generate() and not chain.invoke(). It should not include all of the response metadata that i
s being printed here. 

https://preview.redd.it/vzocmpoy7vpc1.png?width=1103&format=png&auto=webp&s=3890c438dfef3a70cb58
01c820380236a7a62435

Should'nt the output contain only AIMessage(content='.........') and not anything else? I Know I c
an use definition.content in this case, but in reality I cannot use that as this output is going to be used by langgraph
 for creating a reflection agent, in which I need to use the output like it is. 

I checked all documentation and my pro
mpt template as well the call to the LLM is exactly as it should be, but in the examples they show, the chain.invoke com
mand should not print response metadata.

&#x200B;
```
---

     
 
all -  [ Build an LLM-powered application using LangChain ](https://www.leewayhertz.com/build-llm-powered-apps-with-langchain/) , 2024-03-23-0909
```

```
---

     
 
all -  [ How to build AI agents for information retrieval online ](https://www.reddit.com/r/LangChain/comments/1bktz0j/how_to_build_ai_agents_for_information_retrieval/) , 2024-03-23-0909
```
\[New in my AI agent journey\]

  
Hi,

As I mentionned in the title of this post, I'm wondering if Langchain is the bes
t framework to build AI agents that are able to retrieve information online.  


I'll give you one example :   


* Step
 1 :I would like to give my agent a list of website and ask them if this company is a B2C company or a B2B company.
* St
ep 2 : Chain this agent to another : if it's a B2B company find the pricing

Is is possible to do so with Langchain ? 


If yes, do you know where I could find a tutorial to get me started ?

If not what is the best framework out there ? I s
aw [https://github.com/joaomdmoura/crewai/](https://github.com/joaomdmoura/crewai/) & [superagent.sh](https://superagent
.sh) but I'm not sure if these are exactly what I'm looking for.  


Thanks for your help !  

```
---

     
 
all -  [ Please explain the logic behind the evaluation of the llama index. ](https://www.reddit.com/r/LangChain/comments/1bktatx/please_explain_the_logic_behind_the_evaluation_of/) , 2024-03-23-0909
```
I wrote this after looking at the Ensemble Retriever docs.

[https://docs.llamaindex.ai/en/stable/examples/retrievers/en
semble\_retrieval/](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)

&#x200B;

And can you
 explain the code for the evaluation part in detail with comments? A post is happening, but I don't know what it is. Bel
ow is the evaluation code

&#x200B;

    from llama_index.core.evaluation import (
         CorrectnessEvaluator,
      
   SemanticSimilarityEvaluator,
         RelevancyEvaluator,
         FaithfulnessEvaluator,
         PairwiseComparison
Evaluator,
    )
    
    from llama_index.core.evaluation.eval_utils import (
         get_responses;
         get_resu
lts_df;
    )
    from llama_index.core.evaluation import BatchEvalRunner
    
    import numpy as np
    
    evaluator
_c = CorrectnessEvaluator(llm=eval_llm)
    evaluator_s = SemanticSimilarityEvaluator()
    evaluator_r = RelevancyEvalu
ator(llm=eval_llm)
    evaluator_f = FaithfulnessEvaluator(llm=eval_llm)
    
    pairwise_evaluator = PairwiseCompariso
nEvaluator(llm=eval_llm)
    
    
    max_samples = 5
    
    eval_qs = eval_dataset.questions
    qr_pairs = eval_dat
aset.qr_pairs
    ref_response_strs = [r for (_, r) in qr_pairs]
    
    base_query_engine = vector_indices[-1].as_quer
y_engine(similarity_top_k=2)
    
    query_engine = RetrieverQueryEngine(retriever, node_postprocessors=[reranker])
   
 
    base_pred_responses = get_responses(
         eval_qs[:max_samples], base_query_engine, show_progress=True
    )
 
   
    pred_responses = get_responses(
         eval_qs[:max_samples], query_engine, show_progress=True
    )
    
    
sponse_strs = [str(p) for p in pred_responses]
    base_pred_response_strs = [str(p) for p in base_pred_responses]
    

    evaluator_dict = {
         'correctness': evaluator_c,
         'faithfulness': evaluator_f,
         'semantic_sim
ilarity': evaluator_s,
    }
    batch_runner = BatchEvalRunner(evaluator_dict, workers=1, show_progress=True)
    
    
eval_results = await batch_runner. evaluate_responses(
         queries=eval_qs[:max_samples],
         responses=pred_r
esponses[:max_samples],
         reference=ref_response_strs[:max_samples],
    )
    
    base_eval_results = await bat
ch_runner.aevaluate_responses(
         queries=eval_qs[:max_samples],
         responses=base_pred_responses[:max_sampl
es],
         reference=ref_response_strs[:max_samples],
    )
    
    results_df = get_results_df(
         [eval_resu
lts, base_eval_results],
         ['Ensemble Retriever', 'Base Retriever'],
         ['correctness', 'faithfulness', 'se
mantic_similarity'],
    )
    display(results_df)
```
---

     
 
all -  [ How can I combine ChromaDB and SQL in langchain? ](https://www.reddit.com/r/LangChain/comments/1bkqww1/how_can_i_combine_chromadb_and_sql_in_langchain/) , 2024-03-23-0909
```
I have a ChromaDB database which I can query information about a specific data, however, this data also has numerical da
ta that I would like to transform into a SQL database, in .db form.

However, I want to be able to infer whether the LLM
 should call the vector db, and go through a ChromaDB chain for the answer, or go through an SQL chain. 

How can I make
 this happen, automatically as the user asks questions? Basically, how can I create an agent that can determine which on
e to run?
```
---

     
 
all -  [ Chatbot in production  ](https://www.reddit.com/r/LangChain/comments/1bkmo3b/chatbot_in_production/) , 2024-03-23-0909
```
Any of you are happy and have almost perfect result either their LLM chatbots with business data?
Happy to discuss
```
---

     
 
all -  [ Daily struggles with my LLM based chatbot in production ](https://www.reddit.com/r/LangChain/comments/1bklgf7/daily_struggles_with_my_llm_based_chatbot_in/) , 2024-03-23-0909
```
What are some challenges you face after deploying your LLM based application in production? 

My only goal is to improve
 the accuracy of my chatbot. It seems like everything boils down to this unless there are any other special usecases you
 are using the LLMs for. Basically. I try to monitor for all the responses of my chatbot and measure them objectively so
 I can tweak and improve the accuracy. This seems pretty basic. But, what are some of the other levers that I can pull t
o improve the accuracy of my RAG based chat application?

&#x200B;

I am also building a tooling for tracing and monitor
ing the responses with higher cardinality compared to the ones that are in the market. Plan to open source it pretty soo
n.
```
---

     
 
all -  [ chunking strategies for code? ](https://www.reddit.com/r/LangChain/comments/1bkkqel/chunking_strategies_for_code/) , 2024-03-23-0909
```
I'm looking to build a RAG app on our github repositories but wanted to ask if anyone has done something like this and w
hat chunking strategies worked and didn't work. I've been looking at semantic chunking but unsure how this would work wi
th code? 
```
---

     
 
all -  [ Okahu AI Observability is now in preview! ](https://www.reddit.com/r/AIObservability/comments/1bkknxl/okahu_ai_observability_is_now_in_preview/) , 2024-03-23-0909
```
Observe your AI apps and cloud infra they run on with [Okahu](https://www.okahu.ai/) to understand how to make them work
 better - more reliable, performant and cost-effective.

Check out [What’s Okahu you ask?](https://youtu.be/JOno9MXenps)
 on Youtube

Check out [this Github repo](https://github.com/okahu/okahu-demo-openai) to try Okahu yourself with a sampl
e chatbot that uses OpenAI and Langchain right from your Github Codespaces and Okahu developer API. 

Give us feedback o
n what observations and systems you want use to support next! 

Add a comment to this discussion or reach out to us at [
dx@okahu.ai](mailto:dx@okahu.ai). 
```
---

     
 
all -  [ Need advice for structuring multimodal data for RAG ](https://www.reddit.com/r/LangChain/comments/1bkhdqe/need_advice_for_structuring_multimodal_data_for/) , 2024-03-23-0909
```
Hey folks,  
I am in the process of building my first custom GPT and have some questions regarding how to work properly 
with multimodal data. Let me explain what I am trying to achieve.  
I am creating a helper tool that will assist me in a
nalyzing various pricing strategies of different SaaS tools. I have a dataset of 100k SaaS companies that have been labe
led in some way, so I can cluster them based on their industry, category, etc.

Here is what I have as an input for my G
PT so far:

1. I have collected screenshots of their pricing pages, which are stored in S3.
2. I have collected the HTML
 for the pricing pages, which is stored in MongoDB.
3. I have a table of the companies with enriched data.

I would like
 to build RAG on top of these documents, but I am a bit concerned about the next steps. My plan is to start with a simpl
e one and use LlamaIndex. Here are the steps I have in mind:

1. Connect the data to the LlamaHub and pick the proper da
tabase. I want to keep the connection between the three mediums. and thus, I am not sure which database is best for my c
ase. Should I use a vector database, graph database, or key-value database here?
2. Query the data and come up with eval
uation metrics based on expert knowledge.

I have some questions along the way:

1. Should I parse the data from the scr
eenshots and HTML structure beforehand, or can I put it into storage as it is? Will it help with the quality of RAG?
```
---

     
 
all -  [ text-embedding-3-large chunking question for RAG ](https://www.reddit.com/r/LangChain/comments/1bkh8wq/textembedding3large_chunking_question_for_rag/) , 2024-03-23-0909
```
We know 3-large has a 8191 token context window. I have text articles that are anywhere from 2500-4500 tokens each. Is t
here any advantage to chunking these? Or will I lose some of the context splitting articles into pieces?

Is it better t
o just get embeddings on whole articles or is it still a good idea to split them up into paragraphs? Or both? Feed it wh
ole articles and paragraphs?

Thanks in advance for your insight.
```
---

     
 
all -  [ LangChain Functionality in Node.js and Python for Text Processing ](https://www.reddit.com/r/LangChain/comments/1bkg3bg/langchain_functionality_in_nodejs_and_python_for/) , 2024-03-23-0909
```
Does LangChain for Node.js offer the same level of functionality as its Python counterpart when it comes to functions an
d features? 

If not, is there an alternative framework ?

Context : I am familiar with Node.js. I am looking to interac
t with an LLM for text extraction, NER, and coherence. I aim to take the response to create nodes, relationships, and la
bels in a Neo4j graph database.
```
---

     
 
all -  [ Struggling to get an interview for entry level Machine Learning Engineer/Data Science roles ](https://www.reddit.com/r/resumes/comments/1bkcno9/struggling_to_get_an_interview_for_entry_level/) , 2024-03-23-0909
```
As mentioned in the title, I'm a new grad looking to break into the ML space but am struggling to get even a single inte
rview. Please review my resume and let me know of any suggestions. Feel free to be harsh. Thanks!

https://preview.redd.
it/h8uy6n247qpc1.png?width=913&format=png&auto=webp&s=9c3aa991ae69e54de74ec1eda3ef537c89dde477
```
---

     
 
all -  [ Rule Based LLM Chatbot ](https://www.reddit.com/r/LangChain/comments/1bkcllq/rule_based_llm_chatbot/) , 2024-03-23-0909
```
I want to build a LLM Chatbot that can follow a particular flow the one we build in intent based chatbot frameworks. I w
ant the llm to collect some information from user based on it fetch some data handle fallback queries and it should not 
deviate from the flow handling multi turn conversations.Any idea or open source framework that does this? Basically I wa
nt to use RASA stories and feed it to LLM so that it can follow a particular conversational flow. 
```
---

     
 
all -  [ 22 New Data Science, Data Engineering and Machine Learning jobs ](https://www.reddit.com/r/jobbit/comments/1bkbtai/22_new_data_science_data_engineering_and_machine/) , 2024-03-23-0909
```
|Job Title|Company|Location|Country|Skills|
|:-|:-|:-|:-|:-|
|[Data Scientist](https://datayoshi.com/offer/575107/data-s
cientist)|[CodeUp](https://www.datayoshi.com/company/codeup-jobs)|[Los Angeles](https://datayoshi.com/offer/575107/data-
scientist)|[United States](https://datayoshi.com/offer/575107/data-scientist)|[Machine Learning, Data Visualization](htt
ps://datayoshi.com/offer/575107/data-scientist)|
|[(Senior) Data Analyst – Digital Analytics (m/f/d)](https://datayoshi.
com/offer/945939/senior-data-analyst-digita)|[L'Oréal](https://www.datayoshi.com/company/l'oréal-jobs)|[Düsseldorf](http
s://datayoshi.com/offer/945939/senior-data-analyst-digita)|[Germany](https://datayoshi.com/offer/945939/senior-data-anal
yst-digita)|[SQL, Power BI, Python](https://datayoshi.com/offer/945939/senior-data-analyst-digita)|
|[Senior Data Analys
t - Demand & Assortment Planning...](https://datayoshi.com/offer/660763/senior-data-analyst-demand)|[Decathlon Digital](
https://www.datayoshi.com/company/decathlon-digital-jobs)|[Paris](https://datayoshi.com/offer/660763/senior-data-analyst
-demand)|[France](https://datayoshi.com/offer/660763/senior-data-analyst-demand)|[Modeling, Spark, Python](https://datay
oshi.com/offer/660763/senior-data-analyst-demand)|
|[Développeur Big Data / Data analyst H/F](https://datayoshi.com/offe
r/254174/developpeur-big-data-data-an)|[CNAM](https://www.datayoshi.com/company/cnam-jobs)|[Paris](https://datayoshi.com
/offer/254174/developpeur-big-data-data-an)|[France](https://datayoshi.com/offer/254174/developpeur-big-data-data-an)|[S
QL, Java, Tableau](https://datayoshi.com/offer/254174/developpeur-big-data-data-an)|
|[Senior Data Analyst - Value Chain
 (f/m/d)](https://datayoshi.com/offer/469469/senior-data-analyst-value-ch)|[Decathlon Digital](https://www.datayoshi.com
/company/decathlon-digital-jobs)|[Croix](https://datayoshi.com/offer/469469/senior-data-analyst-value-ch)|[France](https
://datayoshi.com/offer/469469/senior-data-analyst-value-ch)|[Tableau, scikit-learn, Spark](https://datayoshi.com/offer/4
69469/senior-data-analyst-value-ch)|
|[Stagiaire Data Engineer (6 mois)](https://datayoshi.com/offer/149005/stagiaire-da
ta-engineer-6-moi)|[AXA Partners](https://www.datayoshi.com/company/axa-partners-jobs)|[Malakoff](https://datayoshi.com/
offer/149005/stagiaire-data-engineer-6-moi)|[France](https://datayoshi.com/offer/149005/stagiaire-data-engineer-6-moi)|[
Spark](https://datayoshi.com/offer/149005/stagiaire-data-engineer-6-moi)|
|[Data Analyst](https://datayoshi.com/offer/10
7630/data-analyst)|[Hatch](https://www.datayoshi.com/company/hatch-jobs)|[Sydney](https://datayoshi.com/offer/107630/dat
a-analyst)|[Australia](https://datayoshi.com/offer/107630/data-analyst)|[](https://datayoshi.com/offer/107630/data-analy
st)|
|[Data Engineer](https://datayoshi.com/offer/394607/data-engineer)|[BCT Resourcing](https://www.datayoshi.com/compa
ny/bct-resourcing-jobs)|[London](https://datayoshi.com/offer/394607/data-engineer)|[United Kingdom](https://datayoshi.co
m/offer/394607/data-engineer)|[Python, Scala](https://datayoshi.com/offer/394607/data-engineer)|
|[Machine Learning Engi
neer](https://datayoshi.com/offer/355609/machine-learning-engineer)|[IQVIA](https://www.datayoshi.com/company/iqvia-jobs
)|[Warsaw](https://datayoshi.com/offer/355609/machine-learning-engineer)|[Poland](https://datayoshi.com/offer/355609/mac
hine-learning-engineer)|[Python, Machine Learning](https://datayoshi.com/offer/355609/machine-learning-engineer)|
|[Data
 Engineer](https://datayoshi.com/offer/614299/data-engineer)|[9am](https://www.datayoshi.com/company/9am-jobs)|[Austria]
(https://datayoshi.com/offer/614299/data-engineer)|[Austria](https://datayoshi.com/offer/614299/data-engineer)|[ETL, SQL
, Python](https://datayoshi.com/offer/614299/data-engineer)|
|[AI Engineer (Python, Langchain)](https://datayoshi.com/of
fer/240666/ai-engineer-python-langchain)|[JUPUS](https://www.datayoshi.com/company/jupus-jobs)|[Germany](https://datayos
hi.com/offer/240666/ai-engineer-python-langchain)|[Germany](https://datayoshi.com/offer/240666/ai-engineer-python-langch
ain)|[Python](https://datayoshi.com/offer/240666/ai-engineer-python-langchain)|
|[Staff/Senior Data Engineer](https://da
tayoshi.com/offer/793093/staff-senior-data-engineer)|[Glia](https://www.datayoshi.com/company/glia-jobs)|[Spain](https:/
/datayoshi.com/offer/793093/staff-senior-data-engineer)|[Spain](https://datayoshi.com/offer/793093/staff-senior-data-eng
ineer)|[SQL, Kafka](https://datayoshi.com/offer/793093/staff-senior-data-engineer)|
|[Data Analyst (m/w/d)](https://data
yoshi.com/offer/270696/data-analyst-m-w-d)|[Pink Personalmanagement GmbH](https://www.datayoshi.com/company/pink-persona
lmanagement-gmbh-jobs)|[Herford](https://datayoshi.com/offer/270696/data-analyst-m-w-d)|[Germany](https://datayoshi.com/
offer/270696/data-analyst-m-w-d)|[Power BI](https://datayoshi.com/offer/270696/data-analyst-m-w-d)|
|[Master Data Analys
t](https://datayoshi.com/offer/155622/master-data-analyst)|[Hach](https://www.datayoshi.com/company/hach-jobs)|[Berlin](
https://datayoshi.com/offer/155622/master-data-analyst)|[Germany](https://datayoshi.com/offer/155622/master-data-analyst
)|[SQL](https://datayoshi.com/offer/155622/master-data-analyst)|
|[Junior Data Engineer](https://datayoshi.com/offer/323
784/junior-data-engineer)|[Team Remotely Inc](https://www.datayoshi.com/company/team-remotely-inc-jobs)|[New Haven](http
s://datayoshi.com/offer/323784/junior-data-engineer)|[United States](https://datayoshi.com/offer/323784/junior-data-engi
neer)|[Modeling, Scala](https://datayoshi.com/offer/323784/junior-data-engineer)|
|[Data Scientist 1](https://datayoshi.
com/offer/248159/data-scientist-1)|[PayPal](https://www.datayoshi.com/company/paypal-jobs)|[Bengaluru](https://datayoshi
.com/offer/248159/data-scientist-1)|[India](https://datayoshi.com/offer/248159/data-scientist-1)|[SQL, Python, Machine L
earning](https://datayoshi.com/offer/248159/data-scientist-1)|
|[Machine Learning Engineer II](https://datayoshi.com/off
er/367087/machine-learning-engineer-ii)|[The Shoprite Group of Companies](https://www.datayoshi.com/company/the-shoprite
-group-of-companies-jobs)|[Brackenfell](https://datayoshi.com/offer/367087/machine-learning-engineer-ii)|[South Africa](
https://datayoshi.com/offer/367087/machine-learning-engineer-ii)|[Machine Learning](https://datayoshi.com/offer/367087/m
achine-learning-engineer-ii)|
|[AI Product Manager](https://datayoshi.com/offer/234947/ai-product-manager)|[Match Health
](https://www.datayoshi.com/company/match-health-jobs)|[Birmingham](https://datayoshi.com/offer/234947/ai-product-manage
r)|[United Kingdom](https://datayoshi.com/offer/234947/ai-product-manager)|[Machine Learning](https://datayoshi.com/offe
r/234947/ai-product-manager)|
|[Senior  Data Analyst](https://datayoshi.com/offer/950284/senior-data-analyst)|[Optum](ht
tps://www.datayoshi.com/company/optum-jobs)|[Dublin](https://datayoshi.com/offer/950284/senior-data-analyst)|[Ireland](h
ttps://datayoshi.com/offer/950284/senior-data-analyst)|[Power BI, AWS, Data Visualization](https://datayoshi.com/offer/9
50284/senior-data-analyst)|
|[Data Engineer](https://datayoshi.com/offer/981999/data-engineer)|[MindPal](https://www.dat
ayoshi.com/company/mindpal-jobs)|[Lyon](https://datayoshi.com/offer/981999/data-engineer)|[France](https://datayoshi.com
/offer/981999/data-engineer)|[AWS](https://datayoshi.com/offer/981999/data-engineer)|
|[Junior Machine Learning Engineer
](https://datayoshi.com/offer/830779/junior-machine-learning-engine)|[Patterned Learning Career](https://www.datayoshi.c
om/company/patterned-learning-career-jobs)|[Enterprise](https://datayoshi.com/offer/830779/junior-machine-learning-engin
e)|[United States](https://datayoshi.com/offer/830779/junior-machine-learning-engine)|[Machine Learning, Deep Learning](
https://datayoshi.com/offer/830779/junior-machine-learning-engine)|
|[Data Engineer H/F](https://datayoshi.com/offer/849
434/data-engineer-h-f)|[LesJeudis](https://www.datayoshi.com/company/lesjeudis-jobs)|[Clichy](https://datayoshi.com/offe
r/849434/data-engineer-h-f)|[France](https://datayoshi.com/offer/849434/data-engineer-h-f)|[SQL](https://datayoshi.com/o
ffer/849434/data-engineer-h-f)|
                        
 Hey, here are 22 New Data Science, Data Engineering and Machin
e Learning jobs. 

 For more, check our Google sheet with more opportunities in Data Science and Machine Learning (updat
ed each week) [here](https://docs.google.com/spreadsheets/d/1Vsg1Jmc0ZIDc_tPqZTzhbgxGIeTDQkUsBySMNbbCFI4/) 

 If you wan
t to take some Data and ML courses, click [here](https://learncrunch.com/courses?utm_source=reddit&source=reddit) 

  Le
t me know if you have any questions. Cheers!
```
---

     
 
all -  [ Suggestions on working agents and base LLMs? ](https://www.reddit.com/r/LangChain/comments/1bkb1kc/suggestions_on_working_agents_and_base_llms/) , 2024-03-23-0909
```
Hi. I’m testing a variety of LLaMa2 7b and 13b (Hermes2Pro, MistralInstruct0.2, Chat, Solar10) as base for the React age
nt, but I can’t get outputs consistently as I’m encountering these issues:

1. After providing the final answer, the LLM
 keeps running other actions and it gets off track with eg. Non relevant questions or even random programming code.
2. S
ometimes it calls the tools incorrectly, especially if I switch to the structured chat agent (non existing arguments or 
swapped args between functions).

What I’m guessing is that I need larger models. I would appreciate someone else’s expe
rience and takes on this. Thank you very much!

```
---

     
 
all -  [ In need of data scientist in ATLANTA/GA ](https://www.reddit.com/r/DataScientist/comments/1bk8wsd/in_need_of_data_scientist_in_atlantaga/) , 2024-03-23-0909
```
  

# data scientist ( long term role)

**Role - Data Scientist**

**Skills Required** \-Proficiency in SQL, Natural Lan
guage Processing (NLP) using technologies like PyTorch, TensorFlow, and Apache Spark is essential. A strong foundation i
n Python programming and familiarity with Databricks and pandas for data manipulation is required.  
Machine Learning En
gineer Comprehensive understanding of Machine Learning models and algorithms is necessary. The ability to script in Pyth
on for data analysis, and experience with Python libraries such as HuggingFace, Langchain, scikit-learn and Keras is exp
ected.

send your resume to [kiruthick.murali@mazosol.com](mailto:kiruthick.murali@mazosol.com)
```
---

     
 
all -  [ data scientist ( long term role) ](https://www.reddit.com/r/atlantajobs/comments/1bk8uqr/data_scientist_long_term_role/) , 2024-03-23-0909
```
**Role - Data Scientist**	

  **Skills Required** \-Proficiency in SQL,  Natural Language Processing (NLP) using technol
ogies like PyTorch, TensorFlow, and Apache Spark is essential. A strong foundation in Python programming and familiarity
 with Databricks and pandas for data manipulation is required.  
Machine Learning Engineer	Comprehensive understanding o
f Machine Learning models and algorithms is necessary. The ability to script in Python for data analysis, and experience
 with Python libraries such as HuggingFace, Langchain, scikit-learn and Keras is expected.

send your resume to [kiruthi
ck.murali@mazosol.com](mailto:kiruthick.murali@mazosol.com)

&#x200B;
```
---

     
 
all -  [ Need input on Software Project ](https://www.reddit.com/r/LangChain/comments/1bk8t5f/need_input_on_software_project/) , 2024-03-23-0909
```
I'm building a software application. I want to use a LLM as the basis. I will finetune the model with about 20,000 pages
 of legal text. Specifically laws all around the country. I will then use the trained model to answer help companies cre
ate compliant products and services. At the moment I am unsure as to the best way to go about it. My initial thought was
 to use gpt 3.5 and then further train it with the 20,000 pages of text. The text will be broken down by state and feder
al agencies. This text will be added to as new laws and regulations are passed.

&#x200B;

The goal is for the model to 
only answer based on the data set it's finetuned with. The data will be broken down by state. For example if they want i
nformation about loan requirements, they will ask the system and it will return with an outline of the requirements for 
loans by state. It will respond in a way that's easy to understand.

&#x200B;

My thinking is once I have all the data c
ollected, using Langchain to fine tune the LLM. Am I on the right path here?
```
---

     
 
all -  [ Planning the development for a new app for a client with 2M+ existing users ](https://www.reddit.com/r/softwarearchitecture/comments/1bk83el/planning_the_development_for_a_new_app_for_a/) , 2024-03-23-0909
```
**TLDR;**

Built a GPT wrapper app with LangChain+Vector storage using Flowai + NextJS + Clerk + Firebase. Should I cont
inue building with this for a scalable app (2M+ users) or write my own services/APIs using Node.js, Langchain, Postgres 
(pgvector)?

**Why thinking of scale from the start?**  
I run a software outsourcing business. Recently got a project f
rom a client who is running a B2C app with 2M+ users. They're planning to launch a new app, the development has to be do
ne from scratch. The only 2 business requirements I have been give is that they need faster iterations and scalable appl
ication. The reason they need scale from the start it because they've planned massive PR activities around the launch an
d are also looking at moving their existing users to the new app, thereby shutting down the existing app.

**App Synopsi
s**

1. The app is largely a wrapper on GPT with very few REST APIs:
2. Auth Module
3. Uploading content to store in a V
ector DB
4. Storing/Retrieving conversation history from DB
5. Payment Module
6. GPT communication layer with Langchain 
+ prompt templates

**Work Done**

As part of my pitch, I had created a quick demo using NextJS + Clerk + Pinecone + Flo
wAI + Firebase. It took me a total of 5 days to create this working Demo MVP.

**My Confusion**

1. Should I continue wi
th this stack itself, and work to refine the frontend and additional minor changes?
2. If yes, will that be scalable eno
ugh?
3. Should I write code the traditional way, wherein I create my own services for communicating with GPT, APIs, etc.
 using Node.js (Nest.js), mongoDB + Prisma, and use self hosted vector storage (Postgres + pgvector)?
```
---

     
 
all -  [ Best way to create an AI browsing agent ](https://www.reddit.com/r/LangChain/comments/1bk4v99/best_way_to_create_an_ai_browsing_agent/) , 2024-03-23-0909
```
Hi folks!

I have been interested in AI for some time, but now the time has come for I want to create a self-browsing ag
ent that answers a certain question.

Couple of examples:

1️⃣ Prompt: what is the company [www.segment.com](https://www
.segment.com) about?

\- Should execute a Google search  
\- Navigate to the about-us page  
\- Read the page and return
 the result

&#x200B;

2️⃣ Prompt: what is the difference between [www.segment.com](https://www.segment.com) and [www.in
tercom.com](https://www.intercom.com)?

\- Should split this into multiple tasks, doing something similar to the workflo
w above.  
\- Returns a detailed comparison based on the scanned pages

&#x200B;

What are the best ways of implementing
 this? Are there any open-source frameworks that I might get inspired by?
```
---

     
 
all -  [ My debut book on GenAI is a  International Bestseller now ! ](https://i.redd.it/j9xhh57o9opc1.png) , 2024-03-23-0909
```
I'm happy to share that my debut book 'LangChain in your Pocket: Beginners guide to building Generative AI applications 
using LLMs' that was released in late Jan'24 is now amongst International Bestsellers (AI category) on amazon.com . A bi
g thanks to everyone for the support !!

You can check out the book here :  https://amzn.in/d/iWh7a7Y


```
---

     
 
all -  [ Store metadata in faiss and retrieve along with embedding? ](https://www.reddit.com/r/LocalLLaMA/comments/1bk3tkw/store_metadata_in_faiss_and_retrieve_along_with/) , 2024-03-23-0909
```
Hey everyone, just looking for some opinions/suggestions or maybe an example if you have one to help me move forward on 
this project.

To give some background,

- using GPT I’ve summarized about 500 different docs, each about 6000 words ori
ginally now condensed down to around 300

- with those summaries, I intend to create embeddings using langchain faiss an
d store them in a vector database

- along with each embedding set I want to attach a metadata tag that will link back t
o the original full text doc

- when the similarity search returns the most relevant embeddings (based on the summaries)
, I will pull the metadata tag that links to the full docs for each relevant summary, and pass all of the full docs to G
PT to provide a thorough answer 

I’m just having trouble figuring out how to tag the meta data with my embeddings and h
ow to capture it in the results from the similarity search. Does anyone have any examples similar to this that they coul
d share? 
```
---

     
 
all -  [ Talk with your Data! (LangChain + Streamlit) ](https://www.reddit.com/r/MediumApp/comments/1bk2nio/talk_with_your_data_langchain_streamlit/) , 2024-03-23-0909
```
Read my article to learn how to build a simple GenAI bot, with LangChain and Streamlit in Python.

Give it a dataset and
 get straight answers on it!

[https://medium.com/python-in-plain-english/talk-with-your-data-c26aac1836b2](https://medi
um.com/python-in-plain-english/talk-with-your-data-c26aac1836b2)
```
---

     
 
all -  [ How to build a RAG on structed data? ](https://www.reddit.com/r/LangChain/comments/1bk0kyo/how_to_build_a_rag_on_structed_data/) , 2024-03-23-0909
```
I have a word doc and an excel file whose information is interconnected? The excel file outlines the process steps and t
he word file has process specifics. 

I want to build a RAG by leveraging these two files to generate a document based o
n some prompts. What is the best strategy to do it?
```
---

     
 
all -  [ Creating chatbot of characters using RAG ](https://www.reddit.com/r/LangChain/comments/1bk0bo3/creating_chatbot_of_characters_using_rag/) , 2024-03-23-0909
```
I have the biography of a fictional character. It is about 160 pages long. How do I create a chatbot of this character w
ith memory using RAG? I am using Gemini btw. 
```
---

     
 
all -  [ [For Hire] Ex-Booking[dot]com Data Analyst and GenAI specialist at a Startup [35 USD/hr] ](https://www.reddit.com/r/SaaS/comments/1bjzsxo/for_hire_exbookingdotcom_data_analyst_and_genai/) , 2024-03-23-0909
```
Hey, I have been using this subreddit to get clients and have completed 3 jobs here, all with good reviews.

Here are my
 skills and experience:

1) Technical Skills: Python, SQL, R 

2) Academics: Bs Econometrics, Mathematics and Computer S
cience

3) Specialty: GenAI, Statistics, Data Visualization.

4) Sectors: Databases, Hospitality, ecommerce and Telecom



Here are some of my projects (I write extensively on Medium):

Link: https://arslanshahid-1997.medium.com/using-langch
ain-to-teach-an-llm-to-write-like-you-aab394d54792

Link: https://towardsdatascience.com/money-balling-cricket-probabili
ty-of-100-using-repeated-conditioning-2fc8dbceb42e


I have over 4+ years experience in Data Science. 


Please do reach
 out, fair rate of 35 USD/hr. 
```
---

     
 
all -  [ Langchain in Production (& Alternatives) ](https://www.reddit.com/r/LangChain/comments/1bjxx32/langchain_in_production_alternatives/) , 2024-03-23-0909
```
Has anyone here succesfully deployed LangChain in production? If yes, what were the main issues enountered and how did y
ou approach them?

If not, what alternatives did you use or considering (e.g. Haystack etc.) ?
```
---

     
 
all -  [ what is the advantage of overlapping in chunking strategy ](https://www.reddit.com/r/LangChain/comments/1bjxvov/what_is_the_advantage_of_overlapping_in_chunking/) , 2024-03-23-0909
```
I am implementing RAG and trying to understand what's the advantage of Overlapping.  
Consider this text:  
`'One of the
 most important things I didn't understand about the world when I was a child is the degree to which the returns for per
formance are superlinear.'`  
 which is chunked and overlapped as  using Naive or any strategy :  
`chunk 1 : One of the
 most important things`  
`Chunk 2 : things I didn't understand about`  
`chunk 3: about the world when I was a child`  

and so on..  
As you can see there is a word overlap with the chunks.   
What advantage does LLM get when you feed over
lapping  `chunk2` and `chunk3` to execute RAG prompt against a user query. 
```
---

     
 
all -  [ Best Search Tool in Langchain  ](https://www.reddit.com/r/LangChain/comments/1bjsx89/best_search_tool_in_langchain/) , 2024-03-23-0909
```
Hi all, was going through the search tools available via langchain. Just wanted to check which is the best one to use? W
hat are the key aspects to consider other than cost? If anyone who has used/compared these APIs that would be a great va
lue add to my research 
```
---

     
 
all -  [ Best Search Tool in Langchain  ](https://www.reddit.com/r/Langchaindev/comments/1bjsw3d/best_search_tool_in_langchain/) , 2024-03-23-0909
```
Hi all, was going through the search tools available via langchain. Just wanted to check which is the best one to use
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-23-0909
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-23-0909
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

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-23-0909
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-23-0909
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
