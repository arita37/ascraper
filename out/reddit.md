 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 1690531314.0
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

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 1690189139.0
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

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 1689790263.0
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

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 1689516377.0
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
MachineLearning -  [ '[N]' '[D]' Langchain? What is it?? ](https://www.reddit.com/r/MachineLearning/comments/150mzax/n_d_langchain_what_is_it/) , 1689454973.0
```
want to know more about Langchain  
Check out [https://nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf](https:
//nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf)
```
---

     
 
MachineLearning -  [ [D] The Problem With LangChain ](https://www.reddit.com/r/MachineLearning/comments/14zlaz6/d_the_problem_with_langchain/) , 1689352833.0
```
https://minimaxir.com/2023/07/langchain-problem/

tl;dr it's needlessly complex, and I provide code examples to demonstr
ate such.

A few weeks ago when I posted about creating a LangChain alternative to /r/MachineLearning, most of the comme
nts replied 'what exactly is the issue with LangChain', so I hope this provides more clarity!
```
---

     
 
MachineLearning -  [ [D] 📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1) ](https://www.reddit.com/r/MachineLearning/comments/14xww89/d_the_learning_corner_andrew_ng_free_ai_courses/) , 1689187280.0
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

     
 
MachineLearning -  [ [P] langchain-lite alternative ](https://www.reddit.com/r/MachineLearning/comments/14xf9xb/p_langchainlite_alternative/) , 1689140460.0
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

     
 
MachineLearning -  [ [D] What have been your use cases for LLM autonomous agents? ](https://www.reddit.com/r/MachineLearning/comments/14w817y/d_what_have_been_your_use_cases_for_llm/) , 1689026848.0
```
I've been using GPT for completions on a daily basis for a while now - code completion and search-like chatting, basical
ly. I've recently been playing around with both ChatGPT plugins and LangChain for autonomous-agent-like behavior, and al
though the idea of the LLM interacting with the environment through API calls or code interpretation seems promising, in
 practice I haven't found such a useful and usable case for it like completions yet.

LangChain's OpenAPI toolkit with i
ts planner/controller agent duo seems to get lost 90% of the time, making it unusable. This happens even with an /api en
dpoint telling it exactly how to interact with the API and prompt templates suggesting that this endpoint be used to get
 the API specs. Maybe I'm just not getting it right...

As for ChatGPT plugins, other than web search for more updated r
esults I haven't really found a use case where I could not do the same thing with completions. Code Interpreter shaves o
ff a few seconds vs completions and running whatever script it produces locally, but it's not very useful in face of com
pliance or privacy requirements of not uploading stuff into OpenAI. For example I wanted to speed up a work related vide
o and add a separate audio track to it. I couldn't upload the video to OpenAI as it contained internal work stuff, so I 
just used completions for an ffmpeg script to do the job and ran it locally. Same thing with transforming or plotting CS
V data - can't really update customer data to OpenAI, so just get the script and run it locally.

Anyway, I can *think o
f* a lot of cool use cases for autonomous agents and the like, but I haven't been able to *actually use* it in my daily 
routine, unlike text completion. Have you been using autonomous agents successfully and regularly?
```
---

     
 
MachineLearning -  [ [D] Hacking LangChain for Fun and Profit ](https://www.reddit.com/r/MachineLearning/comments/14w0ht7/d_hacking_langchain_for_fun_and_profit/) , 1689010315.0
```
[https://blog.kevinhu.me/2023/07/10/hacking-langchain-for-fun-and-profit/](https://blog.kevinhu.me/2023/07/10/hacking-la
ngchain-for-fun-and-profit/)

I'm starting a series of blogs to delve into LangChain. Hope this helps anyone who's inter
ested in LLM and building with LangChain.
```
---

     
 
MachineLearning -  [ [D] - Are there any AI benchmarks that involve successful longterm problem solving when running as a ](https://www.reddit.com/r/MachineLearning/comments/14v4l2o/d_are_there_any_ai_benchmarks_that_involve/) , 1688924349.0
```
 Even the most powerful LLMs, such as gpt4, seem to get lost or fall into loops when being run as autonomous agents like
 as part of langchain or autogpt. Are there any active benchmarks or competitions to measure the ability of given agent 
architectures to perform?
```
---

     
 
MachineLearning -  [ [R] Chat with documents using LangChain and OpenAI ](https://www.reddit.com/r/MachineLearning/comments/14pkxir/r_chat_with_documents_using_langchain_and_openai/) , 1688395253.0
```
Over the past few months, I've been captivated by the flood of apps claiming to be the ultimate 'ChatGPT for your docume
nts' on Product Hunt. The question that lingered in my mind was, 'How do these apps actually work?' Curiosity led me dow
n an exciting path of discovery, and I stumbled upon a framework that I think is revolutionizing the world of app develo
pment in the context of Large Language Models - LangChain

I learned that developing a 'ChatGPT for your documents' is e
asily achievable through three broad workflows combined with access to OpenAI API. In fact, I went ahead and prototyped 
such a system on streamlit. 

Step 1 - The Setup: Store your documents as embeddings.
In the first step, use Document Lo
aders (at least 100 are available), provided by LangChain to convert anything from a simple Word document to an AWS S3 d
irectory into Documents. Then, using Document Transformers and Text Embedding Models, you transform your documents into 
embeddings. Finally, store these embeddings in a vector store for searches later on. It's a one-time setup that sets the
 foundation for your Q&A system. 💡🛠️

Step 2 - Establish Context: Find relevant documents.
LangChain's Text Embedding mo
del converts user queries into vectors. These vectors are used by LangChain's retriever to search the vector store and r
etrieve the most relevant documents. You can control the search boundaries based on relevance scores or the desired numb
er of documents. It's all about finding the right context for your Q&A system. 🎯💬

Step 3 - Chat Away: Get answers from 
LLMs.
Now comes the fun part! You pass the user's query and the established context to the Language Models (LLMs). The L
LMs respond with precise answers, taking into account the provided context. It's like having a conversation with your do
cuments. 🤩🗨️


By building these three workflows, a service that acts like a Q&A for a restricted set of documents can b
e set up. Of course, this is just an overview of the approach and all the complex steps of app development will still re
main, I remain fascinated by how the good folks at LangChain have made things simpler. 

What do you think? Have you tri
ed LangChain to build something? Is there any other framework that is equally fascinating?

#llm #openai #chatgpt #docum
ents #generativeai #langchain
```
---

     
