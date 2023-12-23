 
all -  [ Ashamed to asked ](https://www.reddit.com/r/LangChain/comments/18opwbl/ashamed_to_asked/) , 2023-12-23-0909
```
kind of ashamed to ask but what am i missing here ?. the cash\_flow\_data method returns a list of cash flow statements 
in the form of dataframes, then i try to map each iteration to the prompt template but thats not working. instead i get 
this error. Any ideas why? u/hwchase17 . 

https://preview.redd.it/6o8c00uy2x7c1.png?width=2336&format=png&auto=webp&s=6
2d403052114c9de56573f1a85b4306497c23599

https://preview.redd.it/r36pe0uy2x7c1.png?width=2336&format=png&auto=webp&s=897
67aa7dbb3a4a2406229bc9611078ef0f4915d
```
---

     
 
all -  [ Bedrock Claude Performance Issue ](https://www.reddit.com/r/LangChain/comments/18opvla/bedrock_claude_performance_issue/) , 2023-12-23-0909
```
Anybody have any idea what I might be doing wrong here?

    const claudeBedrock = new Bedrock({model: 'anthropic.claude
-v2:1',region: aws_region,modelKwargs: {temperature: 0.0,top_k: 250,top_p: 0.999,stop_sequences: ['Human:'],max_tokens_t
o_sample: maxTokens}}
    
    const chain = = new LLMChain({llm: claudeBedrock, prompt: prompt})

I have tried .`call`,
 .`_call`, .`invoke`, .`predict` and they all produce worse results than through the AWS console.

I have verbose ON and
 literally copy and pasting the logged prompt produced by Langchain into the Bedrock playground and it produces better r
esults.

I tried both Chat & Text in playgrounds using the EXACT same settings as above.

The prompt is asking Claude to
 classify a list of something. I have tried multiple times on both sides and the output through Langchain is WORSE by in
cluding results that is wrong. The console produces correct results everytime.

It's driving me nuts that I'm about to t
ear out Langchain and use AWS's SDK instead.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Is there a way in LC to centralize event notifications and configurations? ](https://www.reddit.com/r/LangChain/comments/18om6xq/is_there_a_way_in_lc_to_centralize_event/) , 2023-12-23-0909
```
https://www.youtube.com/watch?v=D34PyNx71vk

The YouTube video shares an architectural difference between LangChain and 
Microsofts orchestrator. Is there really no way to do the same in LangChain?
```
---

     
 
all -  [ [Langchain] Quelle est la différence entre l'agent des fonctions OpenAI et l'agent multi-fonctions O ](https://www.reddit.com/r/redditenfrancais/comments/18oinsw/langchain_quelle_est_la_différence_entre_lagent/) , 2023-12-23-0909
```
J'ai lu le Doc entier plusieurs fois et j'ai finalement fini par lire le code source, mais je ne sais toujours pas quell
e est la différence entre ces deux agents.

Si quelqu'un a une explication, je serai reconnaissant.

Traduit et reposté 
à partir de la publication 14nreov de la communauté langchain. Pour retrouver la publication originale, insérez l'id de 
la publication après 'reddit.com/'
```
---

     
 
all -  [ How do Callbacks for streaming response exactly work? (In Streamlit application) ](https://www.reddit.com/r/LangChain/comments/18ogw3p/how_do_callbacks_for_streaming_response_exactly/) , 2023-12-23-0909
```
Hi,

I'm currently trying to implement my RAG application in Streamlit without the use of LangChain for various reasons,
 however i have a problem to get the streaming response right for my LLM (AWS SageMaker endpoint).

The previous approac
h that works is passing a custom Streamhandler (that takes the streamlit container) to the Chain that overrides the on\_
llm\_new\_token method (writes to the container with every call of the method) and modifying the sagemaker\_endpoint.py 
that it calls the method for every Token i get from the Event Stream. 

As seen here: [https://github.com/langchain-ai/c
hat-langchain/issues/39](https://github.com/langchain-ai/chat-langchain/issues/39)

&#x200B;

Now when trying to get thi
s to work without LangChain i only get empty responses.

I call the endpoint via boto3 client and successfully get a res
ponse stream. However when iterating with the TokenIterator nothing happens. This approach would work in a normal python
 script with writing to the console but not within my Streamlit application.

    def call_llm(prompt, container):
     
   response = boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
         
       )
        print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for toke
n in TokenIterator(response['Body']):
            current_completion += token
            print(token) # Nothing happens
 here
            container.markdown(current_completion) # Nothing happens here either

Same problem when i create a str
eam\_handler class (not inherited from the LangChain BaseCallbackHandler) with the corresponding method. I don't really 
understand how the Callbacks work within LangChain. It seems like i can't get the same behaviour if i code it myself.

 
   def call_llm(prompt, stream_handler): # Give a streamhandler with corresponding container instead
        response = 
boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
                )
     
   print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for token in TokenIter
ator(response['Body']):
            current_completion += token
            print(token) # Nothing happens here
        
    stream_handler.on_llm_new_token(current_completion) # Nothing happens here                         
        either


I'd be very thankful for a workaround or an explanation how the Callbacks work in LangChain.
```
---

     
 
all -  [ LangChain State of AI 2023 ](https://blog.langchain.dev/langchain-state-of-ai-2023/) , 2023-12-23-0909
```

```
---

     
 
all -  [ [Local Llama] Comment exposer un modèle dans une API? ](https://www.reddit.com/r/redditenfrancais/comments/18od590/local_llama_comment_exposer_un_modèle_dans_une_api/) , 2023-12-23-0909
```
J'ai un PC avec un RTX 3090 et je voudrais l'utiliser pour des modèles comme LLAMA2. Je voudrais ouvrir un port et offri
r la puissance d'inférence de ce PC à d'autres applications exécutant Langchain en dehors du réseau domestique.

J'ai pe
nsé à combiner fastapi avec le package local HF, mais je crois qu'il existe d'autres options beaucoup mieux.

Traduit et
 reposté à partir de la publication 15qs2br de la communauté localllama. Pour retrouver la publication originale, insére
z l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ How to use LLM response stream without LangChain ](https://www.reddit.com/r/StreamlitOfficial/comments/18od2xf/how_to_use_llm_response_stream_without_langchain/) , 2023-12-23-0909
```
Hi,

I developed a little RAG application and now i want to rebuild most parts without using LangChain for various reaso
ns.

I'm using a SageMakerEndpoint from AWS as my LLM. It was pretty difficult to get the response stream to work with L
angChain, now i have a similiar problem when i try the same without LangChain.

&#x200B;

The solution with LangChain is
 described here: [https://github.com/langchain-ai/chat-langchain/issues/39](https://github.com/langchain-ai/chat-langcha
in/issues/39)

It's pretty straightforward. We have to create a CallbackManager that takes the container and writes on e
very new token. However i don't really understand why we need that in the first place?

My attempt was to implement the 
TokenIterator from here:

[https://aws.amazon.com/de/blogs/machine-learning/stream-large-language-model-responses-in-ama
zon-sagemaker-jumpstart/](https://aws.amazon.com/de/blogs/machine-learning/stream-large-language-model-responses-in-amaz
on-sagemaker-jumpstart/)

pass the container to my llm-call function like this:

    def call_llm(prompt, container):
  
      response = boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
      
          )
        print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for t
oken in TokenIterator(response['Body']):
            current_completion += token
            print(token) # Nothing happ
ens here
            container.markdown(current_completion) # Nothing happens here either

The same code works in a norm
al python application. I guess streamlit just works in a different way i don't understand yet.

I tried the same approac
h with a StreamHandler (writing my own instead of using LangChain). I passed the stream handler with the container to th
e function and called the overwritten on\_new\_llm\_token method inside the TokenIterator loop. Thats the same approach 
as in the solution described just without inheriting from the BaseCallBackHandler from LangChain. This doesn't work eith
er.

THe LangChain approach would be to write your own StreamHandler that overwrites the BaseCallBackHandler. However i 
don't see why this approach works and my own doesn't. What makes the LangChain CallbackHandler so 'special'. I'm probabl
y overseeing something here.

&#x200B;

Thank you for your help
```
---

     
 
all -  [ [Langchain] L'ingénierie rapide semble être une conjecture - comment évaluer correctement l'applicat ](https://www.reddit.com/r/redditenfrancais/comments/18obpkw/langchain_lingénierie_rapide_semble_être_une/) , 2023-12-23-0909
```
Comment les gens évaluent-ils la qualité de vos applications LLM? Je gère un chatbot en santé mentale en production (pet
ite échelle - 10 utilisateurs actifs) et j'ai passé beaucoup de temps à des invites en train de mener, mais ce n'est que
 des conjectures.

Je vais faire un ajustement à l'invite et exécuter quelques conversations de test et obtenir un peu l
es vibrations de savoir si c'est mieux ou pire qu'avant le toit. Est-ce ce que vous faites aussi ou est-ce que je manque
 quelque chose ???

Traduit et reposté à partir de la publication 164ey51 de la communauté langchain. Pour retrouver la 
publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Langchain returns similarity_search_with_relevance_scores in negative ](https://www.reddit.com/r/LangChain/comments/18o9afp/langchain_returns_similarity_search_with/) , 2023-12-23-0909
```
Guys, I'm doing a similarity search and using relevance scores because I understand relevance scores return scores betwe
en 0 and 1. However when I use Langchain to return these scores, they come back in negatives. However when I use custom 
code for chroma or faiss, I get scores between 0 and 1. Is this a bug in Langchain, pls help.
```
---

     
 
all -  [ Get time needed for individual components of ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/18o2r72/get_time_needed_for_individual_components_of/) , 2023-12-23-0909
```
Hi all,

Is there a way I can get the time needed for each individual components of ConversationalRetrievalChain?

For e
g, how do I get the time needed for the LLM to generate a reply?
```
---

     
 
all -  [ My import of FAISS is not recognized in my IDE ](https://www.reddit.com/r/pythonhelp/comments/18o2obg/my_import_of_faiss_is_not_recognized_in_my_ide/) , 2023-12-23-0909
```
I'm testing a code from a tutorial to see if i can integrate its concept into mine. But for some reason when I type impo
rt FAISS like below it just stays white unline the rest of the imports in the IDE. I dont know why its not recognized, I
ve traied pip install langchain, pip install faiss-cpu, pip install 'langchain\[all\]', and I looked at the documentatio
n. I am not sure whats causing this and any help is appreciated

    from dotenv import load_dotenv
import streamlit as 
st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.open
ai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    load_dotenv()
    st.set_page_confi
g(page_title='Ask your pdf')
    st.header('Ask your PDF')

    pdf = st.file_uploader('Upload your pdf', type='pdf')

 
   if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
     
       text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator='\n',
         
   chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )

        chunks = tex
t_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, e
mbeddings)

        user_question = st.text_input('ask a question about your pdf: ')



if __name__=='__main__':
    mai
n()

&#x200B;
```
---

     
 
all -  [ How to pass some arguments to function call via code and some extracted from LLM? ](https://www.reddit.com/r/LangChain/comments/18nzw4v/how_to_pass_some_arguments_to_function_call_via/) , 2023-12-23-0909
```
I have the following:  
I want to be able to use agents and pass one argument programmatically. I ideally dont want that
 in prompt.

    def testFunc(text1, email):
        print(text1)
        print(email)
    
    
    tools = [
    Struc
turedTool.from_function(
 func=testFunc,
 name='testing',
 args_schema=TestSchema,
 description='tester',
 return_direct
=True,

 )
]
    
    model_with_tools = model.bind(
        functions=[format_tool_to_openai_function(t) for t in tools
],
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', template),
            Messages
Placeholder(variable_name='chat_history'),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
          
  ('user', '{input}'),
        ]
    )
    agent = (
        {
            'input': lambda x: x['input'],
            'a
gent_scratchpad': lambda x: format_to_openai_function_messages(
                            x['intermediate_steps']
    
                    ),
            'chat_history': lambda x: x['chat_history'],
            'email': lambda x: x['email'
],
        }
        | prompt
        | model_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )
    
    age
nt_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, return_intermediate_steps=True
    )
    
 
   result = agent_executor.invoke(
                {'input': 'this is the test code', 'chat_history': [], 'email': 'TEST
@GMAIL.COM'}
            )

I want the output to be 

    this is the test code
    TEST@GMAIL.com

Basically I want the
 email to be passed programmatically and the other arguments to be passed using the LLM. I cant figure this out. Have be
en going at it for a while. No matter what, the function is being called with the prompt, which doesnt have the email an
d it is hallucinating the email as [user@example.com](mailto:user@example.com)  


Is there no way to pass the email to 
the function, maybe a additional kwarg thing or extra configs or something?  
After the prompt part of the chain ends, I
 can see the part entering the LLM is:  


     'kwargs': {           'content': this is the test code',           'addi
tional_kwargs': {}         } 
```
---

     
 
all -  [ Errors using SQL Agent ](https://www.reddit.com/r/LangChain/comments/18ntfoa/errors_using_sql_agent/) , 2023-12-23-0909
```
Hello everyone. I'm using Langchain (js) in my Next.js app and used this guide [https://js.langchain.com/docs/integratio
ns/toolkits/sql](https://js.langchain.com/docs/integrations/toolkits/sql) (that someone very helpful shared with me here
 on reddit) to integrate the SQL agent.

 I'm getting **Agent stopped due to max iterations.** or a random incorrect ans
wer from the agent. 

 I implemented it pretty much exactly like the docs I referenced but with a postgreSQL db in Supab
ase instead of a local .db. 

Any thoughts or recommendations are appreciated👍. Thanks in advance
```
---

     
 
all -  [ How to use Langsmith with a FastAPI/uvicorn setup ](https://www.reddit.com/r/LangChain/comments/18npk5y/how_to_use_langsmith_with_a_fastapiuvicorn_setup/) , 2023-12-23-0909
```
Hi there fellow Langchainers,

I have created an agent in a ipynb. Works great and by simply adding
LANGCHAIN_TRACING_V2
 = os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
LANGCHAIN_ENDPOINT = os.getenv('
LANGCHAIN_ENDPOINT')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
and adding these values to the .env file and 

f
rom langsmith import Client
client = Client()

Every agent_executor.invoke({'input': 'input query here'})['output']

is 
nicely logged in Langsmith.

But when I wrap this same agent in a fastapi application with uvicorn, it doesn't work. The
 agent works fine, I can use the agent through Postman just fine. But nothing is logged in Langsmith.

Any help is great
ly appreciated.
```
---

     
 
all -  [ How to distribute LLM apps and UI/UX? ](https://www.reddit.com/r/LocalLLaMA/comments/18np956/how_to_distribute_llm_apps_and_uiux/) , 2023-12-23-0909
```
Pretty new to the space but I'm a programmer. I see a lot of YouTube tutorials using Langchain, Ollama, and 50 other too
ls. Seems easy to build my own app.

How are these apps packaged and distributed so other people can install and interac
t with them? What are the best frameworks to use for this? How do you build a custom UI? Looking for best practices or s
hortest path to something basic.

For example: do you use Langchain and launch a Web UI from a local nodejs server that 
lets users modify their documents for RAG or swap models?

Thanks for any helpful responses.
```
---

     
 
all -  [ [Langchain] Besoin d'aide pour augmenter la vitesse de mon application basée sur LLM ](https://www.reddit.com/r/redditenfrancais/comments/18no9yi/langchain_besoin_daide_pour_augmenter_la_vitesse/) , 2023-12-23-0909
```
J'ai construit quelque chose en utilisant Langchain, Chromadb et LLM d'Openai. J'utilise également les intégres d'Openai
, l'ADA-002.
Cependant, les réponses sont très lentes. Pour les petites questions complexes, il faut 20 à 30 secondes po
ur répondre.
La taille du VectorStore est de 62 Mo seulement mais elle est toujours très lente.
Je voulais demander si l
'utilisation d'une instance AWS EC2 G3 avec des GPU augmentera ou non la vitesse? Ou toute autre solution basée sur le c
loud.
De plus, y a-t-il d'autres façons? J'explore également VLLM pour son paramètre de taille parallèle du tenseur.
Que
lle est la meilleure approche que je puisse adopter pour augmenter la vitesse des réponses?

Ps. Je suis un débutant dan
s ce domaine, désolé si j'ai écrit quelque chose de stupide ici :)

Traduit et reposté à partir de la publication 15rpug
k de la communauté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/
'
```
---

     
 
all -  [ [Langchain] Quel est le meilleur VectorStore pour auto-hoster vos indices vectoriels? ](https://www.reddit.com/r/redditenfrancais/comments/18nnse7/langchain_quel_est_le_meilleur_vectorstore_pour/) , 2023-12-23-0909
```
Je sais que Pinecone est le plus simple, mais sur le niveau libre, ils suppriment vos index après 7 jours. Quel magasin 
vectoriel à Langchain prend en charge la sauvegarde d'un index localement afin que vous puissiez tirer des vecteurs enre
gistrés comme Pinecone? J'ai essayé le chroma, mais cela ne semble pas avoir cette fonctionnalité de ce que je peux dire
. Au lieu de retirer de la conduite Persiste, il passera un appel API pour rétroser les mêmes intérêts.

Traduit et repo
sté à partir de la publication 12ia7nc de la communauté langchain. Pour retrouver la publication originale, insérez l'id
 de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Langchain] Quel modèle d'intégration utilisez-vous les gars? ](https://www.reddit.com/r/redditenfrancais/comments/18nnos2/langchain_quel_modèle_dintégration_utilisezvous/) , 2023-12-23-0909
```
J'essaie de tester plus de modèles d'intégration et je me demande ce que cette communauté utilise ...

Je sais que cela 
'peut varier en fonction du cas d'utilisation', donc dans ce cas, veuillez partager le modèle et le cas d'utilisation co
nnexe.

Actuellement, j'utilise principalement BGE-GARD-V1.5 ou Instructor-XL ...

(intéressé par l'encodeur BI et l'enc
odeur croisé)

Merci im avance !!!

Traduit et reposté à partir de la publication 1816mb5 de la communauté langchain. Po
ur retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Summary of long PDFs ](https://www.reddit.com/r/LangChain/comments/18nlcpm/summary_of_long_pdfs/) , 2023-12-23-0909
```
Hey people,    


I'm new to langchain and have a few questions.    


If I want to summarize large PDFs (e.g. long scie
ntific texts) in an easy-to-understand language, does a vector-based database make sense? Or can I just split the text u
p and then have it summarized piece by piece and create a summary at the end?   


Is the context of the entire PDF pres
erved in both versions?  


I hope you understand my question and can help me. 
```
---

     
 
all -  [ Which framework should I use to build Question-Answering system ? ](https://www.reddit.com/r/LocalLLaMA/comments/18nk6sv/which_framework_should_i_use_to_build/) , 2023-12-23-0909
```
Hi

I currently build a QA system using RAG. I have experience with Langchain and using it to build a POC. But when I st
arted to apply it for production and make more custom to fit with my ideal, I found it too difficult to control the fram
ework, those chains, agents, and prompts are too complicated to control. 

Can you recommend any framework that is more 
controllable? or Should I build from scratch?
```
---

     
 
all -  [ Getting general information over a CSV ](https://www.reddit.com/r/LangChain/comments/18nccz3/getting_general_information_over_a_csv/) , 2023-12-23-0909
```
Hello everyone. I'm new to Langchain and I made a chatbot using Next.js (so the Javascript library) that uses a CSV with
 soccer info to answer questions. Specific questions, for example 'How many goals did **Haaland** score?' get answered p
roperly, since it searches info about Haaland in the CSV (I'm embedding the CSV and storing the vectors in Pinecone).

T
he problem starts when I ask general questions, meaning questions without keywords. For example, 'who made more assists?
', or maybe something extreme like 'how many rows are there in the CSV?'. It completely fails. I'm guessing that it only
 gets the relevant info from the vector db based on the query and it can't answer these types of questions.

&#x200B;

I
'm using `ConversationalRetrievalQAChain` from Langchain

    chain.ts
    
    /* create vectorstore */
      const vec
torStore = await PineconeStore.fromExistingIndex(
        new OpenAIEmbeddings({}),
        {
          pineconeIndex,
 
         textKey: 'text',
        }
      );
    
      return ConversationalRetrievalQAChain.fromLLM(
        model,
  
      vectorStore.asRetriever(),
        { returnSourceDocuments: true }
      );

And using it in my API in Next.js.

 
   route.ts
    
    const res = await chain.call({
        question: question,
        chat_history: history
          
.map((h) => {
            h.content;
          })
          .join('\n'),
      });

&#x200B;

Any suggestions are welcom
ed and appreciated. Also feel free to ask any questions. Thanks in advance
```
---

     
 
all -  [ Identify a Langchain like project like in this video clip ](https://www.reddit.com/r/Langchaindev/comments/18nbrvm/identify_a_langchain_like_project_like_in_this/) , 2023-12-23-0909
```
Can you Advise on finding the open source projects like Azure Cognitive Search + GPT, maybe using Langchain??

This 20 s
econd clip shows exactly the functionality we're looking for  [https://youtube.com/clip/Ugkx4Bx61tbWTnuvDmfEecj2R-msM2AI
3kWA?si=tT7HkGz\_m2wzIeL\_](https://youtube.com/clip/Ugkx4Bx61tbWTnuvDmfEecj2R-msM2AI3kWA?si=tT7HkGz_m2wzIeL_)
```
---

     
 
all -  [ Looking for tutorial on local JS LLMs ](https://www.reddit.com/r/LangChain/comments/18nb0t3/looking_for_tutorial_on_local_js_llms/) , 2023-12-23-0909
```
Hi all,

Are there any resources on using a local JS copy of an LLM (namely Flan-T5) with langchainJS (especially if usi
ng Xenova’s transformers.js for the LLM inference)? I’ve been looking for resources on using the two libraries for a loc
al JS project but information is sparse.
```
---

     
 
all -  [ Integrating LlamaIndex with Langchain. ](https://www.reddit.com/r/LangChain/comments/18n65if/integrating_llamaindex_with_langchain/) , 2023-12-23-0909
```
Hey guys, I am wondering if you know of good guides to go about doing this \^

And would it result in a better memory re
trieval system? (I've heard LlamaIndex is better for RAG systems?) Or would you build everything in Langchain? My system
 will involve a fine-tuned model, external knowledge, plus I am trying to figure out how to store conversation history i
n the vector db for memory retrieval. Eventually I'll add more components like speech-to-text software.. is this support
ed with langchain? Any guidance on this is greatly appreciated.

Right now I'm using Flowise which is built on top of La
ngChain, but haven't found any info on integrating LlamaIndex with Flowise specifically.
```
---

     
 
all -  [ Build your own GPT 5 with Mistral 7B and LangChain ](https://youtu.be/Bc-OSax1G2o) , 2023-12-23-0909
```
Can you develop a latest, your own GPT model with the latest release of mistral 7-b. in this video they talk about using
 Retrieval augmented generation and mistral 7-b. what are your guys thought?
```
---

     
 
all -  [ PGVector - Table ](https://www.reddit.com/r/LangChain/comments/18n2an2/pgvector_table/) , 2023-12-23-0909
```
i was using OPENAIEmbedding before but now i changed it to AzureOpenAIEmbedding but re-building the vector db takes a ve
ry long time. is there anyway i can drop the existing table and re-build it from scratch? although i already have `pre_d
elete_collection=True`

I am using 0.0.348 version 
```
---

     
 
all -  [ Text pre-processing before embedding ](https://www.reddit.com/r/LangChain/comments/18n1741/text_preprocessing_before_embedding/) , 2023-12-23-0909
```
I am trying to create a QNA chatbot with OpenAI API, after using RecursiveCharacterTextSplitter,  texts are coming with 
**'\\n'** Should I be worried? because I have to upsert it into the Pinecone database, and also if there is any preproce
ssing needed before upserting please tell me.. this is my first project

these are the texts: 

`['The\ncow,\na\ngentle\
nherbivorous\nmammal\nof\nthe\nBovidae\nfamily,\nis\na\nvital\ncontributor\nto\nagriculture\nand\nhuman\nsustenance\nglo
bally.\nCharacterized\nby\nits\nlarge\nbody,\ncloven\nhooves,\nand\ndistinctively\npatterned\nhide,\ncows\nprimarily\nse
rve\nas\nsources\nof\nmilk,\nagriculture,livestock,\nfarming\nand\nleather.\nBos\ntaurus,\nthe\nmost\ncommon\nspecies,\n
exists\nin\nvarious\nbreeds,']`

my code : 

    loader = PdfReader('cow.pdf')
    text = ''
    for i,page in enumerate
 (loader.pages):
        content = page.extract_text()
        if content:
            text += content
    
    text_spl
itter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', ' '],
        chunk_size = 400,
        chunk_
overlap  = 20,
        length_function = len,
    )
    
    texts = text_splitter.split_text(text)
    print(texts)
   
 print(len(texts))
    
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    vectorstore = Pinecone.fro
m_texts(texts,embeddings,index_name=PINECONE_INDEX)

&#x200B;
```
---

     
 
all -  [ How can I modify the context retrieved by RetrievalQA Chain? ](https://www.reddit.com/r/LangChain/comments/18n0obz/how_can_i_modify_the_context_retrieved_by/) , 2023-12-23-0909
```
Guys, I'm in a pickle. I'm evaluating my RAG using Trulens and this takes in the RetrievalQA chain. But I want to modify
 the context to add more information to it say from the metadata. Is it possible to modify the context retrieved by Retr
ievalQA to add information from metadata and perhaps add more info to the context?
```
---

     
 
all -  [ Need help in adding context awareness to LLM RAG pipeline ](https://www.reddit.com/r/LangChain/comments/18mxiny/need_help_in_adding_context_awareness_to_llm_rag/) , 2023-12-23-0909
```
Hello all, 

I want to add context awareness to my LLM RAG pipeline. Here are 2 approaches I am thinking of. Please help
 me if I am going in the right direction, and also what should be the ideal approach :

Approach 1 :
Step 1.  Use an LLM
 to do co reference resolution in the new query, based on immediate last conversarion, and get the modified query.   
Ex
ample :
 last conversarion : What is Google? 
New query: what does it do ? 

Modified query : what does Google do . 

St
ep 2. Now based on modified query, get similar responses based on similarity score of previous conversations and add it 
to the prompt. 

Cons :
1. With coreference resolution  since we are using only immediate last query, it would lose out 
on, where the user query refers to noun or subject from earlier conversation .  

Pros :
Woukd only pass the relevant co
nversation. 

Approach 2 : 
Summarize the conversation history,  and store it in memory. As tye conversation proceeds, k
eep on adding to the conversation history. 

Cons :
In case of context switching, the summary would also have non releva
nt context being added to the prompt. How to handle this ?
```
---

     
 
all -  [ RetrievalQA with llamacpp api call ](https://www.reddit.com/r/LangChain/comments/18mwpft/retrievalqa_with_llamacpp_api_call/) , 2023-12-23-0909
```
Hi all,

I am trying to create a chatbot that uses both regular chat or RAG. 
When using the chat functionality I’m able
 to use the API offered by llama cpp server.
But how would I use the API when using the retrievalQA method, to search do
cuments from a vectordb (chroma).

Thanks
```
---

     
 
all -  [ [Local Llama] Modèles à finetuned pour l'appel de fonction? ](https://www.reddit.com/r/redditenfrancais/comments/18mvsg3/local_llama_modèles_à_finetuned_pour_lappel_de/) , 2023-12-23-0909
```
Bonjour. Y a-t-il des modèles LLAMA2 finetunés qui peuvent encore fonctionner de manière fiable pour l'appel de fonction
? (Configuration des agents à Langchain et autres). La discussion précédente a environ 2 mois, donc je me demande s'il y
 a eu des avancées à ce sujet.

J'ai essayé de créer un chatbot qui peut rechercher sur Internet et peut être hébergé lo
calement, mais les modèles que j'ai essayés sont terribles à ce sujet.

Traduit et reposté à partir de la publication 17
0pej3 de la communauté localllama. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit
.com/'
```
---

     
 
all -  [ Route between LLMs ](https://www.reddit.com/r/LangChain/comments/18mrv75/route_between_llms/) , 2023-12-23-0909
```
Is there any way to route between different LLM models, like for codng related prompts it should use an LLM model that i
s good at coding and for conversational prompts a model that is good at chatting/conversing.
```
---

     
 
all -  [ Best practice for RAG with follow-up chat questions and LLM conversation? ](https://www.reddit.com/r/LocalLLaMA/comments/18mqwg6/best_practice_for_rag_with_followup_chat/) , 2023-12-23-0909
```
I am building something like a personal AI tutor for a hobby. I have done a few POCs using Langchain and Autogen, but I 
am still not sure what the right 'architecture' would look like. 

Simple example: discuss with the student which subjec
t (e.g. history), and which particular topic (e.g. ancient Rome) should be studied. Then the chain would need to 'collec
t' the relevant knowledge from RAG sources (so it has grounding and does not hallucinate, and also has access to the exa
ct set of knowledge that is determined by a particular school system). Then after it has the basics collected via the RA
G pattern, it would then discuss the topic with the student, ask follow-up questions, provide tests for the students to 
assess his/her knowledge, etc. In this 'mode', it wouldn't use any RAG lookup, but use what it has already put in the co
ntext earlier. 

The problem with Langchain ConversationalRetrievalChain with ConversationBufferMemory is that it still 
assumes that I am mainly using it for a RAG like use case. Maybe I am mistaken,  not sure. I have built another POC with
 Autogen, and that seems to work better, e.g. it can use more RAG more like a tool (function), and it can be better 'ste
ered' into the above working mode. But it is still not perfect. 

Also, it would not be a bad thing to realize this with
out having to use Langchain. 

**TL/DR:** I was wondering if there's a best practice for my use case, a personal tutor, 
which uses a RAG pattern, but the student would also be able to chat about the already extracted info extensively. 

&#x
200B;

&#x200B;
```
---

     
 
all -  [ [Machine Learning] [D] Y a-t-il quelque chose que Langchain peut faire mieux que l'utilisation direc ](https://www.reddit.com/r/redditenfrancais/comments/18m8be4/machine_learning_d_y_atil_quelque_chose_que/) , 2023-12-23-0909
```
Je n'ai pas beaucoup utilisé Chatgpt ni aucun autre LLMS, j'ai lu sur Langchain et ses cas d'utilisation, et j'ai du mal
 à enrouler la tête exactement ce qu'elle fait. D'après ce que je comprends, c'est une interface alternative pour les LL
M, permettant une commutation facile entre eux, et facilite le travail pour des cas d'utilisation spécifiques. Si je vou
lais écrire une application ou un script pour interagir avec LLMS et effectuer d'autres tâches, comment Langchain serait
-il meilleur que de simplement faire des appels API à un LLM, de récupérer le résultat en tant que chaîne et de faire qu
oi que ce soit?

Traduit et reposté à partir de la publication 165airj de la communauté machinelearning. Pour retrouver 
la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Favorite setup for agency ](https://www.reddit.com/r/LangChain/comments/18m3tb3/favorite_setup_for_agency/) , 2023-12-23-0909
```
What would be your favorite setup client hosted to have csv, pdf and api chatbot?
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-23-0909
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-23-0909
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-23-0909
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-23-0909
```
I've been trying to work with structured data in language models, and it's proving to be quite challenging. I'm confiden
t that with Langchain, I should be able to solve the problem, but I'm not entirely sure which path to take among all the
 options the library offers.

My issue is as follows: I have data in the form of dictionaries regarding a series of prod
ucts, for example, laptops. The data looks like this:

{Identifier 1: X, Identifier 2: Y, Value name: Z}

(Several succe
ssive dictionaries like this.)

I want to use this series of dictionaries as context, then feed a different dictionary i
nto the Language Model, and have it tell me if the 'Value name' makes sense given Identifiers 1 and 2. An example would 
be Identifier 1: laptops, Identifier 2: brand, Value name: Lenovo. In this case, it should return affirmative since Leno
vo makes sense as a brand. However, if I input 'oranges,' it should return negative.

Any ideas on which library I could
 use to tackle this problem?
```
---

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-23-0909
```
Hi all!

A couple of days ago, when I was scrolling down Hacker News, exploring news about OpenAI and the latest specula
tion about Q\*, it occurred to me to create a ChatBot that would allow me to interact with Hacker News directly, in a co
nversation.

Using streamlit, langchain and openai functions I managed to create a first version of this chat (I still h
ave to add RAG for news analysis and test other types of LLMs). 

Here is an example, what do you think?

Code: [https:/
/github.com/neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhacker
bot.streamlit.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://i.redd.it/rtpof7biqi2c1.gif
```
---

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-23-0909
```
 

  
For example with the following structure:

* System = GPT-4 Turbo + Llama2 +3rd LLM (!)+ Google or Bing API for we
bsearch + Langchain + any vectorDB + Document upload + longterm Memory + …

Idee behind it is to get more accurate, upda
ted (websearch) and specialized system or even let the LLms discuss your prompt before completion! Question is also, how
 shall the interaction of multiple LLMs in a system be organzied (Algorithm, Python Library …)? And what kind of Interac
tion can/should this be? Master-slave or Multi-Master system?
```
---

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-23-0909
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user.
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2023-12-23-0909
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-23-0909
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-23-0909
```
In the domain of document analysis, the convergence of text, tables, and images presents formidable challenges for conve
ntional RAG (Retrieval Augmented Generation) methodologies. This complexity is further compounded within semi-structured
 data, notably in the extraction of tables from PDFs. Enter LangChain, a pioneering tool adept at navigating these intri
cate landscapes. Augmenting its capabilities is LlamaIndex, integrating Multi-Modal Retrieval Augmented Generation (RAG)
 techniques. Together, LangChain and LlamaIndex stand poised to revolutionize the handling and extraction of diverse con
tent types, promising a breakthrough in unraveling insights from varied data formats.

Link in the comment
```
---

     
