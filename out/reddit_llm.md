 
all -  [ LangGraph: The Core of LangChain's Knowledge Representation ](https://youtu.be/0aSF7pFCIRM) , 2024-12-11-0914
```

```
---

     
 
all -  [ Best practices for rag ](https://www.reddit.com/r/LLMDevs/comments/1hbes3d/best_practices_for_rag/) , 2024-12-11-0914
```
Hi llmdevs! Any suggestions on best practices for rag? For a beginner? I have been playing around with rag for about a m
onth now, and what all knowledge i have so far is what is given by openai and Claude that helped me with my project. I a
m not getting desired results back so iam assuming there are issues with my setup.

I've tried llamaindex and langchain 
and their default chucking embedding tools (along with custom chucking with cosine similarity as suggested by openai). A
nd worked with faiss and qdrant so far as my vector stores along with llama various versions and openai.

My use case ha
s to do with public sec filings (and one day private financial data from my company, if my setup works).

If it were you
, how would go about setting up the stack? Any help is greatly appreciated. Will answer any missing pieces of informatio
n. 
```
---

     
 
all -  [ Need help: Infinite Loop on RNEventSource with Server-Sent Events (SSE) - Only Receiving “attempt: 1 ](https://www.reddit.com/r/reactnative/comments/1hbepuo/need_help_infinite_loop_on_rneventsource_with/) , 2024-12-11-0914
```
I am working on a React Native expo managed project using RNEventSource to handle Server-Sent Events (SSE) from a langch
ain endpoint. My backend is correctly streaming data (confirmed via Postman), but the frontend gets stuck in an infinite
 loop of the same response, only receiving:

    LOG  Open SSE connection.
    LOG  Stream Data: {'attempt': 1, 'run_id'
: '1efb7463-0ff8-60c3-bd10-17ccc210899f'}
    WARN  Unexpected Data: {'run_id':'1efb7463-0ff8-60c3-bd10-17ccc210899f','a
ttempt':1}
    LOG  Stream Data: {'attempt': 1, 'run_id': '1efb7463-0ff8-60c3-bd10-17ccc210899f'}
    WARN  Unexpected D
ata: {'run_id':'1efb7463-0ff8-60c3-bd10-17ccc210899f','attempt':1'}
    ...

Code:  


    const askDogy = async (reques
t) => {
      const url = `${assitantBaseUrl}/threads/${threadId}/runs/stream`
      const requestBody = JSON.stringify(
{
        assistant_id: assistantID,
        input: {
          messages: [{ role: 'user', content: request }],
        
},
        stream_mode: ['messages'],
      })
    
      const options = {
        body: requestBody,
        method: '
POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'text/event-stream',
        }
,
      }
    
      eventSourceRef.current = new RNEventSource(url, options)
    
      eventSourceRef.current.addEvent
Listener('open', () => {
        console.log('Open SSE connection.')
      })
    
      eventSourceRef.current.addEvent
Listener('message', (event) => {
        console.log('Raw Event:', event)
        try {
          const data = JSON.pars
e(event.data)
          console.log('Parsed Data:', data)
    
          if (data.content) {
            console.log('AI
 Reply Content:', data.content)
            setChatResponse('Bot', data.content, true)
          } else {
            co
nsole.warn('Unexpected Data:', data)
          }
        } catch (error) {
          console.error('Error parsing event 
data:', error)
        }
      })
    
      eventSourceRef.current.addEventListener('error', (error) => {
        conso
le.error('Stream error:', error)
    
            if (error.status === 409) {
              console.log('Conflict detect
ed, creating a new thread...')
              // Create a new thread and retry
              tempThreadId = await createT
hread()
              if (!tempThreadId)
                throw new Error('Failed to create a new thread after conflict')

              setThreadId(tempThreadId)
    
              // Retry the stream with the new thread ID
              con
sole.log('Retrying with new thread ID:', tempThreadId)
              await askDogy(request) // Recursive call with the n
ew thread
            } else {
              handleStopStream()
            }
      })
    }

  
**Debugging Observation
s:**

* I receive the same attempt: 1 data repeatedly with no progress.
* The backend should send incremental updates, b
ut the frontend logs do not show progress.

**Questions:**

* Is there a known issue with RNEventSource or its compatibi
lity with React Native?
* Could there be something specific I need to handle in RNEventSource to parse incremental updat
es?
* Any other npm package/library I can use to handle server sent events in react native/expo?

**Things I've tried:**


* Verified backend compliance with the SSE spec.
* Ensured RNEventSource initialization includes proper headers and me
thod.
* Added maximum retries and timeout logic in case of backend failures (now removed).
* Tested backend with Postman
 and it streams correctly.

  
Thanks in advance. Link to [stackoverflow post](https://stackoverflow.com/questions/79270
017/infinite-loop-on-rneventsource-with-server-sent-events-sse-only-receiving-a)
```
---

     
 
all -  [ [For Hire] Experienced AI/Full Stack & DevOps Developer – Seeking Challenging, High-Impact Projects! ](https://www.reddit.com/r/forhire/comments/1hbbhib/for_hire_experienced_aifull_stack_devops/) , 2024-12-11-0914
```
🚀 **Your All-in-One Solution for AI/ML, Full Stack Development, and DevOps!**

👋 Hi, I’m Sheryar, an experienced AI/ML E
ngineer, Full Stack Developer, and DevOps Specialist. I’m here to help turn your ideas into scalable, high-performance s
olutions!

💻 **Full Stack Development Expertise**  
🔹 Stunning UIs: React/Angular  
🔹 Robust APIs: Node.js, NestJS  
🔹 S
eamless Payment Integration: Stripe  
🔹 Cloud Infrastructure: AWS, GCP

🤖 **AI & Machine Learning**  
🔹 Smart Chatbots: 
Built with LangChain  
🔹 Custom AI Models: NLP, Automation

⚙️ **DevOps Solutions**  
🔹 CI/CD Pipelines: GitHub Actions,
 Jenkins  
🔹 Containerization: Docker, Kubernetes  
🔹 Infrastructure as Code: Terraform, Ansible  
🔹 Monitoring Tools: P
rometheus, Grafana

🌟 **Recent Projects**  
🚗 **Ride-Sharing**: Real-time tracking & payments  
📦 **Logistics**: Multi-s
top delivery optimization  
🛒 **E-Commerce**: Scalable Kubernetes clusters

💰 **Rates**: $20–$25/hour (negotiable)  
📧 *
*Let’s talk!** DM me to discuss your project!  
GitHub: [storm1033](https://github.com/storm1033)

**Let’s build somethi
ng amazing together!** 🌐✨

# 🌟 Let's Build Something Amazing Together! 🌟

# 👋 Hi, I'm Sheryar!

An AI/ML Engineer, Full 
Stack Developer, and DevOps Specialist. I help transform ideas into scalable, high-performance solutions. Whether you're
 looking to build a robust app, deploy intelligent AI systems, or streamline your infrastructure, I’ve got you covered!


# 🚀 What I Do Best:

# Full Stack Development

From sleek, user-friendly interfaces to powerful backends, I create seam
less web applications:

* **Stunning UIs**: React | Angular
* **Robust APIs**: Node.js | NestJS
* **Seamless Payment Int
egrations**: Stripe
* **Cloud Infrastructure**: AWS | GCP

# AI & Machine Learning

Unlock the potential of AI to elevat
e your product with intelligent, data-driven features:

* **AI Chatbots**: Powered by LangChain
* **Tailored AI Models**
: NLP, Automation, and more

# DevOps Excellence

I automate, optimize, and ensure reliability at scale:

* **CI/CD Pipe
lines**: GitHub Actions | Jenkins
* **Containerization**: Docker | Kubernetes
* **Infrastructure as Code**: Terraform | 
Ansible
* **Monitoring**: Prometheus | Grafana

# 🌟 Featured Projects

Here’s a glimpse of what I’ve worked on recently:


* **Ride-Sharing App**: Real-time vehicle tracking, seamless payments
* **Logistics Platform**: Multi-stop delivery ro
ute optimization
* **E-Commerce Platform**: Scalable Kubernetes clusters handling high traffic

# 💡 Let’s Collaborate!


* 💰 **Rate**: $20–$25/hour (negotiable depending on the project)
* 📩 **Reach Out**: DM me to discuss your project!

📍 **
GitHub**: [storm1033](https://github.com/storm1033)

**Let's turn your ideas into scalable, impactful solutions!** 🌐✨
```
---

     
 
all -  [ What is your go-to way of calling LLMs ?  ](https://www.reddit.com/r/node/comments/1hba5qq/what_is_your_goto_way_of_calling_llms/) , 2024-12-11-0914
```
For once, nodejs is not the main area of experimentation, we are a bit behind python for tooling. Still, what do y'all u
se for interfacing with llms ? For validating structured data ?

I know people hate on langchain, but there has to be so
mething better than raw openai package?
```
---

     
 
all -  [ How do you go about building a cursor/codeium clone ](https://www.reddit.com/r/LangChain/comments/1hb5yzl/how_do_you_go_about_building_a_cursorcodeium_clone/) , 2024-12-11-0914
```
So I want to build a similar UI like cursor. But I don’t want this for code. What I want is a dashboard/canvas on one si
de and a chat interface on another where the user can add stuff to chat from the dashboard and the AI can answer them. W
ould love to know how you guys think this can be built 
```
---

     
 
all -  [ Using Ollama and getting validation-error at invoke-function ](https://www.reddit.com/r/LangChain/comments/1hb55e6/using_ollama_and_getting_validationerror_at/) , 2024-12-11-0914
```
I am currently trying out Ollama for the first time and following a few tutorials (for example this one: https://python.
langchain.com/docs/integrations/llms/ollama/). Even though ollama is working perfectly fine in the terminal, the moment 
I try to use it in VSC through langchain, I get a Validation-Error, that tells me, my Input should be json and a diction
ary. Can anybody help me with this/do you have any idea what I am doing wrong? I have already reinstalled llama and the 
models

https://preview.redd.it/c2zxcn4zn16e1.png?width=1162&format=png&auto=webp&s=80f65b2155fb74a3f5c02e9038a78e65c254
4d80

https://preview.redd.it/a3zgindzn16e1.png?width=1107&format=png&auto=webp&s=b4af5d820386520ebd53892e92c965a9aa5313
46

  
  

```
---

     
 
all -  [ Using Ollama in Langchain and getting validation-error at invoke-function ](https://www.reddit.com/r/ollama/comments/1hb55c4/using_ollama_in_langchain_and_getting/) , 2024-12-11-0914
```
I am currently trying out Ollama for the first time and following a few tutorials (for example this one: https://python.
langchain.com/docs/integrations/llms/ollama/). Even though ollama is working perfectly fine in the terminal, the moment 
I try to use it in VSC through langchain, I get a Validation-Error, that tells me, my Input should be json and a diction
ary. Can anybody help me with this/do you have any idea what I am doing wrong? I have already reinstalled llama and the 
models

https://preview.redd.it/c2zxcn4zn16e1.png?width=1162&format=png&auto=webp&s=80f65b2155fb74a3f5c02e9038a78e65c254
4d80

https://preview.redd.it/a3zgindzn16e1.png?width=1107&format=png&auto=webp&s=b4af5d820386520ebd53892e92c965a9aa5313
46


```
---

     
 
all -  [ Voice agent companies - how are you monitoring and evaluating your calls? ](https://www.reddit.com/r/LangChain/comments/1hb0gyc/voice_agent_companies_how_are_you_monitoring_and/) , 2024-12-11-0914
```
We’re building [Roark Analytics](https://roark.ai/) (voice agent performance analytics) and are curious how other compan
ies monitor and evaluate their calls to improve agent performance.

* Are you tracking metrics like sentiment, intent ac
curacy, or call success rates?
* How are you identifying issues or areas for improvement?
* Do you analyze calls in real
-time or focus on post-call insights?

We’d love to learn more about the tools or strategies you’re using (or wish exist
ed) to monitor and evaluate your voice agents effectively.
```
---

     
 
all -  [ Looking for suggestions on AI courses around LLMs  ](https://www.reddit.com/r/developersPak/comments/1hb04r1/looking_for_suggestions_on_ai_courses_around_llms/) , 2024-12-11-0914
```
So, I used to do AI, mainly Deep Learning back in 2020, 2021 when LLMs were not a thing, I worked on a bunch of freelanc
e projects related to debugging, fine tuning etc so I'm comfortable with NLP, computer vision and stuff. I moved to full
stack webdev in 2023 and then to blockchain web dev so Ive been very disconnected with the new things. 

Im looking for 
any suggestions on systematic pathways to work on production ready llm based apps, I know the basics like langchain and 
RAG but Im completely blank on optimisations, best practices, agents, chains, etc. Can anyone here suggest a course or s
omething? 
```
---

     
 
all -  [ I asked a mobster what he thinks about langchain ](https://www.reddit.com/gallery/1hazuut) , 2024-12-11-0914
```
Loose lips sink ships 👀
```
---

     
 
all -  [ Hierarchical chunking ](https://www.reddit.com/r/LangChain/comments/1hazl77/hierarchical_chunking/) , 2024-12-11-0914
```
Hello everyone,

I’m currently working on a project involving the creation of a chatbot based on RAG (Retrieval-Augmente
d Generation). For the RAG part, I want to implement hierarchical chunking, where the text is chunked hierarchically, wi
th each leaf node containing a concise summary of its hierarchy. I'm not sure if this has already been implemented, so I
’m asking for any resources, articles, or existing implementations related to hierarchical chunking. Any help would be g
reatly appreciated!
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/SideProject/comments/1hazgkb/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-11-0914
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.



# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let yo
u upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, ana
lyze a research paper, and more. To see this in action or dive deeper into the tech behind it, check out this [YouTube v
ideo.](https://www.youtube.com/watch?v=ih9PBGVVOO4)



# Let's look at the market

Made possible by advances in AI like 
ChatGPT and Retrieval-Augmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen co
nsistent growth in market interest, which is currently at an all-time high (source:[google trends](https://trends.google
.com/trends/explore?date=today%205-y&q=pdf%20chat,pdf%20ai&hl=en-GB))

Keywords like 'chat PDF' and 'PDF AI' get between
 1 to 10 million searches every month (source:keyword planner), with a broad target audience that includes researchers, 
students, and professionals across various industries.

Leaders like [PDF.ai](http://PDF.ai) and ChatPDF have already ga
ined millions of users within a year of launch, driven by the growing market demand, with paid users subscribing at arou
nd $20/month.



# Alright, so how do we build this with open source?

The core tech for most PDF AI tools are based on 
the same architecture. You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the 
uploaded PDF’s chapters/topics and store them in a vector database (like Pinecone).

Now, every time the user asks a que
stion, a similarity search is performed to find the most similar PDF topics from the vector database. The selected topic
 contents are then sent to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are
 some of the best open source implementations for this process:

* [GPT4 & LangChain Chatbot for large PDF docs](https:/
/github.com/mayooear/gpt4-pdf-chatbot-langchain) by Mayo Oshin
* [MultiPDF Chat App](https://github.com/alejandro-ao/ask
-multiple-pdfs) by Alejandro AO
* [PDFToChat](https://github.com/Nutlope/pdftochat) by Hassan El Mghari

Worried about b
uilding signups, user management, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everythin
g you need out of the box:

* [SaaS Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) by Remi Wg
* [Open SaaS](ht
tps://github.com/wasp-lang/open-saas) by wasp-lang



# A few ideas to stand out from the noise:

Here are a few strateg
ies that could help you differentiate and achieve product market fit (based on the pivot principles from The Lean Startu
p by Eric Ries):

1. **Narrow down your target audience for a personalized UX:** For instance, an exam prep assistant fo
r students with study notes and quiz generator; or a document due diligence and analysis tool for lawyers.
2. **Add uniq
ue features to increase switching cost:** You could autogenerate APIs for the uploaded PDFs to enable remote integration
s (eg. support chatbot knowledge base); or build in workflow automation features for bulk analyses of PDFs.
3. **Offer p
latform level advantages:** You could ship a native mobile/desktop apps for a more integrated UX; or (non-trivial) offer
 private/offline support by replacing the APIs with local open source deployments (eg. llama for LLM, an embedding model
 from the MTEB list, and FAISS for vector search).

**TMI?** I’m an ex-AI engineer and product lead, so don’t hesitate t
o reach out with any questions!

**P.S.** I've started a free weekly [newsletter](https://saaswithcode.substack.com/p/is
sue-1-launch-a-saas-like-chatpdf) to share open-source/turnkey resources behind popular products (like this one). If you
’re a founder looking to launch your next product without reinventing the wheel, please subscribe :)
```
---

     
 
all -  [ JSON to Youtube Shorts ](https://www.reddit.com/r/LangChain/comments/1hayp1e/json_to_youtube_shorts/) , 2024-12-11-0914
```
Hey there,

For the past few months, I’ve been working on an open-source library for creating faceless videos.

I’m cons
idering turning it into an API so developers can easily integrate it by simply providing the script in scenes.

The API 
would generate:
	•	Voice
	•	Images
	•	Transitions
	•	Captions

I’m thinking of pricing it at around $0.10 per minute ren
dered to cover AI generation costs.

Is this something you’d be willing to pay for?

Thanks for the feedback!

Feel free
 to check out the open source repo: https://github.com/TurboReel/mediachain
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1haykyq/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-11-0914
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.



# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let yo
u upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, ana
lyze a research paper, and more. To see this in action or dive deeper into the tech behind it, check out this [YouTube v
ideo.](https://www.youtube.com/watch?v=ih9PBGVVOO4)



# Let's look at the market

Made possible by advances in AI like 
ChatGPT and Retrieval-Augmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen co
nsistent growth in market interest, which is currently at an all-time high (source: google trends)

Keywords like 'chat 
PDF' and 'PDF AI' get between 1 to 10 million searches every month (source:keyword planner), with a broad target audienc
e that includes researchers, students, and professionals across various industries.

Leaders like PDF.ai and ChatPDF hav
e already gained millions of users within a year of launch, driven by the growing market demand, with paid users subscri
bing at around $20/month.



# Alright, so how do we build this with open source?

The core tech for most PDF AI tools a
re based on the same architecture. You generate text embeddings (AI-friendly text representations; usually via OpenAI AP
Is) for the uploaded PDF’s chapters/topics and store them in a vector database (like Pinecone).

Now, every time the use
r asks a question, a similarity search is performed to find the most similar PDF topics from the vector database. The se
lected topic contents are then sent to an LLM (like ChatGPT) along with the question, which generates a contextual answe
r!

Here are some of the best open source implementations for this process:

* [GPT4 & LangChain Chatbot for large PDF d
ocs](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) by Mayo Oshin
* [MultiPDF Chat App](https://github.com/alej
andro-ao/ask-multiple-pdfs) by Alejandro AO
* [PDFToChat](https://github.com/Nutlope/pdftochat) by Hassan El Mghari

Wor
ried about building signups, user management, payments, etc.? Here are my go-to open-source SaaS boilerplates that inclu
de everything you need out of the box:

* [SaaS Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) by Remi Wg
* [O
pen SaaS](https://github.com/wasp-lang/open-saas) by wasp-lang



# A few ideas to stand out from the noise:

Here are a
 few strategies that could help you differentiate and achieve product market fit (based on the pivot principles from The
 Lean Startup by Eric Ries):

1. **Narrow down your target audience for a personalized UX:** For instance, an exam prep 
assistant for students with study notes and quiz generator; or a document due diligence and analysis tool for lawyers.
2
. **Add unique features to increase switching cost:** You could autogenerate APIs for the uploaded PDFs to enable remote
 integrations (eg. support chatbot knowledge base); or build in workflow automation features for bulk analyses of PDFs.

3. **Offer platform level advantages:** You could ship a native mobile/desktop apps for a more integrated UX; or (non-tr
ivial) offer private/offline support by replacing the APIs with local open source deployments (eg. llama for LLM, an emb
edding model from the MTEB list, and FAISS for vector search).



**TMI?** I’m an ex-AI engineer and product lead, so do
n’t hesitate to reach out with any questions!

**P.S.** I've started a free weekly [newsletter](https://saaswithcode.sub
stack.com/p/issue-1-launch-a-saas-like-chatpdf) to share open-source/turnkey resources behind popular products (like thi
s one). If you’re a founder looking to launch your next product without reinventing the wheel, please subscribe :)
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/SaaS/comments/1hayenp/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-11-0914
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.



# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let yo
u upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, ana
lyze a research paper, and more. To see this in action or dive deeper into the tech behind it, check out this [YouTube v
ideo.](https://www.youtube.com/watch?v=ih9PBGVVOO4)



# Let's look at the market

Made possible by advances in AI like 
ChatGPT and Retrieval-Augmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen co
nsistent growth in market interest, which is currently at an all-time high (source:[google trends](https://trends.google
.com/trends/explore?date=today%205-y&q=pdf%20chat,pdf%20ai&hl=en-GB))

Keywords like 'chat PDF' and 'PDF AI' get between
 1 to 10 million searches every month (source:keyword planner), with a broad target audience that includes researchers, 
students, and professionals across various industries.

Leaders like [PDF.ai](http://PDF.ai) and ChatPDF have already ga
ined millions of users within a year of launch, driven by the growing market demand, with paid users subscribing at arou
nd $20/month.



# Alright, so how do we build this with open source?

The core tech for most PDF AI tools are based on 
the same architecture. You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the 
uploaded PDF’s chapters/topics and store them in a vector database (like Pinecone).

Now, every time the user asks a que
stion, a similarity search is performed to find the most similar PDF topics from the vector database. The selected topic
 contents are then sent to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are
 some of the best open source implementations for this process:

* [GPT4 & LangChain Chatbot for large PDF docs](https:/
/github.com/mayooear/gpt4-pdf-chatbot-langchain) by Mayo Oshin
* [MultiPDF Chat App](https://github.com/alejandro-ao/ask
-multiple-pdfs) by Alejandro AO
* [PDFToChat](https://github.com/Nutlope/pdftochat) by Hassan El Mghari

Worried about b
uilding signups, user management, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everythin
g you need out of the box:

* [SaaS Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) by Remi Wg
* [Open SaaS](ht
tps://github.com/wasp-lang/open-saas) by wasp-lang



# A few ideas to stand out from the noise:

Here are a few strateg
ies that could help you differentiate and achieve product market fit (based on the pivot principles from The Lean Startu
p by Eric Ries):

1. **Narrow down your target audience for a personalized UX:** For instance, an exam prep assistant fo
r students with study notes and quiz generator; or a document due diligence and analysis tool for lawyers.
2. **Add uniq
ue features to increase switching cost:** You could autogenerate APIs for the uploaded PDFs to enable remote integration
s (eg. support chatbot knowledge base); or build in workflow automation features for bulk analyses of PDFs.
3. **Offer p
latform level advantages:** You could ship a native mobile/desktop apps for a more integrated UX; or (non-trivial) offer
 private/offline support by replacing the APIs with local open source deployments (eg. llama for LLM, an embedding model
 from the MTEB list, and FAISS for vector search).



**TMI?** I’m an ex-AI engineer and product lead, so don’t hesitate
 to reach out with any questions!

**P.S.** I've started a free weekly [newsletter](https://saaswithcode.substack.com/p/
issue-1-launch-a-saas-like-chatpdf) to share open-source/turnkey resources behind popular products (like this one). If y
ou’re a founder looking to launch your next product without reinventing the wheel, please subscribe :)
```
---

     
 
all -  [ Best way to run SWE-bench on my LangGraph agents framework? ](https://www.reddit.com/r/LangChain/comments/1hax1nz/best_way_to_run_swebench_on_my_langgraph_agents/) , 2024-12-11-0914
```
I build an agentic framework in LangGraph. What's the easiest way to benchmark it on SWE-bench? 
```
---

     
 
all -  [ How can I pass dataframe as an input in Langgrah? ](https://www.reddit.com/r/LangChain/comments/1hau2yy/how_can_i_pass_dataframe_as_an_input_in_langgrah/) , 2024-12-11-0914
```
I tried to pass a dataframe that does not work, and also there is a main problem, that is could not validate in the stat
e schema.

Then I tried to pass the DataFrame as a Dict, but that also did not work. Interestingly that did not throw an
 error, but the agent was not using this \`data\_dict\`, it generates some sample DataFrame randomly. 

    graph.invoke
(
            {'messages': [HumanMessage(
    content
    =prompt)], 'data_dict': data_dict}, 
            
    config
 
   =thread
        )

  

```
---

     
 
all -  [ Converting hand drawn floor plan to professional
 ](https://www.reddit.com/r/LangChain/comments/1hasrtn/converting_hand_drawn_floor_plan_to_professional/) , 2024-12-11-0914
```
So, was hoping for some thoughts. I am trying to see if there is a way to convert hand drawn floor maps, kinda like: [ht
tps://www.reddit.com/r/floorplan/comments/1aepd6n/are\_there\_any\_tools\_that\_can\_magically\_turn\_my/](https://www.r
eddit.com/r/floorplan/comments/1aepd6n/are_there_any_tools_that_can_magically_turn_my/)

Into something more like: [http
s://cubicasa-wordpress-uploads.s3.amazonaws.com/uploads/2019/07/simple-stylish-1024x991.png](https://cubicasa-wordpress-
uploads.s3.amazonaws.com/uploads/2019/07/simple-stylish-1024x991.png)

Stable Diffusion models tend to hallucinate too m
uch to generate something even midly resembling the original drawn layout.

So I tried to go for a programmatic approach
, once I have a semi decent computer generated mimic of the hand drawn image I could iterate with an agent to add labels
, making refinements.

I tried:

1. Pass the image to an LLM with instructions to return drawing instructions for pycair
o or shapely. (failed, even GPT4o failed pretty badly in the instructions. Almost like it could understand the image but
 did not have spatial understanding (would love anyone's understanding of this))
2. Tried ezdxf for CAD drawing since i 
thought maybe the issue was with the LLM generating pycairo instructions. (also failed, even worse than the pycairo inst
ructions)
3. Now on to converting it to a SVG as a vectorized representation using VTrace which can more easily detect l
ines, polygons, etc. Feed this into (via translating function) pycairo to get a set of instructions that need to be foll
owed to draw this. Next pass the instructions to an LLM to edit back and forth until a good product is achieved. HOWEVER
, I am still unsure whether the LLM will actually be able to understand or provide helpful feedback to edit the instruct
ions for drawing (can it even?)

So reaching out, anyone run into anything similar? any open source models attempt to em
ulate what I am doing? any thoughts on the process? or any models etc that can help here.

Thanks
```
---

     
 
all -  [ Document Priority Retriever ](https://www.reddit.com/r/LangChain/comments/1has712/document_priority_retriever/) , 2024-12-11-0914
```
I am implementing a rag system that has a bunch of files and pdfs, and I am facing a challenge.

I have 10 pdfs with a r
ecap of the year, one file by year so 10 years in total. All those files has the revenue , clients and others, it is bas
ically a executive summary of the year. 

I have used semantic search to embedding it , but the problem is , when I say 
something like what was the revenue of the year, it is taking a top k an old year documents instead of last year. If I s
pecified in the query the year, for example: what was 2023 revenue, it works, but in the first example is there a way to
 prioritize the most recent documents when doing the retriever?

I don't want to filter out by tag, because if the infor
mation asked is not in the most recent file than it should look for the others. Is there a way to easily do it ?
```
---

     
 
all -  [ How to connect to different schema other than public in langraph postgres checkpoint saver ](https://www.reddit.com/r/LangGraph/comments/1harmg6/how_to_connect_to_different_schema_other_than/) , 2024-12-11-0914
```
[https://langchain-ai.github.io/langgraph/concepts/persistence/#using-in-langgraph](https://langchain-ai.github.io/langg
raph/concepts/persistence/#using-in-langgraph)
```
---

     
 
all -  [  [Hiring] Currently working on a RAG + Big Data platform/marketplace and looking for developers  ](https://www.reddit.com/r/LangChain/comments/1harh82/hiring_currently_working_on_a_rag_big_data/) , 2024-12-11-0914
```
I'm currently building a RAG + Big data platform/marketplace. Think what home depot is for home builders, but we offer o
ff-the-shelf AI analytics. The startup's name is Analytics Depot and will be the one stop for all things analytics for r
eal estate, law, finance, insurance, oil and gas, supply chain, ecommerce etc.. 

We do not cater to enterprise customer
s. We cater B2C and B2Small business owners.  
  
The key areas we are focusing on is UI & UX, Data sources (more the me
rrier), Serving the right models for the right profession, and payment/token system. Eventually we will have a marketpla
ce where people can offer their own pipelines and get paid.

If you have built A-Z data pipelines in any of these indust
ries, DM me. I'd love to discuss how we can work together.
```
---

     
 
all -  [ Launched On Product Hunt: Here's the reason why I built it ](https://www.reddit.com/r/u_wait-a-minut/comments/1haq3z4/launched_on_product_hunt_heres_the_reason_why_i/) , 2024-12-11-0914
```
Over the past year of building AI-enabled SaaS applications, I kept hitting the same wall. Going from a Jupyter notebook
 full of AI RAG techniques to something usable in my app was a nightmare. I'm sure if anyone here has taking a look at l
lama-index or langchain cookbook sections you might understand what I'm talking about.

I came to the conclusion that th
is is the problem:  
\- Notebooks are great for testing ideas, but they’re not meant for building applications around th
em.  
\- I had to manually dissect notebooks, build a proof-of-concept API server, integrate it into my app, and pray it
 worked.  
\- The feedback loop was \*painfully\* long—and most of the time, I canned the project because it didn’t quit
e fit.

This frustration comes from a gap in roles:

1. Data Scientists/AI Devs want notebooks to experiment with method
s and techniques—but it's not their main focus to also create an API for other applications to use.
2. App Developers ju
st want simple APIs to test and integrate quickly to see if it actually enhances their app.

This is where KitchenAI com
es in. A tool that bridges this gap by transforming your AI Jupyter notebooks into production-ready API server in minute
s.

But why??  
\- Shorter Development Cycles  
Test, iterate, and deploy AI techniques faster and cut the feedback loop
 in half.  
\- Vendor and Framework Agnostic  
Use the libraries you’re comfortable with, no lock-ins.  
\- Plugin Archi
tecture  
Extend functionality with plugins for evaluation frameworks, observability, prompt management, and more.  
\- 
Open Source and Local-First  
Built on trusted technologies like Django, so you stay in control—no 3rd-party dependencie
s required.  
\- Docker-Ready  
Share your API server as a lightweight container for easy collaboration.

We’ve released
 KitchenAI as an Apache-licensed open-source tool, so anyone can use it. Up next is a managed cloud version with deeper 
integrations, metrics, analytics, and workflows for teams with more complex needs. One short term goal is to go straight
 from colab to a KitchenAI cloud hosted API so development can be absolutely seamless.

Give it a spin and a star: [http
s://github.com/epuerta9/kitc...](https://github.com/epuerta9/kitchenai)

The product hunt profile as well, a demo video 
is included: [https://www.producthunt.com/posts/kitchenai-2?utm\_source=other&utm\_medium=social](https://www.producthun
t.com/posts/kitchenai-2?utm_source=other&utm_medium=social)
```
---

     
 
all -  [ Do you know any examples of public or easy access RAGs chatbots using OpenAI API? ](https://www.reddit.com/r/OpenAI/comments/1hapw3c/do_you_know_any_examples_of_public_or_easy_access/) , 2024-12-11-0914
```
Hello everybody, this is my first post here. 

In the company I work for we are developing a proof of concept of a chatb
ot for internal use capable to answer almost any question related to the use of the products we sell (at least that is w
hat we are aiming for). 

We are using the RAG approach, feeding the chatbot with all the documentation in PDF we have (
manuals, logs, Support files, release notes, etc...). 

For this, we are using Langchain, ChromaDB and the OpenAI API, t
he DB was made using the text-embedding-3-large and playing with the temp parameters and changing between the models 4O 
and 4O-mini, cleaning the PDFs to quit irrelevant text, set up the metadata for every document in the BD, etc...

In gen
eral, the results are regular, the chatbot can anwer questions about the products with good approach, but when the user 
ask about the steps to perform certain task the chatbot usually hallucinates even when the instruccions can be found in 
the documentation. 

So, I'm wondering if you guys know any 'public' chatbot based on OpenAI and that follows the RAG ap
proach. We would like to evaluate if the chatbot we are aiming is viable or we would need  to find another way.

Sorry i
f there's any type, English is not my first language. 
```
---

     
 
all -  [ How to do agentic RAG with the plan-and-execute methodology? ](https://www.reddit.com/r/Rag/comments/1hap12s/how_to_do_agentic_rag_with_the_planandexecute/) , 2024-12-11-0914
```
I want to combine [agentic RAG](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_agentic_rag.i
pynb) with [plan and execute](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/p
lan-and-execute.ipynb) agents. I've built the [multi-vector agentic RAG workflow](https://colab.research.google.com/driv
e/1-tw-vgIgJMcXbdbSQwdhUTpsc663wMcw#scrollTo=7e22e20c-aac6-4c9d-b3c8-5822296b3ecf) in langgraph on some PDFs with tables
 by following the agentic RAG tutorial, but I am quite new to langgraph and as of yet have been unable to integrate the 
plan-and-execute method in my agentic RAG workflow.

In particular, here is the problem I want to solve. I am able to ca
lculate 'light dues', 'port dues' and 'vehicle dues' separately (i.e., in 3 different runs) in my agentic RAG workflow. 
But I want to be able to calculate all these charges in one shot - i.e., if I ask the agent, 'what are the total charges
 for a given vessel', it should be able to plan that in order to calculate the total charges it needs to calculate these
 3 individual charges (so it has 3 intermediate tasks), then calculate each of them (either one by one or in parallel), 
and then sum them up to present the final answer (the total charges) which is the fourth task.

How do I accomplish this
?

[Here](https://colab.research.google.com/drive/1vlkrUxj1fMxCJFe12Myh414AYxa79SRB) is my attempt, but there are issues
 with the node definitions and/one edge interaction:

>
```
---

     
 
all -  [ Launched an Open Source Tool on Product Hunt. Want to share why I built it. ](https://www.reddit.com/r/webdev/comments/1haoavw/launched_an_open_source_tool_on_product_hunt_want/) , 2024-12-11-0914
```
Over the past year of building AI-enabled SaaS applications, I kept hitting the same wall. Going from a Jupyter notebook
 full of AI RAG techniques to something usable in my app was a nightmare. I'm sure if anyone here has taking a look at l
lama-index or langchain cookbook sections you might understand what I'm talking about.  
  
I came to the conclusion tha
t this is the problem:  
\- Notebooks are great for testing ideas, but they’re not meant for building applications aroun
d them.  
\- I had to manually dissect notebooks, build a proof-of-concept API server, integrate it into my app, and pra
y it worked.  
\- The feedback loop was \*painfully\* long—and most of the time, I canned the project because it didn’t 
quite fit.  
  
This frustration comes from a gap in roles:  
1. Data Scientists/AI Devs want notebooks to experiment wi
th methods and techniques—but it's not their main focus to also create an API for other applications to use.  
2. App De
velopers just want simple APIs to test and integrate quickly to see if it actually enhances their app.

This is where Ki
tchenAI comes in. A tool that bridges this gap by transforming your AI Jupyter notebooks into production-ready API serve
r in minutes.  
  
But why??  
\- Shorter Development Cycles  
Test, iterate, and deploy AI techniques faster and cut th
e feedback loop in half.  
\- Vendor and Framework Agnostic  
Use the libraries you’re comfortable with, no lock-ins.  

\- Plugin Architecture  
Extend functionality with plugins for evaluation frameworks, observability, prompt management, 
and more.  
\- Open Source and Local-First  
Built on trusted technologies like Django, so you stay in control—no 3rd-pa
rty dependencies required.  
\- Docker-Ready  
Share your API server as a lightweight container for easy collaboration. 
 
  
We’ve released KitchenAI as an Apache-licensed open-source tool, so anyone can use it. Up next is a managed cloud v
ersion with deeper integrations, metrics, analytics, and workflows for teams with more complex needs. One short term goa
l is to go straight from colab to a KitchenAI cloud hosted API so development can be absolutely seamless.  
  
Give it a
 spin and a star: [https://github.com/epuerta9/kitc...](https://github.com/epuerta9/kitchenai)

The product hunt profile
 as well, a demo video is included: [https://www.producthunt.com/posts/kitchenai-2?utm\_source=other&utm\_medium=social]
(https://www.producthunt.com/posts/kitchenai-2?utm_source=other&utm_medium=social)
```
---

     
 
all -  [ Alternatives to run localLLM on private network  ](https://www.reddit.com/r/LocalLLaMA/comments/1han8mb/alternatives_to_run_localllm_on_private_network/) , 2024-12-11-0914
```
noobie question here:
I've been working with Langchain + localLLMs (using APIs) for a week now and I wondering If there'
s a way to deploy my agents on a private network (like the one from a company). Is there a way to do it with localLLM so
 other people on the network can acess?
```
---

     
 
all -  [ Visual Agents is Self-Aware Software: A Brief Intro ](https://youtu.be/iiDWPlrors4?si=Qnx7KDdU3KMq2JUS) , 2024-12-11-0914
```
Built on top of langchain in part.
```
---

     
 
all -  [ Building Recommendation System with RAG ](https://www.reddit.com/r/LangChain/comments/1hak0ml/building_recommendation_system_with_rag/) , 2024-12-11-0914
```
I like to build a recommendation system with RAG and wanted to hear others thoughts. I want to give recommendations base
d on multiple quizzes students take. For example, students would take 2-3 tests and based on those results, recommend qu
estions that they need to solve to improve their skills.

Here my data would be the following. For each test: testId, qu
estion number, choice selected(A,B,C,D), O/X (correct/incorrect) and category that the question belongs to.

My thinking
 is: I would feed these data into a vectorstore. Now when student has take 3 tests, I would feed this and based on those
 3 tests, I will do some kind of similiarity search and recommend questions that other students got wrong/correct and ge
t those test+question number out.

Would something like this be possible with RAG?
```
---

     
 
all -  [ GenAI and?? ](https://www.reddit.com/r/learnmachinelearning/comments/1haj5p5/genai_and/) , 2024-12-11-0914
```
Background: I have been working as a GenAI Engineer from mid of 2023 and basically this is what I have started my career
 with. I knew python and then as things came out I was doing development and learning the frameworks like Langchain, Lan
gGraph, Streamlit, Chainli, LlamaIndex, Haystack and what not.. I know a bit about Azure as we did deployments on azure.



After 1.5 year of experience in this domain, I think this is something that should not be your only skill. I want to 
learn something that will complement GenAI. I have exploring few options like DevOps, WebDevelopment ( the path is too l
ong, HTML, CSS, Javascript and goes the list goes on). What do you think I should learn/focus so that in some time I’ll 
standout from the crowd?



```
---

     
 
all -  [ [For Hire] Experienced AI/Full Stack & DevOps Developer – Seeking Challenging, High-Impact Projects! ](https://www.reddit.com/r/forhire/comments/1hairsl/for_hire_experienced_aifull_stack_devops/) , 2024-12-11-0914
```
Your All-in-One Solution for AI/ML, Full Stack, & DevOps!

👋 Hi, I’m Sheryar, a seasoned AI/ML Engineer, Full Stack Deve
loper, and DevOps Expert. Let's transform your ideas into powerful, scalable solutions!

💻 **Full Stack Expertise**  
🔹 
Beautiful UIs: React/Angular  
🔹 Powerful APIs: Node.js, NestJS  
🔹 Payment Integration: Stripe  
🔹 Cloud Hosting: AWS, 
GCP

🤖 **AI & Machine Learning**  
🔹 Intelligent Chatbots: Powered by LangChain  
🔹 Tailored AI Models: NLP, Automation


⚙️ **DevOps Excellence**  
🔹 CI/CD Pipelines: GitHub Actions, Jenkins  
🔹 Containerization: Docker, Kubernetes  
🔹 Infr
astructure as Code: Terraform, Ansible  
🔹 Monitoring: Prometheus, Grafana

🌟 **Recent Projects**  
🚗 Ride-Sharing: Real
-time tracking & payments  
📦 Logistics: Optimized multi-stop delivery  
🔹 E-Commerce: Scalable Kubernetes clusters

💰 *
*Rate**: $20–$25/hour (negotiable)  
📧 DM me to discuss your project!  
GitHub: [storm1033](https://github.com/storm1033
)

Let’s create something amazing together! 🌐✨
```
---

     
 
all -  [ Humanized AI agent of service support. LANGCHAIN+RAG. ](https://www.reddit.com/r/LangChain/comments/1hahyqe/humanized_ai_agent_of_service_support_langchainrag/) , 2024-12-11-0914
```
Hello everyone, how are you?  
For some time now, I've been self-studying the development of an AI for customer support 
services.

One challenge I've been facing—and it seems to be a common issue—is the humanization of the AI. But let's put
 that aside for now.

My current idea is: is using LangChain + RAG a good approach to keep moving forward?

I'm organizi
ng all the company's information, such as departments, types of service, when the AI should transfer to another departme
nt, and its behaviors, into a markdown file. However, I feel that its performance isn't as good compared to another AI I
’ve implemented purely in Node.js, with all the context embedded directly in the prompt.

If you have any ideas on how I
 can proceed or what I should study, I’d appreciate it. Also, if there’s something I need to change in my mindset regard
ing the current LangChain + RAG project, feel free to share.

Edit: Forgot to share more info.  
I'm using LANGCHAIN+RAG
+Multiquery.

The user says something, which is then rephrased into 5 different variations. Based on these variations, s
imilarity is searched, and a response is returned accordingly.
```
---

     
 
all -  [ Problem with code tracking in Langsmith in Colab ](https://www.reddit.com/r/Langchaindev/comments/1hafzbo/problem_with_code_tracking_in_langsmith_in_colab/) , 2024-12-11-0914
```
Hey guys, 

I have a problem with tracking in Langsmith in the following code (using Colab): 

    from langchain_core.d
ocuments import Document
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langch
ain_community.document_loaders import WebBaseLoader
    from langchain.text_splitter import CharacterTextSplitter
    fr
om langchain.prompts import ChatPromptTemplate
    from langchain_community.vectorstores.faiss import FAISS
    from lan
gchain_openai import AzureOpenAIEmbeddings
    import logging
    from langchain.chains import create_retrieval_chain
  
  from langsmith import Client
    
    
    from langchain_core.messages import HumanMessage, AIMessage
    from langch
ain_core.prompts import MessagesPlaceholder
    
    
    
    def get_document_from_web(url):
      logging.getLogger('
langchain_text_splitters.base').setLevel(logging.ERROR)
      loader = WebBaseLoader(url)
      docs = loader.load()
   
   splitter = CharacterTextSplitter(
          chunk_size=400,
          chunk_overlap=20
          )
      splitDocs = 
splitter.split_documents(docs)
      return splitDocs
    
    
    
    def create_db(docs):
        embeddings = Azure
OpenAIEmbeddings(
            model='text-embedding-3-large',
            azure_endpoint='https://langing.openai.azure.c
om/openai/deployments/Embed-test/embeddings?api-version=2023-05-15',
            openai_api_key='xxx',
            opena
i_api_version='2023-05-15'
        )
        vectorStore = FAISS.from_documents(docs, embeddings)
        return vectorS
tore
    
    def create_chain(vectorStore):
        prompt = ChatPromptTemplate.from_messages([
            ('system', 
'Answet the quistion based on the following context: {context}'),
            MessagesPlaceholder(variable_name='chat_hi
story'),
            ('human', '{input}')
        ])
    
    
    
    
        #chain = prompt | model
        chain =
 create_stuff_documents_chain(llm=model,
                                         prompt=prompt)
    
        retriever 
= vectorStore.as_retriever(search_kwargs = {'k':3})
        retriever_chain = create_retrieval_chain(
            retrie
ver,
            chain
        )
        return retriever_chain
    
    def process_chat(chain, question,chat_history):

      response = chain.invoke({
        'input': question,
        'chat_history': chat_history
        })
      return
 response['answer']
    
    chat_history = []
    
    
    if __name__ == '__main__':
      docs =get_document_from_we
b('https://docs.smith.langchain.com/evaluation/concepts')
      vectoreStore = create_db(docs)
      chain = create_chai
n(vectoreStore)
      while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
         
   break
        response = process_chat(chain, user_input, chat_history)
        chat_history.append(HumanMessage(conte
nt= user_input))
        chat_history.append(AIMessage(content = response))
        print('Bot:', response)
    
    
  
  

Everything is runing well but I do not see it in Langsmith, does anyone have any idea why?  

  
Thanks a looot for 
any tips 




```
---

     
 
all -  [ Job Opening ](https://www.reddit.com/r/submarines/comments/1hadjq8/job_opening/) , 2024-12-11-0914
```
As a former Navy Nuclear Electronics Technician (EWS/EDPO) who served aboard the USS TOLEDO, I founded VeteranAI with a 
clear mission: revolutionizing the VA disability claims process by fixing problems veterans have. VeteranAI is partnerin
g directly with veteran service organizations to streamline and improve the VA disability process. We're currently seeki
ng a Backend Developer to join our mission. Why Submariners? Having served alongside some of the most dedicated and skil
led professionals in the military, I know firsthand the unique problem-solving abilities and work ethic submariners brin
g to any challenge.

  
The ideal candidate will be responsible for developing and maintaining server-side logic and int
egrating user-facing elements crafted by front-end developers. You will play a crucial role in delivering high-quality s
oftware solutions that ensure the functionality and efficiency of our applications. This role requires a strong understa
nding of RESTful architecture, FastAPI, LangChain, and other AI tooling. Knowledge of the VA disability process is highl
y valued.

  
Job Type: Full-time

Location: Remote

Pay: $135,000.00 per year

Start Date: Mid January

Send resume or 
questions: [team@veteranai.co](mailto:team@veteranai.co)

Duties

1.  Design and Implement Backend Systems: Architect sc
alable and efficient backend solutions using appropriate technologies and best practices.
2.  Translate Problems to Code
: Analyze complex requirements and develop robust, maintainable code solutions to address them effectively.
3.  Collabor
ate Across Teams: Work closely with team members to drive project success and ensure seamless integration of components.


  
Experience

*  Proven experience as a Backend Engineer or similar role in application development.
*  Proficiency i
n Python, FastAPI, and RESTful architecture.
*  Experience with AI tooling such as LangChain and vector stores.
*  Knowl
edge of Docker, AWS, Redis, and PostgreSQL.
*  Familiarity with version control systems like Git.
*  Strong problem-solv
ing skills and the ability to work independently and as part of a team.
*  Knowledge of the VA disability process is hig
hly desirable.

  
Benefits:

* Dental insurance 
* Flexible schedule 
* Health insurance  
* Paid time off
* Vision ins
urance
* 401k

Compensation Package: 

*  RSU / Stock options 
* Salaried 
```
---

     
 
all -  [ Developing Memory Aware Chatbots with LangChain, LangGraph, Gemini and MongoDB. ](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb) , 2024-12-11-0914
```
In this step by step guide you will learn:

1. How to create a chatbot using LangChain, Gemini.
2. Handle Chat History u
sing LangGraph and MongoDB.
```
---

     
 
all -  [ What's the best way to replicate a langgraph flow to do the same calculation, but for multiple diffe ](https://www.reddit.com/r/LangChain/comments/1hab667/whats_the_best_way_to_replicate_a_langgraph_flow/) , 2024-12-11-0914
```
I have the following agent workflow to do a calculation:

`# Graph`

`from langgraph.graph import END, StateGraph, START
`

`from langgraph.prebuilt import ToolNode`



`# Define a new graph`

`workflow = StateGraph(AgentState)`



`# Define
 the nodes we will cycle between`

`workflow.add_node('agent', agent)  # agent`

`retrieve = ToolNode([retriever_tool])`


`workflow.add_node('retrieve', retrieve)  # retrieval`

`workflow.add_node('rewrite', rewrite)  # Re-writing the quest
ion`

`workflow.add_node(`

`'generate', generate`

`)  # Generating a response after we know the documents are relevant
`

`# Call agent node to decide to retrieve or not`

`workflow.add_edge(START, 'agent')`



`# Decide whether to retriev
e`

`workflow.add_conditional_edges(`

`'agent',`

`# Assess agent decision`

`tools_condition,`

`{`

`# Translate the 
condition outputs to nodes in our graph`

`'tools': 'retrieve',`

`END: END,`

`},`

`)`



`# Edges taken after the \`a
ction\` node is called.`

`workflow.add_conditional_edges(`

`'retrieve',`

`# Assess agent decision`

`grade_documents,
`

`)`

`workflow.add_edge('generate', END)`

`workflow.add_edge('rewrite', 'agent')`



`# Compile`

`graph = workflow.
compile()`

  
And here is the flow diagram:

https://preview.redd.it/h9mvbao82u5e1.png?width=662&format=png&auto=webp&s
=43e6c3bcae27e18267e1b931e7ee39c99310b03e

For example, the user question would be, 'What is the cost of books?', and th
e agent will do a search in the vector DB for the total cost of books and return a response.

I have the same type of ca
lculation to be done for 3 different things (say, calculate cost of books, cost of pens and cost of blackboards, and to 
find the total cost incurred we just sum these 3 up). I want to be able to repeat/replicate the retrieve-rewrite-generat
e part of the workflow for the 3 calculations, connect them to the main agent node, and then combine the 3 generate node
s into a 'totalCost' node to reach the \_end\_ node. How do I do that?  


The user question would be, 'What is the tota
l cost of this classroom', and I want the agent to break it down into 3 questions: 'What is the cost of books?', 'What i
s the cost of pens?' and 'What is the cost of blackboards?', and then do the vector DB querying for each of these questi
ons, get responses for each of these queries, sum them all up and give the final response.
```
---

     
 
all -  [ How to Efficiently Handle 1K+ SQL Records for a Text-to-SQL Use Case? ](https://www.reddit.com/r/LangChain/comments/1haae1o/how_to_efficiently_handle_1k_sql_records_for_a/) , 2024-12-11-0914
```
I am working on a text-to-SQL use case for a client, where I need to handle over 1K+ SQL records. The challenge arises a
s these records exceed the context window of the Llama-3.3 model provided by Groq. Additionally, I need to generate a gr
aphical representation of this data, and I’m considering using Plotly JSON for this purpose.

Is there an efficient way 
to handle this large dataset, send the data to the frontend, and generate the required graphical representation without 
overwhelming the context window or compromising performance? Suggestions or best practices would be highly appreciated!
```
---

     
 
all -  [ [For Hire] Frontend and Backend Developer with the top and latest development technologies for a gre ](https://www.reddit.com/r/forhire/comments/1ha9i3f/for_hire_frontend_and_backend_developer_with_the/) , 2024-12-11-0914
```
Hi Redditors,

I'm Emad a Full-stack Web developer/engineer with 8 years of experience, and I'm looking for new projects
 to start working on, please take a look at my portfolio here [https://www.sx-portfolio.com](https://www.sx-portfolio.co
m) (let me know if you need more examples or direct links to live websites in the PM)

**Here is my skill set:**

**For 
Frontend:**

* HTML / CSS
* JS / ESNext
* Webpack / Gulp / Grunt / Gatsby
* React (With Redux, Zustand, or MobX)
* Next.
js
* Vuejs (With VueX)
* Angular
* TypeScript

**For Backend:**

* Node.js
* Python
* Express.js
* MongoDB
* Mongoose
* 
Nest.js
* GraphQL
* Meteor (with Apollo and React)
* TypeScript

**For AI-based projects:**

* Python
* Langchain
* Fast
API
* Uvicorn
* Pydantic

**For Desktop Apps:**

* Electron

**For Mobile Apps (iOS and Android):**

* React Native
* Ex
po

**For Design:**

* Photoshop
* Illustrator

**Here is my Resume:**  [My resume link!](http://www.sx-portfolio.com/we
bsite-resources/My%20resume.pdf)

**And here are some testimonials from my clients :)**

* [Slips](https://www.reddit.co
m/r/testimonials/comments/agfmwf/pos_swordx10_is_a_brilliant_developer_and_a/)
* [VidSync](https://www.reddit.com/r/test
imonials/comments/5gvz3d/pos_uswordx10_excellent_frontend_dev/)
* [Las Cruces Directory](https://www.reddit.com/r/testim
onials/comments/5hyks4/uswordx10_is_awesome/)
* [SigurenZalog](https://www.reddit.com/r/testimonials/comments/5jsfqf/pos
_quality_web_design_from_uswordx10/)
* [Bitlounge](https://www.reddit.com/r/testimonials/comments/5lh2pz/pos_uswordx10_t
op_fontend_devdesigner/)
* [Foxul](https://www.reddit.com/r/testimonials/comments/5l3p8j/pos_quality_web_coding_from_usw
ordx10/)
* [LootTicket](https://www.reddit.com/r/testimonials/comments/5nfh1j/pos_uswordx10_is_an_amazing_front_end_dev/
)

**My Pricing:**

I work hourly for $35/hr and my fixed prices depend on your project's complexity.

Don't worry about
 the price, just PM me with your project and I'm sure we can figure out something that goes with your budget. :)

If you
 have any questions don't hesitate to PM me and I will be more than happy to answer you :) and here is my portfolio agai
n if you need my contact details [www.sx-portfolio.com](https://www.sx-portfolio.com) (Click the red handle in the top-r
ight or pm me for it)
```
---

     
 
all -  [ What are the best techniques and tools to have the model 'self-correct?' ](https://www.reddit.com/r/Rag/comments/1ha9643/what_are_the_best_techniques_and_tools_to_have/) , 2024-12-11-0914
```
# CONTEXT
I'm a noob building an app that analyses financial transactions to find out what was the max/min/avg balance e
very month/year. Because my users have accounts in multiple countries/languages that aren't covered by Plaid, I can't re
ly on Plaid -- I have to analyze account statement PDFs.

Extracting financial transactions like ||||||| 2021-04-28 | 45
2.10 | credit ||||||| _almost_ works. The model will hallucinate most times and create some transactions that don't exis
t. It's always just one or two transactions where it fails.

I've now read about Prompt Chaining, and thought it might b
e a good idea to have the model check its own output. Perhaps say 'given this list of transactions, can you check they'r
e all present in this account statement' or even way more granular do it for every single transaction for getting it 100
% right 'is this one transaction present in this page of the account statement', _transaction by transaction_, and have 
it correct itself.

# QUESTIONS:
1) is using the model to self-correct a good idea?

2) how could this be achieved? 

3)
 should I use the regular api for chaining outputs, or langchain or something? I still don't understand the benefits of 
these tools

# More context:
- I started trying this by using Docling to OCR the PDF, then feeding the markdown to the L
LM (both in its entirety and in hierarchical chunks). It wasn't accurate, it wouldn't extract transactions alright
- I t
hen moved on to Llama vision, which seems to be yielding much better results in terms of extracting transactions. but st
ill makes some mistakes
- My next step before doing what I've described above is to improve my prompt and play around wi
th temperature and top_p, etc, which I have not played with so far!
```
---

     
 
all -  [ Event-Driven Patterns for AI Agents ](https://www.reddit.com/r/LangChain/comments/1ha8mrc/eventdriven_patterns_for_ai_agents/) , 2024-12-11-0914
```
I've been diving deep into multi-agent systems lately, and one pattern keeps emerging: high latency from sequential tool
 execution is a major bottleneck. I wanted to share some thoughts on this and hear from others working on similar proble
ms. This is somewhat of a langgraph question, but also a more general architecture of agent interaction question.

# The
 Context Problem

For context, I'm building [potpie.ai](https://potpie.ai/), where we create knowledge graphs from codeb
ases and provide tools for agents to interact with them. I'm currently integrating langgraph along with crewai in our ag
ents. One common scenario we face an agent needs to gather context using multiple tools - For example, in order to get t
he complete context required to answer a user’s query about the codebase, an agent could call:

* A keyword index query 
tool
* A knowledge graph vector similarity search tool
* A code embedding similarity search tool.

Each tool requires th
e same inputs but gets called sequentially, adding significant latency.

# Current Solutions and Their Limits

Yes, you 
can parallelize this with something like LangGraph. But this feels rigid. Adding a new tool means manually updating the 
DAG. Plus it then gets tied to the exact defined flow and cannot be dynamically invoked. I was thinking there has to be 
a more flexible way. Let me know if my understanding is wrong. 

# Thinking Event-Driven

I've been pondering the idea o
f event-driven tool calling, by having tool consumer groups that all subscribe to the same topic.

    # Publisher patte
rn for tool groups
    @tool
    def gather_context(project_id, query):
        context_request = {
            'project
_id': project_id,
            'query': query
        }
        publish('context_gathering', context_request)
        
  
  
    @subscribe('context_gathering')
    async def keyword_search(message):
        return await process_keywords(mess
age)
    
    @subscribe('context_gathering')
    async def docstring_search(message):
        return await process_docs
trings(message)

This could extend beyond just tools - bidirectional communication between agents in a crew, each reacti
ng to events from others. A context gatherer could immediately signal a reranking agent when new context arrives, while 
a verification agent monitors the whole flow.

There are many possible benefits of this approach:

# Scalability

* Hori
zontal scaling - just add more tool executors
* Load balancing happens automatically across tool instances
* Resource ut
ilization improves through async processing

# Flexibility

* Plug and play - New tools can subscribe to existing topics
 without code changes
* Tools can be versioned and run in parallel
* Easy to add monitoring, retries, and error handling
 utilising the queues

# Reliability

* Built-in message persistence and replay
* Better error recovery through dedicate
d error channels

# Implementation Considerations

From the LLM, it’s still basically a function name that is being retu
rned in the response, but now with the added considerations of :

* How do we standardize tool request/response formats?
 Should we? 
* Should we think about priority queuing? 
* How do we handle tool timeouts and retries
* Need to think abo
ut message ordering and consistency across queue
* Are agents going to be polling for response?

I'm curious if others h
ave tackled this:

* Does tooling like this already exist?
* I know Autogen's new architecture is around event-driven ag
ent communication, but what about tool calling specifically?
* How do you handle tool dependencies in complex workflows?

* What patterns have you found for sharing context between tools?

The more I think about it, the more an event-driven 
framework makes sense for complex agent systems. The potential for better scalability and flexibility seems worth the ad
ded complexity of message passing and event handling. But I'd love to hear thoughts from others building in this space. 
Am I missing existing solutions? Are there better patterns?

Let me know what you think - especially interested in heari
ng from folks who've dealt with similar challenges in production systems.
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-11-0914
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
