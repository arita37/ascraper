 
all -  [ Whats in your RAG setup? ](https://www.reddit.com/r/LocalLLaMA/comments/1apcqq4/whats_in_your_rag_setup/) , 2024-02-13-0910
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
all -  [ Whats your RAG setup? ](https://www.reddit.com/r/LLMDevs/comments/1apcmxt/whats_your_rag_setup/) , 2024-02-13-0910
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;

&#x200B;

```
---

     
 
all -  [ LlamaIndex or LangChain with LlamaIndex for RAG with documents ](https://www.reddit.com/r/LocalLLaMA/comments/1ap7hrt/llamaindex_or_langchain_with_llamaindex_for_rag/) , 2024-02-13-0910
```
My goal is to create a chatbot to do Q&As with documents. Do I need to learn both LangChain and LlamaIndex? Or just Llam
aIndex would be sufficient? In other words, for my intended applications, what will I miss if I just use LlamaIndex with
out LangChain? Thanks.
```
---

     
 
all -  [ Please help on some technical questions re: building a RAG chatbot system ](https://www.reddit.com/r/LangChain/comments/1ap6waq/please_help_on_some_technical_questions_re/) , 2024-02-13-0910
```
 Hi I am attempting to build a end-to-end chatbot (using Langchain) with retrieval functionality with basically 0 LLM ex
perience and I would really appreciate it if I can get some tips. High-level speaking I am trying to build a chatbot tha
t I can program with natural language instructions and have the bot retrieve the right information based on natural lang
uage instructions.

Basically the architecture of the RAG chatbot includes the following components:

* **Client:** Rece
ives query from the user.
* **Instruction module:** Conditional statements in natural language format such as 'if user a
sks about X, then go to Y website and download Z'.
* **Retrieval module:** Takes programmatic instructions based on the 
Instruction module and fetch the instructed data.
* **Interpreter module:**  


1. Analyzes user query to fetch relevant
 instructions from the Instruction module, if none found then skip

* 2) Translates relevant instructions from natural l
anguage to programmatic instructions
* 3) Send the programmatic instructions to the Retrieval module and initiate a proc
ess chain for getting the right data
* 4) Pass along the user query along with the fetched data to the LLM for analysis.


**Some questions I have are:**

* First is this even a reasonable or realistic architecture?
* What's the best way to 
build functions 1, 2, and 3 for the interpreter module?
* Do you have any recommended frameworks, processes, and archite
cture that can better achieve the intended functionalities?
```
---

     
 
all -  [ Evaluate my resume - Data Scientist positions, aiming for MAANGs. ](https://i.redd.it/20528f0u37ic1.jpeg) , 2024-02-13-0910
```

```
---

     
 
all -  [ Just found ctransformers doesn't work with Tokenizer ](https://www.reddit.com/r/LocalLLaMA/comments/1ap5xgl/just_found_ctransformers_doesnt_work_with/) , 2024-02-13-0910
```
I was looking for how to get the tokenizer from a GGUF model and realized it (almost) doesn't actually work.

Came acros
s this documentation on ctransformers ([https://pypi.org/project/ctransformers/#langchain](https://pypi.org/project/ctra
nsformers/#langchain)):

 

>To use it with 🤗 Transformers, create model and tokenizer using:  
>  
>`from ctransformers
 import AutoModelForCausalLM, AutoTokenizer model = AutoModelForCausalLM.from_pretrained('marella/gpt-2-ggml', hf=True) 
tokenizer = AutoTokenizer.from_pretrained(model)` 

I thought: 'Sweet, that's pretty easy!' But when I run it, `AutoToke
nizer.from_pretrained(model)` throws NotImplementedError.

https://preview.redd.it/66ic68kbw6ic1.png?width=1660&format=p
ng&auto=webp&s=a7652d0e36fc43882ec98957183f2c9c1a93d27f

  
Further search led me to [https://github.com/marella/ctransf
ormers/issues/184](https://github.com/marella/ctransformers/issues/184), which is this exact issue raised on ctransforme
rs repo back in Dec 2023. I haven't tried this but according to this the only solution is to downgrade transformers lib 
to 4.33, which rips a lot of features off. Also it looks like the not implemented error has been there all the time. Not
 sure what caused that breakage.

Just want to share my findings since it's pretty disappointing to find that such basic
 function is not working :(
```
---

     
 
all -  [ Control token size of a tool ](https://www.reddit.com/r/LangChain/comments/1ap2rr3/control_token_size_of_a_tool/) , 2024-02-13-0910
```
I have an agent which uses a custom tool to search and provide an output, my problem. Is many times the output of the to
ol which is being passes to. The llm surpasses the token limit, is there away to chunk the output of the tool and gather
 the responses and send the whole responses to the user?
```
---

     
 
all -  [ LangChain playlist with 60 tutorials ](https://www.reddit.com/r/learnmachinelearning/comments/1ap1uy7/langchain_playlist_with_60_tutorials/) , 2024-02-13-0910
```
Hey everyone, check out this LangChain (generative AI framework) playlist comprising of 60 tutorials explaining everythi
ng from scratch
https://youtube.com/playlist?list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ&si=8bXhqED-NiVITZK9
```
---

     
 
all -  [ Agents vs Chains ](https://www.reddit.com/r/generativeAI/comments/1ap1hf2/agents_vs_chains/) , 2024-02-13-0910
```
Hey everyone, check out how Agents are different from chains in LangChain in this new tutorial: https://youtu.be/A3Gm6KP
xy4k
```
---

     
 
all -  [ AI document jury ](https://www.reddit.com/r/LangChain/comments/1ap0pbx/ai_document_jury/) , 2024-02-13-0910
```
I need to make an AI that can judge a document based on some criteria. The criteria can be like:
- The document explains
 the market segmentation efficiently 
- The document mentions how market works and explaining each type of markets.

The
 AI will judge the document based on above criteria and will give a score. 
This is just a topic for example and the cri
teria and the document can be for other topics.

I have created a chatbot using RAG but for this one I still don't have 
a clue for the approach. Mainly because with chatbot, I retrieve like 5 nearest chunks by cosine similarity while for th
is one, I don't think retrieving nearest chunks by cosine similarity to the question will return all the chunks for the 
document part the criteria needs to judge. And I can't just give the LLM all chunks from the document right? Any advice 
for this one? Any help would be really appreciated.
```
---

     
 
all -  [ RAG Chatbot locally, beginner here ](https://www.reddit.com/r/LangChain/comments/1ap0fce/rag_chatbot_locally_beginner_here/) , 2024-02-13-0910
```
Hey, I'm a langChain beginner and I want to build an Chatbot application which will retrieve and run llm locally. I am u
sing Chroma to create and fetch from the vectorstore, and using Llama-7b for the llm. I want to use langserve and so i c
reate a server with the chain. I now will use streamlit to listen to that port and invoke the chain. I am stuck, because
 I am confused on how to store memory. I dont want to store it in the langchain server (as it would stored for every use
r the same. Correct me if I am wrong). So I want to store it in streamlit session state somehow and use buffer window in
 the langchain server. I am now very confused on what I should do. Need help, thanks!
```
---

     
 
all -  [ What happens if we send nodes again to chrome vector store ](https://www.reddit.com/r/LangChain/comments/1ap036k/what_happens_if_we_send_nodes_again_to_chrome/) , 2024-02-13-0910
```
If I have executed this code once and then run it again with different nodes. So what happens
1) does the new nodes get 
replaced by the older ones
2) it compares the new and older nodes and insert only those nodes that are new, keeping the 
older intact
3) it doesnt check and insert all the nodes(newer as well as older ones


import chromadb
chroma_client = c
hromadb.HttpClient(host='host', port=8000,)
from llama_index.vector_stores import ChromaVectorStore
from llama_index.pos
tprocessor.cohere_rerank import CohereRerank
chroma_collection = chroma_client.get_or_create_collection('collection')
ve
ctor_store6 = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context6 = StorageContext.from_defaults(vec
tor_store=vector_store6)
index7 = VectorStoreIndex(nodes=nodes, storage_context=storage_context6, service_context=servic
e_context)
```
---

     
 
all -  [ Website Scraping: Automatic CSS-Selector identification of the main textual content ](https://www.reddit.com/r/LangChain/comments/1aozqzh/website_scraping_automatic_cssselector/) , 2024-02-13-0910
```
The HTML code of many websites is very complicated. This is mainly because HTML is a markup language that is a mix of st
ructural, styling and text elements. It is also because many websites are overloaded with HTML tags and CSS instructions
. 

As a result, it can be a challenge to **identify the area** in the HTML code that represents **the main textual cont
ent** (e.g. for text extraction, vector databases or RAG applications).

In the following article, I show a **statistica
l-algorithmic approach** on how to determine the CSS selector(s) that represent the main content and filter out negligib
le elements.

https://developers-blog.org/python-website-scraping-automatic-selector-identification/

![enter image desc
ription here](https://developers-blog.org/wp-content/uploads/2024/02/visuzalisation-star-page-html-structure-and-depende
ncies-tree-54.png)
```
---

     
 
all -  [ Auto ai agent apps suggestion or something else? ](https://www.reddit.com/r/ChatGPT/comments/1aowboq/auto_ai_agent_apps_suggestion_or_something_else/) , 2024-02-13-0910
```
Please can you guide me towards a solution to learn for two projects?

**Request 1:**

**TLDR: Best easy UI app currentl
y for multi ai agent chained output to prompt auto workflow to assemble a larger prompt response output content (researc
h) document for each item line item (initia input to agent 1) in a google sheet or form input?**

Can you advise what is
 the easiest to use ai agent app with GUI that works on windows (python is ok if i must and ideally has some GUI but if 
there is an epic one without ill use it) to setup a step by step workflow easily that can take an initial input like a g
oogle sheet as the context and the first agent with use it plus its instructions and it will start its part of compiling
 a research report which is basically just prompt plus input and then sent result to the next agent who will use its out
put and their instructions to get more data and so on.   


So just steps and agents chained together one after the othe
r to fetch responses from the llm or their own tasks building on previous outputs, chatgpt API and I end up with a longe
r 5-10 page file of the output as a research report in chapters and it will do this report for each line in the google s
heet automatically and run as long as it needs to until its done? Like one of these? Autogen studio, Crewai, Chatdev, ai
agent dot app, llmstack, leapai. mindpal dot space has a nice multi agent assembly flow builder but no api input and out
put. Also something that can work with large documents well as inputs iedally for later project.

**Request 2:** **What 
is the best agent or bot large file handler/chat/processing app or stack where I can carefully auto scour multiple large
 documents and pull information from then all effectively** around a certain topic and create a long topic specific docu
ment for me just focused on the teaching on that subject pulled from the other large documents in a useful structured wa
y to make sense.

I guess agents that chat with eachother like a research project and it will make it easier as the data
 gets pulled in and they decide its context and where it must be in the new document and how its integrated with the res
t of the data pulled so far and then 1 but that keeps extracting new data from all the documents in a ongoing logical wa
y from the first to the last. Tried chat with do aps but output too small and cant automate workflows or multi agents.


What are the best tools for working with large documents currently, creating and extracting topical info for reseaand st
udy? Privategpt,, llama\_index, memgpt, langchain etc?

Thanks!
```
---

     
 
all -  [ Agent app suggestions please for 2 use cases ](https://www.reddit.com/r/AutoGPT/comments/1aovry9/agent_app_suggestions_please_for_2_use_cases/) , 2024-02-13-0910
```
Please can you guide me towards a solution to learn for two projects?

**Request 1:**

**TLDR: Best easy UI app currentl
y for multi ai agent chained output to prompt auto workflow to assemble a larger prompt response output content (researc
h) document for each item input item in a google sheet or form input?**

Can you advise what is the easiest to use ai ag
ent app with GUI that works on windows (python is ok if i must and ideally has some GUI but if there is an epic one with
out ill use it) to setup a step by step workflow easily that can take an inital input like a google sheet as the context
 and the first agent with use it plus its instructions and it will start its part of compiling a research report which i
s basically just prompt plus input and then sent result to the next agent who will use its output and their instructions
 to get more data and so on.   


So just steps and agents chained together one after the other to fetch responses from 
the llm or their own tasks building on previous outpits, chatgpt API and I end up with a longer 5-10 page file of the ou
tput as a research report in chapters and it will do this report for each line in the google sheet automatically and run
 as long as it needs to until its done? Like one of these? Autogen studio, Crewai, Chatdev, aiagent dot app, llmstack, l
eapai. mindpal dot space has a nice multi agent assembly flow builder but no api input and output. Also sometjing tha ca
n wrk with large documents well as inputs iedally for later project.

**Request 2:** **What is the best agent or bot lar
ge file handler/chat/processing app or stack where I can carefully auto scour multiple large documents and pull informat
ion from then all effectively** around a certain topic and create a long topic specific document for me just focused on 
the teaching on that subject pulled from the other large documents in a useful structured way to make sense.

I guess ag
ents that chat with eachother like a research project and it will make it easier as the data gets pulled in and they dec
ide its context and where it must be in the new document and how its integrated with the rest of the data pulled so far 
and then 1 but that keeps extracting new data from all the documents in a ongoing logical way from the first to the last
. Tried chat with do aps but output too small and cant automate workflows or multi agents.

What are the best tools for 
working with large documents currently, creating and extracting topical info for reseaand study? Privategpt,, llama\_ind
ex, memgpt, langchain etc?

Thanks!
```
---

     
 
all -  [ consistent memory ](https://www.reddit.com/r/Chatbots/comments/1aovrtd/consistent_memory/) , 2024-02-13-0910
```
Hello, I'm at the final steps in developing a chatbot using langchain, I'm facing a problem tho, when I run my chatbot o
n VS code, it forgets the previous conversation, however this does not happen on Jupyter Notebook, I've searched up and 
my problem might be variables consistency, is there a way to make it persistent in remembering previous conversation??  

If you guys think another problem might be the cause please tell me about it.  
Any help would be appreciated.  
Thanks
!
```
---

     
 
all -  [ Verbose for LCEL and for new agents (LangChain 0.1.0) ](https://www.reddit.com/r/LangChain/comments/1aovp1n/verbose_for_lcel_and_for_new_agents_langchain_010/) , 2024-02-13-0910
```
While working with LCEL and the newer way of handling agents in LangChain 0.1.0 i was wondering why verbose=true cant be
 set anymore. It was very useful for debugging and understanding the thought process of the agent. I know about the call
back handlers but i was wondering if there is a better and cleaner way, like the verbose=true in legacy LangChain.
```
---

     
 
all -  [ Search Product Catalog Images Using Azure Search and Azure OpenAI with LangChain ](https://www.reddit.com/r/AZURE/comments/1aovah9/search_product_catalog_images_using_azure_search/) , 2024-02-13-0910
```
 

In the ever-evolving landscape of retail, businesses are continually seeking innovative solutions to streamline their
 operations and enhance customer experiences. One such breakthrough is the implementation of artificial intelligence (AI
) to search product catalog images efficiently. This transformative technology not only simplifies the search process bu
t also empowers businesses to provide personalized and seamless shopping experiences for their customers. The Need for A
I in Product Catalog Image Search: Traditional methods of searching through product catalogs involve manual tagging and 
categorization, which can be time-consuming and prone to human error. As the volume of products in a catalog grows, mana
ging and searching for specific items becomes a daunting task.  
Here I have implemented a Fashion agent using Azure Sea
rch , Cognitive Services and GPT-4 with LangChain which can search product catalog to recommend write product to custome
r based on the requirement.  


[https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search
-and-openai-with-langchain-3a844bc5c27c](https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azur
e-search-and-openai-with-langchain-3a844bc5c27c)
```
---

     
 
all -  [ Journalist AI Review 2024 ](https://www.reddit.com/r/geniunereviewed/comments/1aouvr3/journalist_ai_review_2024/) , 2024-02-13-0910
```
&#x200B;

[Journalist AI Review 2024](https://preview.redd.it/wa4m5qez14ic1.png?width=1200&format=png&auto=webp&s=765739
b271e088a16269fc5dcdd845c38f8ff91c)

# Journalist AI Review 2024

**Journalist AI Review 2024: Hype or Hero?** Confused 
about Journalist AI's capabilities?\\

This in-depth review, based on thorough research, unravels its secrets.

Dive int
o its strengths, and weaknesses, and discover if it's your 2024 writing partner in crime!

**Key Takeaways:**

&#x200B;


* Journalist AI is an AI-powered writing tool designed to assist content creators, journalists, and marketers with gene
rating high-quality, SEO-optimized content.
* It offers features such as content generation in various formats, SEO opti
mization, image generation with Dall-e 3 integration, multilingual support through LangChain, and collaboration tools vi
a Google Docs integration.
* Pricing plans cater to individual and team needs, with varying content limits and feature a
ccess.
* User reviews highlight strengths like speed, efficiency, and high-quality output, but also mention potential we
aknesses in factual accuracy and creative control.

## Journalist AI Review 2024: Verdict

**Need fast, SEO-optimized co
ntent?** Journalist AI delivers, generating articles, blogs, and more. **Accuracy concerns linger,** so fact-checking is
 crucial. **Team features and image generation shine,** but limited creative control might leave some wanting more. **Id
eal for budget-conscious content creators comfortable with editing.** Explore alternatives for highly creative or techni
cal content. **Overall:** A helpful tool, but weigh your needs carefully before diving in.

[Try Journalist Ai Here](htt
ps://tryjournalist.com/?via=geniunereviewed)

## What is Journalist AI?

Journalist AI is an **AI-powered writing assist
ant** that leverages advanced algorithms to generate various content formats, including articles, blog posts, product de
scriptions, social media captions, and more. It is geared towards **content creators, journalists, marketers, and anyone
** seeking to **improve their content creation efficiency and quality**.

## Key Features of Journalist AI

Journalist A
I boasts a diverse range of features designed to empower users across the content creation spectrum. Let's explore some 
of the most notable ones:

### Content Generation

&#x200B;

* **Variety of formats:** Generate content in diverse forma
ts like articles, blog posts, product descriptions, social media captions, press releases, and more.
* **AI-powered writ
ing:** Advanced algorithms analyze your input (topic, keywords, tone) and generate unique, human-quality content.
* **Cu
stomizable style and tone:** Tailor your content to specific audiences and brand voices by adjusting the level of formal
ity, creativity, and humor.

### SEO Optimization

&#x200B;

* **Keyword research:** Identify relevant keywords to targe
t and optimize your content for search engine ranking.
* **Meta tag generation:** Automatically generate meta tags and d
escriptions that align with your target keywords.
* **Structured data markup:** Include structured data markup to enhanc
e search engine understanding and rich snippet visibility.

### Image Generation

&#x200B;

* **Dall-e 3 integration:** 
Leverage Dall-e 3's powerful AI to generate high-quality images that complement your content.
* **Contextual relevance:*
* Images are tailored to match your content's theme and topic for improved engagement.
* **Customization options:** Choo
se from various image styles and formats to suit your brand identity.

### Multilingual Support

&#x200B;

* **LangChain
 integration:** Translate your content into multiple languages seamlessly with LangChain's advanced translation technolo
gy.
* **Reach wider audiences:** Expand your reach to global audiences by creating multilingual content that resonates w
ith diverse cultures.
* **Quality assurance:** Maintain consistent messaging and brand voice across different languages.


### Collaboration Tools

&#x200B;

* **Google Docs integration:** Collaborate with team members in real-time by editin
g and providing feedback within Google Docs.
* **Streamlined workflows:** Facilitate seamless collaboration and content 
sharing within teams.
* **Improved efficiency:** Boost productivity by working together effectively on content projects.


## User Reviews and Testimonials (Continued)

**Positive reviews** of Journalist AI frequently highlight its:

&#x200B
;

* **Speed and efficiency:** Users appreciate the ability to generate content quickly and easily, saving them valuable
 time and effort.
* **High-quality output:** Many users commend the quality of the generated text, praising its natural 
language flow, grammar, and coherence.
* **Improved SEO:** Content creators value the built-in SEO optimization features
 that help their content rank higher in search results.
* **Easy to use interface:** The intuitive interface is lauded f
or its user-friendliness, making it accessible even for those with limited technical experience.

However, **negative re
views** sometimes mention:

&#x200B;

* **Factual accuracy:** Concerns exist regarding the potential for factual inaccur
acies, especially in technical or complex topics.
* **Limited creative control:** Some users feel restricted by the lack
 of fine-grained control over the creative aspects of the generated content.
* **Price:** While some find the pricing pl
ans affordable, others consider them expensive, especially for individuals or small businesses.
* **Customer support:** 
A few users express dissatisfaction with the quality or responsiveness of customer support.

It's important to remember 
that individual experiences can vary based on specific needs, expectations, and usage patterns. It's recommended to try 
the free plan or a trial period before committing to a paid subscription.

## Alternatives to Journalist AI

Several oth
er AI-powered writing tools compete with Journalist AI, each with its own strengths and weaknesses. Here are a few notab
le alternatives:

&#x200B;

* **Articoolo**: Offers a wider range of content formats and languages, but user reviews men
tion inconsistencies in quality.
* **Rytr**: Known for its affordability and user-friendly interface, but may lack custo
mization options compared to Journalist AI.
* **Writesonic**: Strong focus on long-form content and marketing copy, but 
pricing can be higher than Journalist AI.
* **Wordtune**: Primarily focused on rewriting and rephrasing existing content
, rather than generating original text.

Exploring these alternatives can help you find the best fit for your specific n
eeds and budget.

### Strengths and Weaknesses of Journalist AI

**Strengths:**

&#x200B;

* **Content quality:** Journa
list AI excels at generating grammatically correct, well-structured, and human-quality text that can serve as a solid fo
undation for further editing and refinement.
* **SEO optimization:** Built-in keyword research, meta tag generation, and
 structured data markup features effectively aid in content optimization for search engines, potentially boosting organi
c traffic.
* **Multilingual support:** Seamless integration with LangChain empowers content creators to reach global aud
iences by translating content into multiple languages, preserving brand voice and messaging.
* **Collaboration tools:** 
Google Docs integration streamlines team workflows, enabling real-time collaboration and feedback sharing, fostering con
tent creation efficiency.
* **Image generation:** Dall-e 3 integration offers a unique advantage, allowing users to crea
te high-quality, contextually relevant images that enhance content engagement and visual appeal.

**Weaknesses:**

&#x20
0B;

* **Factual accuracy:** While generally reliable, concerns remain regarding potential factual inaccuracies, especia
lly in complex or technical domains. Double-checking facts and conducting thorough research are crucial before publishin
g AI-generated content.
* **Limited creative control:** Users seeking highly creative or unique content might find the l
evel of control over style and tone insufficient. Exploring alternative tools with more granular control might be necess
ary for specific creative needs.
* **Learning curve:** While the interface is user-friendly, mastering advanced features
 and achieving optimal results might require some practice and experimentation.
* **Limited customer support:** User rev
iews suggest areas for improvement in customer support response time and comprehensiveness. Consulting online resources 
or communities might be necessary for certain troubleshooting needs.
* **Pricing:** Some users, particularly individuals
 or small businesses, might find the paid plans expensive compared to competitors. Carefully evaluating usage needs and 
budget constraints is essential before subscribing.

It's crucial to remember that strengths and weaknesses are relative
. Journalist AI's advantages might outweigh its limitations for specific users, while others might find alternative tool
s more suitable.

### Is Journalist AI Right for You?

Journalist AI can be a valuable tool for various user groups, dep
ending on their needs and expectations. Here's a breakdown:

&#x200B;

* **Content creators:** Ideal for bloggers, journ
alists, and marketers seeking to generate high-quality content quickly and efficiently, especially those comfortable wit
h post-editing to ensure factual accuracy.
* **Businesses:** Can benefit from SEO-optimized content creation, multilingu
al support, and team collaboration tools, particularly for marketing and communication teams.
* **Agencies:** Efficient 
content generation for client projects can be a time-saver, but careful review and editing are essential to maintain qua
lity standards.
* **Non-profit organizations:** Budget-friendly plans and the ability to create content in multiple lang
uages can be valuable assets for communication and outreach efforts.

However, if you prioritize:

&#x200B;

* **Highly 
creative content:** Explore tools offering more granular control over style and tone.
* **Absolute factual accuracy:** C
onsider tools specifically designed for technical writing or fact-checking.
* **Extensive customer support:** Opt for to
ols with readily available and comprehensive support options.
* **Free or very affordable solutions:** Explore freemium 
plans or budget-friendly alternatives.

Carefully assess your specific needs and priorities before making a decision.

#
## FAQs about Journalist AI

**Q: How accurate is the content generated by Journalist AI?**

A: While generally reliable
, factual accuracy, especially in complex topics, requires careful review and potential fact-checking before publishing.


**Q: Does Journalist AI plagiarize content?**

A: Journalist AI uses its own algorithms and does not directly copy con
tent from other sources. However, it's crucial to use it ethically and responsibly, ensuring originality and citing sour
ces if necessary.

**Q: Can I use Journalist AI for academic writing?**

A: While it can be a helpful starting point, us
ing AI-generated content directly in academic writing is generally not recommended due to potential plagiarism concerns.
 Always consult your instructor and adhere to academic integrity guidelines.

**Q: Does Journalist AI offer a free trial
?**

A: Yes, Journalist AI offers a free plan with limited content generation capacity. This allows you to test the tool
 and see if it meets your needs before committing to a paid plan.

**Q: What are the payment options for Journalist AI?*
*

A: Journalist AI accepts major credit cards and PayPal for paid subscriptions.

**Q: How does Journalist AI compare t
o other AI writing tools?**

A: Each tool has its strengths and weaknesses. Consider factors like content quality, featu
res, pricing, and ease of use when comparing options.
```
---

     
 
all -  [ let the context to keep track of all the files ](https://www.reddit.com/r/LangChain/comments/1aoulwf/let_the_context_to_keep_track_of_all_the_files/) , 2024-02-13-0910
```
Now chatgpt4 can track all the files we just uploaded in a conversation, and we can ask anything about a specific file, 
such as the name, let the model to search in a specific file.

I am wondering how we can do the same thing using langcha
in without using openai's retrivel tool?

Thanks in advance.
```
---

     
 
all -  [ Search Product Catalog Images Using Azure Search and OpenAI with Langchain ](https://www.reddit.com/r/LangChain/comments/1aou182/search_product_catalog_images_using_azure_search/) , 2024-02-13-0910
```
 In the ever-evolving landscape of retail, businesses are continually seeking innovative solutions to streamline their o
perations and enhance customer experiences. One such breakthrough is the implementation of artificial intelligence (AI) 
to search product catalog images efficiently. This transformative technology not only simplifies the search process but 
also empowers businesses to provide personalized and seamless shopping experiences for their customers. The Need for AI 
in Product Catalog Image Search: Traditional methods of searching through product catalogs involve manual tagging and ca
tegorization, which can be time-consuming and prone to human error. As the volume of products in a catalog grows, managi
ng and searching for specific items becomes a daunting task.  


Here I have implemented a Fashion agent using Azure Sea
rch , Cognitive Services and GPT-4 which can search product catalog to recommend write product to customer based on the 
requirement. 

[https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search-and-openai-with-
langchain-3a844bc5c27c](https://medium.com/@manoranjan.rajguru/search-product-catalog-images-using-azure-search-and-open
ai-with-langchain-3a844bc5c27c)
```
---

     
 
all -  [ Langchain powered search ](https://www.reddit.com/r/LangChain/comments/1aojxqa/langchain_powered_search/) , 2024-02-13-0910
```
I'm looking into LangChain to power search on some inventory. I would like to get parameters for this search from the de
scription to serve the customer. However, the customer should be able to ask his search query in any possible way, but o
bviously the API in the backend can support only a limited set of inputs.   


Exactly how would this work? And what too
ls should I consider? The idea is not to provide a response in the chat, but to provide it like an inventory search.  
```
---

     
 
all -  [ Building AI Chatbot from scratch with Llama2, Langchain and Vector database using RAG workflow ](https://www.reddit.com/r/artificial/comments/1aohn26/building_ai_chatbot_from_scratch_with_llama2/) , 2024-02-13-0910
```
Pretty detailed one in case any one wants to build one 
https://youtu.be/V8329yuXHKM
```
---

     
 
all -  [ LangChain and .NET ](https://www.reddit.com/r/dotnet/comments/1aoea8o/langchain_and_net/) , 2024-02-13-0910
```
I'm actively working on developing a new set of AI features available in VS Code, as part of SnippetHub, and next up is 
improving the context for AI features.

Given that the infrastructure is mostly on .NET technologies, I'm trying to figu
re out the best way to integrate LangChain with .NET.   
Is there a NuGet package available?

If you've had the chance t
o integrate LangChain into your .NET API, I'd appreciate it if you could share what the challenges were and if you used 
a NuGet package
```
---

     
 
all -  [ Better context with LangChain and VS Code AI coding assistant ](https://www.reddit.com/r/artificial/comments/1aoe4q8/better_context_with_langchain_and_vs_code_ai/) , 2024-02-13-0910
```
I'm actively working on developing new features for the AI coding assistant, which already has a VS Code extension where
 all the features are available.

To improve context in coding assistance (like AI Chat, AI Lens, and similar), I'm cons
idering what the best option would be. I've read a lot about LangChain and see that it offers some cool options for bett
er context when AI features come into play.

Has anyone integrated LangChain and what are your experiences? 

It would b
e great if someone could share specific use-cases from production and feedback.
```
---

     
 
all -  [ AI Assisted Assistant ](https://www.reddit.com/r/LangChain/comments/1ao7wte/ai_assisted_assistant/) , 2024-02-13-0910
```
Hey everyone, I’m about to build a Assistant which takes input from user like name, email and some other attributes and 
then check in the database to verify if the info already there or not, but after that it’ll ask some more follow up ques
tions to get input from user and verify more information in different format like pdf or jpeg.

Now I know it’s doable u
sing tools but exactly how? Because moving from one question to another question using API is getting boilerplate for me
, Is there any relevant or close enough resources available online to start? It’s just 1yr I’m into development so any h
elp will be appreciated.
```
---

     
 
all -  [ Finetuning Advice? ](https://www.reddit.com/r/LangChain/comments/1ao6rgk/finetuning_advice/) , 2024-02-13-0910
```
I am trying to finetune Llama2 7b on a single T4 GPU using Qlora, I found a lot of resources to help developing the pipe
line and everything is good, however I noticed something weird, everyone trying to finetune Llama2 7b using this method 
is setting max tokens(input+output) to **2048** although the maximum number of allowed tokens for Llama2 is **4092**, is
 the reason that long (inputs, outputs) pairs may need a bigger GPU? or I am missing something here.

I am asking this b
ecause my data contains long prompts and completions and I need to know if this effects how much GPU I'll need for finet
uning.
```
---

     
 
all -  [ Triform - Early Beta - Platform for Hosting and Orchestration of Python Focusing on LangChain ](https://www.reddit.com/r/LangChain/comments/1ao5p68/triform_early_beta_platform_for_hosting_and/) , 2024-02-13-0910
```
So we just opened up testing of a new platform called Triform. We have 400 registered users already, but still want more
 people to come in and check it out to be able to refine our product before we launch in production.

Anyone who signs u
p and creates at least one module and one flow in our testing system will get to keep a permanent free account on our pl
atform even in production.

Signup with your GitHub: [https://triform.ai](https://triform.ai)

Check out the readme at: 
[https://triform-docs.readthedocs.io/](https://triform-docs.readthedocs.io/)

Any and all feedback is appreciated!
```
---

     
 
all -  [ Multi-model architecture ](https://www.reddit.com/r/LangChain/comments/1ao2qn5/multimodel_architecture/) , 2024-02-13-0910
```
Does it make sense to ask several different llm and then consolidate the answers? If llm are trained on different data, 
it may help to get more diverse answers and improve results.
```
---

     
 
all -  [ Langchain RAG + CrewAI Agent? ](https://www.reddit.com/r/LangChain/comments/1anw9vt/langchain_rag_crewai_agent/) , 2024-02-13-0910
```
I seem to not be able to wrap my mind around it, but how do you feed a Langchain RAG implementation into an agent framew
ork like CrewAI? I can use both separately, but I'm not seeing how to combine the two... 
```
---

     
 
all -  [ Metadata retrieval + search ](https://www.reddit.com/r/LangChain/comments/1anuw6i/metadata_retrieval_search/) , 2024-02-13-0910
```
I am. Trying to implement a rag to discuss my data , I use chromadb and conversational retrievalchain. Let's say I uploa
d 20 documents,. 10 pdfs and 10 texts.  Everytime I aks a question to the ai I want in the answer to add the citation,  
also if I ask howamy pdf files are stored in the dB I want to know the number, I want also to. Ask find all the docs who
. Include this phrase and the ai should return me the filenames. To conclude, I want the ai to search not only the docs 
but the Metadata as well. Has anyone implemented something similar? Or has anything o suggest?

Thank you for your help 
😊
```
---

     
 
all -  [ Just got a 4090 24GB, what should I run? ](https://www.reddit.com/r/LocalLLaMA/comments/1anu3m5/just_got_a_4090_24gb_what_should_i_run/) , 2024-02-13-0910
```
I’m upgrading from a 3080 where I messed around with small models.   Anything bigger and better I should try out?

Espec
ially things that would help manage projects or document tasks or assistant like duties, I didn’t get into langchain, et
c. before but maybe worthwhile now, or with more horsepower?

Or maybe something that makes meme pictures of dogs?
```
---

     
 
all -  [ So is this sub gonna change its name to langchain-community? ](https://www.reddit.com/r/LangChain/comments/1anlp6l/so_is_this_sub_gonna_change_its_name_to/) , 2024-02-13-0910
```
I suspect this means they are gearing up for a paid subscription release. I updated and see that “langchain” is deprecia
ted… does this mean they are gearing up for a paid subscription version? *Microsoft Teams Classic has entered the chat *

```
---

     
 
all -  [ I don't understand....? ](https://www.reddit.com/r/LangChain/comments/1ankqzw/i_dont_understand/) , 2024-02-13-0910
```
Okay so when I'm looking at the documentation for langchain openapi toolkit, it is not making sense to me. 

I recreated
 this with my own API and yaml. I keep hitting the token limit because it feeds the entire yaml for reference. My tokens
 are 71k, just about the size of the one in the documentation. 

I would think the agent would use the documention as a 
resource, but not in sending the entire request. Maybe I'm not understanding this correctly, can someone please explain 
this to me? 

I get everything to run with all the authentication, but I keep hitting the token limit. What should I do?
 

https://python.langchain.com/docs/integrations/toolkits/openapi
```
---

     
 
all -  [ pinecone API ](https://www.reddit.com/r/StreamlitOfficial/comments/1anfqit/pinecone_api/) , 2024-02-13-0910
```
hello, I'm building a rag using langchain and Gemini, I'm stuck tho on the API part, how can I put my API online, I unde
rstand that you need to create a .env file for local deployment, but how exactly can I put my pinecone API online?
```
---

     
 
all -  [ Gemini + Google Search Agent Curious what you can build yourself in the @Google Gemini era? Spend a  ](https://www.reddit.com/r/chatgpt_newtech/comments/1anebts/gemini_google_search_agent_curious_what_you_can/) , 2024-02-13-0910
```
Gemini + Google Search Agent   Curious what you can build yourself in the  u/Google  Gemini era? Spend a few minutes wit
h LangChain  founding engineer  u/eyfriis  and quickly get up and running with a Gemini-powered agent that has access to
 Google Search  [http://aitutor21.com/bbs/board.php?bo\_table=news&wr\_id=2157](http://aitutor21.com/bbs/board.php?bo_ta
ble=news&wr_id=2157)
```
---

     
 
all -  [ Pipeline Vs Modular coding while creating LLM app ](https://www.reddit.com/r/TheLLMStack/comments/1ancqez/pipeline_vs_modular_coding_while_creating_llm_app/) , 2024-02-13-0910
```
Why every LLM framework is focusing more on creating pipeline based code structure to develop app? I can see langchain, 
llamaindex and haystack mostly focusing on developing app using pipelines rather then using individual modules. Is their
 particular advantage to this approach?
```
---

     
 
all -  [ How to fetch ID's in Pgvector ](https://www.reddit.com/r/LangChain/comments/1an9aw2/how_to_fetch_ids_in_pgvector/) , 2024-02-13-0910
```
Is there any way to  fetch ID's of a particular document stored in Postgres pgvector db to delete the particular documen
t embeddings.
```
---

     
 
all -  [ Langchain for QA ](https://www.reddit.com/r/LangChain/comments/1an90yi/langchain_for_qa/) , 2024-02-13-0910
```
Hello, everyone I created a python flask api for document chatbot.

Embedding with open ai and for Q&A Langchain Faiss i
s used.

Its take 2 sec to get the answer from chain I test this by adding time on evey step.

is there any way to make 
it fast? or other options.?

Its there any way i can make it fast?
```
---

     
 
all -  [ Data Insights suggestion using langchain ](https://www.reddit.com/r/LangChain/comments/1an371k/data_insights_suggestion_using_langchain/) , 2024-02-13-0910
```
 I'm facing a problem with Google Sheets while trying to analyze a dataset with over 100 records. It seems there's a tok
en issue preventing me from generating plots and insights effectively.

I'm using lanchains google drive library get the
 files and feeding them as docs and asking fixed question in  **response = chain.run(input\_documents=doc\_list, questio
n=prompt)**

Any quick fixes or alternative tools you recommend for handling large datasets?  


  
below is my code,  



 

from langchain import OpenAI  
import pandas as pd  
from langchain.sql\_database import SQLDatabase  
from langcha
in.chat\_models import ChatOpenAI  
from langchain.agents.agent\_toolkits import SQLDatabaseToolkit  
from langchain.age
nts import create\_sql\_agent,Tool,AgentType,initialize\_agent,create\_pandas\_dataframe\_agent  
from langchain.memory 
import ConversationBufferMemory  
import psycopg2  
import pymysql  
\# Setting up the api key  
import environ  
from l
angchain.document\_loaders import GoogleDriveLoader  
import os  
from langchain.llms import OpenAI  
from langchain.cha
ins.summarize import load\_summarize\_chain  
from langchain.chat\_models import ChatOpenAI  
import environ  
from lang
chain.chains.question\_answering import load\_qa\_chain  
env = environ.Env()  
environ.Env.read\_env()  
import json  

API\_KEY = env('apikey')  
   
def query\_agent(query):  
 '''  
Query an agent and return the response as a string.  
A
rgs:  
agent: The agent to query.  
query: The query to ask the agent.  
Returns:  
The response from the agent as a str
ing.  
'''  
 loader = GoogleDriveLoader(folder\_id='1YXa\_GCtVPu1MzK2tiW8J21CsNITHqKwl',  
 file\_types=\['sheet'\],  

 credentials\_path='credentials.json')  
 docs = loader.load()  
 llm = ChatOpenAI(temperature=0.6, openai\_api\_key=API
\_KEY,model='gpt-3.5-turbo-16k')  
 chain = load\_qa\_chain(llm, chain\_type='stuff')  
   
   
 titles = \[\]  # Initia
lize an empty list to store titles  
 for doc in docs:  
 if doc.metadata is not None and 'title' in doc.metadata:  
 ti
tle = doc.metadata\['title'\]  
 if title not in titles:  
 titles.append(title)  # Append the title to the list  
\#pri
nt(titles)  
 whole\_response = ''  
 google\_docs = \[\]  
 for title in titles:  
 print(f'---------------------------
-------------TITLE: {title}----------------------------------------')  
 doc\_list = \[\]  
 for doc in docs:  
 if doc.
metadata is not None and doc.metadata\['title'\] == title:  
 doc\_list.append(doc)  
 prompt = (  
 '''  
You are an AI
 assistant acting as a data analyst, you are presenting results to a dashboard.  
Please provide details about the data 
that is available in the following format:  
   
I Want the response only in below format for the given dataset:  
a pyt
hon dictionary with the following keys:  
{  
dataset\_name: will provide the Name of the dataset,  
data\_description: 
will provide a Description of the data,  
possible\_insights: \[will provide a python list of 3 possible meaningful bar 
or line plots that can be achieved from the data fields present in this data\], make sure you only suggest plots based u
pon fields available in this dataset.  
}  
'''   
)  
 response = chain.run(input\_documents=doc\_list, question=prompt
)  
   
   
 \# print('#############'+title)  
 \# print(response.\_\_str\_\_())  
 \# print('##############')  
 whole\
_response += '\\n' + response  
   
 \#filter  
 data\_dict = json.loads(response)  
 \#print(data\_dict)  
 data\_name 
= data\_dict\['dataset\_name'\]  
 data\_description = data\_dict\['data\_description'\]  
 possible\_insights = data\_d
ict\['possible\_insights'\]  
   
 \#prompt  
 for i in range(3):  
 plot\_prompt = (  
 '''  
You are an AI assistant a
cting as a data analyst, you are presenting results to a dashboard.  
you have the following data available - {name}, a 
little more about the data - {description}.  
based upon the data available, return information from data required to pl
ot the following - {plot}  
If the query requires creating a bar chart, reply as following string:  
 {{'bar': {{'column
s': \['A', 'B', 'C'\], 'data': \[\[valueA, valueB, valueC\], \[valueA, ValueB, valueC\]\]}}}}  
   
If the query require
s creating a line chart, reply as following string:  
 {{'line': {{'columns': \['A', 'B', 'C'\], 'data': \[\[valueA, val
ueB, valueC\], \[valueA, ValueB, valueC\]\]}}}}  
make sure to replace the columns and data with the actual data (from t
he provided data only) required to plot the chart, do all the required data processing like grouping data,aggregating ba
sed on condition for bar plot, and return response in the mentioned way only.  
don't forget to put all the strings in d
ouble quotes.  
'''.format(name=data\_name, description=data\_description, plot=possible\_insights\[i\])  
)  
 \#print(
f'##########################################PLOT PROMPT: {plot\_prompt}##########################################')  
 p
lot\_response = chain.run(input\_documents=doc\_list, question=plot\_prompt)  
 print(plot\_response.\_\_str\_\_() + '##
########################################')  


\# print('#############')  
 \# print(whole\_response)  
   
 \# # Conver
t the response to a string.  
 \# return response.\_\_str\_\_()
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-13-0910
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-13-0910
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-13-0910
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-13-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-13-0910
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-13-0910
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-13-0910
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-13-0910
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-13-0910
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

     
