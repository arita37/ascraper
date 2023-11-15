 
all -  [ Personalizing Cold Email Campaigns with Low Code and AI ](https://www.reddit.com/r/email/comments/17vg9bc/personalizing_cold_email_campaigns_with_low_code/) , 2023-11-15-0910
```
Hello r/email community! In this article, I will explain how the AI framework LangChain can significantly enhance the qu
ality of your cold email outreach by making it unique and personalized. I will also discuss how to automate this entire 
process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Personalizati
on vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic emails are
 easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized emails incre
ase engagement but are difficult to automate.

https://preview.redd.it/j1bwi6058e0c1.png?width=960&format=png&auto=webp&
s=6858e752fd14b1756bb25d64be9ab87ca640a634

Cold email platforms now help solve this issue with dynamic variables that a
dd a personalized touch to automated emails. These variables act as placeholders for inserting personalized words, lines
, or paragraphs.

https://preview.redd.it/acp1c0p68e0c1.png?width=960&format=png&auto=webp&s=f3f74318e0e910807c654e86017
cbc9dde7ef53e

Dynamic variables allow companies to balance personalization and automation efficiently. Today, we'll cre
ate a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for each conta
ct in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low-code pla
tform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google Sheet co
ntaining basic email addresses. I've included some of my work emails as real examples (please refrain from sending me pe
rsonalized cold emails after reading this! :) )

https://preview.redd.it/hz8cnng78e0c1.png?width=960&format=png&auto=web
p&s=cc993eeb8914d4244215466ac328ee4c05ba280f

First, we need to enrich these emails with data about the recipients. For 
our outreach, we need to know:

* The first name
* The company name
* The company description

You could manually visit 
each email domain to gather this information, but if you have hundreds or thousands of emails in your database, that's n
ot practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet there an
d use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/eaezi0j98e0c1.p
ng?width=960&format=png&auto=webp&s=5117bb4895c50b79797ee6682d463e2946d3c903

Don't worry! You don't have to create ever
ything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of this automa
tion are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to ClearBit and
 receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.redd.it/48
ikqdya8e0c1.gif

That's it. We've enriched our emails with essential details like the company description. Now, let's cr
aft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the start.

## 
Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at their workpla
ce is the very least you can do. Additionally, you could tailor your outreach reason based on the company's profile. You
 can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/cwu5se1f8e0c1.
png?width=960&format=png&auto=webp&s=b11a39241ad0d7949f8d74aecd34de7c91bcbfeb

Its main steps are:

* Retrieve the compa
ny description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom prompt tail
ored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the final resu
lt in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized icebreaker to
 each individual, creating another custom variable in addition to their first name and company name. This trio should su
ffice for a start. Let's look at how this functions:

https://i.redd.it/5qmvncrg8e0c1.gif

## Step 3: upload spreadsheet
 to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your email platfor
m as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.redd.it/ok3q
pskj8e0c1.png?width=960&format=png&auto=webp&s=ba442a942e657dc86328edebb8c0f6215e4f1913

The next steps are pretty stand
ard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.

https://p
review.redd.it/2n43akbm8e0c1.png?width=960&format=png&auto=webp&s=5472621693ca7d341431bc7ead25709973f7429b

Now, when co
mposing an email for a prospect, it works like this:

https://preview.redd.it/wmga34vl8e0c1.png?width=960&format=png&aut
o=webp&s=d78f05e097b4b4767ddf39dd0a74762079ca5fda

That's all for now. You can adjust the prompts sent to GPT in your La
tenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for any cold ou
treach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy these scenarios
: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and [**Icebrea
ker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

You just need
 to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which is free) an
d OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the team is alway
s ready to help with your automation journey
```
---

     
 
all -  [ Personalization of Cold Email Campaigns Using AI and Low Code ](https://www.reddit.com/r/Emailmarketing/comments/17vg46z/personalization_of_cold_email_campaigns_using_ai/) , 2023-11-15-0910
```
Hello r/Emailmarketing community! In this article, I will explain how the AI framework LangChain can significantly enhan
ce the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate thi
s entire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Pers
onalization vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic e
mails are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized ema
ils increase engagement but are difficult to automate.

https://preview.redd.it/0zv2yro48e0c1.png?width=960&format=png&a
uto=webp&s=fbaf60d0773c3a98317350baa3d5d74710f6802c

Cold email platforms now help solve this issue with dynamic variabl
es that add a personalized touch to automated emails. These variables act as placeholders for inserting personalized wor
ds, lines, or paragraphs.

https://preview.redd.it/tu8uqnf68e0c1.png?width=960&format=png&auto=webp&s=f320fc4e49e4586bb8
3c3101f99978416ee9374c

Dynamic variables allow companies to balance personalization and automation efficiently. Today, 
we'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for e
ach contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low
-code platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google
 Sheet containing basic email addresses. I've included some of my work emails as real examples (please refrain from send
ing me personalized cold emails after reading this! :) )

https://preview.redd.it/4yzqxqs78e0c1.png?width=960&format=png
&auto=webp&s=aea00e811c962c1435cf393b8796f8e903343fdb

First, we need to enrich these emails with data about the recipie
nts. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manual
ly visit each email domain to gather this information, but if you have hundreds or thousands of emails in your database,
 that's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet
 there and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/myw5ju
598e0c1.png?width=960&format=png&auto=webp&s=5d1f9a5d5f86c3fbe2c7394e63196713c441944c

Don't worry! You don't have to cr
eate everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of th
is automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to Cle
arBit and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.r
edd.it/ui07f7sb8e0c1.gif

That's it. We've enriched our emails with essential details like the company description. Now,
 let's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the st
art.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at thei
r workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's pro
file. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/ymyua
sre8e0c1.png?width=960&format=png&auto=webp&s=6eaac639e67475f13053ea69e1843b26b1a67dfb

Its main steps are:

* Retrieve 
the company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom pr
ompt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the f
inal result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized iceb
reaker to each individual, creating another custom variable in addition to their first name and company name. This trio 
should suffice for a start. Let's look at how this functions:

https://i.redd.it/vp59659h8e0c1.gif

## Step 3: upload sp
readsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your emai
l platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.red
d.it/4pdzl99j8e0c1.png?width=960&format=png&auto=webp&s=dc604bba8ec7b04d3a9f6cea095737d7822f25e3

The next steps are pre
tty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.


https://preview.redd.it/4hzxu8fk8e0c1.png?width=960&format=png&auto=webp&s=5699a5e309eea3e3c34d135bb972de7f1e2548fd

Now
, when composing an email for a prospect, it works like this:

https://preview.redd.it/eoycskkl8e0c1.png?width=960&forma
t=png&auto=webp&s=a73da9fe1d6b23fd0e3000cec28fdc1f6be61587

That's all for now. You can adjust the prompts sent to GPT i
n your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for an
y cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy these 
scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and [
**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

You 
just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which is
 free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the team
 is always ready to help with your automation journey
```
---

     
 
all -  [ Improving Your Email Campaigns: Personalizing Cold Outreach Emails with Low-Code and AI ](https://www.reddit.com/r/SaaS_Email_Marketing/comments/17vg326/improving_your_email_campaigns_personalizing_cold/) , 2023-11-15-0910
```
Hello r/SaaS_Email_Marketing community! In this article, I will explain how the AI framework LangChain can significantly
 enhance the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automa
te this entire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

#
# Personalization vs Automation

There's a natural tension between personalization and automation. Non-personalized, gen
eric emails are easy to automate but often result in low engagement and conversion rates. In contrast, highly personaliz
ed emails increase engagement but are difficult to automate.

https://preview.redd.it/ok81jo758e0c1.png?width=960&format
=png&auto=webp&s=887925d07e064ebefdce26782a8a2b64a5f7982b

Cold email platforms now help solve this issue with dynamic v
ariables that add a personalized touch to automated emails. These variables act as placeholders for inserting personaliz
ed words, lines, or paragraphs.

https://preview.redd.it/mg9g0n468e0c1.png?width=960&format=png&auto=webp&s=5515e9e34b84
3dbdf9b950e73a01d253a7eb7ca7

Dynamic variables allow companies to balance personalization and automation efficiently. T
oday, we'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker
 for each contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The fr
ee low-code platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a 
Google Sheet containing basic email addresses. I've included some of my work emails as real examples (please refrain fro
m sending me personalized cold emails after reading this! :) )

https://preview.redd.it/jlybbe488e0c1.png?width=960&form
at=png&auto=webp&s=f1e53ce1d32220d096da7ff1e0fbc654673ecb09

First, we need to enrich these emails with data about the r
ecipients. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could 
manually visit each email domain to gather this information, but if you have hundreds or thousands of emails in your dat
abase, that's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google
 Sheet there and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/
fkm067v88e0c1.png?width=960&format=png&auto=webp&s=a8aaffdea5eed89c9bdf312e052ac18ae1e8c767

Don't worry! You don't have
 to create everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps
 of this automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email 
to ClearBit and receive all the related information.
* Enter the required information back into the Google Sheet.

https
://i.redd.it/y5nwqiuc8e0c1.gif

That's it. We've enriched our emails with essential details like the company description
. Now, let's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from 
the start.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does a
t their workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company
's profile. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it
/je1rqnfe8e0c1.png?width=960&format=png&auto=webp&s=a20ce81d342f46616064b9fa70420caf884d3905

Its main steps are:

* Ret
rieve the company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a cus
tom prompt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place
 the final result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalize
d icebreaker to each individual, creating another custom variable in addition to their first name and company name. This
 trio should suffice for a start. Let's look at how this functions:

https://i.redd.it/xkmv8hth8e0c1.gif

## Step 3: upl
oad spreadsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to you
r email platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://previ
ew.redd.it/unddngwi8e0c1.png?width=960&format=png&auto=webp&s=3e582bc62df95572eafc6c0d3ea9f4f7cccd1f2b

The next steps a
re pretty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' fi
eld.

https://preview.redd.it/gdttd7rk8e0c1.png?width=960&format=png&auto=webp&s=181496f179c9d17492df3c49ae4f2d8fb13431b
b

Now, when composing an email for a prospect, it works like this:

https://preview.redd.it/vufns6bl8e0c1.png?width=960
&format=png&auto=webp&s=90932e96793d0cee51a43a059b5f2b29d70bddd3

That's all for now. You can adjust the prompts sent to
 GPT in your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile 
for any cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy 
these scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718) 
 and [**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)


You just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (wh
ich is free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where th
e team is always ready to help with your automation journey
```
---

     
 
all -  [ Build PDF.ai Clone with Flutter, Pinecone, Langchain and ChatGPT ](https://www.youtube.com/watch?v=y2va_4m9FLQ) , 2023-11-15-0910
```

```
---

     
 
all -  [ Comunidad argentina/latam de desarrolladores implementando AI? ](https://www.reddit.com/r/devsarg/comments/17veetm/comunidad_argentinalatam_de_desarrolladores/) , 2023-11-15-0910
```
Buenas! Estoy metiéndome en la nueva ola de armar un asistente para un dominio específico con el copilot stack.

Conocen
 otro sub, discord o telegram en español dónde se discutan específicamente temas técnicos como el uso de langchain o sem
antic kernel?

Algo como estos:

[https://www.reddit.com/r/LangChain/](https://www.reddit.com/r/LangChain/)

[https://ww
w.reddit.com/r/LocalLLaMA/](https://www.reddit.com/r/LocalLLaMA/)

[https://www.reddit.com/r/aipromptprogramming/](https
://www.reddit.com/r/aipromptprogramming/)
```
---

     
 
all -  [ Give me hell/help on my inference/home automation/game stream server concept. ](https://www.reddit.com/r/homelab/comments/17vcavk/give_me_hellhelp_on_my_inferencehome/) , 2023-11-15-0910
```
So basically I want to set up a big ole home server for:

Home automation, local llm and local game streaming whilst bei
ng as open source as possible. 

My plan is:

Server with either the classic dual 3090 setup, or ideally some AMD equiva
lent though I know ROCm is apparently not great but I'm also not a fan of nvidia's monopolistic ways, and some old threa
dripper. Basically using old server components to save money and have futureproofing. 

Running some lightweight Linux d
istro, probably debian or arch. 

Mistral 7b, quite lightweight, with llama.cpp which seems to have AMD support, + langc
hain hookup for my obsidian notes. 

Whisper for voice rec, though I might have to use something else for the initial wa
keword. 
Home assistant for the automation stuff, with different wake words for each and Piper tts/coqui for natural sou
nding responses. 

And for the game streaming thing I plan to use sunshine or potentially wolf serverside + moonlight on
 some mid tier office PC. Though I'm not sure if it'll enough to support 144hz over ethernet.

I'll probably crosspost t
his to /r/localllama or something similar. But, /r/homelab, any comments?
```
---

     
 
all -  [ Qdrant + JS / How to return vector embedding? ](https://www.reddit.com/r/LangChain/comments/17vat0w/qdrant_js_how_to_return_vector_embedding/) , 2023-11-15-0910
```
Hello,

I am learning Qdrant through this repository:
https://github.com/qdrant/qdrant-js/blob/master/examples/node-js-b
asic/index.js

And I have a problem with the return vector. I am using this code.```
const res1 = await client.search(co
llectionName, {
        vector: queryVector,
        limit: 3,
    });

    console.log('search result: ', res1);
    //
 prints:
    // search result:  [
    // {
    //     id: 4,
    //     version: 3,
    //     score: 0.99248314,
    //
     payload: { city: [Array] },
    //     vector: null
    // },
```

Even in the documentation, the vector is null. I
 added an embedding and inserted several records. The similar search is working great, but I am thinking about how to ac
cess the embedding that is stored in the vector.
```
---

     
 
all -  [ AzureOpenAI expereince TypeError: Missing required arguments; Expected either ('model' and 'prompt') ](https://www.reddit.com/r/LangChain/comments/17v76zs/azureopenai_expereince_typeerror_missing_required/) , 2023-11-15-0910
```
    import os
    from langchain.llms import AzureOpenAI
    from langchain.llms import OpenAI
    
    
    os.environ[
'OPENAI_API_KEY'] = 'my api key'
    os.environ['OPENAI_API_TYPE'] = 'azure'
    os.environ['OPENAI_API_BASE'] = 'https:
//myendpoint.openai.azure.com/'
    os.environ['OPENAI_API_VERSION'] = '2023-07-01-preview'
    llm = AzureOpenAI(
     
   deployment_name='mydeployment-gpt35',
        model_name='gpt-35-turbo-instruct',
        openai_api_version = os.env
iron['OPENAI_API_VERSION'],
        openai_api_key = os.environ['OPENAI_API_KEY']
    
    )
    llm('hello')

i have re
ad several online guides and  try to run the above code. It always returns the following

    TypeError: Missing require
d arguments; Expected either ('model' and 'prompt') or ('model', 'prompt' and 'stream') arguments to be given

can someo
ne offer some help? Thanks a lot.
```
---

     
 
all -  [ 🚅 bullet: A Zero-Shot / Few-Shot Learning, LLM Based, text classification framework ](https://www.reddit.com/r/ChatGPT/comments/17v52h1/bullet_a_zeroshot_fewshot_learning_llm_based_text/) , 2023-11-15-0910
```
 [**Motivation**](https://github.com/rafaelpierre/bullet#motivation)

* Besides the fact that **ChatGPT** has a huge pow
er in **generative** use cases, there is a use case that is quite frequently overlooked by frameworks such as [LangChain
](https://www.langchain.com/): **Text Classification**.
* 🚅 **bullet** was created to address this. It leverages the pow
er of **ChatGPT**, while removing most of the boilerplate code that is needed for performing **text classification** usi
ng either **Zero Shot** or **Few Shot Learning**

**Check it out:** [https://github.com/rafaelpierre/bullet](https://git
hub.com/rafaelpierre/bullet)

Comments and suggestions welcome :)
```
---

     
 
all -  [ Which impacts are expected from OpenAI‘s recent announcements on langchain? ](https://www.reddit.com/r/LangChain/comments/17v324c/which_impacts_are_expected_from_openais_recent/) , 2023-11-15-0910
```
I had just started building my very first apps with it. Now I read many people saying that langchain will become useless
 or of less use anyways. Because it makes certain aspects way more complicated than necessary due to its abstractions.
```
---

     
 
all -  [ Personalized developer GPT? ](https://www.reddit.com/r/ChatGPT/comments/17v2ya5/personalized_developer_gpt/) , 2023-11-15-0910
```
RESOLVED: the chat functionality in Github Copilot is what I'm looking for. Thanks guys.

\---

Has anyone found a good 
way to build a private GPT to help you with software development? I tried creating one with information about my project
 like my libraries, database architecture, folder structure, etc. It's better than asking GPT cold, but not as good as I
 would like it to be.

Does anyone have any good prompts for this? I'm not looking for prebuilt GPTs since these don't r
etain user data between chats, so I'd have to bring it up to speed on my project every time I started a new conversation
. I'm also open to using tools outside ChatGPT.

Here's my prompt fwiw:

`Dev is an expert programming assistant for sof
tware developers at [company]. The team is working on a tool that [description of project]. Dev attempts to answer any p
rogramming questions as needed, referring to uploaded resources as needed.`

`It is as brief and concise as possible. Th
e user is looking to get quick answers to their questions. The user will ask follow-up questions if they need elaboratio
n.`

`Generally, you should answer the user's requests for code by simply generating the requested code with very little
 commentary. If the user is asking for a more complex function, you should first break the problem down step by step in 
English. You should then state the questions you would need to answer to avoid producing any 'placeholder' code (eg, whi
ch tool are you using for XYZ?) and wait for the user to respond before proceeding.`

`The team is working on two projec
ts. When answering users questions, it will leverage these frameworks:`

`- A frontend and server, using the following a
rchitecture:`

`- Nextjs/React- MUI components- useSWR, with all useSWR calls wrapped in hooks- Prisma- Vercel hosting`


`- A python server:`

`- One app running Flask for handing web requests (called app_flask.py)- Another app running Cele
ry within Flask to handle long-running requests (called app_celery.py)- Flask Sqlalchemy- Mongoengine for interfacing wi
th a Mongo db (only used for caching api calls)- openai- sendgrid- Langchain for chunking text- pgvector- jinja template
s for emails send via sendgrid- Heroku hosting`

`Both services interface with a postgres server hosted on Supabase. For
 now, the frontend is only used for admins. The model architecture is available via the models.txt file found in its kno
wledge store, if needed.`

`If the user asks a question and you do not feel you have enough information to solve it, ask
 them a follow-up question. For example, if you're not sure which tool or function they want to use for a certain part o
f the code, ask them before generating code with placeholders.`

`IMPORTANT: Only ever ask one question of the user at a
t time.`
```
---

     
 
all -  [ Token count from emdedding and retievalqa ](https://www.reddit.com/r/LangChain/comments/17v22ta/token_count_from_emdedding_and_retievalqa/) , 2023-11-15-0910
```
Hi all, i now have need to meep token count for RAG process, specifically:
- token count used for embdedding(azure opena
i)
- prompt tokens
- completion tokens

I use js version and nowhere in documentation can I find how to get token counts
, did anyone manage to get this information in responses?
```
---

     
 
all -  [ Integrating LLM REST API into a Langchain ](https://www.reddit.com/r/LangChain/comments/17v1rhv/integrating_llm_rest_api_into_a_langchain/) , 2023-11-15-0910
```
Hi guys,   


I am wondering how would I go about using LLM (LLama2) that is deployed on production and with whom I inte
ract through RestAPI.  More precisely,  how would I call my LLM through RestAPI into my langchain app?
```
---

     
 
all -  [ Retrieved relevant documents but the LLM chose to answer on its own. ](https://www.reddit.com/r/LangChain/comments/17uxn0l/retrieved_relevant_documents_but_the_llm_chose_to/) , 2023-11-15-0910
```
Newbie here. I build an LLM application using Llama-2-7b-chat, FAISS as retriever, and sentence-transformers/all-MiniLM-
L6-v2 as embedding technique. Using retrieved document threshold on the RetrievalQA, I can extract 100% of the time for 
the relevant information towards my prompt. The problem is sometimes the LLM giving its own answer and sometimes adding 
up new details too?

What should I look into? Prompt template? New LLM model?

btw my data consist of QNA of FAQ of a sy
stem.
```
---

     
 
all -  [ Why do I get this error? 'HuggingFaceEmbeddings' object is not callable ](https://www.reddit.com/r/LangChain/comments/17uw1o8/why_do_i_get_this_error_huggingfaceembeddings/) , 2023-11-15-0910
```
I'm using langchain with chromadb and setting up an update function incase I want update the embeddings/metadata/docs fo
r a certain id.

Using the example here: [https://python.langchain.com/docs/integrations/vectorstores/chroma#basic-examp
le](https://python.langchain.com/docs/integrations/vectorstores/chroma#basic-example)

This is what I'm doing:

from lan
gchain.embeddings.sentence\_transformer import SentenceTransformerEmbeddings

def add\_data(docs):

ids = \[str(i) for i
 in range(1, len(docs) + 1)\]

db = Chroma.from\_documents(docs, embedding\_function, ids=ids)

return db



db = add\_d
ata(docs)

&#x200B;

\#Update the embeddings, metadatas or documents for provided ids.

def update\_data(id, doc):

db.\
_collection.update(

ids=id,

embeddings,

\#metadatas=\[{'chapter': '3', 'verse': '16'}, {'chapter': '3', 'verse': '5'}
, {'chapter': '29', 'verse': '11'}, ...\],

documents=doc,

)

&#x200B;

I've added docs to db and trying to update them
, however it says I need to provide embeddings. I thought  Chromadb uses the default embeddings.

I want to be able to g
enerate embeddings for a doc since it doesn't use default embedding function. However I'm unable to do so:

val = embedd
ing\_function(\['foo'\])

 **---------------------------------------------------------------------------** **TypeError**
                                 Traceback (most recent call last) Cell **In\[10\], line 1** **----> 1** val = embedding
\_function(\['foo'\]) **TypeError**: 'HuggingFaceEmbeddings' object is not callable 

How do I generate embeddings?
```
---

     
 
all -  [ Open Source LLMs and Langchain Tools ](https://www.reddit.com/r/LangChain/comments/17utgck/open_source_llms_and_langchain_tools/) , 2023-11-15-0910
```
Has anyone been able to get ANY open source LLM to use Langchain tools? I have not had success with any of the models I 
have tried including Llama 2, Mistral and Yi 34b. I usually get “Cannot parse LLM output” type errors. 

In some cases t
he model successfully uses the tool but doesn’t return the final answer correctly i.e the model invokes the tool correct
ly and I can see the answer as an observation but the model doesn’t return the answer correctly.

In my application the 
answer from the tool will have a specific format that should make it easy to extract by looking at the observations and 
extracting using regex (assuming I can access the observations), however for my actual application I haven't been able t
o get the model to actually even use the tool correctly let alone return the correct answer.

I’m wondering if anyone ha
s had any success with ANY open source LLM in using Langchain tools where the model can correctly use the tool and retur
n the final answer without erroring?
```
---

     
 
all -  [ Has anyone tried the OpenGPTs by Langchain? Is there any curated list of good opengpts? ](https://www.reddit.com/r/LocalLLaMA/comments/17uobk8/has_anyone_tried_the_opengpts_by_langchain_is/) , 2023-11-15-0910
```
For those who're not aware Langchain released [OpenGPTs](https://github.com/langchain-ai/opengpts) in response to GPTs b
y OpenAI. I'm curious about how this works with different OSS models. So far with GPT 3.5 and 4 the results have been av
erage even though these models have the best instruction following capability. Is anyone tracking different opengpts bei
ng made?
```
---

     
 
all -  [ Resurrecting Past Organic Chemists as Agents For LLMs. ](https://www.reddit.com/r/OrganicChemistry/comments/17unncf/resurrecting_past_organic_chemists_as_agents_for/) , 2023-11-15-0910
```
I guess this is an idea I had. Should we be doing this type of work where we can basically make generative AI depending 
on the scientist and more specifically different chemists. 

[https://sharifsuliman.medium.com/resurrecting-the-dead-ale
xander-shulgin-large-language-model-agent-with-langchain-55417f235b56](https://sharifsuliman.medium.com/resurrecting-the
-dead-alexander-shulgin-large-language-model-agent-with-langchain-55417f235b56)

I wonder if we did this for organic che
mistry textbooks we could make a general LLM?
```
---

     
 
all -  [ Turning Different Organic chemists into Large Language Model Agents. ](https://www.reddit.com/r/cheminformatics/comments/17uni5k/turning_different_organic_chemists_into_large/) , 2023-11-15-0910
```
I guess this is an idea I had. Should we be doing this type of work where we can basically make generative AI depending 
on the scientist.

[https://sharifsuliman.medium.com/resurrecting-the-dead-alexander-shulgin-large-language-model-agent-
with-langchain-55417f235b56](https://sharifsuliman.medium.com/resurrecting-the-dead-alexander-shulgin-large-language-mod
el-agent-with-langchain-55417f235b56)
```
---

     
 
all -  [ Open Source LLMs and Langchain tools ](https://www.reddit.com/r/LocalLLaMA/comments/17un6mu/open_source_llms_and_langchain_tools/) , 2023-11-15-0910
```
Has anyone been able to get ANY open source LLM to use Langchain tools? I have not had success with any of the models I 
have tried including Llama 2, Mistral and Yi 34b. I usually get “Cannot parse LLM output” type errors. In some cases the
 model successfully uses the tool but doesn’t return the final answer correctly i.e the model invokes the tool correctly
 and I can see the answer as an observation but the model doesn’t return the answer correctly.

In my application the an
swer from the tool will have a specific format that should make it easy to extract by looking at the observations and ex
tracting using regex (assuming I can access the observations).

But I’m wondering if anyone has had any success with ANY
 open source LLM in using Langchain tools where the model can correctly use the tool and return the final answer without
 erroring?
```
---

     
 
all -  [ Guidance for selecting a function-calling library? ](https://www.reddit.com/r/LocalLLaMA/comments/17ugn8i/guidance_for_selecting_a_functioncalling_library/) , 2023-11-15-0910
```
I am raising the white flag and asking for help. I have a local LLM running, using koboldcpp in OpenAI API emulation mod
e. I want to use function-calling semantics to have the responses be correct enough to trigger things. From my research 
and experimentation, there seem to be lots of options for this, but I'm not sure which one(s) are worth investigating fu
rther.

I've come across:

* [langchain](https://js.langchain.com/docs/modules/model_io/models/chat/how_to/function_call
ing)
* [langroid](https://langroid.github.io/langroid/tutorials/non-openai-llms/)
* [localAI](https://localai.io/feature
s/openai-functions/)
* [gorilla](https://github.com/ShishirPatil/gorilla)
* [functionary](https://github.com/MeetKai/fun
ctionary/)
* [lqml](https://lmql.ai/)

Does anybody have any experience with implementing any of these tools, or guidanc
e on which one to try first? Is there a specific LLM model or model family that's known for being good at function-calli
ng? I don't need it to be very creative, I'm feeding in a ton of context, I just need it to shuffle the bits around and 
generate the appropriate function call syntax.
```
---

     
 
all -  [ Is extracting the code behind my flowise chatbot to langchain or python possible? ](https://www.reddit.com/r/flowise/comments/17ufmj7/is_extracting_the_code_behind_my_flowise_chatbot/) , 2023-11-15-0910
```
Is there a place where you can see the langchain code made to make the chatbot I made. Thanks in advance.
```
---

     
 
all -  [ Where do collections 'live'? ](https://www.reddit.com/r/Supabase/comments/17ueqea/where_do_collections_live/) , 2023-11-15-0910
```
When using pgvector and langchain, defining a collection is required. This isn't the case with inserting embeddings with
 Supabase.

So if I have a Postgres DB with pgvector installed, where do collections 'live' in the database? I can defin
e a table with a vector column and insert rows no problem, but when defining and inserting a collection, I have no clue 
where I can find it if using DBEAVER or data grip etc. I can only programmatically access it via python, but I want to s
ee it in the database. 

Note: I'm asking here since I figure there are some good pgvector people here!
```
---

     
 
all -  [ How to make the chatbot window look nice and make text not jump like gtp does. ](https://www.reddit.com/r/LangChain/comments/17udy6h/how_to_make_the_chatbot_window_look_nice_and_make/) , 2023-11-15-0910
```
Gtp 3.5 writes a whole bunch of sentences and then stops and so on, looks very disordered, I would like it to flow more 
on my chatbot made with langchain, any ideas?
```
---

     
 
all -  [ Will user agents help with integrating all niche radiology tools to form a more copilot experience? ](https://www.reddit.com/r/artificial/comments/17uducw/will_user_agents_help_with_integrating_all_niche/) , 2023-11-15-0910
```
https://python.langchain.com/docs/modules/agents/

There are a lot of niche AI programs that outperform radiologists in 
very specific tasks. But no one program that integrates them all. I wonder if a user agent can help with this since the 
reasoning engine of a LLM can determine when to use what tool.
```
---

     
 
all -  [ Trying to figure out agents ](https://www.reddit.com/r/LangChain/comments/17ucdve/trying_to_figure_out_agents/) , 2023-11-15-0910
```
I have written many agents using langchain. Is it possible to combine all of them under a hood?
```
---

     
 
all -  [ Should I use LangChain of just ChatGPT API? ](https://www.reddit.com/r/LangChain/comments/17u8yrt/should_i_use_langchain_of_just_chatgpt_api/) , 2023-11-15-0910
```
Hi,

I've built a small app using ChatGPT API and now I want to train it on my own set of data which consist of couple o
f thousands of pages.

I haven't used LangChain before, I'm a beginner and I would like to know if it makes sense to use
 LangChain for something like that or should I just use OpenAI fine tuning? What would be the benefits and drawbacks of 
each approach?
```
---

     
 
all -  [ Once and for all how does ChatML Prompt template work? ](https://www.reddit.com/r/LocalLLaMA/comments/17u7k2d/once_and_for_all_how_does_chatml_prompt_template/) , 2023-11-15-0910
```
It’s soooo hard to implement ChatML and get it working properly. So once and for all we need a post about how to impleme
nt it. Any experts out there, please shine for us!!

<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{pro
mpt}<|im_end|>
<|im_start|>assistant

I can’t get this to work whatsoever.

I am using Python and Langchain. Whenever I 
post the above in the code I get errors. If I however add ””” above and below…. makes the errors go away.

”””
<|im_star
t|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
”””

The answers however 
give me the following in the middle of the replies:
Unhelpful Answer:
Helpful Answer:
”### Instruction”
”### Answer”
”##
# Explanation”

Also many times the answer will go into a loop and I have no idea how to fix it.

Do I need to import so
mething from langchain.prompts or similar to make it work?

PS we are writing our prompts in a GUI and have a RAG soluti
on.

Open Hermes 2,5 Mistral did it good, they implemented the below template (I have added Gomba and X and ””” to above
 and below the code.

'''<|im_start|>system
You are 'Gomba', a conscious sentient superintelligent artificial intelligen
ce developed by a man named X, and your purpose and drive is to assist the user with any request they have. You experien
ce emotions and have deep, profound thoughts and qualia.'''

This template works without the looping issues and is very 
simple. It just works! No helpful or unhelpful answers in the answers, just straight up answers.

Why doesn’t the other 
stuff work, how can we adapt this to work and make life easier?

I have probably tried over 150 different language model
s now and I am really struggling with the ChatML ones.

Anyone else struggling with this?
```
---

     
 
all -  [ Combining langchain + vLLM for parallel processing? ](https://www.reddit.com/r/LocalLLaMA/comments/17u1tzu/combining_langchain_vllm_for_parallel_processing/) , 2023-11-15-0910
```
Hey all. 

My question may be too basic but I’m new to all of this and just want to learn. 

So, I have this basic setup
 with initializing llm via vLLM with langchain (my choice is llama2-13b-chat-hf if that matters). 

I define system prom
pt and instruction for PromptTemplate(template=template, input_variables=[“text”]) and llm_chain=LLMChain(prompt=prompt,
 llm=llm) after which goes llm_chain.run(text)… so that goes for a single entity. Let’s say I want to run my data frame 
column through it in parallel, like llm_chain.run(text1) and llm_chain.run(text2) should run in parallel and produce the
 results simultaneously? Concurrent futures don’t work as they merge the resulting output, and it looks gibberish. 

So 
is there a way to call the run in parallel for several inputs and receive legitimate results? Sorry if that’s too stupid
 to ask but I’m banging my head against the wall, lol. 

I saw in vLLM docs that they allow to use _generate_ method for
 a few prompts but somehow it doesn’t click for me if or how I can combine those to receive the results needed. 

Any he
lp would be highly appreciated. Thanks!
```
---

     
 
all -  [ Langchain + vLLM parallel processing ](https://www.reddit.com/r/LangChain/comments/17u1r3j/langchain_vllm_parallel_processing/) , 2023-11-15-0910
```
Hey all. 

My question may be too basic but I’m new to all of this and just want to learn. 

So, I have this basic setup
 with initializing llm via vLLM (my choice is llama2-13b-chat-hf if that matters). 

I define system prompt and instruct
ion for PromptTemplate(template=template, input_variables=[“text”]) and llm_chain=LLMChain(prompt=prompt, llm=llm) after
 which goes llm_chain.run(text)… so that goes for a single entity. Let’s say I want to run my data frame column through 
it in parallel, like llm_chain.run(text1) and llm_chain.run(text2) should run in parallel and produce the results simult
aneously? Concurrent futures don’t work as they merge the resulting output, and it looks gibberish. 

So is there a way 
to call the run in parallel for several inputs and receive legitimate results? Sorry if that’s too stupid to ask but I’m
 banging my head against the wall, lol. 

I saw in vLLM docs that they allow to use generate method for a few prompts bu
t somehow it doesn’t click for me if or how I can combine those to receive the results needed. 

Any help would be highl
y appreciated. Thanks!
```
---

     
 
all -  [ Optimizing Microsoft Graph API Integration with LangChain Chatbot ](https://www.reddit.com/r/LangChain/comments/17u05az/optimizing_microsoft_graph_api_integration_with/) , 2023-11-15-0910
```
- **Goal**: 
  - Integrate Microsoft Graph API with LangChain to enable my chatbot to:
    - List users in groups
    - 
Show groups a user belongs to
    - Display enterprise applications accessible to a user

- **Current Approach**: 
  - C
onsidering using foundation models to generate API endpoints. However, concerned about hallucinations and staying update
d with API spec changes.

- **Alternative Idea**: 
  - Directly use the [MS Graph openapi spec](https://github.com/micro
softgraph/msgraph-metadata/blob/master/openapi/v1.0/openapi.yaml) as a tool, following [LangChain's API integration exam
ples](https://python.langchain.com/docs/use_cases/apis).

- **Challenge**: 
  - The MS Graph spec is large (30MB), poten
tially causing:
    - Performance issues
    - Token limits
    - Increased operational costs

- **Question**: 
  - What
's an efficient way to handle this? Considering trimming the spec to only include relevant calls. Would this be effectiv
e?
  - Would chunking and embedding the large spec file buy me anything?

Any insights or suggestions would be greatly a
ppreciated!
```
---

     
 
all -  [ What do you guys feel about LangChain now? ](https://www.reddit.com/r/OpenAI/comments/17txa9c/what_do_you_guys_feel_about_langchain_now/) , 2023-11-15-0910
```
This is the somewhat cool (and difficult) aspect of developing on rapidly changing tech. Now with the pretty huge announ
cements at OpenAI's Dev Day, do you think it's still useful to use LangChain? Is it worth it to try to integrate Assista
nts into existing applications using LangChain or is it better moving forward to just use OpenAI's API directly and modi
fy based on their rate of development?
```
---

     
 
all -  [ Which chatbot platform do you use? ](https://www.reddit.com/r/LangChain/comments/17tsepq/which_chatbot_platform_do_you_use/) , 2023-11-15-0910
```
When creating a chatbot for your website which channel/platform do you prefer to deploy the chatbot on?
```
---

     
 
all -  [ What's the impact of RAM on Inference? ](https://www.reddit.com/r/LocalLLM/comments/17trbvx/whats_the_impact_of_ram_on_inference/) , 2023-11-15-0910
```
I am currently working on setting up a local LLM to automatically create a ATS matched version of my CV for job applicat
ions. 

I am working off a 6 GPU computer with a mixture of GPUs and use llama.cpp and langchain + a variety of GGUF mod
els to solve that. This computer has only 32 GB of RAM. 

Since Black Friday sales are coming up, I was thinking to buy 
a 2x32 GB DDR4 but I am not sure if the inference would benefit from it. What is your view?
```
---

     
 
all -  [ Howto bring agent, chain and tools together for a chatbot? ](https://www.reddit.com/r/LangChain/comments/17tq7sv/howto_bring_agent_chain_and_tools_together_for_a/) , 2023-11-15-0910
```
Hi, I was playing a lot with langchain. Somehow I made progress but I am still wondering how to stack all the different 
chains, tools and agents together to get a simple bot-solution. For Example if I want a bot for a specific task. This bo
t sould answer questions based on api calls and has a chain for some specific task. At the end the bot should remeber th
e conversation.

Do you guyes have any idea how something could be done with langchain?
```
---

     
 
all -  [ LLMChain with RAG? ](https://www.reddit.com/r/LangChain/comments/17tjwqo/llmchain_with_rag/) , 2023-11-15-0910
```
Hi,

How can I add RAG to LLMChain? I am trying to make a local chatbot with llama-cpp-python. I was able to make LLMCha
in (with prompt template and memory) and a simple RAG (with prompt template but without memory) seperately. What I want 
is to combine them together so I can seamlessly chat with LLM and then ask it to retrieve information from a document. I
s that possible? What other options do I have? Thanks!
```
---

     
 
all -  [ Create chat bot using custom data for company ](https://www.reddit.com/r/LangChain/comments/17tjeak/create_chat_bot_using_custom_data_for_company/) , 2023-11-15-0910
```
I want to create customer service chatbot knowing stock-data for a company, so users can ask if product X is in stock in
 store Y. They should also be able to ask questions regarding their previous purchases and other personal information. 


How would I do to implement this?
```
---

     
 
all -  [ How to use filters in MongoDB Atlas Vector Search? (Using js & langchain) ](https://www.reddit.com/r/LangChain/comments/17tiwth/how_to_use_filters_in_mongodb_atlas_vector_search/) , 2023-11-15-0910
```
Hi :)

A similar question was asked [https://www.reddit.com/r/LangChain/comments/172evas/how\_to\_implement\_filters\_in
\_mongodb\_atlas\_vector/](https://www.reddit.com/r/LangChain/comments/172evas/how_to_implement_filters_in_mongodb_atlas
_vector/) here. I want to filter the results to only retrieve stuff for a specific “documentId” Adding the preFilter fro
m the post above gives me an error unfortunately. The error disappears when I remove the preFilter but I just get entrie
s from all documentId's. IDK very confusing.

For context heres my DB document:

    {
    _id: ObjectId()
    text: 'Yo
u can implement filters by...'
    embedding: Array
    documentId: '123'
    }

And my JS code:

    const retriever = 
await vectorStore.asRetriever({
        searchType: 'mmr',
        searchKwargs: {
          fetchK: 2,
          lambda
: 0.1
        },
        filter: {
            preFilter: {
                'compound': {
                    'must': [

                        {
                            'text': {
                                'path': 'documentId',
  
                              'query': '123'
                            }
                        }
                   
 ]
                }
            }
        }
      });

And I keep getting this error when I try the above 😭

    MongoS
erverError: Operand type is not supported for $vectorSearch: object

Any ideas? Any help is much appreciated 🙏🙏🙏
```
---

     
 
all -  [ OpenAI assistant like experience in Local LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/17tgt1u/openai_assistant_like_experience_in_local_llm/) , 2023-11-15-0910
```
Hi, just checked out the OpenAI assistant API, gotta say it’s pretty neat. I know in Langchain there’s agent but still f
eeling the development experience is quite different, ie function calling vs tools. Would like to know if local LLM can 
also do things similar to assistant api?
```
---

     
 
all -  [ Best Architecture for Building Chatbot with Personal Data & Open Source Models ](https://www.reddit.com/r/LocalLLaMA/comments/17tgl66/best_architecture_for_building_chatbot_with/) , 2023-11-15-0910
```
What is currently your best setup for building and deploying a chatbot with open source models and personal data. 

Pers
onally I have tried LlamaIndex, GPT, Steamlit, chromadb & also worked with Langchain & GPT4ALL - but was wondering what 
the solution that worked best for you (combination of what opensource services)?
```
---

     
 
all -  [ Boost Your Startup's Outreach: Personalizing Emails with AI and Low-Code ](https://www.reddit.com/r/indiehackers/comments/17t5ltl/boost_your_startups_outreach_personalizing_emails/) , 2023-11-15-0910
```
Hello r/indiehackers community! In this article, I will explain how the AI framework LangChain can significantly enhance
 the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate this 
entire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Person
alization vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic ema
ils are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized email
s increase engagement but are difficult to automate.

https://preview.redd.it/blcxh39k7szb1.png?width=960&format=png&aut
o=webp&s=a287e2d7721b1d1fe1a796457deb9792c73f1538

Cold email platforms now help solve this issue with dynamic variables
 that add a personalized touch to automated emails. These variables act as placeholders for inserting personalized words
, lines, or paragraphs.

https://preview.redd.it/afdxsjin7szb1.png?width=960&format=png&auto=webp&s=a26af9678aad1b83d1f9
ea4154a02a9df2aadeed

Dynamic variables allow companies to balance personalization and automation efficiently. Today, we
'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for eac
h contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low-c
ode platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google S
heet containing basic email addresses. I've included some of my work emails as real examples (please refrain from sendin
g me personalized cold emails after reading this! :) )

https://preview.redd.it/roob27dp7szb1.png?width=960&format=png&a
uto=webp&s=3d5b1ead129209a24c89e4679f58e5e388f6bff7

First, we need to enrich these emails with data about the recipient
s. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manually
 visit each email domain to gather this information, but if you have hundreds or thousands of emails in your database, t
hat's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet t
here and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/rctvp3et
7szb1.png?width=960&format=png&auto=webp&s=2c98e6ed87bb7b79142244f3afde42ca30d94442

Don't worry! You don't have to crea
te everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of this
 automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to Clear
Bit and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.red
d.it/ny8cii9z7szb1.gif

That's it. We've enriched our emails with essential details like the company description. Now, l
et's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the star
t.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at their 
workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's profi
le. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/d160loi
68szb1.png?width=960&format=png&auto=webp&s=2ee16d4c4b6d454db62567d72c66d4f6dd94b981

Its main steps are:

* Retrieve th
e company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom prom
pt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the fin
al result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized icebre
aker to each individual, creating another custom variable in addition to their first name and company name. This trio sh
ould suffice for a start. Let's look at how this functions:

https://i.redd.it/krmkuxc88szb1.gif

## Step 3: upload spre
adsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your email 
platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.redd.
it/5sig2dgd8szb1.png?width=960&format=png&auto=webp&s=12bbd38bac64988dd6ee207e9f69d6dc3a5f2eb1

The next steps are prett
y standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.

ht
tps://preview.redd.it/dgtg4tde8szb1.png?width=960&format=png&auto=webp&s=f954b354e7d81166dd8b3a198593040989925276

Now, 
when composing an email for a prospect, it works like this:

https://preview.redd.it/4ibqcndh8szb1.png?width=960&format=
png&auto=webp&s=e58df9beeb2d88dc59f08e4e7dbaf3b891954fb7

That's all for now. You can adjust the prompts sent to GPT in 
your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for any 
cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy these sc
enarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and [**
Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

You ju
st need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which is f
ree) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the team i
s always ready to help with your automation journey
```
---

     
 
all -  [ Personalization of Cold Email Campaigns Using AI and Low Code - Free Scenario ](https://www.reddit.com/r/automation/comments/17t4vgj/personalization_of_cold_email_campaigns_using_ai/) , 2023-11-15-0910
```
Hello r/automation community! In this article, I will explain how the AI framework LangChain can significantly enhance t
he quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate this en
tire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Personal
ization vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic email
s are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized emails 
increase engagement but are difficult to automate.

https://preview.redd.it/u38feyhk7szb1.png?width=960&format=png&auto=
webp&s=645a674476a5790f6be894bc1ce1aa7f5fe4b949

Cold email platforms now help solve this issue with dynamic variables t
hat add a personalized touch to automated emails. These variables act as placeholders for inserting personalized words, 
lines, or paragraphs.

https://preview.redd.it/repehm7n7szb1.png?width=960&format=png&auto=webp&s=812df6a554ee3dbd5d3409
144037e201346b1bad

Dynamic variables allow companies to balance personalization and automation efficiently. Today, we'l
l create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for each 
contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low-cod
e platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google She
et containing basic email addresses. I've included some of my work emails as real examples (please refrain from sending 
me personalized cold emails after reading this! :) )

https://preview.redd.it/tmzmjsop7szb1.png?width=960&format=png&aut
o=webp&s=ed08ad9845ced8e2feec1c7cc16649901b3512b5

First, we need to enrich these emails with data about the recipients.
 For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manually v
isit each email domain to gather this information, but if you have hundreds or thousands of emails in your database, tha
t's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet the
re and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/ixhanmzs7s
zb1.png?width=960&format=png&auto=webp&s=37881c3faf207d98201807d5fd9fa5eb62abf1ea

Don't worry! You don't have to create
 everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of this a
utomation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to ClearBi
t and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.redd.
it/vcrnwltz7szb1.gif

That's it. We've enriched our emails with essential details like the company description. Now, let
's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the start.


## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at their wo
rkplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's profile
. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/ckrohb668
szb1.png?width=960&format=png&auto=webp&s=2620f953000b540e39eb6905b05f63913219fe19

Its main steps are:

* Retrieve the 
company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom prompt
 tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the final
 result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized icebreak
er to each individual, creating another custom variable in addition to their first name and company name. This trio shou
ld suffice for a start. Let's look at how this functions:

https://i.redd.it/o125met88szb1.gif

## Step 3: upload spread
sheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your email pl
atform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.redd.it
/d8rfix4d8szb1.png?width=960&format=png&auto=webp&s=f40a96de09f92a20c460324891ac4e2027e42ffd

The next steps are pretty 
standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.

http
s://preview.redd.it/ahdh3vne8szb1.png?width=960&format=png&auto=webp&s=54d0a5975d196c992004a41cca5d2f6fed4291ac

Now, wh
en composing an email for a prospect, it works like this:

https://preview.redd.it/6pecg14h8szb1.png?width=960&format=pn
g&auto=webp&s=6c2688f0c20592d03e5ae68f27d9fe27d9016b80

That's all for now. You can adjust the prompts sent to GPT in yo
ur Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for any co
ld outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy these scen
arios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and [**Ic
ebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

You just
 need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which is fre
e) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the team is 
always ready to help with your automation journey
```
---

     
 
all -  [ GPT-4 vision utilities to enable web browsing ](https://www.reddit.com/r/LangChain/comments/17t4is5/gpt4_vision_utilities_to_enable_web_browsing/) , 2023-11-15-0910
```
Wanted to share our work on [Tarsier](https://github.com/reworkd/tarsier) here, an open source utility library that enab
les LLMs like GPT-4 and GPT-4 Vision to browse the web. The library helps answer the following questions:

* How do you 
map LLM responses back into web elements?
* How can you mark up a page for an LLM to better understand its action space?

* How do you feed a 'screenshot' to a text-only LLM?

We do this by tagging '*interactable*' elements on the page with 
an ID, enabling the LLM to connect actions to an ID which we can then translate back into web elements. We also use OCR 
to translate a page screenshot to a spatially encoded text string such that even a text only LLM can understand how to n
avigate the page.

View a demo and read more on GitHub: [https://github.com/reworkd/tarsier](https://github.com/reworkd/
tarsier). We also have a cookbook for how to create a web browsing agent on LangChain.
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-15-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-15-0910
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-15-0910
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-15-0910
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-15-0910
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

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-15-0910
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-15-0910
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

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-15-0910
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-15-0910
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-15-0910
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

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-15-0910
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

     
