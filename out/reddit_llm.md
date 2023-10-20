 
all -  [ How to build a chatbot that doesn’t hallucinate ](https://www.reddit.com/r/ArtificialInteligence/comments/17brr5e/how_to_build_a_chatbot_that_doesnt_hallucinate/) , 2023-10-20-0909
```
Seeing a lot of talk about LLM observability and we have quite an in-production pipeline so figured I’d share how we do 
it.  
Building AI products is different than non-AI products: They can output things you never instructed them to. That 
was barely possible before LLMs. Now, it’s common.  
Whether you’re offering B2B solutions that live on other people’s s
ites or building an AI chatbot for yourself, you don’t want it to lie to users (hallucinating) or for users to coax it i
nto saying things that harm your business.  
FYI: LangSmith makes LangChain prompts/outputs easier to observe, log, and 
debug by creating traces of each conversation. We offer customers custom AI chatbots powered by GPT and LangChain.  
Her
e's what we've learned after tracing 140M (million, yes million) customer chats:  
**Debugging is a heck of a lot easier
.**  
Tedious debugging became smooth. LangSmith highlighted user trip-ups we didn’t even know about and helped us polis
h our prompts.  
That let us ship countless changes (some subtle, some major), and prevented a lot of curly GPT response
s from reaching end users—especially important since our product reaches our customers’ end users.  
**Troubleshooting i
s now a team sport.**  
Before LangSmith, there were a handful of solo-expeditioner-engineers who bravely waded through 
QA’ing our LLMs calls and responses. That happened in a silo with lots of time-consuming trial and error.  
While integr
ating LangSmith, we set up a custom snippet that sends negative user feedback (and its LangSmith trace) to an internal S
lack channel. When feedback comes in, multiple engineers work to resolve any wonkiness or errors.  
**We’re not making s
tupid guesses anymore.**  
Before LangSmith, we guessed the what, how, and why of GPTs responses. While we had a decent 
idea, it wasn’t until we examined traces closely that we saw the details like decision processes, roles, document retrie
val steps, LangChain's interventions, elastic search, you name it!  
We now have a much more granular and explicit view 
of how our chatbot functions.  
**Prototyping is so much faster**  
We recently switched over to GPT-4. Being able to pr
ototype the model transition (before going to prod) was critical to the upgrade. GPT-3 and GPT-4 behave differently, so 
adapting prompts, roles, and protocols for document retrieval and acknowledging sources, etc. needed fine-tuning.  
The 
playground really let us stress test things and make the change confidently.  
\---  
Happy to share what one of our tra
ces looks like too if that's helpful!
```
---

     
 
all -  [ Which Chunk Size, Chunk overlap and Model to use for inserting text in Flowise? ](https://www.reddit.com/r/LangChain/comments/17browm/which_chunk_size_chunk_overlap_and_model_to_use/) , 2023-10-20-0909
```
I insert a lot of research text from PDFs into Pinecone with Flowise. I can't say what chunk size, chunk overlap and mod
el is best for this task.

I was able to extract the text from the PDFs in acceptable quality, keeping the text in the h
eaders and footers.

Should I use the 'normal' gpt-3.5 or the 16k version? Or would it even be better to use GPT-4 for i
nserting data?

Greetings

[View Poll](https://www.reddit.com/poll/17browm)
```
---

     
 
all -  [ Text to sql for large databases ](https://www.reddit.com/r/LangChain/comments/17bq8is/text_to_sql_for_large_databases/) , 2023-10-20-0909
```
Has anyone actually implemented Text to SQL for large databases ? I'm talking around 1500 tables. I've tried SQL agents 
and most of the time it works, but the issue is with the token usage. It used up 10$ worth of credits in a short period 
of time.

Is it possible to restrict the number of table schemas being sent for each request. Or identify which table sc
hemas should be sent with each request ( I've heard somewhere that using a vector db to identify which tables are releva
nt for a query might help, not sure though).

&#x200B;
```
---

     
 
all -  [ AI/Deep Learning Solutions for Preprocessing Diverse and Messy CSV Files ](https://www.reddit.com/r/LangChain/comments/17blrgp/aideep_learning_solutions_for_preprocessing/) , 2023-10-20-0909
```
I'm dealing with a multitude of CSV files where the formats and structures vary widely, with mixed styles, inconsistent 
headers, and sometimes even headers smack in the middle of the data. It's a nightmare for any machine learning endeavor.


Manually cleaning and preprocessing these files would be imposible as there are too many small tables, and I'm wonderi
ng if there's an out-of-the-box AI or deep learning solution that can help. Ideally, I'm looking for something that can 
among other preprocessing steps:

Identify and standardize headers
Split tables if there's an unexpected header in the m
iddle
Fill in missing values
Turn these chaotic CSVs into clean, ML-friendly tables

Has anyone encountered a tool or mo
del that can handle such tasks? Any recommendations or advice would be a lifesaver!

Thanks in advance for your help!
```
---

     
 
all -  [ I made this in flowise.ai and i've been wondering how to convert it into python code? Does any one k ](https://i.redd.it/kof9gp9516vb1.png) , 2023-10-20-0909
```

```
---

     
 
all -  [ Meetup de AI4Devs en La Plata ](https://www.reddit.com/r/devsarg/comments/17bikrr/meetup_de_ai4devs_en_la_plata/) , 2023-10-20-0909
```
Buenass, les cuento que en La Plata estamos armando una comunidad de AI4Devs, la idea es tener un espacio donde comparti
r herramientas de AI que se usen en el dia a dia de los devs, ya sea para integrarlas con aplicaciones, para el desarrol
lo en si o para boludear. Es decir, no es necesario tener conocimientos tecnicos de machine learning sino solo ser dev y
 estar interesado en AI.

Ya tenemos fecha para la primera Meetup con dos charlas confirmadas. Va a ser el viernes 27 en
 espacio Weiaut en La Plata, es gratis y para el que quiera ir le dejo el siguiente form para inscribirse: [https://form
s.gle/7hFewEp3LoCeq43K7](https://forms.gle/7hFewEp3LoCeq43K7)

&#x200B;

&#x200B;

https://preview.redd.it/5jmn7yroq5vb1
.png?width=4500&format=png&auto=webp&s=b3162d09e78cf894ca24e69ebe8b46837dcf1d68
```
---

     
 
all -  [ Stable but Evolving Summary over Time? ](https://www.reddit.com/r/ChatGPTCoding/comments/17bikc7/stable_but_evolving_summary_over_time/) , 2023-10-20-0909
```
Does anyone have experience updating summarizations with addendums? I'm trying to take an existing summary (for which th
e original text has been discarded) and prompt to look at a new block of raw text and ask for an update to the summary t
o encode the new information.  


The challenge is that I'd like the summary to remain around the same length over time 
as this process iterates, keeping the most salient information in the summary. My attempts so far have yielded either (a
) dropping information because it is 're-summarizing' the summary in addition to incorporating the new addendum, or (b) 
just adding on new details to the summary over time. Where what I'd really like is for new 'important' details in the ad
dendums to trump less important details in existing summaries, and keep the summary size more or less stable over time. 
 


Happy for any pointers to places people have done this successfully -- prompt examples, langchain agents, etc. 
```
---

     
 
all -  [ How can I create user input/output for this code block? ](https://www.reddit.com/r/learnpython/comments/17bhhyt/how_can_i_create_user_inputoutput_for_this_code/) , 2023-10-20-0909
```
from langchain.chat\_models import ChatOpenAI  
from langchain.prompts import HumanMessagePromptTemplate  
from langchai
n.schema.messages import SystemMessage  
chat\_template = ChatPromptTemplate.from\_messages(  
\[  
SystemMessage(  
con
tent=(  
'You are a helpful assistant that re-writes the user's text to '  
'sound more upbeat.'  
)  
),  
HumanMessage
PromptTemplate.from\_template('{text}'),  
\]  
)  
llm = ChatOpenAI()  
llm(chat\_template.format\_messages(text='i don
t like eating tasty things.'))  


Its my first time using langchain and I'm curious
```
---

     
 
all -  [ i'm having problem while using LLama2 models with Langchain , tell me the best way to work with LLam ](https://www.reddit.com/r/LangChain/comments/17bfqdy/im_having_problem_while_using_llama2_models_with/) , 2023-10-20-0909
```
So many Errors , when i try to use ChatpromptTemplate it gives me error , it does not recognize the chat models or LLMs


  
 

`callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])`  
`# Make sure the model path is correct
 for your system!`  
`llm = LlamaCpp(`  
 `model_path='models/llama-2-13b-chat.ggmlv3.q4_0.bin', callback_manager=callba
ck_manager, verbose=True,n_ctx=4096, max_tokens=1000, last_n_tokens_size=1000 , temperature=0`  
`)`  
`llama_embeddings
 = LlamaCppEmbeddings(model_path='models/llama-2-13b-chat.ggmlv3.q4_0.bin')`
```
---

     
 
all -  [ product recommendations advice ](https://www.reddit.com/r/LangChain/comments/17bdufy/product_recommendations_advice/) , 2023-10-20-0909
```
I am looking to a create a bot on WhatsApp that provides products based on a user's preferences.

5 questions - style, b
udget, etc 

It would then display 5 products that best match those preferences.

It would be linked to a product feed (
XML or RSS) so that would auto update.

What is the best tech stack to achieve this? E.g. openai, pinecone, langchain, e
tc.  What pitfalls should I be aware of?

I have experience building WhatsApp bots but this specific integration is new 
to me.

Thanks
```
---

     
 
all -  [ Update collection in Qdrant(don't want to create collection from scratch) ](https://www.reddit.com/r/LangChain/comments/17bc1ij/update_collection_in_qdrantdont_want_to_create/) , 2023-10-20-0909
```
I am using Qdrant as the vector db for a RAG project. I would like some inputs and thoughts on how to update the existin
g collection in qdrant. The user can upload multiple files and I am adding these documents embedding in the same collect
ion. Now if the user updates some text in one of the document instead of recreating the entire collection I want to upda
te the payload and vectors of the document that got updated. Recreating the collection from scratch is an expensive task
 is there way to update the collection by deleting the old document and inserting the new one and update document.
```
---

     
 
all -  [ Chatbot based on SQL results with temporary chat history? ](https://www.reddit.com/r/LangChain/comments/17bc0j1/chatbot_based_on_sql_results_with_temporary_chat/) , 2023-10-20-0909
```
Hello, 

First off, here is my background situation:
We have a table that contains scraped results of different articles
 around the globe (not sentiment analysis), and those articles might have thousand of keywords. 

The analytical team is
 requiring a chatbot that can ask questions based off these results.

By using SQL Chain from langchain, it kinda had th
e expected results. However, we have two problems:

1- The token limit is a pain, because most of the results are huge a
round 20k tokens.

2- The sqlchain isn't actually a chatbot. It just gives you an answer, but it won't respond to querie
s like 'make the previous answer in a json format', etc.

I know I am newbie in chatbots so I would like any general 'th
inking' process or direction, just point me to any topic
```
---

     
 
all -  [ 300+ Free Udemy Certificate Courses -Limited Time - 19/10/23 ](https://www.reddit.com/r/Newudemy/comments/17b9ld0/300_free_udemy_certificate_courses_limited_time/) , 2023-10-20-0909
```
 View All Courses: [https://inventhigh.net](https://inventhigh.net/)

1. WordPress Theme Development from Scratch 2.0-[h
ttps://inventhigh.net/udemy/advanced-wordpress-theme-development-with-bootstrap/](https://inventhigh.net/udemy/advanced-
wordpress-theme-development-with-bootstrap/)
2. WooCommerce Theme Development: Advanced Course-[https://inventhigh.net/u
demy/woocommerce-wordpress-theme-development/](https://inventhigh.net/udemy/woocommerce-wordpress-theme-development/)
3.
 Ultra-Fast WordPress Speed With 10Web WordPress Web Hosting-[https://inventhigh.net/udemy/ultra-fast-wordpress-speed/](
https://inventhigh.net/udemy/ultra-fast-wordpress-speed/)
4. Python Programming Language | Master Python Course (Arabic)
-[https://inventhigh.net/udemy/python\_tutorials/](https://inventhigh.net/udemy/python_tutorials/)
5. Python And Flask  
Demonstrations Practice Course-[https://inventhigh.net/udemy/python-and-flask-only-demonstration-course/](https://invent
high.net/udemy/python-and-flask-only-demonstration-course/)
6. Linux Tmux-[https://inventhigh.net/udemy/linux-tmux/](htt
ps://inventhigh.net/udemy/linux-tmux/)
7. Learn Web Design using WordPress & Start Freelancing-[https://inventhigh.net/u
demy/become-successful-wordpress-freelancer-to-make-money-online/](https://inventhigh.net/udemy/become-successful-wordpr
ess-freelancer-to-make-money-online/)
8. Haskell Exercises for Beginners-[https://inventhigh.net/udemy/haskell-exercises
-for-beginners/](https://inventhigh.net/udemy/haskell-exercises-for-beginners/)
9. Convert a one page HTML5 Template to 
a WordPress Theme-[https://inventhigh.net/udemy/convert-html5-template-to-wordpress-theme/](https://inventhigh.net/udemy
/convert-html5-template-to-wordpress-theme/)
10. Computer Basics-[https://inventhigh.net/udemy/basic-of-computer/](https
://inventhigh.net/udemy/basic-of-computer/)
11. CSS Crash Course For Beginners-[https://inventhigh.net/udemy/css-crash-c
ourse-for-beginners-g/](https://inventhigh.net/udemy/css-crash-course-for-beginners-g/)
12. Asteroids with Python PyGame
-[https://inventhigh.net/udemy/asteroids-with-python-pygame/](https://inventhigh.net/udemy/asteroids-with-python-pygame/
)
13. Linode: Foundations of Web Server Security-[https://inventhigh.net/udemy/linode-foundations-of-web-server-security
/](https://inventhigh.net/udemy/linode-foundations-of-web-server-security/)
14. Linode: Build and Deploy Responsive Webs
ites on the Cloud-[https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/](https://inven
thigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/)
15. Learn Bootstrap - For Beginners-[https://
inventhigh.net/udemy/learn-bootstrap-for-beginners/](https://inventhigh.net/udemy/learn-bootstrap-for-beginners/)
16. Ja
vaScript, Bootstrap, & PHP - Certification for Beginners-[https://inventhigh.net/udemy/javascript-bootstrap-php-certific
ation-for-beginners/](https://inventhigh.net/udemy/javascript-bootstrap-php-certification-for-beginners/)
17. Bootstrap 
& jQuery - Certification Course for Beginners-[https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-be
ginners/](https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-beginners/)
18. AWS Beginner to Interme
diate: EC2, IAM, ELB, ASG, Route 53-[https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/
](https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/)
19. AWS & React: Deploy an Auto-S
caling E-Commerce App with ELB-[https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/](
https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/)
20. DevOps Interview Questions P
reparation Guide - 2023-[https://inventhigh.net/udemy/devops-interview-questions-preparation-guide/](https://inventhigh.
net/udemy/devops-interview-questions-preparation-guide/)
21. Quantitative Finance with Python-[https://inventhigh.net/ud
emy/quantitative-finance-with-python/](https://inventhigh.net/udemy/quantitative-finance-with-python/)
22. Azure Open AI
 & Prompt Engineering Zero to Hero with Chatgpt-[https://inventhigh.net/udemy/azopenai/](https://inventhigh.net/udemy/az
openai/)
23. Object Oriented Programming in C++  &  Interview Preparation-[https://inventhigh.net/udemy/cracking-cpp-int
erview/](https://inventhigh.net/udemy/cracking-cpp-interview/)
24. Gatsby JS | Build a personal blog using gatsbyJS-[htt
ps://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/](https://inventhigh.net/udemy/g
atsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/)
25. Drupal For Absolute Beginners (2023)-[https://inventh
igh.net/udemy/drupal-masterclass/](https://inventhigh.net/udemy/drupal-masterclass/)
26. ChatGPT Plugins: The Complete G
uide-[https://inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/](https://inventhigh.net/udemy/chatgpt-plugins-the
-complete-guide/)
27. Build, Host & Manage WordPress Websites using AI \[10Web\]-[https://inventhigh.net/udemy/build-hos
t-manage-super-fast-wordpress-websites-in-10web/](https://inventhigh.net/udemy/build-host-manage-super-fast-wordpress-we
bsites-in-10web/)
28. PHP & MySQL - Certification Course for Beginners-[https://inventhigh.net/udemy/php-mysql-certifica
tion-course-for-beginners/](https://inventhigh.net/udemy/php-mysql-certification-course-for-beginners/)
29. Introduction
 to Domain Names and Web Hosting - Quick Guide-[https://inventhigh.net/udemy/introduction-to-domain-names-and-web-hostin
g-quick-guide/](https://inventhigh.net/udemy/introduction-to-domain-names-and-web-hosting-quick-guide/)
30. HTML, JavaSc
ript, & Bootstrap - Certification Course-[https://inventhigh.net/udemy/html-javascript-bootstrap-certification-course/](
https://inventhigh.net/udemy/html-javascript-bootstrap-certification-course/)
31. HTML & CSS - Certification Course for 
Beginners-[https://inventhigh.net/udemy/html-css-certification-course-for-beginners/](https://inventhigh.net/udemy/html-
css-certification-course-for-beginners/)
32. Create a Members Only Blog using PHP, MySQL, & AJAX-[https://inventhigh.net
/udemy/create-a-members-only-blog-using-php-mysql-ajax/](https://inventhigh.net/udemy/create-a-members-only-blog-using-p
hp-mysql-ajax/)
33. Configure NGINX on a Cloud Server: Digital Ocean & AWS-[https://inventhigh.net/udemy/configure-nginx
-on-a-cloud-server-digital-ocean-aws/](https://inventhigh.net/udemy/configure-nginx-on-a-cloud-server-digital-ocean-aws/
)
34. Cloud Computing Essentials: Linode, Linux, and LAMP Stack-[https://inventhigh.net/udemy/cloud-computing-essentials
-linode-linux-and-lamp-stack/](https://inventhigh.net/udemy/cloud-computing-essentials-linode-linux-and-lamp-stack/)
35.
 ChatGPT Expert Professional Certification-[https://inventhigh.net/udemy/chatgpt\_expert/](https://inventhigh.net/udemy/
chatgpt_expert/)
36. Adobe Lightroom Classic CC: Master the Library Module-[https://inventhigh.net/udemy/adobe-lightroom
-classic-cc-master-the-library-module/](https://inventhigh.net/udemy/adobe-lightroom-classic-cc-master-the-library-modul
e/)
37. Practical Photography for Absolute Beginners: 9 Courses in 1-[https://inventhigh.net/udemy/complete-photography-
course/](https://inventhigh.net/udemy/complete-photography-course/)
38. Practical Cisco Networking Labs in Cisco Packet 
Tracer-[https://inventhigh.net/udemy/practical-cisco-networking-labs/](https://inventhigh.net/udemy/practical-cisco-netw
orking-labs/)
39. Information Security Fundamentals-[https://inventhigh.net/udemy/infosec-fundamentals/](https://inventh
igh.net/udemy/infosec-fundamentals/)
40. Create a WordPress website with Hostinger!-[https://inventhigh.net/udemy/wordpr
ess-and-hosting-for-beginners/](https://inventhigh.net/udemy/wordpress-and-hosting-for-beginners/)
41. Tally Erp 9 + Tal
ly Prime + GST - Certificate Course-[https://inventhigh.net/udemy/tallygst/](https://inventhigh.net/udemy/tallygst/)
42.
 Building AI Saas Apps / AI Tools with \[No Code\] x ChatGPT-[https://inventhigh.net/udemy/ai-saas-apps/](https://invent
high.net/udemy/ai-saas-apps/)
43. Excel for Data Analysis & Financial Analysis-[https://inventhigh.net/udemy/microsoft-e
xcel-course-for-financial-analysis/](https://inventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/)
44. TI
KTOK Masterclass: Build Your Business With TIKTOK-[https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-w
ith-tiktok/](https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-with-tiktok/)
45. Squarespace Templates
 Unleashed: Rapid Professional Websites-[https://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional
-websites/](https://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional-websites/)
46. Squarespace B
ox of Tricks: Master Website Builders in 2023-[https://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/](https
://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/)
47. Sell Photo Online: Beginners Guide Stock Photography-
[https://inventhigh.net/udemy/mastering-stock-photography-step-by-step-guideline/](https://inventhigh.net/udemy/masterin
g-stock-photography-step-by-step-guideline/)
48. SEO Link Building & Content Writing Course: Get HQ Backlinks-[https://i
nventhigh.net/udemy/seo-link-building-2023/](https://inventhigh.net/udemy/seo-link-building-2023/)
49. PowerPoint - Micr
osoft PowerPoint For Beginners 2023-[https://inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/](https:
//inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/)
50. Macroeconomic Analysis: Investigating Inflati
on Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/](https://inve
nthigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/)
51. Learn 10 Ways to Make MORE Money on Y
ouTube!-[https://inventhigh.net/udemy/learn-to-make-money-on-youtube/](https://inventhigh.net/udemy/learn-to-make-money-
on-youtube/)
52. LangChain & OpenAI: Build Python Projects with No-Code 2023-[https://inventhigh.net/udemy/langchain-ope
nai-chatgpt-api-for-no-code-python-developers/](https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-py
thon-developers/)
53. JavaScript And PHP Programming Complete Course-[https://inventhigh.net/udemy/javascript-and-php-pr
ogramming-complete-course/](https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/)
54. How to Tra
nsform Your Life with 12 Amazing Powers-[https://inventhigh.net/udemy/12-great-powers-to-change-your-life/](https://inve
nthigh.net/udemy/12-great-powers-to-change-your-life/)
55. How to Make Money with YOUTUBE SHORTS Worldwide-[https://inve
nthigh.net/udemy/how-to-make-money-with-youtube-shorts/](https://inventhigh.net/udemy/how-to-make-money-with-youtube-sho
rts/)
56. How To Write Your Business Plan (in One Day} With ChatGPT-[https://inventhigh.net/udemy/business-planning-simp
lified-write-your-plan-with-chatgpt/](https://inventhigh.net/udemy/business-planning-simplified-write-your-plan-with-cha
tgpt/)
57. English Grammar tenses & structures-[https://inventhigh.net/udemy/english-grammar-course-tenses-structures/](
https://inventhigh.net/udemy/english-grammar-course-tenses-structures/)
58. Drinking Water Explained: Safety, Process & 
Challenges-[https://inventhigh.net/udemy/introduction-to-drinking-water-treatment/](https://inventhigh.net/udemy/introdu
ction-to-drinking-water-treatment/)
59. Dog Training Secrets: Behavior Insights-[https://inventhigh.net/udemy/dog-traini
ng-and-behavior-learn-research-backed-approaches/](https://inventhigh.net/udemy/dog-training-and-behavior-learn-research
-backed-approaches/)
60. ChatGPT: Make Money with ChatGPT as a New Freelancer-[https://inventhigh.net/udemy/chatgpt-make
-money-with-chatgpt-as-a-new-freelancer/](https://inventhigh.net/udemy/chatgpt-make-money-with-chatgpt-as-a-new-freelanc
er/)
61. Chair Yoga Teacher Training Certificate - Yoga Alliance CE-[https://inventhigh.net/udemy/chair-yoga-teacher-tra
ining-certificate-yoga-alliance-ce/](https://inventhigh.net/udemy/chair-yoga-teacher-training-certificate-yoga-alliance-
ce/)
62. C++ And Java Training Crash Course 2022-[https://inventhigh.net/udemy/c-and-java-training-crash-course-2022/](h
ttps://inventhigh.net/udemy/c-and-java-training-crash-course-2022/)
63. Best of Digital Marketing: #1 Digital Marketing 
Course 2023-[https://inventhigh.net/udemy/digital-marketing-2021/](https://inventhigh.net/udemy/digital-marketing-2021/)

64. YouTube Academy 2023: Complete Beginner to Pro Step-by-Step-[https://inventhigh.net/udemy/youtubeacademy/](https://
inventhigh.net/udemy/youtubeacademy/)
65. Work from Home : Work Life Balance and Time Management-[https://inventhigh.net
/udemy/work-from-home-work-life-balance/](https://inventhigh.net/udemy/work-from-home-work-life-balance/)
66. Video Edit
ing with Avid Media Composer First for Beginners-[https://inventhigh.net/udemy/learn-avid-media-composer-first-for-begin
ners/](https://inventhigh.net/udemy/learn-avid-media-composer-first-for-beginners/)
67. Video Editing with Adobe Premier
e Pro CC for Beginners-[https://inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/](https://in
venthigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/)
68. The Mega PRO Digital Marketing Course A-
Z : In Hindi-[https://inventhigh.net/udemy/learn-digital-marketing-course-hindi/](https://inventhigh.net/udemy/learn-dig
ital-marketing-course-hindi/)
69. The Complete Teach-Yourself Drummer's Guide-[https://inventhigh.net/udemy/the-complete
-teach-yourself-drummers-guide/](https://inventhigh.net/udemy/the-complete-teach-yourself-drummers-guide/)
70. The Art o
f the Portrait - Drawing For Beginners-[https://inventhigh.net/udemy/master-portrait-drawing/](https://inventhigh.net/ud
emy/master-portrait-drawing/)
71. Start a Profitable Affiliate Coupons Website -Passive Income-[https://inventhigh.net/u
demy/start-a-profitable-discount-coupons-website-passive-income/](https://inventhigh.net/udemy/start-a-profitable-discou
nt-coupons-website-passive-income/)
72. Print on Demand 2023: From Zero to Profitable Business-[https://inventhigh.net/u
demy/print-on-demand-course/](https://inventhigh.net/udemy/print-on-demand-course/)
73. PowerShell Functions Master Clas
s-[https://inventhigh.net/udemy/powershell-functions-master-class/](https://inventhigh.net/udemy/powershell-functions-ma
ster-class/)
74. Pedagogy in Teaching, Lesson Plan & Classroom Management-[https://inventhigh.net/udemy/pedagogy-in-teac
hing-lesson-plan-classroom-management/](https://inventhigh.net/udemy/pedagogy-in-teaching-lesson-plan-classroom-manageme
nt/)
75. Options Trading for Beginners - Intro Session-[https://inventhigh.net/udemy/options-trading-for-beginners-intro
-session/](https://inventhigh.net/udemy/options-trading-for-beginners-intro-session/)
76. Online Course Masterclass: Cre
ate Your Own Course In 30 Days-[https://inventhigh.net/udemy/online-course-masterclass/](https://inventhigh.net/udemy/on
line-course-masterclass/)
77. Media Mindful \[A Digital Detox Journey\]-[https://inventhigh.net/udemy/media-mindful-a-di
gital-detox-journey/](https://inventhigh.net/udemy/media-mindful-a-digital-detox-journey/)
78. Mastering Doodly: Create 
Engaging Whiteboard Animations-[https://inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/](https:
//inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/)
79. Make YouTube Thumbnails & Get More Views
 (Photoshop +Online)-[https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/](https:/
/inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/)
80. Macroeconomic Analysis: Investig
ating Inflation Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/]
(https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/)
81. Learn Structural Enginee
ring by Drawing Reading & ETABS-[https://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/](h
ttps://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/)
82. Learn Graphic Design using Canv
a & Start Freelancing-[https://inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/](https://
inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/)
83. Learn Content Writing using AI & St
art Freelancing-[https://inventhigh.net/udemy/ai-content-writing/](https://inventhigh.net/udemy/ai-content-writing/)
84.
 Learn Content Writing using AI & Make Money Online-[https://inventhigh.net/udemy/ai-content-course/](https://inventhigh
.net/udemy/ai-content-course/)
85. Learn Basics of Adobe Photoshop CC for Beginners-[https://inventhigh.net/udemy/learn-
basics-of-adobe-photoshop-cc-for-beginners/](https://inventhigh.net/udemy/learn-basics-of-adobe-photoshop-cc-for-beginne
rs/)
86. Learn Basics Of Adobe After Effects CC for Beginners-[https://inventhigh.net/udemy/learn-basics-of-adobe-after-
effects-cc-for-beginners-learn/](https://inventhigh.net/udemy/learn-basics-of-adobe-after-effects-cc-for-beginners-learn
/)
87. How to be a programmer | Full guide to start (Arabic)-[https://inventhigh.net/udemy/how\_to\_become\_a\_programme
r/](https://inventhigh.net/udemy/how_to_become_a_programmer/)
88. Grow Your YouTube Channel Faster 2023 (Advanced) StepB
yStep-[https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-proven-results-2022/](https://inventhigh.net/u
demy/the-youtube-academy-speed-growth-plan-proven-results-2022/)
89. Generate Income with Your YouTube, Despite Limited 
Views-[https://inventhigh.net/udemy/generate-income-with-your-youtube-despite-limited-views/](https://inventhigh.net/ude
my/generate-income-with-your-youtube-despite-limited-views/)
90. Fundamentals of computer science | Short Term Course(Ar
abic)-[https://inventhigh.net/udemy/basics\_of\_programming/](https://inventhigh.net/udemy/basics_of_programming/)
91. E
xecutive Diploma in Corporate Entrepreneurship-[https://inventhigh.net/udemy/corporate-entrepreneurship/](https://invent
high.net/udemy/corporate-entrepreneurship/)
92. Executive Diploma in Business Strategy-[https://inventhigh.net/udemy/dip
loma-business-strategy/](https://inventhigh.net/udemy/diploma-business-strategy/)
93. Executive Assistant Professional C
ertification (EAPC)-[https://inventhigh.net/udemy/executive-assistant/](https://inventhigh.net/udemy/executive-assistant
/)
94. Disruptive Thinking For World-Changing Innovative Ideas-[https://inventhigh.net/udemy/disruptive-thinking/](https
://inventhigh.net/udemy/disruptive-thinking/)
95. Diploma In Concrete Technology l Be a Concrete Technologist-[https://i
nventhigh.net/udemy/concrete-technologycivil-engineers-lifeline-in-construction/](https://inventhigh.net/udemy/concrete-
technologycivil-engineers-lifeline-in-construction/)
96. Create and Sell Digital Art using AI \[Passive Income\]-[https:
//inventhigh.net/udemy/ai-art-course/](https://inventhigh.net/udemy/ai-art-course/)
97. Color Grading and Video Editing 
with Davinci Resolve 18-[https://inventhigh.net/udemy/color-grading-and-video-editing-with-davinci-resolve/](https://inv
enthigh.net/udemy/color-grading-and-video-editing-with-davinci-resolve/)
98. Color Correction & Grading with Adobe Premi
ere Pro-[https://inventhigh.net/udemy/color-correction-grading-with-adobe-premiere-pro/](https://inventhigh.net/udemy/co
lor-correction-grading-with-adobe-premiere-pro/)
99. Cold Email & Lead Generation using AI \[Masterclass\]-[https://inve
nthigh.net/udemy/ai-cold-email/](https://inventhigh.net/udemy/ai-cold-email/)
100. Chat GPT & Midjourney: Personal Digit
al Marketing Assistants-[https://inventhigh.net/udemy/chatgpt-digital-marketing/](https://inventhigh.net/udemy/chatgpt-d
igital-marketing/)
101. C programming language | The Complete C Course (Arabic)-[https://inventhigh.net/udemy/c-programm
ing-language-from-a-to-z/](https://inventhigh.net/udemy/c-programming-language-from-a-to-z/)
102. Business Networking fo
r Success and Company Growth: Part One-[https://inventhigh.net/udemy/business-networking-1/](https://inventhigh.net/udem
y/business-networking-1/)
103. Build a Profitable Online Courses Business \[Complete Guide\]-[https://inventhigh.net/ude
my/complete-guide-become-a-six-figure-online-course-instructor/](https://inventhigh.net/udemy/complete-guide-become-a-si
x-figure-online-course-instructor/)
104. Become a Successful Affiliate Marketer \[Success Blueprint\]-[https://inventhig
h.net/udemy/become-a-six-figure-affiliate-marketer-success-blueprint/](https://inventhigh.net/udemy/become-a-six-figure-
affiliate-marketer-success-blueprint/)
105. Arabic| Learn Arabic with Mina | Comprehensive Arabic course-[https://invent
high.net/udemy/learn-arabic-language-d/](https://inventhigh.net/udemy/learn-arabic-language-d/)
106. Affiliate Marketing
 & MLM Network Marketing For Fashion-[https://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fas
hion/](https://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/)
107. AI x ChatGPT for Pr
oductivity 101 \[Masterclass\]-[https://inventhigh.net/udemy/ai-productivity/](https://inventhigh.net/udemy/ai-productiv
ity/)
108. AI for Business Strategy & Planning \[Masterclass\]-[https://inventhigh.net/udemy/ai-business-course/](https:
//inventhigh.net/udemy/ai-business-course/)
109. Private Equity Course for Beginners (PEQ101)-[https://inventhigh.net/ud
emy/private-equity-course-for-beginners-peq101/](https://inventhigh.net/udemy/private-equity-course-for-beginners-peq101
/)
110. Personal Brand Mastery : Online Personal Branding Essentials-[https://inventhigh.net/udemy/personal-branding-mas
tery-online-personal-branding-essentials/](https://inventhigh.net/udemy/personal-branding-mastery-online-personal-brandi
ng-essentials/)
111. Nuts & Bolts of Capital Markets-[https://inventhigh.net/udemy/nuts-bolts-of-capital-markets/](https
://inventhigh.net/udemy/nuts-bolts-of-capital-markets/)
112. Mechanical Engineering Mastery Series : HVAC Engineering 10
1-[https://inventhigh.net/udemy/mechanical-engineering-course/](https://inventhigh.net/udemy/mechanical-engineering-cour
se/)
113. Mastering Presentations and Public Speaking (Ultimate guide)-[https://inventhigh.net/udemy/presentations-and-p
ublic-speaking/](https://inventhigh.net/udemy/presentations-and-public-speaking/)
114. Investment Banking for Beginners 
(IB101)-[https://inventhigh.net/udemy/investment-banking-for-beginners-ib101/](https://inventhigh.net/udemy/investment-b
anking-for-beginners-ib101/)
115. Introduction to Microsoft Word for Beginners to Intermediate-[https://inventhigh.net/u
demy/introduction-to-microsoft-word-for-beginners/](https://inventhigh.net/udemy/introduction-to-microsoft-word-for-begi
nners/)
116. Internet & Cloud Computing Foundations-[https://inventhigh.net/udemy/internet-cloud-computing-foundations/]
(https://inventhigh.net/udemy/internet-cloud-computing-foundations/)
117. How the Internet Works & the Web Development P
rocess-[https://inventhigh.net/udemy/how-the-internet-works-the-web-development-process/](https://inventhigh.net/udemy/h
ow-the-internet-works-the-web-development-process/)
118. HVAC Design Basics : Understanding HVAC systems With Details-[h
ttps://inventhigh.net/udemy/hvac-systems/](https://inventhigh.net/udemy/hvac-systems/)
119. Financial Modeling in Excel 
- DCF Model of Big Books Corp-[https://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/](htt
ps://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/)
120. Financial Modeling | Social Medi
a Sector : Twitter-[https://inventhigh.net/udemy/financial-modeling-social-media-sector-twitter/](https://inventhigh.net
/udemy/financial-modeling-social-media-sector-twitter/)
121. Financial Modeling | Food & Beverages Sector : Starbucks-[h
ttps://inventhigh.net/udemy/financial-modeling-food-beverages-sector-starbucks/](https://inventhigh.net/udemy/financial-
modeling-food-beverages-sector-starbucks/)
122. Financial Analysis & Modeling | Islamic Banking-[https://inventhigh.net/
udemy/financial-modeling-islamic-banking-modeling/](https://inventhigh.net/udemy/financial-modeling-islamic-banking-mode
ling/)
123. Financial Analysis & Modeling | Automobile Sector-[https://inventhigh.net/udemy/financial-modeling-automobil
e-sector-maruti-suzuki/](https://inventhigh.net/udemy/financial-modeling-automobile-sector-maruti-suzuki/)
124. Computer
 Vision Fundamentals-[https://inventhigh.net/udemy/computer-vision-fundamentals/](https://inventhigh.net/udemy/computer-
vision-fundamentals/)
125. Complete Guide to Explosive Power Training-[https://inventhigh.net/udemy/athletic-power-train
ing-certificate/](https://inventhigh.net/udemy/athletic-power-training-certificate/)
126. Chief Customer Experience Offi
cer Executive Certification-[https://inventhigh.net/udemy/chief\_customer\_experience\_officer/](https://inventhigh.net/
udemy/chief_customer_experience_officer/)
127. Candlestick Chart Pattern & Renko Trading (2 Course Bundle)-[https://inve
nthigh.net/udemy/candlestick-renko/](https://inventhigh.net/udemy/candlestick-renko/)
128. CEO Chief Executive Officer E
xecutive Certification-[https://inventhigh.net/udemy/certified-chief-executive-officer/](https://inventhigh.net/udemy/ce
rtified-chief-executive-officer/)
129. Artificial General Intelligence (AGI)-[https://inventhigh.net/udemy/artificial-ge
neral-intelligence/](https://inventhigh.net/udemy/artificial-general-intelligence/)
130. Apache Hive for Data Engineers 
(Hands On) with 2 Projects-[https://inventhigh.net/udemy/apache-hive-for-data-engineers-hands-on/](https://inventhigh.ne
t/udemy/apache-hive-for-data-engineers-hands-on/)
131. 4 Comprehensive Practice Tests for any Python Certification-[http
s://inventhigh.net/udemy/4-comprehensive-practice-tests-for-any-python-certification/](https://inventhigh.net/udemy/4-co
mprehensive-practice-tests-for-any-python-certification/)
132. \[Weight Loss\] : Get Your Dream Body with Diet & Cardio-
[https://inventhigh.net/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/](https://inventhigh.net/udemy/weigh
t-loss-get-your-dream-body-with-nutrition-cardio/)
133. \[Tips & Technics\] : How to Lead Effective Meetings 2022 -New-[
https://inventhigh.net/udemy/tips-technics-how-to-lead-effective-meetings-2022/](https://inventhigh.net/udemy/tips-techn
ics-how-to-lead-effective-meetings-2022/)
134. \[Tips & Technics\] : How to Become a Great Leader Skills 2022-[https://i
nventhigh.net/udemy/tips-technics-how-to-become-a-great-leader-skills/](https://inventhigh.net/udemy/tips-technics-how-t
o-become-a-great-leader-skills/)
135. \[Practice Exams\] AWS Certified Solutions Architect Associate-[https://inventhigh
.net/udemy/practice-exams-aws-certified-solutions-architect-associate-u/](https://inventhigh.net/udemy/practice-exams-aw
s-certified-solutions-architect-associate-u/)
```
---

     
 
all -  [ 300+ Free Udemy Certificate Courses -Limited Time - 19/10/23 ](https://www.reddit.com/r/udemyfreebies/comments/17b9jpo/300_free_udemy_certificate_courses_limited_time/) , 2023-10-20-0909
```
 View All Courses: https://inventhigh.net                 

1. WordPress Theme Development from Scratch 2.0-[https://inv
enthigh.net/udemy/advanced-wordpress-theme-development-with-bootstrap/](https://inventhigh.net/udemy/advanced-wordpress-
theme-development-with-bootstrap/) 

2. WooCommerce Theme Development: Advanced Course-[https://inventhigh.net/udemy/woo
commerce-wordpress-theme-development/](https://inventhigh.net/udemy/woocommerce-wordpress-theme-development/) 

3. Ultra
-Fast WordPress Speed With 10Web WordPress Web Hosting-[https://inventhigh.net/udemy/ultra-fast-wordpress-speed/](https:
//inventhigh.net/udemy/ultra-fast-wordpress-speed/) 

4. Python Programming Language | Master Python Course (Arabic)-[ht
tps://inventhigh.net/udemy/python\_tutorials/](https://inventhigh.net/udemy/python_tutorials/) 

5. Python And Flask  De
monstrations Practice Course-[https://inventhigh.net/udemy/python-and-flask-only-demonstration-course/](https://inventhi
gh.net/udemy/python-and-flask-only-demonstration-course/) 

6. Linux Tmux-[https://inventhigh.net/udemy/linux-tmux/](htt
ps://inventhigh.net/udemy/linux-tmux/) 

7. Learn Web Design using WordPress & Start Freelancing-[https://inventhigh.net
/udemy/become-successful-wordpress-freelancer-to-make-money-online/](https://inventhigh.net/udemy/become-successful-word
press-freelancer-to-make-money-online/) 

8. Haskell Exercises for Beginners-[https://inventhigh.net/udemy/haskell-exerc
ises-for-beginners/](https://inventhigh.net/udemy/haskell-exercises-for-beginners/) 

9. Convert a one page HTML5 Templa
te to a WordPress Theme-[https://inventhigh.net/udemy/convert-html5-template-to-wordpress-theme/](https://inventhigh.net
/udemy/convert-html5-template-to-wordpress-theme/) 

10. Computer Basics-[https://inventhigh.net/udemy/basic-of-computer
/](https://inventhigh.net/udemy/basic-of-computer/) 

11. CSS Crash Course For Beginners-[https://inventhigh.net/udemy/c
ss-crash-course-for-beginners-g/](https://inventhigh.net/udemy/css-crash-course-for-beginners-g/) 

12. Asteroids with P
ython PyGame-[https://inventhigh.net/udemy/asteroids-with-python-pygame/](https://inventhigh.net/udemy/asteroids-with-py
thon-pygame/) 

13. Linode: Foundations of Web Server Security-[https://inventhigh.net/udemy/linode-foundations-of-web-s
erver-security/](https://inventhigh.net/udemy/linode-foundations-of-web-server-security/) 

14. Linode: Build and Deploy
 Responsive Websites on the Cloud-[https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud
/](https://inventhigh.net/udemy/linode-build-and-deploy-responsive-websites-on-the-cloud/) 

15. Learn Bootstrap - For B
eginners-[https://inventhigh.net/udemy/learn-bootstrap-for-beginners/](https://inventhigh.net/udemy/learn-bootstrap-for-
beginners/) 

16. JavaScript, Bootstrap, & PHP - Certification for Beginners-[https://inventhigh.net/udemy/javascript-bo
otstrap-php-certification-for-beginners/](https://inventhigh.net/udemy/javascript-bootstrap-php-certification-for-beginn
ers/) 

17. Bootstrap & jQuery - Certification Course for Beginners-[https://inventhigh.net/udemy/bootstrap-jquery-certi
fication-course-for-beginners/](https://inventhigh.net/udemy/bootstrap-jquery-certification-course-for-beginners/) 

18.
 AWS Beginner to Intermediate: EC2, IAM, ELB, ASG, Route 53-[https://inventhigh.net/udemy/aws-beginner-to-intermediate-e
c2-iam-elb-asg-route-53/](https://inventhigh.net/udemy/aws-beginner-to-intermediate-ec2-iam-elb-asg-route-53/) 

19. AWS
 & React: Deploy an Auto-Scaling E-Commerce App with ELB-[https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-
e-commerce-app-with-elb/](https://inventhigh.net/udemy/aws-react-deploy-an-auto-scaling-e-commerce-app-with-elb/) 

20. 
DevOps Interview Questions Preparation Guide - 2023-[https://inventhigh.net/udemy/devops-interview-questions-preparation
-guide/](https://inventhigh.net/udemy/devops-interview-questions-preparation-guide/) 

21. Quantitative Finance with Pyt
hon-[https://inventhigh.net/udemy/quantitative-finance-with-python/](https://inventhigh.net/udemy/quantitative-finance-w
ith-python/) 

22. Azure Open AI & Prompt Engineering Zero to Hero with Chatgpt-[https://inventhigh.net/udemy/azopenai/]
(https://inventhigh.net/udemy/azopenai/) 

23. Object Oriented Programming in C++  &  Interview Preparation-[https://inv
enthigh.net/udemy/cracking-cpp-interview/](https://inventhigh.net/udemy/cracking-cpp-interview/) 

24. Gatsby JS | Build
 a personal blog using gatsbyJS-[https://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-grap
hql/](https://inventhigh.net/udemy/gatsbyjs-graphql-build-a-personal-blog-using-gatsbyjs-graphql/) 

25. Drupal For Abso
lute Beginners (2023)-[https://inventhigh.net/udemy/drupal-masterclass/](https://inventhigh.net/udemy/drupal-masterclass
/) 

26. ChatGPT Plugins: The Complete Guide-[https://inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/](https://
inventhigh.net/udemy/chatgpt-plugins-the-complete-guide/) 

27. Build, Host & Manage WordPress Websites using AI \[10Web
\]-[https://inventhigh.net/udemy/build-host-manage-super-fast-wordpress-websites-in-10web/](https://inventhigh.net/udemy
/build-host-manage-super-fast-wordpress-websites-in-10web/) 

28. PHP & MySQL - Certification Course for Beginners-[http
s://inventhigh.net/udemy/php-mysql-certification-course-for-beginners/](https://inventhigh.net/udemy/php-mysql-certifica
tion-course-for-beginners/) 

29. Introduction to Domain Names and Web Hosting - Quick Guide-[https://inventhigh.net/ude
my/introduction-to-domain-names-and-web-hosting-quick-guide/](https://inventhigh.net/udemy/introduction-to-domain-names-
and-web-hosting-quick-guide/) 

30. HTML, JavaScript, & Bootstrap - Certification Course-[https://inventhigh.net/udemy/h
tml-javascript-bootstrap-certification-course/](https://inventhigh.net/udemy/html-javascript-bootstrap-certification-cou
rse/) 

31. HTML & CSS - Certification Course for Beginners-[https://inventhigh.net/udemy/html-css-certification-course-
for-beginners/](https://inventhigh.net/udemy/html-css-certification-course-for-beginners/) 

32. Create a Members Only B
log using PHP, MySQL, & AJAX-[https://inventhigh.net/udemy/create-a-members-only-blog-using-php-mysql-ajax/](https://inv
enthigh.net/udemy/create-a-members-only-blog-using-php-mysql-ajax/) 

33. Configure NGINX on a Cloud Server: Digital Oce
an & AWS-[https://inventhigh.net/udemy/configure-nginx-on-a-cloud-server-digital-ocean-aws/](https://inventhigh.net/udem
y/configure-nginx-on-a-cloud-server-digital-ocean-aws/) 

34. Cloud Computing Essentials: Linode, Linux, and LAMP Stack-
[https://inventhigh.net/udemy/cloud-computing-essentials-linode-linux-and-lamp-stack/](https://inventhigh.net/udemy/clou
d-computing-essentials-linode-linux-and-lamp-stack/) 

35. ChatGPT Expert Professional Certification-[https://inventhigh
.net/udemy/chatgpt\_expert/](https://inventhigh.net/udemy/chatgpt_expert/) 

36. Adobe Lightroom Classic CC: Master the 
Library Module-[https://inventhigh.net/udemy/adobe-lightroom-classic-cc-master-the-library-module/](https://inventhigh.n
et/udemy/adobe-lightroom-classic-cc-master-the-library-module/) 

37. Practical Photography for Absolute Beginners: 9 Co
urses in 1-[https://inventhigh.net/udemy/complete-photography-course/](https://inventhigh.net/udemy/complete-photography
-course/) 

38. Practical Cisco Networking Labs in Cisco Packet Tracer-[https://inventhigh.net/udemy/practical-cisco-net
working-labs/](https://inventhigh.net/udemy/practical-cisco-networking-labs/) 

39. Information Security Fundamentals-[h
ttps://inventhigh.net/udemy/infosec-fundamentals/](https://inventhigh.net/udemy/infosec-fundamentals/) 

40. Create a Wo
rdPress website with Hostinger!-[https://inventhigh.net/udemy/wordpress-and-hosting-for-beginners/](https://inventhigh.n
et/udemy/wordpress-and-hosting-for-beginners/) 

41. Tally Erp 9 + Tally Prime + GST - Certificate Course-[https://inven
thigh.net/udemy/tallygst/](https://inventhigh.net/udemy/tallygst/) 

42. Building AI Saas Apps / AI Tools with \[No Code
\] x ChatGPT-[https://inventhigh.net/udemy/ai-saas-apps/](https://inventhigh.net/udemy/ai-saas-apps/) 

43. Excel for Da
ta Analysis & Financial Analysis-[https://inventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/](https://i
nventhigh.net/udemy/microsoft-excel-course-for-financial-analysis/) 

44. TIKTOK Masterclass: Build Your Business With T
IKTOK-[https://inventhigh.net/udemy/tiktok-masterclass-build-your-business-with-tiktok/](https://inventhigh.net/udemy/ti
ktok-masterclass-build-your-business-with-tiktok/) 

45. Squarespace Templates Unleashed: Rapid Professional Websites-[h
ttps://inventhigh.net/udemy/squarespace-templates-unleashed-rapid-professional-websites/](https://inventhigh.net/udemy/s
quarespace-templates-unleashed-rapid-professional-websites/) 

46. Squarespace Box of Tricks: Master Website Builders in
 2023-[https://inventhigh.net/udemy/squarespace-web-design-box-of-tricks/](https://inventhigh.net/udemy/squarespace-web-
design-box-of-tricks/) 

47. Sell Photo Online: Beginners Guide Stock Photography-[https://inventhigh.net/udemy/masterin
g-stock-photography-step-by-step-guideline/](https://inventhigh.net/udemy/mastering-stock-photography-step-by-step-guide
line/) 

48. SEO Link Building & Content Writing Course: Get HQ Backlinks-[https://inventhigh.net/udemy/seo-link-buildin
g-2023/](https://inventhigh.net/udemy/seo-link-building-2023/) 

49. PowerPoint - Microsoft PowerPoint For Beginners 202
3-[https://inventhigh.net/udemy/powerpoint-microsoft-powerpoint-for-beginners/](https://inventhigh.net/udemy/powerpoint-
microsoft-powerpoint-for-beginners/) 

50. Macroeconomic Analysis: Investigating Inflation Trend with R-[https://inventh
igh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/](https://inventhigh.net/udemy/macroeconomic-a
nalysis-investigating-inflation-trend-with-r/) 

51. Learn 10 Ways to Make MORE Money on YouTube!-[https://inventhigh.ne
t/udemy/learn-to-make-money-on-youtube/](https://inventhigh.net/udemy/learn-to-make-money-on-youtube/) 

52. LangChain &
 OpenAI: Build Python Projects with No-Code 2023-[https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-
python-developers/](https://inventhigh.net/udemy/langchain-openai-chatgpt-api-for-no-code-python-developers/) 

53. Java
Script And PHP Programming Complete Course-[https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/
](https://inventhigh.net/udemy/javascript-and-php-programming-complete-course/) 

54. How to Transform Your Life with 12
 Amazing Powers-[https://inventhigh.net/udemy/12-great-powers-to-change-your-life/](https://inventhigh.net/udemy/12-grea
t-powers-to-change-your-life/) 

55. How to Make Money with YOUTUBE SHORTS Worldwide-[https://inventhigh.net/udemy/how-t
o-make-money-with-youtube-shorts/](https://inventhigh.net/udemy/how-to-make-money-with-youtube-shorts/) 

56. How To Wri
te Your Business Plan (in One Day} With ChatGPT-[https://inventhigh.net/udemy/business-planning-simplified-write-your-pl
an-with-chatgpt/](https://inventhigh.net/udemy/business-planning-simplified-write-your-plan-with-chatgpt/) 

57. English
 Grammar tenses & structures-[https://inventhigh.net/udemy/english-grammar-course-tenses-structures/](https://inventhigh
.net/udemy/english-grammar-course-tenses-structures/) 

58. Drinking Water Explained: Safety, Process & Challenges-[http
s://inventhigh.net/udemy/introduction-to-drinking-water-treatment/](https://inventhigh.net/udemy/introduction-to-drinkin
g-water-treatment/) 

59. Dog Training Secrets: Behavior Insights-[https://inventhigh.net/udemy/dog-training-and-behavio
r-learn-research-backed-approaches/](https://inventhigh.net/udemy/dog-training-and-behavior-learn-research-backed-approa
ches/) 

60. ChatGPT: Make Money with ChatGPT as a New Freelancer-[https://inventhigh.net/udemy/chatgpt-make-money-with-
chatgpt-as-a-new-freelancer/](https://inventhigh.net/udemy/chatgpt-make-money-with-chatgpt-as-a-new-freelancer/) 

61. C
hair Yoga Teacher Training Certificate - Yoga Alliance CE-[https://inventhigh.net/udemy/chair-yoga-teacher-training-cert
ificate-yoga-alliance-ce/](https://inventhigh.net/udemy/chair-yoga-teacher-training-certificate-yoga-alliance-ce/) 

62.
 C++ And Java Training Crash Course 2022-[https://inventhigh.net/udemy/c-and-java-training-crash-course-2022/](https://i
nventhigh.net/udemy/c-and-java-training-crash-course-2022/) 

63. Best of Digital Marketing: #1 Digital Marketing Course
 2023-[https://inventhigh.net/udemy/digital-marketing-2021/](https://inventhigh.net/udemy/digital-marketing-2021/) 

64.
 YouTube Academy 2023: Complete Beginner to Pro Step-by-Step-[https://inventhigh.net/udemy/youtubeacademy/](https://inve
nthigh.net/udemy/youtubeacademy/) 

65. Work from Home : Work Life Balance and Time Management-[https://inventhigh.net/u
demy/work-from-home-work-life-balance/](https://inventhigh.net/udemy/work-from-home-work-life-balance/) 

66. Video Edit
ing with Avid Media Composer First for Beginners-[https://inventhigh.net/udemy/learn-avid-media-composer-first-for-begin
ners/](https://inventhigh.net/udemy/learn-avid-media-composer-first-for-beginners/) 

67. Video Editing with Adobe Premi
ere Pro CC for Beginners-[https://inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/](https://
inventhigh.net/udemy/video-editing-with-adobe-premiere-pro-cc-for-beginners/) 

68. The Mega PRO Digital Marketing Cours
e A-Z : In Hindi-[https://inventhigh.net/udemy/learn-digital-marketing-course-hindi/](https://inventhigh.net/udemy/learn
-digital-marketing-course-hindi/) 

69. The Complete Teach-Yourself Drummer's Guide-[https://inventhigh.net/udemy/the-co
mplete-teach-yourself-drummers-guide/](https://inventhigh.net/udemy/the-complete-teach-yourself-drummers-guide/) 

70. T
he Art of the Portrait - Drawing For Beginners-[https://inventhigh.net/udemy/master-portrait-drawing/](https://inventhig
h.net/udemy/master-portrait-drawing/) 

71. Start a Profitable Affiliate Coupons Website -Passive Income-[https://invent
high.net/udemy/start-a-profitable-discount-coupons-website-passive-income/](https://inventhigh.net/udemy/start-a-profita
ble-discount-coupons-website-passive-income/) 

72. Print on Demand 2023: From Zero to Profitable Business-[https://inve
nthigh.net/udemy/print-on-demand-course/](https://inventhigh.net/udemy/print-on-demand-course/) 

73. PowerShell Functio
ns Master Class-[https://inventhigh.net/udemy/powershell-functions-master-class/](https://inventhigh.net/udemy/powershel
l-functions-master-class/) 

74. Pedagogy in Teaching, Lesson Plan & Classroom Management-[https://inventhigh.net/udemy/
pedagogy-in-teaching-lesson-plan-classroom-management/](https://inventhigh.net/udemy/pedagogy-in-teaching-lesson-plan-cl
assroom-management/) 

75. Options Trading for Beginners - Intro Session-[https://inventhigh.net/udemy/options-trading-f
or-beginners-intro-session/](https://inventhigh.net/udemy/options-trading-for-beginners-intro-session/) 

76. Online Cou
rse Masterclass: Create Your Own Course In 30 Days-[https://inventhigh.net/udemy/online-course-masterclass/](https://inv
enthigh.net/udemy/online-course-masterclass/) 

77. Media Mindful \[A Digital Detox Journey\]-[https://inventhigh.net/ud
emy/media-mindful-a-digital-detox-journey/](https://inventhigh.net/udemy/media-mindful-a-digital-detox-journey/) 

78. M
astering Doodly: Create Engaging Whiteboard Animations-[https://inventhigh.net/udemy/mastering-doodly-2d-animation-white
board-animation/](https://inventhigh.net/udemy/mastering-doodly-2d-animation-whiteboard-animation/) 

79. Make YouTube T
humbnails & Get More Views (Photoshop +Online)-[https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-
free-online-site/](https://inventhigh.net/udemy/create-youtube-thumbnails-in-photoshop-and-free-online-site/) 

80. Macr
oeconomic Analysis: Investigating Inflation Trend with R-[https://inventhigh.net/udemy/macroeconomic-analysis-investigat
ing-inflation-trend-with-r/](https://inventhigh.net/udemy/macroeconomic-analysis-investigating-inflation-trend-with-r/) 


81. Learn Structural Engineering by Drawing Reading & ETABS-[https://inventhigh.net/udemy/learn-structural-architectur
al-vastu-plans-along-etabs/](https://inventhigh.net/udemy/learn-structural-architectural-vastu-plans-along-etabs/) 

82.
 Learn Graphic Design using Canva & Start Freelancing-[https://inventhigh.net/udemy/canva-mastery-become-freelance-graph
ic-designer-in-1-hour/](https://inventhigh.net/udemy/canva-mastery-become-freelance-graphic-designer-in-1-hour/) 

83. L
earn Content Writing using AI & Start Freelancing-[https://inventhigh.net/udemy/ai-content-writing/](https://inventhigh.
net/udemy/ai-content-writing/) 

84. Learn Content Writing using AI & Make Money Online-[https://inventhigh.net/udemy/ai
-content-course/](https://inventhigh.net/udemy/ai-content-course/) 

85. Learn Basics of Adobe Photoshop CC for Beginner
s-[https://inventhigh.net/udemy/learn-basics-of-adobe-photoshop-cc-for-beginners/](https://inventhigh.net/udemy/learn-ba
sics-of-adobe-photoshop-cc-for-beginners/) 

86. Learn Basics Of Adobe After Effects CC for Beginners-[https://inventhig
h.net/udemy/learn-basics-of-adobe-after-effects-cc-for-beginners-learn/](https://inventhigh.net/udemy/learn-basics-of-ad
obe-after-effects-cc-for-beginners-learn/) 

87. How to be a programmer | Full guide to start (Arabic)-[https://inventhi
gh.net/udemy/how\_to\_become\_a\_programmer/](https://inventhigh.net/udemy/how_to_become_a_programmer/) 

88. Grow Your 
YouTube Channel Faster 2023 (Advanced) StepByStep-[https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-pr
oven-results-2022/](https://inventhigh.net/udemy/the-youtube-academy-speed-growth-plan-proven-results-2022/) 

89. Gener
ate Income with Your YouTube, Despite Limited Views-[https://inventhigh.net/udemy/generate-income-with-your-youtube-desp
ite-limited-views/](https://inventhigh.net/udemy/generate-income-with-your-youtube-despite-limited-views/) 

90. Fundame
ntals of computer science | Short Term Course(Arabic)-[https://inventhigh.net/udemy/basics\_of\_programming/](https://in
venthigh.net/udemy/basics_of_programming/) 

91. Executive Diploma in Corporate Entrepreneurship-[https://inventhigh.net
/udemy/corporate-entrepreneurship/](https://inventhigh.net/udemy/corporate-entrepreneurship/) 

92. Executive Diploma in
 Business Strategy-[https://inventhigh.net/udemy/diploma-business-strategy/](https://inventhigh.net/udemy/diploma-busine
ss-strategy/) 

93. Executive Assistant Professional Certification (EAPC)-[https://inventhigh.net/udemy/executive-assist
ant/](https://inventhigh.net/udemy/executive-assistant/) 

94. Disruptive Thinking For World-Changing Innovative Ideas-[
https://inventhigh.net/udemy/disruptive-thinking/](https://inventhigh.net/udemy/disruptive-thinking/) 

95. Diploma In C
oncrete Technology l Be a Concrete Technologist-[https://inventhigh.net/udemy/concrete-technologycivil-engineers-lifelin
e-in-construction/](https://inventhigh.net/udemy/concrete-technologycivil-engineers-lifeline-in-construction/) 

96. Cre
ate and Sell Digital Art using AI \[Passive Income\]-[https://inventhigh.net/udemy/ai-art-course/](https://inventhigh.ne
t/udemy/ai-art-course/) 

97. Color Grading and Video Editing with Davinci Resolve 18-[https://inventhigh.net/udemy/colo
r-grading-and-video-editing-with-davinci-resolve/](https://inventhigh.net/udemy/color-grading-and-video-editing-with-dav
inci-resolve/) 

98. Color Correction & Grading with Adobe Premiere Pro-[https://inventhigh.net/udemy/color-correction-g
rading-with-adobe-premiere-pro/](https://inventhigh.net/udemy/color-correction-grading-with-adobe-premiere-pro/) 

99. C
old Email & Lead Generation using AI \[Masterclass\]-[https://inventhigh.net/udemy/ai-cold-email/](https://inventhigh.ne
t/udemy/ai-cold-email/) 

100. Chat GPT & Midjourney: Personal Digital Marketing Assistants-[https://inventhigh.net/udem
y/chatgpt-digital-marketing/](https://inventhigh.net/udemy/chatgpt-digital-marketing/) 

101. C programming language | T
he Complete C Course (Arabic)-[https://inventhigh.net/udemy/c-programming-language-from-a-to-z/](https://inventhigh.net/
udemy/c-programming-language-from-a-to-z/) 

102. Business Networking for Success and Company Growth: Part One-[https://
inventhigh.net/udemy/business-networking-1/](https://inventhigh.net/udemy/business-networking-1/) 

103. Build a Profita
ble Online Courses Business \[Complete Guide\]-[https://inventhigh.net/udemy/complete-guide-become-a-six-figure-online-c
ourse-instructor/](https://inventhigh.net/udemy/complete-guide-become-a-six-figure-online-course-instructor/) 

104. Bec
ome a Successful Affiliate Marketer \[Success Blueprint\]-[https://inventhigh.net/udemy/become-a-six-figure-affiliate-ma
rketer-success-blueprint/](https://inventhigh.net/udemy/become-a-six-figure-affiliate-marketer-success-blueprint/) 

105
. Arabic| Learn Arabic with Mina | Comprehensive Arabic course-[https://inventhigh.net/udemy/learn-arabic-language-d/](h
ttps://inventhigh.net/udemy/learn-arabic-language-d/) 

106. Affiliate Marketing & MLM Network Marketing For Fashion-[ht
tps://inventhigh.net/udemy/affiliate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/](https://inventhigh.net/udemy/affi
liate-marketing-mlm-for-waveifyoulike-t-shirt-fashion/) 

107. AI x ChatGPT for Productivity 101 \[Masterclass\]-[https:
//inventhigh.net/udemy/ai-productivity/](https://inventhigh.net/udemy/ai-productivity/) 

108. AI for Business Strategy 
& Planning \[Masterclass\]-[https://inventhigh.net/udemy/ai-business-course/](https://inventhigh.net/udemy/ai-business-c
ourse/) 

109. Private Equity Course for Beginners (PEQ101)-[https://inventhigh.net/udemy/private-equity-course-for-begi
nners-peq101/](https://inventhigh.net/udemy/private-equity-course-for-beginners-peq101/) 

110. Personal Brand Mastery :
 Online Personal Branding Essentials-[https://inventhigh.net/udemy/personal-branding-mastery-online-personal-branding-es
sentials/](https://inventhigh.net/udemy/personal-branding-mastery-online-personal-branding-essentials/) 

111. Nuts & Bo
lts of Capital Markets-[https://inventhigh.net/udemy/nuts-bolts-of-capital-markets/](https://inventhigh.net/udemy/nuts-b
olts-of-capital-markets/) 

112. Mechanical Engineering Mastery Series : HVAC Engineering 101-[https://inventhigh.net/ud
emy/mechanical-engineering-course/](https://inventhigh.net/udemy/mechanical-engineering-course/) 

113. Mastering Presen
tations and Public Speaking (Ultimate guide)-[https://inventhigh.net/udemy/presentations-and-public-speaking/](https://i
nventhigh.net/udemy/presentations-and-public-speaking/) 

114. Investment Banking for Beginners (IB101)-[https://inventh
igh.net/udemy/investment-banking-for-beginners-ib101/](https://inventhigh.net/udemy/investment-banking-for-beginners-ib1
01/) 

115. Introduction to Microsoft Word for Beginners to Intermediate-[https://inventhigh.net/udemy/introduction-to-m
icrosoft-word-for-beginners/](https://inventhigh.net/udemy/introduction-to-microsoft-word-for-beginners/) 

116. Interne
t & Cloud Computing Foundations-[https://inventhigh.net/udemy/internet-cloud-computing-foundations/](https://inventhigh.
net/udemy/internet-cloud-computing-foundations/) 

117. How the Internet Works & the Web Development Process-[https://in
venthigh.net/udemy/how-the-internet-works-the-web-development-process/](https://inventhigh.net/udemy/how-the-internet-wo
rks-the-web-development-process/) 

118. HVAC Design Basics : Understanding HVAC systems With Details-[https://inventhig
h.net/udemy/hvac-systems/](https://inventhigh.net/udemy/hvac-systems/) 

119. Financial Modeling in Excel - DCF Model of
 Big Books Corp-[https://inventhigh.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/](https://inventhig
h.net/udemy/financial-modeling-in-excel-dcf-model-of-big-books-inc/) 

120. Financial Modeling | Social Media Sector : T
witter-[https://inventhigh.net/udemy/financial-modeling-social-media-sector-twitter/](https://inventhigh.net/udemy/finan
cial-modeling-social-media-sector-twitter/) 

121. Financial Modeling | Food & Beverages Sector : Starbucks-[https://inv
enthigh.net/udemy/financial-modeling-food-beverages-sector-starbucks/](https://inventhigh.net/udemy/financial-modeling-f
ood-beverages-sector-starbucks/) 

122. Financial Analysis & Modeling | Islamic Banking-[https://inventhigh.net/udemy/fi
nancial-modeling-islamic-banking-modeling/](https://inventhigh.net/udemy/financial-modeling-islamic-banking-modeling/) 


123. Financial Analysis & Modeling | Automobile Sector-[https://inventhigh.net/udemy/financial-modeling-automobile-sect
or-maruti-suzuki/](https://inventhigh.net/udemy/financial-modeling-automobile-sector-maruti-suzuki/) 

124. Computer Vis
ion Fundamentals-[https://inventhigh.net/udemy/computer-vision-fundamentals/](https://inventhigh.net/udemy/computer-visi
on-fundamentals/) 

125. Complete Guide to Explosive Power Training-[https://inventhigh.net/udemy/athletic-power-trainin
g-certificate/](https://inventhigh.net/udemy/athletic-power-training-certificate/) 

126. Chief Customer Experience Offi
cer Executive Certification-[https://inventhigh.net/udemy/chief\_customer\_experience\_officer/](https://inventhigh.net/
udemy/chief_customer_experience_officer/) 

127. Candlestick Chart Pattern & Renko Trading (2 Course Bundle)-[https://in
venthigh.net/udemy/candlestick-renko/](https://inventhigh.net/udemy/candlestick-renko/) 

128. CEO Chief Executive Offic
er Executive Certification-[https://inventhigh.net/udemy/certified-chief-executive-officer/](https://inventhigh.net/udem
y/certified-chief-executive-officer/) 

129. Artificial General Intelligence (AGI)-[https://inventhigh.net/udemy/artific
ial-general-intelligence/](https://inventhigh.net/udemy/artificial-general-intelligence/) 

130. Apache Hive for Data En
gineers (Hands On) with 2 Projects-[https://inventhigh.net/udemy/apache-hive-for-data-engineers-hands-on/](https://inven
thigh.net/udemy/apache-hive-for-data-engineers-hands-on/) 

131. 4 Comprehensive Practice Tests for any Python Certifica
tion-[https://inventhigh.net/udemy/4-comprehensive-practice-tests-for-any-python-certification/](https://inventhigh.net/
udemy/4-comprehensive-practice-tests-for-any-python-certification/) 

132. \[Weight Loss\] : Get Your Dream Body with Di
et & Cardio-[https://inventhigh.net/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/](https://inventhigh.net
/udemy/weight-loss-get-your-dream-body-with-nutrition-cardio/) 

133. \[Tips & Technics\] : How to Lead Effective Meetin
gs 2022 -New-[https://inventhigh.net/udemy/tips-technics-how-to-lead-effective-meetings-2022/](https://inventhigh.net/ud
emy/tips-technics-how-to-lead-effective-meetings-2022/) 

134. \[Tips & Technics\] : How to Become a Great Leader Skills
 2022-[https://inventhigh.net/udemy/tips-technics-how-to-become-a-great-leader-skills/](https://inventhigh.net/udemy/tip
s-technics-how-to-become-a-great-leader-skills/) 

135. \[Practice Exams\] AWS Certified Solutions Architect Associate-[
https://inventhigh.net/udemy/practice-exams-aws-certified-solutions-architect-associate-u/](https://inventhigh.net/udemy
/practice-exams-aws-certified-solutions-architect-associate-u/) 
```
---

     
 
all -  [ Suggestion: GPT4all-style LocalDocs collections ](https://www.reddit.com/r/faraday_dot_dev/comments/17b8ty0/suggestion_gpt4allstyle_localdocs_collections/) , 2023-10-20-0909
```
Dear Faraday devs,Firstly, thank you for an excellent product. I have no trouble spinning up a CLI and hooking to llama.
cpp directly, but your app makes it so much more pleasant.

If I might suggest something, please add support for local d
ocument collections (reference: [https://docs.gpt4all.io/gpt4all\_chat.html#localdocs-beta-plugin-chat-with-your-data](h
ttps://docs.gpt4all.io/gpt4all_chat.html#localdocs-beta-plugin-chat-with-your-data)). This would make characters vastly 
more useful for certain use cases - for example, a DIY repairman who has a corpus it can pull on, or fictional character
s who have world knowledge, like an engineer who has manuals for major spacecraft.

I do this already with my own Gradio
 + Langchain document loader setup, but honest Faraday is so much nicer to interact with. If you have the time to includ
e this, I'd really appreciate it. Even cooler (Although not strictly required) if it can be some kind of drag and drop d
ataset builder.

Cheers, and have a good day!

https://preview.redd.it/obx4f35lp2vb1.png?width=1496&format=png&auto=webp
&s=bbe05cb9dfd6aee8d62550f7f237bd2dbe2326d5
```
---

     
 
all -  [ Streaming not working when routing between Runnables ](https://www.reddit.com/r/LangChain/comments/17b5gaw/streaming_not_working_when_routing_between/) , 2023-10-20-0909
```
I'm trying to stream the response of a simple route I've created among 2 Runnables without success. When I stream each R
unnable independelty, it streams perfectly. When I create a route to choose which one of them should be the next step, i
t doesn't stream the result. Can someone provide some guidance?

Here's the example:

    # ----------------- Runnable 1
 -----------------
    
    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template='{page_content}')
    def _c
ombine_documents(docs, document_prompt = DEFAULT_DOCUMENT_PROMPT, document_separator='\n\n'):
      doc_strings = [forma
t_document(doc, document_prompt) for doc in docs]
      return document_separator.join(doc_strings)
      
    def _form
at_chat_history(chat_history: List[Tuple]) -> str:
      buffer = ''
        for dialogue_turn in chat_history:
        
  human = 'Human: ' + dialogue_turn[0]
          ai = 'Assistant: ' + dialogue_turn[1]
          buffer += '\n' + '\n'.j
oin([human, ai])
      return buffer
      
    _inputs = RunnableMap({
      'standalone_question': {
        'question
': lambda x: x['question'],
        'chat_history': lambda x: _format_chat_history(x['chat_history'])
      } | PromptFa
ctory.CONDENSE_QUESTION_PROMPT | ChatOpenAI(temperature=0, streaming=True) | StrOutputParser(),
    })
    _context = {

      'context': itemgetter('standalone_question') | vector_retriever | _combine_documents,
      'question': lambda x: 
x['standalone_question']
    }
    Runnable1 = _inputs | _context | PromptFactory.PROMPT | ChatOpenAI(temperature=0, str
eaming=True)
    
    # ----------------- Stream the response: -----------------
    
    for s in Runnable1.stream({'qu
estion': 'Hello!', 'chat_history': []}):
      print(s, end='', flush=True)

**The above stream works**

    # ---------
-------- Runnable 2 -----------------
    
    Runnable2 = RunnableMap({
      'response': {
        'question': lambda 
x: x['question'],
        'chat_history': lambda x: _format_chat_history(x['chat_history']),
        'context': lambda x
: QueriesContext.get_result()
      } | PromptTemplate.from_template(PromptFactory.followup_context_template) | ChatOpen
AI(temperature=0, streaming=True) | StrOutputParser(),
    })
    
    # ----------------- Stream the response: --------
---------
    
    for s in Runnable2.stream({'question': 'Hello!', 'chat_history': [], 'context': ['initialvalue']}):
 
     print(s, end='', flush=True)

**The above stream also works**

    def get_result(text):
      return ['newvalue']

    router_chain = PromptTemplate.from_template(PromptFactory.router_template_test) | ChatOpenAI(temperature=0, streamin
g=True) | StrOutputParser()
    
    def route(info):
      if 'runnable1' in info['topic'].lower():
        return Runn
able1
      elif 'runnable2' in info['topic'].lower():
        return Runnable2
      else:
        raise Exception('Inv
alid topic')
    
    full_runnable_router_chain = {
      'topic': router_chain,
      'question': lambda x: x['questio
n'],
      'chat_history': lambda x: x['chat_history'],
      'context': lambda x: x['context']
    } | RunnableLambda(r
oute)
    
    # ----------------- Stream the response: -----------------
    
    for s in full_runnable_router_chain.s
tream({'question': 'Hello!', 'chat_history': [], 'context': ['initialvalue']}):
      print(s.content, end='', flush=Tru
e)

**The above stream doesn't stream**
```
---

     
 
all -  [ Generating code using langchain ](https://www.reddit.com/r/LangChain/comments/17b32k3/generating_code_using_langchain/) , 2023-10-20-0909
```
Hey fellow buds!
Sorry if it's too a dumb question but I am currently working on a code generator tool using langchain.

I have a set of questions(questionnaire), sample input format, sample output format and I want to use langchain/llm mode
ls to generate code that converts input format to output format.

What is the best way to do this with or without using 
langchain?

Thanks!
```
---

     
 
all -  [ Ask questions over documents process ](https://www.reddit.com/r/LangChain/comments/17b2i8k/ask_questions_over_documents_process/) , 2023-10-20-0909
```
If I follow this ([https://python.langchain.com/docs/use\_cases/question\_answering](https://python.langchain.com/docs/u
se_cases/question_answering/)) to ask questions over documents, are my documents sent to langchain or openai at any poin
t?  Or do they stay local on my machine?
```
---

     
 
all -  [ Hiring announcements / job ads? ](https://www.reddit.com/r/LangChain/comments/17b1if6/hiring_announcements_job_ads/) , 2023-10-20-0909
```
Are hiring announcements / job ads for LangChain and related roles allowed on this subreddit? 

Mods, perhaps you could 
create a pinned thread for companies seeking talent?
```
---

     
 
all -  [ Llama 2 7B 32K Instruct summarizes and outlines text... inconsistently ](https://www.reddit.com/r/LocalLLaMA/comments/17b0n8t/llama_2_7b_32k_instruct_summarizes_and_outlines/) , 2023-10-20-0909
```
Hi everyone,

I'm brand new to using LLMs. I have so far got two different models to produce valid, appropriate, coheren
t, 'intelligent' responses with llama.cpp and Langchain, including the long context Llama 2 7B 32K Instruct. I don't und
erstand why things work or not, and was hoping for pointers to higher level guidance.

Currently I'm working on getting 
Llama 2 7B 32K Instruct to receive a short (approx. 1500 word), highly abstract text (an encyclopedia article I wrote on
 a topic in the humanities) and produce either a one paragraph summary, an outline, a Markdown document that could be co
nverted into slides by Pandoc, and a limerick about the information. The prompts I used for each worked at least once. S
ometimes the same prompt (with the same settings) will simply produce a copy of the original text or part of the origina
l prompt.

I'm wondering where in the process this inconsistency emerges. 

Related to this is that in order to use the 
Instruct model I not only had to use the prompt format (using `[INST]` and `[/INST]`) but also add these as stop words t
o the LlamaCpp object parameters, because otherwise the model would apparently instruct itself and keep going on both re
lated and unrelated responses. Even just the opening tag was not sufficient to stop this kind of output. It would also t
hrow in end tags into responses and then continue on. I don't know whether or how this is related, except they are both 
examples of my general ignorance of the underlying process this software follows.

Any general comments or advice would 
be welcome 😁
```
---

     
 
all -  [ Resume Roast/Review. ](https://i.redd.it/vm124swr50vb1.jpg) , 2023-10-20-0909
```
Hey everyone, please go through this thoroughly and review or roast it. 
Even though I am a full time developer, I am us
ing this resume to apply for better jobs in Fullstack, Frontend or Backend.
But I am getting no responses. Please tell m
e whatever may be wrong with this resume or my skills or experience.
Thank you ☺️
```
---

     
 
all -  [ [Local Llama] Quelqu'un a-t-il déjà un modèle pour Rag et Oobabooga API ](https://www.reddit.com/r/redditenfrancais/comments/17aqzqu/local_llama_quelquun_atil_déjà_un_modèle_pour_rag/) , 2023-10-20-0909
```
Par exemple. Utilisation de Langchain, Llamaindex ou leur propre Python

Traduit et reposté à partir de la publication h
ttps://www.reddit.com/16lq5b7
```
---

     
 
all -  [ LlamaCpp inference using AMD GPU ](https://www.reddit.com/r/LocalLLaMA/comments/17aou51/llamacpp_inference_using_amd_gpu/) , 2023-10-20-0909
```
Hi, I am working on a proof of concept that involves using quantized llama models (llamacpp) with [Langchain function](h
ttps://python.langchain.com/docs/integrations/llms/llamacpp)s. It has been working fine with both CPU or CUDA inference.
 However, I am wondering if it is now possible to utilize a AMD GPU for this process. This could potentially help me mak
e the most of my available hardware resources.  
Has anyone ever tried that?
```
---

     
 
all -  [ [Local Llama] Meilleur modèle à usage commercial? ](https://www.reddit.com/r/redditenfrancais/comments/17aoor8/local_llama_meilleur_modèle_à_usage_commercial/) , 2023-10-20-0909
```
Donc, j'ai passé un très bon moment jusqu'à présent avec vicuna 1.3 et exllama. A réussi à les faire fonctionner incroya
blement bien avec Langchain et Llama-Index. Je sais commencer à penser dans les applications logicielles potentielles et
 la licence restrictive de Llama est une nuisance.

Quel est le meilleur modèle pour une utilisation commerciale que vou
s avez trouvée? J'ai entendu de bonnes choses à propos de Falcon, mais je n'ai pas trouvé de versions quantifiées pour c
ela (si quelqu'un le sait, veuillez dire).

Traduit et reposté à partir de la publication https://www.reddit.com/14j5z7q

```
---

     
 
all -  [ [Langchain] Quelqu'un a été construit / bricolé d'un chatbot PDF? J'ai une question. ](https://www.reddit.com/r/redditenfrancais/comments/17aoke3/langchain_quelquun_a_été_construit_bricolé_dun/) , 2023-10-20-0909
```
Salut tout le monde,

Je construis une application où les utilisateurs peuvent télécharger des PDF et discuter avec eux.
 J'utilise Pinecone pour gérer les intérêts de ces PDF. Je me demande comment je devrais gérer les intérêts du PDF téléc
hargé de chaque utilisateur dans le backend de mon application, en considérant le concept d'index et espaces de noms de 
Pinecone.

Dois-je créer un index distinct pour chaque utilisateur ou un espace de noms distinct pour le PDF de chaque u
tilisateur? Quelle devrait être la relation entre eux et comment puis-je séparer entre plusieurs utilisateurs / PDF? Par
 exemple, si j'ai 1000 utilisateurs (chaque utilisateur peut télécharger plusieurs PDF), si je crée 1000 index (où chaqu
e index correspondait à un utilisateur, et un autre espace de noms peut être pour chacun de ses documents), ou un index 
ayant 1000 espaces de noms (un pour chaque utilisateur)?

Est-il possible d'y parvenir sans construire l'authentificatio
n en ce moment? J'apprécierais vraiment toutes les idées ou suggestions à ce sujet. Merci d'avance!

Traduit et reposté 
à partir de la publication https://www.reddit.com/12kqmwz
```
---

     
 
all -  [ Error while using ChatpromptTemplate (using LLama model ) ](https://www.reddit.com/r/LangChain/comments/17aloxd/error_while_using_chatprompttemplate_using_llama/) , 2023-10-20-0909
```
Hi, i'm using LLama2 model so getting error here   
Here is my code 

 

`from langchain.prompts.chat import (`  
 `Chat
PromptTemplate,`  
 `SystemMessagePromptTemplate,`  
 `HumanMessagePromptTemplate,`  
`)`  
 

`llm = LlamaCpp(`  
 `mod
el_path='models/llama-2-7b-chat.ggmlv3.q4_0.bin', callback_manager=callback_manager, verbose=True,n_ctx=4096, max_tokens
=1000, last_n_tokens_size=1000`  
`)`  


`template = 'You are an assistant that helps users find information about movi
es.'`  
`system_message_prompt = SystemMessagePromptTemplate.from_template(template)`  
`human_template = 'Find informat
ion about the movie {movie_title}.'`  
`human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)`
  
`chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])`  
`response = llm(cha
t_prompt.format_prompt(movie_title=str('Inception')).to_messages())`  
`print(response.content)`

&#x200B;

# This is th
e error

 **ValueError**    

 Traceback (most recent call last) **d:\\LLMs\\Langchain\\lang.ipynb Cell 42** line 1  11 
human\_message\_prompt = HumanMessagePromptTemplate.from\_template(human\_template)  13 chat\_prompt = ChatPromptTemplat
e.from\_messages(\[system\_message\_prompt, human\_message\_prompt\]) **---> 15** response = llm(chat\_prompt.format\_pr
ompt(movie\_title=str('Inception')).to\_messages())  17 print(response.content) 

 File **d:\\LLMs\\Langchain\\langch\_e
nv\\lib\\site-packages\\langchain\\llms\\base.py:332**, in BaseLLM.\_\_call\_\_**(self, prompt, stop, callbacks, \*\*kwa
rgs)**     

330 '''Check Cache and run the LLM on the given prompt and input.'''     331 if not isinstance(prompt, str)
: **--> 332** 

raise ValueError(     333 'Argument \`prompt\` is expected to be a string. Instead found '     334 f'{ty
pe(prompt)}. If you want to run the LLM on multiple prompts, use '     335 '\`generate\` instead.'     336     )     337
 return (     338 self.generate(\[prompt\], stop=stop, callbacks=callbacks, \*\*kwargs)     339 .generations\[0\]\[0\]  
   340 .text     341 )

  **ValueError**: Argument \`prompt\` is expected to be a string. Instead found <class 'list'>. 
If you want to run the LLM on multiple prompts, use \`generate\` instead. 

&#x200B;

  


&#x200B;
```
---

     
 
all -  [ LLM stands for … ](https://www.reddit.com/r/ArtificialInteligence/comments/17ak79q/llm_stands_for/) , 2023-10-20-0909
```
ChatGPT:
“””

Overview:

Imagine you have a big box of crayons and each crayon can draw a different type of picture. Now
, you want to draw a picture of a super cool robot like Jarvis from Iron Man. To do this, you’d pick crayons that can dr
aw parts of Jarvis and make them work together. In the big-kid world, these crayons are like different computer tools an
d programs. You want to use something called LangChain to make all these tools draw together. But to get the drawing to 
talk like Jarvis, you’ll need a special crayon that knows how to draw Jarvis’ voice.

Detailed Explanation:

Creating a 
comprehensive flow with LangChain to utilize Lifelong Learning Machines (LLMs) and other machine learning models is an a
mbitious task. To give your system a persona like Jarvis from Iron Man, you would need to focus on developing or obtaini
ng a Text-to-Speech (TTS) and Natural Language Generation (NLG) system that can mimic Jarvis’ tone, voice, and manner of
 speaking.

“””

Lifelong Learning Machines? 

Did I miss something ???

 🤣🧐🤷🏼‍♂️🤦🏼‍♂️
```
---

     
 
all -  [ SQLAgent exceeding max token for most join statements ](https://www.reddit.com/r/LangChain/comments/17aiaxw/sqlagent_exceeding_max_token_for_most_join/) , 2023-10-20-0909
```
I am trying to get the SQLAgent to be able to do queries on my database for more than just one table. For example, if I 
ask 'Give me a list of inventory for organization id: 13',  the langchain agent has to start joining tables, say an inve
ntory table to a store table to an organization table. It quickly exceeds the max tokens.  This is causing issue for the
 SQL Agent querying anything other than data only on 1 table.    


Also, If I have multiple organizations in my databas
e, I need to be able to strip out the data from the other orgs. 'If a user were to ask: 'Give me a list of my stores' I 
would need to have the agent also do 'Remove all store not connected to the users organization'.   


Is there any way t
o help the SQLAgent join tables better and strip out data based on a parentID?  
Would it need multiple DB instances wit
h just a single organizations data so that it doesnt need to strip out data?  
I dont really understand vector embedding
s, but would converting the db a vector store with instances make for faster querying?
```
---

     
 
all -  [ What to vector embed? ](https://www.reddit.com/r/LangChain/comments/17agsw2/what_to_vector_embed/) , 2023-10-20-0909
```
It seems a good amount of enterprise implementations are built using some form of RAG. What are some common use cases? S
ummarizing structured data, knowledge bot, providing insight/recommendations, etc? What are the most practical?
```
---

     
 
all -  [ Give a single model access to images and a text prompt? ](https://www.reddit.com/r/LangChain/comments/17adc8s/give_a_single_model_access_to_images_and_a_text/) , 2023-10-20-0909
```
I may be looking in the wrong place but how can I give a single model access to an image and a text prompt at the same t
ime?

For example, providing a picture of animals then asking the multi-modal llm what animals are in the picture.
```
---

     
 
all -  [ LangChain and Transformers ](https://www.reddit.com/r/ChatGPT/comments/17a8np8/langchain_and_transformers/) , 2023-10-20-0909
```
Hi frands, 

I am a software developer. I think I learned a lot by running examples of LangChain and transformers.js in 
a browser environment. (I run samples then checked network logs)

​​Do you have any interest in a new chat UI?

A web-ba
sed chat app that runs only client-side (100% privately).

I am thinking of creating a chat playground with LangChainAI.


LangChain has lots of features, and I believe I can implement many of them in my app.

I can easily add many tools to 
interact with Gmail, search, calendar, drive, etc., converting these tools into a marketplace like App Store. I can add 
plan and execute agents with them. I can also use AutoGPT and BabyAGI as an agent.

Chat integrations for Anthropic, Azu
re, OpenAI, Baidu, Bedrock, Ollama, etc.

Text embedding models to chat with your own docs and data. OpenAI, Ollama, Ten
sorFlow, Transformers.js.
```
---

     
 
all -  [ Reliable ways to get structured output from llms ](https://www.reddit.com/r/LocalLLaMA/comments/17a4zlf/reliable_ways_to_get_structured_output_from_llms/) , 2023-10-20-0909
```
What are the current best ways to get structured output from local llm/openai reliably ? I have found the following opti
ons and tried some of them,

Microsoft guidance - [https://github.com/guidance-ai/guidance](https://github.com/guidance-
ai/guidance)

LMQL - [https://lmql.ai/](https://lmql.ai/)

llama.cpp grammar - [https://github.com/ggerganov/llama.cpp/d
iscussions/2494](https://github.com/ggerganov/llama.cpp/discussions/2494)

langchain [https://python.langchain.com/docs/
modules/model\_io/output\_parsers/](https://python.langchain.com/docs/modules/model_io/output_parsers/)

jsonformer - [h
ttps://github.com/1rgs/jsonformer](https://github.com/1rgs/jsonformer)

salute - [https://github.com/LevanKvirkvelia/sal
ute](https://github.com/LevanKvirkvelia/salute)

outlines - [https://github.com/outlines-dev/outlines](https://github.co
m/outlines-dev/outlines)

Was looking for something that could work with both local llm’s (gguf/gptq models) and openai 
but i guess that’s difficult right now ? (also, i am more inclined towards typescript based solutions(zod) if possible)


I ran into a few problems for eg, guidance-ai doesn’t seem to work with text-generation ui because the openai api adapt
er doesn’t support logit\_bias.

It will be great to know the experience of others with these approaches.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, others as needed) ](https://www.reddit.com/r/forhire/comments/17a0q5k/for_hire_programmerweb_developerit_consultant/) , 2023-10-20-0909
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ LLama2 prompt template ](https://www.reddit.com/r/LangChain/comments/179zm9g/llama2_prompt_template/) , 2023-10-20-0909
```
Hi everyone,

I recently started to use langchain and ollama together to test Llama2 as a POC for a RAG system. 

Being 
in early stages my implementation of the whole system relied until now on basic templating (meaning only a system paragr
aph at the very start of the prompt with no delimiter symbols). And I do believe that changing this template to better s
uit the format intended by llama2 could at least bring more interesting outputs. For reference, I looked over this artic
le on HugginfFace that specifically goes over 'how to prompt llama2' ([https://huggingface.co/blog/llama2](https://huggi
ngface.co/blog/llama2)).

Leading to my question: have any of you tried to implement 'advance' prompt template such as t
he one used by llama2 and if so did you had to change significant portion of the existing prompt template (I'm worried a
bout the prefix required before the user input in the chat history)  and how did it turn out ?

&#x200B;
```
---

     
 
all -  [ Langchain + tabulur data on huggingface ](https://www.reddit.com/r/LangChain/comments/179xluu/langchain_tabulur_data_on_huggingface/) , 2023-10-20-0909
```
Is there any way to make langchain work with tabular data with huggingface models. There are lot of tutorials for how to
 make it work with OpenAiAPi, but not with other llms
```
---

     
 
all -  [ LangChain doc search is 👎 ](https://www.reddit.com/r/LangChain/comments/179xi52/langchain_doc_search_is/) , 2023-10-20-0909
```
I know we want to promote LLM support bots, but the search in the LangChain docs is super bad.

&#x200B;

**Mendable** '
can answer' questions with AI, but it miserably fails to index and search the docs, in contrast to good search products 
like Algolia.

&#x200B;

I am sure 99% of my queries would be resolved properly with Algolia but fail with Mendable
```
---

     
 
all -  [ How do i fine tune an LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/179w79k/how_do_i_fine_tune_an_llm/) , 2023-10-20-0909
```
I have a 24gb Card and i want to fine tune an llm on a dataset i created whats the best way?

And is it even possible

H
ere is my Dataset i want to use it for langchain:

[My Trainings Data](https://www.file-upload.net/download-15204875/tra
iningdata3.0.xlsx.html)

Source:

[https://huggingface.co/datasets/iamtarun/python\_code\_instructions\_18k\_alpaca](htt
ps://huggingface.co/datasets/iamtarun/python_code_instructions_18k_alpaca)(A Few Code Questions)

[https://huggingface.c
o/datasets/MadVoyager/stable\_diffusion\_instructional\_dataset](https://huggingface.co/datasets/MadVoyager/stable_diffu
sion_instructional_dataset)(Everything That has to do something with prompts and Picture generation)
```
---

     
 
all -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-20-0909
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

     
 
all -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-20-0909
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

     
 
all -  [ How your business can use OpenAI GPT ](https://www.reddit.com/r/LingoBlocks/comments/179vr7l/how_your_business_can_use_openai_gpt/) , 2023-10-20-0909
```
There’s many business use cases for a custom chat interface like ChatGPT, but using the company’s own internal content a
s the source. Think company policies, documents, project resources, etc.

I’ve been wrapping my head around, and buildin
g, GPT projects for the past 2 years (software dev of 7 years). Always learning, but what I’m sharing is basically the s
tandard approach to create a custom ChatGPT-like application that you can add your own data to.

If you know how to prog
ram, you could explore Open Source libraries like LangChain to handle processing of custom data. It’s a free program tha
t makes the process of interacting with different LLMs easier. Next you’ll want to connect it to a vector database to ma
ke the processed data available for referencing, and finally OpenAI’s API for the LLM generations (or your LLM of choice
).

Regardless of the solution you choose, how all this works from a technical perspective is:

1. You need to break up 
any large text content into smaller pieces. This process is called chunking. You do this to later make each chunk search
able in the vector database.
2. ⁠You’ll want to vectorize each chunk and add this vector into a database. By doing this,
 you can embed (vectorize) natural language to search the vector database for relevant chunks.
3. With the returned chun
ks, you can combine them all (within respects to the context window limit of the LLM of choice), and now your generated 
response will contain the information it needs to give you an accurate output.

Making a secure and privacy-focused solu
tion for businesses is also important. If you use the OpenAI API, data is not used to train their models (source [OpenAI
 Enterprise Privacy](https://openai.com/enterprise-privacy)).

I hope this makes sense. Let me know if there’s any quest
ions on the topic.
```
---

     
 
all -  [ How to fix 'libmagic is unavailable' error in Python ](https://www.reddit.com/r/LangChain/comments/179v9m5/how_to_fix_libmagic_is_unavailable_error_in_python/) , 2023-10-20-0909
```
 

I am getting the following error message when I try to run my Python code:

libmagic is unavailable but assists in fi
letype detection on file-like objects. Please consider installing libmagic for better results.

I have tried installing 
libmagic, but I am still getting the error message. I am using windows and Python 3.8. I installed it the same way as I 
have installed all my packages before and never run into any such errors.

Does anyone know how to solve this issue?
```
---

     
 
all -  [ Is GPT-4 getting faster? ](https://www.reddit.com/r/LangChain/comments/179pgnn/is_gpt4_getting_faster/) , 2023-10-20-0909
```
&#x200B;

https://preview.redd.it/clhg4ee5roub1.png?width=5000&format=png&auto=webp&s=5b7ddb30068e8e8e2fa9b6dc521e4c6351
3f3fed

Seeing that GPT-4 latencies for both regular requests and computationally intensive requests have more than halv
ed in the last 3 months.

Wrote up some notes on that here: [https://blog.portkey.ai/blog/gpt-4-is-getting-faster/](http
s://blog.portkey.ai/blog/gpt-4-is-getting-faster/)

Curious if others are seeing the same?
```
---

     
 
all -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-20-0909
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

     
 
all -  [ Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/GPT3/comments/179j4pw/exploring_methods_to_improve_text_chunking_in_rag/) , 2023-10-20-0909
```

Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunk
ing function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algor
ithms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out 
there, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising a
pproaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large 
Language Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embeddin
g) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've a
lso tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the
 query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a n
ot extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis 
and reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrap
ing to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to 
modify the text used to generate embeddings, while returning the original text after the recall phase. But this is still
 a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd app
reciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel ch
unking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking fo
r RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-20-0909
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

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-20-0909
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-20-0909
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-20-0909
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-20-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-20-0909
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

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-20-0909
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

     
