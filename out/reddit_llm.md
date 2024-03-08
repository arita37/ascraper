 
all -  [ Tutorial on improving a Langchain RAG application using Evals, Tracing, and Playground. ](https://docs.parea.ai/tutorials/getting-started-rag) , 2024-03-08-0910
```

```
---

     
 
all -  [ How I Reduced Our Startup's LLM Costs by Almost 90% ](https://www.reddit.com/r/SaaS/comments/1b92w5o/how_i_reduced_our_startups_llm_costs_by_almost_90/) , 2024-03-08-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong. I know because I learned the hard way.

I’m not saying it’s hard per se, but as of this writing, gpt-4-tu
rbo costs $0.01/$0.03 per 1000 input/output tokens. This can quickly add up if you’re building a complex AI workflow.

Y
es, you could use less expensive, worse performing models, like GPT 3.5 or an open-source one like Llama, stuff everythi
ng into one API call with excellent prompt engineering, and hope for the best. But this probably won’t turn out that gre
at. This type of approach doesn’t really work in production—at least not yet with the current state of AI.

**It could g
ive you the right answer 90% or even 99% of the time.** But that one time it decides to go off the rails, it’s really fr
ustrating. As a developer and/or business, you know you must never break a user’s experience. It might be okay for a toy
 app or prototype but not for a production-grade application you charge for.

Imagine if Salesforce or any other establi
shed software company said its reliability was only one or two nines. That would be insane. No one would use it.

**But 
this is the state of most AI applications today. They’re unreliable.**

# AI isn’t a Universal Function

The non-determi
nistic nature of LLMs forces us to be more thoughtful about how we write our code. We should not just “hope” that an LLM
 will always correctly respond. We need to build redundancy and proper error handling. For some reason, many builders fo
rget everything they learned about software engineering and treat AI like some magical universal function that doesn’t f
ail.

**It’s not there yet.**

To fix this limitation, we must write code that only interacts with AI when absolutely ne
cessary—that is, when a system needs some sort of “human-level” analysis of unstructured data. Subsequently, whenever po
ssible, we must force the LLM to return references to information (i.e., a pointer) instead of the data itself.

**When 
I recognized these two things, I had to redesign the backend architecture of my personal software business completely.**


# Rearchitecting Jellypod

For context, I started an app called Jellypod. It enables users to subscribe to email newsl
etters and get a daily summary of the most important topics from all of them as a single podcast.

This seems pretty sim
ple on the outside—and the MVP honestly was. The app would just process each email individually, summarize it, convert i
t to speech, and stitch all the audio together, side-by-side, into a daily podcast.

The output was fine, but it needed 
to be better.

If two different newsletters discussed the same topic, the “podcast” would talk about it twice, not reali
zing we had already mentioned it. You could say, “Well, why don’t you just stuff all the newsletter content into one big
 LLM call to summarize everything?”

Well, that’s what I tried at first.

And it failed. **Miserably.**

Even with an ex
tremely detailed prompt using all the best practices, I couldn’t guarantee that the LLM would always detect the most imp
ortant topics, summarize everything, and consistently create an in-depth output. Also, the podcast always needed to be \
~10 minutes long.

So I went back to the drawing board. How can I make this system better? And yes, we’re getting to the
 cost reduction part - don’t worry!

# Defining the Requirements

Jellypod must be able to process any number of input d
ocuments (newsletters) and create an output that always includes the top ten most important topics across all those inpu
ts. If two subparts of any input are about the same topic, we should recognize that and merge the sections into one topi
c.

For example, if the Morning Brew has a section about US Elections and the Daily Brief also has a section on the curr
ent state of US Politics, they should be merged. I’ll skip over how I determined a similarity threshold (i.e., should tw
o topics be merged or remain separate).

# Exploding Costs

I built on top of a few different approaches outlined in pap
ers written by the LangChain community to semantic chunk and organize everything in a almost deterministic way.

**But t
his was INSANELY expensive.** The number of API calls grew at a rate of O(n log n), with n being the number of input chu
nks from all newsletters.

So, I had a dilemma. Do I keep this improved and more expensive architecture or throw it down
 the drain?

I decided to keep it and figure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool
 called OpenPipe that allows you to fine-tune open-source models almost too easily. It looked legit and was backed by YC
ombinator, so I gave it a try.

I swapped out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my
 LLM API calls to OpenAI but recorded all inputs and outputs. This created unique datasets for each of my prompts, which
 I could use to fine-tune a cheaper open-source model.

After about a week of recording Jellypod’s LLM calls, I had abou
t 50,000 rows of data. And with a few clicks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with 
the new fine-tuned model.

**And it reduced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tok
ens to $1.20. And cost per output token dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new arc
hitecture for approximately the same cost as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral ou
tput quality was just as high as GPT-4 by a series of evals and in-app customer feedback.

By redesigning the system to 
only use AI for the smallest unit of work it’s actually needed for, I could confidently deploy a fine-tuned model as a d
rop-in replacement for GPT 4. And by prompting to return pointers to data instead of the data itself, I could ensure dat
a integrity while reducing the number of output tokens consumed.

# In Conclusion

If you’re considering building an AI 
application, I would encourage you to take a step back and think about your architecture’s output reliability and costs.
 What happens if the LLM doesn’t answer your prompt in the right way? Can you prompt the model to return data identifier
s instead of raw data? And, is it possible to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights 
when I started, but hey, you live and learn.

I hope you found at least some parts of this interesting! I thought there 
were enough learnings to share. Feel free to reach out if you’re curious about the details.
```
---

     
 
all -  [ How I Reduced Our LLM Costs by Over 85% ](https://www.reddit.com/r/Entrepreneur/comments/1b92suo/how_i_reduced_our_llm_costs_by_over_85/) , 2024-03-08-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong. I know because I'm building one. 

I’m not saying it’s hard per se, but as of this writing, gpt-4-turbo c
osts $0.01/$0.03 per 1000 input/output tokens. This can quickly add up if you’re building a complex AI workflow.

Yes, y
ou could use less expensive, worse performing models, like GPT 3.5 or an open-source one like Llama, stuff everything in
to one API call with excellent prompt engineering, and hope for the best. But this probably won’t turn out that great. T
his type of approach doesn’t really work in production—at least not yet with the current state of AI.

**It could give y
ou the right answer 90% or even 99% of the time.** But that one time it decides to go off the rails, it’s really frustra
ting. As a developer and/or business, you know you must never break a user’s experience. It might be okay for a toy app 
or prototype but not for a production-grade application you charge for.

Imagine if Salesforce or any other established 
software company said its reliability was only one or two nines. That would be insane. No one would use it.

**But this 
is the state of most AI applications today. They’re unreliable.**

# AI isn’t a Universal Function

The non-deterministi
c nature of LLMs forces us to be more thoughtful about how we write our code. We should not just “hope” that an LLM will
 always correctly respond. We need to build redundancy and proper error handling. For some reason, many builders forget 
everything they learned about software engineering and treat AI like some magical universal function that doesn’t fail.


**It’s not there yet.**

To fix this limitation, we must write code that only interacts with AI when absolutely necessa
ry—that is, when a system needs some sort of “human-level” analysis of unstructured data. Subsequently, whenever possibl
e, we must force the LLM to return references to information (i.e., a pointer) instead of the data itself.

**When I rec
ognized these two things, I had to redesign the backend architecture of my personal software business completely.**

# R
earchitecting Jellypod

For context, I started an app called Jellypod. It enables users to subscribe to email newsletter
s and get a daily summary of the most important topics from all of them as a single podcast.

This seems pretty simple o
n the outside—and the MVP honestly was. The app would just process each email individually, summarize it, convert it to 
speech, and stitch all the audio together, side-by-side, into a daily podcast.

The output was fine, but it needed to be
 better.

If two different newsletters discussed the same topic, the “podcast” would talk about it twice, not realizing 
we had already mentioned it. You could say, “Well, why don’t you just stuff all the newsletter content into one big LLM 
call to summarize everything?”

Well, that’s what I tried at first.

And it failed. **Miserably.**

Even with an extreme
ly detailed prompt using all the best practices, I couldn’t guarantee that the LLM would always detect the most importan
t topics, summarize everything, and consistently create an in-depth output. Also, the podcast always needed to be ~10 mi
nutes long.

So I went back to the drawing board. How can I make this system better? And yes, we’re getting to the cost 
reduction part - don’t worry!

# Defining the Requirements

Jellypod must be able to process any number of input documen
ts (newsletters) and create an output that always includes the top ten most important topics across all those inputs. If
 two subparts of any input are about the same topic, we should recognize that and merge the sections into one topic.

Fo
r example, if the Morning Brew has a section about US Elections and the Daily Brief also has a section on the current st
ate of US Politics, they should be merged. I’ll skip over how I determined a similarity threshold (i.e., should two topi
cs be merged or remain separate).

# Exploding Costs

I built on top of a few different approaches outlined in papers wr
itten by the LangChain community to semantic chunk and organize everything in a almost deterministic way.

**But this wa
s INSANELY expensive.** The number of API calls grew at a rate of O(n log n), with n being the number of input chunks fr
om all newsletters.

So, I had a dilemma. Do I keep this improved and more expensive architecture or throw it down the d
rain?

I decided to keep it and figure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool calle
d OpenPipe that allows you to fine-tune open-source models almost too easily. It looked legit and was backed by YCombina
tor, so I gave it a try.

I swapped out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my LLM A
PI calls to OpenAI but recorded all inputs and outputs. This created unique datasets for each of my prompts, which I cou
ld use to fine-tune a cheaper open-source model.

After about a week of recording Jellypod’s LLM calls, I had about 50,0
00 rows of data. And with a few clicks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with the ne
w fine-tuned model.

**And it reduced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tokens to
 $1.20. And cost per output token dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new architect
ure for approximately the same cost as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral output q
uality was just as high as GPT-4 by a series of evals and in-app customer feedback.

By redesigning the system to only u
se AI for the smallest unit of work it’s actually needed for, I could confidently deploy a fine-tuned model as a drop-in
 replacement for GPT 4. And by prompting to return pointers to data instead of the data itself, I could ensure data inte
grity while reducing the number of output tokens consumed.

# In Conclusion

If you’re considering building an AI applic
ation, I would encourage you to take a step back and think about your architecture’s output reliability and costs. What 
happens if the LLM doesn’t answer your prompt in the right way? Can you prompt the model to return data identifiers inst
ead of raw data? And, is it possible to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights when I
 started, but hey, you live and learn.

I hope you found at least some parts of this interesting! I thought there were e
nough learnings to share. Feel free to reach out if you’re curious about the details.
```
---

     
 
all -  [ How I Reduced Our LLM Costs by Over 85% ](https://www.reddit.com/r/ArtificialInteligence/comments/1b92hlk/how_i_reduced_our_llm_costs_by_over_85/) , 2024-03-08-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong.

I’m not saying it’s hard per se, but as of this writing, gpt-4-turbo costs $0.01/$0.03 per 1000 input/ou
tput tokens. This can quickly add up if you’re building a complex AI workflow.

Yes, you could use less expensive, worse
 performing models, like GPT 3.5 or an open-source one like Llama, stuff everything into one API call with excellent pro
mpt engineering, and hope for the best. But this probably won’t turn out that great. This type of approach doesn’t reall
y work in production—at least not yet with the current state of AI.

**It could give you the right answer 90% or even 99
% of the time.** But that one time it decides to go off the rails, it’s really frustrating. As a developer and/or busine
ss, you know you must never break a user’s experience. It might be okay for a toy app or prototype but not for a product
ion-grade application you charge for.

Imagine if Salesforce or any other established software company said its reliabil
ity was only one or two nines. That would be insane. No one would use it.

**But this is the state of most AI applicatio
ns today. They’re unreliable.**

# AI isn’t a Universal Function

The non-deterministic nature of LLMs forces us to be m
ore thoughtful about how we write our code. We should not just “hope” that an LLM will always correctly respond. We need
 to build redundancy and proper error handling. For some reason, many builders forget everything they learned about soft
ware engineering and treat AI like some magical universal function that doesn’t fail.

**It’s not there yet.**

To fix t
his limitation, we must write code that only interacts with AI when absolutely necessary—that is, when a system needs so
me sort of “human-level” analysis of unstructured data. Subsequently, whenever possible, we must force the LLM to return
 references to information (i.e., a pointer) instead of the data itself.

**When I recognized these two things, I had to
 redesign the backend architecture of my personal software business completely.**

# Rearchitecting Jellypod

For contex
t, I started an app called Jellypod. It enables users to subscribe to email newsletters and get a daily summary of the m
ost important topics from all of them as a single podcast.

This seems pretty simple on the outside—and the MVP honestly
 was. The app would just process each email individually, summarize it, convert it to speech, and stitch all the audio t
ogether, side-by-side, into a daily podcast.

The output was fine, but it needed to be better.

If two different newslet
ters discussed the same topic, the “podcast” would talk about it twice, not realizing we had already mentioned it. You c
ould say, “Well, why don’t you just stuff all the newsletter content into one big LLM call to summarize everything?”

We
ll, that’s what I tried at first.

And it failed. **Miserably.**

Even with an extremely detailed prompt using all the b
est practices, I couldn’t guarantee that the LLM would always detect the most important topics, summarize everything, an
d consistently create an in-depth output. Also, the podcast always needed to be ~10 minutes long.

So I went back to the
 drawing board. How can I make this system better? And yes, we’re getting to the cost reduction part - don’t worry!

# D
efining the Requirements

Jellypod must be able to process any number of input documents (newsletters) and create an out
put that always includes the top ten most important topics across all those inputs. If two subparts of any input are abo
ut the same topic, we should recognize that and merge the sections into one topic.

For example, if the Morning Brew has
 a section about US Elections and the Daily Brief also has a section on the current state of US Politics, they should be
 merged. I’ll skip over how I determined a similarity threshold (i.e., should two topics be merged or remain separate).


# Exploding Costs

I built on top of a few different approaches outlined in papers written by the LangChain community t
o semantic chunk and organize everything in a almost deterministic way.

**But this was INSANELY expensive.** The number
 of API calls grew at a rate of O(n log n), with n being the number of input chunks from all newsletters.

So, I had a d
ilemma. Do I keep this improved and more expensive architecture or throw it down the drain?

I decided to keep it and fi
gure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool called OpenPipe that allows you to fine
-tune open-source models almost too easily. It looked legit and was backed by YCombinator, so I gave it a try.

I swappe
d out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my LLM API calls to OpenAI but recorded al
l inputs and outputs. This created unique datasets for each of my prompts, which I could use to fine-tune a cheaper open
-source model.

After about a week of recording Jellypod’s LLM calls, I had about 50,000 rows of data. And with a few cl
icks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with the new fine-tuned model.

**And it redu
ced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tokens to $1.20. And cost per output token 
dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new architecture for approximately the same cos
t as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral output quality was just as high as GPT-4 b
y a series of evals and in-app customer feedback.

By redesigning the system to only use AI for the smallest unit of wor
k it’s actually needed for, I could confidently deploy a fine-tuned model as a drop-in replacement for GPT 4. And by pro
mpting to return pointers to data instead of the data itself, I could ensure data integrity while reducing the number of
 output tokens consumed.

# In Conclusion

If you’re considering building an AI application, I would encourage you to ta
ke a step back and think about your architecture’s output reliability and costs. What happens if the LLM doesn’t answer 
your prompt in the right way? Can you prompt the model to return data identifiers instead of raw data? And, is it possib
le to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights when I started, but hey, you live and le
arn.

I hope you found at least some parts of this interesting! I thought there were enough learnings to share. Feel fre
e to reach out if you’re curious about the details.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1b8zd7n/for_hire_programmerweb_developerit_consultant/) , 2024-03-08-0910
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 14 years of professional experience. I am available for all sorts of programming and
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

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Github web loader + Pinecone Index fail due to UTF-16 encoding when trying to Upsert vector embeddin ](https://www.reddit.com/r/LangChain/comments/1b8xh9g/github_web_loader_pinecone_index_fail_due_to/) , 2024-03-08-0910
```
Hi folks, I'm putting together a simple Github RAG chatbot using \`GithubRepoLoader\` and Pinecone vector store. However
 when upserting the embeddings to Pinecone, the upsert process fails with the error: \`PineconeBadRequestError: Missing 
low surrogate.\`  
After a bit of research this seem to be due to how UTF-16 encodes the Unicode Characters outside the 
BMP (Basic Multilingual Plane) are represented using a pair of surrogate code points in UTF-16 encoding. The error messa
ge indicates that a high surrogate code point (D800–DBFF) was found without a corresponding low surrogate (DC00–DFFF) fo
llowing it.  
Now with that being said, my question is:   
Would it be feasible to use UTF-8 instead? Where would be a g
ood place (at what level of the stack) in the code would you make some changes to inject a parameter for a different (i.
e. UTF-8) encoding?  
TYIA
```
---

     
 
all -  [ llama index Does embedding occur in this process? ](https://www.reddit.com/r/LangChain/comments/1b8wv7p/llama_index_does_embedding_occur_in_this_process/) , 2024-03-08-0910
```
&#x200B;

    llm = OpenAI(model='gpt-4-0125-preview')
    chunk_sizes = [128, 256, 512, 1024]
    nodes_list = []
    v
ector_indices = []
    for chunk_size in chunk_sizes:
        print(f'Chunk Size: {chunk_size}')
        splitter = Sent
enceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_size // 2)
        nodes = splitter.get_nodes_from_documents(doc
s)
        for node in nodes:
            node.metadata['chunk_size'] = chunk_size
            node.excluded_embed_metad
ata_keys = ['chunk_size']
            node.excluded_llm_metadata_keys = ['chunk_size']
        nodes_list.append(nodes)

        vector_index = VectorStoreIndex(nodes)
        vector_indices.append(vector_index) 
    
    -------------------
-----------------------------------------------------------------
    
    #HTTP Request: POST https://api.openai.com/v1
/embeddings 'HTTP/1.1 200 OK'
    #HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    #HTTP R
equest: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    #Chunk Size: 256
    #HTTP Request: POST https:/
/api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    #HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 2
00 OK'
    #Chunk Size: 512
    #HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    #Chunk Si
ze: 1024
    #HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    

I ran the above code, and 
something was posted with openai. Is this embedding?

&#x200B;
```
---

     
 
all -  [ After struggling with LangChain text splitters, I decided to make my own convenient service to chunk ](https://www.reddit.com/r/LangChain/comments/1b8trzs/after_struggling_with_langchain_text_splitters_i/) , 2024-03-08-0910
```
In my experience developing RAG-based applications with LangChain, I was surprised to find that there aren't any simple,
 reliable ways to chunk files. The default [Text Splitters](https://js.langchain.com/docs/modules/data_connection/docume
nt_transformers/) that LangChain offers employ a naive form of chunking that doesn't consider positioning data like sect
ions, subsections, paragraphs or tables. 

This led me to implement my own chunking service that includes deep positioni
ng data like page index and bounding box coordinates for every chunk.

You can try it out for free here (no account/api 
key required):

https://filechipper.com

Would any of you be interested in something like this? Let me know!
```
---

     
 
all -  [ Chatbot via Kendra/Bedrock/LangChain returning non-relevant documents ](https://www.reddit.com/r/LangChain/comments/1b8sex2/chatbot_via_kendrabedrocklangchain_returning/) , 2024-03-08-0910
```
I am building a RAG chatbot on internal corporate documents. My specific architecture is Amazon Kendra for document retr
ieval, Amazon Bedrock using foundation models (llama or cohere), and LangChain as the orchestrator. I have purposely ask
ed it a question that is not in the corporate documentation. The bot correctly returns that it doesn’t know, but it is s
till returning documents from Kendra. I’m using AmazonKendraRetriever as the retriever and ConversationalRetrievalChain 
as the chain. Trying to figure out how to not return any src documents when it’s an out of scope question. Any help is a
ppreciated!
```
---

     
 
all -  [ How To Build a Custom Chatbot Using LangChain With Examples ](https://www.reddit.com/r/Langchaindev/comments/1b8rz4q/how_to_build_a_custom_chatbot_using_langchain/) , 2024-03-08-0910
```
Hey everyone, I have written a new blog that explains how you can create a custom AI-powered chatbot using LangChain wit
h code examples.

At the end of this blog, I have also given a working chatbot, that has been developed using LangChain,
 OpenAI API, and Pinecone that you can use and test.

You can read it at [LangChain Chatbot](https://www.deligence.com/l
angchain-chatbot/)

Feedback appreciated!
```
---

     
 
all -  [ Can't make the chat to understand previous context ](https://www.reddit.com/r/LangChain/comments/1b8prsz/cant_make_the_chat_to_understand_previous_context/) , 2024-03-08-0910
```
Could someone kindly assist me with this issue?

[https://github.com/langchain-ai/langchain/discussions/18722](https://g
ithub.com/langchain-ai/langchain/discussions/18722)
```
---

     
 
all -  [ Doubts about choosing vet for storage ](https://www.reddit.com/r/LangChain/comments/1b8po5e/doubts_about_choosing_vet_for_storage/) , 2024-03-08-0910
```
Hi.  Just starting a new journey on this, and Need some clarification. I’m building a complex rag system for many differ
ent kind of documents. The way I understand between the many commercially available vector stores, some have different s
trengths and advantages depending on what king of data you retrieving. 
There is some good comparison between then in re
gards of kind of data and chunk sizes? Ro help on which to choose, or this difference is negligible and we can choose wh
atever is easier to implement?
```
---

     
 
all -  [ stop agent from generate new input. ](https://www.reddit.com/r/LangChain/comments/1b8p37d/stop_agent_from_generate_new_input/) , 2024-03-08-0910
```
How I can stop LLM Agent new input, I want just to stop the generation process and extract the first AI answer.  


&#x2
00B;

https://preview.redd.it/xz8t0cdpbvmc1.png?width=765&format=png&auto=webp&s=b249549b5be459acfbc4aed3b3181023fb2298d
d

https://preview.redd.it/fjsfyv4abvmc1.png?width=1102&format=png&auto=webp&s=0a5f8df8e756e7cfa6580d014bbcbf7270822af1
```
---

     
 
all -  [ gpt secret key not working in llama index. It seems like ](https://www.reddit.com/r/LangChain/comments/1b8p2se/gpt_secret_key_not_working_in_llama_index_it/) , 2024-03-08-0910
```
Using llama index, we wanted to implement RAG. I put the secret key in the .env file and tried to load it with dotenv, b
ut the result was as follows.

    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    llm = OpenAI(
model='gpt-4-0125-preview')
    chunk_sizes = [128, 256, 512, 1024]
    nodes_list = []
    vector_indices = []
    for 
chunk_size in chunk_sizes:
        print(f'Chunk Size: {chunk_size}')
        splitter = SentenceSplitter(chunk_size=chu
nk_size, chunk_overlap=chunk_size // 2)
        nodes = splitter.get_nodes_from_documents(docs)
        for node in node
s:
            node.metadata['chunk_size'] = chunk_size
            node.excluded_embed_metadata_keys = ['chunk_size']
 
           node.excluded_llm_metadata_keys = ['chunk_size']
        nodes_list.append(nodes)
        vector_index = Vect
orStoreIndex(nodes)
        vector_indices.append(vector_index) 
    

And below are the execution results. And what is 
this post 200 and url? What does this mean? Embedding? Or what?

    Chunk Size: 128
    HTTP Request: POST https://api.
openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'

    HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    Chunk Size: 256
    HTTP Request: POS
T https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    HTTP Request: POST https://api.openai.com/v1/embeddings 'HT
TP/1.1 200 OK'
    Chunk Size: 512
    HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'
    Chu
nk Size: 1024
    HTTP Request: POST https://api.openai.com/v1/embeddings 'HTTP/1.1 200 OK'

&#x200B;
```
---

     
 
all -  [ Building a email responder with langchain? ](https://www.reddit.com/r/LangChain/comments/1b8mfdw/building_a_email_responder_with_langchain/) , 2024-03-08-0910
```
As the text suggests, can I build an application for creating responses for emails when i provide them with a email text
? Any advice or heads up in this direction would help me start with the project.

Thanks in advance!
```
---

     
 
all -  [ Auto GPT is hallucinating.How to make AutoGPT read json data and work onto it to generate test seque ](https://www.reddit.com/r/LangChain/comments/1b8mans/auto_gpt_is_hallucinatinghow_to_make_autogpt_read/) , 2024-03-08-0910
```
So I'm using an LLM = AzureChatOpenAI() and i have a .json data file that has  the content of various APIs in the form  
:
 '2': {
        'Method': 'POST',
        'Path': '',
        'FunctionName': '',
        'FunctionCode': '{\...\}',
 
       'Queries': []
    } 

I have a list of these and I'm using AzureOpenAI() as my embeddings model to create a vecto
r store db and retrieve. The I'm initialising my agent= AutoGPT with memory as vectorstore.as_retriever.

My end goal is
 to generate end to end flow of these APIs for testing purposes for the given api and original prompt is 
 agent.run('Wh
at are the different API sequences that are possible to test the end to end flow of the API for the given APIs. The diff
erent fields that are present in the json are path, method, queries,FunctionName and FunctionCode. You cannot ask for hu
man input.Start by using APIs wivh no prerequisitesand authentication') 

Also I've defined custom tool which 
@tool
def
 get_api_based_on_index(index: int) -> dict:
    '''Get API details based on the given index number'''
    if str(index)
 in data:
        return data[str(index)]  
    else:
        raise ValueError(f'Index {index} not found in the data.')


But right now my langchain agent is hallucinating and not able to get api values and fields and is only looping around 
3-4 APIs .

Can anyone look into this and help me such that I can get this agent to retrieve the json data as vectors an
d  go through all of that data and generate me test flow sequences of various APIs that is generally done in end to end 
software testing.
```
---

     
 
all -  [ What is the difference between llama index and Langchain? ](https://www.reddit.com/r/LangChain/comments/1b8iaac/what_is_the_difference_between_llama_index_and/) , 2024-03-08-0910
```
So far, I have implemented RAG using Langchain. In the case of Langchain’s RAG,

It was like this: 'Load document -> Tex
t split -> Chroma vector DB embedding -> llm.'



However, in the case of llama index, it looks like there is no vector 
DB embedding. Am I misunderstanding it?

And setting the embedding model doesn't seem to exist in the llama index.

I wo
uld appreciate it if you could explain. or git code please
```
---

     
 
all -  [ Userinterface for the API key?? The answer is : Poe ](https://www.reddit.com/r/ChatGPTPro/comments/1b8fkb7/userinterface_for_the_api_key_the_answer_is_poe/) , 2024-03-08-0910
```
Yeah, it is fairly simple to set up a custom chatbot on  with the server feature. This way, you  can use any chatbot  th
at you have an api for, and make poe the user interface. Im so happy i found this, going to have a lot of fun trying all
 the new models without having to pay a subscription im not going to use to the fullest.

Basicly, you write some python
 code, deploy it on modal website which offer 30 dollars of compute per month, and this will only require max 1dollar si
nce it isnt the one doing the inference. Then connect it to poe and you are up and running. The only problem is, that th
e documentation is confusing as f, but i feel like i understand it completely now, and it is fairly simple. Feel free to
 ask.

  
Note: this way you can make infinite chatbots and even do langchain or very complicated agents and much more, 
much cheaper even. Consider making a model, that uses some advanced prompt tactic before it comes up with the answer. Po
ssible!, on the web, available on your phone, anywhere. 
```
---

     
 
all -  [ Career Direction for a heavily technical but well rounded SE ](https://www.reddit.com/r/salesengineers/comments/1b8e8k9/career_direction_for_a_heavily_technical_but_well/) , 2024-03-08-0910
```
Hoping to get some internet wisdom here. My career has taken me from M&A and management consulting, to running a family 
business in petro equipment remanufacturing, and in the past \~8 years in Data Engineering, Data Science, and setting up
 a SE department.    


Here’s a quick rundown of my career path:

* **Early Career:** Undergrad in finance, first job i
n management consulting (M&A), ran systems engineering and sales for a family business while I was at PwC concurrently.

* **Shift to Tech:** Sold the family business and knew I wanted to do something heavily technical. Moved to TN, did a bo
otcamp and got linked with a network of heavy hitters in the health tech scene.  Ran BI and DW for a health tech start u
p, exited, and was recruited to do big-data DE for another startup. Earned my MS in Data Science from Georgia Tech, init
ially transitioning from data engineering to data science.
* **Move to SE:** I built a few prototypes and did some R&D o
n the side which landed some big clients outside of our target industry (our PE overlords pegged it at $150m of addition
al TAM).  Also did a side project which ended up featured in the New York Times and a bunch of other health tech publica
tions.  That generated enough interest that the C-Suite asked me to setup a sales engineering department (easy move beca
use DS was moving way too slow for my taste).
* **Tech and Sales Intersection:** Automated a lot of our sales team's pro
cesses which sped them up and built a few prototypes and case studies to land $2M in ARR within my first 8 months in the
 formal SE role.
* **Skills and Interests:** I'm deep into Spark (Scala, PySpark, SparkSQL), Python, SQL, DW architectur
e (big and normal data environments), Azure Cloud infrastructure, Machine Learning, LLMs / Agents, and Tableau (regretta
bly). My W2 expertise is largely in healthcare economy data but I’ve also built a side-project with a FastAPI, langchain
 backend / retool front-end to support a buddy from college who wants to expand his crypto hedge fund. I'm technically v
ery well rounded.

**What I’m Looking For:**

* Insight into sales or sales engineering roles that need someone who’s no
t just technical but *really* technical. I love programming and building things but also have a track record of closing 
deals and building stuff to make my sales team faster.
* To connect with folks in tech-heavy SE roles to understand what
 their day-to-day and teams look like.

**Why I’m Exploring:**

* Growth concerns with my current company, especially gi
ven our target industry's slim margins.
* I’m the go-to engineer on the non-engineering side, often stretched thin acros
s tasks that don’t align with my role or support my commission goals.
* Despite significant contributions, especially on
 the consulting/research side, it’s not reflecting in my compensation.

Would love to hear your thoughts, experiences, o
r if you know of roles that might fit my blend of skills and passions I've got going on. 
```
---

     
 
all -  [ Curly braces in prompts again... ](https://www.reddit.com/r/LangChain/comments/1b8cpcz/curly_braces_in_prompts_again/) , 2024-03-08-0910
```
I saw the previous discussion about using double curly braces inside a template to avoid expansion in a prompt's format 
method.

However, I'm still having a problem with this, even with double curly-braces, when I use a \`FewShotPrompt\`.  
I have \*examples\* in the FSP that contain code. So I suspect what is going wrong is that the double curly-braces help 
when the examples are folded into the prompt, but then when the \*input\* is folded in, the double curly braces have bee
n stripped and I get an error.

This seems like a numbskull problem on my part, so even just a pointer to some tutorial 
about using a FewShotPrompt with code (surely there must be one?) would be great.
```
---

     
 
all -  [ How to Improve RAG speed with OpenAI? ](https://www.reddit.com/r/LangChain/comments/1b87p0i/how_to_improve_rag_speed_with_openai/) , 2024-03-08-0910
```
I am using assistant api as agent in the LangChain framework. I’m using gpt4-0125-preview for this agent. The reason why
 I use agent is because I do not want every query to search the database. And I find the assistant api agent is smarter 
than the ReAct agent in terms of generating responses.

I have only one tool for linking to a retrieval chain. When the 
user asks certain question, the agent invokes a chain and pass query into the retrieval system. I pass in gpt-4-preview-
0125 for the retrieval chain.
To improve the retrieval process, I use multi-query to help generate sub questions from th
e original questions to dig into the details. I use gpt3.5-1106 for the multi query retriever as this doesn’t require mu
ch reasoning. So essentially,
I use the assistant api(gpt-4-0125) as agent, gpt4-0125 for the retrieval chain and gpt3.5
 1106 as the multi query retriever.

In terms of data preparation. I use manual chunking. By manual chunking I mean I ma
nually gather relevant content into one ‘document’. This is because I see splitter does not consider context so it’s bet
ter to do the chunking on my own. 

The problem is that the average response time for 1000-2000 token is ranging from 10
s to 30s. I tried using gpt3.5 as the agent in assistant api. Speed cuts down to 3-10s. But the generation is way worse.
 This one I’m not sure why as I keep the gpt4-0125 in the retrieval chain. I assume the generation should be good…

How 
should I improve my architecture to enhance speed?


```
---

     
 
all -  [ How does indexing work? ](https://www.reddit.com/r/LangChain/comments/1b86gzl/how_does_indexing_work/) , 2024-03-08-0910
```
Does indexing happen sequentially in llamindex/langchain? I mean say I've a pdf containing images and text. When I store
 the embeddings in the vector database, the order of text and images matters (text just below a fig. might be explaining
 about the fig), so is it good to go with default implementation?
```
---

     
 
all -  [ Calling - Software Dev Beta Testers ](https://www.reddit.com/r/BetaTestersNeeded/comments/1b8165p/calling_software_dev_beta_testers/) , 2024-03-08-0910
```
We are starting Beta Testing of our Software AI platform in the next \~30 days. Feel free to join if your a Software Dev
 with skill set in (and to be expanded on shortly): React, React Native, Serverless, Langchain, or Salesforce/APEX!

[ht
tps://activate.kodey.ai/beta-signup](https://activate.kodey.ai/beta-signup)
```
---

     
 
all -  [ React Native Langchain support? ](https://www.reddit.com/r/LangChain/comments/1b815jv/react_native_langchain_support/) , 2024-03-08-0910
```
React Native is incompatible with langchain, when are we going to get an update?

i found this but there is no solution 
even the one provided with langchain maintainer himself [https://stackoverflow.com/questions/77307779/react-native-issue
-while-implementing-langchain/77313089#77313089?newreg=6af4405652b844fd81c2d0735b49c25f](https://stackoverflow.com/quest
ions/77307779/react-native-issue-while-implementing-langchain/77313089#77313089?newreg=6af4405652b844fd81c2d0735b49c25f)

```
---

     
 
all -  [ Free courses and guides for learning Generative AI ](https://www.reddit.com/r/Entrepreneur/comments/1b7zurr/free_courses_and_guides_for_learning_generative_ai/) , 2024-03-08-0910
```
**Text-to-image focused resources:**

* [*Free course is designed*](https://www.udemy.com/course/a-hands-on-guide-to-pra
ctical-use-of-generative-ai/learn/lecture/42466882#overview) to demonstrate the practical applications of generative AI 
for business owners, marketers, entrepreneurs and everyone who needs visual assets
* [*Website*](https://stable-diffusio
n-art.com/) with full of SD-focused resources
* [*Blog*](https://followfoxai.substack.com/archive) to learn about fine-t
uning and other interesting stuff

**LLM focused resources:**

* [Google free course](https://www.cloudskillsboost.googl
e/paths/118) - this learning path provides an overview of generative AI concepts, from the fundamentals of large languag
e models to responsible AI principles
* [Scrimba free Course](https://scrimba.com/learn/buildaiapps) - Build AI Apps wit
h ChatGPT, DALL-E and GPT-4
* [The Foundational Model Certification](https://learn.activeloop.ai/courses/langchain) is y
our essential gateway to mastering Large Language Models (LLMs) - from training to putting them in production
* [Prompt 
Engineering Guide](https://learnprompting.org/docs/intro)
* [18 Lessons teaching everything](https://microsoft.github.io
/generative-ai-for-beginners/#/)you need to know to start building Generative AI applications by Microsoft
* [Deep Learn
ing Fundamentals](https://lightning.ai/courses/deep-learning-fundamentals/) is a free course on learning deep learning u
sing a modern open-source stack.
* [Natural Language Processing](https://www.youtube.com/playlist?list=PLofp2YXfp7TZZ5c7
HEChs0_wfEfewLDs7), a masters-level NLP course offered as part of the Masters of Computer Science Online at UT Austin

W
hat should I add?
```
---

     
 
all -  [ Calling - Software Dev Beta Testers ](https://www.reddit.com/r/beta_testers/comments/1b7z0yn/calling_software_dev_beta_testers/) , 2024-03-08-0910
```
We are starting Beta Testing of our Software AI platform in the next \~30 days. Feel free to join if your a Software Dev
 with skill set in: React, React Native, Serverless, Langchain, or Salesforce/APEX!

&#x200B;

[https://activate.kodey.a
i/beta-signup](https://activate.kodey.ai/beta-signup)
```
---

     
 
all -  [ Autogen vs. LangGraph ](https://www.reddit.com/r/LangChain/comments/1b7q44y/autogen_vs_langgraph/) , 2024-03-08-0910
```
Which library comes out on top? I am building a multi-agent system in production but still have not decided which framew
ork to use
```
---

     
 
all -  [ When implementing RAG, can I use various retrievers? ](https://www.reddit.com/r/LangChain/comments/1b7op5w/when_implementing_rag_can_i_use_various_retrievers/) , 2024-03-08-0910
```
hello! Are you doing well?

&#x200B;

Among the types of retrievers, I came across a total of four retriever methods: Mu
lti, self, time, and parent.

&#x200B;

Is it possible to run multiple Retrievers in one project?

&#x200B;

For example
, if we were to create a chatbot that answers school rules, would it be possible to use multiple Multi Query and Parent 
functions at the same time?

&#x200B;

Or is it possible to use only one Retriver?

&#x200B;

If only one Retriever is a
vailable, can you tell me why?
```
---

     
 
all -  [ Repo Size over 500mb ](https://www.reddit.com/r/nextjs/comments/1b7o0eq/repo_size_over_500mb/) , 2024-03-08-0910
```
I got a project that I'm working on, it been a pain keeping it below 500mb. I find it annoying that the projects get so 
big, but then again i'm using MUI... What should I use instead?

https://preview.redd.it/lp8vx88iimmc1.png?width=473&for
mat=png&auto=webp&s=2f2a0849aff01060ec1a75223a666f1d99d4f49e
```
---

     
 
all -  [ Building my One-Man Media Team with AI Agents (Using Langchain & LangGraph) ](https://www.reddit.com/r/LangChain/comments/1b7mhy2/building_my_oneman_media_team_with_ai_agents/) , 2024-03-08-0910
```
Hey everyone, I wanted to share some recent work I did using Langchain and LangGraph to prototype an Agent pipeline for 
generating a newsletter + tweets from scratch.

Here's the link: [https://youtu.be/i71Rm-7oG4k?si=B4Z2hBbh386EbswC](http
s://youtu.be/i71Rm-7oG4k?si=B4Z2hBbh386EbswC)

Hope it helps.
```
---

     
 
all -  [ Why would OpenAI flag a newly created script with a '429 - rate exceeded' error, when I just created ](https://www.reddit.com/r/OpenAI/comments/1b7lk9u/why_would_openai_flag_a_newly_created_script_with/) , 2024-03-08-0910
```
Literally just created a simple langchain example. This was the result:

RateLimitError: Error code: 429 - {'error': {'m
essage': 'You exceeded your current quota, please check your plan and billing details. For more information on this erro
r, read the docs: [https://platform.openai.com/docs/guides/error-codes/api-errors](https://platform.openai.com/docs/guid
es/error-codes/api-errors).', 'type': 'insufficient\_quota', 'param': None, 'code': 'insufficient\_quota'}}
```
---

     
 
all -  [ Autonomous agent framework comparison ](https://www.reddit.com/r/singularity/comments/1b7czo0/autonomous_agent_framework_comparison/) , 2024-03-08-0910
```
Does anyone have something that compares/contrasts the different autonomous agent frameworks out there these days (ie. l
angchain, autogen, etc.). There seems to be so many floating around but hard to discern the pros and cons of each.
```
---

     
 
all -  [ Confluence cleanup ](https://www.reddit.com/r/LangChain/comments/1b7byjo/confluence_cleanup/) , 2024-03-08-0910
```
 Hello,

I'm fairly new to LangChain, and I'm wondering if it's a use case that can be well executed with LangChain.   

I would like to create a helper/copilot (chatbot) in the first place to identify irrelevant, duplicate, or contradictory
 content and assist me in restructuring the navigation tree. 
```
---

     
 
all -  [ Seeking Advice for RAG App ](https://www.reddit.com/r/LangChain/comments/1b7b57n/seeking_advice_for_rag_app/) , 2024-03-08-0910
```
Hello,

I'm an intern with an ambitious project that could earn me a full-time position. Our company often engages in ex
tensive referencing of files, documents, and web research, which is time-consuming. My solution is to automate these tas
ks through a bot, leveraging LangChain and GPT-4 for intelligent query processing.

**Project Overview:**

The bot will 
integrate with Microsoft Teams, enabling users to submit queries and receive document references or research results. It
 will serve different departments, each possibly requiring access to a vast array of data (Word, Excel, PDFs, emails, et
c.). The data volumes we're looking at span gigabytes to terabytes. Given this, I'm leaning towards using a vertical dat
abase to manage this diverse and voluminous data efficiently.

**Seeking Advice on:**

1. **Vertical Database Selection:
** Given my inclination towards a vertical database for this project, which specific vertical database systems would you
 recommend for handling both structured and unstructured data across such a broad spectrum of file types and sizes?

2. 
**Database Structure:** Is it more advantageous to maintain a single comprehensive database or to deploy multiple databa
ses, one for each department, to streamline data management and querying processes?

3. **Project Architecture:** How sh
ould I structure the interaction between the vertical databases, the LangChain bot, and the GPT-4 API to ensure seamless
 operation and scalability? What considerations should I keep in mind to support the large data volume and diverse file 
types?

4. **Managing Large Datasets:** Any insights on efficiently processing and retrieving information from large Exc
el files filled with extensive numerical data would be especially helpful. Are there particular strategies or technologi
es that would facilitate handling such datasets?

I am very much open to learning from your experiences and suggestions,
 including any alternative approaches or tools that could enhance the project. My ultimate aim is to develop a convincin
g proof of concept that clearly demonstrates the potential benefits and feasibility of the initiative.

Thank you immens
ely for your guidance and support!

```
---

     
 
all -  [ Hirering full stack developer with Langchain knowledge ](https://www.reddit.com/r/LangChain/comments/1b7915m/hirering_full_stack_developer_with_langchain/) , 2024-03-08-0910
```
We are looking to hire a full stack developer to help us with ai projects. You must be excellent at these skills:
Englis
h
Langchain with Python
Setting up a frontend that works coherently with the backend and can be used by multiple users.

If you are interested, please message us you resume at Team@dialogintelligens.dk
```
---

     
 
all -  [ Llama plus text similarity ](https://www.reddit.com/r/LangChain/comments/1b7470g/llama_plus_text_similarity/) , 2024-03-08-0910
```
Hello guys, i am extracting information about someone using llama and then using this information to compare it to a tex
t of requirements. For example:

Req: person needs to have skills A or similar.

What can be the best technologies to do
 this comparison?  
I was trying embeddings models and then calculating the l2 distance between the requirements and the
 skills but i seem to be getting bad scores for people that should be 'good'.

Anyone ever dived into this realm? Can´t 
seem to find good info online.
```
---

     
 
all -  [ Update: Langtrace Preview: An opensource LLM monitoring tool - achieving better cardinality compared ](https://www.reddit.com/r/LangChain/comments/1b6phov/update_langtrace_preview_an_opensource_llm/) , 2024-03-08-0910
```
This is with regards to: [https://www.reddit.com/r/LangChain/comments/1b4s7cw/building\_a\_open\_source\_llm\_monitoring
\_software/](https://www.reddit.com/r/LangChain/comments/1b4s7cw/building_a_open_source_llm_monitoring_software/)  


Ju
st wanted to share an update on my open source LLM monitoring tool. I do not have a UI yet, so asked chatGPT to plot the
 spans of a trace I generated for a langchain example code that uses agents. Below is the screenshot of my tool's trace 
plotted:

https://preview.redd.it/xvqgcukrgemc1.png?width=2980&format=png&auto=webp&s=0eaa0d298e047457520359017123054f65
570621

  
Same output from Langsmith:

https://preview.redd.it/lulyrgh6gemc1.png?width=778&format=png&auto=webp&s=db44f
54bf8d561ed379a2ea3e1dfe2319ee9ab84

&#x200B;

Feedback/comments/thoughts welcome
```
---

     
 
all -  [ Local Models w/ M1 Pro? ](https://www.reddit.com/r/LangChain/comments/1b6n1k9/local_models_w_m1_pro/) , 2024-03-08-0910
```
Hello. 

How capable is an M1 Pro 3.2 GHz and 32 GB of ram at running local models? I’m deciding whether to buy a used m
achine for $1K to power a Langchain based project I’m working on. 

I’m also considering using cloud services and wait u
ntil the new Mac hardware launches which will likely be optimized for LLMs. 

Thanks!🙏 
```
---

     
 
all -  [ Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/machinelearningnews/comments/1b6k0s7/scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-08-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/tnwmdqdfedmc1.png?width=1301&format=png&a
uto=webp&s=819867865e8a7361f306b5aa111919aa9a4d5bb9)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
all -  [ Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MLQuestions/comments/1b6jzz7/scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-08-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/ib26vnfaedmc1.png?width=1301&format=png&a
uto=webp&s=166e69be2a820476cd836f86f0eeece532807a3a)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
all -  [ Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/mlops/comments/1b6jyl8/scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-08-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/v5rc3w9wddmc1.png?width=1301&format=png&a
uto=webp&s=d5736aeac19741ce95112dfebe14cd58cd7f11e1)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 (Inferless) a month.

Here is the tutori
al - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hackern
ews here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
all -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-08-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
all -  [ Effective way to summarize 10k page documents ](https://www.reddit.com/r/LangChain/comments/1b6fiyt/effective_way_to_summarize_10k_page_documents/) , 2024-03-08-0910
```
Hello,

Is there an effective way to summarize 10k page documents. 

So I have chunks of 300 words and their embeddings 
already stored in the database.

I can apply clustering algorithm like k means. But for such large documents, I think ef
fective cluster size would be 100-150, with each cluster of being approximately 25-30k tokens. 

That would mean 100 api
 calls to get chunk summary , and final api call yo get final summary. 

1. How can we optimize this ? Not necessarily u
sing clustering, any other way to  make it kore cost efficient. As passing 32k prompt to model is very expensive itself,
  and to add 100 api calls. 

2. For such large documents what metrics can I use to ensure summary is good and model isn
't hallucinating. 

Thanks! 
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-08-0910
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-08-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-08-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-08-0910
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-03-08-0910
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

     
