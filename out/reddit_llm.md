 
all -  [ Optimizing ollama for Mixtral 8X7B on MacBook Pro M1 Pro ](https://www.reddit.com/r/LocalLLaMA/comments/1ae9fju/optimizing_ollama_for_mixtral_8x7b_on_macbook_pro/) , 2024-01-30-0909
```
Hello /r/LocalLLaMA

I am looking for some guidance on how to best configure ollama to run Mixtral 8X7B on my Macbook Pr
o M1 Pro 32GB. I am able to run dolphin-2.5-mixtral-8x7b.Q4\_K\_M in LM Studio with the model loaded into memory if I in
crease the wired memory limit on my Macbook to 30GB. However, when I try use mixtral through the langchain ollama client
 for node, ollama defaults to cpu inference and it takes so long thinking about the prompt that it's unusable. In LM stu
dio my inference speed is about 18 tok/s. I have tested with dolphin-2.5-mixtral Q4\_K\_M from TheBloke's huggingface, a
nd mixtral-8x7b-text-v0.1-q4\_K\_M from the ollama library.   


Just now I tried to run each of those models using the 
ollama CLI to make sure it's not my app (it's been working fine with both Mistral 7B locally and the OpenAI client), and
 both models also are not using GPU inference when run from the terminal. I said 'Hello' and they both hallucinated resp
onses, one in Korean about the vote to ban sexual alliance, and the other a user query about how to package fonts for ad
obe illustrator. 

I know ollama is supposed to be optimized for Apple Silicon out of the box, but is there any configur
ation I can do to force it to load the model into memory?  Is there a better integration I could be using for langchain?
 I'm only using ollama because that's what was in the docs. 
```
---

     
 
all -  [ Free internet research tools? ](https://www.reddit.com/r/LangChain/comments/1ae7y59/free_internet_research_tools/) , 2024-01-30-0909
```
Are there any research tools available to do research on the internet for free? Has anyone had any good or bad experienc
es with this type of task?
```
---

     
 
all -  [ Searching Youtube with Langchain Tools + Streamlit ](https://jdsemrau.substack.com/p/searching-youtube-with-langchain) , 2024-01-30-0909
```

```
---

     
 
all -  [ RAG for documents with chapters and sub-chapters ](https://www.reddit.com/r/LangChain/comments/1ae3urf/rag_for_documents_with_chapters_and_subchapters/) , 2024-01-30-0909
```
I want to implement RAG for a 100 pages document that has a hierarchical structure of chapters, sub-chapters, etc. There
fore I chunk the document into smaller paragraphs. In many cases, a chunk within a sub-chapter makes only sense in the c
ontext of the title of the sub-chapter, e.g. (6.1 Method ABC, 6.1.1 Disadvantages).

I wonder what are the most common a
pproaches in RAG to handle hierarchical structures, which are very common in longer documents?
```
---

     
 
all -  [ I created a python tool to easily load repos, docs or papers into an LLM ](https://www.reddit.com/r/ChatGPTPro/comments/1ae36zt/i_created_a_python_tool_to_easily_load_repos_docs/) , 2024-01-30-0909
```
 It's run from the command line and accepts as input:

* GitHub repository URL (e.g., [https://github.com/jimmc414/1file
llm](https://github.com/jimmc414/1filellm))
* ArXiv abstract URL (e.g., [https://arxiv.org/abs/2401.14295](https://arxiv
.org/abs/2401.14295))
* Local folder repo path (e.g., C:\\python\\PipMyRide)
* Webpage URL (e.g., [https://llm.datasette
.io/en/stable/](https://llm.datasette.io/en/stable/))

It outputs two text files and shows the token counts for both to 
the console.

* uncompressed\_text.txt is all text from the selection as it is written. It also includes a simple header
 message explaining where the text following originated. This text file is automatically written to the working director
y and copied into the clipboard for ease pasting into an LLM.
* compressed\_text.txt is all text from the selection with
 all stopwords and whitespace removed as well as converting to lowercase to lower token usage.

[https://github.com/jimm
c414/1filellm](https://github.com/jimmc414/1filellm)

&#x200B;

https://preview.redd.it/2kvh066zfffc1.png?width=1925&for
mat=png&auto=webp&s=044c94fc73bb6dd1c535728eb639066a1ac140a7
```
---

     
 
all -  [ How to Install LangChain ](https://www.reddit.com/r/ArtificialInteligence/comments/1ae263u/how_to_install_langchain/) , 2024-01-30-0909
```
LangChain is an open source conversational AI assistant created by Anthropic. It allows you to have natural language con
versations powered by large language models.  
  
Installing LangChain on your own machine takes just a few simple ste
ps.

https://www.successtechservices.com/how-to-install-langchain/
```
---

     
 
all -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-01-30-0909
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

     
 
all -  [ Integration of Supabase SSR Auth with Next.js 14 and MUI for Styling ](https://www.reddit.com/r/Supabase/comments/1ady2pp/integration_of_supabase_ssr_auth_with_nextjs_14/) , 2024-01-30-0909
```
Hello everyone,

I've put together a project that demonstrates a straightforward integration of Supabase's server-side r
endering authentication with Next.js 14, using Material-UI for styling. It's a basic setup intended to help those lookin
g to implement Supabase auth in a Next.js environment with an emphasis on simplicity.

**Key Aspects:**

* Uses Supabase
 for authentication.
* Implements server-side rendering in Next.js 14.
* Applies Material-UI for the styling component.


**Getting Started:**

The repository includes everything from setting up your Supabase and Next.js project to running t
he application. It covers:

* Setting up a Supabase account and a Next.js project.
* Detailed installation instructions.

* Configuring your database and environment variables for the project.

**Purpose of the Project:**

This project aims 
to provide a simple example of integrating Supabase's authentication with Next.js's server-side rendering capabilities, 
using Material-UI for a bit of styling. It's meant to be a starting point for anyone looking to explore these technologi
es together.

**Looking for Feedback:**

I’m interested in any suggestions or contributions to make this integration exa
mple more helpful for developers starting with Supabase and Next.js. You can find the project here: [GitHub - SupabaseAu
thWithSSR](https://github.com/ElectricCodeGuy/SupabaseAuthWithSSR).

Feel free to check out the project and share your t
houghts or questions.

&#x200B;

**Question:**

I'm considering putting together a tutorial on using LangChain and OpenA
I's ChatGPT model for building a chat application, with Redis handling the conversation storage. This setup aims to demo
nstrate a practical application of AI and efficient data storage. Would this be of interest, or are there specific aspec
ts of integrating these technologies you'd like to explore? Feedback and suggestions are welcome.
```
---

     
 
all -  [ good starting points for a new project involving chains of LLM operations ](https://www.reddit.com/r/LangChain/comments/1adxilw/good_starting_points_for_a_new_project_involving/) , 2024-01-30-0909
```
what are some good notebooks or repos that i could use to start playing around with a system that chains together multip
le operations including RAG operation?

i want in the end to have a system that does the following:

input -> enters som
e LLM that outputs another text -> retrieve some documents and output multiple different texts -> for each of the output
ted texts go through another LLM

i know it shouldn't be very complicated but i have a hard time getting started and i d
on't see anything that does that but I'm sure it exists.  


specifically, i don't see anywhere an example of a chain th
at passes the output of an LLM as the input to another LLM instance
```
---

     
 
all -  [ Why does it seem prompt testing is hard? Is it data formatting? Or the actual testing? ](https://www.reddit.com/r/LangChain/comments/1adx6ny/why_does_it_seem_prompt_testing_is_hard_is_it/) , 2024-01-30-0909
```
I can write the code, but it seems all-over-the-place. Not very reusable.

I like my csv, but the world likes their json
s formatted in alpeca/openAI/mistral/(did I miss any?). 

When you do the final comparison between your model's output a
nd the correct answer, you are doing this in a dataframe/csv. 

When you run multiple rounds of prompt testings, I suppo
se I could flatten this each time. 

What does langchain do for this?
```
---

     
 
all -  [ LCEL - Citations chain with chat history ](https://www.reddit.com/r/LangChain/comments/1advsq8/lcel_citations_chain_with_chat_history/) , 2024-01-30-0909
```
Hey, I'm trying to use these two guides from the Langchain documentation:

\- [https://python.langchain.com/docs/use\_ca
ses/question\_answering/citations](https://python.langchain.com/docs/use_cases/question_answering/citations)

\- [https:
//python.langchain.com/docs/use\_cases/question\_answering/chat\_history](https://python.langchain.com/docs/use_cases/qu
estion_answering/chat_history)

 to create a chain that will return structured output with citations but also will accep
t chat\_history. 

Has anyone managed to create something similar using LCEL? 

&#x200B;
```
---

     
 
all -  [ ChatPromptTemplate keeps telling me I have 2 arguments ](https://www.reddit.com/r/LangChain/comments/1adu5e9/chatprompttemplate_keeps_telling_me_i_have_2/) , 2024-01-30-0909
```
I have qa pairs like 
```
# Example question-answer pairs
qa_pairs = [
    {'question': 'Who leads the rebellion in 'Ani
mal Farm'?', 'answer': 'The pigs, specially Snowball and Napoleon, leads the rebellion.'},
    {'question': 'What is the
 main theme of 'Animal Farm'?', 'answer': 'The main theme are the corruption of power.'},
    {'question': 'What happens
 to Boxer in the novel?', 'answer': 'Boxer is send to a slaughterhouse by the pigs.'}
]
```
Then I'm trying to iterate t
hem like 
```
def create_grading_prompt(qa_pair):
    return [
        ('system', 'You are a helpful AI bot. Your name i
s {name}.'),
        ('human', f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\n\nPlease grade the gramma
r of the answer based on the following rubric:\n{grammar_rubric}')
    ]

# Process each question-answer pair
for qa_pai
r in qa_pairs:
    grammar_and_grading_chain = SequentialChain([
        ChatPromptTemplate.from_messages(create_grading
_prompt(qa_pair)),
        llm,
        StrOutputParser()
    ])
    result = grammar_and_grading_chain.invoke(qa_pair)

    print(f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\nGrade: {result}\n')
```
throws
```
{
	'name': 
'TypeError',
	'message': 'Serializable.__init__() takes 1 positional argument but 2 were given',
	'stack': '------------
---------------------------------------------------------------
TypeError                                 Traceback (mos
t recent call last)
Cell In[6], line 9
      7 # Process each question-answer pair
      8 for qa_pair in qa_pairs:
----
> 9     grammar_and_grading_chain = SequentialChain([
     10         ChatPromptTemplate.from_messages(create_grading_pr
ompt(qa_pair)),
     11         llm,
     12         StrOutputParser()
     13     ])
     14     result = grammar_and_g
rading_chain.invoke(qa_pair)
     15     print(f\'Question: {qa_pair['question']}\
Answer: {qa_pair['answer']}\
Grade: {
result}\
\')

TypeError: Serializable.__init__() takes 1 positional argument but 2 were given'
}
```
because my previous
 try was throwing this same error.
My previous try
```
grammar_and_grading_chain = SequentialChain([
    ChatPromptTempl
ate(lambda qa_pair: f'Question: {qa_pair['question']}\nAnswer: {qa_pair['answer']}\n\nPlease grade the grammar of the an
swer based on the following rubric:\n{grammar_rubric}'),
    llm,
    StrOutputParser()
])


# Process each question-ans
wer pair
for qa_pair in qa_pairs:
    result = grammar_and_grading_chain.invoke(qa_pair)
    print(f'Question: {qa_pair[
'question']}\nAnswer: {qa_pair['answer']}\nGrade: {result}\n')
```
I looked at documentation here: https://api.python.la
ngchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#
and don't understand what I'm doing w
rong.
```
---

     
 
all -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-01-30-0909
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

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1adtarm/for_hire_programmerweb_developerit_consultant/) , 2024-01-30-0909
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $50/h.

Satisfied customers:

https://www.reddit.com/r/testimonia
ls/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsd
ze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_grea
t_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_hones
t_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https:/
/www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Please note: I am not a de
signer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Navigating a Career Comeback After a Break – Seeking Guidance and Opportunities! ](https://www.reddit.com/r/ADHD_Programmers/comments/1adr98l/navigating_a_career_comeback_after_a_break/) , 2024-01-30-0909
```
**TLDR:** After freelancing, I took a break due to mental health challenges, and now I'm struggling to re-enter the job 
market. Seeking advice on overcoming skill gaps, getting remote opportunities, and battling job market uncertainties.

*
*Introduction:**
Hey everyone,

I'm reaching out for guidance and support as I stand at a career crossroads. My journey 
in the tech industry includes experience in Machine Learning, remote subcontracting for a Fortune 10 company, and freela
ncing. However, unexpected life challenges led to a break for personal matters, including supporting ailing family membe
rs and constructing my house.

**Career Snapshot:**

- Sabbatical (1.5 years)

- **Machine Learning Consultant (1.5 year
s):**
  - Contributed to ML team's impact through effective MLOps implementation.
  - Developed a real-time liveness ser
vice with face detection, achieving low-latency performance.
  - Transitioned from individual notebooks to modularized s
cripts for a smoother development process.

- **Analytics ETL Engineer - Fortune 500 (Remote) (1.5 years) (Subcontractin
g):**
  - Automated In-Process Quality Control (IPQC) Audit, enhancing quality control.
  - Designed Tableau dashboards 
for dynamic manufacturing data, saving 200 hours weekly.

- **Internships in few MNC companies after college (1 year)**


**Break, Challenges, and ADHD Diagnosis:**
After a successful freelancing period, I took a break in June 2022 for menta
l health reasons. Recently diagnosed with ADHD, the inattentive subtype has posed significant challenges in my daily lif
e. Despite the productive break, returning to the industry has become daunting due to uncertainties in the job market an
d the struggle with skill gaps exacerbated by ADHD-related difficulties.

**Options and Seeking Guidance:**
- [x] Reache
d out to Previous clients and friends - No current opportunities.
- [ ] Considering applying to job portals for full-tim
e or contract jobs (Remote/Out of India).
- [ ] Exploring referrals but struggling with leetcode and revising Data Scien
ce concepts.
- [ ] Hesitant about gigs on freelancing platforms due to concerns about a race to the bottom.


**Neurodiv
ersity Hiring Programs in India:**
Considering my recent ADHD diagnosis, I'm contemplating whether to apply for hiring p
rograms for neurodivergent individuals, such as Microsoft's Neurodiversity hiring initiative in India. Any insights or a
dvice on this would be greatly appreciated.

**Seeking Advice:**
Am I being delusional to hope for a remote overseas job
 soon, given the current job market challenges? I'm open to any advice, insights, or recommendations on how to navigate 
this phase and make a successful comeback. I've shared my technical background and projects below to provide a comprehen
sive view.

**Skills:**

| **Skill Category**    | **Skills**                                                           
                                                                                                |
|---------------------
---|--------------------------------------------------------------------------------------------------------------------
---------------------------------------------------|
| Programming Languages  | Python                                  
                                                                                                                        
      |
| Visualization          | Tableau, Matplotlib, Folium                                                          
                                                                               |
| Operating Systems      | MacOS, Linux
 (Debian), Windows                                                                                                      
                               |
| Databases              | MySQL                                                       
                                                                                                         |
| DevOps/Tool
s           | CI/CD (GitHub Actions), Docker, Apache Airflow, Streamlit                                                 
                                                          |
| Other                  | Git, NLP, Scikit-Learn, TensorFlo
w, Cloud (GCP, AWS), Weights & Biases, Langchain, Sagemaker, Pandas, Numpy, Jupyter, DLib, OpenCV, Hydra                
               |

**Additional Personal Projects:**

| **Project**                                | **Description**     
                                                                                                                        
                       |
|--------------------------------------------|-------------------------------------------------
-------------------------------------------------------------------------------------------------------------------|
| I
mage Classification Telegram bot         | Developed an end-to-end image classification system with TensorFlow, deployed
 on Telegram. Improved F1 score by 20%, implemented MLOps workflow, and CI/CD pipeline.  |
| Object detection & classifi
cation Webapp  | Implemented object detection with TensorFlow and OCR using TesseractOCR. Deployed on Google Cloud Platf
orm, with a Streamlit front-end and Docker.                    |
| Idea Generation                            | Used Ope
nAI API for idea generation and Streamlit for pain point analysis.                                                      
                                      |
| Other Projects                             | Undertook diverse projects, inclu
ding a Pneumonia Prediction Dashboard, and facial landmark detection using various technologies and OpenAI.          |


**Conclusion:**
I appreciate your time in reading my story. If you have any advice, job leads, or can point me in the ri
ght direction, please feel free to share. I'm determined to make a successful comeback and contribute meaningfully to th
e tech community.

*Note: I made the decision to take a break after ensuring I had enough savings to survive. However, I
 never anticipated that depression would amplify the challenges posed by ADHD. I am honestly unsure how to seek help or 
ask for referrals.*

Thank you!
```
---

     
 
all -  [ Navigating a Career Comeback After a Break – Seeking Guidance and Opportunities! ](https://www.reddit.com/r/cscareerquestions/comments/1adqzx0/navigating_a_career_comeback_after_a_break/) , 2024-01-30-0909
```
**TLDR:** Started freelancing right after internship, took a break for personal reasons, and struggling to re-enter the 
job market. Seeking advice on overcoming skill gaps, getting remote opportunities, and battling job market uncertainties
.

**Introduction:** Hey everyone,

I'm reaching out to seek guidance and support as I find myself at a crossroads in my
 career. I'm from India & had a unique journey in the tech industry. I've gathered experience in Machine Learning, worke
d remotely as a subcontractor for a Fortune 10 company, and even ventured into freelancing. However, life threw some une
xpected challenges my way, and I had to take a break to attend to personal matters, including supporting an ailing famil
y member and constructing my house.

**Career Snapshot:**

* **Sabbatical (1.5 years)**
* **Machine Learning Consultant 
(1.5 years):**
   * As a Machine Learning Consultant, I played a key role in supporting and expanding the ML team's impa
ct across the company through effective MLOps implementation.
   * I created a real-time liveness service incorporating 
face detection, achieving remarkable low-latency performance.
   * To enhance efficiency, I facilitated a smoother devel
opment process by transitioning from individual notebooks to modularized scripts.
* **Analytics ETL Engineer - Fortune 5
00 (Remote) (1.5 years) (Subcontracting):**
   * Automated In-Process Quality Control (IPQC) Audit, enhancing quality co
ntrol.
   * Designed Tableau dashboards for dynamic manufacturing data, saving 200 hours weekly.
* **A few internships i
n MNC companies after college (1 year)**

**Break and Challenges:** After freelancing successfully, I took a break in Ju
ne 2022 to focus on my mental health. Despite the productive period, I'm now facing challenges getting back into the ind
ustry. I've explored different options, such as reaching out to previous clients, practicing DSA, and considering freela
ncing platforms. However, uncertainties about the job market and skill gaps are making the process daunting.

**Options 
and Seeking Guidance:**

\- \[x\] Reached out to Previous clients and friends - No current opportunities.

\- \[ \] Cons
idering applying to job portals for full-time or contract jobs (Remote/Out of India).

\- \[ \] Exploring referrals but 
struggling with leetcode and revising Data Science concepts.

\- \[ \] Hesitant about gigs on freelancing platforms due 
to concerns about a race to the bottom.

**Seeking Advice:** Am I being delusional to hope for a remote overseas job soo
n, given the current job market challenges? I'm open to any advice, insights, or recommendations on how to navigate this
 phase and make a successful comeback. I've shared my technical background and projects below to provide a comprehensive
 view.

**Skills:**

|**Skill Category**|**Skills**|
|:-|:-|
|Programming Languages|Python|
|Visualization|Tableau, Matp
lotlib, Folium|
|Operating Systems|MacOS, Linux (Debian), Windows|
|Databases|MySQL|
|DevOps/Tools|CI/CD (GitHub Actions
), Docker, Apache Airflow, Streamlit|
|Other|Git, NLP, Scikit-Learn, TensorFlow, Cloud (GCP, AWS), Weights & Biases, Lan
gchain, Sagemaker, Pandas, Numpy, Jupyter, DLib, OpenCV, Hydra|

**Additional Personal Projects:**

|**Project**|**Descr
iption**|
|:-|:-|
|**Image Classification Telegram bot**|Developed an end to end image classification system with Tensor
Flow, deployed on Telegram. Improved F1 score by 20%, implemented MLOps workflow, and CI/CD pipeline.|
|**Object detecti
on & classification Webapp**|Implemented object detection with TensorFlow and OCR using TesseractOCR. Deployed on Google
 Cloud Platform, with a Streamlit front-end and Docker.|
|**Idea Generation**|Used OpenAI API for idea generation and St
reamlit for pain point analysis.|
|**Other Projects**|Undertook diverse projects, including a Covid-19 X-ray Prediction 
Dashboard, MyCryptoPal, and facial landmark detection using various technologies and OpenAI.|

**Conclusion:** I appreci
ate your time in reading my story. If you have any advice, job leads, or can point me in the right direction, please fee
l free to share. I'm determined to make a successful comeback and contribute meaningfully to the tech community.

Thank 
you!
```
---

     
 
all -  [ Speed up Agents ](https://www.reddit.com/r/LangChain/comments/1adqrwj/speed_up_agents/) , 2024-01-30-0909
```
Hi everybody!

I'm currently developing some agents on Langchain for many purpose.
Some are just documents analysis or d
ata extraction from documents, and other are more Chatbot Rag based
The first category are not really agents, they are r
efine chain (a bit modified from the LCEL turo one) + stuff one
And the second is Langchain Agents (ZeroShotPrompt)

Bot
h run with GPT4

But here is the thing :

For the first category, as the pdf can goes to 5 to 20 pages, my agents take s
everal minutes to handle them
Also, I remarqued that the more I put a defined structure in the prompt to extracr informa
tion, the more it is long (can go up to 10min)

And for the second category, as there is a multi query retrieval Generat
ion based on pinecone, it also take 1 min  before generation.

I look for conceptual way to explain that.
We see a lot o
f agent out there which are more fast 

- is it the framework Langchain that slow down everything?
- is I had a local mo
del would it be faster ?
- is because of the Rag too complex?
- how could I drastically shorten my prompt but keeping cl
ear schema for data extraction?


Thanks you all for your help !
```
---

     
 
all -  [ Language switching for tools ](https://www.reddit.com/r/Langchaindev/comments/1adpwif/language_switching_for_tools/) , 2024-01-30-0909
```
I'm trying to use langchain with GPT for a search tool. The search database query has a language code (en or zh) and whe
n the tool is used, the language code is determined from the user query.

How can I get langchain to run the tool twice 
- in all available language codes translating the user query when necessary and compare the search content and get the m
ost appropriate one before returning an answer? 

Does this need to be done via the prompt or a more programmatic approa
ch?
```
---

     
 
all -  [ Anukool: My job hunting assistant ](https://www.reddit.com/r/opensource/comments/1adpfah/anukool_my_job_hunting_assistant/) , 2024-01-30-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. Consequently, I developed Anu
kool under the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as 
well. Since I'm new to ML and LLM, any advice or feedback is greatly appreciated, and contributions are also welcome. I 
plan to utilize Llama-2 soon to further open-source the project.

Check out the GitHub link, and please star it if you f
ind the project interesting: https://github.com/dakshesh14/anukool
```
---

     
 
all -  [ Chat UI with RAG ](https://www.reddit.com/r/OpenAI/comments/1adfira/chat_ui_with_rag/) , 2024-01-30-0909
```
is there a website or tool that lets you chat with pdfs or other text files like chatgpt? Unfortunately Librechat can't 
do this as far as I know or at least not yet. And I mean not chat with pdfs websites, I want a normal chat interface tha
t also is able to interact with pdfs if needed, and I'd like to use my own API key.

I was thinking trying to build some
thing like this myself but it's not that easy. You'd need some sort of agent that is called when asked. That whole langc
hain framework got annoyingly clustered with functions..
 
thanks
```
---

     
 
all -  [ Looking for a production level vector db ](https://www.reddit.com/r/LangChain/comments/1adf3o6/looking_for_a_production_level_vector_db/) , 2024-01-30-0909
```
Im looking for a production level vector db, so I was thinking about plain pg + pgvector, the problem is that I can't fi
nd an easy way of finding a good library to interact with it, so far I'm using raw queries like this (i will leave code 
at the bottom). I don't know if this is the best way apart from chroma, weaviate, pinecone, etc etc this is going to be 
at production level por mi company to be used internally.  
WITH vector\_matches AS (  
SELECT document\_id, 1 - (embedd
ing <=> %s) AS similarity  
FROM documents\_embeddings  
WHERE 1 - (embedding <=> %s) > %s  
ORDER BY similarity DESC  

LIMIT %s  
)  
SELECT d.page\_content, d.metadata, d.file\_id, vm.similarity  
FROM documents d  
INNER JOIN vector\_mat
ches vm ON d.id = vm.document\_id  


&#x200B;
```
---

     
 
all -  [ HackerNews AI built using function calling ](https://www.reddit.com/r/LangChain/comments/1adarpa/hackernews_ai_built_using_function_calling/) , 2024-01-30-0909
```
Hi reddit, I built an AI that can interact with the Hacker News API: [https://hn.aidev.run](https://hn.aidev.run)

You c
an ask questions like:

* What's on hackernews about AI?
* What's on hackernews about iPhone?
* What's trending on hacke
rnews?
* What are users showing on hackernews?
* What are users asking on hackernews?
* Summarize this story: [https://n
ews.ycombinator.com/item?id=39156778](https://news.ycombinator.com/item?id=39156778)

It uses function calling to query 
the HN api.

To answer questions about a particular topic, it’ll search its knowledge base (a vector db that is periodic
ally updated with the “top stories”) and get details about those stories from the API.

This is pretty barebones and I b
uilt it today in < 2 hours, so it probably won’t meet your high standards. If you give it a try, I’d love your feedback 
on how I can improve it.

If you’re interested, I built this using [phidata](https://github.com/phidatahq/phidata)

Than
ks for reading and would love to hear what you think.
```
---

     
 
all -  [ Why separate langchain and langchain_core for python package ](https://www.reddit.com/r/LangChain/comments/1ad9x8c/why_separate_langchain_and_langchain_core_for/) , 2024-01-30-0909
```
Hey, I'm trying to familiarize myself with the internals of the langchain python package, I noticed that langchain and l
angchain\_core are separated and in the internal code they have similar sub packages. my question is what is the need fo
r this separation and what is the thought process behind what should be implemented in langchain vs langchain\_core. Tha
nks
```
---

     
 
all -  [ What is the best on-prem vector db ](https://www.reddit.com/r/LangChain/comments/1ad52as/what_is_the_best_onprem_vector_db/) , 2024-01-30-0909
```
I'm building an app using LangChain to integrate with ChatGPT. I need a vector DB to store the embeddings. I want to use
 an on-prem option, not a cloud one. There are quite a few options I see from my searches. Wondering what folks would re
commend. Thanks.
```
---

     
 
all -  [ Use HTML splitter for JSX (React) code? ](https://www.reddit.com/r/LangChain/comments/1ad4eye/use_html_splitter_for_jsx_react_code/) , 2024-01-30-0909
```
I am creating a chatbot over the data of my **static React website**.

I fetch the page files from the file system using
 the [DirectoryLoader](https://js.langchain.com/docs/modules/data_connection/document_loaders/file_directory). I could u
se a web loader but I want it to work even in local development.

The issue is the text splitter.

I couldn't find a pro
per text splitter for JSX (React) code. But I seem to get decent results with the [HTML recursive text splitter](https:/
/js.langchain.com/docs/modules/data_connection/document_transformers/code_splitter#html), probably because JSX and HTML 
are so similar.

Before I send my documents to the HTML splitter, I **remove all import statements and class names** (to
 get rid of the unnecessary clutter). I keep everything else (which might include some JavaScript code).

Is my approach
 fine? Is the HTML splitter suited for this use case? Is it normal that there is no text overlap in the generated docume
nts?
```
---

     
 
all -  [ Streamlit run app.py - blank screen help ( vscode) - OpenAI chat bot project ](https://youtu.be/x0AnCE9SE4A?si=Yb1LMCiz5AJ1RE7E) , 2024-01-30-0909
```
Hello, I'm a newbie programmer and having mind boggling issue of my app not deploying...it is a chat bot...everything se
ems to be fine just the error was Inport error: Openai can't be imported from langchain. I don't know..have scoured the 
internet for the fixes, but unable to find a solution.

Saw a tutorial from free coding camp on YouTube and it seems to 
work in that tutorial. I followed step by step even checked multiple times.

If someone can help me find out what is wro
ng I will be very grateful.

It may be a simple thing or complex I don't know as I don't have a 360 degree understanding
 of python libraries or streamlit requirements. I followed the tutorial 100% though. I can say that.

I reached 1:14:00 
in the video
```
---

     
 
all -  [ Streamlit run app.py - blank screen help ( vscode) - OpenAI chat bot project ](https://youtu.be/x0AnCE9SE4A?si=8J46bJ3WXX-w0xf9) , 2024-01-30-0909
```
Hello, I'm a newbie programmer and having mind boggling issue of my app not deploying...it is a chat bot...everything se
ems to be fine just the error was openai can't be imported from langchain. I don't know ..have scoured the internet for 
the fixes, but unable to find a solution. 

Saw a tutorial from free coding camp on YouTube and it seems to work in that
 tutorial. I followed step by step even checked multiple time.

If someone can help me find out what is wrong I will be 
very grateful. 

It may be a simple thing or complex I don't know as I don't have a 360 degree understanding of python l
ibraries or streamlit requirements. I followed the tutorial 100% though. I can say that.

I reached 1:14:00 in the video

```
---

     
 
all -  [ Is there any git dedicated for text-to-SQL to be inference on local LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/1ad26zr/is_there_any_git_dedicated_for_texttosql_to_be/) , 2024-01-30-0909
```
I am trying to find a method to use local LLM for queries and use it for RAG purposes as well as text-to-SQL purposes. L
angChain SQL agent doesn’t work well with the local models.. so trying to find if there is any git that can help me solv
e this issue
```
---

     
 
all -  [ Qdrant DB: Payload Limit Exceeded Error ](https://www.reddit.com/r/LangChain/comments/1ad0vvg/qdrant_db_payload_limit_exceeded_error/) , 2024-01-30-0909
```
I am trying to store Langchain Documents in the qdrant database(docker). When I try storing them in the db. I am getting
 this error. Please help me solve this.

&#x200B;

UnexpectedResponse: Unexpected Response: 400 (Bad Request)

Raw respo
nse content:

b'{'status':{'error':'Payload error: JSON payload (46866880 bytes) is larger than allowed (limit: 33554432
 bytes).'},'time':0.0}'
```
---

     
 
all -  [ Is there a reranking example with Langchain? ](https://www.reddit.com/r/LangChain/comments/1acywew/is_there_a_reranking_example_with_langchain/) , 2024-01-30-0909
```
I want to rerank my retrieved documents but couldn't find an example on Langchain. Ant pointers would help. (not looking
 for context compression)
```
---

     
 
all -  [ Best Practices for Semantic Search on 200k vectors (30GB) Worth of Embeddings? ](https://www.reddit.com/r/LangChain/comments/1acxxbw/best_practices_for_semantic_search_on_200k/) , 2024-01-30-0909
```
Hi, I have converted some domain-specific name vectors into embeddings, with a dataset size of 200k words. All the embed
dings were generated using OpenAI's embedding model 3 (3072 dim per embedding) . Now I am planning to implement semantic
 search similarity. Given a domain keyword, I want to find the top 5 most similar matches. After embedding all 280k word
s, the size of the JSON file containing the embeddings is around 30GB.

I am new to this domain and evaluating the best 
options.

1. Should I use a cloud vector database like Pinecone or Typsense, or host locally on DigitalOcean?
2. If I go
 with a cloud option like Typsense, what configuration (RAM, etc.) would I need for 280k embeddings (30GB in size)? And 
how much would it likely cost?

I have been confused for the past few days and unable to find useful resources. Any help
 or advice you could provide would be greatly appreciated.
```
---

     
 
all -  [ Efficient Chunking Strategies for PDF Information Extraction with AI Tools ](https://www.reddit.com/r/LangChain/comments/1acudx2/efficient_chunking_strategies_for_pdf_information/) , 2024-01-30-0909
```
 Hello,

I'm working on extracting information from PDFs containing tables using OpenAI, LangChain, and FAISS. My focus 
is on extracting value especially regarding specific keywords present in these documents. I'm looking for advice on opti
mal chunking strategies for these PDFs to ensure comprehensive information extraction without losing key details. Any in
sights or best practices would be greatly appreciated!

Thank you!
```
---

     
 
all -  [ LangChain Blog on AI mental health therapy ](https://www.reddit.com/r/LangChain/comments/1acou6m/langchain_blog_on_ai_mental_health_therapy/) , 2024-01-30-0909
```
Nice blog article about how to build an AI therapist with LangChain: [https://blog.langchain.dev/mental-health-therapy-a
s-an-llm-state-machine/](https://blog.langchain.dev/mental-health-therapy-as-an-llm-state-machine/)
```
---

     
 
all -  [ Most capable function calling open source models? ](https://www.reddit.com/r/LocalLLaMA/comments/1ackxxt/most_capable_function_calling_open_source_models/) , 2024-01-30-0909
```
we've had a myriad of impressive tools and projects developed by talented groups of individuals which incorporate functi
on calling and give us the ability to create custom functions as tools that our ai models can call, however it seems lik
e they're all entirely based around openai's chatgpt function calling.

my question is what open source models are you a
ware of that are consistently capable of recognizing when they have a function tool available and actually call them pro
perly?

i'd like to make more effective use of things like memgpt, autogen, langroid, langchain, gorilla, and a number o
f other great projects but i want to make sure i'm not wasting my time using models that aren't good at function calling
.

**Edit:** Adding models and links to them as I discover them or others recommend them so that people can easily find 
this info in one place. These are links to the original models by their original authors. In the case of unquantized mod
els for quantized versions look for these models quantized by your favorite huggingface uploaders.

Described best by /u
/SatoshiNotMe

>With tools/function-calling, it's good to distinguish two levels of difficulty:  
>  
>ONCE: one-off too
l calling: a single-round interaction where an LLM must generate a funtion-call given an input. This could be used for e
xample in a pipeline of processing steps, e.g. use LLM to identify sensitive items in a passage via a function call, wit
h output showing a list of dicts containing sensitive item, sensitive category. You could use this as one step in a mult
i-step (possibly batch) pipeline  
>  
>MULTI: in a multi-round conversation with a user (or another Agent), the LLM nee
ds to distinguish between several types of 'user' msgs it needs to respond to:user message that doesn't need a tooluser 
msg that needs a tool/fn-call responseresult of a fn-callerror from an attempted fn-call (e.g. Json/Pydantic validation 
err), or reminder about a forgotten fn-call

&#x200B;

* [Dolphin-2.7-mixtral-8x7b](https://huggingface.co/cognitivecomp
utations/dolphin-2.7-mixtral-8x7b) \- Multi
* [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Ins
truct-v0.2) \- Single
* [NexusRaven-V2-13B](https://huggingface.co/Nexusflow/NexusRaven-V2-13B) \- Single
* [Functionary
-small-v2.2-GGUF](https://huggingface.co/meetkai/functionary-small-v2.2-GGUF) \- Multi
* [Functionary-medium-v2.2-GGUF](
https://huggingface.co/meetkai/functionary-medium-v2.2-GGUF) \- Multi
* [natural-functions-GGUF](https://huggingface.co/
cfahlgren1/natural-functions-GGUF) \- Multi
```
---

     
 
all -  [ Singlestore Zoom call reviews ](https://www.reddit.com/r/dataengineering/comments/1aciszo/singlestore_zoom_call_reviews/) , 2024-01-30-0909
```


I’m sorry to be mean , but offlate some of the weekly zoom calls have really bad speakers . There is a guy who wears B
lippi glasses and when asked questions , he says the tutorial is in progress and asks the audience to follow his LinkedI
n profile . It sounds more like he is interested in getting followers rather than he knowing the subject . I doubt he kn
ows things about langchain, llama index , etc , when asked about it , he gives a nod and lame smile . These zoom calls w
ere excellent when Akmal ran the show . I never missed Akmal’s calls. Nowadays I get out of the call when that blippi jo
ins . 
#singlestore #weeklycalls
```
---

     
 
all -  [ Has anyone found a ChatGPT plugin that's better than web pilot or vox script at reading external con ](https://www.reddit.com/r/LLMs/comments/1achfsl/has_anyone_found_a_chatgpt_plugin_thats_better/) , 2024-01-30-0909
```
 

I use webpilot and vox script all the time and wondering if some people prefer something else.

I especially like bot
h because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with Bing can't be relie
d on to do it consistently.

I have some examples in this article I generated.  
[https://www.learninternetgrow.com/real
-time-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)
```
---

     
 
all -  [ Has anyone found a ChatGPT plugin that's better than web pilot or vox script at reading external con ](https://www.reddit.com/r/OpenAI/comments/1achf51/has_anyone_found_a_chatgpt_plugin_thats_better/) , 2024-01-30-0909
```
 I use webpilot and vox script all the time and wondering if some people prefer something else.

I especially like both 
because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with Bing can't be relied 
on to do it consistently.

I have some examples in this article I generated.  
[https://www.learninternetgrow.com/real-t
ime-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)  


Alternatively, looking for exa
mples where someone recreates this functionality in langchain.
```
---

     
 
all -  [ Has anyone found an example of coupling LangChain with external URL requests? ](https://www.reddit.com/r/LangChain/comments/1achbg7/has_anyone_found_an_example_of_coupling_langchain/) , 2024-01-30-0909
```
 

I use webpilot and vox script all the time and wondering if there are examples of achieving this with LangChain.

I e
specially like both because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with B
ing can't be relied on to do it consistently.

I have some examples in this article I generated.  
[https://www.learnint
ernetgrow.com/real-time-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)  
 
```
---

     
 
all -  [ Query CSV code not working help! ](https://www.reddit.com/r/LangChain/comments/1aceuxq/query_csv_code_not_working_help/) , 2024-01-30-0909
```
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    from langchain.documen
t_loaders import CSVLoader
    from langchain.vectorstores import DocArrayInMemorySearch
    from IPython.display import
 display, Markdown
    from langchain.llms import OpenAI
    
    file = 'OutdoorClothingCatalog_1000.csv'
    loader = 
CSVLoader(file_path=file)
    print(loader)
    
    from langchain.indexes import VectorstoreIndexCreator
    
    inde
x = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])
    
    query 
='Please list all your shirts with sun protection \
        in a table in markdown and summarize each one.'
    
    fro
m langchain_openai import ChatOpenAI
    
    model_name = 'gpt-3.5-turbo-instruct'
    llm_replacement_model = ChatOpen
AI(temperature=0.0, model=model_name, openai_api_key=openai.api_key)
    response = index.query(query, llm=llm_replaceme
nt_model
    

&#x200B;

&#x200B;

    ---------------------------------------------------------------------------
    V
alidationError                           Traceback (most recent call last)
    Cell In[22], line 5
          3 model_nam
e = 'gpt-3.5-turbo-instruct'
          4 llm_replacement_model = ChatOpenAI(temperature=0.0, model=model_name, openai_ap
i_key=openai.api_key)
    ----> 5 response = index.query(query, llm=llm_replacement_model)
    
    File ~/.pyenv/versio
ns/3.12.0/lib/python3.12/site-packages/langchain/indexes/vectorstore.py:46, in VectorStoreIndexWrapper.query(self, quest
ion, llm, retriever_kwargs, **kwargs)
         42 retriever_kwargs = retriever_kwargs or {}
         43 chain = Retrieva
lQA.from_chain_type(
         44     llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        
 45 )
    ---> 46 return chain.run(question)
    
    File ~/.pyenv/versions/3.12.0/lib/python3.12/site-packages/langcha
in_core/_api/deprecation.py:145, in deprecated.<locals>.deprecate.<locals>.warning_emitting_wrapper(*args, **kwargs)
   
     143     warned = True
        144     emit_warning()
    --> 145 return wrapped(*args, **kwargs)
    
    File ~/.p
yenv/versions/3.12.0/lib/python3.12/site-packages/langchain/chains/base.py:538, in Chain.run(self, callbacks, tags, meta
data, *args, **kwargs)
        536     if len(args) != 1:
        537         raise ValueError('`run` supports only one 
positional argument.')
    --> 538     return self(args[0], callbacks=callbacks, tags=tags, metadata=metadata)[
        
539         _output_key
        540     ]
    ...
      Field required [type=missing, input_value={'embedding': [0.00682
570..., -0.02392816262769903]}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.5/v
/missing
    metadata
      Field required [type=missing, input_value={'embedding': [0.00682570..., -0.02392816262769903
]}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.5/v/missing

&#x200B;

&#x200B;


Help, this is from a course I'm taking on Deep learning
```
---

     
 
all -  [ How do i merge / combine two texts into one? ](https://www.reddit.com/r/LangChain/comments/1acbcqn/how_do_i_merge_combine_two_texts_into_one/) , 2024-01-30-0909
```
I am a noob experimenting with LLMs and i am looking for a reliable method for merging / combining two texts into one cr
edible sounding merged text. Does that take a langchain based RAG or am i simply too stupid to engineer the right prompt
 in a mixtral or something similar? :)
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-30-0909
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-30-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-30-0909
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-30-0909
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-30-0909
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-30-0909
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-30-0909
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

     
