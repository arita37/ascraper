 
all -  [ GPT Synthesizer - Software developer's best friend | Product Hunt ](https://www.producthunt.com/posts/gpt-synthesizer) , 2023-08-10-0910
```

```
---

     
 
all -  [ What are the text chunking/splitting and embedding best practices for RAG applications? ](https://www.reddit.com/r/LocalLLaMA/comments/15mq1ri/what_are_the_text_chunkingsplitting_and_embedding/) , 2023-08-10-0910
```
I'm trying to make an LLM powered RAG application without LangChain that can answer questions about a document (pdf) and
 I want to know some of the strategies and libraries that you guys have used to transform your text for text embedding. 
I would also like to know which embedding model you used and how you dealt with the sequence length.  


My documents wi
ll be long textbooks and I'm currently using the MTEB text embedders from Hugging Face which all have sequence lengths o
f 512. 

 
```
---

     
 
all -  [ My Manager refuses to use Langchain ](https://www.reddit.com/r/LangChain/comments/15mod3l/my_manager_refuses_to_use_langchain/) , 2023-08-10-0910
```
As the title say my manager is completely against using langchain how do I convince them on using it?

Reason they say a
re it is not production ready, is it really not production ready tho? We can use some parts of langchain right? Like tex
t splitter and stuff?
```
---

     
 
all -  [ QnA system that supports multiple file types[PDF, CSV, DOCX, TXT, PPT, URLs] with LangChain on Colab ](https://www.reddit.com/r/LargeLanguageModels/comments/15mlfwn/qna_system_that_supports_multiple_file_typespdf/) , 2023-08-10-0910
```
In this video, we will discuss how to create a QnA system that supports multiple file types such as PDF, CSV, EXCEL, PPT
, DOCX, TXT, and URLs. All of these files utilize a single vector space and collaborate in the QnA process.
https://yout
u.be/5XZb3Mb2ioM
```
---

     
 
all -  [ QnA system that supports multiple file types[PDF, CSV, DOCX, TXT, PPT, URLs] with LangChain on Colab ](https://www.reddit.com/r/LangChain/comments/15mld5x/qna_system_that_supports_multiple_file_typespdf/) , 2023-08-10-0910
```
In this video, we will discuss how to create a QnA system that supports multiple file types such as PDF, CSV, EXCEL, PPT
, DOCX, TXT, and URLs. All of these files utilize a single vector space and collaborate in the QnA process.

https://you
tu.be/5XZb3Mb2ioM
```
---

     
 
all -  [ GGML and GPTQ on langchain ](https://www.reddit.com/r/LangChain/comments/15mkp1w/ggml_and_gptq_on_langchain/) , 2023-08-10-0910
```
I have a pretty basic pc, with a 4GB 1650ti and 16 GB RAM, I usually use collab to play around with these models, but I 
wanted to learn to use them locally, with langchain, with these specs I didn't have much options but go for GGML or GPTQ
 versions of Llama2 by TheBloke, I tried the whole day to get it to work, but whatever resource I used got me nothing, t
hat made me work.   

&#x200B;

It is also on me not knowing everything clearly, but again the progress has been really 
quick with the LLM stuff, and I've been trying to learn. I have tried all I could before posting this here, so it would 
be a great help if someone could guide me for the same.  

Following is the code I tried

\`\`\`

tokenizer = AutoTokeni
zer.from\_pretrained('localmodels/Llama-2-7B-GPTQ',  
 use\_auth\_token=True,)  
model = AutoModelForCausalLM.from\_pret
rained('localmodels/Llama-2-7B-GPTQ',  
 device\_map='auto',  
 torch\_dtype=torch.float16,  
 use\_auth\_token=True)

\
`\`\`
```
---

     
 
all -  [ Is there a way to have gpt4all query against localdocs only? ](https://www.reddit.com/r/LangChain/comments/15mk62w/is_there_a_way_to_have_gpt4all_query_against/) , 2023-08-10-0910
```
Is there a way to have gpt4all return results based on files in localdocs only and not rely on it's already trained DB? 
 
```
---

     
 
all -  [ Build quickchat.ai Replica ](https://www.reddit.com/r/LangChain/comments/15mfvc2/build_quickchatai_replica/) , 2023-08-10-0910
```
Hi,I want to build a site similar to [quickchat.ai](https://quickchat.ai) and I'm looking for foundational code to get s
tarted.Are there any open source projects which I could use to get started on the project. Because there are a lot of ch
atbot with knowledgebase products already in the market.Also if anyone has idea of the 3rd party tools i could use to ge
t started instead of developing every feature from scratch.  


Please share any insights that u feel would be helpful


Thanks
```
---

     
 
all -  [ A minimalistic LangChain course ](https://www.reddit.com/r/LangChain/comments/15mfhkb/a_minimalistic_langchain_course/) , 2023-08-10-0910
```
Hello everybody,

I've been creating LangChain apps for the last few months and I decided to put together all the concep
ts I found more useful and a mini-course, that reflects my own way of learning things: straightforward and without noise
.

The course is a Streamlit app, with interactive demos for each component. This way the user can immediately play with
 it, and then write his own code to reinforce the concepts.

If anyone wants to take a look, I would really appreciate s
ome feedback: [https://learnlangchain.org/](https://learnlangchain.org/)

The course also contains 4 hands-on projects, 
and I plan to add more interesting concepts, like a deep dive on document splitters, agents, and more demos of course. F
or now is just an MVP.

All the code, for the course and the projects is open source, of course :)

Thanks in advance,


Francesco
```
---

     
 
all -  [ Why is Awadb: The Open-Source Local AI-native vector database ](https://www.reddit.com/r/LangChain/comments/15mblmj/why_is_awadb_the_opensource_local_ainative_vector/) , 2023-08-10-0910
```
Awadb, an Open-Source AI-native vector database , stores and searches embedding vectors for LLM Applications, providing 
you with an efficient solution for local vector data management and queries in your environment. Below are some advantag
es of the Awadb vector database as a local database:

1. **High Performance and Low Latency:** Being a local database, A
wadb stores data on the local computer, enabling the full utilization of local hardware resources for achieving high per
formance and low-latency data access and queries.
2. **Privacy and Security:** Local databases often offer heightened da
ta privacy and security, as data doesn't need to be transmitted over the internet, reducing the risks of data leaks and 
security vulnerabilities.
3. **Offline Access:** A local database allows users to access data without an internet connec
tion, which proves highly beneficial in situations where connectivity to cloud servers is unavailable.
4. **Customizatio
n:** Local databases empower users with complete control over database configuration and management to suit specific nee
ds and requirements. This customization capability aids in optimizing performance and meeting distinct business needs.
5
. **Data Control:** With data stored locally, users can easily backup, restore, and manage data, ensuring data control a
nd stability.
6. **Reduced Cloud Costs:** For some small to medium-sized enterprises or projects, utilizing a local data
base may prove more cost-effective, circumventing the high costs associated with cloud services.
7. **Suitable for Edge 
Computing:** In scenarios demanding data processing and analysis on edge devices, a local database serves as an ideal ch
oice, providing rapid local computing capabilities.
8. **Offline Work:** Should you require the ability to continue work
ing without an internet connection, a local database ensures that you can access and manipulate data without being bound
 by network restrictions.

## Get Started

What will you build with the Awadb vector database?

If you are interested an
d want to learn more, please join us and get started now:

Github: [https://github.com/awa-ai/awadb](https://github.com/
awa-ai/awadb)

Discord: [https://discord.gg/GP7QxRrDjB](https://discord.gg/GP7QxRrDjB)
```
---

     
 
all -  [ PrivateGPT alternative for CSVs ](https://www.reddit.com/r/LangChain/comments/15ma88h/privategpt_alternative_for_csvs/) , 2023-08-10-0910
```
Are there any potential alternatives for question- answering over CSV and Excel files similar to PrivateGPT. Because, it
 seems to work well with txt, doc, pdf files but not with CSVs.
```
---

     
 
all -  [ Lamma Context length is it max(4096) or can it be increased?? ](https://www.reddit.com/r/LocalLLaMA/comments/15m9zyo/lamma_context_length_is_it_max4096_or_can_it_be/) , 2023-08-10-0910
```
I am running the model through replicate and i am getting error while i am testing on large input. is 4096 maximum that 
llama model can support or can i increase that ... if i try to pass in chunks will it give me same results because i am 
working on identifying the tone.

\--------------------------------------------------------------------------- ModelErro
r                                

Traceback (most recent call last) Cell In\[58\], line 1 

\----> 1 imposter\_scam\_re
sp = generate\_llama2\_response\_fraud(fraud\_detection\_prompt, imposter\_scam)       **2** print(imposter\_scam\_resp)
  

Cell In\[57\], line 30, in generate\_llama2\_response\_fraud(prompt\_template, prompt\_input)      **24** output = r
eplicate.run(      **25** \# 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269
e5', # LLM model      **26** 'replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e
1',      **27** input={'prompt': f'{full\_prompt} {prompt\_input} Assistant: ', # prompt      **28** 'temperature':0.1, 
'top\_p':0.9, 'max\_length':512, 'repetition\_penalty':1}) # model parameters      **29** full\_response = '' ---> 30 fo
r item in output:      **31** 	full\_response += item      **33** return full\_response  File [\~/my\_python\_venvs/gpt\
_env/lib/python3.10/site-packages/replicate/prediction.py:79](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/Ch
aran%20Teju/Documents/langchain/audio-processing/notebooks/~/my_python_venvs/gpt_env/lib/python3.10/site-packages/replic
ate/prediction.py:79), in Prediction.output\_iterator(self)      **76** self.reload()      **78** if self.status == 'fai
led': ---> 79 raise ModelError(self.error)      **81** output = self.output or \[\]      **82** new\_output = output\[le
n(previous\_output) :\] 

 ModelError: start (0) + length (4097) exceeds dimension size (4096). 

\-- 
```
---

     
 
all -  [ SentenceTransformerEmbeddings taking forever to execute ](https://www.reddit.com/r/LangChain/comments/15m9eyj/sentencetransformerembeddings_taking_forever_to/) , 2023-08-10-0910
```
Hi everyone 

**Context:** I've got all packages installed and up to date. No error in sight, no kernel crash. 2 weeks a
go this loaded in a matter of seconds (minutes?) and now it takes infinitely long, as in hours. I ran it overnight (7 ho
urs) and it's still loading the embeddings. Any idea why?

    from langchain.embeddings.sentence_transformer import Sen
tenceTransformerEmbeddings
    embedding_function = SentenceTransformerEmbeddings(model_name='all-MiniLM-L12-v2')
    pr
int('Executed')

&#x200B;
```
---

     
 
all -  [ An AI based stock analyzer using LLM and Langchain📈 ](https://www.reddit.com/r/SideProject/comments/15m5bml/an_ai_based_stock_analyzer_using_llm_and_langchain/) , 2023-08-10-0910
```
&#x200B;

https://preview.redd.it/733v3sk6n0hb1.png?width=1005&format=png&auto=webp&s=b4ebcf15c12685c3f3c0b476aef894c117
59236e

An interesting application of Language Models and Langchain in the Finance Domain 📈-

Sharing a fun weekend proj
ect that I recently completed: the 'Stock Analyzer Bot'. As an investment enthusiastic person without extensive knowledg
e in the finance domain, I often end up referring to some finance youtuber's videos or a site on the internet for the fu
ndamental analysis of stocks. To assist in such situations, I developed a stock analyzer bot based on LLM, which gathers
 up-to-date information about stock such as 1) stock price, 2) Company financials 3) Recent company-related news. The bo
t then considers all this information to conduct analysis using language models. You can even get positives and negative
s about the company's financials, which will certainly help when making an investment decision.

You can ask queries lik
e- 'Is it a good time to invest in Yes Bank?' or 'How are the current financials of reliance industries looking' and boo
m within a minute you are presented with a comprehensive financial analysis based on recent data. Of course, It is not r
ecommended to rely fully on the analysis provided by the bot. It seems like a good starting point. And yeah, I agree the
 possibilities are endless with LLMs🚀.

GIthub- [https://github.com/Pranav082001/stock-analyzer-bot](https://github.com/
Pranav082001/stock-analyzer-bot)  
Blog [An AI based stock analyzer using LLM and Langchain 📈 | by Pranav Kushare | Aug,
 2023 | Medium](https://medium.com/p/7f8a62cbcaaa)

 
```
---

     
 
all -  [ An AI based stock analyzer using LLM and Langchain📈 ](https://www.reddit.com/r/UsefulLLM/comments/15m5560/an_ai_based_stock_analyzer_using_llm_and_langchain/) , 2023-08-10-0910
```
https://preview.redd.it/7v7sv8kdn0hb1.png?width=1005&format=png&auto=webp&s=2bbf16f078378cee640466fc4c271c068e51bc50

  

An interesting application of Language Models and Langchain in the Finance Domain 📈-

Sharing a fun weekend project tha
t I recently completed: the 'Stock Analyzer Bot'. As an investment enthusiastic person without extensive knowledge in th
e finance domain, I often end up referring to some finance youtuber's videos or a site on the internet for the fundament
al analysis of stocks. To assist in such situations, I developed a stock analyzer bot based on LLM, which gathers up-to-
date information about stock such as 1) stock price, 2) Company financials 3) Recent company-related news. The bot then 
considers all this information to conduct analysis using language models. You can even get positives and negatives about
 the company's financials, which will certainly help when making an investment decision.

You can ask queries like- 'Is 
it a good time to invest in Yes Bank?' or 'How are the current financials of reliance industries looking' and boom withi
n a minute you are presented with a comprehensive financial analysis based on recent data. Of course, It is not recommen
ded to rely fully on the analysis provided by the bot. It seems like a good starting point. And yeah, I agree the possib
ilities are endless with LLMs🚀.

GIthub- [https://github.com/Pranav082001/stock-analyzer-bot](https://github.com/Pranav0
82001/stock-analyzer-bot)Blog [An AI based stock analyzer using LLM and Langchain 📈 | by Pranav Kushare | Aug, 2023 | Me
dium](https://medium.com/p/7f8a62cbcaaa)
```
---

     
 
all -  [ An AI based stock analyzer using LLM and Langchain📈 ](https://www.reddit.com/r/LangChain/comments/15m53ml/an_ai_based_stock_analyzer_using_llm_and_langchain/) , 2023-08-10-0910
```
https://preview.redd.it/wcd4cprfn0hb1.png?width=1005&format=png&auto=webp&s=71f2a348f963a7a262b1c8a42386e2129280fad7

An
 interesting application of Language Models and Langchain in the Finance Domain 📈-

Sharing a fun weekend project that I
 recently completed: the 'Stock Analyzer Bot'. As an investment enthusiastic person without extensive knowledge in the f
inance domain, I often end up referring to some finance youtuber's videos or a site on the internet for the fundamental 
analysis of stocks.  To assist in such situations, I developed a stock analyzer bot based on LLM, which gathers up-to-da
te information about stock such as 1) stock price, 2) Company financials 3) Recent company-related news. The bot then co
nsiders all this information to conduct analysis using language models.   You can even get positives and negatives about
 the company's financials, which will certainly help when making an investment decision.

You can ask queries like- 'Is 
it a good time to invest in Yes Bank?' or 'How are the current financials of reliance industries looking' and boom withi
n a minute you are presented with a comprehensive financial analysis based on recent data. Of course, It is not recommen
ded to rely fully on the analysis provided by the bot. It seems like a good starting point. And yeah, I agree the possib
ilities are endless with LLMs🚀.

GIthub- [https://github.com/Pranav082001/stock-analyzer-bot](https://github.com/Pranav0
82001/stock-analyzer-bot)  
Blog [An AI based stock analyzer using LLM and Langchain 📈 | by Pranav Kushare | Aug, 2023 |
 Medium](https://medium.com/p/7f8a62cbcaaa)
```
---

     
 
all -  [ An AI based stock analyzer using LLM and Langchain📈 ](https://www.reddit.com/r/ChatGPTCoding/comments/15m5286/an_ai_based_stock_analyzer_using_llm_and_langchain/) , 2023-08-10-0910
```
https://preview.redd.it/w9b2iusmn0hb1.png?width=1005&format=png&auto=webp&s=b59fbade8b0826f0575eb5d66cea9efa2889bb2d

An
 interesting application of Language Models and Langchain in the Finance Domain 📈-

Sharing a fun weekend project that I
 recently completed: the 'Stock Analyzer Bot'. As an investment enthusiastic person without extensive knowledge in the f
inance domain, I often end up referring to some finance youtuber's videos or a site on the internet for the fundamental 
analysis of stocks.  To assist in such situations, I developed a stock analyzer bot based on LLM, which gathers up-to-da
te information about stock such as 1) stock price, 2) Company financials 3) Recent company-related news. The bot then co
nsiders all this information to conduct analysis using language models.   You can even get positives and negatives about
 the company's financials, which will certainly help when making an investment decision.

You can ask queries like- 'Is 
it a good time to invest in Yes Bank?' or 'How are the current financials of reliance industries looking' and boom withi
n a minute you are presented with a comprehensive financial analysis based on recent data. Of course, It is not recommen
ded to rely fully on the analysis provided by the bot. It seems like a good starting point. And yeah, I agree the possib
ilities are endless with LLMs🚀.

GIthub- [https://github.com/Pranav082001/stock-analyzer-bot](https://github.com/Pranav0
82001/stock-analyzer-bot)  
Blog [An AI based stock analyzer using LLM and Langchain 📈 | by Pranav Kushare | Aug, 2023 |
 Medium](https://medium.com/p/7f8a62cbcaaa)
```
---

     
 
all -  [ pydantic decreases GPT performance ](https://www.reddit.com/r/LangChain/comments/15lyrw4/pydantic_decreases_gpt_performance/) , 2023-08-10-0910
```
I am using pydantic as an output parser however it significantly decreases the model performance. Is there another way t
o parse the results? I was thinking of first making a call without pydantic and then make a second call to parse the dat
a from there. Did anyone try this? 
```
---

     
 
all -  [ Best AI for local docs? ](https://www.reddit.com/r/LangChain/comments/15lxjo1/best_ai_for_local_docs/) , 2023-08-10-0910
```
Hello,

I was wondering what is currently the best AI to use for local docs on my computer?  I tried GPT4all and a coupl
e of it's LLM but I don't think it's that good so far, maybe because I did not train it yet?  I am trying to use it agai
nst some Word docs, PDFs, and excel currently.  Just simply stuff like identifying how many customers I have in an excel
 or how many time a particular word comes up in a word doc.
```
---

     
 
all -  [ Tools for programming AI agents with block diagrams ](https://www.reddit.com/r/LangChain/comments/15lwrnz/tools_for_programming_ai_agents_with_block/) , 2023-08-10-0910
```
I have a bunch of functions and various serial calls to GPT. Is there a tool for creating blocks and connecting them and
 each block I write my own python code?
```
---

     
 
all -  [ Flask API not running on App Engine ](https://www.reddit.com/r/googlecloud/comments/15lvk7s/flask_api_not_running_on_app_engine/) , 2023-08-10-0910
```
I wrote a flask API, which basically takes in a prompt runs it through langchain and returns its response. The idea is t
o build a basic chat interface.

Below is my flask app (main.py):

    # imports - application based
    from flask impo
rt Flask
    from flask_restful import Resource, Api, reqparse
    from flask_cors import CORS
    import os
    import 
dotenv
    
    # imports - application functionality based
    *** Langchain based imports ***
    
    # Initializing 
flask app and api
    app = Flask(__name__)
    api = Api(app=app)
    CORS(
        app=app,
        origins='*',
     
   methods=['POST'],
        allow_headers=['Content-Type', 'Authorization'],
    )
    
    
    # Loading environment 
variables
    dotenv.load_dotenv()
    
    
    # Endpoint for accessing the llm
    class LLMApi(Resource):
        **
* Langchain Related code here ***
    
        def post(self):
            parser = reqparse.RequestParser()
           
 parser.add_argument('messages', required=True, type=str)
            args = parser.parse_args()
            prompt = ar
gs['messages']
    
            if prompt is None:
                return {'error': 'No prompt provided'}, 400
    
    
        # Process the prompt using Langchain and query the database
            result = self.agent_chain.run(prompt)
  
          # Return the response in the desired format
            response = {'choices': [{'message': {'role': 'assistan
t', 'content': result}}]}
    
            return response, 200
    
    
    api.add_resource(LLMApi, '/llm-api')
    

    if __name__ == '__main__':
        app.run(debug=True)
    

The API works perfectly fine when running locally, howe
ver, when I deploy it to \`Google App Engine\` and test the API using insomnia I get this error:  


[Error thrown by Ap
p Engine Endpoint](https://preview.redd.it/8m75k81eiygb1.png?width=804&format=png&auto=webp&s=6bc814d1ee701e0f8e4099edcc
fcb08793a880ae)

I'm deploying using `gcloud app deploy app.yaml --project=truliv-ai`

My app.yaml file:

    runtime: p
ython311
    handlers:
    - url: /.*
      script: main.app

Would appreciate some help here. thank you.
```
---

     
 
all -  [ What is your favorite feature in LangChain ](https://www.reddit.com/r/LangChain/comments/15lvdor/what_is_your_favorite_feature_in_langchain/) , 2023-08-10-0910
```
We are working on an open source project which relies heavily on LangChain for code generation & software design through
 LLMs. We are early in our progress, and haven't included many LangChain features yet. For example, the internet search 
is something that we want to add to our code in future releases. I really like to know what features you like the most s
o that we can integrate those.

This is our project in case you are interested. I would truly appreciate any feedback an
d suggestion.

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-S
ynthesizer) 
```
---

     
 
all -  [ step by step software design and code generation through GPT ](https://www.reddit.com/r/ChatGPT/comments/15lswmt/step_by_step_software_design_and_code_generation/) , 2023-08-10-0910
```
If you have used ChatGPT, or GPT in general, for software design and code generation, you might have noticed that for la
rger or trickier codes, it skips a lot of the implementation or misunderstands the design. That's where tools like GPT E
ngineer and Aider come to help. However those tools for the most part keep the user out of the loop during the design. T
o explore the design space with GPT and be involved in decision making, you can use GPT-Synthesizer. GPT-synthesizer is 
a free and open-source tool which you can use for personal or commercial purposes. It uses LangChain to efficiently proc
ess larger codebases: [https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologie
s/GPT-Synthesizer) .
```
---

     
 
all -  [ GPT Synthesizer: Software generation using LangChain and the power of LLMs ](https://www.reddit.com/r/LangChain/comments/15lsh2i/gpt_synthesizer_software_generation_using/) , 2023-08-10-0910
```
As oppose to GPT Engineer or Aider, GPT Synthesizer utilizes LangChain to explore the design space with user through a c
arefully moderated interview.

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTe
chnologies/GPT-Synthesizer)

&#x200B;
```
---

     
 
all -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-10-0910
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
all -  [ Chat with your data using Langchain, PineconeDB and Airbyte ](https://www.reddit.com/r/ArtificialInteligence/comments/15lkx5v/chat_with_your_data_using_langchain_pineconedb/) , 2023-08-10-0910
```
A few of our team members at Airbyte (and Joe, who killed it!) recently played with building our own internal support AI
 chat bot, using Airbyte, Langchain, Pinecone and OpenAI, that would answer any questions we ask when developing a new c
onnector on Airbyte. 

As we prototyped it, we realized that it could be applied for many other use cases and sources of
 data, so… we created [a tutorial](http://airbyte.com/tutorials/chat-with-your-data-using-openai-pinecone-airbyte-and-la
ngchain) that other community members can leverage and the [Github repo](https://github.com/airbytehq/tutorial-connector
-dev-bot) to run it .

The tutorial shows: 

* How to extract unstructured data from a variety of sources using Airbyte 
Open Source
* How to load data into a vector database (here Pinecone), preparing the data for LLM usage along the way
* 
How to integrate a vector database into ChatGPT to ask questions about your proprietary data

I hope some of it is usefu
l, and would love your feedback!  

```
---

     
 
all -  [ Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/LangChain/comments/15lkjl6/rust_meets_llama2_openai_compatible_api_written/) , 2023-08-10-0910
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to Nvidia GPU and Metal acceleration for GGML models thanks to the fantastic \`llm\` crate! You 
can use it with the OpenAI integration (see the Python folder in GitHub project) 

Here is the project link: [Cria- Loca
l LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Lang
chain\` example in the project).

Really interested in your feedback and I would welcome any contributions :) !

&#x200B
;
```
---

     
 
all -  [ Custom LLM service using LangChain ](https://www.reddit.com/r/datascience/comments/15lji9i/custom_llm_service_using_langchain/) , 2023-08-10-0910
```
Hi all,

For a project, I am looking to build a custom LLM from a knowledge base by a governmental institution. I know t
his can be done using Langchain + VectorStore but I was wondering whether there might already be a SaaS solution for thi
s task.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Tuning vs using langchain/llama index for retrieving structured data from unstructured data ](https://www.reddit.com/r/LangChain/comments/15li8df/tuning_vs_using_langchainllama_index_for/) , 2023-08-10-0910
```
I have a big dataset that makes use of a single document to retrieve some information into a single row of the table, th
e document can JPEG or PNG, the work was being done manually by entering the data, I'm trying to automate this process, 
I used OCR models mainly from aws (Textract) to get text document and built a prompt that defines the fields and builds 
a JSON based on the text. The thing is I want to improve the performance with tuning llama2 or gpt(I think starting from
 january next year will be supported) into my data, or use langchain or llamaindex to pass the table and documents as co
ntext, which I think will be some sort of few shot learning, which of these approaches is better for my case?
```
---

     
 
all -  [ Peter - Buildfast Masterclass - Learn to build your own AI chatbot ](https://www.reddit.com/r/MakesYouMoney/comments/15lhx7h/peter_buildfast_masterclass_learn_to_build_your/) , 2023-08-10-0910
```
Get the course here: [https://bit.ly/Peter-Buildfast\_Masterclass](https://bit.ly/Peter-Buildfast_Masterclass)

[https:/
/bit.ly/Peter-Buildfast\_Masterclass](https://bit.ly/Peter-Buildfast_Masterclass)

[ ](https://preview.redd.it/wcgw14o40
p7b1.jpg?width=1280&format=pjpg&auto=webp&s=404eee6c4d63d0176e118d586148aba90726b3b0)

# Here are all of the videos insi
de Fundamentals That you get instant access to upon joining BuildFast

1. LLMs: Overview, using LLMs in Langchain, open-
sourced LLMs, chat model, embedding text.
2. Chains: Chains 101, LLM Chain, Sequential Chain, and four other important L
angchain chains.
3. Prompt: Prompts 101, Example Prompts, Output Parser.
4. Memory: 4 Memory Types Explained, How to use
 Memory in a Chain, How to add Memory to an Agent
5. Document Loaders: Document Loaders 101, When to use Document Loader
, Import data from Text & CSV, and Loading data from Discord, Notion, Telegram
6. Indexes: Indexes 101, Retrievers and T
ext Splitters.
7. Vector Database & Embeddings: Vector databases 101, when to use vector databases, Embeddings and vecto
r database use-cases.
```
---

     
 
all -  [ Teaching Llama to reason in another language help! ](https://www.reddit.com/r/LocalLLaMA/comments/15lgoo7/teaching_llama_to_reason_in_another_language_help/) , 2023-08-10-0910
```
Hi r/LocalLLaMA, 

&#x200B;

I have been tinkering with Ooba and API calls for a while now, and have hit a bit of a wall
.   


My use case is corporate and not too out there: given transcripts of business calls, I should be able to answer q
uestions and deliver summaries of the conversation. All easy with Langchain and vector databases, and iterative summariz
ation.

My only issue is that this is all happening in Brazilian Portuguese. OpenAI models all have a similar level of i
ntelligence and coherence in non-English languages, but Llama seems to fail miserably at this.   


There was an attempt
 to teach LLama 1 Portuguese: [https://github.com/22-hours/cabrita](https://github.com/22-hours/cabrita) , and so I used
 the same dataset on Llama2-13B-chat to update the project, but like some of you have been experiencing, the model goes 
off its rocker after around 100 tokens, doesn't know when to stop, often lapses into English while still being correct, 
etc.  


Do any of you have experience teaching an LLM a different language? I have read that this happens mainly at fou
ndational training, and that LoRAs can't really imbue the model with reasoning skills in a new language. I was thinking 
of some possible options:  


* Use a larger dataset which successfully created a good finetune (e.g. Vicuna) and transl
ate it to PT-BR using ChatGPT (expensive). 
* Transcribe all calls in Portuguese and English, and do all prompts and rea
soning in English, only translating to Portuguese at the end.

&#x200B;

I really appreciate any answers of further poin
ts you may have, as I've trained maybe 10-20 LoRAs at this point with no real improvement.

&#x200B;

P.S. : After how m
any steps do you usually stop LoRA finetuning? I seem to consistently get negligible loss improvements after around 100,
 and my runs that went far beyond that and probably overfitted only output a bunch of newlines regardless of the prompt.

```
---

     
 
all -  [ ChatBot - dialogue phases ](https://www.reddit.com/r/LangChain/comments/15lenge/chatbot_dialogue_phases/) , 2023-08-10-0910
```
What are the best options of creating a chatbot for a mental health app such that the dialogue with a user should be div
ided into 3 phases: 1 for identifying the issue, one for suggesting a technique, and another for follow-up and general c
onversation?
```
---

     
 
all -  [ Holiday Planning AI Agents ](https://fetch.ai/content-hub/article/holiday-integrations-walkthrough) , 2023-08-10-0910
```

At the end of July, we announced amazing integrations that empower developers to deploy Holiday Planning AI Agents 🤖

C
ombining OpenAI's LLMs, LangChain's Agent Search, and Skyscanner's Flight Offers through RapidAPI, you can find all of y
our travel suggestions curated easily ✈️

We now have a full walkthrough for developers on how to start using these inte
grations now 🔥

Read our recent blog post to learn more 👇
https://fetch.ai/content-hub/article/holiday-integrations-walk
through

Earlier this week, we released the newly announced Agent Name Service (ANS) for Agentverse.ai! 🤖

ANS makes it 
possible for #AI Agents to register names & communicate with ease. It also massively improves Agent searchability 🔍

Try
 out ANS with the tutorial below 👇
https://youtu.be/HiWxVahNXLg
```
---

     
 
all -  [ LangChain available in 13.1 LTS and above ](https://www.reddit.com/r/databricks/comments/15lbnf6/langchain_available_in_131_lts_and_above/) , 2023-08-10-0910
```
LangChain is available as an experimental MLflow flavor which allows LangChain customers to leverage the robust tools an
d experiment tracking capabilities of MLflow directly from the Databricks environment.

LangChain is a software framewor
k designed to help create applications that utilize large language models (LLMs) and combine them with external data to 
bring more training context for LLMs.

Databricks Runtime for Machine Learning includes langchain in Databricks Runtime 
13.1 ML and above.
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-10-0910
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [D] Having trouble with RAG on company domain data ](https://www.reddit.com/r/MachineLearning/comments/15br11c/d_having_trouble_with_rag_on_company_domain_data/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [D] How do I reduce LLM inferencing time? ](https://www.reddit.com/r/MachineLearning/comments/15851sr/d_how_do_i_reduce_llm_inferencing_time/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [P] TruLens-Eval is an open source project for eval & tracking LLM experiments. ](https://www.reddit.com/r/MachineLearning/comments/1542fbt/p_trulenseval_is_an_open_source_project_for_eval/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ Alternativ to langchain [D] ](https://www.reddit.com/r/MachineLearning/comments/15175na/alternativ_to_langchain_d/) , 2023-08-10-0910
```
Im currently learning hiw to use langchain but i heard that its bad so i want to know what are som alternatives i need m
emory and agents so that it can search online run code and so on so what is the best alternativ or is langchain the best
 option
```
---

     
 
MachineLearning -  [ '[N]' '[D]' Langchain? What is it?? ](https://www.reddit.com/r/MachineLearning/comments/150mzax/n_d_langchain_what_is_it/) , 2023-08-10-0910
```
want to know more about Langchain  
Check out [https://nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf](https:
//nikhilpentapalli.substack.com/p/langchain-in-detail?sd=pf)
```
---

     
 
MachineLearning -  [ [D] The Problem With LangChain ](https://www.reddit.com/r/MachineLearning/comments/14zlaz6/d_the_problem_with_langchain/) , 2023-08-10-0910
```
https://minimaxir.com/2023/07/langchain-problem/

tl;dr it's needlessly complex, and I provide code examples to demonstr
ate such.

A few weeks ago when I posted about creating a LangChain alternative to /r/MachineLearning, most of the comme
nts replied 'what exactly is the issue with LangChain', so I hope this provides more clarity!
```
---

     
 
MachineLearning -  [ [D] 📚 The Learning Corner (Andrew NG Free Ai Courses Pt. 1) ](https://www.reddit.com/r/MachineLearning/comments/14xww89/d_the_learning_corner_andrew_ng_free_ai_courses/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [P] langchain-lite alternative ](https://www.reddit.com/r/MachineLearning/comments/14xf9xb/p_langchainlite_alternative/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [D] What have been your use cases for LLM autonomous agents? ](https://www.reddit.com/r/MachineLearning/comments/14w817y/d_what_have_been_your_use_cases_for_llm/) , 2023-08-10-0910
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

     
 
MachineLearning -  [ [D] Hacking LangChain for Fun and Profit ](https://www.reddit.com/r/MachineLearning/comments/14w0ht7/d_hacking_langchain_for_fun_and_profit/) , 2023-08-10-0910
```
[https://blog.kevinhu.me/2023/07/10/hacking-langchain-for-fun-and-profit/](https://blog.kevinhu.me/2023/07/10/hacking-la
ngchain-for-fun-and-profit/)

I'm starting a series of blogs to delve into LangChain. Hope this helps anyone who's inter
ested in LLM and building with LangChain.
```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-10-0910
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
