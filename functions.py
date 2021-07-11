import twitter
import os
import time
import requests
###############
import urllib3
import json

def aaaa():
    r = urllib3.urlopen(url='https://twitter.com/okinnansc/status/1412779977498578945/photo/1')
    content = r.read()
    # extract download link
    download_url = json.loads(content)['link']
    download_content = urllib3.urlopen(download_url).read()
    # save downloaded content to file
    f = open('test.mp3', 'wb')
    f.write(download_content)
    f.close()

###############
def auth(api_key, api_secret_key, access_token, access_secret):
    api = twitter.Api(consumer_key=api_key, consumer_secret=api_secret_key, access_token_key=access_token, access_token_secret=access_secret)
    return api

def downloader(tweet, name):
    if tweet.media != None:
        twmedia = tweet.media[0]
        link = twmedia.expanded_url
        print(link)
        #download_archive(url=link, endereco=f"./content/{name}")

def download_archive(url, endereco):
    resposta = requests.get(url, stream=True) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

def getInfo(api, userID):
    timeline = api.GetUserTimeline(user_id=userID, count=100) 
    for tweet in timeline:
        name = (tweet.id_str)
        archive = open(f"./content/{name}.txt", "w")
        archive.write(tweet.text)
        downloader(tweet=tweet, name=name)
