 
all -  [ Free AI Backlink Outreach Message Generator ](https://www.reddit.com/r/nextjs/comments/1aju5ff/free_ai_backlink_outreach_message_generator/) , 2024-02-06-0909
```
Had a lot of fun building this with Next.js and the following stack. 🤓

🔗 [https://www.backlinkgpt.com/free-seo-tools/ba
cklink-outreach-message-generator](https://www.backlinkgpt.com/free-seo-tools/backlink-outreach-message-generator)

✅ La
ngchain Expression Language for Prompting and Parsing  
✅ React Hook-Forms for Form State Management

✅ Vercel AI SDK fo
r seamless streaming
```
---

     
 
all -  [ AI for Finance/Investment Research ](https://www.reddit.com/r/LangChain/comments/1ajmnlo/ai_for_financeinvestment_research/) , 2024-02-06-0909
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

     
 
all -  [ Chat with arXiv papers using function calling ](https://www.reddit.com/r/LangChain/comments/1ajit2n/chat_with_arxiv_papers_using_function_calling/) , 2024-02-06-0909
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

     
 
all -  [ Creating LLMs Apps on Chemical CSV Data ](https://www.reddit.com/r/cheminformatics/comments/1ajif6w/creating_llms_apps_on_chemical_csv_data/) , 2024-02-06-0909
```
[https://medium.com/@sharifsuliman/converting-your-knowledge-graph-csv-into-a-large-language-model-with-langchain-and-ch
ainlit-475c8c1b8073](https://medium.com/@sharifsuliman/converting-your-knowledge-graph-csv-into-a-large-language-model-w
ith-langchain-and-chainlit-475c8c1b8073)

Still working on making this CSV agent better but I figured in the future thes
e CSV agents on domain specific chemical data will be useful. 
```
---

     
 
all -  [ 🔥 [FOR HIRE]. AI Chatbot | ChatGPT | Langchain | VectorDB | Huggingface | Prompt Engineering | NLP ](https://www.reddit.com/r/ForHire_AI/comments/1ajflae/for_hire_ai_chatbot_chatgpt_langchain_vectordb/) , 2024-02-06-0909
```
[https://remoteai.io/talent/profile/@eastonjim](https://remoteai.io/talent/profile/@eastonjim)
```
---

     
 
all -  [ Looking to the future of vector database and RAG ](https://medium.com/@infiniflowai/looking-to-the-future-of-vector-databases-be86f218dc94) , 2024-02-06-0909
```

```
---

     
 
all -  [ is there an alternative for system, user and assistant messages in langchain? ](https://www.reddit.com/r/Langchaindev/comments/1ajaj12/is_there_an_alternative_for_system_user_and/) , 2024-02-06-0909
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

     
 
all -  [ Resume buildup ](https://www.reddit.com/r/resumes/comments/1aja0fb/resume_buildup/) , 2024-02-06-0909
```
Hi, i am an undergrad cs major, i needed help with my resume, I'd love your input on this, how can i rewrite the content
 in my resume for a better perspective of being a ai/ml engineer or a data analyst/data scientist?

 

[need help with r
esume](https://preview.redd.it/q6ej5pjinpgc1.png?width=869&format=png&auto=webp&s=4061b2a9c81ad8a84327b03232d9c9016bfa45
42)
```
---

     
 
all -  [ How to request translation of a very long document to LangChain? ](https://www.reddit.com/r/LangChain/comments/1aj7q8x/how_to_request_translation_of_a_very_long/) , 2024-02-06-0909
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

     
 
all -  [ My raw story of using Langchain to build my DIY chatbot ](https://www.reddit.com/r/LangChain/comments/1aj5mnq/my_raw_story_of_using_langchain_to_build_my_diy/) , 2024-02-06-0909
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

     
 
all -  [ Ollama vision using Llava running locally on my macbook. Inference speed is 🔥 ](https://www.reddit.com/r/LangChain/comments/1aivgaa/ollama_vision_using_llava_running_locally_on_my/) , 2024-02-06-0909
```
https://reddit.com/link/1aivgaa/video/xwtl03439mgc1/player

[Code if interested.](https://github.com/phidatahq/phidata/b
lob/main/cookbook/ollama/image.py)
```
---

     
 
all -  [ How to use AzureOpenAI Embeddings with ChromDB or FAISS? ](https://www.reddit.com/r/LangChain/comments/1airll4/how_to_use_azureopenai_embeddings_with_chromdb_or/) , 2024-02-06-0909
```
Hi guys,
           I tried langchain-openai's Azure Embedding abstraction, but am getting multiple errors when I try it
 with Chroma or FAISS. May I know a solution for this?
```
---

     
 
all -  [ Is function calling supported with RAG? ](https://www.reddit.com/r/LangChain/comments/1aio67k/is_function_calling_supported_with_rag/) , 2024-02-06-0909
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

     
 
all -  [ Why are basic things not documented correctly, never seem to work? ](https://www.reddit.com/r/LangChain/comments/1aimin7/why_are_basic_things_not_documented_correctly/) , 2024-02-06-0909
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

     
 
all -  [ Best AI Research agent? ](https://www.reddit.com/r/OpenAI/comments/1aijjj9/best_ai_research_agent/) , 2024-02-06-0909
```
Looking for a Research tool that is able to complete in depth research tasks through browsing online. Copilot/bing aren’
t thorough enough, and remember coming across a langchain based one a while back but can’t remember the name of the proj
ect.
```
---

     
 
all -  [ Creating vector embedding from multiple pdf ](https://www.reddit.com/r/LangChain/comments/1aiiyd6/creating_vector_embedding_from_multiple_pdf/) , 2024-02-06-0909
```
Can anyone suggest methods for creating vector embedding d from multiple PDFs using Langchain embedding and retrievers.K
ind of stuff used in applications like Chatpdf
```
---

     
 
all -  [ My debut book on Generative AI : LangChain in your Pocket is out ! ](https://www.reddit.com/r/nonfiction/comments/1aiggfh/my_debut_book_on_generative_ai_langchain_in_your/) , 2024-02-06-0909
```
I am thrilled to announce the launch of my debut technical book, “**LangChain in your Pocket:** ***Beginner’s Guide to B
uilding Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback formats.

In
 this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework designed for harne
ssing Generative AI. Through practical examples and hands-on exercises, you’ll gain the skills necessary to develop a di
verse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet-enabled GPT, Multi-Docu
ment RAG and more.

# Key Features:

* Step-by-step code explanations with expected outputs for each solution.
* No prer
equisites: If you know Python, you’re ready to dive in.
* Practical, hands-on guide with minimal mathematical explanatio
ns.

*I would greatly appreciate if you can check out the book and share your thoughts through reviews and ratings:* [ht
tps://www.amazon.in/dp/B0CTHQHT25](https://www.amazon.in/dp/B0CTHQHT25)

# About me:

I'm a Senior Data Scientist at DBS
 Bank with about 5 years of experience in Data Science & AI. Additionally, I manage 'Data Science in your Pocket', a [Me
dium Publication](https://medium.com/@mehulgupta_7991) & [YouTube channel](https://www.youtube.com/@datascienceinyourpoc
ket/videos) with \~600 Data Science & AI tutorials and a cumulative million views till date. To know more, you can check
 [here](https://www.linkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ Open to Critique: 3rd Year Student Seeks to Polish Resume & Explore Projects ](https://www.reddit.com/r/resumes/comments/1aigf9g/open_to_critique_3rd_year_student_seeks_to_polish/) , 2024-02-06-0909
```
 Greetings, fellow professionals! As a 3rd year student aiming to land my dream internship/job, I'm humbly seeking valua
ble insights on my resume. Any areas for improvement or suggestions for impactful projects to strengthen my candidacy wo
uld be immensely helpful. I'm eager to learn and grow! 

&#x200B;

https://preview.redd.it/lom1gaxe8igc1.png?width=990&f
ormat=png&auto=webp&s=c8817e41671838c2d335ec8a55f52d242e58c358
```
---

     
 
all -  [ My debut book : LangChain in your Pocket is out !! ](https://www.reddit.com/r/LlamaIndex/comments/1aig705/my_debut_book_langchain_in_your_pocket_is_out/) , 2024-02-06-0909
```
&#x200B;

https://preview.redd.it/mrie73q16igc1.png?width=934&format=png&auto=webp&s=4bfcf2b42fd3e2ca781c5e2d0ed1c919105
f12d2

I am thrilled to announce the launch of my debut technical book, “**LangChain in your Pocket:** ***Beginner’s Gui
de to Building Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback forma
ts.

In this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework designed fo
r harnessing Generative AI. Through practical examples and hands-on exercises, you’ll gain the skills necessary to devel
op a diverse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet-enabled GPT, Mul
ti-Document RAG and more.

# Key Features:

* Step-by-step code explanations with expected outputs for each solution.
* 
No prerequisites: If you know Python, you’re ready to dive in.
* Practical, hands-on guide with minimal mathematical exp
lanations.

*I would greatly appreciate if you can check out the book and share your thoughts through reviews and rating
s:* [https://www.amazon.in/dp/B0CTHQHT25](https://www.amazon.in/dp/B0CTHQHT25)

# About me:

I'm a Senior Data Scientist
 at DBS Bank with about 5 years of experience in Data Science & AI. Additionally, I manage 'Data Science in your Pocket'
, a [Medium Publication](https://medium.com/@mehulgupta_7991) & [YouTube channel](https://www.youtube.com/@datasciencein
yourpocket/videos) with \~600 Data Science & AI tutorials and a cumulative million views till date. To know more, you ca
n check [here](https://www.linkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ My debut book : LangChain in your Pocket is out !! ](https://www.reddit.com/r/generativeAI/comments/1aifydl/my_debut_book_langchain_in_your_pocket_is_out/) , 2024-02-06-0909
```
&#x200B;

I am thrilled to announce the launch of my debut technical book, “**LangChain in your Pocket:** ***Beginner’s 
Guide to Building Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback fo
rmats.

https://preview.redd.it/rm6tygyi3igc1.png?width=934&format=png&auto=webp&s=868abde885275550f734a24da265f8deef12a
276

In this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework designed fo
r harnessing Generative AI. Through practical examples and hands-on exercises, you’ll gain the skills necessary to devel
op a diverse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet-enabled GPT, Mul
ti-Document RAG and more.

# Key Features:

* Step-by-step code explanations with expected outputs for each solution.
* 
No prerequisites: If you know Python, you’re ready to dive in.
* Practical, hands-on guide with minimal mathematical exp
lanations.

*I would greatly appreciate if you can check out the book and share your thoughts through reviews and rating
s:* [https://www.amazon.in/dp/B0CTHQHT25](https://www.amazon.in/dp/B0CTHQHT25)

or at GumRoad : [https://mehulgupta.gumr
oad.com/l/hmayz](https://mehulgupta.gumroad.com/l/hmayz)

# About me:

I'm a Senior Data Scientist at DBS Bank with abou
t 5 years of experience in Data Science & AI. Additionally, I manage 'Data Science in your Pocket', a [Medium Publicatio
n](https://medium.com/@mehulgupta_7991) & [YouTube channel](https://www.youtube.com/@datascienceinyourpocket/videos) wit
h \~600 Data Science & AI tutorials and a cumulative million views till date. To know more, you can check [here](https:/
/www.linkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ My debut book : LangChain in your Pocket is out !! ](https://www.reddit.com/r/Langchaindev/comments/1aifqic/my_debut_book_langchain_in_your_pocket_is_out/) , 2024-02-06-0909
```
&#x200B;

https://preview.redd.it/aes3wij91igc1.png?width=786&format=png&auto=webp&s=d10d6d32c2f720991265d0a2b3b874989d5
2afb4

I am thrilled to announce the launch of my debut technical book, “**LangChain in your Pocket:** ***Beginner’s Gui
de to Building Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback forma
ts.

In this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework designed fo
r harnessing Generative AI. Through practical examples and hands-on exercises, you’ll gain the skills necessary to devel
op a diverse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet-enabled GPT, Mul
ti-Document RAG and more.

# Key Features:

* Step-by-step code explanations with expected outputs for each solution.
* 
No prerequisites: If you know Python, you’re ready to dive in.
* Practical, hands-on guide with minimal mathematical exp
lanations.

*I would greatly appreciate if you can check out the book and share your thoughts through reviews and rating
s:* [https://www.amazon.in/dp/B0CTHQHT25](https://www.amazon.in/dp/B0CTHQHT25)

# About me:

I'm a Senior Data Scientist
 at DBS Bank with about 5 years of experience in Data Science & AI. Additionally, I manage '***Data Science in your Pock
et***', a [Medium Publication](https://medium.com/@mehulgupta_7991) & [YouTube channel](https://www.youtube.com/@datasci
enceinyourpocket/videos) with \~600 Data Science & AI tutorials and a cumulative million views till date. To know more, 
you can check [here](https://www.linkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ My debut book: LangChain in your Pocket is out ! ](https://www.reddit.com/r/LangChain/comments/1aifn1l/my_debut_book_langchain_in_your_pocket_is_out/) , 2024-02-06-0909
```
I am thrilled to announce the launch of my debut technical book, “**LangChain in your Pocket:** ***Beginner’s Guide to B
uilding Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback formats.

In
 this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework designed for harne
ssing Generative AI. Through practical examples and hands-on exercises, you’ll gain the skills necessary to develop a di
verse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet-enabled GPT, Multi-Docu
ment RAG and more.

# Key Features:

* Step-by-step code explanations with expected outputs for each solution.
* No prer
equisites: If you know Python, you’re ready to dive in.
* Practical, hands-on guide with minimal mathematical explanatio
ns.

*I would greatly appreciate if you can check out the book and share your thoughts through reviews and ratings:* [ht
tps://www.amazon.in/dp/B0CTHQHT25](https://www.amazon.in/dp/B0CTHQHT25)

Or at GumRoad : [https://mehulgupta.gumroad.com
/l/hmayz](https://mehulgupta.gumroad.com/l/hmayz)

# About me:

I'm a Senior Data Scientist at DBS Bank with about 5 yea
rs of experience in Data Science & AI. Additionally, I manage 'Data Science in your Pocket', a [Medium Publication](http
s://medium.com/@mehulgupta_7991) & [YouTube channel](https://www.youtube.com/@datascienceinyourpocket/videos) with \~600
 Data Science & AI tutorials and a cumulative million views till date. To know more, you can check [here](https://www.li
nkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ Looking for Help with Retrieval Issues in Information Retrieval Application(LangChain, OpenAI, and F ](https://www.reddit.com/r/LangChain/comments/1aiaidl/looking_for_help_with_retrieval_issues_in/) , 2024-02-06-0909
```
Hello Everyone,

I am currently developing an information retrieval application designed to work with HTML pages, rangin
g in length from 30 to 200 pages. The application utilizes LangChain, OpenAI, and FAISS for its core functionalities. A 
significant part of the process involves chunking HTML pages, many of which contain numerous tables. My method involves 
extracting tables from the HTML pages, identifying them by their top titles for indexing and retrieval purposes.

Howeve
r, I have encountered two main issues during retrieval:

* Long Query Handling: When the query is slightly longer, the r
etrieval system does not return the correct answer. It seems to struggle with maintaining accuracy as the query length i
ncreases.
* Variance in Wording: The system fails to correctly retrieve chunks when there is a discrepancy between the w
ording in the query and the chunks. For example, if the query uses 'six' but the chunk contains '6', the system does not
 recognize them as a match.

These challenges are hindering the application's ability to accurately retrieve information
, especially when dealing with nuanced or detailed queries.

I am reaching out to this community for advice or strategie
s on how to address these issues. Specifically, I am interested in approaches that could improve the handling of long qu
eries and the recognition of synonymous terms or different word forms (like numerals versus written numbers) during the 
retrieval process.

Any suggestions or insights on how to refine the retrieval accuracy of this application would be gre
atly appreciated.

Thank you in advance for your help!
```
---

     
 
all -  [ Embeddings from Vector Stores ](https://www.reddit.com/r/LangChain/comments/1ai3k14/embeddings_from_vector_stores/) , 2024-02-06-0909
```
Currently I'm using Chroma as a vector db for a langchain agent. I'm looking to do some metadata extraction/clustering w
ith the core embeddings. Is this something that can be easily accessed for each document - seems the db queries will onl
y return Document/text content. Is there clean way to have access to all embeddings and have them in a numpy array for e
xample? 

&#x200B;

Appreciate any help.. of course its not too difficult to just re-do the embeddings and access them d
irectly but I'm wondering if there is a way to avoid paying 2x

&#x200B;

Thanks!
```
---

     
 
all -  [ Need some reviews in my resume. ](https://www.reddit.com/r/resumes/comments/1ai1uiu/need_some_reviews_in_my_resume/) , 2024-02-06-0909
```
&#x200B;

https://preview.redd.it/psqp00y0segc1.png?width=660&format=png&auto=webp&s=0822dd684503f53a9f8de4ef0de35cbeb39
c65e4

https://preview.redd.it/9agog1y0segc1.png?width=660&format=png&auto=webp&s=21432efabdc8d73150edba2cbbef01fede6a19
02
```
---

     
 
all -  [ Extracting Answer Source Chunks from GPT Responses in Langchain ](https://www.reddit.com/r/LLMDevs/comments/1ahs82h/extracting_answer_source_chunks_from_gpt/) , 2024-02-06-0909
```
Hey everyone,

I've been working on a project where I extract information from a large PDF document. I've completed the 
initial steps, including reading the PDF, splitting it into chunks, converting them to embeddings, and storing them in a
 vector database.

For the next step, I perform a similarity check with a limit of 28. Each chunk has a size of 350, wit
h an overlap of 80. After that, I send these chunks to GPT with a specific question. GPT provides answers, but I'm strug
gling to determine from which chunk the answer originated.

Is there a way to identify the specific chunk(s) that GPT us
ed to generate the answer? Alternatively, is there a solution to get an array of chunks that may contain the answer out 
of the 28 available?

Any insights or suggestions on how to achieve this would be greatly appreciated!

Thanks in advanc
e!
```
---

     
 
all -  [ Noob-friendly Recap ](https://www.reddit.com/r/LocalLLaMA/comments/1ahr6ds/noobfriendly_recap/) , 2024-02-06-0909
```
I recently started getting in LLM-powered applications by myself and using online resources. What I discovered is that L
LMs have become so mainstream that there are so many platform, frameworks, and model to choose from. And usually I don't
 even understand what are the key differences between one another

This is what I understood, please enlighten me and wh
oever comes here through a Google search

- LLMs are huge models and if I want to run them locally I should use a quanti
zed version: what are the best practices? What are the requirements? I'm currently using windows but I'm having so much 
troubles 

- Faster inference: what are the differences between vLLM, llamacpp, and ollama? The second one is the only o
ne that *should* work on windows. Should I always use these frameworks? Are they used only to load the quantized model? 


- Deployment. What are the best platform / best practices regarding the deployment phase? I guess a logic choice would
 be having the LLM available via API

- Fine-tuning. There are multiple ways to fine-tune a LLM. LORA seems a good trade
-off. Should I use a particular framework to apply it? Moreover, let's say I fine-tune my model over different use-cases
. In production, how do I swap the weights for these different models efficiently? 

- Orchestrator. LangChain should be
 the most popular one, but is it the one to go for? I see they are working on a huge refactor
```
---

     
 
all -  [ SQL Agent + Vector Store RAG ](https://www.reddit.com/r/LangChain/comments/1ahpvmm/sql_agent_vector_store_rag/) , 2024-02-06-0909
```
Hello! First timer here. 

I'm learning the ropes with LangChain, and have successfully made

1. A chat which integrates
 with a Postgres/Chroma vector store to augment responses
2. A chat which uses a SQL Agent with BigQuery to introspect a
nd query a dataset

What I am struggling to figure out now, is how do I combine them? I want to have the vector store au
gment the prompts used by the SQL agent. I think it will yield me better results if I can layer in project documentation
 and examples. However, the API documentation doesn't make it clear (At least to me) how to effectively accomplish this.
 

Hope somebody can help!
```
---

     
 
all -  [ Manager Wants to switch from LangChain to Copilot Studio for a Client Product - Thoughts? ](https://www.reddit.com/r/Langchaindev/comments/1ahfbzb/manager_wants_to_switch_from_langchain_to_copilot/) , 2024-02-06-0909
```
 Hey everyone!

I'm having a bit of trouble and could really use your wisdom. My company is eager to add AI to their pro
ducts and daily operations.

We have this internal initiative where people from various departments come together to inn
ovate or improve something, to add more value to the organization. My group has the task to develop an AI Chatbot, to as
sume some of the functions typically performed by an analyst, in a specific type of service, where it interacts with the
 customer, collects information for a specific process and uses this information to parameterize the company's system, f
or that specific customer.

Here's the problem: we have about 160 person-hours per month, split between three of us, ove
r the next three months, to go from having zero expertise in creating AI-powered apps to delivering a functional AI-powe
red chatbot MVP.

It is clear that they do not know what they are doing about this matter. They gave us ChatGPT licenses
 after we requested OpenAI API credits. So they asked us to create a detailed AI spending plan, so they can evaluate (an
d yes, we are a technology company with over 1k employees).

Now they want us to move our development efforts to Copilot
 Studio, abandoning our current development with Python and Langchain. From what I gather, this may not be the wisest co
urse of action, especially considering the intricate context management our project requires (different rules for answer
s, complex questions) and the potential lock-in with the Microsoft ecosystem (also, for what I could check, the client n
eeds to pay for copilot studio as well). They don't even have paid Copilot Studio yet (don't know if they will ever do).


The challenge is that we don't really know much about AI development (we're trying to study it in the meantime), so it
's hard to argue with them.

Can anyone here help us understand if it's true that Copilot Studio could be a better solut
ion? Yes? No?

I would deeply appreciate any information or advice you could share so I can craft a well-informed respon
se.

Thank you very much in advance for your contribution and time!
```
---

     
 
all -  [ Manager Wants to switch from LangChain to Copilot Studio for a Client Product - Thoughts? ](https://www.reddit.com/r/LangChain/comments/1ahfbmm/manager_wants_to_switch_from_langchain_to_copilot/) , 2024-02-06-0909
```
 

Hey everyone!

I'm having a bit of trouble and could really use your wisdom. My company is eager to add AI to their p
roducts and daily operations.

We have this internal initiative where people from various departments come together to i
nnovate or improve something, to add more value to the organization. My group has the task to develop an AI Chatbot, to 
assume some of the functions typically performed by an analyst, in a specific type of service, where it interacts with t
he customer, collects information for a specific process and uses this information to parameterize the company's system,
 for that specific customer.

Here's the problem: we have about 160 person-hours per month, split between three of us, o
ver the next three months, to go from having zero expertise in creating AI-powered apps to delivering a functional AI-po
wered chatbot MVP.

It is clear that they do not know what they are doing about this matter. They gave us ChatGPT licens
es after we requested OpenAI API credits. So they asked us to create a detailed AI spending plan, so they can evaluate (
and yes, we are a technology company with over 1k employees).

Now they want us to move our development efforts to Copil
ot Studio, abandoning our current development with Python and Langchain. From what I gather, this may not be the wisest 
course of action, especially considering the intricate context management our project requires (different rules for answ
ers, complex questions) and the potential lock-in with the Microsoft ecosystem (also, for what I could check, the client
 needs to pay for copilot studio as well). They don't even have paid Copilot Studio yet (don't know if they will ever do
).

The challenge is that we don't really know much about AI development (we're trying to study it in the meantime), so 
it's hard to argue with them.

Can anyone here help us understand if it's true that Copilot Studio could be a better sol
ution? Yes? No?

I would deeply appreciate any information or advice you could share so I can craft a well-informed resp
onse.

Thank you very much in advance for your contribution and time!
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-06-0909
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-06-0909
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-06-0909
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-06-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-06-0909
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-02-06-0909
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-06-0909
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-06-0909
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-06-0909
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-02-06-0909
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

     
