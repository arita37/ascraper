 
all -  [ Do I need to pay for unit test with langsmith library? ](https://www.reddit.com/r/LangChain/comments/1g33fsy/do_i_need_to_pay_for_unit_test_with_langsmith/) , 2024-10-14-0913
```
Pretty simple question I think?

I was reading the following:

[https://docs.smith.langchain.com/how\_to\_guides/evaluat
ion/unit\_testing](https://docs.smith.langchain.com/how_to_guides/evaluation/unit_testing)

But I don't get if I need to
 use the LangSmith web app to see the results or I can simply use the langsmith library to run my unit tests and get the
 results without the tracing.. Is this doable?

Is the use of the web app mandatory? Or langsmith can be used solely as 
a library without the tracing?

Thank you in advance!
```
---

     
 
all -  [ Which framework between haystack, langchain and llamaindex, or others? ](https://www.reddit.com/r/Rag/comments/1g31urm/which_framework_between_haystack_langchain_and/) , 2024-10-14-0913
```
The use case is the following.
Database: vector database with 10k scientific articles.
User needs: the user will need th
e chatbot both for advanced research on the dataset and chat with those results. 

Please let me know your advices!! 
```
---

     
 
all -  [ [Hiring][Remote] Software Engineer ](https://www.reddit.com/r/jobbit/comments/1g31h8x/hiringremote_software_engineer/) , 2024-10-14-0913
```
* Full-time opportunity
* Remote
* Compensation - $125k - $190k
* 4+ years of experience
* Experience with one or more o
f the following areas (or related technologies): 
   * Modern web/backend technologies: React, Typescript, Node, Next, P
ython
   * AI techniques and workflows: LLMs, RAG, Langchain, CoreML
   * Mobile development: Flutter (Dart), iOS (Swift
), Android (Kotlin)
   * Cloud platforms/infrastructure: GCP, AWS, Azure, Docker
   * Databases: Relational (PostgreSQL,
 MySQL) or Non-relational (MongoDB, Firestore)

Apply - [https://peerlist.io/company/squint/careers/software-engineer/jo
bhkknpn86qnjqbk2jaqlrngdperq](https://peerlist.io/company/squint/careers/software-engineer/jobhkknpn86qnjqbk2jaqlrngdper
q)
```
---

     
 
all -  [ [Hiring][Remote] Software Engineer ](https://www.reddit.com/r/RemoteJobHunters/comments/1g31erw/hiringremote_software_engineer/) , 2024-10-14-0913
```
* Full-time opportunity
* Remote 
* Compensation - $125k - $190k
* 4+ years of experience
* Experience with one or more 
of the following areas (or related technologies): 
   * Modern web/backend technologies: React, Typescript, Node, Next, 
Python
   * AI techniques and workflows: LLMs, RAG, Langchain, CoreML
   * Mobile development: Flutter (Dart), iOS (Swif
t), Android (Kotlin)
   * Cloud platforms/infrastructure: GCP, AWS, Azure, Docker
   * Databases: Relational (PostgreSQL
, MySQL) or Non-relational (MongoDB, Firestore)

Apply - [https://peerlist.io/company/squint/careers/software-engineer/j
obhkknpn86qnjqbk2jaqlrngdperq](https://peerlist.io/company/squint/careers/software-engineer/jobhkknpn86qnjqbk2jaqlrngdpe
rq)
```
---

     
 
all -  [ Idea: Interest in a competition model to build agents for businesses ](https://www.reddit.com/r/LangChain/comments/1g2zpr3/idea_interest_in_a_competition_model_to_build/) , 2024-10-14-0913
```
Imagine there was a platform whereby a business spec for a workflow (e.g. creating facebook ads) was understood.

Now le
ts assume the business who was interested in creating an agent for this commonly repeated workflow didn't have the resou
rces to do it and there wasn't a reasonable substitute already on the market.

The super simple spec might look somethin
g like:

* **Objective**: from a list of 100 ideas, create five 10s video variants from supplied Napkin Pitches for each
.
* **Constraints:**
   * At least 5 videos from the 500 created videos must pass a qualitative review and be selected
 
  * The total cost to me, the business, must be X or less
   * The total time to generate must be Y or less

Let's assum
e this business offers a $2000 prize for the winning submission (as judged by performance against the constraints) under
 a fixed contest length duration (e.g. 2 weeks). If you won, you'd secure the prize and your source code would be made a
vailable to the business + potentially made open for others to consume.

Without knowing more, if a platform and paradig
m like this existed, would you be interested in participating?
```
---

     
 
all -  [ All-In-One Tool for LLM Evaluation ](https://www.reddit.com/r/LangChain/comments/1g2z2q1/allinone_tool_for_llm_evaluation/) , 2024-10-14-0913
```
I was recently trying to build an app using LLMs but was having a lot of difficulty engineering my prompt to make sure i
t worked in every case. 

So I built this tool that automatically generates a test set and evaluates my model against it
 every time I change the prompt. The tool also creates an api for the model which logs and evaluates all calls made once
 deployed.

https://reddit.com/link/1g2z2q1/video/a5nzxvqw2lud1/player

Please let me know if this is something you'd fi
nd useful and if you want to try it and give feedback! Hope I could help in building your LLM apps!
```
---

     
 
all -  [ Extracting Regex Patterns from Strings - Trying to Think of Techniques to Improve ](https://www.reddit.com/r/LangChain/comments/1g2y6o4/extracting_regex_patterns_from_strings_trying_to/) , 2024-10-14-0913
```
Recently I've been working on a project that requires me to generate a ton of regex patterns from a large amount of stri
ngs. These strings can be in any form and may or may not have a pattern in them. An example of my use case would be tryi
ng to extract all of the names of people from a sentence. I need to generate both the name and the reusable regex patter
n required to extract the name in future strings. For example, in the string 'John Doe went to the store', the goal of t
he system would be to extract 'John Doe' with a regex pattern of '\^\\s\*John\\s+Doe'. The regex pattern just needs to b
e able to match to another sentence like 'I went to dinner with John Doe'. Both of those sentences would be able to be m
atched from the regex pattern generated from the first pattern.

There is a hidden complexity in that the sentence could
 be something like 'George walked his dog Max'. In this case, 'George' would be the desired extraction, rather than 'Max
'.

Right now, I am using two different LangChain functions to extract these patterns. One of them extracts the name wit
h some simple prompt engineering as well as a couple few-shot examples of names and sentences. The other generates the r
egex pattern with a similar approach of using some prompt engineering and few-shot examples.

The problem that I am havi
ng right now is that my accuracy has hit a ceiling. I am currently sitting at around 60% accuracy on the strings. Most o
f the strings are incredibly complex and either have a ton of noise, or they have multiple names and determining which o
ne is correct is non-trivial. Are there any techniques that could be used to help my use case?

Thanks for any help!
```
---

     
 
all -  [ Open-Source Embodied Agents from NASA/JPL ](https://youtu.be/mZTrSg7tEsA?si=r6_56O0O38lxQSaM) , 2024-10-14-0913
```
Hey r/robotics 👋

We recently shared a preprint of an upcoming IEEE article about ROSA: the Robot Operating System Agent
 (https://arxiv.org/abs/2410.06472).

ROSA works with ROS/ROS2 and popular language models like GPT-4o and Llama3.1 to m
ake it easy for humans to interact with robots using natural language. Check out the demo video to see what this new way
 of building and operating robots can do.

The project is open-source and can be easily added to existing ROS/ROS2 proje
cts. Just type ‘pip install jpl-rosa’ and you’ll be able to create an agent in a few lines of code. You can also customi
ze the agent with Robot System Prompts and your own custom tools using the LangChain standard for tool creation. There a
re lots of examples on the repository (https://github.com/nasa-jpl/rosa) and Wiki (https://github.com/nasa-jpl/rosa/wiki
).

We’d love to hear from you and are open to collaboration with the community. Let us know what you think!
```
---

     
 
all -  [ From Beginner to Problem-Solving Pro: The Ultimate Guide to Mastering Python ](https://www.reddit.com/r/BMSCE/comments/1g2qopn/from_beginner_to_problemsolving_pro_the_ultimate/) , 2024-10-14-0913
```


> If you want to become exceptional at something, you need the right guidance and a relentless focus on practice. Prob
lem-solving with Python is no different. Whether you're a beginner or already have some Python experience, here’s a dist
illed guide to the best resources that will take you from zero to hero.

---

**Interactive Platforms: Learn by Doing**

   - **LeetCode**: The go-to platform for sharpening your algorithmic skills. Problems range from easy to hard, perfect 
for anyone targeting tech interviews or leveling up their problem-solving skills. 
     - [Start Here](https://leetcode.
com/problemset/all/?difficulty=EASY&page=1&tag=python)
   
   - **HackerRank**: Solid for beginners, offering a well-str
uctured Python track. Good to build confidence before diving into harder challenges.
     - [Explore Python Track](https
://www.hackerrank.com/domains/tutorials/10-days-of-python)
   
   - **CodeSignal**: Ideal for those who want to challeng
e themselves with real-world coding tests and company-specific problems.
     - [Check it out](https://codesignal.com/)

   
   - **Codewars**: Solve community-created 'kata' and see how others think. A great way to learn different problem-s
olving techniques.
     - [Start solving](https://www.codewars.com/)

**The Best Courses: From Concept to Code**
   - **
'Python for Everybody' by University of Michigan on Coursera**: More than just Python basics, this course teaches you ho
w to think like a programmer.
     - [Enroll for Free](https://www.coursera.org/specializations/python)
   
   - **'Mast
ering Data Structures & Algorithms using Python' on Udemy**: Deep dive into solving complex problems with Python. Great 
if you want to understand the 'why' behind each solution.
     - [Course Link](https://www.udemy.com/course/python-for-d
ata-structures-algorithms-and-interviews/)
   
   - **MIT's 'Computational Thinking using Python' on EdX**: Not just cod
ing, but thinking like a computer scientist. Highly recommended for those who want to develop a strong foundation.
     
- [Learn More](https://www.edx.org/course/introduction-to-computer-science-and-programming-using-python)

**Essential Re
ads: From Beginner to Pro**
   - **'Python Programming: An Introduction to Computer Science' by John Zelle**: A clear an
d practical introduction to Python and problem-solving.
   - **'Automate the Boring Stuff with Python' by Al Sweigart**:
 Real-world examples make it easy to apply Python to everyday tasks.
   - **'Elements of Programming Interviews in Pytho
n'**: A no-nonsense guide to mastering interview-style problems.
   - **'Python Crash Course' by Eric Matthes**: Packed 
with hands-on exercises to quickly improve your coding and problem-solving.

**Tutorials & Blogs: Sharpen Your Edge**
  
 - **Real Python**: Clean, insightful tutorials on Python and algorithms. Great if you like to learn through reading.
  
   - [Visit Real Python](https://realpython.com/)
   
   - **GeeksforGeeks**: An extensive repository of problems, expla
nations, and Python solutions.
     - [Explore GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/
)
   
   - **LeetCode Discuss**: Community-driven solutions and problem-solving discussions, especially valuable for int
erview prep.
     - [Join the Community](https://leetcode.com/discuss/)

**YouTube: Bite-sized Mastery**
   - **Tech Wit
h Tim**: Problem-solving tutorials, coding challenges, and practical examples.
     - [Tech With Tim](https://www.youtub
e.com/c/TechWithTim)
   
   - **CS Dojo**: Easy-to-follow explanations of algorithms with Python.
     - [CS Dojo](https
://youtube.com/@csdojo?si=lMjat_rv-c9FPqHM) 
   
   - **Kite**: Quick tutorials focusing on coding challenges.
     - [K
ite on YouTube](https://youtube.com/@kitehq?si=YuqpJYwBGpUDi3pt) 

**Competitive Programming: Level Up Your Skills**
   
- **TopCoder**: For those who thrive on solving complex challenges against the clock.
     - [TopCoder Python Track](htt
ps://www.topcoder.com/)
   
   - **Codeforces**: Real-time contests that test your coding speed and efficiency.
     - [
Start Competing](https://codeforces.com/)
   
   - **Exercism.io**: Solve problems and get feedback from mentors—perfect
 if you value personal growth.
     - [Join Exercism](https://exercism.io/tracks/python)

**DSA Resources: Become Unstop
pable**
   - **NeetCode**: Curated problem sets and videos that make DSA simpler to understand.
     - [NeetCode Resourc
es](https://neetcode.io/)
   
   - **AlgoExpert**: If you can invest, this is gold. Get high-quality explanations and ch
allenges.
     - [Check out AlgoExpert](https://www.algoexpert.io/)
   
   - **'Introduction to Algorithms' (CLRS)**: A 
classic. Pair it with Python and tackle the hardest problems.

---

**The Truth About Mastery**: 
> 'Learning to solve p
roblems with Python is not just about syntax, it’s about developing a mind that can break down complexity into simplicit
y. The key is practice, consistency, and a hunger for real understanding.' 

You don’t need a hundred resources; you nee
d focus. Pick a few from this list and dive deep. You'll be amazed at what you can achieve.

---

This guide should be a
 helpful launchpad, whether you're aiming for coding interviews, leveling up for competitive programming, or just love s
olving problems. What’s your favorite resource? Drop your go-to recommendations below!


**Additional 🔗 to some of the l
atest Python libraries :**

- [Polars](https://www.pola.rs/)
- [DuckDB](https://duckdb.org/)
- [PyCaret](https://pycaret
.gitbook.io/docs/)
- [JAX](https://jax.readthedocs.io/en/latest/)
- [LangChain](https://github.com/hwchase17/langchain)

- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [Caffe2](https://caffe2.ai/)
- [Transformers (Hugging Face)](
https://github.com/huggingface/transformers)
- [PyOD](https://pyod.readthedocs.io/en/latest/)
- [Plotly](https://plotly.
com/python/)
- [Bokeh](https://docs.bokeh.org/en/latest/)
- [Pydot](https://github.com/pydot/pydot) 

These links provid
e documentation and details for each library, making it easier to explore and integrate them into your projects.
```
---

     
 
all -  [ Mastering Problem-Solving with Python: A Curated Path for the Driven ](https://www.reddit.com/r/DTU__Delhi/comments/1g2qebd/mastering_problemsolving_with_python_a_curated/) , 2024-10-14-0913
```


> If you want to become exceptional at something, you need the right guidance and a relentless focus on practice. Prob
lem-solving with Python is no different. Whether you're a beginner or already have some Python experience, here’s a dist
illed guide to the best resources that will take you from zero to hero.

---

**Interactive Platforms: Learn by Doing**

   - **LeetCode**: The go-to platform for sharpening your algorithmic skills. Problems range from easy to hard, perfect 
for anyone targeting tech interviews or leveling up their problem-solving skills. 
     - [Start Here](https://leetcode.
com/problemset/all/?difficulty=EASY&page=1&tag=python)
   
   - **HackerRank**: Solid for beginners, offering a well-str
uctured Python track. Good to build confidence before diving into harder challenges.
     - [Explore Python Track](https
://www.hackerrank.com/domains/tutorials/10-days-of-python)
   
   - **CodeSignal**: Ideal for those who want to challeng
e themselves with real-world coding tests and company-specific problems.
     - [Check it out](https://codesignal.com/)

   
   - **Codewars**: Solve community-created 'kata' and see how others think. A great way to learn different problem-s
olving techniques.
     - [Start solving](https://www.codewars.com/)

**The Best Courses: From Concept to Code**
   - **
'Python for Everybody' by University of Michigan on Coursera**: More than just Python basics, this course teaches you ho
w to think like a programmer.
     - [Enroll for Free](https://www.coursera.org/specializations/python)
   
   - **'Mast
ering Data Structures & Algorithms using Python' on Udemy**: Deep dive into solving complex problems with Python. Great 
if you want to understand the 'why' behind each solution.
     - [Course Link](https://www.udemy.com/course/python-for-d
ata-structures-algorithms-and-interviews/)
   
   - **MIT's 'Computational Thinking using Python' on EdX**: Not just cod
ing, but thinking like a computer scientist. Highly recommended for those who want to develop a strong foundation.
     
- [Learn More](https://www.edx.org/course/introduction-to-computer-science-and-programming-using-python)

**Essential Re
ads: From Beginner to Pro**
   - **'Python Programming: An Introduction to Computer Science' by John Zelle**: A clear an
d practical introduction to Python and problem-solving.
   - **'Automate the Boring Stuff with Python' by Al Sweigart**:
 Real-world examples make it easy to apply Python to everyday tasks.
   - **'Elements of Programming Interviews in Pytho
n'**: A no-nonsense guide to mastering interview-style problems.
   - **'Python Crash Course' by Eric Matthes**: Packed 
with hands-on exercises to quickly improve your coding and problem-solving.

**Tutorials & Blogs: Sharpen Your Edge**
  
 - **Real Python**: Clean, insightful tutorials on Python and algorithms. Great if you like to learn through reading.
  
   - [Visit Real Python](https://realpython.com/)
   
   - **GeeksforGeeks**: An extensive repository of problems, expla
nations, and Python solutions.
     - [Explore GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/
)
   
   - **LeetCode Discuss**: Community-driven solutions and problem-solving discussions, especially valuable for int
erview prep.
     - [Join the Community](https://leetcode.com/discuss/)

**YouTube: Bite-sized Mastery**
   - **Tech Wit
h Tim**: Problem-solving tutorials, coding challenges, and practical examples.
     - [Tech With Tim](https://www.youtub
e.com/c/TechWithTim)
   
   - **CS Dojo**: Easy-to-follow explanations of algorithms with Python.
     - [CS Dojo]( http
s://youtube.com/@csdojo?si=lMjat_rv-c9FPqHM) 
   
   - **Kite**: Quick tutorials focusing on coding challenges.
     - [
Kite on YouTube](https://youtube.com/@kitehq?si=YuqpJYwBGpUDi3pt) 

**Competitive Programming: Level Up Your Skills**
  
 - **TopCoder**: For those who thrive on solving complex challenges against the clock.
     - [TopCoder Python Track](ht
tps://www.topcoder.com/)
   
   - **Codeforces**: Real-time contests that test your coding speed and efficiency.
     - 
[Start Competing](https://codeforces.com/)
   
   - **Exercism.io**: Solve problems and get feedback from mentors—perfec
t if you value personal growth.
     - [Join Exercism](https://exercism.io/tracks/python)

**DSA Resources: Become Unsto
ppable**
   - **NeetCode**: Curated problem sets and videos that make DSA simpler to understand.
     - [NeetCode Resour
ces](https://neetcode.io/)
   
   - **AlgoExpert**: If you can invest, this is gold. Get high-quality explanations and c
hallenges.
     - [Check out AlgoExpert](https://www.algoexpert.io/)
   
   - **'Introduction to Algorithms' (CLRS)**: A
 classic. Pair it with Python and tackle the hardest problems.

---

**The Truth About Mastery**: 
> 'Learning to solve 
problems with Python is not just about syntax, it’s about developing a mind that can break down complexity into simplici
ty. The key is practice, consistency, and a hunger for real understanding.' 

You don’t need a hundred resources; you ne
ed focus. Pick a few from this list and dive deep. You'll be amazed at what you can achieve.

---

This guide should be 
a helpful launchpad, whether you're aiming for coding interviews, leveling up for competitive programming, or just love 
solving problems. What’s your favorite resource? Drop your go-to recommendations below!


 **Latest Python libraries bel
ow:**

- [Polars](https://www.pola.rs/)
- [DuckDB](https://duckdb.org/)
- [PyCaret](https://pycaret.gitbook.io/docs/)
- 
[JAX](https://jax.readthedocs.io/en/latest/)
- [LangChain](https://github.com/hwchase17/langchain)
- [LightGBM](https://
lightgbm.readthedocs.io/en/latest/)
- [Caffe2](https://caffe2.ai/)
- [Transformers (Hugging Face)](https://github.com/hu
ggingface/transformers)
- [PyOD](https://pyod.readthedocs.io/en/latest/)
- [Plotly](https://plotly.com/python/)
- [Bokeh
](https://docs.bokeh.org/en/latest/)
- [Pydot](https://github.com/pydot/pydot) 

These links provide documentation and d
etails for each library, making it easier to explore and integrate them into your projects.
```
---

     
 
all -  [ For RAG Devs - langchain or llamaindex? ](/r/Rag/comments/1g2h7s8/for_rag_devs_langchain_or_llamaindex/) , 2024-10-14-0913
```

```
---

     
 
all -  [ Generate <-> Validation for chat ](https://www.reddit.com/r/LangChain/comments/1g2n6tj/generate_validation_for_chat/) , 2024-10-14-0913
```
I'm building a chatbot with langgraph. To reduce errors, I've created a validation node which works like 

- Generator n
ode generates the response based on customer input

- Then the generation is sent to a validator. If the validation is s
uccessful, send the response to customers

- Else, send the response back to generator with feedback to regenerate. 

  

Facing trouble implementing this w.r.t storing history and getting the proper response from validation. Has anyone done
 anything similar to this? 
```
---

     
 
all -  [ 401 Unauthorized Error with Jina AI Embeddings API in Flask App – Need Help Troubleshooting ](https://www.reddit.com/r/LangChain/comments/1g2mlon/401_unauthorized_error_with_jina_ai_embeddings/) , 2024-10-14-0913
```
Hey Redditors!

I’m working on a Flask app that uses the Jina AI Embeddings API to process and embed document text. The 
app runs fine locally, but when I try to query the Jina API for embeddings, I keep getting the following error in the lo
gs:

(did this in my env itself)

https://preview.redd.it/3yt5h0052iud1.png?width=926&format=png&auto=webp&s=79eac415c74
3aa93730b847317030ede9fab1be0

It seems like the API request is being rejected due to an authorization issue, but I’m no
t sure why, since I’m including the API key in the headers as a Bearer token. Here's the relevant part of my \`app.py\` 
code where I make the request to Jina:

https://preview.redd.it/vnb5w0a62iud1.png?width=812&format=png&auto=webp&s=64c25
fa32f350c6807ee01766372d99ef0562342

and hence this at the end

https://preview.redd.it/kjkwrdx72iud1.png?width=1023&for
mat=png&auto=webp&s=3a21d3b521520cb5e48c18b7c1d8622cb5135bdc

Here’s what I’ve checked so far:

1. API Key: I’ve confirm
ed that my \`JINAAI\_API\_KEY\` is correct and stored in my environment variables.
2. Flask App Setup: My Flask app runs
 successfully on \`localhost:5000\`, and I'm using ngrok to tunnel traffic externally.
3. ngrok: The external URL works 
fine for other routes, but the API request to Jina still fails with a 401 error.

Any ideas on why this could be happeni
ng? Could it be something with the API key, headers, or maybe an issue with the way I’m handling the request?

Any advic
e would be greatly appreciated!

Thanks in advance!


```
---

     
 
all -  [ Text to SQL Public Chatbot ](https://www.reddit.com/r/LangChain/comments/1g2j6ro/text_to_sql_public_chatbot/) , 2024-10-14-0913
```
Hello all,

have you ever implemented a public chatbot that is able to query the DB ? What are the guardrails you put in
 place to avoid data leaking and breachs? 

I am thinking in a project where the chatbot will be available in a website 
where not logged people can use it and looking for the security piece on it besides row leves securities in the db
```
---

     
 
all -  [ What's the most efficient way to handle references like figures, tables or other sections in a RAG p ](https://i.redd.it/dsojnplzrgud1.png) , 2024-10-14-0913
```
 I could think of two ways and I'm currently implementing both. In my usecase, I'm converting all pages in a document ar
e into image format and using a multimodal llm for querying. Once I retrieve a relevant image, if there are external ref
erences,

A. Do RAG once more to retrieve the reference.

B. Identify all the references initially using the index page 
and parse and store them separately in a folder as images

With A, there are chances of RAG identifying just plain refer
ences elsewhere and not the actual definition

With B, there is a chance that some references might not be extracted cor
rectly
```
---

     
 
all -  [ I thought of a way to benefit from chain of thought prompting without using any extra tokens! ](https://www.reddit.com/r/LangChain/comments/1g2ihf5/i_thought_of_a_way_to_benefit_from_chain_of/) , 2024-10-14-0913
```
Ok this might not be anything new but it just struck me while working on a content moderation script just now that I can
 strucure my prompt like this:

```
You are a content moderator assistant blah blah...

This is the text you will be mod
erating:  
  
<input>  
[...]
</input>

You task is to make sure it doesn't violate any of the following guidelines:

[.
..]
  
Instructions:
  
1. Carefully read the entire text.  
2. Review each guideline and check if the text violates any
 of them.  
3. For each violation:  
   a. If the guideline requires removal, delete the violating content entirely.  
 
  b. If the guideline allows rewriting, modify the content to comply with the rule.  
4. Ensure the resulting text maint
ains coherence and flow.  
etc...

Output Format:
  
Return the result in this format:
  
<result>  
[insert moderated t
ext here]
</result>

<reasoning>  
[insert reasoning for each change here]  
</reasoning>

```
  
Now the key part is th
at I ask for the reasoning at the very end. Then when I make the api call, I pass the closing `</result>` tag as the **s
top** option so as soon as it's encountered the generation stops:

```
const response = await model.chat.completions.cre
ate({
  model: 'meta-llama/llama-3.1-70b-instruct',
  temperature: 1.0,
  max_tokens: 1_500,
  stop: '</result>',
  mess
ages: [
    {
      role: 'system',
      content: prompt
    }
  ]
});
```

My thinking here is that by structuring the
 prompt in this way (where you ask the model to explain itself) you beneft from it's 'chain of thought' nature and by cu
tting it off at the stop word, you don't use the additional tokens you would have had to use otherwise. Essentially gett
ing to keep your cake and eating it too!

Is my thinking right here or am I missing something?
```
---

     
 
all -  [ For RAG Devs - langchain or llamaindex? ](https://www.reddit.com/r/LLMDevs/comments/1g2ha43/for_rag_devs_langchain_or_llamaindex/) , 2024-10-14-0913
```
I've started learning rag. Learnt vector data ases, chucking etc. now confused about which framework to use.
```
---

     
 
all -  [ For RAG Devs - langchain or llamaindex? ](https://www.reddit.com/r/Rag/comments/1g2h7s8/for_rag_devs_langchain_or_llamaindex/) , 2024-10-14-0913
```
I've started learning rag. Learnt vector databases, chucking etc. now confused about which framework to use.
```
---

     
 
all -  [ Langchain clinet connection error ](https://www.reddit.com/r/LangChain/comments/1g2b2w5/langchain_clinet_connection_error/) , 2024-10-14-0913
```
I keep getting this error when using LangSmith:  
HTTPError: \[Errno 403 Client Error: Forbidden for url: [https://api.s
mith.langchain.com/datasets\]](https://api.smith.langchain.com/datasets]) {'detail':'Forbidden'}

    os.environ['LANGCH
AIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
    os.environ['LANGC
HAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

I have accessed the api\_keys.

How do I fix this? Can someone please h
elp?

Edit: I am also importing

    from langsmith import Client 
    client = Client()

Also when I set up langsmith w
ith same steps in windows env it worked but now i am using linux environment so it's easier to later deploy on aws lambd
a. Does this have to do anything with Linux environment?  

```
---

     
 
all -  [ What are you using for building & evaluating your LLM application? ](https://www.reddit.com/r/LocalLLaMA/comments/1g28kve/what_are_you_using_for_building_evaluating_your/) , 2024-10-14-0913
```
I have built the implementation of my LLM app in python, so it’s really just text and API calls and whatever complex wor
kflows, chains, orchestration around the LLMs you can just program yourself. I’m curious what folks are doing out there,
 are they doing implementation themselves or using tools?

I know there’s dozens of tools out there like Langchain, Hays
tack, Adalflow, Flowise, Llamaindex, etc.

At the end of the day these are just complex workflows, but I feel like I’m s
pending more time debugging my code than just using something to iterate more quickly. 

Especially around Evals. If I h
ave the criteria to measure against such as unit tests and LLM as a judge. I just want a tool that can quickly send 100 
or 1,000 inputs into my workflow then measure the results. All the eval tools I’ve looked at are for simple one prompts,
 if I have a complex DAG like workflow of multiple chains, steps, etc what’s a good tool for this out there?

Is there a
n LLM stack folks are using out there to make this quicker/easier? Or is doing this orchestration in code just the best 
way for this.

The closest (payed) thing I’ve seen for this is Vellum.
```
---

     
 
all -  [ ChatGPT API to remember some background info before conversation ](https://www.reddit.com/r/LangChain/comments/1g26gbz/chatgpt_api_to_remember_some_background_info/) , 2024-10-14-0913
```
Hi, I’d like to make my chatgpt api to remember some background info such as some pdf documents etc. Can I do this perma
nently with the API, not having to feed with the data everytime?
```
---

     
 
all -  [ I have 2 User Manuals I would like to use to build an AI Help Bot ](https://www.reddit.com/r/LangChain/comments/1g24vha/i_have_2_user_manuals_i_would_like_to_use_to/) , 2024-10-14-0913
```
Hey Guys! I am fairly new  to the scene. I have been using OpenAI's api for this. However, with the manual being 500 pag
es it seems to struggle every now and then. I would like to seek help and guidance on this. Any input helps. The goal is
 for the LLM to be able to take in questions and answer based on the manual. Is LangChain appropriate for this use case?
 Any veterans can give me a rough framework on how I should do this?
```
---

     
 
all -  [ A Generative AI Tool for Enhanced Documentation Clarity ](https://www.reddit.com/r/PythonProjects2/comments/1g2490b/a_generative_ai_tool_for_enhanced_documentation/) , 2024-10-14-0913
```
Hi everyone! I’m new to the world of Generative AI and currently exploring concepts like Large Language Models (LLMs) an
d Langchain. I recently worked on an exciting project called [DelvInDocs.AI](https://github.com/hrithikkoduri/DelvInDocs
.AI), aimed at enhancing the understandability of extensive documentation using Langchain, Open AI GPT and embeddings an
d Activeloop's Deeplake for vector database.

This tool scrapes information from all the parent and child links from the
 provided input base URLs of the documentation. Users can ask questions and receive tailored code snippets and cohesive 
responses across various libraries (e.g., React, Node.js, Tailwind CSS, MongoDB). This streamlines the process of findin
g relevant information from complex documentation and saves valuable development time.

I’d love for you to check it out
 by cloning the GitHub Repo: \[ [https://github.com/hrithikkoduri/DelvInDocs.AI](https://github.com/hrithikkoduri/DelvIn
Docs.AI) \]. 

https://reddit.com/link/1g2490b/video/82pdp4botcud1/player


```
---

     
 
all -  [ Announcing Laravel Synapse v0.1.0 - Seamlessly Integrate AI Agents into Your Laravel Applications 🧠 ](https://www.reddit.com/r/laravel/comments/1g23vzj/announcing_laravel_synapse_v010_seamlessly/) , 2024-10-14-0913
```
Hey everyone! I'm excited to announce the release of \*\*Synapse v0.1.0\*\*, a new package that simplifies creating and 
managing AI agents in Laravel apps. Inspired by Langchain and Saloon, Synapse allows you to build AI-driven applications
 with flexible, scalable agents.

# Key Features:

* \*\*Multiple AI Integrations\*\*: Out-of-the-box support for \*\*Op
enAI\*\* and \*\*Claude\*\*.
* \*\*Customizable Agent Lifecycle\*\*: Easily extend and modify the agent lifecycle with b
uilt-in hooks.
* \*\*Dynamic Prompts\*\*: Leverage Laravel’s Blade system to build highly dynamic, \`few-shot\` prompts.

* \*\*Prebuilt Agents\*\*: Start quickly with prebuilt agents for popular integrations like OpenAI.
* \*\*Custom Tools\
*\*: Create custom tools that can interact with agents, make API calls, and more.

Check out the documentation and get s
tarted here: \[Synapse\](https://github.com/use-the-fork/synapse)

Feel free to share your feedback or questions. I’m ex
cited to see what the community builds with it!
```
---

     
 
all -  [ Front end tools ](https://www.reddit.com/r/LangChain/comments/1g22rxh/front_end_tools/) , 2024-10-14-0913
```
Which front end frameworks/tools you all been using ? 

I am using React to create my interfaces because I really don't 
like streamlit and the way to customized it. So I am wonder what you guys have been using.

Also if you have good open-s
ource things that helps you to accelerate the chat creation. I know we have some but sometimes they require you to deplo
y in a single place and I want my interfaces to be deployed non matter where .
```
---

     
 
all -  [ Need help with learning how to make a rag!! ](https://www.reddit.com/r/learnmachinelearning/comments/1g21mr2/need_help_with_learning_how_to_make_a_rag/) , 2024-10-14-0913
```
I am building a rag that can read word documents and answer questions on said word documents. I want it to be able to ha
ve chat history that will be saved to mongo db and for the output to contain the source from which document and page num
ber it got the information from. I am also using google collab since my laptop cant run doom. So far this is the code I 
have down:

    from langchain_community.document_loaders import Docx2txtLoader
    from langchain.text_splitter import 
RecursiveCharacterTextSplitter
    from langchain.chains import RetrievalQA
    from langchain.vectorstores import Chrom
a
    from langchain.embeddings import HuggingFaceEmbeddings
    from transformers import AutoModelForCausalLM, AutoToke
nizer, pipeline
    from langchain.llms import HuggingFacePipeline
    from langchain.memory import ConversationBufferMe
mory
    from langchain_core.output_parsers import StrOutputParser
    from langchain.prompts import PromptTemplate
    
from langchain_core.runnables import RunnablePassthrough
    from pymongo import MongoClient
    import os
    import to
rch
    
    # Load documents from local files
    doc_paths = ['./Minecraft Basics for AI.docx', './Minecraft Mining fo
r AI.docx']
    all_documents = []
    for doc_path in doc_paths:
        if os.path.isfile(doc_path):
            loade
r = Docx2txtLoader(doc_path)
            data = loader.load()
            for page_num, doc in enumerate(data):
        
        doc.metadata = {'source': doc_path, 'page_number': page_num + 1}
                all_documents.append(doc)
     
   else:
            print(f'File {doc_path} does not exist.')
    
    # Create embeddings with a smaller, more efficie
nt model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    
    # Create r
etriever if there are valid documents
    if all_documents:
        text_splitter = RecursiveCharacterTextSplitter(chunk
_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(all_documents)
    
        # Create the C
hroma vector store
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    
        # Cr
eate a retriever
        retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 6})
    else
:
        print('No valid documents were loaded.')
        retriever = None
    
    # Set up the LLM model with a small
er model to reduce RAM usage
    model_name = 'EleutherAI/gpt-neo-1.3B' 
    tokenizer = AutoTokenizer.from_pretrained(m
odel_name)
    pipe = pipeline('text-generation', model=model_name, tokenizer=tokenizer, max_length=512, device='cuda' i
f torch.cuda.is_available() else -1)  # Use GPU if available
    llm = HuggingFacePipeline(pipeline=pipe)
    
    # Def
ine the prompt template
    prompt_template = '''
    <|system|>
    Answer the question based on your knowledge. Use th
e following context to help:
    
    {context}
    
    </s>
    <|user|>
    {question}
    </s>
    <|assistant|>
   
 '''
    prompt = PromptTemplate(
        input_variables=['context', 'question'],
        template=prompt_template,
   
 )
    
    # MongoDB setup
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client['chat_his
tory_db']
    chat_collection = db['chats']
    
    # Setup conversation buffer memory
    memory = ConversationBufferM
emory(memory_key='chat_history', return_messages=True)
    
    # Set up the QA chain with document combiner
    llm_cha
in = prompt | llm | StrOutputParser()
    rag_chain = {'context': retriever, 'question': RunnablePassthrough()} | llm_ch
ain
    
    # Function to interact with the bot via terminal
    def chat_with_bot():
        print('Start chatting wit
h the bot (type 'exit' to stop)')
        while True:
            user_input = input('You: ')
            if user_input.
lower() == 'exit':
                break
            response = rag_chain.run(user_input)
            # Save chat histor
y to MongoDB
            chat_record = {
                'user': user_input,
                'bot': response,
          
  }
            chat_collection.insert_one(chat_record)
            # Display bot response
            print(f'Bot: {res
ponse}')
    
    if __name__ == '__main__':
        chat_with_bot()
    


```
---

     
 
all -  [ Please help a stressed out intern ](https://www.reddit.com/r/LangChain/comments/1g213oe/please_help_a_stressed_out_intern/) , 2024-10-14-0913
```
Hi everyone.

Posting in this sub in hopes for some guidance. 
I’m an intern for this startup company and i’ve been task
ed to create a conversational ai agent for customer service.

I’ve been banging my head against the wall for two weeks n
ow reading the documentation and following so many tutorials and books, which many have become outdated now due to the d
eprecation of a lot of things in langchain. Also, the head of the team quit a long time ago and due to budget reasons th
ey’re hiring an intern (me lol) instead, so i have no subject matter expert to even guide or help me in any way. 

Pleas
e someone help me yall i’m legit desperate, tired, broke, dehydrated and trying my absolute best to land a job. 

I just
 feel so lost. 

Context: 

We’re supposedly using pinecone as the vector db and i’ll put the documents and build the re
spective knowledge base on it. 

Obstacle 1: I don’t know how the knowledge base should look like. The document manuals 
they have for company policies isn’t that good i think but yet again i have no caliber to judge whether this would be ok
ay to finetune the llm on or not. Depending on the issue the customer is facing, the llm would either respond accordingl
y or even call an api to get live info on the product shipping status.

Onto langchain, the big boss. I’m so lost on whe
ther i’m piecing the code correctly or not and the output isn’t really helping. 

Obstacle 2: I first used “Conversation
alRetreivalChain.from_llm “ after embedding one of their documents in a basic faiss db just to test the flow out. The ou
tput was okay but now it’s deprecated and i’m trying to use “create_retreival_chain” and “create_history_aware_retreiver
” but i cant seem to piece it to get the same output as before. 

Tried following a walkthrough in their documentation, 
wth is “create_retreiver_tool” and why is it a tool not a chain like the other? What’s the difference and idk which i sh
ould use. 

Obstacle 3: they deprecated “ConversationBufferMemory” and i’ve no idea now how to create an agent with memo
ry.  Trying to piece everything together and i also tried using “create_stuff_documents_chain” but still can’t get the o
utput to look like how it was when i used “ConversationalRetreivalChain”

Obstacle 4: what are all these prompts? I woul
d look at two tutorials that seem to be doing the same thing but one uses prompts and the other doesnt. I am honestly so
 confused at this point.

I could go on and on but i think these are my major obstacles. 

I would really appreciate jus
t any guidance at this point, please.


```
---

     
 
all -  [ I built a completely autonomous AI employee using Langgraph ](https://www.reddit.com/r/LangChain/comments/1g1ze8u/i_built_a_completely_autonomous_ai_employee_using/) , 2024-10-14-0913
```
Hey, I'm Dhruv and I'm building The AI Agent Co. We just launched our first completely autonomous AI employee with a nov
el UI to support AI-Human Interaction. Would love your feedback on it! You can check out our agent here: [travisaiagent.
com](http://travisaiagent.com) (please try to view it on a laptop/desktop, haven't designed it for mobiles yet)
```
---

     
 
all -  [ Need some in-depth help! Opensearch vs. Pinecone ](https://www.reddit.com/r/Rag/comments/1g1xmtj/need_some_indepth_help_opensearch_vs_pinecone/) , 2024-10-14-0913
```
A bit of context:

I have computer science background and I *have some knowledge of Machine learning* but still not as p
rofound as you ;)

That being said:

Our usecase is to embed (vectorize)  documents -> and later based on queries retrie
ve the most relevant document.

Our current solution looks like:

* embedding using Titan model on Bedrock
* storing vec
tors on Pinecone

I am really eager to switch to Opensearch (you may ask why? we can discuss it in another thread :D).


But my concern is that: Pinecone is so trendy, and it is essentially designed for vector databases; although it is not t
he case for Opensearch.

**What will I lose by switching from Pinecone to Opensearch?**

my technical knowledge is limit
ed and I would like to ask your opinion on it, please.

(regarding the implementation: it is feasible using **knn\_vecto
r** s of Opensearch, have read some documents and workshops on it: e.g. [link](https://python.langchain.com/docs/integra
tions/vectorstores/opensearch/))

Bests ;)
```
---

     
 
all -  [ A Generative AI Tool for Enhanced Documentation Clarity ](https://www.reddit.com/r/generativeAI/comments/1g1tesl/a_generative_ai_tool_for_enhanced_documentation/) , 2024-10-14-0913
```
Hi everyone! I’m new to the world of Generative AI and currently exploring concepts like Large Language Models (LLMs) an
d Langchain. I recently worked on an exciting project called [**DelvInDocs.AI**](https://github.com/hrithikkoduri/DelvIn
Docs.AI), aimed at enhancing the understandability of extensive documentation using Langchain, Open AI GPT and embedding
s and Activeloop's Deeplake for vector database.

This tool scrapes information from all the parent and child links from
 the provided input base URLs of the documentation. Users can ask questions and receive tailored code snippets and cohes
ive responses across various libraries (e.g., React, Node.js, Tailwind CSS, MongoDB). This streamlines the process of fi
nding relevant information from complex documentation and saves valuable development time.

I’d love for you to check it
 out by cloning the GitHub Repo: \[ [https://github.com/hrithikkoduri/DelvInDocs.AI](https://github.com/hrithikkoduri/De
lvInDocs.AI) \]. Any feedback, suggestions, and contributions through forking would be greatly appreciated

https://redd
it.com/link/1g1tesl/video/t9zhqp55j9ud1/player
```
---

     
 
all -  [ Memory choice in a chatbot ](https://www.reddit.com/r/LangChain/comments/1g1susv/memory_choice_in_a_chatbot/) , 2024-10-14-0913
```
I’m developing a chatbot and I was wondering what kind of memory state people use.
Does ConversationBufferMemory without
 Window use a lot of overhead and decrease the response performance after a while?
```
---

     
 
all -  [ LangChain: Custom Function Streaming in BaseTool Not Working as Expected ](https://www.reddit.com/r/LangChain/comments/1g1sp5q/langchain_custom_function_streaming_in_basetool/) , 2024-10-14-0913
```
Fellow Redditors,

I've asked this question on the LangChain Discord, but you know how it is—I usually get better respon
ses here on Reddit. So, here goes...

I'm encountering an issue with custom function streaming in LangChain's BaseTool u
sing `astream_events`. Looking for insights or potential solutions.

**Issue:**

* Standard LangChain chain streaming wo
rks fine.
* In custom variation: `run_manager.on_text` calls don't stream events in real-time.
* Events are collected by
 the tool before being sent, rather than streaming.

**Goal:**

* Achieve real-time event streaming from custom function
, similar to standard LangChain chains.
* Convert custom function to `RunnableLambda` for automatic callback handling.


**Resources:**

* Code example: [Gist](https://gist.github.com/sharrajesh/98238425679e648d3b15bb025c36ebeb)
* GitHub iss
ue: [#27299](https://github.com/langchain-ai/langchain/issues/27299)

Environment: LangChain 0.2.16, Python 3.11.3

Has 
anyone encountered similar issues or have suggestions? Any input is appreciated.
```
---

     
 
all -  [ NaturalAgents - notion-style editor to easily create AI Agents ](https://www.reddit.com/r/LanguageTechnology/comments/1g1rzi2/naturalagents_notionstyle_editor_to_easily_create/) , 2024-10-14-0913
```
[NaturalAgents](https://github.com/NaturalAgents/NaturalAgents) is the easiest way to create AI Agents in a notion-style
 editor without code - using plain english and simple macros. It's fully open-source and will be actively maintained.

H
ow this is different from other agent builders -

1. No boilerplate code (imagine langchain for multiple agents)
2. No c
ode experience
3. Can easily share and build with others
4. Readable/organized agent outputs
5. Abstracts agent communic
ations without visual complexity (image large drag and drop flowcharts)

Would love to hear thoughts and feel free to re
ach out if you're interested in contributing!
```
---

     
 
all -  [ Problem with passing private state between nodes ](https://www.reddit.com/r/LangChain/comments/1g1pufn/problem_with_passing_private_state_between_nodes/) , 2024-10-14-0913
```
I have some information from one node that I would like to be passed to another node without it being outputted when I r
un 'return output'.

I was following the tutorial here: [https://langchain-ai.github.io/langgraph/how-tos/pass\_private\
_state/](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/)

The tutorial works fine when it uses 'gr
aph.invoke()'

However, when I stream the state using 'graph.stream()', I am still able to see the outputs of each node,
 including the private state of node 1.

Does anything have any suggestions on how to solve this issue?

  

```
---

     
 
all -  [ OpenAI’s new framework for Agents. Why is Langgraph so complicated?  ](https://www.reddit.com/gallery/1g1pkki) , 2024-10-14-0913
```
Langgraph example for basic agent vs OpenAI’s new framework. I’d love to stick with langchain for agents but it’s too co
mplicated to run and deploy without Langgraph cloud. 

https://github.com/openai/swarm - Link 
```
---

     
 
all -  [ RAG frontend advice needed (Streamlit vs Nuxt) ](https://www.reddit.com/r/LangChain/comments/1g1kfj6/rag_frontend_advice_needed_streamlit_vs_nuxt/) , 2024-10-14-0913
```
Hey all,

I have the task of building a RAG system for one of the company departments to use. They will upload their fil
es and perform different tasks using agents. Now the requirement is that at least 11 people can use the system simultane
ously, along with an admin panel and some accounts being used by multiple people at once. I have 3 options to build it:


1. LC and Streamlit standalone app.  
2. LC + FastAPI backend and Streamlit frontend  
3. LC + FastAPI backend and Nuxt
 frontend

My issue is that I don't have much experience building interfaces with Streamlit and from the very basic thin
gs that I have used it for it seemed quite slow and unpleasant as far as UX goes (although I am no expert with it so I m
ight very well be entirely responsible for the bad experience). So I am not sure how suitable Streamlit would be as a st
andalone application as far as concurrence usage goes and stress/load capabilities. I believe the 3rd option would be th
e best in terms of results, but the 1st and 2nd give the easiest maintenance as all would be python based.

Could you sh
are your opinions and advice please?

-------

Edit:
My boss wants to go more for the 1st and if not the 2nd option beca
use of the easier maintenance as most guys on the team only use Python I guess. So the question of Streamlit's capabilit
ies to handle the stress load is the most important one in terms of making the choice..
```
---

     
 
all -  [ What is all the buzz about agents about? How is it different from an app that makes multiple calls t ](https://www.reddit.com/r/LangChain/comments/1g1k3xl/what_is_all_the_buzz_about_agents_about_how_is_it/) , 2024-10-14-0913
```
I'm trying to keep myself up to date with LLM stuff after having built a few LLM apps on the side. I am starting to see 
more and more people post about 'agents', but I can't quite figure out how an 'agent' differs from a regular software ap
p that calls multiple APIs.



The cynical side of me is thinking this is a buzzword, but I want to be a bit more open m
inded...is there something more to agents than just an app that makes decisions to call different APIs based on the outp
ut of an LLM? 
```
---

     
 
all -  [ How to stream Langgraph output from graph.stream into Streamlit??? ](https://www.reddit.com/r/LangChain/comments/1g1ja8j/how_to_stream_langgraph_output_from_graphstream/) , 2024-10-14-0913
```
I am trying to create a streamlit app using Langgraph in the backend, ollama for llm and a few tools. I got the code to 
work properly in the terminal, and the output is being streamed. 

When I plug this output into streamlit's write\_strea
m function, it treats eavh token as one output. any help with this??

The github repo is [https://github.com/PratikBhang
ale/LangGraph-Chatbot](https://github.com/PratikBhangale/LangGraph-Chatbot)
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-14-0913
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-14-0913
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-14-0913
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-14-0913
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
