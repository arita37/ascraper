 
all -  [ What is the difference between organizing data with collections vs with meta tags? ](https://www.reddit.com/r/LangChain/comments/1f5661h/what_is_the_difference_between_organizing_data/) , 2024-08-31-0912
```
I'm using Chroma with huggingface, I'm trying to figure out ways to organize the data. I process multiple large PDFs, ea
ch for different topics. I was planning on adding meta tags for each document so I can filter questions so that they onl
y apply to a specific topic, but I'm wondering if I should add them to different collections instead. What would the mai
n differences be?
```
---

     
 
all -  [ Help: Managing multiple inputs ](https://www.reddit.com/r/LangChain/comments/1f55i46/help_managing_multiple_inputs/) , 2024-08-31-0912
```
Hi Everyone,

I'm developing an AI-powered resume analysis chatbot using LangChain. The process begins with the user pro
viding a job description and a resume. The application then analyzes the resume based on the job description and offers 
feedback.

After this initial analysis, the user can ask questions or queries related to the resume, and the chatbot sho
uld respond based on the earlier context.

My challenge is managing this input flow—specifically, handling the initial i
nputs (job description and resume) and then seamlessly transitioning to processing subsequent user queries. Note that I 
need to take the job description separately since it's the only input passed to the retriever.

Here’s the code snippet 
for the initial chain:

    chain = (
        {
            'context' : get_context,
            'job_description' : lam
bda inputs: inputs['job_description'],
            'resume' :  lambda inputs: inputs['resume']
        }
        | templ
ate
        | hf
        | StrOutputParser()
    )

Has anyone implemented a similar setup, or do you have suggestions o
n structuring the input handling for this scenario?

Thanks in advance for your help!
```
---

     
 
all -  [ How to work with Claude using ChatVertexAI ](https://www.reddit.com/r/LangChain/comments/1f54feh/how_to_work_with_claude_using_chatvertexai/) , 2024-08-31-0912
```
Hi everyone, I wanna use an llm via ChatVertexAI from Google Cloud. As you know there's lots of different LLM on Google 
Cloud but when I pass a model name in ChatVertexAI I only can Google's gemini models. I can't see the model names that f
rom a different provider such as Antropic, Mistral, Llama etc. How to use these models using ChatVertexAI library.
```
---

     
 
all -  [ Roast my Resume. SDE @ Microsoft with 2+ years of experience.
 ](https://i.redd.it/8q9aiax8otld1.png) , 2024-08-31-0912
```

```
---

     
 
all -  [ Does anyone have experience using tools with image responses? ](https://www.reddit.com/r/LangChain/comments/1f4vbyo/does_anyone_have_experience_using_tools_with/) , 2024-08-31-0912
```
I have a tool that generates an image (in particular, it graphs some data).

I'm trying to create an agent that can call
 the tool and then further analyze the image. The idea is that the agent will have an easier time interpreting the data 
if it is visually represented (as opposed to a long string of numbers), same as a human.

If I make the graph myself and
 then pass it to the llm (I'm using ChatGPT 4o-mini) using the method [here](https://python.langchain.com/v0.2/docs/how_
to/multimodal_inputs/) (which uses a `HumanMessage` with the image represented by a byte64-string), ChatGPT works exactl
y as expected.

  
But if I create a tool that returns the same `HumanMessage`, bind that tool to the llm with `create_o
penai_tools_agent` and ask the llm to load the image itself, it is no longer able to interpret the image as anything mor
e than a string of bytes. I have looked through the docs without finding anything.

  
Does anyone have experience with 
something like this?

  
MWE:

    importimport matplotlib.pyplot as plt
    import io
    
    from langchain_core.tool
s import tool
    from langchain_openai import ChatOpenAI
    
    from langchain.agents import AgentExecutor, create_op
enai_tools_agent
    from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
    
    from langc
hain_core.messages import HumanMessage
    
    
    @tool
    def load_secret_image():
        'load a secret image tha
t I have prepared for you'
    
        #mwe: just plot a simple graph
        plt.plot([1,2,4])
    
        with io.By
tesIO() as buf:
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_data = base64.b64en
code(buf.read()).decode('utf-8')
        
        return HumanMessage(
            content = [
            {'type': 'tex
t', 'text': ''},
            {
                'type': 'image_url', 
                'image_url': {'url': f'data:image/p
ng;base64,{image_data}'}
            }]
            )
    
    
    
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    

    # it works when manually using the tool's output as input
    pure_message = load_secret_image({})
    response = l
lm.invoke([
        ('system', 'You are a helpful AI bot'),
        ('human', 'What is this image?'),
        pure_messa
ge
        ])
    
    print('--- Response when directly using the tool's output as input ---')
    print(response) #suc
cess
    
    
    # it doesn't work when using the tool as part of an agent run 
    prompt = ChatPromptTemplate.from_m
essages([
        ('system', 'You are a helpful AI bot'),
        ('human', '{input}'),
        MessagesPlaceholder('age
nt_scratchpad'),
    ]
    )
    agent = create_openai_tools_agent(llm, tools = [load_secret_image], prompt = prompt)
  
  executor = AgentExecutor(agent = agent, tools=[load_secret_image])
    
    
    #run model
    print('\n--- Response 
when using the tool as part of an agent run ---')
    response = executor.invoke({'input': 'What is this image?'})
    p
rint(response) #fail
    
    
     matplotlib.pyplot as plt
    import io
    
    from langchain_core.tools import too
l
    from langchain_openai import ChatOpenAI
    
    from langchain.agents import AgentExecutor, create_openai_tools_a
gent
    from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
    
    from langchain_core.me
ssages import HumanMessage
    
    
    @tool
    def load_secret_image():
        'load a secret image that I have pre
pared for you'
    
        #mwe: just plot a simple graph
        plt.plot([1,2,4])
    
        with io.BytesIO() as b
uf:
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_data = base64.b64encode(buf.rea
d()).decode('utf-8')
        
        return HumanMessage(
            content = [
            {'type': 'text', 'text': 
''},
            {
                'type': 'image_url', 
                'image_url': {'url': f'data:image/png;base64,{i
mage_data}'}
            }]
            )
    
    
    
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    
    # it wo
rks when manually using the tool's output as input
    pure_message = load_secret_image({})
    response = llm.invoke([

        ('system', 'You are a helpful AI bot'),
        ('human', 'What is this image?'),
        pure_message
        ]
)
    
    print('--- Response when directly using the tool's output as input ---')
    print(response) #success
    
  
  
    # it doesn't work when using the tool as part of an agent run 
    prompt = ChatPromptTemplate.from_messages([
  
      ('system', 'You are a helpful AI bot'),
        ('human', '{input}'),
        MessagesPlaceholder('agent_scratchpa
d'),
    ]
    )
    agent = create_openai_tools_agent(llm, tools = [load_secret_image], prompt = prompt)
    executor =
 AgentExecutor(agent = agent, tools=[load_secret_image])
    
    
    #run model
    print('\n--- Response when using t
he tool as part of an agent run ---')
    response = executor.invoke({'input': 'What is this image?'})
    print(respons
e) #fail
    
    
    



[Model outputs](https://preview.redd.it/6pmutq500tld1.png?width=1088&format=png&auto=webp&s=9
5bfe9099063c7824d7a0511cbc2121fcdeb027e)

  


  

```
---

     
 
all -  [ Function call Authentication  ](https://www.reddit.com/r/LangChain/comments/1f4uxpe/function_call_authentication/) , 2024-08-31-0912
```
I have a dashboard that displays client portfolio information. I'm trying to implement a chatbot using LangChain and the
 function calling method to retrieve this portfolio information through API calls. However, the challenge I'm facing is 
that all these APIs require a bearer token for authentication. I'm struggling to find a way to pass this token to the (f
unction calling) tools I'm using. Can anyone help me with this? 
```
---

     
 
all -  [ RAG Me Up - Easy RAG as a service platform ](https://www.reddit.com/r/Rag/comments/1f4uosk/rag_me_up_easy_rag_as_a_service_platform/) , 2024-08-31-0912
```
New to this subreddit but highly relevant so figured I'd post our repository for doing RAG: [https://github.com/AI-Comma
ndos/RAGMeUp](https://github.com/AI-Commandos/RAGMeUp)

Key features:

* Built on top of Langchain so you don't have to 
do it (trust me, worth it)
* Uses self-inflection to rewrite vague queries
* Integrates with OS LLMs, Azure, ChatGPT, Ge
mini, Ollama
* Instruct template and history bookkeeping handled for you
* Hybrid retrieval through Milvus and BM25 with
 reranking
* Corpus management through web UI to add/view/remove documents
* Provenance attribution metrics to see how m
uch documents attribute to the generated answer <-- this is unique, we're the only ones who have this right now

Best of
 all - you can run and configure it through a single .env file, no coding required.
```
---

     
 
all -  [ 🚀 Revolutionizing RAG: The Power of Re-ranking: ](https://medium.com/@nirdiamant21/relevance-revolution-how-re-ranking-transforms-rag-systems-0ffaa15f1047) , 2024-08-31-0912
```
Ever wondered how to take your Retrieval-Augmented Generation (RAG) system to the next level? Re-ranking is the game-cha
nger in information retrieval that's transforming how we deliver relevant content to users.

Key benefits:
- Enhanced re
levance in search results
- Improved handling of complex queries
- Boosted performance in RAG systems

Curious to learn 
more? Read a short but comprehensive Medium blog post I wrote about it:
```
---

     
 
all -  [ RAG Me Up now supports Ollama ](https://www.reddit.com/r/LangChain/comments/1f4thb0/rag_me_up_now_supports_ollama/) , 2024-08-31-0912
```
You can now run super fine-grained RAG out of the box on Ollama without writing a single line of code, check it out: [ht
tps://github.com/AI-Commandos/RAGMeUp](https://github.com/AI-Commandos/RAGMeUp)
```
---

     
 
all -  [ You can avoid wasting resources with Semantic Caching - a guide to reduce your app cost and latency ](https://www.reddit.com/r/ChatGPTCoding/comments/1f4rmjf/you_can_avoid_wasting_resources_with_semantic/) , 2024-08-31-0912
```
Hey everyone,

Today, I'd like to share a powerful technique to drastically cut costs and improve user experience in LLM
 applications: S**emantic Caching**.  
This method is particularly valuable for apps using OpenAI's API or similar langu
age models.

The Challenge with AI Chat Applications As AI chat apps scale to thousands of users, two significant issues
 emerge:

1. Exploding Costs: API calls can become expensive at scale.
2. Response Time: Repeated API calls for similar 
queries slow down the user experience.

**Semantic caching addresses both these challenges effectively.**

Understanding
 Semantic Caching Traditional caching stores exact key-value pairs, which isn't ideal for natural language queries. Sema
ntic caching, on the other hand, understands the meaning behind queries.

(🎥 I've created a YouTube video with a hands-o
n implementation if you're interested: [https://youtu.be/eXeY-HFxF1Y](https://youtu.be/eXeY-HFxF1Y) *)*

# How It Works:


1. Stores the essence of questions and their answers
2. Recognizes similar queries, even if worded differently
3. Reus
es stored responses for semantically similar questions

The result? Fewer API calls, lower costs, and faster response ti
mes.

Key Components of Semantic Caching

1. Embeddings: Vector representations capturing the semantics of sentences
2. 
Vector Databases: Store and retrieve these embeddings efficiently

The Process:

1. Calculate embeddings for new user qu
eries
2. Search the vector database for similar embeddings
3. If a close match is found, return the associated cached re
sponse
4. If no match, make an API call and cache the new result

Implementing Semantic Caching with GPT-Cache GPT-Cache
 is a user-friendly library that simplifies semantic caching implementation. It integrates with popular tools like LangC
hain and works seamlessly with OpenAI's API.

# Basic Implementation:

    from gptcache import cache
    from gptcache.
adapter import openai
    
    cache.init()
    cache.set_openai_key()

# Tradeoffs

Benefits of Semantic Caching

1. Co
st Reduction: Fewer API calls mean lower expenses
2. Improved Speed: Cached responses are delivered instantly
3. Scalabi
lity: Handle more users without proportional cost increase

Potential Pitfalls and Considerations

1. Time-Sensitive Que
ries: Be cautious with caching dynamic information
2. Storage Costs: While API costs decrease, storage needs may increas
e
3. Similarity Threshold: Careful tuning is needed to balance cache hits and relevance

# Conclusion

Conclusion Semant
ic caching is a game-changer for AI chat applications, offering significant cost savings and performance improvements.  

Implement it to can scale your AI applications more efficiently and provide a better user experience.

Happy hacking : 
)
```
---

     
 
all -  [ Help: Managing Chat History Efficiently ](https://www.reddit.com/r/LangChain/comments/1f4pkvl/help_managing_chat_history_efficiently/) , 2024-08-31-0912
```
Hi everyone,

I'm working on a project where I use a Vision-Language Model to perform detailed assessments on a series o
f uploaded images. The process involves analyzing up to 20 images in several steps. However, I've run into a significant
 challenge with managing input tokens.

The core issue is that with each interaction, I need to resend the entire histor
y of the conversation, including all the images, to ensure the model has the necessary context. This quickly leads to a 
high token cost and eventually runs into the context window limit.

I’m wondering if it's possible to add memory to the 
chat in LangChain to store and reuse the input tokens without needing to resend them every time. Ideally, I’d like to ma
intain the model's understanding of the images across multiple steps without re-uploading them, keeping the token usage 
efficient.

Does anyone have experience dealing with a similar use case? Are there strategies within LangChain to manage
 this more effectively? I’m open to advice, suggestions, or even a paid consultation to explore potential solutions.

Th
anks in advance for any help!
```
---

     
 
all -  [ Not getting relevant answers after specifying the top_k to smaller values then the data we have. ](https://www.reddit.com/r/u_Single-Philosophy760/comments/1f4nygf/not_getting_relevant_answers_after_specifying_the/) , 2024-08-31-0912
```
I ain't getting relevant answers if I specify the top\_k to like smaller than the datas we have. When I specify the corr
ect number of datas we have it gives relevant answers. Soo what is the solution for this?

FYI - I am developing the bot
 in Ruby. 

  
Here is the code

    # app/services/chatbot_service.rb
    require 'langchain'
    require 'openai'
    
require 'pinecone'
    require 'dotenv/load'
    require 'json'
    
    class RetrievalTool
      attr_reader :name, :d
escription
    
      def initialize(name, func, description)
        @name = name
        @func = func
        @descrip
tion = description
      end
    
      def execute(input)
        @logger.info('Executing retrieval tool with input: #{
input}')
        @func.call(input)
        @logger.info('Retrieval result: #{result.inspect}')
        result
      end

    end
    
    class ChatbotService
      def initialize
        Dotenv.load
    
        @openai_api_key = ENV['OPENA
I_API_KEY']
        @pinecone_api_key = ENV['PINECONE_API_KEY_FREE']
        @pinecone_environment = ENV['PINECONE_ENVIR
ONMENT']
    
        OpenAI.configure do |config|
          config.access_token = @openai_api_key
        end
    
    
    Pinecone.configure do |config|
          config.api_key = @pinecone_api_key
          config.environment = @pinecone
_environment
        end
    
        @pinecone = Pinecone::Client.new
        @index_name = 'foaps-merged'
        @nam
espace = 'merged'
        @index = @pinecone.index(@index_name)
        @llm = Langchain::LLM::OpenAI.new(api_key: @open
ai_api_key, default_options: { temperature: 3.0, chat_completion_model_name: 'gpt-4o' })
        @openai_client = OpenAI
::Client.new
        @logger = Logger.new(STDOUT) # Logs to standard output; you can configure this to a file if needed

    
        # Initialize the retriever tool with retrieve_response method
        @retriever_tool = RetrievalTool.new(

          'search_datas',                         # Name of the tool
          method(:retrieve_response),             #
 Function to be called
          'Search and return information related to the data you have. If calculation is needed, 
perform it.'
        )
      end
    
      def chat(input, memory)
        system_message = <<~MSG
        You are a da
ta analyst of Foaps company. Your name is Incredible. Answer questions based on the data you have. Answer it clearly by 
checking the data you have. Double check before answering.
    
        The available data columns are as follows:
     
   - **combo_amount**: The total amount associated with a combo item.
        - **combo_id**: A unique identifier for th
e combo item.
        - **combo_name**: The name of the combo item.
        - **combo_updated_at**: The date and time wh
en the combo item was last updated.
        - **location_id**: A unique identifier for the location where the combo is o
ffered.
        - **location_name**: The name and address of the location.
        - **location_updated_at**: The date a
nd time when the location information was last updated.
        - **restaurant_id**: A unique identifier for the restaur
ant offering the combo.
        - **restaurant_name**: The name of the restaurant.
        - **restaurant_updated_at**: 
The date and time when the restaurant information was last updated.
    
        Ensure that your responses are helpful,
 professional, and easily understandable. Double-check the data for accuracy before providing answers.
      MSG
    
  
      @logger.info('Received input: #{input}')
    
        context = @retriever_tool.execute(input)
        @logger.inf
o('Retrieved context: #{context}')
        
        messages = [
          { role: 'system', content: system_message },

          { role: 'system', content: 'Context: #{context}' },
          *memory,
          { role: 'user', content: inpu
t }
        ]
    
        response = @llm.chat(messages: messages)
        @logger.info('Generated response: #{response
.completion}')
    
        response.completion
      end
    
      def print_vector_stats
        index_stats = @index
.describe_index_stats
        @logger.info('Full index stats: #{index_stats.inspect}')
    
        namespace_stats = in
dex_stats['namespaces']
        @logger.info('Namespace stats: #{namespace_stats.inspect}')
    
        if namespace_st
ats.nil? || namespace_stats.empty?
          @logger.info('No namespace statistics available.')
          total_vectors 
= 0
        else
          if namespace_stats.key?(@namespace)
            total_vectors = namespace_stats[@namespace]['
vectorCount']
            @logger.info('Vectors in namespace '#{@namespace}': #{total_vectors}')
          else
        
    @logger.info('Namespace '#{@namespace}' not found. Available namespaces: #{namespace_stats.keys}')
            total
_vectors = 0
          end
        end
    
        total_vectors
      end
    
      private
    
      def get_embedd
ing(text)
        response = @openai_client.embeddings(
          parameters: {
            model: 'text-embedding-3-lar
ge',
            input: text
          }
        )
        response['data'][0]['embedding']
      end
    
      def ret
rieve_response(question)
        vector = get_embedding(question)
        # @logger.info('Query vector: #{vector.inspect
}')
    
        # Log the vector to ensure it is correct
        # puts 'Query vector: #{vector.inspect}'
    
        
# total_vectors = print_vector_stats # Retrieve total vector count
        results = @index.query(
          vector: vec
tor,
          namespace: @namespace,
          top_k: 50,  # Use total vectors as top_k
          # top_k: top_k,
     
     include_metadata: true,
          include_values: true
        )
        # puts 'Raw results: #{results.inspect}'
 
   
        if results['matches']
          # Extract and format metadata from each match
          matches_info = resul
ts['matches'].map do |match|
            {
              id: match['id'],  # Retrieve ID from the result
              t
ext: match['metadata']['text'],
              combo_amount: match['metadata']['combo_amount'].to_f,  # Convert to float 
for comparison
              combo_id: match['metadata']['combo_id'],
              combo_name: match['metadata']['combo
_name'],
              combo_updated_at: match['metadata']['combo_updated_at'],
              location_id: match['metada
ta']['location_id'],
              location_name: match['metadata']['location_name'],
              location_updated_at:
 match['metadata']['location_updated_at'],
              restaurant_id: match['metadata']['restaurant_id'],
            
  restaurant_name: match['metadata']['restaurant_name'],
              restaurant_updated_at: match['metadata']['restaur
ant_updated_at']
            }
          end
      
          @logger.info('Matches information: #{matches_info.inspect}
')
      
          matches_info # Return all the extracted information
        else
          'No relevant data found.'

        end
      end
    end
```
---

     
 
all -  [ Agentic RAG Using CrewAI & LangChain! ](https://www.reddit.com/r/LangChain/comments/1f4nogp/agentic_rag_using_crewai_langchain/) , 2024-08-31-0912
```
I tried to build an end to end Agentic RAG workflow using LangChain and CrewAI and here is the complete [tutorial video]
(https://youtu.be/tioFxI_WTkk). 

Share any feedback if you have:) 
```
---

     
 
all -  [ Metadata management using langchain and vector store ](https://www.reddit.com/r/LangChain/comments/1f4mcoh/metadata_management_using_langchain_and_vector/) , 2024-08-31-0912
```
Business requirements: we have lot of websites where the tech team has listed solutions when we hit a wall. 
We want the
 RAG application to process a question and spit out the link where the solution is located. 

Context: we are using lang
chainJS, chroma DB 

Does anyone know what do we and how should we design the data system to albe able to achieve this ?
 
```
---

     
 
all -  [ [0 YoE, Student, SWE Intern 2025, United States] ](https://www.reddit.com/r/resumes/comments/1f4jodp/0_yoe_student_swe_intern_2025_united_states/) , 2024-08-31-0912
```
I haven't gotten any interviews yet for the 2025 internship cycle (120+ Applications). What can I do to improve?

https:
//preview.redd.it/45pp3p5xipld1.png?width=1098&format=png&auto=webp&s=5774e2014e569212c20f12bf6ca3a039f4ccebd5

&#x200B;

```
---

     
 
all -  [ working with Langgraph js and Langgraph Studio  ](https://www.reddit.com/r/LangChain/comments/1f4jhgg/working_with_langgraph_js_and_langgraph_studio/) , 2024-08-31-0912
```
I am using langgraph js for my project. I was wondering whether you can get Langgraph Studio working with langgraph js. 
There are no docs on this, only for python version but no js version. 
```
---

     
 
all -  [ Handling multiple concurrent chat sessions in production. Multi-threading or Asynchronous Programmin ](https://www.reddit.com/r/LangChain/comments/1f4j8mq/handling_multiple_concurrent_chat_sessions_in/) , 2024-08-31-0912
```
Chatbots have a lot (by cpu standards) free time when processing queries because they interface with OpenAI/Google's ser
vers to process those queries. But python is a single threaded interpreter due to the Global Interpreter Lock. So when m
ultiple people are hitting the API what's the best way to handle those multiple sessions? FYI I am using Gemini and I am
 not using LangChain/LangGraph and directly using the Gemini Python SDK. But if you think this will be an impediment ple
ase tell me why and how to go about migrating.

Obviously each session must be associated with a uuid and stored in a di
ctionary with all the required data. Should I spawn the function for responding to a new query for a session in a new th
read? Or define async functions to handle the messages? There are some tools my chatbot/agent uses which makes calls to 
Gemini API's too. So should these also be defined in async functions? 
```
---

     
 
all -  [ Protecting against Prompt Injection ](https://www.reddit.com/r/LangChain/comments/1f4ixl0/protecting_against_prompt_injection/) , 2024-08-31-0912
```
I've recently been thinking about prompt injections

The current approach to dealing with them seems to consist of sendi
ng user input to an LLM, asking it to classify if it's malicious or not, and then continuing with the workflow. That's l
eft the hair on the back of my neck standing up. 

1. Extra cost, granted it small, but LLM's ain't free

2. Like lighti
ng a match to check for a gas leak, sending a prompt to an LLM to see if the prompt can jailbreak the LLM seems wrong. T
echnically as long as you're inspecting the response and limit it to just 'clean' / 'malicious' it should be \`ok\`. 

B
ut still it feels off. 

  
So threw together a simple CPU based logistic regression model with sklearn that identifies 
if a prompt is malicious or not. 

It's about 102KB, so runs v. fast on a web server. 

[https://huggingface.co/thevgerg
roup/prompt\_protect](https://huggingface.co/thevgergroup/prompt_protect)

  
Expect I'll make some updates along the wa
y.  

But have a go, let me know what you think  

```
---

     
 
all -  [ LLM-3D Print: Large Language Models To Monitor and Control 3D Printing
 ](https://www.reddit.com/r/LangChain/comments/1f4gehi/llm3d_print_large_language_models_to_monitor_and/) , 2024-08-31-0912
```
**Not my work so cant answer technical questions but I think this might belong here. Want to know if something like this
 can be made using langchain?** As someone who is a 3D printing hobbyist and work with LLMs this is super exciting.

I j
ust came across an interesting paper that explores a **Multi-Agent LLM Framework** for autonomous 3D printing, and I had
 to share it here. This framework uses multiple Large Language Models (LLMs), ChatGPT4 in this case, each acting as its 
own intelligent agent, to manage different aspects of the 3D printing process. It’s pretty cool how they’ve set it up! 


[https://arxiv.org/abs/2408.14307](https://arxiv.org/abs/2408.14307)



Overall it seems actually useful use-case for L
LMs, and not just another LLM RAG or question/ans bot. Would love to hear thoughts on other potential applications using
 langchain.
```
---

     
 
all -  [ Senior Machine Learning Engineer Role Available! ](https://www.reddit.com/r/MLjobs/comments/1f4fmz0/senior_machine_learning_engineer_role_available/) , 2024-08-31-0912
```
Are you an experienced machine learning engineer with a passion for building advanced AI solutions? **Loka**, a leading 
tech consultancy based in Silicon Valley, is looking for a skilled Senior Machine Learning Engineer to join our dynamic 
team!  
  
**Required Hard Skills:**

* 4+ years of ML engineering experience
* Bachelor’s degree in Computer Science or
 related
* Experience with Python, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, etc.)
* Experien
ce building GenAI solutions using LLMs, including frameworks like LangChain and LlamaIndex, prompt engineering, fine-tun
ing and serving models, and implementing common patterns like RAG and NLQ
* Client-facing experience
* Familiarity with 
containerization and orchestration tools

**Interested? For the full job description and to apply, check the link:** [ht
tps://app7.greenhouse.io/intern.../applications/4074124007](https://app7.greenhouse.io/internal_job_board/applications/4
074124007?fbclid=IwZXh0bgNhZW0CMTAAAR06V-GNkc9hMT1r6Osq5i5K_vwJe9fyR7QlrYoBh2WjDG7eEeVndqNOTkE_aem_3I3k2aRgVQw7kCMgXq5-p
w)  

```
---

     
 
all -  [ Domain specific Agentic RAG with LangChain and LangGraph ](https://www.reddit.com/r/LangChain/comments/1f4drgh/domain_specific_agentic_rag_with_langchain_and/) , 2024-08-31-0912
```
Hello everyone,

I just finished a new blog post on how to add domain specific data to RAG using Agents and make a smart
er Corrective RAG.

Here's the link: [https://www.metadocs.co/2024/08/29/simple-domain-specific-corrective-rag-with-lang
chain-and-langgraph/](https://www.metadocs.co/2024/08/29/simple-domain-specific-corrective-rag-with-langchain-and-langgr
aph/)

Have a nice read
```
---

     
 
all -  [ Implementing LangChain with OpenAI: Tool Calling and Streaming Output ](https://www.reddit.com/r/LangChain/comments/1f4d5pf/implementing_langchain_with_openai_tool_calling/) , 2024-08-31-0912
```


Hi everyone,

I’m exploring how to implement LangChain 2.0 with OpenAI’s models and I’m particularly interested in usi
ng tool calling and streaming output features.

Does anyone have experience or examples of how to set up LangChain with 
OpenAI for:

	1.	Tool Calling: How to configure LangChain to call external tools or APIs using OpenAI’s chat models?
	2.
	Streaming Output: Steps to enable and handle streaming output for real-time interactions?

Any guidance, code snippets,
 or resources would be greatly appreciated. Thanks!
```
---

     
 
all -  [ Most commonly used HuggingFaceEmbedding models ](https://www.reddit.com/r/LangChain/comments/1f4b4fa/most_commonly_used_huggingfaceembedding_models/) , 2024-08-31-0912
```
Which HuggingFaceEmbeddings/sentence transformer models do you guys use the most for your various GenAI RAG projects?
```
---

     
 
all -  [ Open Source AI Agent for Developer Relations ](https://www.reddit.com/r/LangChain/comments/1f4atex/open_source_ai_agent_for_developer_relations/) , 2024-08-31-0912
```
We just launched on Product Hunt and Open Sourced our AI Agent that assists with managing developer relations. We built 
the Agent using LangGraph Studio, and we cannot recommend it enough. The OSS repo can also be a good starting point to m
ake dev focussed Agents! Any feedback welcome :)

[https://www.producthunt.com/posts/develyn](https://www.producthunt.co
m/posts/develyn)  


[https://github.com/openfunnel/develyn](https://github.com/openfunnel/develyn)

https://preview.red
d.it/dc880zz3knld1.png?width=1920&format=png&auto=webp&s=eb7f6265216b2a3cc761d3a4db84dfee708f279a
```
---

     
 
all -  [ How to extract textual data from Excel and PPTs and store in vector db for RAG? ](https://www.reddit.com/r/LangChain/comments/1f48zch/how_to_extract_textual_data_from_excel_and_ppts/) , 2024-08-31-0912
```
I would also need to store metadata to give citations of my queried result, like the file_name, sheet_name, row_id/colum
n_id or slide numbers in case of PPTs.

Read somewhere to read the files as pandas df and store in SQL database and run 
query agents on top of it. That is not an option. Need to use vector DB and RAG.
```
---

     
 
all -  [ Data hub for LLMs and RAG ](https://www.reddit.com/r/LLMDevs/comments/1f48kf3/data_hub_for_llms_and_rag/) , 2024-08-31-0912
```
Is there a provider where I can connect multiple data sources like for example google drive and sharepoint via single si
gn on and then use the complete data from all sources to create a RAG Chatbot with langchain?
```
---

     
 
all -  [ Extensive open source RAG tutorials is getting viral ](https://github.com/NirDiamant/RAG_Techniques) , 2024-08-31-0912
```
Hi all,

Sharing a repo I was working on for a while. 

It’s open-source and includes many different strategies for RAG 
(currently 23), including tutorials, and visualizations.

This is great learning and reference material.  
Open issues, 
suggest more strategies, and use as needed.

It got very popular - 5K stars within a month!

Enjoy!
```
---

     
 
all -  [ How can we restrict Database tables for particular users ](https://www.reddit.com/r/LangChain/comments/1f43iht/how_can_we_restrict_database_tables_for/) , 2024-08-31-0912
```
I have fine-tuned a META LLAMA 3.1 to generate SQL queries based on our schema. This model is integrated with LangChain'
s SQL chain to execute the query and provide the final response.

Now, what I want to achieve is to implement permission
s or restrictions based on user roles. Currently, the model gives output to all users, irrespective of any restrictions.
 For example, if HR users access this, they should only be able to query HR-related tables. Similarly, accounts users sh
ould only access accounts-related tables.

We can retrieve these user roles from the logged-in user information in ERPNe
xt, as it is integrated into our system.
```
---

     
 
all -  [ How to use OpenAI's Assistants API with LangChain? ](https://www.reddit.com/r/LangChain/comments/1f42rtg/how_to_use_openais_assistants_api_with_langchain/) , 2024-08-31-0912
```
I didn't find any wrapper or guide for using OpenAI's Assistants API in Langchain which has Code Interpreter, Websearch 
and file storage. How to use it? Is it a separate thing entirely?

EDIT: \[Solved\] Import from `langchain.agents.openai
_assistant.base.OpenAIAssistantRunnable`. So it wasn't in docs, but in API Reference [here](https://python.langchain.com
/v0.2/api_reference/langchain/agents/langchain.agents.openai_assistant.base.OpenAIAssistantRunnable.html#langchain.agent
s.openai_assistant.base.OpenAIAssistantRunnable).
```
---

     
 
all -  [ AI agents hype or real?  ](https://www.reddit.com/r/LangChain/comments/1f4264n/ai_agents_hype_or_real/) , 2024-08-31-0912
```
I see it everywhere, news talking about the next new thing. Langchain talks about it in any conference they go to. Many 
other companies also arguing this is the next big thing. 

I want to believe it sounds great in paper. I tried a few thi
ngs myself with existing frameworks and even my own code but LLMs seem to break all the time, hallucinate in most workfl
ows, failed to plan, failed on classification tasks for choosing the right tool and failed to store and retrieve data su
ccessfully, either using non structure vector databases or structured sql databases.

Feels like the wild west with ever
yone trying many different solutions. I want to know if anyone had much success here in actually creating AI agents that
 do work in production.

I would define an ai agent as :
- AI can pick its own course of action with the available tools

- AI can successfully remember , retrieve and store previous information.
- AI can plan the next steps ahead and can as
k for help for humans when it gets stuck successfully.
- AI can self improve and learn from mistakes.
```
---

     
 
all -  [ Any personal projects? ](https://www.reddit.com/r/LangChain/comments/1f40lxr/any_personal_projects/) , 2024-08-31-0912
```
Has anyone made or planning to make any interesting or useful personal projects using LangChain?
I am trying to teach La
ngChain some office juniors and want to assign them a fun personal project. 
```
---

     
 
all -  [ sql data to embeddings? ](https://www.reddit.com/r/Rag/comments/1f3zp2r/sql_data_to_embeddings/) , 2024-08-31-0912
```
Hi all - I'm early in my learning process about using LLMs with rag prompts, and at a high level it all is making sense.
  Ultimately, I'm looking for an architectural understanding of a RAG solution, since an operating assistant still might
 not hit the best practices.

I have a working assistant that references log data using OpenAI's assistant API, referenc
ing the data via file attachments. There are some limitations on the size of the data with this approach, so I've been f
ollowing this langchain tutorial on RAG with sql queries:  [https://python.langchain.com/v0.2/docs/tutorials/qa\_chat\_h
istory/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)

  
You'll note that this tutorial dynamical
ly builds a query based on table schema info, then runs said query to extract data. But how does this work?  Is all the 
data returned from the query turned to an embedding behind the scenes? 

Is my understanding of embeddings even correct 
in that your text data (from documents, sql queries, web pages, wherever) is converted to a vector store and persisted (
somewhere) for reference by the LLM when evaluating the prompt? Once persisted, the LLM can intelligently search the vec
tor store, thereby keeping the size of the prompt within the token limits?


```
---

     
 
all -  [ Which langchain model provider for a Q for Business app? ](https://www.reddit.com/r/aws/comments/1f3z5x6/which_langchain_model_provider_for_a_q_for/) , 2024-08-31-0912
```
So, you can build apps via q for business, and under the hood it uses bedrock right, but the q for business bit does do 
some extra processing. (Seems it directs your request to different models)

is it possible to integrate that directly to
 langchain? if not, does the q for business app expose the bedrock endpoints that are trained on your docs, so you can t
hen build a langchain app?
```
---

     
 
all -  [ Where can I find people to chat with about langchain / LLM app development? ](https://www.reddit.com/r/LangChain/comments/1f3ymw8/where_can_i_find_people_to_chat_with_about/) , 2024-08-31-0912
```
I sadly don't know many other people in my real life who are working on langchain / LLM based apps and agents.  I'd like
 to find more people working on this sort of thing to learn from, chat with, and have some kind of community.  Any tips?


So far I checked out langchain's Discord.  It didn't look super active, and it seemed focused on Langchain itself -- w
hich makes sense, but I'm more interested in what we can do with these apps.

I've also of course checked here and got s
ome great answers to a question.  So maybe this is the answer.  Just wondering if there are more good places I can go to
 connect with people working on this stuff.
```
---

     
 
all -  [ Looking for Open-Source LangChain Apps with a Well-Structured Codebase ](https://www.reddit.com/r/LangChain/comments/1f3xskm/looking_for_opensource_langchain_apps_with_a/) , 2024-08-31-0912
```
Hi all,

I'm currently exploring LangChain and would love to see some open-source projects that utilize it effectively. 
I'm particularly interested in examples that showcase good coding patterns and practices. If anyone has come across any 
well-structured LangChain apps or repositories, I'd greatly appreciate it if you could share them. Thanks!
```
---

     
 
all -  [ [0 YoE, Fresher, SWE, India] ](https://i.redd.it/g1rpwfkp6kld1.jpeg) , 2024-08-31-0912
```
I am hoping to apply for tech companies for swe roles this december, please review my CV and suggest if any changes are 
to be done in the formatting, vocabulary, project description and anything.
Thanks in Advance!
```
---

     
 
all -  [ We created FloAI and created a support agent using it ](https://www.reddit.com/r/LangChain/comments/1f3wpi0/we_created_floai_and_created_a_support_agent/) , 2024-08-31-0912
```
We ([rootflo](https://rootflo.ai)) have been toying around AI for a while now. After doing a couple of smaller projects 
we understood the importance of using AI to maximize the efficiency of AI automation. That's when we tried out some avai
lable frameworks like auto-gen and crew-ai.

Trying out some of the existing frameworks, we felt limited by their capabi
lities and lack of control. This is when we tried to come up with out own framework for building agentic AI bots/agents.
 The thought was around composability where we want to make components like Lego blocks that can come together to create
 bigger structures. The inspiration came from some good whitepapers, and talks from a few veterans in the AI space like 
AndrewNg. We used langGraph as the underlying backend but will plan extensibility.

I would like some feedback from the 
community, and ideas that we can pursue that you see are some of the shortcomings of the current frameworks out there. H
ere a support agent implemented using FloAI: [https://medium.com/rootflo/build-an-agentic-ai-customer-support-bot-using-
floai-533660fb9c9b](https://medium.com/rootflo/build-an-agentic-ai-customer-support-bot-using-floai-533660fb9c9b)



Pro
ject URL: [https://github.com/rootflo/flo-ai](https://github.com/rootflo/flo-ai)

Some inspirations:

[https://arxiv.org
/abs/2308.08155](https://arxiv.org/abs/2308.08155)  
[https://arxiv.org/abs/2305.04091](https://arxiv.org/abs/2305.04091
)  
[https://arxiv.org/abs/2403.14403](https://arxiv.org/abs/2403.14403)  
[https://www.youtube.com/watch?v=sal78ACtGTc]
(https://www.youtube.com/watch?v=sal78ACtGTc)
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-31-0912
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-31-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-31-0912
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

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-31-0912
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-31-0912
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

     
