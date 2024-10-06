 
all -  [ Can anyone help me to get first full time job please  ](https://i.redd.it/cndhtqa9czsd1.jpeg) , 2024-10-06-0914
```

```
---

     
 
all -  [ Question About Agent Toolkits and Contributing to Agent tools ](https://www.reddit.com/r/LangChain/comments/1fwuyty/question_about_agent_toolkits_and_contributing_to/) , 2024-10-06-0914
```
For context, I'm basically a beginner at the LangChain codebase and want to find ways to contribute towards open source.
 Currently, I'm looking into contributing a Spotify tool for agents to use, but had a question about the file structure.


Under `libs/community/langchain_community/tools` exists all the tools that I'm assuming an agent can use, but not all 
of these tools have toolkits under `libs/community/langchain_community/agent_toolkits`.

So What are these toolkits exac
tly, and why would some of the implemented tools need them compared to others?
```
---

     
 
all -  [ How I deployed a NestJS task in as a Lambda to react to S3 events ](https://www.reddit.com/r/nestjs/comments/1fwu316/how_i_deployed_a_nestjs_task_in_as_a_lambda_to/) , 2024-10-06-0914
```
I'm working on a RAG application using nestjs, exposing an API to a vuejs application. One huge part of a RAG is about i
ngesting the data.  
  
The idea was to use a Lambda function that reacts to S3 bucket events and ingests the data. As I
 already had an API and lots of abstractions/wrappers over Langchain (js). I needed to maximize code reuse without havin
g to deploy the whole nestjs application in a lambda. Also, I didn't wanted to have a worker/queue on nestjs side for ha
ndling ingests.

After some research, I was able to turn my nest api into a nestjs monorepo, having two applications: th
e API, and a standalone application that basically only creates an nestjs application context and exposes a function han
dler. In the bootstrap, we store the application context in the global scope, which is persisted for a few minutes, even
 after the lambda finishes the execution.

The main issue here is that the way nestjs builds/bundles, it exposes a IIFE 
(Immediately Invoked Function Expression), so the handler function was not accessible outsite the module, Lambda could n
ot use it.

The solution I found was to build nestjs with webpack, specifically for \`libraryTarget: 'commonjs2'\`. Also
, in the webpack configuration I was able to reduce a lot of the bundle size with tree-shaking.

In the end of the day, 
I have a .cjs file exposing the handler function, and over 2MB of dependencies bundleded in separated .js files (compare
d with 400MB node\_modules in the whole application), so I can read/make small changes in the handler function directly 
in the AWS Lambda console for small changes/tests.

This lambda is reacting to events in s3. A book with 4MB and 600+ pa
ges (mainly text, few images) is taking about 20 seconds to ingest, and using about 256mb on lambda, which costs 0.08$ p
er 1k executions, only after 80K executions in the free tier - Of course that there are other costs involved, such as da
ta ingress/egress.  


I'm pretty happy with the results, after creating the wrapper for the lambda I could reuse basica
lly all of the code that I already had for ingesting files from the API.   
Not sure if I have overcomplicated this. Do 
you guys have any recommendations about this approach?  

```
---

     
 
all -  [ Simulation and CI/CD for agents ](https://www.reddit.com/r/LangChain/comments/1fws0mw/simulation_and_cicd_for_agents/) , 2024-10-06-0914
```
Is anyone building CI/CD and for agents? Agents break all the time due to changes in models, nodes, functions etc. Testi
ng manually for different cases is hard if you have a wide range of inputs the agent is supposed to handle. 
```
---

     
 
all -  [ [Open source] r/RAG's official resource to help navigate the flood of RAG frameworks
 ](https://www.reddit.com/r/LangChain/comments/1fwqp07/open_source_rrags_official_resource_to_help/) , 2024-10-06-0914
```
Hey everyone!

If you’ve been active in r/RAG, you’ve probably noticed the massive wave of new RAG tools and frameworks 
that seem to be popping up every day. Keeping track of all these options can get overwhelming, fast.

That’s why I creat
ed [RAGHub](https://github.com/Andrew-Jang/RAGHub), our official community-driven resource to help us navigate this ever
-growing landscape of RAG frameworks and projects.

# What is RAGHub?

RAGHub is an open-source project where we can col
lectively list, track, and share the latest and greatest frameworks, projects, and resources in the RAG space. It’s mean
t to be a living document, growing and evolving as the community contributes and as new tools come onto the scene.

# Wh
y Should You Care?

* Stay Updated: With so many new tools coming out, this is a way for us to keep track of what's rele
vant and what's just hype.
* Discover Projects: Explore other community members' work and share your own.
* Discuss: Eac
h framework in RAGHub includes a link to Reddit discussions, so you can dive into conversations with others in the commu
nity.

# How to Contribute

You can get involved by heading over to the [RAGHub GitHub repo](https://github.com/Andrew-J
ang/RAGHub). If you’ve found a new framework, built something cool, or have a helpful article to share, you can:

* Add 
new frameworks to the [Frameworks table](https://github.com/Andrew-Jang/RAGHub).
* Share your projects or anything else 
RAG-related.
* Add useful resources that will benefit others.

You can find instructions on how to contribute in the [CO
NTRIBUTING.md](https://github.com/Andrew-Jang/RAGHub/blob/main/CONTRIBUTING.md) file.
```
---

     
 
all -  [ October 5, 2024 - 960 Top Free Udemy Course Deals (Live updates) ](https://www.reddit.com/r/udemyfreebies/comments/1fwn7sd/october_5_2024_960_top_free_udemy_course_deals/) , 2024-10-06-0914
```
1. QuickBooks Online: Streamline US Tax Deductions

https://www.easylearn.ing/course/quickbooks-online-tax-deductions




2. Regressions & Correlation

https://www.easylearn.ing/course/regression-correlation-course



3. Solar Cell Technolog
y

https://www.easylearn.ing/course/solar-cell-technology-course



4. HR with Odoo 17 AI-Powered Policies and Procedure
s Manual

https://www.easylearn.ing/course/odoo-17-hr-course



5. Supply Chain Operations Specialization, PLM,Odoo 17 P
lanning

https://www.easylearn.ing/course/supply-chain-operations-specialization



6. CRM , E-commerce Website Exam ,Od
oo 17 Certification

https://www.easylearn.ing/course/odoo-17-certification-course



7. Manufacturing ‎Certification Ex
am , Odoo 17 Certification

https://www.easylearn.ing/course/odoo-17-manufacturing-certification



8. Accounting Certif
ication Exam , Odoo 17 Certification

https://www.easylearn.ing/course/odoo-17-accounting-certification-course



9. Acc
ounting and auditing with artificial intelligence-Odoo 17

https://www.easylearn.ing/course/accounting-auditing-artifici
al-intelligence



10. Total Quality Management: Certification

https://www.easylearn.ing/course/total-quality-managemen
t-certification



11. Taller Literario (2da parte): Cómo Escribir Profesionalmente

https://www.easylearn.ing/course/ta
ller-literario-escritura-creativa



12. Curso De Python 3 Desde Cero Para Novatos

https://www.easylearn.ing/course/cur
so-python-3-cero-novatos



13. Theory of Constraints: Certification

https://www.easylearn.ing/course/theory-of-constra
ints-certification-course



14. Python Certification - The Next Level Python

https://www.easylearn.ing/course/python-c
ertification-hindi



15. Python Project for Basics Data Analysis

https://www.easylearn.ing/course/data-analysis-with-p
ython-project



16. Angular

https://www.easylearn.ing/course/angular-course-hindi



17. Become SAP Ariba Certified Co
nsultant Spend Analysis

https://www.easylearn.ing/course/sap-ariba-spend-analysis-course



18. Photoshop Express - Mas
tering Adobe Photoshop In 2 Hours

https://www.easylearn.ing/course/photoshop-express-course



19. Veeam Certified Arch
itect (VMCA) v12.1 Practice Exam - 2024

https://www.easylearn.ing/course/veeam-certified-architect-vmca-v12-1-practice-
exam



20. ChatBot de IA para Wordpress: Para Principiantes y Avanzados

https://www.easylearn.ing/course/chatbots-ia-w
ordpress



21. DP-900 Microsoft Azure Data Fundamentals Certification Exams

https://www.easylearn.ing/course/dp-900-ce
rtification



22. Éducation Financière

https://www.easylearn.ing/course/education-financiere-independance



23. Trans
form Your Arduino into Automatic Coin Operated Machine

https://www.easylearn.ing/course/arduino-weight-machine



24. P
IC Microcontroller: Garage Door System Ultrasonic Sensor

https://www.easylearn.ing/course/garage-door-system-pic-microc
ontroller



25. AI-900 Azure AI Fundamentals

https://www.easylearn.ing/course/ai-900-practice-questions



26. Azure D
eveloper Associate AZ-204

https://www.easylearn.ing/course/azure-developer-associate-az-204-practice-tests



27. Micro
soft Azure Data Fundamentals DP900 Practice

https://www.easylearn.ing/course/azure-data-fundamentals-dp900-practice-tes
ts



28. Canva Magic Studio AI Tools for Quick, Easy Content Creation

https://www.easylearn.ing/course/canva-ai-design




29. Fire Up Creativity in Your Child

https://www.easylearn.ing/course/child-creativity-course



30. Ultimate Adobe
 Photoshop for Beginners - Zero to Hero

https://www.easylearn.ing/course/photoshop-tutorial-for-beginners



31. Oracle
 Cloud Infrastructure Architect Professional - Exams

https://www.easylearn.ing/course/oracle-cloud-infrastructure-archi
tect-professional-exam-prep



32. 350+ Exercises - Python Programming Mega Pack - OOP

https://www.easylearn.ing/course
/python-oop-exercises



33. Calculus: Applications of Derivatives

https://www.easylearn.ing/course/calculus-applicatio
ns-derivatives



34. Full Stack Data Science Developer Course from scratch

https://www.easylearn.ing/course/full-stack
-data-science-developer-course



35. AWS Certified DevOps Engineer Professional Practice Exams

https://www.easylearn.i
ng/course/aws-devops-engineer-professional-practice-exams



36. Coding for everybody: Full stack development course

ht
tps://www.easylearn.ing/course/coding-for-everyone-course



37. Microsoft Certified: Azure Security Engineer Associate 
Exams

https://www.easylearn.ing/course/azure-security-engineer-associate-certification



38. Data Scientist Certificat
ion: Test Your Skills with Tests

https://www.easylearn.ing/course/data-scientist-certification-practice-tests



39. Sa
lesforce Certified Platform Developer II - Mock Exams

https://www.easylearn.ing/course/salesforce-platform-developer-ii
-mock-exams



40. Data Science Bootcamp in Python: 250+ Exercises to Master

https://www.easylearn.ing/course/python-da
ta-science-bootcamp



41. Super way to Learn Arduino | Creative

https://www.easylearn.ing/course/learn-arduino-program
ming



42. Software Manual Testing full Course in Hindi / Urdu

https://www.easylearn.ing/course/software-manual-testin
g-hindi-urdu-course



43. Learn Python + JavaScript + Microsoft SQL for Data science

https://www.easylearn.ing/course/
python-javascript-sql-data-science-course



44. Lean Problem Solving: Creative Solutions for Teams & Leaders

https://w
ww.easylearn.ing/course/creative-problem-solving



45. Reverse Engineering 4: Software Protection

https://www.easylear
n.ing/course/reverse-engineering-software-protection



46. MS-900: Microsoft 365 Certified: Fundamentals - Mock Exams


https://www.easylearn.ing/course/ms-900-practice-exams



47. Basics of the Arabic Language

https://www.easylearn.ing/c
ourse/arabic-language-course-beginners



48. Fullstack web development : CSS JavaScript and PHP Mastery

https://www.ea
sylearn.ing/course/css-javascript-php-mysql



49. DP-900: Azure Data Fundamentals DP900 Practice Test Oct 2024

https:/
/www.easylearn.ing/course/dp-900-practice-tests



50. Complete Network Hacking Course 2024 - Beginner to Advanced

http
s://www.easylearn.ing/course/wifi-hacking-course



51. Technical Analysis Mastery: Successful Trading Strategies

https
://www.easylearn.ing/course/technical-analysis-trading



52. Perspective Management: Foundations of Leadership Excellen
ce

https://www.easylearn.ing/course/perspective-management-leadership-excellence



53. Investment Management & Technic
al Analysis: A Trading Guide

https://www.easylearn.ing/course/investment-management-technical-analysis-indian-stock-mar
ket



54. Time Management for Stress Management

https://www.easylearn.ing/course/time-management-stress-reduction



5
5. Brain computer interface with deep learning

https://www.easylearn.ing/course/brain-computer-interface-deep-learning




56. 500+ SAS Interview Questions Practice Test

https://www.easylearn.ing/course/sas-interview-questions-practice-tes
t



57. Ultimate PRTG Network Monitoring with Full Lab GNS3

https://www.easylearn.ing/course/prtg-network-monitoring-c
ourse



58. PHP with MySQL: Build 7 PHP and MySQL Projects

https://www.easylearn.ing/course/build-php-mysql-projects




59. Security Awareness Training - CyberSecurity for Everyone!

https://www.easylearn.ing/course/cybersecurity-for-ever
yone



60. RPA Project: Identify the process to automate

https://www.easylearn.ing/course/identify-right-process-autom
ate



61. NodeJS Masterclass (Express, MongoDB, OpenAI) - 2024 Ready!

https://www.easylearn.ing/course/nodejs-mastercl
ass



62. Flutter Masterclass (Dart, APIs, Firebase & More) - 2024

https://www.easylearn.ing/course/flutter-course-202
4



63. RPA Project: Process Definition Document (PDD)

https://www.easylearn.ing/course/rpa-project-management-pdd




64. Trading from A to Z: forex, crypto, stock proven strategy !

https://www.easylearn.ing/course/forex-trading-course




65. Complete Italian Course : Conversation Lessons for Beginners

https://www.easylearn.ing/course/learn-italian-conve
rsation-beginner



66. تعلم التحليل الأساسي في التداول في سوق العملات

https://www.easylearn.ing/course/تحليل-اساسي-فور
كس



67. CLF-C02 AWS Certified Cloud Practitioner Exam Tests Oct 2024

https://www.easylearn.ing/course/aws-certified-c
loud-practitioner-exam-preparation



68. Unlocking the Power of Relative Clauses in English language

https://www.easyl
earn.ing/course/english-grammar-relative-clauses



69. AI-900 Azure AI Fundamentals Practice Tests | Azure AI 2024

htt
ps://www.easylearn.ing/course/ai-900-azure-ai-fundamentals-practice-tests



70. AZ-900 Practice Tests for Microsoft Azu
re Fundamentals 2024

https://www.easylearn.ing/course/azure-fundamentals-exam-prep



71. AZ-400 Practice Tests: Micros
oft Azure DevOps Solutions Exam

https://www.easylearn.ing/course/microsoft-azure-devops-solutions-exam



72. Azure AI-
050: Generative AI Solutions with Azure OpenAI

https://www.easylearn.ing/course/azure-ai-fundamentals-generative-ai




73. AI-102 Microsoft Azure AI Engineer Associate Exam

https://www.easylearn.ing/course/ai-102-exam-preparation



74. M
s Certified: Azure AI Fundamentals AI-900 Practice Exam

https://www.easylearn.ing/course/azure-ai-fundamentals-ai-900-e
xam-prep



75. AZ-900 - Microsoft Azure Fundamentals - شرح بالعربي

https://www.easylearn.ing/course/az-900-azure-funda
mentals-arabic



76. CISCO CCNA 200-301 Practice Exams (6) + Explanations

https://www.easylearn.ing/course/cisco-ccna-
200-301-practice-exams



77. CompTIA Security+ 701 Practice Exam (2024)

https://www.easylearn.ing/course/sy0-701-pract
ice-test



78. Web-Based Embedded System Simulator

https://www.easylearn.ing/course/web-based-embedded-simulator



79
. CompTia Network+ N10-009 Practice Exam (2024)

https://www.easylearn.ing/course/comptia-network-plus-n10-009-practice-
exam



80. Arduino Home Security System

https://www.easylearn.ing/course/arduino-home-security-system



81. Debugging
 Javascript / NodeJS

https://www.easylearn.ing/course/javascript-debugging-course



82. Projektmanagement: Produktivit
ät und Mindset für Erfolg

https://www.easylearn.ing/course/projektmanagement-kurs



83. Power Electronics for Electric
 Vehicles

https://www.easylearn.ing/course/electric-vehicle-power-electronics



84. Python desde Principiante hasta Ni
vel Ingeniería

https://www.easylearn.ing/course/curso-python-principiante-profesional



85. Crear un ecommerce FULLSTA
CK PHP y MySQL - Tienda Online

https://www.easylearn.ing/course/ecommerce-development-php-mysql



86. The Ultimate For
ex Algorithmic Trading Course | Build 5 Bots

https://www.easylearn.ing/course/forex-algorithmic-trading-course



87. \
[DEA-C01 | ARA-C01\] Snowflake Advanced Certification Prep

https://www.easylearn.ing/course/snowflake-advanced-certific
ation-prep



88. The Expert’s Secret to Mobile Application Testing \[2024\]

https://www.easylearn.ing/course/mobile-te
sting-training



89. CISSP Certification exam - Security Professional 2024 Part 1

https://www.easylearn.ing/course/cis
sp-certification-exam-prep



90. Python Programming Language (Practice Projects)

https://www.easylearn.ing/course/prac
tical-python-projects



91. Problem Solving with C programming language

https://www.easylearn.ing/course/c-programming
-problem-solving



92. Learn Kindergarten - 1 English with Appu & Tiger

https://www.easylearn.ing/course/learn-english
-preschoolers



93. Learn Kindergarten - 2 English with Appu & Tiger

https://www.easylearn.ing/course/kindergarten-eng
lish-course



94. Learn Grade - 7 Math with Appu & Tiger

https://www.easylearn.ing/course/grade-7-math-course



95. L
earn Grade - 4 Math with Appu & Tiger

https://www.easylearn.ing/course/grade-4-math-appu-tiger



96. Learn Grade - 6 M
ath with Appu & Tiger

https://www.easylearn.ing/course/grade-6-math-fun



97. Learn Grade - 1 Math with Appu & Tiger


https://www.easylearn.ing/course/first-grade-math-appu-tiger



98. Learn Grade - 2 Math with Appu & Tiger

https://www.
easylearn.ing/course/learn-grade-2-math



99. Learn Kindergarten Math with Appu & Tiger

https://www.easylearn.ing/cour
se/kindergarten-math-appu-tiger



100. DP-600 Certification Microsoft Fabric - Tests Pratiques 2024

https://www.easyle
arn.ing/course/microsoft-fabric-dp-600-certification



101. Advance Professional Course in Steel Commercial (Part-II)


https://www.easylearn.ing/course/steel-commercial-building-design-part-2



102. Unlock the Secrets of Polynomials: Comm
and On Algebra

https://www.easylearn.ing/course/master-algebra-polynomials



103. ChatGPT for Construction Managers

h
ttps://www.easylearn.ing/course/chatgpt-construction-management



104. Antivirus Evasion - Hard Core

https://www.easyl
earn.ing/course/antivirus-evasion-masterclass



105. JavaScript Fundamentals for Absolute Beginners

https://www.easyle
arn.ing/course/javascript-basics-course



106. 600+ Design Patterns Interview Questions Practice Test

https://www.easy
learn.ing/course/design-patterns-interview-questions



107. AWS Certified Solution Architect Associate  SAA-C03 \[HINDI
\]

https://www.easylearn.ing/course/aws-certified-solutions-architect-associate-saa-c03-exam-prep-hindi



108. تعلم نط
ق اللغة الإنجليزية - صوتيات اللغة

https://www.easylearn.ing/course/تعلم-نطق-اللغة-الإنجليزية



109. AWS Certified SysO
ps Administrator Associate SOA-C02 \[2024\]

https://www.easylearn.ing/course/aws-sysops-administrator-associate-soa-c02
-certification



110. Beginner's Exam Practice Guide for SHRM-SCP Certification

https://www.easylearn.ing/course/shrm-
scp-exam-practice-guide



111. RPA Project: Gathering requirements

https://www.easylearn.ing/course/rpa-requirements-g
athering



112. 1400+ Deep Learning Interview Questions and Practice Tests

https://www.easylearn.ing/course/deep-learn
ing-interview-questions



113. \[New\] 750+ Excel Interview Questions and Practice Tests

https://www.easylearn.ing/cou
rse/excel-interview-practice



114. \[NEW\] 1100+ Git Interview Questions and Practice Tests

https://www.easylearn.ing
/course/git-interview-questions



115. DevOps Bootcamp: CI/CD, Automation, and Cloud Mastery\[Hindi\]

https://www.easy
learn.ing/course/devops-bootcamp-hindi



116. AWS Certified SysOps Administrator Associate SOA-C02 \[HINDI\]

https://w
ww.easylearn.ing/course/aws-sysops-administrator-associate-soa-c02-exam-prep-hindi



117. Ultimate AWS Certified Soluti
ons Architect Associate SAA-C03

https://www.easylearn.ing/course/aws-certified-solutions-architect-associate-saa-c03




118. Introduction to Linux Shell Scripting in Hindi

https://www.easylearn.ing/course/linux-shell-scripting-hindi



11
9. Securing Your Ubuntu Environment: Best Practices

https://www.easylearn.ing/course/ubuntu-security-guide



120. Crea
te Space Invaders with Python PyGame

https://www.easylearn.ing/course/space-invaders-python



121. OOP Design Patterns
 in Python

https://www.easylearn.ing/course/oop-design-patterns-python



122. Ethical Hacking: Crypto 101

https://www
.easylearn.ing/course/ethical-hacking-cryptography



123. Machine Learning Intro for Python Developers

https://www.eas
ylearn.ing/course/machine-learning-python-beginner



124. RPA Project: Mapping the process(es)

https://www.easylearn.i
ng/course/rpa-process-mapping



125. \[New\] 1300+ Computer Vision Interview Practice Questions

https://www.easylearn.
ing/course/computer-vision-interview-questions



126. 960+ Cryptography Interview Questions and Practice Tests

https:/
/www.easylearn.ing/course/cryptography-interview-questions



127. Learn Advanced RAG : Vector to Graph RAG wth LangChai
n Neo4j

https://www.easylearn.ing/course/rag-course



128. 5 Real-Time Use Cases using Machine Learning

https://www.e
asylearn.ing/course/real-world-machine-learning



129. AWS Certified Data Engineer Associate DEA-C01 Practice Exam

htt
ps://www.easylearn.ing/course/aws-data-engineer-associate-practice-exam



130. \[NEW\] Salesforce Certified AI Associat
e | Practice Exams

https://www.easylearn.ing/course/salesforce-certified-ai-associate-practice-exams



131. Aprende Ha
cking Ético: Protege y Penetra Redes

https://www.easylearn.ing/course/cybersecurity-expert



132. JavaScript 10 Projec
ts in 10 Days Course for Beginners

https://www.easylearn.ing/course/javascript-web-development-10-projects



133. Buil
d Convai Artificial Intelligence AR App With Unity3D.

https://www.easylearn.ing/course/unity3d-ar-course



134. Compre
hensive Financial Statement : A Practical Assessment

https://www.easylearn.ing/course/financial-statement-assessment-co
urse



135. Veeam Certified Engineer (VMCE v12) - Exam Practice Tests 24

https://www.easylearn.ing/course/veeam-vmce-v
12-certification



136. Prompt Engineering and RAG for Software Engineers

https://www.easylearn.ing/course/prompt-engi
neering-for-software-engineers



137. Visualizing Sensors Data

https://www.easylearn.ing/course/sensor-data-visualizat
ion-esp32



138. Ultimate Generative Persuasion: Sell and Present w/ ChatGPT

https://www.easylearn.ing/course/chatgpt-
persuasion-course



139. Sistema Punto de Venta con PHP, MVC, POO y MySQL

https://www.easylearn.ing/course/curso-php-s
istema-ventas



140. Line Follower Robot: Master Robotics with Precision and Code

https://www.easylearn.ing/course/lin
e-follower-robot-arduino



141. Google Professional Cloud DevOps Engineer - GCP - Exams

https://www.easylearn.ing/cour
se/google-cloud-devops-certification



142. Solid Principles for Clean Code Programming & Architecture

https://www.eas
ylearn.ing/course/solid-principles-clean-code-architecture



143. React Hook Form: The Complete Guide with React (2024)


https://www.easylearn.ing/course/react-hook-form-guide



144. ESRI ArcGIS Online : Formation Pratique (4 en 1 )

http
s://www.easylearn.ing/course/formation-arcgis-online



145. SVM for Beginners: Support Vector Machines in R Studio

htt
ps://www.easylearn.ing/course/svm-beginner-guide



146. Introduction to C#, easy and clear explanation.

https://www.ea
sylearn.ing/course/master-c-sharp



147. Python Design Patterns: Complete Guide \[2024 Edition\]

https://www.easylearn
.ing/course/python-design-patterns-mastery



148. Climate Change Explained: Causes, Consequences and Solutions

https:/
/www.easylearn.ing/course/climate-change-explained



149. Advanced Excel - مهارات اكسل متقدمة

https://www.easylearn.in
g/course/excel-chatgpt-integration



150. 9 TO 5 wealth Creation :Blueprint to create wealth

https://www.easylearn.ing
/course/9-to-5-wealth-creation



151. Entire Export Digital And Social Media Marketing In 1 Course

https://www.easylea
rn.ing/course/export-digital-marketing-course



152. PHP with MySQL: Build Complete Forum with Admin Panel

https://www
.easylearn.ing/course/php-mysql-forum-admin-panel



153. Lean Manufacturing Academy: Certified Master Lean Course.

htt
ps://www.easylearn.ing/course/lean-manufacturing-certification



154. QuickBooks Desktop vs QBO Multiple Currencies

ht
tps://www.easylearn.ing/course/quickbooks-desktop-qbo-multiple-currencies



155. Python, Java and PHP Essentials: Compl
ete Coding Bootcamp

https://www.easylearn.ing/course/python-java-php-bootcamp



156. Mastering C & C++ Programming: Fr
om Fundamentals to Advanced

https://www.easylearn.ing/course/c-programming-fundamentals



157. DevOps Bootcamp: CI/CD,
 Automation, and Cloud Mastery

https://www.easylearn.ing/course/devops-bootcamp



158. DevOps : CI/CD with Jenkins in 
Hindi

https://www.easylearn.ing/course/devops-jenkins-course-hindi



159. GitLab CI: Pipelines, CI/CD and DevOps for B
eginners

https://www.easylearn.ing/course/gitlab-ci-cd-devops



160. Ansible for the Absolute Beginner - DevOps in Hin
di

https://www.easylearn.ing/course/ansible-devops-beginner-hindi



161. Learn DevOps: Infrastructure Automation With 
Terraform\[2024\]

https://www.easylearn.ing/course/learn-terraform-aws-infrastructure-automation



162. AWS Certified 
Solution Architect-Associate Practice Tests

https://www.easylearn.ing/course/aws-certified-solutions-architect-associat
e-practice-tests



163. Introduction to SafeTest - A Netflix-backed Automation Tool

https://www.easylearn.ing/course/s
afetest-course



164. Get Started with Salesforce - For Absolute beginners

https://www.easylearn.ing/course/salesforce
-beginner-course



165. Developing a digital business growth strategy

https://www.easylearn.ing/course/digital-busines
s-growth-strategy



166. AWS Certified Data Engineer - Associate (DEA-C01) Exam Guide

https://www.easylearn.ing/course
/aws-certified-data-engineer-associate-practice-exams



167. Mastering the AWS Certified AI Practitioner Exam

https://
www.easylearn.ing/course/aif-c01-practice-questions



168. Construye tu Propio Sistema POS con PHP 8 y MySQL

https://w
ww.easylearn.ing/course/curso-php-mysql-pos



169. ChatGPT for Academic Research

https://www.easylearn.ing/course/chat
gpt-academic-research



170. Ms Azure Administrator Associate - AZ-104 Practice Exam

https://www.easylearn.ing/course/
az-104-practice-exams



171. \[NEW\] 1500 Master SQL: Interview Questions - Practice Tests

https://www.easylearn.ing/c
ourse/master-sql-interview-questions



172. 1500 New CompTIA IT Fundamentals ITF+ FC0-U61 Practice Exams

https://www.e
asylearn.ing/course/comptia-it-fundamentals-practice-exams



173. Certified Kubernetes Security Specialist Masterclass


https://www.easylearn.ing/course/kubernetes-security-specialist-training



174. AWS Certified Cloud Practitioner

http
s://www.easylearn.ing/course/aws-cloud-fundamentals



175. Python Web Development: Building Interactive Websites

https
://www.easylearn.ing/course/python-web-development-course



176. FOCP Exam: Dominate with Practice & Expertise (2024 Ed
ition)

https://www.easylearn.ing/course/focp-exam-practice-tests



177. Salesforce Marketing Cloud Consultant Practice
 Test 2024

https://www.easylearn.ing/course/salesforce-marketing-cloud-certification-practice-exams



178. Comprehensi
ve ISTQB Foundation Level Exam Certification Prep

https://www.easylearn.ing/course/istqb-foundation-level-exam-prep




179. Ultimate ISTQB AI Testing Exam Certification 2024

https://www.easylearn.ing/course/istqb-ai-testing-certification-
exam



180. PSK I : Professional Scrum with Kanban Test - Exam 2024

https://www.easylearn.ing/course/psk-i-exam-prep




181. PSPO 1 Exam+1200QS & Explanations

https://www.easylearn.ing/course/pspo-1-exam-prep



182. Certified Scrum Mast
er Certification - CSM - Practice Tests

https://www.easylearn.ing/course/csm-exam-prep-course



183. ASQ Certification
 Exam Prep: 6 Practice Tests

https://www.easylearn.ing/course/asq-certification-exam-prep



184. Scaled Professional S
crum ( SPS ) Exam - Test 2024

https://www.easylearn.ing/course/scaled-professional-scrum-sps-exam-preparation



185. P
SPO 2 -Product Owner Level 2 Practice Exam - Test 2024

https://www.easylearn.ing/course/pspo-2-practice-exams



186. M
aster FOCP Exam Prep: 6 Updated Practice Tests

https://www.easylearn.ing/course/focp-exam-prep-course



187. ITIL 4 DP
I Exam Success Guide: 6 Practice Tests\\Questions

https://www.easylearn.ing/course/itil-4-dpi-certification-exam-prep




188. Ultimate AMLS Exam Prep: 6 Practice Tests

https://www.easylearn.ing/course/amls-exam-prep



189. CSM Exam+600QS
 & Explanations

https://www.easylearn.ing/course/csm-exam-practice-tests



190. ITIL 4 HVIT Exam Mastery: 6 Practice T
ests & Explanations

https://www.easylearn.ing/course/itil-4-hvit-certification-exam



191. Professional Agile Leadersh
ip Exam +1200 Questions

https://www.easylearn.ing/course/professional-agile-leadership-exam



192. 6 Updated Practice 
Tests: IASSC Exam Prep \[2024\]

https://www.easylearn.ing/course/iassc-exam-prep-2024



193. P3O Certification Exam Pr
ep: 6 Practice Tests \[2024\]

https://www.easylearn.ing/course/p3o-practice-tests



194. Odoo 17 Certification Exam Pr
eparation

https://www.easylearn.ing/course/odoo-17-certification-exam-preparation



195. MSP Certification Exam Prep: 
6 Practice Tests

https://www.easylearn.ing/course/msp-exam-practice-tests



196. Master the SPS Exam 2024: Comprehensi
ve Certification Prep

https://www.easylearn.ing/course/sps-exam-prep-course



197. Scrum Developer Certification - PSD
 -  Practice Test - Exams

https://www.easylearn.ing/course/psd-exam-practice-tests



198. ITIL 4 CDS Exam Prep: 6 Full
 Practice Tests with & Questions

https://www.easylearn.ing/course/itil-4-cds-exam-prep



199. Diseño 3D para Videojueg
os con Blender

https://www.easylearn.ing/course/curso-blender-modelado-3d-videojuegos



200. Power BI: Gráficos y visu
alización de datos

https://www.easylearn.ing/course/curso-power-bi-visualizacion-datos



201. Curso de Tableau: Anális
is y Visualización de Datos

https://www.easylearn.ing/course/curso-tableau-analista-datos



202. Frameworks, Índices, 
Transacciones y mucho más con MongoDB

https://www.easylearn.ing/course/curso-mongodb



203. Microsoft Excel: Fundament
os

https://www.easylearn.ing/course/curso-excel-fundamentos



204. Curso Python: Programación Numérica con NumPy

http
s://www.easylearn.ing/course/curso-numpy-python



205. Curso Python: Manejo de Datos con Pandas

https://www.easylearn.
ing/course/curso-python-pandas-analisis-datos



206. Decision Trees, Random Forests, Bagging & XGBoost: R Studio

https
://www.easylearn.ing/course/decision-trees-r-studio



207. The Complete Android & Kotlin App Development A-Z Bootcamp


https://www.easylearn.ing/course/android-app-development-kotlin-bootcamp



208. Como Vender en AMAZON FBA Completo Paso
 a Paso, Español 2025

https://www.easylearn.ing/course/curso-amazon-fba-espanol



209. Personal Finance #11-Stock Inve
stment -Equity Investments

https://www.easylearn.ing/course/stock-investment-guide



210. Organic Digital Marketing: T
he Updated 2024 Masterclass

https://www.easylearn.ing/course/youtube-marketing-mastery



211. React & Next.js: From Be
ginner to Pro in No Time

https://www.easylearn.ing/course/react-nextjs-course



212. Blueprint For Successful  Microse
rvices & API Implementation

https://www.easylearn.ing/course/microservices-api-deployment-declarative-configuration




213. Harnessing AI and Machine Learning for Geospatial Analysis

https://www.easylearn.ing/course/geospatial-analysis-ai




214. Master JavaScript, HTML, and CSS with 30 Projects in 30 Days

https://www.easylearn.ing/course/30-projects-in-3
0-days



215. Complete Payroll Management in Excel &TALLY ERP9 &TallyPrime

https://www.easylearn.ing/course/payroll-ma
nagement-excel-tally



216. Elementor Hosting 2024: Crea una Tienda Online con WordPress

https://www.easylearn.ing/cou
rse/elementor-hosting-wordpress-tienda-online



217. Comprehensive C# Programming Practice Test: Code Mastery

https://
www.easylearn.ing/course/c-sharp-programming-practice-test



218. Proyecto Java NetBeans: Control de Versiones con Git,
 GitHub

https://www.easylearn.ing/course/curso-git-github-netbeans-java



219. Salesforce Marketing Cloud Email/Admin/
Consultant Training

https://www.easylearn.ing/course/salesforce-marketing-cloud-certification-training



220. Seven Qu
ality Control Tools to improve everyday performance.

https://www.easylearn.ing/course/quality-control-tools



221. Apr
ende WPF y MAUI desde CERO usando C#

https://www.easylearn.ing/course/curso-wpf-maui-c-sharp



222. 17 in 1: Complete 
Personal Transformation Masterclass

https://www.easylearn.ing/course/personal-transformation-masterclass



223. Python
 for Scientific Research

https://www.easylearn.ing/course/python-for-scientific-research



224. Master Content Creatio
n : Become a paid Content Creator

https://www.easylearn.ing/course/content-creation-mastery



225. AWS Certified Machi
ne Learning Engineer - Associate | Exams

https://www.easylearn.ing/course/aws-certified-machine-learning-engineer-assoc
iate-exam-prep



226. Master CDPSE: Certified Data Privacy Solutions Engineer

https://www.easylearn.ing/course/cdpse-c
ertification-course



227. Network Mastery for Ethical Hackers

https://www.easylearn.ing/course/ethical-hacking-networ
k-security



228. Burp Suite Mastery: From Beginner to Advanced

https://www.easylearn.ing/course/burp-suite-mastery




229. PMI-PBA Exam Ready: Practice Tests for Business Analysts

https://www.easylearn.ing/course/pmi-pba-exam-prep



23
0. Supercharging your business with AI tools

https://www.easylearn.ing/course/ai-for-business-growth



231. Comment ne
 plus échouer ? Le système de la réussite

https://www.easylearn.ing/course/reussir-guide-ultime-potentiel



232. CSO C
hief Security Officer Executive Certification

https://www.easylearn.ing/course/cso-certification-assessment



233. Wor
d Wizard : Using Microsoft Word Like a Pro in 2024

https://www.easylearn.ing/course/word-for-beginners-advanced



234.
 Interface Windows User Commands From The Beginner To Admin

https://www.easylearn.ing/course/windows-command-line-maste
ry



235. Practice Tests | AWS Certified Solutions Architect Associate

https://www.easylearn.ing/course/aws-solutions-
architect-associate-practice-tests



236. CDO Chief Digital Officer Executive Certification

https://www.easylearn.ing/
course/chief-digital-officer-certification



237. PIC Microcontroller Insect Detector

https://www.easylearn.ing/course
/pic-microcontroller-insect-detector



238. Unveil the Magic of Gaming — Powered by Arduino!

https://www.easylearn.ing
/course/arduino-game-development



239. TESOL Certification: Become a Professional English Teacher

https://www.easylea
rn.ing/course/tesol-certification-online-course



240. Master Filmora: Editing, Motion Graphics, and Color Grading

htt
ps://www.easylearn.ing/course/master-filmora-editing



241. Generative AI Beginner to Advance

https://www.easylearn.in
g/course/generative-ai-beginner-advanced



242. Modélisation financière : cours complet de finance sur Excel

https://w
ww.easylearn.ing/course/modelage-financier-excel



243. Machine Learning use in React Native - The Practical Guide

htt
ps://www.easylearn.ing/course/react-native-machine-learning-course



244. Complete Age & Gender Detection Using DNN & O
PENCV Project

https://www.easylearn.ing/course/age-gender-detection-dnn-opencv



245. Python Beginners to Advance Boot
camp

https://www.easylearn.ing/course/python-beginner-to-advanced



246. Build Your English A2 to B1 through Story-Bas
ed Learning

https://www.easylearn.ing/course/english-a2-b1-course



247. Comienza a programar: Python desde 0

https:/
/www.easylearn.ing/course/curso-python-principiantes



248. No Oil Cooking Recipes - Eat Healthy! Live Strong!

https:/
/www.easylearn.ing/course/healthy-cooking-without-oil



249. ChatGPT ve Yapay Zeka: kapsamlı yapay zeka eğitimi

https:
//www.easylearn.ing/course/chatgpt-e-giris



250. Create A Project Tracker Using Spreadsheet Software

https://www.easy
learn.ing/course/project-management-spreadsheets



251. Modelowanie finansowe: Kompletny kurs finansów w Excelu

https:
//www.easylearn.ing/course/modelowanie-finansowe-excel



252. Finanzmodellierung: Vollständiger Finanzkurs in Excel

ht
tps://www.easylearn.ing/course/finanzmodellierung-excel-kurs



253. Financial Modeling: Complete Finance Course on Exce
l

https://www.easylearn.ing/course/financial-modeling-course-excel



254. 財務モデリング：Excelで学ぶ完全なファイナンスコース

https://www.ea
sylearn.ing/course/excel-financial-modeling-training



255. Finansal modelleme: Excel'de eksiksiz finans kursu

https:/
/www.easylearn.ing/course/excel-finansal-modelleme-kursu



256. Excel النمذجة المالية: دورة تدريبية كاملة في برنامج

ht
tps://www.easylearn.ing/course/دورة-نمذجة-excel-المالية



257. 财务建模：Excel 中的完整财务课程 - 金融

https://www.easylearn.ing/cour
se/excel-financial-modeling-course



258. Modelagem Financeira, Finanças e Gestão financeira no Excel

https://www.easy
learn.ing/course/modelagem-financeira-excel



259. Modelización financiera: curso completo de finanzas en Excel

https:
//www.easylearn.ing/course/curso-modelacion-financiera-excel



260. Public Relations: Crisis Communications Oil and Gas
 Industry

https://www.easylearn.ing/course/oil-gas-crisis-communications



261. Python for Data Science Pro: The Compl
ete Mastery Course

https://www.easylearn.ing/course/master-python-data-science



262. Hands on Cisco Labs: Secure your
 Cisco Network

https://www.easylearn.ing/course/cisco-network-security-labs



263. PHP CodeIgniter 4: Build Complete J
ob Portal

https://www.easylearn.ing/course/php-codeigniter-4-job-portal-course



264. An Introduction To Cyber Securit
y Fundamentals

https://www.easylearn.ing/course/cybersecurity-fundamentals



265. Email Etiquette: Essential Skill for
 Corporate Communication

https://www.easylearn.ing/course/email-etiquette-corporate-communication



266. The Ultimate 
Google Tag Manager Course: Beginner to Advanced

https://www.easylearn.ing/course/learn-google-tag-manager



267. Tech 
Lead & Staff Engineer Survival Primer in 75 mins

https://www.easylearn.ing/course/tech-lead-mastery



268. How to Add 
Value in the Project Management Role

https://www.easylearn.ing/course/elevate-your-pm-role



269. Productivity and Tim
e Management

https://www.easylearn.ing/course/productivity-time-management-course



270. AWS Certified SysOps Administ
rator - Associate SOA-C02 Exams

https://www.easylearn.ing/course/aws-certified-sysops-administrator-associate-soa-c02-e
xam-preparation



271. Financial Modeling on Excel Complete finance course on Excel

https://www.easylearn.ing/course/f
inancial-modeling-excel-course



272. ChatGPT & IA : Formation complète ChatGPT, Dall-e

https://www.easylearn.ing/cour
se/chatgpt-formation-complete



273. \[New\]  VMware Certified Professional - VCP-DTM Practice Exam

https://www.easyle
arn.ing/course/vcp-dtm-practice-exams



274. Matlab course for wireless communication engineering

https://www.easylear
n.ing/course/matlab-course-ofdm-noma



275. New Microsoft AZ-900: Microsoft Azure Fundamentals Practice

https://www.ea
sylearn.ing/course/azure-fundamentals-practice-tests



276. \[New\] - AZ-104 Microsoft Azure Administrator-Practice Tes
t

https://www.easylearn.ing/course/microsoft-azure-administrator-practice-exams



277. New Business Analyst Certificat
ion (PMI-PBA)

https://www.easylearn.ing/course/pmi-pba-certification-prep



278. Sales Crash Course - B2B Sales Skills
 & Business Development

https://www.easylearn.ing/course/b2b-sales-training



279. SC-400 Certification Challenge: Ess
ential Practice Tests

https://www.easylearn.ing/course/sc-400-certification-practice-tests



280. IBM watsonx Generati
ve AI Engineer Associate - Exams

https://www.easylearn.ing/course/ibm-watsonx-generative-ai-engineer-associate-exam-pre
p



281. Mastering GitLab Building Continuous Integration Pipelines

https://www.easylearn.ing/course/gitlab-ci-cd-cour
se



282. Mastering Advanced Java with Object-Oriented Programming

https://www.easylearn.ing/course/advanced-java-mast
ery



283. Data Analytics Masters - From Basics To Advanced

https://www.easylearn.ing/course/data-analytics-masterclas
s



284. Beginner Guide to Learn T-Shirt Design With Photoshop

https://www.easylearn.ing/course/learn-photoshop-t-shir
t-design



285. Basic Electronics - Test your knowledge. (Multiple Choice)

https://www.easylearn.ing/course/electronic
s-fundamentals-quiz



286. AWS Certified DevOps Engineer - Professional DOP-C02

https://www.easylearn.ing/course/aws-d
evops-engineer-professional-dop-c02-practice-exam



287. Windows 10 Services Administration and Troubleshooting

https:
//www.easylearn.ing/course/windows-10-services-administration



288. CCNA (Cisco Certified Network Associate) Practice 
Exams 2024

https://www.easylearn.ing/course/ccna-practice-exams



Deals number 289 to 960 can be found on:

https://ww
w.easylearn.ing/


```
---

     
 
all -  [ Should I use an agentic framework to build multi-agent infrastructure. ](https://www.reddit.com/r/LocalLLaMA/comments/1fw8dwx/should_i_use_an_agentic_framework_to_build/) , 2024-10-06-0914
```
I want to build a llm-application, but IDK if I should use something like langchain (or an alternative) vs writing my ow
n AI agents, and tools. What would be better in your opinions? And how should I go about it??


```
---

     
 
all -  [ Why is it not standard for OpenAI and other libraries to offer API reference docs in an AI-friendly  ](https://www.reddit.com/r/OpenAI/comments/1fw7vta/why_is_it_not_standard_for_openai_and_other/) , 2024-10-06-0914
```
**Edit:** I misspoke, and it's really the *library reference* (for me, `openai-python`) that I want this for.

Seriously
, how hard would it be to go at least some of the way down this list?

----

**Zero:** <-- Somehow, this is where we are
 now.

1. Provide the full library reference in a single markdown document.
2. Semantically split into chunks.
3. Togeth
er with embeddings.
4. Along with a really simple LangChain snippet that lets you chat with it.
5. Hosted on their websi
te. (You could bring your own API key, the project wouldn't have to pay.)
```
---

     
 
all -  [ How to access modules in other parts of the repo when dynamically loading? ](https://www.reddit.com/r/learnpython/comments/1fw6kvr/how_to_access_modules_in_other_parts_of_the_repo/) , 2024-10-06-0914
```
Hi all, got a bit of a conundrum here trying to get dynamic module loading with importlib to work properly 

I have the 
following package structure:

    my_project/
    ├── __init__.py
    ├── llm_provider/
    │   ├── __init__.py
    │   
└── base_client.py (class BaseLLMProvider)
    ├── agents/
    │   ├── __init__.py
    │   ├── base_agent.py
    │   └──
 basic_math_agent/
    │       ├── __init__.py
    │       └── agent.py
    └── supervisor/
        ├── __init__.py
    
    └── agent_manager.py

`agent_manager` attempts to dynamically load `basic_math_agent` using `importlib`, which works
 fine. However, `basic_math_agent` has a standard import statement of `from llm_provider.base_client import BaseLLMProvi
der`. This import fails, because as far as I am able to discern when using `importlib` to dynamically load a module, it 
does not share the same project root as the rest of the project, so `basic_math_agent` is unable to see `llm_provider`.


I receive this error:

    2024-10-04 10:33:50,288 [INFO] Starting Supervisor...
    2024-10-04 10:33:50,288 [INFO] Sea
rching for agents in directory: /home/user/personal/my_project/supervisor/../agents
    2024-10-04 10:33:50,288 [INFO] T
rying to import agent from directory: basic_math_agent
    2024-10-04 10:33:50,746 [ERROR] Error importing agent from 'b
asic_math_agent': cannot import name 'BaseLLMProvider' from 'llm_provider.base_client' (/home/user/personal/my_project/l
lm_provider/base_client.py)

In `my_project/__init__.py`, I try to update the sys root path to include the project root 
as I've seen suggested elsewhere, but it doesn't seem to work.

    import os
    import sys

    project_root = os.path
.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)

Any suggestions on what best practice is here or 
how I can go about solving this?

For additional reference, here are the relevant snippets of code:

`llm_provider/base_
client.py`

    from pydantic import ValidationError, BaseModel
    class BaseLLMClient(BaseModel):

`agents/base_agent.
py`

    from abc import abstractmethod
    from typing import Any, Dict, Optional
    from langchain.agents import Agen
tType
    from llm_provider.base_client import BaseLLMClient
    from langchain.tools import BaseTool
    from superviso
r.llm_registry import LLMRegistry, LLMType
    from shared_tools.message_bus import MessageBus

    class BaseAgent:
   
     def __init__(self, llm_registry: LLMRegistry, message_bus: MessageBus, config: Optional[Dict] = None):
            
self.llm_registry = llm_registry
            self.config = config or {}
            self.state = None
            self.v
ersion = None
            self.message_bus = None

`agents/basic_math_agent/agent.py`

    from typing import Any, Dict,
 Optional
    from agents.base_agent import BaseAgent
    from langchain.tools import BaseTool
    from llm_provider.bas
e_client import BaseLLMClient
    from supervisor.llm_registry import LLMRegistry, LLMType
    from .tools.basic_math_to
ol import BasicMathTool, BasicMathInput, BasicMathOutput

    class BasicMathAgent(BaseAgent):
        def __init__(self
, llm_registry: LLMRegistry, message_bus: MessageBus, config: Optional[Dict] = None):
            super().__init__(llm_r
egistry, message_bus, config)
            self.tool = BasicMathTool(llm_registry.get_llm(LLMType.DEFAULT))

`supervisor/
agent_manager.py`

    def register_agents(self):
        try:
            agents_dir = Path(os.path.join(os.path.dirnam
e(__file__), '..', 'agents'))
            logger.info(f'Searching for agents in directory: {agents_dir}')

            #
 Add the project root to the Python path
            project_root = os.path.join(agents_dir.parent.resolve())
          
  sys.path.append(project_root)

            # Add the subdirectories to the Python path
            subdirs = [os.path.
join(project_root, d) for d in os.listdir(project_root) if os.path.isdir(os.path.join(project_root, d))]
            for
 subdir in subdirs:
                sys.path.append(subdir)

            for agent_dir in agents_dir.iterdir():
        
        if agent_dir.is_dir() and not agent_dir.name.startswith('_'):
                    logger.info(f'Trying to import
 agent from directory: {agent_dir.name}')
                    try:
                        agent_module = importlib.impo
rt_module(f'agents.{agent_dir.name}.agent')
                        agent_classes = [cls for cls in agent_module.__dict_
_.values() if isinstance(cls, type) and issubclass(cls, BaseAgent) and cls != BaseAgent]
                        if not 
agent_classes:
                            logger.warning(f'Skipping agent directory '{agent_dir.name}' as it does not c
ontain a valid agent class.')
                            continue

                        logger.info(f'Found {len(age
nt_classes)} agent classes in {agent_dir.name}')
                        for agent_class in agent_classes:
             
               try:
                                logger.info(f'Trying to register agent: {agent_class.__name__}')
   
                             agent_config_file = agent_dir / 'config.yaml'
                                if agent_conf
ig_file.exists():
                                    logger.info(f'Loading config from {agent_config_file}')
          
                          with open(agent_config_file, 'r') as f:
                                        agent_config =
 yaml.safe_load(f)
                                else:
                                    logger.info(f'No config fil
e found for {agent_class.__name__}, using default config.')
                                    agent_config = {}

     
                           agent = agent_class(self.config.llm_client_factory, self.message_bus, **agent_config.get('con
fig', {}))
                                self.register_agent(agent)
                                logger.info(f'Succ
essfully registered agent: {agent_class.__name__}')
                            except Exception as e:
                 
               logger.error(f'Error registering agent '{agent_class.__name__}' from '{agent_dir.name}': {e}')
          
          except Exception as e:
                        logger.error(f'Error importing agent from '{agent_dir.name}': {
e}')
                else:
                    logger.debug(f'Skipping directory {agent_dir.name} as it is not a directo
ry or starts with an underscore.')
        except Exception as e:
            logger.error(f'Error registering agents: {
e}')
```
---

     
 
all -  [ Advanced LLM parsing is the key to advanced AI applications. ](https://www.reddit.com/r/datascience/comments/1fw5k23/advanced_llm_parsing_is_the_key_to_advanced_ai/) , 2024-10-06-0914
```
In my experience, when people consider applying LLMs to a project they often fall into two camps:

1. they turn the proj
ect into a chat bot
2. they use an LLM for some key feature in a larger application, resulting in an error prone mess

t
here's tremendous power in using LLMs to power specific features within larger applications, but LLMs inconsistency in o
utput structure makes it difficult to use their output within a programmatic system. You might ask an llm to output JSON
 data, for instance, and the LLM decides it's appropriate to wrap the data in a `\`\`\`json \`\`\`` markdown format. you
 might ask an LLM to output a list of values, and it responds with something like this:

    here's your list
    [1,2,3
,4]

There's an infinite number of ways LLM output can go wrong, which is why output parsing is a thing.

I've had the b
est luck, personally, with LangChain in this regard. [LangChain's pydantic parser](https://python.langchain.com/docs/how
_to/output_parser_structured/) allows one to define an object which is either constructed from the LLMs output, or an er
ror gets thrown. They essentially use a clever prompting system paired with the user's defined structure to coax the mod
el into a consistent output.

That's not fool proof either, which is why it's a common practice to either re-try or re-p
rompt. You can either just re-prompt on a failure, or pass the response which failed to parse to the LLM again and ask t
he LLM to correct it's mistake. For robust LLMs this works consistently enough where it's actually viable in application
s (assuming proper error handling). I made a post about [LangGraph](https://www.reddit.com/r/datascience/comments/1fknby
i/langgraph_allows_you_to_make_falsifiable_testable/) recently, this can also be used to construct complex loops/decisio
ns which can be useful for adding a level of robustness into LLM responses.

If you can learn how to consistently turn a
n LLMs output into JSON, there's a whole world of possible applications.

I'm curious what LLM parsing tricks you employ
, and what you've seen the most success with!
```
---

     
 
all -  [ a way to chunk large txt file or HTML ](https://www.reddit.com/r/LangChain/comments/1fw2125/a_way_to_chunk_large_txt_file_or_html/) , 2024-10-06-0914
```
Hi

I have a large text file (approximately 1 million words) and an HTML version of it. Each page ends with a unique key
word indicating a page break. I need a way to automatically split the text into chunks based on these keywords and then 
send each chunk to Claude for translation into English.

any ideas folks?
```
---

     
 
all -  [ Postgresql Checkpointer on LangGraphJS ](https://www.reddit.com/r/LangChain/comments/1fw0ifo/postgresql_checkpointer_on_langgraphjs/) , 2024-10-06-0914
```
I am doing some research and initial setup for implementing an agentic system on a large production application and am t
rying to find information on whether the Postgresql checkpointing system is currently implemented for LangGraphJS. 

I c
ame across this discussion, https://github.com/langchain-ai/langgraph/discussions/1796 - so I wanted to ask for some cla
rification and to see if anyone can maybe point me in the right direction as far as documentation goes, etc.. 

Thanks!
```
---

     
 
all -  [ Need resource for RAG agent in LangGraph ](https://www.reddit.com/r/LangChain/comments/1fvzoh6/need_resource_for_rag_agent_in_langgraph/) , 2024-10-06-0914
```
I am looking to build rag agent in Langgraph, so if anyone has resources or learning material apart from official docume
ntion then please share it. 
```
---

     
 
all -  [ I created a discord server to discuss agentic systems engineering ](https://www.reddit.com/r/LangChain/comments/1fvz82r/i_created_a_discord_server_to_discuss_agentic/) , 2024-10-06-0914
```
Hey guys, I created a discord channels for developers building AI agents (using any framework or none). Join if you're i
nterested in learning and sharing with the community: [https://discord.gg/nRgm5DbH](https://discord.gg/nRgm5DbH)
```
---

     
 
all -  [ Using ChatOpenAI with LangGraph.js to Build a Personal Assistant AI Agent ](https://www.reddit.com/r/LangChain/comments/1fvyhb9/using_chatopenai_with_langgraphjs_to_build_a/) , 2024-10-06-0914
```
Made a beginner guide on how to use LangGraph and ChatGpt to create an AI Agent that acts as a personal assistant 👉 [htt
ps://www.js-craft.io/blog/chatopenai-langgraph-js-ai-agent/](https://www.js-craft.io/blog/chatopenai-langgraph-js-ai-age
nt/)

Please let me know your thoughts :) 
```
---

     
 
all -  [ Speaker Diarization for audio with multiple languages ](https://www.reddit.com/r/LangChain/comments/1fvvr5r/speaker_diarization_for_audio_with_multiple/) , 2024-10-06-0914
```
I have a call record with two people speaking in combination of languages like english, telugu and hindi. How to diarize
 it. I tried pyannote models available in the huggingface. It's not working well and I'm not getting any accurate result
s. What are the available options and how to proceed further
```
---

     
 
all -  [ advice from people working in tech from early 2000 ](https://www.reddit.com/r/codingbootcamp/comments/1fvvfhk/advice_from_people_working_in_tech_from_early_2000/) , 2024-10-06-0914
```
guys as someone with 15+ yoe, I want to ask others who have experience, what advice would you give to the young new grad
s and those who are looking into the SWE and data careers?   
  
From my point of view:  I want to say that it's not wor
th pursuing careers in software or data analytics anymore, the AI crushing it, I can replace 5-6 people in current busin
ess that I work in, using Cursor Composer and Aider connected to sonnet3.5, and soon the o1 models will get upgraded to 
real gpt5 which will nail the multi-file editing better than sonnet and opus which are already amazing, these 2 years ar
e the last years of '6 figures' wages in tech, this is why: the number of businesses, existing and upcoming, is limited,
 and it will not grow all of a sudden to a x5 demand (x5 number of businesses need to appear), while the reduction in re
quired head count of software and data peeps goes down x5 if not x10 (if we consider upcoming gpt5 and new anthropic rel
eases in the next 2 years and link it into agents like [crew.ai](http://crew.ai/) and self written langchain (business s
pecific agents) the headcount required to deliver the business goals goes down x10 easily, WHILE universities are still 
full of upcoming SWEs and AI/ML data scientists, who are students now, and they'll be in the market too (in addition to 
all self-taught folks from east europe, latam, asia, and their uni of course, who are looking for remote work) it's goin
g to be a bloodbath, I can already hire engineers for 2-3k euro in Poland, Serbia, Asia, India, Mexico, who were until r
ecently non-existent (before covid we had not much practice of such massive outsourcing as we do now, at the moment ever
y business looking to cut costs and opens offices in Belgrade and Bucharest etc'). 

The big tech swims in money so they
'll keep paying 6 figures for a while, to the most experienced leads and seniors, staff, directors, but it'll go down to
 'back to reality' rates which are below 6 figures in the next 5-6 years as well, and the competition for the roles is a
lready fierce. If you want to work routinely 10-12 hours a day, PLUS keep yourself up to date on latest tech and in good
 shape of algorithms (add 2-3 hours a week to keep yourself in shape) this career is for you, BUT high rates are no long
er guaranteed for folks who want a quiet 9-5 office job. the more hardcore nerds like me, who have no life, no kids, no 
hobbies, will keep the high paying jobs, but this shit is not for regular healthy people, so my sincere advice for young
 folks would be to stay away from SWE and try hardware networking, chip manufacturing, biology, space sciences, aerospac
e (probably best niche in upcoming future), defense (obviously, but take care of karma so you don't end up in hell lol, 
not worth the 6 figures), microbiology, medicine, ocean stuff, oil and gas and geo sciences maybe, agriculture science i
n upcoming climate change might be good direction too since there's a lot of trouble in the sector that needs fixing, an
d so on. just my sincere 2 cents :)))

I hope this will help someone to make a good decision in life, you're welcome to 
disagree and I know I might be completely wrong and 'new businesses and new use cases for SWEs will get created in the u
pcoming golden age of AI' theory of the youtubers exists ('influencers' :D the ones who can't make $$ in tech and become
 youtubers to make ends meet, they aren't the best ones to listen to honestly, I'm sorry guys. but just think about it, 
we're dying in tech jobs with 10-12 hour shifts already, who of us in a sane mind will be a youtube influencer in our fr
ee time, for 5$ per 10000 views or smth? when our rates are 100-120$/hour at work, why would we do youtube?? don't liste
n to these dummies, they're on youtube cos the job is too hard for them anyway).

Take care! 
```
---

     
 
all -  [ Hybrid retrieval on Postgres - (sub)second latency on ~30M documents ](https://www.reddit.com/r/LangChain/comments/1fvunhv/hybrid_retrieval_on_postgres_subsecond_latency_on/) , 2024-10-06-0914
```
We had been looking for open source ways to scale out our hybrid retrieval in Langchain beyond the capability of the def
ault Milvus/FAISS vector store with the default in-memory BM25 indexing but we couldn't find any proper alternative.

Th
at's why we have implemented this ourselves and are now releasing it for others to use:

* Dense vector embedding search
 on Postgres through pgvector
* Sparse BM25 search on Postgres through ParadeDB's pg\_search
   * A custom retriever for
 the BM25 search
* 1 Dockerfile that spins up a Postgres facilitating both

We have benchmarked this on a dataset loadin
g just shy of 30M chunks into Postgres with a hybrid search using BM25 and vector search and have achieved (sub)second r
etrieval times.

Check it out: [https://github.com/AI-Commandos/RAGMeUp/blob/main/README.md#using-postgres-adviced-for-p
roduction](https://github.com/AI-Commandos/RAGMeUp/blob/main/README.md#using-postgres-adviced-for-production)
```
---

     
 
all -  [ RAG Tabular Type Data ](https://www.reddit.com/r/Rag/comments/1fvtfr2/rag_tabular_type_data/) , 2024-10-06-0914
```
I want to create a Chroma Vector Store using Langchain from pdf documents, but what's happening is that my pdf contain s
ome tabular data, now when I am querying AI model for table data, It is not able to identify it. 

So is there any techn
ique or library for reading tabular data perfectly in order to create vector store
```
---

     
 
all -  [ Real estate llm ](https://www.reddit.com/r/LangChain/comments/1fvt4d3/real_estate_llm/) , 2024-10-06-0914
```
Has anybody has any idea how to build a real estate llm which scans through various real estate listings in real time an
d notify the user about the listing if it is profitable investment. I have not much experience in langchain can anyone t
ell me is it possible 
```
---

     
 
all -  [ What are some hobby projects that you've built with langchain? ](https://www.reddit.com/r/LangChain/comments/1fvqjpu/what_are_some_hobby_projects_that_youve_built/) , 2024-10-06-0914
```
I'm looking to build some hobby projects with LangChain for teaching people.

Wondering if anyone has any beginner-inter
mediate project ideas using LangChain that would be fun to build for beginners.
```
---

     
 
all -  [ AI Agent Marketplaces ](https://www.reddit.com/r/LangChain/comments/1fvj04p/ai_agent_marketplaces/) , 2024-10-06-0914
```
We're seeing a rising trend in companies trying to build AI agent marketplaces. I think it'll only be a few more months 
until someone figures out how to do it at scale. What do you guys think will be the most important features on these mar
ketplaces that will make them beneficial for creators?
```
---

     
 
all -  [ How to create a manual LLM chain for Conservational RAG? ](https://www.reddit.com/r/LangChain/comments/1fvf9vw/how_to_create_a_manual_llm_chain_for/) , 2024-10-06-0914
```
It might be a noob question, I want to create a llm chain something like

llm | chat\_history | prompt | documents

I'm 
separately retrieving the documents from vectorstore, and filtering the retrieved documents based on my own logic for my
 usecase, and only the filtered documents I want to pass to my llm for generating response and keeping chat\_history (I'
m aware of create\_stuff\_document and history\_aware\_retriever approach for conservational RAG, but in that approach I
 can't use my manual document filtering)

EDIT- I FIGURED IT ABOUT

    chat_history = []
    
    documents = [] # or a
ny other document coming from different function
    
    prompt = ChatPromptTemplate.from_messages([
        ('system',
 '''You are a Helpful Assistant
            You will consider the provided context as well. <context> {context} </contex
t>'''),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{input}')
        ])
    
    rag_
chain = (
        {
            'input': lambda x: x['input'],
            'context': lambda x: documents,
            '
chat_history': lambda x: x['chat_history'],
        }
        | prompt
        | llm
        | StrOutputParser()
    )
 
   
    chain = RunnablePassthrough.assign(context=lambda x: documents, chat_history=lambda x: x['chat_history']).assign
(
        answer=rag_chain
    )
    
    while True:
        user_input = input()
        if user_input in {'q', 'Q'}:

            break
        response = chain.invoke({'input': user_input, 'chat_history': chat_history})
        print(res
ponse)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=respo
nse['answer']))  
    
    
```
---

     
 
all -  [ text-embedding-004 from Gemini is not available on LangChain ](https://www.reddit.com/r/LangChain/comments/1fvf4hk/textembedding004_from_gemini_is_not_available_on/) , 2024-10-06-0914
```
I am trying to use Gemini's [text-embedding-004](https://ai.google.dev/gemini-api/docs/embeddings) model in LangChain ho
wever LangChain only supports text-embedding-001 according to this [doc](https://python.langchain.com/docs/integrations/
text_embedding/google_generative_ai/). I tried to change 001 to 004 but it returns error saying that the model is not su
pported. I am just curious why LangChain only supports 001, which is not mentioned anywhere in the current doc of Google
.
```
---

     
 
all -  [ Langfuse vs Helicone for prompt managing and experimentation. ](https://www.reddit.com/r/LangChain/comments/1fv8bcj/langfuse_vs_helicone_for_prompt_managing_and/) , 2024-10-06-0914
```
Those two services seem to be the most advanced and actively developed solutions for this. I am not sure which way to go
, especially since Langfuse's architecture will soon be very similar than that of Helicone's, see [https://github.com/or
gs/langfuse/discussions/1902](https://github.com/orgs/langfuse/discussions/1902) . The pricing of the non-self hosted ve
rsions are quite comparable, however it seems that Helicone does offer model output caching, which means it pays basical
ly by itself for our use case. On the other hand Langfuse seems to have a more comprehensive documentation and more self
 hosted centric development, not entirely sure.

What are your experiences using one of those services? Can you recommen
d one or another similar tool?
```
---

     
 
all -  [ Help me prioritize my tech stack. ](https://www.reddit.com/r/developersPak/comments/1fv7oo5/help_me_prioritize_my_tech_stack/) , 2024-10-06-0914
```
I want to learn

-Advance React
-Redux


-Node.Js
-Express.Js
-MongoDb
-MySQL

-nextJS

-Gsap
-Three.js
-Famermotion

-G
raphQl

-Socket.io
-WebRtc
-WebGL

-TypeScript

-Jenkins
-Docker
-Kubernetes

-Langchain.js
-Rag

I just have one year l
eft then I have to start working in my FYP project. Prioritize this which are most most important in an order.
My goal i
s to become a full stack expert developer and it is a dream.
```
---

     
 
all -  [ Has anyone gotten Langchain RetirevalQA to work with ChatAnthropic? ](https://www.reddit.com/r/LangChain/comments/1fv7k4w/has_anyone_gotten_langchain_retirevalqa_to_work/) , 2024-10-06-0914
```
I developed my application with OpenAI RAG and sold huge things to the business on how our arch can switch between Claud
e and GPT on runtime. 

The only problem is I am getting issues like 'Cant Instantiate BaseLanguageModel without impleme
ntation to abstract methods like agenerate_prompt'. I have made no changes, just using VoyageAI and new langchain_anthro
pic package to use claude-3.5. Unable to understand where this issue is. 

Any help, code references or versions of Lang
chain packages where people have made this work would be greatly appreciated! 
```
---

     
 
all -  [ AI-Powered RFP Document Comparison and Gap Analysis with Interactive Chat (openai,llamaindex,langcha ](https://www.reddit.com/r/OpenAI/comments/1fv4i0m/aipowered_rfp_document_comparison_and_gap/) , 2024-10-06-0914
```
Hey everyone! 👋

I've been working on this cool little web app called RFP Analyzer. It's basically a tool that helps you
 break down Request for Proposal (RFP) documents and your responses to them. Super handy if you're dealing with a lot of
 these in your work!

[video screen recording of the rfp analyzer tool in action](https://reddit.com/link/1fv4i0m/video/
jofsq8inpisd1/player)

**What it does:**

* You upload your RFP and response PDFs
* It processes them and gives you a ne
at summary
* You can chat with an AI about the documents, so you can also use it to validate if your actually capturing 
the data from the document correctly
* It generates a report comparing the two

**UI using web tech (Flask, HTMX, Alpine
.js).**

[Ui of the RFP Analyzer ](https://preview.redd.it/aany534goisd1.png?width=2880&format=png&auto=webp&s=b8e913a5b
c761868a904636c9bb6da467822701a)

I will soon open-sourced it on GitHub, so feel free to check it out, star it, or even 
contribute if you're feeling generous! Feel free to ask questions :)

[https://github.com/lesteroliver911/openai-rfp-res
ponse-analyzer](https://github.com/lesteroliver911/openai-rfp-response-analyzer)
```
---

     
 
all -  [ Llama 3.2: A brief analysis of vision capabilities ](https://www.reddit.com/r/LangChain/comments/1fv4i0d/llama_32_a_brief_analysis_of_vision_capabilities/) , 2024-10-06-0914
```
Thanks to the open-source gods! Meta finally released the multi-modal language models. There are two models: a small 11B
 one and a mid-sized 90B one.

The timing couldn't be any better, as I was looking for an open-access vision model for a
n application I am building to replace GPT4o.

So, I wanted to know if I can supplement GPT4o usage with Llama 3.2; thou
gh I know it’s not a one-to-one replacement, I expected it to be good enough considering Llama 3 70b performance, and it
 didn’t disappoint.

I tested the model on various tasks that I use daily,

* General Image Understanding
   * Image cap
tioning
   * counting objects
   * identifying tools
   * Plant disease identification
* Medical report analysis
* Text 
extraction
* Chart analysis

Consider going through this article to dive deeper into the tests. [Meta Llama 3.2: A deep 
dive into vision capabilities.:](https://composio.dev/blog/meta-llama-3-2-a-deep-dive-into-vision-capabilities/)

# What
 did I feel about the model?

The model is great and, indeed, a great addition to the open-source pantheon. It is excell
ent for day-to-day use cases, and considering privacy and cost, it can be a potential replacement for GPT-4o for this ki
nd of task.

However, GPT-4o is still better for difficult tasks, such as medical imagery analysis, stock chart analysis
, and similar tasks.

I have yet to test them for getting the coordinates of objects in an image to create bounding boxe
s. If you have done this, let me know what you found.

Also, please comment on how you liked the model’s vision performa
nce and what use cases you plan on using it for.
```
---

     
 
all -  [ Stock Insights with AI Agent-Powered Analysis With Lyzr Agent API ](https://www.reddit.com/r/LangChain/comments/1fv47sq/stock_insights_with_ai_agentpowered_analysis_with/) , 2024-10-06-0914
```
Hi everyone! I've just created an app that elevates stock analysis by integrating FastAPI and Lyzr Agent API. Get real-t
ime data coupled with intelligent insights to make informed investment decisions. Check it out and let me know what you 
think!

Blog: [https://medium.com/@harshit\_56733/step-by-step-guide-to-build-an-ai-stock-analyst-with-fastapi-and-lyzr-
agent-api-9d23dc9396c9](https://medium.com/@harshit_56733/step-by-step-guide-to-build-an-ai-stock-analyst-with-fastapi-a
nd-lyzr-agent-api-9d23dc9396c9)
```
---

     
 
all -  [ Few shot learning with tool usage ](https://www.reddit.com/r/LangChain/comments/1fv44ld/few_shot_learning_with_tool_usage/) , 2024-10-06-0914
```
Hello,

I'm building an agent using Claude 3.5 Sonnet as LLM. Does anyone have experience with few shot learning that in
volves tool usage? How should I format the examples? Thank you!
```
---

     
 
all -  [ Paid internship test  ](https://i.redd.it/0uq2o1qbiisd1.png) , 2024-10-06-0914
```
Tommorow i got my paid internship test,he said he will have a test which will be some task of coding i will have to perf
orm

I wanna know what should i expect and should prepare for tommorow

I have attached an image of my cv that contain m
y skills
```
---

     
 
all -  [ Thoughts about OPEA? ](https://www.reddit.com/r/LangChain/comments/1fv2zw3/thoughts_about_opea/) , 2024-10-06-0914
```
Hello,

I was looking for a 'production grade' deployment architecture for Langchain using microservices and stumbled up
on [OPEA](https://opea.dev/), has anyone used/tried it? The architecture (below) seems quite interesting and you can use
 Lanchain in any of the microservice

https://preview.redd.it/jo5409lw4isd1.png?width=881&format=png&auto=webp&s=9082ac5
6cfa7edfe94ed6090753ace695a459c2b

Both Intel, AMD, SAP and other big companies are in the project so it seems quite a b
ig effort
```
---

     
 
all -  [ Cross-Paged Table PDFs for Extraction Testing (Vertical/Horizontal Splits/Handwritten) ](https://www.reddit.com/r/LangChain/comments/1fuz911/crosspaged_table_pdfs_for_extraction_testing/) , 2024-10-06-0914
```
Hey everyone,

I'm working on a project to test and improve the extraction of tables from PDFs, especially when the tabl
es are split across multiple pages. This includes tables that:

* Are split **vertically** across pages (e.g., rows on o
ne page, continued on the next).
* Are split **horizontally** across pages (e.g., columns on one page, continued on the 
next).

If you have any PDFs with these types of cross-paged tables, I'd really appreciate it if you could share them wi
th me. 

Thanks in advance for your help!
```
---

     
 
all -  [ Streaming with LangGraph ](https://www.reddit.com/r/LangChain/comments/1fusj4e/streaming_with_langgraph/) , 2024-10-06-0914
```
I need my langgraph app to stream ai responses. But I can’t get CompiledStateGraph to stream out a response.

.astream(s
tream_mode=“messages”) almost works, except it just spit out everything in one go like .invoke

Maybe .astream_event or 
.astream_log might the solution? I need your help on this.

Thanks 🙏 
```
---

     
 
all -  [ Newbie on langchain ](https://www.reddit.com/r/LangChain/comments/1fuqqf7/newbie_on_langchain/) , 2024-10-06-0914
```
Trying to understand why langchain is not overkill especially for basic PrompTemplate or OutputParser features. Anyone h
ave a satisfying answer? 
Do you use langchain for every kind of operation in tour project or do you also feel it’s an o
verkill sometimes?
```
---

     
 
all -  [ Why use Flowise when n8n offers RAG and more? ](https://www.reddit.com/r/LangChain/comments/1fuqbmf/why_use_flowise_when_n8n_offers_rag_and_more/) , 2024-10-06-0914
```
I've used both Flowise and n8n to create my Chatbot that executes a RAG operation to answer the user's queries.

The flo
w executes an n8n HTTP POST request to Flowise that returns the LLM's response. The time to reaponse was around 6 second
s. Too slow compared to using the native chatbox in Flowise (am I doing something wrong?)

Then, I realized that I can d
uplicate the RAG operation on n8n itself, ditching Flowise altogether. It worked.

I'd love to know your opinions on whe
ther n8n can replace Flowise completely. Am I missing the point of why Flowise is still relevant?
```
---

     
 
all -  [ Trying to Help With LLM Apps ](https://www.reddit.com/r/LangChain/comments/1fulbos/trying_to_help_with_llm_apps/) , 2024-10-06-0914
```
I just recently started building an LLM Application and was having difficulty knowing if my workflow was good enough for
 production without testing it many times.

So I tried to build this tool that automatically evaluates my workflow befor
e I even run it and have actually been able to get more reliable outputs way faster!

https://preview.redd.it/c8acftj4kd
sd1.png?width=3080&format=png&auto=webp&s=d0c9178ca17352a22944b5f4a28d254dec8028b5

I wanted to share this with you guys
 to help anyone else having a similar problem. Please let me know if this is something you’d find useful and if you want
 to try it.

Best of luck on creating your LLM Apps!
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-06-0914
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

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-06-0914
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

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-06-0914
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

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-10-06-0914
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-10-06-0914
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-06-0914
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

     
