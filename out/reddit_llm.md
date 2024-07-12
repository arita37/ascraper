 
all -  [ First Chatbot Design ](https://www.reddit.com/r/LearningAIChatbot/comments/1e12qhm/first_chatbot_design/) , 2024-07-12-0911
```
As the title suggets, I am attempting to make my first chatbot ever for a school project. I have done some research and 
am thinking of using LangChain with a Jupyter notebook. I want this chatbot to be able to run outside my environment in 
VSCode as well, whether that be an application or website. I also need to design a UI in Figma and convert this into HTM
L/CSS to be the face of the chatbot. Any resource recommendations, tutorials, or advice is greatly appreciated. Or if yo
u think there is a better way of going about this please let me know below.
```
---

     
 
all -  [ What embedding model is everyone using? ](https://www.reddit.com/r/LangChain/comments/1e11luo/what_embedding_model_is_everyone_using/) , 2024-07-12-0911
```
I was wondering what embedding model people have had success with for their vector store? I might be wrong but on langch
ain it simply implies everyone uses the openai one. Are there options for this?
```
---

     
 
all -  [ Hallucinations: Why You Should Care as an AI Developer ](https://www.reddit.com/r/pythia/comments/1e0z4jy/hallucinations_why_you_should_care_as_an_ai/) , 2024-07-12-0911
```
https://preview.redd.it/64btbssbcybd1.png?width=2048&format=png&auto=webp&s=050dff23beaa0e475cab8917ee5dd14e7dfb9ae9

*U
nderstand why hallucination detection is important for reliable LLMs. Learn the characteristics of a good hallucination 
detector.*

From speech recognition to text generation, generative AI and LLMs have become involved in various applicati
ons and scenarios. The generative AI industry is projected to become a $1.3 Trillion market by 2032, with a compound ann
ual growth rate (CAGR) of 42%. Generative AI products are predicted to add about $289 billion of new revenue to the soft
ware industry.

These projections for expansion reflect the presence of LLMs in all aspects of life, including healthcar
e. Their pervasive presence emphasizes the need for reliable AI to protect end-users from misleading decisions. However,
 LLMs often produce hallucinated outputs, resulting in penalties, lost trust in AI, reputation damage, and human life.


Let’s explore the need for AI reliability and how to achieve reliable AI solutions.

# Why Does AI Reliability Matter?


Though LLMs have become increasingly intelligent, they still tend to hallucinate. AI hallucinations are AI-generated out
puts that seem confident but are inaccurate and misleading.

Industry-leading LLMs like ChatGPT have a 31% hallucination
 rate when used for scientific purposes. These hallucinations have significant costs, including:

* **Healthcare costs:*
* Misdiagnoses can lead to deaths and serious disabilities. It can also cost healthcare providers significant losses in 
penalties and reputation damage.
* **Litigation costs:** AI hallucinations can cause legal penalties in cases such as pr
ivacy violations or sensitive remarks. Legal errors can average $250,000 in settlements.
* **Financial sector:** When LL
Ms are used for research purposes, hallucinations can guide researchers toward poor decision-making. Poor investment dec
isions can lead to millions in losses.
* **Operational downtime:** Erroneous or misleading information can lead to disru
ptions or failures in operational processes. AI-related downtime can cost $10,000 per hour.
* **Brand damage:** Misleadi
ng outputs can damage a company's reputation and result in client hostility.

Governments and NGOs are becoming involved
 in achieving reliable AI. For example, the EU AI Act is a European regulation on AI protection that covers various aspe
cts of AI development and deployment to ensure safe AI.

Complying with these regulations requires the development of re
liableLLMs that produce reliable outputs.

# Existing AI Reliability Solutions and Their Challenges

Existing AI reliabi
lity solutions include bias detection, explainable AI (XAI) methods, adversarial techniques, etc. These solutions detect
 hallucinations and ensure reliable AI to some extent, but their limitations keep them from achieving safe and accurate 
AI.

They lack continuous monitoring support, transparency, and claim verification, which gives rise to their limitation
s, including:

1. **Limited scalability:** Current methods depend on the availability of high-quality training data, whi
ch prevents them from offering scalable AI reliability solutions.
2. **Lack of explainability:** Current methods fail to
 explain why a particular LLM response is flagged as a hallucination, making it difficult for developers to fix factual 
issues.
3. **Low accuracy:** Existing solutions are not as accurate, making them ineffective for mission-critical applic
ations like life sciences.

# 10 Things to Look for in an AI Reliability Solution

AI reliability solutions must meet ce
rtain criteria to effectively detect hallucinations and offer transparency in their decisions. Here are the ten key thin
gs to look for in an AI reliability solution:

# 1. LLM Usage Scenarios

An AI reliability solution should accommodate d
ifferent LLM usage scenarios. The three LLM usage scenarios include:

1. **Zero context:** The AI reliability solution s
hould be able to directly compare references it finds with the LLM’s responses to assess accuracy.
2. **Noisy context:**
 When a question includes some context but is either noisy or incomplete, the AI reliability solution must be capable of
 consulting authoritative data before the LLM generates a response.
3. **Accurate context:** When the context is complet
e and reliable, it can use the references to provide a comprehensive summary or information in response.

[LLM usage sce
narios](https://preview.redd.it/iws0jnex8vbd1.png?width=2880&format=png&auto=webp&s=1b7e2fd50a37a4e82735bdd06619f35dccbb
4066)

These scenarios/ contexts guide the reliability solution in finding references and verifying LLM claims.

# 2. Cl
aim Extraction

The hallucination detection solutions should be able to decompose LLM responses into knowledge triplets.
 Unlike traditional methods, knowledge triplets extract granular details from content and highlight the relationship amo
ng words within a sentence.

Knowledge triplets represent **<subject, predicate, object>**, highlighting the connection 
between the three and creating a better contextual understanding. For example:

[Knowledge Triplet Example](https://prev
iew.redd.it/mvzxmp319vbd1.png?width=2352&format=png&auto=webp&s=5d357b26bf3f7170136c18755ba5300c02a17865)

# 3. Claim Ca
tegorization

After the claim extraction from LLM responses and references/ knowledge base, the hallucination detector m
ust be able to categorize them based on their hallucination levels. Claim categorization guides developers toward the im
provement of LLM by offering insights into its capabilities. The four categories for claim categorization include:

1. *
*Entailment:** Claims in both response and references, indicating accurate outputs.
2. **Contradiction:** Claims present
 in LLM responses but disregarded by references.
3. **Missing facts:** Claims present in references but absent in LLM re
sponses, representing gaps in LLM responses.
4. **Neutral:** Claims present in LLM response but are neither contradicted
 nor confirmed by the references.

[Claim categorization based on hallucination level](https://preview.redd.it/n57d4dh39
vbd1.png?width=1798&format=png&auto=webp&s=51b4161dc45f7dc7c17bedb82d1587eafe0d5df2)

# 4. Accuracy Metrics

An AI monit
oring tool must be able to calculate the overall accuracy of LLM based on claim categorization. The accuracy metric repr
esents the proportion of factually correct claims in the LLM response. Mathematically, accuracy is measured as:

https:/
/preview.redd.it/9dkux1979vbd1.png?width=2780&format=png&auto=webp&s=41a63d1930d462cf8497831112191e2e6df0e628

Where:

*
 Entailment: Claims flagged as Entailment
* Contradiction: Claims flagged as Contradiction
* Reliability: Calculated usi
ng external data (i.e., knowledge graphs or RAGs)

# 5. Task Specific Metrics

There are two types of task-specific metr
ics, i.e., Core metrics specialized to the task and additional metrics for measuring the quality of the responses with r
espect to the task.

Specializing core metrics rely on the type of AI checker being used:

1. LLM-based checkers can enh
ance their accuracy by considering additional context provided in the form of a question when generating claim classific
ation.
2. NLI-based checkers utilize a QA (Question Answering) evaluator model to verify the alignment of a response wit
h a question.
3. Knowledge graph-based checkers rely on Knowledge Graphs (KGs) to verify structured information about en
tities, relationships, and concepts.

https://preview.redd.it/7kjj902d9vbd1.png?width=1436&format=png&auto=webp&s=ff9cd0
af3478d8f36b2aeaaa8a675934a68d668d

# 6. Systematic Error

The AI hallucination detector must be able to identify system
atic errors. Systematic errors are recurring inconsistencies in LLM responses. Identifying them involves:

1. Comparing 
the reference information to itself. This means using the same reference as the knowledge base and the standard for comp
arison.
2. Generating core metrics to assess LLM performance. Metrics highlight the system's ability to classify claims 
as true, false, or neutral correctly.
3. Defining a systematic error checker, which is the harmonic mean of the compleme
nt of Entailment and Contradiction.

The ideal result is 100% Entailment, 0% Contradiction, and 0% Neutral claims. Mathe
matically, a systematic error checker is represented as:

https://preview.redd.it/871dqk9j9vbd1.png?width=1962&format=pn
g&auto=webp&s=c3453f014e83b6c7ff0439b15199b2ebf3ea6ead

# 7. Robust Set of Validators

An AI reliability solution should
 use a robust set of input/ output validators to protect sensitive information from leakage, misleading outputs, and tox
ic outputs. These validators validate LLM inputs and responses to ensure they meet quality standards and are accurate. T
he validators also protect against cyber attacks such as malicious input or prompt injections.

[Example Input\/Output V
alidators](https://preview.redd.it/hdgv807m9vbd1.png?width=2058&format=png&auto=webp&s=fd786a3c48737ac62e6e943598e6bee12
79ca1e0)

# 8. Reporting

A good hallucination detection solution provides reports highlighting hallucination trends ove
r time. These reports give insight into model improvement with time and systematic errors. Updated reports allow targete
d adjustments to enhance the LLM’s reliability and effectiveness.

Moreover, detailed analysis of these trends helps und
erstand the underlying causes of hallucinations, resulting in better training and fine-tuning.

# 9. Continuous Alerting
 and Monitoring

Continuous monitoring and alerting are crucial for real-time hallucination detection and on-time correc
tion. Continuous monitoring keeps track of LLM outputs against each user query, highlighting a model’s strengths and wea
knesses. Alerting systems send email/SMS notifications about LLM performance, which helps address bias in model outputs 
before it perpetuates bias in the public.

[Real-time Monitoring and Alert Rules Example](https://preview.redd.it/iikmvy
ks9vbd1.png?width=2852&format=png&auto=webp&s=e369d8975793f59e21d955581e6d84b136b0c8e8)

# 10. LangChain Integration

La
ngChain is a Natural Language Processing (NLP) framework that provides pre-trained models and tools to customize and imp
rove model performance. LangChain has an active community, and LLM developers use it to develop robust LLMs because of i
ts flexibility and support. The ability of an AI reliability solution to integrate with LangChain makes it a handy choic
e for hallucination detection, as most of the LLM workflows are built using LangChain.

[LangChain Workflow with AI Reli
ability Solution](https://preview.redd.it/lyeikorw9vbd1.png?width=2684&format=png&auto=webp&s=53db6572ce38efa43f837b498c
5d5091cc47e0d8)

# Wisecube’s Pythia: a Reliable Hallucination Detection Tool

Wisecube’s [Pythia](https://askpythia.ai/
blog/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinations), an AI reliability solution, boasts the ten crucia
l characteristics of AI hallucination detectors. These characteristics set Pythia apart from other solutions by offering
 the following benefits:

* **Enhanced reliability:** Reduces the risk of AI errors using built-in hallucination detecti
on and validators
* **Trustworthy outputs:** Builds trust in AI systems through continuously monitoring accurate and rel
iable outputs.
* **Easy integration:** Integrates into existing LangChain workflows, empowering developers to develop tr
ustworthy AI systems.
* **Customizable detection:** Pythia can be configured to suit specific use cases, resulting in im
proved flexibility and increased accuracy.

**To learn more about the impact of hallucinations and the characteristics o
f an effective AI reliability solution,** [**watch the webinar here.** ](https://www.youtube.com/watch?v=PXFXKMJO9jo&t=2
0s)

*The article was originally published on* [Pythia's website.](https://askpythia.ai/blog/hallucinations-why-you-shou
ld-care-as-an-ai-developer)
```
---

     
 
all -  [ An independent, 'self-aware' LLM Agent under 100 lines of Python ](https://www.reddit.com/r/Python/comments/1e0ypgo/an_independent_selfaware_llm_agent_under_100/) , 2024-07-12-0911
```
**What My Project Does:** 

In short, Uffe is...

* a **sub-100 lines** LLM agent.
* fitted with **long-term memory**.
*
 **self-a**ware in the sense that all the code in Uffe is injected into the system prompt.
* going to **use your termina
l**. Whatever you have access to, uffe has access to.
* a real doer, he will probably not ask for permission, he just ge
ts things done.
* completely independent. You can run uffe on vanilla python.

Uffe may not be the most powerful agent o
ut there but it is simple enough that anyone can understand how it works. Because the code is so small it is no big deal
 including it in the system prompt. Does this improve performance? Probably not with current LLMs, but who knows what ha
ppens when GPT-6 arrives. In theory, Uffe can modify its own code as he sees fit.

**Target Audience**

The purpose of t
his project is to demonstrate that it is possible to create a somewhat useful agent without using huge frameworks such a
s Langchain or Autogen. In fact, Uffe doesn't even depend on openai python library despite using GPT-4 as LLM.

This is 
not a code golf project, the goal is to always keep it below 100 lines of python code but not to a cost of readability. 
As a principle, I'm aiming to keep it 100% independent from 3rd party libraries. Anyone that knows python should be able
 to follow and understand the code.

**Comparison**

There are some other pretty simple agents out there, such as [babya
gi](https://github.com/yoheinakajima/babyagi/blob/main/babyagi.py), however, it has over 600 lines of python code and 7 
dependencies. It is of course possible to create an even more compact agent using a framework, but again, the purpose he
re is simplicity and transparency. These frameworks, especially Langchain is immensely opaque due to its obsession with 
abstraction layers. 

As far as I know there are no other Agent with the same properties as Uffe. 

**Show me**

I have 
a short demo video on Github: [https://github.com/visendi-labs/uffe](https://github.com/visendi-labs/uffe)

**What is it
 useful for?**

It can handle smaller tasks that don't require too big context.

**Now what?**

There is a lot of room f
or improvement, especially regarding the long term memory. Ideas and PR:s are more than welcome.
```
---

     
 
all -  [ AI agents. Are no-code platforms better? ](https://www.reddit.com/r/LangChain/comments/1e0xdgw/ai_agents_are_nocode_platforms_better/) , 2024-07-12-0911
```
On one hand I really want to build from the ground up and see what happens every step of the way, on the other hand, I’m
 trying to embrace abstraction, l would just go for a no-code drag and drop if the final product works fine. I have been
 looking into [~SmythOS~](https://smythos.com/), a no code platform for creating AI agents and I think I am sold. But I 
still can’t shake the feeling that it’s too good to be true. What do you think? Would you go for a no code option or wou
ld you rather just do everything yourself?


```
---

     
 
all -  [ A List of free Courses from Coursera for Computer Science Students. ](https://www.reddit.com/r/coursera/comments/1e0wjdf/a_list_of_free_courses_from_coursera_for_computer/) , 2024-07-12-0911
```
You might check out some free courses courses on Programming, Data Structure, Algorithms, Computer Architecture, Embedde
d Systems and IoT. [Read More](https://medium.com/p/f10816891ad1).  [Subscribe for more Free Stuffs](https://studyandexp
lore.medium.com/subscribe).

1. Introduction to Machine Learning By Duke University
2. Data Science Math Skills By Duke 
University
3. Learn to Program: The Fundamentals(Python)
4. Building Systems with the ChatGPT API by Andrew Ng
5. Learn 
Kali Linux
6. Introduction to Statistics By Stanford University
7. ChatGPT Prompt Engineering for Developers
8. LangChai
n Chat with Your Data By [DeepLearning.AI](http://deeplearning.ai/)
9. Introduction to Generative AI
10. Preparation for
 Job Interviews(Guided Project)
11. Use SurveyMonkey to Create a Survey and Analyze Results
12. Deep Learning with PyTor
ch : Image Segmentation(Guided Project)
13. AWS S3 Basics (Guided Project)
```
---

     
 
all -  [  A List of free courses from Coursera.  ](https://www.reddit.com/r/udemyfreebies/comments/1e0uzmo/a_list_of_free_courses_from_coursera/) , 2024-07-12-0911
```
Free Online Courses from Reputed Universities on Programming, Data Structure, Algorithms, Computer Architecture, Embedde
d Systems and IoT. [Read More](http://cse.mx-router-ii.com/l/free-coursera-courses-on-computer-science).

1. Introductio
n to Machine Learning By Duke University
2. Data Science Math Skills By Duke University
3. Learn to Program: The Fundame
ntals(Python)
4. Building Systems with the ChatGPT API by Andrew Ng
5. Learn Kali Linux
6. Introduction to Statistics By
 Stanford University
7. ChatGPT Prompt Engineering for Developers
8. LangChain Chat with Your Data By [DeepLearning.AI](
http://DeepLearning.AI)
9. Introduction to Generative AI
10. Preparation for Job Interviews(Guided Project)
11. Use Surv
eyMonkey to Create a Survey and Analyze Results
12. Deep Learning with PyTorch : Image Segmentation(Guided Project)
13. 
AWS S3 Basics (Guided Project)
```
---

     
 
all -  [ How can I set up Llama 3 tokenizer with tiktoken? Where can I find the tokenizer model?? ](https://www.reddit.com/r/LocalLLaMA/comments/1e0u9sd/how_can_i_set_up_llama_3_tokenizer_with_tiktoken/) , 2024-07-12-0911
```
Tl;dr, the title.    
Can someone share like a link and a code snippet/guide if needed for the model I need to use tikto
ken with llama3?

  
Context:

To my understanding, llama 3 is using BPE tiktoken tokenizer, 'llama-bpe', which is simil
ar but different from OpenAI's tokenizers.

I'm not sure if llama 3 uses the same tokenizer as llama or llama 2, but it'
s confusing me when searching.  I read through the python implementation ( [https://github.com/meta-llama/llama3/blob/ma
in/llama/tokenizer.py](https://github.com/meta-llama/llama3/blob/main/llama/tokenizer.py) ), but 'path' is used as place
holders everywhere that it's mentioned, and there is no actual link to the correct model I need to run this code!

I was
 previously using llama.cpp which I believe handles this for you, but I've since migrated over to vLLM because I found i
t nicer for serving models.  I'm also in the process of throwing out my old langchain code, which for the life of me, I 
could not get to co-operate with llama 3's prompt format.  The only reason my code is working locally right now is by tr
icking Langchain into thinking that my vLLM server is actually ChatOpenAI, but then it cries about not having the right 
tokenizer for 'get\_num\_tokens\_from\_messages'.  I just need to fix this tokenizer issue as a duct tape solution, and 
then I think I'm just going to finally scrap all my langchain code.
```
---

     
 
all -  [ CV roasting ](https://i.redd.it/mpvo0e0f8xbd1.jpeg) , 2024-07-12-0911
```
I applied to hundreds of job ads about data science in London and some remote but hardly getting any friction. Any recom
mendations?
```
---

     
 
all -  [ My Serverless Visual LangGraph Editor ](https://www.reddit.com/gallery/1e0twcd) , 2024-07-12-0911
```

```
---

     
 
all -  [ Implementing chat history for Llama-3 in Python ](https://www.reddit.com/r/LocalLLaMA/comments/1e0setw/implementing_chat_history_for_llama3_in_python/) , 2024-07-12-0911
```
I'm using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) (Python bindings for LlamaCPP) for inference w
ith a GGUF of Llama-3 8B Instruct, and I want to implement chat history to enable having a conversation with the model a
s opposed to just making independent calls. I know that higher-level frameworks like LangChain have chat history impleme
nted, but I need to stick to lower-level stuff for a variety of reasons. llama-cpp-python has worked great for me so far
.

Has anybody made a custom implementation of working with chat history? Maybe a data structure to store, load, and wor
k with chat history? Specifically, chat history enabled by passing in the last k interactions to the model. Or honestly 
even summary-based chat history would do. I can write something myself, but if someone has already implemented this, tha
t would be ideal.

Also, when chat history is passed to the model as a summary instead of just the last k interactions, 
how is this summary provided to the model? What kind of system prompt is used in that case?
```
---

     
 
all -  [ 'Why does my RAG suck and how do I make it good' ](https://www.reddit.com/r/LangChain/comments/1e0rsou/why_does_my_rag_suck_and_how_do_i_make_it_good/) , 2024-07-12-0911
```
I've heard so many AI teams ask this question, I decided to sum up my take on this in a short post. Let me know what you
 guys think.

The way I see it, the first step is to change how you identify and approach problems. Too often, teams use
 vague terms like “it ***feels*** like” or “it ***seems*** like” instead of specific metrics, like “the feedback score f
or this type of request improved by 20%.”

When you're developing a new AI-driven RAG application, the process tends to 
be chaotic. There are too many priorities and not enough time to tackle them all. Even if you could, you're not sure how
 to enhance your RAG system. You sense that there's a 'right path' – a set of steps that would lead to maximum growth in
 the shortest time. There are a myriad of great trendy RAG libraries, pipelines, and tools out there but you don't know 
which will work on *your* documents and *your* usecase ([as mentioned in another Reddit post that inspired this one](htt
ps://www.reddit.com/r/LangChain/comments/1dr5kki/the_most_important_thing_to_build_great_rag_system/)).

I discuss this 
whole topic more detail in my [Substack article](https://pashpashpash.substack.com/p/why-does-my-rag-suck-and-how-do-i) 
including specific advice for pre-launch and post-launch, but in a nutshell, when starting any RAG system ***you need to
 capture valuable metrics like cosine similarity, user feedback, and reranker scores - for every retrieval, right from t
he start***.

Basically, in an ideal scenario, you will end up with an **observability table** that looks like this:

* 
**retrieval\_id** (some unique identifier for every piece of retrieved context)
* **query\_id** (unique id for the input
 query/question/message that RAG was used to answer)
* **cosine similarity score** (null for non-vector retrieval e.g. e
lastic search)
* **reranker relevancy score** (highly recommended for ALL kinds of retrieval, including vector and tradi
tional text search like elastic)
* **timestamp**
* **retrieved\_context** (optional, but nice to have for QA purposes)
 
  * e.g. `'The New York City Subway [...]'`
* **user\_feedback**
   * e.g. `true (thumbs up)`

Once you start collecting
 and storing these super powerful observability metrics, you can begin analyzing production performance. We can [categor
ize this analysis into two main areas](https://x.com/jxnlco/status/1803899526723387895):

1. Topics: This refers to the 
content and context of the data, which can be represented by the way words are structured or the embeddings used in sear
ch queries. You can use topic modeling to better understand the types of responses your system handles.
   * E.g. People
 talking about their family, or their hobbies, etc.
2. Capabilities (Agent Tools/Functions): This pertains to the functi
onal aspects of the queries, such as:
   * Direct conversation requests (e.g., *“Remind me what we talked about when we 
discussed my neighbor's dogs barking all the time.”*)
   * Time-sensitive queries (e.g., *“Show me the latest X”* or *“S
how me the most recent Y.”*)
   * Metadata-specific inquiries (e.g., *“What date was our last conversation?”*), which mi
ght require specific filters or keyword matching that go beyond simple text embeddings.

By applying clustering techniqu
es to these topics and capabilities (I cover this in more depth in my [previous article on K-Means clusterization](https
://pashpashpash.substack.com/p/tackling-the-challenge-of-document)), you can:

* Group similar queries/questions togethe
r and categorize them by topic e.g. *“Product availability questions”* or capability e.g. *“Requests to search previous 
conversations”*.
* Calculate the frequency and distribution of these groups.
* Assess the average performance scores for
 each group.

This data-driven approach allows you to prioritize system enhancements based on actual user needs and syst
em performance. For instance:

* If person-entity-retrieval commands a significant portion of query volume (say 60%) and
 shows high satisfaction rates (90% thumbs up) with minimal cosine distance, this area may not need further refinement.

* Conversely, queries like 'What date was our last conversation' might show poor results, indicating a limitation of our
 current functional capabilities. If such queries constitute a small fraction (e.g., 2%) of total volume, it might be mo
re strategic to temporarily exclude these from the system’s capabilities (*“I forget, honestly!”* or *“Do you think I'm 
some kind of calendar!?”*), thus improving overall system performance.
   * Handling these exclusions gracefully signifi
cantly improves user experience.
      * When appropriate, Use humor and personality to your advantage instead of saying
 *“I cannot answer this right now.”*

**TL;DR:**

Getting your RAG system from “sucks” to “good” isn't about magic solut
ions or trendy libraries. The first step is to implement strong observability practices to continuously analyze and impr
ove performance. Cluster collected data into topics & capabilities to have a clear picture of how people are using your 
product and where it falls short. Prioritize enhancements based on real usage and remember, a touch of personality can g
o a long way in handling limitations.

For a more detailed treatment of this topic, check out my [article here](https://
pashpashpash.substack.com/p/why-does-my-rag-suck-and-how-do-i). I'd love to hear your thoughts on this, please let me kn
ow if there are any other good metrics or considerations to keep in mind!
```
---

     
 
all -  [ training LLM for Langgraph specific use ](https://www.reddit.com/r/LangChain/comments/1e0r49j/training_llm_for_langgraph_specific_use/) , 2024-07-12-0911
```
Hello everyone,



I wanna use a LLM to create an agent in langgraph with this kind of architecture:

https://preview.re
dd.it/uw5c6kozmwbd1.png?width=199&format=png&auto=webp&s=ca17ef164138c99d913c9d068c59ef5c996ad56c

The idea is similar t
o a React agent where the model has to provide a prompt for my terminal tool and observe if it achieve a given objective
.

I have a question about how should i train such model?

Could i use DPO/ORPO procedure to align my model on multi-ste
p feeding him the context each time?

Or is there a smarter way to do that?

Thanks for your suggestions!
```
---

     
 
all -  [ I built a suite of AI Agents to help me optimize my budget and make better investment decisions ](https://www.reddit.com/r/SideProject/comments/1e0qopg/i_built_a_suite_of_ai_agents_to_help_me_optimize/) , 2024-07-12-0911
```
I built a pipeline of containers using[ ~Dagger~](https://dagger.io/) and GitHub Actions to automate the process of fetc
hing, updating and structuring data to send to an agentic workflow, using[ ~LangChain~](https://www.langchain.com/) to i
nteract with multiple LLM models that use tools and custom functions to help me answer these questions;

1. Are there tr
ends and habits that my wife and l can learn from our spending and what actionable insights can we take to help better p
ropel us to our financial goals?

2. How can I analyze and summarize information and data necessary to help me make more
 well informed investment decisions?

With the first pipeline (Budgeting Buddy):

* I use a Tiller plugin in Google Shee
ts to fetch transactions from multiple bank accounts
* I use GitHub Actions to trigger a pipeline of containers every 4 
days
* The first container fetches transactions from the spreadsheet
* Another fetches transactions from a MongoDB datab
ase, to filter for new transactions
* The next container uses a zero-shot classification model; facebook/bart-large-mnli
 to classify my transactions into different categories (grocery, snacks, takeouts, entertainment, transportation, credit
 card payment, shopping, personal care and healthcare)
* The next container writes this data to a MongoDB database
* I r
euse a container fetching data from MongoDB, passing the output to a method that structures the data. Specifically, I us
e Atlas Search to aggregate data on the week and category level
* I pass this output to a container that makes a number 
of OpenAI calls to carry out tasks to generate nuanced advice (based on historical spend) to help me budget
* I send thi
s output to another container that sends this feedback back to me via SMS

Dagger Modules:[~https://daggerverse.dev/sear
ch?q=EmmS21~](https://daggerverse.dev/search?q=EmmS21) 

My Second pipeline (Investment Optimizer):

* Fetches data from
 my Google Sheets (re-using a module from the previous pipeline)
* Specifically extract my debt and structure this data

* My AI Agent interacts with a few tools (fetch stocks - using a method running inside a Dagger module, plotly- to draw 
up visualizations to explain the rationale of the decisions made) and custom functions (i. A function that uses data ret
rieved through search on different types of debts and grades the information ie. Does this type of debt have a high, low
 or moderate impact on factors that affect my credit score, converting the; high, low and moderate ratings produced by L
LM to multipliers. The function uses these multipliers to change the interest rate to factor in not just the interest ra
te but the ‘importance of the debt’. I have another function that spells out the logic of paying off all minimum payment
s for my debt then comparing the interest savings from paying off every $1k of debt versus the returns from investing in
 high performing stocks based on past returns. Percentages are assigned to each option and the remainder of the availabl
e money is allocated based on this).
* The output is sent through another container to me via email.

I am currently reb
uilding the Investment Optimizer to focus purely on helping me make informed investment decisions. This means considerin
g fundamental analysis as opposed to just historical return rates (ie. I am looking at data from 10-Q and 10-K filings o
ver a 10 year period along with search data to build AI Agents that will identify 2 stocks per month and produce a summa
ry of these stocks and factors likely to drive their growth. I would use this information to carry out more research on 
the stocks and potentially invest if it makes sense).

Here’s the presentation of what I built:[~https://www.youtube.com
/watch?v=YxfW-TgOGkc~](https://www.youtube.com/watch?v=YxfW-TgOGkc) 
```
---

     
 
all -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-12-0911
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

     
 
all -  [ Generative UI ](https://www.reddit.com/r/LangChain/comments/1e0qc2w/generative_ui/) , 2024-07-12-0911
```
Hi,

I have a few questions after watching the generative UI videos by Langchain (fyi my fullstack/frontend knowledge is
 poor).

What's the difference between Langchain's generative UI vs just streaming data to the front end to be made into
 a react component with websockets.

For example, I am streaming results to my React frontend from my django backend. In
 my frontend I am using  `new WebSocket(\${REACT_APP_WS_URL}/ws/chat/\)`   and   `ws.current.onmessage`   to check for  
 `{'event': 'on_tool_start', ...}.`    If event is 'on\_tool\_start', it returns a loading component instead of a text m
essage response, and if the message is   `{'event': 'on_tool_end', 'output': [{ 'key':'value', ..]}`   it replaces the l
oading component with a react component that takes 'output' as inputs.

Follow up questions

* Why does the Langchain im
plementation use react server components in the frontend when there is a separate backend server with FastAPI?
* What is
 ai/rsc in   `(import { createStreamableUI } from 'ai/rsc')`   . It looks like it's next/Vercel specific? Where are the 
docs for createStreamableUI ?
* How much value is there from the extra complexity in Langchain implementation (specifica
lly in the frontend).

[Here is the gen ui repo](https://github.com/bracesproul/gen-ui-python/tree/main)  
[Here is the 
youtube video](https://www.youtube.com/watch?v=d3uoLbfBPkw&t=1557s)
```
---

     
 
all -  [ Fine Tuning LLM with tool Usage ](https://www.reddit.com/r/LangChain/comments/1e0oqol/fine_tuning_llm_with_tool_usage/) , 2024-07-12-0911
```
I've been having issues training my llm to be able to use tool during certain part of the conversaiton. Prior to fine-tu
ning the interaction with the agent is good, it calls all the necessary when needed, but I haven't found a way to incorp
orate the tool usage in the training data correctly, I'm missing something... after training it simply doesn't use any t
ools.... I'm currently using langgraph. Any suggestions woud be highly appreciated.
```
---

     
 
all -  [ Langchain + Django ORM integration  ](https://www.reddit.com/r/LangChain/comments/1e0nqxb/langchain_django_orm_integration/) , 2024-07-12-0911
```
I have been working with django and langchain for few days. What i have noticed is  it’s not possible to save the langch
ain messages directly with the django ORM. So the integration seems bit confusing when trying to save some details using
 the django models and others using pydantic models for langchain. Is this a missing support by langchain or am I missin
g something ?
```
---

     
 
all -  [ Looking for research papers to beef up my Hackathon project ](https://www.reddit.com/r/LangChain/comments/1e0mgl2/looking_for_research_papers_to_beef_up_my/) , 2024-07-12-0911
```
I created a quick proof of concept by copy pasting LangChain code from here [https://js.langchain.com/v0.1/docs/modules/
agents/agent\_types/tool\_calling/](https://js.langchain.com/v0.1/docs/modules/agents/agent_types/tool_calling/)

It bas
ically uses a tool calling agent that uses the google search tool, web browser tool and a retriever tool that allows a u
ser to search for data and also query their own uploaded documents. I ended up using the tool calling agent as the reAct
 agent was causing a lot of bugs. The issue now is that I read a few research papers on reAct  prompting and was plannin
g to use them as sources to beef up my hackathon presentation and make it look more cutting edge. I'm just wondering whe
ther anyone has any similar papers that can make my current POC sound more cutting edge? I know this probably sounds rea
lly stupid to you but I really want to win this hackathon and I believe that the presentation is equally as important as
 the MVP. Thanks a lot.
```
---

     
 
all -  [ Hallucinations: Why You Should Care as an AI Developer ](https://www.reddit.com/r/pythia/comments/1e0lprc/hallucinations_why_you_should_care_as_an_ai/) , 2024-07-12-0911
```
https://preview.redd.it/ewfgdm97avbd1.png?width=2048&format=png&auto=webp&s=a981cdc6221ef83e4143546160d40debc0605635

*U
nderstand why hallucination detection is important for reliable LLMs. Learn the characteristics of a good hallucination 
detector.*

From speech recognition to text generation, generative AI and LLMs have become involved in various applicati
ons and scenarios. The generative AI industry is projected to become a [$1.3 Trillion market](https://www.bloomberg.com/
professional/insights/data/generative-ai-races-toward-1-3-trillion-in-revenue-by-2032/#:~:text=Bloomberg%20Intelligence&
text=Generative%20AI%20is%20poised%20to,our%20proprietary%20market%2Dsizing%20model.) by 2032, with a compound annual gr
owth rate (CAGR) of 42%. Generative AI products are predicted to add about $289 billion of new revenue to the software i
ndustry.

These projections for expansion reflect the presence of LLMs in all aspects of life, including healthcare. The
ir pervasive presence emphasizes the need for reliable AI to protect end-users from misleading decisions. However, LLMs 
often produce hallucinated outputs, resulting in penalties, lost trust in AI, reputation damage, and human life.

Let’s 
explore the need for AI reliability and how to achieve reliable AI solutions.

# Why Does AI Reliability Matter?

Though
 LLMs have become increasingly intelligent, they still tend to hallucinate. AI hallucinations are AI-generated outputs t
hat seem confident but are inaccurate and misleading.

Industry-leading LLMs like ChatGPT have a [31%](https://www.medpa
getoday.com/ophthalmology/generalophthalmology/105672#:~:text=The%20mean%20hallucination%20rate%20for,and%2029%25%20with
%20version%204.0.) hallucination rate when used for scientific purposes. These hallucinations have significant costs, in
cluding:

* **Healthcare costs:** Misdiagnoses can lead to [deaths and serious disabilities](https://www.statnews.com/20
23/07/21/misdiagnoses-cost-the-u-s-800000-deaths-and-serious-disabilities-annually-study/). It can also cost healthcare 
providers significant losses in penalties and reputation damage.
* **Litigation costs:** AI hallucinations can cause leg
al penalties in cases such as privacy violations or sensitive remarks. Legal errors can average [$250,000](https://www.b
hfloridalaw.com/the-average-settlement-for-a-medical-malpractice-case/) in settlements.
* **Financial sector:** When LLM
s are used for research purposes, hallucinations can guide researchers toward poor decision-making. Poor investment deci
sions can lead to millions in losses.
* **Operational downtime:** Erroneous or misleading information can lead to disrup
tions or failures in operational processes. AI-related downtime can cost [$10,000](https://www.linkedin.com/pulse/cost-d
owntime-thoughtsol-infotech-pvt-ltd-vjljc/) per hour.
* **Brand damage:** Misleading outputs can damage a company's repu
tation and result in client hostility.

Governments and NGOs are becoming involved in achieving reliable AI. For example
, the [EU AI Act](https://artificialintelligenceact.eu/#:~:text=What%20is%20the%20EU%20AI,AI%20to%20three%20risk%20categ
ories.) is a European regulation on AI protection that covers various aspects of AI development and deployment to ensure
 safe AI.

Complying with these regulations requires the development of reliableLLMs that produce reliable outputs.

# E
xisting AI Reliability Solutions and Their Challenges

Existing AI reliability solutions include bias detection, explain
able AI (XAI) methods, adversarial techniques, etc. These solutions detect hallucinations and ensure reliable AI to some
 extent, but their limitations keep them from achieving safe and accurate AI.

They lack continuous monitoring support, 
transparency, and claim verification, which gives rise to their limitations, including:

1. **Limited scalability:** Cur
rent methods depend on the availability of high-quality training data, which prevents them from offering scalable AI rel
iability solutions.
2.  **Lack of explainability:** Current methods fail to explain why a particular LLM response is fla
gged as a hallucination, making it difficult for developers to fix factual issues.
3. **Low accuracy:** Existing solutio
ns are not as accurate, making them ineffective for mission-critical applications like life sciences.

# 10 Things to Lo
ok for in an AI Reliability Solution

AI reliability solutions must meet certain criteria to effectively detect hallucin
ations and offer transparency in their decisions. Here are the ten key things to look for in an AI reliability solution:


# 1. LLM Usage Scenarios

An AI reliability solution should accommodate different LLM usage scenarios. The three LLM u
sage scenarios include:

1. **Zero context:** The AI reliability solution should be able to directly compare references 
it finds with the LLM’s responses to assess accuracy.
2. **Noisy context:** When a question includes some context but is
 either noisy or incomplete, the AI reliability solution must be capable of consulting authoritative data before the LLM
 generates a response.
3. **Accurate context:** When the context is complete and reliable, it can use the references to 
provide a comprehensive summary or information in response.

[LLM usage scenarios](https://preview.redd.it/iws0jnex8vbd1
.png?width=2880&format=png&auto=webp&s=1b7e2fd50a37a4e82735bdd06619f35dccbb4066)

These scenarios/ contexts guide the re
liability solution in finding references and verifying LLM claims.

# 2. Claim Extraction

The hallucination detection s
olutions should be able to decompose LLM responses into knowledge triplets. Unlike traditional methods, knowledge triple
ts extract granular details from content and highlight the relationship among words within a sentence.

Knowledge triple
ts represent **<subject, predicate, object>**, highlighting the connection between the three and creating a better conte
xtual understanding. For example:

[Knowledge Triplet Example](https://preview.redd.it/mvzxmp319vbd1.png?width=2352&form
at=png&auto=webp&s=5d357b26bf3f7170136c18755ba5300c02a17865)

# 3. Claim Categorization

After the claim extraction from
 LLM responses and references/ knowledge base, the hallucination detector must be able to categorize them based on their
 hallucination levels. Claim categorization guides developers toward the improvement of LLM by offering insights into it
s capabilities. The four categories for claim categorization include:

1. **Entailment:** Claims in both response and re
ferences, indicating accurate outputs.
2. **Contradiction:** Claims present in LLM responses but disregarded by referenc
es.
3. **Missing facts:** Claims present in references but absent in LLM responses, representing gaps in LLM responses.

4. **Neutral:** Claims present in LLM response but are neither contradicted nor confirmed by the references.

[Claim cat
egorization based on hallucination level](https://preview.redd.it/n57d4dh39vbd1.png?width=1798&format=png&auto=webp&s=51
b4161dc45f7dc7c17bedb82d1587eafe0d5df2)

# 4. Accuracy Metrics

An AI monitoring tool must be able to calculate the over
all accuracy of LLM based on claim categorization. The accuracy metric represents the proportion of factually correct cl
aims in the LLM response. Mathematically, accuracy is measured as:

https://preview.redd.it/9dkux1979vbd1.png?width=2780
&format=png&auto=webp&s=41a63d1930d462cf8497831112191e2e6df0e628

Where:

* Entailment: Claims flagged as Entailment
* C
ontradiction: Claims flagged as Contradiction
* Reliability: Calculated using external data (i.e., knowledge graphs or R
AGs)

# 5. Task Specific Metrics

There are two types of task-specific metrics, i.e., Core metrics specialized to the ta
sk and additional metrics for measuring the quality of the responses with respect to the task.

Specializing core metric
s rely on the type of AI checker being used:

1. LLM-based checkers can enhance their accuracy by considering additional
 context provided in the form of a question when generating claim classification.
2. NLI-based checkers utilize a QA (Qu
estion Answering) evaluator model to verify the alignment of a response with a question.
3. Knowledge graph-based checke
rs rely on Knowledge Graphs (KGs) to verify structured information about entities, relationships, and concepts.

https:/
/preview.redd.it/7kjj902d9vbd1.png?width=1436&format=png&auto=webp&s=ff9cd0af3478d8f36b2aeaaa8a675934a68d668d

# 6. Syst
ematic Error

The AI hallucination detector must be able to identify systematic errors. Systematic errors are recurring 
inconsistencies in LLM responses. Identifying them involves:

1. Comparing the reference information to itself. This mea
ns using the same reference as the knowledge base and the standard for comparison.
2. Generating core metrics to assess 
LLM performance. Metrics highlight the system's ability to classify claims as true, false, or neutral correctly.
3. Defi
ning a systematic error checker, which is the harmonic mean of the complement of Entailment and Contradiction.

The idea
l result is 100% Entailment, 0% Contradiction, and 0% Neutral claims. Mathematically, a systematic error checker is repr
esented as:

https://preview.redd.it/871dqk9j9vbd1.png?width=1962&format=png&auto=webp&s=c3453f014e83b6c7ff0439b15199b2e
bf3ea6ead

# 7. Robust Set of Validators

An AI reliability solution should use a robust set of input/ output validators
 to protect sensitive information from leakage, misleading outputs, and toxic outputs. These validators validate LLM inp
uts and responses to ensure they meet quality standards and are accurate. The validators also protect against cyber atta
cks such as malicious input or prompt injections.

[Example Input\/Output Validators](https://preview.redd.it/hdgv807m9v
bd1.png?width=2058&format=png&auto=webp&s=fd786a3c48737ac62e6e943598e6bee1279ca1e0)

# 8. Reporting

A good hallucinatio
n detection solution provides reports highlighting hallucination trends over time. These reports give insight into model
 improvement with time and systematic errors. Updated reports allow targeted adjustments to enhance the LLM’s reliabilit
y and effectiveness.

Moreover, detailed analysis of these trends helps understand the underlying causes of hallucinatio
ns, resulting in better training and fine-tuning.

# 9. Continuous Alerting and Monitoring

[Continuous monitoring](http
s://askpythia.ai/blog/why-continuous-monitoring-is-essential-for-maintaining-ai-integrity) and alerting are crucial for 
real-time hallucination detection and on-time correction. Continuous monitoring keeps track of LLM outputs against each 
user query, highlighting a model’s strengths and weaknesses. Alerting systems send email/SMS notifications about LLM per
formance, which helps address bias in model outputs before it perpetuates bias in the public.

[Real-time Monitoring and
 Alert Rules Example](https://preview.redd.it/iikmvyks9vbd1.png?width=2852&format=png&auto=webp&s=e369d8975793f59e21d955
581e6d84b136b0c8e8)

# 10. LangChain Integration

[LangChain](https://www.langchain.com/) is a Natural Language Processi
ng (NLP) framework that provides pre-trained models and tools to customize and improve model performance. LangChain has 
an active community, and LLM developers use it to develop robust LLMs because of its flexibility and support. The abilit
y of an AI reliability solution to [integrate with LangChain](https://askpythia.ai/blog/a-guide-to-integrating-the-pythi
a-api-using-wisecube-python-sdk) makes it a handy choice for hallucination detection, as most of the LLM workflows are b
uilt using LangChain.

[LangChain Workflow with AI Reliability Solution](https://preview.redd.it/lyeikorw9vbd1.png?width
=2684&format=png&auto=webp&s=53db6572ce38efa43f837b498c5d5091cc47e0d8)

# Wisecube’s Pythia: a Reliable Hallucination De
tection Tool

Wisecube’s [Pythia](https://askpythia.ai/blog/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinati
ons), an AI reliability solution, boasts the ten crucial characteristics of AI hallucination detectors. These characteri
stics set Pythia apart from other solutions by offering the following benefits:

* **Enhanced reliability:** Reduces the
 risk of AI errors using built-in hallucination detection and validators
* **Trustworthy outputs:** Builds trust in AI s
ystems through continuously monitoring accurate and reliable outputs.
* **Easy integration:** Integrates into existing L
angChain workflows, empowering developers to develop trustworthy AI systems.
* **Customizable detection:** Pythia can be
 configured to suit specific use cases, resulting in improved flexibility and increased accuracy.

**To learn more about
 the impact of hallucinations and the characteristics of an effective AI reliability solution,** [**watch the webinar he
re.** ](https://www.youtube.com/watch?v=PXFXKMJO9jo&t=20s)

*The article was originally published on* [Pythia's website.
](https://askpythia.ai/blog/hallucinations-why-you-should-care-as-an-ai-developer)
```
---

     
 
all -  [ Chat interfaces are holding back LLMs - we need a more visual approach ](https://www.reddit.com/r/LangChain/comments/1e0k7e8/chat_interfaces_are_holding_back_llms_we_need_a/) , 2024-07-12-0911
```
I believe that chat interfaces are the worst way to interact with LLMs, but they're currently our only real option (voic
e doesn't count). Here's my reasoning:

1. Even though we're programmed as humans to 'prompt' each other in daily intera
ctions, I've observed that when it comes to LLMs, people are very deficient at it.
2. In the past few decades, Microsoft
 and Apple have trained us to use computers primarily through visual interactions (clicks, taps, buttons, etc.).
3. Mayb
e the interface for LLMs should be more visual, rather than relying on text prompting.

What do you guys think about thi
s? Are we limiting the potential of LLMs by sticking to chat interfaces? Could a more visual approach make these AI tool
s more accessible and effective for the average user?
```
---

     
 
all -  [ RAG Techniques for a Big Codebase with 10k Repos ](https://www.reddit.com/r/LangChain/comments/1e0jpkk/rag_techniques_for_a_big_codebase_with_10k_repos/) , 2024-07-12-0911
```
This post by an AI engineer explains the challenges they encountered when implementing RAG for massive enterprise codeba
ses and how they solved them. They share lots of alpha on strategies for chunking, creating vector embeddings for code c
hunks, using LLMs to generate natural language descriptions that improve indexing, and using LLMs to rank the chunks tha
t are retrieved from the vector store: [https://www.codium.ai/blog/rag-for-large-scale-code-repos/](https://www.codium.a
i/blog/rag-for-large-scale-code-repos/)
```
---

     
 
all -  [ Filtering based on Metadata ](https://www.reddit.com/r/LangChain/comments/1e0iovb/filtering_based_on_metadata/) , 2024-07-12-0911
```
Hey everyone, I am trying to filter the items I retrieve by Metadata fields. I have like 5 metadata fields and I am tryi
ng to use 3 filters using 3 of those fields but somehow, only one of them does not work.

I declare the attribute info i
n metadata\_field\_info like that:

    AttributeInfo(
        name='speaker',
        description='The person who spoke
, identified as either 'Moderator' or 'Participant'.',
        type='string',
    ),

Then, I try to filter it like

   
         filter=f'and(eq('speaker', 'Participant'), eq('participant', 'k6'), ({part_filter}))',

However, this did not w
ork. So I asked Claude and updated it:

            filter_str=f'speaker == 'Participant' and participant == 'k6' and ({
part_filter})',

This also did not work. I decided to check LangChain documentations and using [this page](https://pytho
n.langchain.com/v0.1/docs/modules/data_connection/retrievers/self_query/) as a reference, I changed it to:

            
filter=f'and(eq(\'speaker\', \'Participant\'), eq(\'participant\', \'k6\'), ({part_filter}))',

When this also did not w
ork. I got suspicious about whether there was a problem with my tagging so I checked my DB and found out it was also cor
rect. The item below is tagged 'Moderator' as you can see but it is retrieved when I use the filters above.

https://pre
view.redd.it/5x8krgis8ubd1.jpg?width=1080&format=pjpg&auto=webp&s=8d193e29a4eef3213b7097c10b2ceab7da664bfa

Weird part i
s I use exactly same syntax for other filters and they work. I am lost. Any ideas?
```
---

     
 
all -  [ how to use agentexecutor.stream_events with streamlit ](https://www.reddit.com/r/LangChain/comments/1e0ezhj/how_to_use_agentexecutorstream_events_with/) , 2024-07-12-0911
```
I'm trying to create a streaming agent chatbot with streamlit as the frontend. I was able to find an example of this usi
ng callbacks, and streamlit even has a special callback class.

However, it looks like things sure change quickly. From 
langchain's documentation it looks like callbacks is being deprecated, and there is a new function astream\_events. I'm 
very happy with how simple it is to stream events with astream\_events.

However, I'm having some issues with getting th
is to work with streamlit. It's mostly working, but for some small details. For example:

        async for event in age
nt_executor.astream_events(
                    {'input': user_query},
                    version='v2',
               
     config=cfg
                ):
                kind = event['event']
                if kind == 'on_chat_model_strea
m':
                    content = event['data']['chunk'].content
                    if content:
                       
 answer_container.write(content)

There are other events, but I can illustrate this problem with just 'on\_chat\_model\_
stream'. 

Just focusing on the event 'on\_chat\_model\_stream', this causes the content to be written one word in every
 line, so the chat message looks like:

Hello

how

may

I

help

you

So, it looks like the content is being written to
ken by token. However, I can't use write\_stream, because I would get the error \`\`st.write\_stream\` expects a generat
or or stream-like object as input not <class 'str'>. Please use \`st.write\` instead for this data type.\`

How do I get
 the content to stream in this case?
```
---

     
 
all -  [ I used Langchain to build a Slack Agent - My Experience ](https://www.reddit.com/r/LangChain/comments/1e03z0y/i_used_langchain_to_build_a_slack_agent_my/) , 2024-07-12-0911
```
My AI Agent does the following:

* Instant answers from the web in any Slack channel
* Code interpretation & execution o
n the fly
* Smart web crawling for up-to-date info

project link : [git.new/slack-bot-agent-ollama](http://git.new/slack
-bot-agent-ollama)

**My experience with Langchain**

One of the key advantages of Langchain is its ability to integrate
 different LLMs into your applications. This flexibility allows you to experiment with various models and find the one t
hat best suits your needs.

Langchain's approach is a game-changer. However, I do have one gripe - the documentation cou
ld be better. I wasn't aware that I needed to use the ChatModels instead of the direct models, and this wasn't specified
 clearly enough. This kind of information is crucial for users to get up and running quickly.

https://preview.redd.it/j
jtezql9nqbd1.png?width=1283&format=png&auto=webp&s=5707c453e8a1f1bc0f756b6821780603065dd4fb
```
---

     
 
all -  [ What is your RAG Setup?  ](https://www.reddit.com/r/LocalLLaMA/comments/1e033xj/what_is_your_rag_setup/) , 2024-07-12-0911
```
I'd like to know what comprises your RAG setup. 

Is it as simple as a Langchain Q&A or something more complex with a cu
stom encoder, reranker, searcher and custom chunking and all those?
```
---

     
 
all -  [ Comparing Ollama Mistral and GPT-4o ](https://www.reddit.com/r/agentswithai/comments/1e033kt/comparing_ollama_mistral_and_gpt4o/) , 2024-07-12-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'
* Mathematics: 'What is the
 significance of the Riemann Hypothesis in number theory?'
* Economics: 'How does inflation affect purchasing power and 
economic growth?'
* Psychology: 'What is cognitive dissonance and how does it influence human behavior?'
* Environmental
 Science: 'What are the primary causes and effects of ocean acidification?'
* Technology: 'How might artificial general 
intelligence (AGI) impact the job market?'

# My Experience setting it up with Ollama

I've used HuggingFace for using O
pen Source LLMs all this while. I admit that had it's own hassles but it wasn't very hard to set up as long as you paid 
good attention to the docs. This time i decided to use Ollama. I run a windows machine, so i installed it and struggled 
for a bit in terms of setting it up and using it with Langchain. You have to use ChatOllama and not just Ollama, but it 
was very easy to bind the tools using Composio. I also tried setting it up on Colab but running the server, connecting i
t to the agent with a trigger is difficult.

As for connecting with Slack i used triggers on Composio. You can use it to
 connect agents to Slack and set a trigger everytime the bot is tagged and a message is sent, its also LLM agnostic. I u
sed it for my previous project and it worked very well.

if you want to try the project here's the link: [git.new/slack-
bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
|Performance on wri
ting|Performs exceptionally well for its size, often outperforming larger models on certain benchmarks. It is very good 
if you want concise and precise answers. This can be beneficial for readers who want a quick overview without diving int
o too much detail.|Provides more detailed and longer responses. It has better writing structure compared to mistral, ans
wers have more depth and includes subtle details. It is better if you want to research deep into a topic.|
|Strengths|Pe
rformed well in the Agentic workflow. The whole process of the agent being triggered when it receives a message and gene
rating a response after internet search was completed quicker.|Performed equally well in the Agentic workflow. Larger qu
eries can be accomodated and understood by the LLM. Hallucinates less in comparison to mistral.|
|Weakness|Larger querie
s cannot be accomodated sometimes and i get a 500 error. Significant effort in setting it up on your system. Windows or 
Linux.|It becomes expensive quickly. It should be explicitly told to provide concise answers if you dont want detailed r
esponses to everything.|
```
---

     
 
all -  [ Comparing GPT-4o with Open Source Models ](https://www.reddit.com/r/OpenAI/comments/1e02ney/comparing_gpt4o_with_open_source_models/) , 2024-07-12-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'

# My Experience setting it
 up with Ollama

I've used HuggingFace for using Open Source LLMs all this while. I admit that had it's own hassles but 
it wasn't very hard to set up as long as you paid good attention to the docs. This time i decided to use Ollama. I run a
 windows machine, so i installed it and struggled for a bit in terms of setting it up and using it with Langchain. You h
ave to use ChatOllama and not just Ollama, but it was very easy to bind the tools using Composio. I also tried setting i
t up on Colab but running the server, connecting it to the agent with a trigger is difficult.

As for connecting with Sl
ack i used triggers on Composio. You can use it to connect agents to Slack and set a trigger everytime the bot is tagged
 and a message is sent, its also LLM agnostic. I used it for my previous project and it worked very well.

if you want t
o try the project here's the link: [git.new/slack-bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

# Comparison
 Table

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
||||
|Performance on writing|Performs exceptionally well for its size
, often outperforming larger models on certain benchmarks. It is very good if you want concise and precise answers. This
 can be beneficial for readers who want a quick overview without diving into too much detail.|Provides more detailed and
 longer responses. It has better writing structure compared to mistral, answers have more depth and includes subtle deta
ils. It is better if you want to research deep into a topic.|
|Strengths|Performed well in the Agentic workflow. The who
le process of the agent being triggered when it receives a message and generating a response after internet search was c
ompleted quicker.|Performed equally well in the Agentic workflow. Larger queries can be accomodated and understood by th
e LLM. Hallucinates less in comparison to mistral.|
|Weakness|Larger queries cannot be accomodated sometimes and i get a
 500 error. Significant effort in setting it up on your system. Windows or Linux.|It becomes expensive quickly. It shoul
d be explicitly told to provide concise answers if you dont want detailed responses to everything.|
```
---

     
 
all -  [ RAG to search for an information about an employee within a vast collection of documents ](https://www.reddit.com/r/LangChain/comments/1e02kx2/rag_to_search_for_an_information_about_an/) , 2024-07-12-0911
```
Hello everyone,

I have to build a Retrieval-Augmented Generation (RAG) system using a Large Language Model (LLM) **to s
earch for an information about an employee within a vast collection of documents.** The LLM must return the information 
with references indicating the specific page and document.

if someone already done a project similar or can help me wit
h the steps.

what i decided to do is to select an open source llm (qwen2), then fine tune it, after that build a RAG

*
*what is your opinion gays**  
**i need your help**
```
---

     
 
all -  [ Using Ollama Mistral and GPT-4o for my AI Agent - Comparison  ](https://www.reddit.com/r/LocalLLaMA/comments/1e02jpo/using_ollama_mistral_and_gpt4o_for_my_ai_agent/) , 2024-07-12-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'

# My Experience setting it
 up with Ollama

I've used HuggingFace for using Open Source LLMs all this while. I admit that had it's own hassles but 
it wasn't very hard to set up as long as you paid good attention to the docs. This time i decided to use Ollama. I run a
 windows machine, so i installed it and struggled for a bit in terms of setting it up and using it with Langchain. You h
ave to use ChatOllama and not just Ollama, but it was very easy to bind the tools using Composio. I also tried setting i
t up on Colab but running the server, connecting it to the agent with a trigger is difficult.

As for connecting with Sl
ack i used triggers on Composio. You can use it to connect agents to Slack and set a trigger everytime the bot is tagged
 and a message is sent, its also LLM agnostic. I used it for my previous project and it worked very well.

if you want t
o try the project here's the link: [git.new/slack-bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

# Comparison
 Table

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
|Performance on writing|Performs exceptionally well for its size, oft
en outperforming larger models on certain benchmarks. It is very good if you want concise and precise answers. This can 
be beneficial for readers who want a quick overview without diving into too much detail.|Provides more detailed and long
er responses. It has better writing structure compared to mistral, answers have more depth and includes subtle details. 
It is better if you want to research deep into a topic.|
|Strengths|Performed well in the Agentic workflow. The whole pr
ocess of the agent being triggered when it receives a message and generating a response after internet search was comple
ted quicker.|Performed equally well in the Agentic workflow. Larger queries can be accomodated and understood by the LLM
. Hallucinates less in comparison to mistral.|
|Weakness|Larger queries cannot be accomodated sometimes and i get a 500 
error. Significant effort in setting it up on your system. Windows or Linux.|It becomes expensive quickly. It should be 
explicitly told to provide concise answers if you dont want detailed responses to everything.|
```
---

     
 
all -  [  UI for langgraph for agent with user input ](https://www.reddit.com/r/LangChain/comments/1e02blv/ui_for_langgraph_for_agent_with_user_input/) , 2024-07-12-0911
```
What’s the  best tool to make a UI for an agent that interacts with the user as it processes tgrough the graph. 
```
---

     
 
all -  [ Connecting Langchain to Snowflake DB with SSO authentication ](https://www.reddit.com/r/LangChain/comments/1e00w6o/connecting_langchain_to_snowflake_db_with_sso/) , 2024-07-12-0911
```
I want to connect my langchain to Snowflake db. But the snowflake I am using have no password but SSO. What is the synta
x should be used to connect the snowflake to langchain using the following function SQLDatabase.from\_uri?
```
---

     
 
all -  [ Accurate Multimodal Slides Search with Real-Time Updates from SharePoint, Google Drive, and Local Da ](https://www.reddit.com/r/LangChain/comments/1dzzrw5/accurate_multimodal_slides_search_with_realtime/) , 2024-07-12-0911
```
Hi r/langchain, I'm sharing an example on building a multi-modal search application using GPT-4o, featuring extraction o
f metadata and hybrid indexing for accurately retrieving relevant information from presentations.

* Repo: [~https://git
hub.com/pathwaycom/llm-app/tree/main/examples/pipelines/slides\_ai\_search~](https://github.com/pathwaycom/llm-app/tree/
main/examples/pipelines/slides_ai_search)
* Architecture: [~https://github.com/pathwaycom/llm-app/tree/main/examples/pip
elines/slides\_ai\_search#architecture~](https://github.com/pathwaycom/llm-app/tree/main/examples/pipelines/slides_ai_se
arch#architecture)

This project also focuses on automatically updating indexes as changes happen in your repository.   

  
**Quick details:**

* **Ingestion:** The application reads slide files (PPTX and PDF) stored locally or on Google Dr
ive or Microsoft SharePoint.
* **Parsing:** Utilizes the SlideParser from Pathway, configured with a detailed schema. Th
e app parses images, charts, diagrams, and other visual elements as well, and features automatic unstructured metadata e
xtraction. 
* **Indexing:** Parsed slide content is embedded using OpenAI's embedder and stored in Pathway's vector stor
e ([natively available on LangChain](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pathway/)) that is
 optimized for incremental indexing.

**How it helps:**

1. Text in presentations is often limited. This example removes
 the need to manually sift through countless presentations by recalling keywords.
2. Organize your slide library by topi
c or other criteria. Indexes update automatically whenever a slide is added, modified, or removed.

**Preliminary Result
s:**

* This method has proven to be efficient in managing large volumes of slides, ensuring that the most up-to-date an
d accurate information is available. It significantly enhances productivity by streamlining the search process across Po
werPoints, PDFs, and Slides.

Open to your questions and feedback!
```
---

     
 
all -  [ How are you managing long form content? ](https://www.reddit.com/r/LangChain/comments/1dzxzu0/how_are_you_managing_long_form_content/) , 2024-07-12-0911
```
I'm trying to get Claude to generate content that could be up to 8,000 tokens long.

To overcome the max token output li
mitations, I have specifically prompted Claude to stop generating when the max token limit is reached, and then continue
 exactly where you left off when the user responds with a 'continue' message.

  
Example of the prompt:

    const prom
pt = `
    Generate me an adventure story that is between 6000 - 7000 words long
    If you reach the max token output, 
the user will send a message saying 'continue'
    Before continuing, you should check the previous outputs and start ex
actly where you left off so that the output is coherent and consistent. 
    You should not ackowledge the 'continue' me
ssage in the output, just continue generating the content. 
    We will join the outputs together at the end and they sh
ould form a coherent and consistent response. 
    If you have finished generating the content and the user asks you to 
continue, you should just respond with an empty message. 
    
    For example: 
      Assistant: mess 
      User: cont
inue 
      Assistant: age   
    `

The problem is that it won't do as I ask, it just keeps shortening the story, I fin
d this weird because when I change the max tokens to something like, 50 and then change the requested story to have a le
ngth of 200 words, it works fine for multiple continuations.

Anyone faced this before?
```
---

     
 
all -  [ Is there an alternative to data version control (DVC) on Snowflake? ](https://www.reddit.com/r/snowflake/comments/1dzxi34/is_there_an_alternative_to_data_version_control/) , 2024-07-12-0911
```
Hi all! I am an NLP data scientist. I would like to introduce Snowflake to my company due to its recent native support o
f hosted LLMs and Streamlit.

For data preprocessing and LLM prompt development, I am using DVC in combination with MLfl
ow. I am aware that for the latter you have the option to deploy a staged LangChain to Snowflake. That is cool.

However
, for the DVC part, it is not clear to me how I would keep track of my data versioning during model development.

How wo
uld you do that while developing on Snowflake? Would you do data science model development on Snowflake directly at all?

```
---

     
 
all -  [ Langchain One Hour Ultimate Guide ](https://www.reddit.com/r/generative/comments/1dzv1hk/langchain_one_hour_ultimate_guide/) , 2024-07-12-0911
```
The video tutorial covers:

* How to use LLM from HuggingFaceHub without even loading it.
* Prompt Template for Open Sou
rce LLM
* Converting normal text to Langchain schema
* Vector Database and embedding important functions
* Memory
* LCEL


Langchain Zero to LCEL: [https://www.youtube.com/watch?v=TWmV95-dUgQ](https://www.youtube.com/watch?v=TWmV95-dUgQ)
```
---

     
 
all -  [ Langchain Ultimate Guide using Open Source LLMs ](https://www.reddit.com/r/LangChain/comments/1dzuxak/langchain_ultimate_guide_using_open_source_llms/) , 2024-07-12-0911
```
The video tutorial covers:

- How to use LLM from HuggingFaceHub without even loading it.   
- Prompt Template for Open 
Source LLM  
- Converting normal text to Langchain schema  
- Vector Database and embedding important functions  
- Memo
ry  
- LCEL 

Langchain Zero to LCEL: [https://www.youtube.com/watch?v=TWmV95-dUgQ](https://www.youtube.com/watch?v=TWmV
95-dUgQ)
```
---

     
 
all -  [ Real Time AI Workers using Django x LangChain ](https://www.reddit.com/r/LangChain/comments/1dzs2p4/real_time_ai_workers_using_django_x_langchain/) , 2024-07-12-0911
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

     
 
all -  [ Help Needed: Seeking Advice on Approach and Implementation! (I'm new to this) ](https://www.reddit.com/r/LangChain/comments/1dzrp0a/help_needed_seeking_advice_on_approach_and/) , 2024-07-12-0911
```
Hi, everyone I need help/advice/ideas with approaching a problem. I'm working on a project that generates questions base
d on other questions and documents that have been given. The results should be a mixture of reoccurring questions and ne
wly generated questions from what's uploaded. 



Now I'm still new to building AI products, all I could come up with co
ncerning approaching this problem is to load the document, parse it, chunk it up, and embed the chunks into a vector dat
abase. As for the generation, I'm thinking of using a prompt template and passing the embedding in the prompt.



What d
o y'all think, any suggestions for how I can achieve this? Thanks in advance.
```
---

     
 
all -  [ Serverless Vector/Graph Database for RAG ](https://www.reddit.com/r/LangChain/comments/1dzrcfl/serverless_vectorgraph_database_for_rag/) , 2024-07-12-0911
```
Hello, what are the most used serveless vector/graph databases for LLM RAG usage, with convenient integration in Python 
and AWS (Knowledge base in Bedrock)? Ideally which are PAYG. I wanted to use OpenSearch from AWS, but I don't wanna pay 
700 USD/month though and other solutions don't seem to be serverless at all.
```
---

     
 
all -  [ RAG + Agent  ](https://www.reddit.com/r/LangChain/comments/1dzqcxy/rag_agent/) , 2024-07-12-0911
```
Please can someone provide me a documentation or link or explaination, How to work with RAG with agents  
I have a DB on
 pinecone and i make a tool of it  
then i used a built in tool   
and combine those tools as  
tools = \[tool1,tool2\] 
 
but i am not getting good results and sometimes even it goes in a loop and doesnot generate anything
```
---

     
 
all -  [ Azure Openai GPT 3.5 and 4 not calling multiple tools in parallel  ](https://www.reddit.com/r/LangChain/comments/1dzpiyh/azure_openai_gpt_35_and_4_not_calling_multiple/) , 2024-07-12-0911
```
Hi,i’am facing a bug when trying to call multiple tools at parallel.The model is calling only a single tool every-time. 
See below code.  
The code is given in **langchain documentation** so i tried that but **not getting** the same results 
as in documentation

u/tool  
def add(a: int, b: int) → int:  
“”'Adds a and b.

    Args:
        a: first int
        
b: second int
    '''
    return a + b

u/tool  
def multiply(a: int, b: int) → int:  
“”'Multiplies a and b.

    Args:

        a: first int
        b: second int
    '''
    return a * b

tools = \[add,multiply\]

llm\_with\_tools = llm.b
ind\_tools(tools)  
query = 'What is 3 \* 12? Also, what is 11 + 49?'  
llm\_with\_tools.invoke(query).tool\_calls

Expe
cted Output :\[{'name': 'multiply',  
'args': {'a': 3, 'b': 12},  
'id': 'call\_UL7E2232GfDHIQGOM4gJfEDD'},  
{'name': '
add',  
'args': {'a': 11, 'b': 49},  
'id': 'call\_VKw8t5tpAuzvbHgdAXe9mjUx'}\]

My output:  
\[{'name': 'multiply', 'ar
gs': {'a': 3, 'b': 12}, 'id': 'call\_7lwm1rk1b7IYSzwxeyIvhRI9'}\]
```
---

     
 
all -  [ spacy SpanCat for address parsing
 ](https://www.reddit.com/r/nlp_knowledge_sharing/comments/1dzp68o/spacy_spancat_for_address_parsing/) , 2024-07-12-0911
```
Hey all, I'm working on a project to standardize/normalize address data using spacy-llm spacy.SpanCat.v3. I plan to trai
n the model with examples of correctly labeled addresses to help it automatically correct a dataset filled with inconsis
tently formatted addresses. My main-address column is divided into \['NAME', 'STREET', 'BUILDING', 'LOCALITY', 'SUBAREA'
, 'AREA', 'CITY'\]

There are wrong addresses in format like City, area, name, street, building and other various cases 
which i need to handle as well. My end-goal is that i will give input txt to the model and it will normalize all the add
resses and split them into appropriate labels accordingly as well.

Has anyone here worked on something similar or used 
spacy-LLM for address parsing or something like seperating entities and formatting them? I'd appreciate any insights or 
tips on setting this up effectively. Also, how do i use the langchain/Ollama models. Im not interested in using prodigy 
:3 

Anyyyyyy help would be appreciated!
```
---

     
 
all -  [ Resume critique please ](https://www.reddit.com/r/resumes/comments/1dzp4bc/resume_critique_please/) , 2024-07-12-0911
```
https://preview.redd.it/3ci6doh71nbd1.png?width=590&format=png&auto=webp&s=640a7bf91ece79e1fcd5e32d671a4e61e4c2496a

loo
king for swe intern as a second-year ucsb student! Any help is greatly appreciated!
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-12-0911
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-12-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-12-0911
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-12-0911
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

     
