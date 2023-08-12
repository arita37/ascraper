 
all -  [ Best LangChain features to support in a software development AI-assisted tool ](/r/LangChain/comments/15oj0ax/best_langchain_features_to_support_in_a_software/) , 2023-08-12-0909
```

```
---

     
 
all -  [ Best LangChain features to support in a software development AI-assisted tool ](https://www.reddit.com/r/LangChain/comments/15oj0ax/best_langchain_features_to_support_in_a_software/) , 2023-08-12-0909
```
Hello fellow programmers. Me and my friends recently used LangChain and some fancy prompt engineering techniques to auto
generate a code base for a rather complex software project using GPT.

We made our tool free and open source under the M
IT license, and we intend to keep at it and improve it and add more features to it.

Here is the tool: [https://github.c
om/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer)

I wonder what do yo
u think should be supported by a tool like this? Especially regarding the features that LangChain enable.

Please either
 comment here, or file an issue on our github. I truly appreciate your time and your feedback. I also appreciate it if y
ou would kindly leave us a star on github.
```
---

     
 
all -  [ Using langchainjs for real-world applications. ](https://www.reddit.com/r/LangChain/comments/15ogvjs/using_langchainjs_for_realworld_applications/) , 2023-08-12-0909
```
[https://github.com/amalshehu/langchain-js-realworld](https://github.com/amalshehu/langchain-js-realworld)
```
---

     
 
all -  [ [D] How we evaluated LLMs in prod ](https://www.reddit.com/r/MachineLearning/comments/15ogknd/d_how_we_evaluated_llms_in_prod/) , 2023-08-12-0909
```
This is going to be a post about the challenges I faced while working with ChatGPT in my previous company and the things
 we did to overcome them over a 2+ month struggle. Check us out at [www.twilix.io](https://www.twilix.io/) if anything b
elow resonates with you and I hope you find some of it helpful.

So to begin, in my previous company we invested a few m
onths building a chatbot to help with user onboarding. At first everything was great, and we saw a 40% decrease in drop-
off rates (which is significant given we were building a consumer facing app), but somehow over time this drop-off rate 
started creeping up again. Perplexed by the unexpected turn in metrics, management started to question the benefits of m
aintaining this chatbot and was skeptical that we were cherry picking examples to showcase its performance for the sake 
of not wasting our efforts. They also knew that GPT4 got shadow nerfed which didn't help our case at all.

We had a lot 
of back and forth and eventually came to the conclusion that somehow the chatbot performance have to be quantified to ju
stify it's purpose. So, our team spent another 2 months engineering an evaluation solution to show leadership that the c
hatbot is performing as expected while identifying areas of improvement to craft a more refined product roadmap. We ende
d up trying a lot of different things, and after a long process of iteration and experimentation here are the things tha
t worked for us:

1. Generating synthetic datasets (these act as 'ground truths' pair of queries and expected responses)
 to benchmark performance.
2. Training models to determine the similarity score to assess every ChatGPT output in produc
tion (we use the generated synthetic dataset to do this to compare expected responses vs real responses)
3. Classifying 
the type of use cases the chatbot was used for (this allowed us to see which use cases were performing worse)
4. Logging
 configurations in our LLM stack and building visualizations on the web to identify what gives the best results (tempera
ture, LangChain configurations, lLamaIndex chunking sizes, these type of configurations)
5. Monitoring how our costs and
 latency are affected by tweaking different parameters
6. Lastly, A/B test to figure out the optimal parameters on diffe
rent sets of users (from experience, typically for a user onboarding chatbot use case around 5,000 users interacting wit
h your chatbot should be enough to collect some meaningful datapoints)

The most important learnings that we took away w
as that whilst synthetic data is OK you do need to generate large amounts of it. The sweet spot is different depending o
n the use case + the specifics of your knowledge base (eg, a corpus of internal documents vs a collection of websites), 
and I say sweet spot because after a certain amount of datapoints everything else kind of becomes noise and actually neg
atively affects your analysis more than the benefit it brings.

We ended up showing where our chatbot onboarding experie
nce fell short and was able to fix it through rapid iteration. There's still no set standard for LLM evaluation but I ho
pe my previous experiences helped. (Our team is now building out this evaluation system as a standalone product at [www.
twilix.io](https://www.twilix.io/) so check us out if you also want some concrete proof that ChatGPT is performing as ex
pected for your business)
```
---

     
 
all -  [ Langchain Expression Language: Easy declarative way to code and lot more! ](https://youtu.be/AM77pbogh5s) , 2023-08-12-0909
```

With the newly introduced Langchain Expression Language(LCEL), 

1. Engaging with core components becomes as easy using
 pipe operation.
2. The black box behind how to optimize  LLMs calls is taken away with batch, stream and a sync APIs.
3
. Conversation Retrieval Chain, VectorStore retrieval  & Memory based prompts are well structured with easily shared boi
ler plate using RunningPassThrough and ItemGetter.
4. Function calling, similar to OpenAI , is now here.
5. And lot more
 syntactical sugar is offered. 

Check out the video for an easy quick tutorial over each topic with a practical example
!
```
---

     
 
all -  [ Langchain + LLaMa 2 consuming too much VRAM ](https://www.reddit.com/r/LocalLLaMA/comments/15oaa18/langchain_llama_2_consuming_too_much_vram/) , 2023-08-12-0909
```
I was playing around with a GitHub project on a conda environment on Windows and I was surprised to see that LLama 2 13B
 4bit was using up to 25GB VRAM (16GB on one GPU and 9GB on the second one) for a simple summarization task on a documen
t with less than 4KB. I wanted to find out if there was an issue with Langchain or if it's just how it goes with LLMs be
cause seeing that a model occupies 8GB on disk and uses almost triple the amount of VRAM is suspicious. Am I doing somet
hing wrong?
```
---

     
 
all -  [ Is langchain worth it, over function calling? ](https://www.reddit.com/r/ChatGPTCoding/comments/15o9rug/is_langchain_worth_it_over_function_calling/) , 2023-08-12-0909
```
I find langchain a bit frustrating to work with.  I think it's partly a documentation issue, but I think the design is a
 bit confusing as well.  Since OpenAI came out with function calling I'm not sure I need chains.

I still may use langch
ain as a utility library for all its integrations, but without using the chains functionality due to the added complexit
y.

What do you think?
```
---

     
 
all -  [ Stuck at $500 MRR & Seeking Distribution/Marketing Advice ](https://www.reddit.com/r/SaaS/comments/15o9alc/stuck_at_500_mrr_seeking_distributionmarketing/) , 2023-08-12-0909
```
Hey everyone! 👋  
  
I'm Milan, founder of Robofy, an AI chatbot tool I've poured countless hours into. Robofy is live
 for around 3 months now. Our Monthly Recurring Revenue (MRR) has been stagnant at around $500 for the last 3 months, wh
ich has been a tad frustrating. I rebranded in June to Robofy but still am stuck at $500 and I am looking for fresh idea
s.  
  
One thing I've noticed is an extremely large number of similar products popping up in the market. It's both ex
citing and intimidating because it confirms a demand, but also adds that much more competition. I think most of the comp
etitors are coming up because of the cookbook published by OpenAI and the progress made by Langchain.  
  
Nevertheles
s, here's where I need your help:  
  
**Marketing**: I've the basic marketing avenues (Google Ads, Facebook Ads, etc.
) but the ROI hasn't been great. In fact, I would say that I recovered only 20% of my investment of $2500 in ads. Hence 
am in need of fresh, out-of-the-box strategies that can help stand out in this saturated space.  
  
**Distribution**:
 While our product is great, I believe our main challenge lies in getting it in front of the right eyes. Any ideas or ch
annels we might not have tapped into yet? I tried Twitter but again I faced the most common problem - not getting enough
 eyeballs.  


I tried creating a reseller plan so as to change target audience from direct customers to smaller IT com
panies. I got 2 orders for it now and that creates a bulk of my revenue. 

  
A few additional points:  
  
The prima
ry audience is small to medium businesses looking to streamline their customer support.  
We have a free tier, as well 
as paid packages with more features and benefits.  


I genuinely believe in Robofy, and I've had really positive feedb
ack from our few users. It's just the scaling and distribution part where we're having a hiccup.  
  
Cheers.  

```
---

     
 
all -  [ Use Llama2 to Improve the Accuracy of Tesseract OCR ](https://github.com/Dicklesworthstone/llama2_aided_tesseract) , 2023-08-12-0909
```
I've been disappointed by the very poor quality of results that I generally get when trying to run OCR on older scanned 
documents, especially ones that are typewritten or otherwise have unusual or irregular typography. I recently had the id
ea of using Llama2 to use common sense reasoning and subject level expertise to correct transcription errors in a 'smart
' way-- basically doing what a human proofreader who is familiar with the topic might do.

I came up with the linked scr
ipt that takes a PDF as input, runs Tesseract on it to get an initial text extraction, and then feeds this sentence-by-s
entence to Llama2, first to correct mistakes, and then again on the corrected text to format it as markdown where possib
le. This was surprisingly easier than I initially expected thanks to the very nice tooling now available in libraries su
ch as llama-cpp-python, langchain, and pytesseract. But the big issue I was encountering was that Llama2 wasn't just cor
recting the text it was given-- it was also hallucinating a LOT of totally new sentences that didn't appear in the origi
nal text at all (some of these new sentences used words which never appeared elsewhere in the original text).

I figured
 this would be pretty simple to filter out using fuzzy string matching-- basically check all the sentences in the LLM co
rrected text and filter out sentences that are very different from any sentences in the original OCRed text. To my surpr
ise, this approach worked very poorly. In fact, lots of other similar tweaks, including using bag-of-words and the spacy
 NLP library in various ways (spacy worked very poorly in everything I tried), also didn’t work.

Finally I realized tha
t I had a good solution staring me in the face: Llama2. I realized I could get sentence level vector embeddings straight
 from Llama2 using langchain. So I did that, getting embeddings for each sentence in the raw OCRed text and the LLM corr
ected text, and then computed the cosine similarity of each sentence in the LLM corrected text against all sentences in 
the raw OCRed text. If no sentences match in the raw OCRed text, then that sentence has a good chance of being hallucina
ted.

In order to save the user from having to experiment with various thresholds, I saved the computed embeddings to an
 SQLite database so they only had to be computed once, and then tried several thresholds, comparing the length of the fi
ltered LLM corrected text to the raw OCRed text; if things worked right, these texts should be roughly the same length. 
So as soon as the filtered length dips below the raw OCRed text length, it backtracks and uses the previous threshold as
 the final selected threshold.

Anyway, if you have some very old scanned documents laying around, you might try them ou
t and see how well it works for you. Do note that it's extremely slow, but you can leave it overnight and maybe the next
 day you'll have your finished text, which is better than nothing! I feel like this could be useful for sites like the I
nternet Archive-- I've found their OCR results to be extremely poor for older documents.

I'm open to any ideas or sugge
stions you might have. I threw this together in a couple days and know that it can certainly be improved in various ways
. One idea that I thought might be fun would be to make this work with a Ray cluster, sending a different page of the do
cument to each of the workers in the cluster to do it all at the same time.
```
---

     
 
all -  [ Does using langchain and openai worth training negative scenarios? ](https://www.reddit.com/r/Chatbots/comments/15o7d3e/does_using_langchain_and_openai_worth_training/) , 2023-08-12-0909
```
Is using langchain and OpenAI to create chatbot is preferrable to use?

Since designing contains a lot of portion of tra
ining prompt to not to give answers out of the topic.
```
---

     
 
all -  [ Could not load Llama model from path: ./Models/llama-7b.ggmlv3.q2_K.bin. Received error Llama.__init ](https://www.reddit.com/r/LocalLLaMA/comments/15o56kw/could_not_load_llama_model_from_path/) , 2023-08-12-0909
```
&#x200B;

>from langchain.llms import LlamaCpp  
>  
>from langchain import PromptTemplate, LLMChain  
>  
>from langcha
in.callbacks.manager import CallbackManager  
>  
>from langchain.callbacks.streaming\_stdout import StreamingStdOutCall
backHandler  
>  
>template = '''Question: {question}  
>  
>Answer: Let's work this out in a step by step way to be sur
e we have the right answer.'''  
>  
>prompt = PromptTemplate(template=template, input\_variables=\['question'\])  
>  

>callback\_manager = CallbackManager(\[StreamingStdOutCallbackHandler()\])  
>  
>llm = LlamaCpp(  
>  
>model\_path='./
Models/llama-7b.ggmlv3.q2\_K.bin',  
>  
>input={'temperature': 0.75,  
>  
>'max\_length': 2000,  
>  
>'top\_p': 1},  

>  
>callback\_manager=callback\_manager,  
>  
>verbose=True,  
>  
>)  
>  
>llm\_chain = LLMChain(prompt=prompt, llm
=llm)

&#x200B;

https://preview.redd.it/kwvc162rkghb1.png?width=797&format=png&auto=webp&s=d9a5c03721a553bd0b898cad708e
0afa446af0ed

>(llm) C:\\llm>python app1.py C:\\llm\\lib\\site-packages\\langchain\\utils\\utils.py:155: UserWarning: WA
RNING! input is not default parameter.                 input was transferred to model\_kwargs.                 Please co
nfirm that input is what you intended.   warnings.warn( Exception ignored in: <function Llama.\_\_del\_\_ at 0x000001923
B3AE680> Traceback (most recent call last):   File 'C:\\llm\\lib\\site-packages\\llama\_cpp\\llama.py', line 1507, in \_
\_del\_\_     if self.model is not None: AttributeError: 'Llama' object has no attribute 'model' Traceback (most recent 
call last):   File 'C:\\llm\\app1.py', line 14, in <module>     llm = LlamaCpp(   File 'C:\\llm\\lib\\site-packages\\lan
gchain\\load\\serializable.py', line 74, in \_\_init\_\_     super().\_\_init\_\_(\*\*kwargs)   File 'pydantic\\main.py'
, line 341, in pydantic.main.BaseModel.\_\_init\_\_ pydantic.error\_wrappers.ValidationError: 1 validation error for Lla
maCpp \_\_root\_\_   Could not load Llama model from path: ./Models/llama-7b.ggmlv3.q2\_K.bin. Received error Llama.\_\_
init\_\_() got an unexpected keyword argument 'input' (type=value\_error)

&#x200B;
```
---

     
 
all -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-08-12-0909
```
What are the possible practical approaches to creating an 'AI tutor' for a custom fantasy language, i.e. a language whic
h is definitely not covered in any large, mainstream LLM?

Assume in the fantasy language (like Game of Throne's Dothrak
i, but completely custom, so it's guaranteed not to be covered at all by an existing LLM), we have a dictionary of terms
, and a simple description of a grammar. What can I do with that?

Initially I was thinking of using 'Retrieval-Augmente
d Generation' (RAG), where I would pass it my dictionary of terms and their definitions and the grammar doc (i.e. the so
urce documents), and using OpenAI's LLM and LangChain's API wrapper and Pinecone long-term memory vector database, store
 the dictionary/grammar in Pinecone's vector database. Then a query comes in to translate an English word to a fantasy w
ord, and it looks in the Pinecone DB for similar English words, then passes the results with the fantasy word to the LLM
, along with the query, and generates a nice English response, with the fantasy word somewhere in there.

But that doesn
't seem like it would work the more I think about it. Then if I want to add the ability for it to translate English to t
he fantasy language, that seems impossible without first having a huge corpus of translation material (which is complete
ly impractical for a fantasy language). So can an existing generic LLM take a grammar as input, and learn to speak a fan
tasy language? If so, how would you make that happen?

Or what are other approaches to accomplishing this sort of thing?

```
---

     
 
all -  [ How to evaluate ChatGPT rigorously ](https://www.reddit.com/r/ChatGPT/comments/15o0ecd/how_to_evaluate_chatgpt_rigorously/) , 2023-08-12-0909
```
This is going to be a post about the challenges I faced while working with ChatGPT in my previous company and the things
 we did to overcome them over a 2+ month struggle. Check us out at [www.twilix.io](https://www.twilix.io) if anything be
low resonates with you and I hope you find some of it helpful.

So to begin, in my previous company we invested a few mo
nths building a chatbot to help with user onboarding. At first everything was great, and we saw a 40% decrease in drop-o
ff rates (which is significant given we were building a consumer facing app), but somehow over time this drop-off rate s
tarted creeping up again. Perplexed by the unexpected turn in metrics, management started to question the benefits of ma
intaining this chatbot and was skeptical that we were cherry picking examples to showcase its performance for the sake o
f not wasting our efforts. They also knew that GPT4 got shadow nerfed which didn't help our case at all. 

We had a lot 
of back and forth and eventually came to the conclusion that somehow the chatbot performance have to be quantified to ju
stify it's purpose. So, our team spent another 2 months engineering an evaluation solution to show leadership that the c
hatbot is performing as expected while identifying areas of improvement to craft a more refined product roadmap. We ende
d up trying a lot of different things, and after a long process of iteration and experimentation here are the things tha
t worked for us:

1. Generating synthetic datasets (these act as 'ground truths' pair of queries and expected responses)
 to benchmark performance. 
2. Training models to determine the similarity score to assess every ChatGPT output in produ
ction (we use the generated synthetic dataset to do this to compare expected responses vs real responses)
3. Classifying
 the type of use cases the chatbot was used for (this allowed us to see which use cases were performing worse)
4. Loggin
g configurations in our LLM stack and building visualizations on the web to identify what gives the best results (temper
ature, LangChain configurations, lLamaIndex chunking sizes, these type of configurations)
5. Monitoring how our costs an
d latency are affected by tweaking different parameters
6. Lastly, A/B test to figure out the optimal parameters on diff
erent sets of users (from experience, typically for a user onboarding chatbot use case around 5,000 users interacting wi
th your chatbot should be enough to collect some meaningful datapoints)

The most important learnings that we took away 
was that whilst synthetic data is OK you do need to generate large amounts of it. The sweet spot is different depending 
on the use case + the specifics of your knowledge base (eg, a corpus of internal documents vs a collection of websites),
 and I say sweet spot because after a certain amount of datapoints everything else kind of becomes noise and actually ne
gatively affects your analysis more than the benefit it brings. 

We ended up showing where our chatbot onboarding exper
ience fell short and was able to fix it through rapid iteration. There's still no set standard for LLM evaluation but I 
hope my previous experiences helped. Our team is now building out this evaluation system as a standalone product at [www
.twilix.io](https://www.twilix.io) so check us out if you also want some concrete proof that ChatGPT is performing as ex
pected for your business. Hope it helped : )

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ I've recently released a website that utilizes AI to create learning paths for any skill. ](https://www.reddit.com/r/SideProject/comments/15nwh5d/ive_recently_released_a_website_that_utilizes_ai/) , 2023-08-12-0909
```
I use Next.js, Langchain and deployed it on Vercel.

The operation is simple, input a prompt with the skill you want to 
learn, and receive an AI-generated learning path.

Features:

* Generate learning paths
* Track your progress
* Publish 
your learning paths

Link: [https://skillai.io](https://skillai.io)

&#x200B;

[Home](https://preview.redd.it/wv172ulrce
hb1.png?width=2440&format=png&auto=webp&s=cff2337ae29f6e346675f09aada3b55208c87a4e)

&#x200B;

[Learning path generated]
(https://preview.redd.it/f3szvxhwcehb1.png?width=2818&format=png&auto=webp&s=929e7f362870883691ac5a11adb230aab8c7277b)


&#x200B;
```
---

     
 
all -  [ Chatbot that only pulls specific data from a SQL database based on UserID? ](https://www.reddit.com/r/LangChain/comments/15nqfc3/chatbot_that_only_pulls_specific_data_from_a_sql/) , 2023-08-12-0909
```
I have a SQL database that external partners access but they can only see information attached to their unique user ID. 
Is it possible to create a chatbot using langchain that recognizes each persons unique user id and only pulls the releva
nt data from the SQL database without giving them access to the rest?
```
---

     
 
all -  [ Is there a way to summarize the current chain? ](https://www.reddit.com/r/LangChain/comments/15npkpp/is_there_a_way_to_summarize_the_current_chain/) , 2023-08-12-0909
```
I’m building a clone of chatGPT for personal development. 

I’m missing the feature to show a summary of the history lik
e in chatGPT side panel. 

Is there a way to get it from Langchain?
```
---

     
 
all -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-08-12-0909
```
&#x200B;

https://preview.redd.it/wl1gtcngnchb1.jpg?width=1500&format=pjpg&auto=webp&s=24e35d852603c6139fd67f79457ec593f
bad99f7

If you're someone who's curious about or working with LLMs there's a cool panel discussion coming up: 

* Compa
ring the pros and cons of using existing LLMs, prompt engineering, and fine-tuning on custom datasets for different ente
rprise use cases.
* Fine-Tuning LLMs: Exploring the advantages and challenges of fine-tuning LLMs on custom datasets to 
align with specific business objectives.
* Tools and platforms: Discussing the various tools and platforms to facilitate
 LLM implementation 
* Overcoming Challenges: Addressing the challenges associated with adopting LLMs, including data pr
ivacy, creating high quality datasets, computational resources, ethical considerations, and the need for specialized exp
ertise.
* Future Directions: Exploring emerging trends, advancements, and potential future applications of LLMs in the e
nterprise context.

Here's the event info: [https://www.eventbrite.com/e/large-language-models-for-enterprise-success-ch
allenges-and-approaches-tickets-695089811337?aff=oddtdtcreator](https://www.eventbrite.com/e/large-language-models-for-e
nterprise-success-challenges-and-approaches-tickets-695089811337?aff=oddtdtcreator)
```
---

     
 
all -  [ Best features to support in a software development AI-assisted tool ](https://www.reddit.com/r/ChatGPT/comments/15nln2f/best_features_to_support_in_a_software/) , 2023-08-12-0909
```
Hello fellow programmers. Me and my friends recently used LangChain and some fancy prompt engineering techniques to auto
generate a code base for a rather complex software project using GPT.

We made our tool free and open source under the M
IT license, and we intend to keep at it and improve it and add more features to it. 

Here is the tool: [https://github.
com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer) 

I wonder what do 
you think should be supported by a tool like this? 

Please either comment here, or file an issue on our github. I truly
 appreciate your time and your feedback. I also appreciate it if you would kindly leave us a star on github. 
```
---

     
 
all -  [ strugle to chat with docs ](https://www.reddit.com/r/LangChain/comments/15nl2ll/strugle_to_chat_with_docs/) , 2023-08-12-0909
```
 I recently cloned the [**gpt4-pdf-chatbot-langchain**](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) reposito
ry from GitHub which integrates with Pinecone. However, I've encountered an issue after ingesting a document of about 50
0 pages with embedded links. The chatbot seems to 'hallucinate' or misinterpret these links, which is quite unexpected. 
I'm seeking alternative solutions or suggestions to address this. Any guidance would be greatly appreciated. Thank you. 
 
 
```
---

     
 
all -  [ Open Source Vector Embedding Pipeline to Ingest Gigabytes of Data ](https://www.reddit.com/r/LangChain/comments/15nl2b7/open_source_vector_embedding_pipeline_to_ingest/) , 2023-08-12-0909
```
🚀 Excited to announce the release of the initial version of our open-source vector embedding pipeline, VectorFlow! 🎉

Ou
r pipeline is built to embed large volumes of data quickly and reliably. While embedding a handful of PDFs for Q&A might
 seem straightforward, the real challenge arises when you're faced with ingesting gigabytes of unstructured data consist
ently and frequently.

With just a simple API request, you can effortlessly embed and store raw data in any vector datab
ase, eliminating the need for complex cloud infrastructure setups.

🔗 Check out our Github repo: [https://github.com/dga
rnitz/vectorflow](https://github.com/dgarnitz/vectorflow) and check out our website: [https://www.getvectorflow.com/](ht
tps://www.getvectorflow.com/)

For all the innovators working with vector databases, we're eager to hear your insights, 
feedback, and ideas for the roadmap! 🌐🔍📊🚀
```
---

     
 
all -  [ Unleash the Power of LLMs in Your Telegram Bot on a Budget ](https://www.reddit.com/r/TelegramBots/comments/15njryp/unleash_the_power_of_llms_in_your_telegram_bot_on/) , 2023-08-12-0909
```
Interested in supercharging your Telegram bot with large language models (LLMs)? Here's a concise guide:

* **Introducti
on**: Harness LLMs like llama2-chat and vicuna. The bot is hosted on Amazon's free-tier EC2, with LLM inference on Beam 
Cloud.
* **Telegram Bot Setup**: Initiate with u/botfather on Telegram, get your token, and start a conversation with yo
ur bot.
* **Hosting**: Deploy on Amazon’s free-tier EC2 instance. The guide provides steps from EC2 setup to bot launch.

* **LLM Integration**: Beam Cloud, an affordable choice, is used for LLM inference. The bot taps into langchain and hug
gingface.

🔗 [**GitHub Repo**](https://github.com/ma2za/telegram-llm-guru) 🔗 [**Full Medium Article**](https://medium.co
m/@saverio3107/crafting-a-cost-effective-llm-powered-telegram-bot-a-step-by-step-guide-4d1e760e7eec) 🔗 [**Join Medium fo
r More Updates**](https://medium.com/@saverio3107/membership)

Dive in, experiment, and enhance your Telegram bot's capa
bilities! Feedback and insights are welcome. 🚀
```
---

     
 
all -  [ How langchain isable to achieve (almost) perfect SQL query ? ](https://devblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/) , 2023-08-12-0909
```
Me and my time is working on how to implement a natural language to SQL query generation based on a database using Seman
tic kernel(SK).
Our approach was to give the Kernel (chains equivalent in SK) the schema of the database.
We also have t
o explicitly mentioned the values of certain columns to increase the performance.
We observe that only davinci is able t
o generate most appropriate SQL query compare to gpt-35-turbo.
The same is started by the following [article](https://de
vblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/) as well.

Interestingly langchain use
s gpt-35-turbo to create SQL query.So my question is what langchain is doing differently???
```
---

     
 
all -  [ Using Document metadata in ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/15niet1/using_document_metadata_in/) , 2023-08-12-0909
```
Hey, I need some help with my ConversationalRetrievalChain app.

For context i'm using RecursiveTextSplitter and FAISS t
o store the text of the PDFs i upload.   
I manually add the metadata to the Documents such as each chunk will have 'sou
rce' and 'page\_number'  
I'm then using a ConversationalRetrievalChain.from\_llm alongside SystemMessagePromptTemplate 
and Human... that feed in a ChatPromptTemplate.

Now that you know the basic arch, here is the problem.  
When I upload 
multiple documents, I want to be able to look for an answer that says:  
' This doc says X, this doc says Y'  


Because
 I am using the RecursiveTextSplitter, the chunks I get are all Documents according to llm.   
So even if I upload 2 pdf
s only, i get an answer relative to:  
'Doc 1 says z, Doc 2 says x, Doc 3 says c, Doc 4 says d'  
Because it doesn't hav
e context of what document belongs to which pdf.   


What I want to do is let the llm tap into the Metadata of each chu
nk to support its explanation. Then instead of showing multiple documents, it will pinpoint which chunks belong to which
 document.   
Any help is appreciated
```
---

     
 
all -  [ Struggling with 404 Errors in LangChain: How Can I Ensure Valid Webpage Links? ](https://www.reddit.com/r/LangChain/comments/15nemtf/struggling_with_404_errors_in_langchain_how_can_i/) , 2023-08-12-0909
```
Hi everyone, I've been working with LangChain and SerpAPI to retrieve webpage links for a project. Unfortunately, I've e
ncountered an issue where some of the links are returning a '404 Page Not Found' error. I want to ensure that the links 
I'm retrieving are both accessible and available. Can anyone provide guidance or suggestions on how to verify the validi
ty of these links or filter out the ones that are not working? Thanks in advance for your help!
```
---

     
 
all -  [ Open source Facebook/ig/whatsapp messenger chatbot with langchain ](https://www.reddit.com/r/LangChain/comments/15ne3rt/open_source_facebookigwhatsapp_messenger_chatbot/) , 2023-08-12-0909
```
Basically what the tittle says, Im developing a private software right now but in my journey to learn using langchain an
d some other API tests I used Facebook messenger as my UI instead of making one (no domain,no fees,no database necessary
) to test some basic to advanced features of a chatbot, let it be a simple chat chain Q&A with DB queries or a full fled
ge agent like auto-gpt(non multi-agent). Here’s my deal. I’m creating the github open source because i haven’t seen(last
 time I checked) a complete repo for this, I belive is of value for begginer/intermediate level for developers of Llm ap
ps to start here with the merge of good ui/ux (we use it all the time no designing thinking is required) and can be furt
her improved(reduced response time,local LLMs, speech2text,text2image,file2text) I wanna know if some of you are looking
 for this or interested enough to make the complete guide and start a discord sever for further development in GitHub re
pository.

Extra:
As my own point of view, I hope many of us share the same excitement of working with bleeding edge tec
hnology of AI and so do big industries are(Facebook buying Llama , “X” with the account verification, KhanAcademy with C
hatGPT tutor…) but for now they only live in the software environment(I hope sooner or later boston dynamics just connec
ts to the  mic array and a speaker with gpt api to a spot) so the main road for the LLMs is to grow popularity in the vi
rtual space.As for now they work mainly for category of virtual assistant and that globally would be condensed into thes
e category always… until we can have friendly talks over the internet with out any propuse or objective making it the du
mbest/smartest virtual friend/Teacher, and creating engienieering parts for cars, developing new instruments or solution
s for the applied science, we are gradually looking at this but for now the more virtual agent populate the platforms th
e more we can socially experiment and as mentioned before the industires for sure may see this as competition, and if th
ere’s a way to eradicate this they would love to do it and make it their own or worse . They would never able to reach t
he same power as they could do in the earlier years mostly because of the lack of control…This is just a smart part of t
he model which makes me feel like I don’t have a bicycle for the mind but a Raptor F-22.
```
---

     
 
all -  [ Is there any way to show the verbose in our streamlit UI ](https://www.reddit.com/r/LangChain/comments/15ndsq5/is_there_any_way_to_show_the_verbose_in_our/) , 2023-08-12-0909
```
I am working on a project on agents that can show verbose in terminal but not in UI is there any way to show this ??
```
---

     
 
all -  [ After spending 1,000+ hours building AI chatbots, here’s why you shouldn’t build your own ](https://www.reddit.com/r/SaaS/comments/15n8ua8/after_spending_1000_hours_building_ai_chatbots/) , 2023-08-12-0909
```
I’ve personally spent over 1,000 hours building AI chatbots.

Here’s what I’ve learnt over the last 6 months, and why I 
think the majority of businesses are wasting a huge amount of time and resources when they decide to “build their own” A
I chatbots.

Consider this, would you build your own enterprise search for your business?

## ✅ Why you should build you
r own AI chatbot

“*It’s never been easier to build an AI chatbot”* — no doubt you’ll have heard this countless times in
 all those daily AI newsletters.

You’ve probably been eyeing up [Langchain](https://python.langchain.com/docs/get_start
ed/introduction.html) or [Llama Index](https://www.llamaindex.ai/), read their docs and a few tutorials, and fancy deplo
ying your own AI bot in a weekend hack.

In fact, here’s exactly how you’d do it:

1. Fetch, transform, and ingest your 
data into a [vector database](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
2. Spin up a chat
 interface from a [template](https://vercel.com/templates/next.js/nextjs-ai-chatbot)
3. Connect to a super-intelligent A
I model, like [OpenAI’s ChatGPT](https://platform.openai.com/docs/models/gpt-3-5), that uses your content and can have a
 conversation with someone — answering their questions like an expert

Simple right?

After your weekend hackathon (and 
after you’ve shared your MVP with your team), you realize you want to take your AI chatbot to the next stage, after all,
 now you now have complete control over the:

* **Underlying data used by the chatbot** \- you can add all your private 
forecast reports or internal process docs and learning materials.
* **User interface and branding -** you can make it fe
el like it’s *really* a part of your existing stack.
* **Data privacy and security -** you can decide what happens to a 
user's chat history, or how ingested data is stored and processed. If your data is particularly sensitive, this may even
 be table stakes.
* **Access to your secure or private systems  -** systems that you wouldn’t want to expose to a 3rd Pa
rty.

All sounds good, right? But there are some pretty significant drawbacks, and there are some things your team will 
*need* in order to make a success of this.

## ❌ Why you shouldn’t build your own chatbot

Nothing is ever as easy as it
 seems.

As useful as the frameworks and libraries are to get you started quickly, they hide a lot of detail and a long 
list of small decisions that all add up to have a significant impact on the quality of your chatbot (and the risk to you
r business).

Here are all the things you’ll need to consider and stay on top of if you are going to build yourself:

* 
**Initial business case:** A custom AI chatbot for a business is [estimated to cost upwards of $50,000](https://hyperise
.com/blog/how-much-does-it-cost-to-develop-a-chatbot) and these costs can quickly spiral upwards for use cases that requ
ire a high degree of accuracy or where a company has large volumes of content for the chatbot to access. You will need t
o justify this to management, likely before you can demonstrate the actual value.
* **AI expertise:** You’ll need people
 in the business who understand how LLMs work at a high level. Especially what they can’t do. This expertise will be ess
ential if you want your chatbot to be more than just a novel toy for customers or employees (better start actually readi
ng that AI book you bought yourself to “get up to speed”)
* **Product continuity:** What happens when you leave? Looking
 forward to having to document how your AI chatbot works for the next person or team?
* **AI provider and model selectio
n:** You’ll need to decide on which AI provider you partner with and which AI model you want to use. This will involve w
eighing up the Pros and Cons and trade-offs you’ll need to make e.g. Speed vs. Cost vs. Quality
* **Keeping up with AI d
evelopments:** You’ll need a team to constantly stay on top of the latest AI developments to make sure your chatbot is l
everaging the newest tech. But importantly, to make sure you’re not reliant on methods that are being phased out. We’ve 
seen changes to AI models that change answer quality overnight, the solutions for which, never seem to be straightforwar
d!
* **Preparing your data and content**: The data processing stage is crucial, this is where your content is manipulate
d into an optimal format for AI models to use. There are 20+ small, technical, decisions packed into just this topic and
 hundreds of edge cases to consider (did you know Arabic takes up 4x as many tokens as English for example?). There are 
already large groups of companies dedicated to solving just this problem, like [carbon.ai](http://carbon.ai) and [psychi
c.dev](http://psychic.dev)
* **Automated chat testing:** You’ll have to define a testing approach to understand how chan
ges you make affect the quality of your chatbot. The biggest challenge here is the sheer number of permutations that are
 available to you. We worked out there are over 1 million combinations today, and this grows with every new model and pa
rameter. With each permutation, you have to test your AI chatbot like real humans would — but in an automated way, at sc
ale, to be meaningful.
* **Integrations:** Do you want to integrate your chatbot with Slack or Teams? Or embed it on you
r website? These are all additional features that need to be built and approvals for them takes months with A LOT of bac
k and forth on minor details.

We live and breathe all these topics and challenges every day (and even for us some days 
they can feel overwhelming!). But we specialise, deeply, in all these areas with a single goal: creating the best AI cha
tbot to provide answers based on your content.

## Why reinvent the wheel?

Now, back to our enterprise search analogy. 
You wouldn’t consider building it yourself, even though it is fundamental in helping your teams locate the right content
 or data. You know how intricate and specialized the art of *good* search is. AI chat is much the same but with *much* m
ore uncertainty.

You also have to ask yourself if there aren’t more important challenges to be working on in your busin
ess? For instance, considering where AI fits more strategically, instead of how you are going to pre-process 5,000 PDF r
eports.

So, after 1,000+ hours building AI chatbots, I’m confident when I say that for 90%+ of businesses, buying in yo
ur AI chatbot solution is the way to go, but if you are still not convinced, here is the breakdown to help:

||If you wa
nt to BUILD…|If you want to BUY…|
|:-|:-|:-|
|AI capability and knowledge|Existing internal AI capability or expertise|L
imited or no existing AI knowledge in the business|
|Data sensitivity|Highly sensitive data is required for the AI chatb
ot to access|Private (not highly sensitive) or public data and content|
|Content type|Business content is static and lim
ited to <500 items/reports/documents|Business content can be dynamic, growing, and, available in large volumes of >1,000
 items/reports/documents|
|Dedicated team|Ability to dedicate a team to building and managing an AI chatbot|Objective to
 integrate AI chatbot capability into an existing team to manage (like enterprise search)|
|Chatbot as core differentiat
or|You expect an AI chatbot to be a significant differentiator and part of your business’s offering|An AI chatbot will l
everage or enrich your business’s existing core offering e.g. your editorial trend reports|

And while you may think tha
t Slack or Teams integrations, personalization, data security, and enterprise controls are other reasons to build your o
wn. With most providers, these features come out of the box.

Of course, your ‘buy instead of build’ strategy may change
 over time. For example, if your chatbot becomes a central part of your business offering or how it works, then it might
 justify the investment to build your own at some stage. But initially, while you dip your toes to see where generative 
AI solutions, like a chatbot, fit within your business. It’s probably best to just optimize for learning quickly and get
ting something live.

## So, what next?

The best thing you can do for your business is to start. Today.

The average [m
yaskai.com](https://myaskai.com/?utm_source=reddit&utm_medium=organic&utm_content=why-not-build) customer has their firs
t AI chatbot live in under 10 mins.

I’ve now helped over 30,000 businesses build an AI chatbot, trained on their own da
ta and content, branded and personalized, and launched to where their customers or employees most need it.
```
---

     
 
all -  [ Increasing the performance of retrievers ](https://www.reddit.com/r/LangChain/comments/15n8n06/increasing_the_performance_of_retrievers/) , 2023-08-12-0909
```
I have noticed that I am being faced with a lot of inconsistencies when it comes some answers. I am already using a cust
om router and a custom agent, but I am using the retrievers that comes with each vectorstore. But I realised that even w
hen saving the vectorstore and loading it, the performance of my chatbot has been inconsistent.  
Sometimes it answers a
 certain question, sometimes no. Sometimes I need to make very small changes into my input query for it to work. And the
n sometimes it just never finds the answer to my question, despite the answer being clearly found in the document.  
Thi
s is to note that I have already testing the different chunking approaches and found the one that apparently suits my da
ta the best. But I have no idea how to fix the inconsistency issue and how to increase the performance of the retriever 
after experimenting with both different embeddings and different vectorstores. and even different chain types.

Is there
 a way where I can first of all print the chunks that I am retrieving to make sure that when the chatbot states that he 
did not find the answer in the documents, the answer was really not in these chunks.  
What is some approaches I can tak
e to increase the consistency and performance of my retriever?
```
---

     
 
all -  [ Django eating up api calls during system checks. ](https://www.reddit.com/r/django/comments/15n8cli/django_eating_up_api_calls_during_system_checks/) , 2023-08-12-0909
```
I am in college and have this app I'm building with langchain and openAI. 
I'm using chatgpt 3.5T with it. 
Lately I saw
 increased quota usage ever since we started testing our app. Today I ran the app and saw that during system checks, it 
showed me the error that my openAI account has run out of usage credits. 

I've increased the limit by 2 dollars but I c
an't figure out how to stop the system checks from running the api calls again and again and eating up my credits while 
I change each line of code and test my app. 

Please help me out. Thank you.
```
---

     
 
all -  [ Using prompt templates after LoRA on raw text ](https://www.reddit.com/r/LocalLLaMA/comments/15n84m8/using_prompt_templates_after_lora_on_raw_text/) , 2023-08-12-0909
```
Hello all, 

I'm a little overwhelmed with all the developments and I feel like I don't know where to begin. So I apolog
ise if this question sounds very basic.

Let's say I want my LLM to sound like Phoebe Buffay from Friends. I don't have 
a QnA format, but just raw text for this purpose. 

As I understand, I can perform LoRA using the WebUI.

Once my fine t
uned model is ready, I want to use this to be able to converse with the user using specific prompts.

My question is, ca
n I feed this fine tuned model to LangChain so I can use their prompt template successfully? Or are there alternatives? 


Or can I do all of this using HuggingFace? 

Sorry, I'm very lost and I can't seem to understand if the finetuned mode
ls can be used by other frameworks.
```
---

     
 
all -  [ Help - Categorizing documents by content? ](https://www.reddit.com/r/LangChain/comments/15n6nld/help_categorizing_documents_by_content/) , 2023-08-12-0909
```
Does anyone know of a solution to categorize many documents into different headers based on their content? For example t
he prompt would be 'categorize which documents refer to concept x, y, and z.' 

Output:

X:
Doc 1,
Doc 52,
Doc 80

Y:
Do
c 7, Doc 52

Z:
Doc 2
```
---

     
 
all -  [ Best solution to deal with context and high token consumption ](https://www.reddit.com/r/OpenAI/comments/15n6b93/best_solution_to_deal_with_context_and_high_token/) , 2023-08-12-0909
```
Hi

I'm pretty new in this AI field and currently working on a mobile app chatbot. The AI part would

\- Have a specific
  behavior and multiple predefined tasks as the app is focused on a specific domain (health)

\- Connect to internal API
s to retrieve data from the project backend

For testing purposes, I am currently  storing user's history in a messages 
object in Mongo, then sending the whole history each time to GPT. When it's the very first call from the user I append t
he system instructions as the first prompt of the history.

The system instructions is by itself quiet token consuming a
nd the more messages get stored the faster I get limited by the API..

I heard about Rasa AI, Langchain, vectors DB, emb
edding and fine-tuning.

I tried to get GPT summarize the conversation each 10 or so messages but the result isn't  inte
resting (at all).

The ideal solution would be to host an open source AI somewhere in the future but I would like to hav
e some insights about what would be the best option  right now to handle this issue.

Thanks a lot.
```
---

     
 
all -  [ Return Source Documents (PDFs) with a source snippets. ](https://www.reddit.com/r/LocalLLaMA/comments/15n36uh/return_source_documents_pdfs_with_a_source/) , 2023-08-12-0909
```
Hi,
is it anyhow possible to return the source documents with a snippet in a PDF Q&A Chatbot of the sources the LLM was 
given for creating the answer?
I know that there is in langchain a function for that but in my case it's only giving me 
the name of the
PDF, not a snippet of the lines which were taken.
```
---

     
 
all -  [ Return Source Documents (PDFs) with a source snippets. ](https://www.reddit.com/r/LangChain/comments/15n33ea/return_source_documents_pdfs_with_a_source/) , 2023-08-12-0909
```
Hi,

is it anyhow possible to return the source documents with a snippet in a PDF Q&A Chatbot of the sources the LLM was
 given for creating the answer? 

I know that there is in langchain a function for that but in my case it’s only giving 
me the name of the PDF, not a snippet of the lines which were taken.
```
---

     
 
all -  [ CtrlX Search - New paradigm of video search ](https://www.reddit.com/r/LangChain/comments/15n323s/ctrlx_search_new_paradigm_of_video_search/) , 2023-08-12-0909
```
Hey everyone 🙂

We've developed an exciting beta testbed over at [CtrlX Video](https://dev.ctrlx.video/?utm_srouce=reddi
t-langchain). It’s an engine that enables deep searches within videos using AI. Here's a brief overview:

• Search capab
ilities: Extract key video features like actions, objects, on-screen text, speech, and more.

• Fast Search: Convert vid
eo info into vector representations for quick, scalable semantic search.

• Potential Uses: From contextual advertising 
to content moderation and even natural language-based CCTV footage search.

• API Integration: Easy integration for devs
 to make videos searchable with just a few API calls. We're seeking feedback to refine it further. Please check out our 
playground, loaded with sample YouTube videos (total 10 hours, 170 vids) for you to try.

https://i.redd.it/91rxlmi8x7hb
1.gif

Feel free to reach out if you'd like to explore the API or upload your own videos. \[email: [xavier@ctrlx.video](
mailto:xavier@ctrlx.video)\] Your insights will be invaluable! 🙏
```
---

     
 
all -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-08-12-0909
```
would it be possible to train or fine-tune a small (1-3B) model who's sole purpose is to perform function calls? similar
 to how we have tiny models like replit-v2-3B that are super capable at specific things like code auto-complete .  


i 
know that's how openAI implemented function call was by fine-tuning gpt-3.5/4 but I'm thinking just a straight up base m
odel trained to understand and excel at function calls (similar to Gorilla for apis)

i'm thinking it would be a perfect
 'glue' for bigger LLM apps-- avoiding the need for external tools like langchain/quidance/etc...
```
---

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-12-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-12-0909
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to  Nvidia GPU and Metal acceleration for GGML models !

Here is the project  link: [Cria- Local
 LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Langc
hain\` example in the project).

This is an ongoing project, I have implemented the \`embeddings\` and \`completions\` r
outes. The \`chat-completion\` route will be here very soon!

Really interested in your feedback and I would welcome any
 help :) !

&#x200B;

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-12-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-12-0909
```
 I worked for less than a year as a Data Engineer. I decided to look for other challenges and got a job as an AI enginee
r developing language models.

The product of the company that hired me is related to data and metadata management. My t
asks will be to introduce features to the product, including a chat function that will allow for asking questions about 
data. Other tasks will include research and proposing additional AI-related functionalities to the product (on premise).
 I have a two weeks left to start work and I need to prepare a bit. My job will involve implementing ready-made solution
s and conducting research (high level - I need to implement valuable features and no one cares how).

**What are the mos
t important things I should learn before starting work?**

First of all, I replicated a few applications from this blog:
 [https://blog.streamlit.io/tag/llms/](https://blog.streamlit.io/tag/llms/)

Then I have focused on Langchain. I'm also 
in the middle of a course on Udemy about Next-Gen AI projects - Beginner friendly - Langchain, Pinecone - OpenAI, Huggin
gFace & LLAMA 2 models

I need a roadmap that will guide me a bit. I'm looking for blogs/materials/courses that will giv
e me practical knowledge in this matter.
```
---

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-12-0909
```
I have a data set that isn't that large \~200 pdfs. I have done the regular RAG approach with Langchain, extracting text
, splitting into chunks, embedding with OpenAi embeddings and FAISS vector storage. However, when I do a similarity sear
ch with a question I would like answered it returns the wrong context. The documents are semi-structured information of 
examined bridges. A question I would like answered is f.e. 'what is the construction date of bridge X?'. When I input th
is question I get a lot of context of construction dates of other bridges. I think this is because the bridges are not e
xplicitly mentioned in the text. I tried adding the bridge name and document name to the page content string of the chun
ks, but this does nothing.

Does anyone have any tips on improving the embeddings retrieval in this case?
```
---

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-12-0909
```
I am running text inferencing on Llama2-7b through langchain. I have downloaded the model from langchain's Huggingface l
ibrary, and I am running the model on AWS ml.g4dn.12xlarge which has 4x**nvidia t4**, which gives a total 64GB of GPU me
mory and 192GB of normal memory. It is able to answer my queries in around 10 seconds for small queries, and upto 3 mins
 for big queries.

The task I am doing is retrieving information from a document(Understanding Machine Learning PDF) in 
a conversational way. I've extracted the main parts of the notebook and put it up [here](https://colab.research.google.c
om/drive/1uFNkZ6FI0qffwRpW6ubfdq0HrCqcqVUi?usp=sharing).

Where can I make changes to speed up the transaction. Is there
 any change I can do in the model configuration to speed it up? Because if I use HuggingFaceHubAPI, it is able to give a
n answer in less than 5 seconds. Are there any other areas I can optimise?

I appreciate any help you can provide. Thank
s!
```
---

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 2023-08-12-0909
```
Hey [r/MachineLearning](https://www.reddit.com/r/MachineLearning/),

The team at TruEra recently released an open source
 project for evaluation & tracking of LLM applications called [TruLens-Eval](https://github.com/truera/trulens/tree/main
/trulens_eval). We’ve specifically targeted retrieval-augmented QA as a core use case and so far we’ve seen it used for 
comparing different models and parameters, prompts, vector-db configurations and query planning strategies. I’d love to 
get your feedback on it.

The core idea behind the project is feedback functions. Analogous to labeling functions, feedb
ack functions are models used to score the text produced by LLMs. We already have a variety of out-of-the-box feedback f
unctions to use for eval including relevance, language match, sentiment and moderation that can be applied to inputs, ou
tputs or intermediate steps of your application.

On top of eval, there’s also built-in tracking of cost and latency.

W
e made it easy to integrate with different setups using connectors for langchain, llama-index + an option to use it with
out a framework.

[Langchain Quickstart Colab](https://colab.research.google.com/github/truera/trulens/blob/releases/rc-
trulens-eval-0.5.0/trulens_eval/examples/colab/quickstarts/langchain_quickstart_colab.ipynb)

[Llama-Index Quickstart Co
lab](https://colab.research.google.com/github/truera/trulens/blob/releases/rc-trulens-eval-0.5.0/trulens_eval/examples/c
olab/quickstarts/llama_index_quickstart_colab.ipynb)

[No Framework Quickstart Colab](https://colab.research.google.com/
github/truera/trulens/blob/releases/rc-trulens-eval-0.5.0/trulens_eval/examples/colab/quickstarts/no_framework_quickstar
t_colab.ipynb)

Last, the project comes with a streamlit dashboard for visualization of your experiments and associated 
metrics.

[TruLens dashboard for comparing different app versions](https://preview.redd.it/q68b1l27pycb1.jpg?width=1233&
format=pjpg&auto=webp&s=cfb1704624a8b6642b249a32d0afee85ea9f62d9)

Please let us know what you use this for or if you ha
ve feedback! And thanks to all contributors to this project and the open source community!
```
---

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 2023-08-12-0909
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
MachineLearning -  [ '[N]' '[D]' Langchain? What is it?? ](https://www.reddit.com/r/MachineLearning/comments/150mzax/n_d_langchain_what_is_it/) , 2023-08-12-0909
```
want to know more about Langchain  
Check out [https://nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf](https:
//nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf)
```
---

     
 
MachineLearning -  [ [D] The Problem With LangChain ](https://www.reddit.com/r/MachineLearning/comments/14zlaz6/d_the_problem_with_langchain/) , 2023-08-12-0909
```
https://minimaxir.com/2023/07/langchain-problem/

tl;dr it's needlessly complex, and I provide code examples to demonstr
ate such.

A few weeks ago when I posted about creating a LangChain alternative to /r/MachineLearning, most of the comme
nts replied 'what exactly is the issue with LangChain', so I hope this provides more clarity!
```
---

     
 
MachineLearning -  [ [D] 📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1) ](https://www.reddit.com/r/MachineLearning/comments/14xww89/d_the_learning_corner_andrew_ng_free_ai_courses/) , 2023-08-12-0909
```
📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1)

This is a list of some of the best Ai Free courses by Andrew NG
, we will release the second part of the list on our next newsletter installment (link)

* [**Generative AI with Large L
anguage Models**](https://www.deeplearning.ai/courses/generative-ai-with-llms/?utm_campaign=gaia-launch&utm_content=2545
85614&utm_medium=social&utm_source=linkedin&hss_channel=lcp-18246783)
* [**LangChain: Chat With Your Data**](https://www
.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
* [**LangChain for LLM Application Development**](https:/
/learn.deeplearning.ai/langchain)
* [**How Diffusion Models Work**](https://learn.deeplearning.ai/diffusion-model)
```
---

     
 
MachineLearning -  [ [P] langchain-lite alternative ](https://www.reddit.com/r/MachineLearning/comments/14xf9xb/p_langchainlite_alternative/) , 2023-08-12-0909
```
Although langchain is an impressive library, I tend to find it is…

* a little unintuitive, at least for non-trivial exa
mples or examples that don’t have a predefined chains/templates
* related, it's overly prescriptive; and the various lev
els of abstraction don't resonate with me
* related, can be difficult to debug or understand what’s happening in interme
diate steps of the chain or what’s it’s actually sending OpenAI

So, I built a “langchain-lite” package called `llm-work
flow`

https://github.com/shane-kercheval/llm-workflow

The value proposition is basically:

* easily build up a sequenc
e of tasks (e.g. prompt-template -> chat) called a workflow, where the output of one task serves as the input to the nex
t task in the workflow
* **track history**; understand what's happening in each of the tasks; **aggregate token usage, c
osts, etc. across the workflow**

So a workflow can be anything from `prompt -> chat -> response` to `prompt -> web-sear
ch -> web-scraping -> vector-database & retrieval -> modified prompt -> chat -> response`.

Here's an example of a 'prom
pt enhancer' workflow, where the user provides a prompt, one model enhances/improves the prompt, and the second model an
swers the question based on the enhanced prompt.

```python
prompt_enhancer = OpenAIChat(...)
chat_assistant = OpenAICha
t(...)

def prompt_template(user_prompt: str) -> str:
    return 'Improve the user's request, below, by expanding the re
quest ' \
        'to describe the relevant python best practices and documentation ' \
        f'requirements that shou
ld be followed:\n\n```{user_prompt}```'

def prompt_extract_code(_) -> str:
    # `_` signals that we are ignoring the i
nput (from the previous task)
    return 'Return only the primary code of interest from the previous answer, '\
        
'including docstrings, but without any text/response.'

workflow = Workflow(tasks=[
    prompt_template,      # modifies
 the user's prompt
    prompt_enhancer,      # returns an improved version of the user's prompt
    chat_assistant,     
  # returns the chat response based on the improved prompt
    prompt_extract_code,  # prompt to ask the model to extrac
t only the relevant code
    chat_assistant,       # returns only the relevant code from the model's last response
])
pr
ompt = 'create a function to mask all emails from a string value'
response = workflow(prompt)
```

The `response` is: `d
ef mask_email_addresses(string): .....`

We can view the history, which includes the prompts/responses/tokens/etc. for e
ach interaction:

```python
print(workflow.history())
```

Output:

```
[
    ExchangeRecord(prompt='Improve the user's 
request, below, by ...', response='Create a Python function that adheres to best practice...', timestamp='2023-07-12 04:
45:04.703', cost=0.00063, total_tokens=333, prompt_tokens=58, response_tokens=275),
    ExchangeRecord(prompt='Create a 
Python function that adheres ...', response='Sure! Here\'s an example of a Python function that adh...', timestamp='2023
-07-12 04:45:14.696', cost=0.00149, total_tokens=820,  prompt_tokens=292, response_tokens=528),
    ExchangeRecord(promp
t='Return only the primary code of intere...', response='```python\nimport re\n\ndef mask_email_addresses(strin...', tim
estamp='2023-07-12 04:45:18.875', cost=0.00167, total_tokens=1051, prompt_tokens=850, response_tokens=201)
]
```

We can
 also summarize costs/tokens/etc.

```python
print(workflow.sum('cost'))             # 0.0034
print(workflow.sum('total_
tokens'))     # 1961
print(workflow.sum('prompt_tokens'))    # 1104
print(workflow.sum('response_tokens'))  # 857
```

M
ore examples can be found here: https://github.com/shane-kercheval/llm-workflow/tree/main/examples

Feedback welcome.
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-12-0909
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
