from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
import sys
import os
import spoonacular as sp
import requests
import flask
import random


keywordList = ["pasta", "pizza", "soup", "cake", "cookies", "rice", "steak", "chicken", "ham", "kebab", "egg", "bagel"]#list of keywords to use
num = random.randint(0, 11)#random generator to choose which to search for
searchQuery = keywordList[num] + " -filter:links"#build the search query for tweepy
#Twitter--------------------------------------------------------------------------------------------------------------

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)



tweets = Cursor(auth_api.search, q=searchQuery, lang="en").items(1)#get 5 tweets with keyword in it
for tweet in tweets:
    tweety = "'{}' -@{} {}".format(tweet.text, tweet.user.screen_name, tweet.created_at)#format tweet info

#Spoonacular--------------------------------------------------------------------------------------------------------------

spoon_key = os.environ['SPOON_KEY']
api = sp.API(spoon_key)
url1 = "https://api.spoonacular.com/recipes/complexSearch?apiKey="
url2 = "&query="
url3 = "&number=1&includeIngredients"
url = url1 + str(spoon_key) + url2 + keywordList[num] + url3 #combine parts to make whole url
response = requests.get(url)
respo = response.json()#make it .json() to select parts

ID = respo['results'][0]['id']#get ID
url = "https://api.spoonacular.com/recipes/" + str(ID) + "/information?apiKey=" + str(spoon_key)#make new url to get specific info
respons = requests.get(url)
res = respons.json()

#get needed info
title = res['title']
link = res['image']
spoonacularSource = res['spoonacularSourceUrl']
servSize = res['servings']
totTime = res['readyInMinutes']
ingred = []
ingredAmount = []

#for loop to parse
for i in range(len(res['extendedIngredients'])):
    ingred.append(res['extendedIngredients'][i]['name']) #get name of ingredient
    ingredAmount.append(str(res['extendedIngredients'][i]['measures']['us']['amount']) + res['extendedIngredients'][i]['measures']['us']['unitShort']) #get amount of ingredient


#Flask--------------------------------------------------------------------------------------------------------------
app = flask.Flask(__name__)
@app.route('/') # Python Decorator
def index():
    
    return flask.render_template(
        "index.html",
        keyWord = keywordList[num],
        ftweet = tweety,
        tit=title,
        lin=link,
        sourc=spoonacularSource,
        servin=servSize,
        minutes=totTime,
        len = len(ingred),
        ingred=ingred,
        ingredAmount = ingredAmount
        
        )
        
        
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
)