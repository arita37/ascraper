 
all -  [ Can SmythOS RAG handle enterprise level RAG systems?
 ](https://www.reddit.com/r/LangChain/comments/1eyy9h2/can_smythos_rag_handle_enterprise_level_rag/) , 2024-08-23-0911
```
I have read a good number of posts on this sub of inquiries and discussion into the right approach when it comes to RAG.
 The sentiment around it, as far as I can tell, is that it might not be the hero that it was hoisted to be from the begi
nning and to get the best results from it, you gotta put in the work, a lot of work.

I found out that SmythOS has a num
ber of data related components,

* Data Lookup
* Data Source Indexer
* Data Source Cleaner

The platform is no code but 
I would assume that under the hood these data components use RAG for storage, indexing, search etc

I created a simple w
orkflow that I had to add a couple of documents, around 10, and with the data components and an LLM, I tried retrieving 
information from the docs through chat and it worked fairly well. 

I know 10 documents aren’t much and I know I might n
ot be knowledgeable enough about RAG to know what to test for and that’s why I’m asking here for your opinions, what’s y
our take on how SmythOS handles data retrieval, search and indexing? Would it be sufficient for an enterprise level RAG 
solution?
```
---

     
 
all -  [ JSONLoader, search for key but return content ](https://www.reddit.com/r/LangChain/comments/1eyxj6n/jsonloader_search_for_key_but_return_content/) , 2024-08-23-0911
```
`llm = ChatOpenAI(model='gpt-4o')`

`loader = JSONLoader(`

`file_path='./extracted_data.jsonl',`

`jq_schema='.title',`


`text_content=False,`

`json_lines=True,`

`)`

I have a JSON format like this:

{

'title': 'X Title',

'content': 'X
 content'

}

Is it possible to search based on the title but return the content to the LLM?


```
---

     
 
all -  [ Where to start langchain and generative ai as a begineer? ](https://www.reddit.com/r/generativeAI/comments/1eype0m/where_to_start_langchain_and_generative_ai_as_a/) , 2024-08-23-0911
```
Do i really need the knowledge of machine learning and deep learning to learn this?
```
---

     
 
all -  [ Token streaming + structured response parsing ](https://www.reddit.com/r/LangChain/comments/1eynruh/token_streaming_structured_response_parsing/) , 2024-08-23-0911
```
I'm trying to build a POC of re-work of my AI chat app that I've built using LangChain and gpt-4 using full streaming ca
pabilities. My goal is to make visual/audio latency as minimal as possible. What I want is to use *astream\_events* per 
LangChain docs to get token streaming. My system prompt has some places where I request structured responses along with 
text. Here is an example:

    Here is a form you need to fill-in: { 'content':'user-form', 'form-id':'form-1a2b3c4d'}


My understanding that *JsonOutputParser* supports streaming I can attach it to my LCEL, but it doesn't work this way - I
 still receive raw tokens in *astream\_events*, but I can get the parsed result when streaming is over (not what I need)
.

Is there any way to parse a stream of tokens and extract structured content out of it? I believe there are some ways,
 but wasn't able to google them, unfortunately. What do you use for that?
```
---

     
 
all -  [ Where can I find examples of RAG prompts that yield hallucinations? ](https://www.reddit.com/r/LangChain/comments/1eymihq/where_can_i_find_examples_of_rag_prompts_that/) , 2024-08-23-0911
```

```
---

     
 
all -  [ Question about PDF Parsing. Please Help Me! ](https://www.reddit.com/r/LangChain/comments/1eylm73/question_about_pdf_parsing_please_help_me/) , 2024-08-23-0911
```
Hello. Everyone. I recently started studying RAG. So I need your advice.



When working with PDF documents, we often ne
ed to load them using a PDFLoader and then divide the content into chunks, ideally grouping related content together. Ho
wever, PDF documents frequently have a highly unstructured format, with images interspersed within the text. Current PDF
Loaders like Marker, while advanced, cannot automatically concatenate text sections and separately identify images in th
e same way a human would perceive the document structure. This limitation presents a significant challenge.

Given these
 constraints, how should developers approach the task of effectively processing such complex PDF structures? What strate
gies can be employed to:



Accurately identify and group related textual content?

Properly handle embedded images and 
other non-textual elements?

Maintain the logical flow and context of the document during the chunking process?



Can y
ou provide some best practices or methodologies that address these challenges in PDF processing and chunking, particular
ly for documents with mixed content types and complex layouts?

https://preview.redd.it/114apizad8kd1.png?width=1316&for
mat=png&auto=webp&s=5e60ea3c32f46ad3b374f6b650f7250472c4033d

  

```
---

     
 
all -  [ Fine-tuning in another language ](https://www.reddit.com/r/LangChain/comments/1eylgcz/finetuning_in_another_language/) , 2024-08-23-0911
```
I need to 'feed' a model custom data, but it is in Bulgarian. Is there a way to do this?

```
---

     
 
all -  [ How can I create my own version of NotebookLM? How can I evaluate it against a csv of questions and  ](https://www.reddit.com/r/LocalLLaMA/comments/1eyla7p/how_can_i_create_my_own_version_of_notebooklm_how/) , 2024-08-23-0911
```
I tried notebookLM today, and was very underwhelmed.

  
I want to make my own version of it, or use an open source vers
ion that someone else has made. As far as I can see, notebookLM is just a RAG application using Google's models. I've re
ad about how LangChain, LlamaIndex, and Haystack are used to create RAG applications, but i'm getting a bit overwhelmed 
reading about them on the internet. So many differing opinions. I've only used MilvusDB for my vector database before, a
nd the quickstart guide they gave used LlamaIndex and OpenAI. I need to learn Langchain and Haystack.

  
For the LLMs a
ctually answering queries, i'm hoping to evaluate Claude, Gemini, GPT, and LLaMA against eachother.

  
I have a created
 a csv file of 20 questions and answers so far, and plan to get more. I wonder if this will be helpful in evaluating the
 rag applications against eachother.

  
I looked at [RagBuilder](https://www.reddit.com/r/LocalLLaMA/comments/1eujz24/r
agbuilder_now_supports_azureopenai_googlevertex/) but did not really like it. If I could speak to the dev maybe I could 
figure it out, but I don't think I need to use something so complicated.

  
How do I start on this project?
```
---

     
 
all -  [ What’s your preferred approach to RAG search? ](https://www.reddit.com/r/LangChain/comments/1eyl7c3/whats_your_preferred_approach_to_rag_search/) , 2024-08-23-0911
```
I wrote the same post in the r/RAG community, but I haven't got a response there yet because that community is still qui
te small. So I'll ask here. I'm new to Reddit, and this is my very first post, so please be gentle!

I've been working o
n building RAG systems and have noticed that search tends to be the current bottleneck, particularly in specialized doma
ins. Existing methods often struggle to accurately select the most relevant context chunks.

How do you handle this? Wha
t’s your preferred approach to RAG search — vector-based, full-text, or hybrid? Do you rely on custom formulas, reranker
s, query expansion/reformulation, or specialized dictionaries?

Have you worked with knowledge bases containing hundreds
 of thousands or even millions of documents? How has that experience shaped your approach? Thanks to everyone who respon
ds! This is important to me!
```
---

     
 
all -  [ 2025 graduate, doubting whether i will get a good job or not ](https://www.reddit.com/r/developersIndia/comments/1eyl15n/2025_graduate_doubting_whether_i_will_get_a_good/) , 2024-08-23-0911
```
https://preview.redd.it/6qs6fc5y88kd1.png?width=759&format=png&auto=webp&s=2289ba1699333a088181ac6c364a9f18654f01a6


```
---

     
 
all -  [ High-Precision RAG for Table Heavy Documents… (Using LangChain, Unstructured.io, & KDB.AI) ](https://www.reddit.com/r/kdbai/comments/1eykuqz/highprecision_rag_for_table_heavy_documents_using/) , 2024-08-23-0911
```
One aspect of RAG that’s been bugging me is the decline in accuracy when retrieving specific values from embedded tables
 within a document. It’s even worse when the document is packed with multiple similar complex tables (especially nested 
columns), like in an earnings report. So I set out on a mission to improve RAG on table heavy documents using [LangChain
](https://www.linkedin.com/company/langchain/), [unstructured.io](https://www.linkedin.com/company/unstructuredio/), and
 [KDB.AI](https://www.linkedin.com/company/kdb-ai/), and wrote this article to tell the tale: [https://lnkd.in/gBDNYx68]
(https://lnkd.in/gBDNYx68)  
Key highlights:  
✔ Precise table extraction techniques  
✔ Contextual enrichment using LLM
s  
✔ Clever format standardization tricks  
✔ A unified embedding approach for optimal retrieval  
Enjoy the article an
d share your thoughts in the comments below!
```
---

     
 
all -  [ Support for open source library flow-prompt for Gemini-Claude-OpenAI ](https://www.reddit.com/r/ClaudeAI/comments/1eykriw/support_for_open_source_library_flowprompt_for/) , 2024-08-23-0911
```
Hey, we're (3 developers) developing library flow-prompt based on our experience as Director of AI and other AI startups
. The problem we faced:  
- langchain is good for prototyping, with debugging langchain exceptions for customizzations; 
 
- to distribute the load in production environments across multiple Azure models, or Claude which has OpeAI as fallbac
k startegy;  
- pro-prompting, you need a more smart way to define what should go in prompt and in what order, and budge
t automatically is calculated;  
- model agnostic, btw Gemini, OpenAI, Claude. Despite they need to have their own rules
, with format of adding in the prompt;

So we all included in that library, and 

We added the first CI/CD pipeline ther
e. Which defines statements from the human written response for specific test context. And we compare statements from hu
man response and real LLM response.   
  
We're using that library in the some companies. I'm sure more can benefit. And
 we would be blissed if you will provide feedback and share what you want from next prompt library you wanna try.  
[htt
ps://www.flow-prompt.com/](https://www.flow-prompt.com/)

discord:   
[https://discord.gg/rrgpnspAQa](https://discord.gg
/rrgpnspAQa)


```
---

     
 
all -  [ Tips for Reducing LangChain Package Size in AWS Lambda? ](https://www.reddit.com/r/LangChain/comments/1eykko9/tips_for_reducing_langchain_package_size_in_aws/) , 2024-08-23-0911
```
Hi everyone,

I'm currently working on a project where we're using LangChain in an AWS Lambda function. However, we're f
acing some challenges with the 'langchain' package size due to the dependencies it pulls in, specifically 'numpy' and 's
qlalchemy,' which are significantly bloating our Lambda layer.

At this stage, we only need 'langchain' for the legacy `
AgentExecutor`, and we're trying to keep our deployment as lightweight as possible. Has anyone encountered a similar iss
ue? If so, do you have any tips or workarounds for minimizing the package size or selectively excluding certain dependen
cies?

Any advice would be greatly appreciated!

[](https://www.reddit.com/user/hwchase17/) 
```
---

     
 
all -  [ How to make llm more robust in looking and filtering data for the responses. ](https://www.reddit.com/r/LangChain/comments/1eyjq2f/how_to_make_llm_more_robust_in_looking_and/) , 2024-08-23-0911
```
I was working on a agent where the task was to just using prompt and function calling, I need to make a chabot. 

Bot wo
rks fine with openai gpt4o-mini until I increased one more function. After that I noticed that llm is not using the func
tions properly. So I changed llm to gpt-4o . It start calling appropriately but still lacks in filtering data. It doesn'
t give right answer even the return datatype from the function is structured.

What methods one can suggest to improve t
his thing ?

I have tried improve the prompting , but it doesn't work in enhancing the data looking part.

I added a fil
ter function also to get the accuracy but it doesn't work. The parameter length is too long.
```
---

     
 
all -  [ My Resume Needs Debugging! Help Fix This Mess Before It Crashes My Job Hunt! ](https://i.redd.it/a87ugq2vp7kd1.jpeg) , 2024-08-23-0911
```
Hey folks,I’m looking for some feedback on my resume. I want to make sure it's polished and error-free before sending it
 out. 

Thanks in advance for your help!
```
---

     
 
all -  [ Gemini 1.5 Pro Exp not available  ](https://www.reddit.com/r/LangChain/comments/1eyglwx/gemini_15_pro_exp_not_available/) , 2024-08-23-0911
```
Hi!

I’m trying to use gemini-1.5-pro-exp-0801 with Langchain but get a 404 saying the model is not available. I am able
 to use it with GenAI SDK though. Any thoughts? Has anybody else faced this issue?
```
---

     
 
all -  [ [0 YoE, Student, SDE, India] ](https://www.reddit.com/r/resumes/comments/1eygc8j/0_yoe_student_sde_india/) , 2024-08-23-0911
```
Hey everyone, I am going to apply for SWE FTE roles this year, I need a review on my CV, I had my Internship last summer
 at a firm in Data Analytics role( it is at a Big4 but I admit that I haven't been allotted even a decent amount of work
), and I attached my projects and skills too, I have few academic achievements and extra curricular section in my full r
esume, which I don't want to reveal, please give your review and suggestions on these sections, how do I improvise it, I
 feel this doesn't look good, any suggestions would be appreciated, thanks a lot in advance.

https://preview.redd.it/ss
lg8n0157kd1.png?width=1350&format=png&auto=webp&s=41e3b6f2d1f8bfba46326dc1931bde28c7b73199


```
---

     
 
all -  [ So many people were talking about RAG so I created r/Rag ](https://www.reddit.com/r/LangChain/comments/1eyf4vw/so_many_people_were_talking_about_rag_so_i/) , 2024-08-23-0911
```
In the fast-moving world of AI, I see posts about RAG multiple times every hour in hundreds of different subreddits. It 
definitely is a technology that won't go away soon. For those who don't know what RAG is , it's basically combining LLMs
 with external knowledge sources. This approach lets AI not just generate coherent responses but also tap into a deep we
ll of information, pushing the boundaries of what machines can do.

But you know what? As amazing as RAG is, I noticed s
omething missing. Despite all the buzz and potential, there isn’t really a go-to place for those of us who are excited a
bout RAG, eager to dive into its possibilities, share ideas, and collaborate on cool projects. I wanted to create a spac
e where we can come together - a hub for innovation, discussion, and support.
```
---

     
 
all -  [ Deploying Model to Fireworks ](https://www.reddit.com/r/LangChain/comments/1eyeheu/deploying_model_to_fireworks/) , 2024-08-23-0911
```
I am building on LangGraph and I want to used finetuned Llama 3.1 8b

So I finetuned lama-3.1-8b-instruct-bnb-4bit with 
unsloth and have necessary files in a folder, but how to deploy it to [fireworks.ai](http://fireworks.ai/) is confusing,
 tried to follow the docs  
  
I have windows, but I have ubuntu installed in which I installed firecracker



Really wo
uld appreciate guidance:)
```
---

     
 
all -  [ Is My Approach Considered RAG, and How Can I Improve It? ](https://www.reddit.com/r/LangChain/comments/1eye7bj/is_my_approach_considered_rag_and_how_can_i/) , 2024-08-23-0911
```
Hi everyone,

I'm working with LLMs (like GPT-4) and I want to understand if my current approach is considered a Retriev
al-Augmented Generation (RAG) method and how I might improve it.

Here’s what I’m doing: I’ve set up various tools with 
descriptions that the LLM can use. For example, if a user requests information about 'X,' the LLM calls a specific tool 
that returns data related to 'X.' The LLM then processes this data as part of its response.

For instance, I might have 
a single tool that accepts an input of resource_type. Depending on this input, the LLM fetches different data to work wi
th.

Is this method in line with the RAG framework? If so, are there any best practices or improvements I could implemen
t to enhance the effectiveness of this setup?

Thanks for your insights!
```
---

     
 
all -  [ How to Prevent LLM from Overwriting Parameters Passed to a LangChain Tool in a Custom Agent? ](https://www.reddit.com/r/LangChain/comments/1eyd29z/how_to_prevent_llm_from_overwriting_parameters/) , 2024-08-23-0911
```
I'm working on a custom LangChain agent that uses a tool to make API calls based on parameters passed in the code. Howev
er, I'm encountering an issue where the LLM is generating its own parameters instead of using the ones I pass. Here’s th
e relevant code:

    import requests
    from langchain_core.pydantic_v1 import BaseModel, Field
    from typing import
 Optional
    from langchain.agents import Tool, AgentExecutor, create_tool_calling_agent
    from langchain.chat_models
 import ChatOpenAI
    from langchain_core.tools import StructuredTool
    
    def get_swagger_file(api_name):
        
api_list = requests.get('https://api.apis.guru/v2/list.json').json()
        preferred_version = api_list[api_name]['pre
ferred']
        swagger_url = api_list[api_name]['versions'][preferred_version]['swaggerUrl']
        return requests.g
et(swagger_url).json()
    
    class APIToolInput(BaseModel):
        api_name: str
        method: str
        endpoin
t: str
        params: Optional[dict] = Field(default=None)
        data: Optional[dict] = Field(default=None)
    
    
def call_api(api_name: str, method: str, endpoint, params: dict = None, data: dict = None) -> str:
        swagger_spec 
= get_swagger_file(api_name)
        paths = swagger_spec.get('paths', {})
        if endpoint not in paths:
           
 return {'error': 'Path not found'}
        
        if method not in paths[endpoint]:
            return {'error': 'Met
hod not found'}
    
        server = swagger_spec['servers'][0]['url']
        url = f'{server}{endpoint}'
    
       
 # Make the API call
        response = requests.request(method, url, params=params)
        json_response = response.js
on()
        
        return json_response
    
    def api_tool(input_data: APIToolInput) -> str:
        api_name = in
put_data.api_name
        method = input_data.method
        endpoint = input_data.endpoint
        params = input_data.
params
        data = input_data.data
        
        # Call the API with the parameters
        return call_api(api_na
me, method, endpoint, params, data)
    
    tool = StructuredTool(
        name='APITool',
        func=api_tool,
     
   description='Calls the specified API endpoint with the given method and parameters.',
        args_schema=APIToolInpu
t
    )
    
    llm = ChatOpenAI(temperature=0.7, model_name='gpt-4')
    
    from langchain_core.prompts import ChatP
romptTemplate
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are a helpful as
sistant'),
            ('human', '{input}'),
            ('placeholder', '{agent_scratchpad}'),
        ]
    )
    
   
 agent = create_tool_calling_agent(
        tools=[tool],
        llm=llm,
        prompt=prompt
    )
    
    agent_ex
ecutor = AgentExecutor(agent=agent, tools=[tool], verbose=True)
    
    api_name = 'trakt.tv'
    method = 'get'
    en
dpoint = '/movies/anticipated'
    
    response = agent_executor.invoke({
        'input': 'What are the most anticipat
ed movies?',
        'api_name': api_name,
        'method': method,
        'endpoint': endpoint
    })

The problem is
 that the tool is not using the parameters I provide, but instead, the LLM seems to be generating them. Here’s the outpu
t:

    Entering new AgentExecutor chain...
    
    Invoking: APITool with {'api_name': 'movieDatabase', 'method': 'GET
', 'endpoint': '/movies/anticipated'}

As you can see, the `api_name` has changed to `movieDatabase`, even though I pass
ed `trakt.tv`. I want the tool to use the parameters I define in the code, not those generated by the LLM.

There a way 
to ensure that the parameters I pass are respected?

Any advice or suggestions would be greatly appreciated.
```
---

     
 
all -  [ Significant change in runtime of code when LLM functions are stored in different file ](https://www.reddit.com/r/LangChain/comments/1eycn9t/significant_change_in_runtime_of_code_when_llm/) , 2024-08-23-0911
```
So I'm working on development of a tool which uses ChromaDB, langchain and OpenAI key's from Azure.  
Previously the who
le code was stored in a single file, and there were some global variables in the file. What I did is divided the code in
to separate modules and stored all global vars in a different file and accessing and updating them in each file. What co
uld be the possible reason for increase in time. Everything except accessing global variables is same.
```
---

     
 
all -  [ User Interface for LangGraph Agent ](https://www.reddit.com/r/LangChain/comments/1eyb3fe/user_interface_for_langgraph_agent/) , 2024-08-23-0911
```
Hello, everyone which framework do you guys use for creating a user interface in your agent/rag project? streamlit, grad
io or others?

And what is the simplest way to create a user interface for a PoC agent project?

Thanks, have a nice day
.
```
---

     
 
all -  [ Build LLM applications without using any framework  ](https://www.reddit.com/r/ChatGPT/comments/1ey9z4n/build_llm_applications_without_using_any_framework/) , 2024-08-23-0911
```
As there are so many frameworks like crewai, langchain, llamaindex and so on. I was wondering is there any way to build 
pipelines with good old ETL methods. Basically Agentic approach is fancy way to say ETL. Are there any suggestions or st
eps I can follow to build LLM powered apps using openai, pydantic and my data. Been curious for while. Please let me kno
w! 
```
---

     
 
all -  [ Is RAG still a thing? ](https://www.reddit.com/r/LangChain/comments/1ey94rs/is_rag_still_a_thing/) , 2024-08-23-0911
```
I was working on a project to put a code base behind RAG/LLM. And I was blocked by access to CI machine allowed by my jo
b. A few months later, I'm wondering out loud if RAG is still a thing or if this project should use something else. 

At
 this point, I'm using a version of ChatGPT 4 for the LLM (not OpenAI), so not training our own LLM. RAG had been so so 
and had been planning on experimenting w/ different text embedders.
```
---

     
 
all -  [ LangGraph Visualizer support for VS Code ](https://www.reddit.com/r/LangChain/comments/1ey8rs6/langgraph_visualizer_support_for_vs_code/) , 2024-08-23-0911
```
[https://marketplace.visualstudio.com/items?itemName=hfloveyy.langgraphv](https://marketplace.visualstudio.com/items?ite
mName=hfloveyy.langgraphv)

# LangGraph Visualizer

LangGraph Visualizer is a VS Code extension for visualizing and mani
pulating LangGraph structures directly within your coding environment.

# Features

* Interactive graph visualization an
d manipulation
* Real-time updates reflecting code changes
* Automatic vertical or horizontal layout organization
* New 
graph template for quick project starts
* Seamless Python file integration

# Getting Started

1. Install LangGraph Visu
alizer from VS Code Marketplace.
2. Open a Python file with a LangGraph structure or create a new one.
3. Use the comman
d palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) to 'Open LangGraph Visualizer' or 'New LangGraph'.

# Usage

* Visualize and
 edit existing graphs or create new ones
* Modify graph structure visually or via Python code
* Rearrange layout with 'V
ertical' or 'Horizontal' buttons
* Add new nodes with the 'Add Node' button
* Use standard VS Code save shortcut (Cmd + 
S / Ctrl + S) to update the visualization

# Tip

Ensure your file is saved to see changes reflected in the graph visual
ization.

# Requirements

* Visual Studio Code 1.60.0+
* Python 3.7+

# Feedback and Contributions

We welcome your inpu
t! Please visit our [GitHub repository](https://github.com/hfyydd/langgraphv) for issues and pull requests.

# License


This project is under the MIT License. See the [LICENSE](https://github.com/hfyydd/langgraphv/blob/HEAD/LICENSE) file fo
r details.
```
---

     
 
all -  [ Question about parsing PDF ](https://www.reddit.com/r/LangChain/comments/1ey8og3/question_about_parsing_pdf/) , 2024-08-23-0911
```
Here's a translated and rephrased version of your question that aims to convey your intent clearly in English:

I'm tryi
ng to find the best way to parse PDF files that have multiple column layouts and contain numerous images. I'm facing som
e challenges and would appreciate advice on how to proceed:

1. When I load the file using LlamaParse, it correctly orde
rs the content of each page according to the layout (left to right). However, when I attempt to combine text that spans 
multiple pages and then apply a TextSplitter, I encounter issues. For instance, a table from the right column might be i
nserted in the middle of the left column's text, preventing the left column's text from connecting properly with the tex
t on the next page's left column. This makes it difficult to apply the TextSplitter effectively. What would be a good ap
proach to resolve this issue?
2. I've considered using PDFPlumber to create bounding boxes for images, then combining th
e text from multiple pages that falls outside these bounding boxes. My plan was to process this combined text using a Te
xtSplitter, handle the images (within the bounding boxes) separately, and add metadata to indicate which page each image
 appears on. However, I realized that using a TextSplitter would render the original page metadata meaningless. This lea
ves me unsure about how to properly set metadata for the images to maintain their context within the document.

Can you 
suggest effective strategies for handling these challenges in parsing complex PDF layouts while preserving the relations
hip between text and images across multiple pages?

https://preview.redd.it/m98zrmqkq4kd1.png?width=1316&format=png&auto
=webp&s=a1001802e7e231efff6da540e0c9d77315e59e8f


```
---

     
 
all -  [ [3 YoE, Data Science Contractor, Data Scientist, USA] - I am targeting Tier 1 companies. ](https://www.reddit.com/r/resumes/comments/1ey7veg/3_yoe_data_science_contractor_data_scientist_usa/) , 2024-08-23-0911
```
I'm looking for some resume advice. I've been applying to various data science jobs through referrals and have not been 
lucky - I wanted to understand if my resume is failing me or if it's the saturated market.

I tailor my resume as well. 
I am primarily targeting Data Scientist and Senior Data Analyst roles

Give me your honest and most brutal feedback if a
ny, any advice and feedback is appreciated.

Thanks

https://preview.redd.it/i5ruhwr4k4kd1.png?width=5100&format=png&aut
o=webp&s=80a33ae2f5128ddd82b410fdf365f2a044e64235


```
---

     
 
all -  [ [1 YoE, Data Science Co-op, Data Scientist, United States] ](https://www.reddit.com/r/resumes/comments/1ey4bpi/1_yoe_data_science_coop_data_scientist_united/) , 2024-08-23-0911
```
I've been applying to entry-level data science positions but haven't received any callbacks. My only professional experi
ence in the field is from a co-op, and I’m unsure if my resume highlights the right projects. Some job postings ask for 
GenAI, LLM, or deep learning experience, while others emphasize data engineering skills. I'm confused about what to incl
ude on my resume to get noticed by hiring managers. Any advice on improving my resume or strategy would be greatly appre
ciated! Please tell me everything wrong with my resume

https://preview.redd.it/jugj7bstp3kd1.png?width=977&format=png&a
uto=webp&s=384a381edbb0562c485b61d5c6bd7d1a3ea5f0c6


```
---

     
 
all -  [ Advice Needed: Struggling with Entry-Level Data Science Resume and Job Applications ](https://www.reddit.com/r/learnmachinelearning/comments/1ey3yp0/advice_needed_struggling_with_entrylevel_data/) , 2024-08-23-0911
```
've been applying to entry-level data science positions but haven't received any callbacks. My only professional experie
nce in the field is from a co-op, and I’m unsure if my resume highlights the right projects. Some job postings ask for G
enAI, LLM, or deep learning experience, while others emphasize data engineering skills. I'm confused about what to inclu
de on my resume to get noticed by hiring managers. Any advice on improving my resume or strategy would be greatly apprec
iated!

https://preview.redd.it/vttp9f1vm3kd1.png?width=977&format=png&auto=webp&s=69e4f610f1a4f14e20668ee65025b9c59a31a
42c


```
---

     
 
all -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-23-0911
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
all -  [ Human in the Loop for Autonomous Agents ](https://www.reddit.com/r/LangChain/comments/1ey1qia/human_in_the_loop_for_autonomous_agents/) , 2024-08-23-0911
```


I found myself building a bunch of LLM-backed features that needed to use tool calling, and some of those tools involv
ed doing things that were somewhat high stakes - communicating on my behalf or modifying shared / production data. one e
xample - I wanted to replace a marketing website with a chatbot + vector DB loaded with the previous content, docs, and 
blog posts.

Between hallucinations, missing knowledge base info, and the LLM generally writing like an psuedo-intellect
ual high schooler, I realized I couldn't trust it to communicate unsupervised with my website visitors. I needed a way t
o improve the percent of high-quality responses, and do it this at scale.

I wired up a prototype that would

1. consult
 me in slack before sending any response down to a website visitor
2. incorporate my feedback into the knowledge base, a
nd
3. reformulate answers until I approved the message
4. send it to the visitor

That prototype evolved into what is no
w HumanLayer [https://github.com/humanlayer/humanlayer#why-humanlayer](https://github.com/humanlayer/humanlayer#why-huma
nlayer)

  
Update - want to acknowledge this is similar to some of the stuff u/tisi3000 has posted as well!
```
---

     
 
all -  [ * Possibly noob post, I need help or a reference to some article to write the appropriate data for a ](https://www.reddit.com/r/LangChain/comments/1exyxkf/possibly_noob_post_i_need_help_or_a_reference_to/) , 2024-08-23-0911
```
Am attempting to use the langchain/StructuredOutputParser to generate json from the openai response, this is the output 
i am looking for...  


    // example
    {
        'ratings': [
            {
                'num': 1,
              
  'title': 'Customer Engagement',
                'score': 8,
                'total': 10,
                'comment': 'G
ood customer engagement'
            },
            {
                'num': 2,
                'title': 'Product Knowle
dge',
                'score': 9,
                'total': 10,
                'comment': 'Excellent product knowledge'

            },
            {
                'num': 3,
                'title': 'Problem Solving',
                'scor
e': 7,
                'total': 10,
                'comment': 'Needs improvement in problem solving'
            }
    
    ],
        'total_obtained': 24,
        'total_score_available': 30
    }

I can't find a proper explanation of the
 docs to help me. Do you have any ideas?  this is my current schema that does not produce the result...😔

response\_sche
mas = \[  
ResponseSchema(  
name='rating',  
description='Individual rating item',  
fields=\[  
{'name': 'num', 'type'
: 'int'},  
{'name': 'title', 'type': 'str'},  
{'name': 'score', 'type': 'int'},  
{'name': 'total', 'type': 'int'},  

{'name': 'comment', 'type': 'str'},  
\]  
), ResponseSchema(  
name='ratings\_response',  
description='Ratings respons
e',  
fields=\[  
{'name': 'ratings', 'type': 'Dict\[str, Rating\]'},  
{'name': 'total\_obtained', 'type': 'int'},  
{'
name': 'total\_score\_available', 'type': 'int'},  
\]  
)\]
```
---

     
 
all -  [ Getting a structured tavily response ](https://www.reddit.com/r/LangChain/comments/1exwujh/getting_a_structured_tavily_response/) , 2024-08-23-0911
```
I've tried different things such as binding TavilySearchResults and my own Pydantic Model as llm tools but I never seem 
to get reliable results. Does anyone have an idea on how to achieve a structured output from using Tavily as a tool? 

F
or example: I'm using Tavily to find the best restaurant in Boston. I'd like to get certain information about that resta
urant as a structured response (e.g. 'location': 'example street', 'opening hours:' 'mo-fr'...).

I also tried using the
 TavilySearchAPIRetriever but without success.
```
---

     
 
all -  [ Suggestions needed in building AI part of a SAAS platform  ](https://www.reddit.com/r/developersIndia/comments/1exvhjr/suggestions_needed_in_building_ai_part_of_a_saas/) , 2024-08-23-0911
```
Hey, I’m working on a platform where users can connect their Ads accounts, allowing us to retrieve and store their ad da
ta. Users can then interact with a chatbot to ask questions like 'How did my ads perform last week?' or 'What can I do t
o improve performance?' The chatbot provides answers based on the available data context.

Currently, I’m using a RAG ap
proach, where I chunk the data, store it in a vector database, and use LangChain to create the pipeline with a prompt te
mplate. However, I’m running into issues where the chatbot sometimes generates incorrect responses, and I’m also encount
ering token limit errors.

I’m looking for alternative methods to address these problems and would really appreciate you
r insights and feedback on this.
```
---

     
 
all -  [ Developed a New Project for Extracting structured data from unstructured text Using Azure AI and Ope ](https://www.reddit.com/r/LangChain/comments/1exuop7/developed_a_new_project_for_extracting_structured/) , 2024-08-23-0911
```
Hey everyone!

I've developed a new project that uses Azure AI Document Intelligence and Azure OpenAI to extract structu
red data from all kinds of documents—PDFs, Word files, images, and more. For example, let’s say you want to extract some
 pre-defined information from a utility bill in a structured format.

Here's how it works:

1. Your documents get ingest
ed by the service.
2. Azure AI Document Intelligence converts them into structured Markdown.
3. I then use Azure AI's fu
nction calling capabilities to send the Markdown to Azure OpenAI, which parses it and outputs the data in clean JSON for
mat.

The best part is, this is highly customizable to fit your specific needs. You can define your own data schemas and
 prompts, and the system will handle the rest.

This is a paid service, so if you're interested in a demo or want to lea
rn more about how I can help with your document processing needs, feel free to shoot me a DM. I'm offering this as a fre
elance service, and I'd be happy to show you how it all comes together!

```
---

     
 
all -  [ Suggestion on fresher salary for SDE mostly working in LLM/RAG fullstack application ](https://www.reddit.com/r/developersIndia/comments/1exu0i5/suggestion_on_fresher_salary_for_sde_mostly/) , 2024-08-23-0911
```
from the last one month i was working in the 8 year old company as a trainee there they newly open an ai labs where i wa
s soley responsbile to work on various project that revolves around LLM/RAG fullstack application based on LLM/RAG mostl
y work with open ai langchain, llamaindex
so today my training period is completed and they are going to offer me full t
ime role there so on the upcoming days i had a salary discussion with my company director as i am directly working with 
him 

Wanted to know about what was the salary i should expect from them for this role

and what was the starting salary
 for this role 


```
---

     
 
all -  [ Headless IDE for Coding Agents ](https://www.reddit.com/r/LocalLLaMA/comments/1extoy6/headless_ide_for_coding_agents/) , 2024-08-23-0911
```
\[Update\]: added demo

Hi all! This post is less about models and more about tooling. But it's 100% LLM-related and can
 be run locally.

After making several attempts to make coding agents work I noticed the same pattern: the better the to
ols you give to agents, the better outcomes they produce. So I thought what if I gave them a proper IDE except it would 
be headless since agents don’t need a UI? That’s how I came to build Hide, a headless IDE for coding agents.

Hide is bu
ilt on top of existing tools and standards for coding like devcontainers and LSP. When given a code repo, Hide spins up 
a devcontainer, installs the dependencies, and provides APIs for codebase interaction. Developers can craft custom toolk
its using Hide APIs or use Hide's pre-built toolkits for popular frameworks like Langchain.

The project is still a work
 in progress but it can already be tried. I’m curious to hear what you think.

Documentation: [https://hide.sh/](https:/
/hide.sh/)

GitHub: [https://github.com/artmoskvin/hide](https://github.com/artmoskvin/hide)

Demo: [https://www.loom.co
m/share/3b4927249302487d985cc02fb606d9ca](https://www.loom.com/share/3b4927249302487d985cc02fb606d9ca)
```
---

     
 
all -  [ Learning Path for LangChain as a Full Stack Dev with 10+ Years Experience? ](https://www.reddit.com/r/LangChain/comments/1extkyw/learning_path_for_langchain_as_a_full_stack_dev/) , 2024-08-23-0911
```
Hey folks ✌️

I’m a full stack dev with 10+ years in the game, mostly working with JavaScript/TypeScript, React, and Nod
e.js. I’m diving into LangChain and would love some guidance on the best way to learn it.

What’s the best learning path
 or resources for someone with my background? And just to be clear, a 1-hour online course or just reading the docs does
n’t count—I’m looking for something meatier! 😅

Thanks!
```
---

     
 
all -  [ llmio: A Lightweight Library for LLM I/O ](https://www.reddit.com/r/Python/comments/1exsm6z/llmio_a_lightweight_library_for_llm_io/) , 2024-08-23-0911
```
Hey everyone,

&nbsp;

I'm excited to share [llmio](https://github.com/badgeir/llmio), a lightweight Python library for 
LLM I/O. llmio makes it easy to define and use tools with large language model (LLM) APIs that are compatible with OpenA
I's API format.

&nbsp;

**What My Project Does**:

- **Easy tool definition**: Uses type annotations to parse function 
signatures and automatically adds them to the agent's capabilities.
- **Focus on what matters**: Abstracts away the API 
details so you can concentrate on your core project.
- **Lightweight**: The core library itself is less than 500 lines o
f code.
&nbsp;

**Target Audience**:
llmio is designed for developers who are working with LLM agents / applications wit
h tool capabilities,
and for people who want a quick way to set up and experiment with tools.
It is designed for product
ion use.

&nbsp;

**Comparison**:

Allthough alternatives like Langchain exists, these libraries attempt to do much more
. **llmio** is meant as a lightweight library with a clear and simple interface for adding tool capabilities to LLM agen
ts and applications.

&nbsp;

Check it out on [Github](https://github.com/badgeir/llmio), I'd love to hear your feedback
 and see what you build with it!

```
---

     
 
all -  [ How do I add chat memory to RetrievalQA chain in langchain? ](https://www.reddit.com/r/Rag/comments/1exq8lb/how_do_i_add_chat_memory_to_retrievalqa_chain_in/) , 2024-08-23-0911
```
I have tried the memory classes in langchain but they don't seem to do the job well. I know there is an option of using 
Conversational chain but my task involved a lot of vector search so that wouldn't be the best solution. I believe the in
dustry standard is use another chain to store context and rephrase the user input to include context in the question bef
ore passing it to the RetrievalQA. However, my manager wants me to store just the questions and answers of first 10 conv
ersations. I'm not sure how to do it. I was thinking - store them in a list and update it in prompt template 'history' p
laceholder as a str. Either way idk how to do it. Pls help!
```
---

     
 
all -  [ How are you doing Agent Workflows? ](https://www.reddit.com/r/LangChain/comments/1expshp/how_are_you_doing_agent_workflows/) , 2024-08-23-0911
```
Hey Friends!

I'm wondering - how are you orchestrating agent workflows? I've seen some cool tools like [hatchet.run](ht
tp://hatchet.run), but there are more AI specific ones too (+LangGraph). I'm curious what the community is up to.

What 
makes a good workflow orchestration tool?
```
---

     
 
all -  [ World's Most Comprehensive RAG Tutorials Repo (Open Source) Now Open to Contributions + Community Di ](https://github.com/NirDiamant/RAG_Techniques) , 2024-08-23-0911
```
Our open-source RAG repository is exploding! Here's why:

- 20+ cutting-edge techniques
- Detailed explanations & visual
izations
- Real-world use cases
- Active community

🌟 Contribute & Get Recognized!
Add techniques, improve docs, create 
visuals - every contributor gets credited!

 📚 Here to Learn?
Dive into our guides and notebooks. All levels welcome!

 
🔗 Get Involved:
1. Star & fork the repo
2. Contribute your expertise
3. Join our Discord (link in repo)
```
---

     
 
all -  [ Pause/Terminate Streaming Messages (LangGraph) ](https://www.reddit.com/r/LangChain/comments/1expes5/pauseterminate_streaming_messages_langgraph/) , 2024-08-23-0911
```
In ChatGPT one can press the stop button while the interface is streaming a response, to halt the remaining responses, a
nd the incomplete response is stored in history.

I have no idea if the LLM itself is actually halted, or if it just sto
ps accepting new messages from the backend.

Is there a way to do this canceling in the graph?

I use the graphs `astrea
m_events` and yield responses to the front-end via FastAPI's StreamingResponse. I imagine that to halt streaming, I can 
listen for a flag in the endpoint method, and instead of yield, I could just break or return, which would stop sending r
esponses.

However, the LLM will still be being executed. Is it possible halt execution as well?
Even more, rather than 
stop the graph altogether, is it possible to just stop that LLM node? That way, it could proceed to the other nodes I ha
ve that work on saving conversation messages, etc.
```
---

     
 
all -  [ Multi-Agent  Supervision  (OpenAI Assistants: Directly) ](https://www.reddit.com/r/LangChain/comments/1exp8nl/multiagent_supervision_openai_assistants_directly/) , 2024-08-23-0911
```
I’ve been diving into multi-agent architecture Supervision  using OpenAI Assistants, and I’ve hit a snag. While tutorial
s on supervision work great, I’m having trouble directly connecting with a specific Assistant ID  (OpenaAI ) that I want
 modify through the OpenAI dashboard.





Is anyone else facing this issue? Have you found any solutions or workarounds
? I’d love to hear your thoughts or experiences. I’m eager to get this working smoothly, so any advice would be greatly 
appreciated!



I’m looking forward to your responses!
```
---

     
 
all -  [ Using Fallbacks in LangChain.js ](https://www.reddit.com/r/LangChain/comments/1exooz7/using_fallbacks_in_langchainjs/) , 2024-08-23-0911
```
Hi folks! I've made this short article on how to use Fallbacks in LangChain.js   
[https://www.js-craft.io/blog/fallback
s-langchain-javascript/](https://www.js-craft.io/blog/fallbacks-langchain-javascript/)

I think fallbacks are a useful f
eature and can be used in many creative ways. What do you think? 
```
---

     
 
all -  [ How to develop a structured Streamlit + Langchain app ? ](https://www.reddit.com/r/LangChain/comments/1exoi03/how_to_develop_a_structured_streamlit_langchain/) , 2024-08-23-0911
```
Hello everyone , I'm a web dev currently learning AI , a beginner in Python and AI in general .

If anyone of you is fam
iliar with ReactJS or other web frameworks , you know that when building a project we structure our app into different c
omponents ( src/pages , src/modules , src/utils etc ) .

Is there any standard way of developing streamlit apps in a mod
ular way similar to how we do in ReactJS and other frameworks ?

Asking this because I'm currently developing a PDF RAG 
app . It is \~500 lines of code in a single file ( app . py file ) ... One function after another ... and the code doesn
't look good at all

I hope I'm able to convey my problem , I've asked this question in Streamlit reddit as well , repea
ting here as I use Langchain in my app extensively . Thanks in advance !
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-23-0911
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-23-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-23-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-23-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
