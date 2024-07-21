 
all -  [ Top enhancements to try once you have a vanilla RAG set-up with a text vector database? ](/r/LocalLLaMA/comments/1e84de2/top_enhancements_to_try_once_you_have_a_vanilla/) , 2024-07-21-0912
```

```
---

     
 
all -  [ Infinity surpasses 1k Github stars & new inference package launch - `pip install embed`  ](https://www.reddit.com/r/LocalLLaMA/comments/1e83cah/infinity_surpasses_1k_github_stars_new_inference/) , 2024-07-21-0912
```
Today, I am launching [https://github.com/michaelfeil/embed](https://github.com/michaelfeil/embed) (MIT). After launchin
g the async framework for OpenAI compatible embedding, re-ranking, clip and classification requests.

[https://github.co
m/michaelfeil/infinity](https://github.com/michaelfeil/infinity) recently hit 1000 Github stars & \~300 PRs/Issues/Discu
ssions. A learning is that the ecosystem (llamaindex, langchain, others) are not ready for asynchronous usage. As a resu
lt, I am launching a more streamlined version with a synchronous API that returns synchronous futures on each method. 


Features:  
- Runs on AMD, CUDA and CPU, via torch or onnx. Automatically chooses optimal settings (e.g. O-4, FA2)  
- O
ptions for int8/fp8 weight-only quantization   
- embedding quantization [https://huggingface.co/blog/embedding-quantiza
tion](https://huggingface.co/blog/embedding-quantization) 
```
---

     
 
all -  [ Hey guys I know we all hate langchain but I have a question  ](https://www.reddit.com/r/datascience/comments/1e7xtww/hey_guys_i_know_we_all_hate_langchain_but_i_have/) , 2024-07-21-0912
```
I’m building a chat bot . And since the data is in a data warehouse,  it’s in a table . Do you think retrieval methods p
erform better when the data is in a text format, just a docs file or it works just the same on a tabular data too and cs
v or parquet format. And I’m planning on using llama index or langchain. Thank you 
```
---

     
 
all -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-07-21-0912
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
all -  [ Has anyone been able to use ChatAnthropicVertex tool calling? ](https://www.reddit.com/r/ClaudeAI/comments/1e7qksc/has_anyone_been_able_to_use_chatanthropicvertex/) , 2024-07-21-0912
```
Seems there are a lot of bugs in it's implementation. bind_tools with ChatAnthropicVertex is literally unusable because 
it doesn't return finish_reason. Tool calls are also incorrect. Have you been able to use it. #langchain #VertexAi
```
---

     
 
all -  [ Is learning langchain worth it?  ](https://www.reddit.com/r/learnmachinelearning/comments/1e7pj1l/is_learning_langchain_worth_it/) , 2024-07-21-0912
```
Hello, 

I recently heard about langchain(ik I'm late) but I read briefly about it, and understood it is used for creati
ng genAi apps. But most of the reddit review is pretty negative for this library. 

So is it worth it to learn and creat
e projects using this or no
```
---

     
 
all -  [ This sums up my experience with all LLM orchestration frameworks ](https://i.redd.it/xwlgql6idmdd1.jpeg) , 2024-07-21-0912
```
Langchain in a nutshell. 
```
---

     
 
all -  [ Search for data across entire text files ](https://www.reddit.com/r/LangChain/comments/1e7pcxp/search_for_data_across_entire_text_files/) , 2024-07-21-0912
```
I'm having problems building my system.

Let's say I have one (or more pdf files), I load, splitters, chunking, clean da
ta,... and then save it to a vector database (qdrant). I can query its data quite well with knowledge questions located 
somewhere in the files.

But suppose in my data file is a list of about 1000 products distributed on many different page
s, is there any way I can solve the question: 'How many products are there?' Are not?

Or ask 'List all the major and mi
nor headings in the file' and it can answer correctly if there is no table of contents available.

My problem is that I 
can't read the whole document when putting it in the context part of LLM, because it's too long if k is increased in the
 retrievers part, and I also don't think it can completely satisfy the context content because Maybe it is still left so
mewhere in other segments if k is fixed?

If anyone has any ideas or solutions, please help me.
```
---

     
 
all -  [ Persists documents on ParentDocumentRetrieval ](https://www.reddit.com/r/LangChain/comments/1e7h5ea/persists_documents_on_parentdocumentretrieval/) , 2024-07-21-0912
```
Is there any way to persists the parent documents in the ParentDocumentRetrieval?  
All the tutorials I see use the InMe
moryStore, but I'd like to persist the parent documents in a redis database or a mysql database.  

```
---

     
 
all -  [ Deploy Langgraph in Google Cloud? ](https://www.reddit.com/r/LangChain/comments/1e7em5x/deploy_langgraph_in_google_cloud/) , 2024-07-21-0912
```
Hello everyone. Has anyone deployed Langgraph in Google Cloud services? Currently, I've created my own method to do it u
sing the Reasoning Engine, but I am a newbie in cloud services. I want to know if there is a better way to do it
```
---

     
 
all -  [ Bind functions with Ollama model from ChatOpenAI. ](https://www.reddit.com/r/LangChain/comments/1e7cvzl/bind_functions_with_ollama_model_from_chatopenai/) , 2024-07-21-0912
```
I want to bind some functions into a llm, I'm using the ChatOpenAI wrapper to connect to a Ollama llama3 model locally, 
I have this code:

        options = ['FINISH'] + members
        function_def = {
            'name': 'route',
        
    'description': 'Select the next role',
            'parameters': {
                'title': 'routeSchema',
         
       'type': 'object',
                'properties': {
                    'next': {
                        'title': 
'Next',
                        'anyOf': [
                            {'enum': options},
                        ],
   
                 },
                },
                'required': ['next'],
            },
        }
        prompt = C
hatPromptTemplate.from_messages(
            [
                ('system', system_prompt),
                MessagesPlaceh
older(variable_name='messages'),
                (
                    'system',
                    'Given the conversa
tion above, who should act next?'
                    'Or should we FINISH?: select one of {options}
                )
 
           ]
        ).partial(options=str(options), team_members=','.join(members))
        
        # Bind the functio
n to the LLM, specify the function call, and parse the output as JSON
        return (
            prompt
            | 
llm.bind_functions(functions=[function_def], function_call='route')
            | JsonOutputFunctionsParser()
        )


This is the LLM I'm using:

    llm = ChatOpenAI(base_url='http://localhost:11434/v1', model='llama3', api_key='ollama'
)

However, I encounter the following issue:

langchain\_core.exceptions.OutputParserException: Could not parse function
 call: 'function\_call'

Could anyone help me here? Thanks :)
```
---

     
 
all -  [ What’s the Best Python Library for Extracting Text from PDFs? ](https://www.reddit.com/r/LangChain/comments/1e7cntq/whats_the_best_python_library_for_extracting_text/) , 2024-07-21-0912
```
Hello everyone, I hope you're all doing well! I’m currently on the lookout for a library that can extract text in paragr
aph chunks from PDFs. For instance, I need it to pull out the Introduction with all its paragraphs separately, the Concl
usion with all its paragraphs separately, and so on, essentially chunking the text by paragraphs. Do you have any sugges
tions? Thanks!
```
---

     
 
all -  [ Steaming Hot AI Tools 2024-2025 ](https://www.reddit.com/r/LLMoney/comments/1e79lk4/steaming_hot_ai_tools_20242025/) , 2024-07-21-0912
```
# Super Index

scraped and merged using AI,  **Kindly** join and benefit from our community. Updated on July-2024

# Fea
tured Tools

1. [Freedom GPT](https://shorturl.at/StjP0) : fully uncensored chat, 🤙 m**ake calls!** chatbot, text 2 vide
o or image, interesting product. moderately affordable, 150 credits earnable = 30 tasks.
2. [AI Camp](https://aicamp.so/
?via=swamix) : AI-powered platform that merges multiple providers like OpenAI, Gemini, ANthropic etc. It offers features
 like chat, assistant, teamspaces, and extensions to enhance productivity and innovation. input your own key if dont wan
na use their pricing!

# Search Engines

1. [Bing Chat](https://www.bing.com/chat) - Conversational AI powered by Micros
oft Bing. *Use case: Web search with conversational context.*
2. [Perplexity](https://www.perplexity.ai/) : web search e
nabled Chatbot, more accurate answers. and image search. free usage with limits.
3. [Phind](https://www.phind.com/) : In
telligent search engine and coding assistant. *Use case: Code search and understanding.*
4. [Komo.ai](http://Komo.ai) : 
found to be useful for coding, as it has less hallucinations.
5. [Brave Search](https://search.brave.com) : Another grea
t search engine, with better UI. Privacy centric as they claim.

# Chatbots / API providers

* [GPT-4o(omni)](https://op
enai.com/index/hello-gpt-4o/) : ability to process and generate text, audio, and visual content seamlessly, more assista
nt like.
* [Anthropic Claude](https://claude.ai) : One of top scoring AI model, available as API. highest MMLU scores.  
file upload.
* [Meta AI](https://www.meta.ai/) : new llama-3 models, can try in the UI, country restrictions apply at th
e moment.
* [Google Gemini](https://gemini.google.com/app) : another good model, API is free to use with limits. file up
load available.
* [Groq](https://groq.com/) : Fastest inference on model of choice, currently 800Tokens per second. can 
try llama3 if meta page not opening.

# Apps

* [Sonic Suite](https://writesonic.com/ai-article-writer-generator) : set 
of AI tools for writers and bloggers and in general. requires account, cheap pro plan.
* [you.com](http://you.com) : per
plexity like app, somethings are interesting. paid account. knowledge is not realtime. file support.
* [Mapchannels](htt
ps://www.mapchannels.com/AISearchMap.aspx): ultimate UI lol, does some interesting applications using maps.
* [tiledesk.
com](http://tiledesk.com) : A platform for creating your own chatbots, with drag and drop interface. innovative concept.

* [protagoras.app](https://protagoras.app)  : assists with seo, great for bloggers and small business owners. Suggested
 by redditor in comments.
* [Kazimir.ai](https://kazimir.ai/) - Search engine for AI-generated images.

# Opensource Pro
jects

currently merging index of [built with ollama](https://github.com/ollama/ollama/tree/main?tab=readme-ov-file#web-
-desktop) , [Built with LLamaIndex ](https://github.com/kyrolabs/awesome-langchain/blob/main/README.md),

# Web & Deskto
p Applications

* [Open WebUI](https://github.com/open-webui/open-webui): Web-based user interface for Ollama
* [Enchant
ed](https://github.com/AugustDev/enchanted): macOS native client for Ollama
* [Hollama](https://github.com/fmaclen/holla
ma): Desktop application for Ollama
* [Lollms-Webui](https://github.com/ParisNeo/lollms-webui): Web interface for langua
ge models including Ollama
* [LibreChat](https://github.com/danny-avila/LibreChat): Open-source chat interface with Olla
ma support
* [Bionic GPT](https://github.com/bionic-gpt/bionic-gpt): Enterprise-ready application using Ollama
* [HTML U
I](https://github.com/rtcfirefly/ollama-ui): Simple HTML-based UI for Ollama
* [Saddle](https://github.com/jikkuatwork/s
addle): Lightweight web UI for Ollama
* [Chatbot UI](https://github.com/ivanfioravanti/chatbot-ollama): Web-based chatbo
t interface for Ollama
* [Chatbot UI v2](https://github.com/mckaywrigley/chatbot-ui): Enhanced version of the Chatbot UI

* [Typescript UI](https://github.com/ollama-interface/Ollama-Gui): TypeScript-based graphical interface for Ollama
* [M
inimalistic React UI](https://github.com/richawo/minimal-llm-ui): Simple React-based UI for Ollama models
* [Ollamac](ht
tps://github.com/kevinhermawan/Ollamac): macOS client for Ollama
* [big-AGI](https://github.com/enricoros/big-AGI): Adva
nced AI interface with Ollama integration
* [Cheshire Cat](https://github.com/cheshire-cat-ai/core): AI assistant framew
ork with Ollama support
* [Amica](https://github.com/semperai/amica): AI chat application using Ollama
* [chatd](https:/
/github.com/BruceMacD/chatd): Chat daemon for Ollama
* [Ollama-SwiftUI](https://github.com/kghandour/Ollama-SwiftUI): Sw
iftUI client for Ollama
* [Dify.AI](https://github.com/langgenius/dify): LLM application development platform with Ollam
a integration
* [MindMac](https://mindmac.app): macOS application for AI interactions, including Ollama
* [NextJS Web In
terface](https://github.com/jakobhoeg/nextjs-ollama-llm-ui): Next.js-based web interface for Ollama
* [Msty](https://mst
y.app): AI chat application with Ollama support
* [Chatbox](https://github.com/Bin-Huang/Chatbox): Crossplatform AI chat
bot app with Ollama integration
* [WinForm Ollama Copilot](https://github.com/tgraupmann/WinForm_Ollama_Copilot): Window
s Forms-based copilot using Ollama
* [NextChat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web): Web-based chat inte
rface with Ollama support
* [Alpaca WebUI](https://github.com/mmo80/alpaca-webui): Web interface for Alpaca models using
 Ollama
* [OllamaGUI](https://github.com/enoch1118/ollamaGUI): Graphical user interface for Ollama
* [OpenAOE](https://g
ithub.com/InternLM/OpenAOE): AI operations platform with Ollama integration
* [Odin Runes](https://github.com/leonid2000
0/OdinRunes): Ollama-based application
* [LLM-X](https://github.com/mrdjohnson/llm-x): Progressive Web App for Ollama
* 
[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm): Docker and native app for LLM interactions, including Olla
ma
* [Ollama Basic Chat](https://github.com/rapidarchitect/ollama_basic_chat): Simple chat interface using HyperDiv Reac
tive UI
* [Ollama-chats RPG](https://github.com/drazdra/ollama-chats): RPG-style chat interface for Ollama
* [QA-Pilot](
https://github.com/reid41/QA-Pilot): Tool for chatting with code repositories using Ollama
* [ChatOllama](https://github
.com/sugarforever/chat-ollama): Open-source chatbot with knowledge base support
* [CRAG Ollama Chat](https://github.com/
Nagi-ovo/CRAG-Ollama-Chat): Web search with Corrective RAG using Ollama
* [RAGFlow](https://github.com/infiniflow/ragflo
w): Retrieval-Augmented Generation engine using Ollama
* [StreamDeploy](https://github.com/StreamDeploy-DevRel/streamdep
loy-llm-app-scaffold): LLM Application Scaffold with Ollama support
* [chat](https://github.com/swuecho/chat): Team-orie
nted chat web app using Ollama
* [Lobe Chat](https://github.com/lobehub/lobe-chat): AI chat application with Ollama inte
gration
* [Ollama RAG Chatbot](https://github.com/datvodinh/rag-chatbot): Local chatbot for multiple PDFs using Ollama a
nd RAG
* [BrainSoup](https://www.nurgo-software.com/products/brainsoup): Flexible native client with RAG & multi-agent a
utomation
* [macai](https://github.com/Renset/macai): macOS client for Ollama and other AI backends
* [Olpaka](https://g
ithub.com/Otacon/olpaka): User-friendly Flutter Web App for Ollama
* [OllamaSpring](https://github.com/CrazyNeil/OllamaS
pring): Ollama Client for macOS
* [LLocal.in](https://github.com/kartikm7/llocal): Electron Desktop Client for Ollama
* 
[Ollama with Google Mesop](https://github.com/rapidarchitect/ollama_mesop/): Mesop Chat Client implementation with Ollam
a
* [Kerlig AI](https://www.kerlig.com/): AI writing assistant for macOS using Ollama
* [AI Studio](https://github.com/M
indWorkAI/AI-Studio): AI development environment with Ollama support
* [Sidellama](https://github.com/gyopak/sidellama):
 Browser-based LLM client for Ollama

# Terminal Applications

* [oterm](https://github.com/ggozad/oterm): Terminal-base
d chat interface for Ollama
* [Ellama](https://github.com/s-kostyaev/ellama): Emacs client for Ollama
* [Emacs client](h
ttps://github.com/zweifisch/ollama): Another Emacs client for Ollama
* [gen.nvim](https://github.com/David-Kunz/gen.nvim
): Neovim plugin for Ollama
* [ollama.nvim](https://github.com/nomnivore/ollama.nvim): Neovim plugin for Ollama integrat
ion
* [ollero.nvim](https://github.com/marco-souza/ollero.nvim): Another Neovim plugin for Ollama
* [ollama-chat.nvim](h
ttps://github.com/gerazov/ollama-chat.nvim): Neovim chat plugin for Ollama
* [ogpt.nvim](https://github.com/huynle/ogpt.
nvim): Neovim plugin for GPT-like functionality using Ollama
* [gptel](https://github.com/karthink/gptel): Emacs client 
for various LLMs, including Ollama
* [Oatmeal](https://github.com/dustinblackman/oatmeal): Terminal UI for LLMs, includi
ng Ollama
* [cmdh](https://github.com/pgibler/cmdh): Command-line interface for Ollama
* [ooo](https://github.com/npahlf
er/ooo): Simple CLI tool for Ollama
* [shell-pilot](https://github.com/reid41/shell-pilot): CLI tool for shell command a
ssistance using Ollama
* [tenere](https://github.com/pythops/tenere): Terminal user interface for Ollama
* [llm-ollama](
https://github.com/taketwo/llm-ollama): Ollama integration for Datasette's LLM CLI
* [typechat-cli](https://github.com/a
naisbetts/typechat-cli): CLI tool for chatting with Ollama models
* [ShellOracle](https://github.com/djcopley/ShellOracl
e): CLI tool for generating shell commands using Ollama
* [tlm](https://github.com/yusufcanb/tlm): Terminal LLM client s
upporting Ollama
* [podman-ollama](https://github.com/ericcurtin/podman-ollama): Podman wrapper for Ollama
* [gollama](h
ttps://github.com/sammcj/gollama): Go-based CLI for Ollama

# Database Integrations

* [MindsDB](https://github.com/mind
sdb/mindsdb): AI layer for databases with Ollama integration
* [chromem-go](https://github.com/philippgille/chromem-go):
 Go library for embedding vectors with Ollama support

# Package Managers

* [Pacman](https://archlinux.org/packages/ext
ra/x86_64/ollama/): Arch Linux package for Ollama
* [Helm Chart](https://artifacthub.io/packages/helm/ollama-helm/ollama
): Kubernetes Helm chart for Ollama
* [Guix channel](https://codeberg.org/tusharhero/ollama-guix): GNU Guix channel for 
Ollama

# Libraries

* [LangChain](https://python.langchain.com/docs/integrations/llms/ollama): Python library for LLM a
pplications with Ollama support
* [LangChain.js](https://js.langchain.com/docs/modules/model_io/models/llms/integrations
/ollama): JavaScript version of LangChain with Ollama integration
* [LangChainGo](https://github.com/tmc/langchaingo/): 
Go implementation of LangChain with Ollama support
* [LangChain4j](https://github.com/langchain4j/langchain4j): Java imp
lementation of LangChain with Ollama integration
* [LangChainRust](https://github.com/Abraxas-365/langchain-rust): Rust 
implementation of LangChain with Ollama support
* [LlamaIndex](https://gpt-index.readthedocs.io/en/stable/examples/llm/o
llama.html): Data framework for LLM applications with Ollama integration
* [LiteLLM](https://github.com/BerriAI/litellm)
: Library for LLM interactions, including Ollama
* [OllamaSharp](https://github.com/awaescher/OllamaSharp): .NET library
 for Ollama
* [Ollama for Ruby](https://github.com/gbaptista/ollama-ai): Ruby library for Ollama
* [Ollama-rs](https://g
ithub.com/pepperoni21/ollama-rs): Rust library for Ollama
* [Ollama-hpp](https://github.com/jmont-dev/ollama-hpp): C++ l
ibrary for Ollama
* [Ollama4j](https://github.com/amithkoujalgi/ollama4j): Java library for Ollama
* [ModelFusion](https
://modelfusion.dev/integration/model-provider/ollama): TypeScript library with Ollama integration
* [OllamaKit](https://
github.com/kevinhermawan/OllamaKit): Swift library for Ollama
* [Ollama for Dart](https://github.com/breitburg/dart-olla
ma): Dart library for Ollama
* [Ollama for Laravel](https://github.com/cloudstudio/ollama-laravel): Laravel package for 
Ollama
* [LangChainDart](https://github.com/davidmigloz/langchain_dart): Dart implementation of LangChain with Ollama su
pport
* [Semantic Kernel - Python](https://github.com/microsoft/semantic-kernel): Python library for AI orchestration wi
th Ollama support
* [Haystack](https://github.com/deepset-ai/haystack-integrations): NLP framework with Ollama integrati
on
* [Elixir LangChain](https://github.com/brainlid/langchain): Elixir implementation of LangChain with Ollama support
*
 [rollama](https://github.com/JBGruber/rollama): R library for Ollama
* [ollama-r](https://github.com/hauselin/ollama-r)
: Another R library for Ollama
* [Ollama-ex](https://github.com/lebrunel/ollama-ex): Elixir library for Ollama
* [Ollama
 Connector for SAP ABAP](https://github.com/b-tocs/abap_btocs_ollama): ABAP connector for Ollama
* [Testcontainers](http
s://testcontainers.com/modules/ollama/): Testing library with Ollama support
* [Portkey](https://portkey.ai/docs/welcome
/integration-guides/ollama): AI development platform with Ollama integration
* [PromptingTools.jl](https://github.com/sv
ilupp/PromptingTools.jl): Julia package for LLM prompting with Ollama support
* [LlamaScript](https://github.com/Project
-Llama/llamascript): TypeScript library for Ollama

# Mobile Applications

* [Enchanted](https://github.com/AugustDev/en
chanted): iOS client for Ollama
* [Maid](https://github.com/Mobile-Artificial-Intelligence/maid): Mobile AI application 
using Ollama

# Extensions & Plugins

* [Raycast extension](https://github.com/MassimilianoPasquini97/raycast_ollama): R
aycast extension for Ollama
* [Discollama](https://github.com/mxyng/discollama): Discord bot for the Ollama Discord chan
nel
* [Continue](https://github.com/continuedev/continue): AI-powered development tool with Ollama support
* [Obsidian O
llama plugin](https://github.com/hinterdupfinger/obsidian-ollama): Obsidian plugin for Ollama integration
* [Logseq Olla
ma plugin](https://github.com/omagdy7/ollama-logseq): Logseq plugin for Ollama integration
* [NotesOllama](https://githu
b.com/andersrex/notesollama): Apple Notes plugin for Ollama
* [Dagger Chatbot](https://github.com/samalba/dagger-chatbot
): Dagger-based chatbot using Ollama
* [Discord AI Bot](https://github.com/mekb-turtle/discord-ai-bot): Discord bot usin
g Ollama
* [Ollama Telegram Bot](https://github.com/ruecat/ollama-telegram): Telegram bot for Ollama
* [Hass Ollama Conv
ersation](https://github.com/ej52/hass-ollama-conversation): Home Assistant conversation component for Ollama
* [Rivet p
lugin](https://github.com/abrenneke/rivet-plugin-ollama): Rivet plugin for Ollama integration
* [Obsidian BMO Chatbot pl
ugin](https://github.com/longy2k/obsidian-bmo-chatbot): Obsidian plugin for chatbot functionality using Ollama
* [Cliobo
t](https://github.com/herval/cliobot): Telegram bot with Ollama support
* [Copilot for Obsidian plugin](https://github.c
om/logancyang/obsidian-copilot): Obsidian plugin for AI-assisted writing using Ollama
* [Obsidian Local GPT plugin](http
s://github.com/pfrankov/obsidian-local-gpt): Obsidian plugin for local GPT functionality using Ollama
* [Open Interprete
r](https://docs.openinterpreter.com/language-model-setup/local-models/ollama): Interpreter for running LLMs locally, inc
luding Ollama
* [Llama Coder](https://github.com/ex3ndr/llama-coder): Copilot alternative using Ollama
* [Ollama Copilot
](https://github.com/bernardo-bruning/ollama-copilot): Proxy for using Ollama as a GitHub Copilot alternative
* [twinny]
(https://github.com/rjmacarthy/twinny): Copilot and Copilot chat alternative using Ollama
* [Wingman-AI](https://github.
com/RussellCanfield/wingman-ai): Copilot code and chat alternative using Ollama and HuggingFace
* [Page Assist](https://
github.com/n4ze3m/page-assist): Chrome Extension for AI assistance using Ollama
* [AI Telegram Bot](https://github.com/t
usharhero/aitelegrambot): Telegram bot using Ollama backend
* [AI ST Completion](https://github.com/yaroslavyaroslav/Ope
nAI-sublime-text): Sublime Text 4 AI assistant plugin with Ollama support
* [Discord-Ollama Chat Bot](https://github.com
/kevinthedang/discord-ollama): TypeScript Discord Bot with Ollama integration
* [Discord AI chat/moderation bot](https:/
/github.com/rapmd73/Companion): Python-based Discord bot using Ollama for chat and moderation
* [Headless Ollama](https:
//github.com/nischalj10/headless-ollama): Scripts for automatic Ollama installation on various OS
```
---

     
 
all -  [ Using Langchain runnables and running into pydantic errors ](https://www.reddit.com/r/LangChain/comments/1e77ye2/using_langchain_runnables_and_running_into/) , 2024-07-21-0912
```
Hi Y'all,  
I encounter this issue with running langchain runnables and it can't get input\_schema. To replicate this us
ing a basic chain. This happens with all the chain, when I look for input\_schema it yells with this error for those cha
in's inputs.  
Any leads on how to resolve this issue?  
TIA

https://preview.redd.it/rwbz1r8b5idd1.png?width=1468&forma
t=png&auto=webp&s=dcfb12069db3cf22268725f921c36a3c5a09ab27


```
---

     
 
all -  [ Using astram_events on langgraph with parallel chains ](https://www.reddit.com/r/LangChain/comments/1e77fkx/using_astram_events_on_langgraph_with_parallel/) , 2024-07-21-0912
```
Hi everybody. I am trying to streaming the response of a langgraph. With astream\_events is it possible to choose in the
 metadata the node we want to stream the response, and in my case is of course the last node. The problem is that the ch
ain used in the last node has been built using runnable Parallel, because I needed to invoke multiple chains in parallel
. But what I am interested in is just the output of one of the chains. However the astream\_event applied on the last no
de streams out the output of the chains mixed. So I get the streaming of all the chain at the same time and it get messe
d up. Has anyone already tried to build a graph with parallel indipendent chains and used astream\_events on it??
```
---

     
 
all -  [ Rag, response json parsed ](https://www.reddit.com/r/LangChain/comments/1e73y4n/rag_response_json_parsed/) , 2024-07-21-0912
```
hi.
im actually working on a rag projet, that suppose to take a CV in entry and recommand a list of job according to the
 cv skills.
at this stage i have the full rag system who take the cv and index it on pinecone, for the jobs offer it wor
k the same.
for the model i use a rag chain with 2 different retriever.
but im stuck on how to get the response as a jso
n.
```
---

     
 
all -  [ LangGraph Stability ](https://www.reddit.com/r/LangChain/comments/1e73gzj/langgraph_stability/) , 2024-07-21-0912
```
Is LangGraph production-ready?

I am finally seeing more documentation on checkpoint implementations, such as persistenc
e using PostgreSQL, MongoDB, and Redis. Thanks a lot to the LangChain devs for the continued development of this open so
urce tool.

However, I notice that these implementations are mainly phrased as 'example' implementations. Does this mean
 they are not production ready?

Are checkpoints in a stable condition? I have been wanting to add an implementation mys
elf, but chalked it up to be something I'd have to spend considerable time implementing as the specifications is lengthy
. However, now I see the code for the core checkpoint usage has been updated recently, and even the implementations have
 new things like `write` and `channel`.

There are also other areas (comment sections under the notebooks) where someone
 states that `thread_ts` has been deprecated, and `checkpoint_id` is now being used. Yet, the notebook example implement
ations themselves still use `thread_ts`.

Finally, the behind the scenes of what is stored is a bit complicated to under
stand as well, without much explanations nor documentations. And even these base abstractions seem to be changing recent
ly. For example, the checkpointer implementations have some code 'for backward compatibility'.

If I were to maintain an
 implementation for another dialect (MariaDB, SQL Server, etc), changing it at such a dynamic pace would take more away 
from using LangGraph itself on my projects. Especially when the LangGraph changes are discovered when browsing the git h
istory, rather than the LangGraph blogs or documentations.

Can these be documented? It's a bit of a magic right now wit
h what is being stored unless one attempts to actually reverse engineer it. Again, I do not have an issue doing that; af
ter all, it is an open source tool. However, with the ever-changing seemingly silent changes, it will make it difficult 
to keep up.

Is LangGraph stable? Or still in heavy development?
```
---

     
 
all -  [ Suggestions on my resume ](https://i.redd.it/qxsm0uat2hdd1.jpeg) , 2024-07-21-0912
```
I have been working as a data scientist for sometime now after studying some things online and then started getting a fo
rmal education from IITM to grasp more in depth knowledge on the same. Now I’m looking for a job switch from being a con
sultant to a full time role in a big company. What are my chances to get a job and what can improve in my resume to do s
o? 

I had posted my previous resume yesterday and based on feedback I’ve made changes and putting my new resume again f
or feedback. 
```
---

     
 
all -  [ LangGraph-GUI: Self-hosted Visual Editor for Node-Edge Graphs with Reactflow & Ollama ](https://www.reddit.com/r/LangChain/comments/1e72vpe/langgraphgui_selfhosted_visual_editor_for/) , 2024-07-21-0912
```
Hi everyone,

I'm excited to share my latest project: LangGraph-GUI ( [https://github.com/LangGraph-GUI/](https://github
.com/LangGraph-GUI/) ) It's a powerful, self-hosted visual editor for node-edge graphs that combines:

* Reactflow front
end for intuitive graph manipulation
* Ollama backend for AI capabilities on GPU-enabled PCs
* Docker Compose for easy s
etup

https://preview.redd.it/12jviwao1hdd1.jpg?width=1541&format=pjpg&auto=webp&s=68717af32acc7acdd8ee2dd09d294f83f6cbe
d31

Key Features:

* low code or no code
* Local LLM such gemma2
* Simple self-hosting with Docker Compose

See more on
 [Documentation](https://langgraph-gui.github.io/)

This project builds on my previous work with [LangGraph-GUI-Qt](http
s://github.com/LangGraph-GUI/LangGraph-GUI-Qt) and [CrewAI-GUI](https://github.com/LangGraph-GUI/CrewAI-GUI), now levera
ging Reactflow for an improved frontend experience.

I'd love to hear your thoughts, questions, or feedback on LangGraph
-GUI. How might you use this tool in your projects?

Moreover, if you want to learn langgraph, we have [LangGraph Learni
ng for dummy](https://github.com/LangGraph-GUI/LangGraph-learn)
```
---

     
 
all -  [ 'Attention Isn’t All You Need' ](https://www.reddit.com/r/LangChain/comments/1e72ayj/attention_isnt_all_you_need/) , 2024-07-21-0912
```
You've probably heard about Mistral's groundbreaking release of Codestral Mamba, a 7B parameter model. But why all the h
ype over a 7B model when we have giants like GPT-4? Well, it's not just about size this time – it's about architecture. 
🔍

The **Transformer Dilemma:**

Transformers have been the cornerstone architecture for language models, powering every
thing from open-source LLMs to chatGPT and Claude.

However, they come with a significant drawback: as context expands, 
so does processing time (hello, quadratic bottleneck!).

Transformers are undeniably effective, storing every detail fro
m the past for theoretically perfect recall.

On the other hand, traditional RNN (Recurring Neural Networks)– forget a l
ot, retaining only a small portion in their hidden state and discarding the rest. This makes them highly efficient but l
ess effective since discarded information cannot be retrieved.

Finding the Sweet Spot - **Enter Mamba** 🐍.

Mamba belon
gs to a class of models known as State Space Models (SSMs). SSMs excel in understanding and predicting how systems (like
 cars) evolve based on measurable data.

Notably, Mamba offers comparable performance and scalability to Transformers bu
t crucially eliminates the quadratic bottleneck in the Attention Mechanism.

Language models are good at summarizing tex
t, though some details may be lost. However, summarizing other forms of content, like a two-hour movie, is trickier.

Th
is is where Mamba's long-term memory comes into play, enabling the model to retain important information.

Why should yo
u care? Mamba could be a game-changer for tasks requiring extensive context, like:

1. DNA processing 🧬

2. Report writi
ng 📚

3. Agents with long-term memory and goals 🤖(Mistral - Codestral Mamba)


```
---

     
 
all -  [ how to instruct GPT4 to format text?  ](https://www.reddit.com/r/LangChain/comments/1e71886/how_to_instruct_gpt4_to_format_text/) , 2024-07-21-0912
```
how do you do it? I would like the reponse to be properly formatted in markdown for example. This does work somewhat but
 it still uses some non-unicode formatting for example: '\\( LAF,max \\geq 45 \\)' instead of using '≥'. Even with one-s
hot prompting it does not follow the instructions properly. 

  
Maybe there is another model that is trained on this ta
sk? Any suggestions? How do you solve this?
```
---

     
 
all -  [ How to use Langchain with Portkey AI? (I'm beginner with LLMs) ](https://www.reddit.com/r/LangChain/comments/1e7093e/how_to_use_langchain_with_portkey_ai_im_beginner/) , 2024-07-21-0912
```
Hello,

I am currently looking into using LLMs for a project and figured Portkey might be a good start to test out diffe
rent models. With a bit of research I saw that langchain is basically the number one library for doing this kind of thin
gs, because of RAG support etc.

What I do not quite understand is how do I integrate Portkey-AI with Langchain? I am qu
ite confused here, would appreciate any input on this topic. Thanks!
```
---

     
 
all -  [ Arabic PDF RAG ](https://www.reddit.com/r/LangChain/comments/1e6zj3b/arabic_pdf_rag/) , 2024-07-21-0912
```
Helllo guys, i am trying to create a PDF chatbot using Huggingface models. Open source embeddings and Open source LLM. H
ave anyone does this before  or have similar kind of project ? I would be grateful if you help me . 
```
---

     
 
all -  [ How to trace cost of RAGAS? ( I am using LANGFUSE) ](https://www.reddit.com/r/LangChain/comments/1e6yz2y/how_to_trace_cost_of_ragas_i_am_using_langfuse/) , 2024-07-21-0912
```
I use this code and decorator ***observe()*** to trace ragas cost. However, as you can see the result below. Total cost 
is 0$ for function ***score\_with\_ragas()***

  
Any simple ideas to help? Thank you. 

https://preview.redd.it/lvjrbdg
eufdd1.png?width=2594&format=png&auto=webp&s=948f921caf2cb56f5592ec39f161f4527438d286

    from app.core.services.openai
 import llm
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import LangchainLLMWrapper
 
   from ragas.metrics import answer_relevancy, faithfulness, context_utilization
    from ragas.metrics.critique import 
harmfulness
    
    from app.biz.performance.base import init_ragas_metrics
    from app.core.services.store import emb
eddings
    
    # metrics you chose
    metrics = [faithfulness, answer_relevancy, context_utilization, harmfulness]
  
  
    init_ragas_metrics(
        metrics,
        llm=LangchainLLMWrapper(llm),
        embedding=LangchainEmbeddingsW
rapper(embeddings),
    )

    import asyncio
    
    from langfuse.decorators import observe
    
    from app.core.da
tasets.main import dataset, langfuse
    from app.core.services.performance import metrics
    
    
    @observe(as_typ
e='generation')
    async def score_with_ragas(query, chunks, answer, ground_truths):
        scores = {}
        for m 
in metrics:
            print(f'calculating {m.name}')
            scores[m.name] = await m.ascore(
                row=
{'question': query, 'contexts': chunks, 'answer': answer, 'ground_truths': ground_truths}
            )
        return s
cores
    
    
    # Function to handle the full process including scoring
    async def main():
        for row in dat
aset:
            question, contexts, answer, ground_truths = (row['question'], row['contexts'], row['answer'],
        
                                                 row['ground_truths'])
            trace = langfuse.trace(name='rag', in
put=question,
                                   output={
                                       'answer': answer,
     
                                  'contexts': contexts
                                   })
            # pass it as sp
an
            trace.span(
                name='retrieval', input={'question': question, 'ground_truths': ground_truths
},
                output={'contexts': contexts}
            )
            # use llm to generate a answer with the chunk
s
            # answer = get_response_from_llm(question, chunks)
            answer = row['answer']
            trace.sp
an(
                name='generation', input={'question': question, 'contexts': contexts, 'ground_truths': ground_truths
},
                output={'answer': answer}
            )
    
            ragas_scores = await score_with_ragas(questi
on, contexts, answer, ground_truths)
            for m in metrics:
                trace.score(name=m.name, value=ragas_
scores[m.name])
    
    
    # Run the main function
    asyncio.run(main())
    
```
---

     
 
all -  [ Why my RAG is a bad RAG ? ](https://www.reddit.com/r/LangChain/comments/1e6yskw/why_my_rag_is_a_bad_rag/) , 2024-07-21-0912
```
    import streamlit as st
    import os 
    from langchain_openai import ChatOpenAI 
    from langchain_core.messages 
import HumanMessage, AIMessage, SystemMessage
    from dotenv import load_dotenv 
    from llama_parse import LlamaParse
 
    from langchain_community.document_loaders import UnstructuredMarkdownLoader 
    from langchain.text_splitter impo
rt RecursiveCharacterTextSplitter  
    from langchain_openai import OpenAIEmbeddings
    
    from pinecone import Pine
cone, ServerlessSpec  
    from langchain_pinecone import PineconeVectorStore  
    from langchain.retrievers import Con
textualCompressionRetriever
    from cohere.client import Client as CohereClient
    from langchain_cohere import Cohere
Rerank  
    from langchain.chains import create_retrieval_chain
    from langchain.memory import ConversationSummaryMem
ory
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains.combine_documents import create_
stuff_documents_chain
    from langchain.chains import create_history_aware_retriever
    from langchain_core.prompts im
port MessagesPlaceholder
    from langchain_core.chat_history import BaseChatMessageHistory
    from langchain_community
.chat_message_histories import ChatMessageHistory
    from langchain_core.runnables.history import RunnableWithMessageHi
story
    
    import asyncio
    import joblib
    import nest_asyncio
    
    load_dotenv()
    
    nest_asyncio.app
ly()
    
    # clear console function
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # 
OpenAI setup
    openai_api_key = os.getenv('OPENAI_API_KEY')
    llm = ChatOpenAI(
        api_key=openai_api_key,
    
    temperature=0,
        model='gpt-3.5-turbo-0125',
        streaming=True,
    )
    
    # Pinecone setup (for vect
or storage)
    api_key_pinecone = os.getenv('PINECONE_API_KEY')
    pc = Pinecone(api_key=api_key_pinecone)
    
    # 
Cohere setup (for reranking)
    cohere_api_key = os.getenv('COHERE_API_KEY')
    cohere_client = CohereClient(api_key=c
ohere_api_key)
    
    # Cohere model API key and configuration
    embeddings = OpenAIEmbeddings(model='text-embedding
-3-large')
    
    # Initialize Pinecone Vector Store
    vectorStore = PineconeVectorStore(index_name='rag-newchatmode
l', embedding=embeddings)
    
    # Creating pkl string (required for llamaParser to work efficiently)
    def create_p
kl_string(filename):
        file_name, extension = os.path.splitext(filename)
        new_string = file_name + '.pkl'
 
       return new_string
    
    # Loading and Parsing Data with the help of LlamaParse
    def load_or_parse_data(file
_name):
        # LlamaParse creates a pkl file
        # PDF -> pkl -> md -> vector 
        changed_file_ext = create_
pkl_string(file_name)
        data_file = f'data/{changed_file_ext}'
    
        if os.path.exists(data_file):
        
    # Load the parsed data from the file
            parsed_data = joblib.load(data_file)
        else:
            # Pe
rform the parsing step and store the result in llama_parse_documents
            parsingInstructionUber10k = '''The prov
ided document is unstructured
            It contains many tables, text, image and list.
            Try to be precise w
hile answering the questions'''
            parser = LlamaParse(
                api_key='llamaparse-api-key',
         
       result_type='markdown', # we want md file back
                parsing_instruction=parsingInstructionUber10k,
   
             max_timeout=5000,
            )
            llama_parse_documents = parser.load_data(f'PDF_PATH/{file_name}
')
            # Save the parsed data to a file
            print('Saving the parse results in .pkl format ..........')

            joblib.dump(llama_parse_documents, f'data/{file_name}')
    
            # Set the parsed data to the variab
le
            parsed_data = llama_parse_documents
    
        return parsed_data
    
    # Create vector database
   
 def create_vector_database(file_name):
        '''
        Creates a vector database using document loaders and embeddi
ngs.
    
        This function loads urls,
        splits the loaded documents into chunks, transforms them into embedd
ings using OllamaEmbeddings,
        and finally persists the embeddings into a Chroma vector database.
        '''
    
    print(file_name)
        # Call the function to either load or parse the data
        llama_parse_documents = load_o
r_parse_data(file_name)
        with open('data/output.md', 'w', encoding='utf-8') as f:
            for doc in llama_pa
rse_documents:
                f.write(doc.text + '\n')
    
        markdown_path = 'data/output.md'
        print('mar
kdown_path', markdown_path)
        loader = UnstructuredMarkdownLoader(markdown_path, encoding='utf-8')
    
        do
cuments = loader.load()
    
        # Split loaded documents into chunks
        text_splitter = RecursiveCharacterText
Splitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)
    
        # Prep
are texts and metadatas
        texts = [d.page_content for d in docs]
        metadatas = [d.metadata for d in docs]
  
  
        # Inserting to index
        PineconeVectorStore.from_texts(
            texts, embeddings, index_name='rag-n
ewchatmodel', metadatas=metadatas
        )
    
        print('Vector DB created successfully !')
        return
    
 
   async def convert_to_vector(file_path, file_name):
        index_name = 'rag-newchatmodel'
        # Check if the ind
ex exists
        existing_indexes = pc.list_indexes()
        if existing_indexes and existing_indexes[0].name == index
_name:
            # Delete the old index
            pc.delete_index(index_name)
            existing_indexes = pc.list
_indexes()
    
        # Create a new data
        pc.create_index(
            name=index_name,
            dimension=
3072,
            metric='cosine',
            spec=ServerlessSpec(cloud='aws', region='us-east-1'),
        )
        c
reate_vector_database(file_name)
    
    # PDF files directory (to save PDF files to local db)
    save_folder = 'PDF_P
ATH'
    
    if 'file_uploader_key' not in st.session_state:
        st.session_state['file_uploader_key'] = 0
    
   
 if 'uploaded_files' not in st.session_state:
        st.session_state['uploaded_files'] = []
    
    # File uploader i
n the sidebar (Streamlit's PDF uploader widget)
    files = st.sidebar.file_uploader(
        'Upload File', type=['pdf'
], accept_multiple_files=True,key=st.session_state['file_uploader_key'],
    )
    
    if files:
        for uploaded_f
ile in files:
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
    
            
file_path = os.path.join(save_folder, uploaded_file.name)
            with open(file_path, mode='wb') as w:
            
    w.write(uploaded_file.getvalue())
                file_name = uploaded_file.name
                asyncio.run(convert
_to_vector(file_path, file_name))
                st.sidebar.success(f'File {uploaded_file.name} uploaded successfully!'
)
                st.session_state['file_uploader_key'] += 1
            st.rerun()
    
    # Function to list files in
 a directory
    def list_files_in_directory(directory):
        if os.path.exists(directory):
            return os.lis
tdir(directory)
        return []
    
    # Display the list of uploaded files with delete buttons
    st.sidebar.write
('### Uploaded Files:')
    uploaded_files_list = list_files_in_directory(save_folder)
    
    # Function to delete a f
ile
    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
    
    for 
file in uploaded_files_list:
        file_path = os.path.join(save_folder, file)
        col1, col2 = st.sidebar.columns
([3, 1])
        col1.write(file)
        if col2.button('❌', key=file):
            delete_file(file_path)
            
st.rerun()  # Refresh the app to update the file list
    
    # Reranker 
    def reRanker():
        compressor = Cohe
reRerank(client=cohere_client)
        compression_retriever = ContextualCompressionRetriever(
            base_compress
or=compressor,
            base_retriever=vectorStore.as_retriever(
                search_kwargs={'k': 5},
            
),
        )
        return compression_retriever
    
    # Initialize store if not in session state
    if 'store' not
 in st.session_state:
        st.session_state.store = {}
    
    ### Statefully manage chat history ###
    store = {}

    
    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in st.session_st
ate.store:
            st.session_state.store[session_id] = ChatMessageHistory()
        return st.session_state.store[s
ession_id]
    
    contextualize_q_system_prompt = (
        'Given a chat history and the latest user question '
     
   'which might reference context in the chat history, '
        'formulate a standalone question which can be understoo
d '
        'without the chat history. Do NOT answer the question, '
        'just reformulate it if needed and otherwis
e return it as is.'
    )
        
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            
('system', contextualize_q_system_prompt),
            MessagesPlaceholder('chat_history'),
            ('human', '{inpu
t}'),
        ]
    )
    
    compression_retriever = reRanker()
    
    history_aware_retriever = create_history_awar
e_retriever(
        llm, compression_retriever, contextualize_q_prompt
    )
    
    
    # After 19 July
    system_p
rompt = (
        'You are an assistant for question-answering tasks specifically about the provided PDF documents.' 
  
      'Follow the prompt STRICTLY but DO ensure that you don't answer any question out of context.'
        'Use ONLY th
e following pieces of retrieved context to answer the question.' 
        'Provide answers exactly as they are written i
n the PDF, quoting or paraphrasing text directly from the provided context.' 
        'If you can't find the answer in t
he given context, say 'I'm sorry, but I couldn't find information about that in the provided PDF documents.' ' 
        
' Do not use any external knowledge.'
        '\n\n'
        '{context}'
    )
    
    chatPrompt = ChatPromptTemplate.
from_messages(
        [
            ('system', system_prompt),
            MessagesPlaceholder('chat_history'),
       
     ('human', '{input}'),
        ]
    )
        
    question_answer_chain = create_stuff_documents_chain(llm, chatPr
ompt)
    
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    conversationa
l_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key='in
put',
        output_messages_key='answer',
        history_messages_key='chat_history',
    )
    
    
    # generate 
response 
    def generate_response(prompt: str) :
        for chunk in conversational_rag_chain.stream(input={'input': 
prompt},config={'configurable': {'session_id': 'gaurav'}}):
            answer_chunk = chunk.get('answer')
            i
f answer_chunk:
                yield answer_chunk
    
    
    # Render chat history
    session_id = 'gaurav'  # Defi
ne your session ID
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
 
   # Conversation History
    for message in st.session_state.chat_history:
        if isinstance(message,HumanMessage):

            with st.chat_message('Human'):
                st.markdown(message.content)
        else:
            with 
st.chat_message('AI'):
                st.markdown(message.content)
    
    
    prompt = st.chat_input('Hey, What's up
?')
    
    if prompt is not None and prompt !='' :
        st.session_state.chat_history.append(HumanMessage(prompt))

        with st.chat_message('Human'):
            st.markdown(prompt)
    
        if len(pc.list_indexes()) == 0:
    
        st.error('Please upload some files first!')
        else:
            with st.chat_message('AI'):
              
  ai_response = st.write_stream(generate_response(prompt))
    
            st.session_state.chat_history.append(AIMessa
ge(ai_response))
    
```
---

     
 
all -  [ PSA: LangGraph removed the support for self hosting ](https://www.reddit.com/r/LangChain/comments/1e6xli4/psa_langgraph_removed_the_support_for_self_hosting/) , 2024-07-21-0912
```
Heads up, folks! If you're considering LangGraph for your projects, especially for production, here's something you need
 to know. LangGraph has recently removed the option to self-host. This means you can only use their cloud platform from 
now on. 

Here is the commit where they removed instructions on how to self host from the readme: [https://github.com/la
ngchain-ai/langgraph-example/commit/215ef6eb2f653e46cfb442aeed2978c703781a01](https://github.com/langchain-ai/langgraph-
example/commit/215ef6eb2f653e46cfb442aeed2978c703781a01)

While it might seem convenient, there are some significant ris
ks and disadvantages you should consider.

First off, **data ownership**. When you use their cloud service, you're essen
tially handing over your data to them. This raises concerns about privacy and security, especially if you're dealing wit
h sensitive or proprietary information. You're trusting LangGraph to handle and protect your data properly, but you lose
 control over how it's stored and managed.

Secondly, you're **at the mercy of the platform**. If their service experien
ces downtime or technical issues, your system will be affected. This is a huge risk if you're running a production envir
onment where uptime is critical. Any changes they make to their service, pricing, or terms can impact you directly, and 
you have no say in the matter.

This also means that using the cloud version means you're **subject to their updates and
 changes**. They can roll out updates that might not align with your needs or even disrupt your existing setup. This lac
k of control can be frustrating, especially if your project relies on specific features or configurations.

Losing the a
bility to self-host means you sacrifice control over your data and are **fully dependent on their platform's reliability
 and policies**. If these risks are a concern for you, it might be worth looking into alternative solutions that offer s
elf-hosting options or more control over your production environment.
```
---

     
 
all -  [ Routing Use of Langchain Application ](https://www.reddit.com/r/LangChain/comments/1e6x8mb/routing_use_of_langchain_application/) , 2024-07-21-0912
```
HI

  
I am learning langchain these days and what I observe in youtube tutorials that they create chat applications mos
tly in which you get different responses like changing the tone of customer language, get replies to queries from docume
nts etc..

This is what we can do with chatgpt, co-pilot as well. Then how we use langchain in pratical life? Also is th
ere any tutorial on youtube which really create something which we actually use for businesses?
```
---

     
 
all -  [ Retreiving Metadata from Documents ](https://www.reddit.com/r/LangChain/comments/1e6vqw0/retreiving_metadata_from_documents/) , 2024-07-21-0912
```
Hi, I am able to upload the pdf file using the unstrucutred loader and query the PDf file, but I ask something like, Can
 you mention the source file to LLM? It is not answering.

The workflow is

1. Uploading files using an unstructured loa
der, Text Splitter

2. Creating Embeddings

3. Storing in Vector DB

4. creating a retriever (as\_retriever)

5. Creatin
g a Tool

6. creating a conversational agent.

Is there any way to do it?
```
---

     
 
all -  [ Please roast my Resume, current MSCS student graduating May/December 2025 looking for internship/ful ](https://www.reddit.com/r/resumes/comments/1e6vfps/please_roast_my_resume_current_mscs_student/) , 2024-07-21-0912
```
Please help me improve my resume. I just started looking for internships/full-times but haven't landed any interviews ye
t.

[resume](https://preview.redd.it/xwq4gfs7oedd1.png?width=1090&format=png&auto=webp&s=f268b028e26d26f80bf937433fc4318
b48d11d90)


```
---

     
 
all -  [ Guide to create a RAG Agent ](https://www.reddit.com/r/LangChain/comments/1e6umwn/guide_to_create_a_rag_agent/) , 2024-07-21-0912
```
**Introduction**

Hey everyone! 🚀 I’m excited to share a new project: a Retrieval-Augmented Generation (RAG) Agent lev
eraging CrewAI, Composio, and ChatGPT to perform web searches and compile research reports.

**Objectives**

This pr
oject aims to create an intelligent agent that can enhance research capabilities by combining powerful AI tools to searc
h the web and generate comprehensive reports.

**Implementation Details**

* **Tools Used**: Composio, CrewAI, ChatG
PT, Python
* **Setup**:
   1. Navigate to the project directory.
   2. Run the setup file.
   3. Fill in the `.env` 
file with your secrets.
   4. Run the Python script.

**Results**

The RAG agent streamlines the process of conduct
ing web searches and generating research reports, making it a valuable tool for researchers, students, and professionals
.

[REPO LINK](https://git.new/RAGagent)
```
---

     
 
all -  [ Analyze failure modes in code ](https://www.reddit.com/r/LangChain/comments/1e6sdyi/analyze_failure_modes_in_code/) , 2024-07-21-0912
```
My company has a support team to which we want to transition our application to. My task is to automate the process of c
reating the FMEA document. 
I started using genetic RAG with both code tool and documents tool. For code I used summaryi
ndex and set relationships using references of function calls. For documents I used vector index. 
My hope is to prompt 
it the right way to get the failure mode created but the problem is the agent is using one tool or the other but never c
ombined the two. Also when it is making some observations that sounds useful but is not in the final answer. How do I go
 about fixing this?
```
---

     
 
all -  [ Why GPT 4o Mini not be the foundation of Agentic Workflows?
 ](https://www.reddit.com/r/LangChain/comments/1e6pizc/why_gpt_4o_mini_not_be_the_foundation_of_agentic/) , 2024-07-21-0912
```
[There’s been a huge rise in papers on LLM-based agents in the two years,](https://arxiv.org/abs/2309.07864) showing obv
ious benefits in output quality and complexity of the task that can be handled. There are 2 obvious problems:

* Latency
: because agents are talking to each other — usually sequentially — output generation will take longer.
* Cost: much mor
e tokens are being spent on feeding one output to another input. Over and over.

But these are exactly the things GPT 4o
 Mini concerns itself with. I’m actually incorporating it right now into some preprocessing workflows we have at [adorno
.ai](https://adorno.ai/). On principle, I dislike OpenAI, but it seems they've hit the ball out of the park? Again. I'm 
looking for criticism against 4o Mini? Right now it's just rainbows and unicorns, but why is it overhyped?

(I've got a 
full blog post on the subject here: [https://chrisjanwust.medium.com/at-15c-million-tokens-will-gpt-4o-mini-be-the-found
ation-of-agentic-workflows-7fd189138da4](https://chrisjanwust.medium.com/at-15c-million-tokens-will-gpt-4o-mini-be-the-f
oundation-of-agentic-workflows-7fd189138da4) )


```
---

     
 
all -  [ Seeking help and referrals for jobs in Pune ](https://www.reddit.com/r/pune/comments/1e6jnhl/seeking_help_and_referrals_for_jobs_in_pune/) , 2024-07-21-0912
```
I have been searching for jobs for almost a couple of months now. I had been working in a startup previously due to whic
h I opted out for placement scenario in our college. Although, I had to let go of the startup due to a lot of unresolvab
le conflicts.  
I am looking for jobs in Pune at the moment and I am unable to get through initial screening due to heav
y volume of applications where my resume gets lost despite being a better one amongst my peers. Also, many companies are
 picking talents from the campus but aren't picking someone more talented from out of the campus easily.  
I have been a
t my lowest lately, bugged up with a lot of factors. I really really will  be very thankful for any referral or help int
o their companies, whoever is working in Pune.  
From one brother to another, I need help.  
Any suggestions or help wou
ld be welcome, coming from the heart



https://preview.redd.it/afcyovdavbdd1.png?width=762&format=png&auto=webp&s=b0099
ea2f496f8ca6cf199fadf4d82d61f573c34
```
---

     
 
all -  [ Building a RAG with LlamaIndex vs Langchain ](https://www.reddit.com/r/LocalLLaMA/comments/1e6ir2f/building_a_rag_with_llamaindex_vs_langchain/) , 2024-07-21-0912
```
**What did I build?**

I built a tool that’s like a “Chat with PDF” for software/API documentation. You can have an on d
emand RAG system up and running in a few seconds for any doc and you can share it with anyone. This came out of my exper
ience coding and realising how important it is, but its also pretty confusing and difficult if you’re someone new.

link
 if you want to try it: [https://huggingface.co/spaces/Prat0/ClarifyAI](https://huggingface.co/spaces/Prat0/ClarifyAI)


**Overview of Llama Index**

Llama Index is designed specifically for building search and retrieval applications. It pro
vides a simple interface for querying large language models (LLMs) and retrieving relevant documents. Llama Index excels
 in data indexing and retrieval, making it suitable for production-ready RAG applications.

# Key Features of Llama Inde
x

* **Data Indexing and Retrieval**: Llama Index is optimized for indexing and retrieving data efficiently. It converts
 documents into individual nodes for indexing, establishing relationships between these nodes to provide context for the
 information.
* **Simple Interface**: The framework offers a straightforward interface for querying LLMs and retrieving 
relevant documents, making it easy to use for developers.
* **Evaluation Metrics**: Llama Index provides components for 
evaluating RAG-related metrics, such as the retriever, query engine, and response generation

**Overview of Langchain**


Langchain is a more general-purpose framework that simplifies the development and deployment of LLM-powered application
s. It offers a modular and extensible architecture, empowering developers to combine LLMs with various data sources and 
services.

# Key Features of Langchain

1. **Modular Architecture**: Langchain's modular design allows developers to cre
ate diverse LLM architectures, making it suitable for a wide range of applications.
2. **Out-of-the-Box Components**: La
ngchain provides a variety of out-of-the-box components, such as LangSmith, which offers basic organization and versioni
ng of prompts, facilitating the creation of complex AI workflows.

* **Evaluation Suite**: Langchain's LangSmith evaluat
or suite offers more options for general LLM tasks, though it is primarily used for tracing and debugging rather than ev
aluation

# Comparison of Llama Index and Langchain

|Feature|Llama Index|Langchain|
|:-|:-|:-|
|Focus|Data indexing and
 retrieval|General-purpose framework|
|Architecture|Specialized for search and retrieval|Modular and extensible|
|Compon
ents|Node parsers and simple interface|Out-of-the-box components and LangSmith|
|Evaluation|RAG-related metrics|General 
LLM tasks|
|Complexity|Simplified for production-ready RAG|Complex for diverse applications|
|Strength|Llama Index ‘s st
rength lies in code that helps you achieve efficient indexing and querying.|Langchain's strength lies in its support for
 agents and tools.|
```
---

     
 
all -  [ Using create_pandas_dataframe_agent as a tool ](https://www.reddit.com/r/LangChain/comments/1e6hrjb/using_create_pandas_dataframe_agent_as_a_tool/) , 2024-07-21-0912
```
Are you able to create a tool using create\_pandas\_dataframe\_agent?

I am looking to create a chat agent that will be 
able to tell if it should use the create\_pandas\_dataframe\_agent to answer data about specific data, or use a retrieva
l tool and RAG if that is the correct route to extract the desired data.

I have gotten the pandas agent and the retriev
al tool to work independently of each other, but can not get them to work as one agent. Is this the correct way of going
 about solving this problem? Is it even possible?

Any help would be greatly appreciated. Thanks in advance!
```
---

     
 
all -  [ IP address range filter for RAG ](https://www.reddit.com/r/LangChain/comments/1e6hls9/ip_address_range_filter_for_rag/) , 2024-07-21-0912
```
I have two indexes with my pinecone vector databases, one has the sensitive and private data of my org, while other has 
embeddings related to open data.

I want to divert the IP address accordingly, if a user belongs to my org (which is not
ed because of particular IP address range) he must be directed to index which has private and org specific data, while a
 non-org user must be routed to different index which has public data.

Based on the above requirements I have two quest
ions :-

1. Can we achieve it without building and leveraging on AWS architectures AWS Sagemaker, if yes then how?

2. I
f we use AWS sagemaker and deploy this rag+llm model on AWS or build my model by using foundational model of AWS then ho
w can this be achieved.

 
Looking forward for the views.
```
---

     
 
all -  [ Where can i start learning Langchain? ](https://www.reddit.com/r/LangChain/comments/1e6gyij/where_can_i_start_learning_langchain/) , 2024-07-21-0912
```
As the title suggests , please recommend a tutorial  / course to implement a RAG.  
I wnat to query a large csv data set
 using a langchain
```
---

     
 
all -  [ How to integrate python project to a website ](https://www.reddit.com/r/learnmachinelearning/comments/1e6gava/how_to_integrate_python_project_to_a_website/) , 2024-07-21-0912
```
Hii ,
I have created a simple chatbot using langchain , it extracts text from pdf , creates a vector data base and then 
you can ask questions and it will give answers from the data in pdf. I want to integrate it to a website as a FAQ handli
ng system, how can i do it?
I have no prior experience of web development.Please anyone guide me.
```
---

     
 
all -  [ How to implement a RAG with different data sources  ](https://www.reddit.com/r/LangChain/comments/1e6g04p/how_to_implement_a_rag_with_different_data_sources/) , 2024-07-21-0912
```
I'm implementing a RAG with mongo and SQL as data connectors. Each store different entities of data. Now, I want to retr
ieve data based on question asked by user. I tried an approach initially.
I used an LLM to conditionally route to specif
ic data source based on the question user asked. Then, for mongo, I used vector database from mongo and for SQL I genera
ted SQL query using LLM and pass the retrieved data to an LLM to generate an answer. 

I know this is a basic approach a
nd main issue is it is taking so much time. Is there any better and efficient methods to perform a same task.
```
---

     
 
all -  [ The best way to create ask your document RAG system ](https://www.reddit.com/r/LangChain/comments/1e6eqrb/the_best_way_to_create_ask_your_document_rag/) , 2024-07-21-0912
```
Hello guys, I am working on project for chatting with your documents (PDF mostly), so i built a basic RAG system using l
angchain, Unstructured for extraction, qdrant db for indexing and Nvidia qa embedding for embedding, and it’s good but i
t’s not fascinating especially in the chunking and retrieving parts btw i used recursive text splitter, so guys can you 
help me and tell me some advanced approaches for chatting with your pdf, and make it more accurate 
```
---

     
 
all -  [ Does anyone know why `from langchain_google_vertexai import VertexAIEmbeddings` is so slow?  ](https://www.reddit.com/r/GoogleGeminiAI/comments/1e6egdj/does_anyone_know_why_from_langchain_google/) , 2024-07-21-0912
```
It frequently takes 3+ secs to load or it's stuck on it intermittently.  
```
---

     
 
all -  [ Different Output when using SentenceSplitter/TokenTextSplitter on Document and raw text ](https://www.reddit.com/r/LlamaIndex/comments/1e6d6pe/different_output_when_using/) , 2024-07-21-0912
```
    token_splitter = TokenTextSplitter(chunk_size=50, chunk_overlap=5)
    
    text = '''
    Language models that use 
a sequence of messages as inputs and return chat messages as outputs (as opposed to using plain text). These are traditi
onally newer models (older models are generally LLMs, see below). Chat models support the assignment of distinct roles t
o conversation messages, helping to distinguish messages from the AI, users, and instructions such as system messages. 

    Although the underlying models are messages in, message out, the LangChain wrappers also allow these models to take 
a string as input. This means you can easily use chat models in place of LLMs. When a string is passed in as input, it i
s converted to a HumanMessage and then passed to the underlying model. 
    LangChain does not host any Chat Models, rat
her we rely on third party integrations. We have some standardized parameters when constructing ChatModels:
    '''
    
document = Document(text=text)
    text_split_res = token_splitter.split_text(text)
    doc_split_res = token_splitter.g
et_nodes_from_documents([document])

  
Can someone explain why \`text\_split\_res\` and \`doc\_split\_res\` have differ
ent output?

    print(doc_split_res[-1].text)
    print('*' * 60)
    print(text_split_res[-1])

Output

    and then p
assed to the underlying model. 
    LangChain does not host any Chat Models, rather we rely on third party integrations.
 We have some standardized parameters when constructing ChatModels:
    ************************************************
************
    model. 
    LangChain does not host any Chat Models, rather we rely on third party integrations. We hav
e some standardized parameters when constructing ChatModels:


```
---

     
 
all -  [ VectorDB vs SerpAPI ](https://www.reddit.com/r/LangChain/comments/1e6bz6y/vectordb_vs_serpapi/) , 2024-07-21-0912
```
I am implementing RAG using two separate approaches: one with Vector DB and another with Serp API. I have found that Ser
p API is better at capturing the context of the query. I would like to know the use cases for when to use Vector DB and 
when to use Serp API for document search. I know perplexity uses only Serp API and not Vector DB.
```
---

     
 
all -  [ How can i create Medical RAG chatbot.  ](https://www.reddit.com/r/LangChain/comments/1e6bic0/how_can_i_create_medical_rag_chatbot/) , 2024-07-21-0912
```
Hello!
 
I'm currently planning to develop a medical RAG chatbot.

The user will start by filling out a comprehensive qu
estionnaire that includes details such as their name, age, blood group, blood test results, medical history, and other r
elevant medical records.

After the user submits this form, their responses will be processed by an LLM to generate pers
onalized treatment plans, exercise routines, meal recommendations, and sleep schedules, among other tailored advice.

An
y assistance or suggestions for relevant open-source repositories would be greatly appreciated.

Thank you!
```
---

     
 
all -  [ Can I access a URL documentation using Langchain/ Anthropic API? ](https://www.reddit.com/r/ClaudeAI/comments/1e6b04j/can_i_access_a_url_documentation_using_langchain/) , 2024-07-21-0912
```
hi

I'm building a RAG system and while I have some documentation in the vector database which is more specific, I have 
the product documentation on a public URL.  When a user asks a question, I'm thinking it should retrieve the context fro
m the vector db and then access the URL documentation as well. Has anyone tried this and what tools have they used?
```
---

     
 
all -  [ Template to use Microsoft SharePoint as a data source for Enterprise RAG pipelines
 ](https://www.reddit.com/r/LangChain/comments/1e6aby5/template_to_use_microsoft_sharepoint_as_a_data/) , 2024-07-21-0912
```
Hi r/langchain,

Microsoft SharePoint is to enterprises what Google Drive is to consumers. Happy to share my work on an 
app template that makes it easy to build applications that deliver up-to-date answers using your RAG pipeline with Share
Point data. 

* Repo Link: [~https://pathway.com/developers/templates/enterprise\_rag\_sharepoint~](https://pathway.com/
developers/templates/enterprise_rag_sharepoint)

Thousands of employees at large corporations collaborate and make chang
es in the documents stored in Microsoft SharePoint folders – making it a valuable data source for dynamic RAG/Gen AI app
lications to boost productivity. 

However, existing connectors for SharePoint lack necessary security features. My temp
late covers:

* Real-Time Sync with changes in your SharePoint files, with the help of Pathway (link: [~Pathway Vector S
tore on LangChain~](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pathway/)).
* Step by step process 
to setup Entra ID and SSL authentication. 
* Security and Scalability, given the choice of frameworks and minimalistic a
rchitecture.
* Ease of Setup to help you run the app template in Docker within minutes.

I plan to further refine this b
y using:

* [~Adaptive RAG~](https://pathway.com/developers/templates/adaptive-rag): Implementing cost-effective strateg
ies without sacrificing accuracy.
* [~Pathway Rerankers~](https://pathway.com/developers/user-guide/llm-xpack/overview/#
rerankers): Integrating advanced reranking techniques for improved results.
* [~Multimodal Pipelines with Hybrid Indexes
~](https://github.com/pathwaycom/llm-app/tree/main/examples/pipelines/slides_ai_search): Using advanced parsing capabili
ties and indexing techniques

🤝 Let's Discuss! I'm open to your questions and feedback!
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-21-0912
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-21-0912
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-21-0912
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
