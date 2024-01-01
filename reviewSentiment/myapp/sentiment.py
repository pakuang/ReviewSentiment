from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re


tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

#collect reviews from yelp

#make request to site
def get_reviews(yelp_url):
    r= requests.get(yelp_url)
    #extract comments from yelp site
    if(r.status_code!=200):
        return None
    soup = BeautifulSoup(r.text,'html.parser')
    regex= re.compile('.*comment.*')
    results = soup.find_all('p', {'class':regex})
    reviews = [result.text for result in results]
    
    i=10
    while(len(results)!=0):
        r = requests.get(yelp_url+'&start='+str(i))
        soup = BeautifulSoup(r.text,'html.parser')
        regex= re.compile('.*comment.*')
        results = soup.find_all('p', {'class':regex})
        if len(results) == 0:
            break
        if(len(results))>0:
            reviews +=[result.text for result in results]
        i+=10
    return reviews

def get_sentiment(review):
    tokens = tokenizer.encode(review[:512], return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


def get_avg_sentiment(reviews):
    total=0
    for review in reviews:
        total+=get_sentiment(review)
    return total/len(reviews)

