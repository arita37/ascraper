 
all -  [ Help on a rag application ](https://www.reddit.com/r/LangChain/comments/1felvjc/help_on_a_rag_application/) , 2024-09-12-0912
```
So my team and I are working on building a gpt wrapper app and I want to build a rag system by indexing some notes I too
k on “Atomic Habits” book. Obviously it doesn’t make sense to index a whole book so I’m using my notes, or I don’t even 
know how expensive it will be to index the whole thing. I have experience with building small rag applications. My quest
ion is that I’m not experienced and I am looking for opinions on how I can outline this idea and execute it. if anyone h
as any tips regarding using langchain. Thanks
```
---

     
 
all -  [ AWS Reference Architecture for txtai RAG ](https://www.reddit.com/r/aws/comments/1feevhx/aws_reference_architecture_for_txtai_rag/) , 2024-09-12-0912
```
https://preview.redd.it/4e3mygwbl7od1.png?width=1746&format=png&auto=webp&s=650f35fd4139e5ba89f1b21726c60af025181108

[t
xtai](https://github.com/neuml/txtai) is an all-in-one open-source embeddings database for semantic search, LLM orchestr
ation and language model workflows.

txtai has support for both local and API-driven embeddings services and models. Thi
s reference architecture uses AWS Bedrock for embeddings + LLM calls. Content is stored in Postgres/pgvector via Aurora 
or RDS.  
  
Other frameworks like LangChain and LlamaIndex require code changes to switch from local to cloud. The same
 code can handle both with minor configuration changes in txtai!

https://preview.redd.it/lsd9bu4il7od1.png?width=886&fo
rmat=png&auto=webp&s=e28584c49ac346a951ac16bdd469cb15ff062cc5

Code: [https://gist.github.com/davidmezzetti/e5907591e941
1f47da7f9a9e91ec9d84](https://gist.github.com/davidmezzetti/e5907591e9411f47da7f9a9e91ec9d84)
```
---

     
 
all -  [ Reliable Agentic RAG with LLM Trustworthiness Estimates ](https://www.reddit.com/r/LangChain/comments/1fee66b/reliable_agentic_rag_with_llm_trustworthiness/) , 2024-09-12-0912
```
I've been working on Agentic RAG workflows and I found that automating decisions on LLM outputs can be pretty shaky. A*g
entic RAG* considers various retrieval strategies as tools available to an LLM orchestrator that can *iteratively decide
* which tools to call next based on what it’s seen thus far. The tricky part is how do we actually *decide* automaticall
y? 

[Using a trustworthiness score, the RAG Agent can choose more complex retrieval plans or approve the response for p
roduction.](https://preview.redd.it/ie2jqm9xf7od1.png?width=1560&format=png&auto=webp&s=658d5e3ee7391b7c2a1700251b892373
69b25750)

I found some success using uncertainty estimators to verify the trustworthiness of the RAG answer. If the ans
wer was not trustworthy enough, I increase the complexity of the retrieval plan in efforts to get better context. I [wro
te up](https://pub.towardsai.net/reliable-agentic-rag-with-llm-trustworthiness-estimates-c488fb1bd116) some of my findin
gs, if you're interested :)

Has anybody else tried building RAG agents? Have you had success decisioning with noisy LLM
 outputs?


```
---

     
 
all -  [ [1 YoE] Entry Level Engineer looking for roles in Traditional ML and Generative AI ](https://www.reddit.com/r/EngineeringResumes/comments/1fee3u4/1_yoe_entry_level_engineer_looking_for_roles_in/) , 2024-09-12-0912
```
Hi any review of my CV would be helpful thank you. I'm aware of some possible problems that may be present already:

* G
ap between education and previous employment. This is because of massive burnout after finishing degree most likely rela
ted to very recently diagnosed ADHD.
* It looks like there is a lack of traditional ML in my skillset however outside of
 my tutoring I haven't been working on any projects since I finished my education.
* Second role is essentially a contin
uation of the first role working directly with the client - i'm worried the short length of the role will put hiring man
agers off.

I'm looking for roles in London or remotely.

To be honest I'm not sure where to start with my CV, I imagine
 I will need to undertake a couple of projects to showcase more of my skills and help to improve my coverage.  I don't r
eally know if I am making the most of what experience I do have so any help would be appreciated.

https://preview.redd.
it/80g7l2m5g7od1.png?width=5100&format=png&auto=webp&s=b433c0a6f22e6656047cd8eacccc36cd9c5f70a4
```
---

     
 
all -  [ We built a unified customer data RAG for LangChain based on entity resolution technology ](/r/LangChain/comments/1fedc3v/we_built_a_unified_customer_data_rag_for/) , 2024-09-12-0912
```

```
---

     
 
all -  [ We built a unified customer data RAG for LangChain based on entity resolution technology ](https://www.reddit.com/r/LangChain/comments/1fedc3v/we_built_a_unified_customer_data_rag_for/) , 2024-09-12-0912
```
Hi LangChain community,

I'm Steven, one of the co-founders of Tilores, where we focus on real-time entity resolution to
 unify customer data. Recently, we've had some interesting conversations around how our solution could be used with LLMs
, so we built an integration for LangChain.

With this integration, Tilores can serve as a retrieval-augmented generatio
n (RAG) source for customer data. It allows you to unify data from various sources, update profiles in real-time, and pe
rform fuzzy searches across unified customer graphs—all within your LLM workflows.

We're looking for early users to hel
p test and explore some use cases. If you're working with customer data and want to integrate it into your LangChain pro
jects, we'd love to talk.

The setup is quick, with no maintenance, and it scales with your data.

You can see our LangC
hain integration here: [https://github.com/tilotech/langchain-tilores](https://github.com/tilotech/langchain-tilores)

I
'd love to hear your thoughts. 


```
---

     
 
all -  [ Langchain agents fun project idea ](https://www.reddit.com/r/LangChain/comments/1fed189/langchain_agents_fun_project_idea/) , 2024-09-12-0912
```
I need to prepare a fun project with Agents for a team meeting. Can you share with me ideas to showcase how powerful it 
is.
The more fun the better ! 

Thanks ! 
```
---

     
 
all -  [ How can I improve my Github Query Parameter Generator tool ? ](https://www.reddit.com/r/LangChain/comments/1fe8zgz/how_can_i_improve_my_github_query_parameter/) , 2024-09-12-0912
```
Hello everyone , I'm currently learning Langgraph and trying to create a Github Agent which takes in a natural language 
query like 'Frontend developer based in India skilled in NextJS' and generates query parameters that will be used to sea
rch using Github User Search API .

Langchain does not have any tool for this use case , so I'm trying to develop my own
 .

For the project I'm developing , I'm following hierarchical agent architecture .

You can see my 2 tools below i.e.q
uery\_param\_generator tool and fetch\_users tool and their respective agent nodes i.e. query\_param\_generator\_node an
d fetch\_users\_node :

    from langchain_core.tools import tool
    from langchain_core.prompts import ChatPromptTempl
ate
    from langchain_openai import ChatOpenAI
    import requests
    import functools
    from langgraph.prebuilt imp
ort create_react_agent
    
    
    u/tool('query_param_generator')
    def query_param_generator(query:str):
        '
''
        Takes a natural language query as input and returns the appropriate query parameters based on the rules defin
ed in system_message
        '''
    
        query_gen_system = '''
        Strictly follow all the rules below to gene
rate query parameters for GitHub User Search . Ensure all rules are followed to generate accurate search queries.
      
  Only return the query , no extra information .
        # GitHub User Search - Query Parameter Generation Rules
    
  
      The following guidelines define how to construct query parameters for the GitHub User Search. Ensure all rules are
 followed to generate accurate search queries.
    
        # Overview
    
        1. Search Scope: Applies to public p
ersonal GitHub accounts (not organizations).
        2. Query Components: Queries can include:
        3. Keywords: For 
general information like usernames, names, emails, and bios.
        4. Qualifiers: For searching specific fields.
     
   5. Sort Parameters: Optional but can be added for ordering results.
        6. Case Sensitivity: Keywords are case-in
sensitive.
        7. Result Limit: The search returns the first 1000 results, sorted by best match (by default).
    
 
       # Qualifiers & Usage
    
        Each qualifier targets a specific field in the GitHub user data. These cannot b
e mixed with regular keywords.
    
        user:NAME: Matches exact usernames.
        Example: user:braingain
    
   
     in:login: Searches within usernames (non-exact matches allowed).
        Example: braingain in:login
    
        i
n:email: Searches within users' email addresses.
        Example: irina in:email
    
        in:name: Searches within u
sers' full names.
        Example: Irina in:name
    
        fullname:NAME: Similar to in:name, searches users' full na
mes.
        Example: fullname:john smith
    
        location:NAME: Searches users based on location.
        Example:
 location:Boston
    
        language:NAME: Finds users based on the primary language of their public repositories.
   
     Example: language:python
    
        repos:n: Searches users by the number of public repositories.
        Example
: repos:>1000
    
        followers:n: Searches users by the number of followers.
        Example: followers:>1000
    

        created:DATE: Finds users by their GitHub account creation date.
        Example: created:>2020-01-01
    
    
    is:sponsorable: Finds users with a GitHub Sponsors profile.
        Example: is:sponsorable
    
        sort:: Sort
s users based on specific attributes.
        Example: repos:>10000 sort:followers
    
        # Boolean Operators
    
    You can combine keywords and qualifiers using Boolean operators to refine the search. Follow these rules:
    
     
   AND (implied): Combining two different qualifiers or a qualifier and a keyword automatically implies AND.
        Exa
mple: location:'San Francisco' language:python (Finds users in San Francisco who primarily use Python).
    
        OR:
 Explicitly use OR between keywords or in: qualifiers only. For other qualifiers, using the same qualifier twice implies
 OR.
        Example: 'front-end developer' OR 'ui developer'
        Example: location:'new jersey' location:'new york'
 (Finds users in either New Jersey or New York).
    
        NOT (-): Use the minus sign (-) to exclude certain terms o
r qualifiers.
        Example: location:iceland -location:Reykjavik (Finds users in Iceland but not Reykjavik).
    
   
     # Key Limitations & Constraints
    
        Character Limit: Queries must not exceed 256 characters.
    
        
No Parentheses: Do not use parentheses in queries.
    
        AND/OR/NOT Limits: You cannot use more than five AND, OR
, or NOT operators in a single query.
        For example: location:'silicon valley' -language:java -language:c++ -langu
age:python -language:javascript -language:html is valid (5 negations).
        Special Notes on Combining Operators
    

        AND is implied for combining qualifiers and keywords but cannot be used explicitly with certain fields like loc
ation, language, etc.
    
        OR cannot be used explicitly between different qualifiers.
        Example: fullname:
irina user:braingain is interpreted as AND, while fullname:irina OR user:braingain is invalid.
    
        You cannot c
ombine keywords and qualifiers in OR statements.
        Example: language:java OR 'java developer' is invalid, while la
nguage:java 'java developer' is interpreted as AND.
        '''
        query_gen_prompt = ChatPromptTemplate.from_messa
ges(
            [('system', query_gen_system),('user','{input}')]
        )
        query_gen = query_gen_prompt | Chat
OpenAI(model='gpt-4o-mini', temperature=0)
        res = query_gen.invoke(input=query)
        return res.content
    
 
   
    @tool('fetch_users')
    def fetch_users(query_param:str):
        '''Gets a list of Github users based on a que
ry parameters generated by query_param_generator tool.'''
        print('query_param :',query_param)
        res = reque
sts.get(
            f'https://api.github.com/search/users?q={query_param}'
        )
        print('response logged :',
res.json())
        return res.json()
    
    
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    
    def qu
ery_param_generator_node(agent_node):
    
        query_param_generator_agent = create_react_agent(llm, tools=[query_pa
ram_generator])
        query_param_node = functools.partial(agent_node, agent=query_param_generator_agent, name='query_
param_generator')
        return query_param_node
    
    
    def fetch_users_node(agent_node):
    
        fetch_use
rs_agent = create_react_agent(llm, tools=[fetch_users])
        fetch_node = functools.partial(agent_node, agent=fetch_u
sers_agent, name='fetch_users')
        return fetch_node

now , below is the code for my github supervisor agent , this
 agent has query\_param\_generator\_node and fetch\_users\_node agents available :

    import github_agent
    from typ
ing import Annotated, List
    from langchain_core.messages import BaseMessage, HumanMessage
    import operator
    fro
m typing_extensions import TypedDict
    from langchain_openai.chat_models import ChatOpenAI
    from langgraph.prebuilt
 import create_react_agent
    from create_team_supervisor_func import create_team_supervisor_func
    from langgraph.gr
aph import END, StateGraph, START
    import create_image_func
    
    # GithubTeamState graph state
    class GithubTe
amState(TypedDict):
        # A message is added after each team member finishes
        messages: Annotated[List[BaseMe
ssage], operator.add]
        # The team members are tracked so they are aware of
        # the others' skill-sets
     
   team_members: List[str]
        # Used to route work. The supervisor calls a function
        # that will update this
 every time it makes a decision
        next: str
    
    
    # The following functions interoperate between the top l
evel graph state
    # and the state of the research sub-graph
    # this makes it so that the states of each graph don'
t get intermixed
    def enter_chain(message: str):
        results = {
            'messages': [HumanMessage(content=me
ssage)],
        }
        return results
    
    def github_team_supervisor(agent_node)-> str:
    
        llm = Chat
OpenAI(model='gpt-4o-mini')
    
        query_param_node = github_agent.query_param_generator_node(agent_node)
    
   
     fetch_node = github_agent.fetch_users_node(agent_node)
    
        def supervisor_agent(state):
    
            g
ithub_supervisor_agent = create_team_supervisor_func(
                llm,
                'You are a supervisor tasked 
with managing a conversation between the'
                ' following workers:  query_param_generator, fetch_users. Give
n the following user request,'
                ' always respond with the query_param_generator worker as it will be call
ed first and take its output as parameter to fetch_users worker'
                ' After calling fetch_users , respond w
ith FINISH.',
                ['query_param_generator', 'fetch_users'],
            )
            return github_supervis
or_agent
    
        github_graph = StateGraph(GithubTeamState)
        github_graph.add_node('query_param_generator', 
query_param_node)
        github_graph.add_node('fetch_users', fetch_node)
        github_graph.add_node('supervisor', s
upervisor_agent)
    
        # Define the control flow
        github_graph.add_edge('query_param_generator', 'supervis
or')
        github_graph.add_edge('fetch_users', 'supervisor')
        github_graph.add_conditional_edges(
            
'supervisor',
            lambda x: x['next'],
            {'query_param_generator': 'query_param_generator', 'fetch_use
rs': 'fetch_users', 'FINISH': END},
        )
    
    
        github_graph.add_edge(START, 'supervisor')
        chain
 = github_graph.compile()
    
        github_chain = enter_chain | chain
        create_image_func.create_graph_image(c
hain, 'github_graph_image')
        return github_chain

this setup works but can only build basic queries , you can see
 that I've written all the rules for building the query parameters in the system prompt , but still I'm not getting perf
ect output ( the query parameters ) . How can I make improvements to my tools and the code snippet in general .

Thanks 
!
```
---

     
 
all -  [ Recommendations for matching taxonomy structures with data sources ](https://www.reddit.com/r/LangChain/comments/1fe7wt3/recommendations_for_matching_taxonomy_structures/) , 2024-09-12-0912
```
I have these requirement to find this taxonomies in my data. I already vectorized in qdrant, chromadb and opensearch/ela
sticsearch. Now I want to iterate the list from the picture to find relevant data in the mentioned databases.  
  
Any s
uggestions on the best approaches, technologies, or tools to achieve this would be greatly appreciated. Thanks for your 
input!

https://preview.redd.it/uvalq10b26od1.png?width=3380&format=png&auto=webp&s=f224f87dbad43e179c3e5d9b1ac06a2cf1a6
07d8


```
---

     
 
all -  [ Langsmith + RAGAS Evaluation of RAG chatbot ](https://www.reddit.com/r/LangChain/comments/1fe784t/langsmith_ragas_evaluation_of_rag_chatbot/) , 2024-09-12-0912
```
Hey guys, I have an RAG chatbot that was built on chainlit, langchain (version 2). And now, I need to evaluate my llm re
sponses. I'm super new to this and don't know how to approach it. I am going through RAGAS documentation and understood 
that they provide metrics and langsmith has a good UI to visualize the metrics. So How can I implement it? If my chatbot
 is in production, how can I automate this evaluation? And if you have already implemented such thing, please please hel
p me out. Thanks !
```
---

     
 
all -  [ How to get started with building an on premises generative AI platform? ](https://www.reddit.com/r/mlops/comments/1fe5i82/how_to_get_started_with_building_an_on_premises/) , 2024-09-12-0912
```
Hi everyone, 

I recently got a job at a small company that wants to deploy an RAG application on premises for its clien
ts. This company hasn't really done any AI use cases before, although does have some data analytics products in their do
main. The hiring manager wants me to develop their application as a RnD project from the ground up. That means choosing 
an open-source LLM and deploying it on-premise and open-source orchestrators like langchain along with other components 
of a gen AI platform along with the hardware specs needed to run such a platform on-premises. 

I have some experience w
ith LLMs in a hobby project in the Azure cloud and langchain along with a previous job in traditional ML where the infra
structure and server were already set up. But I have never done something of this scale where I had to design the system
 and also choose the infrastructure and hardware requirements along with LLMOps down the line.  

Can someone please gui
de me in going about how to get something of this scale setup? What factors should I consider and if any resources can h
elp in the usecase? 


```
---

     
 
all -  [ Resume review from Analytics Engineer to Data Engineering?  ](https://i.redd.it/qg5f5zb043od1.png) , 2024-09-12-0912
```
Would appreciate everyone's feedback!
```
---

     
 
all -  [ PromptTemplate coupled to LLM parsing output ](https://www.reddit.com/r/LangChain/comments/1fdxh8o/prompttemplate_coupled_to_llm_parsing_output/) , 2024-09-12-0912
```
Hi,

I'm new to this AI world so consider I might be missing some context or not fully understanding something as of yet
.  
Having said that, I was developing an application which generates specific content as I request it to do so. For thi
s project I'm using langchain as a framework and gemini as the LLM. I'm also using RAG technique to retrieve relevant da
ta and use my own custom context.  
I have a simple [main.py](http://main.py) which has 2 messages, one for invoking and
 the other one for building the classic pipe or rag chain as I understand this flow is called.  
That pipeline looks som
ething like this:

`pipeline = (`  
`{'context': my_context,`  
`'query': RunnablePassthrough()}`  
`| prompt`  
`| llm`
  
`| StrOutputParser()`  
`)`

So my doubt came when I needed to change the parsing of the output the LLM was returning
 me. I needed to structure the data in a JSON with some specific types and I've realized that I needed to add that chang
e to the *Prompt.*  
To me this didn't make sense at all since I understood the last call of the pipeline, in this case 
a simple string, was the way to parse the output. To my surprise I've encountered that I needed to add format instructio
ns within the prompt.  
On the prompting side I have something like this:

    parser = JsonOutputParser(pydantic_object
=MyObjectTemplate)
    
    return PromptTemplate(
        template=MY_PROMPT_TEMPLATE,
        input_variables=['query'
],
        partial_variables={'format_instructions': parser.get_format_instructions()},
    )

What I don't understand a
t all is why the line JsonOutputParser(pydantic\_object=MyObjectTemplate) cannot or else why it shouldn't go within the 
last step of the pipeline. I've tried to do so but partial\_variables parameter is required to create the PromptTemplate
 object.  
It's unclear to me so far why If I only want to change the way the LLM responds, I need to change the Prompt.


Can somebody help me understand how to accomplish a refactor to decoupled these two things or enlighten me if there's 
something I'm understanding incorrectly?

Thanks in advance.
```
---

     
 
all -  [ Looking for team to start my hackathon journey. ](https://www.reddit.com/r/hackathons/comments/1fdx9vj/looking_for_team_to_start_my_hackathon_journey/) , 2024-09-12-0912
```
Hey everyone! I want to start my journey in hackathons. I want to create my own team or joining a team. I want to learn 
something new and participant in competitions. If anyone here please respond.
My skills are
Python
Telegram api
Langchai
n
Django(Basics)
React(Basics)
Thanks for approaching....;)
```
---

     
 
all -  [ How to embed and retrieve images in RAG ](https://www.reddit.com/r/SmythOS_/comments/1fdwkar/how_to_embed_and_retrieve_images_in_rag/) , 2024-09-12-0912
```
I'm working on a RAG project involving numerous PDFs and documents.

The documents frequently include screenshots that v
isually illustrate the surrounding text. Given the abundance of these screenshots and their high level of detail, I'm co
ncerned that using a multimodal model to describe the images might be both costly and potentially inaccurate.

As an alt
ernative, I'm considering using image embedding techniques with some form of positional referencing or indexing. I'm int
erested in finding valuable examples or resources that implement this approach, particularly using Langchain or other si
milar frameworks.

Additionally, I'm curious if certain vector databases are better suited for this specific use case. A
ny insights or recommendations would be greatly appreciated.
```
---

     
 
all -  [ Dynamic crawling using LLMs ](https://www.reddit.com/r/LangChain/comments/1fdtgdv/dynamic_crawling_using_llms/) , 2024-09-12-0912
```
I use crawling quite a bit for different parts of my job and have used platforms like scraperapi as well as apis from sc
rapy and others. In recent times i tried firecrawl as well [r.jina.ai](http://r.jina.ai) as well - for crawling. However
, they were all less than perfect. So I defined my own way of crawling and figured this can be quite straight forward..


Basically you can provide a json for what you'd like to have and then ask openai or claude with a url to convert it to 
the provided json - this will convert any website into a json format. 

Now instead of doing it again and again with llm
, you can ask llm to write a code that produces the json output you are expecting given the website.. and you get a code
 that works perfectly and if there are errors you can ask llm to correct it. 

It works quite well for me .. I put up th
e code here [https://github.com/alinaqi/dynamic\_crawler](https://github.com/alinaqi/dynamic_crawler) for anyone who may
 find it interesting.. 

Happy to hear from others on what they think about the approach. 
```
---

     
 
all -  [ Need Suggestions for AI beginners courses? ](https://www.reddit.com/r/PakistaniTech/comments/1fdosl4/need_suggestions_for_ai_beginners_courses/) , 2024-09-12-0912
```
I am a complete beginner in field of AI with zero prior experience although not new in the field of IT(I work on flutter
). AI has always been a keen of interest of me i want to learn about it but dont know where to start as a beginner and w
hat to learn like i go on YouTube and simply type AI and get Langchain, Generative AI , ML,NLP  and etc but dont know wh
at to start please guide me..
Thanks
```
---

     
 
all -  [ Sharing R2R - an open source RAG engine that just works ](https://www.reddit.com/r/Rag/comments/1fdknbm/sharing_r2r_an_open_source_rag_engine_that_just/) , 2024-09-12-0912
```
Hey All,

  
Today I am sharing with you R2R, a project that I have been working on for the last year. R2R is an open so
urce RAG engine that changes your focus as a developer from building RAG pipelines to configuring them. The north star f
or this project is to become the Elasticsearch for RAG.

  
R2R comes with the following features:

* [**📁 Multimodal In
gestion**](https://r2r-docs.sciphi.ai/documentation/configuration/ingestion/overview): Parse `.txt`, `.pdf`, `.json`, `.
png`, `.mp3`, and more.
* [**🔍 Hybrid Search**](https://r2r-docs.sciphi.ai/cookbooks/hybrid-search): Combine semantic an
d keyword search with reciprocal rank fusion for enhanced relevancy.
* [**🔗 Graph RAG**](https://r2r-docs.sciphi.ai/cook
books/graphrag): Automatically extract relationships and build knowledge graphs.
* [**🗂️ App Management**](https://r2r-d
ocs.sciphi.ai/cookbooks/user-auth): Efficiently manage documents and users with full authentication.
* [**🔭 Observabilit
y**](https://r2r-docs.sciphi.ai/cookbooks/observability): Observe and analyze your RAG engine performance.
* [**🧩 Config
urable**](https://r2r-docs.sciphi.ai/documentation/configuration/introduction): Provision your application using intuiti
ve configuration files.
* [**🖥️ Dashboard**](https://github.com/SciPhi-AI/R2R-Dashboard): An open-source React+Next.js a
pp with optional authentication, to interact with R2R via GUI.

# 

We've worked really hard to make the documentation r
obust and as developer friendly as possible. The feedback we are getting from other developers that are switching from a
lternative approaches like LangChain has been very positive.

  
I just wanted to share our work with you all here as I 
am confident that this can accelerate many of your RAG buildouts. We are very responsive and aggressive in implementing 
new features and I would love to hear your likes and dislikes about the system today.

  
Thanks!



 
```
---

     
 
all -  [ An Extensive Open-Source Collection of AI Agent Implementations with Multiple Use Cases and Levels ](https://github.com/NirDiamant/GenAI_Agents) , 2024-09-12-0912
```
Hi all,

In addition to the RAG Techniques repo (6K stars in a month), I'm excited to share a new repo I've been working
 on for a while—AI Agents!

It’s open-source and includes 14 different implementations of AI Agents, along with tutorial
s and visualizations.

This is a great resource for both learning and reference. Feel free to explore, learn, open issue
s, contribute your own agents, and use it as needed. And of course, join our AI Knowledge Hub Discord community to stay 
connected!
Enjoy!
```
---

     
 
all -  [ Best LLM gateway? ](https://www.reddit.com/r/LLMDevs/comments/1fdii62/best_llm_gateway/) , 2024-09-12-0912
```
I'm currently exploring options how to best give access to a variety of models across various vendors (eg OpenAI, Anthro
pic etc.) to our employees…it's for internal playgrounds, POCs and demos only. No production ready applications should r
un through this. We are in the service business, all our clients have their own models in their VPC, we do not supply th
eir infra.

I came across the concept of LLM gateways that to my understanding give you the ability to control access th
rough proxies and/or synthetic keys.

So far, I came across the following list:

LiteLLM -> Seems legit, I like the Lang
Chain integration  
OpenRouter -> Not sure if it's the right fit tbh  
Kong AI Gateway -> Seems overkill for our interna
l usage  
PortKey AI Gateway -> Seems a bit more advanced than LiteLLM

I'm currently tending for LiteLLM…but wanted to 
check if anyone here as experience/recommendations?
```
---

     
 
all -  [ PremSQL: Our Open-Source Journey Towards Secure, Local Text-to-SQL Solutions 🚀 ](https://www.reddit.com/r/LocalLLaMA/comments/1fdibn6/premsql_our_opensource_journey_towards_secure/) , 2024-09-12-0912
```
Hey folks! We're super excited to share our first release of PremSQL, an open-source library that helps developers creat
e secure, local text-to-SQL solutions with small language models. We’ve been working hard to make building and deploying
 these pipelines way less cumbersome, focusing on customizable components that make sense for secure, AI-driven data ana
lysis.

We’re also introducing Prem-1B-SQL, a 1B parameter model fine-tuned from DeepSeek Coder 1B, specifically for Tex
t-to-SQL tasks. It's designed to be lightweight and easy to fine-tune your data, so you’re not stuck relying on closed L
LMs with all the compliance headaches. We’ll be sharing public benchmarks soon, but early results are looking really sol
id.

Some features we’re stoked about:

* **PremSQL Datasets**: Pre-processed, hosted on HuggingFace—perfect for evaluat
ion and fine-tuning.
* **Generators & Executors:** Go from input to SQL to execution effortlessly.
* **Evaluators: Metri
cs** like execution accuracy and Valid Efficiency Score (VES) to keep things on track.
* **Error Handling Datasets**: Th
ese are used to build more resilient models that handle errors gracefully.
* **Tuner:** Fine-tune your models with custo
m evaluation—control the whole training flow!

I would love to hear what the community thinks, and if you find it useful
, a ⭐️ would mean the world. Dive in, explore, and let’s build cool stuff together!

Let’s keep pushing the boundaries o
f what we can do with open source! 🛠️❤️

  
**GitHub repo:** [**https://github.com/premAI-io/premsql**](https://github.c
om/premAI-io/premsql)

[PremSQL architecture](https://preview.redd.it/sdydyq14lznd1.png?width=3158&format=png&auto=webp&
s=abb6839cb4885f3eea146de204a4b228e51fa162)

  

```
---

     
 
all -  [ Hacking a Text-to-SQL Chatbot and Leaking Sensitive Data ](https://www.youtube.com/watch?v=RTFRmZXUdig) , 2024-09-12-0912
```
Just short video to demonstrate a data leakage attack from a Text-to-SQL chatbot 😈   

The goal is to leak the revenue o
f an e-commerce store through its customer-facing AI chatbot.

https://www.youtube.com/watch?v=RTFRmZXUdig
```
---

     
 
all -  [ DSPy- Stop prompting, Start building AI pipelines ](https://www.reddit.com/r/LangChain/comments/1fdgsv4/dspy_stop_prompting_start_building_ai_pipelines/) , 2024-09-12-0912
```
Hey folks,

I read an interesting blog post about DSPy the other day. It's a framework that changes how we work with AI,
 and I thought some of you might find it useful.

The main idea is pretty cool: instead of spending hours tweaking promp
ts, you focus on building the overall flow of your AI program. You set up some metrics to measure what good output looks
 like, and DSPy handles the rest.

A few things stood out to me:

1. It works with different AI models, so you're not lo
cked into one.
2. It breaks big tasks into smaller pieces.
3. It optimizes stuff automatically.

The post talks about ho
w a company called Zoro UK is using DSPy to handle product data from hundreds of suppliers. Sounds like it's helping the
m deal with messy, real-world data.

There's also some talk about how DSPy might help cut costs when you're running AI a
t a large scale.

If you're building AI apps, especially for production, it might be worth a look.

Here's the link if y
ou want to check it out: [https://portkey.wiki/dspy-blog](https://portkey.wiki/dspy-blog)
```
---

     
 
all -  [ Some Advice on my Project ](https://www.reddit.com/r/LangChain/comments/1fdfsm4/some_advice_on_my_project/) , 2024-09-12-0912
```
Hey everyone, I have been developing an example Customer Chatbot (Shopping Assistant) project for an e-commerce website 
to add my portfolio and I want to add some features to the Chatbot such as searching products based on technical specifi
cations or buying via Chatbot etc. At this point I want your ideas/advice for the project. Do you have any idea that can
 be good features to add the Chatbot. It would great to hear your opinion.
```
---

     
 
all -  [ Udemy Free Courses for 10 September 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1fdezf5/udemy_free_courses_for_10_september_2024/) , 2024-09-12-0912
```
# Udemy Free Courses for 10 September 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get th
e courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14628/)Build Hotel Management Billing System wi
th Python3
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14626/)Beginners Guide to Master Computer Programming Bas
ic Concept
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14627/)Ultimate Java Bootcamp | Build Java GUI and JavaFX
 Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14625/)Cryptocurrency Trading And Secrets | The Beginners 
Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14624/)Overcome Cryptocurrency Scams | Learn Bitcoin Profit
 Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14621/)Podcast For Business | How To Grow A Business With P
odcast
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14622/)Complete Oracle JavaFX Bootcamp | Build Real JavaFX Pr
ojects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14618/)Overcome Phone Addiction And Start Social Media Market
ing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14620/)Master Your Mind | Master The Power Of Subconscious Mind

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14619/)Starting A Freelance Business | The Beginners Guide
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/14623/)Build E-Learning Application with Voice Over Using Python 3
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14002/)Playwright Automation Testing Complete Bootcamp UI API\[2024\]
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/11773/)React JS Bootcamp 2024: Build 1 Projects and Get Job-Ready
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14109/)Flutter Web Development Bootcamp:Build 2 Real-World Web Apps
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13617/)Complete C, C , C#, Java and Python Bootcamp FREE Book
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14610/)Instagram Ads Success! How To Run Successful Instagram Ads
* The Complete Gui
de To Breaking Bad Habits! (Mp3 Attached)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/14616/)
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/14617/)Modern Vlogging Guide | How to Become a Successful Vlogger
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/14611/)How To Become A Successful Social Media Influencer
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14614/)Zoom For Business | How To Grow Your Business With Zoom
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/14615/)Artificial Intelligence In Digital Marketing For Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/14612/)Bitcoin Breakthrough Secrets | Complete Cryptocurrency Guide
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/14613/)5 Customized GPT Tools for Startup Success In 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/9373/)Midjourney for Beginners: Embark on Your Artistic Journey
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
6884/)Mastering DALL·E Artistry: AI’s Creative Revolution
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10517/)Air
table for Project Management: From Setup to Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7837/)The Leader
ship Blueprint: Navigate Change and Inspire Teams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12747/)The Future 
is Now: Master Generative AI for Leader (2024)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8556/)HTML5 & CSS3 Co
mplete Course: Build Websites like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9392/)Next-Gen Web Developm
ent: JavaScript & AI Essentials
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13456/)Python & GenAI for Advanced A
nalytics: Build Powerful Models
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6857/)AutoCAD 2023 MasterClass: Prod
uce Amazing Site Plans Quickly
* Mastering OpenCV: A Practical Guide to Computer Vision
* [REDEEM OFFER](https://idownlo
adcoupon.com/udemy/10679/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14603/)ChatGPT Essentials – Master The Ba
sics Of AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14602/)The Ultimate Python Guide for Beginners
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14605/)AZ-700:Designing and Implementing Azure Networking Solutions
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14604/)Certified Ethical Hacker v12 Latest Practice Questions
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14608/)Certified in Cybersecurity (CC) Practice Questions 2024
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/14607/)Fundamentals of Artificial Intelligence Practice Exam 2024
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/14606/)PCAP Certified Associate Python Programmer Practice Exam
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/14609/)Basic to Advanced T-shirt Design with Adobe Photoshop CC
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/12383/)Python Web Development: Building Interactive Websites
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12743/)Master React.js with AI: From Basics to Advanced Development
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/9369/)TypeScript for Beginners: Mastering TypeScript Fundamentals
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/12384/)Learn Python JavaScript Microsoft SQL for Data science
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/13896/)Complete Network Hacking Course 2024 – Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/9416/)ChatGPT Coding Express: Fast-Track Coding with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13
770/)Zero to Hero in LangChain: Build GenAI apps using LangChain
* The Complete Vue.JS Course for Beginners: Zero to Mas
tery
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11064/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1089
6/)IELTS Band 8: IELTS Listening Mastery | IELTS Tenses
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7330/)Engine
ering Drawing / Graphics : Hands-on Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11073/)Angular 16 & RxJ
S: Build Modern Single Page Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14601/)Productividad y Mane
jo del Tiempo
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2539/)Comprehensive CISSP Practice Tests: Ace Your Exa
m confidence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10227/)Investigação em Estratégia e Desenvolvimento de 
Produtos
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5328/)CISSP Cheat Sheet Challenge: Expertly Crafted Practic
e Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6394/)Certificate in Public Relations and Communication Mana
gement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13461/)Master in Generative AI (Artificial Intelligence)
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/1022/)300-730 SVPN: Implementing with Virtual Private Networks pro
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/12580/)Google My Business SEO with AI: Google Maps Course 2024
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13966/)Mastering Power BI: Your Ultimate PL-300 Practice Tests 2024
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/8553/)Master in Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/5048/)Microsoft DP-500 : Azure Enterprise Data Analyst Associate
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/13279/)PMI-ACP Exam Prep – Practice Tests
* Linux Mastery: CLI & Kali Commands Practice Tests pro
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/9096/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8809/)Profession
al Certificate in Career Coaching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11230/)Professional Diploma of Mor
tgage and Lending Broker
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12006/)Professional Certificate in Coaching

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7268/)Kubernetes and Cloud Native Associate (KCNA) (EXAM Prep)2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12914/)Meditation Masterclass: meditation teacher certification
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/14597/)Tajweed Made Easy: Simple Rules for Quran Recitation
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/14598/)Master in Digital Transformation Strategy
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14600/)Python Development and Python Programming Fundamentals
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/9702/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/3221/)Mastering Microsoft Excel A Comprehensive Guide to Boost You
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/364
2/)CSS, JavaScript,PHP And Python Programming All in One Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1445
4/)ISO 9001:2015 Quality Management System (QMS)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10656/)Microsoft Of
fice Training : Master Excel, PowerPoint & Word
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6392/)Executive Cert
ificate in Company Direction
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9109/)Simple React App from Scratch
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/12702/)Professional Certificate: Product Management and Development
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/11142/)Build a User Web App from Scratch with Vanilla PHP 8+
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10737/)Master in Software Architecture, Engineering and Development
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/8988/)PHP with MySQL: Build a Complete Job Portal
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14596/)Professional Certificate in Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14
594/)Teaching For Joy and Justice
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14593/)Teaching With AI: A practic
al guide to a new era of teaching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14592/)SUPPLY CHAIN OPTIMIZATION:W
AREHOUSE MANAGEMENT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14590/)Complete CorelDRAW 2021 Graphic Design | 
Beginners Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14589/)Become SAP Ariba Certified Consultant Spen
d Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14591/)Professional Certificate in Customer Experience Ma
nagement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13932/)Understanding Foundational Literacy and Numeracy (FL
N)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12160/)JavaScript Fundamentals Course for Beginners
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/5644/)Introduction à la Gestion des Ressources Humaines
* A winning marketing str
ategy with a little help of AI models
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11947/)
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/6379/)Mastering School Marketing: Strategies for Success
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/8950/)Live Accounting App by C# .NET Core in Windows Forms and SQL
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/7003/)NumPy, SciPy, Matplotlib & Pandas A-Z: Machine Learning
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/10655/)Canva Rockstar: Design Like a Pro for Social Media Success
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13945/)The Complete Microsoft Excel Data Analysis Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
8898/)Professional Certificate in SMM Social Media Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10460/)
PHP Master Class – The Complete PHP Developer Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14587/)Certifie
d Information Privacy Professional (CIPP/US) Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14585/)Understandi
ng Behavioral Addictions among school children
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14586/)Mastering Digi
tal Wellness
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14583/)Master in Product Design
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/14584/)Business Ideas Generation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7827/)
Microsoft Excel Training – Beginner to Expert Level in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6007/)U
ltimate Guide to Interview Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10236/)Learn JavaScript by Creatin
g 10 Practical Projects
* Public Speaking and Presentation Skills Masterclass
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/11554/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Customer Value / Sel
ling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8886/)Diploma Executivo em Liderança
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/10727/)Master in Product and Brand Management- FMCG, FMCD etc.
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/10454/)JavaScript Fundamentals for Absolute Beginners
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (People & Social Skills)
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/11847/)Excel Formulas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10836/)Kotlin Mastering: Complete Kotlin
 Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14581/)Linux Shell Scripting: A Project-Base
d Approach to Learning
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14579/)Amazon Q Developer for Java
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14578/)Learn Linux Administration and Supercharge Your Career
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14576/)AWS Certified Data Engineer Associate 2024 – Hands On!
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/12989/)SQL Mastery: Beginner’s Guide to MySQL Essentials
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/11034/)Azure Networking services for beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/63
97/)\[NEW\] Ultimate AWS Certified Cloud Practitioner CLF-C02

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HE
RE](https://www.reddit.com/r/udemyfreeebies/hot/)
```
---

     
 
all -  [ Udemy Free Courses for 10 September 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1fdezao/udemy_free_courses_for_10_september_2024/) , 2024-09-12-0912
```
# Udemy Free Courses for 10 September 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get th
e courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14628/)Build Hotel Management Billing System wi
th Python3
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14626/)Beginners Guide to Master Computer Programming Bas
ic Concept
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14627/)Ultimate Java Bootcamp | Build Java GUI and JavaFX
 Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14625/)Cryptocurrency Trading And Secrets | The Beginners 
Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14624/)Overcome Cryptocurrency Scams | Learn Bitcoin Profit
 Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14621/)Podcast For Business | How To Grow A Business With P
odcast
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14622/)Complete Oracle JavaFX Bootcamp | Build Real JavaFX Pr
ojects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14618/)Overcome Phone Addiction And Start Social Media Market
ing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14620/)Master Your Mind | Master The Power Of Subconscious Mind

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14619/)Starting A Freelance Business | The Beginners Guide
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/14623/)Build E-Learning Application with Voice Over Using Python 3
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14002/)Playwright Automation Testing Complete Bootcamp UI API\[2024\]
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/11773/)React JS Bootcamp 2024: Build 1 Projects and Get Job-Ready
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14109/)Flutter Web Development Bootcamp:Build 2 Real-World Web Apps
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13617/)Complete C, C , C#, Java and Python Bootcamp FREE Book
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14610/)Instagram Ads Success! How To Run Successful Instagram Ads
* The Complete Gui
de To Breaking Bad Habits! (Mp3 Attached)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/14616/)
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/14617/)Modern Vlogging Guide | How to Become a Successful Vlogger
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/14611/)How To Become A Successful Social Media Influencer
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14614/)Zoom For Business | How To Grow Your Business With Zoom
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/14615/)Artificial Intelligence In Digital Marketing For Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/14612/)Bitcoin Breakthrough Secrets | Complete Cryptocurrency Guide
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/14613/)5 Customized GPT Tools for Startup Success In 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/9373/)Midjourney for Beginners: Embark on Your Artistic Journey
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
6884/)Mastering DALL·E Artistry: AI’s Creative Revolution
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10517/)Air
table for Project Management: From Setup to Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7837/)The Leader
ship Blueprint: Navigate Change and Inspire Teams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12747/)The Future 
is Now: Master Generative AI for Leader (2024)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8556/)HTML5 & CSS3 Co
mplete Course: Build Websites like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9392/)Next-Gen Web Developm
ent: JavaScript & AI Essentials
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13456/)Python & GenAI for Advanced A
nalytics: Build Powerful Models
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6857/)AutoCAD 2023 MasterClass: Prod
uce Amazing Site Plans Quickly
* Mastering OpenCV: A Practical Guide to Computer Vision
* [REDEEM OFFER](https://idownlo
adcoupon.com/udemy/10679/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14603/)ChatGPT Essentials – Master The Ba
sics Of AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14602/)The Ultimate Python Guide for Beginners
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14605/)AZ-700:Designing and Implementing Azure Networking Solutions
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14604/)Certified Ethical Hacker v12 Latest Practice Questions
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14608/)Certified in Cybersecurity (CC) Practice Questions 2024
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/14607/)Fundamentals of Artificial Intelligence Practice Exam 2024
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/14606/)PCAP Certified Associate Python Programmer Practice Exam
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/14609/)Basic to Advanced T-shirt Design with Adobe Photoshop CC
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/12383/)Python Web Development: Building Interactive Websites
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12743/)Master React.js with AI: From Basics to Advanced Development
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/9369/)TypeScript for Beginners: Mastering TypeScript Fundamentals
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/12384/)Learn Python JavaScript Microsoft SQL for Data science
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/13896/)Complete Network Hacking Course 2024 – Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/9416/)ChatGPT Coding Express: Fast-Track Coding with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13
770/)Zero to Hero in LangChain: Build GenAI apps using LangChain
* The Complete Vue.JS Course for Beginners: Zero to Mas
tery
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11064/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1089
6/)IELTS Band 8: IELTS Listening Mastery | IELTS Tenses
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7330/)Engine
ering Drawing / Graphics : Hands-on Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11073/)Angular 16 & RxJ
S: Build Modern Single Page Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14601/)Productividad y Mane
jo del Tiempo
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2539/)Comprehensive CISSP Practice Tests: Ace Your Exa
m confidence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10227/)Investigação em Estratégia e Desenvolvimento de 
Produtos
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5328/)CISSP Cheat Sheet Challenge: Expertly Crafted Practic
e Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6394/)Certificate in Public Relations and Communication Mana
gement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13461/)Master in Generative AI (Artificial Intelligence)
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/1022/)300-730 SVPN: Implementing with Virtual Private Networks pro
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/12580/)Google My Business SEO with AI: Google Maps Course 2024
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13966/)Mastering Power BI: Your Ultimate PL-300 Practice Tests 2024
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/8553/)Master in Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/5048/)Microsoft DP-500 : Azure Enterprise Data Analyst Associate
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/13279/)PMI-ACP Exam Prep – Practice Tests
* Linux Mastery: CLI & Kali Commands Practice Tests pro
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/9096/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8809/)Profession
al Certificate in Career Coaching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11230/)Professional Diploma of Mor
tgage and Lending Broker
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12006/)Professional Certificate in Coaching

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7268/)Kubernetes and Cloud Native Associate (KCNA) (EXAM Prep)2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12914/)Meditation Masterclass: meditation teacher certification
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/14597/)Tajweed Made Easy: Simple Rules for Quran Recitation
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/14598/)Master in Digital Transformation Strategy
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14600/)Python Development and Python Programming Fundamentals
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/9702/)HTML 5 With Quizzes And Python 3 Complete Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/3221/)Mastering Microsoft Excel A Comprehensive Guide to Boost You
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/364
2/)CSS, JavaScript,PHP And Python Programming All in One Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1445
4/)ISO 9001:2015 Quality Management System (QMS)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10656/)Microsoft Of
fice Training : Master Excel, PowerPoint & Word
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6392/)Executive Cert
ificate in Company Direction
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9109/)Simple React App from Scratch
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/12702/)Professional Certificate: Product Management and Development
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/11142/)Build a User Web App from Scratch with Vanilla PHP 8+
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10737/)Master in Software Architecture, Engineering and Development
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/8988/)PHP with MySQL: Build a Complete Job Portal
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/14596/)Professional Certificate in Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14
594/)Teaching For Joy and Justice
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14593/)Teaching With AI: A practic
al guide to a new era of teaching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14592/)SUPPLY CHAIN OPTIMIZATION:W
AREHOUSE MANAGEMENT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14590/)Complete CorelDRAW 2021 Graphic Design | 
Beginners Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14589/)Become SAP Ariba Certified Consultant Spen
d Analysis
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14591/)Professional Certificate in Customer Experience Ma
nagement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13932/)Understanding Foundational Literacy and Numeracy (FL
N)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12160/)JavaScript Fundamentals Course for Beginners
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/5644/)Introduction à la Gestion des Ressources Humaines
* A winning marketing str
ategy with a little help of AI models
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11947/)
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/6379/)Mastering School Marketing: Strategies for Success
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/8950/)Live Accounting App by C# .NET Core in Windows Forms and SQL
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/7003/)NumPy, SciPy, Matplotlib & Pandas A-Z: Machine Learning
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/10655/)Canva Rockstar: Design Like a Pro for Social Media Success
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13945/)The Complete Microsoft Excel Data Analysis Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
8898/)Professional Certificate in SMM Social Media Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10460/)
PHP Master Class – The Complete PHP Developer Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14587/)Certifie
d Information Privacy Professional (CIPP/US) Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14585/)Understandi
ng Behavioral Addictions among school children
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14586/)Mastering Digi
tal Wellness
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14583/)Master in Product Design
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/14584/)Business Ideas Generation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7827/)
Microsoft Excel Training – Beginner to Expert Level in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6007/)U
ltimate Guide to Interview Skills
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10236/)Learn JavaScript by Creatin
g 10 Practical Projects
* Public Speaking and Presentation Skills Masterclass
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/11554/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Customer Value / Sel
ling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8886/)Diploma Executivo em Liderança
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/10727/)Master in Product and Brand Management- FMCG, FMCD etc.
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/10454/)JavaScript Fundamentals for Absolute Beginners
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (People & Social Skills)
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/11847/)Excel Formulas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10836/)Kotlin Mastering: Complete Kotlin
 Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14581/)Linux Shell Scripting: A Project-Base
d Approach to Learning
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14579/)Amazon Q Developer for Java
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14578/)Learn Linux Administration and Supercharge Your Career
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/14576/)AWS Certified Data Engineer Associate 2024 – Hands On!
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/12989/)SQL Mastery: Beginner’s Guide to MySQL Essentials
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/11034/)Azure Networking services for beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/63
97/)\[NEW\] Ultimate AWS Certified Cloud Practitioner CLF-C02

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HE
RE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Does anyone use Langchain in production? ](https://www.reddit.com/r/LLMDevs/comments/1fddj4l/does_anyone_use_langchain_in_production/) , 2024-09-12-0912
```
I am trying to write a production code using langchain framework which includes lot of summarisations from folders. 

pl
ease suggest if you know any optimised approach to parse large folders and feed to llms.

Thanks!
```
---

     
 
all -  [ Build a RAG based Chatbot for a workplace ](https://www.reddit.com/r/LangChain/comments/1fd9hbg/build_a_rag_based_chatbot_for_a_workplace/) , 2024-09-12-0912
```
 I am currently working as a research engineer in our department.

As a graduate, my research major was in spatial datab
ase computing and query optimizations in the department of AI.

My ex-boss hired me due to the face that I was from AI d
epartment, and he wanted to do some AI based project. Short-story: He quit the office.

So the temporary boss is asking 
me to come up with a new AI based project as we are almost completing a management system. 

Hence, there's no new proje
ct in our company. Me being the only employee who has basic 

idea on Machine learning and some experience using RAG age
nts. I plan to propose a chat-bot

application as a next research project using the workplace data.

However, I have no 
idea about how to develop a chat-model from the scratch. 

I just have a high-level idea of what I plan to do, which mig
ht be planning totally wrong.

I have no idea what devices, computing power, should I use that could run opensource LLM 


models with good performance. How I can scale it so that many users 'employee' could use it

at a same time. How do I 
fine-tune the model using the custom dataset.

How should I get the custom dataset? From where I should extract and how 
should I extract, what format should it be in?

These things are really overwhelming to me. Thus I want to get the sugge
stions and information from this community.

I hope to get good response.
```
---

     
 
all -  [ Comparing approaches of using LLMs for Structured Data Extraction from Unstructured PDFs using Langc ](https://www.reddit.com/r/LangChain/comments/1fcubyi/comparing_approaches_of_using_llms_for_structured/) , 2024-09-12-0912
```
[https://unstract.com/blog/comparing-approaches-for-using-llms-for-structured-data-extraction-from-pdfs/](https://unstra
ct.com/blog/comparing-approaches-for-using-llms-for-structured-data-extraction-from-pdfs/)

**We’ll show two approaches 
in this article:**

* In the first one, we’ll employ [Langchain](https://www.langchain.com/), the popular Python-based L
LM framework in combination with the Pydantic library to use an LLM to create structured output.
* In the second approac
h, we’ll use [an open-source platform, Unstract,](https://github.com/Zipstack/unstract) which is purpose-built for struc
tured document data extraction. Unstract features Prompt Studio, a prompt engineering environment specialized for what w
e’re trying to achieve—document data extraction with LLMs.

Later in the article, once we look in detail into our two ap
proaches of using a regular IDE to do prompt engineering vs. using a specialized environment to do the same, we’ll look 
at these challenges in light of each of those approaches to evaluate how we fared in either case.
```
---

     
 
all -  [ LLMs or ChatModels for Agents? ](https://www.reddit.com/r/LangChain/comments/1fcte0i/llms_or_chatmodels_for_agents/) , 2024-09-12-0912
```
Hi guys, silly question. What do you use for your langgraph agents? LLMs or ChatModels?  
What is the pro and cons of ea
ch?

Thanks
```
---

     
 
all -  [ Proper image recognition for RAG application ](https://www.reddit.com/r/LangChain/comments/1fcsqm5/proper_image_recognition_for_rag_application/) , 2024-09-12-0912
```
I've been trying to make my RAG app accept images as input. I know how to code the features but can't come up with the w
ay to do it (I don't know how to explain it). So here is what I'm trying to do:

I'm trying to create a RAG app that can
 generate answers based on the context and also able to generate answers based on both the context and the image, if pro
vided. Lets say if a user provides the image of a lion and my RAG app is about biology it should be able to retrieve the
 image, answer the user's question using the context.

My first idea was to pass in the image URL into the response prom
pt (just like context) which is then replaced as a description using a Multi Model and ask the question based on that. T
hen I soon discovered a problem, when I ask a follow up question to the previously provided image it would have no idea 
about what I'm talking about because the description is no longer being provided in the response template  prompt.   
  

Another potential issue is that if I ask a question about the image that is not provided by the Multi Model, it would n
ot be able to respond appropriately nor would it be able to regenerate the description of the image.  
  
Please forgive
 me if there are any mistakes in my English, it is not my first language and I hope you can understand what I've written
.  
```
---

     
 
all -  [ Step-by-Step Guide to Build an AI-Powered Reddit Manager That Curates Relevant Content for Daily Pos ](https://www.reddit.com/r/LangChain/comments/1fcrfy7/stepbystep_guide_to_build_an_aipowered_reddit/) , 2024-09-12-0912
```
[https://medium.com/@harshit\_56733/step-by-step-guide-to-build-an-ai-powered-reddit-manager-that-curates-relevant-conte
nt-for-daily-2434cd965509](https://medium.com/@harshit_56733/step-by-step-guide-to-build-an-ai-powered-reddit-manager-th
at-curates-relevant-content-for-daily-2434cd965509)
```
---

     
 
all -  [ Need Help Setting Up a Chatbot with LangChain: SelfRAG, GraphRAG, and LangGraph ](https://www.reddit.com/r/LLMDevs/comments/1fcr4a0/need_help_setting_up_a_chatbot_with_langchain/) , 2024-09-12-0912
```
Hey everyone,

I'm working on building a chatbot using LangChain and could really use some help with configuring a few s
pecific components. My goal is to enhance the chatbot's ability to retrieve relevant information and answer complex ques
tions more effectively. Here's what I'm trying to set up:

1. \*\*SelfRAG:\*\* To improve the system's autonomy in retri
eving relevant information and generating responses.
2. \*\*GraphRAG:\*\* To integrate retrieval with knowledge graphs, 
enhancing the ability to answer complex questions.
3. \*\*LangGraph:\*\* To create and manage knowledge graphs that repr
esent relationships between concepts in the loaded documents.

I'm relatively new to these components, and any guidance 
on how to set them up or best practices for using them would be greatly appreciated. Whether it's documentation, tutoria
ls, code examples, or just some tips from your experience, I'd love to hear from you!

Thanks in advance for your help
```
---

     
 
all -  [ Need Help Setting Up a Chatbot with LangChain: SelfRAG, GraphRAG, and LangGraph ](https://www.reddit.com/r/Rag/comments/1fcr3qz/need_help_setting_up_a_chatbot_with_langchain/) , 2024-09-12-0912
```
Hey everyone,

I'm working on building a chatbot using LangChain and could really use some help with configuring a few s
pecific components. My goal is to enhance the chatbot's ability to retrieve relevant information and answer complex ques
tions more effectively. Here's what I'm trying to set up:

1. \*\*SelfRAG:\*\* To improve the system's autonomy in retri
eving relevant information and generating responses.
2. \*\*GraphRAG:\*\* To integrate retrieval with knowledge graphs, 
enhancing the ability to answer complex questions.
3. \*\*LangGraph:\*\* To create and manage knowledge graphs that repr
esent relationships between concepts in the loaded documents.

I'm relatively new to these components, and any guidance 
on how to set them up or best practices for using them would be greatly appreciated. Whether it's documentation, tutoria
ls, code examples, or just some tips from your experience, I'd love to hear from you!

Thanks in advance for your help!
```
---

     
 
all -  [ Hiring on a Langgraph based company ](https://www.reddit.com/r/LangChain/comments/1fcpmbp/hiring_on_a_langgraph_based_company/) , 2024-09-12-0912
```
Hey guys,

We’re a team of 2 based in Station F in Paris, and we’ve been working on our startup for the past 6 months.


We build a bunch of agents with Langgraph to automate manual tasks on a specific issue related to HR. We are an AI-first
 company, and work with best in class stack (Next.js / Langchain / Langgraph / PostgreSQL / [Temporal.io](http://Tempora
l.io))

We’ll start a funding process soon, and we’re looking to meet rockstars who want to work on cutting edge tech. W
e have so many interesting challenges ahead and a very ambitious roadmap, but our 4 arms are not enough.

Feel free to d
m me if you are in Europe ! 🙂

Louis
```
---

     
 
all -  [ Agentic Discovery & Exploration ](https://www.reddit.com/r/LangChain/comments/1fcnuur/agentic_discovery_exploration/) , 2024-09-12-0912
```
I have been reading quite a bit or research on AI Agents, and specially have experimented notebooks from LangChain and L
lamaIndex (Agentic RAG). I find the WebVoyager research paper particularly interesting together with the LangChain imple
mentation.

Any other resources on the topics of Agents, Agentic Discovery & Exploration someone can point me to?
```
---

     
 
all -  [ Zero to Hero in LangChain: Build GenAI apps using LangChain
 ](https://www.reddit.com/r/Udemy/comments/1fcmb8m/zero_to_hero_in_langchain_build_genai_apps_using/) , 2024-09-12-0912
```
[https://www.udemy.com/course/zero-to-hero-in-langchain/?couponCode=B0A3AC0698BC8036EDF6](https://www.udemy.com/course/z
ero-to-hero-in-langchain/?couponCode=B0A3AC0698BC8036EDF6)  

```
---

     
 
all -  [ Integrating LLM Functionality with Internal APIs in a SaaS Product: Framework Recommendations Needed ](https://www.reddit.com/r/AI_Agents/comments/1fckqwk/integrating_llm_functionality_with_internal_apis/) , 2024-09-12-0912
```
We're a small SaaS company looking to incorporate an LLM agent into our product.   
Our goal is to enable the LLM agent 
to perform (when needed) in-app functions by utilizing our internal APIs. For instance, we want the LLM to be capable of
 initiating an order through an API call.

We're interested in knowing if there are any frameworks available that could 
simplify this integration process. Ideally, we're seeking a solution that's easy to implement and will be adaptive to ea
ch app/API update.

Langchain and such are OK, but they don't help me with extracting the APIs and preparing the agent p
rompt according to them, more so, they will probably break each time we do API change
```
---

     
 
all -  [ Preferred Vector Database: What's Your Top Choice? ](https://www.reddit.com/r/LangChain/comments/1fcjbkr/preferred_vector_database_whats_your_top_choice/) , 2024-09-12-0912
```
Which vector database are you currently using the most?

[View Poll](https://www.reddit.com/poll/1fcjbkr)
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-12-0912
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

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-12-0912
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-12-0912
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-12-0912
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

     
