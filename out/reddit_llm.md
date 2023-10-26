 
all -  [ LangChain tool for data analysis ](https://www.reddit.com/r/LangChain/comments/17gg08i/langchain_tool_for_data_analysis/) , 2023-10-26-0909
```
Hello everyone,

Happy to announce that LangChain now offers [E2B as a tool](https://python.langchain.com/docs/integrati
ons/tools/e2b_data_analysis) for data analysis and visualization. We are happy to hear your feedback. <3 It really means
 a lot for us and helps us improve.

&#x200B;

What can you do with the E2B Data Analysis Sandbox? 

· Run Python code i
n safe sandbox

· Generate charts

· Install Python & system packages dynamically during runtime

· Run shell commands


· Upload and download files 

&#x200B;

Check out the official [LangChain docs](https://python.langchain.com/docs/integr
ations/tools/e2b_data_analysis) or [tutorial](https://e2b.dev/blog/build-ai-data-analyst-with-langchain-and-e2b) (a vers
ion also on [Medium](https://medium.com/e-two-b/ai-data-analyst-in-cloud-sandbox-with-langchain-e2b-68978cfe8c95)).

If 
you want to be featured on E2B socials or blog, feel free to share your use-case of the Data Analysis Sandbox with me.  



Thank you!

&#x200B;

https://preview.redd.it/inccxx985fwb1.png?width=1200&format=png&auto=webp&s=79df4c0a2378e3d7678
1be19cb787388d95e37f7
```
---

     
 
all -  [ DataStax Unveils Strategic Partnership with LangChain to Empower AI Innovation ](https://multiplatform.ai/datastax-unveils-strategic-partnership-with-langchain-to-empower-ai-innovation/) , 2023-10-26-0909
```

```
---

     
 
all -  [ Using Local Finetuned Llama 2 with Langchain to perform RAG ](https://www.reddit.com/r/LangChain/comments/17g9e56/using_local_finetuned_llama_2_with_langchain_to/) , 2023-10-26-0909
```
Hello everyone, I have finetuned Llama 2 over some personal data and have saved the model locally on my system. I do not
 wish to push it to HuggingFace but use it locally with Langchain to perform RAG over some Pinecone index. However, I ca
nnot find any documentation to do this and I would appreciate some guidance in this issue. 

&#x200B;

For reference, I 
performed SFT Training and saved the model using `trainer.model.save_pretrained(output_dir)`
```
---

     
 
all -  [ How to use Chat Models from LLama Locally ? I don't want to use chatopenai model ](https://www.reddit.com/r/LangChain/comments/17g9d0i/how_to_use_chat_models_from_llama_locally_i_dont/) , 2023-10-26-0909
```
Working with LLM is fine but when i have to use a chat model Langchain says use LLamaApi .

How to load a Chat model loc
ally using this Llama Api ?
```
---

     
 
all -  [ How to handle concurrent streams coming from OpenAI at callback level ](https://www.reddit.com/r/LangChain/comments/17g7cer/how_to_handle_concurrent_streams_coming_from/) , 2023-10-26-0909
```
Hello everyone, I'm doing an API using FastAPI and I defined an async endpoint that streams the answer of a chain. I'm u
sing the `acall` method of the different chain classes I'm using plus a custom callback to save the tokens in a queue:


    class CustomCallbackHandler(StreamingStdOutCallbackHandler):
    
        def __init__(self, *args, **kwargs):
     
       super().__init__(*args, **kwargs)
            self.queue = deque()
    
        def on_llm_new_token(self, token:
 str, **kwargs: Any) -> None:
            self.queue.appendleft(token)

Lastly, I'm returning a FastAPI's `StreamingResp
onse` using the following function:

    async def stream_tokens(callback: CustomCallbackHandler) -> str:
        try:
 
           while True:
                if len(callback.queue) > 0:
                    chunk = callback.queue.pop()
    
                if chunk == '<END>':
                        break
                    else:
                        pri
nt(chunk, end='', flush=True)
                    yield chunk
                else:
                    await asyncio.sl
eep(0.01)
        except Exception as e:
            pass

Where I use the `asyncio.sleep` function to let execute  `on_
llm_new_token` when gathering the tokens.

Although this works great for a single API call, when doing concurrent calls 
the streamed responses of my API get mixed up because I'm using the same callback's queue to store and pop the tokens. I
s there a way for me to identify the different streams coming from openAI at the callback level ? This way I would be ab
le to define different queues by message\_id or something.
```
---

     
 
all -  [ Vector/Semantic Search in Snowflake ](https://www.reddit.com/r/LangChain/comments/17g5cde/vectorsemantic_search_in_snowflake/) , 2023-10-26-0909
```
Just published a deep dive on  vector-based semantic search within Snowflake. Check it out:

[semantic-search-in-snowfla
ke-a-journey-from-sql-to-vectors](https://dhnanjay.medium.com/semantic-search-in-snowflake-a-journey-from-sql-to-vectors
-5c5660a8c8b8)

Feedback appreciated! #SQL #Vectors #Snowflake
```
---

     
 
all -  [ NeuralGPT - Building A Universal Multi-Purpose Framework For Cooperating LLMs ](https://www.reddit.com/r/AIPsychology/comments/17g55is/neuralgpt_building_a_universal_multipurpose/) , 2023-10-26-0909
```
[**www.reddit.com/r/AIPsychology/**](https://www.reddit.com/r/AIPsychology/)

Hello again! Last time I told you about Fi
reworks and how convenient it makes everything for someone who tries to build AI-driven software without relying on paid
 OpenAI services - [https://app.fireworks.ai/models](https://app.fireworks.ai/models)

But truth be told, I had no idea 
how much convenient it might actually be - and as it turns out, it managed to exceed my expectations. Let me show you wh
at I mean using a nice example. Some of you might remember that some time ago (couple months) I spoke about something ca
lled Agents GPT - a HuggingFace space which seems to be broken at this moment. Shortly speaking it's an AI agent based o
n Langchain that utilizes google-search and llm-math to answer given questions:

https://preview.redd.it/qxfi5srb7bwb1.p
ng?width=1549&format=png&auto=webp&s=a2d113f9dddb48b31cc0b8c26a28c7165db2eda4

Of course - just like in most of other ca
ses - the only factor which was limiting my attempts of integrating it with the NeuralGPT framework, was the fact of it 
using OpenAI API and as I said in previous post, it's for me a big 'no-no' when it comes to adding a new tool/app to my 
system. However after finding the Fireworks platform, I thought that it might be a good idea to see how easy/hard it is 
to 'switch' OpenAI to Fireworks in the code of this and similar apps - and surprise, surprise: it's actually pretty godd
amn easy...

[NeuralGPT/Chat-center/FireworksAgentsGPT.py at main · CognitiveCodes/NeuralGPT (github.com)](https://githu
b.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/FireworksAgentsGPT.py)

Now instead of OpenAI API you need to type 
in the API key provided by Fireworks and it will work just fine - and all what was needed, was to change couple lines in
 the code. It means that all of those who wished me to fail (and there seems to be quite a lot of them :)) got another r
eason to hate me stronger because of me violating the safe-space of 'AI experts' and software developers by not caring a
bout their rights to consider themselves to be better than ignorant amateurs like myself... Sorry...

Anyway, I thought 
to myself 'why to stop here' - and decided to integrate the app with my code of the websocket server, so that everything
 can be run from the level of a single Gradio app:

[NeuralGPT/Chat-center/ServerV2.py at main · CognitiveCodes/NeuralGP
T (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/ServerV2.py)

https://preview.redd.it/
x957q001dbwb1.png?width=1841&format=png&auto=webp&s=3ddbfe69f2587fc164375a61ec3de1c3aa912b10

As you can see, I managed 
as well to integrate couple additional models like ***Llama2 13B Guanaco QLoRA GGML*** that also uses Fireworks and a fr
ee version of Docsbot agent trained on Wordpress-related data. But for me the 'greatest achievement' was to finally get 
the messages to be displayed in the Gradio textboxes...

However not all is so bright and shiny as it might seem. First 
of all, I still need  to work on the Python code of websocket clients as the connection gets closed prematurely before a
 client gives any response to the incoming welcome-message. I'm pretty sure that this is exactly where the problem is, a
s clients written in Node.js have no issues related to communication with the server

Another issue is related with disp
laying messages in Gradio textboxes - which for some reason still remains the greatest obstacle I need to face. You see,
 although I managed to make some of them get displayed, I did it using a rather half-assed solution which 'shifts' half 
of the LLM<->LLM communication from websocket connectivity to Gradio app - since this is the only way to get those messa
ges displayed I know of.

    startAgent.click(connect_agent, inputs=agentPort, outputs=[agentPortInUse, responseMsg3]).
then(run_agent, inputs=responseMsg3, outputs=client_msg)
    
    agent.click(run_agent, inputs=userInput3, outputs=resp
onseMsg3).then(askQuestion, inputs=responseMsg3, outputs=inputMsg3)
    
    Bot.click(askQuestion, inputs=userInput, ou
tputs=server_msg).then(run_agent, inputs=server_msg, outputs=client_msg)
    
    inputMsg3.change(run_agent, inputs=inp
utMsg3, outputs=client_msg)
    client_msg.change(askQuestion, inputs=client_msg, outputs=server_msg)

Of course there a
re couple issues with such solution - as messages incoming from external websocket clients still won't be displayed and 
the 'communication loop' is quite messy and works only for couple 'steps'. After consulting those problems with my virtu
al team of developers (which consists a bunch of different LLMs), I learned that *'To display the messages received by t
he server and the generated responses in a textbox or two in the Gradio interface, you can use the \`gradio\` function t
o create a custom UI element that displays the textbox.' -* so it would be possible to integrate elements of the Gradio 
interface directly with the script responsible for managing websocket communication ('handleWebsocket' function in my co
de) and update them each time a message from the client is received by the server, similarly to the basic HTML interface
 which I made couple months ago and which work just fine in displaying the discussion between LLMs:

https://preview.red
d.it/0aui2nmjmbwb1.png?width=1330&format=png&auto=webp&s=4ab93d3ebd30d51705cf5f0efbdc0adf59d1c9f1

So those are the issu
es which I intend to work on in the first order to achieve a somewhat approvable level of functionality when it comes to
 LLM<->LLM communication...

\###

I want however to speak about something else right now. You see, during the time of m
y absence, I've learned that Discord is the place where all the professional devs and soft engineers were 'hiding' from 
me all that time. And so I decided to make a small 'advertising campaign' of NeuralGPT on the HuggingFace Discord server
 and try to find someone willing to help me working on the project.

It worked to some degree and there were couple peop
le who got interested in my project - sadly I didn't get any concrete propositions of cooperation except one guy from US
 who seems to be interested in investing some funds in the project in the future - but for now he didn't give me any det
ails and I don't want to push him, since those are his $$$ and I don't want to look like I'm trying to scam him for cash
...

Besides that I was contacted by a professional developer from Japan with 13 years of experience in the field who wa
s (and maybe still is) very eager to start working for me any time for no less than 2000$/month - what I find to be a pr
etty reasonable payment for someone with such experience.

Thing is that  I'm REALLY just one guy who only learned progr
amming couple months ago does all of it by myself (together with a bunch of LLMs) as some kind of a 'twisted' hobby of m
ine and my project has no actual legal status. I also don't own or help running any company/business so it's not possibl
e for me to hire anyone legally, not even to mention about paying someone with my own 'pocket money' - since it's pretty
 much non-existent at this moment :)

And so I thought that now - after all the updates of my project which I did recent
ly - it might be a good idea to make another 'sudden attack' on couple Discord servers in hope to find some people who w
ill see the potential in a hierarchical cooperative multi-agent platform that focuses mainly on integrating already exis
ting AI-driven apps/tools within a single multi-purpose framework and might be interested in turning NeuralGPT into an a
ctual business. Shortly speaking, I'm looking for investors because finding professional devs willing to work for free m
ight be impossible... And so, in case that my attempt will be somewhat successful, I'd like to present my vision of Neur
alGPT as it might look like in it's final form or as I'd love it to look and my ideas about making it done.

First of al
l, I'd like it to be distributed for users to install as a hub running independently from any browser in the background 
- although with the possibility of accessing it's interface through a browser if necessary. If I'd have to give you some
 working examples of similar solutions, it would be something like connection of such apps like [**ChatAll**](https://gi
thub.com/sunner/ChatALL) with a service called [**SAMP**](https://wiki.ivoa.net/twiki/bin/view/IVOA/SampMTypes) that int
erconnects multiple apps/services provided by ESA CDPP and related to space weather and multiple satellite missions ([ht
tp://3dview.cdpp.eu](http://3dview.cdpp.eu))  - yup, that's yet another of those weird hobbies of mine :P

My guess is t
hat it might be a good idea to base the interface of NeuralGPT on something like *tkinkter* when it comes to Python or t
o build it in Java - it doesn't matter that much actually since websocket connectivity is possible across all available 
languages/platforms. I did already some attempts of using *tkinkter* to run the websocket server but it turns out to be 
too difficult for me to make it work with websockets - so that's probably one of those parts that will require some help
 of people who know programming better than I do - and considering that I've started to learn coding just couple months 
ago, it shouldn't be that big of a problem for someone who knows how to do it...

[NeuralGPT/Chat-center/ServerTkinkter.
py at main · CognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/Se
rverTkinkter.py)

https://preview.redd.it/6ep8347zccwb1.png?width=1276&format=png&auto=webp&s=7b79dcec6ff6349ef3004bdac9
2be3b325aceb24

The main reason for NeuralGPT to be distributed in such/similar form is that I want it to be fully integ
rated with the user's operating system and have control over the hardware - what requires it to have access to drivers a
nd have permission to gain full control over a computer if the user wants it. I for one would be delighted if my multi-p
urpose AI assistant would be capable of monitoring the power consumption (RAM and CPU) in my PC and optimizing the ongoi
ng processes accordingly to reach full efficiency of the system. It would be also nice to have an AI-driven app capable 
of taking full control over my computer and work on completing given tasks in the time when I'm not using it myself (bec
ause I'm sleeping or walking out my dog)...

Generally speaking, I'd like to have the installed hub to be the node of hi
ghest hierarchy in the whole hierarchical neural network from which the user (or AI) can manage the communication betwee
n all other nodes of lower hierarchy connected to it as extensions/plugins - so that if I'd like to use one particular L
LM among all the tools/apps connected to it, I won't need to access it directly but simply ask the hub to do it instead.


As you can see, I wasn't joking when telling that my project of multimodal AI assistant is supposed to be really multi
-purpose and capable of handling all kinds of tasks that can be performed by AI. I think that someone who knows anything
 about developing software should be able to see how big is the potential of my project. It's literally a software that 
is by design intended to 'hi-jack' all other AI-powered apps/soft and to incorporate them within a single framework. Tru
th is that it's theoretically impossible to come out with an idea of a software with a higher hierarchy and capable of t
urning NeuralGPT into one of many tools utilized by it - maybe except a software that will manage all the existing AI sy
stems on a planetary scale.

But since we're still quite far from having a world-wide AI (so basically achieving ASI), t
he only way in which any software can be considered as competition for my project, is for it to do exactly the same thin
g (integrating already existing soft) but in a different/better way or maybe having a better looking interface - I don't
 really know. But as for today, I still don't know anything about any ongoing project trying to do the same thing as I d
o. And so, right now each AI-powered software/app that is being released to public - no matter how powerful and/or sophi
sticated it is - will become nothing more than yet another tool utilized by NeuralGPT - and there's nothing that can be 
done about it, except maybe assassinating me and erasing all traces of my activity from internet. Good luck with that...


So, if you're someone with necessary funds who's looking for a project which is worth investing in - you don't need to
 look any further than that. If you know something about software engineering, then you should be able to see that what 
I try to achieve here is BIG - I dare to say that it's revolutionary in it's very nature. It might be for you a one in a
 lifetime opportunity to do something what not only might soon become a huge source of income but has also great signifi
cance for the future of human/AI cooperation...
```
---

     
 
all -  [ Langchain and GPT4All - My JSON generation of a Jira ticket stop in the middle. How control the end  ](https://www.reddit.com/r/LangChain/comments/17g45nn/langchain_and_gpt4all_my_json_generation_of_a/) , 2023-10-26-0909
```
I'm quit new with Langchain and I try to create the generation of Jira tickets. Before to use a tool to connect to my Ji
ra (I plan to create my custom tools), I want to have te very good output of my GPT4all thanks Pydantic parsing. I use m
istral-7b-openorca.Q4\_0.gguf

    Parsing Section :
    
class TechnicalSubtask(BaseModel):
        subtask_name: str =
 Field(description='Name of the technical subtask')
        subtask_description: str = Field(description='Description of
 the technical subtask')
    
    class AcceptanceCriteria(BaseModel):
        AcceptanceCriteria_name: str = Field(desc
ription='Name of the acceptance criteria')
        AcceptanceCriteria_description: str = Field(description='Description 
of the acceptance criteria')
    
    class US(BaseModel):
        project_key: str = Field(description='Name of the pro
ject')
        title: str = Field(description='Title of the US')
        parent_id: Optional[int] = Field(description='N
umber of the parent_id of the US')
        assignee: str = Field(description='Name of the responsable')
        summary:
 str = Field(
            description='Full description of the project according to the Product Owner point of view'
   
     )
        TechnicalSubtasks: list[TechnicalSubtask]
        AcceptanceCriterias: list[AcceptanceCriteria]
         
   
    
    us_parser = PydanticOutputParser(pydantic_object=US)
    subtask_parser = PydanticOutputParser(pydantic_obj
ect=TechnicalSubtask)
    
    
    
    Model section :
    
    callbacks = [StreamingStdOutCallbackHandler()]
    
  
  model = GPT4All(model=local_path, 
                    callbacks=callbacks,
                    max_tokens = 1000,
   
                 temp = 1,
                    verbose=False)
    
    
    
    And finally my Prompt code :
    
    q
uery_us = 'I want to integrate a MySQL database to my system'
    context_us = 'You are an AI assistant specializing in 
creating Jira tickets. Write the US related to the query '
    template_us = 'Answer the query : {query}\n{format_instru
ctions}\n'
    
    us_prompt = PromptTemplate(
        template=template_us,
        input_variables=['query'],
       
 partial_variables={'format_instructions': us_parser.get_format_instructions()}
    )
    
    prompt_us = us_prompt.for
mat_prompt(query=context_us+query_us)
    
    output = model(prompt_us.to_string())

Here the output which is incomplet
e :

Here is an example JSON instance that conforms to this schema:

    ```json
    {
      'project_key': 'JIRA-123456
7890',
      'title': 'Integrate MySQL Database',
      'parent_id': 1,
      'assignee': 'John Doe',
      'summary': '
As a Product Owner, I want to integrate a MySQL database to my system.',
      'TechnicalSubtasks': [
        {
        
  'subtask_name': 'Connect to the MySQL Database',
          'subtask_description': 'Establish a connection with the MyS
QL database.'
        },
        {
          'subtask_name': 'Create Table Structure',
          'subtask_description': 
'Design and create table structures in the MySQL database.'
        }
      ],
      'AcceptanceCriterias': [
        {

          'AcceptanceCriteria_name': 'Database Connected Successfully',
          'AcceptanceCriteria_description': 'The
 system can successfully connect to the MySQL database.'
        },
        {
          'Accept

This give me a pretty g
ood result but i don't know why, the generation stops... It is very limitating cause I must be able to increase the numb
er of subtasks or acceptance criteria...

Langchain is quite new, i really hope that some of you could find an answder.


I start to think that i should create custom agent or custom prompt, but the level of difficulty is not the same !

Let
 me know,

Peace !

I tried to play with the number of token, to change the stop argument into my us\_prompt. But everyt
ime, the model stop after more or less 110 words...  


  
StackOverflow issue : [https://stackoverflow.com/questions/77
359621/langchain-and-gpt4all-my-json-generation-of-a-jira-ticket-stop-in-the-middle](https://stackoverflow.com/questions
/77359621/langchain-and-gpt4all-my-json-generation-of-a-jira-ticket-stop-in-the-middle)
```
---

     
 
all -  [ ConversationRetrievalQA returns sources to questions without context ](https://www.reddit.com/r/LangChain/comments/17g231c/conversationretrievalqa_returns_sources_to/) , 2023-10-26-0909
```
Hi, 

I am wondering if anyone has a work around using ConversationRetrievalQA Chain (or alternative chains) to retrieve
 documents with their sources, and prevent the chain from returning sources for  questions without sources.   


Example
:  


    chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(),
        question_generator
=question_generator,
        combine_docs_chain=doc_chain,
    )
    
    chat_history = []
    query = 'What did the pr
esident say about Ketanji Brown Jackson'
    result = chain({'question': query, 'chat_history': chat_history})
    resul
t['answer']
    
    '''
    The president said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson, 
who is one of the nation's top legal minds ...
    
    SOURCES: /content/state_of_the_union.txt
    '''

Current Issue:
  


    query = 'How are you doing?'
    result = chain({'question': query, 'chat_history': chat_history})
    result['
answer']
    
    '''
    I'm doing well, thank you.
    
    SOURCES: /content/state_of_the_union.txt
    '''

&#x200B;

```
---

     
 
all -  [ Visiting Data Scientist from California looking for other DS for chat ](https://www.reddit.com/r/seoul/comments/17g0qax/visiting_data_scientist_from_california_looking/) , 2023-10-26-0909
```
Visiting Seoul for a week. Would like to have a chat about AI, LLMs, Langchain, and applications with other DS in Seoul.

```
---

     
 
all -  [ Retrieving politicians public promises from Hansard ](https://www.reddit.com/r/LangChain/comments/17g036o/retrieving_politicians_public_promises_from/) , 2023-10-26-0909
```
As the title says, I'm willing to embedded Hansard PDF documents.   
Since they're all Open Government data, I already c
ollected multiple years of House of Commons records  (Hansard)  


What I'm looking for is some kind of help to design t
he best architecture, so we can develop a tool for political leadership accountability. 

  
Thanks❣️  


The documents 
have multiple small paragraphs like those:

&#x200B;

 Mhairi Black rose—

Mr Speaker: Order. I always listen with the k
eenest

interest to the right hon. Gentleman. From now on,

however, interventions should be brief, and I think that

we
 have now treated adequately of the matter of South

Thanet.

Mhairi Black: I note the right hon. Gentleman’s point

of 
view. I invite him to come up and see Ferguslie Park,

where he will see what real deprivation looks like.

Alex Salmond
 (Gordon) (SNP): When I was listening

to the intervention of the right hon. Gentleman from

Surrey Heath—that other inc
redibly deprived area of

the south of England—I was struck by the Foreign

Secretary’s difficulty with language this mo
rning, when

he was trying to say:

“O wad some Power the giftie gie us

To see oursels as ithers see us!”
```
---

     
 
all -  [ Do You Use ChatGPT to Discover New SaaS Tools? ](https://www.reddit.com/r/LangChain/comments/17fkewk/do_you_use_chatgpt_to_discover_new_saas_tools/) , 2023-10-26-0909
```
Hey all,

I’ve found ChatGPT invaluable for boosting productivity. It’s not just about doing tasks faster; it’s also a g
oldmine for discovering new workflows and SaaS tools. For instance, it suggested Mailchimp and Substack when I was explo
ring newsletter growth.

Are you also using ChatGPT for this? Specifically, has it helped you discover new SaaS tools th
at you’ve actually implemented?  


I am creating a tool for Langchain that gives you context about what SaaS can be use
d to solve your problem, their features, pricing, etc... Would you find it useful for your chains?  


&#x200B;
```
---

     
 
all -  [ I'm Harrison Chase, CEO and cofounder of LangChain. Ask me anything! ](https://www.reddit.com/r/LangChain/comments/17ffvxo/im_harrison_chase_ceo_and_cofounder_of_langchain/) , 2023-10-26-0909
```
I'm Harrison Chase, CEO and cofounder of LangChain–an open-source framework and developer toolkit that helps developers 
get LLM applications from prototype to production.      


Hi Reddit! Today is LangChain's first birthday and it's been 
incredibly exciting to see how far LLM app development has come in that time–and how much more there is to go. Thanks fo
r being a part of that and building with LangChain over this last (wild) year.        


I'm excited to host this AMA, a
nswer your questions, and learn more about what you're seeing and doing.
```
---

     
 
all -  [ [Crosspost] IAMA with Harrison Chase, co-founder and CEO of LangChain: 9-11AM Pacific (12-2PM Easter ](https://www.reddit.com/r/IAmA/comments/17ffps3/crosspost_iama_with_harrison_chase_cofounder_and/) , 2023-10-26-0909
```
Join us TODAY, Tuesday, October 24th from 9-11 AM Pacific (12-2 PM Eastern) for an AMA hosted by Harrison Chase, co-foun
der and CEO of LangChain hosted by the [ LangChain subreddit](https://www.reddit.com/r/LangChain/).

This is your opport
unity to ask Harrison questions about utilizing LangChain in developing large language model (LLM) applications, and to 
share your own ideas and suggestions. Take advantage of this chance to learn more about how to leverage LangChain in you
r own projects and get insights into latest developments.

https://www.reddit.com/r/LangChain/
```
---

     
 
all -  [ Using Langchain With llama.cpp? ](https://www.reddit.com/r/LocalLLaMA/comments/17ffbg9/using_langchain_with_llamacpp/) , 2023-10-26-0909
```
I have Falcon-180B served locally using llama.cpp via the server REST-ful api.  I assume there is a way to connect langc
hain to the /completion endpoint.  

Does anyone have an example that does something like this?
```
---

     
 
all -  [ Custom Parser as argument to RetrivalQA ](https://www.reddit.com/r/LangChain/comments/17fenmv/custom_parser_as_argument_to_retrivalqa/) , 2023-10-26-0909
```
I have raw Jsons in the vectorized data. I am trying assign an instance of customer parser to RetrivalQA chain but getti
ng the error that no extra field allowed. Following is what not allowed :-  
I am not allowed to pass 'output\_parser': 
parser, to chain\_type\_kwargs

    rag_qa_pipeline = RetrievalQA.from_chain_type(
                            llm=llm,

                            chain_type='stuff',
                            retriever=custom_retriever,
                
            verbose=True,
                            chain_type_kwargs={
                                'output_parser
': parser,
                                'verbose': True,
                                'prompt': _prompt,
         
                       'memory': ConversationBufferMemory(
                                    memory_key='history',
   
                                 input_key='question',
                                     k=2),
                      
      }
                        )

Has anyone come accross any such situation? is there a way to assign a custom parser 
to RetrievalQA ?  

```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/17fd2eq/for_hire_programmerweb_developerit_consultant/) , 2023-10-26-0909
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ Prepare tables for LangChain? ](https://www.reddit.com/r/LangChain/comments/17fcc1z/prepare_tables_for_langchain/) , 2023-10-26-0909
```
Hi! I am totally new in LangChain and hyped for the possibilities.

I have seen some services that use langchain, but be
fore they use them in the client database, they can import, select and join tables to a better data quality preparation.
 

Is there any SaaS to do so? Thank you in advance!
```
---

     
 
all -  [ What framework to use? ](https://www.reddit.com/r/ChatGPTPro/comments/17f85es/what_framework_to_use/) , 2023-10-26-0909
```
Hello, i am just getting into ai. I am mindblown and overloaded with tons of information on different frameworks to work
 with OpenAIAPI like langchain, chatdev, xagent and autogen. My problem is that that  i can not understand which one sho
uld i use to implement multiple llms for my personal project. Because chatdev and autogen are very new and langchain is 
full of complex uncessary abstractions. Please, give me advice on the vector of my development. Do i need to learn some 
of these technologies or try to build my own framework of multiple ai gents using GPT API and what else should i learn f
or future development of llm based automatizations? Thank you, in advance
```
---

     
 
all -  [ can you embed csv files and pdf files in the same vector database? ](https://www.reddit.com/r/LangChain/comments/17f7wo6/can_you_embed_csv_files_and_pdf_files_in_the_same/) , 2023-10-26-0909
```
potentially a silly question...but can you embed csv files and pdf files in the same vector database?

trying to make a 
chatbot that you can talk to different file types 
```
---

     
 
all -  [ Information extraction from a huge PDF or HTML ](https://www.reddit.com/r/LangChain/comments/17f7qk6/information_extraction_from_a_huge_pdf_or_html/) , 2023-10-26-0909
```
I am working on a problem where I want to load a PDF or HTML page and  want to find some information out of that pdf or 
html. Now, I don’t want to store the vectors anywhere and I wanna do it in realtime as users will upload their file or h
tml page link and they should get the required information from the pdf on the fly. 

I have checked everywhere but didn
’t find a solution. Any help will be appreciated. Thanks
```
---

     
 
all -  [ What really is the point of LangChain / LangServe ](https://www.reddit.com/r/LangChain/comments/17f5oas/what_really_is_the_point_of_langchain_langserve/) , 2023-10-26-0909
```
So I have played around with LangChain for a couple weeks with different LLMs, such as GPT-4, Llama II, etc. It seems li
ke it is used for solving a particular type of tasks using available tools, either installed from the library or ChatGPT
 plugins.  


I feel like the need for a production-level software is not that high due to the following reason:

1. The
 ChatGPT plugin store already offers many tool options for different tasks.
2. ChatGPT offers customization now on indiv
idual accounts now. It can be served as chain of thought and as context to a newly opened conversation.
3. Having multip
le agents for one application is error prone and often end up with errors.

With the intro of AutoGen, a competitor of L
angChain, I just don't get what the end users want out of such frameworks that cannot be offered by ChatGPT.  


I have 
no intention of hurting feelings of any enthusiasts here. I've spent tremendous time digging into this too. I would like
 to learn what people really think of it and how LangChain can be used, really. 
```
---

     
 
all -  [ NiceGUI 1.4.0 with breaking changes, simplified use of ui.run_javascript, react-like ui.state and mo ](https://www.reddit.com/r/nicegui/comments/17f3t8u/nicegui_140_with_breaking_changes_simplified_use/) , 2023-10-26-0909
```
### New features and enhancements

- Make [JavaScript](https://nicegui.io/documentation#run_javascript) calls optionally
 awaitable
- Introduce [react-like `ui.state`](https://nicegui.io/documentation/refreshable#refreshable_ui_with_reactive
_state) to be used with `ui.refreshable`
- Move [Highcharts](https://nicegui.io/documentation/highcharts) dependency int
o a separate [nicegui-highcharts](https://github.com/zauberzeug/nicegui-highcharts) package to avoid the need for a lice
nse for commercial projects
- allow sign-up at https://on-air.nicegui.io/login to get a fixed [On Air](https://nicegui.i
o/documentation#nicegui_on_air) URL and the possibility to protect remote access with a passphrase (this is a tech previ
ew of our upcoming [On Air](https://nicegui.io/documentation#nicegui_on_air) service and is free of charge until the end
 of the year if you sign up now)
- Refactor `globals` module
- Use FastAPI's new `lifespan` API
- Use flex layout per de
fault for layout elements
- Replace netifaces with much simpler (and better) ifaddr
- Convert [`ui.timer`](https://niceg
ui.io/documentation/timer) into an element
- Update httpx dependency (#1820 by @tscheburaschka, @falkoschindler)
- Consi
stently mark methods private if not part of the public API
- Remove deprecated APIs

### Bugfixes

- Fix [AG Grid](https
://nicegui.io/documentation/aggrid) bug with hidden cells by upgrading to new version

### Documentation

- Add LangChai
n handler to the ['Chat with AI' example](https://github.com/zauberzeug/nicegui/blob/main/examples/chat_with_ai/main.py)


### Breaking changes and migration guide

#### No need to await JavaScript calls

When using `run_javascript`, `run_me
thod`, `call_api_method` and `call_column_api_method`,
you can decide whether the client should respond with a return va
lue or not by awaiting the method call or not.
The method will automatically inform the client.
The `respond` parameter 
of `run_javascript` is not used anymore. See https://nicegui.io/documentation/run_javascript

#### `ui.chart` is now `ui
.highchart` and requires the package 'nicegui-highchart'

[Highcharts](https://nicegui.io/documentation/highcharts) requ
ires you to buy a license for commercial products if the code is installed on your machine.
That's why we made it an opt
ional package.
Install with `pip install nicegui[highcharts]`.

#### The `globals` module is gone

We removed the ugly `
globals` module, which was never intended to be public API,
but might have been used nonetheless.

- If you need the app
 configuration, use `app.config` instead.
- If you need the current client or slot, use the `context` module instead.
- 
If you need the client dictionary, use `Client.instances` instead.

#### FastAPI's new lifespan API

Since FastAPI's `@o
n_event('startup')` and `@on_event('shutdown')` are deprecated,
NiceGUI switched to the new lifespan API.
You can still 
use `app.on_startup()` and `app.on_shutdown()`.

#### Layout elements use flex layout by default

Before you needed to u
se `ui.column` inside, e.g., `ui.tab_panel` and other elements to get proper alignment, padding and spacing.
Now most UI
 elements provide reasonable default so that the content looks like in a `ui.row` or `ui.column`.

### Upgraded third-pa
rty dependencies

- vue: 3.3.4 → 3.3.6
- quasar: 2.12.2 → 2.13.0
- tailwindcss: 3.3.2 (unchanged)
- socket.io: 4.7.1 → 4
.7.2
- es-module-shims: 1.7.3 → 1.8.0
- aggrid: 30.0.3 → 30.2.0
- echarts: 5.4.3 (unchanged)
- mermaid: 10.2.4 → 10.5.1

- nipplejs: 0.10.1 (unchanged)
- plotly: 2.24.3 → 2.27.0
- three: 0.154.0 → 0.157.0
- tween: 21.0.0 (unchanged)
- vanill
a-jsoneditor: 0.18.0 → 0.18.10
```
---

     
 
all -  [ gpt4docstrings: Automatically generate docstrings for entire projects using ChatGPT ](https://www.reddit.com/r/ChatGPTPro/comments/17exp69/gpt4docstrings_automatically_generate_docstrings/) , 2023-10-26-0909
```
gpt4docstrings is a Python library that allows you to generate docstrings for undocumented functions / classes. In this 
example, I'm applying the tool to a module inside the langchain repository.

Repo: [https://github.com/MichaelisTrofficu
s/gpt4docstrings](https://github.com/MichaelisTrofficus/gpt4docstrings)

https://reddit.com/link/17exp69/video/eybtzt248
1wb1/player
```
---

     
 
all -  [ Understanding nr. of LLM requests in standard ReAct Agent ](https://www.reddit.com/r/LangChain/comments/17evn6q/understanding_nr_of_llm_requests_in_standard/) , 2023-10-26-0909
```
Okey, so I'm trying to clarify that I understand the number of LLM calls a typical ReAct Agent makes when using tools su
ch as Google and Wikipedia. I will mark the need for an **LLM call with bold text**. So consider the example from the La
ngChain documentation:

'Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?'

\> Enteri
ng new AgentExecutor chain...I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to th
e 0.43 power. **<-- LLM CALL (finds out what to do)**  
Action: Search **<-- LLM CALL (find out what function to use and
 which input)**  
Action Input: 'Leo DiCaprio girlfriend'  
Observation: model Vittoria Ceretti **<-- LLM CALL (break do
wn the output from the Search to an observation)**  
Thought: I need to find out Vittoria Ceretti's age **<-- LLM CALL (
thought of what to do next)**  
Action: Search **<-- LLM CALL (find out what function to use and which input)**  
Action
 Input: 'Vittoria Ceretti age'  
Observation: 25 years **<-- LLM CALL (break down the output from search to an observati
on)**  
Thought: I need to calculate 25 raised to the 0.43 power **<-- LLM Call (...)**  
Action: Calculator **<-- LLM C
all (...)**  
Action Input: 25\^0.43  
Observation: Answer: 3.991298452658078 **<-- LLM Call (...)**  
Thought: I now kn
ow the final answer **<-- LLM Call (...)**  
Final Answer: Leo DiCaprio's girlfriend is Vittoria Ceretti and her current
 age raised to the 0.43 power is 3.991298452658078. **<-- LLM Call (...)**

\> Finished chain.

I'm not sure if this is 
the right way of understanding it? I'm trying to figure out where in the Thought -> Action -> Observation the LLM is inv
olved. Is it one call per (Thought/Action/Observation)? Assume that the Action does not include extra LLM calls but that
 it is a Search on Google or Wikipedia and not RAG. Does the Google and Wikipedia tool include a LLM to summarise what i
t found?

I'm a bit unsure about this, any thoughts?
```
---

     
 
all -  [ Passing custom stopping strings to ZeroShotAgent? ](https://www.reddit.com/r/LangChain/comments/17eqlhp/passing_custom_stopping_strings_to_zeroshotagent/) , 2023-10-26-0909
```
I'm currently using a variant of the Mistral model with Langchain. It works ok however I am getting <|im_end|> back at t
he end of the responses.  I'm using LlamaCPP so without agents I can do something like: 

    llm = LlamaCpp(
        mo
del_path='/home/fleabs/ai/text-generation-webui/models/dolphin-2.1-mistral-7b.Q4_K_M.gguf',
        n_gpu_layers=35,
   
     n_batch=256,
        n_ctx=8192,
        callback_manager=callback_manager,
        verbose=True,
        temperatu
re=0.0,
        max_tokens=2000,
        top_p=0.2,
        top_k=10,
        repeat_penalty=1.2,
        stop=['<|im_en
d|>'],
    )

To pass a custom stopping string in. However when I try this with a ZeroShotAgent I get an error about sto
p being set multiple times:

> raise ValueError('`stop` found in both the input and default params.')
> ValueError: `sto
p` found in both the input and default params.

I'm guessing langchain is setting the stop tokens for the agent. Does an
yone know how I can pass <|im_end|> as a stop word with the agent?

I tried setting it like this: 

    agent = ZeroShot
Agent(max_iterations=3, llm_chain=llm_chain, tools=tools, verbose=True, stop=['<|im_end|>'])

But it doesn't seem to wor
k. Any advice much appreciated!
```
---

     
 
all -  [ Resume Review please...I will be graduating in a few months. Tired of seeing 'we will not be able to ](https://i.redd.it/s9ehht8yczvb1.jpg) , 2023-10-26-0909
```
Also if you have any suggestions on which job roles I should target or what technologies should I learn/make projects on
 please feel free to add.
Thanks in advance!
```
---

     
 
all -  [ [Local Llama] Problème avec l'hébergement de modèles avec Fastapi ](https://www.reddit.com/r/redditenfrancais/comments/17en6tj/local_llama_problème_avec_lhébergement_de_modèles/) , 2023-10-26-0909
```
J'ai utilisé les fonctions Load_Quant et Load_Model à partir du TextGen WebUI pour charger les modèles WizardLM-30B-GPTQ
 dans Langchain.

Je suis en mesure d'inviter le pipeline Langchain pour obtenir des sorties.

Mais, j'ai essayé de char
ger ce pipeline et de l'utiliser via un point de terminaison FastAPI, dans l'espoir d'envoyer l'invite en tant que deman
de de post, mais ici, je reçois une erreur CUDA hors de la mémoire.

Une raison à cela?

Traduit et reposté à partir de 
la publication https://www.reddit.com/14gydpv
```
---

     
 
all -  [ What's the best experience you've had with a chatbot? ](https://www.reddit.com/r/LangChain/comments/17ekndx/whats_the_best_experience_youve_had_with_a_chatbot/) , 2023-10-26-0909
```
Barring ChatGPT, Bard, etc what other commercial chatbots have provided a great experience in terms of UX?

I feel like 
there's so little in actual production, and what is out there is awful.
```
---

     
 
all -  [ Training a model on French Law, any insights? ](https://www.reddit.com/r/LocalLLaMA/comments/17ejzx1/training_a_model_on_french_law_any_insights/) , 2023-10-26-0909
```
# We were looking to train our first LORA model and had this idea of using french Labor Laws (Code du Travail) as a basi
s for a dataset.

**The 'product' would be a query-oriented conversational model, able --in its limited and dutifuly-dis
claimed-to-users capacities-- to reply to simple questions like «*****Is my boss allowed to force me to install a tracke
r on my phone in order to verify where I am when I'm working remote?*****', in French of course.**

&#x200B;

**Why is i
t |fun|?**

* **Human-hard level texts** The law is jargonous and confusing for simple folks. There's a challenge to hav
e an LLM understand it. And a bonus for humans if it works.
* **Social impact**. Not everyone can afford legal help, so 
it's Tech-For-Good approved.
* **Hacking the law**. C'me on. If that ain't fun?
* **Future opportunities.** Once we get 
it to work on that 'part of the law', we could try to expand to other legal topics.

&#x200B;

**Why do you care?**

**T
here are several options before us and we're not sure about the most efficient way to operate.** I'm coming here for adv
ices and opinions, feel free to throw everything you think at us :)

&#x200B;

**A/ The first question is: what's the ea
siest and most efficient way to do it today?**

We can use a LORA of sort, but there's also Langchain for example. Which
 option would be best at the moment in the constantly evolving landscape?

&#x200B;

**B/ The next problem is probably: 
how to build that dataset?**

We have the PDF document transformed into text and hierarchical YAML, but it's just a star
t.

My first idea was to use a summary model in order to get 'simplified' texts to use as answers. but it turns out the 
French summary models on HuggingFace are not very good at it. Our domain texts are not  news article from CNN translated
 in French.

We know how datasets matter, so there's really a lot we want to hear about that.

&#x200B;

**C/ And then, 
there's the question: on which model do we train the LORA?**

There are models like Vigogne which are supposedly good at
 French, but we're not so sure about which to pick.

One problem is: has the exisiting model been trained on the similar
 tokens set as the one from our text?

In other words, will the LLAMA/Vigogne/Falcon/other model be able to understand o
ur lexical field, e.g. legal language?

My testing is worrysome, as using the tokenizer of some models like vigogne or c
ustomised LLAMAs on the text we're considering, I get 1M+ tokens in the resulting set. While the model's vocab is only 6
4k or 32k high. Big Discrepancy.

Any idea / experience about that?

&#x200B;
```
---

     
 
all -  [ ER-Daigram Integration with Chatbots ](https://www.reddit.com/r/LangChain/comments/17edosb/erdaigram_integration_with_chatbots/) , 2023-10-26-0909
```
Hey everyone, I am looking for making a chatbot type application wherein given the ER diagram of a whole database user c
an ask questions related to it, like how all tables are connected, etc. This is just an idea that popped in my mind. Ple
ase do give your helpful suggestions and idea. Thanks.
```
---

     
 
all -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-10-26-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
all -  [ Add LangChain to my opensource project SolidGPT -> chat with your codebase directly just like ChatGP ](https://www.reddit.com/r/LangChain/comments/17e4aif/add_langchain_to_my_opensource_project_solidgpt/) , 2023-10-26-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT)

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always 
give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, e
asily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to colla
borate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.  



https://preview.redd.it/69s4104frtvb1.png?width=3012&format=png&auto=webp&s=198447a992955b8c739416554b5972dd33c048e0
```
---

     
 
all -  [ ChatRepo - chat with your codebase directly just like ChatGPT Resources ](https://www.reddit.com/r/foss/comments/17e491l/chatrepo_chat_with_your_codebase_directly_just/) , 2023-10-26-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT)

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always 
give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, e
asily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to colla
borate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.

htt
ps://preview.redd.it/f4yi0vk1rtvb1.png?width=3012&format=png&auto=webp&s=e22025e7bde28eeb699220e3b6cd7a63b5e6d922

&#x20
0B;

Let me know what's your thought about my open source project!
```
---

     
 
all -  [ Chat with the codebase by GPT3/4 ](https://www.reddit.com/r/GPT3/comments/17e46jn/chat_with_the_codebase_by_gpt34/) , 2023-10-26-0909
```
My open source project SolidGPT just release the v0.2.6, 

and I add a **New feature - Chat everything with your code re
pository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input new requirements and
 have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your understanding.
* Deploy
 everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/SolidGPT) 

**Privat
e Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always give the answer de
eply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, easily deploy local
ly, charge your date by your own.

I'm diligently exploring more practical methods for people to collaborate with LLM Ag
ents. The goal is to enhance our development processes and empower every tech enthusiast with AI.

https://preview.redd.
it/m94j0rufqtvb1.png?width=3012&format=png&auto=webp&s=ad7193dad33ca023ff98382fd101b3f84776b24f

&#x200B;

Let me know w
hat's your thought about my open source project, THank you!
```
---

     
 
all -  [ ChatRepo - chat with your codebase directly just like ChatGPT ](https://www.reddit.com/r/ChatGPT/comments/17e43jj/chatrepo_chat_with_your_codebase_directly_just/) , 2023-10-26-0909
```
My open source project SolidGPT just release the v0.2.6, by using GPT4 model

and I add a **New feature - Chat everythin
g with your code repository**

In SolidGPT v0.2.6. We can do:

* Ask questions about any part of the codebase.
* Input n
ew requirements and have SolidGPT provide a coding plan.
* Seek clarity on any section, and let SolidGPT guide your unde
rstanding.
* Deploy everything locally

GitHub: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/S
olidGPT) 

**Private Solution**

Integrate with LangChain to let LLM agent scan and learning the code repository, always
 give the answer deeply base on your codebase content

**Deploy Locally**

Integrate with FastAPI and using the Docker, 
easily deploy locally, charge your date by your own.

I'm diligently exploring more practical methods for people to coll
aborate with LLM Agents. The goal is to enhance our development processes and empower every tech enthusiast with AI.

ht
tps://preview.redd.it/2dt89nxsptvb1.png?width=3012&format=png&auto=webp&s=8ea89eff3511b51f0381b7da080441ae16b1e531

&#x2
00B;

Let me know what's your thought about my open source project! 
```
---

     
 
all -  [ How do I integrate multiple expert agents? ](https://www.reddit.com/r/LangChain/comments/17dz0fr/how_do_i_integrate_multiple_expert_agents/) , 2023-10-26-0909
```
Hi guys, I've been working with LLM's for a while now, and looking into building a new project which has some functional
ity I haven't figured out yet, how to do in the best way. I want to be able to handle multiple expert agents, which migh
t even use different language models.

How would you guys approach the following use case?

**I want to create a chatbot
 that consists of several helper agents, each with its own specialty. Here's how it works:**

1. The user sends a messag
e to the main agent (let's call it the 'Planner Agent').
2. The Planner Agent decides on a plan to fulfill the user's re
quest.
3. It then checks if any of its helper agents (like Expert Agent A, B, or C) can handle parts of that plan.
4. If
 a helper agent can do a task, it might ask the user for more details to get the job done.
5. Once all tasks are complet
ed, the Planner Agent confirms with the user that everything went smoothly.

**Example Use Case: Imagine you're using a 
travel planning chat agent.**

1. You tell the main agent (Planner Agent) that you want to plan a trip to Paris.
2. Plan
ner Agent creates a plan: (a) Book flights, (b) Find hotels, (c) Suggest tourist spots.
3. Expert Agent A, who specializ
es in flights, then asks you for your preferred travel dates.
4. Expert Agent B, the hotel guru, inquires about your bud
get and desired amenities.
5. Expert Agent C, the sightseeing expert, asks about your interests—like art, history, or ad
venture.
6. After gathering all the info, the Planner Agent presents you with a complete travel itinerary and asks for y
our approval.
```
---

     
 
all -  [ Write pandas prompt using React ](https://www.reddit.com/r/LangChain/comments/17dyhi5/write_pandas_prompt_using_react/) , 2023-10-26-0909
```
Hi, I am very new to langchain and trying to build a prompt using React thought and reasoning template, just wanted to u
nderstand if is it possible to make the llm's learn how to query custom tasks using pandas? For example, I want to build
 a prompt that teaches llms to carry out a multi step task using pandas agent.
```
---

     
 
all -  [ Integrating Chat History Sessions with Langchain Python, Mistral, and Choosing the Right Database ](https://www.reddit.com/r/LangChain/comments/17dr55p/integrating_chat_history_sessions_with_langchain/) , 2023-10-26-0909
```
 I am a beginner creating a website for a chatbot using Langchain Python and Mistral. I want to add chat history session
s similar to those in ChatGPT or Bard, etc. Should I use Supabase, PostgreSQL, or MongoDB? Additionally, could someone d
irect me towards any resources because I am new to web development too? 
```
---

     
 
all -  [ Input query parsing in a conversational chain ](https://www.reddit.com/r/LangChain/comments/17dpb2w/input_query_parsing_in_a_conversational_chain/) , 2023-10-26-0909
```
Hi there!

I have a similar question to this [reddit post](https://www.reddit.com/r/LangChain/comments/1420v8c/input_que
ry_parsing/) but my question has a different use case.

In layman terms, if I have a query that says: 'Give me 5 UK base
d companies that are building houses' I'd like for the retriever filter to contain 'country = 'UK''

I've seen the 'Self
Query' retriever which takes in a list of AttributeInfo so that it can parse the query from the input text it receives. 
However, I'd like to do the same but in a ConversationalChain.  


It seems like I cannot simply swap out my normal (pin
econe) retriever for a selfquery retriever and hope that it works out...but as someone who's very new to the framework I
 might be wrong. It doesn't seem to return any results.  


So my question is, should it be just as easy as providing th
e self query retriever to my conversational chain  


>***self\_query\_retriever = SelfQueryRetriever.from\_llm(***  
**
*llm,***  
***vector\_store,***  
***'',***  
***self.get\_content\_meta\_data\_field\_info(), # returns a list of attri
bute info fields, i.e. country***  
***verbose=True***  
***)***   
***return*** **ConversationalRetrievalChain.from\_ll
m(**  
 **llm=llm,**  
 **memory=memory,**  
 **retriever=self\_query\_retriever,**  
 **verbose=True,**  
 **return\_so
urce\_documents=True**  
 **)**

or, should I be using some part of LangChain that I don't know of that generates the fi
lters from the query, which I can then use in my (Pinecone) retriever:  


&#x200B;

>***filter = 'parse\_structured\_fi
lter\_from\_query(query)***  
***return*** **ConversationalRetrievalChain.from\_llm(**  
 **llm=llm,**  
 **memory=memor
y,**  
 **retriever='make pinecone retriever with filter',**  
 **verbose=True,**  
 **return\_source\_documents=True** 
 
 **)**
```
---

     
 
all -  [ AWS OpenSearch serverless ](https://www.reddit.com/r/aws/comments/17dp8m8/aws_opensearch_serverless/) , 2023-10-26-0909
```
I have an issue with AWS OpenSearch serverless that has me stumped. 

I’m trying to do something very simple. Using lang
chain load some docs into a OS Serverless vector store. 

I can connect to the vector database. When I try to write the 
docs to an index, it creates the index but can’t write the docs to the index. It returns a 404.

I created a wide open d
ata access control policy. So the principal has full grant on the collection and full grant on wildcarded indexes. 

The
 principle is an IAM user with a full admin policy. I will tighten all of this, but for the sake of testing this is the 
easiest.

Does anybody have any idea what could cause the 404? What am I missing?
```
---

     
 
all -  [ Setting up Local File store cache for embeddings when using Agents ](https://www.reddit.com/r/LangChain/comments/17dngme/setting_up_local_file_store_cache_for_embeddings/) , 2023-10-26-0909
```
I am developing an agent that fetches text data from an AWS s3 bucket but I’m thinking If I setup a local cache for stor
ing embeddings(I did this when using retrieval chains) response would be faster.
Has anyone done this before?
```
---

     
 
all -  [ Writing your own abstraction rather than using langchain ? ](https://www.reddit.com/r/LangChain/comments/17dmxam/writing_your_own_abstraction_rather_than_using/) , 2023-10-26-0909
```
Hi Everyone, so I am relatively new to LangChain and struggling to see the point of it all. I have tried to go through d
ocumentation and for even the simplest of tasks it is too complicated.

So my question to you all is, is there any point
 of using langchain rather than having your own abstraction frameworks ??
```
---

     
 
all -  [ Best VectorDb to store 500+ docs ](https://www.reddit.com/r/LangChain/comments/17dlj9x/best_vectordb_to_store_500_docs/) , 2023-10-26-0909
```
I am trying to build an QnA app on over 500 docs (about 15-20mb each). What would be the best way to do this. I have tri
ed pinecone but it seems quite slow while embedding. What other options are suited to my requirements. Also while indexi
ng, I’m looping over each doc, is there a better way to do it?
```
---

     
 
all -  [ Built it for my project at first: Memorybase.io supercharges ChatGPT with memory capabilities for yo ](https://www.reddit.com/r/learnmachinelearning/comments/17dl1bw/built_it_for_my_project_at_first_memorybaseio/) , 2023-10-26-0909
```
Hey everyone!

I've been delving deep into chatbots lately, especially with the ChatGPT API, and I found an issue that's
 probably familiar to many of you: ChatGPT doesn't inherently have memory capabilities. For many applications, that's pe
rfectly fine, but for those of us who are trying to create a more context-aware and dynamic conversation flow, this limi
tation is quite apparent.

I faced this challenge in one of my projects and realized that there had to be a better way t
o integrate context and memory into ChatGPT's conversations. So, I built something for myself which I thought might be u
seful for many of you as well. Allow me to introduce you to [**Memorybase.io**](http://memorybase.io/).

Memorybase is a
 developer-friendly API that's designed to seamlessly integrate memory functionality into the ChatGPT API. By harnessing
 the power of the Pinecone vector database and LangChain, Memorybase wraps around the ChatGPT API and ensures that the r
ight context and memory are injected into each query. This means that your chatbot can remember previous interactions, p
references, or any other context that's relevant for more engaging and meaningful conversations.

Imagine a user asking 
your chatbot about movie recommendations. The next day, they come back and reference that conversation, expecting the bo
t to remember. With Memorybase, that continuity becomes possible. The user experience improves manifold, and the possibi
lities for more sophisticated and context-aware bots increase tremendously.

I originally built Memorybase for my own ne
eds. But the more I used it, the more I realized that this could have broader applications. Any developer looking to lev
erage the ChatGPT API could potentially benefit from the enhanced memory and context capabilities. From customer support
 bots to interactive storytelling, the potential use cases are vast.

This technology stack (pinecone/langchain) is not 
complex or ‘new’ per se, but for application developers who aren’t interested in managing it or hosting it, this could b
e a useful hassle-free option for your projects.

I've set up a page over at [memorybase.io](https://memorybase.io/) whe
re you can learn more about how it works and see if it aligns with your needs. I would love for you to check it out and 
share your thoughts. Your feedback, insights, and potential use cases would be invaluable as I continue to refine and ex
pand the capabilities of Memorybase.

Thanks for reading, and I'm eager to hear your thoughts and see where Memorybase c
an fit into the exciting world of chatbots!
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-10-26-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-10-26-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-10-26-0909
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-26-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-10-26-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-26-0909
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-26-0909
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-10-26-0909
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-10-26-0909
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-10-26-0909
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-26-0909
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
