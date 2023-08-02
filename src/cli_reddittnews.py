"""

Fetch secret from here:
https://www.reddit.com/prefs/apps/


pip install praw fire utilmy


export reddit_client='i05gtu1-NrbJqCxHFHxW3g'
export reddit_client_secret='Ak1qkvZdqnAfCCSK7rq9HcyBuaWoTQ'
export reddit_ua='Bot'
export reddit_subreddit='MachineLearning,OpenAI,ChatGPT,OpenAIDev,learnmachinelearning'


cd utilmy/webscrapper/

python cli_redditnews.py run --query 'icml 2023, neurips 2023'  --dirout ztnp/reddit/



"""
import fire, os, praw, pandas as pd, csv
from utilmy import (date_now, pd_to_file, os_makedirs, log)


def run(query:str='icml 2023 ', dirout:str="ztmp/", subreddits=None, reddit_limit=10, reddit_sort='top', verbose=1):

    ### from https://www.reddit.com/prefs/apps/
    client_id     = "KqVbVrlmGdbowtjuNIMAmQ" 
    client_secret = "XN4XRE7_pOw9rzreelTFYogmBTWW_g" 
    user_agent    = "DailyNews"  ### Same from Secret page
    reddit = praw.Reddit(client_id = client_id,#my client id
                     client_secret = client_secret,  #your client secret
                     user_agent    = user_agent #user agent name
                     )
    log(reddit.read_only)
    if verbose > 1 :
        log(client_id, client_secret, user_agent)

    if subreddits is None :
        subreddits = ['MachineLearning','DeepLearning']
        
    if isinstance(query, str):
        query = query.split(",")

    ymd = date_now(fmt='%y%m%d', returnval='str')    

    log("########## Start Scrapping")
    df = pd.DataFrame() 
    for s in subreddits:
        subreddit = reddit.subreddit(s) 
        log('fetching:', s)

        for item in query:
            ddict = {
            "title" : [], "score" : [], "id" : [], "url" : [], "comms_num": [], "dt" : [], "body" : []
            }
            
            for submi in subreddit.search(query,sort = reddit_sort,limit = reddit_limit):
                ddict["title"].append(submi.title)
                ddict["score"].append(submi.score)
                ddict["id"].append(submi.id)
                ddict["url"].append(submi.url)
                ddict["comms_num"].append(submi.num_comments)
                ddict["dt"].append(submi.created)
                ddict["body"].append(submi.selftext)

            dfres = pd.DataFrame(ddict)
            log( f'{item}: N article: ', len(dfres))
            df = pd.concat([df,dfres], axis=0,ignore_index=True)


    for ci in df.columns: 
        df[ci] = df[ci].apply(lambda x : str(x).replace('"', "'" ))


    for ci in  ['body']:
       df[ ci ] = df[ci].apply(lambda x : reformat(x) )     

    # df['dt'] = df['dt'].apply(lambda x : date_now(int(x), fmt="%Y%m%d_%H%m%"))


    cols= ['title', 'body', 'url', 'comms_num', 'dt', 'score', 'id' ] 


    pd_to_file(df[cols], dirout + f"/reddit_{ymd}.csv", 
               sep='\t', quoting=csv.QUOTE_NONNUMERIC, quotechar='"')

    try :
      os.remove(dirout + f"/reddit_{ymd}.tsv")
      os.rename(dirout + f"/reddit_{ymd}.csv", dirout + f"/reddit_{ymd}.tsv")          
    except: pass   
    return


def reformat(ss):

    sall = ""
    kbatch = 60
    n = int(len(ss) / kbatch)
    for ii in range(n+1):
        sall = sall + ss[ii*kbatch:(ii+1)*kbatch] + "\n"
    return sall[:-1]


if __name__ == "__main__":
  fire.Fire(run)

