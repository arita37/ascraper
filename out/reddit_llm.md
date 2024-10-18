 
all -  [ Why Langchain tools are fetching fake results? ](https://www.reddit.com/r/LangChain/comments/1g6521c/why_langchain_tools_are_fetching_fake_results/) , 2024-10-18-0912
```
I am building an AI agent with web searching functions in Langchain. However, almost all fetched web results are fake re
sults (information was fake; url was fake; date was fake: today is 10/17, but the returned news showed date of 10/20). A
nyone know why is that? Example:

\`\`\`python

    output = agent_executor.invoke(
        {'input': 'Tell me some rece
nt news about the 2024 US presidential election. I want news with publication date after 10/15/2024'}
    )
    print(ou
tput['output'])
    

\`\`\`

Output:

\`\`\`  
> Entering new AgentExecutor chain...  
Answer the following questions a
s best you can. You have access to the following tools:  
  
search\_and\_contents(query: str) - Search for webpages bas
ed on the query and retrieve their contents.  
find\_similar\_and\_contents(url: str) - Search for webpages similar to a
 given URL and retrieve their contents.  
The url passed in should be a URL returned from \`search\_and\_contents\`.  
y
ahoo\_finance\_news - Useful for when you need to find financial news about a public company. Input should be a company 
ticker. For example, AAPL for Apple, MSFT for Microsoft.  
riza\_exec\_python - Execute Python code to solve problems.  

  
The Python runtime does not have filesystem access. You can use the httpx  
or requests library to make HTTP request
s. Always print output to stdout.  
wikipedia - A wrapper around Wikipedia. Useful for when you need to answer general q
uestions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.  

  
Use the following format:  
  
Question: the input question you must answer  
Thought: you should always think about
 what to do  
Action: the action to take, should be one of \[search\_and\_contents, find\_similar\_and\_contents, yahoo\
_finance\_news, riza\_exec\_python, wikipedia\]  
Action Input: the input to the action  
Observation: the result of the
 action  
... (this Thought/Action/Action Input/Observation can repeat N times)  
Thought: I now know the final answer  

Final Answer: the final answer to the original input question  
  
Begin!  
  
Question: Tell me some recent news about
 the 2024 US presidential election. I want news with publication date after 10/15/2024  
Thought: To find recent news ab
out the 2024 US presidential election, I should search for webpages with a query that includes the election and a date r
ange to filter out older news.  
Action: search\_and\_contents  
Action Input: '2024 US presidential election news after
 10/15/2024'  
Observation:   
\[  
{  
'url': '[https://www.cnn.com/2024/10/20/politics/2024-election-news/index.html](
https://www.cnn.com/2024/10/20/politics/2024-election-news/index.html)',  
'contents': 'CNN Projects:... (rest of the co
ntents truncated for brevity)'  
},  
{  
'url': '[https://www.nbcnews.com/politics/2024-election/live-blog/live-updates
-2024-presidential-election-rcna112641](https://www.nbcnews.com/politics/2024-election/live-blog/live-updates-2024-presi
dential-election-rcna112641)',  
'contents': 'Live updates:... (rest of the contents truncated for brevity)'  
}  
\]  

Thought: The search results are from reputable news sources, but the contents are truncated. I should find similar webpa
ges to these results to see if I can find more detailed information.  
Action: find\_similar\_and\_contents  
Action Inp
ut: '[https://www.cnn.com/2024/10/20/politics/2024-election-news/index.html](https://www.cnn.com/2024/10/20/politics/202
4-election-news/index.html)'  
Observation:   
\[  
{  
'url': '[https://www.cnn.com/2024/10/22/politics/2024-election-l
atest-developments/index.html](https://www.cnn.com/2024/10/22/politics/2024-election-latest-developments/index.html)',  

'contents': 'Latest on the 2024 US presidential election:... (rest of the contents truncated for brevity)'  
}  
\]  
T
hought: I now know the final answer  
Final Answer: Here are some recent news articles about the 2024 US presidential el
ection with publication dates after 10/15/2024:  
  
\* CNN: 'CNN Projects:...' (published 10/20/2024) - [https://www.cn
n.com/2024/10/20/politics/2024-election-news/index.html](https://www.cnn.com/2024/10/20/politics/2024-election-news/inde
x.html)  
\* NBC News: 'Live updates:...' (no specific publication date mentioned, but appears to be live updates) - [ht
tps://www.nbcnews.com/politics/2024-election/live-blog/live-updates-2024-presidential-election-rcna112641](https://www.n
bcnews.com/politics/2024-election/live-blog/live-updates-2024-presidential-election-rcna112641)  
\* CNN: 'Latest on the
 2024 US presidential election:...' (published 10/22/2024) - [https://www.cnn.com/2024/10/22/politics/2024-election-late
st-developments/index.html](https://www.cnn.com/2024/10/22/politics/2024-election-latest-developments/index.html)  
  
>
 Finished chain.  
Here are some recent news articles about the 2024 US presidential election with publication dates aft
er 10/15/2024:  
  
\* CNN: 'CNN Projects:...' (published 10/20/2024) - [https://www.cnn.com/2024/10/20/politics/2024-el
ection-news/index.html](https://www.cnn.com/2024/10/20/politics/2024-election-news/index.html)  
\* NBC News: 'Live upda
tes:...' (no specific publication date mentioned, but appears to be live updates) - [https://www.nbcnews.com/politics/20
24-election/live-blog/live-updates-2024-presidential-election-rcna112641](https://www.nbcnews.com/politics/2024-election
/live-blog/live-updates-2024-presidential-election-rcna112641)  
\* CNN: 'Latest on the 2024 US presidential election:..
.' (published 10/22/2024) - [https://www.cnn.com/2024/10/22/politics/2024-election-latest-developments/index.html](https
://www.cnn.com/2024/10/22/politics/2024-election-latest-developments/index.html)

\`\`\`
```
---

     
 
all -  [ 5.5 h (4.7 stars)- LangChain Mastery: Build Powerful Generative AI Apps ](https://www.easylearn.ing/course/generative-ai-with-langchain) , 2024-10-18-0912
```

```
---

     
 
all -  [ [Project] Are embeddings the best strategy to look for product matches in complex datasets? ](https://www.reddit.com/r/LangChain/comments/1g6140c/project_are_embeddings_the_best_strategy_to_look/) , 2024-10-18-0912
```
I'm working on a project where I have a dataset of approximately 1000 combinations of product characteristics (like form
at, page count, printing type, paper type, etc.). Although there is a lot of overlap, each row ultimately represents a u
nique combination of characteristics, and my task is to find the best match for a given product description coming from 
another dataset.

LLMs do not seem a good idea, as 1000 categories are a lot. Moreover, we're talking about categories w
ith very specific, technical nouns in them.

Initially, I thought of using **embeddings** (with models like NV-Embed-v2)
 to compare these descriptions based on cosine similarity. However, I'm wondering if this is the most effective strategy
, considering that some columns have very specific values that might benefit from exact or near-exact matching, while ot
hers may need more flexibility. 

So, my question is: i**s relying purely on embeddings the best strategy, or is there a
re some other strategy that I am missing here?** 

If anyone has worked on similar problems or has suggestions on how to
 approach this more efficiently, I’d love to hear your thoughts!
```
---

     
 
all -  [ ChatBot Evaluation Metric ](https://www.reddit.com/r/LangChain/comments/1g60yhx/chatbot_evaluation_metric/) , 2024-10-18-0912
```
I am a 3rd year undergrad at IIT Bombay, India, and currently intern season is going on in our college and in my resume 
I have things like RAG and Chatbot. In my last two interviews, I was asked question from my resume and puzzles (Brainste
ller level).

The question that was common in the both the interviews goes like '**What are some of the most common eval
uation metric that we use to test chatbots?'**. For example in classification we make use of precision and recall values
 to know the quality of fthe model.

  
So right after my first interview I surfed the web to know some metrics to evalu
ate chatbots. I got to know about some on the methods but didn't got any metrics (like a value that can quantify whether
 my model is good or not).

Can anyone help me, explain or find some resources to learn the same.

I would really apprec
iate any help.
```
---

     
 
all -  [ Langchain: combining Rag for search and SQL to match ](https://www.reddit.com/r/LangChain/comments/1g60ty7/langchain_combining_rag_for_search_and_sql_to/) , 2024-10-18-0912
```
I have to create a chatbot that uses as input a command to carry out research and matches of Employees: in particular I 
have a Rag in which I store the employee resume as a long text and I have a Postgress database used to check the availab
ility in working on certain dates. 

In input I could receive the following prompt: 'Tell me 4 employees who has good ar
tificial intelligence skills available to work from date xx-xx-xx to date yy-yy-yy'. 

Thank you very much!
```
---

     
 
all -  [ [October 18] Enroll Now: Free Udemy Course Available Today ](https://www.reddit.com/r/udemyfreebies/comments/1g5z5rg/october_18_enroll_now_free_udemy_course_available/) , 2024-10-18-0912
```
Python Programming for Beginners: Learn Python from Scratch

[https://freewebcart.com/python-programming-for-beginners-l
earn-python-from-scratch/](https://freewebcart.com/python-programming-for-beginners-learn-python-from-scratch/)

&#x200B
;

Microsoft Excel - Advanced Formulas & Functions with GenAI

[https://freewebcart.com/microsoft-excel-advanced-formula
s-functions-with-genai/](https://freewebcart.com/microsoft-excel-advanced-formulas-functions-with-genai/)

&#x200B;

Exc
el Charts- Data Visualization Secrets - Beginner to Pro

[https://freewebcart.com/excel-charts-data-visualization-secret
s-beginner-to-pro/](https://freewebcart.com/excel-charts-data-visualization-secrets-beginner-to-pro/)

&#x200B;

JavaScr
ipt From Scratch ( Part 1 - Beginner Level)

[https://freewebcart.com/javascript-from-scratch-part-1-beginner-level/](ht
tps://freewebcart.com/javascript-from-scratch-part-1-beginner-level/)

&#x200B;

3D Printing with ' Ultimaker CURA Slice
r- Start to finish'

[https://freewebcart.com/3d-printing-with-ultimaker-cura-slicer-start-to-finish/](https://freewebca
rt.com/3d-printing-with-ultimaker-cura-slicer-start-to-finish/)

&#x200B;

Learn ChatGPT, Midjourney, AI and Use it For 
Passive Income

[https://freewebcart.com/learn-chatgpt-midjourney-ai-and-use-it-for-passive-income/](https://freewebcart
.com/learn-chatgpt-midjourney-ai-and-use-it-for-passive-income/)

&#x200B;

Zero to Hero in Ollama: Create Local LLM App
lications

[https://freewebcart.com/zero-to-hero-in-ollama-create-local-llm-applications/](https://freewebcart.com/zero-
to-hero-in-ollama-create-local-llm-applications/)

&#x200B;

Adobe InDesign CC for Beginner to Advanced Masterclass

[ht
tps://freewebcart.com/adobe-indesign-cc-for-beginner-to-advanced-masterclass/](https://freewebcart.com/adobe-indesign-cc
-for-beginner-to-advanced-masterclass/)

&#x200B;

Advanced MS Word Excel PowerPoint Course for Job Success

[https://fr
eewebcart.com/advanced-ms-word-excel-powerpoint-course-for-job-success/](https://freewebcart.com/advanced-ms-word-excel-
powerpoint-course-for-job-success/)

&#x200B;

The Complete Guide to Instagram Marketing for Businesses

[https://freewe
bcart.com/the-complete-guide-to-instagram-marketing-for-businesses/](https://freewebcart.com/the-complete-guide-to-insta
gram-marketing-for-businesses/)

&#x200B;

The Complete T-Shirt Design Toolkit: PS, AI & Canva

[https://freewebcart.com
/the-complete-t-shirt-design-toolkit-ps-ai-canva/](https://freewebcart.com/the-complete-t-shirt-design-toolkit-ps-ai-can
va/)

&#x200B;

Zero to Hero in LangChain: Build GenAI apps using LangChain

[https://freewebcart.com/zero-to-hero-in-la
ngchain-build-genai-apps-using-langchain/](https://freewebcart.com/zero-to-hero-in-langchain-build-genai-apps-using-lang
chain/)

&#x200B;

Mastering HTML5 and CSS3 (Part 2 - Intermediate Level)

[https://freewebcart.com/mastering-html5-and-
css3-part-2-intermediate-level/](https://freewebcart.com/mastering-html5-and-css3-part-2-intermediate-level/)

&#x200B;


Mastering React: React Crash Course with Mini Projects

[https://freewebcart.com/mastering-react-react-crash-course-wit
h-mini-projects/](https://freewebcart.com/mastering-react-react-crash-course-with-mini-projects/)

&#x200B;

Python Cras
h Course: Dive into Coding with Hands-On Projects

[https://freewebcart.com/python-crash-dive-into-coding-with-hands-on-
projects/](https://freewebcart.com/python-crash-dive-into-coding-with-hands-on-projects/)

&#x200B;

Python Complete Cou
rse And Flask Framework, HTML Essentials

[https://freewebcart.com/python-complete-course-and-flask-framework-html-essen
tials/](https://freewebcart.com/python-complete-course-and-flask-framework-html-essentials/)

&#x200B;

Master Logo Desi
gn with Photoshop Illustrator Zero to Pro

[https://freewebcart.com/master-logo-design-with-photoshop-illustrator-zero-t
o-pro/](https://freewebcart.com/master-logo-design-with-photoshop-illustrator-zero-to-pro/)

&#x200B;

Microsoft Ads Mas
terClass - All Campaigns & Features

[https://freewebcart.com/microsoft-ads-masterclass-2024-all-campaigns-features/](ht
tps://freewebcart.com/microsoft-ads-masterclass-2024-all-campaigns-features/)

&#x200B;

Python Programming Complete Beg
inners Course Bootcamp 2024

[https://freewebcart.com/learn-python-from-scratch-its-usage-by-nasa-in-mars-rovers/](https
://freewebcart.com/learn-python-from-scratch-its-usage-by-nasa-in-mars-rovers/)

&#x200B;

Object Oriented Programming i
n C++ & Interview Preparation

[https://freewebcart.com/object-oriented-programming-in-c-interview-preparation/](https:/
/freewebcart.com/object-oriented-programming-in-c-interview-preparation/)

&#x200B;

2024 R Programming Bootcamp for Abs
olute Beginners

[https://freewebcart.com/2022-r-programming-bootcamp/](https://freewebcart.com/2022-r-programming-bootc
amp/)

&#x200B;

Mastering Pointers in C : A Course on Efficient Programming

[https://freewebcart.com/mastering-pointer
s-in-c-a-course-on-efficient-programming/](https://freewebcart.com/mastering-pointers-in-c-a-course-on-efficient-program
ming/)

&#x200B;

CSS, JavaScript,PHP And Python Programming All in One Course

[https://freewebcart.com/css-javascriptp
hp-and-python-programming-all-in-one-course/](https://freewebcart.com/css-javascriptphp-and-python-programming-all-in-on
e-course/)

&#x200B;

How to Make AI Videos: Mastering AI Text-to-Video Creation

[https://freewebcart.com/how-to-make-a
i-videos-mastering-ai-text-to-video-creation/](https://freewebcart.com/how-to-make-ai-videos-mastering-ai-text-to-video-
creation/)

&#x200B;

Master AI-Powered Chatbots, 24/7 Appointment Booking with AI

[https://freewebcart.com/master-ai-p
owered-chatbots-24-7-appointment-booking-with-ai/](https://freewebcart.com/master-ai-powered-chatbots-24-7-appointment-b
ooking-with-ai/)

&#x200B;

Microsoft Excel - Beginner to Advance with Example

[https://freewebcart.com/learn-excel-fro
m-beginner-to-advance-with-example/](https://freewebcart.com/learn-excel-from-beginner-to-advance-with-example/)

&#x200
B;

Mastering ChatGPT (AI) and PowerPoint presentation

[https://freewebcart.com/mastering-chatgpt-ai-and-powerpoint-pre
sentation/](https://freewebcart.com/mastering-chatgpt-ai-and-powerpoint-presentation/)

&#x200B;

Problem Solving with C
++ programming language

[https://freewebcart.com/problem-solving-with-c-programming-languages/](https://freewebcart.com
/problem-solving-with-c-programming-languages/)

&#x200B;

JavaScript From Scratch ( Part 1 - Beginner Level)

[https://
freewebcart.com/javascript-from-scratch-part-1-beginner-level/](https://freewebcart.com/javascript-from-scratch-part-1-b
eginner-level/)

&#x200B;

CentOS Linux and Ubuntu Linux: Managing Packages

[https://freewebcart.com/centos-linux-and-u
buntu-linux-managing-packages/](https://freewebcart.com/centos-linux-and-ubuntu-linux-managing-packages/)

&#x200B;

Mas
tering HTML5 and CSS3 (Part 2 - Intermediate Level)

[https://freewebcart.com/mastering-html5-and-css3-part-2-intermedia
te-level/](https://freewebcart.com/mastering-html5-and-css3-part-2-intermediate-level/)

&#x200B;

Master of Essential C
++ Programming Beginner to Advanced

[https://freewebcart.com/master-of-essential-c-programming-beginner-to-advanced/](h
ttps://freewebcart.com/master-of-essential-c-programming-beginner-to-advanced/)

&#x200B;

C# Test Automation Engineer -
 from Zero to Hero

[https://freewebcart.com/c-test-automation-engineer-from-zero-to-hero/](https://freewebcart.com/c-te
st-automation-engineer-from-zero-to-hero/)

&#x200B;

Build Complete PHP MySQL Food Ordering Ecommerce Store

[https://f
reewebcart.com/build-complete-2023-php-mysql-food-ordering-ecommerce-store/](https://freewebcart.com/build-complete-2023
-php-mysql-food-ordering-ecommerce-store/)

&#x200B;

Master Filmora: Editing, Motion Graphics, and Color Grading

[http
s://freewebcart.com/master-filmora-editing-motion-graphics-and-colorgrading/](https://freewebcart.com/master-filmora-edi
ting-motion-graphics-and-colorgrading/)

&#x200B;

Social Media Video Editing With Premiere Pro Canva Filmora

[https://
freewebcart.com/social-media-video-editing-with-premiere-pro-canva-filmora/](https://freewebcart.com/social-media-video-
editing-with-premiere-pro-canva-filmora/)

&#x200B;

Complete Python For Absolute Beginners

[https://freewebcart.com/co
mplete-python-2023-for-absolute-beginners/](https://freewebcart.com/complete-python-2023-for-absolute-beginners/)

&#x20
0B;

Mastering Database Management with Knex.js and PostgreSQL

[https://freewebcart.com/mastering-database-management-w
ith-knex-js-and-postgresql/](https://freewebcart.com/mastering-database-management-with-knex-js-and-postgresql/)

&#x200
B;

Learn UI UX Design Adobe XD : Learn User Experience Design

[https://freewebcart.com/learn-ui-ux-design-adobe-xd-lea
rn-user-experience-design/](https://freewebcart.com/learn-ui-ux-design-adobe-xd-learn-user-experience-design/)

&#x200B;


Excel Analytics: Linear Regression Analysis in MS Excel

[https://freewebcart.com/excel-analytics-linear-regression-an
alysis-in-ms-excel/](https://freewebcart.com/excel-analytics-linear-regression-analysis-in-ms-excel/)

&#x200B;

C# Mast
ering Course For Beginners

[https://freewebcart.com/c-mastering-course-for-beginners/](https://freewebcart.com/c-master
ing-course-for-beginners/)

&#x200B;

Metasploit from Scratch: Beginner to Professional

[https://freewebcart.com/metasp
loit-from-scratch-beginner-to-professional/](https://freewebcart.com/metasploit-from-scratch-beginner-to-professional/)


&#x200B;

ChatGPT Masterclass: The Ultimate Beginner's Guide!

[https://freewebcart.com/chatgpt-masterclass-the-ultimat
e-beginners-guide/](https://freewebcart.com/chatgpt-masterclass-the-ultimate-beginners-guide/)

&#x200B;

Essential Micr
osoft PowerPoint Course for Everyone

[https://freewebcart.com/essential-microsoft-powerpoint-course-for-everyone/](http
s://freewebcart.com/essential-microsoft-powerpoint-course-for-everyone/)

&#x200B;

Support Vector Machines in Python: S
VM Concepts & Code

[https://freewebcart.com/support-vector-machines-in-python-svm-concepts-code/](https://freewebcart.c
om/support-vector-machines-in-python-svm-concepts-code/)

&#x200B;

Complete Video Editing Course With Motion Graphics


[https://freewebcart.com/complete-video-editing-course-with-motion-graphics/](https://freewebcart.com/complete-video-edi
ting-course-with-motion-graphics/)

&#x200B;

Complete Linear Regression Analysis in Python

[https://freewebcart.com/co
mplete-linear-regression-analysis-in-python/](https://freewebcart.com/complete-linear-regression-analysis-in-python/)

&
#x200B;

Adobe Illustrator Course for Graphics Design

[https://freewebcart.com/adobe-illustrator-course-for-graphics-de
sign/](https://freewebcart.com/adobe-illustrator-course-for-graphics-design/)

&#x200B;

Adobe After Effect Essential: L
earn Video Motion Animation

[https://freewebcart.com/adobe-after-effect-essential-learn-video-motion-animation/](https:
//freewebcart.com/adobe-after-effect-essential-learn-video-motion-animation/)

&#x200B;

SVM for Beginners: Support Vect
or Machines in R Studio

[https://freewebcart.com/svm-for-beginners-support-vector-machines-in-r-studio/](https://freewe
bcart.com/svm-for-beginners-support-vector-machines-in-r-studio/)

&#x200B;

Filmora 11/X/9: Zero to Hero in Video Editi
ng

[https://freewebcart.com/filmora-9-and-x-zero-to-hero-in-video-editing-2021/](https://freewebcart.com/filmora-9-and-
x-zero-to-hero-in-video-editing-2021/)

&#x200B;

Social Media Mastery 2023| Increase Customer Conversion Rate

[https:/
/freewebcart.com/social-media-mastery-increase-customer-conversion-rate/](https://freewebcart.com/social-media-mastery-i
ncrease-customer-conversion-rate/)

&#x200B;

Build from Scratch a Modern REST API with PHP 8

[https://freewebcart.com/
build-a-modern-rest-api-with-php-8/](https://freewebcart.com/build-a-modern-rest-api-with-php-8/)

&#x200B;

Learn HTML 
and CSS from Beginning to Advanced

[https://freewebcart.com/learn-html-and-css-from-beginning-to-advanced/](https://fre
ewebcart.com/learn-html-and-css-from-beginning-to-advanced/)

&#x200B;

Adobe Premiere Pro CC: Video Editing for Beginne
rs

[https://freewebcart.com/adobe-premiere-pro-cc-2021-video-editing-for-beginners/](https://freewebcart.com/adobe-prem
iere-pro-cc-2021-video-editing-for-beginners/)

&#x200B;

Adobe Photoshop CC Complete Mastery Course Basic to Advanced


[https://freewebcart.com/adobe-photoshop-cc-complete-mastery-course-basic-to-advanced/](https://freewebcart.com/adobe-ph
otoshop-cc-complete-mastery-course-basic-to-advanced/)

&#x200B;

Best Online Video Editor InVideo : 5+ Real World Proje
cts

[https://freewebcart.com/best-online-video-editor-invideo-5-real-world-projects/](https://freewebcart.com/best-onli
ne-video-editor-invideo-5-real-world-projects/)

&#x200B;

ChatGPT Prompt Engineering Mastery

[https://freewebcart.com/
chatgpt-prompt-engineering-mastery/](https://freewebcart.com/chatgpt-prompt-engineering-mastery/)

&#x200B;

Essential E
xcel With Tips Trick Shortcuts and Job Success

[https://freewebcart.com/essential-excel-with-tips-trick-shortcuts-and-j
ob-success/](https://freewebcart.com/essential-excel-with-tips-trick-shortcuts-and-job-success/)

&#x200B;

Videoscribe 
Whiteboard Animations : MasterClass With Project

[https://freewebcart.com/videoscribe-whiteboard-animations-masterclass
-with-project/](https://freewebcart.com/videoscribe-whiteboard-animations-masterclass-with-project/)

&#x200B;

Build a 
User Web App from Scratch with Vanilla PHP 8+

[https://freewebcart.com/build-a-full-user-web-app-from-scratch-with-vani
lla-php8/](https://freewebcart.com/build-a-full-user-web-app-from-scratch-with-vanilla-php8/)

&#x200B;

Build from Scra
tch a Modern REST API with PHP 8

[https://freewebcart.com/build-a-modern-rest-api-with-php-8/](https://freewebcart.com/
build-a-modern-rest-api-with-php-8/)

&#x200B;

C++ And PHP Complete Course for C++ and PHP Beginners

[https://freewebc
art.com/c-and-php-complete-course-2023/](https://freewebcart.com/c-and-php-complete-course-2023/)
```
---

     
 
all -  [ Got rejected for a Placement Offer after interning. And even my Manager was shocked. ](https://www.reddit.com/r/developersIndia/comments/1g5w64g/got_rejected_for_a_placement_offer_after/) , 2024-10-18-0912
```
So few days back, The company (huge Product based MNC) after a whole month of review , extended their Pre Placement Offe
rs to 2025 Undergraduates in which unfortunately I didn't get.
I was part of a Data Operations and Engineering team duri
ng my internship and me with another cointern came up with a GenAI solution to prepare a Data Validation Engine for the 
Data Product Platform which included a Semantic Table Recommendation based on Business Rule and a Natural Language Data 
Validation Platform with Dashboard to select , drag and drop and see end results. It was a complete Full Stack project f
or a 3year B.Tech student who straight got thrown into world of Oracle, PySpark, Langchain , NLP , React , FastAPI, and 
even we mounted the Dashboard as a specific route of API and almost prepared it for pre-production.

Now, our manager an
d other teammates (SDE I and II) said that this is a new team and one of most ambitious long term project and they are i
n need of personnel and based on what we accomplished in 2 months, they said they definitely wanted to see us back in Ja
nuary to improve the platform and actually push it into Production.

Also it's normal for the Company to push 90-100% co
nversion from Internship to Permanent Job offers from its last 3-4 year track record.

But everything changed, when the 
PPOs dropped in. Colleges were witnessing 30-50% conversion only and the conversions for the students didn't make any se
nse in any way. Though I was lucky enough to come back to college and get a backup Job Offer but I waited desperately fo
r this PPO since I felt like family in those two months and because of this I gave up my streaks of practice and got dev
iated from my own projects and everything. 
Today, I talked with one of my senior SDE from the team and he said that rev
iew of our work was impeccable and they were themselves shocked that we didn't get. My other co-intern who is also place
d in a backup offer had the same interaction who was himself shocked how could they cancel our PPOs.
The manager said , 
after they submitted the review and requirements, the HR gave no visibility to the managers themselves and hence no cons
ultation from the actual need was taken while extending. For a large organisation venturing deep into AI in daily life p
rojects, extending offers to 31/84 people and that too in Legacy Stack like C# , Java , Frontend was quite abnormal for 
the students. 

Though how much I pretend to be not affected by this event but deep down I am broken from inside. I work
ed day and night , I even worked from office every day where WFH was still there. 

Well, though I have this huge MNC in
ternship in experience, but in reality, I am not in that big of a college that anything I do can beat this company nor I
 was such consistent code-worm who kept on grinding Leetcode and DSA everyday. Now I am even worse than most in my colle
ge.

```
---

     
 
all -  [ Appending Tool Messages to the Final Response in a ReAct Agent
 ](https://www.reddit.com/r/LangChain/comments/1g5so66/appending_tool_messages_to_the_final_response_in/) , 2024-10-18-0912
```
I'm currently working on a ReAct agent using LangGraph, where I'm calling various endpoints (tools) to generate the fina
l answer. My endpoints gives the final response in the tool message which has the required answer that I want. The agent
's workflow is as follows:

1. The user query is received, and the appropriate tool is selected based on the query type 
(e.g., RAG for general queries,  Web Search for current events and some other tools).
2. The selected tool is called, an
d the response is generated.
3. Then using assistant call I get the final response which has just the response and not o
ther fields that were given by tool message.

My challenge is that the structure of the final response generated by the 
assistant does not match the desired structure. The tool-generated answers contain quite a lot of fields that I want to 
include in the final answer.  
 For example:

{ 'data\_points': \[\], 'answer': '', 'sources': '', 'followup\_questions'
: \[\], 'thoughts': '', 'indexes': \[\], 'query': '', 'total\_tokens': , 'prompt\_tokens': , 'completion\_tokens': , 'ca
che\_hit': , 'history': \[ { 'user': '' } \], 'prompt\_prefix': '', 'instructions': \[\], 'agent\_mode': '', 'references
': \[ { 'order': , 'url': '', 'number': } \] }

Ideally, I would like to take the ToolMessage from the state and append 
it to the final response to have more control over the response structure. This way, I can customize the final response 
to include all the relevant fields from the tool-generated answers. I tried structure output formatting but that did not
 work for me.  What would be the best to achieve this?
```
---

     
 
all -  [ AgentCraft Hackathon: Preperation Event Webinar 🚀 ](https://www.meetup.com/diamantai/events/304039632/?utm_medium=referral&utm_campaign=share-btn_savedevents_share_modal&utm_source=link) , 2024-10-18-0912
```
Get ready for the upcoming AgentCraft Hackathon in conjunction with LangChain with this essential online preparation eve
nt!

📅 Live Webinar:
- Europe: Tuesday, October 22nd, 19:00 IDT

- USA: Tuesday, October 22nd, 12:00 EST

🔍 Event Highli
ghts:
- 🧠 Hackathon Overview

- 💻 Building Your Tutorial Agent

- 👥 Team Formation

- 🌐 GitHub Collaboration

- 💡 Ideas 
for Agents

- 🏆 Prizes and Recognition

- 🎓 Educational Track

- 🔒 Registration Info

- 📜 Rules for a Valid Tutorial

- 
🎥 Submission Guidelines

Don't miss this chance to gear up for the hackathon, find teammates, and get crucial informatio
n to succeed!

Join the Meetup event now for all the details and to secure your spot
```
---

     
 
all -  [ How to Get Token Usage with astream in LangGraph ](https://www.reddit.com/r/LangChain/comments/1g5nz5g/how_to_get_token_usage_with_astream_in_langgraph/) , 2024-10-18-0912
```
Hey everyone,

I’m working with `langgraph` and trying to retrieve the token usage during streaming using `astream`. How
ever, I’m having trouble getting the token counts as documented.

Here’s a snippet of my current code:

    async for st
ep in graph.astream(state, config=config, stream_mode='values'):
        print(step)

But when I run it, I’m only gettin
g something like this:

    {
        'messages': [
            HumanMessage(content='hello', additional_kwargs={}, resp
onse_metadata={}, id='6ad01f76-5c39-4eb2-b0e3-e9ced1866c2a'),
            AIMessage(content='¡Hola! ¿En qué puedo ayudar
te hoy?', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-08-06', 'system_f
ingerprint': 'fp_a20a4ee344'}, id='run-caefe971-5c4a-45ac-9c94-938d6166f02d-0')
        ]
    }

Based on LangGraph's [d
ocumentation](https://langchain-ai.github.io/langgraph/how-tos/stream-values/#stream-values), I was expecting the token 
usage to be included in the `response_metadata`. It should look something like this:

    {
        'messages': [
      
      HumanMessage(content='what's the weather in sf', id='54b39b6f-054b-4306-980b-86905e48a6bc'),
            AIMessage
(content='', additional_kwargs={'tool_calls': [{'id': 'call_avoKnK8reERzTUSxrN9cgFxY', 'function': {'arguments': '{'city
':'sf'}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'pr
ompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_5e6c71d4a8', 'finish
_reason': 'tool_calls'}, id='run-f2f43c89-2c96-45f4-975c-2d0f22d0d2d1-0')
        ]
    }

Has anyone else encountered t
his issue or have any suggestions on how to ensure the token usage gets returned? Any help or tips would be much appreci
ated!

  
SOLVED: I just had to pass `stream_usage=True` to the LLM :D
```
---

     
 
all -  [ How to improve the performance of retrieval-augmented generation (RAG) models on time-relevant queri ](https://www.reddit.com/r/LangChain/comments/1g5nrbk/how_to_improve_the_performance_of/) , 2024-10-18-0912
```
**Problem Statement:** RAG models prioritize similarity between query and context, but struggle with time-sensitive quer
ies. I am using milvus, but open to other options as well. For instance:

* Retrieving information about a specific date
 (e.g., 'Can you tell me something about 22-June-2023?').
* Finding events or activities happening in a specific locatio
n at a specific time (e.g., 'What can I do next week in New York?')
* Determining the schedule of recurring events (e.g.
, 'When is the football season happening this year?')

**Challenge:** How to prioritize recent content when multiple sim
ilar contents exist? One potential solution is to rely on meta-data, but this approach has limitations:

* Requires fetc
hing all relevant content to filter by date
* Fails if the most recent content is not fetched
* I need to index all date
s in metadata

Any one have clue how to handle this problem?
```
---

     
 
all -  [ Choosing the Best Multilingual LLM for RAG-based Multilingual Chatbot Development ](https://www.reddit.com/r/LangChain/comments/1g5nfrg/choosing_the_best_multilingual_llm_for_ragbased/) , 2024-10-18-0912
```
Hi everyone,

I'm working on developing a multilingual chatbot using Retrieval-Augmented Generation (RAG). I'm currently
 looking for the best multilingual language model (LLM) that fits this purpose.

I’d appreciate any advice on the follow
ing:

* Are there existing benchmarks for RAG performance that focus on multilingual capabilities?
* Any recommendations
 for specific models that have performed well for multilingual tasks, especially in non-English contexts?

Thanks in adv
ance for any insights or experiences you can share!
```
---

     
 
all -  [ Udemy Free Courses for 17 October 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1g5n48x/udemy_free_courses_for_17_october_2024/) , 2024-10-18-0912
```
# Udemy Free Courses for 17 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19328/)Primavera P6 Unveiled: Step-by-Step Beginn
er’s Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19327/)Ethology for veterinerian an introduction
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/19326/)ChatGPT for Product Management & Innovation
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/19325/)Free Natural Language Processing (NLP) Tutorial – Natural Language Processing: A 3-
Step Process to Master NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19324/)Free Tutorial – Se déplacer au Gab
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19323/)Free Physics Tutorial – Basis of Vectors to solve Physics 
Problems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19322/)Free Tutorial – Corporate Learning and Development
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19321/)Free Forex Trading Tutorial – Forex Nedir ? Forex Piyasasında 
Nasıl Yatırım Yapılır ?
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19320/)Free Medical Writing Tutorial – Medic
al Writing For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19319/)Free Oracle Card Reading Tutorial – 
Intuitive Oracle Readings
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19318/)Free Tutorial – Mastering the Art o
f Journaling: Unlock Your Creativity
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19317/)Free Software Developmen
t Tutorial – Coding with Cursor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19316/)Free Data Analysis Tutorial –
 Master SQL and Databases in 30 Days: A Complete Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19315/)Free V
im Text Editor Tutorial – Learn Neovim The Hard Way ( Part 1 )
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19314
/)Free Tutorial – Learn “Simple Stupid Blogging” (Beginner Guide)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19
313/)Free Project Planning Tutorial – Planning 101: Learn the Basics of Effective Planning
* Free Tutorial – Anti-Burnou
t Blueprint: Sustainable Success in 24/7 World
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19312/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/19311/)Free Object-Oriented Design (OOD) Tutorial – Foundations of Object Oriented
 Design Principles Explained
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19310/)Free Generative AI (GenAI) Tutor
ial – Become an AI-Powered Engineer: Cursor, the AI-First IDE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19309/
)Free Salesforce Apex Tutorial – Working with Data in Apex – Part 2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
19308/)Free Web Development Tutorial – Cómo convertir un Diseño en Figma a una Página Web
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/19307/)Free Generative AI (GenAI) Tutorial – Using AI as your personal assistant
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/19306/)Free AI Agents Tutorial – Autogen Studio – Build Low Code Multi Agent AI Appli
cations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19305/)Learn MySQL – For Beginners
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/19304/)HTML & CSS – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/19303/)Internet and Web Development Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19302
/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19301/)Ultimate Guide 
to Product Design: Design Thinking Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19300/)Global Career Dev
elopment, Job Search, Interviewing Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19299/)Business Administra
tion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19298/)Master Splits & Conditioning for Martial or Performance 
Arts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19297/)\[NEW\] Master 90+ Linux Commands Line Practice & Learn 
(2024)
* Python And Flask Framework Complete Course
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19296/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/19295/)Mastering ChatGPT (AI) and PowerPoint presentation
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/19294/)Microsoft Excel – Beginner to Advance with Example
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/19293/)Executive Diploma of Chief Technology Officer
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/19292/)Professional Diploma in Public Relations and PR Management
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/19291/)The Complete Data Structures and Algorithms Course in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/19290/)Level 1 – Japanese Candlesticks Trading Mastery Program
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/19289/)Professional Diploma of the Executive Assistant
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19288/)Profe
ssional Diploma in Agile and Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19287/)Learn Spring Modulith: Mon
olith to Microservices Seamlessly
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19286/)\[NEW\] Mastering Cloud Com
puting Basic to Advanced Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19285/)Advanced Diploma in Techno
logy Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19284/)Excel Charts & Graphs: Master Class Excel Cha
rts & Graphs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19283/)Facing Cyber Threats: 7 Consequences and 11 Myth
s Exposed
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19282/)Cyber Security Essentials: 18 Expert Tips for Prote
ction
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19281/)Heron’s Formula Unleashed: The Triangle Calculator
* Ti
ps and Techniques for Crafting Captivating and Engaging
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19280/)
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/19279/)The Speech Writer’s Guide: Mastering the Craft
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/19278/)Mastering Clear and Concise Reports: The Art and Science
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19277/)Web Application Fundamentals: Building Your Foundation Part3
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19276/)Web Application Fundamentals: Building Your Foundation Part4
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19275/)Professional Diploma in Business English and Communications
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/19274/)Crafting a Winning Job Application: The Essentials
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/19273/)The Ultimate Resume Writing Guide: Crafting a Winning Prof
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/19272/)Resume Mastery: Crafting Your Career Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
19270/)Visualization techniques for Decision Makers and Leaders
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1926
9/)Generative AI For Leaders : The #1 surging skill for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19268/)
Introduction to Financial Products & Services
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19267/)Data Structures
 Algorithm DSA | Python+Javascript LEETCODE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19266/)The Art of Commun
ication: A Path to Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19265/)Introduction to ICT Skills: A Comp
rehensive Overview
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19264/)Web Application Fundamentals: Building You
r Foundation Part2
* Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/19263/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19262/)Python Programming Complete Beginners Co
urse Bootcamp 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19261/)ITS-303 Python Certification Exam IT Speci
alist Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19260/)Learn Guitar Chords: Electric & Acoustic fo
r All Levels
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19259/)AI Tools for UX UI Designers and Web Designers
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19258/)Comprehensive TypeScript Practice Exam: Basics to Advanced
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/19257/)HTML, CSS, Java, & JavaScript: Full Stack Programming Course
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/19256/)SK0-005: CompTIA Server+ Practice test 2024
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/19255/)XK0-005: CompTIA Linux+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/19254/)CV0-003: CompTIA Cloud+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1925
3/)FCP\_FAZ\_AD-7.4: FortiAnalyzer Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19252/)Google 
Slides: Full Guide to Creating Impactful Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19251/)CAS003:
 CompTIA Adv Security Practitioner Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19250/)CS0-003
: CompTIA CySA+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19249/)Microsoft Ads MasterClass 
– All Campaigns & Features
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19248/)CS0-001: CompTIA CySA+ Practice te
st 2024
* JN0-664: Juniper Network Professional Security Practice 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udem
y/19247/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19246/)JN0-683: Juniper Networks Specialist Security Pract
ice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19245/)2024 R Programming Bootcamp for Absolute Beginners
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19244/)CSS, JavaScript,PHP And Python Programming All in One Course
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19243/)Developing successful Professional Relationships
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/19242/)Hands On Python Data Science – Data Science Bootcamp
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/19241/)How to Make AI Videos: Mastering AI Text-to-Video Creation
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19240/)Advanced Program in Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19
239/)600+ React Interview Questions Practice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19238/)Beat anxiet
y by dealing with your trauma : in 5 easy steps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19237/)Python Progra
mming: Python Bootcamp For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19236/)Mastering Pointers in C 
: A Course on Efficient Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19235/)Java And C++ And PHP Cras
h Course All in One For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19234/)LangGraph Mastery: Develop 
LLM Agents with LangGraph
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19233/)LangChain Mastery:Develop LLM Apps 
with LangChain & Pinecone
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19232/)Microsoft Applied Skills: Gen AI so
lutions with Azure OpenAI
* Python 3: Fundamentals
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19231/)
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/19230/)Python 3: Deep Dive (Part 3 – Dictionaries, Sets, JSON)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/19229/)Python 3: Deep Dive (Part 2 – Iterators, Generators)
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19228/)Python 3: Deep Dive (Part 1 – Functional)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/19227/)Azure ChatGPT and OpenAI Service – The Complete Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/19226/)Computer Security: A Hands-on Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19225/)Internet Sec
urity: A Hands-on Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19224/)Web Security: A Hands-on Approach

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19223/)Spring 6 & Spring Boot 3 for Beginners (Includes 6 Projects)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19222/)Introduction to Machine Learning Models (AI) Testing
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/19221/)Core Java and Coding for Automation Testers – For Beginners
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/19220/)Curso de Gmail 2024, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/19219/)Cómo Ganar Dinero con YouTube 2024 | Curso de YouTube 2024
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/19218/)Cómo Transmitir en Vivo Por las Redes Sociales 2024
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/19217/)NVIDIA-Certified Associate: Generative AI LLMs – Mock Exams
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/19216/)SQL Essentials – Thinking in SQL form Beginners to Pro

GET MORE FREE ONLINE COURSES WITH CERTI
FICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Udemy Free Courses for 17 October 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1g5n46e/udemy_free_courses_for_17_october_2024/) , 2024-10-18-0912
```
# Udemy Free Courses for 17 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19328/)Primavera P6 Unveiled: Step-by-Step Beginn
er’s Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19327/)Ethology for veterinerian an introduction
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/19326/)ChatGPT for Product Management & Innovation
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/19325/)Free Natural Language Processing (NLP) Tutorial – Natural Language Processing: A 3-
Step Process to Master NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19324/)Free Tutorial – Se déplacer au Gab
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19323/)Free Physics Tutorial – Basis of Vectors to solve Physics 
Problems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19322/)Free Tutorial – Corporate Learning and Development
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19321/)Free Forex Trading Tutorial – Forex Nedir ? Forex Piyasasında 
Nasıl Yatırım Yapılır ?
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19320/)Free Medical Writing Tutorial – Medic
al Writing For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19319/)Free Oracle Card Reading Tutorial – 
Intuitive Oracle Readings
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19318/)Free Tutorial – Mastering the Art o
f Journaling: Unlock Your Creativity
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19317/)Free Software Developmen
t Tutorial – Coding with Cursor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19316/)Free Data Analysis Tutorial –
 Master SQL and Databases in 30 Days: A Complete Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19315/)Free V
im Text Editor Tutorial – Learn Neovim The Hard Way ( Part 1 )
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19314
/)Free Tutorial – Learn “Simple Stupid Blogging” (Beginner Guide)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19
313/)Free Project Planning Tutorial – Planning 101: Learn the Basics of Effective Planning
* Free Tutorial – Anti-Burnou
t Blueprint: Sustainable Success in 24/7 World
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19312/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/19311/)Free Object-Oriented Design (OOD) Tutorial – Foundations of Object Oriented
 Design Principles Explained
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19310/)Free Generative AI (GenAI) Tutor
ial – Become an AI-Powered Engineer: Cursor, the AI-First IDE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19309/
)Free Salesforce Apex Tutorial – Working with Data in Apex – Part 2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
19308/)Free Web Development Tutorial – Cómo convertir un Diseño en Figma a una Página Web
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/19307/)Free Generative AI (GenAI) Tutorial – Using AI as your personal assistant
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/19306/)Free AI Agents Tutorial – Autogen Studio – Build Low Code Multi Agent AI Appli
cations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19305/)Learn MySQL – For Beginners
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/19304/)HTML & CSS – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/19303/)Internet and Web Development Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19302
/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19301/)Ultimate Guide 
to Product Design: Design Thinking Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19300/)Global Career Dev
elopment, Job Search, Interviewing Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19299/)Business Administra
tion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19298/)Master Splits & Conditioning for Martial or Performance 
Arts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19297/)\[NEW\] Master 90+ Linux Commands Line Practice & Learn 
(2024)
* Python And Flask Framework Complete Course
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19296/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/19295/)Mastering ChatGPT (AI) and PowerPoint presentation
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/19294/)Microsoft Excel – Beginner to Advance with Example
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/19293/)Executive Diploma of Chief Technology Officer
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/19292/)Professional Diploma in Public Relations and PR Management
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/19291/)The Complete Data Structures and Algorithms Course in Python
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/19290/)Level 1 – Japanese Candlesticks Trading Mastery Program
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/19289/)Professional Diploma of the Executive Assistant
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19288/)Profe
ssional Diploma in Agile and Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19287/)Learn Spring Modulith: Mon
olith to Microservices Seamlessly
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19286/)\[NEW\] Mastering Cloud Com
puting Basic to Advanced Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19285/)Advanced Diploma in Techno
logy Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19284/)Excel Charts & Graphs: Master Class Excel Cha
rts & Graphs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19283/)Facing Cyber Threats: 7 Consequences and 11 Myth
s Exposed
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19282/)Cyber Security Essentials: 18 Expert Tips for Prote
ction
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19281/)Heron’s Formula Unleashed: The Triangle Calculator
* Ti
ps and Techniques for Crafting Captivating and Engaging
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19280/)
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/19279/)The Speech Writer’s Guide: Mastering the Craft
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/19278/)Mastering Clear and Concise Reports: The Art and Science
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19277/)Web Application Fundamentals: Building Your Foundation Part3
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19276/)Web Application Fundamentals: Building Your Foundation Part4
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19275/)Professional Diploma in Business English and Communications
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/19274/)Crafting a Winning Job Application: The Essentials
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/19273/)The Ultimate Resume Writing Guide: Crafting a Winning Prof
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/19272/)Resume Mastery: Crafting Your Career Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
19270/)Visualization techniques for Decision Makers and Leaders
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1926
9/)Generative AI For Leaders : The #1 surging skill for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19268/)
Introduction to Financial Products & Services
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19267/)Data Structures
 Algorithm DSA | Python+Javascript LEETCODE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19266/)The Art of Commun
ication: A Path to Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19265/)Introduction to ICT Skills: A Comp
rehensive Overview
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19264/)Web Application Fundamentals: Building You
r Foundation Part2
* Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/19263/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19262/)Python Programming Complete Beginners Co
urse Bootcamp 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19261/)ITS-303 Python Certification Exam IT Speci
alist Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19260/)Learn Guitar Chords: Electric & Acoustic fo
r All Levels
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19259/)AI Tools for UX UI Designers and Web Designers
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19258/)Comprehensive TypeScript Practice Exam: Basics to Advanced
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/19257/)HTML, CSS, Java, & JavaScript: Full Stack Programming Course
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/19256/)SK0-005: CompTIA Server+ Practice test 2024
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/19255/)XK0-005: CompTIA Linux+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/19254/)CV0-003: CompTIA Cloud+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1925
3/)FCP\_FAZ\_AD-7.4: FortiAnalyzer Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19252/)Google 
Slides: Full Guide to Creating Impactful Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19251/)CAS003:
 CompTIA Adv Security Practitioner Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19250/)CS0-003
: CompTIA CySA+ Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19249/)Microsoft Ads MasterClass 
– All Campaigns & Features
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19248/)CS0-001: CompTIA CySA+ Practice te
st 2024
* JN0-664: Juniper Network Professional Security Practice 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udem
y/19247/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19246/)JN0-683: Juniper Networks Specialist Security Pract
ice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19245/)2024 R Programming Bootcamp for Absolute Beginners
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19244/)CSS, JavaScript,PHP And Python Programming All in One Course
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19243/)Developing successful Professional Relationships
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/19242/)Hands On Python Data Science – Data Science Bootcamp
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/19241/)How to Make AI Videos: Mastering AI Text-to-Video Creation
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19240/)Advanced Program in Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19
239/)600+ React Interview Questions Practice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19238/)Beat anxiet
y by dealing with your trauma : in 5 easy steps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19237/)Python Progra
mming: Python Bootcamp For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19236/)Mastering Pointers in C 
: A Course on Efficient Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19235/)Java And C++ And PHP Cras
h Course All in One For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19234/)LangGraph Mastery: Develop 
LLM Agents with LangGraph
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19233/)LangChain Mastery:Develop LLM Apps 
with LangChain & Pinecone
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19232/)Microsoft Applied Skills: Gen AI so
lutions with Azure OpenAI
* Python 3: Fundamentals
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19231/)
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/19230/)Python 3: Deep Dive (Part 3 – Dictionaries, Sets, JSON)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/19229/)Python 3: Deep Dive (Part 2 – Iterators, Generators)
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/19228/)Python 3: Deep Dive (Part 1 – Functional)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/19227/)Azure ChatGPT and OpenAI Service – The Complete Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/19226/)Computer Security: A Hands-on Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19225/)Internet Sec
urity: A Hands-on Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19224/)Web Security: A Hands-on Approach

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19223/)Spring 6 & Spring Boot 3 for Beginners (Includes 6 Projects)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19222/)Introduction to Machine Learning Models (AI) Testing
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/19221/)Core Java and Coding for Automation Testers – For Beginners
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/19220/)Curso de Gmail 2024, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/19219/)Cómo Ganar Dinero con YouTube 2024 | Curso de YouTube 2024
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/19218/)Cómo Transmitir en Vivo Por las Redes Sociales 2024
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/19217/)NVIDIA-Certified Associate: Generative AI LLMs – Mock Exams
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/19216/)SQL Essentials – Thinking in SQL form Beginners to Pro

GET MORE FREE ONLINE COURSES WITH CERTI
FICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Gemini endpoint url ](https://www.reddit.com/r/LangChain/comments/1g5coqw/gemini_endpoint_url/) , 2024-10-18-0912
```
Where can we find the endpoint URL to use the Gemini API key? Has anyone else encountered a similar issue while using th
e Gemini API key?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1g5alz7/list_of_free_and_best_selling_discounted_courses/) , 2024-10-18-0912
```
# Udemy Free Courses for 17 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19234/)LangGraph Mastery: Develop LLM Agents with
 LangGraph
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19233/)LangChain Mastery:Develop LLM Apps with LangChain 
& Pinecone
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19232/)Microsoft Applied Skills: Gen AI solutions with Az
ure OpenAI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19231/)Python 3: Fundamentals
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/19230/)Python 3: Deep Dive (Part 3 – Dictionaries, Sets, JSON)
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/19229/)Python 3: Deep Dive (Part 2 – Iterators, Generators)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/19228/)Python 3: Deep Dive (Part 1 – Functional)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19227/)
Azure ChatGPT and OpenAI Service – The Complete Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19226/)Compute
r Security: A Hands-on Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19225/)Internet Security: A Hands-on
 Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19224/)Web Security: A Hands-on Approach
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/19223/)Spring 6 & Spring Boot 3 for Beginners (Includes 6 Projects)
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/19222/)Introduction to Machine Learning Models (AI) Testing
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/19221/)Core Java and Coding for Automation Testers – For Beginners
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/19220/)Curso de Gmail 2024, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/19219/)Cómo Ganar Dinero con YouTube 2024 | Curso de YouTube 2024
* Cómo Transmitir en Vivo Por las Redes S
ociales 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19218/)
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/19217/)NVIDIA-Certified Associate: Generative AI LLMs – Mock Exams
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/19216/)SQL Essentials – Thinking in SQL form Beginners to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/192
15/)300-815: Implementing Cisco Adv Call Control Mobilie 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19214/
)300-810: Implementing Cisco Collaboration Applications 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19213/)
300-730: Implementing Secure Solutions with VPN 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19212/)300-735:
 Automating Programming Cisco Security Solution 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19211/)300-725:
 Securing the Web with Cisco Web Security 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19210/)300-720: Secur
ing Email with Cisco Email Security 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19209/)2V0-21.23: Professio
nal VMware vSphere 8.x Practice Exam 24
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19208/)300-835: Automating C
isco Collaboration Solutions 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19207/)300-910: Implementing DevOp
s Solutions and Practices 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19206/)350-201: Implementing Cisco Cy
berOps Core Technologies 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19205/)350-401: Implementing Operating
 Cisco Network 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19204/)350-501: Implementing Operating Cisco Ser
vice Provider 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19203/)350-601: Implementing and Operating Cisco 
Data Center 2024
* 400-007: CCIE Security Written Exam 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19202/)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19201/)500-230: Implementing Cisco Business Resiliency 2024
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/19200/)500-210: Implementing Cisco Business Resiliency 2024
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/19199/)500-052: Implementing Cisco IP Telephony Video, Part 1 2024
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/19198/)400-101: Implementing Cisco IP Routing 2024
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/19197/)350-901: Developing Applications Using Cisco Core 2024
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/19196/)350-701: Implementing and Operating Cisco Security Core 2024
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/19195/)70-347: Enabling Office 365 Services Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/19194/)500-490: Implementing Cisco Collaboration Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
19193/)500-560: Implementing Cisco Collaboration Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19192/
)500-325: Implementing Cisco Collaboration Applications 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19191/)
500-285: Implementing Cisco Collaboration Applications 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19190/)5
00-275: Implementing Cisco Collaboration Applications 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19189/)50
0-240: Implementing Cisco Business Resiliency 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19188/)70-412: Co
nfig Adv Windows Server 2012 Service Practice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19187/)70-414: Im
plementing Windows Server 2012 Practice Test 2024
* 70-417: Upgrade MCSA Windows Server 2012 Practice Test 2024
* [REDEE
M OFFER](https://idownloadcoupon.com/udemy/19186/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19185/)70-448: Mi
crosoft SQL Server 2008 R2 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19184/)70-487: Develop
 Windows Azure Web Service Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19183/)70-489: Develop
ing Microsoft SharePoint Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19182/)70-492: Adv Micro
soft SharePoint Server Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19181/)700-680: Cisco Data
 Center Unified Computing Sale Specialist
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19180/)700-651: Cisco Coll
aboration Cloud and Managed Services Sale
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19179/)700-551: Cisco Clou
d and Managed Services Sales Specialist
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19178/)70-687: Configuring W
indows 8 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19177/)70-686: Windows Desktop Technicia
n Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19176/)70-528: TS: Microsoft .NET Framework 2.0
 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19175/)Advanced Program in Product & CX Manageme
nt and Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19174/)Business development and sales processes –
 a bird’s eye view
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19173/)Breakthrough Practices for Safer Schools
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19172/)700-765: Cisco IoT Solutions Sales Specialist Exam
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/19171/)700-905: Cisco DevNet Professional Exam
* 700-751: Cisco CyberOps Profes
sional Exam
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19170/)
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/19169/)700-750: Cisco CyberOps Associate Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19168/)C-level mana
gement: 20 models for business operations (3/5)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19167/)C++ And PHP C
omplete Course for C++ and PHP Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19166/)CISA: Information Sy
stems Auditor Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19165/)Microsoft Azure: Hands On 
Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19164/)AZ 104 – Manage Identities
 and Governance in Azure
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19163/)CLF-C02: AWS Certified Cloud Practit
ioner Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19162/)Cloud Engineer (Google) Practice Tes
t – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19161/)Google Cloud (GCP) MasterClass : GCP Live Projects 2
024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19160/)Fortinet (NSE-4): Network Security Practice Test – 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19159/)Ethically Hack the Planet Part 4
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/19158/)DA-104: Tableau Desktop Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/19157/)Complete Python For Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19156/)JN0-335:
 Juniper Networks Specialist Security Practice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19155/)JN0-280: 
Juniper Networks Specialist Cloud Security Practice
* JN0-252: Juniper Networks Specialist Cloud Practice 2024
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/19154/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19153/)JN0-231: Ju
niper Networks Specialist Security Ptactice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19152/)JN0-230: Jun
iper Networks Associate Security Practice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19151/)JN0-104: Junip
er Networks Internet Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19150/)How neuromarketing 
can influence buying behavior
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19149/)JN0-349: Juniper Network Profes
sional Security Practice 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19148/)JN0-351: Juniper Network Profes
sional Data Cente Practice 24
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19147/)JN0-648: Juniper Networks Exper
t Security Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19146/)Leadership – Leading a Communit
y
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19145/)PCCSA: Palo Alto Network Cyber Security Practice Test -2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19144/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/19143/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/19142/)VCP550: VMware Data Center Practice Test -2024
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/19141/)SC-400: Microsoft Info Protection Admin Practice Test 2024
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/19140/)SAA-C03 AWS Certified Solutions Architect Associate Practice
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/19139/)Professional Scrum Master PSM 1 / PSM1 Mock Exams | 2023
* CentOS Linux and Ubuntu Linux: 
Managing Packages
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/19138/)
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/19137/)Python Data Structures & Algorithms: Ace Coding Interviews
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/19136/)Peak Performance: the 7 essentials for sales supremacy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/19135/)Executive Diploma in Sales and Service Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19134/)Jav
aScript From Scratch ( Part 1 – Beginner Level)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19133/)Discover Your
 Business Priority
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19132/)Master the Basics of Paleo Diet
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/19131/)Problem Solving with C++ programming language
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/19130/)Python Programming Language (Practice Projects)
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/19129/)Mastering HTML5 and CSS3 (Part 2 – Intermediate Level)
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/19128/)Google Analytics 4 (GA4) Certification. How to Pass the Exam
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/19127/)Reputation Management: Take Control of Your Company’s Image
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/19126/)Instagram Marketing. How to Promote Your Business!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/191
25/)Facebook Marketing 2024. Promote Your Business on Facebook!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1912
4/)Project Management Fundamentals: A Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/19123/)B2B Ou
tbound Lead Generation Mastery

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com
/)
```
---

     
 
all -  [ [October 17] Enroll Now: Free Udemy Course Available Today ](https://www.reddit.com/r/udemyfreebies/comments/1g592jt/october_17_enroll_now_free_udemy_course_available/) , 2024-10-18-0912
```
Python Programming for Beginners: Learn Python from Scratch

[https://freewebcart.com/python-programming-for-beginners-l
earn-python-from-scratch/](https://freewebcart.com/python-programming-for-beginners-learn-python-from-scratch/)

&#x200B
;

Python for Data Science: Python Programming & Data Analysis

[https://freewebcart.com/python-for-data-science-python-
programming-data-analysis/](https://freewebcart.com/python-for-data-science-python-programming-data-analysis/)

&#x200B;


Learn ChatGPT, Midjourney, AI and Use it For Passive Income

[https://freewebcart.com/learn-chatgpt-midjourney-ai-and-
use-it-for-passive-income/](https://freewebcart.com/learn-chatgpt-midjourney-ai-and-use-it-for-passive-income/)

&#x200B
;

Zero to Hero in Ollama: Create Local LLM Applications

[https://freewebcart.com/zero-to-hero-in-ollama-create-local-l
lm-applications/](https://freewebcart.com/zero-to-hero-in-ollama-create-local-llm-applications/)

&#x200B;

Adobe Illust
rator CC for Learning Graphics Design

[https://freewebcart.com/adobe-illustrator-cc-for-learning-graphics-design/](http
s://freewebcart.com/adobe-illustrator-cc-for-learning-graphics-design/)

&#x200B;

Adobe InDesign CC for Beginner to Adv
anced Masterclass

[https://freewebcart.com/adobe-indesign-cc-for-beginner-to-advanced-masterclass/](https://freewebcart
.com/adobe-indesign-cc-for-beginner-to-advanced-masterclass/)

&#x200B;

Advanced MS Word Excel PowerPoint Course for Jo
b Success

[https://freewebcart.com/advanced-ms-word-excel-powerpoint-course-for-job-success/](https://freewebcart.com/a
dvanced-ms-word-excel-powerpoint-course-for-job-success/)

&#x200B;

The Complete Guide to Instagram Marketing for Busin
esses

[https://freewebcart.com/the-complete-guide-to-instagram-marketing-for-businesses/](https://freewebcart.com/the-c
omplete-guide-to-instagram-marketing-for-businesses/)

&#x200B;

The Complete T-Shirt Design Toolkit: PS, AI & Canva

[h
ttps://freewebcart.com/the-complete-t-shirt-design-toolkit-ps-ai-canva/](https://freewebcart.com/the-complete-t-shirt-de
sign-toolkit-ps-ai-canva/)

&#x200B;

Figma for User Interface and User Experience UIUX Design

[https://freewebcart.com
/figma-for-user-interface-and-user-experience-uiux-design/](https://freewebcart.com/figma-for-user-interface-and-user-ex
perience-uiux-design/)

&#x200B;

Zero to Hero in LangChain: Build GenAI apps using LangChain

[https://freewebcart.com/
zero-to-hero-in-langchain-build-genai-apps-using-langchain/](https://freewebcart.com/zero-to-hero-in-langchain-build-gen
ai-apps-using-langchain/)

&#x200B;

Mastering HTML5 and CSS3 (Part 2 - Intermediate Level)

[https://freewebcart.com/ma
stering-html5-and-css3-part-2-intermediate-level/](https://freewebcart.com/mastering-html5-and-css3-part-2-intermediate-
level/)

&#x200B;

Java Masterclass: The Complete Guide

[https://freewebcart.com/java-masterclass-the-ultimate-beginner
s-guide/](https://freewebcart.com/java-masterclass-the-ultimate-beginners-guide/)

&#x200B;

Mastering React: React Cras
h Course with Mini Projects

[https://freewebcart.com/mastering-react-react-crash-course-with-mini-projects/](https://fr
eewebcart.com/mastering-react-react-crash-course-with-mini-projects/)

&#x200B;

Python Crash Course: Dive into Coding w
ith Hands-On Projects

[https://freewebcart.com/python-crash-dive-into-coding-with-hands-on-projects/](https://freewebca
rt.com/python-crash-dive-into-coding-with-hands-on-projects/)

&#x200B;

Windows Server with PowerShell: Active Director
y

[https://freewebcart.com/windows-server-with-powershell-active-directory/](https://freewebcart.com/windows-server-wit
h-powershell-active-directory/)

&#x200B;

Python Complete Course And Flask Framework, HTML Essentials

[https://freeweb
cart.com/python-complete-course-and-flask-framework-html-essentials/](https://freewebcart.com/python-complete-course-and
-flask-framework-html-essentials/)

&#x200B;

Master Logo Design with Photoshop Illustrator Zero to Pro

[https://freewe
bcart.com/master-logo-design-with-photoshop-illustrator-zero-to-pro/](https://freewebcart.com/master-logo-design-with-ph
otoshop-illustrator-zero-to-pro/)

&#x200B;

AI Tools for UX UI Designers and Web Designers

[https://freewebcart.com/be
st-ai-tools-for-ux-ui-designers-and-web-designers/](https://freewebcart.com/best-ai-tools-for-ux-ui-designers-and-web-de
signers/)

&#x200B;

Microsoft Ads MasterClass - All Campaigns & Features

[https://freewebcart.com/microsoft-ads-master
class-2024-all-campaigns-features/](https://freewebcart.com/microsoft-ads-masterclass-2024-all-campaigns-features/)

&#x
200B;

Python Programming Complete Beginners Course Bootcamp 2024

[https://freewebcart.com/learn-python-from-scratch-it
s-usage-by-nasa-in-mars-rovers/](https://freewebcart.com/learn-python-from-scratch-its-usage-by-nasa-in-mars-rovers/)

&
#x200B;

Object Oriented Programming in C++ & Interview Preparation

[https://freewebcart.com/object-oriented-programmin
g-in-c-interview-preparation/](https://freewebcart.com/object-oriented-programming-in-c-interview-preparation/)

&#x200B
;

Google Slides: Full Guide to Creating Impactful Presentation

[https://freewebcart.com/google-slides-full-guide-to-cr
eating-impactful-presentation/](https://freewebcart.com/google-slides-full-guide-to-creating-impactful-presentation/)

&
#x200B;

Salesforce Fundamentals : A Complete Guide for Beginners

[https://freewebcart.com/salesforce-fundamentals-a-co
mplete-guide-for-beginners/](https://freewebcart.com/salesforce-fundamentals-a-complete-guide-for-beginners/)

&#x200B;


2024 R Programming Bootcamp for Absolute Beginners

[https://freewebcart.com/2022-r-programming-bootcamp/](https://free
webcart.com/2022-r-programming-bootcamp/)

&#x200B;

Mastering Pointers in C : A Course on Efficient Programming

[https
://freewebcart.com/mastering-pointers-in-c-a-course-on-efficient-programming/](https://freewebcart.com/mastering-pointer
s-in-c-a-course-on-efficient-programming/)

&#x200B;

CSS, JavaScript,PHP And Python Programming All in One Course

[htt
ps://freewebcart.com/css-javascriptphp-and-python-programming-all-in-one-course/](https://freewebcart.com/css-javascript
php-and-python-programming-all-in-one-course/)

&#x200B;

How to Make AI Videos: Mastering AI Text-to-Video Creation

[h
ttps://freewebcart.com/how-to-make-ai-videos-mastering-ai-text-to-video-creation/](https://freewebcart.com/how-to-make-a
i-videos-mastering-ai-text-to-video-creation/)

&#x200B;

Master AI-Powered Chatbots, 24/7 Appointment Booking with AI


[https://freewebcart.com/master-ai-powered-chatbots-24-7-appointment-booking-with-ai/](https://freewebcart.com/master-ai
-powered-chatbots-24-7-appointment-booking-with-ai/)

&#x200B;

Microsoft Excel - Beginner to Advance with Example

[htt
ps://freewebcart.com/learn-excel-from-beginner-to-advance-with-example/](https://freewebcart.com/learn-excel-from-beginn
er-to-advance-with-example/)

&#x200B;

Mastering ChatGPT (AI) and PowerPoint presentation

[https://freewebcart.com/mas
tering-chatgpt-ai-and-powerpoint-presentation/](https://freewebcart.com/mastering-chatgpt-ai-and-powerpoint-presentation
/)

&#x200B;

Problem Solving with C++ programming language

[https://freewebcart.com/problem-solving-with-c-programming
-languages/](https://freewebcart.com/problem-solving-with-c-programming-languages/)

&#x200B;

Python Data Structures & 
Algorithms: Ace Coding Interviews

[https://freewebcart.com/python-data-structures-algorithms-ace-coding-interviews/](ht
tps://freewebcart.com/python-data-structures-algorithms-ace-coding-interviews/)

&#x200B;

JavaScript From Scratch ( Par
t 1 - Beginner Level)

[https://freewebcart.com/javascript-from-scratch-part-1-beginner-level/](https://freewebcart.com/
javascript-from-scratch-part-1-beginner-level/)

&#x200B;

CentOS Linux and Ubuntu Linux: Managing Packages

[https://fr
eewebcart.com/centos-linux-and-ubuntu-linux-managing-packages/](https://freewebcart.com/centos-linux-and-ubuntu-linux-ma
naging-packages/)

&#x200B;

Mastering HTML5 and CSS3 (Part 2 - Intermediate Level)

[https://freewebcart.com/mastering-
html5-and-css3-part-2-intermediate-level/](https://freewebcart.com/mastering-html5-and-css3-part-2-intermediate-level/)


&#x200B;

Build a Backend REST API with Node JS from Scratch

[https://freewebcart.com/learn-how-to-build-a-backend-res
t-api-with-node-js/](https://freewebcart.com/learn-how-to-build-a-backend-rest-api-with-node-js/)

&#x200B;

Master of E
ssential C++ Programming Beginner to Advanced

[https://freewebcart.com/master-of-essential-c-programming-beginner-to-ad
vanced/](https://freewebcart.com/master-of-essential-c-programming-beginner-to-advanced/)

&#x200B;

C# Test Automation 
Engineer - from Zero to Hero

[https://freewebcart.com/c-test-automation-engineer-from-zero-to-hero/](https://freewebcar
t.com/c-test-automation-engineer-from-zero-to-hero/)

&#x200B;

Build a Backend REST API with Node JS from Scratch

[htt
ps://freewebcart.com/learn-how-to-build-a-backend-rest-api-with-node-js/](https://freewebcart.com/learn-how-to-build-a-b
ackend-rest-api-with-node-js/)

&#x200B;

Build Complete PHP MySQL Food Ordering Ecommerce Store

[https://freewebcart.c
om/build-complete-2023-php-mysql-food-ordering-ecommerce-store/](https://freewebcart.com/build-complete-2023-php-mysql-f
ood-ordering-ecommerce-store/)

&#x200B;

Master Filmora: Editing, Motion Graphics, and Color Grading

[https://freewebc
art.com/master-filmora-editing-motion-graphics-and-colorgrading/](https://freewebcart.com/master-filmora-editing-motion-
graphics-and-colorgrading/)

&#x200B;

Social Media Video Editing With Premiere Pro Canva Filmora

[https://freewebcart.
com/social-media-video-editing-with-premiere-pro-canva-filmora/](https://freewebcart.com/social-media-video-editing-with
-premiere-pro-canva-filmora/)

&#x200B;

Complete Python For Absolute Beginners

[https://freewebcart.com/complete-pytho
n-2023-for-absolute-beginners/](https://freewebcart.com/complete-python-2023-for-absolute-beginners/)

&#x200B;

Python 
for Everyone Master the Basics of Programming

[https://freewebcart.com/python-for-everyone-master-the-basics-of-program
ming/](https://freewebcart.com/python-for-everyone-master-the-basics-of-programming/)

&#x200B;

Mastering Database Mana
gement with Knex.js and PostgreSQL

[https://freewebcart.com/mastering-database-management-with-knex-js-and-postgresql/]
(https://freewebcart.com/mastering-database-management-with-knex-js-and-postgresql/)

&#x200B;

Learn UI UX Design Adobe
 XD : Learn User Experience Design

[https://freewebcart.com/learn-ui-ux-design-adobe-xd-learn-user-experience-design/](
https://freewebcart.com/learn-ui-ux-design-adobe-xd-learn-user-experience-design/)

&#x200B;

Excel Analytics: Linear Re
gression Analysis in MS Excel

[https://freewebcart.com/excel-analytics-linear-regression-analysis-in-ms-excel/](https:/
/freewebcart.com/excel-analytics-linear-regression-analysis-in-ms-excel/)

&#x200B;

C# Mastering Course For Beginners


[https://freewebcart.com/c-mastering-course-for-beginners/](https://freewebcart.com/c-mastering-course-for-beginners/)


&#x200B;

Metasploit from Scratch: Beginner to Professional

[https://freewebcart.com/metasploit-from-scratch-beginner-t
o-professional/](https://freewebcart.com/metasploit-from-scratch-beginner-to-professional/)

&#x200B;

ChatGPT Mastercla
ss: The Ultimate Beginner's Guide!

[https://freewebcart.com/chatgpt-masterclass-the-ultimate-beginners-guide/](https://
freewebcart.com/chatgpt-masterclass-the-ultimate-beginners-guide/)

&#x200B;

Essential Microsoft PowerPoint Course for 
Everyone

[https://freewebcart.com/essential-microsoft-powerpoint-course-for-everyone/](https://freewebcart.com/essentia
l-microsoft-powerpoint-course-for-everyone/)

&#x200B;

Support Vector Machines in Python: SVM Concepts & Code

[https:/
/freewebcart.com/support-vector-machines-in-python-svm-concepts-code/](https://freewebcart.com/support-vector-machines-i
n-python-svm-concepts-code/)

&#x200B;

Complete Video Editing Course With Motion Graphics

[https://freewebcart.com/com
plete-video-editing-course-with-motion-graphics/](https://freewebcart.com/complete-video-editing-course-with-motion-grap
hics/)

&#x200B;

Complete Linear Regression Analysis in Python

[https://freewebcart.com/complete-linear-regression-ana
lysis-in-python/](https://freewebcart.com/complete-linear-regression-analysis-in-python/)

&#x200B;

Adobe Illustrator C
ourse for Graphics Design

[https://freewebcart.com/adobe-illustrator-course-for-graphics-design/](https://freewebcart.c
om/adobe-illustrator-course-for-graphics-design/)

&#x200B;

Adobe After Effect Essential: Learn Video Motion Animation


[https://freewebcart.com/adobe-after-effect-essential-learn-video-motion-animation/](https://freewebcart.com/adobe-afte
r-effect-essential-learn-video-motion-animation/)

&#x200B;

SVM for Beginners: Support Vector Machines in R Studio

[ht
tps://freewebcart.com/svm-for-beginners-support-vector-machines-in-r-studio/](https://freewebcart.com/svm-for-beginners-
support-vector-machines-in-r-studio/)

&#x200B;

Filmora 11/X/9: Zero to Hero in Video Editing

[https://freewebcart.com
/filmora-9-and-x-zero-to-hero-in-video-editing-2021/](https://freewebcart.com/filmora-9-and-x-zero-to-hero-in-video-edit
ing-2021/)

&#x200B;

Social Media Mastery 2023| Increase Customer Conversion Rate

[https://freewebcart.com/social-medi
a-mastery-increase-customer-conversion-rate/](https://freewebcart.com/social-media-mastery-increase-customer-conversion-
rate/)

&#x200B;

Build from Scratch a Modern REST API with PHP 8

[https://freewebcart.com/build-a-modern-rest-api-with
-php-8/](https://freewebcart.com/build-a-modern-rest-api-with-php-8/)

&#x200B;

Learn HTML and CSS from Beginning to Ad
vanced

[https://freewebcart.com/learn-html-and-css-from-beginning-to-advanced/](https://freewebcart.com/learn-html-and-
css-from-beginning-to-advanced/)

&#x200B;

Adobe Premiere Pro CC: Video Editing for Beginners

[https://freewebcart.com
/adobe-premiere-pro-cc-2021-video-editing-for-beginners/](https://freewebcart.com/adobe-premiere-pro-cc-2021-video-editi
ng-for-beginners/)

&#x200B;

Python And Django Framework And HTML 5 Stack Complete Course

[https://freewebcart.com/pyt
hon-and-django-framework-and-html-5-complete-course-2022/](https://freewebcart.com/python-and-django-framework-and-html-
5-complete-course-2022/)

&#x200B;

Adobe Photoshop CC Complete Mastery Course Basic to Advanced

[https://freewebcart.c
om/adobe-photoshop-cc-complete-mastery-course-basic-to-advanced/](https://freewebcart.com/adobe-photoshop-cc-complete-ma
stery-course-basic-to-advanced/)

&#x200B;

Best Online Video Editor InVideo : 5+ Real World Projects

[https://freewebc
art.com/best-online-video-editor-invideo-5-real-world-projects/](https://freewebcart.com/best-online-video-editor-invide
o-5-real-world-projects/)

&#x200B;

ChatGPT Prompt Engineering Mastery

[https://freewebcart.com/chatgpt-prompt-enginee
ring-mastery/](https://freewebcart.com/chatgpt-prompt-engineering-mastery/)

&#x200B;

Essential Excel With Tips Trick S
hortcuts and Job Success

[https://freewebcart.com/essential-excel-with-tips-trick-shortcuts-and-job-success/](https://f
reewebcart.com/essential-excel-with-tips-trick-shortcuts-and-job-success/)

&#x200B;

Videoscribe Whiteboard Animations 
: MasterClass With Project

[https://freewebcart.com/videoscribe-whiteboard-animations-masterclass-with-project/](https:
//freewebcart.com/videoscribe-whiteboard-animations-masterclass-with-project/)

&#x200B;

Build a User Web App from Scra
tch with Vanilla PHP 8+

[https://freewebcart.com/build-a-full-user-web-app-from-scratch-with-vanilla-php8/](https://fre
ewebcart.com/build-a-full-user-web-app-from-scratch-with-vanilla-php8/)

&#x200B;

Build from Scratch a Modern REST API 
with PHP 8

[https://freewebcart.com/build-a-modern-rest-api-with-php-8/](https://freewebcart.com/build-a-modern-rest-ap
i-with-php-8/)

&#x200B;

C++ And PHP Complete Course for C++ and PHP Beginners

[https://freewebcart.com/c-and-php-comp
lete-course-2023/](https://freewebcart.com/c-and-php-complete-course-2023/)
```
---

     
 
all -  [ Looking for some cool Project Ideas.  ](https://www.reddit.com/r/LangChain/comments/1g54rea/looking_for_some_cool_project_ideas/) , 2024-10-18-0912
```
I recently got my hands dirty on langchain and langgraph, so i was thinking of making a project to know how much I know 
and to practice what I learned. I was looking for some cool project ideas using langgraph and langchain, it should not h
ave to be much complex and not too easy to implement. So guys please share some of the cool project idea you guys have o
r you currently working on ✌🏻

Thank you in advance 🙌🙏🏻
```
---

     
 
all -  [ [FOR HIRE] I will develop custom Salesforce solutions for you at an affordable price ](https://www.reddit.com/r/hiring/comments/1g53d0x/for_hire_i_will_develop_custom_salesforce/) , 2024-10-18-0912
```
Hey there! I'm David,

Are you overwhelmed with repetitive tasks or dreaming up exciting Salesforce projects? Let me bri
ng my expertise in Salesforce development to help you out!

With over 7 years of experience, I've worked on a variety of
 projects, focusing on Flows, Lightning Web Components (LWC), and integrations.

What can I do for you?

* Build Custom 
LWC: Create responsive components tailored to your needs, following the LDS from SF.

* Automate Processes: Streamline y
our workflows and eliminate manual tasks.

* Integrate Systems: Seamlessly connect Salesforce with other platforms.

* D
evelop Innovative Solutions: From custom apps to unique features, let’s build something great together.

* Work with AI:
 Using cool stuff like Langchain or the Chat-GPT API.

If you believe you have something that I could do for you, please
 place a $bid and send me the details of the project. As always, the price depends, but It's usually from 50$ to 100$ fo
r simple projects.



```
---

     
 
all -  [ What's the best framework for building productiin levwl RAG application? ](https://www.reddit.com/r/u_Tech_8976/comments/1g5310o/whats_the_best_framework_for_building_productiin/) , 2024-10-18-0912
```
Langchain is good for prototyping but when it comes to production level RAG I found that langchain is not good enough. C
an someone suggest some framework to build production level RAG application? What about llmaindex?
```
---

     
 
all -  [ AI News this week ](https://www.reddit.com/r/brainscriblr/comments/1g52vqt/ai_news_this_week/) , 2024-10-18-0912
```
||
||
|OpenAI's new '[Swarm](https://link.mail.beehiiv.com/ss/c/u001.bCJQm5nTOkyoUpvPqxXWZMOsre0WB3hJUyVxQAm__4HIO4v9uY6
6cAXbEzVswcWf8v1uU7-0Yk4VHyNvJa2CUBdbS2s48OjErH6RXPwdb-Ka_sGzXtLyZ3Fi1JVKu2xr3hGZlUoJ4Lk-WeyosHoE4WobxtB1y2hhPAhCk-UGOX8
ZZXjr5xJzSEdn39bDeGmARGksreb_Tkv6O5_OPUZxqkB3Rv2n0Tt_zOxvWr0KAv4UwpMcXw1R8owHvt4xPsJ9/4am/9ENZbDoZQWeDK8jSHCurcg/h1/h001
.n4RBfuz2eOecxl7AFemrxExSrneQA5lYl5QRug9uQiE)' framework enables developers to create multi-agent AI systems. It orchest
rates collaboration between AI agents on complex tasks using 'Routines' (step-by-step instructions) and 'Handoffs' (task
 delegation). Swarm facilitates smooth communication and coordination between agents, making it easier to build, test, a
nd control sophisticated AI systems. It's primarily designed for developers and researchers working on AI assistants, ro
botics, and task automation.|
|[Amazon](https://link.mail.beehiiv.com/ss/c/u001.U0cWUjXPgPq-FBBCovcNs6m3fN7FkkcIdUfHhdbT
GRGOya7OT-s81EqCzBtGctnsroWa8BH3gaMco4YAhnKOX7Z_lBID49_leyRuXyFi0oQ7fZhEgvnBi2S7sg6pNcrrZ2SEnjRBdSYBQNAAmF7XjzOWKhYAb2KM
sx8ie5YaPpwWeqi8h569zdilxM0-NdjbE7N1Y3lyE8a5BFK2ChoSBjxOCerTMyrnR6feUXY_gmywThsews_jnMo4KEzT54lHx4ax--YTu3dMOkoYNmykbDSd
0JSpQyARo8p5NMF4emsWJxNXf2m9E32htiQg55spUGa3aoEZn8ZaHr-70UGwGEaaORKXEK3UDSZjbwn2iUo/4am/9ENZbDoZQWeDK8jSHCurcg/h2/h001.m
o4zp4aaiDj4dMljy_lzpRUXXdwp710T3mpV_SStdvA) has built an AI-shopping bot.|
|[Langchain](https://link.mail.beehiiv.com/ss
/c/u001.bCJQm5nTOkyoUpvPqxXWZPfVviZxL4uMVDMAsYwQj7-__3zLdejqOQMUCUmH-mnissFOZbrcdlmMfGjuqX7FsiIt0LZjhrt3pt84vyOdpmsxRdIb
W_d_eQx1SqaXWNeRHahRWwh0JJN1PGmKPTXTkA4HyxwnLXjHxCaG5y8w5GYR3vhf716qW2MdHz69lLWfuMrnpuk1QfWwL0FO1rLI9qb-3FdjNu9ELdE3B2PS
EfLL6V5vZ7VybBcZuAsoVrF_rK6Zm2WDcJSc2CjWIKyNuQ/4am/9ENZbDoZQWeDK8jSHCurcg/h3/h001.cV0EotQc92jLszSY9Wozvhk9u70EcspCaOXFZt
z6aH8) has revealed Kotaemon and open-source RAG UI for document chat.|
|In a recent [Tweet](https://link.mail.beehiiv.c
om/ss/c/u001.Hb21N8P-60x7GolUpHo-ktEi_mxjwW9ydRKeLuaiVHa6G7izolZ6TpwQo4wHe-NhwVHdrDcAk3n68PdlCgDPKdE0JMRmDCdccOqpOhpStsQ
IAv74Z3lBr_qqscckZa9W4FfLtdnaKaogfl1iZBhz5Tbg0hbmqrR_LAFbabW-gNR8fdRxLGDpfluDq7_p2yS3VuLmjleIJ0cima1BazL_pDAYeO2fdRkWgRu
jhZml_uwV-bTQ1_GNetg_eRAHT-g8ZoMQA_BOJDVjyXotDCRlDQ/4am/9ENZbDoZQWeDK8jSHCurcg/h4/h001.m6GiQ2Pok0dRDFHU4ebvUrwk4di-eidzS
CN6omvNfJA) former OpenAI board member Karpathy suggested there should be more diversity in model fine-tuning.|
```
---

     
 
all -  [ Challenges in Word Counting with Langchain and Qdrant ](https://www.reddit.com/r/Langchaindev/comments/1g51dlk/challenges_in_word_counting_with_langchain_and/) , 2024-10-18-0912
```
I am developing a chatbot using Langchain and Qdrant, and I'm encountering challenges with tasks involving word counts. 
For example, after vectorizing the book The Lord of the Rings, I ask the AI how many times the name 'Frodo' appears, or 
to list the main characters and how frequently their names are mentioned. I’ve read that word counting can be a limitati
on of AI systems, but I’m unsure if this is a conceptual misunderstanding on my part or if there is a way to accomplish 
this. Could someone clarify whether AI can reliably count words in vectorized documents, or if this is indeed a known li
mitation?

I'm not asking for a specific task to be done, but rather seeking a conceptual clarification of the issue. Ev
en though I have read the documentation, I still don't fully understand whether this functionality is actually feasible


I attempted to use the functions related to the vectorization process, particularly the similarity search method in Qdr
ant, but the responses remain uncertain. From what I understand, similarity search works by comparing vector representat
ions of data points and returning those that are most similar based on their distance in the vector space. In theory, th
is should allow for highly relevant results. However, I’m unsure if my setup or the nature of the task—such as counting 
occurrences of a specific word like 'Frodo'—is making the responses less reliable. Could this be a limitation of the met
hod, or might there be something I’m missing in how the search is applied?
```
---

     
 
all -  [ Challenges in Word Counting with Langchain and Qdran ](https://www.reddit.com/r/LangChain/comments/1g517g7/challenges_in_word_counting_with_langchain_and/) , 2024-10-18-0912
```
I am developing a chatbot using Langchain and Qdrant, and I'm encountering challenges with tasks involving word counts. 
For example, after vectorizing the book *The Lord of the Rings*, I ask the AI how many times the name 'Frodo' appears, o
r to list the main characters and how frequently their names are mentioned. I’ve read that word counting can be a limita
tion of AI systems, but I’m unsure if this is a conceptual misunderstanding on my part or if there is a way to accomplis
h this. Could someone clarify whether AI can reliably count words in vectorized documents, or if this is indeed a known 
limitation?
```
---

     
 
all -  [ I built a Langchain Agent that can use any website as a custom tool ](https://www.reddit.com/r/AI_Agents/comments/1g4zlqr/i_built_a_langchain_agent_that_can_use_any/) , 2024-10-18-0912
```
Here is the repo if anyone is interested:

[https://github.com/dendrite-systems/langchain-dendrite-example/tree/main](ht
tps://github.com/dendrite-systems/langchain-dendrite-example/tree/main)

It can go get OpenAI's API status, send emails,
 help search for conflicting trademarks and a few other random things :) 
```
---

     
 
all -  [ Laravelpy concept. Would you use this? ](https://www.reddit.com/r/laravel/comments/1g4z0nc/laravelpy_concept_would_you_use_this/) , 2024-10-18-0912
```
Hey Laravel Devs

Been working on a concept for an opensource laravel package over the past few weeks (still in early st
ages) it's called Laravelpy

The concept is to be able to harness the power of Python in your Laravel Application, my go
al is to achieve the following

Run custom Python scripts using Laravel syntax e.g. Python::run('your/custom/pyton/scrip
t.py')

Have out of the box integrations with popular python libraries such as pandas, matplotlib, NumPy, LangChain just
 to name a few. (see work in progress for Pandas in the attached image)

Upon installation have a Python virtual environ
ment and manage pip install using artisan

I have more ideas on how I could take this further but I wanted to get some i
nitial feedback to see if anyone would use a package like this?

[Concept of usage ](https://preview.redd.it/44r5xsunk5v
d1.png?width=3768&format=png&auto=webp&s=a950057ea8f7ff0c3efc9143fd15358afd46898e)


```
---

     
 
all -  [ Realna plata?  ](https://www.reddit.com/r/programiranje/comments/1g4xe1e/realna_plata/) , 2024-10-18-0912
```
Pozdrav ljudi, zanima me realna plata za ovaj stack. Prave se vise SaaS projekata. 

  
1. React JS  
2. Express JS  
3.
 MongDB & PostgresSQL  
4. LangChain (OpenAI Embeddings, LLM Chains etc)  
5. Azure (Blog Storage, Embeddings Storage, I
ndexing service, search service, Cognitive Services, Azure AI Studio) - Very Important.  
6. And NPM Libraries in genera
l (There are many used in this project)
```
---

     
 
all -  [ How I Started Learning Machine Learning ](https://www.reddit.com/r/learnmachinelearning/comments/1g4x299/how_i_started_learning_machine_learning/) , 2024-10-18-0912
```
Hello, everyone. As promised, I'll write a longer post about how I entered the world of ML, hoping it will help someone 
shape their path. I'll include links to all the useful materials I used alongside the story, which you can use for learn
ing.

I like to call myself an AI Research Scientist who enjoys exploring new AI trends, delving deeper into understandi
ng their background, and applying them to real products. This way, I try to connect science and entrepreneurship because
 I believe everything that starts as scientific research ends up 'on the shelves' as a product that solves a specific us
er problem.

I began my journey in ML in 2016 when it wasn't such a popular field. Everyone had heard of it, but few wer
e applying it. I have several years of development experience and want to try my hand at ML. The first problem I encount
ered was where to start - whether to learn mathematics, statistics, or something else. That's when I came across a name 
and a course that completely changed my career.

# Let's start

You guessed it. It was Professor Andrew Ng and his globa
lly popular Machine Learning course available on Coursera (I still have the certificate, hehe). This was also my first o
fficial online course ever. Since that course no longer exists as it's been replaced by a new one, I recommend you check
 out:

1. [Machine Learning (Stanford CS229)](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)

2. [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

These two 
courses start from the basics of ML and all the necessary calculus you need to know. Many always ask questions like whet
her to learn linear algebra, statistics, or probability, but you don't need to know everything in depth. This knowledge 
helps if you're a scientist developing a new architecture, but as an engineer, not really. You need to know some basics 
to understand, such as how the backpropagation algorithm works.

I know that Machine Learning (Stanford CS229) is a very
 long and arduous course, but it's the right start if you want to be really good at ML. In my time, I filled two thick n
otebooks by hand while taking the course mentioned above.

# TensorFlow and Keras

After the course, I didn't know how t
o apply my knowledge because I hadn't learned specifically how to code things. Then, I was looking for ways to learn how
 to code it. That's when I came across a popular framework called Keras, now part of TensorFlow. I started with a new co
urse and acquiring practical knowledge:

1. [Deep Learning Specialization](https://www.coursera.org/specializations/deep
-learning)
2. [Deep Learning by Ian Goodfellow](https://www.deeplearningbook.org/)
3. [Machine Learning Yearning by Andr
ew Ng](https://info.deeplearning.ai/machine-learning-yearning-book)

These resources above were my next step. I must adm
it that I learned the most from that course and from the book Deep Learning by Ian Goodfellow because I like reading boo
ks (although this one is quite difficult to read).

# Learn by coding

To avoid just learning, I went through various Gi
tHub repositories that I manually retyped and learned that way. It may be an old-fashioned technique, but it helped me a
 lot. Now, most of those repositories don't exist, so I'll share some that I found to be good:

1. [Really good Jupyter 
notebooks that can teach you the basics of TensorFlow](https://github.com/mrdbourke/tensorflow-deep-learning)
2. [Anothe
r good repo for learning TF and Keras](https://github.com/codebasics/deep-learning-keras-tf-tutorial)

# Master the chal
lenge

After mastering the basics in terms of programming in TF/Keras, I wanted to try solving some real problems. There
's no better place for that challenge than Kaggle and the popular Titanic dataset. Here, you can really find a bunch of 
materials and simple examples of ML applications. Here are some of my favorites:

1. [Titanic - Machine Learning from Di
saster](https://www.kaggle.com/c/titanic/overview)
2. [Home Credit Default Risk](https://www.kaggle.com/competitions/hom
e-credit-default-risk/overview)
3. [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/h
ouse-prices-advanced-regression-techniques)
4. [Two Sigma: Using News to Predict Stock Movements](https://www.kaggle.com
/competitions/two-sigma-financial-news)

I then decided to further develop my career in the direction of applying ML to 
the stock market, first using predictions on time series and then using natural language processing. I've remained in th
is field until today and will defend my doctoral dissertation soon.

# How to deploy models

To continue, before I move 
on to the topic of specialization, we need to address the topic of deployment. Now that we've learned how to make some b
asic models in Keras and how to use them, there are many ways and services, but I'll only mention what I use today. For 
all my ML models, whether simple regression models or complex GPT models, I use FastAPI. It's a straightforward framewor
k, and you can quickly create API endpoints. I'll share a few older and useful tutorials for beginners:

1. [AI as an AP
I tutorial series](https://www.youtube.com/watch?v=56qQNcHJxyQ)
2. [A step-by-step guide](https://medium.com/@ganiyuabdu
lwajeed2002/a-step-by-step-approach-to-building-a-fast-api-for-deep-learning-classification-projects-cbd2ea6bc2f2)
3. [P
roductizing an ML Model with FastAPI and Cloud Run](https://medium.com/semantixbr/deploy-an-ml-model-with-fastapi-and-cl
oud-run-part-1-1a0b0f3b3a5d)

Personally, I've deployed on various cloud providers, of which I would highlight GCP and A
WS because they have everything needed for model deployment, and if you know how to use them, they can be quite cheap.


# Chose your specialization

The next step in developing my career, besides choosing finance as the primary area, was my
 specialization in the field of NLP. This happened in early 2020 when I started working with models based on the Transfo
rmer architecture. The first model I worked with was BERT, and the first tasks were related to classifications. My recom
mendations are to master the Transformer architecture well because 99% of today's LLM models are based on it. Here are s
ome resources:

1. [The legendary paper 'Attention Is All You Need'](https://proceedings.neurips.cc/paper_files/paper/20
17/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
2. [Hugging Face Course on Transformers](https://huggingface.co/lear
n/nlp-course/chapter1/1)
3. [Illustrated Guide to Transformers - Step by Step Explanation](https://towardsdatascience.co
m/illustrated-guide-to-transformers-step-by-step-explanation-f74876522bc0)
4. [Good repository](https://github.com/Niels
Rogge/Transformers-Tutorials)
5. [How large language models work, a visual intro to transformers](https://www.youtube.co
m/watch?v=wjZofJX0v4M)

After spending years using encoder-based Transformer models, I started learning GPT models. Good
 open-source models like Llama 2 then appear. Then, I started fine-tuning these models using the excellent Unsloth libra
ry:

1. [How to Finetune Llama-3 and Export to Ollama](https://docs.unsloth.ai/tutorials/how-to-finetune-llama-3-and-exp
ort-to-ollama)
2. [Fine-tune Llama 3.1 Ultra-Efficiently with Unsloth](https://huggingface.co/blog/mlabonne/sft-llama3)


After that, I focused on studying various RAG techniques and developing Agent AI systems. This is now called AI enginee
ring, and, as far as I can see, it has become quite popular. So I'll write more about that in another post, but here I'l
l leave what I consider to be the three most famous representatives, i.e., their tutorials:

1. [LangChain tutorial](htt
ps://python.langchain.com/docs/tutorials/)
2. [LangGraph tutorial](https://langchain-ai.github.io/langgraph/tutorials/)

3. [CrewAI examples](https://github.com/crewAIInc/crewAI-examples)

# Here I am today

Thanks to the knowledge I've gene
rated over all these years in the field of ML, I've developed and worked on numerous projects. The most significant publ
icly available project is developing an agent AI system for well-being support, which I turned into a [mobile applicatio
n](https://sintelly.com/download/). Also, my entire doctoral dissertation is related to applying ML to the stock market 
in combination with the development of GPT models and reinforcement learning (more on that in a separate post). After lo
ng 6 years, I've completed my dissertation, and now I'm just waiting for its defense. I'll share everything I'm working 
on for the dissertation publicly [on the project](https://primoinvesting.com/), and in tutorials I'm preparing to write.


If you're interested in these topics, I announce that I'll soon start with activities of publishing content on Medium 
and a blog, but I'll share all of that here on Reddit as well. Now that I've gathered years of experience and knowledge 
in this field, I'd like to share it with others and help as much as possible.

If you have any questions, feel free to a
sk them, and I'll try to answer all of them.

Thank you for reading.
```
---

     
 
all -  [ Relevant file retrieval  ](https://www.reddit.com/r/LangChain/comments/1g4tsbo/relevant_file_retrieval/) , 2024-10-18-0912
```
I’m trying to implement what OpenAI Assistant API is doing when I feed it with some documents. 
So if my question is rel
ated to something on the documents that I have in a directory, it should take that into account; if not, it can provide 
a general answer. Is embeddings only approach here? 
```
---

     
 
all -  [ [OFFER] I will develop custom Salesforce solutions for you at an affordable price ](https://www.reddit.com/r/slavelabour/comments/1g4tf5u/offer_i_will_develop_custom_salesforce_solutions/) , 2024-10-18-0912
```
Hey there! I'm David,

Are you overwhelmed with repetitive tasks or dreaming up exciting Salesforce projects? Let me bri
ng my expertise in Salesforce development to help you out!

With over 7 years of experience, I've worked on a variety of
 projects, focusing on Flows, Lightning Web Components (LWC), and integrations.

What can I do for you?

* Build Custom 
LWC: Create responsive components tailored to your needs, following the LDS from SF.
* Automate Processes: Streamline yo
ur workflows and eliminate manual tasks.
* Integrate Systems: Seamlessly connect Salesforce with other platforms.
* Deve
lop Innovative Solutions: From custom apps to unique features, let’s build something great together.
* Work with AI: Usi
ng cool stuff like Langchain or the Chat-GPT API.

If you believe you have something that I could do for you, please pla
ce a $bid and send me the details of the project. As always, the price depends, but It's usually from 25$ to 50$ for sim
ple projects.
```
---

     
 
all -  [ What is the best custom agent you made using langchain or langgraph? ](https://www.reddit.com/r/LangChain/comments/1g4sj37/what_is_the_best_custom_agent_you_made_using/) , 2024-10-18-0912
```
I just want to see it's effectiveness through your experience.

I plan on creating a tool that queries on tabular data a
nd tweak it to work fine on large open source models. If you have done something similar please let me know what it was.

```
---

     
 
all -  [ Technique beyond RecursiveCharacterTextSplitter for unstructured PDF RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1g4rcji/technique_beyond_recursivecharactertextsplitter/) , 2024-10-18-0912
```
I built a local RAG using ollama, langchain and llama3.2, using a MultiQueryRetriever to parse through multiple PDF and 
ask a set of identical questions for each.

The accuracy is good but not perfect, and I have noticed that failures tend 
to be happen on data that looks like a table in the PDF.

For example:
```
----------------|----|
Population 2023 | x  |

Population 2024 | y  |
Population 2025 | z  |
----------------|----|
```

will show up in the chunks of RecursiveCharac
terTextSplitter as 

```
Population 2023
Population 2024
Population 2025
x
y
z
```

and the chat will either retrieve th
e wrong information or not find the information at all. I would like to improve my PDF ingestion (chunking/splitting, ve
ctor embeddings) to be able to more accurately retrieve the correct data. I have played around with the embedding model,
 chunk size and overlap, but those won't fix this issue.

What techniques could I use to improve the layout of the chunk
s stored in my vector database? Or should I look into a different technique altogether?

Here is the current code regard
ing indexing:

```
TEXT_EMBEDDING_MODEL = os.getenv('TEXT_EMBEDDING_MODEL', 'nomic-embed-text')

def create_vector_embed
dings_from_pdf(file):
  # Ingest the PDF
  loader = UnstructuredPDFLoader(file_path=file)
  document_data = loader.load(
)

  # Vector Embeddings of PDF (split and chunking)
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, ch
unk_overlap=50)
  splits = text_splitter.split_documents(document_data)

  # Add to vector database
  embeddings = Ollam
aEmbeddings(model=TEXT_EMBEDDING_MODEL, show_progress=False)
  vector_db = Chroma.from_documents(
    documents=splits,

    embedding=embeddings
  )
  return vector_db
```

Thank you!
```
---

     
 
all -  [ How to chang database when using vector_store? ](https://www.reddit.com/r/LangChain/comments/1g4qe4z/how_to_chang_database_when_using_vector_store/) , 2024-10-18-0912
```
I wanna use my test\_db database in my milvus, but i donnnot find the way to change database as langchain.Milvus.vector\
_store defaultly use the default database. 
```
---

     
 
all -  [ Using LangChain to manage visual models for editing 3D scenes ](https://www.reddit.com/r/LangChain/comments/1g4n12e/using_langchain_to_manage_visual_models_for/) , 2024-10-18-0912
```
An ECCV paper, Chat-Edit-3D, utilizes ChatGPT to drive (by LangChain) nearly 30 AI models and enable 3D scene editing.


[https://github.com/Fangkang515/CE3D](https://github.com/Fangkang515/CE3D)

https://reddit.com/link/1g4n12e/video/5j54cy
ufl0vd1/player


```
---

     
 
all -  [ Unable to get desired results with ChatPromptTemplate and Prompt Caching with Anthropic ](https://www.reddit.com/r/LangChain/comments/1g4ip6z/unable_to_get_desired_results_with/) , 2024-10-18-0912
```
I have a long prompt of instructions that performs as intended when I use PromptTemplate.  
After reading about Prompt C
aching, I tried to implement it with the ChatPromptTemplate, but it did not work as intended. The demo of prompt caching
 uses a book as its context. I have a smaller context but specific instructions.  
Tried fine-tuning the prompt, but the
 model hallucinates badly.

Example: When I ask a question, it does not use the same question to reason/generate the ans
wer.
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-18-0912
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

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-18-0912
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

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-18-0912
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

     
