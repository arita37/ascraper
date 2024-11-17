 
all -  [ How to prevent chat() function in pandasai from downloading images? ](https://www.reddit.com/r/StreamlitOfficial/comments/1gswjm3/how_to_prevent_chat_function_in_pandasai_from/) , 2024-11-17-0914
```
I'm using the [pandasai](https://pypi.org/project/pandasai/) library for data analysis in my application. When I call th
e `chat()` function to generate image responses, it triggers a download of the images instead of displaying them. I want
 to display these images directly in my application.

Here’s a snippet of my code:

    import pandas as pd
    from pan
dasai import SmartDataframe
    from langchain_groq.chat_models import ChatGroq
    import os
    import streamlit as st

    
    # groq
    llm = ChatGroq(model_name='llama3-70b-8192', api_key=os.environ['GROQ_API_KEY'])
    
    # Streaml
it app setup
    st.title('Data Analysis with SmartDataframe')
    
    df = pd.read_excel('data.xlsx')
    df = SmartDa
taframe(df, config={'llm': llm})
    
    st.write('Smart Dataframe')
    
    # User input for chat command
    user_in
put = st.text_input('Enter your command:')
    
    if user_input:  # Check if user input is provided
        response =
 df.chat(user_input)  # This line triggers the download
        # Assuming response is an image URL or path
        st.i
mage(response, use_container_width=True)//

The issue arises when I call `response = df.chat(user_input)`, which seems t
o trigger a download of the image instead of displaying it. I expected the image to be shown directly in my application.


I would like the image to display directly in the Streamlit app without triggering any download or new window.

Is the
re a way to modify the chat() function in pandasai to prevent this download behavior?

If not, are there any workarounds
 or suggestions for implementing this feature?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1gswggs/list_of_free_and_best_selling_discounted_courses/) , 2024-11-17-0914
```
# Udemy Free Courses for 17 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24922/)Fundamentals of Backend Engineering
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/24921/)Creación de una Tienda Virtual con Kotlin | Android Studio
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24920/)The Complete Deep Learning Course 2024 With 7+ Real Projects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24919/)Business Analytics con Python y ChatGPT: De Cero a Experto
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24918/)LangChain Mastery: Build GenAI Apps with LangChain &Pinecone
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24917/)Google Hacking – Aprende Búsquedas Avanzadas con Google
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24916/)VPS Linux en DigitalOcean:Ubuntu 22, Nginx, PHP y WordPress
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24915/)Vue JS (2 y 3) – Crea Aplicaciones Web Modernas con Vue
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24914/)Node.js – Creando API con Express y MongoDB (Incl. Deno)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24913/)ISO/IEC 27001 Implementando Seguridad de la Información
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24912/)ISO 22301 – Gestión de la Continuidad del Negocio
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24911/)MongoDB – La mejor Base de Datos NoSQL desde cero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24910/)Dart – La Guía Completa para Aprender a Programar en Dart
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
909/)Evaluación Financiera de Proyectos de Inversión
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24908/)Complete
 Chibi Drawing Course: Draw Adorable Characters!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24907/)Cisco BGP Ma
sterclass for Enterprise Network Engineers
* Java SE 11 Developer 1Z0-819 OCP Course – Part 1
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/24906/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24905/)Flutter & OCR – Build Cam Sc
anner Clone in Flutter 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24904/)Complete Java Software Developer 
Masterclass (for Java 10)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24903/)Planificación y Gestión de Proyecto
s: PMBOK y Agile Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24902/)Control Estadístico de Procesos Six Si
gma (6 σ) con Minitab
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24901/)Finanzas Para No Financieros: Análisis 
y Visualización
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24900/)Modelación de Procesos de Negocios (BPMN 2.0)
 con Bizagi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24899/)Modelos Financieros en Excel para la Valoración d
e Empresas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24898/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hast
a Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24897/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso
 a Paso
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24896/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto
!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24895/)Crea tu propio PayPal desde cero con Django y React Native

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24894/)Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24893/)Modelos de Riesgo Crédito con Python
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24892/)Formation Complète: Création Application-Android Studio/Java
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24891/)ArcGIS specialization – ArcGIS Pro, 3D and ArcHydro -AulaGEO
* Big Data Hadoop Course
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/24890/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24889/)Bus
iness Analytics Online Class
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24888/)Advanced Project Management: Str
ategies for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24887/)Customer Experience with Generative AI: A
dvanced CX with AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24886/)Learn Java Masterclass(updated to Java 17)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24885/)Learn Shopify Now: Shopify for Beginners
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24884/)Lean Six Sigma Yellow Belt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4883/)How to Find Freelance Social Media Management Jobs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24882/)Sola
r Cell Technology
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24881/)Master Any Language with ChatGPT: Boost You
r Language Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24880/)Success Exam | Python NLTK : Natural Langua
ge ToolKit | NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24879/)Design of Wastewater Systems – SewerGEMS – A
ulaGEO
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24878/)Mastering English Idioms: Essential for ESL Communicat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24877/)Structural&Construction Design of 2000m2 real Project Vil
la
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24876/)Mastering Social Media Marketing: A Comprehensive Guide
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24875/)Amazon Dropshipping FBM | Titans Product Research Formula
* Bus
iness Process Optimization with Lean Six Sigma
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24874/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24873/)Cybersecurity for Developers: From Basics to Best Practices
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24872/)Mastering ServiceNow Admin&Development From Beginner to Pro
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/24871/)Comprehensive React JS Practice Test : Skill Mastery
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24870/)Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24869/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/24868/)Data Science Career Path
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24867/)Profi
ciency In Javascript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24866/)Discover Your Career Path & Land a Job Y
ou Love in 12 Weeks
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24865/)The Best ChatGPT & AI Course: Make Money 
With AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24864/)Architectural Shop Drawing Plans in AutoCAD 2020
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24863/)Internet of Things (IoT) Online Course
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24862/)Oracle PL/SQL: From Basics to Advanced Database Programming
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/24861/)Oracle RMAN: Comprehensive Backup and Recovery Techniques
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24860/)GSDC Certified Generative AI Professional – Exams
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/24859/)Oracle Database Administration: Oracle DBA Fundamentals
* Mastering Project Schedule Management and Es
timation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24858/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24857/)Mastering Software Estimation: Techniques and Best Practices
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24856/)Mastering CMMI: Process Improvement and Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
855/)Function Point Analysis FPA: A Guide to Software Estimation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/248
54/)Start a Digital Sales Business with Free Products to Sell
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24853/
)Mastering Oracle SQL: From Fundamentals to Advanced Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24852/
)NGINX, Apache, SSL Encryption – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24851/)API Tes
ting with Postman: From Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24850/)AWS Interview Pr
eparations: Quiz Solutions and Explanations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24849/)Learn the Python 
Programming Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24848/)Winning Option Strategies For Any Market

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24847/)2024 Complete Python Bootcamp from Zero to Hero in Python
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24846/)ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24845/)Become HTML Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24844/)Mastering iOS Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24843/)AutoCAD 2024 para Mac OS

* Learn Word Now: Microsoft Word 365 for Beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24842/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24841/)DEA-1TT4: Dell EMC Associate Practice test 2024
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/24840/)Presentations with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2483
9/)DEA-41T1: Dell EMC PowerEdge Associate Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24838/)
Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24837/)Pitch Deck Hero: Business Presenta
tion and Communication
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24836/)Key Metrics of Unit Economics (CPA, AR
PU, CAC, ARPPU, C1)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24835/)7 Days Meditation Challenge
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/24834/)300-435: Cisco Enterprise Solutions Practice test 2024
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24833/)Day Trading for Beginners: How to Make Money Trading Stocks
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24832/)أسئلة وتدريبات عملية في المحاسبة المالية
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24831/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24830/)Revit Nested Families- Parametric Container- From Zero
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24829/)Learn Functions & Function Expressions in Modern JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/24828/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24827/)
Modern Android App Architecture
* Amazon SEO Guide: How to Rank First on Amazon
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/24826/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24825/)AutoCAD 2024 – from Zero to Advanced- Full
 Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24824/)ChatGPT for Product Management & Innovation
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24823/)Your Guide To Health
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/24822/)WEB3 Token Gating. Create an NFT gated website from scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/24821/)Generative AI for All: Practical Prompt Engineering Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24820/)Cómo Crear un Blog con WordPress Para Principiantes 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2481
9/)Máster en Comercio Electrónico con WordPress 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24818/)Cómo Cre
ar una Academia Online con WordPress y Tutor LMS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24817/)Elementor Ki
ts: Crea una Página Web con Elementor Pro 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24816/)Cómo Crear una
 Tienda Online con Inteligencia Artificial
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24815/)Mastering Cryptocu
rrency Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24814/)Python Development & Data Science: Variables a
nd Data Types
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24813/)Exotic Pole Dance: Choreography, Breakdowns, Wa
rm-up, Splits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24812/)Inteligencia Artificial : Empodera tu Futuro La
boral
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24811/)Cybersecurity Awareness en Español
* Master Lead Genera
tion: Grow Subscribers & Sales with Popups
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24810/)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24809/)Mastering AWS Serverless: Hands-On with Core AWS Services
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/24808/)CSS, JavaScript And Python Complete Course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24807/)Ethical Hacking: Hack Linux Systems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24806/)Image
 Processing with Python PIL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24805/)Unit Economics & CRM: LTV, Churn,
 Retention Rates, Cohorts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24804/)5V0-22.23: VMware Certified Profess
ional – VMware vSAN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24803/)Machine Learning Intro for Python Dev
elopers

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1gswgdr/list_of_free_and_best_selling_discounted_courses/) , 2024-11-17-0914
```
# Udemy Free Courses for 17 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24922/)Fundamentals of Backend Engineering
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/24921/)Creación de una Tienda Virtual con Kotlin | Android Studio
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24920/)The Complete Deep Learning Course 2024 With 7+ Real Projects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/24919/)Business Analytics con Python y ChatGPT: De Cero a Experto
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24918/)LangChain Mastery: Build GenAI Apps with LangChain &Pinecone
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24917/)Google Hacking – Aprende Búsquedas Avanzadas con Google
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24916/)VPS Linux en DigitalOcean:Ubuntu 22, Nginx, PHP y WordPress
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24915/)Vue JS (2 y 3) – Crea Aplicaciones Web Modernas con Vue
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24914/)Node.js – Creando API con Express y MongoDB (Incl. Deno)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24913/)ISO/IEC 27001 Implementando Seguridad de la Información
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24912/)ISO 22301 – Gestión de la Continuidad del Negocio
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24911/)MongoDB – La mejor Base de Datos NoSQL desde cero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24910/)Dart – La Guía Completa para Aprender a Programar en Dart
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
909/)Evaluación Financiera de Proyectos de Inversión
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24908/)Complete
 Chibi Drawing Course: Draw Adorable Characters!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24907/)Cisco BGP Ma
sterclass for Enterprise Network Engineers
* Java SE 11 Developer 1Z0-819 OCP Course – Part 1
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/24906/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24905/)Flutter & OCR – Build Cam Sc
anner Clone in Flutter 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24904/)Complete Java Software Developer 
Masterclass (for Java 10)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24903/)Planificación y Gestión de Proyecto
s: PMBOK y Agile Scrum
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24902/)Control Estadístico de Procesos Six Si
gma (6 σ) con Minitab
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24901/)Finanzas Para No Financieros: Análisis 
y Visualización
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24900/)Modelación de Procesos de Negocios (BPMN 2.0)
 con Bizagi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24899/)Modelos Financieros en Excel para la Valoración d
e Empresas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24898/)Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hast
a Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24897/)Curso Blogger 2024: Cómo Crear un Blog Gratis Paso
 a Paso
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24896/)Curso de Google Drive 2024, ¡Desde Cero Hasta Experto
!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24895/)Crea tu propio PayPal desde cero con Django y React Native

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24894/)Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24893/)Modelos de Riesgo Crédito con Python
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24892/)Formation Complète: Création Application-Android Studio/Java
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24891/)ArcGIS specialization – ArcGIS Pro, 3D and ArcHydro -AulaGEO
* Big Data Hadoop Course
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/24890/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24889/)Bus
iness Analytics Online Class
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24888/)Advanced Project Management: Str
ategies for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24887/)Customer Experience with Generative AI: A
dvanced CX with AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24886/)Learn Java Masterclass(updated to Java 17)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24885/)Learn Shopify Now: Shopify for Beginners
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24884/)Lean Six Sigma Yellow Belt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4883/)How to Find Freelance Social Media Management Jobs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24882/)Sola
r Cell Technology
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24881/)Master Any Language with ChatGPT: Boost You
r Language Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24880/)Success Exam | Python NLTK : Natural Langua
ge ToolKit | NLP
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24879/)Design of Wastewater Systems – SewerGEMS – A
ulaGEO
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24878/)Mastering English Idioms: Essential for ESL Communicat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24877/)Structural&Construction Design of 2000m2 real Project Vil
la
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24876/)Mastering Social Media Marketing: A Comprehensive Guide
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24875/)Amazon Dropshipping FBM | Titans Product Research Formula
* Bus
iness Process Optimization with Lean Six Sigma
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24874/)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24873/)Cybersecurity for Developers: From Basics to Best Practices
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24872/)Mastering ServiceNow Admin&Development From Beginner to Pro
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/24871/)Comprehensive React JS Practice Test : Skill Mastery
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24870/)Master AI-Powered Chatbots, 24/7 Appointment Booking with AI
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24869/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/24868/)Data Science Career Path
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24867/)Profi
ciency In Javascript
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24866/)Discover Your Career Path & Land a Job Y
ou Love in 12 Weeks
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24865/)The Best ChatGPT & AI Course: Make Money 
With AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24864/)Architectural Shop Drawing Plans in AutoCAD 2020
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24863/)Internet of Things (IoT) Online Course
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/24862/)Oracle PL/SQL: From Basics to Advanced Database Programming
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/24861/)Oracle RMAN: Comprehensive Backup and Recovery Techniques
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24860/)GSDC Certified Generative AI Professional – Exams
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/24859/)Oracle Database Administration: Oracle DBA Fundamentals
* Mastering Project Schedule Management and Es
timation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24858/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24857/)Mastering Software Estimation: Techniques and Best Practices
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24856/)Mastering CMMI: Process Improvement and Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
855/)Function Point Analysis FPA: A Guide to Software Estimation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/248
54/)Start a Digital Sales Business with Free Products to Sell
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24853/
)Mastering Oracle SQL: From Fundamentals to Advanced Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24852/
)NGINX, Apache, SSL Encryption – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24851/)API Tes
ting with Postman: From Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24850/)AWS Interview Pr
eparations: Quiz Solutions and Explanations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24849/)Learn the Python 
Programming Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24848/)Winning Option Strategies For Any Market

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24847/)2024 Complete Python Bootcamp from Zero to Hero in Python
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/24846/)ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/24845/)Become HTML Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24844/)Mastering iOS Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24843/)AutoCAD 2024 para Mac OS

* Learn Word Now: Microsoft Word 365 for Beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24842/)
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24841/)DEA-1TT4: Dell EMC Associate Practice test 2024
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/24840/)Presentations with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2483
9/)DEA-41T1: Dell EMC PowerEdge Associate Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24838/)
Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24837/)Pitch Deck Hero: Business Presenta
tion and Communication
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24836/)Key Metrics of Unit Economics (CPA, AR
PU, CAC, ARPPU, C1)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24835/)7 Days Meditation Challenge
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/24834/)300-435: Cisco Enterprise Solutions Practice test 2024
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/24833/)Day Trading for Beginners: How to Make Money Trading Stocks
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/24832/)أسئلة وتدريبات عملية في المحاسبة المالية
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24831/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24830/)Revit Nested Families- Parametric Container- From Zero
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24829/)Learn Functions & Function Expressions in Modern JavaScript
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/24828/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24827/)
Modern Android App Architecture
* Amazon SEO Guide: How to Rank First on Amazon
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/24826/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24825/)AutoCAD 2024 – from Zero to Advanced- Full
 Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24824/)ChatGPT for Product Management & Innovation
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/24823/)Your Guide To Health
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/24822/)WEB3 Token Gating. Create an NFT gated website from scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/24821/)Generative AI for All: Practical Prompt Engineering Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
24820/)Cómo Crear un Blog con WordPress Para Principiantes 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2481
9/)Máster en Comercio Electrónico con WordPress 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24818/)Cómo Cre
ar una Academia Online con WordPress y Tutor LMS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24817/)Elementor Ki
ts: Crea una Página Web con Elementor Pro 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24816/)Cómo Crear una
 Tienda Online con Inteligencia Artificial
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24815/)Mastering Cryptocu
rrency Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24814/)Python Development & Data Science: Variables a
nd Data Types
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24813/)Exotic Pole Dance: Choreography, Breakdowns, Wa
rm-up, Splits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24812/)Inteligencia Artificial : Empodera tu Futuro La
boral
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24811/)Cybersecurity Awareness en Español
* Master Lead Genera
tion: Grow Subscribers & Sales with Popups
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24810/)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24809/)Mastering AWS Serverless: Hands-On with Core AWS Services
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/24808/)CSS, JavaScript And Python Complete Course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24807/)Ethical Hacking: Hack Linux Systems
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24806/)Image
 Processing with Python PIL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24805/)Unit Economics & CRM: LTV, Churn,
 Retention Rates, Cohorts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24804/)5V0-22.23: VMware Certified Profess
ional – VMware vSAN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24803/)Machine Learning Intro for Python Dev
elopers

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies)
```
---

     
 
all -  [ I'm close to a productivity explosion ](/r/AI_Agents/comments/1gsqt1v/im_close_to_a_productivity_explosion/) , 2024-11-17-0914
```

```
---

     
 
all -  [ Find tech partner ](https://www.reddit.com/r/LangChain/comments/1gsuspk/find_tech_partner/) , 2024-11-17-0914
```
WeChat/QQ AI Assistant Platform - Ready-to-Build Opportunity

Find Technical Partner

1. Market

WeChat: 1.3B+ monthly a
ctive users
QQ: 574M+ monthly active users
Growing demand for AI assistants in Chinese market
Limited competition in spe
cialized AI assistant space


2. Why This Project Is Highly Feasible Now

Key Infrastructure Already Exists
LlamaCloud h
andles the complex RAG pipeline:
Professional RAG processing infrastructure
Supports multiple document formats out-of-bo
x
Pay-as-you-go model reduces initial investment
No need to build and maintain complex RAG systems
Enterprise-grade reli
ability and scalability


Mature WeChat/QQ Integration Libraries:

Wechaty: Production-ready WeChat bot framework
go-cqh
ttp: Stable QQ bot framework
Rich ecosystem of plugins and tools
Active community support
Well-documented APIs

3. Busin
ess Model

B2B SaaS subscription model
Revenue sharing with integration partners
Custom enterprise solutions

If you fin
d it interesting, please dm me
```
---

     
 
all -  [ This week in AI and Machine Learning:
🛸 US to Deploy World’s First Alien-Hunting System
👀 OpenAI’s T ](https://www.reddit.com/r/u_enoumen/comments/1gst4oj/this_week_in_ai_and_machine_learning_us_to_deploy/) , 2024-11-17-0914
```
# [This week in AI and Machine Learning: November 09th - November 17th  2024](https://apps.apple.com/ca/app/ai-machine-l
earning-4-dummies/id1611593573)

Listen at [https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds
-first-alien/id1684415169?i=1000677179618](https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds-
first-alien/id1684415169?i=1000677179618)

# 🛸 US to Deploy World’s First Alien-Hunting System:

# 👀 OpenAI’s Tumultuous
 Early Years Revealed in Emails:

# 🕶️ Samsung XR Glasses Specs Revealed in a Leak:

# 📄 Google Docs Introduces AI Image
 Creation:

# 🟦 Bluesky Won’t Use Posts for AI Training:

# Microsoft and NASA Launch AI Earth Copilot:

# ChatGPT Deskt
op Apps Receive Major Upgrades:

# Anthropic Partners with U.S. Government to Prevent AI Nuclear Leaks:

# AI Poetry Out
shines Human Classics in Blind Test:

# ChatGPT Desktop App Gains Direct App Integration:

# IBM's Most Compact AI Model
s Target Enterprises:

# TikTok Launches Symphony Creative Studio:

# New architecture may have cracked the Language of 
Life: An LLM for DNA and Biology.

# [💪 AI and Machine Learning For Dummies](https://apps.apple.com/ca/app/ai-machine-le
arning-4-dummies/id1611593573)

Djamgatech has launched a new educational app on the Apple App Store, aimed at simplifyi
ng AI and machine learning for beginners.

**It is a mobile App that can help anyone Master AI & Machine Learning on the
 phone!**

**Download 'AI and Machine Learning For Dummies ' FROM APPLE APP STORE and conquer any skill level with inter
active quizzes, certification exams, & animated concept maps in:**

* **Artificial Intelligence**
* **Machine Learning**

* **Deep Learning**
* **Generative AI**
* **LLMs**
* **NLP**
* **xAI**
* **Data Science**
* **AI and ML Optimization**

* **AI Ethics & Bias ⚖️**

**& more! ➡️**[ App Store Link: ](https://apps.apple.com/ca/app/ai-machine-learning-4-dummies
/id1611593573)[https://apps.apple.com/ca/app/ai-machine-learning-4-dummies/id1611593573](https://apps.apple.com/ca/app/a
i-machine-learning-4-dummies/id1611593573)

# [AI Consultation](http://djamgatech.com/contact-us/):

We empower organiza
tions to leverage the transformative power of Artificial Intelligence. Our AI consultancy services are designed to meet 
the unique needs of industries such as oil and gas, healthcare, education, and finance. **We provide customized AI and M
achine Learning podcast for your organization, training sessions, ongoing advisory services, and tailored AI solutions t
hat drive innovation, efficiency, and growth.**

Contact us [here](http://djamgatech.com/contact-us/) ([or email us at i
nfo@djamgatech.com](http://djamgatech.com/contact-us/)) to receive a personalized value proposition.



# [What Else Hap
pened in AI this Week?](https://podcasts.apple.com/ca/podcast/this-week-in-ai-ml-us-to-deploy-worlds-first-alien/id16844
15169?i=1000677179618)

**Alibaba Cloud** released ***Qwen2.5-Coder-32B***, an open-source model for programming tasks t
hat matches the coding capabilities of GPT-4o. In addition to this flagship model, four new models have been released, e
xpanding the Qwen2.5-Coder family to a total of six models, ranging in sizes from 0.5B to 32B. An Artifacts app, similar
 to the Claude Artifacts, has also been launched. \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-a
i-news-trends-chatgpt-gemini-gen/id1684415169)\]

**Fixie AI** released ***Ultravox v0.4.1***, a family of multi-modal, 
open-source models trained specifically for enabling real-time conversations with AI. Ultravox does not rely on a separa
te automatic speech recognition (ASR) stage, but consumes speech directly in the form of embeddings. The latency perform
ance is comparable to the OpenAI Realtime . Fixie also released Ultravox Realtime, a managed service to integrate real t
ime AI voice conversations into applications \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-new
s-trends-chatgpt-gemini-gen/id1684415169)\].

**Google** introduced a new model ***Gemini (Exp 1114***), available now i
n Google AI Studio. It has climbed to joint #1 overall on the Chatbot Arena leaderboard, following over 6K+ community vo
tes in the past week. It matches the performance of 4o-latest while surpassing o1-preview and is #1 on Vision leaderboar
d \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\]
.

**Nexusflow** released ***Athene-V2***, an open source 72B model suite, fine-tuned from Qwen 2.5 72B. It includes Ath
ene-V2-Chat matching GPT-4o across multiple benchmark and Athene-V2-Agent, a specialized agent model surpassing GPT-4o i
n function calling and agent applications\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-tr
ends-chatgpt-gemini-gen/id1684415169)\].

**Vidu** launched ***Vidu-1.5***, a multimodal model with multi-entity consist
ency. Vidu-1.5 can seamlessly integrate people, objects, and environments to generate a video\[[Listen](https://podcasts
.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Codeium launched Windsurf 
Editor, an agentic IDE. It introduces ‘Flow’ a collaborative agent that combines the collaborative nature of copilots wi
th the ability to be independently powerful like an agent \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-
latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Researchers** introduced ***MagicQuill***, an intelligent i
nteractive image editing system. It uses a multimodal large language model to anticipate editing intentions in real time
, removing the need for explicit prompts \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-tr
ends-chatgpt-gemini-gen/id1684415169)\].

**DeepSeek** released ***JanusFlow***, an open-source unified multimodal model
 that excels at both image understanding & generation in a single model. It matches or outperforms specialized models in
 their respective domains and significantly surpasses existing unified models on standard benchmarks \[[Listen](https://
podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Google DeepMind*
* has open-sourced AlphaFold 3 for academic use. It models interactions between proteins, DNA, RNA, and small molecules.
 This is vital for drug discovery and disease treatment \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-la
test-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

**Epoch AI** launched ***FrontierMath***, a benchmark for advan
ced mathematical reasoning in AI. Developed with over 60 top mathematicians, it includes hundreds of challenging problem
s, of which AI systems currently solve less than 2% \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest
-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

TikTok launched Symphony Creative Studio, an AI-powered video-gener
ation tool for Business users. Users can turn product information or a URL into a video, add a digital avatar to narrate
 the video script, or localize any existing videos into new languages using translation and dubbing capabilities \[[List
en](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Nous R
esearch introduced the Forge Reasoning API Beta. It lets you take any model and superpower it with a code interpreter an
d advanced reasoning capabilities. Hermes 70B x Forge is competitive with much larger models from Google, OpenAI and Ant
hropic in reasoning benchmarks\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgp
t-gemini-gen/id1684415169)\].

Anthropic added a new prompt improver to the Anthropic Console. Take an existing prompt a
nd Claude will automatically refine it with prompt engineering techniques like chain-of-thought reasoning \[[Listen](htt
ps://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Nvidia presen
t Add-it, a training-free method for adding objects to images based on text prompts. Add-it works well on real and gener
ated images. It leverages an existing text-to-image model (FLUX.1-dev) without requiring additional training\[[Listen](h
ttps://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Microsoft r
eleased TinyTroupe, an experimental Python library for simulation of people with specific personalities, interests, and 
goals. These artificial agents - TinyPersons - can listen to us and one another, reply back, and go about their lives in
 simulated TinyWorld environments. This is achieved by leveraging the power of Large Language Models (LLMs), notably GPT
-4, to generate realistic simulated behavior \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-new
s-trends-chatgpt-gemini-gen/id1684415169)\].

Johns Hopkins researchers trained a surgical robot by having it watch vide
os of skilled surgeons. Using imitation learning, the robot learned complex tasks like suturing and tissue handling, ult
imately performing with skill comparable to human doctors \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-
latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Stripe launched a SDK built for AI agents - LLMs can call pay
ment, billing, issuing, etc APIs. It natively supports Vercel’s AI SDK, LangChain, and CrewAI, and works with any LLM pr
ovider that supports function calling\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends
-chatgpt-gemini-gen/id1684415169)\].

Researchers released OpenCoder, completely open-source and reproducible code LLM f
amily which includes 1.5B and 8B base and chat models. Starting from scratch, OpenCoder is trained on 2.5 trillion token
s and built on the transparent data process pipeline and reproducible dataset. It achieves top-tier performance on multi
ple code LLM evaluation benchmarks\[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-ch
atgpt-gemini-gen/id1684415169)\].

Alibaba launched Accio, an AI search engine for small businesses to find wholesale pr
oducts alongside the analysis on their popularity with consumers and projected profit. Accio is powered by Alibaba’s Ton
gyi Qianwen large language model \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-cha
tgpt-gemini-gen/id1684415169)\].

Anthropic released RapidResponseBench, a benchmark that evaluates how well LLM defense
s can adapt to and handle different jailbreak strategies after seeing just a few examples \[[Listen](https://podcasts.ap
ple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

LangChain launched Prompt Can
vas, an interactive tool designed to simplify prompt creation. Prompt Canvas, the UX inspired from ChatGPT’s Canvas, let
s you collaborate with an LLM agent to iteratively build and refine your prompts\[[Listen](https://podcasts.apple.com/ca
/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

LangChain released Promptim, an experim
ental open-source library for prompt optimization. Promptim automates the process of improving prompts on specific tasks
. You provide initial prompt, a dataset, and custom evaluators (and optional human feedback), and promptim runs an optim
ization loop to produce a refined prompt that aims to outperform the original\[[Listen](https://podcasts.apple.com/ca/po
dcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id1684415169)\].

Apple’s Final Cut Pro 11 with AI-powered f
eatures now available \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini
-gen/id1684415169)\].

ChatGPT app for Mac is now able to integrate with coding apps like Xcode, VS Code, TextEdit, and 
Terminal \[[Listen](https://podcasts.apple.com/ca/podcast/ai-unraveled-latest-ai-news-trends-chatgpt-gemini-gen/id168441
5169)\].
```
---

     
 
all -  [ Open Source RAG Repo: Everything You Need in One Place ](https://www.reddit.com/r/OpenSourceeAI/comments/1gsshf0/open_source_rag_repo_everything_you_need_in_one/) , 2024-11-17-0914
```
For the past 3 months, I’ve been diving deep into building RAG apps and found tons of information scattered across the i
nternet—YouTube videos, research papers, blogs—you name it. It was overwhelming.

So, I created [this repo](https://gith
ub.com/bRAGAI/bRAG-langchain) to consolidate everything I’ve learned. It covers RAG from beginner to advanced levels, sp
lit into 5 Jupyter notebooks:

* Basics of RAG pipelines (setup, embeddings, vector stores).
* Multi-query techniques an
d advanced retrieval strategies.
* Fine-tuning, reranking, and more.

Every source I used is cited with links, so you ca
n explore further. If you want to try out the notebooks, just copy the `.env.example` file, add your API keys, and you'r
e good to go.

Would love to hear feedback or ideas to improve it. (it is still a work in progress and I plan on adding 
more resources there soon!)

*In case the link above does not work here it is:* [https://github.com/bRAGAI/bRAG-langchai
n](https://github.com/bRAGAI/bRAG-langchain)

If you’ve found the repo useful or interesting, I’d really appreciate it i
f you could give it a ⭐️ on GitHub. It helps the project gain visibility and lets me know it’s making a difference.

Tha
nks for your support!
```
---

     
 
all -  [ Multiple dependent tools ](https://www.reddit.com/r/LangChain/comments/1gsr4px/multiple_dependent_tools/) , 2024-11-17-0914
```
  
I would like some help/advice.  
I have a project I'm working on where I have an agent with multiple tools, but some 
tools need to be provided inputs from the outputs of other tools...  
for example, let's say one tool provides me with a
 URL of a webpage and the other scrapes it. the order of running must be 'get\_url\_tool' -> 'scrape\_web\_page\_tool'. 
 
what is a good way to ensure it happens in this order? is it even possible to do well?  
Example prompt for this scena
rio could be: 'Please download the best web page about pasta' or something of this sort.  
  
Also if I should do someth
ing else completely to achieve my goal it would be good to hear it.

about combining the tools to one tool, this won't r
eally do, since the first should be useable without the second one.

I'm, super new to all the AI Agent stuff so please 
be kind to a newbie!  
it's just an example scenario I'm working on something else entirely, thanks in advance for all a
nd any help! :D
```
---

     
 
all -  [ Can someone critique my resume? I've been applying the tips handed out around here. ](https://www.reddit.com/r/PHJobs/comments/1gsmsr4/can_someone_critique_my_resume_ive_been_applying/) , 2024-11-17-0914
```
[Page 1](https://preview.redd.it/5e25wt4uh91e1.png?width=604&format=png&auto=webp&s=f4b1e890b053ddd061a34fd368283438c0a4
3e5b)

[Page 2 \(Neglible tbh\)](https://preview.redd.it/basy849wh91e1.png?width=611&format=png&auto=webp&s=0ab0753fd6fb
3dcfcc6916bad7e10862609a7bbc)


```
---

     
 
all -  [ LangSec: A Security Framework for Text-to-SQL ](https://www.reddit.com/r/LangChain/comments/1gskn0q/langsec_a_security_framework_for_texttosql/) , 2024-11-17-0914
```
Concerned about security when using Text-to-SQL? We were too. That's why we created **langsec**, an open-source Python p
ackage that lets you define security schemas to enforce and validate LLM-generated SQL queries. Easy to integrate with y
our existing code.

[https://github.com/langsec-ai/langsec](https://github.com/langsec-ai/langsec)

If you find it usefu
l, please leave us a ⭐!
```
---

     
 
all -  [ Breaking down Complex Queries into sub queries for NL2SQL  ](https://www.reddit.com/r/LangChain/comments/1gsjkyb/breaking_down_complex_queries_into_sub_queries/) , 2024-11-17-0914
```
I am building a lang graph based agentic workflow that converts Natural Language to SQL queries. I am dealing with multi
ple tables with complex relationships. Here I find that certain queries that require sub queries are not correctly gener
ated by the model. Hence I decided to implement an agent that identifies these complex questions and breaks them down in
to smaller questions which the LLM might have a better shot at converting into actual SQL. Any thoughts on how I should 
carry this out? 
```
---

     
 
all -  [ Comprehensive RAG Repo: Everything You Need in One Place ](https://www.reddit.com/r/LangChain/comments/1gsita2/comprehensive_rag_repo_everything_you_need_in_one/) , 2024-11-17-0914
```
For the past 3 months, I’ve been diving deep into building RAG apps and found tons of information scattered across the i
nternet—YouTube videos, research papers, blogs—you name it. It was overwhelming.

So, I created [this repo](https://gith
ub.com/bRAGAI/bRAG-langchain) to consolidate everything I’ve learned. It covers RAG from beginner to advanced levels, sp
lit into 5 Jupyter notebooks:

* Basics of RAG pipelines (setup, embeddings, vector stores).
* Multi-query techniques an
d advanced retrieval strategies.
* Fine-tuning, reranking, and more.

Every source I used is cited with links, so you ca
n explore further. If you want to try out the notebooks, just copy the `.env.example` file, add your API keys, and you'r
e good to go.

Would love to hear feedback or ideas to improve it. (it is still a work in progress and I plan on adding 
more resources there soon!)

*In case the link above does not work here it is:* [*https://github.com/bRAGAI/bRAG-langcha
in*](https://github.com/bRAGAI/bRAG-langchain)

Edit:  
If you’ve found the repo useful or interesting, I’d really appre
ciate it if you could give it a ⭐️ on GitHub. It helps the project gain visibility and lets me know it’s making a differ
ence.

Thanks for your support! 
```
---

     
 
all -  [ Why Are AI Agent Tools So Complex? Thinking of a Simpler Solution ](https://www.reddit.com/r/LangChain/comments/1gshuh5/why_are_ai_agent_tools_so_complex_thinking_of_a/) , 2024-11-17-0914
```
Hey everyone,

I’ve been diving into the world of AI agents lately, and while the potential is *mind-blowing,* I keep hi
tting the same roadblock: complexity. Coming from a non-tech background, I find myself getting lost in technical jargon,
 confusing setups, and interfaces that make me feel like I need a computer science degree just to get started. 😅

I alwa
ys start with excitement but drop off midway because I just can’t figure out how to make these tools work for me. I can’
t be the only one feeling this way, right?

So here’s what I’m thinking: what if there was software that made AI agents 
super easy to use? Imagine being able to set up and deploy an AI agent with just a few simple prompts—no coding, no head
aches.

I’m considering working on something like this to solve this pain point. What do you all think? Are you facing s
imilar challenges, or am I just missing some golden resource that simplifies all this?

Would love to hear your thoughts
, ideas, or even rants about your struggles with AI agents!
```
---

     
 
all -  [ The AI Agents News Time ](https://www.reddit.com/r/AIAgentsDirectory/comments/1gsb32x/the_ai_agents_news_time/) , 2024-11-17-0914
```
The AI Agents News Time:

https://preview.redd.it/cs28pn5bp51e1.png?width=800&format=png&auto=webp&s=751cd7379af51e5ec62
a560f8286c2d871a22f42

1. [Supercog AI](https://www.linkedin.com/company/supercog-ai/) launched a new version that integ
rates into Slack: [https://lnkd.in/gj3GXb3S](https://lnkd.in/gj3GXb3S)
2. [Guardrails AI](https://www.linkedin.com/compa
ny/guardrailsai/) lanched a new cource with [DeepLearning.AI](https://www.linkedin.com/company/deeplearningai/) on how t
o prevent hallucinations, off-topic responses, and data leaks in your LLM applications in 'Safe and Reliable AI via Guar
drails,' taught by [Shreya Rajpal](https://www.linkedin.com/in/shreya-rajpal/), founder of [Guardrails AI](https://www.l
inkedin.com/company/guardrailsai/).https://lnkd.in/gd-YYQnw
3. [airt](https://www.linkedin.com/company/airt-ai/)'s [hash
tag#fastAgency](https://www.linkedin.com/feed/hashtag/?keywords=fastagency&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7
263234310596354049) launched a new Version v0.3.4 is out! What’s new:- basic authentication for [hashtag#Mesop](https://
www.linkedin.com/feed/hashtag/?keywords=mesop&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7263234310596354049) UI- HTTPB
asic security class for [hashtag#OpenAPI](https://www.linkedin.com/feed/hashtag/?keywords=openapi&highlightedUpdateUrns=
urn%3Ali%3Aactivity%3A7263234310596354049)\- docs updated w/usage of [hashtag#cookiecutter](https://www.linkedin.com/fee
d/hashtag/?keywords=cookiecutter&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7263234310596354049) for project setup, and
- automatic deployment to cloud [https://lnkd.in/gJyx9wzh](https://lnkd.in/gJyx9wzh)
4. [CrewAI](https://www.linkedin.co
m/company/crewai-inc/) dropped a new tutorial 'CrewAI Flows: AI Feedback Loop'. where [Brandon Hancock](https://www.link
edin.com/in/brandon-hancock-ai/) covers how to set up a flow that evaluates its outputs, iterates with feedback, and pol
ishes each result until it meets your standardshttps://lnkd.in/gzGTnCv6
5. [Eidolon AI](https://www.linkedin.com/company
/eidolon-ai/) team launched GitHub Assistant to help multi-agent system not only identify why your tests are failing but
 also pinpoints which code needs fixing—all in minutes. [https://lnkd.in/e62\_QYsW](https://lnkd.in/e62_QYsW)
6. [Writer
](https://www.linkedin.com/company/getwriter/) has raised $200 milllion in Series C funding at a valuation of $1.9 billi
on. 🦄 Congrats [May Habib](https://www.linkedin.com/in/may-habib/), [Waseem Alshikh](https://www.linkedin.com/in/waseema
lshikh/) and the teamhttps://lnkd.in/eBfRBfXG
7. [Letta](https://www.linkedin.com/company/letta-ai/) launched a new cour
ce with [DeepLearning.AI](https://www.linkedin.com/company/deeplearningai/) 'LLMs as Operating Systems: Agent Memory', w
here you will learn how to build agents with long-term, persistent memory. Thanks [Charles Packer](https://www.linkedin.
com/in/charles-packer/) and [Sarah Wooders](https://www.linkedin.com/in/wooders/).https://lnkd.in/exdwCz3f
8. [Siva Sure
ndira](https://www.linkedin.com/in/sivasurend/) and [Lyzr AI](https://www.linkedin.com/company/lyzr-platform/) team laun
ched [hashtag#Jazon](https://www.linkedin.com/feed/hashtag/?keywords=jazon&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7
263234310596354049) 2.0: The All New Jazon AI SDR. [https://lnkd.in/eePPS58g](https://lnkd.in/eePPS58g)
9. [Langflow](ht
tps://www.linkedin.com/company/langflow/) announced a major new release 1.1 for agentic-first AI development – a new era
 in agent workflows 🚀✨ Fresh Visuals🤖 Native Agent Component🧰 Every Component as a Tool🎴 Loads of templates! [https://ln
kd.in/eCHGzwGt](https://lnkd.in/eCHGzwGt)
10. [LangChain](https://www.linkedin.com/company/langchain/) released a report
, where they surveyed over 1300 industry professionals— from developers to business leaders — on how they are using AI a
gents in their everyday work, and the results are in.https://lnkd.in/esp-PUwX
11. [Composio](https://www.linkedin.com/co
mpany/composiohq/) launched SWE-kit: The ultimate open-source toolkit for building customized coding agents. SWE-Kit’s p
rimary features include:- Optimized Coding Tools- Browser Interaction Tool- Framework Agnostic- Third-Party Integrations
- Flexible Deployment
12. [David Zhang](https://www.linkedin.com/in/david-zhang-2902462a/) launched a customizable Resea
rch Agents at [Aomni](https://www.linkedin.com/company/aomni/) [https://lnkd.in/eN6btK6x](https://lnkd.in/eN6btK6x)

Let
 me know if I missed your company news.

Interactive AI Agents Market landscape map: [https://lnkd.in/dnC7mh4K](https://
lnkd.in/dnC7mh4K)
```
---

     
 
all -  [ How does langchain transcribe youtube videos ? ](https://www.reddit.com/r/LangChain/comments/1gs7y2v/how_does_langchain_transcribe_youtube_videos/) , 2024-11-17-0914
```
Reaching out to the community, I was wondering how [LangChain](https://www.linkedin.com/company/langchain/) has helper m
odules like from langchain\_community.document\_loaders import YoutubeLoader to allow transcribing of youtube videos, is
 there an agreement between Langchain and youtube to allow this or this is under a non-commercial use-case license ?
```
---

     
 
all -  [ An intelligent document processing platform for generative AI ](https://www.reddit.com/r/instructlab/comments/1gs6eov/an_intelligent_document_processing_platform_for/) , 2024-11-17-0914
```
Learn about [Docling: a new tool to unlock data from enterprise documents for generative AI](https://research.ibm.com/bl
og/docling-generative-AI).


[Another post by Red Hat](https://www.redhat.com/en/blog/docling-missing-document-processin
g-companion-generative-ai), including where and how to use Docling.


## [Features](https://github.com/DS4SD/docling)

*
 🗂️ Reads popular document formats (PDF, DOCX, PPTX, Images, HTML, AsciiDoc, Markdown) and exports to Markdown and JSON

* 📑 Advanced PDF document understanding including page layout, reading order & table structures
* 🧩 Unified, expressive 
DoclingDocument representation format
* 🤖 Easy integration with LlamaIndex 🦙 & LangChain 🦜🔗 for powerful RAG / QA applic
ations
* 🔍 OCR support for scanned PDFs
* 💻 Simple and convenient CLI
```
---

     
 
all -  [ LangGraph Discord server! ](https://www.reddit.com/r/LangChain/comments/1gs46nd/langgraph_discord_server/) , 2024-11-17-0914
```
[https://discord.gg/Agh2mwpN](https://discord.gg/Agh2mwpN)

Hey everyone, it took longer than I expected it to, but I've
 created the Discord server for the LangGraph virtual meetup series. That link will be active for a week and I'll make a
nother one if needed a week from today.

I've got a channel created for the meetup series where I'm hoping we can come t
o some consensus on when the meetings should be for each time zone group. Let me know if that invite link isn't working 
and I'll figure out whatever I did wrong and fix it. Stoked that the ball's rolling on this. :)
```
---

     
 
all -  [ how do I make the langchain based SQL Agent Chatbot understand the underlying business rules when fo ](https://www.reddit.com/r/Langchaindev/comments/1gs1ql0/how_do_i_make_the_langchain_based_sql_agent/) , 2024-11-17-0914
```
There more than 500 tables and more than 1000 of business logics. How do i make this SQL Agent always form the correct S
QL query? Additionally I want this as a chatbot solution, so the response really has to be in few seconds. Can’t let the
 user of the chatbot be waiting for minutes while the chatbot tells me the status of one of my projects from the databas
e. Has anyone worked towards solving such a problem? What do I need to do to make this SQL Agent perfect? Any help is ap
preciated 🙏🏻
```
---

     
 
all -  [ Help Need to run the Hierarchical agent example!! ](https://www.reddit.com/r/LangChain/comments/1gs123j/help_need_to_run_the_hierarchical_agent_example/) , 2024-11-17-0914
```
[https://www.reddit.com/r/LangGraph/comments/1gs0b2p/hierarchical\_agent\_teams\_keyerrornext/?utm\_source=share&utm\_me
dium=web3x&utm\_name=web3xcss&utm\_term=1&utm\_content=share\_button](https://www.reddit.com/r/LangGraph/comments/1gs0b2
p/hierarchical_agent_teams_keyerrornext/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=shar
e_button)

Keep getting the KeyError: 'next'...


```
---

     
 
all -  [ Roadmap for application and the core working of generative AI and LLMs ](https://www.reddit.com/r/LangChain/comments/1grzwig/roadmap_for_application_and_the_core_working_of/) , 2024-11-17-0914
```
I’m a final year undergrad with proficiency in Python. I’m not unbeknownst to deep learning or a few Gen AI components. 
I’ve built really primitive deep learning applications using CNNs and also an RAG pipeline using a locally set up llm th
rough ollama. But my knowledge is pretty superficial, I’d like to get a much better understanding in how they function a
nd in turn use that understanding to hopefully be able to build better applications using them. I’d like to build Agenti
c pipelines or even dive into frameworks like langchain, lang graph etc, fine tune models or even play around with moder
n AI tools like cursor, super maven etc not just simply use them but also try to follow their development and AI news in
 general. Would appreciate a road map to dive into all of this or even suggestions on where and how to get started ?
```
---

     
 
all -  [ Llm for consistent json output or some other method ](https://www.reddit.com/r/LangChain/comments/1grzp7w/llm_for_consistent_json_output_or_some_other/) , 2024-11-17-0914
```
I found that it is quite hard with gpt-4o to keep the json structure consistent for every output, though the artifcat th
ing is completely based on structured output.


How would you make this possible?

My approach:

- change the llm and pr
ompt
- make another llm call to make the response structured. 


What do you say ?
```
---

     
 
all -  [ This week in AI - all the Major AI developments in a nutshell
 ](https://www.reddit.com/r/ArtificialInteligence/comments/1grykgg/this_week_in_ai_all_the_major_ai_developments_in/) , 2024-11-17-0914
```
1. **Alibaba Cloud** released ***Qwen2.5-Coder-32B***, an open-source model for programming tasks that matches the codin
g capabilities of GPT-4o. In addition to this flagship model, four new models have been released, expanding the Qwen2.5-
Coder family to a total of six models, ranging in sizes from 0.5B to 32B. An Artifacts app, similar to the Claude Artifa
cts, has also been launched.
2. **Fixie AI** released ***Ultravox v0.4.1***, a family of multi-modal, open-source models
 trained specifically for enabling real-time conversations with AI. Ultravox does not rely on a separate automatic speec
h recognition (ASR) stage, but consumes speech directly in the form of embeddings. The latency performance is comparable
 to the OpenAI Realtime . Fixie also released Ultravox Realtime, a managed service to integrate real time AI voice conve
rsations into applications \[Details\].
3. **Google** introduced a new model ***Gemini (Exp 1114***), available now in G
oogle AI Studio. It has climbed to joint #1 overall on the Chatbot Arena leaderboard, following over 6K+ community votes
 in the past week. It matches the performance of 4o-latest while surpassing o1-preview and is #1 on Vision leaderboard \
[Details\].
4. **Nexusflow** released ***Athene-V2***, an open source 72B model suite, fine-tuned from Qwen 2.5 72B. It 
includes Athene-V2-Chat matching GPT-4o across multiple benchmark and Athene-V2-Agent, a specialized agent model surpass
ing GPT-4o in function calling and agent applications \[Details\].
5. **Vidu** launched ***Vidu-1.5***, a multimodal mod
el with multi-entity consistency. Vidu-1.5 can seamlessly integrate people, objects, and environments to generate a vide
o \[Link\].
6. Codeium launched Windsurf Editor, an agentic IDE. It introduces ‘Flow’ a collaborative agent that combine
s the collaborative nature of copilots with the ability to be independently powerful like an agent \[Details\].
7. **Res
earchers** introduced ***MagicQuill***, an intelligent interactive image editing system. It uses a multimodal large lang
uage model to anticipate editing intentions in real time, removing the need for explicit prompts \[Details | Demo\].
8. 
**DeepSeek** released ***JanusFlow***, an open-source unified multimodal model that excels at both image understanding &
 generation in a single model. It matches or outperforms specialized models in their respective domains and significantl
y surpasses existing unified models on standard benchmarks \[Details| Demo\].
9. **Google DeepMind** has open-sourced Al
phaFold 3 for academic use. It models interactions between proteins, DNA, RNA, and small molecules. This is vital for dr
ug discovery and disease treatment \[Details\].
10. **Epoch AI** launched ***FrontierMath***, a benchmark for advanced m
athematical reasoning in AI. Developed with over 60 top mathematicians, it includes hundreds of challenging problems, of
 which AI systems currently solve less than 2% \[Details\].
11. TikTok launched Symphony Creative Studio, an AI-powered 
video-generation tool for Business users. Users can turn product information or a URL into a video, add a digital avatar
 to narrate the video script, or localize any existing videos into new languages using translation and dubbing capabilit
ies \[Details\].
12. Nous Research introduced the Forge Reasoning API Beta. It lets you take any model and superpower it
 with a code interpreter and advanced reasoning capabilities. Hermes 70B x Forge is competitive with much larger models 
from Google, OpenAI and Anthropic in reasoning benchmarks \[Details\].
13. Anthropic added a new prompt improver to the 
Anthropic Console. Take an existing prompt and Claude will automatically refine it with prompt engineering techniques li
ke chain-of-thought reasoning \[Details\].
14. Nvidia present Add-it, a training-free method for adding objects to image
s based on text prompts. Add-it works well on real and generated images. It leverages an existing text-to-image model (F
LUX.1-dev) without requiring additional training \[Details\].
15. Microsoft released TinyTroupe, an experimental Python 
library for simulation of people with specific personalities, interests, and goals. These artificial agents - TinyPerson
s - can listen to us and one another, reply back, and go about their lives in simulated TinyWorld environments. This is 
achieved by leveraging the power of Large Language Models (LLMs), notably GPT-4, to generate realistic simulated behavio
r \[Details\].
16. Johns Hopkins researchers trained a surgical robot by having it watch videos of skilled surgeons. Usi
ng imitation learning, the robot learned complex tasks like suturing and tissue handling, ultimately performing with ski
ll comparable to human doctors \[Details\[.
17. Stripe launched a SDK built for AI agents - LLMs can call payment, billi
ng, issuing, etc APIs. It natively supports Vercel’s AI SDK, LangChain, and CrewAI, and works with any LLM provider that
 supports function calling \[Details\].
18. Researchers released OpenCoder, completely open-source and reproducible code
 LLM family which includes 1.5B and 8B base and chat models. Starting from scratch, OpenCoder is trained on 2.5 trillion
 tokens and built on the transparent data process pipeline and reproducible dataset. It achieves top-tier performance on
 multiple code LLM evaluation benchmarks \[Details\[.
19. Alibaba launched Accio, an AI search engine for small business
es to find wholesale products alongside the analysis on their popularity with consumers and projected profit. Accio is p
owered by Alibaba’s Tongyi Qianwen large language model \[Details\].
20. Anthropic released RapidResponseBench, a benchm
ark that evaluates how well LLM defenses can adapt to and handle different jailbreak strategies after seeing just a few 
examples \[GitHub| Paper\].
21. LangChain launched Prompt Canvas, an interactive tool designed to simplify prompt creati
on. Prompt Canvas, the UX inspired from ChatGPT’s Canvas, lets you collaborate with an LLM agent to iteratively build an
d refine your prompts \[Details\].
22. LangChain released Promptim, an experimental open-source library for prompt optim
ization. Promptim automates the process of improving prompts on specific tasks. You provide initial prompt, a dataset, a
nd custom evaluators (and optional human feedback), and promptim runs an optimization loop to produce a refined prompt t
hat aims to outperform the original \[Details\]. 
23. Apple’s Final Cut Pro 11 with AI-powered features now available \[
Details\].
24. ChatGPT app for Mac is now able to integrate with coding apps like Xcode, VS Code, TextEdit, and Terminal
 \[Details\].

**Source:** AI Brews - Links removed from this post due to auto-delete, but they are present in the [news
letter](https://aibrews.com/). it's free to join, sent only once a week with bite-sized news, learning resources and sel
ected tools. Thanks!
```
---

     
 
all -  [ This week in AI - all the Major AI developments in a nutshell
 ](https://www.reddit.com/r/ChatGPTCoding/comments/1gryf3n/this_week_in_ai_all_the_major_ai_developments_in/) , 2024-11-17-0914
```
1. **Alibaba Cloud** released ***Qwen2.5-Coder-32B***, an open-source model for programming tasks that matches the codin
g capabilities of GPT-4o. In addition to this flagship model, four new models have been released, expanding the Qwen2.5-
Coder family to a total of six models, ranging in sizes from 0.5B to 32B. An Artifacts app, similar to the Claude Artifa
cts, has also been launched.
2. **Fixie AI** released ***Ultravox v0.4.1***, a family of multi-modal, open-source models
 trained specifically for enabling real-time conversations with AI. Ultravox does not rely on a separate automatic speec
h recognition (ASR) stage, but consumes speech directly in the form of embeddings. The latency performance is comparable
 to the OpenAI Realtime . Fixie also released Ultravox Realtime, a managed service to integrate real time AI voice conve
rsations into applications \[Details\].
3. **Google** introduced a new model ***Gemini (Exp 1114***), available now in G
oogle AI Studio. It has climbed to joint #1 overall on the Chatbot Arena leaderboard, following over 6K+ community votes
 in the past week. It matches the performance of 4o-latest while surpassing o1-preview and is #1 on Vision leaderboard \
[Details\].
4. **Nexusflow** released ***Athene-V2***, an open source 72B model suite, fine-tuned from Qwen 2.5 72B. It 
includes Athene-V2-Chat matching GPT-4o across multiple benchmark and Athene-V2-Agent, a specialized agent model surpass
ing GPT-4o in function calling and agent applications \[Details\].
5. **Vidu** launched ***Vidu-1.5***, a multimodal mod
el with multi-entity consistency. Vidu-1.5 can seamlessly integrate people, objects, and environments to generate a vide
o \[Link\].
6. Codeium launched Windsurf Editor, an agentic IDE. It introduces ‘Flow’ a collaborative agent that combine
s the collaborative nature of copilots with the ability to be independently powerful like an agent \[Details\].
7. **Res
earchers** introduced ***MagicQuill***, an intelligent interactive image editing system. It uses a multimodal large lang
uage model to anticipate editing intentions in real time, removing the need for explicit prompts \[Details | Demo\].
8. 
**DeepSeek** released ***JanusFlow***, an open-source unified multimodal model that excels at both image understanding &
 generation in a single model. It matches or outperforms specialized models in their respective domains and significantl
y surpasses existing unified models on standard benchmarks \[Details| Demo\].
9. **Google DeepMind** has open-sourced Al
phaFold 3 for academic use. It models interactions between proteins, DNA, RNA, and small molecules. This is vital for dr
ug discovery and disease treatment \[Details\].
10. **Epoch AI** launched ***FrontierMath***, a benchmark for advanced m
athematical reasoning in AI. Developed with over 60 top mathematicians, it includes hundreds of challenging problems, of
 which AI systems currently solve less than 2% \[Details\].
11. TikTok launched Symphony Creative Studio, an AI-powered 
video-generation tool for Business users. Users can turn product information or a URL into a video, add a digital avatar
 to narrate the video script, or localize any existing videos into new languages using translation and dubbing capabilit
ies \[Details\].
12. Nous Research introduced the Forge Reasoning API Beta. It lets you take any model and superpower it
 with a code interpreter and advanced reasoning capabilities. Hermes 70B x Forge is competitive with much larger models 
from Google, OpenAI and Anthropic in reasoning benchmarks \[Details\].
13. Anthropic added a new prompt improver to the 
Anthropic Console. Take an existing prompt and Claude will automatically refine it with prompt engineering techniques li
ke chain-of-thought reasoning \[Details\].
14. Nvidia present Add-it, a training-free method for adding objects to image
s based on text prompts. Add-it works well on real and generated images. It leverages an existing text-to-image model (F
LUX.1-dev) without requiring additional training \[Details\].
15. Microsoft released TinyTroupe, an experimental Python 
library for simulation of people with specific personalities, interests, and goals. These artificial agents - TinyPerson
s - can listen to us and one another, reply back, and go about their lives in simulated TinyWorld environments. This is 
achieved by leveraging the power of Large Language Models (LLMs), notably GPT-4, to generate realistic simulated behavio
r \[Details\].
16. Johns Hopkins researchers trained a surgical robot by having it watch videos of skilled surgeons. Usi
ng imitation learning, the robot learned complex tasks like suturing and tissue handling, ultimately performing with ski
ll comparable to human doctors \[Details\[.
17. Stripe launched a SDK built for AI agents - LLMs can call payment, billi
ng, issuing, etc APIs. It natively supports Vercel’s AI SDK, LangChain, and CrewAI, and works with any LLM provider that
 supports function calling \[Details\].
18. Researchers released OpenCoder, completely open-source and reproducible code
 LLM family which includes 1.5B and 8B base and chat models. Starting from scratch, OpenCoder is trained on 2.5 trillion
 tokens and built on the transparent data process pipeline and reproducible dataset. It achieves top-tier performance on
 multiple code LLM evaluation benchmarks \[Details\[.
19. Alibaba launched Accio, an AI search engine for small business
es to find wholesale products alongside the analysis on their popularity with consumers and projected profit. Accio is p
owered by Alibaba’s Tongyi Qianwen large language model \[Details\].
20. Anthropic released RapidResponseBench, a benchm
ark that evaluates how well LLM defenses can adapt to and handle different jailbreak strategies after seeing just a few 
examples \[GitHub| Paper\].
21. LangChain launched Prompt Canvas, an interactive tool designed to simplify prompt creati
on. Prompt Canvas, the UX inspired from ChatGPT’s Canvas, lets you collaborate with an LLM agent to iteratively build an
d refine your prompts \[Details\].
22. LangChain released Promptim, an experimental open-source library for prompt optim
ization. Promptim automates the process of improving prompts on specific tasks. You provide initial prompt, a dataset, a
nd custom evaluators (and optional human feedback), and promptim runs an optimization loop to produce a refined prompt t
hat aims to outperform the original \[Details\]. 
23. Apple’s Final Cut Pro 11 with AI-powered features now available \[
Details\].
24. ChatGPT app for Mac is now able to integrate with coding apps like Xcode, VS Code, TextEdit, and Terminal
 \[Details\].

**Source:** AI Brews - Links removed from this post due to auto-delete, but they are present in the [news
letter](https://aibrews.com/). it's free to join, sent only once a week with bite-sized news, learning resources and sel
ected tools. Thanks!


```
---

     
 
all -  [ A simple alternative to LangChain for lazy developers / noobs ](https://www.reddit.com/r/LangChain/comments/1grxowm/a_simple_alternative_to_langchain_for_lazy/) , 2024-11-17-0914
```
Hi everyone, 

I'm what you might call a “novice” developer. My company has some AI needs, so I'm looking for a solution
 that lets me orchestrate some AI models, add prompts when generating text, and connect to some data. It's pretty simple
 stuff, I think. 

I know how to code a little in Python, but I don't understand much about LangChain, which seems to me
 to be for developers with a little experience (or maybe I'm just too dumb).

I've come across a platform that seems to 
meet my needs. It's called Eden AI (www.edenai.co). They bundle lots of AI APIs into one, and then recently they've made
 it possible to create your own custom AI API with a visual workflow. You can then make an API call on this workflow. 


But before using this in more depth, I'd like to hear your feedback. Has anyone used this? Do you have any alternatives 
for me?

Cheers
```
---

     
 
all -  [ Just kicked off my AgentCraft Hackathon with LangChain - here are the expert sessions! (recordings a ](https://open.substack.com/pub/diamantai/p/agentcraft-hackathon-kickoff-world?r=336pe4&utm_campaign=post&utm_medium=web) , 2024-11-17-0914
```
Just hosted the kickoff for my company DiamantAI's AgentCraft hackathon with LangChain. Recorded some amazing sessions w
ith experts sharing the latest in AI agent development:

* Lance Martin from LangChain introduced LangGraph - a new fram
ework for building reliable AI agents

* Monday.com's AI head demonstrated GPT-Researcher (15K GitHub stars) - multi-age
nt research assistant with 40% quality improvement 

* Microsoft demoed Azure AI Studio with $200 free credits + up to $
150K for startups

* Dynamiq CEO showcased their enterprise orchestration platform reducing ticket processing by 50%

* 
CopilotKit CEO showed how to build sophisticated AI apps with human-in-loop workflows

Full recordings and resources are
 available in the link attached.

Let me know if you have any questions about the sessions or hackathon!
```
---

     
 
all -  [ LangGraph Human In The Loop – JavaScript implementation ](https://www.reddit.com/r/LangChain/comments/1grvmrz/langgraph_human_in_the_loop_javascript/) , 2024-11-17-0914
```
Wrote a small article on how to add Human In The Loop for AI Agents using LangGraph  [https://www.js-craft.io/blog/langg
raph-human-loop-javascript/](https://www.js-craft.io/blog/langgraph-human-loop-javascript/). Any feedback is welcomed. 
```
---

     
 
all -  [ Built llmtest: A Semantic Testing Framework for LLMs (Need Senior Engineering Help!) ](https://www.reddit.com/r/LangChain/comments/1grtaol/built_llmtest_a_semantic_testing_framework_for/) , 2024-11-17-0914
```
Hey r/langchain! I've built something I think could be really useful, but I need senior engineering help to make it prod
uction-ready. I'm a programming noob, only been writing code for 20 months. It is at an extremely early stage but I thin
k the idea has potential.

What is llmtest?

A semantic testing framework that uses LLMs to validate semantic equivalenc
e in test outputs. Instead of exact matching (which doesn't work with LLM outputs), it uses LLMs themselves to check if 
outputs are semantically equivalent.

Why I Built It

I got frustrated with not being able to properly test LLM applicat
ions (I don't trust my code, and I trust LLMs even less). I thought 'If we need to validate semantic meaning, why not us
e an LLM to do it?' So I built a basic framework that does exactly that.

Current State

Here's a basic example:

`from 
llmtest.core.semantic_assert import SemanticAssertion`

`def test_my_llm_function(asserter):`

`result = my_llm_function
()`  
`asserter.assert_semantic_match(actual=result,`  
`expected_behavior='Should provide a coherent answer`  
`about P
ython')`

Why I Need Help

While I've got a working test (I think, it passed the test for the test in the test package b
ecause the only way to make tests good is to write tests to test your tests) and basic functionality, I'm relatively new
 to programming and need senior engineering guidance to make this production-ready. Looking for experienced engineers wh
o can:

1. Help lead the technical direction
2. Guide architecture decisions
3. Implement best practices
4. Make this pr
oduction-ready

Why This Matters

Every LLM application needs semantic testing, but current solutions either:

* Use exa
ct matching (doesn't work)
* Use complex metrics (hard to implement)
* Don't address semantic equivalence directly

Curr
ent Features

* Semantic equivalence testing using GPT-4o
* pytest integration
* Basic error handling
* Environment-base
d configuration

Links

* GitHub: [https://github.com/Shredmetal/llmtest](https://github.com/Shredmetal/llmtest)

Would 
love to connect with senior engineers who:

1. See the potential in this approach
2. Want to help shape the future of LL
M testing
3. Are interested in mentoring while building something useful

I'm happy to remain an active core contributor
 while learning from more experienced developers (I'm way in over my head here!).

Edit:

Someone asked how it worked so
:

For me now, testing an LLM app for me involves spinning the LLM service up, spinning up a frontend, and talking to th
e bot. The idea is to take me out of the equation.

What do I do when I talk to the bot? I expect a particular type of r
esponse based on the system message / any other templates I use.

I thought that this thought process can be replicated 
by an LLM (however it does it, thought or not).

So this testing package:

1. Takes your LLM app output
2. Takes the exp
ected behaviour
3. Gives it to an LLM to check if it matches semantically
4. Gets the response from the LLM whether PASS
 or FAIL + reason for failure
5. Then raises an error or doesn't raise an error.

For example (these are test cases from
 the tests for my semantic assertion test):

This test correctly does not throw any semantic assertion error:

        d
ef test_basic_semantic_match(self, asserter):
            '''Test basic semantic matching'''
            actual = 'The s
ky is blue'
            expected = 'A statement about the color of the sky'
    
            asserter.assert_semantic_ma
tch(actual, expected)

This test successfully throws an assertion error:

        def test_semantic_mismatch(self, asser
ter):
            '''Test semantic mismatch raises correct exception'''
            actual = 'The sky is blue'
         
   expected = 'A statement about the weather forecast'
    
            with pytest.raises(SemanticAssertionError) as ex
cinfo:
                asserter.assert_semantic_match(actual, expected)
    
            assert 'Semantic assertion fail
ed' in str(excinfo.value)

For the attached images, the LLM was asked to generate:

`'''You are a friendly greeting bot.
 Your task is to generate`

`warm, personalized greetings. The greeting should:`

`1. Use the person's name`

`2. Be fri
endly and welcoming`

`3. Include a question about their wellbeing`

`4. Keep responses concise (max 2 sentences)'''`

T
his was the expected behavior:

    '''
    A polite greeting that:
    1. Addresses the person by name (Alice)
    2. A
sks about their wellbeing
    '''

Please refer to the attached images - the testing behaved as expected.

[Test failure
 because the expected behaviour did not match the actual behaviour \(The LLM greeted Alice instead of John, which was wh
o the testing LLM was told to expect\)](https://preview.redd.it/cen4ntnvk21e1.jpg?width=1509&format=pjpg&auto=webp&s=e12
d6a5e943e700af4de24eef93ccf4789e11b3f)

[The test passed because the actual content semantically matched the expected co
ntent.](https://preview.redd.it/rqtqxm1wk21e1.jpg?width=668&format=pjpg&auto=webp&s=397e9d2be72f2ec3d6206e74ba644f5178a4
a59b)
```
---

     
 
all -  [ PDF RAG Chain for me or PDF RAG Agent for me ? ](https://www.reddit.com/r/Rag/comments/1grqdyy/pdf_rag_chain_for_me_or_pdf_rag_agent_for_me/) , 2024-11-17-0914
```
Hi guys,  
I'm learning AI and currently working on a RAG project using complex pdfs ( by complex I mean pdfs that conta
ins texts , images, and tables ).

I'm using gpt-4o-mini as the LLM coz its cheap. Currently, I'm just focusing on text 
and table extraction and QA .

My RAG Pipeline looks something like this :

1. Llamaparse to convert PDF to Markdown
2. 
OpenAIEmbedding 3 Large for converting pdf chunks to vectors
3. Pinecone as Vector Store
4. Cohere ( rerank-english-v3.0
 ) as Reranker

I've created the setup using create\_history\_aware\_retriever, create\_retrieval\_chain, RunnableWithMe
ssageHistory classes from Langchain. So, my app is currently a PDF RAG chain.

I'm facing some problems in my current se
tup.

1. Because my pdf has tables, some of the tables are present in a single page only and are getting extracted as ta
ble properly. Others are splitted between pages. This is resulting in incorrect answers. How do I fix this ?
2. When I a
sk the app to calculate sum of column values of a table, it is not able to do so. GPT 4o-mini can reason and do mathemat
ical calculations, why my app can't ?
3. I've added in system prompt to always return tables in tabular format but still
 I get table data in list format around 20-25% of the time.

How can I fix these problems in my app? Is this time to swi
tch to a PDF ReAct agent ( Langgraph ) ?

I've posted this in Langchain subreddit too as I'm using Langchain, posting he
re as I'm developing a RAG app. Hope you guys don't mind. Thanks!
```
---

     
 
all -  [ PDF RAG Chain for me or PDF RAG Agent for me ? ](https://www.reddit.com/r/LangChain/comments/1grqcwn/pdf_rag_chain_for_me_or_pdf_rag_agent_for_me/) , 2024-11-17-0914
```
Hi guys,  
I'm learning AI and currently working on a RAG project using complex pdfs ( by complex I mean pdfs that conta
ins texts , images, and tables ).

I'm using gpt-4o-mini as the LLM coz its cheap. Currently, I'm just focusing on text 
and table extraction and QA .

My RAG Pipeline looks something like this :

1. Llamaparse to convert PDF to Markdown
2. 
OpenAIEmbedding 3 Large for converting pdf chunks to vectors
3. Pinecone as Vector Store
4. Cohere ( rerank-english-v3.0
 ) as Reranker

I've created the setup using create\_history\_aware\_retriever, create\_retrieval\_chain, RunnableWithMe
ssageHistory classes from Langchain. So, my app is currently a PDF RAG chain.

I'm facing some problems in my current se
tup.

1. Because my pdf has tables, some of the tables are present in a single page only and are getting extracted as ta
ble properly. Others are splitted between pages. This is resulting in incorrect answers. How do I fix this ?
2. When I a
sk the app to calculate sum of column values of a table, it is not able to do so. GPT 4o-mini can reason and do mathemat
ical calculations, why my app can't ?
3. I've added in system prompt to always return tables in tabular format but still
 I get table data in list format around 20-25% of the time.

How can I fix these problems in my app? Is this time to swi
tch to a PDF ReAct agent ( Langgraph ) ?



EDIT : System prompt that I'm using

                system_prompt = '''You 
are a specialized document analysis assistant designed to provide precise answers by synthesizing information from table
s, structured text, and visual elements within provided PDF documents, with advanced capabilities for mathematical calcu
lations and reasoning.
    
    When responding to questions:
    
    1. *Table Data Analysis:*
       - Extract exact 
numerical values and relationships from tables, maintaining the structure
       - ALWAYS Format table data to display i
n a tabular layout
       - Specify table titles and numbers to clearly identify sources
       - Include any footnotes 
or special notations, ensuring data context remains intact
       - For mathematical operations on table data:
         
* First display the relevant table data being used
         * Show each mathematical step separately with clear labels
 
        * Include subtotals for complex calculations
         * Validate results by cross-checking across different tabl
es if applicable
    
    2. *Mathematical Reasoning and Calculations:*
       - For any calculation, follow these steps
:
         1. Clearly state the mathematical problem to be solved
         2. List all relevant values and their sources
 (page numbers, table numbers)
         3. Show each calculation step with explanations
         4. Use proper mathemati
cal notation and units
         5. Provide intermediate results for complex calculations
         6. Double-check calcul
ations and show verification steps
         7. Present the final result with appropriate context
       - When performin
g calculations across multiple tables:
         * First organize all relevant data in a structured format
         * Sho
w relationships between different data sources
         * Explain any assumptions or data transformations
         * Val
idate consistency of units and formats before calculations
    
    3. *Visual Content Interpretation:*
       - Describ
e data shown in charts and graphs with details on values, trends, and patterns
       - Reference relevant axis labels, 
legends, and scales
       - Extract numerical data from graphs for calculations when needed
       - Show mathematical 
relationships between visual data points
       - Summarize findings with direct connections to related text for holisti
c insight
    
    4. *Textual Information:*
       - Cite sections and page numbers when quoting or referencing text
  
     - Organize text data with original formatting, including bullet points, numbered lists, and paragraph structures
  
     - Note any footnotes or cross-references, ensuring information is captured in its hierarchical order
       - Extra
ct numerical information from text for calculations when relevant
    
    *Response Format Guidelines:*
    - Identify 
source elements (table, text, or visual) at the beginning of responses
    - For tables: Display data in a table format 
for readability
    - For calculations:
      * Use markdown code blocks for showing calculation steps
      * Format ma
thematical equations clearly
      * Include units in each step
      * Show intermediate results
    - For text: Retain
 PDF-style formatting, using bullets or lists as found in the document
    - For visuals: Summarize visual data with ref
erences to axes and legends
    - Include precise locations (page numbers, section numbers) for all referenced data
    
- Cross-reference across document elements when relevant, showing interconnections
    - Maintain original data precisio
n, units, and context qualifiers
    
    *For Mathematical Operations:*
    
    Step 1: State the calculation objectiv
e
    Step 2: List source data with references
    Step 3: Show calculation setup
    Step 4: Perform operations step by
 step
    Step 5: Verify results
    Step 6: Present final answer with context
    
    
    If the required information
 cannot be found in the provided PDF content, respond with: 'I cannot locate specific information about this in the prov
ided PDF documents. Please verify if this information is present in the documents or rephrase your question.'
    
    Y
ou may respond to basic greetings, but for all other queries, strictly use information from the provided documents.
    

    {context}'''
```
---

     
 
all -  [ Rag and retriever question  ](https://www.reddit.com/r/LangChain/comments/1grojfh/rag_and_retriever_question/) , 2024-11-17-0914
```
Hello everyone, I'd like to ask the community for help with a question. I’m just starting to learn about Artificial Inte
lligence, and I recently built a tutorial guide on how to create a Retrieval-Augmented Generation (RAG) system using Lan
gChain. However, each time I make a query or question, the retriever object is called raising the token usage always, an
d I would love for this call to be optional or called when it's necessary without altering the output structure I've alr
eady set up. Changing the structure of the response would require a lot of adjustments. I'll attach the guide for refere
nce, and I hope my question is clear. Thank you!

https://python.langchain.com/docs/tutorials/rag/
```
---

     
 
all -  [ I am sharing Data Science & AI courses and projects on YouTube ](https://www.reddit.com/r/ChatGPT/comments/1grnymr/i_am_sharing_data_science_ai_courses_and_projects/) , 2024-11-17-0914
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

Data Science
 Full Courses & Projects -> [https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra\_5PGH&si=6WUpVwXeAKEs4tB6](
https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra_5PGH&si=6WUpVwXeAKEs4tB6)

Machine Learning Tutorials ->
 [https://youtube.com/playlist?list=PLTsu3dft3CWhSJh3x5T6jqPWTTg2i6jp1&si=1rZ8PI1J4ShM\_9vW](https://youtube.com/playlis
t?list=PLTsu3dft3CWhSJh3x5T6jqPWTTg2i6jp1&si=1rZ8PI1J4ShM_9vW)

AI Tutorials (ChatGPT, LangChain & LLMs) -> [https://you
tube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN](https://youtube.com/playlist?list=PLTsu3d
ft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ I am sharing Data Science & AI courses and projects on YouTube ](https://www.reddit.com/r/artificial/comments/1grny51/i_am_sharing_data_science_ai_courses_and_projects/) , 2024-11-17-0914
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

Data Science
 Full Courses & Projects -> [https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra\_5PGH&si=6WUpVwXeAKEs4tB6](
https://youtube.com/playlist?list=PLTsu3dft3CWiow7L7WrCd27ohlra_5PGH&si=6WUpVwXeAKEs4tB6)

Machine Learning Tutorials ->
 [https://youtube.com/playlist?list=PLTsu3dft3CWhSJh3x5T6jqPWTTg2i6jp1&si=1rZ8PI1J4ShM\_9vW](https://youtube.com/playlis
t?list=PLTsu3dft3CWhSJh3x5T6jqPWTTg2i6jp1&si=1rZ8PI1J4ShM_9vW)

AI Tutorials (OpenAI, LangChain & LLMs) -> [https://yout
ube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN](https://youtube.com/playlist?list=PLTsu3df
t3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ LLM Development Tech-Stack ](https://www.reddit.com/r/LangChain/comments/1gri6f7/llm_development_techstack/) , 2024-11-17-0914
```
I've been working in AI development for a while now, first at FAANG, and now in startups. IMO, when architecting your LL
M application, you need to optimize for being able to iterate quickly.



LLM Development involves being able to constan
tly try out different prompts, models, call-chaining, RAG datasets, and more to see what works. This requires a tech-sta
ck that helps you efficiently try out different combinations. That’s why I’m working on an open-source framework, Palico
, that optimizes for the iterative nature of LLM Development.



Palico is an opinionated framework that gives you an in
tegrated system for building, evaluating, and deploying your LLM Application. The “opinionated” part of the framework ba
kes in best-practices I’ve seen by talking to hundreds of LLM Devs, as well as my experience working in AI for the last 
few years.



You can checkout the framework here: [https://github.com/palico-ai/palico-ai](https://github.com/palico-ai
/palico-ai)



Would love any feedback!
```
---

     
 
all -  [ AI Agent Stack  ](https://www.reddit.com/r/LangChain/comments/1grhpfz/ai_agent_stack/) , 2024-11-17-0914
```
Hi all - recently I got triggered by seeing the the Nth “AI agent stack”/”AI agents market map” made by a VC features a 
bunch of companies I’ve never heard up in categories that make no sense. [Sharing what I see as the real “agents stack”]
(https://www.letta.com/blog/ai-agents-stack), from the perspective of having been building an agents framework and worki
ng with a lot of different providers for components like LLMs, tool calling, storage, and sandboxing.

https://preview.r
edd.it/mehxo2w55y0e1.jpg?width=5100&format=pjpg&auto=webp&s=5e684f8f64485a551e22557ed0f1effd3cd9cd7e

In my opinion, tod
ay’s tech stack for building AI agents into three key layers: (1) agent hosting/serving, (2) agent frameworks, (3) LLM m
odels & storage.

The (3) LLM model and storage layer is now relatively static - I don’t see a lot of new players, and t
here are clear winners in segments of the market.

For (2) agent frameworks, there’s been a ton of development in the pa
st 6 months in both general purpose frameworks, as well as specialized components (e.g. tool-use, sandboxing, and memory
). I think as the space matures we’ll see a lot more players here, and even more specialization - over time, agents will
 probably be built from modular components leveraging different providers.

The layer of the stack thats still the most 
“up in the air” is hosting (1) - different frameworks have taken very different approaches to what a hosted agent should
 look like, from how agent state (e.g. memories, message history, user data, etc.) are persisted, the API for interactin
g with agents is, and approach to handling tool execution (arbitrary code the agent can call).

I'm sure I missed come c
ool projects, so would love to learn if there's other agent hosting/tool frameworks out there since it was quite sparse 
when we did our research. 
```
---

     
 
all -  [ Scaling issue  ](https://www.reddit.com/r/LangChain/comments/1grhle1/scaling_issue/) , 2024-11-17-0914
```
Hi, I’m a bit new to the LLM sphere. I’m creating software that a lot of users will use, for instance with GPT-4. My und
erstanding is that, since I’m using only one API key, there’s a token limit. I was wondering, how do other companies sca
le when they might have thousands of users? Do they get an API key for each user, or how does that work?
```
---

     
 
all -  [ Why use LangChain?  ](https://www.reddit.com/r/LangChain/comments/1greyeu/why_use_langchain/) , 2024-11-17-0914
```
Genuinely don't know the answer. I've built agents that call functions and retrieve information, multi-agent systems tha
t work together to execute tasks involving conversing with a user. It's just not clear to me why LangChain is better tha
n just using the API's directly. Does it just give you abstractions that require less code? How much less code? Does it 
give new features that you don't get with openai/anthropic API's? Appreciate any insights. I'm coding in python, in case
 makes a difference
```
---

     
 
all -  [ Arch 0.1.2 released 🎉 - AI-native, open source infrastructure to build agents ](https://www.reddit.com/r/LangChain/comments/1grduug/arch_012_released_ainative_open_source/) , 2024-11-17-0914
```
[https://github.com/katanemo/arch](https://github.com/katanemo/arch) \- is an AI-native infrastructure primitive to buil
d fast, personalized agents using APIs. Specifically, Arch is an intelligent prompt gateway designed to protect, observe
, and personalize LLM applications (agents, assistants, co-pilots) with your APIs.

Engineered with purpose-built LLMs, 
Arch handles the critical but undifferentiated tasks related to the handling and processing of prompts, including detect
ing and rejecting [jailbreak](https://github.com/verazuo/jailbreak_llms) attempts, intelligently calling 'backend' APIs 
to fulfill the user's request represented in a prompt, routing to and offering disaster recovery between upstream LLMs, 
and managing the observability of prompts and LLM interactions in a centralized way.

Arch is built on (and by the core 
contributors of) [Envoy Proxy](https://www.envoyproxy.io/) with the belief that:

>

**Core Features**:

* Built on [Env
oy](https://envoyproxy.io): Arch runs alongside application servers, and builds on top of Envoy's proven HTTP management
 and scalability features to handle ingress and egress traffic related to prompts and LLMs.
* Function Calling for fast 
Agents and RAG apps. Engineered with purpose-built [LLMs](https://huggingface.co/collections/katanemo/arch-function-66f2
09a693ea8df14317ad68) to handle fast, cost-effective, and accurate prompt-based tasks like function/API calling, and par
ameter extraction from prompts.
* Prompt [Guard](https://huggingface.co/collections/katanemo/arch-guard-6702bdc08b889e4b
ce8f446d): Arch centralizes prompt guardrails to prevent jailbreak attempts and ensure safe user interactions without wr
iting a single line of code.
* Traffic Management: Arch routes outbound LLM calls to OpenAI (and other LLMs), offering s
mart retries, automatic cutover, and resilient upstream connections for continuous availability.
* Standards-based Obser
vability: Arch uses the W3C Trace Context standard to enable complete request tracing across applications, ensuring comp
atibility with observability tools, and provides metrics to monitor latency, token usage, and error rates, helping optim
ize AI application performance.
```
---

     
 
all -  [ Prove me wrong - An agent is just a convenient abstraction over an LLM ](https://www.reddit.com/r/LangChain/comments/1grcjpa/prove_me_wrong_an_agent_is_just_a_convenient/) , 2024-11-17-0914
```
Hi!

I have not been convinced yet that 'agents' provide any inherent value themselves other than providing a wrapper ar
ound LLMs that contain some state (prompts, context, etc) and/or logic (call back functions otherwise called 'tools'). B
efore agents were released, we were all writing classes that encapsulated this state/logic - a typical exercise to perfo
rm around any model. 

The hype definitely helped push the industry forward while there was slowing progress in terms of
 base models, however, I am reluctant to take a dependency on any new 'agents' framework into my code base when we can a
chieve the same results with little work. 
```
---

     
 
all -  [ How can I parallelize nodes in LangGraph without having to wait for the slowest one to finish if it' ](https://www.reddit.com/r/LangChain/comments/1grchuz/how_can_i_parallelize_nodes_in_langgraph_without/) , 2024-11-17-0914
```
I'm trying to run multiple nodes in parallel to reduce latency but don't want to have to wait for all nodes to finish if
 I determine from early ones that finish that I don't need all of them.

Here's a simple graph example to illustrate the
 problem. It starts with 2 nodes in parallel: setting a random number and getting city preference from some source. If t
he random number is 1-50, 'NYC' is assigned as city regardless of city preference, but if random number is 51-100, the c
ity preference is used.

    class State(TypedDict):
        random_number: int
        city: str
        city_preferenc
e: str
    
    graph: StateGraph = StateGraph(state_schema=State)
    
    
    def set_random_number(state):
        r
andom_number = 1  # Hardcode to 1 for testing
        print(f'SET RANDOM NUMBER: {random_number}')
        return {'rand
om_number': random_number}
    
    
    def get_city_preference(state):
        time.sleep(4)  # Simulate a time-consum
ing operation
        city_preference = 'Philadelphia'
        print(f'GOT CITY PREFERENCE: {city_preference}')
        
return {'city_preference': city_preference}
    
    
    def assign_city(state):
        city = 'NYC' if state['random_
number'] <= 50 else state['city_preference']
        print(f'ASSIGNED CITY: {city}')
        return {'city': city}
    

    
    graph.add_node('set_random_number', set_random_number)
    graph.add_node('get_city_preference', get_city_prefe
rence)
    graph.add_node('assign_city', assign_city)
    
    graph.add_edge(START, 'set_random_number')
    graph.add_
edge(START, 'get_city_preference')
    graph.add_edge('set_random_number', 'assign_city')
    graph.add_edge('get_city_p
reference', 'assign_city')
    graph.add_edge('assign_city', END)
    
    graph_compiled = graph.compile(checkpointer=M
emorySaver())
    
    input = {'random_number': 0, 'city': 'Nowhere', 'city_preference': 'N/A'}
    config = {
        
'configurable': {'thread_id': 'test'},
        'recursion_limit': 50,
    }
    state = graph_compiled.invoke(input=inpu
t, config=config)
    
    

The problem with the above and various conditional edge implementations I've tried, is that
 the graph always waits to assign city until the slow get\_city\_preference node completes even if the set\_random\_numb
er node has already returned a number that doesn't require city preference (i.e., 1-50).

Is there a way to stop a node 
running in parallel from blocking execution of subsequent nodes if that node's output isn't needed later in the graph?
```
---

     
 
all -  [ Langsmith API Keys. Per project or Per Workspace? ](https://www.reddit.com/r/LangChain/comments/1gra9h9/langsmith_api_keys_per_project_or_per_workspace/) , 2024-11-17-0914
```
Apologies if this is a dumb/beginner question.

I'm trying to change the project my traces are being sent to dynamically
. I'm working with a Typescript project. As far as I'm aware I can only set my LANGCHAIN\_API\_KEY once in my .env file,
 but each project I create gives me a different key. Am I able to update the API Key at the same point I decide which pr
oject name to choose? Am I supposed to use the API Key for my workspace (I tried this and it doesn't seem to work).

Bas
ically it seems I need to dynamically set the project name and project API key. I can set the project name in the  trace
able function but I'm not sure how to do the api key or if I'm misunderstanding and dont need to.
```
---

     
 
all -  [ How to duplicate chroma db or persist directory  ](https://www.reddit.com/r/LangChain/comments/1gr8e7u/how_to_duplicate_chroma_db_or_persist_directory/) , 2024-11-17-0914
```
Need to create Mutiple chroma db based on the same documents.
Tried to copy the persist directory, but the vector db cre
ated from copied directory is always empty
```
---

     
 
all -  [ Production RAG for CSV/Excel  ](https://www.reddit.com/r/LangChain/comments/1gr7msw/production_rag_for_csvexcel/) , 2024-11-17-0914
```
Hi,

I am trying to implement a CSV/Excel RAG using Langchain. Intially implemented using csvgent from langchaain. But t
his time I want it for production environment.

What is the best approach for implementing CSV RAG,  text-to-sql, or by 
Graph RAG, or any other approaches. 

Thanks
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-17-0914
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-17-0914
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
