 
all -  [ What are other LLM's with executable API? ](https://www.reddit.com/r/LangChain/comments/16h6zmm/what_are_other_llms_with_executable_api/) , 2023-09-13-0909
```
One thing I like about GPT models is that I don't need to maintain or own a heavy infrastructure to run the model. I can
 make a call to their API and have the embeddings and inferences done. What other similar LLM's I can use where I can ma
ke an API call and get the outcomes rather than downloading huge models and maintaining on local infra?
```
---

     
 
all -  [ Build an AI SMS Chatbot with Replicate, LLaMA 2, and LangChain ](https://dev.to/twilio/build-an-ai-sms-chatbot-with-replicate-llama-2-and-langchain-3i72) , 2023-09-13-0909
```

```
---

     
 
all -  [ What ancillary services are you paying for? ](https://www.reddit.com/r/LangChain/comments/16h4vvp/what_ancillary_services_are_you_paying_for/) , 2023-09-13-0909
```
i.e. serpapi etc

And what benefit are you getting from it / what are you using it for
```
---

     
 
all -  [ Is there a way to dynamically use grammar ](https://www.reddit.com/r/Langchaindev/comments/16h4gqn/is_there_a_way_to_dynamically_use_grammar/) , 2023-09-13-0909
```
My code is below. I want to initialize the model without the grammar parameters. However, when I ask for a detailed step
 by step plan I would like that returned as a list. What is the best way to do this without having to create a new insta
nce of llamacpp?   



```
import os
import sys
import argparse
from langchain.llms import LlamaCpp
import chromadb
impo
rt json
import uuid
import re
import datetime
from langchain.chains import LLMChain
from langchain.memory import Convers
ationBufferMemory
from langchain.prompts import PromptTemplate

# Load the configuration values from the JSON file
with 
open('model_config.json', 'r') as config_file:
    config = json.load(config_file)

class TemporaryNetworkError(Exceptio
n):
    def __init__(self, message='A temporary network error occurred'):
        super().__init__(message)

class Chrom
aVectorStore:
    def __init__(self, collection_name='chroma_collection'):
        # Get the current date and time
     
   current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
   
     collection_name_time = f'{formatted_datetime}_{collection_name}'

        self.chroma_client = chromadb.Client()
  
      self.chroma_client = chromadb.PersistentClient(path='./')
        self.collection = self.chroma_client.create_coll
ection(name=collection_name_time)

    def store(self, result):
        unique_id = str(uuid.uuid4())  # Generate a uniq
ue ID for the result
        # Convert result to string if it's not already
        print(type(result))
        print(re
sult)
        result_str = str(result) if not isinstance(result, str) else result
        self.collection.add(documents=
[result], ids=[unique_id])

class AutonomousAgent:
    def __init__(self, prompt_path, model_path):
        self.prompt_
path = prompt_path
        self.model_path = model_path
        self.plan = []
        self.results = []
        self.pr
ompt = ''
        self.llama = LlamaCpp(
            model_path=args.model_path,
            n_gpu_layers=config['n_gpu_
layers'],
            n_batch=config['n_batch'],
            n_threads=config['n_threads'],
            f16_kv=config['f
16_kv'],
            n_ctx=config['n_ctx'],
            max_tokens=config['max_tokens'],
            temperature=config[
'temperature'],
            verbose=config['verbose'],
            use_mlock=config['use_mlock'],
            echo=True

        )
        self.chroma_vector_store = ChromaVectorStore()

    def extract_steps(self, text):
        # Remove co
ntent between ``` ```
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)

        pattern = r'(\d+)\.\s(.*?)
(?=\d+\.|$)'
        matches = re.findall(pattern, text, re.DOTALL)
        steps_with_numbers = [(int(match[0]), match[
1].strip()) for match in matches if match[1].strip() != '']
        steps_with_numbers.sort(key=lambda x: x[0])
        
steps = [step[1] for step in steps_with_numbers]
        return steps

    def fetch_prompt(self):
        with open(sel
f.prompt_path, 'r') as file:
            self.prompt = file.read()

    def get_plan(self):
        prompt = f'''Give a 
detailed step by step plan to complete the following task. Do not include any programming code in your response. Do not 
include examples. You must return a numbered list interperable by Python. The format for a numbered list is 1. Step 1 2.
 Step 2 3. This is a more detailed step.

            {self.prompt}
            '''
        result = self.llama(prompt)

        self.plan = self.extract_steps(result)
        print('The plan is: ' + ', '.join(self.plan))

    def execute_pl
an(self):
        for step in self.plan:
            retry_count = 0
            while retry_count < 3:
                
try:
                    result = self.llama(step)
                    self.results.append((step, result))
             
       self.chroma_vector_store.store(result)
                    break
                except TemporaryNetworkError:
  
                  retry_count += 1
                    if retry_count == 3:
                        sys.exit(1)

    def
 archive_results(self):
        if not os.path.exists('output'):
            os.makedirs('output')
        current_datet
ime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
        filename = 
f'output/{formatted_datetime}_results.txt'

        with open(filename, 'w') as file:
            for step, result in se
lf.results:
                file.write(f'Query: {step}\nResult: {result}\n\n')

if __name__ == '__main__':
    parser = 
argparse.ArgumentParser(description='Autonomous agent that executes a plan based on a prompt.')
    parser.add_argument(
'--prompt_path', type=str, default='prompt.md', help='Path to the prompt file.')
    parser.add_argument('--model_path',
 type=str, required=True, help='Path to the language model file.')
    args = parser.parse_args()

    agent = Autonomou
sAgent(args.prompt_path, args.model_path)
    agent.fetch_prompt()
    agent.get_plan()
    agent.execute_plan()
    age
nt.archive_results()
```
```
---

     
 
all -  [ Langchain and embeddings: Attribution ](https://www.reddit.com/r/LangChain/comments/16h1f9y/langchain_and_embeddings_attribution/) , 2023-09-13-0909
```
Hi,
I'm using langchain, embeddings and the openai API to 'talk to my pdf documents'. When I want to verify the response
 I must open the pdf manually and use the search function. How can I generate source attributions like. Document 'xy.pdf
', Page 24, Line 3.
Is there a 'out of the box' solution or do I need to implement it by myself?
```
---

     
 
all -  [ LangChain and GPT Tokens ](https://www.reddit.com/r/LangChain/comments/16h0x6a/langchain_and_gpt_tokens/) , 2023-09-13-0909
```
I was planning on using LangChain in a recent project. Basically, I have hundreds of documents worth of text from a text
book, and I wanted to create a 'chatbot' which could return information to questions which could be found in the textboo
k. However, I realized that OpenAI doesn't offer free credits for the API anymore, so I was wondering: how many tokens w
ill it take to do all of this? Will all of the pages of the textbook count as tokens in the prompt, or will only the que
stion I ask count? I don't want to run it once and accidentally waste like 50 dollars worth of tokens.
```
---

     
 
all -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-13-0909
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
all -  [ Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with Tool U ](https://www.reddit.com/r/LocalLLaMA/comments/16gxlor/kani_a_lightweight_highly_hackable_opensource/) , 2023-09-13-0909
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function` decorator) to turn any function into an AI-callable function!

Kani works with any model and has 
built-in tools for HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt engineering
 under the hood and doesn't require learning complex library tools---all defaults are minimal and highly customizable.


Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab.research.
google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/github/zhud
otexe/kani/blob/main/examples/colab_examples.ipynb)

If you're interested in learning more check out our links below!  

Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zhudotexe/kani
](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
all -  [ Using LangChain and GPT in robotic projects ](https://www.reddit.com/r/LangChain/comments/16gx6wj/using_langchain_and_gpt_in_robotic_projects/) , 2023-09-13-0909
```
We are using LangChain and GPT3.5 to generate a ROS (Robot Operating System) framework for robotic projects:

[https://g
ithub.com/RoboCoachTechnologies/ROScribe](https://github.com/RoboCoachTechnologies/ROScribe)

This is a special-domain c
ode generation software. Earlier we published GPT-synthesizer as a general-domain code-generation tool:

[https://github
.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer)

We are a robotic 
company and ROScribe will be our main product. We have a lot of plans on how to expand on it. I hope these softwares pro
ve useful to you. We would love to hear your feedback and have you as a contributor on our projects.
```
---

     
 
all -  [ The fine-tuned model is not getting better ](https://www.reddit.com/r/LangChain/comments/16gwgr5/the_finetuned_model_is_not_getting_better/) , 2023-09-13-0909
```
I've fine-tuned the model and I'm using it with Langchain SQL Agent to respond to SQL queries. However, I've noticed tha
t the results I'm getting are identical to those from the untrained GPT-3.5 model. To provide some context, we have appr
oximately 20 tables, and I've trained the fine-tuned model using around 50 examples so far. Below is the code I've imple
mented for the SQL agent. Could you please review it and let me know if there are any issues? Even when I pose questions
 based on the examples I've used for training, the responses appear to be incorrect. Is there something crucial that I m
ight be overlooking? I'm considering adding a few hundred more examples to the training set, but is there anything else 
I should be doing to improve the performance of the model?

&#x200B;

    finetuned_llm = ChatOpenAI(temperature=0, mode
l_name='ft:gpt-3.5-turbo-0613:xxxxx::xxxx')
    
    agent_executor = create_sql_agent(
        llm=ChatOpenAI(temperatu
re=0, model_name='gpt-3.5-turbo-0613'),
        toolkit=SQLDatabaseToolkit(db=db, llm=finetuned_llm),
        verbose=Tr
ue,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        top_k=5
    )

I have built the finetuned model fo
llowing this document - [https://medium.com/dataherald/fine-tuning-gpt-3-5-turbo-for-natural-language-to-sql-4445c1d37f7
c](https://medium.com/dataherald/fine-tuning-gpt-3-5-turbo-for-natural-language-to-sql-4445c1d37f7c) 
```
---

     
 
all -  [ The fine-tuned model is not getting better ](https://www.reddit.com/r/ChatGPTCoding/comments/16gwern/the_finetuned_model_is_not_getting_better/) , 2023-09-13-0909
```
I've fine-tuned the GPT3.5 model and I'm using it with Langchain SQL Agent to respond to SQL queries. However, I've noti
ced that the results I'm getting are identical to those from the untrained GPT-3.5 model. To provide some context, we ha
ve approximately 20 tables, and I've trained the fine-tuned model using around 50 examples so far. Below is the code I'v
e implemented for the SQL agent. Could you please review it and let me know if there are any issues? Even when I pose qu
estions based on the examples I've used for training, the responses appear to be incorrect. Is there something crucial t
hat I might be overlooking? I'm considering adding a few hundred more examples to the training set, but is there anythin
g else I should be doing to improve the performance of the model?

&#x200B;

    finetuned_llm = ChatOpenAI(temperature=
0, model_name='ft:gpt-3.5-turbo-0613:xxxxx::xxxx')
    
    agent_executor = create_sql_agent(
        llm=ChatOpenAI(te
mperature=0, model_name='gpt-3.5-turbo-0613'),
        toolkit=SQLDatabaseToolkit(db=db, llm=finetuned_llm),
        ver
bose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        top_k=5
    )

&#x200B;

&#x200B;
```
---

     
 
all -  [ Discrepancy in outputs from chat.openai.com v/s via the langchain API ](https://www.reddit.com/r/ChatGPTCoding/comments/16guxui/discrepancy_in_outputs_from_chatopenaicom_vs_via/) , 2023-09-13-0909
```
I notice that the same prompt gives me fantastic results on https://chat.openai.com, and does not on `gpt-3.5-turbo-16k`
 via langchain + python. I've reduced the variables as much as I can. Does the chat console use a better model underneat
h or something?

This is roughly my code:
    
    
    llm = ChatOpenAI(
    openai_api_key=xyz,
    temperature=0.5,
 
   model_name='gpt-3.5-turbo-16k',
    streaming=True,
    cache=True,
    )    
    
     create_structured_output_chai
n(
        llm=llm,
        memory=memory,
        prompt=prompt,
        output_schema=some_pydantic_schema,
        ve
rbose=True,
    )

I set verbose to true, so langchain prints the entire prompt to console and then I can take that to t
he openai.chat.com console which gives much better results.
```
---

     
 
all -  [ Creating a RAG-System that references the name of a document where the information is from (like Bin ](https://www.reddit.com/r/LangChain/comments/16gujc5/creating_a_ragsystem_that_references_the_name_of/) , 2023-09-13-0909
```
Hey Community,

i was wondering how to create a RAG-System where the LLM can provide the Name of the Document it retriev
ed the information from. I cannot find good resources regarding this topic.  


Thanks in advance!
```
---

     
 
all -  [ I made a secure GPT-4 for my company knowledge base. ](https://www.reddit.com/r/Entrepreneur/comments/16gnmaw/i_made_a_secure_gpt4_for_my_company_knowledge_base/) , 2023-09-13-0909
```
Almost no companies integrate chat GPT with their sensitive data for obvious reasons. The OpenAI API compromises securit
y.  
  
However, Morgan Stanley just launched a GPT-4 of their entire knowledge base for every employee a few months a
go.  
  
But they really have something to hide, I thought. So there must be a secure way to do this!  
  
That thou
ght got me spending a few days in the OpenAI security rabbit hole.  
  
Turns out there is a solution - all you have t
o do is use Azure OpenAI instead of the plain old OpenAI API. Then you top it with LangChain and you have a pretty badas
s AI assistant for every single team member.  
  
You pretty much just talk to your company's SOPs, product specificat
ions, or any other structured/unstructured data.  
  
A huge time saver top-down. Senior empolyees don't get the same 
annoying questions over and over again, and the juniors get to ask the bot literally anything and anytime.  
  
So now
 I'm rolling out a project that does just this for companies (securely integrating GPT-4 for your knowledge base), and I
'm willing to do a few companies from r/EntrepreneurRideAlong for free, just to collect the case studies. Comment and le
t's collab!
```
---

     
 
all -  [ I made a secure GPT-4 for my company knowledge base. ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/16gnjs8/i_made_a_secure_gpt4_for_my_company_knowledge_base/) , 2023-09-13-0909
```
Almost no companies integrate chat GPT with their sensitive data for obvious reasons. The OpenAI API compromises securit
y.

However, Morgan Stanley just launched a GPT-4 of their entire knowledge base for every employee a few months ago. 


But they really have something to hide, I thought. So there must be a secure way to do this!

That thought got me spendi
ng a few days in the OpenAI security rabbit hole.

Turns out there is a solution - all you have to do is use Azure OpenA
I instead of the plain old OpenAI API. Then you top it with LangChain and you have a pretty badass AI assistant for ever
y single team member.

You pretty much just talk to your company's SOPs, product specifications, or any other structured
/unstructured data. 

A huge time saver top-down. Senior empolyees don't get the same annoying questions over and over a
gain, and the juniors get to ask the bot literally anything and anytime.

So now I'm rolling out a project that does jus
t this for companies (securely integrating GPT-4 for your knowledge base), and I'm willing to do a few companies from r/
EntrepreneurRideAlong for free, just to collect the case studies. Comment and let's collab!
```
---

     
 
all -  [ Best LLM ](https://www.reddit.com/r/LangChain/comments/16gnidn/best_llm/) , 2023-09-13-0909
```
What is the best LLM other than GPT that is free to use? Like i want good performance for GTX 1650 and 8gb ram with i5 1
1th gen
```
---

     
 
all -  [ AzureChatOpenAI System-User-assistant input ](https://www.reddit.com/r/LangChain/comments/16gmr7a/azurechatopenai_systemuserassistant_input/) , 2023-09-13-0909
```
If I use the openai platform or use official API, i can set system user assistant message. But how can i do this in Azur
eChatOpenAI in langchain. The reason i want to use AzureChatOpenAI is because of retry implementation
```
---

     
 
all -  [ Langchain + Azure Formrecognizer: How to pass documents into agent.run()? ](https://www.reddit.com/r/Langchaindev/comments/16gl6fh/langchain_azure_formrecognizer_how_to_pass/) , 2023-09-13-0909
```

I am following a tutorial that says you should call it like this:

‘agent.run('what is the due date of the following in
voice?' 'data/Sample-Invoice-printable.png')‘

But I cannot get it to run on a local file. There is an error message tha
t the resource cannot be found.

In addition: What kind of formatting is it in the example with the two arguments not se
parated by a comma? I am confused.
```
---

     
 
all -  [ Loading a web page and returning structured output ](https://www.reddit.com/r/LangChain/comments/16gkhf4/loading_a_web_page_and_returning_structured_output/) , 2023-09-13-0909
```
I am interested to know how you all would tackle the following use case:

I want to load a url of a page that contains a
 recipe for a meal. I use the CheerioWebLoader for this in combination with the html-to-text package. I then obtain the 
document for this page, which I then divide into chunks. 

This is the part where it gets a but confusing for me. Ultima
tely I want to obtain an object from these chunks that has properties such as recipe title, preparation time, ingredient
s, etc. But I do not fully understand how I can connect Langchain's structured output parser to these chunks. 

What I w
ould do now is run a number of chat queries (such as 'What is the title of this recipe?') on these chunks and then push 
the results of these queries into an array of strings. Eventually I'll get a properly shaped response object back, but t
his is a slow process and it might take up to a minute to take a response back.

I was wondering if there is a better or
 quicker strategy to obtain structured output from a large document, such as a website.
```
---

     
 
all -  [ Best open source FUNCTION CALLING solution? ](https://www.reddit.com/r/LargeLanguageModels/comments/16gjj4x/best_open_source_function_calling_solution/) , 2023-09-13-0909
```
I love the OpenAI's function calling/arg parsing solution but I am trying to use local model. I know we can use FastChat
+Langchain to mimic it but it is very very very bad (vicuna-13b-v1.5-16k). 

my question is: any suggested model fine tu
ned for this purpose? is a bigger model will performs better? thanks
```
---

     
 
all -  [ Is langchain messing up my gpt 3.5 output? ](https://www.reddit.com/r/LangChain/comments/16ggg13/is_langchain_messing_up_my_gpt_35_output/) , 2023-09-13-0909
```
I notice that the same prompt gives me fantastic results on https://chat.openai.com, and does not on `gpt-3.5-turbo-16k`
 via langchain + python. I've reduced the variables as much as I can. Or does the chat console use a better model undern
eath or something?
```
---

     
 
all -  [ Can you use an agent in a Router Chain? ](https://www.reddit.com/r/LangChain/comments/16g9pme/can_you_use_an_agent_in_a_router_chain/) , 2023-09-13-0909
```
I'm trying to use an an agent in a router chain for a chatbot I'm developing. looking at the logs it looks like the rout
er selects the agent and passes it everything properly and the agent runs just fine. But at the parse step it fails beca
use there's no key 'text', which makes no sense to me. Any advice? Has anyone been able to do this successfully? 
```
---

     
 
all -  [ What are the hard and technical skills you need to be a Machine Learning/ Data Scientist ](https://www.reddit.com/r/PinoyProgrammer/comments/16g2cnn/what_are_the_hard_and_technical_skills_you_need/) , 2023-09-13-0909
```
# [Context]

May naka sticky na thread which can be found here [How to Become a data scientist:](https://www.reddit.com/
r/PinoyProgrammer/comments/l8zf7v/how_to_become_a_data_scientist/)

&#x200B;

[Generated with https:\/\/hotpot.ai\/](htt
ps://preview.redd.it/vk4bhtw24onb1.png?width=256&format=png&auto=webp&s=226e9825b57afda2599f66e99318298b111792c7)

Eto y
ung mga tips nya

&#x200B;

>***educational background*** *- <blah>*  
>  
>***learn the fundamentals*** *- <blah>*  
> 
 
>***rack up relevant experience*** *- <blah>*  
>  
>***apply, apply, apply***  *- <blah>*  
>  
>*Data Science jobs f
or fresh grads are a rarity back then so I took a job as a software engineer just to rack up experience, constantly join
ing Kaggle competitions and studying about DS. Finally got a job as a Data Scientist after 2 years.*

&#x200B;

Now, I'm
 **NOT** going to dispute what he has shared, but tingin ko, medyo vague yung tips and hindi ganun ka-tangible. Unfortun
ately, OP already deleted his account so no way for him to update and add more info. In case you have a new account, pls
 message me.

So, naisip ko na dagdagan with something more tangible yung tips and advice nya. By sharing the hard and t
echnical skills, the courses, MOOCS, and links that I personally used and utilized.

# [Massive Open Online Courses (MOO
Cs)]

* [Statistics for Data Science and Business Analysis](https://www.udemy.com/course/statistics-for-data-science-and
-business-analysis/)\- costs less than Php 1000, Udemy also has regular discounts pa. One can finish the course in a few
 weeks to a few months. What is important is that you, OO IKAW, don't need to rush finishing this as this is one of the 
fundamental skills. Now if you're very good in stat, no need for this. I finished this course in a month during covid
* 
[Introduction to Computational Thinking and Data Science](https://learning.edx.org/course/course-v1:MITx+6.00.2x+3T2020)
\- I took this course in EDX, may assignments, lectures, and exams. I finished this in like 2 months during the height o
f covid. This is an official course and has a certificate from the Massachusetts Institute of Technology.
* [DeepLearnin
g.AI TensorFlow Developer Professional Certificate](https://www.coursera.org/professional-certificates/tensorflow-in-pra
ctice) \- I completed this in around 2 months during the tail-end of COVID, but I was already using Tensorflow for more 
than a year. I haven't taken the official Google certification, but this was an amazing course. Intermediate to Advanced
 knowledge of Python is a must.
* [TensorFlow: Advanced Techniques Specialization](https://www.coursera.org/specializati
ons/tensorflow-advanced-techniques)\- took this course immediately after i finished the course above, it took me around 
2 months to finish. Marami akong natutunan na bagong techniques and approaches using Tensorflow.
* [Fine Tune BERT with 
Tensorflow](https://www.coursera.org/learn/fine-tune-bert-tensorflow/)**-** **Bidirectional Encoder Representations from
 Transformers (BERT),** one of the most important libraries for Natural Language Processing, released in 2018 by Google.
 During that time, it was State of the Art (SOTA) and became the de facto standard library when working with NLP with a 
Deep Learning Library.
* [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-p
rompt-engineering-for-developers/)\- You will learn how to use a large language model (LLM) to quickly build new and pow
erful applications

# [Youtube channels]

* [STATQUEST](https://www.youtube.com/@statquest)\- this guy explains very com
plex Statistics and Data science concepts and formulas in an excellent way complete with visuals, animations, and sample
 computations. Very valuable resource to help 'bake-in' the knowledge and concepts

# [Cloud Competencies and Certs]

* 
[Microsoft Azure Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/az-900/)\- this is the entry cert 
for Azure Cloud, I started poking into Azure circa 2019, I took this cert during the height of COVID. Took me around 2 m
onths to review, personally run and setup  the GITHUB repos
   * I took a UDEMY course for the Fundamentals but unfortun
ately, wala na yung course sa Udemy. So here's a good alternative [https://www.udemy.com/course/az900-azure/](https://ww
w.udemy.com/course/az900-azure/)
* [Designing and Implementing a Data Science Solution on Azure](https://learn.microsoft
.com/en-us/certifications/exams/dp-100/)\- I took this during the height of COVID pandemic, I also downloaded the offici
al GITHUB repo of Microsoft then studied for this cert for around 2 months.

# [Website Memberships]

* [Kaggle.com](htt
ps://Kaggle.com) \- unarguably the largest data science community today, also leading the democratization of AI/ Machine
 Learning/ Deep Learning. Sign up for membership then study the notebooks (aka kernels), participate in the forums, uplo
ad and create datasets, as well as join competitions. They have a discord channel too which one can optionally join.
* [
Medium.com](https://Medium.com) \- good source of articles
* [Stackoverflow.com](https://Stackoverflow.com) \- no need f
or an explanation
* [Huggingface.co](https://Huggingface.com)\- Simple, safe way to store and distribute neural networks
 weights safely and quickly.

# [Python, Libraries, and others]

* **Python-** one of the best language for datascience,
 has lots of [libraries and ecosystem is very much alive.](https://survey.stackoverflow.co/2023/)
* [Adherence to PEP8 S
tandards](https://peps.python.org/pep-0008/)\- for writing beautiful Python code.
* [Creating python environments with c
onda](https://stackoverflow.com/questions/48174935/conda-creating-a-virtual-environment) **-** for modularity and managi
ng environments
* **SQL-** plain-ol' SQL, as long as you can write optimal SQL code, and you know how to join tables pro
perly and know when to use LEFT vs INNER vs OUTER.
   * I personally used SQL on POSTGRESQL, SQL SERVER, SNOWFLAKE, and 
DATABRICKS with minimal changes in syntax. MUST-LEARN.
* [Numpy](https://numpy.org/) **-** you have to get comfortable w
orking with numbers
* [Scikit-Learn](https://scikit-learn.org/) **-** scikit-learn is a free software machine learning l
ibrary for the Python programming language. It features various classification, regression and clustering algorithms
* [
Pandas](https://pandas.pydata.org/) \- you need to become very competent when massaging and aggregating data
   * [Aggre
gations](https://stackoverflow.com/a/43173207/1465073)\- bread and butter mo
* [Simple Linear Regression](https://scikit
-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)**-** Simple linear regression
* [XGBOOST
](https://xgboost.readthedocs.io/en/stable/)\- if you work with structured or tabular data, almost nothing beats XGBOOST

* [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)  library used to compute cosine-si
milarity among dense and sparse vectors/ embeddings.
* [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.d
ecomposition.PCA.html)**,** [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)**,** [U
MAP](https://umap-learn.readthedocs.io/en/latest/), etc- various dimension-reduction libraries, know when to use when, a
nd what.
* [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)**,** [HDBScan](https:
//scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html)**,** etc- for clustering
* [NLTK](https://www.
nltk.org/)**-** a suite of libraries and programs for symbolic and statistical natural language processing for English w
ritten in the Python programming language
* [BERT](https://huggingface.co/blog/bert-101)\- and BERT derivations (Roberta
, ALBERT, SBERT, etc)
* [List Comprehension](https://medium.com/techtofreedom/8-levels-of-using-list-comprehension-in-py
thon-efc3c339a1f0) \- Super important
* **Other important Python libraries**\- [os](https://docs.python.org/3/library/os
.html), [re](https://docs.python.org/3/library/re.html), [requests](https://pypi.org/project/requests/), [json](https://
docs.python.org/3/library/json.html), [python](https://docs.python.org/3/library/pickle.html),  [swifter](https://github
.com/jmcarpenter2/swifter),  (and many more)
* [Scalars, Vectors, Matrices, and Tensors](https://www.stephanosterburg.co
m/math_data_types) \- Good [visualization](https://towardsdatascience.com/better-visualizing-tensors-thanks-to-cities-b9
7e6b4ca2ca), An *tensor* is an array of data (numbers, functions, etc.) which is expanded in any number (0 and greater) 
of dimensions

# [Tensorflow vs Pytorch + Keras]

* Either library would be good, but based on what I'm reading nowadays
, [Pytorch](https://pytorch.org/) seem to have the advantage. You wont get wrong with either as both Deep Learning Frame
works are very mature, well documented. I personally prefer [Tensorflow](https://www.tensorflow.org/), but if you can le
arn and be proficient with both, then much much better.

# [Kaggle + Practice (KELANGAN MO ITO)]

* [Kaggle Datasets](ht
tps://www.kaggle.com/datasets) \- download datasets that pique your interests from Kaggle
* [Kaggle Notebooks](https://w
ww.kaggle.com/code) \- best way to learn is to find a working example, with a corresponding dataset.

# [Data Visualizat
ion]

* [MATPLOTLIB](https://matplotlib.org/)\- comprehensive library for creating static, animated, and interactive vis
ualizations in Python (required)
* [Seaborn](https://seaborn.pydata.org/)**-** Python library for better visually pleasi
ng charts and graphs (optional)
* [Tableau](https://www.tableau.com/en-gb/trial/tableau-software) **vs** [PowerBI](https
://powerbi.microsoft.com/en-us/downloads/)\- optional, but I chose POWERBI kasi yun ang pinoprovide ng company namin. (o
ptional)
* **Excel- w**hen you talk to business people, this is one of the best and easiest ways to share data and chart
s (highly recommended)
* **Powerpoint-** you will be presenting your findings to business and technical people, and ever
yone in between (highly recommended)

&#x200B;

# [Cutting Edge/ State Of The Art (SOTA)]

Eto ang mga cutting edge NGAY
ON, as I write this September 12, 2023.

* [OpenAI.com](https://OpenAI.com) \- ChatGPT, no need to explain
* [Meta AI's 
Llama](https://ai.meta.com/blog/large-language-model-llama-meta-ai/)\- a state-of-the-art foundational [large language m
odel](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/) designed to help 
researchers advance their work in this subfield of AI.
* [Langchain](https://python.langchain.com/)\- is a framework for
 developing applications powered by language models.
* [Kor](https://eyurtsev.github.io/kor/tutorial.html)\- is a thin w
rapper on top of LLMs that helps to extract structured data using LLMs.
* [Pinecone](https://www.pinecone.io/)\- fully-m
anaged, developer-friendly, and easily scalable vector database
* [https://www.youtube.com/@DataIndependent](https://www
.youtube.com/@DataIndependent)
   * One of the BEST resources on how to weave and integrate Langchain + LLM (like Llama 
or ChatGPT) + your own data + [Retrieval Augmented Generation (RAG)](https://research.ibm.com/blog/retrieval-augmented-g
eneration-RAG)

# [So you want to deploy these LLMs  on your local eh?]

* [https://huggingface.co/TheBloke/](https://hu
ggingface.co/TheBloke/)\- choose your quantized GGUF/ GGML/ GPTQ models
* [https://github.com/ggerganov/llama.cpp](https
://github.com/ggerganov/llama.cpp) \- Port of Facebook's LLaMA model in C/C++
* [https://github.com/oobabooga/text-gener
ation-webui](https://github.com/oobabooga/text-generation-webui)\- A Gradio web UI for Large Language Models. Supports t
ransformers, GPTQ, llama.cpp (GGUF), Llama models.
* [https://github.com/turboderp/exllama](https://github.com/turboderp
/exllama) \- A more memory-efficient rewrite of the HF transformers implementation of Llama for use with quantized weigh
ts.
* NOTE: I have a deep-learning PC and i tried all the deployments methods above

# [Nice to haves]

* **Data Pipelin
e Orchestration**\- if you have knowledge with something like [Azure Data Factory](https://azure.microsoft.com/en-us/pro
ducts/data-factory/) or [Databricks](https://www.databricks.com/) to pull data from point A to B, then much better. Most
 companies nowadays are still in the early stages of data maturity, only the FAANG level companies have dedicated Data E
ngineers to pull the data for you. Most of the time, like sa case ko, I also double down as the data engineer
* [Docker]
(https://www.docker.com/)**-** when deploying your models to production, you will most likely create images of your appl
ication with your model for containerization and will deploy it
* **Linux-** sometimes I double down as a DEVOPS person 
as well and do my own deployment of models with DOCKER in Azure, most (if not all) VMs and computes in the cloud are HEA
DLESS Linux meaning  no GUI. So you have to be somewhat proficient with Linux command like `sudo -rm -rf` , **ok dont do
 that if ayaw mong magulpi ng mga teammates mo.** But, seriously, linux proficiency is a nice to have.
* [Spacy](https:/
/spacy.io/)**-** *spaCy* is a free open-source library for Natural Language Processing in Python
* **Object Oriented Pro
gramming-** arguably not a must, but when your goal is to actually deploy models to production, your code must be very m
odular, easy to understand, and adheres to industry standards and patterns.
* [Flask](https://flask.palletsprojects.com/
en/2.3.x/)**/** [Streamlit](https://streamlit.io/)**-** for your application's web part
* [Doccano](https://github.com/d
occano/doccano)**-** open source labelling and text annotation software.
* [Beautiful Soup](https://pypi.org/project/bea
utifulsoup4/) **+** [Selenium](https://www.selenium.dev/)**-** for webscraping and automating it
* [Regex](https://regex
101.com/)**-** Yung hate mo nung college, malaking bagay ngayon
* VectorDB- like [Pinecone](https://www.pinecone.io/) or
 [Redis](https://redis.io/)
* [FASTAPI](https://fastapi.tiangolo.com/) \- FastAPI is a modern web framework for building
 RESTful APIs in Python-
* Cloud platform competencies - blob storages, cloud VMs and computes, Linux terminal, how to s
pinup services, how to deploy models, how to deploy containers, etc. Overlap with DEVOPS, but I am quite proficient so I
 can do tasks with minimal to no DEVOPS assistance.

&#x200B;

# [Software]

* **Jupyter notebook/ lab**\- notebook for 
Python
* **Visual Studio Code-** good IDE from Microsoft
* **GIT-** for storing your code, cloning repos, etc

# [Other 
Important Concepts and Misc]

* **Descriptive and Inferential statistics**
* **Measures of Central Tendency and Dispersi
on**
* **Normality Tests**
* **Null and Alternative Hypothesis**
* **Different t-tests**
* **How to read p-values**
* **
Confusion Matrix and Type-1 and Type-2 errors**
* **Multilabel vs Multiclass**
* **Imputations**
* **Standardization vs.
 Normalization**
* **Scaling and different preprocessing techniques**
* **Outlier detection, standard deviation, IQR**
*
 **Classification Metrics**\- when to use what and how to read
   * Accuracy, Precision, Recall, F1-score, etc
* **Regre
ssion Metrics**
   * Mean Squared Error, Mean Absolute Error, Root Mean Squared Error, R-squared, etc
* **Sparse vs. Den
se Vectors**
* **Distance Measurements**
   * Euclidean Distance, Manhattan Distance, Cosine Similarity, etc
* **Dimensi
on Reduction and curse of dimensionality**
* **Supervised, Semi-supervised, and Unsupervised learning**
* **Word Embeddi
ngs**
* **Handling imbalanced data**
   * Smote, Classweights, Undersampling, oversmapling, synthetic data generation, e
tc
* **Data Leakage and how to identify and address them**
* **Hyperparameterization**
* **(Model) Weights and biases**

* **Overfitting vs Underfitting, convergence**
* **Activation functions in Deep Learning**
* **Model Ensembling**
* **En
codings**
   * ascii, utf-8,  utf-16
* **File types**
   * parquet, csv, json, xml, excel
* **Tokens, unigrams, bigrams,
 trigrams, ngrams**
* **Gradient Descent, Learning Rates, local and global minima**
   * Statquest is very good in expla
ining the math and I manually computed the derivatives by hand as exercise. Very good discussion and tutoral.
* **(And m
any many many, ..., many more)-** Ill leave it up to you to research these topics, but you will naturally bump into thes
e concepts and terms as you study and go along.

# [Related Post]

* [How to become a data engineer](https://www.reddit.
com/r/PinoyProgrammer/comments/166usob/comment/jym6906/?utm_source=share&utm_medium=web2x&context=3)

# [Notes and Advic
e]

* I went Azure with my cloud platform,  you can choose other cloud platforms like AWS and GCP
* I went Tensorflow wi
th my Deep learning library, you can choose Pytorch here
* Nagkaroon na ng mga Bachelor of Science In Data Science na me
dyo recent lang ata na naoffer sa mga universities, I dont have visibility sa curriculum nila.
* Two people with the sam
e role 'DATA SCIENTIST' can actually be doing different things.
* I believe there are two main flavors of data scientist
s, the 'theory-inclined' na mga super henyo sa mga algorithms and jargon, and the 'implementation-inclined' na just util
izes the libraries to do the calculations, I am more of the latter.
* Sometimes the problem is complex, sometimes it's n
ot, you have to know which algorithm to choose. But before everything else, you have to know the problem at hand and kel
angan mo maintindihan ang nuances and gain domain knowledge. Sometimes a very good solution is a very simple one.
* Don'
t fall for those MASTER-DATA SCIENCE in 3 months snake-oil stuff, The field is fast evolving and no, you can't MASTER th
is field in 3 months.
* **I WONT SUGARCOAT**  but this is a very deep and technical field, if you do not have a knack fo
r studying, burning the midnight oil, failing-miserably nang paulit-ulit, learning from your mistakes, and overcoming th
em, **then go back**. But if you love challenges and you have the grit, soldier on.
* Di mo maiiwasan na makipagusap wit
h people from other countries and various levels (c-levels, managers, fellow developers, business people, etc), so polis
h your communication skills.
* You must be open-minded as there are countless ways to approach a problem, but you also h
ave to know when to call someone's BS.
* The list above is my personal journey and there are countless resources, even b
etter ones that I've mentioned. So share 'em in the comments!
* I'm far from being an expert in Data Science, and I cons
ider myself as a perpetual student who is still learning and studying.
* Keep your ego in check, there will always be so
meone better than you.
* Buy a notebook and a pen, jot down notes, solve equations by hand, never underestimate the hand
-brain connection
* Enjoy and celebrate the small wins

# [GOOD LUCK]
```
---

     
 
all -  [ Langchain + Azure Formrecognizer: How to pass documents? ](https://www.reddit.com/r/LangChain/comments/16g20dc/langchain_azure_formrecognizer_how_to_pass/) , 2023-09-13-0909
```
I am following a tutorial that says you should call it like this:

‘agent.run('what is the due date of the following inv
oice?'
    'data/Sample-Invoice-printable.png')‘

But I cannot get it to run on a local file. There is an error message 
that the resource cannot be found.

In addition: What kind of formatting is it in the example with the two arguments not
 separated by a comma? I am confused.

I read that the file needs to be given as a URL, so I tried it with “file:///path
-to-file“, but it didn’t work either.
```
---

     
 
all -  [ Advice on fine-tuning ](https://www.reddit.com/r/LangChain/comments/16g18bn/advice_on_finetuning/) , 2023-09-13-0909
```
I'm very much a newbie (both with Langchain and Python), so please forgive any questions asked in ignorance.

I am curre
ntly trying to fine-tune ChatGPT on a CSV of data I have. The problem is the CSV is very large and contains fields with 
large paragraphs of text. The CSV has about 50k entries in it. It works well when I try to fine tune based on a small sa
mple of around 20 entries on the original CSV. But if I increase the number of entries to even around 100, I get an erro
r saying the rate limit has been reached.

I'm using a CSVLoader to load my document, and then indexing it with the Vect
orstoreIndexCreator. What can I do to be more efficient?

Thank you!
```
---

     
 
all -  [ Open-source end to end chatbot product and data collector ](https://www.reddit.com/r/LangChain/comments/16g04ls/opensource_end_to_end_chatbot_product_and_data/) , 2023-09-13-0909
```
Hey all, I was thinking of creating an open-source tool that merges search engine, chatbot, and data collection function
alities, enabling searches across platforms like Slack, GitHub, and Google Docs and aiding in the collection of conversa
tional data for LLM fine-tuning (for when incremental training of chatbots becomes a thing).

I've got a slidedeck for t
he project below, analysing similar products and possible gaps in the market, and ultimately attempting to find a way to
 alleviate duplication of efforts across companies. Maybe there's some langchain contributors in here that has an opinio
n on this. Let me know your thoughts, and if anyone would like to contribute.

[https://docs.google.com/presentation/d/1
orbE7mxIH1iegC0koDvK05KiUv225MbbzSoYWjcljd4/edit#slide=id.g1c276c7e915\_4\_5](https://docs.google.com/presentation/d/1or
bE7mxIH1iegC0koDvK05KiUv225MbbzSoYWjcljd4/edit#slide=id.g1c276c7e915_4_5)
```
---

     
 
all -  [ Chain Conversations for Context ](https://www.reddit.com/r/LangChain/comments/16fyrje/chain_conversations_for_context/) , 2023-09-13-0909
```
**Tl;Dr:**If you have an idea that you need assistance in its creation; try using a 'Master' chat, and use only refined 
and condensed information from 'sub-chats' as its input to ensure you get the most contextual reply. This method reduces
 the amount of prompt engineering required at various stages of the chat, ie; the beginning/ middle/ end. Responses are 
more contextual, and there is a perceived compounding affect within the original model context window where replies are 
very good even when compared against advanced prompting techniques.---

Background:I've been using ChatGPT everyday sinc
e its inception. Over the past year, I've envisioned an assistant language model of my own for fun. With the help of Ope
nAI I've been able to achieve this at an advanced level, and there's been a poignant observation that has helped me real
ly develop this application (more than just creating a model, but also training, advanced nlp, vectorstores, tokens, emb
eddings/ embeddings models... it was a lot, I promise):

The issue:Using ChatGPT, you have a limited context window. Reg
ardless of the size of this window (it's not infinite), you will begin to have degrading quality replies at some point. 
Even with advanced gradient descent techniques, from what I've observed, you still sacrifice context as the conversation
 is lengthened. This issue is poignant when developing large code-bases, as eventually the code slowly becomes less and 
less compatible on the first try, or the use of advanced prompt techniques for later in the conversation are required (a
nd not guaranteed). But this is universally true if the conversation you're having requires specific context throughout 
its history.

My observed solution to maintain context without prompt engineering:Structure your chats so that the infor
mation you abstract during your conversation can be pulled in a formatted way, and then inserted into a 'Master' chain. 
The idea is, if you have a large conceptual idea, it's likely that it will require branches of thought to be unified at 
some point in order to replicate the big-picture idea; ie: for what you want to see to actually happen. In that sense, y
ou need to structure your responses so that when one branch is completed- you can copy/paste that information in its ful
l context back into your master chat branch. The idea is to shove as much context as possible into one single chat. It's
 best to have a unified context repository. A single chat container which contains only information with as much rich co
ntext as possible. Use multiple other chats to refine your ideas, condense the logic, and create a dense conversation ra
ther than a long one where useless embeddings are stealing context later in the chat.

Why it works:In the practice of r
efining your idea, you allow the nlp model to curate its own definitions and language. By the time you've refined your i
dea, you've basically let the model use its own parameters to curate suitable verbose (its own language with underlying 
context) that enhances the quality of the response when used as the input in your Master chat. This is a simple concept,
 but imo one of the most important distinctions of why this method is important.

Simple Example:i. I want to create an 
application that converts my pdf to tokens and embeddings.ii. To do this, I might ask ChatGPT, 'how can i do this', and 
use its response as my individual chat windows. So, it might say, okay you need to transform the data to CSV, use nltk t
o tokenize the data, use openai for the embeddings, and then you might want to explore the data- is there anything furth
er you'd like to discuss.... etc. etc.'iii. so, now my chat windows become; a. transform pdf to csv, b. nltk for tokeniz
ing csv data, c. openai for embeddings, d. exploring embedding data. from there, I'd ask questions to the chat window un
til I felt comfortable about how that specific step is achieved.\*I constantly ask ChatGPT to think critically, think an
alytically, and provide your response in a step by step format where each individual step is in succession of the previo
us step and forms a logical pattern. *something like that*I. Master Chat: includes the answers to my questions from the 
individual sub-chats.II. I'm updating my Master-Chat as new information is presented that contributes to a condensed sol
ution. \*the Master-Chat is still very conversational, although now it's a bit more intentional with its results. imo th
is creates a compounding effect in which the more dense the information provided, the longer lasting the context as the 
conversation continues. The answers you receive within the first context window (4k/ 8k/ 16k/ 32k, wtv.) will be vastly 
superior. This is easier than prompt engineering, it's simply organizing the information in a better way.

Final Tip:You
 can further refine the context of your discussions with ChatGPT, by simply using the instructions in your settings.i. W
hat would you like ChatGPT to know about you to provide better responses? 'Hi G, my name is 'x', and I'm working on the 
following project: '.ii. How would you like ChatGPT to respond? 'Just be your normal, helpful, self. Thank you. I love y
ou.'

Disclaimer: I understand the underlying technology is more complicated than the suggested advice implies, and in p
ractice may operate differently, albeit come to the same conclusion imo. This is practical advice. I just see so much no
nsense about 'prompt-engineering' and the reality is, while important, it's not the end-all. And, you can use simpler pr
ompting techniques like asking the chat for step-step replies, which are providing contextually rich information that ca
n be used to create better conversations in new chats.

I thought this was interesting, especially if new Users are havi
ng trouble with the context window, plus all the talk about degrading replies. This is just one way to combat that.
```
---

     
 
all -  [ Problem with asymmetric search ](https://www.reddit.com/r/LangChain/comments/16fu2e1/problem_with_asymmetric_search/) , 2023-09-13-0909
```
I vectorized my content and saved it in the database to be used in a chatbot. However, I have a problem with the search.


As the user's question is small, he favors small vectors, which are generally not the best. However, if I transform th
e user's question into a larger question, it returns better results.

What can I do to improve this asymmetric search, c
onsidering that the user's question will generally be small?
```
---

     
 
all -  [ How to Configure User Access Tokens for Tools in Langchain Agent? ](https://www.reddit.com/r/LangChain/comments/16frolt/how_to_configure_user_access_tokens_for_tools_in/) , 2023-09-13-0909
```
I have two essential tools, Jira and Notion, both of which require user access tokens in the request header. I'm using t
hese tools through the Langchain Agent, and I need guidance on how to properly add the relevant access tokens to ensure 
seamless integration. Can you provide step-by-step instructions or best practices for configuring user access tokens in 
the Langchain Agent when we are using tools?
```
---

     
 
all -  [ Which are some good, lightweight models that can be used? ](https://www.reddit.com/r/LangChain/comments/16frbes/which_are_some_good_lightweight_models_that_can/) , 2023-09-13-0909
```
I am creating a Document based Query/Answer application on my corporate machine. It is unable to get local issuer certif
icate, thus I am unable to use most of the LLMs that have been provided since most of them download the model when calle
d. So essentially, no API calls allowed.

As of right now, I am using GPT4All local model and the sentence transformer a
ll-MiniLM-L6-v2 for embeddings. But this combination is way too slow when querying. Do you guys have any other suggestio
ns and combinations? When suggesting, please keep in mind the problem I mentioned lol. 

Thank you so much.
```
---

     
 
all -  [ How to edit specific sections of a document using an LLM? ](https://www.reddit.com/r/LangChain/comments/16fp7s4/how_to_edit_specific_sections_of_a_document_using/) , 2023-09-13-0909
```
Are  there any pipelines or perhaps a Langchain chain that would allow me to  use an LLM to identify and edit specific p
ortions/sections of a  document based on a query?

I  understand I can have the document indexed using an abrupt charact
er  split of a set number of characters, and edit the relevant chunk and  re-append to the document, however if the cont
ent that is to be edited  is spread across two chunks, I would end up having to regenerate both  those chunks and re-app
ending to the original document. However I don't  know how to include the context of the previous chunk to have a smooth
  continuation into the 2nd chunk.

Hence  my question, is there any implementation for this? Or a simpler, better  appr
oach that I am missing? Any resources or help is greatly  appreciated.
```
---

     
 
all -  [ A RAG bot can retrieves content on-demand! ](https://www.reddit.com/r/Langchaindev/comments/16fin8v/a_rag_bot_can_retrieves_content_ondemand/) , 2023-09-13-0909
```
A RAG bot can retrieves web/local content on demand! it uses [ActionWeaver](https://github.com/TengHu/ActionWeaver) to c
ombine and orchestrate llama index and langchain tools together for a new search experience.

Here is the [Github](https
://github.com/TengHu/Interactive-RAG) repo

[Interactive RAG Demo](https://www.loom.com/share/f3d7a8e80b3e47618d27730e01
eb4bca)
```
---

     
 
all -  [ 🦙 LlamaIndex vs. LangChain 🦜 ](https://www.gettingstarted.ai/langchain-vs-llamaindex-difference-and-which-one-to-choose/) , 2023-09-13-0909
```
Here’s my latest post about LlamaIndex and LangChain and which one would be better suited for a specific use case.

Plea
se send me your feedback!
```
---

     
 
all -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-13-0909
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
all -  [ I built an AI Agent (BondAI) that actually works and has a friendly API for easy integration into ot ](https://www.reddit.com/r/ChatGPTCoding/comments/16fecm1/i_built_an_ai_agent_bondai_that_actually_works/) , 2023-09-13-0909
```
📢 I'm excited to introduce **BondAI**, an AI Agent framework and CLI, with a lightweight yet robust API making integrati
on into your own applications straightforward and easy.

**Repository:** [**https://github.com/krohling/bondai**](https:
//github.com/krohling/bondai)

# ⚡️Examples

Here's an example of buying/selling Stocks with [Alpaca Markets](https://al
paca.markets/). I strongly recommend using Paper Trading btw!

    from bondai import Agent 
    from bondai.tools.alpac
a_markets import (
        CreateOrderTool, 
        GetAccountTool, 
        ListPositionsTool
    )
    
    task = (

        'I want you to sell off all of my existing positions.'
        'Then I want you to buy 10 shares of NVIDIA with 
a limit price of $456.'
    )
    
    Agent(tools=[   CreateOrderTool(),   GetAccountTool(),   ListPositionsTool() ]).r
un(task) 

[**Here's an example**](https://github.com/krohling/bondai/tree/main/examples/online-research) of BondAI doin
g online research and [**here's a home automation example**](https://github.com/krohling/bondai/tree/main/examples/home-
automation).

# 🔍 What is BondAI?

**BondAI** is a framework crafted for the smooth integration and customization of Con
versational AI Agents. Leveraging the power of OpenAI's [**function calling support**](https://openai.com/blog/function-
calling-and-other-api-updates), it sidesteps the hurdles often encountered in building a Conversational Agent, offering 
solutions such as:

* Memory management
* Error handling
* Integrated semantic search
* A rich array of pre-existing too
ls
* Ease of crafting custom tools

Moreover, it offers a **CLI interface** that promises an impressive command line age
nt experience, available to anyone with an OpenAI API Key!

# 🏗️ Why build BondAI?

I am convinced that AI agents are go
ing to be an important architecture for the future of AI. Despite their phenomenal problem-solving abilities, the existi
ng tooling often fell short in performing simple tasks, and the frameworks appeared unnecessarily complicated. This spur
red the birth of **BondAI**, aiming to address these shortcomings and offer a more optimized environment for agent imple
mentations.

I am keen on hearing your feedback on **BondAI**'s functionality and any suggestions for improvements!

# 🛠
️ Installation & Usage

Get started with BondAI with a simple: pip install bondaiThe CLI tool offers a ready-to-use agen
t experience packed with several default tools. You can also integrate it with various tools such as Google Search, Alpa
ca Markets, and LangChain Tools to execute a myriad of tasks effectively. Detailed guides and examples for usage are ava
ilable in the README.

# 🔧 APIs and Custom Tools

The BondAI framework offers flexible APIs to build your agent and crea
te custom tools for a personalized experience. It follows a straightforward implementation approach, making the tool cre
ation process hassle-free for developers.

Examples of included Tools:

* Google and Duck Duck Go Search
* Semantic Sear
ch for Files and Websites
* Alpaca Markets
* Gmail Integration
* Easily import tools from LangChain!

# 🐋 Docker Contain
er

For a secure environment, especially while using tools with file system access, running **BondAI** within a docker c
ontainer is highly recommended. Follow the steps in the REAME to easily build and run the **BondAI** container.

🚀 Join 
the mission; contribute to BondAI! And please share feedback/ideas in the comments!
```
---

     
 
all -  [ Editing specific sections of documents? ](https://www.reddit.com/r/LocalLLaMA/comments/16fdr8r/editing_specific_sections_of_documents/) , 2023-09-13-0909
```
Are there any pipelines or perhaps a Langchain chain that would allow me to use an LLM to identify and edit specific por
tions/sections of a document based on a query? 

I understand I can have the document indexed using an abrupt character 
split of a set number of characters, and edit the relevant chunk and re-append to the document, however if the content t
hat is to be edited is spread across two chunks, I would end up having to regenerate both those chunks and re-appending 
to the original document. However I don't know how to include the context of the previous chunk to have a smooth continu
ation into the 2nd chunk.

Hence my question, is there any implementation for this? Or a simpler, better approach that I
 am missing? Any resources or help is greatly appreciated. 
```
---

     
 
all -  [ Support for additional query parameters ](https://www.reddit.com/r/LangChain/comments/16fb2p5/support_for_additional_query_parameters/) , 2023-09-13-0909
```
Hi! I would like to set a range and/or limit/offset while doing vector queries, so that instead of fetching the top n re
sults I can specify that I want the 1st, 2nd, 3,rd result and so on.

This seems to be a supported function in several o
f the integrated vector DBs, see for example [Weaviate](https://weaviate.io/developers/weaviate/search/similarity#number
-of-results) and [Supabase](https://supabase.com/docs/reference/javascript/range). How do I modify my queries using Lang
chain to make use of these functions? Is it supported? I tried asking this question in the langchain github but didn't g
et any help. I am using the JS version of Langchain.
```
---

     
 
all -  [ A RAG bot can retrieves content on demand ](https://www.reddit.com/r/LangChain/comments/16fac58/a_rag_bot_can_retrieves_content_on_demand/) , 2023-09-13-0909
```
hey guys, I implemented A RAG bot can retrieves web/local content on demand, it uses [ActionWeaver](https://github.com/T
engHu/ActionWeaver) to orchestrate llama index and langchain tools to combine search and RAG.

[Github](https://github.c
om/TengHu/Interactive-RAG)

[Interactive RAG Demo](https://www.loom.com/share/f3d7a8e80b3e47618d27730e01eb4bca)
```
---

     
 
all -  [ A RAG bot can retrieves content on demand ](https://www.reddit.com/r/LlamaIndex/comments/16faasl/a_rag_bot_can_retrieves_content_on_demand/) , 2023-09-13-0909
```
hey guys, I implemented A RAG bot can retrieves web/local content on demand, it uses [ActionWeaver](https://github.com/T
engHu/ActionWeaver) to orchestrate llama index and langchain tools to combine search and RAG.

[Github](https://github.c
om/TengHu/Interactive-RAG)

[Interactive RAG Demo](https://www.loom.com/share/f3d7a8e80b3e47618d27730e01eb4bca)

📷
```
---

     
 
all -  [ Where is the error stack trace...? ](https://www.reddit.com/r/LangChain/comments/16f72wy/where_is_the_error_stack_trace/) , 2023-09-13-0909
```
I get the error below sometimes which would be fine if I could trace the problem and debug but I can't for the love of m
e figure out why the stack trace is hidden because this is all I see in my terminal 

[LLM run error](https://preview.re
dd.it/3ltiwnihxgnb1.png?width=1320&format=png&auto=webp&s=ccc62cf930f9d91c48022dae69c5fea0fcf11e04)

How do you go about
 this?
```
---

     
 
all -  [ Multiple models running on one system ](https://www.reddit.com/r/LocalLLaMA/comments/16f4177/multiple_models_running_on_one_system/) , 2023-09-13-0909
```
Is it possible to run multiple models at the same time on the same system and let them interact with each other on somet
hing like langchain?
```
---

     
 
all -  [ I made a KNOWLEDGE ASSISTANT. ](https://www.reddit.com/r/LangChain/comments/16f1i6b/i_made_a_knowledge_assistant/) , 2023-09-13-0909
```
I made a **KNOWLEDGE ASSISTANT**, which allows you to upload PDF, WORD, TXT, and CSV documents, vectorize and store the 
documents after splitting, and combine them with the OpenAI GPT model to ask questions and return answers. Visual parame
ter adjustment is provided at each step. Turning on DEBUG mode lets you see information such as similarity search, promp
t words, produced content, etc.

&#x200B;

https://reddit.com/link/16f1i6b/video/wuywix0qtfnb1/player

Please let me kno
w what you think.
```
---

     
 
all -  [ LLMChain timeout error with OpenAI ](https://www.reddit.com/r/LangChain/comments/16f0nkg/llmchain_timeout_error_with_openai/) , 2023-09-13-0909
```
I'm running a series of calls using a vary simple LLMChain and very often get a TimeoutError.The error crashes my server
 and doesn't retry automatically (I read somewhere that LangChain should handle the retries automatically).

Here's the 
full error I'm getting:

    Error in handler LangChainTracer, handleChainError: TimeoutError: The operation was aborted
 due to timeout
    file:///Users/[redacted...]/node_modules/langchain/dist/util/openai.js:6
            error = new Err
or(e.message);
                    ^
    
    Error [TimeoutError]: Request timed out.
        at wrapOpenAIClientError 
(file:///Users/[redacted...]/node_modules/langchain/dist/util/openai.js:6:17)
        at file:///Users/[redacted...]/nod
e_modules/langchain/dist/chat_models/openai.js:517:31
        at process.processTicksAndRejections (node:internal/proces
s/task_queues:95:5)
        at async RetryOperation._fn (/Users/[redacted...]/node_modules/p-retry/index.js:50:12) {
   
   attemptNumber: 1,
      retriesLeft: 6
    }
    
    Node.js v20.5.1

Looking into LangSmith I can see the timed out
 requests have waited for 600 seconds. That's a lot!

* Is there anything I can do so LangChain handles the retries?
* I
f not, what's the best way to handle the retries. I was looking into [handleChainError()](https://js.langchain.com/docs/
api/callbacks/classes/LangChainTracer#handlechainerror)
* Can I reduce the waiting time to way less than 600 seconds?
```
---

     
 
all -  [ JS/TS EXAMPLE REPOS? ](https://www.reddit.com/r/LangChain/comments/16eyp9z/jsts_example_repos/) , 2023-09-13-0909
```
Looking to learn how to build a self hosted langchain bot that will use scrapers to pull in data. Not super sure where t
o start. I’ve gone through some docs but I’d love to hear some recommendations of stacks or read through some repos to l
earn how to build properly. 

Thanks. Xo
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-13-0909
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-13-0909
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-13-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-13-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-13-0909
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-09-13-0909
```
We've created an open source chat bot builder, on top of PostgresML. This tool makes it easy to ingest documents and set
 a system prompt for a chatbot with knowledge of your content. The innovation is in the simplicity and efficiency, rathe
r than the functionality.

PostgresML runs open source embedding models alongside pgvector in Postgres to implement chat
 bot prompt creation without any network calls, which makes it \~4x faster than competing architectures. It can also do 
text generation with that prompt (and no additional network hops) using any open source model from HuggingFace, but it a
lso integrates with the GPT-4 API if you'd like to use that instead. 

The full writeup including some benchmarks for co
mpeting architectures is here:  [https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-kno
wledge-based-chatbots-part-I](https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-knowle
dge-based-chatbots-part-I)

You can chat with a deployment that has access to our blogs and documentation content it in 
\[our Discord\]([https://discord.com/channels/1013868243036930099/1013868243536072868](https://discord.com/channels/1013
868243036930099/1013868243536072868)), where it answers questions addressed to @PgBot.

&#x200B;

* The source code for 
the bot builder and server is only a few hundred lines of Python [https://github.com/postgresml/postgresml/tree/master/p
gml-apps/pgml-chat#readme](https://github.com/postgresml/postgresml/tree/master/pgml-apps/pgml-chat#readme)
* The chat a
pp is so small, because it's delegates all the vector db and embedding generation options to our Python client SDK, whic
h is available for anyone to build other apps with: [https://pypi.org/project/pgml/](https://pypi.org/project/pgml/)
* T
he Python client SDK is so small, because it's just a wrapper around the Rust client SDK: [https://github.com/postgresml
/postgresml/tree/master/pgml-sdks/rust/pgml](https://github.com/postgresml/postgresml/tree/master/pgml-sdks/rust/pgml). 
Currently we also support JS/Typescript SDKs as well, all generated from the same safe and efficient underlying Rust imp
lementation, using some fancy Rust macros.
* The Rust client SDK is also pretty simple though, because it just delegates
 everything to the Postgres database extension, which is where everything is computed in a single GPU accelerated proces
s, without having to load any ML models, data, or dependencies on client apps, effectively eliminating all the typical M
L data<->model network hops. Which makes it faster, simpler and safer.

This lays out what we think a is a better approa
ch to AI application architecture compared to libraries like LangChain or LlamaIndex, that focus on glueing together dis
parate data stores, algorithms, models over the network.  

```
---

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-09-13-0909
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.

Checkout the entire blog post at [https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f](https://thevatsalsaglani.med
ium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f)
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-13-0909
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
